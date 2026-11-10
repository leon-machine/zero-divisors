# bridges: run 2026-11-10-phase2 (bridge-hunter)

Read: attack-NA, attack-NB, attack-WB (complete), attack-BA, attack-BB, attack-WA (re-read after their results
sections were written, about 13:40). Store entities read directly under store/claims/. Scratch (outside the lab,
recomputations only, not evidence for the store): bridge.py (Cl(2,2), exact) and inv.py (Cl(3,3), exact) in the
session scratchpad. Labels: stored / computed / argued. Nothing here is proved; no proposal is filed.

## Links to relay

### L1. (P) on the horizon arrays is a consequence of (Q), and none of cluster B's open choices touches the count
Entities: singularity.q-joint-quasi-freeness-s-wave (v3), synthesis.premise-positivity-of-values,
synthesis.univalence-even-extension-split (iii), singularity.rate-discharge-hypothesis-iii,
synthesis.half-integer-weight-array-carries-half-ln2. Attackers: BA, BB (B2, B4), WA, WB (W3).
- stored: the KMS relation on a full mode factor fixes the marginal as the Gibbs state
  (univalence-even-extension-split (iii)); the gluing equation gives n = lambda (1 - n) with lambda > 0, so
  0 < n < 1 (rate-discharge-hypothesis-iii, as quoted in (Q)); (Q) makes the joint functional the gauge-invariant
  quasi-free one with those marginals.
- argued (three lines, classical): on a finite array, a linear normalised functional that is KMS at real beta for
  H = sum omega_k n_k is tr(e^{-beta H} x)/Z with no positivity assumed (e^{beta H} rho is central), and it is
  positive because the n_k are self-adjoint idempotents. So for (Q)'s functional the positivity clause of (P) is a
  theorem, not a further premise. It holds over an ordered field containing the Boltzmann factors (not over Q at
  the Hawking weights; with rational occupations it holds over Q).
- computed (bridge.py, Cl(2,2), occupations 1/3 and 1/5): the product functional is invariant under the mode-wise
  boosts v -> t v, w -> w/t (t = 4, 3/2), and its Gram matrix on the 16 blades is positive definite for the stored
  adjoint and for the boosted one; the stored rho = (1/4)(1 + e1)(1 + p2) is not invariant and is not real for the
  boosted adjoint. This agrees with BA's filed split result (number-diagonal functionals "contain all stored
  thermal products") and with BB's link (under the mode-wise average E_N, (P) is non-negativity of sector weights).
- Consequence across clusters (argued): the counted entropy sum_k s(beta omega_k) is the Shannon entropy of the
  weights omega(E) of that functional on the atoms prod (1 +- p_k)/2, p_k = e_k f_k (computed: each p_k has square
  one, is self-adjoint, even, and invariant under the mode-wise boosts; these are atoms of BA's B1 built from a
  commuting set of blades). The state is split-independent, the projectors are even and split-independent, and
  the state is E_N-invariant. So (1/2) ln 2 and the residue do not depend on which split is supplied, on whether
  odd elements are observables, or on which descent (mode-wise or total parity) is adopted. Cluster W's audit can
  say this in one sentence; cluster B can say that the horizon arrays are a place where (P) is derived and has no
  content beyond ordinary weights.
- Limits: this is not a derivation of (P). It says that a thermal premise (every value functional is KMS for a
  flow of dagger-automorphisms) implies positivity; BB's lambda_c and the box functional are KMS for no such flow.
  On the continuum (type III) positivity is presupposed, not derived: the stored positivity of (N+) is positivity
  of the null-translation generator on a GNS space, a different positivity
  (synthesis.positive-conformal-energy-gives-positive-null-translations).

### L2. The stored theorem "stationary implies even" sorts WB's three twists and bears on BB's record result
Entities: synthesis.univalence-from-even-stationary-dynamics (v5, clauses 3, 4), singularity.p-univalence,
WB's proposal synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter, BB's proposal
synthesis.records-keep-even-states-even-only-for-parity-homogeneous-observables. Attackers: WB, WA, BB, BA.
- stored: every state stationary under the flow of H = sum omega_k N_k is even if and only if no signed sum of an
  odd number of weights vanishes; it holds when all weights are odd multiples of one omega_0, and then the grading
  is the flow at time pi/omega_0; it fails at a zero weight and at an odd resonance (example weights 1, 2, 3, a
  stationary positive state that is not even).
- computed (one line of arithmetic): for weights proportional to k + delta, a signed sum of m of them is an
  integer plus (number of plus signs minus number of minus signs) delta, and for odd m that difference is odd. So
  odd resonances exist exactly when delta is rational with odd denominator. Twist 1/2 and twist 1/4: none
  (stationary implies even; univalence follows from stationarity). Twist 1/3: resonances exist, for example
  k = 0, 1, -2 with weights 1/3, 4/3, -5/3; by the stored clause 4 there are stationary positive states that are
  not even. So WB's point (sqrt(2/3), 1/3) is excluded by a stored theorem's hypothesis failing, with no appeal to
  the wording of (Q)'s parity clause: at that array univalence would be an independent premise. Twist 0 fails by
  the zero weight (stored). Worth one clause in WB's (iv) or a remark.
- argued: on an array of (Q) v3 the grading is the Killing flow at one modular period, so every element fixed by
  the Killing flow is even. With BA's formalisation of irreversible recording (record projectors fixed by every
  later evolution) the recorded observables on horizon arrays are even, which is the parity-homogeneous case of
  BB's record result, obtained from the dynamics and not from the reading "univalence holds after records". It
  does not hold at the zero offset ((Q) v2, flow the identity).
- Duplication warning for referees (stored): synthesis.univalence-even-extension-split (i) already states that
  omega o E is the unique even state agreeing with omega on the even part; BA's B2 lemma on the parity average
  and BB's descent clause should cite it and not restate it. Neither findings file lists these two entities.

### L3. The horizon count is a count of registered units, not of rungs (cluster N against the stored array results)
Entities: standard-model.trichotomy-what-kind-number (units sentence), tower.fock-module-one-qubit-per-rung,
synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping, synthesis.de-sitter-mode-count.
Attackers: NA, NB; WA for the number.
- stored: the trichotomy says "in the boundary modes' own units, qubits, one per rung of the Fock module, the
  horizon's capacity is pi N^2/ln 2 qubits". The residue result says, under (Q) v3: "The literal structural unit,
  one ladder pair, cannot carry the capacity at these weights, since no mode has zero weight", the units average
  two arrays "any unit sizes", "no premise fixes the grouping", and pi N^2/ln 2 "is therefore that of registered
  units, not of light rays". An array is an infinite band of ladder pairs carrying (1/2) ln 2.
- argued: so the number 4.8 x 10^122 counts bits of thermal capacity in units whose grouping is free, not rungs
  (ladder pairs) of a Fock module. Three consequences. (a) NA's clause (v) and N4 ("C pairs need C floors",
  "the horizon number is a mode count") and the suggested restatement of standard-model.why-large compare the
  count with pair counts of the tower: the stored array results do not license reading it as a pair count; only
  the state-count comparison (2^407 < C < 2^408) is neutral. (b) NB's integrality remark (K-N3b) takes "rungs
  counted by integers" as its premise; with units that average two arrays and a free grouping there is no stored
  integer, which supports NB's recommendation 2 on stored grounds. (c) The trichotomy's units sentence needs the
  qualifier "units of capacity ln 2" (a decision for Leon; it predates (Q) v3).
- stored, for RUN.md's bridge question on the normalisation: de-sitter-mode-count (ii) already states
  |J| = 4 pi kappa_c N^2 "whatever the residue". With kappa_c = 3/(4 pi) this is 3 N^2 exactly (WA P1 (v), NB
  link 4, NA link agree); N3's table is untouched because the count is defined from N. By WB's W4 the value 3 N^2
  is a counterfactual, since the continuum's entropy is not a consistent extension of the energy clause.

### L4. The split behind (P): what the store already holds, for BA's split proposal and NB's forms proposal
Entities: synthesis.positive-structure-is-twistor-form-at-imaginary-time (i), (ii), (iv),
synthesis.incidence-vacua-thermofield-real-capacity (iv), BA's proposal
synthesis.splits-adapted-to-the-null-pairs-and-the-states-common-to-all-of-them, NB's proposal
synthesis.invariant-forms-on-the-fock-module-and-the-pair-counts-of-a-next-level. Attackers: BA, BB, NB.
- stored: (iv) "a state for the adjoint of a Hermitian form exists if and only if the form is definite" and "no
  positive structure is preserved by a boost"; (i) the invariant Hermitian forms on the chirality half are the
  multiples of one form of signature (2,2). NB's clause (every form treating all vectors alike is neutral or
  alternating) and BA's clause (the null pairs do not fix the split) are the real-coefficient, any-rung versions
  of these. Both proposals should name the stored theorem as prior stored statement; referees will ask.
- computed (bridge.py, Cl(2,2), all 16 blades): the blade inverse is x -> B c(x) B^{-1}, c the Clifford conjugate
  and B the product of the generators of square +1. stored: the positive structure has h^{-1} Sigma = J =
  I_7 e_1 e_+, and e_1, e_+ are the two generators of square +1 of Cl(2,4). So the stored positive structure is
  the adjoint of the split in the sense of (P), with the same element B. This answers half of BA's decision 4
  ("are the h_m exactly the adjoints of splits") at the stored centre; for general m it is argued only (positive
  2-planes of R^{2,4} and the forward tube both have real dimension 8). BB's remark (in Cl(1,3) the blade inverse
  is gamma_0 x~ gamma_0) is the same formula with B = gamma_0.
- stored: thermofield (iv) says the beta = 2 pi condition on an incidence line "depends on the frame and scale
  fixed by the Hermitian structure, the dilation not being unitary for it". The ascent pair is n_0, n_inf/2, so
  BA's one-mode scale t on the ascent mode is the dilation. The unsupplied scale of the split is a unit of length.
- Verdict on candidate (2): link confirmed, but both ends were already found by the attackers (NB link 2, BA
  link 1). What is new is the stored anchor (iv), the formula for B, and the dilation reading of t.

### L5. WB's twists against the stored recurrence result
Entities: synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays (ii), (iv), WB's
proposal, WA's P2. Attackers: WB, WA.
- stored: clause (iv) there already carries the zeta sea at a general offset for a CCR array,
  -(kappa/2) B_2(delta), B_2(a) = a^2 - a + 1/6. computed (exact): WB's ground-test conic
  (delta - 1/2)^2 = (1 - r^2)/12 is B_2(delta)/2 = -r^2/24, the same polynomial with the fermionic sign; at the
  three passing points the sea phase over the array's own window is 1/24, 1/96, 1/36 of a turn. WB's proposal
  should cite the stored clause for the polynomial.
- computed: the half-arrays (spacing 2 kappa, twists 1/4 and 3/4) are the even-k and odd-k sublattices of the
  stored array (WA says the same from P2 (iii)); each has phase 1/48 per thermal period and (1/4) ln 2 (float
  check of the two sublattice sums), so the stored conditions 24 | n and 12 | n are unchanged when counted in
  entropy: 12 ln 2 either way. "Four per unit" is a regrouping covered by "fixes no grouping", not a rival count.
- Twist 1/3: one-window flow of order 3, sea phase 1/36 per own window, window incommensurate with the thermal
  period (r^2 = 2/3), so no recurrence at the modular period at all. No link to the stored orders 24, 12 or to the
  order-3 phase of one generation (that 3 comes from 16/24). Rejected as a structural link; see also L2.

## Links rejected

- Candidate (7), NB's triality lead. stored: no entity mentions Spin(8) triality or octonions (text search of
  all entity.md; the only "triality" is colour triality in two standard-model entities). computed (inv.py, exact,
  Cl(3,3)): the 15 bivectors have no common invariant vector in the 8-dimensional Fock module (joint rank 8),
  while the ascent's vector space V_3 + hyperbolic plane has a 2-dimensional invariant subspace. So (F_3, beta_-)
  and the vectors of rung four are inequivalent modules of the three-rung spin group: the invariant-form rule at
  three gives a Cl(4,4) that is not the stored ascent as an equivariant statement; an identification needs an
  outer automorphism that does not fix the three-rung spin group. What is true without triality (argued): F_3 with
  beta_- is a split 8-space polarised by its two chirality halves (stored:
  standard-model.imported-pair-systems-two-chirality-halves), on which the spin group acts through the polarisation
  group of a four-pair level, the classical coincidence of Spin(3,3) with SL(4). Relay to NB and NA as a negative:
  NB's decision 5 can be closed as "not the ascent; a parallel construction".
- Candidate (3) as an identity of numbers. The Gibbs weights are Born weights of the array's state on a stated
  projector family (kept, inside L1), but there is no link between BA's rational weights of sharp states and the
  value (1/2) ln 2: the array state is mixed, its weights at the Hawking point are not rational, and B1's
  uniqueness says nothing about which mixture. Z = sqrt 2 for one array against the adjoined sqrt 2 of the
  Tsirelson state: (theta_3/eta)^3 = 2 sqrt 2 at the self-dual point is an identity of theta constants; no
  structural link found; coincidence as far as tested.
- Candidate (4) as a constraint. No stored relation ties the unit per Planck area to N; the count scales as N^2
  for every residue (stored), so nothing in cluster W moves N or NA's independence statement. Kept only as L3.
- Candidate (6) beyond L2. "The parity average is a time average over the modular period" is stored already
  (univalence-from-even-stationary-dynamics, clause 3); no new statement about B's mixed-parity value 14/5: that
  uses a pair state, which is not stationary under a horizon flow and is outside L1.
- The split's scale against N. The scale t of the split is moved by the dilation (L4), and NA and NB show the
  full dilation fixes N. So the split supplies a unit of length and no dimensionless number; it cannot bear on N.
  Not audited over the cone.
- WB's Pell remark (m^2 - 3p^2 = 1 against the phase 1 denominator law X^2 - 2Y^2): different forms, no common
  stored object; WB claims none; none found.
- The flag as supplier of the split: rejected by BA and BB (argued) and by the stored classification (tube
  points, not a sign of J); nothing to add.

## Not done
No cone audit; labcli not used. L1's classical statements (KMS uniqueness on a matrix algebra, positivity of
quasi-free functionals with occupations in [0,1]) are from memory. The identification of all h_m with adjoints
of splits is argued by a dimension count only. BA's and BB's proposals were not read, only their findings.
