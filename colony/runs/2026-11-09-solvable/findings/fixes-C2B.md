# Fixes C2B (fix round, run 2026-11-09-solvable)

check4: pending (orchestrator). Only runcheck.py was run. Pre-fix copies: work/C2B/pre-fix-brst/, work/C2B/pre-fix-koide/.

## synthesis.higgs-sector-brst-does-not-fix-the-breaking-pattern-of-two-doublets (R1 section 5, SOUND WITH FIXES)
1. Quartet positivity in (iii) needed the 't Hooft mixing cancellation and mass equality. Done:
   - Added Fact synthesis.imported-brst-kugo-ojima-strocchi-and-gribov@1 to `uses`, with premise() in
     check_one_coupling_sign_decides_the_pattern and \claimref in formal (iii) and the proof.
   - The proof of (iii) now gives the standard computation in a few lines: the A-h cross terms are
     g d(A <W_a, h>); the mass matrices are g^2 kappa^-1 Gamma (vectors, ghosts) and g^2 W kappa^-1 W^T (Goldstones);
     at a stationary point the Hessian kills the Goldstone directions, by the identity of (i); AB and BA have the
     same nonzero spectrum.
   - The extraction note names synthesis.field-level-brst-of-the-two-doublets-and-the-thooft-feynman-gauge (iv), (v)
     as the intended citation (override 3).
2. (iv) is now labelled "a corollary of stored clauses" in the formal, the one-liner and the extraction note. The
   formal ends with the sentence naming lift-locus (1) (circle or trivial stabiliser) and D-term (1), (2); the proof
   cites lift-locus (1) for the circle stabiliser. "New: the rank theorem on the lift locus" is dropped.
3. The counter-model pair is labelled prior art (Ferreira-Santos-Barroso, Ivanov) in GA form, in both the formal (iii)
   and the note. The note now says: "New for the store: the stationarity condition (i) ... and the reading that the
   BRST construction is consistent for either pattern."
4. Conventions: I adopted the sibling's realisation (e0, e1, e2; weak T_a = e12/2, e20/2, e01/2 on the left;
   hypercharge y phi e12 on the right, y = 1/2; basis 1, e12, e02, e01) in the formal, the proof and the check.
   - K is now the span{1, e12} part and K' the span{e02, e01} part.
   - The charge-breaking example is (1, e02); the dictionary is (z1, z2) -> z1 + e01 z2.
   - The unbroken generator is Z = T1 - Y/(2y); the rank proof was rewritten with it.
   - The check's pinned values were recomputed: at the non-stationary point V = 3/8, the gradient is
     (3/2, 0, 0, 0, 0, -3, 0, 0), and the obstruction matrix has entries ±3/4 and ±3/2.
   - Two sample points were moved: the kappa = +1 vacuum, and one interior lift-locus point (both were aligned or off L
     in the new basis).
   - The rank census is unchanged: 1 / 672 / 5888.
   - The formal says no statement depends on y != 0.
- Nilpotency (overlap ruling): kept as one sentence (it is needed for (iii)). The intended citation (the sibling's (ii))
  is named in the note and the proof.
- runcheck: 6/6 PASS.

## synthesis.koide-middle-mass-bound-closes-the-remaining-quark-dressing-class (R1 section 7, SOUND WITH FIXES)
1. Formal (iv): "R* (1.88, 2.19, 8.67, 17.5 to two places)" is replaced by the stored intervals (1.88, 1.89),
   (2.19, 2.20), (8.67, 8.68), (17.5, 17.6). The check now also certifies Q < 2/3 at the upper ends 1.89, 2.20, 8.68
   and 17.56 from the stored quantities (coverage and proof updated).
2. Lay: "whatever the up quark's mass" now reads "whatever the up quark's mass below the charm mass".
3. Amending the stored theorem's last sentence of (iv) is a maintainer decision. It is listed in attack-C2B.md
   Decisions for Leon, item 2; I made no edit.
4. Optional prior art added to the extraction note: the bound is the theta = 0 point of the trigonometric
   parametrisation (Foot, hep-ph/9402242, cited from memory).
- runcheck: 4/4 PASS.
