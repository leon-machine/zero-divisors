"""The review service end to end, against a fake ORCID that signs tokens with the test key
(tests/fixtures/reviews), and recorded ORCID and OpenAlex responses for the qualification check.
What it writes must pass tp.reviews' own checks: the same rules CI applies."""
import json
import os
import shutil
import tempfile
import threading
import unittest
import urllib.parse
import urllib.request

import yaml

from tests.fixture_store import build
from tests.test_reviews import ALICE, BOB, LEON, TEST_ISS, FIX, rd, sign_token
from tp import qualify, reviews as R
from tp.review_publish import GitHubPublisher, LocalPublisher
from tp.review_server import COOKIE, ReviewService, make_handler

E = os.path.join
DOCS = E(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
CLIENT = "test-client"


class FakeOrcid:
    """Hands out a code per sign-in and returns a token for it, as ORCID would."""

    def __init__(self):
        self.who, self.nonce_override, self.started = ALICE, None, {}

    def authorize_url(self, state, nonce):
        self.started[state] = nonce
        return "https://orcid.test/oauth/authorize?" + urllib.parse.urlencode(
            {"state": state, "nonce": nonce, "client_id": CLIENT})

    def exchange(self, code):
        nonce = self.nonce_override or self.started[code]
        return {"id_token": sign_token({"iss": TEST_ISS, "aud": CLIENT, "sub": self.who,
                                        "nonce": nonce, "iat": 1794568941,
                                        "given_name": "Ada", "family_name": "Reviewer"})}


def works_for(orcid, dois, client=True):
    src = ({"source-client-id": {"path": "0000-0002-3054-1567"}, "source-orcid": None,
            "source-name": {"value": "Crossref"}} if client else
           {"source-client-id": None, "source-orcid": {"path": orcid}})
    return {"group": [{"external-ids": {"external-id": [
        {"external-id-type": "doi", "external-id-value": d, "external-id-relationship": "self"}]},
        "work-summary": [{"source": src, "type": "journal-article"}]} for d in dois]}


def openalex(subfield, authors):
    return {"primary_topic": {"subfield": {"id": f"https://openalex.org/subfields/{subfield}",
                                           "display_name": "Mathematical Physics"}},
            "authorships": [{"author": {"orcid": f"https://orcid.org/{a}"}} for a in authors]}


class Fetch:
    """Recorded responses by URL; anything unrecorded is a 404 (None)."""

    def __init__(self):
        self.pages = {}

    def __call__(self, url):
        return self.pages.get(url.split("?")[0])

    def publications(self, orcid, n=3, subfield=2610, author=True, client=True):
        dois = [f"10.1234/test.{i}" for i in range(n)]
        self.pages[f"https://pub.orcid.org/v3.0/{orcid}/works"] = works_for(orcid, dois, client)
        for d in dois:
            self.pages[f"https://api.openalex.org/works/doi:{urllib.parse.quote(d)}"] = \
                openalex(subfield, [orcid] if author else ["0000-0000-0000-0000"])


class ServiceCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = build(E(self.tmp, "store"))
        self.log = E(self.tmp, "review-log")
        os.makedirs(E(self.root, R.KEYS_DIR))
        shutil.copy(E(FIX, "test_key_public.json"), E(self.root, R.KEYS_DIR))
        cfg = rd(E(self.root, "config.yaml"))
        cfg["reviews"] = {"enabled": True, "log": "../review-log",
                          "orcid": {"issuers": [TEST_ISS], "client_ids": [CLIENT]},
                          "maintainer_orcids": [LEON], "rule_versions": [1], "terms_versions": [1],
                          "server": {"base_url": "https://review.test"}}
        with open(E(self.root, "config.yaml"), "w") as fh:
            yaml.safe_dump(cfg, fh)
        self.orcid, self.fetch = FakeOrcid(), Fetch()
        self.env = {"TP_REVIEW_STATE": E(self.tmp, "state")}
        self.svc = self.service()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def service(self):
        return ReviewService(self.root, orcid=self.orcid, fetch=self.fetch, env=self.env,
                             publisher=LocalPublisher(self.root, self.log), docs_dir=DOCS)

    # one submission, as a browser would make it --------------------------
    def form(self, eid="fx.witt.car", **kw):
        e = self.svc.store.entities[eid]
        f = {"version": [str(e.version)], "fingerprint": [R.fingerprint(e)],
             "verdict": ["endorse"], "scope": ["statement", "proof"], "depth": ["line-by-line"],
             "conflicts": ["none"], "email": ["ada@example.org"], "terms": ["1"]}
        f.update({k: v if isinstance(v, list) else [v] for k, v in kw.items()})
        return f

    def start(self, path, form):
        status, headers, body = self.svc.handle("POST", path, form=form)
        self.assertEqual(status, 303, body.decode()[:400])
        q = urllib.parse.parse_qs(urllib.parse.urlsplit(headers["Location"]).query)
        cookie = headers["Set-Cookie"][0].split(";")[0].split("=", 1)[1]
        return q["state"][0], q["nonce"][0], cookie

    def finish(self, state, cookie):
        return self.svc.handle("GET", "/callback", query={"code": [state], "state": [state]},
                               cookies={COOKIE: cookie})

    def submit(self, path="/review/fx.witt.car", form=None):
        state, nonce, cookie = self.start(path, form or self.form())
        status, _, body = self.finish(state, cookie)
        return status, body.decode(), nonce

    def checked(self):
        st = R.load(self.root, rd(E(self.root, "config.yaml")),
                    __import__("tp.model", fromlist=["load_store"]).load_store(self.root).entities)
        return {c for r in st for c, _, _ in r.errors}, st


class Submitting(ServiceCase):
    def test_form_page(self):
        status, _, body = self.svc.handle("GET", "/review/fx.witt.car")
        self.assertEqual(status, 200)
        self.assertIn(R.fingerprint(self.svc.store.entities["fx.witt.car"]), body.decode())
        self.assertIn("Sign in with ORCID to submit", body.decode())

    def test_review_is_sealed_qualified_and_recorded(self):
        self.fetch.publications(ALICE)
        status, body, nonce = self.submit()
        self.assertEqual(status, 200, body)
        self.assertIn("It counts towards the result", body)
        codes, recs = self.checked()
        self.assertEqual(codes, set())
        self.assertEqual(recs[0].hash, nonce)       # ORCID sealed exactly what was stored
        st = __import__("tp.model", fromlist=["load_store"]).load_store(self.root)
        row = R.standing(recs, st.entities, st.config)["fx.witt.car"]
        self.assertEqual(row["trust"], "human-checked")
        entry = rd(E(self.log, "records", nonce + ".json"), json.load)
        self.assertEqual(entry["by"], "Ada Reviewer")
        self.assertEqual(entry["qualification"]["route"], "publications")
        self.assertNotIn("email", json.dumps(entry))         # the email never reaches the log
        contacts = rd(E(self.tmp, "state", "contacts.json"), json.load)
        self.assertEqual(contacts[nonce]["email"], "ada@example.org")

    def test_unqualified_reviewer_is_recorded_but_does_not_count(self):
        self.fetch.publications(ALICE, author=False)      # someone else's papers linked
        status, body, _ = self.submit()
        self.assertIn("does not count towards trust", body)
        codes, recs = self.checked()
        self.assertEqual(codes, set())
        self.assertIsNone(recs[0].attached["qualification"]["route"])

    def test_objection_needs_location_and_defect(self):
        status, _, body = self.svc.handle("POST", "/review/fx.witt.car",
                                          form=self.form(verdict="object"))
        self.assertEqual(status, 400)
        f = self.form(verdict="object", location="proof", step="2",
                      defect="Step 2 uses associativity of a product not shown to be associative.")
        status, body, _ = self.submit(form=f)
        self.assertEqual(status, 200, body)
        codes, recs = self.checked()
        self.assertEqual(recs[0].signed["location"], "proof step 2")

    def test_changed_result_is_refused(self):
        status, _, body = self.svc.handle("POST", "/review/fx.witt.car",
                                          form=self.form(fingerprint="0" * 64))
        self.assertEqual(status, 400)
        self.assertIn("changed since the page was opened", body.decode())

    def test_terms_must_be_accepted(self):
        status, _, _ = self.svc.handle("POST", "/review/fx.witt.car", form=self.form(terms=""))
        self.assertEqual(status, 400)


class SignIn(ServiceCase):
    def test_other_browser_is_refused(self):
        state, _, cookie = self.start("/review/fx.witt.car", self.form())
        status, _, body = self.svc.handle("GET", "/callback",
                                          query={"code": [state], "state": [state]}, cookies={})
        self.assertEqual(status, 400)
        self.assertFalse(os.path.isdir(E(self.log, "records")))

    def test_token_for_something_else_is_refused(self):
        self.orcid.nonce_override = "f" * 64
        status, body, _ = self.submit()
        self.assertEqual(status, 400)
        self.assertIn("did not match", body)
        self.assertFalse(os.path.isdir(E(self.log, "records")))

    def test_state_is_used_once(self):
        state, _, cookie = self.start("/review/fx.witt.car", self.form())
        self.assertEqual(self.finish(state, cookie)[0], 200)
        self.assertEqual(self.finish(state, cookie)[0], 400)


class Withdrawing(ServiceCase):
    def published(self):
        _, _, h = self.submit()
        self.svc = self.service()               # the server is redeployed after the merge
        return h

    def test_withdrawal_by_the_reviewer(self):
        h = self.published()
        self.assertEqual(self.svc.handle("GET", f"/withdraw/{h}")[0], 200)
        status, body, _ = self.submit(f"/withdraw/{h}",
                                      {"terms": ["1"], "email": ["ada@example.org"],
                                       "note": ["Changed my mind."]})
        self.assertEqual(status, 200, body)
        codes, recs = self.checked()
        self.assertEqual(codes, set())
        st = __import__("tp.model", fromlist=["load_store"]).load_store(self.root)
        row = R.standing(recs, st.entities, st.config)["fx.witt.car"]
        self.assertEqual(row["reviews"][0]["state"], "withdrawn")

    def test_withdrawal_by_someone_else_is_refused(self):
        h = self.published()
        self.orcid.who = BOB
        status, body, _ = self.submit(f"/withdraw/{h}", {"terms": ["1"],
                                                         "email": ["bob@example.org"]})
        self.assertEqual(status, 400)
        self.assertIn("Only the person who made a review", body)

    def test_answers_come_from_a_maintainer(self):
        f = self.form(verdict="object", location="statement",
                      defect="The statement omits the condition that v is null.")
        _, _, h = self.submit(form=f)
        self.svc = self.service()
        form = {"terms": ["1"], "email": ["x@example.org"], "note": ["v is null by definition."]}
        status, body, _ = self.submit(f"/answer/{h}", form)
        self.assertEqual(status, 400)
        self.orcid.who = LEON
        status, body, _ = self.submit(f"/answer/{h}", form)
        self.assertEqual(status, 200, body)
        self.assertEqual(self.checked()[0], set())


class Qualification(unittest.TestCase):
    def test_employment_asserted_by_an_organisation(self):
        emp = {"affiliation-group": [{"summaries": [{"employment-summary": {
            "end-date": None, "organization": {"name": "University X"}, "role-title": "Professor",
            "source": {"source-client-id": {"path": "APP-UNIX"},
                       "source-name": {"value": "University X"}, "source-orcid": None}}}]}]}
        f = Fetch()
        f.pages[f"https://pub.orcid.org/v3.0/{ALICE}/employments"] = emp
        q = qualify.check(ALICE, {}, fetch=f)
        self.assertEqual((q["route"], q["evidence"]["employment"]["organisation"]),
                         ("employment", "University X"))

    def test_self_typed_employment_and_works_do_not_count(self):
        emp = {"affiliation-group": [{"summaries": [{"employment-summary": {
            "end-date": None, "organization": {"name": "University X"},
            "source": {"source-client-id": None, "source-orcid": {"path": ALICE}}}}]}]}
        f = Fetch()
        f.pages[f"https://pub.orcid.org/v3.0/{ALICE}/employments"] = emp
        f.publications(ALICE, client=False)
        self.assertIsNone(qualify.check(ALICE, {}, fetch=f)["route"])

    def test_subject_and_count(self):
        f = Fetch()
        f.publications(ALICE, subfield=1311)          # a subfield outside the rule
        self.assertIsNone(qualify.check(ALICE, {}, fetch=f)["route"])
        f.publications(ALICE, n=2)
        self.assertIsNone(qualify.check(ALICE, {}, fetch=f)["route"])
        f.publications(ALICE, n=3)
        self.assertEqual(qualify.check(ALICE, {}, fetch=f)["route"], "publications")

    def test_invitation(self):
        cfg = {"reviews": {"qualification": {"invited": [BOB]}}}
        self.assertEqual(qualify.check(BOB, cfg, fetch=Fetch())["route"], "invitation")


class Pages(ServiceCase):
    def test_terms_and_privacy(self):
        for path, word in (("/terms", "Reviewer terms"), ("/privacy", "legitimate interests")):
            status, _, body = self.svc.handle("GET", path)
            self.assertEqual(status, 200)
            self.assertIn(word, body.decode())
            self.assertNotIn("<script", body.decode())

    def test_unknown_result(self):
        self.assertEqual(self.svc.handle("GET", "/review/fx.no.such")[0], 400)
        self.assertEqual(self.svc.handle("GET", "/review/<script>")[0], 400)

    def test_over_http(self):
        from http.server import ThreadingHTTPServer
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(self.svc))
        t = threading.Thread(target=httpd.serve_forever, daemon=True)
        t.start()
        try:
            port = httpd.server_address[1]
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/health") as r:
                self.assertEqual(r.read(), b"ok")
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/review/fx.witt.car") as r:
                self.assertIn("frame-ancestors 'none'", r.headers["Content-Security-Policy"])
        finally:
            httpd.shutdown()
            httpd.server_close()


class GitHubPublishing(unittest.TestCase):
    def test_log_first_then_pull_request(self):
        calls = []

        class Resp:
            def __init__(self, data):
                self.data = json.dumps(data).encode()

            def read(self):
                return self.data

            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

        def opener(req, timeout=None):
            calls.append((req.get_method(), req.full_url.split("api.github.com")[1]))
            if req.full_url.endswith("/git/ref/heads/main"):
                return Resp({"object": {"sha": "abc"}})
            if req.full_url.endswith("/pulls"):
                return Resp({"html_url": "https://github.com/o/g/pull/9"})
            return Resp({"content": {"html_url": "https://github.com/o/l/blob/main/x"}})

        p = GitHubPublisher("t", "o/g", "o/l", opener=opener)
        signed = {"kind": "review", "result": "fx.witt.car", "version": 1, "verdict": "endorse"}
        out = p.publish("a" * 64, {"signed": signed, "by": "Ada"})
        self.assertEqual(calls[0], ("PUT", f"/repos/o/l/contents/records/{'a' * 64}.json"))
        self.assertEqual(calls[-1], ("POST", "/repos/o/g/pulls"))
        self.assertEqual(out["pull_request"], "https://github.com/o/g/pull/9")


if __name__ == "__main__":
    unittest.main()
