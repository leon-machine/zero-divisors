# Report, run 2026-11-16-anomaly

Targets: op.strong-cp, op.matter-asymmetry-origin, op.order-four-anomaly-and-sixteen, chosen from a leads survey of
38 open problems (LEADS.md; op.descent-state-and-spectrum left out, worked elsewhere) under one idea: the anomaly
of a charge of the sixteen, locally its pairing with the pseudoscalar part of a gauge field's square, globally the
fixed-point count of the order-four pseudoscalar on a closed five-manifold. Two attackers (constructive,
adversarial), two blind referees and a second-pass referee (all three Claude Opus 5.5), one fix round, two
maintainer agents. About 3.2 million tokens.

## Outcome
- op.strong-cp: settled, by registration. The series neither fixes nor relaxes the angle; by Leon's decision it is
  a registered free input with a refutation condition, which is one branch of the problem's success clause.
- op.matter-asymmetry-origin: stays partial. The conditional inheritance theorem the problem posed is written and
  its algebra proved; the hypotheses it needs are named and three of them are not stored.
- op.order-four-anomaly-and-sixteen: stays open, restated. The count asked for is derived; what it means for
  content is conditional on a literature statement that stays unimported.

## Established (five accepted results, all transport-absent and saying so)
- synthesis.phase-of-the-quark-mass-determinant-on-the-covariant-completion (SOUND WITH FIXES). Proved: off the
  balanced frame the completion is a bijection on pairs of mass matrices preserving symmetric pairs, so the mass
  phase is not fixed. Proved: the readings with a real determinant (real matrices; Y-tilde = Y*; Hermitian) are
  closed by stored data. Proved, a half result: on one-type symmetric stages with real first stages and c_q,
  delta_q real, the determinant is real exactly when the up-down phase is a quarter turn, with nonzero Jarlskog
  invariant, of sign -sgn(c_u c_d R_u R_d). The attacker's pre-registered claim that every real-determinant reading
  is closed was false and is withdrawn. The referee's counterexample to the first sign rule (delta_u = -5) is
  pinned in the check.
- synthesis.colour-angle-term-under-the-stored-maps-and-no-colour-anomalous-phase-of-the-rung-coupling
  (OVERSTATED, restated and renamed, accepted on the second pass, accepted by Leon). Proved: the stored CPT
  conjugation fixes the grade-four part of the colour field square in both of its conventions, given that it acts
  on colour by an automorphism or anti-automorphism (a hypothesis the premise does not state); among outermorphisms
  of vector isometries it is reversed exactly by determinant -1 (the duality rotation reverses it without
  reversing an orientation); it is carried to the mirror up to the sign of the identification of orientations.
  Proved: on the covariant coupling with both family matrices invertible and no further doublet or coloured
  fermion, every phase symmetry has colour coefficient zero. Argued: completeness of the lists of maps and fields.
- synthesis.conditional-inheritance-of-b-minus-l-and-the-conversion-coefficient-as-a-gram-ratio (SOUND WITH
  FIXES). Proved: of the ten bilinear forms on the sixteen invariant under colour and charge only the Majorana
  form and the unstored weak-triplet form change B - L; the conversion coefficient is a Gram ratio of the
  susceptibility form, 28/79 and 8/23 with hypercharge, 12/37 and 10/31 with electric charge; it is blind to
  lepton flavour. Argued: one light doublet on the level branch. Conditional on (R), no washout (W), no injection,
  the naming, the process (A), a thermal descent state (T) and the gravitational pairing (Gr).
- synthesis.spectral-asymmetry-on-real-projective-five-space-from-monogenic-polynomials (SOUND WITH FIXES). Proved
  in Cl(0,6): the Fischer decomposition with dim M_k = 8 C(k+4, 4), the sphere's Dirac operator with eigenvalues
  -/+(k + 5/2), the antipodal lift J with J^2 = -1 and J omega an involution, the generating function
  4/(1 + t)^5, half the spectral asymmetry 1/16 per component of the sixteen. Named background, not derived:
  density, essential self-adjointness, the Mellin lemma.
- synthesis.order-four-structure-on-real-projective-walls-and-the-signed-count-modulo-sixteen (SOUND WITH FIXES).
  Proved: the signed count of omega on its class modulo the Standard Model group is 0 modulo 16 on sixteen
  components and 1 on fifteen (16 the largest modulus for one generation); on a real projective five-space wall
  exactly one side needs an order-four twist; L^5(4) carries no such structure. Argued: the count constrains no
  stored stage.

## Refuted or corrected in the run
- "Every reading with a real determinant is closed by stored data" (attacker's kill condition triggered).
- "The colour four-form is reversed only by orientation-reversing maps" (false: duality rotation).
- The first sign rule of the quarter-turn clause (false for negative delta_q).
- "The flag is the vacuum's one CP-violating datum" (false once the stored quark-stage phase is counted).
- The leads survey's guess that the neutral phase of the two rung doublets relaxes the angle: closed negatively;
  the second invariant W(N) is not constrained.

## Leon's decisions (16 November 2026)
D1. Register the physical colour angle as a free input, and store the exact quarter-turn texture as a conjecture.
D2. Accept the colour-angle result as restated.
D3. Import the anomalous weak process, its equilibrium relation and the lattice freeze-out; restate the registered
    asymmetry to one light doublet with B - L per unit entropy between 2.45e-10 and 2.68e-10; add the assumes edges.
D4. Keep the modulo-16 anomaly statement unimported; op.order-four-anomaly-and-sixteen stays open, restated.

## Maintainer pass
New: synthesis.colour-angle-registered-free-input (postulate);
synthesis.imported-physical-colour-angle-and-its-shift-under-quark-rephasing,
synthesis.imported-neutron-dipole-bound-and-its-conversion-to-the-colour-angle,
synthesis.imported-anomalous-weak-process-changes-b-plus-l-and-keeps-b-minus-l,
synthesis.imported-equilibrium-baryon-number-as-a-fraction-of-b-minus-l,
synthesis.imported-lattice-crossover-and-freeze-out-of-the-anomalous-weak-process (Facts);
synthesis.exact-quarter-turn-texture-of-the-quark-stages (conjecture);
note.synthesis.two-premise-questions-raised-by-the-colour-angle.
Changed: synthesis.matter-asymmetry-registered-free-input 5 -> 6; the conditional inheritance theorem 1 -> 2 (uses
and assumes edges); the order-four structure result 1 -> 2 (uses edge to the spectral asymmetry);
synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them 1 -> 2 (citations repointed).
Open problems: op.strong-cp moved to the settled file; op.order-four-anomaly-and-sixteen, op.matter-asymmetry-origin,
op.rung-unit, op.second-order-breaking, op.qft-structural-inputs updated.

## What the sources say, where it differs from what was expected
- The bound |theta-bar| < 1.98e-10 of Dragos et al. rests on the older neutron limit of 3.0e-26 e cm; with the 2020
  limit of 1.8e-26 the central coefficient gives 1.18e-10 (arithmetic of this pass, marked as such). The premise
  says "about 2e-10".
- A half turn of the angle conserves CP; whether it is excluded is model-dependent literature and is not imported.
- Of Harvey and Turner 1990 only the abstract and a preprint scan were reached; the closed form is quoted through
  three sources that were read. The preprint scan appears to carry another weighting of boson states; not resolved.
- Kuzmin, Rubakov and Shaposhnikov 1985 was not read; it is stated as the 1996 review attributes it.

## Left for a later pass
- Wording in seven entities that still call the process, the coefficient or the neutron bound "not a stored Fact"
  (listed in maintainer-M1.md and maintainer-M2.md).
- The two premise questions of the note: how the stored CPT conjugation acts on the gauge sector; which
  identification of orientations the common-ceiling-coupling premise uses for the angle.
- The one-loop mass phase on the quarter-turn texture (now an attack item of op.second-order-breaking).
- (W), (T), (Gr) as attack items of op.matter-asymmetry-origin; (Gr), the gravitational pairing of B - L on the
  fifteen, is a candidate in-framework source with no rate computed.
