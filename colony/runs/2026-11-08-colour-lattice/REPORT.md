# Run 2026-11-08-colour-lattice: report

Target: op.qft-non-abelian-gauge-fields, attack item "Colour: a colour rotor lattice (none is stored) and its continuum
limit". Prompted by Leon's question of what the graph says about the Yang-Mills mass gap. Method: attacker pair (A
constructive, B adversarial), blind referee C, one fix round, close-out. Pre-registered kill conditions A1-A4 and K1-K7:
none fired.

## Accepted (three results)
- synthesis.colour-centre-flux-bounds-polyakov-lines-and-the-leading-glueball-tube (A; SOUND WITH FIXES): colour rotors
  are the genuine rotors of the e3..e8 block fixing the pure-spinor idempotent E (J-commutation and det = 1 in one
  condition; the referee's counterexample shows the vector condition is needed); triplet character 4(<R>_0 + <R>_6) - 1,
  action (4 beta/3)(1 - <U_p>_0), beta = 6/g^2; centre rotor z exact in Q(sqrt3); the Z3 flux chain bounds every
  surviving term: no R x T fundamental loop has a term below order A, leading (beta/18)^A; the bound does not apply to
  zero triality (three lines on the volume form give 1; adjoint perimeter law argued); Polyakov lines zero at every beta,
  pair (1/9)(beta/18)^(N_t r), baryonic junction (1/27)(beta/18)^(3 N_t) (free spatial boundary); connected plaquette
  correlator leading (1/18)(beta/18)^(4t), no lower term; leading decay rate 4 ln(18/beta) per step at fixed t (uniform
  gap argued, not imported).
- synthesis.a-finite-subgroup-of-colour-shares-its-strong-coupling-expansion-through-link-degree-three (B; OVERSTATED,
  restated; Leon accepted): the 96 J-commuting signed permutations fixing the J-volume trivector form a centreless
  subgroup of SU(3) (Schur); its averages equal Haar through link degree 3 (derived) and differ at degree 4 (20 vs 12
  invariants); the own-plaquette term (beta/18)^A, gluing 1/3, tube terms and the plaquette through beta^2 are shared;
  the plaquette differs at beta^3 (0 vs 1/972); reading (argued): strong coupling cannot separate SU(3) from a centreless
  group that freezes at weak coupling.
- synthesis.colour-triplets-give-the-fundamental-colour-loop-a-perimeter-law-at-strong-coupling (B; SOUND WITH FIXES;
  title now "... at infinite coupling"): frozen triplet, <chi(U_C)> = c(kappa)^P / 3 exactly, c = kappa/6 - kappa^3/288
  + O(kappa^5), rank-one mean link; Wilson quarks, spin trace -2^(P-1), leading hopping term (n_f/6)(2 kappa)^P;
  outside_ga declared for the Grassmann integral (complex unit of the spinor ideal named, identified with j on colour).

## Referee C
All key numbers recomputed by independent exact routes (Weyl integration for SU(3) moments, brute-force enumeration of
G, exhaustive minimal-surface search, matrix trace on the regular module of Cl(4,0), 2D character formula); 10
perturbations broke the checks as expected. Overlap ruling: the degree-3 lemma is shared by A and B1 (and B2 rebuilds
G); not duplicates.

## Leon's decisions (8 November)
Keep the uniform-in-t lattice gap (Osterwalder-Seiler clustering) argued, no import; keep the weak-coupling freezing of
finite groups argued, no import; restate the colour attack item (the series' colour sector has quarks, so its physical
question is QCD's; the Clay problem is pure Yang-Mills); add a note on the weak-factor rotor lattice (the 24 Hurwitz
units give the binary tetrahedral group as a counter-model with identical coefficients through link degree 5); accept
the restated B1.

## Maintainer pass
Cross-references among the three in their extraction notes (E201 forbade them in proposals); the shared degree-3 lemma
left derived in each check (no repointing to a uses edge); weak-factor note added (extraction only); open problem
updated: known paragraph (8 November, colour lattice), colour attack item restated, entities and source extended.

## What this means for the mass gap
Nothing here bears on the Yang-Mills existence and mass-gap problem. The stored results are strong-coupling lattice
statements in GA form (classical: Wilson, Drouffe-Zuber, Muenster, Svetitsky-Yaffe, Osterwalder-Seiler as prior art).
The finite-subgroup result shows sharply why: strong-coupling data are shared with a theory that has no continuum limit.
The Clay problem lives in the weak-coupling continuum limit, which no stored result reaches; and the series' own colour
sector carries quarks, for which the Wilson loop is not an order parameter.

## Checks
Baseline 0 errors 0 warnings. Gate after fixes: all three check4 exit 0 with no findings, validate ok, style clean. Final
tp check 0 errors 0 warnings; build 0 errors (with --author); layout, site, lock; 394 tests OK (1 skipped).

## Costs (approximate subagent tokens)
Attacker A 362k (with fixes), attacker B 388k (with fixes), referee C 295k: about 1.04M.
