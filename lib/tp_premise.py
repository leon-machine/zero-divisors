"""premise() and quantity(): the only ways a check reaches other entities.

Every call is recorded, so the validator can compare the premises a check
actually touched with the premises its derivations declare (layer 4), and the
quantities it read with the quantities the entity lists.
If the premise's own check.py defines EXPORTS (a dict of constructions), it
is returned, so a check can build on what its premise built.
"""
import importlib.util
import os
import re
from fractions import Fraction

TOUCHED = set()
TOUCHED_QUANTITIES = set()
_STORE = None
_DIRS = ("claims", "objects", "predictions", "questions")
_QUANTITY_DIR = "quantities"
_QUANTITY_CACHE = {}
_ID_RE = re.compile(r"^id:\s*['\"]?([^'\"\s]+)['\"]?\s*$", re.M)


def configure(store_root):
    global _STORE
    _STORE = store_root
    _QUANTITY_CACHE.clear()


def _find(pid, dirs):
    for sub in dirs:
        base = os.path.join(_STORE or "", sub)
        if not os.path.isdir(base):
            continue
        # entity folders are named by id; fall back to reading the front matter
        direct = os.path.join(base, pid, "entity.md")
        if os.path.exists(direct):
            return os.path.join(base, pid)
        for name in sorted(os.listdir(base)):
            ent = os.path.join(base, name, "entity.md")
            if os.path.exists(ent):
                with open(ent, encoding="utf-8") as fh:
                    text = fh.read().replace("\r\n", "\n")
                head = text.split("\n---", 1)[0]
                m = _ID_RE.search(head)
                if m and m.group(1) == pid:
                    return os.path.join(base, name)
    return None


def _folder_for(pid):
    return _find(pid, _DIRS)


def premise(pid):
    TOUCHED.add(pid)
    folder = _folder_for(pid)
    if folder is None:
        raise LookupError(f"premise {pid!r} is not in the store")
    path = os.path.join(folder, "check.py")
    if not os.path.exists(path):
        return {}
    spec = importlib.util.spec_from_file_location(f"premise_{pid.replace('.', '_')}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return dict(getattr(mod, "EXPORTS", {}))


def exact_value(text):
    """'0.51099895', '1.22089e19', '-3/4' -> Fraction; anything else raises ValueError.
    Record values are exact decimals (or fractions), never binary floats."""
    if isinstance(text, bool) or not isinstance(text, (str, int)):
        raise ValueError(f"a quantity value is a string, not {type(text).__name__}")
    s = str(text).strip()
    if not re.fullmatch(r"[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?|[+-]?\d+/[1-9]\d*", s):
        raise ValueError(f"{text!r} is not an exact decimal or fraction")
    return Fraction(s)


def quantity(qid):
    """The exact value of the quantity entity qid (quantity.value in
    store/quantities/<qid>/entity.md), as a Fraction."""
    TOUCHED_QUANTITIES.add(qid)
    if qid in _QUANTITY_CACHE:
        return _QUANTITY_CACHE[qid]
    folder = _find(qid, (_QUANTITY_DIR,))
    if folder is None:
        raise LookupError(f"quantity {qid!r} is not in the store")
    import yaml
    with open(os.path.join(folder, "entity.md"), encoding="utf-8") as fh:
        text = fh.read().replace("\r\n", "\n")
    head = text[3:].split("\n---", 1)[0] if text.startswith("---") else ""
    meta = yaml.safe_load(head) or {}
    block = meta.get("quantity") if isinstance(meta, dict) else None
    if not isinstance(block, dict) or "value" not in block:
        raise LookupError(f"quantity {qid!r} has no quantity.value")
    val = exact_value(block["value"])
    _QUANTITY_CACHE[qid] = val
    return val
