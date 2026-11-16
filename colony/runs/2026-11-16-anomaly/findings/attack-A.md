# attack-A (angle A, constructive): run 2026-11-16-anomaly

Status: FINISHED (13:20). Three proposals filed, each with check4 exit 0 and no findings, validate_draft ok. Sections "routes", "choice" and "kill condition" of each problem were written before any
computation ran. Labels: proved / computed / argued / conjectured. Scripts: work/attack-A/.

My share: S2 (op.strong-cp), A2 + A3 (op.matter-asymmetry-origin), G1 (op.order-four-anomaly-and-sixteen).
Not mine (attack-B): S1, S3, G2, G3, anything adversarial.

## Orientation (direct lookups, done)
Read in full: the three problems; BRIEF, POLICIES, RUN, LEADS; REPORT and both attack files of 2026-11-12-asymmetry;
the order-four passages of 2026-11-09-three/bridges.md and 2026-11-09-bridges/attack-C2A.md, attack-C2B.md.
Stored entities read: synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them v1 (with check and
proof), synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix v4, standard-model.bidoublet-complex
v11, standard-model.one-vev-vector-relations-breaking-pattern v7,
synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase v4, neutrino.real-breaking-assumption v2,
dark-matter.premise-cpt-covariance v4, synthesis.flag-conjugate-antilinear-on-one-chirality-and-conjugation-reverses-jarlskog
v1, synthesis.imported-jarlskog-commutator-identity v2, the level-branch results (one-liners), the order-four entity.
Store searches: "monogenic", "Fischer", "eta invariant", "spherical Dirac": no hit. G1 is from scratch.

What is already stored and must not be refiled:
- clause (vi) of the abelian-charges claim: the five equilibrium conditions as the mirrors-composition check enters
  them, their kernel at (N_f, N_H) in {2,3} x {1,2}, the two values 28/79 and 8/23. Conditional, one doublet assumed.
- clauses (iii) to (v) there: B - L is broken by the Majorana element only; A_2(B - L) = 0.
- D = det[H_u, H_d] is reversed by entrywise conjugation and vanishes for real symmetric pairs.
- M_d = beta Y + conj(alpha) Y~, M_u = alpha Y + conj(beta) Y~ and the sum rules; one matrix (Y~ = Y) gives equal
  spectra and V = 1; balanced frame gives M_u = -M_d.

---------------------------------------------------------------------------------------------------------------

## S2. The phase of det(M_u M_d) on the stored quark structure (op.strong-cp, second attack item)

### Routes
R1 (the problem's own). Take the stored completion M_d = beta Y + conj(alpha) Y~, M_u = alpha Y + conj(beta) Y~
   and ask whether any stored statement (real breaking, the CPT premise's adjoint reading, the 10's symmetry, the
   one-type stages) fixes arg det(M_u M_d). Delivers: fixed / not fixed, and on which readings it vanishes.
   Fails if the stored data underdetermine the matrices (expected).
R2 (from another subject: the left-right literature the store already imports,
   synthesis.imported-left-right-bidoublet-two-yukawa-couplings). Hermitian family matrices with real vevs give
   Hermitian mass matrices and a real determinant with a free Jarlskog invariant (the parity mechanism). Test it
   against the stored requirement that the family matrices of a 10 are symmetric. Fails if Hermitian and
   symmetric together force real matrices (then J = 0).
R3 (my own). Treat (Y, Y~) -> (M_u, M_d) as a linear map with the 2 x 2 coefficient matrix [[alpha, conj beta],
   [beta, conj alpha]] of determinant |alpha|^2 - |beta|^2 = 2 m(c). If it is invertible off the balanced frame,
   the completion is no constraint at all on the pair of mass matrices, and the determinant phase is as free as
   in the Standard Model: a rescaling M_u -> z M_u, |z| = 1, keeps every mass and mixing datum and moves the
   phase by N arg z. Then classify the involutions of the pair (Y, Y~) the store's own conjugations supply
   (entrywise conjugation; the star that exchanges c and c*) and compute, for each, the determinant phase, the
   commutator invariant D and the spectra.
Choice: R3, with R1 as the reading of the result and R2 as one clause. Reason: R3 turns "is it fixed" into a
finite exact statement (an invertible linear map), and the classification by involutions answers "is it zero on
any stored reading" reading by reading.

### Kill conditions (registered before computing)
K-S2a. Claim: for m(c) != 0 the map (Y, Y~) -> (M_u, M_d) is a bijection preserving symmetric pairs, so the
   determinant phase is not fixed by the stored structure. Killed if the map is not invertible off the balanced
   frame, or if a stored statement, at its stored wording, restricts the phase (then I report the value it forces).
K-S2b. Claim: every stored reading on which the determinant is real is closed by stored data (real matrices: D = 0
   and cos phi = +-1, excluded; self-conjugate coupling Y~ = conj Y: equal up and down spectra, excluded by
   m_t != m_b). Killed if I find a reading compatible with symmetric family matrices on which a symmetry forces a
   real determinant with D != 0 and unequal spectra. That would be the positive half-result and I would file it
   as such.
K-S2c. Prediction, stated in advance: on symmetric one-type stages the determinant phase of the light blocks is
   2(arg y_u + arg y_d) + const while the Cabibbo phase is arg y_u - arg y_d, so the two are independent, and
   with the up-down phase at a quarter turn and one sector real the mass phase is a half turn. Killed if the
   exact 3 x 3 determinants do not follow this.
Expected outcome, stated in advance: negative. The series does not fix the mass phase.

### Established (final)
Proposal: synthesis.phase-of-the-quark-mass-determinant-on-the-covariant-completion
check4: 0 errors, 0 other findings; validate_draft ok; FILED (proposals/). Scratch: work/attack-A/s2.py.
Notation: Theta = det M_u det M_d, mass phase theta_M its angle in the I_4 plane, D = det[H_u, H_d].
- PROVED (K-S2a did not fire): for m(c) = (|alpha|^2 - |beta|^2)/2 != 0 the stored map (Y, Y~) -> (M_u, M_d)
  is a bijection, Y = (conj(alpha) M_u - conj(beta) M_d)/2m, Y~ = (alpha M_d - beta M_u)/2m, and it preserves
  symmetric pairs. So the completion constrains the pair of mass matrices no more than the Standard Model does:
  M_u -> z M_u keeps H_u, H_d (masses, mixing, D) and turns Theta by z^N. THE SERIES DOES NOT FIX THE MASS PHASE.
  At m(c) = 0: M_d = (beta/alpha) M_u, D = 0.
- PROVED: Theta is invariant under the hypercharge phase of the rung field, not under its common phase; the
  exchange (Y, Y~) -> (Y~*, Y*) conjugates Theta.
- PROVED, the readings with real Theta and what closes each: (a) real matrices: D = 0 (closed by the stored
  nonzero Jarlskog invariant and the stored exclusion of cos phi = +-1); this is what extending the real-breaking
  assumption to the quark matrices would give. (b) self-conjugate coupling Y~ = Y*: M_d = M_u* in every frame,
  Theta >= 0, D != 0, but equal up and down spectra (closed by m_t != m_b). (c) Hermitian matrices with a real
  frame (the left-right parity mechanism): Theta real, D != 0, unequal spectra; but Hermitian and symmetric is
  real, so for the symmetric matrices of a 10 it is (a).
- PROVED: for the stored stage textures, det(J + d(E + X)) = -3 d^2 x y + d^3 (q^2 - p^2) exactly, x y the
  product of the off-diagonal entries of the stored light-plane block. One-type symmetric stages, real first
  stages: Theta = (c_u c_d)^3 (d_u d_d)^2 (t_u t_d)^2 R, R > 0. So theta_M = 2(arg t_u + arg t_d) (+ half turn
  if c_u c_d < 0) while the stored up-down phase is arg t_u - arg t_d: independent (K-S2c prediction holds, with
  the sign of c_u c_d added, which I had missed when registering it).
- PROVED, the positive half-result (K-S2b FIRED IN PART: my registered claim that every real-determinant
  reading is closed by stored data is false): with one sector's stage coefficient real,
  Theta real <=> cos phi in {0, +-1}. The store excludes +-1 and selects |cos phi| < 1/2, so on this reading the
  determinant is real exactly at the QUARTER TURN, the value the stored Cabibbo result selects; there D != 0 and
  the spectra differ; theta_M = 0 if c_u c_d < 0, a half turn if c_u c_d > 0; off the quarter turn but inside
  the stored window theta_M is within a sixth of a turn of 0 or of a half turn, with |cos theta_M| > 1/2. The up
  matrix is then fixed by conjugation composed with the exchange of the first two families, and is the stored
  "twin" M_h P_12 of a Hermitian matrix; the down matrix by plain conjugation; one conjugation for both gives
  D = 0.
- ARGUED: this is a texture at tree level, not a symmetry of the coupled theory (the two sectors need two
  different conjugations), so nothing stored protects it against corrections; the sign is not fixed; the
  coefficient of the colour four-form is untouched. The adjoint reading of the CPT premise holds for every
  (Y, Y~) and constrains nothing.
- Answer to the three questions of S2: is it fixed: no. Is it zero on a stored reading: on (b) (closed), and on
  the quarter-turn reading with c_u c_d < 0 (open, one added premise). Is J != 0 compatible with a real
  determinant there: yes, on the quarter-turn reading; on the 10's symmetric matrices not through Hermiticity.
- Transport-absent. Literature from memory, not checked: Mohapatra and Senjanovic 1978, Beg and Tsao 1978 (parity
  and Hermitian matrices); that a half turn is excluded by the hadron spectrum.
Next step: S4 with attack-B's S1/S3 (no stored conjugation fixes the bare coefficient, no field relaxes it): the
physical angle is a free input unless Leon adopts the quarter-turn premise, which would fix only the mass phase.

---------------------------------------------------------------------------------------------------------------

## A2 + A3. The conversion coefficient and the conditional inheritance of B - L (op.matter-asymmetry-origin)

### Routes
R1 (the problem's own). List the equilibrium conditions species by species (the route of the stored check) and
   solve for general N_f, N_H. Delivers the closed form; adds little to stored clause (vi).
R2 (from the stored charge classification). An equilibrium assignment of chemical potentials IS a charge in the
   sense of the stored claim (six species numbers and the slot charge), and "interaction X is in equilibrium"
   is "the charge is conserved by X". So the equilibrium assignments are the stored conserved space
   span{Y, B - L} (Dirac terms, A_2 = 0, A_3 = 0 automatically), and neutrality is orthogonality to Y in the
   susceptibility form chi(X, X') = N_f tr(X X') on the fermions in the plasma plus 2 h h' per doublet component.
   Then c = n_B / n_(B-L) is a ratio of two Gram determinants. Delivers: the closed form as a theorem with every
   equilibrated interaction named, the broken-phase value by replacing Y by the electric charge (the stored
   remark that with the slot vector fixed the survivor is the electric charge), lepton-flavour blindness.
   Fails if the conserved space is larger than span{Y, B - L} for some stored coupling pattern (the second
   doublet coupling: a Peccei-Quinn charge would add a dimension).
R3 (my own, for A3). Completeness over mass forms, not over a list of channels: classify all 256 bilinear forms
   on the sixteen by colour, electric charge and B - L weight and show which neutral colour-singlet forms carry
   B - L.
Choice: R2 for A2, R3 for A3, merged into one proposal (the coefficient is the last clause of the inheritance
theorem). The doublet count is read from the stored level-branch results.

### Kill conditions (registered before computing)
K-A2. The Gram ratio must equal (8 N_f + 4 N_H)/(22 N_f + 13 N_H) for all N_f = 1..6, N_H = 0..6 and agree with
   the kernel of the five stored conditions. Any mismatch kills the structural statement. With independent slot
   charges h_v, h_w the conserved space must grow by exactly the colour-anomalous charge; if it grows by a
   colour-neutral one the doublet count is ambiguous and I say so. Broken phase: the same ratio with the electric
   charge and the W in the form must reproduce (8 N_f + 4(N_H + 2))/(24 N_f + 13(N_H + 2)) (literature value
   from memory, to be checked at source: Harvey and Turner 1990); if it does not, I report my value and the
   discrepancy.
K-A3. Killed if (a) one of the 45 bivectors is not a weight vector of ad(B - L), or a rung vector does not
   commute with B - L; (b) a colour-singlet, electrically neutral bilinear form on the sixteen with nonzero
   B - L weight exists other than the nu^c nu^c form (the Majorana element) and the nu nu form (weak triplet).
   If (b) finds a third form, the completeness clause is false and the form is reported.
Not attempted (rates): washout through the Majorana element, the 24 generators, the freeze-out temperature.
These enter as named premises with their literature source.

### Established
Proposal: synthesis.conditional-inheritance-of-b-minus-l-and-the-conversion-coefficient-as-a-gram-ratio
check4: 0 errors, 0 other findings; validate_draft ok; FILED (proposals/). A2 and A3 merged (the coefficient is the
last clause of the inheritance theorem). Named hypotheses of the theorem: (R) stored postulate; (W) no washout by
virtual heavy singlets, NOT stored and not implied by (R); (I) no injection (real breaking, stored postulate);
(N) the naming, stored; (A) the anomalous weak process, literature; (T) a thermal descent state above freeze-out.
Details (computed and then proved in the proposal):
- computed: K-A2 holds. With chi(X, X') = N_f tr_15(X X') + boson terms, c = [chi(B, B-L) chi(Y,Y) -
  chi(B,Y) chi(Y,B-L)] / [chi(B-L,B-L) chi(Y,Y) - chi(Y,B-L)^2] = (8 N_f + 4 N_H)/(22 N_f + 13 N_H) on the grid
  N_f = 1..6, N_H = 0..6 (28/79, 8/23). Entries per family: chi(Y,Y) = 10/3 (+ N_H), chi(Y,B-L) = 8/3,
  chi(B-L,B-L) = 13/3, chi(B,B-L) = 4/3, chi(B,Y) = 2/3.
- computed: state-level conserved spaces. Symmetric phase with the weak process: span{T_3, Y, B - L} (dim 3);
  broken phase (neutral slot component fixed): span{Q, B - L} (dim 2). Broken-phase Gram ratio with the W and
  the charged scalars in the form: (8 N_f + 4(N_H + 2))/(24 N_f + 13(N_H + 2)): 12/37 (one doublet), 10/31 (two).
- literature checked at source: Harvey and Turner 1990 (both closed forms, as quoted in hep-ph/0511059 eq. 13a
  and in Khlebnikov and Shaposhnikov hep-ph/9607386 eqs. (18), (19)); Khlebnikov and Shaposhnikov eq. (17): the
  interpolation (28 m_D^2 + 72 m_W^2)/(79 m_D^2 + 222 m_W^2); D'Onofrio, Rummukainen, Tranberg arXiv:1404.3565:
  crossover 159 +- 1 GeV, freeze-out of the weak process 131.7 +- 2.3 GeV, in the broken phase.
- argued: doublet count on the level branch is ONE at freeze-out (stored: second doublet at least about 2.5 TeV;
  freeze-out near 130 GeV), so c lies between 12/37 and 28/79, not 8/23. The two stored doublet couplings
  (Y on c, Y~ on c*) give both doublets the same charge under every conserved charge, so they count as
  multiplicity only when both are light.
- computed: K-A3 holds. The 40 off-diagonal mode bilinears are weight vectors of ad(B - L) (weights 0, +-2/3,
  +-4/3), slot vectors weight 0, T weight -2. Bilinear forms on the sixteen invariant under su(3) + u(1)_Q: 10;
  those with nonzero B - L: exactly two, nu^c nu^c (the Majorana element, weak isospin 0) and nu nu (weak
  isospin 1, not Standard-Model invariant).
- PROVED in the proposal, beyond the interim list: lepton-flavour independence of c (three charges B/3 - L_f);
  independent charges of the slot creation and contraction operators add exactly one charge, of colour
  coefficient 8 (the unit of the module minus 4 n_B, slot charge -2), which the colour anomalous condition
  removes: this is why the two stored doublet couplings count only as multiplicity. Agrees with attack-B's S3
  (no Peccei-Quinn charge).
- Value: (B - L)/s between (79/28) and (37/12) times 8.7e-11, that is 2.45e-10 to 2.68e-10; 8/23 is not the
  working-branch value. Where in the bracket needs v(T*)/T* (literature; not evaluated).
- NOT DONE: any rate ((W), the 24 generators); the heavy pair's split and widths; the mirror's ratio (hypothesis
  (T) fails there: degenerate plasma); completeness beyond bilinear terms of one family.
- Transport-absent (standard particle cosmology recast on the stored charges).
Next step: compute (W) (attack item (b)); evaluate c inside the bracket from the interpolation; the mirror.

---------------------------------------------------------------------------------------------------------------

## G1. The fixed-point count on real projective five-space (op.order-four-anomaly-and-sixteen, third item)

### Routes
R1 (the problem's own, the Lefschetz count). The fixed-point formula for the one nontrivial deck element:
   (1/2) 2^(-3) per Weyl field. Needs an index theorem with boundary; not in the store, not derivable there.
R2 (from the literature on spherical space forms). Quote the eta invariant of RP^5 (Gilkey). Import; excluded
   by Leon's decision of 9 November for the modulo-16 statement, and not a derivation.
R3 (my own; the run's proposed route). The spectrum directly. Spinor fields on S^5 as restrictions of
   polynomials on R^6 with values in the real eight-dimensional spinor space of Cl(0,6); the Fischer
   decomposition P_k (x) S = M_k + x P_(k-1) (x) S; the Dirac operator of the round sphere as
   D = -(x ^ d) - 5/2, with x ^ d = k on M_k and -(k + 5) on x M_k; the lift of the antipodal map by the volume
   element J of the six-space (J^2 = -1), paired with omega so that J omega is an involution, which makes the
   twisted spinors on RP^5 the fields of one parity on S^5; the spectral asymmetry as the Abel sum of
   sum_k (-1)^k 4 C(k+4, 4) t^k = 4/(1 + t)^5.
Choice: R3. Reason: every step except one is finite exact algebra, native to geometric algebra (the complex
structure is the volume element J; no imaginary unit), and the one analytic step can be isolated.

### Kill conditions (registered before computing)
Prediction registered in advance: the Abel sum is +-1/8 per Weyl component, so the invariant xi = eta/2 is
+-1/16, and n components give n/16.
K-G1. Killed if any of: dim M_k from an exact kernel differs from 8 C(k+4, 4) for k <= 3; x ^ d is not k on M_k
   or not -(k + 5) on x M_k; the connection d_X + (1/2) X n is not compatible with the Clifford map X -> X n;
   J fails to commute with D or to square to -1; J omega is not an involution; the Abel value and the value by
   Euler polynomials (the zeta-regularised sum) disagree. If the result is not an odd multiple of 1/16 the
   reading "sixteen from the fixed-point count" is dead and I report the true number.
What will not be proved, stated in advance: that the analytic continuation of the eta function at 0 equals the
Abel sum (one classical Mellin lemma), completeness of the polynomial eigenfunctions in L^2 (density of
polynomials), and that exp(2 pi xi) is the anomaly phase (literature; attack-B's G2).

### Established (final)
Proposal: synthesis.spectral-asymmetry-on-real-projective-five-space-from-monogenic-polynomials
check4: 0 errors, 0 other findings; validate_draft ok; FILED (proposals/).
K-G1 did not fire; the registered prediction (+-1/8, so +-1/16) holds.
- PROVED (exact checks, k <= 3): Fischer decomposition P_k = M_k + x P_(k-1) for S-valued polynomials on the
  six-space with Q(e_a) = -1, S the real 8-dimensional minimal left ideal of Cl(0,6); dim M_k = 8 C(k+4,4);
  d(xP) = -(6 + 2k) P; x ^ d = k on M_k and -(k + 5) on x M_k.
- PROVED: with the Clifford map X -> X n and the connection d_X + X n / 2 (compatibility verified), the Dirac
  operator of the unit sphere is D = -(x ^ d) - 5/2: eigenvalues -(k + 5/2) on M_k, +(k + 5/2) on x M_k,
  multiplicity 4 C(k+4,4) over span{1, J}. No matrices, no imaginary unit: the unit is the volume element J.
- PROVED: the rotors covering x -> -x are +-J, of square -1 (no spin structure on RP^5); J omega is an
  involution (checked in Cl(10,6)), equal to +1 on the half of S (x) V_+ where J acts as the module's unit; so
  the fields on RP^5 for the pair (A, omega) are the even S-valued fields on the sphere (odd ones for omega^-1).
- PROVED: generating function sum (-1)^k 4 C(k+4,4) t^k = 4/(1+t)^5, Abel sum 1/8; the Euler-polynomial
  (zeta-regularised) value is the same 1/8 for every shift tested. So eta(0) = -+1/8, xi = -+1/16 per Weyl
  component; n components: n/16; integer for sixteen, 15/16 for fifteen.
- ARGUED with classical analysis stated in the proof (not stored): completeness of the polynomial
  eigenfunctions (Weierstrass); the continued eta function at 0 equals the Abel sum (Mellin lemma; proof given).
- NOT CLAIMED: that exp(2 pi I xi) is an obstruction (the anomaly statement; literature; attack-B's G2). Without
  it the count constrains nothing; with it, sixteen passes and fifteen fails on a reading without the Majorana
  term.
- Cross-check at source (not a premise): Hsieh, arXiv:1808.02881, eq. (2.47) at m = 2, charge 1 gives
  (11 - 5)/96 = 1/16 mod 1 on S^5/Z_2, and the generator of the bordism group Z_16 of the Spin-Z_4 structure is
  that space: agrees. The same source confirms the stored remark on the lens space: the quotient by Z_m needs an
  internal element of order 2m.
- Transport-absent (classical spectral geometry). New for the store: the derivation, in geometric algebra.
Next step: G2/G3 (attack-B): the conditional statement and the tie to walls.

---------------------------------------------------------------------------------------------------------------

## Unexpected links
1. op.strong-cp <-> generations (and op.second-order-breaking, whose lead says the up-down phase is tied to the
   determinant phase). Exact form of the tie on one-type symmetric stages: mass phase = 2(psi_u + psi_d) (+ half
   turn), Cabibbo phase = psi_u - psi_d. They are independent in general; with one sector real the determinant
   is real exactly at the quarter turn the store already selects. A premise "exact quarter turn" would do two
   things at once: make the determinant real, and turn the stored Cabibbo relation into a prediction with no
   free phase, |V_us|^2 = (x + y)/((1 + x)(1 + y)), testable by the lattice mass ratios (the stored numbers:
   0.2226 at the N_f = 2+1+1 central ratios, inside the window; 0.2205 at the N_f = 2+1 ones, just below it).
2. The same quarter-turn up matrix is the stored "twin" (synthesis.one-type-second-stages-are-twins) of a
   Hermitian matrix: the left-right parity mechanism reappears on symmetric matrices, twisted by the exchange
   of the first two families.
3. op.matter-asymmetry-origin <-> op.strong-cp: the charge that would make the doublet count ambiguous in the
   coefficient (independent slot charges) is the colour-anomalous fourth charge, the would-be Peccei-Quinn charge
   of attack-B's S3. One fact, two uses: no relaxing angle, and both doublets count alike.
4. The conversion coefficient is a Gram ratio of the trace form on the fifteen; the stored remark that with the
   slot vector fixed "the survivor is the electric charge" gives the broken-phase value 12/37 by replacing Y by
   the electric charge in the same ratio.
5. G1 <-> walls (op.wall-class-invariant, attack-B's G3). The derivation does not use dimension six specially:
   on RP^(2m-1) the same steps give multiplicities 2^(m-1) C(k+2m-2, 2m-2), generating function
   2^(m-1)/(1+t)^(2m-1), Abel value 2^(-m), and the volume element of the 2m-space has square (-1)^m, so an
   order-four partner is needed exactly for m odd. Conjectured from the pattern, checked only for m = 3; it
   matches attack-B's statement that exactly one side of a real projective wall needs an order-four twist.
6. G1: with the pair (J, omega) the twisted fields are plain even functions on the sphere; the structure is a
   spin-c structure whose line is the order-four one. The store's remark that the quarter-turn lens space needs
   an order-eight element is the same mechanism (the rotor of the deck generator has fourth power -1).

## Decisions for Leon
S (op.strong-cp)
1. Registration (S4). With my S2 (mass phase free) and attack-B's S1/S3 (bare coefficient fixed by no stored
   conjugation, relaxed by no stored field), the physical angle is a free input of the series. Recommendation:
   register it, in the format of synthesis.matter-asymmetry-registered-free-input: "the physical colour angle
   (coefficient of the colour four-form plus the mass phase) is a registered free input, bounded by the imported
   neutron dipole bound; refuted by any in-framework derivation of it, or by a derived mass phase that the bare
   coefficient is shown not to cancel". New postulate: maintainer only; not filed.
2. Optional premise, yours to adopt or decline: "the quark stages are one-type symmetric with real first stages,
   one sector's second stage real and the other's at an exact quarter turn". It gives a real determinant with
   J != 0 (half a result, tree level, sign open: needs c_u c_d < 0 for the zero angle) and a parameter-free
   Cabibbo relation as its refutation condition. Recommendation: record it as a conjecture or question, not as
   a premise, until something supplies the quarter turn and the sign; it is not protected by a symmetry.
3. Do not extend neutrino.real-breaking-assumption to the quark matrices as worded: that is reading (a), closed
   by the stored Jarlskog invariant and the stored Cabibbo exclusion.
4. Literature to import or leave (cited from memory, unchecked): the parity mechanism (Mohapatra and Senjanovic
   1978; Beg and Tsao 1978); the exclusion of a half-turn angle by the hadron spectrum. The proposal uses
   neither as a premise.
A (op.matter-asymmetry-origin)
5. Imports the proposal's conditional clauses rest on (checked at source in this run): Harvey and Turner 1990,
   the two closed forms; Khlebnikov and Shaposhnikov 1996, hep-ph/9607386, eqs. (17) to (19), the interpolation;
   D'Onofrio, Rummukainen and Tranberg 2014, arXiv:1404.3565, freeze-out 131.7 +- 2.3 GeV below the crossover at
   159 +- 1 GeV. From memory, unchecked: 't Hooft 1976; Kuzmin, Rubakov and Shaposhnikov 1985; the washout bound
   (Fukugita and Yanagida 1990). Your decision of 12 November was not to import the process; the theorem is
   therefore stated as conditional on hypothesis (A).
6. assumes edges for the new claim (maintainer only): neutrino.r-descent-reheats-below-lower-heavy,
   neutrino.real-breaking-assumption, synthesis.matter-asymmetry-registered-free-input.
7. Two hypotheses are not in the store and the theorem names them: (W) no washout by virtual heavy singlets,
   which Premise (R) does NOT imply (its text says the descent's B - L is untouched, but that is the conclusion,
   not a bound on the second-order process); and (T) a thermal descent state reheated above about 132 GeV.
   Options: add them as premises, fold (W) into a restated Premise (R), or leave them as hypotheses of the
   theorem until the rate is computed. Recommendation: leave as hypotheses; compute (W) next.
8. The doublet count. Recommendation: restate synthesis.matter-asymmetry-registered-free-input from "none
   chosen" to one light doublet on the level branch, with (B - L)/s between 2.45e-10 and 2.68e-10 (28/79 is
   the symmetric-phase end, 12/37 the broken-phase end; the literature puts the freeze-out in the broken phase,
   so 28/79, which the stored mirror check uses, is the edge of the bracket and not its centre). Conditional on
   item 5.
9. The problem's status stays partial: this is the conditional theorem with named premises, not a completeness
   proof.
G (op.order-four-anomaly-and-sixteen)
10. The count 1/16 per component is now derived in the store's algebra. The one missing statement for "sixteen,
    not fifteen" is the literature's: that exp(2 pi I xi) is an obstruction (Dai and Freed; Witten; Garcia-
    Etxebarria and Montero; Hsieh, arXiv:1808.02881, whose eq. (2.47) I checked at source and which agrees with
    the derived value). You declined to import it on 9 November. The question is now exactly that one import,
    on a reading without the Majorana term; see attack-B's G2 for its side.
11. Two classical analysis statements are used inside the proof text (Weierstrass density on the sphere; the
    Mellin lemma for the value of the continued series at zero). Accept as proof text, or import as Facts.
12. Cross-check literature cited from memory in the note, not used as premises: the Dirac spectrum of round
    spheres (Trautman; Baer), eta invariants of spherical space forms (Gilkey).
