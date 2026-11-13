"""Expert reviews: records sealed by ORCID (docs/REVIEWS.md).

A review is a record from one person about one version of one result: an endorsement or an
objection. Every record has two parts.

  signed part    what the reviewer submitted. It is stored in the Physics Graph at
                 store/reviews/<result id>/<hash>.yaml, where <hash> is the SHA-256 of its
                 canonical form. ORCID signs that hash: the review server passes it as the
                 OpenID Connect nonce, and ORCID returns it inside the id_token it signs.
  attached part  added by the review server after sign-in: the reviewer's iD and name, ORCID's
                 id_token, and the qualification check. It holds everything identifying, so it
                 lives only in the open review log (a separate repository named by
                 `reviews.log` in store/config.yaml), never in the Physics Graph's history.

Anyone can check a record without trusting the maintainer or the server: the token's RS256
signature against ORCID's published keys (archived in store/orcid_keys/), its issuer and
audience, its subject against the iD, and its nonce against the hash of the signed part.

Records of kind `withdrawal`, `answer` and `ruling` point at another record with `refers_to`.
This module applies reviews and withdrawals. Answers are checked (they must come from a
maintainer's iD) and kept; rulings are checked for shape and kept; neither changes a result's
standing yet (adjudication and lapse are stage 3 of the design).

Nothing here needs a network or a third-party package: the RSA check is done with Python's
own integers, so CI (which installs only pyyaml and jsonschema) runs it as is.

Whether any of this is shown is decided by `reviews.enabled` in store/config.yaml
(`enabled()` below). The records are validated whatever the switch says.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
import re
from dataclasses import dataclass, field

import yaml

REVIEWS_DIR = "reviews"
KEYS_DIR = "orcid_keys"
REVIEW_LOCK = ".tp-reviews-lock.json"
REDACTIONS = "redactions.yaml"

KINDS = ("review", "withdrawal", "answer", "ruling")
VERDICTS = {"review": ("endorse", "object"), "ruling": ("holds", "does not hold")}
SCOPES = ("statement", "proof", "check", "imports")
DEPTHS = ("read", "line-by-line")
ROUTES = ("employment", "publications", "invitation")
SIGNED_FIELDS = ("kind", "result", "version", "fingerprint", "verdict", "scope", "depth",
                 "location", "defect", "conflicts", "note", "refers_to", "terms",
                 "zenodo_credit")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
ORCID_RE = re.compile(r"^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$")
LOCATION_RE = re.compile(r"^(statement|check|proof step [1-9][0-9]*)$")


# ---------------------------------------------------------------------------
# hashing
# ---------------------------------------------------------------------------

def canonical(signed: dict) -> bytes:
    """The signed part as sorted-key, whitespace-free UTF-8 JSON (the form ORCID seals)."""
    return json.dumps(signed, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False).encode("utf-8")


def record_hash(signed: dict) -> str:
    return hashlib.sha256(canonical(signed)).hexdigest()


def fingerprint(entity) -> str:
    """SHA-256 of everything a reviewer is shown and vouches for: the statement, the proofs,
    the check files, the status and links, with every premise pin kept at its version (the
    substantive hash drops pin versions and is cut to 16 characters; this is neither)."""
    sub = entity._substantive()
    blob = json.dumps(sub, sort_keys=True, separators=(",", ":"), default=str,
                      ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# ORCID's id_token: RS256 without third-party packages
# ---------------------------------------------------------------------------

def _b64(s: str) -> bytes:
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))


def _int(s: str) -> int:
    return int.from_bytes(_b64(s), "big")


# DER prefix of DigestInfo for SHA-256 (RFC 8017, section 9.2, note 1)
_SHA256_INFO = bytes.fromhex("3031300d060960864801650304020105000420")


def rs256_ok(signing_input: bytes, sig: bytes, n: int, e: int) -> bool:
    """RSASSA-PKCS1-v1_5 verification with SHA-256 (RFC 8017, section 8.2.2)."""
    k = (n.bit_length() + 7) // 8
    if len(sig) != k:
        return False
    s = int.from_bytes(sig, "big")
    if s >= n:
        return False
    em = pow(s, e, n).to_bytes(k, "big")
    t = _SHA256_INFO + hashlib.sha256(signing_input).digest()
    if k < len(t) + 11:
        return False
    expected = b"\x00\x01" + b"\xff" * (k - len(t) - 3) + b"\x00" + t
    # constant-time comparison is not needed: nothing here is secret
    return em == expected


def load_keys(store_root: str) -> dict:
    """Every RSA key ever seen from ORCID, by key id: store/orcid_keys/*.json, each a JWKS
    as published at https://orcid.org/oauth/jwks (or the sandbox's). Old keys are never
    removed, so tokens signed before ORCID rotates its key stay checkable."""
    keys = {}
    folder = os.path.join(store_root, KEYS_DIR)
    if not os.path.isdir(folder):
        return keys
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".json"):
            continue
        with open(os.path.join(folder, name), encoding="utf-8") as fh:
            doc = json.load(fh)
        for k in doc.get("keys") or []:
            if k.get("kty") == "RSA" and k.get("kid") and k.get("n") and k.get("e"):
                keys[k["kid"]] = {"n": _int(k["n"]), "e": _int(k["e"]),
                                  "issuer": doc.get("issuer"), "file": name}
    return keys


class TokenError(ValueError):
    pass


def verify_token(token: str, keys: dict) -> dict:
    """-> the token's claims when its RS256 signature verifies against an archived ORCID
    key; TokenError otherwise. Claims are not judged here (see check_claims)."""
    if not isinstance(token, str) or token.count(".") != 2:
        raise TokenError("not a JSON web token")
    h64, p64, s64 = token.split(".")
    try:
        header = json.loads(_b64(h64))
        claims = json.loads(_b64(p64))
        sig = _b64(s64)
    except (ValueError, json.JSONDecodeError) as exc:
        raise TokenError(f"unreadable token ({exc})")
    if header.get("alg") != "RS256":
        raise TokenError(f"algorithm {header.get('alg')!r}, expected RS256")
    key = keys.get(header.get("kid"))
    if key is None:
        raise TokenError(f"key {header.get('kid')!r} is not in store/{KEYS_DIR}/")
    if not rs256_ok(f"{h64}.{p64}".encode("ascii"), sig, key["n"], key["e"]):
        raise TokenError("signature does not verify against ORCID's key")
    if key.get("issuer") and claims.get("iss") != key["issuer"]:
        raise TokenError(f"issuer {claims.get('iss')!r} does not match the key's issuer "
                         f"{key['issuer']!r}")
    return claims


def check_claims(claims: dict, *, issuers, audiences, orcid: str, nonce: str) -> list:
    """What is wrong with a verified token's claims for this record (empty when nothing).
    Expiry is ignored on purpose: the token attests what ORCID confirmed at submission."""
    bad = []
    if claims.get("iss") not in issuers:
        bad.append(f"issuer {claims.get('iss')!r} is not accepted ({', '.join(issuers)})")
    aud = claims.get("aud")
    auds = aud if isinstance(aud, list) else [aud]
    if not any(a in audiences for a in auds):
        bad.append(f"audience {aud!r} is not the review service")
    if claims.get("sub") != orcid:
        bad.append(f"token is for {claims.get('sub')!r}, the record says {orcid!r}")
    if claims.get("nonce") != nonce:
        bad.append("the token's nonce is not the hash of the signed part: "
                   "the review was changed after it was signed, or the token belongs to another")
    return bad


# ---------------------------------------------------------------------------
# configuration: the switch and the ORCID settings
# ---------------------------------------------------------------------------

def settings(config: dict) -> dict:
    """store/config.yaml `reviews`, with defaults. Off unless switched on."""
    raw = (config or {}).get("reviews") or {}
    orcid = raw.get("orcid") or {}
    return {
        "enabled": bool(raw.get("enabled", False)),
        "log": raw.get("log"),
        "issuers": list(orcid.get("issuers") or ["https://orcid.org"]),
        "client_ids": list(orcid.get("client_ids") or []),
        "maintainer_orcids": list(raw.get("maintainer_orcids") or []),
        "rule_versions": [int(x) for x in (raw.get("rule_versions") or [1])],
        "terms_versions": [int(x) for x in (raw.get("terms_versions") or [1])],
    }


def enabled(config: dict) -> bool:
    """Whether reviews are shown on the site and through MCP (they are always validated)."""
    return settings(config)["enabled"]


def log_dir(store_root: str, config: dict):
    p = settings(config)["log"]
    if not p:
        return None
    return p if os.path.isabs(p) else os.path.normpath(os.path.join(store_root, p))


# ---------------------------------------------------------------------------
# loading
# ---------------------------------------------------------------------------

@dataclass
class Record:
    hash: str                      # the file name's hash
    path: str                      # store-relative path of the signed part
    signed: dict
    attached: dict = None          # from the open review log, or None
    errors: list = field(default_factory=list)   # (code, message, fix)
    claims: dict = None            # the verified token's claims
    redacted: str = None           # "identity" or "text" when removed on request or for abuse

    @property
    def kind(self):
        return self.signed.get("kind")

    @property
    def result(self):
        return self.signed.get("result")

    @property
    def orcid(self):
        return (self.attached or {}).get("orcid")

    @property
    def valid(self):
        return not self.errors and self.claims is not None and not self.redacted


def _read_yaml(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def redactions(store_root: str) -> dict:
    """store/reviews/redactions.yaml: [{hash, what: identity|text, date, reason}]. The only
    records that may change or disappear after they are accepted."""
    p = os.path.join(store_root, REVIEWS_DIR, REDACTIONS)
    if not os.path.exists(p):
        return {}
    rows = _read_yaml(p) or []
    return {str(r.get("hash")): r for r in rows if isinstance(r, dict) and r.get("hash")}


def review_files(store_root: str) -> list:
    """Store-relative paths of every signed part, sorted."""
    base = os.path.join(store_root, REVIEWS_DIR)
    out = []
    if not os.path.isdir(base):
        return out
    for rid in sorted(os.listdir(base)):
        folder = os.path.join(base, rid)
        if not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder)):
            if name.endswith(".yaml"):
                out.append(f"{REVIEWS_DIR}/{rid}/{name}")
    return out


def _shape(rec: Record, cfg: dict) -> None:
    s, add = rec.signed, rec.errors.append
    if not isinstance(s, dict):
        add(("E130", "the signed part is not a mapping", ""))
        rec.signed = {}
        return
    extra = sorted(set(s) - set(SIGNED_FIELDS))
    if extra:
        add(("E130", f"unknown field(s) in the signed part: {', '.join(extra)}",
             f"the signed part holds only {', '.join(SIGNED_FIELDS)}"))
    kind = s.get("kind")
    if kind not in KINDS:
        add(("E130", f"kind {kind!r} is not one of {', '.join(KINDS)}", ""))
        return
    if not isinstance(s.get("result"), str) or not isinstance(s.get("version"), int):
        add(("E130", "result (an entity id) and version (an integer) are required", ""))
    if s.get("terms") not in cfg["terms_versions"]:
        add(("E130", f"terms {s.get('terms')!r} is not a published version of the reviewer "
             f"terms ({cfg['terms_versions']})", ""))
    if kind in ("withdrawal", "answer", "ruling"):
        if not (isinstance(s.get("refers_to"), str) and HEX64.match(s["refers_to"])):
            add(("E130", f"a {kind} needs refers_to: the hash of the record it concerns", ""))
    if kind in ("review", "ruling") and s.get("verdict") not in VERDICTS[kind]:
        add(("E130", f"verdict {s.get('verdict')!r} is not one of {', '.join(VERDICTS[kind])}", ""))
    if kind == "review":
        if not (isinstance(s.get("fingerprint"), str) and HEX64.match(s["fingerprint"])):
            add(("E130", "a review needs the fingerprint of what the reviewer was shown", ""))
        scope = s.get("scope")
        if not (isinstance(scope, list) and scope and set(scope) <= set(SCOPES)):
            add(("E130", f"scope must be one or more of {', '.join(SCOPES)}", ""))
        if s.get("depth") not in DEPTHS:
            add(("E130", f"depth must be one of {', '.join(DEPTHS)}", ""))
        if not isinstance(s.get("conflicts"), str) or not s["conflicts"].strip():
            add(("E130", "conflicts must be declared (\"none\" if there are none)", ""))
        if s.get("zenodo_credit") not in (True, False):
            add(("E130", "zenodo_credit must be true or false", ""))
        if s.get("verdict") == "object":
            if not (isinstance(s.get("location"), str) and LOCATION_RE.match(s["location"])):
                add(("E130", "an objection names its location: statement, check, or "
                     "'proof step n'", ""))
            if not (isinstance(s.get("defect"), str) and len(s["defect"].strip()) >= 30):
                add(("E130", "an objection states its defect in at least 30 characters", ""))


def _attached(rec: Record, logdir: str) -> None:
    if not logdir:
        rec.errors.append(("E133", "the open review log is not configured "
                           "(reviews.log in store/config.yaml)",
                           "check out the open review log and set reviews.log"))
        return
    p = os.path.join(logdir, "records", rec.hash + ".json")
    if not os.path.exists(p):
        rec.errors.append(("E133", f"no entry for this record in the open review log ({p})",
                           "the review server writes the log entry; a record cannot be "
                           "accepted without it"))
        return
    with open(p, encoding="utf-8") as fh:
        entry = json.load(fh)
    if entry.get("removed"):
        rec.redacted = "identity"
        return
    if record_hash(entry.get("signed") or {}) != rec.hash:
        rec.errors.append(("E133", "the log entry's signed part differs from the store's", ""))
        return
    rec.attached = {k: entry.get(k) for k in ("orcid", "by", "orcid_token", "qualification",
                                              "submitted")}


def _token(rec: Record, keys: dict, cfg: dict) -> None:
    a = rec.attached or {}
    if not (isinstance(a.get("orcid"), str) and ORCID_RE.match(a["orcid"])):
        rec.errors.append(("E135", f"the log entry's iD {a.get('orcid')!r} is not an ORCID iD", ""))
        return
    try:
        claims = verify_token(a.get("orcid_token"), keys)
    except TokenError as exc:
        rec.errors.append(("E134", f"ORCID's token does not check: {exc}",
                           "a review is accepted only with the id_token ORCID signed at "
                           "submission"))
        return
    bad = check_claims(claims, issuers=cfg["issuers"], audiences=cfg["client_ids"],
                       orcid=a["orcid"], nonce=rec.hash)
    if bad:
        rec.errors.append(("E135", "; ".join(bad), ""))
        return
    rec.claims = claims


def load(store_root: str, config: dict, entities: dict = None) -> list:
    """Every record in the store, each checked as far as it can be on its own: shape, file
    name, the open review log, ORCID's token. Cross-record rules (withdrawals by the same
    person, answers by a maintainer, results that exist) are checked in `cross_check`."""
    cfg = settings(config)
    keys = load_keys(store_root)
    logdir = log_dir(store_root, config)
    red = redactions(store_root)
    out = []
    for rel in review_files(store_root):
        name = os.path.basename(rel)[:-5]
        try:
            signed = _read_yaml(os.path.join(store_root, rel))
        except yaml.YAMLError as exc:
            out.append(Record(name, rel, {}, errors=[("E130", f"YAML parse error: {exc}", "")]))
            continue
        rec = Record(name, rel, signed if isinstance(signed, dict) else signed)
        if name in red:
            rec.redacted = str(red[name].get("what") or "identity")
            out.append(rec)
            continue
        _shape(rec, cfg)
        if rec.errors:
            out.append(rec)
            continue
        if record_hash(rec.signed) != name:
            rec.errors.append(("E131", f"file name {name} is not the hash of the signed part "
                               f"({record_hash(rec.signed)})",
                               "the file is named by the SHA-256 of its canonical JSON"))
        elif rel.split("/")[1] != rec.result:
            rec.errors.append(("E131", f"filed under {rel.split('/')[1]} but concerns "
                               f"{rec.result}", ""))
        if not rec.errors:
            _attached(rec, logdir)
        if not rec.errors and not rec.redacted:
            _token(rec, keys, cfg)
        out.append(rec)
    cross_check(out, entities or {}, cfg)
    return out


def cross_check(records: list, entities: dict, cfg: dict) -> None:
    by_hash = {r.hash: r for r in records}
    for r in records:
        if r.errors or r.redacted:
            continue
        e = entities.get(r.result)
        if entities and e is None:
            r.errors.append(("E132", f"concerns {r.result}, which is not in the store", ""))
            continue
        if e is not None and r.signed["version"] > e.version:
            r.errors.append(("E132", f"is for version {r.signed['version']} of {r.result}, "
                             f"which is at version {e.version}", ""))
        if r.kind in ("withdrawal", "answer", "ruling"):
            target = by_hash.get(r.signed["refers_to"])
            if target is None:
                r.errors.append(("E136", f"refers to {r.signed['refers_to'][:12]}..., which is "
                                 "not in the store", ""))
                continue
            if target.result != r.result:
                r.errors.append(("E136", "refers to a record about another result", ""))
            if r.kind == "withdrawal" and target.orcid and r.orcid != target.orcid:
                r.errors.append(("E136", "a withdrawal must come from the iD that made the "
                                 "record it withdraws", ""))
            if r.kind == "answer":
                if target.kind != "review" or target.signed.get("verdict") != "object":
                    r.errors.append(("E137", "an answer must answer an objection", ""))
                elif r.orcid not in cfg["maintainer_orcids"]:
                    r.errors.append(("E137", f"an answer must come from a maintainer's iD "
                                     f"(reviews.maintainer_orcids); {r.orcid} is not one", ""))
            if r.kind == "ruling" and (target.kind != "review"
                                       or target.signed.get("verdict") != "object"):
                r.errors.append(("E136", "a ruling must rule on an objection", ""))


# ---------------------------------------------------------------------------
# standing: what the records mean for a result
# ---------------------------------------------------------------------------

def qualified(rec: Record, cfg: dict) -> bool:
    q = (rec.attached or {}).get("qualification") or {}
    return q.get("route") in ROUTES and q.get("rule") in cfg["rule_versions"]


def standing(records: list, entities: dict, config: dict) -> dict:
    """result id -> {reviews: [...], trust: derived level or None, disputed: bool}.

    A review is current when it is for the result's current version and its fingerprint
    matches; withdrawn when a valid withdrawal by the same iD refers to it. human-read needs
    a current endorsement; human-checked a current endorsement from a qualified reviewer with
    proof in scope at depth line-by-line. A result is disputed while a current objection from
    a qualified reviewer stands (answers and rulings do not change that until stage 3)."""
    cfg = settings(config)
    withdrawn = {r.signed["refers_to"] for r in records
                 if r.valid and r.kind == "withdrawal"}
    out = {}
    for r in records:
        if r.kind != "review" or r.errors:
            continue
        e = entities.get(r.result)
        if e is None:
            continue
        row = out.setdefault(r.result, {"reviews": [], "trust": None, "disputed": False})
        current = (r.signed.get("version") == e.version
                   and r.signed.get("fingerprint") == fingerprint(e))
        state = ("removed" if r.redacted else "withdrawn" if r.hash in withdrawn
                 else "current" if current else "stale")
        q = qualified(r, cfg) if not r.redacted else False
        a = r.attached or {}
        item = {"hash": r.hash, "state": state, "kind": r.kind,
                "verdict": r.signed.get("verdict"), "version": r.signed.get("version"),
                "qualified": q}
        if r.redacted != "text":
            item.update({k: r.signed.get(k) for k in ("scope", "depth", "location", "defect",
                                                      "conflicts", "note") if r.signed.get(k)})
        if not r.redacted:
            item.update({"orcid": a.get("orcid"), "by": a.get("by"),
                         "route": ((a.get("qualification") or {}).get("route") if q else None),
                         "date": _date(r.claims)})
        row["reviews"].append(item)
        if state != "current":
            continue
        if r.signed["verdict"] == "endorse":
            lvl = ("human-checked" if q and "proof" in r.signed["scope"]
                   and r.signed["depth"] == "line-by-line" else "human-read")
            if row["trust"] != "human-checked":
                row["trust"] = lvl
        elif q:
            row["disputed"] = True
    for row in out.values():
        row["reviews"].sort(key=lambda x: (x.get("date") or "", x["hash"]))
    return out


def _date(claims):
    t = (claims or {}).get("iat") or (claims or {}).get("auth_time")
    if not isinstance(t, (int, float)):
        return None
    import datetime
    return datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m-%d")


def effective_trust(own, derived):
    """The level shown: published stays published; otherwise a level earned by reviews
    replaces the front-matter level (ai-proposed or ai-refereed)."""
    if own == "published":
        return own
    return derived or own


# ---------------------------------------------------------------------------
# the accepted state: append-only
# ---------------------------------------------------------------------------

def file_sha(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def lock_state(store_root: str) -> dict:
    """store-relative path -> SHA-256 of the file, for every signed part now in the store."""
    return {rel: file_sha(os.path.join(store_root, rel)) for rel in review_files(store_root)}


def read_lock(store_root: str) -> dict:
    p = os.path.join(store_root, REVIEW_LOCK)
    if not os.path.exists(p):
        return {}
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def write_lock(store_root: str) -> None:
    with open(os.path.join(store_root, REVIEW_LOCK), "w", encoding="utf-8") as fh:
        json.dump(lock_state(store_root), fh, indent=1, sort_keys=True)
        fh.write("\n")


def append_only(store_root: str) -> list:
    """(path, message) for every accepted record that has changed or gone. CI compares the
    store against the lock from the base branch, so a pull request cannot rewrite it.
    Records listed in redactions.yaml are the only exceptions."""
    locked, now = read_lock(store_root), lock_state(store_root)
    red = redactions(store_root)
    out = []
    for rel, sha in sorted(locked.items()):
        h = os.path.basename(rel)[:-5]
        if h in red:
            continue
        if rel not in now:
            out.append((rel, "an accepted review record was removed"))
        elif now[rel] != sha:
            out.append((rel, "an accepted review record was changed"))
    return out


# ---------------------------------------------------------------------------
# command line: tp reviews hash | fingerprint | add | check
# ---------------------------------------------------------------------------

def main(argv) -> int:
    import argparse
    import sys
    ap = argparse.ArgumentParser(prog="tp reviews")
    ap.add_argument("_cmd")
    ap.add_argument("action", choices=("hash", "fingerprint", "add", "check"))
    ap.add_argument("target", nargs="?",
                    help="hash: a signed part (JSON or YAML); fingerprint: an entity id; "
                         "add: a log entry (JSON with signed, orcid, by, orcid_token, "
                         "qualification)")
    ap.add_argument("--store", default="store")
    a = ap.parse_args(argv)
    from .model import load_store
    if a.action == "hash":
        with open(a.target, encoding="utf-8") as fh:
            print(record_hash(yaml.safe_load(fh)))
        return 0
    store = load_store(a.store)
    if a.action == "fingerprint":
        e = store.entities.get(a.target)
        if e is None:
            print(f"no entity {a.target!r}", file=sys.stderr)
            return 1
        print(f"{fingerprint(e)}  {a.target}@{e.version}")
        return 0
    if a.action == "add":
        # record by hand what the review server will write: the signed part into the store,
        # the whole entry into the open review log. Checked before anything is written.
        with open(a.target, encoding="utf-8") as fh:
            entry = json.load(fh)
        signed = entry["signed"]
        h = record_hash(signed)
        logdir = log_dir(a.store, store.config)
        if not logdir:
            print("reviews.log is not set in store/config.yaml", file=sys.stderr)
            return 1
        rec = Record(h, f"{REVIEWS_DIR}/{signed.get('result')}/{h}.yaml", dict(signed),
                     attached={k: entry.get(k) for k in ("orcid", "by", "orcid_token",
                                                         "qualification", "submitted")})
        cfg = settings(store.config)
        _shape(rec, cfg)
        if not rec.errors:
            _token(rec, load_keys(a.store), cfg)
        if rec.errors:
            for code, msg, _ in rec.errors:
                print(f"{code}  {msg}", file=sys.stderr)
            return 1
        os.makedirs(os.path.join(logdir, "records"), exist_ok=True)
        with open(os.path.join(logdir, "records", h + ".json"), "w", encoding="utf-8") as fh:
            json.dump(dict(entry, signed=signed), fh, indent=1, sort_keys=True,
                      ensure_ascii=False)
            fh.write("\n")
        folder = os.path.join(a.store, REVIEWS_DIR, signed["result"])
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, h + ".yaml"), "w", encoding="utf-8") as fh:
            yaml.safe_dump(signed, fh, sort_keys=True, allow_unicode=True)
        print(f"added {h} for {signed['result']}@{signed['version']}")
        return 0
    recs = load(a.store, store.config, store.entities)
    bad = [(r, c, m) for r in recs for c, m, _ in r.errors]
    for r, c, m in bad:
        print(f"{c}  {r.path}\n      {m}")
    for rel, msg in append_only(a.store):
        print(f"E138  {rel}\n      {msg}")
        bad.append((None, "E138", msg))
    print(f"{len(recs)} record(s), {sum(1 for r in recs if r.valid)} checked against ORCID's "
          f"key, {len(bad)} problem(s); reviews are "
          f"{'shown' if enabled(store.config) else 'hidden (reviews.enabled is false)'}")
    return 1 if bad else 0
