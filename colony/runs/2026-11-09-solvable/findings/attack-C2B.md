# Attack C2B (angle B: cross-pollinating, adversarial), cluster C2

Status: two proposals filed (Koide; Higgs-sector BRST pattern). No filing on (a) Virasoro or (c) the sign bit (C2A's).
Scripts: colony/runs/2026-11-09-solvable/work/C2B/.

## Pre-registered kill conditions (written before computing)

T1 op.qft-non-abelian-gauge-fields (a), Virasoro of the Sugawara parts.
- Adversarial conjecture A1: on a finite window no operators L_m (any definition) satisfy the Virasoro relations with
  the stored central values; the window Sugawara parts fail even the sl(2) relation [L_1, L_-1] = 2 L_0.
  KILL A1 if the trace argument fails (some window realises [L_1, L_-1] = 2 H_f exactly on the whole window space).
- Adversarial conjecture A2: the remainder's 52/7 is not a central charge (the coset part fails Virasoro on localised
  vectors or fails to commute with the factor currents). KILL A2 if the coset part satisfies [L_m, L_n] =
  (m - n)L_{m+n} + (52/7)(m^3 - m)/12 delta on the localised vectors where the stored split holds (GKO expects this).

T2 op.qft-non-abelian-gauge-fields (b), Higgs-sector BRST.
- Adversarial conjecture B1: s phi = -g c.phi is nilpotent only under a condition on the vacuum, or fails with two
  doublets. KILL B1 if s^2 = 0 on phi holds identically for every vacuum value and for two doublets (exact check).
- Adversarial conjecture B2 (survives B1 if it dies): the field-level BRST complex with the 't Hooft-Feynman gauge does
  not select the breaking pattern: a charge-breaking two-doublet vacuum gives an equally consistent complex (A-G mixing
  cancelled, ghost mass matrix = vector mass matrix) with Goldstone rank 4. KILL B2 if for some charge-breaking vacuum
  the mixing does not cancel or the ghost and vector mass matrices differ.

T3 op.hypothesis-s, last item (joint Clifford clause versus the sign-bit postulate).
- Adversarial conjecture S1: clause (f) asks more than (F2) for the ten Majorana generators (the adjoint or the
  signature are extra). KILL S1 if (a) the signature is fixed by the two separate CAR systems, and (b) the Fock adjoint
  is the unique (up to scale) inner product making the finite group of signed directions unitary (average + Schur).
- Adversarial conjecture S2: the abstract sign-bit structure cannot see the clause: the untwisted generators generate
  a group isomorphic to the twisted one. KILL S2 if the two groups (order 2^11) are not isomorphic.

T4 op.gram-square-and-face-space, attack item 1 (quark Koide, class D2 > D3 > D1).
- Conjecture K: in the class D2 > D3 > D1 a Koide bracket needs D3/D1 at least R1* with R1* > 7 (down, stored values)
  and R1* > 1000 (up, own-scale values), and in the up sector such a bracket has b_u > b_c, so a dressing that keeps
  the mass order within a sector excludes the class there. KILL K if R1* < 7 (down) or < 1000 (up), or an up-sector
  Koide bracket in the class with b_u <= b_c exists.

## Results

### T4 Koide (op.gram-square-and-face-space item 1): FILED
Routes: (1, problem's own) test the class D2 > D3 > D1 directly with the stored lemma; (2, other subject: the
light-cone/nullity reading of Koide, families.koide-nullity-condition-one-member-invariant) a parameter-free necessary
condition on Koide triples from the cone geometry; (3, own) a universality argument (QCD flavour-blind: one dressing
function F(b) for all six quarks, monotone), dropped: monotone F alone constrains nothing beyond order preservation.
Chosen: 1 + 2. Established (proved, exact, certified with rational root bounds; all masses stored quantities):
- (proved) Middle-mass bound: every Koide triple has middle entry >= (17/2 - 6 sqrt 2) = 0.01472 of the largest,
  equality iff the two smaller coincide (t* = 3/sqrt2 - 2 root of 2t^2 + 8t - 1).
- (computed) m_c/m_t = 0.00738 (own scale), 0.00361 (M_Z): below the bound, so no (x <= m_c, m_c, m_t) is Koide for
  any x; every up Koide bracket with D_c >= D_t has b_u > b_c; order-preserving up bracket needs D_t/D_c >= 1.995
  (own), 4.08 (M_Z). Down passes (m_s/m_b = 0.022, 0.019).
- (proved) The stored (iv) DOES cover the class D2 > D3 > D1 (its proof allows any rho_j in (0, R]); the stored formal
  sentence saying it does not is a misstatement. Sharp class thresholds: D3/D1 >= R_1 in (7.88, 7.89) down own,
  (11.00, 11.01) down M_Z, (2010.2, 2010.3) up own, (4799.8, 4799.9) up M_Z; class D1 > D3 > D2: D3/D2 >= 2.19, 2.63,
  9.36, 19.33. Both classes contain Koide brackets (certified sign changes), so thresholds, not exclusions.
- (proved) No ordering escapes: max_j D3/Dj >= R* in every class, least only at D1 = D2.
- (argued) Data plus store cannot decide whether quark brackets satisfy Koide: no stored dressing law.
Kill condition K: did NOT fire (R_1 = 7.886 > 7 down; 2010 > 1000 up; up bracket order reversed in the class).
Proposal: synthesis.koide-middle-mass-bound-closes-the-remaining-quark-dressing-class.
Gate: runcheck 4/4 pass; check4 exit 0, 0 errors, 0 other findings (W413 fixed by pinning sample values); validate_one
ok, no codes (I305 info only); registered with propose_claim, files identical, coverage.yaml copied, check4 rerun on
proposals/ clean. Ledger: transport-absent.

### T2 Higgs-sector BRST (op.qft-non-abelian-gauge-fields item b): FILED (adversarial part only)
Routes: (1, problem's own) s phi = -g rho(c) phi on the two doublets, test s^2 against the vacuum; (2, other subject:
the rung field's orbit space, synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus) read the Goldstone
rank on the lift locus; (3, own) an independence pair: two gauge-invariant quartics, same BRST data, different
patterns. Chosen: all three (one proposal). Established (doublets as even elements of Cl(3,0), weak left, hypercharge
right; exact):
- (proved) s^2 Phi = 0 for every Phi and v (representation property): B1 kill FIRED, no vacuum condition for s.
- (proved, adversarial) the free part s_0, which the stored quartet construction quantises, is a symmetry of the
  quadratic 't Hooft-Feynman action iff rho(X) grad V(v) = 0 for all X, i.e. (no invariant vector on two doublets)
  iff v is stationary; off it s_0 S_2 = -s_1 S_1 = g <grad V(v), rho(c) h> != 0 (pinned example).
- (proved) Goldstone rank 0 / 3 / 4; rank 3 iff Phi != 0 and K' = 0 (aligned over span{1, e12}); K + K' = N1 N2;
  checked on all 3^8 small-integer pairs (1 / 672 / 5888).
- (proved) Counter-model pair: V = (N1+N2-w)^2 + (N1-N2)^2 + kap K; kap = -1, w = 3/2: global minima aligned (rank 3,
  27 + 5 physical modes), kap = +1, w = 2: global minima charge-breaking (rank 4, 28 + 4), e.g. (1, e23). BRST
  structure intact in both (quartet positivity per mass eigenvector, argued from the stored (ii), (iii) + (i)).
  B2 kill did NOT fire: the BRST construction does not select the pattern.
- (proved) Lift locus: phi2^dagger phi1 = Q(c) = -H^2 forces K = H^4, N1 N2 = H^4 + K'; rank 3 exactly on the stored
  charge-preserving boundary, 4 inside, never 0 (no unbroken electroweak phase); the D-term vacuum (stored) is on the
  boundary, so there the potential derives the neutral pattern.
Proposal: synthesis.higgs-sector-brst-does-not-fix-the-breaking-pattern-of-two-doublets.
Gate: runcheck 6/6 pass; check4 exit 0, 0 errors, 0 other findings (W413 fixed by pinning the obstruction matrix);
validate_one ok, no codes (W215 fixed by citing synthesis.rung-field-on-the-lift-locus in the proof); registered,
files identical, coverage.yaml copied, check4 rerun on proposals/ clean. Ledger: transport-absent.
Overlap note: C2A registers nilpotency, exactness and the 't Hooft mixing for general v; my proposal states s^2 = 0 in
one line (needed for (iii)) and is otherwise the vacuum condition, the rank theorem and the independence pair. If the
orchestrator judges (i) duplicated, the first sentence of (i) can be cut to a citation once C2A's is accepted.

### T1 Virasoro (item a): not filed (C2A's); adversarial results offered
- A1 (proved, elementary; offered to C2A as a clause): on any finite window no operators satisfy even the sl(2)
  relation [L_1, L_-1] = 2 L_0 with L_0 = H_f: the trace of a commutator is 0, while tr H_f > 0 (H_f is a positive
  sum of J* J terms and squares of Hermitian zero modes, nonzero). Even with any other L_0, the traces of
  [L_1, L_-1] = 2 L_0 and [L_2, L_-2] = 4 L_0 + (c/2) 1 force tr L_0 = 0 and then c dim = 0, so c = 0. So the
  relations with c != 0 can hold at most on the band
  domain D (or on localised vectors), never as window operator identities: the defect on a window has trace
  -2 tr H_f (m = 1). A1 kill did NOT fire.
- A2 (literature, not computed): GKO makes so(10)_4 / (su(3)_4 + su(2)_4 + u(1)) a Virasoro of c = 15 - 32/7 - 2 - 1 =
  52/7 once the so(10) and factor Sugawara Virasoro hold on D; C2A's kill K-a tests exactly this. Adversarial
  expectation: A2 kill fires (52/7 is a central charge on D). Not computed here to avoid duplication.

### T3 sign bit (op.hypothesis-s last item): not filed (C2A's)
My S1 (adjoint by averaging over the finite group of signed directions plus Schur on the irreducible 32) and S2 (the
untwisted central product 2^{1+4} o 2^{1+6} is extraspecial of the same type, so isomorphic to the twisted group:
the abstract sign-bit structure cannot see clause (f); its content is which ten operators are the directions) are
C2A's routes 1 and 2. Signature: fixed by the two separate CAR systems (five of square +1, five of -1 over the reals;
any signature over span{1, I4}); adds nothing. Expected outcome: S1 kill fires (clause asks nothing beyond (F2) for
the given ten Majoranas), S2 kill does not fire. Not computed.

### Split with C2A (read midway)
C2A takes (a) Virasoro on D (with GKO for 52/7), (b) nilpotency, exactness and 't Hooft mixing for general v, (c) the
sign-bit reading of clause (f) including the central-product route (my S2) and the adjoint (my S1). I do not file on
(a) or (c). On (b) I file only the part C2A does not register: the vacuum condition at quadratic order and the
independence of the breaking pattern (charge-breaking counter-model, Goldstone rank, rung lift locus).


## Unexpected links
- The quartet result's input (the neutral aligned vacuum of two doublets) and the rung field's orbit space are one
  structure: on the lift locus the Goldstone rank is 3 exactly on the stored charge-preserving boundary
  (Cauchy-Schwarz equality for phi2^dagger phi1 = -H^2), so the D-term result is where the store derives the
  breaking pattern; BRST cannot.
- Koide's light-cone reading (families.koide-nullity-condition-one-member-invariant) gives a parameter-free necessary
  condition, middle >= (17/2 - 6 sqrt 2) largest, which the up quarks violate at c/t alone: the up sector's failure
  is independent of m_u, the down sector's is not (m_s/m_b passes).
- Stored misstatement: synthesis.mass-ordered-dressing-cannot-spoil-koide (formal, last sentence of (iv)) says (iv)
  does not treat D2 > D3 > D1; its own proof covers it.

## Decisions for Leon
1. Koide for quarks (op.gram-square-and-face-space item 1): with the filed result every ordering of the dressing
   factors needs a dressing favouring the heaviest quark (>= 1.88 down, 8.67 up over both lighter; in the class
   D2 > D3 > D1 >= 7.88 down, 2010 up over the lightest, with the up and charm brackets reversed). Recommend: close the
   attack item as decided-negative-for-QCD-dressing and drop the selectivity account for quarks
   (families.selectivity-observation-level stays a conjecture about leptons only), unless a heavy-favouring dressing
   law is proposed as a premise. The data alone cannot decide it (every class contains Koide brackets).
2. Maintainer wording fix (routine): the last sentence of (iv) in synthesis.mass-ordered-dressing-cannot-spoil-koide
   ("Neither (ii) nor (iv) treats ... D2 > D3 > D1") should read that (iv) covers the class with R = D3/D1 and that
   the sharp class bound is in the new proposal.
3. Higgs-sector BRST: record in op.qft-non-abelian-gauge-fields that the breaking pattern cannot come from the BRST
   construction (both patterns are BRST-consistent) and that the stored quartet input must be a stationary vacuum;
   the derivation of the pattern is a question about the series' potential (on the lift locus the D-term derives it;
   with an added invariant W(N) the global minimum is open, as stored). No new premise proposed.
4. Prior art cited from memory in the BRST proposal (BRS/Tyutin, Fujikawa-Lee-Sanda, Ferreira-Santos-Barroso,
   Ivanov): not used as premises; import as Facts only if Leon wants them recorded.
