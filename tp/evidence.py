"""Layer 4: running evidence.

Two kinds of executable evidence:

* check  - a function in the entity's own check.py.  It reaches premises only
           through `premise("<id>")` (lib/tp_premise.py), which records what was
           touched, so declared and actual premises can be compared.  It runs
           sandboxed (audit hook: no sockets, no writes outside a temp dir),
           twice, and under mutation: perturbing its literals must make it fail.
* legacy - a series verify_TXX.py script, run once with GA.check recorded;
           its PASS/FAIL lines are matched to claims by statement tags.
"""
from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import secrets
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(os.path.dirname(HERE), "lib")

TAG_NUM_RE = re.compile(
    r"\b(?:Thms?|Theorems?|Props?|Propositions?|Lems?|Lemmas?|Cors?|Corollar(?:y|ies)|"
    r"Defs?|Definitions?|Facts?|Rems?|Remarks?|Prems?|Premises?|Ax|Axioms?|"
    r"Conjs?|Conjectures?|Examples?|Ex)\.?\s*~?([A-Z]?\d+(?:\.\d+)+)")
TAG_LABEL_RE = re.compile(r"^\s*\[?([a-z]{2,6}:[A-Za-z0-9_\-]+)")


def label_keys(check_label: str) -> set[str]:
    keys = {"num:" + n for n in TAG_NUM_RE.findall(check_label)}
    m = TAG_LABEL_RE.match(check_label)
    if m:
        keys.add("label:" + m.group(1))
    # a check's own identifier at the start of its name ("A1.1 ...", "E1.3d ...",
    # "L CHECK_ALG/...") lets a claim name the checks of a run that carries no
    # paper labels
    cid = re.match(r"^\s*([A-Z]{1,3}\d+(?:\.\d+)*[a-z]?)(?=[\s:(]|$)", check_label)
    if cid:
        keys.add("id:" + cid.group(1))
    # "C11 (CONTROL, floating point; obs:anglefits): ..." names its label in the
    # parenthesised header before the first colon-space
    head = re.match(r"^\s*\w{1,8}\s*\(([^)]*)\)\s*:", check_label)
    if head:
        for lab in re.findall(r"\b([a-z]{2,6}:[A-Za-z0-9_\-]+)", head.group(1)):
            keys.add("label:" + lab)
    return keys


# --------------------------------------------------------------------------
# static checks on a new-style check file
# --------------------------------------------------------------------------

def static_problems(source: str) -> list[tuple[str, str]]:
    probs = []
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return [("E401", f"check does not parse: {exc}")]
    imports_ga = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            probs.append(("E402", f"float literal {node.value!r} at line {node.lineno}"))
        elif isinstance(node, ast.Call) and getattr(node.func, "id", None) == "float":
            probs.append(("E402", f"float() call at line {node.lineno}"))
        elif isinstance(node, ast.Import):
            for a in node.names:
                if a.name.split(".")[0] in ("math", "numpy", "cmath", "random"):
                    probs.append(("E402", f"import {a.name} at line {node.lineno}"))
                if a.name == "GA":
                    imports_ga = True
        elif isinstance(node, ast.ImportFrom):
            mod = (node.module or "").split(".")[0]
            if mod in ("math", "numpy", "cmath", "random"):
                probs.append(("E402", f"from {node.module} import at line {node.lineno}"))
            if mod == "GA":
                imports_ga = True
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            # int / int yields a float in Python 3
            if all(isinstance(x, ast.Constant) and isinstance(x.value, int)
                   for x in (node.left, node.right)):
                probs.append(("E402", f"integer true division at line {node.lineno}; "
                                      "use Fraction"))
    if not imports_ga:
        probs.append(("E403", "check does not import GA"))
    return probs


def lib_modules() -> set[str]:
    """The shared library modules a check may import (lib/*.py)."""
    try:
        return {f[:-3] for f in os.listdir(LIB) if f.endswith(".py")}
    except OSError:
        return set()


def lib_imports(source: str, mods: set[str] | None = None) -> set[str]:
    """The lib/ modules a source file imports by name (import gtg, from fock import x)."""
    mods = lib_modules() if mods is None else mods
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return set()
    out = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            out |= {a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.ImportFrom) and not node.level:
            out.add((node.module or "").split(".")[0])
    return out & mods


def function_names(source: str) -> set[str]:
    """Top-level function names of a check file (empty if it does not parse)."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return set()
    return {n.name for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}


def has_assertion(source: str, func: str) -> bool:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False                     # static_problems reports it (E401)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == func:
            for n in ast.walk(node):
                if isinstance(n, ast.Assert):
                    return True
                if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                        and n.func.attr == "check"):
                    return True
    return False


class _Mutator(ast.NodeTransformer):
    """Replace the k-th integer literal inside one function by n + 1."""

    def __init__(self, func, k):
        self.func, self.k, self.seen, self.inside, self.done = func, k, 0, False, False

    def visit_FunctionDef(self, node):
        if node.name != self.func:
            return node
        self.inside = True
        self.generic_visit(node)
        self.inside = False
        return node

    def visit_Constant(self, node):
        if (self.inside and isinstance(node.value, int)
                and not isinstance(node.value, bool)):
            if self.seen == self.k:
                self.done = True
                self.seen += 1
                return ast.copy_location(ast.Constant(node.value + 1), node)
            self.seen += 1
        return node


def int_literal_count(source: str, func: str) -> int:
    m = _Mutator(func, -1)
    m.visit(ast.parse(source))
    return m.seen


def mutate(source: str, func: str, k: int) -> str | None:
    m = _Mutator(func, k)
    tree = m.visit(ast.parse(source))
    return ast.unparse(tree) if m.done else None


# --------------------------------------------------------------------------
# sandboxed execution
# --------------------------------------------------------------------------

DRIVER = r'''
import json, os, sys, tempfile
TMP = os.path.realpath(tempfile.gettempdir())
WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
DENY = ("subprocess.Popen", "os.system", "os.exec", "os.posix_spawn", "os.spawn",
        "os.fork", "os.forkpty", "os.kill", "os.killpg", "os.remove", "os.rename",
        "os.rmdir", "os.symlink", "os.link", "os.truncate", "os.chmod", "os.chown",
        "os.chdir", "os.putenv", "os.unsetenv", "shutil.rmtree", "shutil.move",
        "sys._getframe", "sys._current_frames", "sys.settrace", "sys.setprofile",
        "gc.get_objects", "gc.get_referrers", "gc.get_referents", "ctypes.dlopen",
        "ctypes.cdata", "ctypes.call_function", "pty.spawn", "webbrowser.open",
        "urllib.Request", "ftplib.connect", "http.client.connect")
FRAMES = {"tb_frame", "gi_frame", "cr_frame", "ag_frame", "f_back", "f_locals",
          "f_globals", "f_builtins", "f_code"}
BANNED_MODULES = {"ctypes", "_ctypes", "_posixsubprocess", "pty", "multiprocessing"}

def _inside_tmp(p):
    p = os.path.realpath(str(p))
    return p == TMP or p.startswith(TMP + os.sep)

def _hook(event, args):
    if event.startswith("socket.") or event.startswith(DENY):
        raise PermissionError("sandbox: " + event)
    if event == "object.__getattr__" and len(args) > 1 and args[1] in FRAMES:
        raise PermissionError("sandbox: frame access")
    if event == "import" and args and str(args[0]).split(".")[0] in BANNED_MODULES:
        raise PermissionError("sandbox: import " + str(args[0]))
    if event == "open" and args:
        mode = args[1] if len(args) > 1 else None
        flags = args[2] if len(args) > 2 else 0
        writes = (isinstance(mode, str) and any(c in mode for c in "wax+")) or \
                 (isinstance(flags, int) and flags & WRITE_FLAGS)
        if writes and not _inside_tmp(args[0]):
            raise PermissionError("sandbox: write to " + str(args[0]))

def _main():
    # the nonce marks the one genuine result line; it lives only in this frame,
    # and frame access is denied to the check once the hook is installed
    nonce = sys.stdin.readline().strip()
    sys.stdin.close()
    out = sys.stdout
    sys.path[:0] = [LIB, FOLDER]
    import tp_premise
    tp_premise.configure(STORE)
    import GA
    import importlib.util
    spec = importlib.util.spec_from_file_location("check_under_test", SRC)
    mod = importlib.util.module_from_spec(spec)
    sys.addaudithook(_hook)
    res = {"ok": False, "error": None}
    try:
        spec.loader.exec_module(mod)
        before = len(GA.FAILURES)
        rv = getattr(mod, FUNC)()
        res["ok"] = (rv is not False) and len(GA.FAILURES) == before
        if len(GA.FAILURES) > before:
            res["error"] = "GA.check failed: " + "; ".join(GA.FAILURES[before:])
    except AssertionError as exc:
        res["error"] = "assertion failed: " + str(exc)
    except BaseException as exc:
        res["error"] = type(exc).__name__ + ": " + str(exc)
    res["touched"] = sorted(tp_premise.TOUCHED)
    res["quantities"] = sorted(getattr(tp_premise, "TOUCHED_QUANTITIES", ()))
    out.write("\n@@RESULT-" + nonce + "@@" + json.dumps(res) + "\n")
    out.flush()

globals().pop("_main")()
'''


def run_check(store_root: str, folder: str, source: str, func: str,
              timeout: int = 60) -> dict:
    """Run one check function in a separate interpreter under an audit hook.

    The hook stops accidents and casual misuse: no network, no process spawning,
    no writes or deletions outside a temporary folder, no frame or gc introspection,
    no ctypes.  It is not a security boundary against hostile code; CI runs this
    layer inside a container with no network and a read-only source tree.  The
    result line is marked with a per-run nonce the check cannot read, so a check
    cannot print a forged result."""
    nonce = secrets.token_hex(16)
    # the check runs with a temporary folder as its working directory
    store_root, folder = os.path.abspath(store_root), os.path.abspath(folder)
    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, "check_under_test.py")
        with open(src, "w", encoding="utf-8") as fh:
            fh.write(source)
        prelude = (f"LIB={LIB!r}\nFOLDER={folder!r}\nSTORE={store_root!r}\n"
                   f"SRC={src!r}\nFUNC={func!r}\n")
        drv = os.path.join(tmp, "driver.py")
        with open(drv, "w", encoding="utf-8") as fh:
            fh.write(prelude + DRIVER)
        env = {"PATH": os.environ.get("PATH", ""), "TMPDIR": tmp,
               "PYTHONHASHSEED": "0"}
        try:
            cp = subprocess.run([sys.executable, "-I", drv], capture_output=True,
                                text=True, timeout=timeout, env=env, cwd=tmp,
                                input=nonce + "\n")
        except subprocess.TimeoutExpired:
            return {"ok": False, "error": f"timeout after {timeout}s", "touched": [],
                    "quantities": [], "timeout": True}
        tag = "@@RESULT-" + nonce + "@@"
        hits = [l for l in cp.stdout.splitlines() if l.startswith(tag)]
        if len(hits) == 1:
            return json.loads(hits[0][len(tag):])
        return {"ok": False, "error": (cp.stderr or cp.stdout)[-600:] or "no result",
                "touched": [], "quantities": []}


# --------------------------------------------------------------------------
# legacy verify scripts
# --------------------------------------------------------------------------

LEGACY_DRIVER = r'''
import json, runpy, sys, os
sys.path[:0] = [LIB]
import GA
RESULTS = []
_orig = GA.check
def _rec(label, ok):
    RESULTS.append([label, bool(ok)])
    _orig(label, ok)
GA.check = _rec
sys.argv = [SCRIPT]
try:
    runpy.run_path(SCRIPT, run_name="__main__")
except SystemExit:
    pass
print("@@LEGACY@@" + json.dumps(RESULTS))
'''


def run_legacy(script_path: str, cache_dir: str, timeout: int = 900) -> list:
    """Run a verify script once (cached by content hash of script and GA.py)."""
    with open(script_path, "rb") as fh:
        h = hashlib.sha256(fh.read())
    with open(os.path.join(LIB, "GA.py"), "rb") as fh:
        h.update(fh.read())
    suite_ga = os.path.join(os.path.dirname(os.path.abspath(script_path)), "GA.py")
    if os.path.exists(suite_ga):           # the GA the script would import beside it
        with open(suite_ga, "rb") as fh:
            h.update(fh.read())
    key = h.hexdigest()[:20]
    os.makedirs(cache_dir, exist_ok=True)
    cache = os.path.join(cache_dir, f"{os.path.basename(script_path)}.{key}.json")
    if os.path.exists(cache):
        with open(cache, encoding="utf-8") as fh:
            return json.load(fh)
    with tempfile.TemporaryDirectory() as tmp:
        drv = os.path.join(tmp, "legacy_driver.py")
        with open(drv, "w", encoding="utf-8") as fh:
            fh.write(f"LIB={LIB!r}\nSCRIPT={os.path.abspath(script_path)!r}\n" + LEGACY_DRIVER)
        try:
            cp = subprocess.run([sys.executable, drv], capture_output=True, text=True,
                                timeout=timeout,
                                cwd=os.path.dirname(os.path.abspath(script_path)))
        except subprocess.TimeoutExpired:
            raise RuntimeError(f"legacy script timed out after {timeout}s: {script_path}")
    results = []
    for line in cp.stdout.splitlines():
        if line.startswith("@@LEGACY@@"):
            results = json.loads(line[len("@@LEGACY@@"):])
    if not results:
        raise RuntimeError(f"legacy script produced no results: {script_path}\n"
                           f"{cp.stderr[-800:]}")
    with open(cache, "w", encoding="utf-8") as fh:
        json.dump(results, fh)
    return results
