"""Tests for lib/series.py: truncated power series identities, Laurent series, rational-function
helpers, exact roots, the exact number classes QS/R2/CY, and the certified bounds, which must
reproduce the pasted helpers bit for bit (exec'd from the checks while they still carry their
copies; containment of known decimal brackets is pinned regardless).
Run: python3 -m unittest discover -s tests -t .
"""
import ast
import inspect
import os
import sys
import unittest
from fractions import Fraction as F

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(ROOT, "lib")
if LIB not in sys.path:
    sys.path.insert(0, LIB)

import GA  # noqa: E402
import series as S  # noqa: E402

CLAIMS = os.path.join(ROOT, "store", "claims")
FAMCOMMON = os.path.join(ROOT, "tests", "fixtures", "gtg", "L09_famcommon.py")


def _check_ns(eid, needle):
    path = os.path.join(CLAIMS, eid, "check.py")
    if not os.path.exists(path):
        return None
    src = open(path).read()
    if needle not in src:
        return None
    ns = {"__name__": "check_under_test"}
    exec(compile(src, path, "exec"), ns)
    return ns


DARK = "dark-tower-matter.five-dimensional-towers"
SPEC = "standard-model.spectrum-run"
DEFICIT = "singularity.deficit-theorem-cost-descent-exactly"


class TestPowerSeries(unittest.TestCase):
    N = 10

    def test_exp_log_inverse(self):
        N = self.N
        a = [F(0), F(1), F(-1, 3), F(2), F(0), F(5, 7)] + [F(0)] * 5
        self.assertEqual(S.ps_log(S.ps_exp(a, N), N), S.ps_trunc(a, N))
        self.assertEqual(S.ps_exp(S.ps_var(N), N), S.taylor_exp(N))
        self.assertEqual(S.ps_log(S.ps_add(S.ps_one(N), S.ps_var(N), N), N), S.taylor_log1p(N))

    def test_powers(self):
        N = self.N
        a = [F(4), F(1), F(-2)]
        r = S.ps_sqrt(a, N)
        self.assertEqual(r[0], 2)
        self.assertEqual(S.ps_mul(r, r, N), S.ps_trunc(a, N))
        c = S.ps_pow(a, F(-3, 2), N)
        self.assertEqual(S.ps_mul(S.ps_pow_int(r, 3, N), c, N), S.ps_one(N))
        self.assertEqual(S.ps_pow_rat([F(1), F(1)], F(1, 2), N), S.taylor_binomial(F(1, 2), N))
        self.assertEqual(S.ps_div(S.ps_one(N), [F(1), F(-1)], N), [F(1)] * (N + 1))

    def test_compose_reversion_calculus(self):
        N = self.N
        asin = S.ps_reversion(S.taylor_sin(N), N)
        self.assertEqual(asin[:6], [0, 1, 0, F(1, 6), 0, F(3, 40)])
        self.assertEqual(S.ps_compose(S.taylor_sin(N), asin, N), S.ps_var(N))
        atan = S.taylor_atan(N)
        self.assertEqual(S.ps_deriv(atan)[:N], S.ps_inv([F(1), F(0), F(1)], N - 1))
        self.assertEqual(S.ps_integrate(S.ps_deriv(atan), N), atan)
        self.assertEqual(S.ps_valuation([0, 0, F(3)]), 2)
        self.assertIsNone(S.ps_valuation([0, 0]))
        self.assertEqual(S.ps_shift([F(0), F(0), F(1), F(2)], -2, 3), [1, 2, 0, 0])
        self.assertEqual(S.ps_eval([F(1), F(2), F(3)], F(1, 2)), F(11, 4))

    def test_laurent_and_rf(self):
        L = S.laurent([F(0), F(1), F(-1)])                     # x - x^2
        self.assertEqual(L, (1, [F(1), F(-1)]))
        inv = S.laurent_inv(L, 4)                              # 1/(x(1 - x)) = x^-1 + 1 + x + ...
        self.assertEqual(inv, (-1, [F(1)] * 6))
        self.assertEqual(S.laurent_mul(L, inv, 4), (0, [F(1), F(0), F(0), F(0), F(0)]))   # known to x^4
        self.assertEqual(S.laurent_coeff(inv, 3), 1)
        self.assertEqual(S.laurent_add(L, S.laurent_shift(L, 1), 3), (1, [F(1), F(0), F(-1)]))
        t = S.rf_var()
        r = S.rf_const(1) / (S.rf_const(1) - t - t * t)       # Fibonacci generating function
        self.assertEqual(S.rf_taylor(r, 8), [1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertTrue(S.rf_pow(r, -2).eqrf(S.rf_poly([1, -1, -1]) * S.rf_poly([1, -1, -1])))
        self.assertEqual(S.pcompose([F(1), F(0), F(1)], [F(1), F(1)]), [2, 2, 1])
        self.assertEqual(S.pbinomial(6, 2), 15)
        self.assertEqual([S.pbinomial(4, k) for k in (-1, 0, 4, 5)], [0, 1, 1, 0])
        Z = S.laurent([F(0), F(0)])
        self.assertEqual(Z, (0, []))
        self.assertEqual(S.laurent_mul(Z, L, 3), (0, []))
        self.assertEqual(S.laurent_mul(L, L, 1), (0, []))                  # valuation 2 > top
        self.assertEqual(S.laurent_inv(S.laurent_shift(L, 3), -5), (0, []))
        self.assertEqual(S.laurent_add(Z, L, 2), L)
        self.assertEqual(S.laurent_add(L, Z, 3), (1, [F(1), F(-1), F(0)]))
        self.assertEqual(S.ps_shift([F(1), F(2)], 2, 4), [0, 0, 1, 2, 0])
        self.assertEqual(S.taylor_cos(5), [1, 0, F(-1, 2), 0, F(1, 24), 0])
        self.assertEqual(S.taylor_sin(5), [0, 1, 0, F(-1, 6), 0, F(1, 120)])
        self.assertEqual(S.ps_pow_int([F(2), F(1)], 0, 3), S.ps_one(3))
        self.assertEqual(S.ps_pow_int([F(2), F(1)], -1, 3), S.ps_inv([F(2), F(1)], 3))


class TestRootsAndNumbers(unittest.TestCase):
    def test_roots(self):
        self.assertEqual(S.iroot(10 ** 12, 3), 10 ** 4)
        self.assertIsNone(S.iroot(10, 2))
        self.assertEqual(S.isqrt(10 ** 20 + 1), 10 ** 10)
        self.assertEqual(S.qpow(F(8, 27), F(2, 3)), F(4, 9))
        self.assertEqual(S.qpow(F(-8), F(1, 3)), -2)
        self.assertEqual(S.qsqrt(F(9, 4)), F(3, 2))
        with self.assertRaises(ValueError):
            S.qpow(F(2), F(1, 2))
        self.assertTrue(S.is_square(F(49, 64)))
        self.assertFalse(S.is_square(F(2)))
        self.assertFalse(S.is_square(F(1, 8)))
        self.assertFalse(S.is_square(F(8)))

    def test_qs_r2_cy(self):
        s2 = S.QS(0, 1, 2)
        self.assertEqual(s2 * s2, 2)
        x = S.R2(3, -2)                                      # 3 - 2 sqrt 2 > 0
        self.assertEqual((x.p, x.q), (3, -2))
        self.assertEqual(x.sign(), 1)
        self.assertEqual(S.R2(1, -1).sign(), -1)
        self.assertEqual(x * S.R2(3, 2), 1)
        self.assertEqual(1 / x, S.R2(3, 2))
        self.assertTrue(S.R2(1, 1) > S.R2(2, 0))
        self.assertEqual(S.QS(1, 2, -3) * S.QS(1, -2, -3), 13)
        z = S.ZETA
        self.assertEqual(z * z * z, S.CY(1))
        self.assertEqual(1 + z + S.Z2, S.CY(0))
        self.assertEqual(z.conj(), S.Z2)
        self.assertEqual(S.ISQ3 * S.ISQ3, S.CY(-3))
        self.assertEqual(S.CY(2, 1).nsq(), 3)
        self.assertFalse(S.CY(0))
        self.assertTrue(S.CY(1) and S.CY(0, 1))
        self.assertEqual(S.R2(), 0)
        self.assertFalse(S.R2())
        self.assertEqual(S.R2(1, 1) ** -2, 1 / (S.R2(1, 1) * S.R2(1, 1)))
        self.assertEqual(S.R2(1, 1) ** 3, S.R2(7, 5))
        self.assertNotEqual(S.R2(1, 1), 1)
        self.assertEqual(S.QS(5, 0, 2), S.QS(5, 0, 3))

    @unittest.skipUnless(os.path.exists(FAMCOMMON), "L09 famcommon not present")
    def test_matches_famcommon(self):
        ns = {"F": F, "GA": GA}
        exec(compile(open(FAMCOMMON).read(), FAMCOMMON, "exec"), ns)
        for m in (2, F(3, 7), 10 ** 6 + 1):
            self.assertEqual(S.sqrt_bounds(m), ns["sqrt_bounds"](m))
            self.assertEqual(S.sqrt_bounds(m, 25), ns["sqrt_bounds"](m, 25))
        for n in (0, 1, 2, 99, 10 ** 30):
            self.assertEqual(S.isqrt(n), ns["isqrt"](n))
        a, b = ns["CY"](F(1, 2), 3), S.CY(F(1, 2), 3)
        self.assertEqual(((a * a).a, (a * a).b), ((b * b).a, (b * b).b))
        r, q = ns["R2"](F(5), F(-7, 2)), S.R2(F(5), F(-7, 2))
        self.assertEqual(r.sign(), q.sign())


class TestBounds(unittest.TestCase):
    PI = (F(314159265358979, 10 ** 14), F(314159265358980, 10 ** 14))
    E1 = (F(271828182845904, 10 ** 14), F(271828182845905, 10 ** 14))
    LN2 = (F(69314718055994, 10 ** 14), F(69314718055995, 10 ** 14))

    def _inside(self, lohi, known):
        lo, hi = lohi
        self.assertLess(lo, known[1])
        self.assertGreater(hi, known[0])
        self.assertLess(hi - lo, F(1, 10 ** 13))

    def test_known_values(self):
        self._inside(S.pi_bracket(), self.PI)
        self._inside(S.pi_bounds(), self.PI)
        self._inside(S.exp_bracket(F(1)), self.E1)
        self._inside(S.exp_bounds(F(1)), self.E1)
        self._inside(S.ln_bounds(2), self.LN2)
        lo, hi = S.log_bounds(F(1, 2))
        self.assertTrue(-self.LN2[1] < hi and lo < -self.LN2[0])
        lo, hi = S.exp_bracket(F(-1))
        self.assertTrue(lo * self.E1[0] < 1 < hi * self.E1[1])
        lo, hi = S.sqrt_bounds(2)
        self.assertTrue(lo * lo <= 2 <= hi * hi)
        lo, hi = S.iroot_bracket(F(2), 3, 1000)
        self.assertEqual((lo, hi), (F(1259, 1000), F(1260, 1000)))
        lo, hi = S.atanh_bounds(F(1, 3))
        self.assertTrue(lo <= hi)
        self.assertEqual(S.round_down(F(1, 3), 8), F(2, 8))
        self.assertEqual(S.round_up(F(1, 3), 8), F(3, 8))

    def test_bit_for_bit_with_pasted_helpers(self):
        dark = _check_ns(DARK, "def pi_bracket")
        if dark is not None:
            self.assertEqual(S.pi_bracket(), dark["pi_bracket"]())
            self.assertEqual(S.pi_bracket(10), dark["pi_bracket"](10))
            for x in (F(1), F(7, 3), F(-2, 5)):
                self.assertEqual(S.exp_bracket(x), dark["exp_bracket"](x))
            self.assertEqual(S.iroot_bracket(F(5, 3), 4, 10 ** 6), dark["iroot_bracket"](F(5, 3), 4, 10 ** 6))
        spec = _check_ns(SPEC, "def pi_bounds")
        if spec is not None:
            self.assertEqual(S.pi_bounds(), spec["pi_bounds"]())
            for x in (F(1), F(13, 2), F(1, 1000)):
                self.assertEqual(S.exp_bounds(x), spec["exp_bounds"](x))
        defi = _check_ns(DEFICIT, "def ln_bounds")
        if defi is not None:
            for n in (2, 3, 10, 97, 1024, 10 ** 9 + 7):
                self.assertEqual(S.ln_bounds(n), defi["ln_bounds"](n))
            self.assertEqual(S.atanh_bounds(F(1, 5)), defi["_atanh_bounds"](F(1, 5)))


class TestLibraryRules(unittest.TestCase):
    def test_static_rules_and_docstrings(self):
        from tp import evidence
        path = os.path.join(LIB, "series.py")
        src = open(path).read()
        self.assertEqual([p for p in evidence.static_problems(src) if p[0] != "E403"], [])
        tree = ast.parse(src)
        self.assertFalse([n.lineno for n in ast.walk(tree) if isinstance(n, ast.Attribute) and n.attr == "setdefault"])
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and not node.name.startswith("_"):
                doc = inspect.getdoc(getattr(S, node.name))
                self.assertTrue(doc and doc.splitlines()[0].strip(), node.name)

    def test_imports_are_fast_and_silent(self):
        import subprocess
        code = ("import sys, time; sys.path.insert(0, %r); t = time.time(); import gtg, fock, series; "
                "print(round(time.time() - t, 3))" % LIB)
        out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True)
        self.assertEqual(out.stderr, "")
        self.assertLess(F(out.stdout.strip()), F(2))


class TestRounding(unittest.TestCase):
    def test_rounds_to(self):
        self.assertTrue(S.rounds_to(F(31416, 10000), 314, -2))
        self.assertFalse(S.rounds_to(F(31416, 10000), 315, -2))
        self.assertFalse(S.rounds_to(F(3145, 1000), 314, -2))     # the half is excluded
        self.assertTrue(S.rounds_to(F(-25, 10), -25, -1))
        self.assertTrue(S.rounds_to(1776970, 177697, 1))

    def test_root_rounds_to(self):
        self.assertTrue(S.root_rounds_to(2, 1414, -3))           # sqrt 2 = 1.41421...
        self.assertFalse(S.root_rounds_to(2, 1415, -3))
        self.assertTrue(S.root_rounds_to(F(11, 4), 1401, -3, k=3))   # (11/4)^(1/3) = 1.40102...
        self.assertFalse(S.root_rounds_to(F(11, 4), 1402, -3, k=3))

    def test_interval_rounds_to(self):
        self.assertTrue(S.interval_rounds_to(F(1395, 1000), F(1404, 1000), 14, -1))
        self.assertFalse(S.interval_rounds_to(F(1395, 1000), F(1450, 1000), 14, -1))
        self.assertFalse(S.interval_rounds_to(F(1349, 1000), F(1400, 1000), 14, -1))


if __name__ == "__main__":
    unittest.main()
