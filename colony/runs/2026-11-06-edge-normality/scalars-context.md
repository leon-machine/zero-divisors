# Results of the 6 November scalars session (Leon's doc "Scalars and the Continuum: Review and Extensions")

Context for filer S. These were computed in a scratch workspace with exact rationals (Fractions, a
bitmask Clifford implementation equivalent to GA.py) and are NOT in the store. Re-prove and re-check
each one with lib/GA.py before filing. Literature named here is from memory unless marked verified.

## File candidates (check each against the store for duplicates first)
R1. Directional skeleton as an F2 quadratic form. Index blades by subsets S of the n directions
    (Z_2^n under symmetric difference); q(S) = 1 iff e_S^2 = -1. Its polar form is the
    anticommutation form; the vee (Salingaros) group is the central extension of Z_2^n by Z_2 that q
    classifies. n even: Arf(q) = 0 iff Cl(p,q) is a real matrix algebra (p-q = 0,2 mod 8), Arf = 1
    iff quaternionic (p-q = 4,6 mod 8); checked for all 24 signatures with n = 2,4,6,8. n odd: the
    radical of the polar form is {empty, full set} (the pseudoscalar = centre) and q on it gives the
    sign of I^2. Likely known in the literature (Salingaros; Lounesto): say so, transport-absent
    unless tied to a series result.
R2. The -1 from symmetry: generators with e_i e_j = c e_j e_i for one central c, the same for all
    pairs; symmetry c_ij = c_ji forces c^2 = 1; c != 1 for distinct directions; the centrality of the
    self-residues e_i^2 then follows and uses exactly c^2 = 1. (Small; perhaps merge into R1.)
R3. Integral orders of the (1,1) plane. Witt pair a, a' (a^2 = a'^2 = 0, {a, a'} = 1) generates
    M_2(Z), the maximal order, with integral idempotents a a' and a' a summing to 1. The orthonormal
    pair e_+, e_- (squares +1, -1) generates an index-4 suborder of M_2(Z) with no idempotents
    ((1 +/- e_+)/2 needs 1/2). The two agree after inverting 2 (quadratic versus bilinear form).
    Compare with transport.regularity-localises-zero-divisors-idempotents and
    one-relation.two-presentations before filing.
R4. Morita ascent and the quaternionic kernel. Cl(p+1,q+1) = M_2(Cl(p,q)); along the (p, p+2)
    chain every level has p - q = 6 mod 8, so every level is M(H) and every even part M(C) (checked
    p = 1..4). The anisotropic kernel (0,2) has Clifford algebra H = Cl(0,2) (e1, e2, e1 e2 all square
    to -1), not C; gamma_2 gamma_1 is its unique even unit imaginary up to sign; I_4, I_6, ... generate
    the centre of the even part (C) and the generator moves only under the naive inclusion.
    Compare with tower.grade-twist-when-it-inner and one-relation.two-presentations first.
R5. Limits as null steps (four exact facts):
    (a) Cl(0,0,1): f(x + e) = f(x) + f'(x) e for every function built algebraically; checked on
        (x^3 + 3x)/(x^2 + 1).
    (b) N commuting square-zero b_i (each a product of two degenerate directions in Cl(0,0,2N), or
        of two Witt null directions in Cl(N,N)): prod (1 + b_i) = exp(sum b_i) exactly, and
        eps^k = k! e_k(b) for eps = sum b_i; checked N = 2..6 (and N = 3 in Cl(6,6)).
    (c) Cl(1,1): a boost with nilpotent rapidity d sends l+ = e_t + e_r to (1 - d) l+; the boost
        with cosh = 5/4 scales l+ by exactly 1/2.
    (d) Rotor square roots R_{k+1} = (1 + R_k)/|1 + R_k| from the half-turn rotor stay in the
        Euclidean field (nested square roots of 2); 2^{k+1} |<R_k>_2| < pi < 2^{k+1}|<R_k>_2|/<R_k>_0;
        the gap times 4^k tends to pi^3/8 (numerical, proof text only). tan and arctan Taylor
        coefficients have only odd denominators (checked to degree 21); exp's have every prime.
    Checks with irrational quantities must stay exact (work in Q(sqrt 2) towers symbolically, or
    check the polynomial identities the tower satisfies); pi bounds are proof text, not check.
R6. The Witt partner is a generalised inverse. n m n = n, m n m = m, {n, m} = 1; with the CAR
    adjoint it is the Moore-Penrose inverse. Derivative without a degenerate direction:
    m (f(x + n) - f(x)) = f'(x) P with P = m n idempotent, integral in M_2(Z) (checked on 2x^3 + 5x).
    Semisimplification as the transport ascent: a degenerate direction has no generalised inverse;
    adding its partner makes the algebra semisimple, hence von Neumann regular. Compare with
    descent-lift.pairing-creator-under-transport-algorithm (Moore-Penrose) and
    transport.regularity-localises-zero-divisors-idempotents first: this may be a restatement.

## Do NOT file (record in findings only)
R7. I_4 gamma_0 gamma_3 = gamma_1 gamma_2 in Cl(1,3) (pi from the kernel; Bisognano-Wichmann
    reflection as I_4 times the transverse pi-rotation): attackers A and B of this run may use it.
    If neither files it by the end, list it as a candidate in your findings.
R8. Uniqueness of the continuum: half-sided modular inclusion with unique vacuum forces type III_1
    (Longo; Wiesbrock); hyperfinite III_1 unique (Connes; Haagerup); R_{1/2} tensor R_{1/3} is III_1
    because log 2 / log 3 is irrational (Araki-Woods). Literature: decisions for Leon (import as Facts).
R9. Speculative: the Hurwitz order of the kernel H = Cl(0,2) needs 1/2, contains
    (1 + g1 + g2 + g1 g2)/2 (cubes to -1), has 24 units, A_4 modulo sign; A_4 has no S_3. Record as a
    lead only.
