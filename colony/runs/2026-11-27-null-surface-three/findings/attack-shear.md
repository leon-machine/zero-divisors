# Attacker `shear`: null-surface data at any field strength; the focusing equation integrated

Run 2026-11-27-null-surface-three. Status: FILED, gates clean (lint, checkone, mutants).

Entity: `store/claims/synthesis.null-surface-data-at-any-field-strength-the-focusing-equation-integrated/`
(entity.md, proof-main.tex, check.py). Scratch: `colony/runs/2026-11-27-null-surface-three/work/shear/`.

## Target
A stored result extending R1 (`synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators`,
clause (iii)) from first order to a field of any strength on one null surface: (a) linearisation of focusing
with rho^2 the transverse area density; (b) closed-form integration in a field-built parameter; (c) focusing
bound; (d) what is true about freedom of the shear on one null surface, with the exact plane wave as the
realising family; (e) the clock.

## Kill conditions (pre-registered 27 November, BEFORE any computation was run)
- (K1) the linear equation rho'' = -(1/2)(<sigma,sigma> - K.R(K)) rho fails on the exact plane wave at second
  order in the amplitude, in exact arithmetic. Would mean an error in R1 clause (iii) or in my definition of
  rho: stop, find it, report it.
- (K2) the closed form (b) (whichever parametrisation is claimed) fails at any order in the amplitude tested
  (orders 0 to 4 at least), or on any exact strong-field example tested.
- (K3) the Kerr-Schild plane wave hb^{-1}(a) = a - H (a.n) n, H = (1/2) w_ij(n.x) y^i y^j, w symmetric
  trace-free, is not torsion-free with vanishing Ricci map in the stored conventions (lib/gtg.py), at a
  generic point and at an amplitude that is not small. Then: find a correct exact family or restrict the claim.
- (K4, added before computing) the congruence K = hb^T(grad phi) with phi = (1/2) nbar.x - (1/2) S_ij(u) y^i y^j,
  S' = w - S^2, is not null (Q(K) != 0 as a jet) or its generators are not affinely parametrised by u = n.x.
  Then the null function is wrong: redo the eikonal equation.

### Outcome
- K1: did NOT fire. The linear equation holds as an exact jet identity on five waves that are not weak
  (profile entries of size 1 to 7, generic point not at the origin, generic initial screen map) and as a series
  identity through order eight at six amplitudes; by interpolation it holds at each of orders 1 to 4.
- K2: did NOT fire. Both integrated forms hold as series identities to order eight (with and without initial
  expansion, with and without matter) and on the exact power-law waves for six exponents.
- K3: did NOT fire. The wave is torsion-free with Omega(a) = (a.l) grad H ^ l (equal, as jets, to Omega solved
  by lib/gtg.py), det hb = 1, Ricci map (tr w)(a.l) l: vacuum exactly when tr w = 0, at any amplitude.
- K4: did NOT fire. Q(K) = 0 as a jet; l . hb(K) = 1.
No stored entry was found wrong. R1 clause (iii) passed every test at any strength, including its shear
equation with the curvature term (the form C(m_i, m_j) is w_ij on the wave), which R1's own check does not test.

## Predictions written down before computing, and what happened
1. Area element rho^4 := -(hb^{-1}(x_1 ^ x_2))^2 obeys K.D rho = (theta/2) rho: CONFIRMED (proved in the entity
   from R1's lemma (2); checked as jets).
2. Parameter s, ds = d lambda/rho: e = 2 rho', de/ds = -<s,s>_s + rho^2 K.R(K), rho^2 an explicit exponential:
   CONFIRMED.
3. Area parameter: p = p_0 exp(-Xi), with matter d(p^2)/d rho = -rho <s,s>_rho p^2 + rho K.R(K): CONFIRMED.
   This is the paper's (3.26a-d) as extracted; no difference in the formula.
4. Plane wave: S' = w - S^2, rho^2 = det E, K.R(K) = tr w: CONFIRMED. Sign of the curvature form:
   (K ^ m_j) . R(K ^ m_i) = + w_ij as a form, i.e. minus w as a map on the screen (R1's hat-C is the map).
5. Exact power-law family, qbar = diag(rho^a, rho^-a), p ~ rho^(-a^2/4), E = diag(lam^p1, lam^p2): CONFIRMED.

Changes of plan made while computing (none changes a claim):
- Convention changed after pre-registration, for agreement with R1: the wave now travels along
  l = (e_0 - e_3)/2 (n.l = 1), its phase l.x is R1's parameter lambda, and the null function is
  phi = n.x + (1/2) y.S(y), so that K = n and the hypersurface is R1's plane N when S = 0 and w = 0. K3 and K4
  were tested in both conventions.
- The check uses null labels (lambda, nu, y^1, y^2) for the flat background instead of Cartesian ones (the jets
  are then sparse and the checks several times faster). lib/gtg.py supports any labels (it is how its static fields are built).
- The order-eight series use the closed-form Omega and test the torsion equation on it as jets; the low-order
  checks solve Omega with lib/gtg.py and compare with the closed form as jets.

## What was established (labelled as in the entity)
(i) area density from hb: proved. (ii) rho'' = -(1/2)(<s,s> - K.R(K)) rho, and the family of parameters
d tau = rho^alpha d lambda in which rho^(1+alpha) obeys a linear equation: proved. (iii) integration in s and
in the area parameter, with the matter term: proved. (iv) focusing bound under (P): proved. (v) the datum on
one generator (a bijection between shape histories in s with two constants and solutions): proved; the
characteristic initial value theorem NOT claimed. (vi) the plane wave as an exact field, its null
hypersurfaces, realisation of every shear history along a generator and of every solution (rho, qbar):
proved, checked. (vii) a null plane crossed by a wave focuses: proved. (viii) clock: relations proved,
reading argued.

## What was weaker than hoped
- (d): no existence statement off the hypersurface, and the realising family carries the same shear history on
  every generator (plane waves are homogeneous across their fronts). Arbitrary dependence on the generator
  label is the characteristic initial value problem and is not touched.
- Third order in the amplitude is vacuous for scalars in vacuum: a quarter turn about the generator maps a
  trace-free profile to its negative, so theta and rho are even in the amplitude. Orders 1 and 3 are tested on
  a wave with matter (tr w != 0), where all of orders 1 to 4 are present and pinned.
- (Superseded in the fix round: the referee supplied the example, now in the check.) At filing time an exact
  rational example of a VACUUM wave crossing a null PLANE and reaching a caustic was not found (the
  second Jacobi field is not rational for the profiles tried). The check has: a wave with matter obeying the
  null energy condition crossing a null plane with rho^2 = 1 - 3/2 lam^2 + 1/2 lam^3 (exact caustic at lam = 1);
  vacuum waves smooth for all lam with an exact caustic of a hypersurface that is not a plane at the start;
  and the proof of (vii) for the general case.
- (e): the clock is a classical relation along one generator. It says nothing about the store's flows.
- (b): the paper's formula is reproduced, not corrected. What is added is its domain (p != 0), the s-form,
  which has no such condition, and the matter term.

## Store search (near-duplicates)
- search_claims: "focusing theorem caustic", "Raychaudhuri expansion null congruence", "plane gravitational wave
  exact vacuum", "clock along null generator area"; grep under store/claims for pp-wave, plane wave, caustic,
  conjugate point, focal, Kerr-Schild.
- `synthesis.imported-raychaudhuri-null-congruence` (imported): the focusing and shear equations. Not used; R1
  clause (iii) is used in its place.
- `synthesis.plane-wave-weak-null-crossing-null-shell-ambiguity`: conformally flat plane waves in the Rosen
  gauge. Its Rosen factor a is my E for the pure-trace profile w = (a''/a) id (a wave with matter). It does
  not treat shear, area density or caustics. Not a duplicate.
- `synthesis.crossing-transport-tipler-threshold-sharp`: a linear equation w'' = nu^2 S w along a crossing
  geodesic for a tractor component; same Jacobi structure, different object.
- No stored focusing bound, no stored area-density equation, no stored caustic statement.
- open_problems.yaml searched for time, flow, clock, modular: no open problem on a clock for the gravitational
  field. Nearest: `synthesis.phase-flow-is-time-rotor-flow-kms-continuation` (settled claim: which boost flow is
  time, for the boundary-mode algebra) and `op.null-positivity-curved-horizons`.

## Filed against
`op.gravitational-field-at-null-momentum` (its statement lists "anything beyond first order" as open, and R1 is
filed there). Named as the other candidate in the extraction note: `op.einstein-from-the-field-theory` (the
orchestrator's first guess). My reason: the result uses one component of the field equation as a hypothesis
and derives nothing of it, whereas it is the classical continuation of R1's datum beyond first order.

## Unexpected links
1. For attacker `stress`: in the Kerr-Schild gauge the plane wave is hb = id + (1/2) W (a.l) l exactly, with no
   second-order part, and its Einstein map is exactly linear in the profile (Ricci map (tr w)(a.l) l). So in
   the parametrisation hb = id + eps H1 the second-order Einstein term G2[H1, H1] vanishes identically on
   these fields, at every point, although the wave focuses every null plane that crosses it at second order
   (theta = -int <sigma, sigma>). A second-order stress defined as G2/(8 pi G) is therefore zero on an exact
   wave in this gauge: an exact instance of "not locally invariant". Consistent with their prediction 4; worth
   a cross-check of their formula in a gauge with h(n) != 0.
2. The exact curvature of the wave is R1's stored first-order curvature R_p[h] at p = l, h = 2w, with no
   correction: the two free directions at null momentum of the stored first-order theorem are, exactly, the
   profile of a field of any strength.
3. Linear forms of focusing form a one-parameter family (d tau = rho^alpha d lambda, rho^(1+alpha) linear):
   alpha = 0 the paper's (3.25f), alpha = 1 the dressing time of Ciambelli, Freidel and Leigh, and the excluded
   alpha = -1 is where it integrates by quadrature (my parameter s).
4. A hypersurface of the FLAT field can have shear (power-law case a = -2: E = diag(1, lam)); the part of the
   shear that is the wave is w = sigma' + theta sigma.

## References appended to store/references.yaml (with `cat >>`, keys checked absent first)
Sachs1962, Penrose1965, Rendall1990, CiambelliFreidelLeigh2024.

## Literature: what was verified and what is from memory
- Read through text extraction (WebFetch, a small model's answer, not the PDF): arXiv:2611.34924 Section 3.2
  (equations (3.20) to (3.28) as extracted); abstract page of arXiv:2309.03932 (dressing time: mu = kappa +
  theta/2 = 0, constraint d_V^2 Omega + Omega(sigma^2 + 8 pi G T_VV) = 0); abstract of arXiv:1912.05960.
- Bibliographic details verified against index pages (scilit), papers not read: Sachs 1962 (J. Math. Phys. 3,
  908-914; the index page did not list the author, the title and journal match), Penrose 1965 (Rev. Mod. Phys.
  37, 215-220), Rendall 1990 (Proc. R. Soc. Lond. A 427, 221-239). JHEP 01 (2024) 166 for Ciambelli, Freidel
  and Leigh is from the search result's link, not from a page I read.
- FROM MEMORY, not verified: Raychaudhuri 1955 and Sachs 1961 as origins (keys already in the store);
  Brinkmann 1925; Bondi, Pirani and Robinson 1959; Kerr and Schild 1965; Hawking and Ellis 1973 for the
  focusing bound; that Doran and Lasenby 2003 does not itself treat the plane wave in this form (not checked);
  M. Reisenberger's use of an area parameter on null generators (2007, 2008) is recalled and NOT cited in the
  entity.

## Decisions for Leon
1. Which open problem the result sits under (see "Filed against"), and whether either takes an attack item
   for a bracket on the shape history at any strength.
2. Whether R1's Limits paragraph cites this result for the classical part of "beyond first order".
3. Whether the stored Clausius derivation (vanishing shear and expansion at the point) takes a note citing
   clause (ii).
4. Whether clause (vi) (the plane wave as an exact field with closed-form Omega) is split off, and whether
   lib/gtg.py takes a plane-wave constructor.
5. Whether the store wants an open problem on how a field-built parameter along a generator relates to the
   flows the series calls time.

## Gates (final, rerun after the last change to check.py)
- `python -m tp.lint <id> --store store`: 0 errors, 0 warnings, 7 info (the seven checks pass; slowest 1.14 s).
  One earlier lint run, made while the other attackers were running, reported one warning. Only the summary line of that run was kept, so the code is inferred, not seen: L409 (a
  check slower than 3 s; the null-plane series then took 2.6 to 3.0 s, and no other warning was ever shown). Fixed by using the closed forms of hb and Omega in
  the order-eight series, tested there as jets against hb^{-1} and the torsion equation, and compared at order
  two with what lib/gtg.py solves. Did not recur in the runs after the fix.
- `python -m tp.checkone <id> --store store`: all 7 checks passed.
- `python -m tp.mutants <id> --store store`: every function "ok"; sampled survivors 0,1,0,0,0,0,0 of 8 (the one
  survivor is a `!= 0` guard). With --every (run before the last two edits): survivors were order bounds of
  series, `!= 0` guards and a range start; no pinned value survived.

## Fix round (after the blind referee's report, verdict SOUND WITH FIXES)
Report: `colony/runs/2026-11-27-null-surface-three/findings/referee-shear.md`. All thirteen required fixes and
all the optional suggestions were applied; nothing was declined. Only files in my entity folder were edited.

Required, by referee number:
1. "What the datum is": extraction note, Reading (Beyond first order) and lay level now say that the component
   of the field equation along the generators leaves the shape history free and slaves the area to it, and
   that the other components on the hypersurface are not examined. The lay sentence on the first of the three
   parts and the one-liner were brought into line too.
2. Clause (iv): the referee's weaker wording is used (the stretch on which field and phi are smooth with
   rho > 0 ends), with a sentence that ending by rho -> 0 is not proved in general, only for the plane waves in
   (vii). I did not attempt the general proof: it needs the equation of the separations for a general field,
   which the entity does not hold. Proof of (iv) reworded to match; proof of (vii) now says why the stretch
   can end only by det E = 0 there.
3. (P) added to the bound at the technical level ("two over the magnitude of the expansion"), the lay level
   and the one-liner.
4. "The same history on every generator" added at lay, technical and one-liner.
5. Lay attribution replaced by the referee's sentence.
6. Lay clock sentence replaced (turning point included).
7. Proof of (vi)(c): the sentence E = E_b C added, with the reason, and the earlier appeal to (i) now points to it.
8. (i): "belong to the field and the hypersurface"; (viii): "Along a generator of a given null hypersurface".
9. (iii): the sentence on the datum entering as a function of s or rho added after form (alpha); technical
   "integrates explicitly once the shape is given as a function of s or of the area"; lay "can be integrated
   explicitly"; the remaining "closed form" wordings for the integration (extraction note, Reading) changed
   the same way. The proof of (iii) says the formulas are integral equations if the shape is given in lambda.
10. Formal (iii): "as extracted, in the paper's component notation, quoted", and the sentence on the second
    independent extraction and the PDF not read directly; the same in the extraction note; one-liner wording
    changed as specified.
11. check_area_density_and_the_linear_focusing_equation_on_strong_waves now builds the five waves with
    E(lambda_0) = ((3, -1), (2, 1)) (rho^4 = 25 at the point), computes the Gram matrix G of the two physical
    separations from the gauge field, differentiates it along the generator, and pins det G = rho^4,
    tr G^{-1}G' = 2 theta and (1/4) tr((G^{-1}G' - theta)^2) = <sigma, sigma>. My own code (helper
    `shape_rate`); the referee's script was not read.
12. Power-law check: label changed to the differential statements at the sample point; a second sample point
    added (lambda = 3 and 5/2), and the shape rate qbar^{-1} qbar' = (a theta/2) diag(1, -1) is now computed
    from the gauge-field Gram matrix instead of being asserted.
13. Formal (i): G introduced as the matrix, in the basis X_1, X_2 of the screen, of minus the product (the
    Gram map), and sigma there as the matrix of the shear, a linear map of the screen; proof (i) likewise.

Optional, all applied:
- (vii): hypothesis weakened to w smooth on an interval [lambda_0, lambda_2], with the bound claimed when
  lambda_1 + 2/|theta(lambda_1)| <= lambda_2; lower levels no longer say "always".
- The referee's exact vacuum null-plane caustic, verified by me before use and added as case (3) of
  check_focusing_bound_and_exact_caustics and to the proof of (vii): w = diag(6/q, -6/q), q = 2 + 2 lam - lam^2,
  S(0) = 0, E = diag(f, b), b = 1 - 3/2 lam^2 + 1/2 lam^3 (exact to order eight in the series of E), f >= 1 on
  [0, 1] by convexity (proof), field smooth and vacuum at lam = 1 with (n ^ e_2).R(n ^ e_2) = -2. It is the same
  b as my wave with matter; I had dismissed the vacuum version because f is not rational, and missed that
  f >= 1 is all that is needed.
- Names: rho^2 is "the area density", rho "the root area density", throughout.
- (viii): the parenthetical marked "for example".
- Dressing-time credit qualified "in an affine frame and up to a constant factor" (formal, technical, note).
- The sixth suggestion (not in the coordinator's list) also applied: form (beta) is now tested with rho itself
  as the variable (lambda reverted as a series in rho), including the quadrature for lambda.

Cross-link recorded in the extraction note and kept consistent in the Reading: on the plane wave in the
Kerr-Schild gauge the Einstein map is exactly linear in the profile, so its quadratic part vanishes
identically; the gauge change to the transverse trace-free form (a displacement quadratic across the plane with
a rotation gauge change) is attributed to the companion computation and not pinned.

Gates after the fix round:
- lint: 0 errors, 0 warnings, 7 info (slowest check 1.18 s).
- checkone: all 7 checks passed.
- mutants: every function "ok"; sampled survivors 0, 1, 1, 0, 2, 0, 0 of 8 (`!= 0` guards and series order
  bounds). A --every run before the last small refactor: no pinned value survived; two new harmless survivors
  are the sample points `point(0)` and `point(1)` of the vacuum null-plane case (the wave is invariant under
  translation in lambda, so the label of the point does not matter).
