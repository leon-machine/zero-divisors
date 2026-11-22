"""The review service: the page where a reviewer writes a review and signs in with ORCID to
submit it (docs/REVIEWS.md, stage 2 of the design).

  python -m tp.review_server --store store [--host 0.0.0.0] [--port 8090]

  GET  /review/<result id>      the form for one result (endorse or object)
  POST /review/<result id>      build the signed part, then send the reviewer to ORCID
  GET  /withdraw/<hash>         withdraw one's own review (signed in again with ORCID)
  GET  /answer/<hash>           the maintainer's answer to an objection
  GET  /callback                ORCID returns here: check the token, qualify, publish
  GET  /terms  /privacy         the reviewer terms and the privacy notice
  GET  /health                  "ok"

How a submission is sealed: the form is filled in first. The server builds the signed part from
it, recomputing the result's fingerprint from the store (a review of an out-of-date page is
refused), and takes its hash. It sends the browser to ORCID with that hash as the OpenID Connect
nonce (authorisation-code flow; the client secret never leaves the server) and a random state,
which is also set as a short-lived cookie so the sign-in completes only in the browser that
started it. ORCID returns a code; the server exchanges it for an id_token, verifies the token's
signature against the archived keys and checks that its nonce is the hash, its audience this
service and its issuer ORCID. It then runs the qualification check (tp/qualify.py) and publishes:
the open review log first, then a pull request (tp/review_publish.py). The contact email is held
only by the server, in a file outside both repositories.

Configuration: `reviews.server` in store/config.yaml (public address, ORCID base address, the
repositories) and environment variables for anything secret:

  TP_ORCID_CLIENT_ID, TP_ORCID_CLIENT_SECRET   the ORCID Public API client
  TP_GITHUB_TOKEN                              may write the open review log and open pull requests
  TP_REVIEW_STATE                              folder for contact emails (default ./review-state)

Pending sign-ins are held in memory for 30 minutes, so run one instance (or pin sessions).
"""
from __future__ import annotations

import argparse
import datetime
import html
import json
import os
import re
import secrets
import sys
import threading
import time
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from . import qualify, reviews
from .model import ID_RE, load_store

MAX_BODY = 64 * 1024
PENDING_TTL = 30 * 60
COOKIE = "rv_state"
TERMS_VERSION = 1
E = html.escape


# ---------------------------------------------------------------------------
# configuration
# ---------------------------------------------------------------------------

def server_settings(config: dict, env=os.environ) -> dict:
    raw = ((config or {}).get("reviews") or {}).get("server") or {}
    base = env.get("TP_REVIEW_BASE_URL") or raw.get("base_url") or "http://localhost:8090"
    return {
        "base_url": base.rstrip("/"),
        "orcid_base": (env.get("TP_ORCID_BASE") or raw.get("orcid_base")
                       or "https://orcid.org").rstrip("/"),
        "client_id": env.get("TP_ORCID_CLIENT_ID") or raw.get("client_id") or "",
        "client_secret": env.get("TP_ORCID_CLIENT_SECRET") or "",
        "graph_repo": raw.get("graph_repo") or "leon-machine/zero-divisors",
        "log_repo": raw.get("log_repo") or "leon-machine/review-log",
        "github_token": env.get("TP_GITHUB_TOKEN") or "",
        "site_url": ((config or {}).get("site_url") or "").rstrip("/"),
        "privacy_contact": raw.get("privacy_contact") or "",
        "state_dir": env.get("TP_REVIEW_STATE") or raw.get("state_dir") or "review-state",
    }


# ---------------------------------------------------------------------------
# ORCID
# ---------------------------------------------------------------------------

class OrcidClient:
    """OpenID Connect against ORCID (or its sandbox): the authorisation URL and the code
    exchange. Tests replace it with a fake that signs tokens with a test key."""

    def __init__(self, base, client_id, client_secret, redirect_uri, opener=None):
        self.base, self.client_id, self.secret, self.redirect = (base, client_id, client_secret,
                                                                 redirect_uri)
        self._open = opener or urllib.request.urlopen

    def authorize_url(self, state: str, nonce: str) -> str:
        q = urllib.parse.urlencode({"client_id": self.client_id, "response_type": "code",
                                    "scope": "openid", "redirect_uri": self.redirect,
                                    "state": state, "nonce": nonce})
        return f"{self.base}/oauth/authorize?{q}"

    def exchange(self, code: str) -> dict:
        body = urllib.parse.urlencode({"client_id": self.client_id, "client_secret": self.secret,
                                       "grant_type": "authorization_code", "code": code,
                                       "redirect_uri": self.redirect}).encode()
        req = urllib.request.Request(f"{self.base}/oauth/token", data=body, method="POST",
                                     headers={"Accept": "application/json",
                                              "Content-Type": "application/x-www-form-urlencoded"})
        with self._open(req, timeout=20) as r:
            return json.loads(r.read().decode("utf-8"))


# ---------------------------------------------------------------------------
# pages
# ---------------------------------------------------------------------------

CSS = """
:root{--bg:#f4f6f8;--panel:#fff;--ink:#18222c;--muted:#56636f;--rule:#dde3e8;--accent:#2747c9;--bad:#b8323f;--good:#217a43}
@media (prefers-color-scheme:dark){:root{--bg:#0b1016;--panel:#121921;--ink:#e2e9ef;--muted:#98a6b3;--rule:#243040;--accent:#8aa2ff;--bad:#ff7d88;--good:#63c98a}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 "IBM Plex Sans","Segoe UI",system-ui,sans-serif}
main{max-width:46em;margin:0 auto;padding:28px 16px 60px}h1{font:600 26px/1.2 "Source Serif 4",Georgia,serif;margin:0 0 6px}
h2{font:600 18px/1.3 system-ui,sans-serif;margin:26px 0 8px}a{color:var(--accent)}.note{color:var(--muted);font-size:14px}
.box{background:var(--panel);border:1px solid var(--rule);border-radius:10px;padding:14px 16px;margin:12px 0}
pre{white-space:pre-wrap;overflow-wrap:anywhere;font:14px/1.5 "IBM Plex Mono",ui-monospace,monospace;margin:0}
fieldset{border:1px solid var(--rule);border-radius:10px;padding:10px 14px;margin:14px 0}legend{font-weight:600;padding:0 4px}
label{display:block;margin:6px 0}input[type=text],input[type=email],textarea,select{width:100%;font:inherit;padding:8px 10px;border:1px solid var(--rule);border-radius:8px;background:var(--panel);color:var(--ink)}
textarea{min-height:6em}button{font:600 16px system-ui,sans-serif;padding:10px 18px;border-radius:8px;border:1px solid var(--accent);background:var(--accent);color:#fff;cursor:pointer}
.err{color:var(--bad);font-weight:600}.ok{color:var(--good);font-weight:600}
"""


def page(title, body, status=200):
    doc = (f"<!doctype html><html lang=en><head><meta charset=utf-8>"
           f"<meta name=viewport content='width=device-width,initial-scale=1'>"
           f"<title>{E(title)} | Physics Graph reviews</title><style>{CSS}</style></head>"
           f"<body><main>{body}<p class=note style='margin-top:40px'>"
           f"<a href='/terms'>Reviewer terms</a> · <a href='/privacy'>Privacy notice</a> · "
           f"ORCID confirms identity only and does not endorse reviews.</p></main></body></html>")
    return status, {"Content-Type": "text/html; charset=utf-8"}, doc.encode("utf-8")


def markdown_page(path, title):
    """A small, safe rendering of the terms and the privacy notice (headings, paragraphs, lists,
    bold): everything is escaped first."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    out, para, lst = [], [], None

    def inline(s):
        s = E(s)
        return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)

    def flush():
        nonlocal para, lst
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para = []
        if lst:
            tag, items = lst
            out.append(f"<{tag}>" + "".join(f"<li>{inline(i)}</li>" for i in items) + f"</{tag}>")
            lst = None

    for line in text.splitlines():
        m = re.match(r"^(#{1,3}) (.*)$", line)
        li = re.match(r"^\s*(?:(\d+)\.|-)\s+(.*)$", line)
        if m:
            flush()
            n = len(m.group(1))
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
        elif li:
            if para:
                flush()
            tag = "ol" if li.group(1) else "ul"
            if not lst or lst[0] != tag:
                flush()
                lst = (tag, [])
            lst[1].append(li.group(2))
        elif not line.strip():
            flush()
        elif lst:
            lst[1][-1] += " " + line.strip()
        else:
            para.append(line.strip())
    flush()
    return page(title, "".join(out))


def redirect(url, cookies=()):
    h = {"Location": url}
    if cookies:
        h["Set-Cookie"] = list(cookies)
    return 303, h, b""


# ---------------------------------------------------------------------------
# the service
# ---------------------------------------------------------------------------

class ReviewService:
    def __init__(self, store_root, orcid=None, publisher=None, fetch=qualify.http_json,
                 env=os.environ, now=time.time, docs_dir=None):
        self.store_root = os.path.abspath(store_root)
        self.env, self.now, self.fetch = env, now, fetch
        self.docs = docs_dir or os.path.join(os.path.dirname(self.store_root), "docs")
        self.lock = threading.Lock()
        self.pending = {}
        self.reload()
        s = self.srv
        self.orcid = orcid or OrcidClient(s["orcid_base"], s["client_id"], s["client_secret"],
                                          s["base_url"] + "/callback")
        if publisher is None:
            from .review_publish import GitHubPublisher, LocalPublisher
            if s["github_token"]:
                publisher = GitHubPublisher(s["github_token"], s["graph_repo"], s["log_repo"])
            else:
                publisher = LocalPublisher(self.store_root,
                                           reviews.log_dir(self.store_root, self.store.config))
        self.publisher = publisher

    def reload(self):
        self.store = load_store(self.store_root)
        self.cfg = reviews.settings(self.store.config)
        self.srv = server_settings(self.store.config, self.env)
        self.keys = reviews.load_keys(self.store_root)
        self.records = {r.hash: r for r in reviews.load(self.store_root, self.store.config,
                                                         self.store.entities)}

    # -- routing ------------------------------------------------------------
    def handle(self, method, path, query=None, form=None, cookies=None):
        query, form, cookies = query or {}, form or {}, cookies or {}
        parts = [p for p in path.split("/") if p]
        try:
            if path == "/health":
                return 200, {"Content-Type": "text/plain"}, b"ok"
            if path == "/terms":
                return markdown_page(os.path.join(self.docs, "REVIEW_TERMS.md"), "Reviewer terms")
            if path == "/privacy":
                return markdown_page(os.path.join(self.docs, "PRIVACY.md"), "Privacy notice")
            if path == "/callback" and method == "GET":
                return self.callback(query, cookies)
            if len(parts) == 2 and parts[0] == "review":
                return (self.review_form(parts[1]) if method == "GET"
                        else self.submit_review(parts[1], form))
            if len(parts) == 2 and parts[0] in ("withdraw", "answer"):
                return (self.refer_form(parts[0], parts[1]) if method == "GET"
                        else self.submit_refer(parts[0], parts[1], form))
            if path == "/":
                return page("Reviews", "<h1>Physics Graph reviews</h1><p>Open a result in the "
                            "Physics Graph and choose <b>Review this result</b>.</p>")
            return page("Not found", "<h1>Not found</h1>", 404)
        except _Refusal as exc:
            return page("Not accepted", f"<h1>Not accepted</h1><p class=err>{E(str(exc))}</p>"
                        "<p>Nothing was submitted. Go back to correct it, or start again from the result page.</p>", 400)

    # -- the form -----------------------------------------------------------
    def _entity(self, rid):
        if not ID_RE.fullmatch(rid or ""):
            raise _Refusal("That is not a result id.")
        e = self.store.entities.get(rid)
        if e is None or e.kind == "note":
            raise _Refusal(f"There is no result {rid} in the Physics Graph.")
        return e

    def _result_box(self, e):
        site = self.srv["site_url"]
        link = f"<a href='{E(site)}/#{E(e.id)}'>Open it in the Physics Graph</a>" if site else ""
        one = (e.levels.get("one-liner") or "").strip()
        return (f"<p class=note>{E(e.id)} · version {e.version} · {E(e.status)}</p>"
                f"<h1>{E(e.title)}</h1>{f'<p>{E(one)}</p>' if one else ''}"
                f"<div class=box><b>Statement</b> (LaTeX source; {link or 'the site renders it'})"
                f"<pre>{E((e.levels.get('formal') or '').strip())}</pre></div>")

    def review_form(self, rid):
        e = self._entity(rid)
        fp = reviews.fingerprint(e)
        contact = self.srv["privacy_contact"]
        return page(f"Review {e.title}", self._result_box(e) + f"""
<form method=post action="/review/{E(e.id)}">
<input type=hidden name=version value="{e.version}"><input type=hidden name=fingerprint value="{fp}">
<fieldset><legend>Your verdict</legend>
<label><input type=radio name=verdict value=endorse required> Endorse: I accept what I checked</label>
<label><input type=radio name=verdict value=object> Object: something specific is wrong</label></fieldset>
<fieldset><legend>What you checked</legend>
<label><input type=checkbox name=scope value=statement> The statement is well-formed and says what its title claims</label>
<label><input type=checkbox name=scope value=proof> The proof is correct as written, given the premises it cites</label>
<label><input type=checkbox name=scope value=check> The machine check tests the statement, not a weaker claim</label>
<label><input type=checkbox name=scope value=imports> Results taken from the literature are stated and cited correctly</label></fieldset>
<fieldset><legend>How far you went</legend>
<label><input type=radio name=depth value=read required> Read it</label>
<label><input type=radio name=depth value=line-by-line> Checked it line by line</label></fieldset>
<fieldset><legend>For an objection</legend>
<label>Where: <select name=location><option value="">(choose)</option><option>statement</option><option>check</option><option value=proof>a step of the proof</option></select></label>
<label>Proof step number (if a step of the proof): <input type=text name=step inputmode=numeric></label>
<label>What is wrong (at least 30 characters): <textarea name=defect></textarea></label></fieldset>
<fieldset><legend>About you</legend>
<label>Conflicts of interest ("none" if there are none): <input type=text name=conflicts value="none" required></label>
<label>Note (optional; please leave out personal information): <textarea name=note></textarea></label>
<label>Contact email, for reminders about your own reviews only (never published): <input type=email name=email required></label>
<label><input type=checkbox name=zenodo_credit value=yes> Name me as a contributor on Physics Graph releases on Zenodo (published releases are permanent)</label>
<label><input type=checkbox name=terms value="{TERMS_VERSION}" required> I accept the <a href="/terms">reviewer terms</a> (version {TERMS_VERSION}) and have read the <a href="/privacy">privacy notice</a></label></fieldset>
<p class=note>Next you sign in with ORCID. ORCID signs a fingerprint of exactly what you submit, so the review cannot be changed afterwards by anyone.{(' Privacy questions: ' + E(contact) + '.') if contact else ''}</p>
<button type=submit>Sign in with ORCID to submit</button></form>""")

    def submit_review(self, rid, form):
        e = self._entity(rid)
        g = lambda k: (form.get(k) or [""])[0].strip()
        if g("terms") != str(TERMS_VERSION):
            raise _Refusal("Please accept the reviewer terms.")
        if g("version") != str(e.version) or g("fingerprint") != reviews.fingerprint(e):
            raise _Refusal("This result has changed since the page was opened. Reload the page "
                           "and review the current version.")
        verdict = g("verdict")
        signed = {"kind": "review", "result": e.id, "version": e.version,
                  "fingerprint": reviews.fingerprint(e), "verdict": verdict,
                  "scope": [s for s in form.get("scope", []) if s in reviews.SCOPES],
                  "depth": g("depth"), "conflicts": g("conflicts") or "none",
                  "terms": TERMS_VERSION, "zenodo_credit": g("zenodo_credit") == "yes"}
        if g("note"):
            signed["note"] = g("note")
        if verdict == "object":
            loc = g("location")
            if loc == "proof":
                if not g("step").isdigit() or int(g("step")) < 1:
                    raise _Refusal("Give the number of the proof step.")
                loc = f"proof step {int(g('step'))}"
            signed["location"], signed["defect"] = loc, g("defect")
        return self._start(signed, g("email"))

    def refer_form(self, kind, h):
        target = self._target(kind, h)
        what = ("Withdraw your review" if kind == "withdrawal" or kind == "withdraw"
                else "Answer this objection")
        e = self.store.entities.get(target.result)
        s = target.signed
        summary = (f"{'Objection at ' + E(s.get('location', '')) + ': ' + E(s.get('defect', '')) if s.get('verdict') == 'object' else 'Endorsement of ' + E(', '.join(s.get('scope') or []))}"
                   f" · version {s.get('version')}")
        return page(what, f"""<p class=note>{E(target.result)}</p><h1>{what}</h1>
<div class=box><b>{E(e.title if e else target.result)}</b><p>{summary}</p></div>
<form method=post action="/{E(kind)}/{E(h)}">
<label>{'Reason (optional)' if kind == 'withdraw' else 'Your answer'}: <textarea name=note {'' if kind == 'withdraw' else 'required'}></textarea></label>
<label>Contact email (never published): <input type=email name=email required></label>
<label><input type=checkbox name=terms value="{TERMS_VERSION}" required> I accept the <a href="/terms">reviewer terms</a> (version {TERMS_VERSION})</label>
<p class=note>{'Only the person who made the review can withdraw it: sign in with the same ORCID iD.' if kind == 'withdraw' else 'Only a maintainer can answer: sign in with a maintainer ORCID iD.'}</p>
<button type=submit>Sign in with ORCID to submit</button></form>""")

    def submit_refer(self, kind, h, form):
        target = self._target(kind, h)
        g = lambda k: (form.get(k) or [""])[0].strip()
        if g("terms") != str(TERMS_VERSION):
            raise _Refusal("Please accept the reviewer terms.")
        signed = {"kind": "withdrawal" if kind == "withdraw" else "answer",
                  "result": target.result, "version": target.signed.get("version"),
                  "refers_to": target.hash, "terms": TERMS_VERSION}
        if g("note"):
            signed["note"] = g("note")
        elif kind == "answer":
            raise _Refusal("An answer needs some text.")
        return self._start(signed, g("email"))

    def _target(self, kind, h):
        if kind not in ("withdraw", "answer") or not reviews.HEX64.match(h or ""):
            raise _Refusal("That is not a review record.")
        r = self.records.get(h)
        if r is None or r.kind != "review":
            raise _Refusal("There is no such review in the Physics Graph.")
        if kind == "answer" and r.signed.get("verdict") != "object":
            raise _Refusal("Only an objection can be answered.")
        return r

    # -- sign-in ------------------------------------------------------------
    def _start(self, signed, email):
        rec = reviews.Record("", "", dict(signed))
        reviews._shape(rec, self.cfg)
        if rec.errors:
            raise _Refusal("; ".join(m for _, m, _ in rec.errors))
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email or ""):
            raise _Refusal("Please give a contact email.")
        h = reviews.record_hash(signed)
        state = secrets.token_urlsafe(24)
        with self.lock:
            t = self.now()
            for k in [k for k, v in self.pending.items() if t - v["t"] > PENDING_TTL]:
                del self.pending[k]
            self.pending[state] = {"signed": signed, "hash": h, "email": email, "t": t}
        secure = "; Secure" if self.srv["base_url"].startswith("https://") else ""
        cookie = f"{COOKIE}={state}; Max-Age={PENDING_TTL}; Path=/; HttpOnly; SameSite=Lax{secure}"
        return redirect(self.orcid.authorize_url(state, h), [cookie])

    def callback(self, query, cookies):
        g = lambda k: (query.get(k) or [""])[0]
        if g("error"):
            raise _Refusal(f"ORCID did not sign you in ({g('error')}). Nothing was submitted.")
        state = g("state")
        with self.lock:
            p = self.pending.pop(state, None)
        if p is None or cookies.get(COOKIE) != state:
            raise _Refusal("This sign-in has expired or was started in another browser. "
                           "Nothing was submitted; please start again.")
        if self.now() - p["t"] > PENDING_TTL:
            raise _Refusal("This sign-in has expired. Nothing was submitted; please start again.")
        tok = self.orcid.exchange(g("code"))
        id_token = tok.get("id_token")
        try:
            claims = reviews.verify_token(id_token, self.keys)
        except reviews.TokenError as exc:
            raise _Refusal(f"ORCID's token did not check ({exc}). Nothing was submitted.")
        orcid = claims.get("sub")
        bad = reviews.check_claims(claims, issuers=self.cfg["issuers"],
                                   audiences=self.cfg["client_ids"] or [self.srv["client_id"]],
                                   orcid=orcid, nonce=p["hash"])
        if bad:
            raise _Refusal("ORCID's token did not match this submission: " + "; ".join(bad))
        signed = p["signed"]
        if signed["kind"] == "withdrawal":
            target = self.records.get(signed["refers_to"])
            if target is None or target.orcid != orcid:
                raise _Refusal("Only the person who made a review can withdraw it.")
        if signed["kind"] == "answer" and orcid not in self.cfg["maintainer_orcids"]:
            raise _Refusal("Only a maintainer can answer an objection.")
        name = " ".join(x for x in (claims.get("given_name"), claims.get("family_name")) if x)
        qual = (qualify.check(orcid, self.store.config, fetch=self.fetch)
                if signed["kind"] == "review" else None)
        entry = {"signed": signed, "orcid": orcid, "by": name or tok.get("name") or orcid,
                 "orcid_token": id_token, "qualification": qual,
                 "submitted": datetime.datetime.fromtimestamp(
                     self.now(), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
        out = self.publisher.publish(p["hash"], entry)
        self._keep_contact(p["hash"], orcid, p["email"])
        q = qual or {}
        counts = ("It counts towards the result's trust level: you meet the qualification rule "
                  f"({E(q['route'])})." if q.get("route") else
                  "It is shown, but does not count towards trust: your public ORCID record does "
                  "not meet the qualification rule. You can ask for a person to look at this "
                  "(see the privacy notice).") if signed["kind"] == "review" else ""
        pr = out.get("pull_request")
        return page("Submitted", f"""<h1 class=ok>Submitted</h1>
<p>Your {E(signed['kind'])} of <b>{E(signed['result'])}</b> is sealed by ORCID and is in the open
review log. {counts}</p>
<div class=box><p class=note>Record</p><pre>{E(p['hash'])}</pre>
{f"<p class=note>Pull request: <a href='{E(pr)}'>{E(pr)}</a></p>" if pr else ''}</div>
<p class=note>It shows on the result page once the maintainer merges it; it stays in the open
review log either way.</p>""")

    def _keep_contact(self, h, orcid, email):
        d = self.srv["state_dir"]
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, "contacts.json")
        with self.lock:
            data = {}
            if os.path.exists(p):
                with open(p, encoding="utf-8") as fh:
                    data = json.load(fh)
            data[h] = {"orcid": orcid, "email": email, "since": int(self.now())}
            with open(p, "w", encoding="utf-8") as fh:
                json.dump(data, fh, indent=1)


class _Refusal(ValueError):
    pass


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

def make_handler(service: ReviewService):
    class Handler(BaseHTTPRequestHandler):
        server_version = "physics-graph-review"

        def log_message(self, fmt, *args):     # one line per request, no bodies or queries
            sys.stderr.write("%s %s %s\n" % (self.address_string(), self.command,
                                             self.path.split("?")[0]))

        def _cookies(self):
            out = {}
            for part in (self.headers.get("Cookie") or "").split(";"):
                if "=" in part:
                    k, v = part.strip().split("=", 1)
                    out[k] = v
            return out

        def _reply(self, status, headers, body):
            self.send_response(status)
            for k, v in headers.items():
                for one in (v if isinstance(v, list) else [v]):
                    self.send_header(k, one)
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Referrer-Policy", "no-referrer")
            self.send_header("Content-Security-Policy",
                             "default-src 'none'; style-src 'unsafe-inline'; form-action 'self' "
                             f"{service.srv['orcid_base']}; frame-ancestors 'none'")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            u = urllib.parse.urlsplit(self.path)
            self._reply(*service.handle("GET", u.path, urllib.parse.parse_qs(u.query), None,
                                        self._cookies()))

        def do_POST(self):
            u = urllib.parse.urlsplit(self.path)
            n = int(self.headers.get("Content-Length") or 0)
            if n > MAX_BODY:
                self._reply(*page("Too large", "<h1>Too large</h1>", 413))
                return
            form = urllib.parse.parse_qs(self.rfile.read(n).decode("utf-8", "replace"))
            self._reply(*service.handle("POST", u.path, {}, form, self._cookies()))

    return Handler


def main(argv=None):
    ap = argparse.ArgumentParser(prog="tp.review_server")
    ap.add_argument("--store", default="store")
    ap.add_argument("--host", default=os.environ.get("HOST", "127.0.0.1"))
    ap.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8090")))
    a = ap.parse_args(argv)
    svc = ReviewService(a.store)
    if not svc.srv["client_id"] or not svc.srv["client_secret"]:
        print("TP_ORCID_CLIENT_ID and TP_ORCID_CLIENT_SECRET are required", file=sys.stderr)
        return 1
    httpd = ThreadingHTTPServer((a.host, a.port), make_handler(svc))
    print(f"review service on http://{a.host}:{a.port} (ORCID: {svc.srv['orcid_base']}; "
          f"publishing to {'GitHub' if svc.srv['github_token'] else 'local folders'})",
          file=sys.stderr)
    httpd.serve_forever()


if __name__ == "__main__":
    sys.exit(main())
