# Fix round FX3: referee F3's findings (run 2026-11-07-consistency)

Entities: referee_F3.txt (10). Every finding was recomputed exactly (lib/GA.py, lib/gtg.py, Fractions; scratch in
/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/FX3/). Versions: all ten were already at
lock + 1 in this run and were kept. Each changed entity has a credit entry (source "maintainer pass 2026-11-07 (GTG
review fixes)"), an `extraction.maintainer_pass_gtg_review` note and, where pins moved, a
`maintainer_pass_pin_review` note. No status, assumes edge or formal mathematics changed.

Counts: 21 findings/items. Applied 19, disputed 0, for Leon 2 (8a formal, 5b c != 0). 22 stale pins reviewed: 15 N, 7 R
(all repinned, the use holds); 0 left. Uses edges added: 6 (all to proved or imported targets; holds_given unchanged,
computed). Checks: 2 new functions, 2 tightened, 2 docstrings; runcheck all pass; check4 0 errors on proposals copies of
the five changed checks (copies deleted). `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon`:
0 errors, 0 warnings (two runs).

## Per finding

- **Docstrings (pairing.curvature-which-loops-move-vacuum, pairing.loop-classes-are-weyl-components).** Applied: the
  bare i in m = e2 + i e3 (and the classes i M/r^3) is now I5, named as the central unit of Cl(2,3). runcheck 5/5, 4/4;
  check4 clean.
- **2a (loop-classes, citation).** Applied. The symmetry of W is now cited as the pair symmetry of the Riemann tensor that
  calR reads by dictionary (iv), in GA a consequence of the first Bianchi identity; trace-freeness to (v). Checked: the
  Bianchi-free linear maps on Cl(1,3) bivectors form a 20-dimensional space, all symmetric.
- **3a, 3b (diagonal-kasner-momentum-constraint).** Applied: synthesis.imported-gtg-dictionary@2 added to uses; Ricci
  symmetry cited to (iv); the sign of R_0i = -g_0 . calR(g_i) tied to (iv)'s null-vector clause by polarisation (exact
  for g_0 . g_i = 0).
- **4a (frozen-point-integrand, Weyl space).** Confirmed and applied: symmetric + trace-free + I-linear gives 11
  dimensions (computed), B -> I4 B the extra map; with first Bianchi, 10. Proof names the Bianchi identity.
- **4b (frame legs in GA).** Applied. Proof (iv) now: K(DX ^ DX, F) = -<I4 calR(a ^ b)(d_b ^ d_a)> = 0 by first Bianchi
  (via <I A B> = <I A ^ B>), eps_X(DX ^ DX, F) = -<calR(a ^ b)(d_b ^ d_a)> = -calR = 0 by trace-freeness. New check
  check_gtg_frame_legs_and_weyl_space (KN map with Ricci part: K = 0, eps = 2 = -calR; I4 map: K = 12; sum; ten Weyl
  maps zero; the 4a Bianchi statements). Five mutants fail.
- **4c (declaration).** Applied: now names the two-forms/four-forms, the Chern-Simons form and its frame-component
  exactness proof, (v)'s global integrals and (v)'s signature-transfer (jet-polynomial) argument.
- **4d (flag).** Applied. Dictionary section 14 prescribes, for every result with a global ingredient, the flag
  sentence at the end of formal and in technical and one extraction.flags entry (37 entities follow it). Added: formal
  and technical sentences, and `'beyond one flat chart: the closed Riemannian S^2 x S^2 and the integrals over it'`.
  It adds no mathematics.
- **Extra (frozen-point-integrand, not a referee finding).** Proof (v) gave the S^2 x S^2 operator on Cl(4,0) as +K1, +K2.
  The store sign is -K1, -K2: computed from the torsion-solved field of S^2(1) x S^2(1/4), consistent with the
  dictionary's new Euclidean note. Corrected, and now asserted in check_gtg_weyl_square_of_weyl_maps. The densities
  are quadratic, so no values change.
- **5a (frozen-point-unique).** Applied: dictionary@2 added to uses.
- **5b.** Applied as text. One sentence says why computing in the Einstein scale loses nothing: another representative
  of [g] gives a tractor gauge field related by a parabolic gauge rotor, by Theorem
  synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection (i) and its closing gauge law. That theorem is
  proved and has holds_given []; it was added to uses @1. The optional c != 0 point goes to Leon.
- **6b (kasner-curvature-wall, Ellis-MacCallum).** Derived in GTG, so nothing is imported and nothing is cited from
  memory.
  - Torsion equation for the frame fields: omega_m x e_n - omega_n x e_m = c^_mn^l e_l, so omega is linear in c^.
  - Field strength: calR(e_m ^ e_n) = -(e^_m(omega_n) - e^_n(omega_m) + omega_m x omega_n - c^_mn^l omega_l).
  - New check check_gtg_ellis_maccallum_frame_formula. It treats the 9 c^ and their 27 frame derivatives as independent
    variables (polynomial Jets) and computes the store-sign scalar of Cl(0,3) exactly. That scalar equals
    4 e_i(a_i) - 6 a.a - (1/2)(2 n:n - (tr n)^2) coefficient by coefficient: 21 monomials, 6 of them derivatives, no
    Jacobi identity needed.
  - Further results: n^ is symmetric, and the unit S^3 gives 6.
  - Mutants on three coefficients fail.
  - The proof's false sentence "not used as a premise" was replaced, and so was the same claim in the extraction note.
- **6a.** Applied. Proof (iv) now displays the closed form of Omega for all z. It was recomputed symbolically in
  alpha_l(T): the Ricci identities then hold identically. The check now compares the solved Omega with the closed
  form, both value and the first derivatives in T and z. Three closed-form mutants fail.
- **6c.** Applied. In (iii) the Hamiltonian constraint is now written as -2 gamma_0 . calG(gamma_0) =
  (tr K)^2 - tr K^2 + s R^(3), citing the Gauss identity in the proof of nondiagonal-kasner (iv), which is already in
  uses. The declaration now names this identity as quoted, not derived in GA.
- **7a (kasner-field).** Applied: dictionary@2 added to uses.
- **8a (positive-structure).** Confirmed: for sigma = (t + x1)^2, grad sigma = 2(t + x1)(e0 - e1), so H(e0) = 2(e0 - e1),
  while 2(e0 . (e0 + e1))(e0 + e1) = 2(e0 + e1). Proof fixed. The check now asserts H0(a) = 2(a . l) l with
  l = e0 - e1 null; the mutant l = e0 + e1 fails. The formal level goes to Leon.
- **10a (tractor-transport).** Applied: gtg-tractor theorem @1 and dictionary @2 added to uses.
- Entities 1 and 9 (ACCEPT): nothing beyond the docstring and pins.

## Stale pins (all repinned)

- N (15): pairing.imported-schwarzschild-connection-curvature 5->6, pairing.imported-weyl-scalars-petrov-type-schwarzschild
  2->3 (x2), pairing.loop-classes-are-weyl-components 4->5, dark-energy.variable-exponents-... 4->5, dark-energy.wall-counterterm
  4->6, dark-energy.frozen-point-makes-stelle-west-vector 5->6, synthesis.promoted-norm-weyl-clock-flat-weight 6->7,
  synthesis.nondiagonal-kasner-residue-weighted-shear 3->4, synthesis.unit-boost-residue-needs-nonpositive-exponent 3->4,
  synthesis.kasner-exit-... 3->4, synthesis.attachment-transport-... 2->3, synthesis.infinity-vacuum-incidence-... 3->4,
  synthesis.positive-structure-is-twistor-form-... 4->5, interior.imported-tractor-connection 2->3.
- R, use holds (7):
  - synthesis.imported-gtg-dictionary 1->2 ((iv) frame-plane reading), in pairing.curvature, loop-classes,
    frozen-point-integrand, kasner-curvature-wall and positive-structure;
  - macdowell-mansouri-principle 2->3 (store sign named), in frozen-point-integrand, cited only in the Reading;
  - positive-structure 2->3 (A3), in frozen-point-integrand, cited for scale non-selection only.

## For Leon

1. synthesis.positive-structure-... formal (iii): replace "$H^{\circ}(a) = 2(a\cdot l)\,l$, $l = e_{0} + e_{1}$ null" with
   "$H^{\circ}(a) = 2(a\cdot l)\,l$, $l = \nabla(t + x_{1}) = e_{0} - e_{1}$ null" (evidence above).
2. synthesis.frozen-point-unique-... formal: "Consequently the Einstein scale of $I'$ ..." needs $c \neq 0$ ($c = 0$ gives
   $I' = 0$). Proposed: "Consequently, for $c \neq 0$, the Einstein scale of $I'$ is $c$ times that of $I$, ...".
3. Noted, decided by section 14: the Beyond-one-flat-chart flag added to frozen-point-integrand's formal and technical (4d).
