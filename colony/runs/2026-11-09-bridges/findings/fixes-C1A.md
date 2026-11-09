# Fixes C1A, run 2026-11-09-bridges (referee R2)

All edits in place in proposals/<id>/; ids unchanged; only runcheck was run (all functions pass on all three).

## synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three (SOUND WITH FIXES)
1. Title: applied. "Quarter turns about blades of square -1 give a state design of order three when I^2 = -1" (88 characters).
2. Clause (i): applied. Generators renamed quarter-turn elements R_c = 1 + k_c; the referee's sentences on rotors
   (rotor exactly when k is a bivector; grade 4 and 6 from eight generators; R R~ = 2k at grade 4; bivector orbits
   7, 21, 35 in Cl(7,1) and 45, 210 in Cl(10,0)) inserted. Confirmed by a new check
   (check_generators_are_rotors_only_for_bivector_blades): grade counts 21/35/7 and 45/210, R R~, the orbits.
3. Technical, lay, extraction note: applied as worded by the referee.
4. Orders: applied. Labelled computed; the formula 2^(2N-2) |Sp(2N-2, 2)| mentioned with its classical input flagged
   as not used.
5. Proof (iv), the adjoint: applied (real-linear map fixing h_c, negating I h_c).
6. Invariant-measure strengthening: applied in (iv), the one-liner, technical and proof (one-line argument;
   R_c R_c^dagger = 2). (iv) relabelled "proved; the imported Fact is a cross-check". Check: a mixture of two orbits
   has the same second moment (in check_invariant_mixtures_and_the_parity_sector_corollary).
7. Parity-sector corollary: applied after (iii) with proof paragraph and check (closed form for d_A, d_B up to 64;
   group means 2/3 in Cl(1,3), 3/5 for one and two modes in Cl(6,0), blade and generic states).
8. Dependants: applied. Powers-of-two restriction in the formal sentence of (v); the note says which dependants can
   cite the result after the retirement of the imported mean-purity Fact (the crossing clause (iv) and clause (iii)
   at powers of two of the Renyi-two comparison; not clause (iii) for general m, n, not Renyi index four and above,
   not Page's average).
Bridge leads: B2 and B3 folded into the note (the theorem applies to the slot module's ten generators, Cl(10,0),
D = 16; bivector turns alone have orbits 45 and 210 there, computed in the new check). Overlap: sibling id named in
the note as intended citation (no proposal-to-proposal citation).
Not done: the id still contains "rotors" (ids are never renamed). The check's internal label and method name
"rotor_action" are unchanged.

## synthesis.field-strength-heat-kernel-coefficients-of-the-dark-towers-fix-no-scale-ratio (SOUND WITH FIXES)
1. Title: applied in shortened form (the referee's wording exceeds 90 characters): "Spin-trace rule in dimensions
   three and five: heat-kernel numbers, running only in four" (87).
2. `uses` and (iv): applied. dark-matter.no-coupling-rule-odd-towers-follows@6,
   dark-tower-matter.r1-has-no-mechanism-odd-towers@3, dark-tower-matter.five-dimensional-towers@4 added to uses,
   cited in (iv) and the proof, and touched by premise() in the table check. (iv) rewritten as consistent with, and
   adding the coefficients to, the stored obstructions; label argued; mirror ratio 1; odd towers only.
3. Reconciliation with five-dimensional-towers (ii): applied (the 8/203 arithmetic is stated as a different
   hypothesis that no stored statement supplies and that does not contradict the stored reduction under R3). The
   wording of the stored reduction is taken from the referee's summary; I did not re-read that entity in full.
4. Formal preamble with H1, H2, U, (S), covariant gauge, the indefinite-form premise and the own-dimension reading:
   applied.
5. Cl(2,1) remark: applied in (i) and the proof, with a check (P A P has dimension 2; w = I P squares to +P).
6. Applied: the modulus/phase sentence in (ii); "effective level"; the scales are the coupling and the bare masses.
7. Applied: normalisation Y = s - k/3; "the number of copies is not stored".
8. One-liner ending: applied.
Bridge lead B5: folded into the note as an argued second route to "a logarithm only at d = 4" (freedom degree
d - 2 of the stored kernel); not a clause, not checked.
No `assumes` edges added (maintainer-only); the premises H1, H2, U, (S), Krein are named in the formal preamble.

## synthesis.no-single-curvature-coupling-serves-the-sakharov-zero-and-the-kasner-tilt (OVERSTATED, restated)
Not rebutted: the referee's counter-example is exact (xi = 1.53, alpha = 1/3 + 4 xi = 1936/300 gives B = 0 with
6 xi = 9.18 inside the window; now a check line).
1. Retitle and rescope: applied at every level. Title "At gauge parameter one no curvature coupling gives the
   Sakharov zero and the Kasner tilt" (88). One-liner, technical, lay, Reading, note all scoped to gauge parameter
   one, with the free-gauge-parameter counter-statement.
2. Clause (ii): applied; counter-statement added as a labelled part of the clause; 6.5258 corrected to 6.5257
   (checked to four places).
3. Massive-vector sentence: deleted from the formal statement, the proof and the check; coverage text updated.
4. Reading: applied (at alpha = 1 no value serves the zero and the tilt, or the matching and the tilt; zero and
   matching are alternatives by definition; neither exclusion holds with alpha free).
5. Scope sentence: applied ((P1); gauge parameter one unless stated).
6. Numerology disclaimer: applied in (iii); the seven-generation remark removed from the one-liner.
7. Labels: (i) "classical; proved given the two stored spectra"; (iv) "restates clause (iv) of the tree-level
   result"; the alpha = 1 numbers of (ii) said to restate the open problem's arithmetic.
The id still says "no single curvature coupling serves" (ids are never renamed).
For Leon (unchanged from the referee): whether the gauge parameter is fixed at one by clause (K1) of the Krein
premise for every statement about B.

check4: pending (orchestrator)
