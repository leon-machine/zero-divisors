"""Expert reviews sealed by ORCID (tp/reviews.py, docs/REVIEWS.md).

One case uses a real token: ORCID's sandbox signed the hash of a review of fx.witt.car on
13 November 2026 (tests/fixtures/reviews/sandbox_entry.json), and its key is archived beside
it. The rest sign tokens with a throwaway test key, so forgery, tampering, withdrawal,
objections and the append-only rule can be exercised without a network.

If the fixture store's fx.witt.car changes, the real review becomes stale (its fingerprint no
longer matches): the token still verifies, but the review stops counting. That is the design
working, and the test says so.
"""
import base64
import copy
import hashlib
import json
import os
import shutil
import tempfile
import unittest

import yaml

from tests.fixture_store import build
from tp import reviews as R
from tp.model import load_store
from tp.validate import validate

E = os.path.join
FIX = E(os.path.dirname(os.path.abspath(__file__)), "fixtures", "reviews")
SANDBOX_CLIENT = "APP-JBQS7ZE3L7HN7N4Z"
TEST_ISS = "https://test.orcid.invalid"
ALICE = "0000-0002-1825-0097"
BOB = "0000-0001-5109-3700"
LEON = "0009-0006-4449-5617"


def rd(path, loader=yaml.safe_load):
    with open(path, encoding="utf-8") as fh:
        return loader(fh)


def b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def sign_token(claims: dict) -> str:
    """An RS256 token signed with the throwaway test key."""
    key = rd(E(FIX, "test_key_private.json"), json.load)
    n, d = int(key["n"]), int(key["d"])
    h = b64(json.dumps({"alg": "RS256", "kid": key["kid"]}).encode())
    p = b64(json.dumps(claims).encode())
    k = (n.bit_length() + 7) // 8
    t = R._SHA256_INFO + hashlib.sha256(f"{h}.{p}".encode()).digest()
    em = b"\x00\x01" + b"\xff" * (k - len(t) - 3) + b"\x00" + t
    s = pow(int.from_bytes(em, "big"), d, n).to_bytes(k, "big")
    return f"{h}.{p}.{b64(s)}"


class ReviewCase(unittest.TestCase):
    ENABLED = True

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = build(E(self.tmp, "store"))
        self.log = E(self.tmp, "review-log")
        os.makedirs(E(self.root, R.KEYS_DIR))
        shutil.copy(E(FIX, "sandbox.orcid.org.json"), E(self.root, R.KEYS_DIR))
        shutil.copy(E(FIX, "test_key_public.json"), E(self.root, R.KEYS_DIR))
        cfg = rd(E(self.root, "config.yaml"))
        cfg["reviews"] = {"enabled": self.ENABLED, "log": "../review-log",
                          "orcid": {"issuers": ["https://sandbox.orcid.org", TEST_ISS],
                                    "client_ids": [SANDBOX_CLIENT, "test-client"]},
                          "maintainer_orcids": [LEON], "rule_versions": [1],
                          "terms_versions": [1]}
        with open(E(self.root, "config.yaml"), "w") as fh:
            yaml.safe_dump(cfg, fh)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    # helpers -------------------------------------------------------------
    def store(self):
        return load_store(self.root)

    def put(self, signed, orcid, *, token=None, by="A. Reviewer", qual=None, claims=None):
        """Write a record as the review server would: the signed part into the store, the
        whole entry into the open review log. -> the record's hash."""
        h = R.record_hash(signed)
        if token is None:
            c = {"iss": TEST_ISS, "aud": "test-client", "sub": orcid, "nonce": h,
                 "iat": 1794568941}
            c.update(claims or {})
            token = sign_token(c)
        folder = E(self.root, R.REVIEWS_DIR, signed["result"])
        os.makedirs(folder, exist_ok=True)
        with open(E(folder, h + ".yaml"), "w") as fh:
            yaml.safe_dump(signed, fh, sort_keys=True)
        os.makedirs(E(self.log, "records"), exist_ok=True)
        entry = {"signed": signed, "orcid": orcid, "by": by, "orcid_token": token,
                 "qualification": qual}
        with open(E(self.log, "records", h + ".json"), "w") as fh:
            json.dump(entry, fh)
        return h

    def review(self, eid="fx.witt.car", verdict="endorse", **kw):
        e = self.store().entities[eid]
        s = {"kind": "review", "result": eid, "version": e.version,
             "fingerprint": R.fingerprint(e), "verdict": verdict,
             "scope": ["statement", "proof"], "depth": "line-by-line", "conflicts": "none",
             "terms": 1, "zenodo_credit": False}
        if verdict == "object":
            s.update(location="proof step 2",
                     defect="Step 2 uses associativity of a product not shown to be associative.")
        s.update(kw)
        return s

    def codes(self):
        st = self.store()
        return {c for r in R.load(st.root, st.config, st.entities) for c, _, _ in r.errors}

    def standing(self, eid="fx.witt.car"):
        st = self.store()
        return R.standing(R.load(st.root, st.config, st.entities), st.entities,
                          st.config).get(eid, {})


class Hashing(unittest.TestCase):
    def test_canonical_form_is_sorted_compact_utf8(self):
        self.assertEqual(R.canonical({"b": 1, "a": "é"}), '{"a":"é","b":1}'.encode("utf-8"))

    def test_yaml_round_trip_keeps_the_hash(self):
        s = {"kind": "review", "note": "yes", "conflicts": "none", "terms": 1,
             "zenodo_credit": False, "scope": ["proof"], "version": 3}
        back = yaml.safe_load(yaml.safe_dump(s, sort_keys=True))
        self.assertEqual(R.record_hash(back), R.record_hash(s))


class RealOrcidToken(ReviewCase):
    """The token ORCID's sandbox signed on 13 November 2026."""

    def setUp(self):
        super().setUp()
        self.entry = rd(E(FIX, "sandbox_entry.json"), json.load)

    def add_real(self):
        e = self.entry
        return self.put(e["signed"], e["orcid"], token=e["orcid_token"], by=e["by"],
                        qual=e["qualification"])

    def test_signature_verifies_without_third_party_packages(self):
        claims = R.verify_token(self.entry["orcid_token"], R.load_keys(self.root))
        self.assertEqual(claims["sub"], "0009-0000-4817-5406")
        self.assertEqual(claims["nonce"], R.record_hash(self.entry["signed"]))

    def test_record_checks_and_counts(self):
        self.add_real()
        self.assertEqual(self.codes(), set())
        row = self.standing()
        fresh = self.entry["signed"]["fingerprint"] == R.fingerprint(
            self.store().entities["fx.witt.car"])
        if fresh:
            self.assertEqual(row["trust"], "human-checked")
            self.assertEqual(row["reviews"][0]["state"], "current")
            self.assertEqual(row["reviews"][0]["date"], "2026-11-13")
        else:   # the fixture store changed since the token was signed: the review is stale
            self.assertEqual(row["reviews"][0]["state"], "stale")

    def test_one_changed_character_breaks_the_seal(self):
        e = self.entry
        signed = dict(e["signed"], note=e["signed"]["note"] + "!")
        self.put(signed, e["orcid"], token=e["orcid_token"], by=e["by"])
        self.assertIn("E135", self.codes())

    def test_claiming_someone_elses_id_fails(self):
        e = self.entry
        self.put(e["signed"], ALICE, token=e["orcid_token"], by="Not Them")
        self.assertIn("E135", self.codes())

    def test_tampered_signature_fails(self):
        e = self.entry
        tok = e["orcid_token"]
        bad = tok[:-4] + ("AAAA" if not tok.endswith("AAAA") else "BBBB")
        self.put(e["signed"], e["orcid"], token=bad, by=e["by"])
        self.assertIn("E134", self.codes())

    def test_production_store_rejects_sandbox_tokens(self):
        self.add_real()
        cfg = rd(E(self.root, "config.yaml"))
        cfg["reviews"]["orcid"] = {"issuers": ["https://orcid.org"], "client_ids": []}
        with open(E(self.root, "config.yaml"), "w") as fh:
            yaml.safe_dump(cfg, fh)
        self.assertIn("E135", self.codes())


class Records(ReviewCase):
    def test_endorsement_levels(self):
        self.put(self.review(depth="read"), ALICE, qual={"route": "publications", "rule": 1})
        self.assertEqual(self.standing()["trust"], "human-read")
        self.put(self.review(), BOB, qual=None)            # unqualified: still only human-read
        self.assertEqual(self.standing()["trust"], "human-read")
        self.put(self.review(note="checked again"), ALICE,
                 qual={"route": "publications", "rule": 1})
        self.assertEqual(self.standing()["trust"], "human-checked")
        self.assertEqual(self.codes(), set())

    def test_unknown_rule_version_does_not_qualify(self):
        self.put(self.review(), ALICE, qual={"route": "publications", "rule": 9})
        self.assertEqual(self.standing()["trust"], "human-read")

    def test_qualified_objection_disputes(self):
        self.put(self.review(verdict="object"), BOB, qual=None)
        self.assertFalse(self.standing()["disputed"])
        self.put(self.review(verdict="object", note="second"), ALICE,
                 qual={"route": "employment", "rule": 1})
        self.assertTrue(self.standing()["disputed"])

    def test_withdrawal_by_the_same_person(self):
        h = self.put(self.review(), ALICE, qual={"route": "employment", "rule": 1})
        w = {"kind": "withdrawal", "result": "fx.witt.car", "version": 1, "refers_to": h,
             "terms": 1, "note": "I no longer stand by this."}
        self.put(w, ALICE)
        self.assertEqual(self.codes(), set())
        row = self.standing()
        self.assertIsNone(row["trust"])
        self.assertEqual(row["reviews"][0]["state"], "withdrawn")

    def test_withdrawal_by_someone_else_is_refused(self):
        h = self.put(self.review(), ALICE, qual={"route": "employment", "rule": 1})
        self.put({"kind": "withdrawal", "result": "fx.witt.car", "version": 1,
                  "refers_to": h, "terms": 1}, BOB)
        self.assertIn("E136", self.codes())
        self.assertEqual(self.standing()["trust"], "human-checked")

    def test_answer_must_come_from_a_maintainer(self):
        h = self.put(self.review(verdict="object"), ALICE)
        ans = {"kind": "answer", "result": "fx.witt.car", "version": 1, "refers_to": h,
               "terms": 1, "note": "Associativity is the Clifford product's, shown in T0."}
        self.put(ans, BOB)
        self.assertIn("E137", self.codes())
        shutil.rmtree(E(self.root, R.REVIEWS_DIR))
        h = self.put(self.review(verdict="object"), ALICE)
        self.put(dict(ans, refers_to=h), LEON)
        self.assertEqual(self.codes(), set())

    def test_new_version_makes_reviews_stale(self):
        self.put(self.review(), ALICE, qual={"route": "employment", "rule": 1})
        p = E(self.root, "claims", "fx.witt.car", "entity.md")
        s = rd(p, lambda fh: fh.read()).replace("version: 1", "version: 2", 1)
        with open(p, "w") as fh:
            fh.write(s)
        row = self.standing()
        self.assertIsNone(row["trust"])
        self.assertEqual(row["reviews"][0]["state"], "stale")

    def test_shape_errors(self):
        bad = self.review(verdict="object")
        bad.pop("defect")
        self.put(bad, ALICE)
        self.assertIn("E130", self.codes())

    def test_unknown_result(self):
        s = self.review()
        s["result"] = "fx.no.such"
        self.put(s, ALICE)
        self.assertIn("E132", self.codes())

    def test_file_must_be_named_by_its_hash(self):
        h = self.put(self.review(), ALICE)
        folder = E(self.root, R.REVIEWS_DIR, "fx.witt.car")
        os.rename(E(folder, h + ".yaml"), E(folder, "0" * 64 + ".yaml"))
        self.assertIn("E131", self.codes())

    def test_record_without_log_entry(self):
        h = self.put(self.review(), ALICE)
        os.remove(E(self.log, "records", h + ".json"))
        self.assertIn("E133", self.codes())

    def test_unknown_key_and_wrong_audience(self):
        s = self.review()
        h = R.record_hash(s)
        tok = sign_token({"iss": TEST_ISS, "aud": "someone-else", "sub": ALICE, "nonce": h})
        self.put(s, ALICE, token=tok)
        self.assertIn("E135", self.codes())


class AppendOnly(ReviewCase):
    def test_accepted_records_cannot_change_or_go(self):
        h = self.put(self.review(), ALICE)
        R.write_lock(self.root)
        self.assertEqual(R.append_only(self.root), [])
        path = E(self.root, R.REVIEWS_DIR, "fx.witt.car", h + ".yaml")
        with open(path, "a") as fh:
            fh.write("# edited\n")
        self.assertEqual(len(R.append_only(self.root)), 1)
        os.remove(path)
        rep = validate(self.store(), layers=(1,), keep_going=True)
        self.assertIn("E138", {f.code for f in rep.findings})

    def test_redaction_is_the_one_exception(self):
        h = self.put(self.review(), ALICE)
        R.write_lock(self.root)
        os.remove(E(self.root, R.REVIEWS_DIR, "fx.witt.car", h + ".yaml"))
        with open(E(self.root, R.REVIEWS_DIR, R.REDACTIONS), "w") as fh:
            yaml.safe_dump([{"hash": h, "what": "identity", "date": "2026-12-01",
                             "reason": "identity removed on request"}], fh)
        self.assertEqual(R.append_only(self.root), [])

    def test_identity_removed_in_the_log(self):
        h = self.put(self.review(), ALICE, qual={"route": "employment", "rule": 1})
        p = E(self.log, "records", h + ".json")
        entry = rd(p, json.load)
        with open(p, "w") as fh:
            json.dump({"signed": entry["signed"], "removed": {"date": "2026-12-01"}}, fh)
        row = self.standing()
        self.assertEqual(row["reviews"][0]["state"], "removed")
        self.assertNotIn("orcid", row["reviews"][0])
        self.assertIsNone(row["trust"])
        self.assertEqual(self.codes(), set())


class Validator(ReviewCase):
    def test_review_findings_reach_the_validator(self):
        bad = self.review(verdict="object")
        bad.pop("location")
        self.put(bad, ALICE)
        rep = validate(self.store(), layers=(1,), keep_going=True)
        self.assertIn("E130", {f.code for f in rep.findings})

    def test_clean_store_with_a_review(self):
        self.put(self.review(), ALICE, qual={"route": "employment", "rule": 1})
        rep = validate(self.store(), layers=(1,), keep_going=True)
        self.assertFalse({f.code for f in rep.findings} & {f"E13{i}" for i in range(9)})


class Switch(ReviewCase):
    """With reviews.enabled false nothing about reviews reaches MCP or the site's data."""
    ENABLED = False

    def lab(self):
        from tp.mcp_server import Lab
        return Lab(self.root)

    def test_hidden_when_switched_off(self):
        self.put(self.review(), ALICE, qual={"route": "employment", "rule": 1})
        d = self.lab().get_claim("fx.witt.car")["derived"]
        self.assertNotIn("reviews", d)
        self.assertNotIn("disputed", d)
        # still validated
        self.assertEqual(self.codes(), set())

    def test_shown_when_switched_on(self):
        self.put(self.review(), ALICE, qual={"route": "employment", "rule": 1})
        cfg = rd(E(self.root, "config.yaml"))
        cfg["reviews"]["enabled"] = True
        with open(E(self.root, "config.yaml"), "w") as fh:
            yaml.safe_dump(cfg, fh)
        d = self.lab().get_claim("fx.witt.car")["derived"]
        self.assertEqual(d["trust"], "human-checked")
        self.assertEqual(d["reviews"][0]["orcid"], ALICE)


if __name__ == "__main__":
    unittest.main()
