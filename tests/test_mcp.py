"""The MCP server speaks JSON-RPC over stdio and its tools work on the fixture."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

from tests.fixture_store import build

LAB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class McpServer(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = build(os.path.join(self.tmp, "store"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def call(self, msgs):
        inp = "\n".join(json.dumps(m) for m in msgs) + "\n"
        cp = subprocess.run([sys.executable, "-m", "tp.mcp_server", "--store", self.root],
                            input=inp, capture_output=True, text=True, cwd=LAB, timeout=120)
        return [json.loads(l) for l in cp.stdout.splitlines() if l.strip()]

    def test_handshake_list_and_calls(self):
        draft = open(os.path.join(self.root, "claims", "fx.parity.grading", "entity.md")).read()
        draft = draft.replace("id: fx.parity.grading", "id: fx.parity.grading-two")
        out = self.call([
            {"jsonrpc": "2.0", "id": 1, "method": "initialize",
             "params": {"protocolVersion": "2024-11-05", "capabilities": {},
                        "clientInfo": {"name": "test", "version": "0"}}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
             "params": {"name": "search_claims", "arguments": {"query": "boost bivector"}}},
            {"jsonrpc": "2.0", "id": 4, "method": "tools/call",
             "params": {"name": "get_claim", "arguments": {"id": "fx.thermo.temperature"}}},
            {"jsonrpc": "2.0", "id": 5, "method": "tools/call",
             "params": {"name": "cone", "arguments": {"id": "fx.thermo.two-state"}}},
            {"jsonrpc": "2.0", "id": 6, "method": "tools/call",
             "params": {"name": "validate_draft",
                        "arguments": {"entity_md": draft.replace("status: proved", "status: maybe")}}},
            {"jsonrpc": "2.0", "id": 7, "method": "tools/call",
             "params": {"name": "propose_claim", "arguments": {
                 "entity_md": draft, "proofs": {"proof-direct.tex": "Generators are odd."}}}},
            {"jsonrpc": "2.0", "id": 8, "method": "tools/call",
             "params": {"name": "nonsense", "arguments": {}}},
        ])
        by = {m["id"]: m for m in out}
        self.assertEqual(len(out), 8)                     # the notification gets no reply
        self.assertEqual(by[1]["result"]["serverInfo"]["name"], "transport-lab")
        names = {t["name"] for t in by[2]["result"]["tools"]}
        self.assertIn("propose_claim", names)
        hits = json.loads(by[3]["result"]["content"][0]["text"])
        self.assertEqual(hits[0]["id"], "fx.boost.sigma")
        got = json.loads(by[4]["result"]["content"][0]["text"])
        self.assertEqual(got["derived"]["holds_given"],
                         ["fx.thermo.period-premise", "fx.transport.principle"])
        cone = {x["id"] for x in json.loads(by[5]["result"]["content"][0]["text"])}
        self.assertIn("fx.null.square-zero", cone)
        v = json.loads(by[6]["result"]["content"][0]["text"])
        self.assertFalse(v["ok"])
        self.assertIn("E105", {f["code"] for f in v["findings"]})
        p = json.loads(by[7]["result"]["content"][0]["text"])
        self.assertTrue(p["accepted_for_review"], p)
        self.assertTrue(by[8]["result"]["isError"])
        # a maintainer accepts the proposal into the store
        cp = subprocess.run([sys.executable, "-m", "tp", "accept", "fx.parity.grading-two",
                             "--store", self.root], capture_output=True, text=True, cwd=LAB)
        self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)
        self.assertTrue(os.path.exists(os.path.join(self.root, "claims", "fx.parity.grading-two")))


if __name__ == "__main__":
    unittest.main()


class McpHardening(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = build(os.path.join(self.tmp, "store"))
        sys.path.insert(0, LAB)
        from tp.mcp_server import Lab
        self.lab = Lab(self.root)
        self.draft = open(os.path.join(self.root, "claims", "fx.parity.grading",
                                       "entity.md")).read()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_path_ids_and_proof_names_are_refused(self):
        victim = os.path.join(self.tmp, "victim")
        os.makedirs(victim)
        open(os.path.join(victim, "keep.txt"), "w").write("x")
        bad = self.draft.replace("id: fx.parity.grading", f"id: {victim}")
        r = self.lab.validate_draft(bad)
        self.assertFalse(r["ok"])
        self.assertTrue(os.path.exists(os.path.join(victim, "keep.txt")))
        good = self.draft.replace("id: fx.parity.grading", "id: fx.parity.grading-two")
        r = self.lab.propose_claim(good, proofs={"../../x.py": "print(1)"})
        self.assertFalse(r["accepted_for_review"])

    def test_layer_four_never_runs_over_mcp(self):
        good = self.draft.replace("id: fx.parity.grading", "id: fx.parity.grading-two")
        r = self.lab.validate_draft(good, check_py="import GA\ndef t():\n    assert 1\n",
                                    layers="4")
        self.assertNotIn(4, r["layers_run"])

    def test_amendment_draft_must_say_what_it_fixes(self):
        from tp.model import load_store, write_lock
        write_lock(load_store(self.root))
        draft = self.draft.replace("version: 1", "version: 2").replace(
            "## formal\n", "## formal\nCorrected: ")
        r = self.lab.validate_draft(draft, proofs={"proof-direct.tex": "Direct.\n"})
        self.assertFalse(r["ok"])
        self.assertIn("E605", {f["code"] for f in r["findings"]})

    def test_document_ids_are_checked(self):
        with self.assertRaises(ValueError):
            self.lab.generate_doc("doc: ../store/config\nspine: []\n")
        with self.assertRaises(ValueError):
            self.lab.regenerate_doc("/etc/passwd")


class McpNavigation(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = build(os.path.join(self.tmp, "store"))
        sys.path.insert(0, LAB)
        from tp.mcp_server import Lab
        self.lab = Lab(self.root)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_neighbourhood_proof_and_digest(self):
        r = self.lab.neighbourhood("fx.boost.sigma")
        self.assertIn("fx.witt.car", [x["id"] for x in r["rests_on"]])
        p = self.lab.get_proof("fx.boost.sigma")
        self.assertTrue(p["proofs"])
        d = self.lab.digest("algebra", "formal")
        self.assertIn("fx.boost.sigma", d)


class McpReading(unittest.TestCase):
    """The tools an AI uses to read: conventions, notation, proofs in steps, search."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = build(os.path.join(self.tmp, "store"))
        open(os.path.join(self.root, "conventions.md"), "w").write("# Conventions\nI4 and I6.")
        sys.path.insert(0, LAB)
        from tp.mcp_server import Lab
        self.lab = Lab(self.root)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_conventions_and_notation(self):
        self.assertIn("I4", self.lab.conventions())
        self.assertEqual(self.lab.notation("Cl"), {"Cl": r"\mathrm{Cl}"})
        with self.assertRaises(ValueError):
            self.lab.notation("nosuch")

    def test_proof_steps_cite_premises(self):
        g = self.lab.get_proof("fx.null.no-inverse")
        steps = g["proofs"]["direct"]["steps"]
        self.assertEqual(len(steps), 1)
        # the fixture proof names no \claimref, so its premise is reported as uncited
        self.assertEqual(g["proofs"]["direct"]["premises_not_cited_in_text"],
                         ["fx.null.square-zero"])

    def test_search_finds_by_title_and_skips_notes(self):
        hits = [h["id"] for h in self.lab.search_claims("null vector inverse")]
        self.assertEqual(hits[0], "fx.null.no-inverse")
        self.assertTrue(all(not h.startswith("note.") for h in hits))

    def test_list_rank_batch_and_empty_query(self):
        r = self.lab.list_entities(sort_by="future_cone_size", limit=3,
                                   fields=["future_cone_size"])
        sizes = [x["future_cone_size"] for x in r["results"]]
        self.assertEqual(sizes, sorted(sizes, reverse=True))
        self.assertEqual(set(r["results"][0]), {"id", "future_cone_size"})
        b = self.lab.get_claims(["fx.null.no-inverse", "nope"], fields=["status"])
        self.assertEqual(b[0], {"id": "fx.null.no-inverse", "status": "proved"})
        self.assertIn("error", b[1])
        listed = self.lab.search_claims("", status="proved", limit=100)
        self.assertTrue(listed and all(x["status"] == "proved" for x in listed))
        with self.assertRaises(ValueError):
            self.lab.list_entities(sort_by="nonsense")


class McpOpenProblems(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = build(os.path.join(self.tmp, "store"))
        open(os.path.join(self.root, "open_problems.yaml"), "w").write(
            "- id: op.a\n  title: A\n  area: algebra\n  kind: research\n  difficulty: tractable\n"
            "  status: open\n  statement: S\n  entities: [fx.boost.sigma]\n"
            "- id: op.b\n  title: B\n  area: algebra\n  kind: housekeeping\n  difficulty: frontier\n"
            "  status: partial\n  statement: T\n  entities: [fx.witt.car]\n")
        sys.path.insert(0, LAB)
        from tp.mcp_server import Lab
        self.lab = Lab(self.root)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_list_and_get(self):
        self.assertEqual(self.lab.list_open_problems()["count"], 2)
        self.assertEqual([p["id"] for p in self.lab.list_open_problems(kind="housekeeping")["problems"]], ["op.b"])
        self.assertEqual([p["id"] for p in self.lab.list_open_problems(entity="fx.boost.sigma")["problems"]], ["op.a"])
        g = self.lab.get_open_problem("op.a")
        self.assertEqual(g["entities"][0]["id"], "fx.boost.sigma")
        with self.assertRaises(ValueError):
            self.lab.get_open_problem("op.none")
