"""Tests for lib/fock.py: CAR relations and the Jordan-Wigner sign in both basis orders, Majoranas,
parity, partial traces, the Chevalley and Fock models of Clifford algebras, and agreement with the
Fock toolkits pasted into checks (reference implementations copied below, each naming its source;
the Cl(2,4) Fock core is also exec'd from the fock-model check while it still carries its copy).
Run: python3 -m unittest discover -s tests -t .
"""
import ast
import inspect
import os
import sys
import unittest
from fractions import Fraction as F
from itertools import permutations

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(ROOT, "lib")
if LIB not in sys.path:
    sys.path.insert(0, LIB)

import GA  # noqa: E402
import fock  # noqa: E402
from fock import LSB, MSB  # noqa: E402

FOCK_CHECK = os.path.join(ROOT, "store", "claims", "correspondence.fock-model-complexified-ascended-algebra", "check.py")


# -- reference implementations, copied verbatim (modulo names) from the checks -------------------

def ref_create_lsb(m, nm):
    """standard-model.matching-traces create(m) with DIM = 2^nm."""
    return {(s | 1 << m, s): F((-1) ** bin(s & ((1 << m) - 1)).count("1"))
            for s in range(2 ** nm) if not s >> m & 1}


def ref_occ(i, m):
    """descent-lift.parity-alone-forces-second-rung occ."""
    return tuple((i >> (m - 1 - k)) & 1 for k in range(m))


def ref_idx(t):
    out = 0
    for b in t:
        out = 2 * out + b
    return out


def ref_ann_msb(k, m):
    """descent-lift.parity-alone-forces-second-rung ann."""
    out = {}
    for i in range(2 ** m):
        t = ref_occ(i, m)
        if t[k]:
            s = sum(t[:k]) % 2
            u = list(t)
            u[k] = 0
            out[(ref_idx(u), i)] = F(-1 if s else 1)
    return out


def _fockcore_available():
    if not os.path.exists(FOCK_CHECK):
        return False
    with open(FOCK_CHECK) as fh:
        return "def wedge_op(i):" in fh.read()


class TestCAR(unittest.TestCase):
    def test_car_both_orders(self):
        m = 3
        d = 2 ** m
        for order in (LSB, MSB):
            a = [fock.ann(k, m, order) for k in range(m)]
            ad = [fock.cre(k, m, order) for k in range(m)]
            for i in range(m):
                self.assertEqual(fock.dag(a[i]), ad[i])
                for j in range(m):
                    self.assertEqual(fock.acomm(a[i], ad[j]), fock.eye(d) if i == j else {})
                    self.assertEqual(fock.acomm(a[i], a[j]), {})
                    self.assertEqual(fock.acomm(ad[i], ad[j]), {})
                self.assertEqual(fock.mm(ad[i], a[i]), fock.num(i, m, order))

    def test_jordan_wigner_sign_pinned(self):
        # LSB: a_1^dag |mode 0 occupied> = -|modes 0, 1>
        self.assertEqual(fock.cre(1, 3, LSB)[(0b011, 0b001)], -1)
        self.assertEqual(fock.cre(0, 3, LSB)[(0b011, 0b010)], 1)
        # MSB: index of (1, 0, 0) is 4; a_1^dag gives (1, 1, 0) = 6 with sign -1
        self.assertEqual(fock.cre(1, 3, MSB)[(6, 4)], -1)
        self.assertEqual(fock.occ(6, 3, MSB), (1, 1, 0))
        self.assertEqual(fock.occ(6, 3, LSB), (0, 1, 1))
        self.assertEqual(fock.idx((1, 1, 0), MSB), 6)
        self.assertEqual(fock.idx((1, 1, 0), LSB), 3)

    def test_matches_pasted_toolkits(self):
        for nm in (3, 5):
            for m in range(nm):
                self.assertEqual(fock.cre(m, nm, LSB), ref_create_lsb(m, nm))
                self.assertEqual(fock.ann(m, nm, MSB), ref_ann_msb(m, nm))
                self.assertEqual(fock.occ(7, nm, MSB), ref_occ(7, nm))

    def test_direct_state_actions(self):
        m = 4
        v = {0b0101: F(2), 0b0110: F(-1), 0b1000: F(3)}
        for k in range(m):
            self.assertEqual(fock.ann_on(k, v), fock.apply(fock.ann(k, m), v))
            self.assertEqual(fock.cre_on(k, v), fock.apply(fock.cre(k, m), v))
        # rungs.* ann(i, st): a_2 on |modes 0, 2> passes one occupied mode
        self.assertEqual(fock.ann_on(2, {0b101: F(1)}), {0b001: F(-1)})

    def test_orders_related_by_bit_reversal(self):
        m = 4

        def rev(s):
            return fock.idx(fock.occ(s, m, LSB), MSB)
        for k in range(m):
            L, M = fock.ann(k, m, LSB), fock.ann(k, m, MSB)
            self.assertEqual({(rev(i), rev(j)): c for (i, j), c in L.items()}, M)

    def test_number_parity_majorana(self):
        m = 3
        d = 2 ** m
        P = fock.parity(m)
        self.assertEqual(fock.mm(P, P), fock.eye(d))
        self.assertEqual(fock.trace(fock.num_total(m)), m * 2 ** (m - 1))
        self.assertEqual(fock.mode_parity(1, m), fock.madd(fock.eye(d), fock.msc(-2, fock.num(1, m))))
        for k in range(m):
            self.assertEqual(fock.acomm(P, fock.ann(k, m)), {})
        for kind, squares in (("real", (1, -1)), ("herm", (1, 1))):
            g = [fock.majorana(p, m, LSB, kind) for p in range(2 * m)]
            for p in range(2 * m):
                for q in range(2 * m):
                    want = fock.msc(2 * squares[p % 2], fock.eye(d)) if p == q else {}
                    self.assertEqual(fock.acomm(g[p], g[q]), want)
            if kind == "herm":
                self.assertTrue(all(fock.meq(fock.dag(x), x) for x in g))
        self.assertTrue(fock.is_even_op(fock.mm(fock.cre(0, m), fock.ann(2, m))))
        self.assertFalse(fock.is_even_op(fock.cre(0, m)))
        self.assertEqual(len(fock.even_states(4)), 8)

    def test_matching_traces_values(self):
        # standard-model.matching-traces: five modes (pair modes 0, 1, 2; slot modes 3, 4), the sixteen
        nm = 5
        even = fock.states(nm, parity=0)
        self.assertEqual(len(even), 16)
        N = [fock.num(k, nm) for k in range(nm)]
        one = fock.eye(2 ** nm)
        NW = fock.madd(N[0], N[1], N[2])
        T3L = fock.msc(F(1, 2), fock.msub(N[3], N[4]))
        T3R = fock.msc(F(1, 2), fock.msub(fock.madd(N[3], N[4]), one))
        BL = fock.msub(one, fock.msc(F(2, 3), NW))
        Y = fock.msc(F(1, 6), fock.msub(fock.msc(3, fock.madd(N[3], N[4])), fock.msc(2, NW)))

        def tr(A):
            return fock.trace(fock.restrict(A, even))
        self.assertEqual(tr(fock.mm(T3L, T3L)), 2)
        self.assertEqual(tr(fock.mm(T3R, T3R)), 2)
        self.assertEqual(tr(fock.mm(BL, BL)), F(16, 3))
        self.assertEqual(tr(fock.mm(Y, Y)), F(10, 3))
        self.assertEqual(tr(fock.mm(T3R, BL)), 0)


class TestOperators(unittest.TestCase):
    def test_partial_traces_and_kron(self):
        A = {(0, 1): F(2), (1, 0): F(3), (1, 1): F(5)}
        B = {(0, 0): F(1), (1, 1): F(7), (0, 1): F(-1)}
        AB = fock.kron(A, B, 2)
        self.assertEqual(fock.ptrace_rec(AB, 1), fock.msc(8, A))
        self.assertEqual(fock.ptrace_sys(AB, 1), fock.msc(5, B))
        self.assertEqual(fock.ptrace(AB, 2, [1], MSB), fock.ptrace_rec(AB, 1))
        self.assertEqual(fock.ptrace(AB, 2, [0], MSB), fock.ptrace_sys(AB, 1))
        self.assertEqual(fock.from_dense(fock.to_dense(AB, 4)), AB)
        rho = fock.outer({0: F(1), 3: F(1)}, {0: F(1), 3: F(1)})
        self.assertEqual(fock.purity(rho), 1)
        self.assertEqual(fock.purity(fock.ptrace_rec(rho, 1)), F(1, 2))

    def test_vectors_and_conjugation(self):
        i = GA.QI_I
        A = {(0, 1): GA.qi(1, 2)}
        self.assertEqual(fock.dag(A), {(1, 0): GA.qi(1, -2)})
        self.assertEqual(fock.transpose(A), {(1, 0): GA.qi(1, 2)})
        u, v = {0: i, 1: GA.qi(1)}, {0: GA.qi(1), 1: i}
        self.assertEqual(fock.braket(u, u), GA.qi(2))
        self.assertEqual(fock.inner(u, v), GA.qi(0, 2))
        self.assertEqual(fock.inner({0: F(2), 5: F(1)}, {0: F(3), 1: F(7)}), 6)
        self.assertEqual(fock.braket({0: i, 5: F(1)}, {0: i, 1: F(7)}), GA.qi(1))
        self.assertTrue(fock.is_even_vec({0: F(1), 3: F(2)}))
        self.assertFalse(fock.is_even_vec({0: F(1), 2: F(2)}))
        self.assertEqual(fock.apply(fock.cre(0, 2), fock.ket((0, 1))), {3: F(1)})
        self.assertEqual(fock.apply(fock.cre(1, 2), fock.ket((1, 0))), {3: F(-1)})


class TestCliffordModels(unittest.TestCase):
    def test_chevalley_matches_ga_ext_c(self):
        B = [[F(1), F(1, 2), F(0)], [F(1, 2), F(-1), F(2)], [F(0), F(2), F(0)]]   # non-diagonal, rational
        n = 3
        for alpha in ([F(1), F(0), F(0)], [F(2), F(-1), F(3)], [F(0), F(1, 3), F(1)]):
            C = fock.chevalley(alpha, B)
            q = sum(alpha[i] * B[i][j] * alpha[j] for i in range(n) for j in range(n))
            self.assertEqual(fock.mm(C, C), fock.msc(q, fock.eye(2 ** n)) if q else {})
            for S in ([], [0], [1, 2], [0, 1, 2]):
                st = {frozenset(S): F(1)}
                self.assertEqual(fock.apply(C, fock.ext_state(st)), fock.ext_state(GA.ext_c(alpha, B, st)))

    def test_fock_model_cl24(self):
        sq = GA.sig(2, 4)
        gens = fock.fock_cl24()
        self.assertTrue(fock.clifford_ok(gens, sq, 8))
        table = fock.blade_table(gens, 8)
        self.assertEqual(len(table), 64)
        rows = [[fock.to_dense(table[b], 8, GA.qi(0))[i][j] for i in range(8) for j in range(8)] for b in table]
        self.assertEqual(GA.field_rank(rows), 64)                  # Cl(2,4)_C = End(C^8)
        x = GA.add(GA.gen(0), GA.scal(3, GA.gen(4)))
        X = fock.rep(x, table)
        self.assertEqual(fock.mm(X, X), fock.msc(GA.dot(x, x, sq), fock.eye(8)))
        Bv = GA.mul(GA.gen(1), GA.gen(5), sq)
        lhs = fock.comm(fock.spin_rep(Bv, table), fock.rep(GA.gen(1), table))
        Bx = GA.scal(F(1, 2), GA.sub(GA.mul(Bv, GA.gen(1), sq), GA.mul(GA.gen(1), Bv, sq)))
        self.assertEqual(lhs, fock.rep(Bx, table))                 # [rho(B), c(x)] = c(B . x)
        for order in (LSB, MSB):
            for pairs, s in (([(0, 1), (2, 3)], (1, -1, -1, -1)), ([(0, 1)], (1, 1)), ([(1, 0)], (1, -1))):
                g = fock.fock_generators(pairs, s, order)
                self.assertTrue(fock.clifford_ok(g, s, 2 ** len(pairs)))

    @unittest.skipUnless(_fockcore_available(), "fock-model check already migrated")
    def test_matches_fockcore(self):
        ns = {"__name__": "fockcore_under_test", "permutations": permutations}
        with open(FOCK_CHECK) as fh:
            exec(compile(fh.read(), FOCK_CHECK, "exec"), ns)
        gens = fock.fock_cl24()
        for k in range(6):
            self.assertEqual(fock.to_dense(gens[k], 8, GA.qi(0)), ns["CB"][k])
        for i in range(3):
            self.assertEqual(fock.to_dense(fock.wedge_op(i, 3), 8, GA.qi(0)), ns["AW"][i])
            self.assertEqual(fock.to_dense(fock.contract_op(i, 3), 8, GA.qi(0)), ns["BW"][i])
        table = fock.blade_table(gens, 8)
        B = GA.mul(GA.gen(0), GA.gen(3), GA.sig(2, 4))
        self.assertEqual(fock.to_dense(fock.spin_rep(B, table), 8, GA.qi(0)), ns["rho"](B))


class TestLibraryRules(unittest.TestCase):
    def test_static_rules_and_docstrings(self):
        from tp import evidence
        path = os.path.join(LIB, "fock.py")
        src = open(path).read()
        self.assertEqual([p for p in evidence.static_problems(src) if p[0] != "E403"], [])
        tree = ast.parse(src)
        self.assertFalse([n.lineno for n in ast.walk(tree) if isinstance(n, ast.Attribute) and n.attr == "setdefault"])
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and not node.name.startswith("_"):
                doc = inspect.getdoc(getattr(fock, node.name))
                self.assertTrue(doc and doc.splitlines()[0].strip(), node.name)


if __name__ == "__main__":
    unittest.main()
