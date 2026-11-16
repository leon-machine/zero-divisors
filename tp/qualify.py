"""The qualification check for reviewers: rule version 1 (docs/REVIEWS.md, "Who counts").

Run by the review server once, when a review is submitted; its result is stored with the review
in the open review log, so the decision can be read later even if the reviewer's record changes.

Any one route qualifies:

  employment    a current employment on the ORCID record whose source is an organisation, not
                the reviewer (ORCID records who added each item)
  publications  at least `min_works` works on the ORCID record that
                  - carry a DOI,
                  - were added by a client (Crossref, a publisher, a search-and-link tool), not
                    typed in by the reviewer,
                  - have, in OpenAlex, a primary subfield in `subfields`, and
                  - list the reviewer's ORCID iD among their authors in OpenAlex
                    (`require_author_match`), so that linking someone else's paper does not count
  invitation    the reviewer's iD is in `invited` (named by the author for their expertise)

Everything the network returns goes through `fetch(url) -> parsed JSON or None`, so tests run on
recorded responses and the server can add caching or rate limiting in one place. ORCID's terms
forbid continuous polling: a record is read once per submission.
"""
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request

RULE_VERSION = 1

DEFAULTS = {
    "min_works": 3,
    # OpenAlex subfield ids: Mathematical Physics 2610; Astronomy and Astrophysics 3103 (where
    # general relativity papers are filed); Nuclear and High Energy Physics 3106; Atomic and
    # Molecular Physics, and Optics 3107 (quantum theory); Algebra and Number Theory 2602;
    # Geometry and Topology 2608
    "subfields": [2610, 3103, 3106, 3107, 2602, 2608],
    "require_author_match": True,
    "invited": [],
    "orcid_api": "https://pub.orcid.org/v3.0",
    "openalex_api": "https://api.openalex.org",
    "mailto": "",                # OpenAlex's "polite pool": an address it can write to
    "max_works_checked": 60,     # an upper bound on OpenAlex lookups per submission
}

DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")


def rule_settings(config: dict) -> dict:
    raw = ((config or {}).get("reviews") or {}).get("qualification") or {}
    out = dict(DEFAULTS)
    out.update({k: v for k, v in raw.items() if k in DEFAULTS})
    out["subfields"] = [int(x) for x in out["subfields"]]
    return out


def http_json(url: str, timeout=15):
    """GET a JSON document; None on a 404, a non-JSON reply or a network error."""
    req = urllib.request.Request(url, headers={"Accept": "application/json",
                                               "User-Agent": "physics-graph-review/1"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception:
        return None


def _source_is_person(source: dict, orcid: str) -> bool:
    """True when the reviewer typed the item in themselves (no organisation or client behind it)."""
    so = (source or {}).get("source-orcid") or {}
    return so.get("path") == orcid and not (source or {}).get("source-client-id")


def employment_route(employments: dict, orcid: str):
    """The first current employment asserted by an organisation, or None."""
    for group in (employments or {}).get("affiliation-group") or []:
        for s in group.get("summaries") or []:
            e = s.get("employment-summary") or {}
            if e.get("end-date"):
                continue
            src = e.get("source") or {}
            if _source_is_person(src, orcid) or not src.get("source-client-id"):
                continue
            org = (e.get("organization") or {}).get("name")
            return {"organisation": org,
                    "source": ((src.get("source-name") or {}).get("value")),
                    "role": e.get("role-title")}
    return None


def candidate_dois(works: dict, orcid: str) -> list:
    """DOIs of works added by a client (not typed in by the reviewer), one per work group."""
    out = []
    for group in (works or {}).get("group") or []:
        dois = [x.get("external-id-value") for x in
                ((group.get("external-ids") or {}).get("external-id") or [])
                if x.get("external-id-type") == "doi" and x.get("external-id-relationship",
                                                                 "self") == "self"]
        dois = [d.strip().lower() for d in dois if d and DOI_RE.match(d.strip())]
        if not dois:
            continue
        summaries = group.get("work-summary") or []
        if not any(not _source_is_person(w.get("source"), orcid)
                   and (w.get("source") or {}).get("source-client-id") for w in summaries):
            continue
        out.append(dois[0])
    return out


def _subfield_id(work: dict):
    sub = ((work or {}).get("primary_topic") or {}).get("subfield") or {}
    m = re.search(r"(\d+)$", str(sub.get("id") or ""))
    return (int(m.group(1)), sub.get("display_name")) if m else (None, None)


def _authors(work: dict) -> set:
    out = set()
    for a in (work or {}).get("authorships") or []:
        o = ((a.get("author") or {}).get("orcid") or "")
        if o:
            out.add(o.rsplit("/", 1)[-1])
    return out


def check(orcid: str, config: dict, fetch=http_json) -> dict:
    """-> {"route": employment|publications|invitation|None, "rule": 1, "evidence": {...}}.
    A route of None means the reviewer does not qualify under this rule; their review is still
    recorded and shown, but does not count towards trust or mark a result disputed."""
    s = rule_settings(config)
    out = {"rule": RULE_VERSION, "route": None, "evidence": {}}
    if orcid in s["invited"]:
        out["route"] = "invitation"
        return out
    base = s["orcid_api"].rstrip("/")
    emp = employment_route(fetch(f"{base}/{orcid}/employments"), orcid)
    if emp:
        out["route"] = "employment"
        out["evidence"] = {"employment": emp}
        return out
    dois = candidate_dois(fetch(f"{base}/{orcid}/works"), orcid)[: s["max_works_checked"]]
    counted, seen = [], 0
    mail = f"?mailto={urllib.parse.quote(s['mailto'])}" if s["mailto"] else ""
    for doi in dois:
        work = fetch(f"{s['openalex_api'].rstrip('/')}/works/doi:{urllib.parse.quote(doi)}{mail}")
        if not work:
            continue
        seen += 1
        sid, sname = _subfield_id(work)
        if sid not in s["subfields"]:
            continue
        if s["require_author_match"] and orcid not in _authors(work):
            continue
        counted.append({"doi": doi, "subfield": sname})
        if len(counted) >= s["min_works"]:
            break
    out["evidence"] = {"works_with_doi": len(dois), "works_found": seen, "counted": counted}
    if len(counted) >= s["min_works"]:
        out["route"] = "publications"
    return out
