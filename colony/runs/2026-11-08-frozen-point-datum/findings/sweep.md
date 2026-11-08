# Sweep: statements that depend on the square class of Lambda/3 (or of another datum)

Run 2026-11-08-frozen-point-datum, Stage 1 (agent S). Store at 12e45eb plus the open problem. Every row below was read
in the store (formal, technical, one-liner and lay levels, proofs, checks; notes by their body). Search: the patterns of
work/S/scan.py (sqrt of anything with Lambda, 3/, ell or Q(I); kappa_Lambda; R_h; SO, so, Spin of (1,4), (4,1), (2,3),
(3,2); Cl of the same; e_W, unit boost, normalised frozen point, I/sqrt; bifurcation sphere, static boost, null eigen,
cosmological horizon; H = sqrt, Lambda = 3H^2, Hubble; de Sitter radius, ell = sqrt; I_Lambda) over claims, objects,
notes and predictions: 332 entities hit, all classified (148 read clause by clause, the other 184 by their matches:
74 standard-form Clifford types, 85 "Hubble" mentions, 25 "horizon" mentions); plus the 34 entities naming I-perp, the 13
naming a unit Stelle-West vector e_V, the 220 distinct sqrt arguments (work/S/sqrt_args.txt), and the scratch list
work/ids.txt (all 32 classified below).

Classes (RUN.md): A holds over Q for every Lambda; B holds over Q iff Lambda/3 is a square, so restating with H fixes it;
C needs more than H (exact extra condition given); D already written with H (or kappa_Lambda = H).
Two refinements, used below and to be confirmed by Leon (decisions D2, D3 in file-S.md):
- B(sum2): group and Lie-algebra labels SO(1,4), so(1,4) (SO(2,3), so(2,3)) of the frozen point's stabiliser. Exact
  condition: Lambda/3 (resp. -Lambda/3) is a sum of two squares in K (theorem (v)(b)); weaker than a square, so H
  supplies it and the restatement with H fixes it; over Q it fails at Lambda = 9. Treated as B.
- A(R): statements over R by their content (pi, exp, KMS states, Hilbert spaces, integrals, real functions such as
  sqrt(r), measured decimals): the completion supplies the roots; the square class has no content there. Rows that
  write sqrt(Lambda/3) or sqrt(3/Lambda) where H or 1/H would do are listed in section 4 as optional wording only.

Checks: work/S/sweep_checks.py (11 functions, all pass: `python3 .../work/S/sweep_checks.py`), and the proposal's check
proposals/synthesis.frozen-point-datum-is-h/check.py (11 functions, check4 clean), cited as "thm (x)".
Restatement convention for T: "Lambda = 3H^2" means "with H in the base field K, H > 0 where K is ordered"; for the
anti-de Sitter side "Lambda = -3H'^2" likewise (decision D1). Lambda itself is then 3H^2 everywhere; nothing else changes.

## 1. Class B (restate with H)

| # | id (version) | level / clause | clause as stored | minimal restatement | check |
|---|---|---|---|---|---|
| B1 | synthesis.de-sitter-static-boost-frozen-point (v6) | formal (iii); preamble; technical | "For Lambda > 0 ... R_h = sqrt(3/Lambda) ... kappa_Lambda = sqrt(Lambda/3) ... with H = sqrt(Lambda/3), B = H u, u = e0 e_W, e_W = W/H, u^2 = +1 ... H times the unit boost"; preamble "for every real Lambda"; technical "horizon at R = sqrt(3/Lambda) with surface gravity sqrt(Lambda/3)" | (iii) opens "For Lambda = 3H^2, H > 0:" and reads R_h = 1/H, kappa_Lambda = H (so kappa^2 = B^2 = Q(I) = H^2), B = H u, e_W = W/H; the definition "H = sqrt(Lambda/3)" is dropped; the period 2pi/kappa = 2pi/H stays (over R). Preamble: "for every Lambda in the base field (in (iii) Lambda = 3H^2)". Technical: R_h = 1/H, surface gravity H. (i), (ii), (v) unchanged (A); (iv) period 2pi/sqrt(-Lambda/3) is A(R) (optional 2pi/H'). Check already samples Lambda = 3H^2 (D). | sw_static_boost; thm (ii)(d)-(g), (iii), (iv) |
| B2 | synthesis.cosmological-horizon-completed-pair (v4) | formal (v); formal (iv) text; one-liner | (v) "A real pair exists exactly when Lambda > 0 ... for Lambda < 0 ... no real null vectors"; (iv) "at x = -+sqrt(12/Lambda) e0"; one-liner "kappa_Lambda = sqrt(Lambda/3)" | (v): "A pair over the base field K exists exactly when Lambda/3 is a nonzero square in K, Lambda = 3H^2 with H != 0 (over an ordered K this needs Lambda > 0, and it is not sufficient: Lambda = 7/3 over Q has none); for Lambda = 0 the plane is degenerate, for Lambda < 0 over an ordered K it is definite (no null vectors over K) ..." rest of (v) unchanged. (iv): "at x = -+(2/H) e0". One-liner: "kappa_Lambda = H". (i)-(iii) already Lambda = 3H^2 (D); check uses rational h (D). | sw_completed_pair; thm (ii)(b), (iv) |
| B3 | obj.synthesis.cosmological-horizon-boundary-modes (v3) | formal | "Let Lambda > 0 ... the completed pair ... in the plane Pi = span{e0, e_W}" | "Let Lambda = 3H^2, H > 0" (the pair and e_W = W/H are those of B2) | sw_completed_pair |
| B4 | odd-extensions.two-towers-one-curved-universe (v6) | formal (i), (ii), (iii), closing sentence | (i) "in a de Sitter universe ... the doubled Cl(1,4) and the mirror's is the complexified Cl(4,1); in anti-de Sitter ... complexified Cl(2,3) and doubled Cl(3,2)"; (ii) bivectors e_mu e5 with squares (+,-,-,-); (iii) "e5^2 = -1 ... e5^2 = +1"; closing "the unit vector along V" | Add the hypothesis "Lambda = 3H^2 (de Sitter) or Lambda = -3H'^2 (anti-de Sitter), with the base field ordered (or -1 not a square in it)"; e5 := H V in de Sitter, e5 := H' V in anti-de Sitter (Q(V) = -3/Lambda, so Q(e5) = -1, +1); closing "the unit vector H V (resp. H'V) along V". Over Q with Lambda/3 = 2 the centres are the fields of discriminants 8 and -8, neither doubled nor Cl(4,1)'s. | sw_unit_stelle_west_and_cl14, sw_anti_de_sitter_unit; thm (ii)(i)(j), (iv), (v)(c), (v)(e) |
| B5 | synthesis.mirror-extensions-causal-convention (v1) | formal (v); check (v) | (v) "doubling ours to Cl(1,4) and complexifying the mirror's to Cl(4,1)"; the check reads the type from signs at Lambda = 3, 1/2, 7 | (v): add "for Lambda = 3H^2, over an ordered base field (the complexification needs -1 not a square: theorem (v)(c))". Check: sample Lambda = 3H^2 (e.g. H = 1, 1/2, 3/7) and compute omega^2 on the basis e0..e3, W/H (Lambda = 1/2 and 7 have Lambda/3 = 1/6, 7/3, not squares). (i)-(iv) are standard-form statements (A). | sw_unit_stelle_west_and_cl14; thm (ii)(j), (v)(c) |
| B6 | odd-extensions.are-ascents-pair-signed (v4) | formal, technical, one-liner; check | "Cl(I-perp) ... the space extension Cl(1,4) for Lambda > 0 (e_V^2 = -1) and the time extension Cl(2,3) for Lambda < 0 (e_V^2 = +1)"; one-liner "Cl(I-perp) equal to Cl(1,4) or Cl(2,3) according to the sign of Lambda" | "for Lambda = 3H^2 (e_V = H V, e_V^2 = -1) ... for Lambda = -3H'^2 (e_V = H'V, e_V^2 = +1)"; one-liner "according to the sign of Lambda, Lambda = 3H^2 or -3H'^2". Check verifies signatures and dimensions only (A; its samples Lambda/3 = 3, 5/4 are not squares, so it cannot test e_V). | sw_unit_stelle_west_and_cl14, sw_anti_de_sitter_unit |
| B7 | odd-extensions.belongs-tower (v5) | formal (iii), technical, one-liner | "the coincidence Cl(I-perp) = Cl(1,4) for Lambda > 0 is induced by an isometry of quadratic spaces (I-perp has signature (1,4) outright)" | "for Lambda = 3H^2 ... induced by an isometry of quadratic spaces (e0..e3 and H V are an orthonormal basis of I-perp)"; "signature (1,4)" stays (A). Check (iii) already samples Lambda/3 a square (D). | sw_unit_stelle_west_and_cl14; thm (ii)(h) |
| B8 | odd-extensions.translation-bivectors-frozen-point (v4) | formal preamble, (i), (ii); technical; one-liner | "e5 = V/|V| the unit Stelle-West direction"; (i) Lambda > 0: Cl(I-perp) = Cl(1,4), e5^2 = -1; (ii) Lambda < 0: Cl(2,3), e5^2 = +1 | "(i) for Lambda = 3H^2, e5 = H V ...; (ii) for Lambda = -3H'^2, e5 = H'V ..."; the preamble defines e5 per case. Check samples Lambda/3 = 4, -1/4, -4/9 (squares: D). | sw_unit_stelle_west_and_cl14, sw_anti_de_sitter_unit |
| B9 | odd-extensions.cosmological-constant-deforms-wall (v3) | formal, technical, one-liner | "deformed to the doubled Cl(1,4) for Lambda > 0 and the complexified Cl(2,3) for Lambda < 0" | "for Lambda = 3H^2 ... for Lambda = -3H'^2, over an ordered base field"; the null generator's square Q = -Lambda/3 and the degenerate Cl(1,3;1) at Lambda = 0 unchanged (A). Check doubles only at square samples (D). | sw_unit_stelle_west_and_cl14, sw_anti_de_sitter_unit |
| B10 | odd-extensions.two-readings-which-which (v2) | formal, technical, one-liner | "the frozen point's [reading of Cl(1,4)], whose fifth direction is the Stelle-West vector ... with fixed norm ell = sqrt(3/Lambda)" | "with Lambda = 3H^2: fixed norm ell = 1/H (Q(V) = -ell^2), and Cl(I-perp) = Cl(1,4) through the unit H V". Check compares squares (A). | sw_unit_stelle_west_and_cl14, sw_radius_and_scales |
| B11 | odd-extensions.not-coupling-between-towers (v3) | technical | "For Lambda > 0 the algebra Cl(I-perp) = Cl(1,4) ... induced by an isometry of quadratic spaces" | "For Lambda = 3H^2 ..." | sw_unit_stelle_west_and_cl14 |
| B12 | odd-extensions.exceptional-algebra-residue-completion-both-sides (v4) | formal (ii), technical | "the weightless normalisation of the frozen point's complement is by sqrt(|Lambda|/3), which for Lambda > 0 is the asymptotic de Sitter rate H = sqrt(Lambda/3), the series' H^2 = Q(I)" | "is by H for Lambda = 3H^2 (by H' for Lambda = -3H'^2), the asymptotic de Sitter rate, H^2 = Q(I)". Clause (i) of the same entity is C1. | sw_radius_and_scales; thm (v)(d) |
| B13 | dark-matter.imported-frozen-point-de-sitter-radius (v6) | formal, technical, one-liner | "its stabiliser is the de Sitter group SO(1,4) ... hyperboloid of radius ell, ell^2 = 3/Lambda"; one-liner "radius sqrt(3/Lambda)" | "On the Einstein region with Lambda = 3H^2, H > 0 ... stabiliser SO(1,4) (I-perp is the standard (1,4) space by the unit W/H) ... radius ell = 1/H"; one-liner "radius 1/H". "signature (1,4)" and "ell^2 = 3/Lambda" stay (A). Store-internal import (T6, T10): T may restate. | sw_group_labels, sw_radius_and_scales; thm (ii)(h), (v)(b) |
| B14 | dark-energy.imported-macdowell-mansouri-theorem-stelle-west (v4, imported) | formal, technical | "V ... of fixed squared norm Q(V) = -ell^2, ell^2 = 3/Lambda ...: the vectors of Cl(1,4) are the fibre of the de Sitter group SO(1,4)" | "with Lambda = 3H^2, ell = 1/H: the frame and the unit H V generate the vectors of Cl(1,4) ..." (anti-de Sitter branch: Lambda = -3H'^2, H'V, SO(2,3)). Literature import: restating it is maintainer-only (decision D5). | sw_unit_stelle_west_and_cl14, sw_group_labels |
| B15 | synthesis.de-sitter-field-fixes-the-observer-tube-point (v4) | formal preamble; proof | "H = (Lambda/3)^{1/2}, kappa_Lambda = H ..., ell = 1/H and rho_Lambda = (12/Lambda)^{1/2} = 2 ell"; proof "round sphere of radius ell = (3/Lambda)^{1/2} = 1/kappa" | "Let Lambda = 3H^2, H > 0; kappa_Lambda = H, ell = 1/H, rho_Lambda = 2/H"; proof "radius ell = 1/H". All later clauses are rational in H (1 - kappa N = (1 - H rho/2)^2/sigma) and unchanged. | sw_radius_and_scales |
| B16 | synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale (v4) | formal; proof | "rho = 2 ell in the de Sitter normalisation sigma = 1 - Lambda Q/12 with ell = (3/Lambda)^{1/2}" | "with Lambda = 3H^2, ell = 1/H, so rho = 2/H" | sw_radius_and_scales |
| B17 | synthesis.frozen-point-complement-window-lowest-causal (v2) | formal preamble, (i)-(iv) | "I ... a vector of the tractor space R^{2,4}"; (ii) admission by Sylvester inertia; (iii) census containing (1,4), (4,1) | Read over the foundation's Q: the standard (1,4) and (4,1) are admitted iff Lambda/3 is a square (a five-dimensional subspace is all of I-perp). Restatement: "Let Lambda = 3H^2 (in (iv) Lambda = -3H'^2), and read a tower's spacetime of signature (p,q) as the standard +-1 form"; then I-perp is the standard (1,4) space over Q and (ii) holds over Q for standard forms (coordinate subspaces one way, Sylvester over R the other). As stored over R it is A(R); the row is B only if the census is meant over Q (decision D2). | sw_complement_window; thm (ii)(h) |
| B18 | note.odd-extensions.what-says-what-it-does-not | body | "the algebra realised in this universe is the doubled Cl(1,4)"; "the asymptotic rate sqrt(Lambda/3)" | "with Lambda = 3H^2, ... the doubled Cl(1,4)"; "the asymptotic rate H" (note wording, maintainer pass) | sw_unit_stelle_west_and_cl14 |
| B19 | note.odd-extensions.abstract | body | "the algebra of I-perp is ... Cl(1,4) for the observed Lambda > 0, Cl(2,3) for Lambda < 0" | "for Lambda = 3H^2 ... for Lambda = -3H'^2" (note wording) | sw_unit_stelle_west_and_cl14 |
| B20 | note.odd-extensions.holographic-coincidence | body | "the de Sitter intermediate Cl(1,4)" | "the de Sitter intermediate Cl(1,4) (Lambda = 3H^2)" (note wording) | sw_unit_stelle_west_and_cl14 |
| B21 | note.odd-extensions.two-bits-compared | body | "the doubled Cl(1,4) against the complexified Cl(2,3)" | add "(Lambda = 3H^2, resp. -3H'^2)" (note wording) | sw_unit_stelle_west_and_cl14 |
| B22 | note.odd-extensions.one-operator-sees-difference | body | "e5 is the real pseudoscalar in one tower and the pseudoscalar times a central complex unit in the other" | "e5 = H V (unit), ..." as in B4 (note wording) | sw_unit_stelle_west_and_cl14 |

### 1b. Class B(sum2): stabiliser group and Lie-algebra labels

Exact condition: SO(I-perp) is carried to SO(1,4) by a similarity iff Lambda/3 is a sum of two squares in K
(thm (v)(b)); SO(2,3) iff -Lambda/3 is (same proof with -d); for interior.non-null-stabilisers, whose I is any vector,
iff Q(I) (resp. -Q(I)) is. Fails over Q at Lambda = 9 (and Lambda = 7/3); holds with H. Uniform minimal restatement:
add "Lambda = 3H^2" where SO(1,4)/so(1,4) is named and "Lambda = -3H'^2" where SO(2,3)/so(2,3) is named (or write
SO(I-perp), decision D3). Check for every row: sw_group_labels (and thm (v)(b)).

| # | id (version) | level | clause |
|---|---|---|---|
| G1 | dark-energy.frozen-point-makes-stelle-west-vector (v7) | formal (i), technical, proof | "reduces the ambient SO(2,4)-structure to the stabiliser of I, the de Sitter group SO(1,4) for Lambda > 0 and the anti-de Sitter group SO(2,3) for Lambda < 0"; "its stabiliser in SO(1,4) (or SO(2,3))". Check already Lambda = 3H^2 (D). |
| G2 | dark-energy.imported-frozen-point-geometry (v7) | formal, technical, one-liner, proof | "stabiliser is the reductive de Sitter group SO(1,4) (for Lambda > 0; anti-de Sitter for Lambda < 0)" |
| G3 | interior.non-null-stabilisers-section-they-act (v5) | formal, technical | "so(1,4) if Q(I) > 0 and so(2,3) if Q(I) < 0" (general I): restate "so(I-perp), which is so(1,4) (resp. so(2,3)) when Q(I) (resp. -Q(I)) is a sum of two squares, in particular for Q(I) = h^2 (resp. -h^2)"; dimension 10, reductive: A |
| G4 | interior.schwarzschild-de-sitter-weighted-limit (v7) | formal, technical, one-liner, proof | "the reductive stabiliser so(1,4)" for Lambda > 0 |
| G5 | interior.stabiliser-rotates-parabolic-reductive (v2) | formal, technical, one-liner | "for Lambda > 0: the de Sitter group SO(1,4) ... for Lambda < 0: the anti-de Sitter group SO(2,3)" |
| G6 | mass.casimir-form-join (v8) | formal | "C2(I_Lambda-perp) is its de Sitter Casimir C2(so(1,4))" |
| G7 | mass.five-broken-generators (v6) | formal, technical | "for the frozen point with Lambda > 0, the stabiliser is so(1,4)" |
| G8 | mass.imported-frozen-point-tractor-connection (v6) | formal, technical, one-liner, proof | "for Lambda > 0 its stabiliser is SO(1,4)" ("signature (1,4)": A) |
| G9 | odd-extensions.imported-frozen-point (v8) | formal, technical, proof | "with stabiliser SO(1,4) or SO(2,3)" |
| G10 | standard-model.imported-grip-area-casimir-form (v5) | formal (iv), technical | "For Lambda > 0, Q(P) = Q(I)(C2(so(2,4)) - C2(so(1,4)))" (technical already "Q(I) = Lambda/3 = H^2") |
| G11 | synthesis.curvature-only-tractor-actions-are-macdowell-mansouri (v3) | formal | "the stabiliser of I (so(1,4) for Lambda > 0, so(2,3) for Lambda < 0; this is Lambda^2(I-perp))" |
| G12 | synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation (v2) | formal | "For rho != 0 the stabiliser is so(1,4) or so(2,3)" |
| G13 | synthesis.euler-term-horizon-entropy-shift (v5) | formal | "the Lorentz block of the field strength of its SO(1,4) (respectively SO(2,3)) gauge field" (an action over R; label only) |
| G14 | synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons (v4) | proof | "the four-dimensional group is the stabiliser of the reduced direction, SO(1,4)" |
| G15 | one-relation.schr-odinger-slow-shadow (v8) | proof | "the de Sitter frozen point is invariant under SO(1,4)" |
| G16 | note.dark-energy.setting-introduction | body | "reduce the ambient SO(2,4)-structure to the de Sitter group SO(1,4)" |
| G17 | note.mass.setting-grip-composite-frozen-point-2 | body | "the stabiliser acts ... through SO(1,4)" |
| G18 | note.mass.setting-machine-verification | body | "that the stabiliser is so(1,4)" |
| G19 | note.mass.setting-successor-problems | body | "the SO(1,4) covariance of (grip)" |
| G20 | note.one-relation.two-residues-named-so-synthesis-can | body | "the frozen point is SO(1,4)-invariant" |

## 2. Class C (needs more than H)

| # | id (version) | level / clause | clause as stored | exact extra condition | minimal restatement | check |
|---|---|---|---|---|---|---|
| C1 | odd-extensions.exceptional-algebra-residue-completion-both-sides (v4) | formal (i); technical; one-liner; check (i); proof (i) | "the sheaf paper's rescaling w -> w/sqrt|Lambda| is proportional, by the fixed factor sqrt 3, to ... e_V = V/|V| ...; Cl(1,3) + <+1/3> = Cl(2,3) from Lambda < 0 and Cl(1,3) + <-1/3> = Cl(1,4) from Lambda > 0"; one-liner "exceptional algebras Cl(2,3) and Cl(1,4)" | The rescaling needs |Lambda| in K^2; the isomorphisms need 3 in K^2 (centres: omega^2 = -+1/3 against -+1). With H in K (|Lambda| = 3H^2): sqrt 3 in K. | Recommended (decision D4): normalise by H (H') instead: "w/H (Lambda = 3H^2) and w/H' (Lambda = -3H'^2) have squares -1 and +1, so the exceptional algebra is exactly Cl(1,3) + <-+1> = Cl(1,4), Cl(2,3); the sheaf paper's rescaling by sqrt|Lambda| differs from it by sqrt 3 and gives Cl(1,3) + <+-1/3>, isomorphic to these exactly when 3 is a square in the base field". Alternative keeping the sheaf rescaling: add "over a base field containing sqrt 3 and H (resp. H')". Check (i): its squares -sign/3 are right; its claim "exceptional algebras Cl(2,3) and Cl(1,4)" is the over-R reading: test the H-normalised family. | sw_sheaf_rescaling; thm (v)(d) |
| C2 | odd-extensions.line-tame-wall (v4) | formal (iii); proof | "the gauge a = b, which makes I_Lambda proportional to I0 + phi, is not smooth at the wall and is not defined for Lambda < 0" (proof: a = b = sqrt(Lambda/6)) | a = b needs Lambda/6 in K^2; with Lambda = 3H^2 this is 2 in K^2 (sqrt 2 besides H): with H rational the gauge a = b is never rational. | "(iii) the gauge a = b ... exists over the base field exactly when Lambda/6 is a square there (with Lambda = 3H^2, when sqrt 2 is in it), never for Lambda < 0 over an ordered field, and is not smooth at the wall; ..." rest unchanged | sw_line_tame_wall_gauge |
| C3 | synthesis.operator-join-point-spectrum-on-positive-energy-modules (v2) | formal (2), (3); check | "At lambda s^4 = 1, B = hbar sqrt(lambda)(A + C^dag) ... K_- = B/hbar sqrt(lambda)" with lambda = Lambda/6 | With Lambda = 3H^2, lambda = H^2/2 and sqrt(lambda) = H/sqrt 2: sqrt 2 in K besides H (the matched scale s^2 = sqrt(2)/H). The stored samples Lambda = 6, 3/2 have sqrt(lambda) rational and H irrational. | "Let Lambda = 3H^2, lambda = H^2/2. (2) At s^2 = sqrt(2)/H (in the base field exactly when sqrt 2 is), B = hbar (H/sqrt 2)(A + C^dag), K_- = sqrt(2) B/(hbar H) ..."; clauses (1), (4), (5) are Hilbert-space statements (A(R)). Check: either sample over span{1, u}, u^2 = 2, or note that its points are not of the form 3H^2 with H rational. | sw_operator_join; thm (v)(f) |
| C4 | mass.weight-polynomial-two-series (v6) | formal, technical | "w = -3/2 +- I4 nu, nu = sqrt(m^2/H^2 - 9/4)" (principal series); complementary series Delta real | nu in K iff m^2/H^2 - 9/4 is a square in K (for the complementary series, Delta in K iff 9/4 - m^2/H^2 is): a condition on m/H, which H does not supply (m/H = 2 fails, 5/2 and 15/8 pass) | "w = -3/2 +- I4 nu with nu in K, nu > 0, nu^2 = m^2/H^2 - 9/4" (taking the weight as the datum and m^2 = (9/4 + nu^2) H^2 as derived removes the condition: decision D6); the expansion nu = m/H - 9H/8m + ... is over R (A(R)) | sw_weight_nu |

## 3. Class D (already written with H or kappa_Lambda = H)

synthesis.cosmological-horizon-completed-pair (i)-(iii) and check (rational h); synthesis.de-sitter-entropy-pi-n-squared;
synthesis.de-sitter-mode-count; synthesis.de-sitter-horizon-translation-is-conformal-null-rotation (check at Lambda = 3);
synthesis.de-sitter-temperature-frozen-point-norm (Lambda = 3H^2; T = sqrt(Q(I))/2pi is A(R) wording);
synthesis.positive-null-energy-gives-r-premises; synthesis.smallness-monomials-exact-hierarchy-casimir;
synthesis.frozen-phase-spectrum-not-red and synthesis.frozen-point-geometry-reads-descent-as-vacuum (Lambda = 3H^2, so
their SO(1,4) is fine); synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion,
synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus and the rung-unit family (H^2 = Lambda/3, N = M_P/H);
standard-model.trichotomy-what-kind-number, standard-model.one-number-explain, standard-model.what-derived-what-not,
programme.n-parameter-of-the-laws, synthesis.number-n-registered-free-input, synthesis.majorana-scale-* (N = M_P/H);
mass.imported-unitary-representations-de-sitter-group (m^2 = Delta(3 - Delta)H^2, nu as parameter);
synthesis.operator-join-casimir-shifts (m^2 = 2H^2). Checks already sampling Lambda = 3H^2 or Lambda/3 a square:
synthesis.de-sitter-static-boost-frozen-point, dark-energy.frozen-point-makes-stelle-west-vector,
dark-energy.imported-frozen-point-geometry, odd-extensions.translation-bivectors-frozen-point,
odd-extensions.belongs-tower (iii), odd-extensions.cosmological-constant-deforms-wall (doubling),
synthesis.de-sitter-temperature-mirror-and-status, interior.sign-fixed-internally (Lambda = 3/4), dark-energy.*-kasner checks.

## 4. A(R): over R by content; optional wording only (no restatement needed)

sqrt(Lambda/3) or sqrt(3/Lambda) written where H or 1/H would read: dark-energy.under-action-written-norm-parameter-laws
(N = M_P sqrt(3/Lambda): N = M_P/H), synthesis.promoted-norm-one-global-pair and synthesis.einstein-route-makes-n-initial-data
(same N), dark-matter.thickness-not-gravitational-quantity (ell = sqrt(3/Lambda) ~ 10^26 m), mass.mass-weight-dictionary
("every mass is sqrt(Lambda) times a factor": H times a factor), neutrino.seesaw-what-gauge-invariance-proves-what
(l = sqrt(6/Lambda) = sqrt2 L_H, L_H = sqrt(3/Lambda): l^2 = 2/H^2), synthesis.cutoff-count-is-not-a-local-density-on-sds
(M < 1/(3 sqrt Lambda): 9 Lambda M^2 < 1), synthesis.euler-term-horizon-entropy-shift (radius sqrt(3/Lambda), Nariai
1/sqrt(Lambda)), synthesis.de-sitter-temperature-mirror-and-status (kappa = sqrt(Q(I))), synthesis.imported-gibbons-hawking-entropy
(H = sqrt(Lambda/3)), synthesis.finite-range-descent-deposit-cannot-seed-cmb (H_Lambda = sqrt(Lambda/3) = H0 sqrt(Omega_Lambda)),
synthesis.r-lambda-regularity-cosmological-horizon, synthesis.clausius-route-newton-constant-is-residue,
synthesis.killing-clock-weights-binary-residue, synthesis.residue-from-mode-entropy (period 2pi/kappa_Lambda),
static-boost (iv) (2pi/sqrt(-Lambda/3)), note.dark-matter.setting-what-could-fix-unit-de-2 (ell = sqrt(3/Lambda)),
note.synthesis.what-n-is-counted (H = sqrt(Lambda/3)), standard-model.dating-descent (conjectured; H0 sqrt(Omega_Lambda)).
Decision D7: whether the maintainer pass rewrites these to H for uniformity (recommended, wording only).

## 5. Class A: checked and safe (brief)

- Rational in Lambda (hold over any K for every Lambda): mass.de-sitter-scale-frozen-point, dark-energy.stelle-west-vector-frozen-point,
  mass.exact-join, mass.grip-real ("real" is the reality structure; "(1,4) form" a signature), rungs.imported-mass-symplectic-area,
  rungs.mass-bracket-frozen-points-grip-slot, synthesis.many-twistor-join, synthesis.massless-composites-de-sitter-conformal-boundary,
  synthesis.three-twistor-composites-massive, synthesis.operator-join-ordering-constants, synthesis.sds-clausius-fixes-area-constant,
  synthesis.slot-covariance-forces-gram-square, synthesis.tube-point-clause-invariant-under-boost-commuting-symmetries,
  synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection, synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared,
  synthesis.duality-complex-structure-does-not-reach-the-frozen-point, odd-extensions.imported-frozen-point-degenerate-algebras,
  odd-extensions.transport-constrains-frozen-point-only-through (orbits are norm levels: Witt, any field),
  synthesis.stelle-west-norm-is-no-local-output, synthesis.frozen-point-action-is-bf-transport-broken-by-the-blade-i-wedge-x,
  interior.sign-fixed-internally, synthesis.majorana-element-is-null-blade-no-frozen-point-condition, synthesis.n-plus-null-ground-state,
  synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise, dark-energy.cosmological-constant-does-not-change-residue,
  synthesis.plane-wave-weak-null-crossing-null-shell-ambiguity; signature labels "(1,4)", "(2,3)" of I-perp everywhere (signs over an ordered field).
- Unit boosts of +-1 planes (Kasner relation sum p_i^2 = 1, hyperbolic atoms, local Rindler): dark-energy.forcing-half-schwarzschild-wall-residue-sense,
  dark-energy.frozen-point-datum-kasner-wall, dark-energy.imported-weighted-limit-schwarzschild-singularity-matching, sheaf.matching-connection-level,
  sheaf.matching-fibre, synthesis.unit-boost-residue-needs-nonpositive-exponent, synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling,
  synthesis.kasner-wall-matter-maxwell-bounces-stiff-moves-residue, hawking.modular-structure-completed-pair, singularity.modular-structure-completed-pair,
  singularity.imported-interior-collar-kasner-form, synthesis.collar-temperature-fixed-locally-by-r-loc, synthesis.local-boost-temperature-is-local-regularity,
  synthesis.r-loc-needs-sheet-labelled-modes, synthesis.phase-flow-is-time-rotor-flow-kms-continuation, state-selection.euclidean-partner-curvature-selected
  (Schwarzschild bifurcation sphere), synthesis.killing-horizon-value-factor-is-the-generator-boost (kappa of a general horizon, over R), note.sheaf.setting-contribution.
- Standard +-1 Clifford types (Cl_Q(p,q) mirrors Cl_R(p,q): realplace test 1 of the scratch, re-proved for the frozen point by thm (i)): the 74
  entities whose Cl(1,4), Cl(2,3), Cl(3,2), Cl(4,1) are extensions of the standard forms (list: work/S/rest_near.txt, tag cl5-far), plus
  odd-extensions.four-extensions-are-four-odd-towers, correspondence.no-real-lorentzian-vacuum-half-flat, synthesis.mirror-extensions-causal-convention (i)-(iv),
  note.odd-extensions.setting-machine-verification. Caveat: these need -1 not a square in the base field (thm (v)(c)); Q is ordered.
- Constant irrationals, not data (sqrt 2, sqrt 3, sqrt 6, sqrt(3/5), sqrt(3/8) normalisations; the scratch's "projective only"
  and "Fock-model convention"): correspondence.reality-conjugation-twistor-form-factor, correspondence.spinor-identification,
  families.alignment-computed-thirteenth-refutation-democracy-one, neutrino.imported-indifference-faces-democratic-alignment-rank,
  synthesis.clifford-conjugation-is-the-twistor-adjoint-and-its-trace-form-is-the-one-particle-gupta-bleuler-form,
  synthesis.covariant-rung-coupling-gives-the-normal-pair-tree-level-b-meson-mixing-that-excludes-the-transmutation-branch,
  synthesis.real-structure-breaks-source-stabiliser-to-z2, standard-model.complete-multiplets-shift-all-three-coefficients,
  standard-model.matching-traces, families.rigidity-pairing-sector-one-event (check). Decision D8 for Leon (out of this run's scope).
- Over R by content, other data (A(R)): singularity.transport-schwarzschild-fibre (sqrt r, sqrt(2M)), scrambling.imported-collars-coframe-exceptional-set-helicity,
  synthesis.circulant-charged-leptons-excluded-with-real-neutrino-sectors, synthesis.koide-channel-phase-is-no-symmetry-angle,
  synthesis.mass-ordered-dressing-cannot-spoil-koide, synthesis.imported-fritzsch-texture-cabibbo-formula, synthesis.complex-neutrino-stages-keep-the-solar-sum-rule,
  synthesis.rung-field-level-needed-off-balance-and-not-right-invariant, synthesis.scale-free-rung-potentials-need-the-flat-physical-branch,
  synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy, mass.weight-composite and families.imported-dictionary-exact-join
  and standard-model.imported-frozen-point-dictionary (nu by its expansion), synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall
  (sqrt(8 pi G) q), synthesis.imported-five-dimensional-chern-simons-gravity, dark-matter.d-democracy-total-mass, dark-matter.democracy-de-sitter-radius-unit-ball,
  dark-matter.no-coupling-rule-odd-towers-follows, synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands,
  synthesis.c-loc-entropy-clause-curvature-independent-density, the remaining "Hubble" mentions (Kasner Hubble normalisation in interior.*, sheaf.*, singularity.*,
  obj.interior.weighted-blow-up-hubble-normalisation-admissible and their notes; measured H0 in cosmology imports) and the remaining "cosmological horizon"
  mentions in thermal and entropy statements (work/S/rest_near.txt), mass.weight-composite / note.mass.what-join-says (sqrt2 |B|/H at leading order),
  note.mass.setting-prior-art (Dixmier's SO(1,4) representations, literature).
- Predictions: none depends (pred.dark-energy-w-minus-one and the four others mentioning Lambda hold for every Lambda).

## Counts
B: 22 rows (17 claims and objects B1-B17, 5 notes B18-B22). B(sum2): 20 rows (15 claims G1-G15, 5 notes G16-G20).
C: 4 rows (C1-C4). D: about 30 entities (section 3). A(R) wording-only: 19 entities (section 4). A: the rest of the 332 hits.
Entities with at least one B, B(sum2) or C row: 45 (claims and objects 35, notes 10; odd-extensions.exceptional-algebra-residue-completion-both-sides
has both a B row, B12, and a C row, C1).
