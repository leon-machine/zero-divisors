"""Call one MCP tool from the shell, as an AI client would.

    python -m tp.ask <tool> '<json arguments>' [--store store]

Prints the tool's JSON result. Every call is appended to the file named by
TP_ASK_LOG (if set), so a session's use of the tools can be measured.
"""
from __future__ import annotations

import json
import os
import sys
import time

from .mcp_server import Lab, TOOLS


def _lab(store):
    """A loaded Lab, cached between calls (a real MCP server stays loaded; this
    keeps the command-line client close to that). The cache is keyed on the
    newest modification time in the store, so any edit invalidates it."""
    import glob
    import hashlib
    import pickle
    import tempfile
    root = os.path.abspath(store)
    newest = max((os.path.getmtime(p) for p in glob.glob(os.path.join(root, "**"),
                                                           recursive=True)), default=0)
    key = hashlib.sha256(f"{root}|{newest}".encode()).hexdigest()[:16]
    path = os.path.join(tempfile.gettempdir(), f"tp-ask-{key}.pickle")
    if os.path.exists(path):
        try:
            with open(path, "rb") as fh:
                return pickle.load(fh)
        except Exception:
            pass
    lab = Lab(store)
    lab._semantic_scores("warm")          # build the semantic index once
    try:
        with open(path, "wb") as fh:
            pickle.dump(lab, fh)
    except Exception:
        pass
    return lab


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    store = "store"
    if "--store" in argv:
        i = argv.index("--store")
        store = argv[i + 1]
        del argv[i:i + 2]
    names = [t[0] for t in TOOLS]
    if not argv or argv[0] in ("-h", "--help", "tools"):
        for t in TOOLS:
            print(f"{t[0]}: {t[1]}\n    arguments: {json.dumps(t[2])}")
        return 0
    name = argv[0]
    args = json.loads(argv[1]) if len(argv) > 1 else {}
    if name not in names:
        print(f"no tool {name!r}; tools: {', '.join(names)}", file=sys.stderr)
        return 2
    t0 = time.time()
    try:
        result = getattr(_lab(store), name)(**args)
        ok = True
    except Exception as exc:          # report the tool's own error, as MCP would
        result, ok = {"error": f"{type(exc).__name__}: {exc}"}, False
    out = result if isinstance(result, str) else json.dumps(result, indent=1, default=str,
                                                             ensure_ascii=False)
    print(out)
    log = os.environ.get("TP_ASK_LOG")
    if log:
        with open(log, "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"tool": name, "args": args, "ok": ok, "chars": len(out),
                                 "seconds": round(time.time() - t0, 2)}) + "\n")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
