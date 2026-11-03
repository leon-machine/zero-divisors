"""Several research programmes side by side in one store (roadmap item 12).

The fixture is given two programmes, the Transport Papers (the default) and
standard physics (one imported Fact), then a third programme is added with its
own subject and entity.  The first programme's files stay untouched and the
store stays clean; an unregistered programme gives E218; the MCP server lists
and filters by programme.  Run:  python -m unittest discover -s tests -t .
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml

from tests.fixture_store import build
from tp import validate as V
from tp.mcp_server import Lab
from tp.model import dump_entity, load_store

E = os.path.join
LAB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REG = {"transport-papers": {"title": "The Transport Papers", "about": "the series",
                            "maintainers": ["leon"]},
       "standard": {"title": "Standard physics", "about": "imported once"}}

NEW_ENTITY = ({"id": "oth.thermo.one-temperature", "kind": "claim", "version": 1,
               "title": "A second programme reads the same temperature",
               "status": "proved", "proposed_by": {"kind": "human", "author": "fixture"},
               "ai_involved": "no", "programme": "other", "subject": "other-thermal",
               "about": ["obj.fock-space"],
               "derivations": [{"name": "direct",
                                "uses": ["fx.qi.kms@1", "fx.witt.car@1"],
                                "proof": "proof-direct.tex"}],
               "checked_by": [{"kind": "proof", "derivation": "direct"}]},
              {"formal": r"One Witt pair in a KMS state is a two-state Gibbs system.",
               "technical": "pending", "lay": "pending",
               "one-liner": "A second programme reads the same temperature"})


def tree_hash(root, skip=("config.yaml", "subjects.yaml")):
    """Hash of every file in the store except the two registries."""
    out = {}
    for d, _, fs in os.walk(root):
        for f in fs:
            p = E(d, f)
            rel = os.path.relpath(p, root)
            if rel not in skip and ".tp-cache" not in rel:
                out[rel] = hashlib.sha256(open(p, "rb").read()).hexdigest()
    return out


class ProgrammeStore(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = build(E(self.tmp, "store"))
        self.config(programmes=REG, default_programme="transport-papers")
        subs = yaml.safe_load(open(E(self.root, "subjects.yaml")))
        for s in subs:
            s["programme"] = "transport-papers"
        subs.append({"id": "std-qft", "title": "Quantum field theory, textbook results",
                     "side": "car", "programme": "standard"})
        yaml.safe_dump(subs, open(E(self.root, "subjects.yaml"), "w"))
        # the imported KMS theorem is standard physics, entered once
        p = E(self.root, "claims", "fx.qi.kms", "entity.md")
        s = open(p).read()
        s = s.replace("subject: thermal", "subject: std-qft\nprogramme: standard", 1)
        open(p, "w").write(s)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def config(self, **kw):
        p = E(self.root, "config.yaml")
        cfg = yaml.safe_load(open(p))
        cfg.update(kw)
        yaml.safe_dump(cfg, open(p, "w"))

    def findings(self):
        rep = V.validate(load_store(self.root), layers=(1, 2, 3), keep_going=True,
                         run_mutants=False)
        return {(f.code, f.severity, f.entity, f.message) for f in rep.findings}

    def errors(self, found):
        return sorted(f for f in found if f[1] == "error")

    def add_second_programme(self):
        cfg = yaml.safe_load(open(E(self.root, "config.yaml")))
        cfg["programmes"]["other"] = {"title": "Another programme", "about": "a second tenant"}
        yaml.safe_dump(cfg, open(E(self.root, "config.yaml"), "w"))
        subs = yaml.safe_load(open(E(self.root, "subjects.yaml")))
        subs.append({"id": "other-thermal", "title": "Another reading of temperature",
                     "side": "car", "programme": "other"})
        yaml.safe_dump(subs, open(E(self.root, "subjects.yaml"), "w"))
        folder = E(self.root, "claims", NEW_ENTITY[0]["id"])
        os.makedirs(folder)
        open(E(folder, "entity.md"), "w").write(dump_entity(*NEW_ENTITY))
        open(E(folder, "proof-direct.tex"), "w").write(
            r"The pair of \claimref{fx.witt.car} is one mode; \claimref{fx.qi.kms} fixes its state.")

    # -------------------------------------------------------------------
    def test_base_store_is_clean(self):
        self.assertEqual(self.errors(self.findings()), [])

    def test_second_programme_added_without_touching_the_first(self):
        before_files, before = tree_hash(self.root), self.findings()
        self.add_second_programme()
        after = self.findings()
        self.assertEqual(self.errors(after), [])
        new = after - before
        self.assertTrue(all(f[2].split("@")[0] == NEW_ENTITY[0]["id"] for f in new), new)
        # nothing of the first programme (or of standard) was edited: only new files appeared
        after_files = tree_hash(self.root)
        self.assertEqual({k: v for k, v in after_files.items() if k in before_files},
                         before_files)
        self.assertEqual(sorted(set(after_files) - set(before_files)),
                         ["claims/oth.thermo.one-temperature/entity.md",
                          "claims/oth.thermo.one-temperature/proof-direct.tex"])
        st = load_store(self.root)
        progs = {eid: V.programme_of(st, e) for eid, e in st.entities.items()}
        self.assertEqual(progs["oth.thermo.one-temperature"], "other")
        self.assertEqual(progs["fx.qi.kms"], "standard")
        self.assertEqual(progs["fx.witt.car"], "transport-papers")

    def test_E218_unregistered_entity_programme(self):
        self.add_second_programme()
        p = E(self.root, "claims", NEW_ENTITY[0]["id"], "entity.md")
        text = open(p).read().replace("programme: other", "programme: nope")
        open(p, "w").write(text)
        e218 = [f for f in self.findings() if f[0] == "E218"]
        self.assertEqual([f[2] for f in e218], ["oth.thermo.one-temperature"])

    def test_E218_unregistered_subject_programme(self):
        subs = yaml.safe_load(open(E(self.root, "subjects.yaml")))
        subs.append({"id": "loose", "title": "Loose", "side": "car", "programme": "nope"})
        yaml.safe_dump(subs, open(E(self.root, "subjects.yaml"), "w"))
        e218 = [f for f in self.findings() if f[0] == "E218"]
        self.assertEqual([f[2] for f in e218], ["subject loose"])

    def test_empty_subject_is_clean(self):
        # a programme's subjects may exist before any entity is filed under them
        self.assertNotIn("std-gr", {e.meta.get("subject")
                                    for e in load_store(self.root).entities.values()})
        subs = yaml.safe_load(open(E(self.root, "subjects.yaml")))
        subs.append({"id": "std-gr", "title": "GR", "side": "metric", "programme": "standard"})
        yaml.safe_dump(subs, open(E(self.root, "subjects.yaml"), "w"))
        self.assertEqual(self.errors(self.findings()), [])

    # MCP ---------------------------------------------------------------
    def test_mcp_lists_and_filters_by_programme(self):
        self.add_second_programme()
        lab = Lab(self.root)
        progs = {p["id"]: p for p in lab.list_programmes()}
        self.assertEqual(sorted(progs), ["other", "standard", "transport-papers"])
        self.assertTrue(progs["transport-papers"]["default"])
        self.assertEqual(progs["transport-papers"]["maintainers"], ["leon"])
        self.assertEqual(progs["standard"]["count"], 1)
        self.assertEqual(progs["standard"]["subjects"], ["std-qft"])
        self.assertEqual(progs["other"]["count"], 1)
        total = lab.list_entities(limit=500)["total"]
        self.assertEqual(progs["transport-papers"]["count"] + 2,
                         len(lab.store.entities))
        std = lab.list_entities(programme="standard", limit=500)
        self.assertEqual([r["id"] for r in std["results"]], ["fx.qi.kms"])
        self.assertEqual(std["results"][0]["programme"], "standard")
        tp = lab.list_entities(programme="transport-papers", limit=500)
        self.assertEqual(tp["total"], total - 2)
        self.assertTrue(all(r["programme"] == "transport-papers" for r in tp["results"]))
        hits = lab.search_claims("KMS Gibbs state", limit=50)
        self.assertIn("fx.qi.kms", [h["id"] for h in hits])
        hits = lab.search_claims("KMS Gibbs state", programme="transport-papers", limit=50)
        self.assertNotIn("fx.qi.kms", [h["id"] for h in hits])
        self.assertTrue(hits)
        self.assertEqual([s["id"] for s in lab.list_subjects(programme="other")],
                         ["other-thermal"])
        self.assertEqual(len(lab.list_subjects()), 4)
        got = lab.get_claims(["oth.thermo.one-temperature"], fields=["programme"])
        self.assertEqual(got, [{"id": "oth.thermo.one-temperature", "programme": "other"}])

    def test_mcp_without_registry_is_backward_compatible(self):
        cfg = yaml.safe_load(open(E(self.root, "config.yaml")))
        cfg.pop("programmes")
        cfg.pop("default_programme")
        yaml.safe_dump(cfg, open(E(self.root, "config.yaml"), "w"))
        lab = Lab(self.root)
        progs = {p["id"]: p for p in lab.list_programmes()}
        self.assertFalse(progs["standard"]["registered"])
        self.assertEqual(lab.list_entities(limit=500)["total"],
                         lab.list_entities(programme=None, limit=500)["total"])

    def test_mcp_stdio_tool(self):
        inp = "\n".join(json.dumps(m) for m in [
            {"jsonrpc": "2.0", "id": 1, "method": "tools/list"},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/call",
             "params": {"name": "list_programmes", "arguments": {}}},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
             "params": {"name": "list_entities", "arguments": {"programme": "standard"}}},
        ]) + "\n"
        cp = subprocess.run([sys.executable, "-m", "tp.mcp_server", "--store", self.root],
                            input=inp, capture_output=True, text=True, cwd=LAB, timeout=120)
        by = {m["id"]: m for m in map(json.loads, cp.stdout.splitlines())}
        tools = {t["name"]: t for t in by[1]["result"]["tools"]}
        self.assertIn("list_programmes", tools)
        for name in ("list_entities", "search_claims", "list_subjects"):
            self.assertIn("programme", tools[name]["inputSchema"]["properties"])
        progs = json.loads(by[2]["result"]["content"][0]["text"])
        self.assertEqual(sorted(p["id"] for p in progs), ["standard", "transport-papers"])
        rows = json.loads(by[3]["result"]["content"][0]["text"])
        self.assertEqual([r["id"] for r in rows["results"]], ["fx.qi.kms"])


if __name__ == "__main__":
    unittest.main()
