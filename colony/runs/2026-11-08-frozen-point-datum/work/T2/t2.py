"""Restater T2 helpers: copy a stored entity to proposals/<id>, bump its version, add the credit,
amendment and maintainer note, and make exact unique text replacements."""
import os
import re
import shutil
import sys

LAB = "/home/claude/phys-graph"
DIRS = ("claims", "objects", "notes")


def stored(eid):
    for d in DIRS:
        p = os.path.join(LAB, "store", d, eid)
        if os.path.isdir(p):
            return p
    raise SystemExit(f"no stored entity {eid}")


def start(eid):
    """Copy store/<kind>/<id> to proposals/<id> (no __pycache__); refuse if it exists."""
    dst = os.path.join(LAB, "proposals", eid)
    if os.path.exists(dst):
        raise SystemExit(f"{dst} exists")
    shutil.copytree(stored(eid), dst, ignore=shutil.ignore_patterns("__pycache__"))
    return dst


def sub(path, old, new, count=1):
    s = open(path, encoding="utf-8").read()
    n = s.count(old)
    if n != count:
        raise SystemExit(f"{path}: expected {count} occurrence(s), found {n} of:\n{old}")
    s = s.replace(old, new)
    open(path, "w", encoding="utf-8").write(s)


def yq(s):
    return "'" + s.replace("'", "''") + "'"


def bump(eid, note, defect, evidence=None, kind="restatement", role="restated with H as the rational datum"):
    """Version v -> v+1 with credit, amendment and maintainer note."""
    p = os.path.join(LAB, "proposals", eid, "entity.md")
    s = open(p, encoding="utf-8").read()
    m = re.search(r"^version: (\d+)$", s, re.M)
    v = int(m.group(1))
    s = s[:m.start()] + f"version: {v + 1}" + s[m.end():]
    credit = (f"- name: Claude Opus 5.5\n  role: {yq(role)}\n  version: {v + 1}\n"
              f"  source: run 2026-11-08-frozen-point-datum\n")
    amend = f"amendments:\n- version: {v + 1}\n  kind: {kind}\n  defect: {yq(defect)}\n"
    if evidence:
        amend += f"  evidence: {evidence}\n"
    # credit list ends where the next top-level key starts
    cm = re.search(r"^credit:\n((?:[- ] .*\n)+)", s, re.M)
    if not cm:
        raise SystemExit("no credit block")
    end = cm.end()
    s = s[:end] + credit + s[end:]
    if re.search(r"^amendments:", s, re.M):
        am = re.search(r"^amendments:\n((?:[- ] .*\n)+)", s, re.M)
        s = s[:am.end()] + amend.split("\n", 1)[1] + s[am.end():]
    else:
        cm = re.search(r"^credit:\n((?:[- ] .*\n)+)", s, re.M)
        s = s[:cm.end()] + amend + s[cm.end():]
    key = "maintainer_pass_2026_11_08"
    if re.search(rf"^  {key}:", s, re.M):
        key = "maintainer_pass_2026_11_08_datum"
    full = (f"Version {v} -> {v + 1}. Leon's decision of 8 November 2026 (op.frozen-point-rational-datum): "
            + note)
    block = f"  {key}:\n    by: ai-maintainer-pass\n    note: >-\n      {full}\n"
    em = re.search(r"^extraction:\n", s, re.M)
    if em:
        s = s[:em.end()] + block + s[em.end():]
    else:
        fm = re.search(r"^---\s*$", s[4:], re.M)
        pos = 4 + fm.start()
        s = s[:pos] + "extraction:\n" + block + s[pos:]
    open(p, "w", encoding="utf-8").write(s)
    return v, v + 1


if __name__ == "__main__":
    print(stored(sys.argv[1]))
