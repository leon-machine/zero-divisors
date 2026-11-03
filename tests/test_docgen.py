"""Document generation, storage and regeneration from the stored version."""
import json
import os
import shutil
import tempfile
import unittest

import yaml

from tests.fixture_store import build
from tp import docgen

E = os.path.join

RECIPE = {
    "doc": "thermometer", "title": "The thermometer", "level": "technical",
    "spine": ["fx.thermo.two-state", "fx.thermo.temperature"],
    "include": {"assumptions": "always", "refutations": "in-cone",
                "predictions": "in-cone"},
    "budget": {"abstract_words": [3, 250]},
}


class DocCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = build(E(self.tmp, "store"))
        self.recipe_path = E(self.tmp, "recipe.yaml")
        yaml.safe_dump(RECIPE, open(self.recipe_path, "w"))
        self.doc = docgen.generate(self.root, self.recipe_path)
        self.folder = self.doc["folder"]

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def blocks(self):
        return json.load(open(E(self.folder, "blocks.json")))

    def edit(self, eid, old, new):
        for sub in ("claims", "objects", "predictions"):
            p = E(self.root, sub, eid, "entity.md")
            if os.path.exists(p):
                s = open(p).read()
                self.assertIn(old, s)
                open(p, "w").write(s.replace(old, new, 1))
                return
        raise KeyError(eid)


class Generation(DocCase):
    def test_selection_and_order(self):
        sel = self.doc["selection"]
        order = sel["order"]
        # premises before dependants
        self.assertLess(order.index("fx.null.square-zero"), order.index("fx.null.no-inverse"))
        self.assertLess(order.index("fx.witt.car"), order.index("fx.boost.sigma"))
        self.assertEqual(order[-1], "fx.thermo.temperature")
        # postulates always surface; imported results are cited, not shown
        self.assertEqual(sel["assumed"], ["fx.thermo.period-premise", "fx.transport.principle"])
        self.assertEqual(sel["cited"], ["fx.qi.kms"])
        # refutation and prediction in the cone are pulled in
        self.assertIn("fx.old.shadow", sel["refutations"])
        self.assertIn("fx.pred.single-temperature", sel["predictions"])

    def test_blocks_and_files(self):
        types = {b["type"] for b in self.blocks()}
        self.assertTrue({"theorem", "fact", "postulate", "refutation", "prediction",
                         "transition", "abstract"} <= types)
        for f in ("recipe.yaml", "blocks.json", "manifest.json", "rendered.tex",
                  "rendered.md", "audit.json", "overrides.json", "changelog.md",
                  "verify_thermometer.py", "versions/v1/blocks.json"):
            self.assertTrue(os.path.exists(E(self.folder, f)), f)
        man = json.load(open(E(self.folder, "manifest.json")))
        self.assertIn("fx.witt.car@1", man["claims"])

    def test_formal_level_carries_proofs(self):
        r = dict(RECIPE, doc="thermometer-formal", level="formal")
        p = E(self.tmp, "r2.yaml")
        yaml.safe_dump(r, open(p, "w"))
        d = docgen.generate(self.root, p)
        bl = json.load(open(E(d["folder"], "blocks.json")))
        thm = next(b for b in bl if b["id"] == "c:fx.null.no-inverse")
        self.assertIn("contradiction", thm["proof"])

    def test_notes_follow_the_result_they_discuss(self):
        from tests.test_validator import NOTE
        d = E(self.root, "notes", "note.fx.remark")
        os.makedirs(d)
        open(E(d, "entity.md"), "w").write(
            NOTE.format(id="note.fx.remark", status="remark", on="fx.null.no-inverse"))
        yaml.safe_dump({"T0:rem:x": {"entity": "note.fx.remark"}},
                       open(E(self.root, "labels.yaml"), "w"))
        r = dict(RECIPE, doc="thermometer-notes", level="formal",
                 include=dict(RECIPE["include"], notes="attached"))
        p = E(self.tmp, "r3.yaml")
        yaml.safe_dump(r, open(p, "w"))
        dd = docgen.generate(self.root, p)
        ids = [b["id"] for b in json.load(open(E(dd["folder"], "blocks.json")))]
        self.assertIn("c:note.fx.remark", ids)
        self.assertEqual(ids.index("c:note.fx.remark"), ids.index("c:fx.null.no-inverse") + 1)
        tex = open(E(dd["folder"], "rendered.tex")).read()
        self.assertIn(r"\begin{remark}\label{c:note.fx.remark}", tex.replace("[A remark on the null vector]", ""))

    def test_audit_pending_levels_are_gaps(self):
        codes = {f["code"] for f in self.doc["audit"]}
        self.assertIn("D107", codes)       # fixture technical levels are pending


class Regeneration(DocCase):
    def test_no_change_no_version(self):
        r = docgen.regenerate(self.root, "thermometer")
        self.assertEqual(r["bump"], "none")

    def test_cosmetic_change_is_a_patch_and_freezes_the_rest(self):
        before = {b["id"]: json.dumps(b, sort_keys=True) for b in self.blocks()}
        self.edit("fx.witt.car", "## technical\npending",
                  "## technical\nTwo null directions pair into one fermionic mode.")
        r = docgen.regenerate(self.root, "thermometer")
        self.assertEqual(r["bump"], "patch")
        after = {b["id"]: json.dumps(b, sort_keys=True) for b in self.blocks()}
        changed = {i for i in after if before.get(i) != after[i]}
        self.assertIn("c:fx.witt.car", changed)
        untouched = [i for i in after if i.startswith("c:") and i != "c:fx.witt.car"]
        for i in untouched:
            self.assertEqual(before[i], after[i], i)
        self.assertTrue(os.path.exists(E(self.folder, "versions/v2/redline.diff")))

    def test_substantive_spine_change_is_major(self):
        self.edit("fx.thermo.two-state", "version: 1", "version: 2")
        self.edit("fx.thermo.temperature", "fx.thermo.two-state@1", "fx.thermo.two-state@2")
        self.edit("fx.thermo.temperature", "version: 1", "version: 2")
        r = docgen.regenerate(self.root, "thermometer")
        self.assertEqual(r["bump"], "major")
        self.assertEqual(r["version"], 2)

    def test_added_claim_is_placed_after_its_premises(self):
        # sigma-square enters the cone: the two-state claim now also uses it
        self.edit("fx.thermo.two-state", "  - fx.qi.kms@1",
                  "  - fx.qi.kms@1\n  - fx.boost.sigma-square@1")
        self.edit("fx.thermo.two-state", "version: 1", "version: 2")
        r = docgen.regenerate(self.root, "thermometer")
        self.assertEqual(r["classes"]["fx.boost.sigma-square"], "added")
        ids = [b["id"] for b in self.blocks()]
        self.assertLess(ids.index("c:fx.boost.sigma"), ids.index("c:fx.boost.sigma-square"))
        self.assertLess(ids.index("c:fx.boost.sigma-square"), ids.index("c:fx.thermo.two-state"))

    def test_imported_result_named_in_spine_moves_into_the_body(self):
        # fx.qi.kms was cited; naming it in the spine shows it, before its first use
        rec = dict(RECIPE, spine=["fx.qi.kms"] + RECIPE["spine"])
        r = docgen.regenerate(self.root, "thermometer", recipe=rec)
        ids = [b["id"] for b in self.blocks()]
        self.assertLess(ids.index("c:fx.qi.kms"), ids.index("s:cited") if "s:cited" in ids
                        else len(ids))
        self.assertLess(ids.index("c:fx.qi.kms"), ids.index("c:fx.thermo.two-state"))
        self.assertTrue(any("c:fx.qi.kms: moved" in line for line in r["changelog"]))

    def test_bibliography_from_the_registry(self):
        yaml.safe_dump({"KMS1959": {"latex": "R. Kubo, J. Phys. Soc. Japan 12 (1957)."}},
                       open(E(self.root, "references.yaml"), "w"))
        from tp.model import load_store
        st = load_store(self.root)
        out = docgen._bibliography(st, r"see \cite{KMS1959} and \cite[p.~2]{Missing}")
        self.assertIn(r"\bibitem{KMS1959} R. Kubo", "\n".join(out))
        self.assertIn("Missing", "\n".join(out))

    def test_removed_claim_is_major_and_logged(self):
        self.edit("fx.boost.sigma", "  uses:\n  - fx.witt.car@1\n", "")
        self.edit("fx.boost.sigma", "version: 1", "version: 2")
        r = docgen.regenerate(self.root, "thermometer")
        self.assertEqual(r["classes"]["fx.witt.car"], "removed")
        self.assertEqual(r["bump"], "major")
        self.assertNotIn("c:fx.witt.car", [b["id"] for b in self.blocks()])
        self.assertTrue(any("fx.witt.car" in c and "removed" in c for c in r["changelog"]))

    def test_override_survives_when_inputs_unchanged(self):
        docgen.set_override(self.root, "thermometer", "c:fx.witt.car", "My own wording.")
        self.edit("fx.boost.sigma-square", "## lay\npending", "## lay\nIt squares to one.")
        self.edit("fx.boost.sigma", "## technical\npending", "## technical\nA commutator.")
        r = docgen.regenerate(self.root, "thermometer")
        b = next(x for x in self.blocks() if x["id"] == "c:fx.witt.car")
        self.assertEqual(b["text"], "My own wording.")
        self.assertNotIn("conflict", b)
        self.assertEqual(r["conflicts"], [])

    def test_override_conflicts_when_inputs_change(self):
        docgen.set_override(self.root, "thermometer", "c:fx.witt.car", "My own wording.")
        self.edit("fx.witt.car", "## technical\npending", "## technical\nNew text.")
        r = docgen.regenerate(self.root, "thermometer")
        self.assertEqual(r["conflicts"], ["c:fx.witt.car"])
        b = next(x for x in self.blocks() if x["id"] == "c:fx.witt.car")
        self.assertEqual(b["text"], "My own wording.")
        self.assertEqual(b["conflict"]["generated"], "New text.")

    def test_refuted_claim_kept_as_refutation(self):
        self.edit("fx.boost.sigma-square", "status: proved", "status: refuted")
        self.edit("fx.boost.sigma-square", "version: 1",
                  "version: 2\nrefuted_by:\n- fx.boost.sigma")
        self.edit("fx.thermo.two-state", "  - fx.qi.kms@1",
                  "  - fx.qi.kms@1\n  - fx.boost.sigma-square@2")
        self.edit("fx.thermo.two-state", "version: 1", "version: 2")
        r = docgen.regenerate(self.root, "thermometer")
        b = next(x for x in self.blocks() if x["id"] == "c:fx.boost.sigma-square")
        self.assertEqual(b["type"], "refutation")


class ProseAudit(DocCase):
    def test_sentence_split_catches_untagged_sentences_in_a_tagged_paragraph(self):
        sents = docgen.split_sentences(
            "First fact here. Second fact here. [[c:fx.witt.car]] Then a link. [[t]]")
        self.assertEqual(len(sents), 3)
        self.assertFalse(docgen.TAG_RE.search(sents[0]))
        self.assertTrue(sents[1].endswith("[[c:fx.witt.car]]"))

    def test_prose_tags_and_numbers(self):
        prose = {"abstract": "A two-state system sets the temperature. [[c:fx.thermo.two-state]]",
                 "introduction": "Untagged sentence here.",
                 "t:^>fx.null.square-zero": "There are 7 steps. [[t]]",
                 "conclusion": "The period is 42 units. [[c:fx.thermo.temperature]]"}
        json.dump(prose, open(E(self.folder, "prose.json"), "w"))
        self.edit("fx.witt.car", "## technical\npending", "## technical\nNew.")
        r = docgen.regenerate(self.root, "thermometer")
        codes = {f["code"] for f in r["audit"]}
        self.assertTrue({"D101", "D103", "D104"} <= codes, codes)


if __name__ == "__main__":
    unittest.main()


class Settings(unittest.TestCase):
    """The running text of a paper becomes setting notes."""

    def test_spans_and_cleaning(self):
        from tp import settings
        body = r"Intro $x$ \begin{theorem}A\begin{theorem}B\end{theorem}\end{theorem} tail"
        sp = settings._spans(body, ["theorem"])
        self.assertEqual(len(sp), 1)                      # outermost only
        self.assertTrue(body[sp[0][0]:sp[0][1]].endswith(r"\end{theorem}\end{theorem}"))
        t = settings._clean(r"See \href{http://x}{the site}\label{a} and \verb|a_b| on page \pageref{t}.")
        self.assertEqual(t, r"See the site and \texttt{a\_b}.")   # "on page N" is dropped

    def test_paper_prose_takes_the_abstract_verbatim(self):
        import tempfile, shutil
        from tests.fixture_store import build
        tmp = tempfile.mkdtemp()
        try:
            root = build(E(tmp, "store"))
            d = E(root, "notes", "note.fx.abstract")
            os.makedirs(d)
            open(E(d, "entity.md"), "w").write(
                "---\nid: note.fx.abstract\nkind: note\nversion: 1\ntitle: Abstract\n"
                "status: setting\nsubject: algebra\nproposed_by: {kind: human, author: fixture}\n"
                "ai_involved: 'no'\ncomments_on: [fx.null.no-inverse]\n"
                "locators: {paper: FX, number: Abstract, line: 1}\n---\n\n## formal\n"
                "The paper says so, untagged.\n\n## technical\npending\n\n## lay\npending\n\n"
                "## one-liner\npending\n")
            r = dict(RECIPE, doc="fx-paper", level="formal", paper="FX", prose="paper",
                     include=dict(RECIPE["include"], settings="attached"))
            p = E(tmp, "r.yaml")
            yaml.safe_dump(r, open(p, "w"))
            dd = docgen.generate(root, p)
            bl = json.load(open(E(dd["folder"], "blocks.json")))
            ab = next(b for b in bl if b["type"] == "abstract")
            self.assertEqual(ab["text"], "The paper says so, untagged.")
            self.assertNotIn("D101", {f["code"] for f in dd["audit"]})
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
