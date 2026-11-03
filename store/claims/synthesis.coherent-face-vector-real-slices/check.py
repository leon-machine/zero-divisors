"""synthesis.coherent-face-vector-real-slices: exact checks in Q(sqrt3)[i].

A number is ((a, b), (c, d)) = (a + b sqrt3) + i (c + d sqrt3) with Fraction entries.
The coherent face vector of the antisymmetric pairing sector is, up to its overall factor
-i sqrt(2/3) sinh r cosh r / sqrt(1 + lambda^2) ... (Proposition rigidity), v = u' + w f_+
with u' = (1,1,1), f_+ = (1, zeta, zeta^2) and w = lambda e^{i chi}.
"""
from fractions import Fraction as F
from tp_premise import premise
from GA import congruence_signature


# ---- Q(sqrt3) -------------------------------------------------------------
def r_add(x, y): return (x[0] + y[0], x[1] + y[1])
def r_sub(x, y): return (x[0] - y[0], x[1] - y[1])
def r_mul(x, y): return (x[0] * y[0] + 3 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def r_scal(q, x): return (q * x[0], q * x[1])
R0, R1 = (F(0), F(0)), (F(1), F(0))


# ---- Q(sqrt3)[i] ----------------------------------------------------------
def c(re, im=R0): return (re, im)
def c_add(x, y): return (r_add(x[0], y[0]), r_add(x[1], y[1]))
def c_sub(x, y): return (r_sub(x[0], y[0]), r_sub(x[1], y[1]))
def c_mul(x, y):
    return (r_sub(r_mul(x[0], y[0]), r_mul(x[1], y[1])), r_add(r_mul(x[0], y[1]), r_mul(x[1], y[0])))
def c_conj(x): return (x[0], r_scal(F(-1), x[1]))
def c_abs2(x): return r_add(r_mul(x[0], x[0]), r_mul(x[1], x[1]))
def c_rat(q, p=F(0)): return ((F(q), F(0)), (F(p), F(0)))
ZERO, ONE, I = c_rat(0), c_rat(1), c_rat(0, 1)
ZETA = ((F(-1, 2), F(0)), (F(0), F(1, 2)))           # -1/2 + i sqrt3/2


def vec_add(u, v): return [c_add(a, b) for a, b in zip(u, v)]
def vec_scal(s, v): return [c_mul(s, a) for a in v]
def bil(u, v):                                          # C(u, v) = sum u_k v_k
    t = ZERO
    for a, b in zip(u, v):
        t = c_add(t, c_mul(a, b))
    return t
def herm(u):                                            # sum |u_k|^2, an element of Q(sqrt3)
    t = R0
    for a in u:
        t = r_add(t, c_abs2(a))
    return t


UP = [ONE, ONE, ONE]
FP = [ONE, ZETA, c_mul(ZETA, ZETA)]
FM = [c_conj(z) for z in FP]


def proj_s(v):                                          # singlet projector P_s = J/3
    m = c_mul(c_rat(F(1, 3)), c_add(c_add(v[0], v[1]), v[2]))
    return [m, m, m]
def proj_d(v): return [c_sub(a, b) for a, b in zip(v, proj_s(v))]


def sigma(x, y, v):                                     # antilinear map v -> (x P_s + y P_d) conj(v)
    vb = [c_conj(a) for a in v]
    return vec_add(vec_scal(x, proj_s(vb)), vec_scal(y, proj_d(vb)))


def perms():
    import itertools
    for p in itertools.permutations(range(3)):
        sgn = 1
        for i in range(3):
            for j in range(i + 1, 3):
                if p[i] > p[j]:
                    sgn = -sgn
        yield p, sgn


def unit_phases():                                      # exact points of the unit circle in Q(i)
    for t in (F(0), F(1), F(1, 2), F(-2, 3), F(5, 7), F(3)):
        d = 1 + t * t
        yield c_rat((1 - t * t) / d, 2 * t / d)
    yield I
    yield c_rat(-1)


TESTS = [[ONE, ZETA, I], [c_rat(2, -1), c_rat(0, 3), c_rat(F(1, 2))], FP, UP]
WS = [c_rat(1), c_rat(1, 1), c_rat(F(1, 2), F(-3, 4)), c_rat(-2, F(1, 3)), c_rat(0, 2), ZETA,
      c_add(c_rat(1), c_mul(c_rat(0, F(1, 5)), ZETA))]


def check_fourier_line_isotropic_and_not_real():
    premise("families.chart-computation-sign-twist-bracket-form")
    assert bil(FP, FP) == ZERO and bil(FM, FM) == ZERO          # Fourier lines are C-null
    assert bil(UP, FP) == ZERO and herm(FP) == (F(3), F(0))
    # f_+ is not a complex multiple of a real vector: f_+[1]/f_+[0] = zeta is not real
    assert c_sub(ZETA, c_conj(ZETA)) != ZERO
    # for every unit phase e: |Re(e f_+)|^2 = |Im(e f_+)|^2 = 3/2 (isotropy), so every real
    # slice of the line carries exactly half its Hermitian norm
    for e in unit_phases():
        ef = vec_scal(e, FP)
        re2 = R0
        im2 = R0
        for a in ef:
            re2 = r_add(re2, r_mul(a[0], a[0]))
            im2 = r_add(im2, r_mul(a[1], a[1]))
        assert re2 == (F(3, 2), F(0)) and im2 == (F(3, 2), F(0))


def check_real_structures():
    """The S3-equivariant antilinear involutions are (x P_s + y P_d) conj with |x| = |y| = 1;
    compatible with C (C(sigma v) = conj C(v)) iff x^2 = y^2 = 1. The coherent vector, times any
    phase, is fixed by none of them unless w = 0."""
    premise("families.chart-computation-sign-twist-bracket-form")
    tests = TESTS
    # the four C-compatible structures: a rational basis of each fixed slice, the restriction
    # of C to it, and its exact signature (GA.congruence_signature): Euclidean for x = y,
    # Lorentzian (1,2) or (2,1) for x = -y
    BO, BE = [c_rat(1), c_rat(-1), c_rat(0)], [c_rat(1), c_rat(1), c_rat(-2)]
    expected = {(1, 1): (3, 0, 0), (1, -1): (1, 2, 0), (-1, 1): (2, 1, 0), (-1, -1): (0, 3, 0)}
    for (xs, ys), sgn_exp in expected.items():
        x, y = c_rat(xs), c_rat(ys)
        rs = ONE if xs == 1 else I                         # singlet fixed: s = x conj(s)
        rd = ONE if ys == 1 else I
        basis = [vec_scal(rs, UP), vec_scal(rd, BO), vec_scal(rd, BE)]
        for b in basis:
            assert sigma(x, y, b) == b
        G = []
        for b1 in basis:
            row = []
            for b2 in basis:
                z = bil(b1, b2)
                assert z[1] == R0 and z[0][1] == F(0)        # C is real and rational on the slice
                row.append(z[0][0])
            G.append(row)
        assert congruence_signature(G) == sgn_exp
    for x in unit_phases():
        for y in unit_phases():
            for v in tests:
                assert sigma(x, y, sigma(x, y, v)) == v              # involution for |x|=|y|=1
                for p, sgn in perms():                               # equivariance under +-P
                    Pv = [c_mul(c_rat(sgn), v[p[k]]) for k in range(3)]
                    lhs = sigma(x, y, Pv)
                    sv = sigma(x, y, v)
                    rhs = [c_mul(c_rat(sgn), sv[p[k]]) for k in range(3)]
                    assert lhs == rhs
            compatible = all(bil(sigma(x, y, v), sigma(x, y, v)) == c_conj(bil(v, v)) for v in tests)
            assert compatible == (c_mul(x, x) == ONE and c_mul(y, y) == ONE)
            # no fixed coherent vector: the doublet part of e * v lies on the line w f_+, and the
            # slice condition d = y conj(d) forces d_1/d_0 real, while d_1/d_0 = zeta
            for e in unit_phases():
                for w in WS:
                    v = vec_scal(e, vec_add(UP, vec_scal(w, FP)))
                    assert sigma(x, y, v) != v


def check_projection_and_koide():
    premise("families.chart-computation-sign-twist-bracket-form")
    premise("families.rigidity-pairing-sector-one-event")
    premise("families.koide-nullity-condition-one-member-invariant")
    MI = c_rat(0, -1)                                        # the overall -i of the coherent vector
    for w in WS:
        v0 = vec_add(UP, vec_scal(w, FP))
        assert bil(v0, v0) == c_rat(3)                       # C(v) = 3 for every lambda, chi
        w2 = c_abs2(w)
        assert herm(v0) == r_add((F(3), F(0)), r_scal(F(3), w2))
        v = vec_scal(MI, v0)
        # the two C-compatible structures whose slice contains the singlet -i u':
        #   x = -1, y = -1 (Euclidean, slice i R^3) and x = -1, y = +1 (Lorentzian)
        for y in (c_rat(-1), c_rat(1)):
            p = [c_mul(c_rat(F(1, 2)), a) for a in vec_add(v, sigma(c_rat(-1), y, v))]
            assert proj_s(p) == proj_s(v)                     # singlet retained in full
            ps, pd = herm(proj_s(p)), herm(proj_d(p))
            assert ps == (F(3), F(0)) and pd == r_scal(F(3, 2), w2)   # doublet keeps half
            # components of p / (-i) are real: sqrt m_k proportional to 1 + Re(w zeta^k) (y = -1)
            # or 1 + Re(-i w zeta^k) = 1 + Im(w zeta^k) (y = +1): delta = chi or chi - pi/2
            # real coordinates of the slice: (i P_s + P_d) p for y = +1, i p for y = -1
            if y == c_rat(-1):
                q = [c_mul(I, a) for a in p]
            else:
                q = vec_add(vec_scal(I, proj_s(p)), proj_d(p))
            for k in range(3):
                assert q[k][1] == R0
                zk = ONE
                for _ in range(k):
                    zk = c_mul(zk, ZETA)
                rot = w if y == c_rat(-1) else c_mul(c_rat(0, -1), w)
                assert q[k][0] == r_add(R1, c_mul(rot, zk)[0])
            # Koide ratio of the projected vector: Q = |p|^2 / (sum p)^2 = 1/3 + |w|^2/6
            tot = R0
            for a in q:
                tot = r_add(tot, a[0])
            assert tot == (F(3), F(0))
            Qnum = r_add(ps, pd)                              # = 3 + (3/2)|w|^2
            assert Qnum == r_mul(r_add((F(1, 3), F(0)), r_scal(F(1, 6), w2)), (F(9), F(0)))
            # on the Lorentzian slice C restricts to -(t^2 - |d|^2): C(p) = -q(p)
            if y == c_rat(1):
                assert bil(p, p) == c(r_scal(F(-1), r_sub(ps, pd)))
    # Koide instance: w = 1 + i (lambda^2 = 2, chi = pi/4): Q = 2/3 exactly, q-null
    w = c_rat(1, 1)
    v = vec_scal(MI, vec_add(UP, vec_scal(w, FP)))
    p = [c_mul(c_rat(F(1, 2)), a) for a in vec_add(v, sigma(c_rat(-1), c_rat(1), v))]
    assert herm(proj_s(p)) == herm(proj_d(p))                 # s^2 = |d|^2: null for q
    assert bil(p, p) == ZERO
    # invariant forms of the condition: |v|^2 = 3 |C(v)| and, for the pairing vector
    # n = a/|a| with a = a_A + lambda e^{i chi} a_B, |C(n)| = 1/(1 + lambda^2) = 1/3
    v0 = vec_add(UP, vec_scal(w, FP))
    assert herm(v0) == (F(9), F(0)) and c_abs2(bil(v0, v0)) == (F(9), F(0))


EXPORTS = {}
