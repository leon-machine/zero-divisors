"""Amendments: what a contributor's new version of an accepted result must show.

An amendment is measured by what it fixes, not by how much it changes. Each new version of an
accepted result made by someone other than a maintainer declares, in `amendments`, its kind and
the defect it fixes:

  - correction: the statement stands; a proof, a check, the status or a link was wrong. Results
    that rely on it still need their pins moved to the new version, but the statement they use is
    the same, so that is a formality (tp repin).
  - restatement: the statement itself was wrong or overstated (a missing hypothesis, a conclusion
    too strong). Every result that relies on it has to be re-checked against the new statement
    before its pin is moved.

A wording change (typo, notation, clarity) changes nothing substantive and keeps the version, so it
needs no declaration and earns no credit entry. A materially different or stronger conclusion is not
an amendment but a new result, linked to the original; whether a changed statement is still the
same theorem is the maintainer's call in review.

findings(old, e) compares an entity with its accepted state (a lock entry) and returns
(code, message, fix) triples:

  E605  the version went up with no `amendments` entry for it
  E606  the version went up with nothing substantive changed (a wording change keeps the version)
  E607  the declared kind does not match what changed
  E608  the evidence names no check of this result
"""


def declared(meta, version):
    for a in meta.get("amendments") or []:
        if isinstance(a, dict) and a.get("version") == version:
            return a
    return None


def findings(old, e):
    """old: the accepted lock entry (with "parts"); e: the new entity. Empty unless the version
    went up and the lock records the parts."""
    out = []
    if not old or "parts" not in old or e.version <= int(old.get("version") or 0):
        return out
    was, now = old["parts"], e.substantive_parts()
    changed = [p for p in ("statement", "proofs", "checks", "rest") if was.get(p) != now.get(p)]
    if not changed:
        out.append(("E606", f"version raised to {e.version} with nothing substantive changed",
                    f"a wording change keeps the version: set version: {old['version']}"))
        return out
    a = declared(e.meta, e.version)
    if not a:
        kind = "restatement" if "statement" in changed else "correction"
        out.append(("E605", f"version {e.version} does not say what it fixes",
                    f"add to amendments: {{version: {e.version}, kind: {kind}, defect: <what was wrong "
                    "with the accepted version>, evidence: <optional: check.py::the_check>}"))
        return out
    if a.get("kind") == "correction" and "statement" in changed:
        out.append(("E607", "declared a correction, but the statement changed",
                    "keep the statement, or declare a restatement and say what was wrong with it"))
    if a.get("kind") == "restatement" and "statement" not in changed:
        out.append(("E607", "declared a restatement, but the statement is unchanged",
                    "declare a correction"))
    ev = str(a.get("evidence") or "")
    if ev:
        refs = {str((c or {}).get("ref") or "") for c in e.meta.get("checked_by") or []
                if isinstance(c, dict)}
        if ev not in refs:
            out.append(("E608", f"the evidence {ev!r} is not one of this result's checks",
                        "name an entry of checked_by, as check.py::function"))
    return out
