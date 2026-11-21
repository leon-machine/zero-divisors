"""Does each contribution's ORCID iD belong to the person who opened the pull request?

  python -m tp.orcid_link --store store --author <github login>

A pull request from anyone but a maintainer must credit every person with an ORCID iD (E610,
tp/validate.py, layer 6). An iD typed into a credit entry could be anyone's, so this check ties
the contribution to the account that opened it: the public ORCID record of at least one person
the pull request newly credits must list that GitHub account among its websites and social
links (https://github.com/<login>, visible to everyone).

  E611  no newly credited person's ORCID record links the pull request's GitHub account
  E612  ORCID could not be reached, or a record could not be read (re-run the check)
  W613  a newly credited co-author's record does not link the account: unverified, for the
        maintainer to judge at review

It reads ORCID's public API (pub.orcid.org, no key needed) and so needs the network: CI runs
it as a step of its own, outside the validator, which stays offline. A maintainer's pull
request is not checked, nor one that credits no new person. Exit status 1 on an error.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request

from .model import load_store

API = "https://pub.orcid.org/v3.0/{}/researcher-urls"
GITHUB_URL = re.compile(r"^(?:https?://)?(?:www\.)?github\.com/([A-Za-z0-9](?:[A-Za-z0-9-]{0,38}))/?$", re.I)


def _is_model(c):
    from .releases import MODEL_RE
    kind = c.get("kind")
    return kind == "ai" or (kind != "person" and bool(MODEL_RE.match(str(c.get("name") or ""))))


def new_people(store):
    """[(entity id, name, orcid)] for every person credited in an entry the accepted lock does
    not hold: all the people of a new entity, and an amendment's new entries."""
    out = []
    for eid, e in sorted(store.entities.items()):
        old = (store.lock.get(eid) or {}).get("credit") or []
        before = {tuple(c[:3]) if isinstance(c, (list, tuple)) else
                  (c.get("name"), c.get("role"), c.get("version")) for c in old}
        for c in e.meta.get("credit") or []:
            if not isinstance(c, dict) or _is_model(c):
                continue
            if (c.get("name"), c.get("role"), c.get("version")) in before:
                continue
            out.append((eid, c.get("name") or "an unnamed entry", c.get("orcid")))
    return out


def _urls(node):
    """Every URL value in an ORCID researcher-urls document, wherever it sits."""
    if isinstance(node, dict):
        u = node.get("url")
        if isinstance(u, dict) and isinstance(u.get("value"), str):
            yield u["value"]
        for v in node.values():
            yield from _urls(v)
    elif isinstance(node, list):
        for v in node:
            yield from _urls(v)


def fetch_urls(orcid, tries=3, timeout=20):
    """The public website links of an ORCID record (raises OSError when ORCID cannot be read)."""
    req = urllib.request.Request(API.format(orcid), headers={
        "Accept": "application/json", "User-Agent": "physics-graph-ci (tp.orcid_link)"})
    last = None
    for k in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return list(_urls(json.load(r)))
        except urllib.error.HTTPError as ex:
            if ex.code == 404:
                raise OSError(f"ORCID has no public record {orcid}") from ex
            last = ex
        except (urllib.error.URLError, OSError, ValueError) as ex:
            last = ex
        time.sleep(2 * (k + 1))
    raise OSError(f"ORCID could not be read for {orcid}: {last}")


def links_account(urls, login):
    """True when one of the links is the GitHub profile of `login` (case does not matter)."""
    for u in urls:
        m = GITHUB_URL.match(u.strip())
        if m and m.group(1).lower() == login.lower():
            return True
    return False


def check(store, author, fetch=fetch_urls):
    """-> [(code, entity, message)]; empty when the pull request passes."""
    gov = store.config.get("governance") or {}
    if author in set(gov.get("maintainers") or []) | set(gov.get("github_logins") or []):
        return []
    people = [(eid, name, oid) for eid, name, oid in new_people(store) if oid]
    if not people:
        return []        # no new person, or only ones without an iD, which E610 refuses already
    findings, linked, unlinked = [], set(), []
    cache = {}
    for eid, name, oid in people:
        if oid not in cache:
            try:
                cache[oid] = links_account(fetch(oid), author)
            except OSError as ex:
                findings.append(("E612", eid, f"{name}: {ex}; re-run the check"))
                cache[oid] = None
        if cache[oid]:
            linked.add(oid)
        elif cache[oid] is False:
            unlinked.append((eid, name, oid))
    if any(c == "E612" for c, _, _ in findings):
        return findings
    if not linked:
        ids = ", ".join(sorted({oid for _, _, oid in people}))
        findings.append(("E611", people[0][0],
                         f"no ORCID record credited here ({ids}) lists the GitHub account {author}; "
                         f"add https://github.com/{author} to your record's websites and social links, "
                         "visible to everyone, then re-run the check"))
        return findings
    for eid, name, oid in unlinked:
        findings.append(("W613", eid, f"{name} ({oid}) is credited but their ORCID record does not list "
                         f"{author}: a co-author the maintainer confirms at review"))
    return findings


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m tp.orcid_link")
    ap.add_argument("--store", default="store")
    ap.add_argument("--author", required=True, help="the pull request's GitHub login")
    a = ap.parse_args(argv)
    findings = check(load_store(a.store), a.author)
    for code, eid, msg in findings:
        print(f"{code}  {eid}\n      {msg}")
    errors = sum(c.startswith("E") for c, _, _ in findings)
    print(f"orcid_link: {errors} error(s), {len(findings) - errors} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
