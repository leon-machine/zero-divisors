"""Quantities (roadmap item 10), the contradiction scan W510 (item 9) and payloads
evaluated by lint (item 11), on the fixture store."""
import contextlib
import io
import json
import os
import re
import shutil
import tempfile
import unittest
from fractions import Fraction

from tests.fixture_store import build
from tp import lint, quantity as Q, validate as V
from tp.model import dump_entity, load_store, parse_entity_text

E = os.path.join

PROV = {"kind": "ai", "session": "test"}


def qmeta(qid, symbol, value, units, status="measured", **block):
    b = {"symbol": symbol, "value": value, "units": units,
         "source": {"citation": "test source", "locator": "table 1"}}
    b.update(block)
    return {"id": qid, "kind": "quantity", "version": 1, "title": f"The quantity {symbol}",
            "status": status, "subject": "algebra", "proposed_by": PROV,
            "ai_involved": "yes", "review": "typed", "quantity": b}


MZ = ("fx.q.z-mass", "M_{Z}", "91.1876", "GeV", dict(uncertainty="0.0021", dimension="mass"))
MTAU = ("fx.q.tau-mass", "m_{\\tau}", "1776.93", "MeV", dict(uncertainty="0.09",
                                                            dimension="mass"))
C = ("fx.q.c", "c", "299792458", "m/s", dict(dimension="velocity", exact=True))


class QuantityCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="quantity-test-")
        self.root = build(E(self.tmp, "store"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def add_quantity(self, spec, status="measured", **over):
        qid, sym, val, units, block = spec
        block = dict(block, **over)
        meta = qmeta(qid, sym, val, units, status, **block)
        folder = E(self.root, "quantities", qid)
        os.makedirs(folder, exist_ok=True)
        with open(E(folder, "entity.md"), "w") as fh:
            fh.write(dump_entity(meta, {"formal": f"${sym} = {val}$ {units}.",
                                        "technical": "pending", "lay": "pending",
                                        "one-liner": "A record value."}))
        return folder

    def folder(self, eid):
        for sub in ("claims", "objects", "predictions", "questions", "notes", "quantities"):
            p = E(self.root, sub, eid)
            if os.path.isdir(p):
                return p
        raise KeyError(eid)

    def set_formal(self, eid, text):
        p = E(self.folder(eid), "entity.md")
        s = open(p).read()
        s = re.sub(r"## formal\n.*?\n\n## technical",
                   lambda m: "## formal\n" + text + "\n\n## technical", s, flags=re.S)
        open(p, "w").write(s)

    def run_main(self, *args):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = Q.main(["quantity", *args, "--store", self.root])
        return code, buf.getvalue()

    def w510(self):
        rep = V.validate(load_store(self.root), layers=(5,), keep_going=True)
        return [f for f in rep.findings if f.code == "W510"], rep


class Units(unittest.TestCase):
    def test_parse_and_convert(self):
        self.assertEqual(Q.parse_units("km/s/Mpc")[1], Q.DIMENSIONS["inverse time"])
        self.assertEqual(Q.parse_units("GeV s")[1], Q.DIMENSIONS["action"])
        self.assertEqual(Q.parse_units("m^-2")[1], Q.DIMENSIONS["inverse area"])
        self.assertEqual(Q.parse_units("MeV fm")[1], Q.DIMENSIONS["energy times length"])
        self.assertEqual(Q.convert(Fraction(1), "GeV", "MeV"), 1000)
        self.assertEqual(Q.convert(Fraction(49), "meV", "eV"), Fraction(49, 1000))
        self.assertIsNone(Q.convert(Fraction(1), "GeV", "m"))
        with self.assertRaises(ValueError):
            Q.parse_units("furlong")

    def test_dimension_agrees(self):
        self.assertTrue(Q.dimension_agrees("GeV", "mass")[0])       # natural units
        self.assertTrue(Q.dimension_agrees("GeV", "energy")[0])
        self.assertTrue(Q.dimension_agrees("1", "dimensionless")[0])
        self.assertFalse(Q.dimension_agrees("GeV", "length")[0])
        self.assertFalse(Q.dimension_agrees("m", "mass")[0])
        self.assertFalse(Q.dimension_agrees("GeV", "colour")[0])

    def test_numbers_and_symbols(self):
        nums = list(Q.numbers(r"$M_{P} = 1.220890 \times 10^{19}$ GeV and 1.39449\ldots"))
        self.assertEqual(nums[0].value, Fraction("1.220890e19"))
        self.assertEqual(nums[0].ulp, Fraction(10) ** 13)
        self.assertTrue(nums[1].dots)
        self.assertEqual(Q.plain(r"\sin^{2} \theta_{W}"), "sin^2 theta_W")
        self.assertTrue(Q.matches_symbol(Q.plain(r"with $m_{\tau}"), {"m_tau"}))
        self.assertFalse(Q.matches_symbol("xm_tau", {"m_tau"}))
        self.assertFalse(Q.matches_symbol("M_P", {"m_p"}))
        self.assertTrue(Q.matches_symbol("OMEGA_L", {"Omega_L"}, ignore_case=True))


class QuantityEntities(QuantityCase):
    def test_valid_quantities_pass_validation_and_check(self):
        for spec in (MZ, MTAU):
            self.add_quantity(spec)
        self.add_quantity(C, status="defined")
        rep = V.validate(load_store(self.root), layers=(1, 2, 3), keep_going=True)
        self.assertEqual(rep.errors(), [], "\n".join(f.render() for f in rep.errors()))
        code, out = self.run_main("check")
        self.assertEqual(code, 0, out)
        self.assertIn("3 quantities, 0 error(s)", out)
        code, out = self.run_main("list")
        self.assertIn("fx.q.z-mass", out)
        self.assertIn("91.1876 +- 0.0021 GeV", out)

    def test_check_finds_bad_values(self):
        cases = [
            (dict(uncertainty="95"), "not below"),                  # uncertainty >= value
            (dict(uncertainty="-0.1"), "negative"),
            (dict(dimension="length"), "do not have dimension"),
            (dict(uncertainty="about 0.002"), "uncertainty"),
        ]
        for over, needle in cases:
            with self.subTest(over=over):
                self.add_quantity(MZ, **over)
                code, out = self.run_main("check")
                self.assertEqual(code, 1, out)
                self.assertIn(needle, out)

    def test_check_finds_unknown_units_and_exact_with_uncertainty(self):
        self.add_quantity(("fx.q.odd", "x", "2", "furlong", {}))
        self.add_quantity(C, status="defined", uncertainty="1")
        code, out = self.run_main("check")
        self.assertEqual(code, 1)
        self.assertIn("unknown unit 'furlong'", out)
        self.assertIn("exact value carries no uncertainty", out)

    def test_users_pinned_and_literal(self):
        self.add_quantity(MZ)
        p = E(self.folder("fx.algebra.dimension"), "check.py")
        src = open(p).read()
        open(p, "w").write(src + "\nMZ = F(911876, 10000)\nROUNDED = 91.19\nOTHER = 92.5\n")
        meta_p = E(self.folder("fx.witt.car"), "entity.md")
        meta, levels, _ = parse_entity_text(open(meta_p).read())
        meta["quantities"] = ["fx.q.z-mass@1"]
        open(meta_p, "w").write(dump_entity(meta, levels))
        users = Q.literal_users(load_store(self.root), detail=True)["fx.q.z-mass"]
        self.assertEqual(users["fx.algebra.dimension"]["check"], ["91.19", "F(911876, 10000)"])
        self.assertEqual(Q.pinned_users(load_store(self.root), "fx.q.z-mass"),
                         [("fx.witt.car", "fx.q.z-mass@1")])
        code, out = self.run_main("users", "fx.q.z-mass")
        self.assertEqual(code, 0)
        self.assertIn("fx.witt.car", out)
        self.assertIn("fx.algebra.dimension: 91.19, F(911876, 10000)", out)
        code, out = self.run_main("show", "fx.q.no-such")
        self.assertEqual(code, 2)


class Contradictions(QuantityCase):
    def setUp(self):
        super().setUp()
        self.add_quantity(MZ)
        self.add_quantity(MTAU)

    def test_clean_fixture_has_no_w510_and_an_i510(self):
        found, rep = self.w510()
        self.assertEqual(found, [])
        self.assertIn("I510", {f.code for f in rep.findings})

    def test_drift_flagged(self):
        self.set_formal("fx.algebra.dimension", r"With $M_{Z} = 91.25$ GeV the bound holds.")
        found, _ = self.w510()
        self.assertEqual(len(found), 1, [f.render() for f in found])
        self.assertIn("quantity drift", found[0].message)
        self.assertEqual(found[0].entity, "fx.algebra.dimension")

    def test_no_drift_within_precision_units_or_other_quantity(self):
        for text in (r"With $M_{Z} = 91.19$ GeV the bound holds.",       # rounded
                     r"With $M_{Z} = 91187.6$ MeV the bound holds.",     # converted
                     r"With $M_{Z} = 3$ the bound holds.",              # not this quantity
                     r"The model predicts $M_{Z} = 91.25$ GeV."):       # a prediction
            with self.subTest(text=text):
                self.set_formal("fx.algebra.dimension", text)
                found, _ = self.w510()
                self.assertEqual(found, [], [f.render() for f in found])

    def test_drift_in_other_units(self):
        self.set_formal("fx.algebra.dimension", r"With $M_{Z} = 91250$ MeV the bound holds.")
        found, _ = self.w510()
        self.assertEqual(len(found), 1)

    def test_same_quantity_disagreement(self):
        self.set_formal("fx.algebra.dimension", r"Here $m_{\tau} = 1776.86$ MeV.")
        self.set_formal("fx.witt.car", r"Here $m_{\tau} = 1776.93$ MeV.")
        found, _ = self.w510()
        self.assertEqual(len(found), 1, [f.render() for f in found])
        self.assertIn("same-quantity disagreement", found[0].message)
        # compatible at the displayed precision: no finding
        self.set_formal("fx.algebra.dimension", r"Here $m_{\tau} = 1776.9$ MeV.")
        found, _ = self.w510()
        self.assertEqual(found, [])

    def test_decimal_drift(self):
        bad = r"$R = 1357472/973455 = 1.3945\ldots$."
        self.set_formal("fx.algebra.dimension", bad)
        found, _ = self.w510()
        self.assertEqual(len(found), 1)
        self.assertIn("decimal drift", found[0].message)
        for ok in (r"$R = 1357472/973455 = 1.39448\ldots$.",
                   r"$R = 1357472/973455 \approx 1.3945$.",
                   r"$r = \tfrac{218}{115} = 1.89565\ldots$."):
            with self.subTest(ok=ok):
                self.set_formal("fx.algebra.dimension", ok)
                found, _ = self.w510()
                self.assertEqual(found, [], [f.render() for f in found])

    def test_sign_convention(self):
        self.set_formal("fx.algebra.dimension",
                        r"$\Omega(e_1) = \sigma_1 B_1$ and the field is "
                        r"$\sum_i p_i B_i \otimes \hat\theta^i$.")
        found, _ = self.w510()
        self.assertEqual(len(found), 2, [f.render() for f in found])
        self.assertTrue(all("sign convention" in f.message for f in found))
        self.set_formal("fx.algebra.dimension",
                        r"$\Omega(e_1) = -\sigma_1 B_1$ and the field is "
                        r"$-\sum_i p_i B_i \otimes \hat\theta^i$; the forms are "
                        r"$\omega^{1}{}_{0} = \sigma_1 \theta^1$.")
        found, _ = self.w510()
        self.assertEqual(found, [], [f.render() for f in found])


class Payload(QuantityCase):
    def lint(self, eid):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = lint.main(["lint", eid, "--store", self.root, "--json", "--no-run"])
        return code, json.loads(buf.getvalue())

    def set_payload(self, eid, payload):
        p = E(self.folder(eid), "entity.md")
        meta, levels, _ = parse_entity_text(open(p).read())
        meta["payload"] = payload
        open(p, "w").write(dump_entity(meta, levels))

    def test_payload_with_quantity_passes_and_fails(self):
        self.add_quantity(MZ)
        self.set_payload("fx.algebra.dimension", [
            {"kind": "count", "python": "len(g.all_blades(2)) == 4", "clause": "dimension"},
            {"kind": "value", "python": "Fraction('91.1876') == Fraction(911876, 10000)",
             "quantity": "fx.q.z-mass"}])
        p = E(self.folder("fx.algebra.dimension"), "check.py")
        src = open(p).read()
        open(p, "w").write("from fractions import Fraction\n" + src)
        rep = V.validate(load_store(self.root), layers=(1,), keep_going=True)
        self.assertEqual(rep.errors(), [], "\n".join(f.render() for f in rep.errors()))
        code, res = self.lint("fx.algebra.dimension")
        self.assertEqual(code, 0, res["findings"])
        self.set_payload("fx.algebra.dimension", [
            {"kind": "count", "python": "len(g.all_blades(2)) == 5", "clause": "dimension"}])
        code, res = self.lint("fx.algebra.dimension")
        self.assertEqual(code, 1)
        msgs = [f["message"] for f in res["findings"] if f["code"] == "L501"]
        self.assertEqual(len(msgs), 1)
        self.assertIn("clause dimension", msgs[0])


if __name__ == "__main__":
    unittest.main()
