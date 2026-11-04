"""Credit: who did what on each entity, and which model, where that is on record.

Every entity carries a `credit` list of {name, role, source?}. The roles follow the papers' own
authorship disclosure: the idea, the direction and the review are Leon Butler's; the mathematics
and the drafting were done with Claude. A model is named only where there is evidence for it, and
`source` says what that evidence is:

  - results extracted from a paper of the series: the model named in the paper's authorship
    disclosure (every paper of the series carries it: Claude Fable 5);
  - results proposed by an AI session (colony runs, maintainer passes): the Co-Authored-By trailer
    of the commit that added the entity to the store;
  - otherwise "Claude (model not recorded)", never a guess.

  python -m tp credit [--store store] [--dry-run]     fill in credit where it is missing

Filling in never changes an existing `credit`: a submitter's own credit stands as written.
"""
import argparse
import glob
import os
import re
import subprocess

AUTHOR = "Leon Butler"
SERIES_MODEL = "Claude Fable 5"
UNRECORDED = "Claude (model not recorded)"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# papers deposited on Zenodo (deposits/*.tex), each with the disclosure naming the model
_DEPOSITED = None
# companion notes and others whose source is not in the repository: their model is not on record
# here, apart from the series notes that carry the standard disclaimer
NOT_SERIES = {"QG notes"}


def _deposited(root):
    global _DEPOSITED
    if _DEPOSITED is None:
        _DEPOSITED = {}
        for f in glob.glob(os.path.join(root, "deposits", "T*.tex")):
            code = os.path.basename(f).split("_")[0]
            with open(f, encoding="utf-8") as fh:
                m = re.search(r"collaboration with (Claude [A-Za-z]+ [0-9.]+)", fh.read())
            if m:
                _DEPOSITED[code] = m.group(1)
    return _DEPOSITED


def for_paper(code, root=REPO):
    """Credit for a result extracted from paper `code`."""
    lead = {"name": AUTHOR, "role": "idea, direction and review"}
    dep = _deposited(root)
    if code in dep:
        return [lead, {"name": dep[code], "role": "mathematics and drafting",
                       "source": f"authorship disclosure of {code}, deposited version"}]
    if code and code not in NOT_SERIES:
        return [lead, {"name": SERIES_MODEL, "role": "mathematics and drafting",
                       "source": f"authorship disclosure of {code}, the series' standard disclaimer"}]
    return [lead, {"name": UNRECORDED, "role": "mathematics and drafting"}]


def for_ai(path, root=REPO):
    """Credit for an AI-proposed entity: the model from the commit that added it."""
    lead = {"name": AUTHOR, "role": "direction"}
    try:
        shas = subprocess.run(["git", "log", "--diff-filter=A", "--format=%H", "--", path],
                              cwd=root, capture_output=True, text=True, check=True).stdout.split()
    except (OSError, subprocess.CalledProcessError):
        shas = []
    if shas:
        body = subprocess.run(["git", "show", "-s", "--format=%b", shas[-1]], cwd=root,
                              capture_output=True, text=True).stdout
        models = sorted({m.strip() for m in re.findall(r"Co-Authored-By: (Claude[^<\n]*)", body)})
        if len(models) == 1:
            return [lead, {"name": models[0], "role": "proposal and drafting",
                           "source": "Co-Authored-By trailer of the commit that added it"}]
    return [lead, {"name": UNRECORDED, "role": "proposal and drafting"}]


def compare(old_credit, new_credit, old_version, new_version):
    """An amendment keeps every earlier credit entry and adds its own.

    old_credit and new_credit are lists of [name, role, version] (as the lock records them) or
    of credit mappings. Returns (removed, unclaimed): the earlier entries missing or changed in the
    new list, and whether the version went up with no credit entry for the new version."""
    def key(c):
        if isinstance(c, dict):
            return (str(c.get("name", "")), str(c.get("role", "")), c.get("version"))
        return (str(c[0]), str(c[1]), c[2] if len(c) > 2 else None)
    new_keys = {key(c) for c in (new_credit or [])}
    removed = [key(c) for c in (old_credit or []) if key(c) not in new_keys]
    unclaimed = bool(new_version and old_version and new_version > old_version
                     and not any(k[2] == new_version for k in new_keys))
    return removed, unclaimed


def describe(entry):
    name, role, version = entry
    return f"{name} ({role}{', v' + str(version) if version else ''})"


def _yaml_block(credit):
    def q(s):
        return "'" + s.replace("'", "''") + "'" if re.search(r"[:#'\"\[\]{}&*!|>%@`]", s) else s
    out = ["credit:"]
    for c in credit:
        out.append(f"- name: {q(c['name'])}")
        out.append(f"  role: {q(c['role'])}")
        if c.get("source"):
            out.append(f"  source: {q(c['source'])}")
    return out


def _frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    return None if end < 0 else (text[4:end], end)


def fill(store_dir="store", root=".", dry_run=False):
    """Add credit (and ai_involved: 'yes' for results from the papers) where it is missing.
    Returns the number of entities changed."""
    import yaml
    changed = 0
    for path in sorted(glob.glob(os.path.join(store_dir, "*", "*", "entity.md"))):
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        fmx = _frontmatter(text)
        if not fmx:
            continue
        fm_text, end = fmx
        meta = yaml.safe_load(fm_text) or {}
        if meta.get("credit"):
            continue
        kind = (meta.get("proposed_by") or {}).get("kind")
        paper = (meta.get("locators") or {}).get("paper")
        if kind == "ai":
            credit = for_ai(os.path.relpath(path, root), root)
        elif paper:
            credit = for_paper(paper, root)
        else:
            credit = [{"name": AUTHOR, "role": "idea, direction and review"},
                      {"name": UNRECORDED, "role": "mathematics and drafting"}]
        lines = fm_text.split("\n")
        # the papers' disclosure says AI was involved: record it
        if kind != "ai" and paper:
            lines = [re.sub(r"^ai_involved: .*$", "ai_involved: 'yes'", ln) for ln in lines]
        at = next((i for i, ln in enumerate(lines) if ln.startswith("ai_involved:")), None)
        if at is None:
            at = next((i for i, ln in enumerate(lines) if ln.startswith("proposed_by:")), len(lines) - 1)
            while at + 1 < len(lines) and lines[at + 1].startswith(" "):
                at += 1
        lines[at + 1:at + 1] = _yaml_block(credit)
        new = "---\n" + "\n".join(lines) + text[end:]
        assert (yaml.safe_load(new[4:new.find("\n---", 4)]) or {}).get("credit") == credit, path
        changed += 1
        if not dry_run:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new)
    return changed


def main(argv=None):
    ap = argparse.ArgumentParser(prog="tp credit")
    ap.add_argument("cmd")
    ap.add_argument("--store", default="store")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    root = os.path.dirname(os.path.abspath(a.store)) or "."
    n = fill(a.store, root, a.dry_run)
    print(f"credit: {n} entit{'y' if n == 1 else 'ies'} {'would be ' if a.dry_run else ''}filled in")
    return 0
