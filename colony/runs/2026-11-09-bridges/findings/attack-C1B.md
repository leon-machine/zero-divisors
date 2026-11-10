# Attack C1B (angle B, adversarial), run 2026-11-09-bridges, cluster C1

Labels: proved / computed / argued / conjectured / memory (literature from memory, unchecked). Status of this
file: PRE-REGISTRATION written before any computation of this run (orientation by lookup only).

## Pre-registered kill conditions and routes (written first)

### X1 finite averages against the Haar imports
Dependants of the two imports (lookup): synthesis.eviction-keeps-one-replica-saddle clause (iii), (iv) needs the
SECOND moment only (mean purity (m+n)/(mn+1)); synthesis.eviction-keeps-one-of-catalan-many-replica-saddles
clause (iii), (iv) needs EVERY moment n >= 2 (and the limit d^{n-1}<tr rho^n> -> C_n).
Routes: (a) the run's own: mean purity over the parity-preserving normaliser, n = 4; (b) from another subject:
F2 quadratic-form data of synthesis.signed-directions (the form b(S,T) = |S||T| + |S cap T|), the normaliser acts
through its isometries, design property = orbit structure on F2 vectors; (c) my own: attack the three places the
link can fail: (1) design order (third against fourth moment), (2) the tensor factorisation under parity
superselection (the even sector of modes A u B is not a tensor product), (3) the generating set (bivector
quarter turns alone against the full normaliser) and the scalar field (real algebra against span{1, unit}).
Choice: (c), with (b) as technique. Kill conditions I try to make fire, each a result either way:
 K1a "the fourth moment of the finite average equals Haar" (if equal at 1|1 qubits my claim of design order 3 dies);
 K1b "mean purity over the even sector for a mode bipartition equals Lubkin (dA+dB)/(dA dB+1)" (my prediction
     before computing: it is (dA+dB)/(dA dB+2), so the stored import is NOT what a superselected sector gives even
     though the design property holds there);
 K1c "bivector quarter turns alone are a 2-design on the even sector for every n" (prediction: holds at n = 4, 6
     by the accidents Sp(2,2) = S3, Sp(4,2) = S6, fails first at n = 8 with two orbits 28 + 35).
 The run's kill ("parity superselection breaks the 2-design property"): prediction, does not fire on a fixed
 sector for the full normaliser.

### X2 dark-tower running
Routes: (a) apply the stored 4d coefficients to each tower's content (sibling's job); (b) other subject:
dark-tower-matter.three-dimensional-phases already treats the 3d factors as dynamical Maxwell-Chern-Simons
fields; synthesis.common-ceiling-coupling-premise is the only stored source of "equal couplings"; (c) my own:
decide whether the stored coefficient formula b = (1/3) sigma w (n + 6 s) has any meaning off dimension four.
Choice: (c). Kill: "the stored import (heat-kernel Fact) gives a logarithm in odd dimension" (then running is
defined there and my objection dies). Second kill: "a stored premise gives equal couplings for the odd towers".

### X3 curvature coupling
Routes: (a) recompute B at the tilt window; (b) other subject: mass.mass-weight-dictionary and the three readings
in synthesis.tree-level-curvature-couplings-stay-blue (xi as a function of the conformal weight w) as a constraint
on the Sakharov zero; (c) my own: which field carries each xi_R; the stored tree-level value for the rung field.
Choice: (b)+(c). Kill for "one datum under three results": the stored statements name different fields, or the
store already fixes xi for the shared field (then it is not a free datum). Kill for my own lead "the unitary
weight range restricts the Sakharov zero to n_g in {3, 4}": the attachment's scalars are not densities of the
dictionary's kind (then the restriction is numerology and is recorded as such).

### X4 Majorana mass as tower pairing, and R5
Routes: (a) stored gap formula on a two-mode block; (b) other subject: quasi-spin of
synthesis.tower-pairing-gap-at-fixed-charges, standard-model.majorana-element ([B-L, T] = -2T); (c) my own:
show the exact obstruction (a pair term on one mode is zero; fixed-charge sectors have no matrix element) and
the minimal block on which the seesaw quadratic x^2 - M x - m^2 appears.
Choice: (c). Kill (the run's): pairing results hold only at fixed charges. Prediction: fires for the stored gap
theorem; the seesaw quadratic appears only on a doubled block (four modes) and with the bilinear, not the
quartic, pairing element. R5 kill: the recurrence test is on free null data where mass terms do not enter.

## Results (kept current)

### X1 (computed so far, 22:20; scripts work/C1B/x1_explore.py, x1_parity.py). FILING INTENT of C1B, so that the
### sibling does not duplicate: the NEGATIVE half only (order-four departure, parity-sector value, generator-set
### failure at eight generators). The positive design theorem (2-design or 3-design statement) is left to C1A.
- Stabiliser-orbit count (proved in outline: isotropic I_A, I_B and an anti-isometry between the quotients):
  #{L : rank 2^e} = Niso(a, a-e) Niso(b, b-e) |Sp(2e, 2)|. Checked by brute force at (1,1), (1,2).
- K1a did not fire: mean tr rho_A^n over the full normaliser orbit equals Haar at n = 2, 3 (a, b <= 6, exact) and
  differs at n = 4 everywhere tried: 13/20 against 22/35 at 1|1 qubits; 3/17 against 52/323 at 2|2. So the
  finite group is a design of order exactly three for these moments. Stored result touched:
  eviction-keeps-one-of-catalan-many clause (iii), (iv) for n >= 4 (the imported all-n Haar moments cannot be
  replaced by the finite average). At the crossing d^{n-1} <tr rho^n> tends to 2, 5, 16, 67, 374 for n = 2..6:
  the Galois numbers G_{n-1}(2) (number of subspaces of F2^{n-1}) in place of the Catalan numbers 2, 5, 14, 42, 132
  (computed to m = 12 in exact rationals; the limit identity is not proved).
- K1b did not fire: on the even sector the full parity-preserving normaliser reproduces the Haar moments OF THE
  SECTOR at n = 2, 3 (m = 2, 3, 4 modes, every split), and these are not Lubkin's: mean purity
  (dA + dB)/(dA dB + 2), proved by the two swap traces dA dB^2/4 and dB dA^2/4 on a sector of dimension dA dB/2.
  The run's kill (parity breaks the 2-design property) does not fire; what parity changes is the value, because
  the sector is (even x even) + (odd x odd), not a tensor product.
- K1c did not fire as predicted: bivector quarter turns alone give the full normaliser at 4 and 6 generators
  (orbits 3 and 15) and fail at 8: orbit 105 of 135 (the perfect matchings), mean purity 17/35 at 2|2 against
  4/9 (sector Haar) and 8/17 (Lubkin). Reason (argued, tied to the stored form q of blade squares): for m even
  P^2 = +1 and q descends to v-perp/v, the real algebra's unit-norm normaliser preserves q, orbits 28 + 35; for m
  odd P^2 = -1, P is a unit of the even subalgebra and the quartic partner of a bivector is P times a blade of
  square -1. So the run's "first computation at n = 4" sits in an accidental case.
- Mean entropy (computed): finite average (2/5) ln 2 < 7/25 against Page's 1/3 at one against one; at the
  crossing the deficit is about 0.85 ln 2 = 0.59 against Page's 1/2 (exact 3/5, 40/51, 921/1105 ln 2 at c = 1, 2, 3).
  A third import, singularity.imported-page-average-entropy-subsystem, cannot be replaced either.
- Proved for every split (double count of strings in families): moments two and three of the finite average equal
  Haar; sector mean purity (dA + dB)/(dA dB + 2).
- FILED: synthesis.finite-normaliser-averages-leave-the-haar-moments-at-order-four-and-on-a-parity-sector
  (check4 exit 0, no findings; validate ok; registered). Overlap with C1A to be merged by the orchestrator: my
  clause (ii) (agreement at orders two and three, proved by counting in the Fock setting with an adjoined central
  unit) is the positive statement C1A files in its own setting (even subalgebra with I^2 = -1). Not proved:
  the identification of the crossing limit with the subspace counts G_{n-1}(2) beyond n = 6 (the limit itself is
  proved to exist as phi sum_k 2^{(n-1)k - k^2}/phi_k^2); "moment four exceeds Haar" is computed for a + b <= 8.
  Next step: prove the q-series identity; decide whether the stored comparisons should say which measure they mean.

### X4 (script = the proposal's check). Kill (pairing results hold only at fixed charges) FIRES, and for Dirac
### masses as well.
- proved: Q(w) = 0, so one mode has no pair term; the stored mass block (composite-scalars (1)) is already a pair
  term mu w_a w_c of the two modes of one array. So every mass term is a pair term; "Majorana = pairing" does not
  single the Majorana term out.
- proved: every pair term shifts (N_a, N_c) by (-1, -1), so the fixed-charge gap theorem contains no bilinear
  mass term of either kind; its gap G n_b belongs to the quartic element. The seesaw is not "the stored gap".
- proved: charges. N: -2 on both; N_a - N_c and the grading: 0 on both; L (opposite on the two arrays): 0 on the
  cross (Dirac) term, 2 on the self (Majorana) term. The flip f_j -> -f_j on the two -k modes is an automorphism
  that turns the block into number-conserving hopping: number violation is relative to the charge.
- proved at K = 0: ad_H^4 - (M^2 + 2 m^2) ad_H^2 + m^4 = 0 (Pfaffian -m^2): energies solve x^2 - M x - m^2 = 0.
  C1A reports an independent agreement and an extension to K != 0 (not tested by me).
- R5: kill fires. The stored verdict uses the array count ("for every mass matrix", clause (i)) and the grading;
  [Gamma, pair] = 0 while [N, pair] = -2 pair. The 3 | n_g verdict is unchanged by a Majorana term; the lead that
  it "needs the number-current sector" is not supported by the stored statement (argued from the wording).
- FILED: synthesis.mass-terms-are-pair-terms-of-the-arrays-and-only-the-charge-separates-majorana-from-dirac
  (check4 exit 0, no findings; validate ok; registered). C1A does not file X4.

### X3 (not filed by me; arithmetic in scratch, exact). Kill "different fields" FIRES on the stored wording.
- computed: B = 16 n_g - 48 + 8(1 - 6 xi) over the stored window xi in [1.522584375, 1.548079215] at n_g = 3 is
  in [-66.31, -65.08]; zero at n_g in [7.068, 7.144]. The maintainer's figures reproduce. With the stored massive
  vector weight -(3 + 6 xi alpha) at alpha = 1 instead of -4 the same window gives B in [-165.8, -162.7]: the
  figure depends on which vector weight is meant.
- lookup, the exact place the link fails: the three appearances are three objects. (1) The Sakharov cancellation's
  scalars are the attachment's helicity-0 modules, conformal by construction (conformal energies k with
  multiplicity k^2; on the unit three-sphere R = 6 and l(l+2) + 6 xi = (l+1)^2 iff xi = 1/6). That is a property
  of the module, not a constraint on a field's action. (2) The rung field's doublets: the store ALREADY records
  xi = 0 at tree level (synthesis.tree-level-curvature-couplings-stay-blue clause (ii): "the stored actions give
  xi = 0 at tree level ... the rung field's D-term action"), and the Newton-coupling result's own example is
  B = 8, which is 16*3 - 48 + 8(1 - 0). So for the rung doublets the open problem's "fixed by none" is true only
  beyond tree level. (3) The tilt's scalar is no stored field: the stored result says a coupling in the window
  "would be a new premise".
- computed, conditional (my own lead, kill partly fires): if the doublets were densities of the stored
  mass-weight dictionary, the Sakharov zero xi = 1/6 + (n_g - 3)/3 lies in the unitary range only for n_g = 3
  (w = -1) and n_g = 4 (w = -3) in the first reading (xi = -w/6), only for n_g = 3 in the second
  (xi = -w(w+3)/12 <= 3/16), never in the third. The tilt window lies outside all three (stored). For one family
  of N_S scalars the window and a Sakharov zero are jointly solvable at integer n_g for no N_S <= 28 (first
  solutions N_S = 29, n_g = 18). This is arithmetic on a surface (alpha = 1, no graviton, sixteen components) with
  the answer three known in advance: numerology unless the doublets are shown to be such densities. Not filed.
- Where C1A is exposed on X3: "the attachment spectrum forces xi = 1/6" is true of the attachment module and is
  being read as a statement about a scalar field of the content; and the elimination n_s - 1 = 3 - sqrt(2 n_g - 5)
  identifies the pre-descent Kasner spectator with the weak-scale doublets and uses the isotropic point only.

### X2 (not filed by me). Kills: "logarithm in odd dimension" does not fire; "equal couplings for odd towers" does
### not fire (no such premise).
- lookup: the stored heat-kernel Fact gives the expansion in every dimension n but its logarithm clause (ii) is
  "in four dimensions" only. In dimension d the flat coefficient tr(E^2/2 + Omega^2/12) multiplies t^{(4-d)/2}:
  a regulator-dependent power in d = 5 (zero in a scale-free scheme) and an ultraviolet-finite term in d = 3.
  By the store's own standard (the Newton-coupling result: the Lambda^2 term depends on the regulator, the
  logarithm does not) the odd towers have no regulator-independent one-loop coefficient: "asymptotically free"
  has no meaning there. argued from stored wording plus standard dimensional analysis (memory for d = 5 being
  infrared free and non-renormalisable).
- computed (my derivation, agrees with C1A's): the stored rule b = (1/3) sigma w (n + 6 s) with n = d and s = -4
  gives (d - 26)/6 per unit Casimir for vector plus ghosts, -11/3 at d = 4, zero at d = 26 (a known coincidence
  with the critical dimension, memory, transport-absent); a spinor of N complex components gives N/3.
- lookup: dark-tower-matter.three-dimensional-phases already takes the abelian factors as dynamical with
  dimensionful e^2 and decides confinement by the Chern-Simons level (phases C and T), not by running; the only
  stored equal-coupling premise is synthesis.common-ceiling-coupling-premise, for the mirror tower alone, under
  which the mirror theory is isomorphic and the scale ratio is 1 identically.
- So the exact place the link fails: a scale ratio for the odd towers needs (a) the dimensionful coupling, (b) the
  free gauge-invariant bare masses (stored: every species has one), (c) a regulator or completion. None is stored.
  In a four-dimensional reading the five-dimensional content gives b_3 = -29/3 under (S), -31/3 without, against
  -7: more negative, but a ratio still needs alpha at a common scale and the thresholds.
- Where C1A is exposed on X2: a table of "field-strength coefficients in the tower's own dimension" is a table of
  heat-kernel numbers, not of beta coefficients; its signs do not decide confinement in d = 3 (decided by the
  level, stored) or d = 5.

## Where the sibling is exposed (summary)
X1: its design theorem lives on an even subalgebra with I^2 = -1; at 8 generators of Euclidean type the parity
operator squares to +1, the bivector turns reach 105 of 135 families and the mean purity is 17/35, so the positive
statement must name the adjoined or internal unit and must not be read as covering the Fock parity sector with
bivector turns only. It also cannot replace Page's average or the all-moment import. X3 and X2: above.
X4: not filed by C1A; its K != 0 extension is untested by me.

## Unexpected links
- The eviction results' radiation is flat of rank 2^{min(j,c)}: exactly the spectrum type of the finite
  average's states (every reduced state of a family is flat of rank a power of two). So eviction's state is a
  member of the finite ensemble, and the comparison "eviction against typical" has a third column, the finite
  average, between them at orders four and up (crossing coefficients 1, then 2, 5, 16, 67 finite, 2, 5, 14, 42 Haar).
- The crossing coefficients of the finite average are (computed) the numbers of subspaces of F2^{n-1}, the same
  binary linear algebra as the stored forms b and q of the signed directions; the Catalan numbers count
  non-crossing permutations. A proof would be a q-series identity
  phi sum_k 2^{jk - k^2}/phi_k^2 = sum_r binom(j, r)_2.
- Whether the algebra's own quarter turns suffice depends on m mod 2 through e_v^2 = (-1)^m and the descent of
  the stored quadratic form q to classes: a mod-8-type (Bott) dependence of the entropy averages on the number of
  directions, not previously linked to the tower clock. argued; only m = 2, 3, 4 computed.
- Mass terms: the store's NJL-type pairing block is a Dirac mass; the Majorana element T is separated from it by
  the B - L charge alone. The flip automorphism is the particle-hole map; it suggests reading (M) as a statement
  about which charge the descent keeps, not about a new kind of term. argued.
- The stored tree-level-couplings result (dark-energy) already fixes xi = 0 for the rung doublets, and the
  einstein result's B = 8 example agrees: op.curvature-coupling-across-subjects understates what is stored.

## Decisions for Leon
1. Merge or keep apart: my X1 clause (ii) (orders two and three agree) and C1A's positive design theorem state
   the same agreement in two settings. Recommendation: keep C1A's as the theorem, cut my clause (ii) to a
   cross-reference after acceptance (a proposal cannot cite a proposal now).
2. Should synthesis.imported-haar-average-purity be retired in favour of the derived second moment? Only the
   Renyi-2 comparison uses it. The all-moment import and Page's average must stay. Maintainer-only.
3. Do the eviction comparisons mean an abstract tensor product (as stored) or modes under a parity
   superselection? If the latter, the Haar column changes at order d^{-2} (2d/(d^2+2), bound
   ln 2 - ln(1 + 2 d^{-2})); leading terms unchanged. A choice of reading.
4. op.curvature-coupling-across-subjects: reword "fixed by none" (tree level fixes xi = 0 for the rung doublets;
   the attachment's value 1/6 is definitional; the tilt's scalar is not a stored field). Recommendation: restate
   the problem as "is there a loop-level or structural reason for xi != 0 on the doublets", or close the
   one-datum reading.
5. op.dark-tower-running: record that the odd towers have no regulator-independent one-loop coefficient and that
   a scale ratio needs three unstored inputs; the mirror ratio is 1 under the common-ceiling premise.
   Recommendation: narrow the problem to the four-dimensional reading or close attack item 3 as not posed.
6. Literature cited from memory in my two proposals (Webb, Zhu, Kueng and Gross on designs; Fattal et al. and
   Dahlsten and Plenio on stabiliser entanglement counts; Bravyi and Kitaev; Nambu and Jona-Lasinio): none is a
   premise; import as Facts only if wanted as prior-art references.
7. The open problem tags I used (op.island-dictionary for X1, op.pair-sector-current for X4) are the nearest
   existing ones; neither target has its own open problem. Maintainer may retag.
