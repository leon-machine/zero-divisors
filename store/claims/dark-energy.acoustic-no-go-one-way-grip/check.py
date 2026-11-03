"""dark-energy.acoustic-no-go-one-way-grip: exact checks on a finite window of the mode array, ported from
legacy verify_T10.py (prop:nogo, six-mode window) and widened to the operator statement itself.

Window: one complex fermion with modes k in {-5/2, ..., 5/2} (6 modes, Fock dimension 64, Jordan-Wigner
signs, exact Fractions), sea filled for k < 0 (the vacuum). Currents J_n = sum_k :a+_k a_{k+n}: over the
window (J_0 normal-ordered against the sea); the graviton modes are the Sugawara bilinears
T_n = (1/2) sum_m :J_m J_{n-m}: (|m|, |n - m| <= 3, positive modes to the right). L0 is the excitation
energy (diagonal), Q the charge. Charge conjugation C is the particle-hole reflection about the sea level,
C a_k C^-1 = a+_{-k}, built as a signed permutation of the Fock basis. States: the vacuum, and the diagonal
thermal state with weights x^(2 L0), x = 1/2 (invariant under U(1), C and the flow of L0); controls: a
chemical potential (weights x^(2 L0) y^Q) and a pure state superposing two charge sectors.
  (1) C is orthogonal and implements a_k -> a+_{-k}; C J_n C^-1 = -J_n, C T_n C^-1 = T_n; both states commute
      with Q and L0 and are C-invariant; the chemical-potential state is not.
  (2) phi(T_n O) = 0 for every n in {-2..2} and every charged probe (a_k, a+_k, a_k a_l, a+_k a+_l) and every
      C-odd neutral probe (J_m), in both states; controls: phi(T_n O) != 0 for C-even neutral O (T_{-n},
      J_1 J_-1), for the C-odd J_0 under a chemical potential, and for a charged probe in the superposition.
  (3) Conformal vacuum: <0| T_2 X |0> = 0 for states X|0> of L0 != 2 built from currents (levels 1, 3, 4),
      and != 0 at level 2.
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

KS = [F(-5, 2), F(-3, 2), F(-1, 2), F(1, 2), F(3, 2), F(5, 2)]
NM = len(KS)
DIM = 1 << NM
X = F(1, 2)
Y = F(1, 3)


def bit(S, i):
    return (S >> i) & 1


def ann(i):
    return fock.ann(i, NM)                 # LSB bitmask order, Jordan-Wigner sign


def cre(i):
    return fock.cre(i, NM)


mm = fock.mm
tp = fock.transpose


def madd(*ops, coeffs=None):
    if coeffs is None:
        return fock.madd(*ops)
    return fock.madd(*[fock.msc(c, A) for c, A in zip(coeffs, ops)])


IDX = {k: i for i, k in enumerate(KS)}
A_ = [ann(i) for i in range(NM)]
C_ = [cre(i) for i in range(NM)]
VAC = sum(1 << i for i, k in enumerate(KS) if k < 0)


def L0(S):
    return sum((k if k > 0 else -k) for i, k in enumerate(KS) if (k > 0) == bool(bit(S, i)))


def Qc(S):
    return sum(1 for i, k in enumerate(KS) if k > 0 and bit(S, i)) - sum(1 for i, k in enumerate(KS) if k < 0 and not bit(S, i))


def J(n):
    terms = []
    for k in KS:
        if k + n in IDX:
            terms.append(mm(C_[IDX[k]], A_[IDX[k + n]]))
    out = madd(*terms) if terms else {}
    if n == 0:
        out = madd(out, {(S, S): F(-1) for S in range(DIM)}, coeffs=[F(1), F(sum(1 for k in KS if k < 0))])
    return out


def T(n):
    terms = []
    for m in range(-3, 4):
        r = n - m
        if abs(r) > 3:
            continue
        terms.append(mm(J(m), J(r)) if m <= r else mm(J(r), J(m)))
    return madd(*terms, coeffs=[F(1, 2)] * len(terms))


def charge_conjugation():
    """C|S> for the basis state |S> = sign_S w(S)|vac>, w(S) = prod a+_k (k > 0 in S) prod a_k (k < 0 not in S)."""
    Cm = {}
    for S in range(DIM):
        ops, cops = [], []
        for i, k in enumerate(KS):
            if k > 0 and bit(S, i):
                ops.append(C_[i])
                cops.append(A_[IDX[-k]])
            if k < 0 and not bit(S, i):
                ops.append(A_[i])
                cops.append(C_[IDX[-k]])
        v = {(VAC, VAC): F(1)}
        w = {(VAC, VAC): F(1)}
        for o, co in zip(reversed(ops), reversed(cops)):
            v = mm(o, v)
            w = mm(co, w)
        (s_img, _), s_sign = next(iter(v.items()))
        assert s_img == S and len(v) == 1 and len(w) == 1
        (t_img, _), t_sign = next(iter(w.items()))
        Cm[(t_img, S)] = s_sign * t_sign
    return Cm


def thermal(chem=False):
    w = {S: X ** (2 * L0(S)) * (Y ** Qc(S) if chem else 1) for S in range(DIM)}
    Z = sum(w.values())
    return {(S, S): w[S] / Z for S in range(DIM)}


def expect(rho, Op):
    return fock.trace(mm(rho, Op))


VACSTATE = {(VAC, VAC): F(1)}


def probes():
    charged = [A_[i] for i in range(NM)] + [C_[i] for i in range(NM)]
    charged += [mm(A_[0], A_[4]), mm(C_[1], C_[3]), mm(A_[2], A_[3])]
    codd = [J(m) for m in range(-3, 4)]
    return charged, codd


def check_charge_conjugation_and_invariant_states():
    premise("dark-energy.imported-s-wave-current-algebra")
    premise("dark-energy.imported-conformal-orthogonality-sugawara-construction")
    Cm = charge_conjugation()
    Ct = tp(Cm)
    ident = {(S, S): F(1) for S in range(DIM)}
    ok = mm(Cm, Ct) == ident
    for k in KS:
        ok = ok and mm(mm(Cm, A_[IDX[k]]), Ct) == C_[IDX[-k]]
    for n in range(-3, 4):
        ok = ok and mm(mm(Cm, J(n)), Ct) == madd(J(n), coeffs=[F(-1)]) and J(n) != {}
    for n in range(-2, 3):
        ok = ok and mm(mm(Cm, T(n)), Ct) == T(n)
    for rho in (VACSTATE, thermal()):
        ok = ok and mm(mm(Cm, rho), Ct) == rho
        ok = ok and all(r == c for (r, c) in rho)            # diagonal: commutes with Q and L0
    ok = ok and mm(mm(Cm, thermal(True)), Ct) != thermal(True)
    ok = ok and L0(VAC) == 0 and Qc(VAC) == 0
    GA.check("C implements the particle-hole reflection, J -> -J, T -> T; the states are invariant", ok)
    assert ok


def check_graviton_blind_to_charged_and_c_odd_probes():
    premise("dark-energy.imported-s-wave-current-algebra")
    premise("dark-energy.imported-conformal-orthogonality-sugawara-construction")
    charged, codd = probes()
    ok = True
    th = thermal()
    for rho in (VACSTATE, th):
        for n in range(-2, 3):
            Tn = T(n)
            ok = ok and all(expect(rho, mm(Tn, O)) == 0 for O in charged + codd)
    # controls: C-even neutral probes couple; a chemical potential or a U(1)-breaking state breaks the no-go
    ok = ok and expect(VACSTATE, mm(T(2), T(-2))) != 0
    ok = ok and expect(th, mm(T(0), mm(J(1), J(-1)))) != 0
    ok = ok and expect(thermal(True), mm(T(0), J(0))) != 0
    S1 = VAC | (1 << IDX[F(1, 2)])
    sup = {(VAC, VAC): F(1, 2), (VAC, S1): F(1, 2), (S1, VAC): F(1, 2), (S1, S1): F(1, 2)}
    ok = ok and any(expect(sup, mm(T(n), O)) != 0 for n in range(-2, 3) for O in charged)
    GA.check("phi(T O) = 0 for charged and C-odd probes; controls nonzero", ok)
    assert ok


def check_vacuum_orthogonality_by_dimension():
    premise("dark-energy.imported-conformal-orthogonality-sugawara-construction")
    vac_ket = {(VAC, VAC): F(1)}
    states = {1: [mm(J(-1), vac_ket)],
              2: [mm(mm(J(-1), J(-1)), vac_ket), mm(J(-2), vac_ket), mm(T(-2), vac_ket)],
              3: [mm(J(-3), vac_ket), mm(mm(J(-1), J(-2)), vac_ket), mm(mm(mm(J(-1), J(-1)), J(-1)), vac_ket)],
              4: [mm(mm(J(-1), J(-3)), vac_ket), mm(mm(J(-2), J(-2)), vac_ket)]}
    bra = tp(mm(T(-2), vac_ket))                 # <0| T_2 = (T_-2 |0>)^dagger
    ok = True
    for h, kets in states.items():
        for ket in kets:
            ok = ok and ket != {} and all(L0(r) == h for (r, c) in ket)
            ov = sum((v for (r, c), v in mm(bra, ket).items()), F(0))
            ok = ok and ((ov != 0) if h == 2 and ket is kets[-1] else (ov == 0 or h == 2))
    ok = ok and sum(v for (r, c), v in mm(bra, states[2][2]).items()) == F(1, 2)
    GA.check("in the vacuum only dimension-two states overlap T", ok)
    assert ok
