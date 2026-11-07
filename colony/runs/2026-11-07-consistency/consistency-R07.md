# Consistency read R07 (dark-energy and interior), 2026-11-07

Read in full: all 171 ids of read_R07.txt, in dependency order: every formal, technical, lay and one-liner
level and every proof file (proof-main.tex, proof-standard-route.tex), with the derivations (uses, assumes,
pins). Extraction notes were read where a level or proof pointed to them (source_formal, maintainer notes of
the entities fixed). Key numbers were recomputed by hand or exactly (scratch R07/verify/v1.py to v4.py).
Check run once (layers 1-3): no error or warning on any entity changed here; three W222 on GA-owned
entities (listed in ga-issues-R07.md).

## Fixed (old -> new version, what)
- interior.weighted-limit-theorem 5 -> 6: proof, phi-line connection sign: -(d_tau a_3) B_3 + cos(theta) R_23 (exact check v4.py).
- sheaf.matching-fibre 4 -> 5: formal cited the holonomy algebra as "Fact obj.interior.weighted-blow-up..." (a Definition); now Fact sheaf.weighted-limit.
- sheaf.matching-connection-level 7 -> 8: same wrong citation, 3x formal and 2x proof, now sheaf.weighted-limit.
- standard-model.trichotomy-what-kind-number 10 -> 11: proof rung arithmetic still R ~ 400 from N ~ 10^60; now R ~ 405 with 2^405 < N^2 < 2^406 (exact interval arithmetic, v3.py), script's coarse pair named as such.
- dark-matter.imported-trichotomy-descents-data 5 -> 6: clause (2) "the frozen action is N-insensitive" (false: prefactor 3/Lambda; not the cited clause) now states the cited content (norm fixed by a constraint, pure gauge, no equation of motion); paper wording kept in source_formal.
- note.dark-energy.point-contact-why-form-not-value 2 -> 3: prefactor "3/Q(I)" corrected to 1/Q(I) = 3/Lambda.
- odd-extensions.imported-frozen-point 6 -> 7: notation clash "e^mu = hb^{-1}(e^mu)" resolved to a -> hb^{-1}(a); translation part hb^{-1}(a) ^ V/Q(V).
- odd-extensions.translation-bivectors-frozen-point 3 -> 4: translation part "e^mu ^ V/ell" (scalar wrong, against its own "up to 1/ell" and the Fact) now -hb^{-1}(a) ^ V/ell^2 = -hb^{-1}(a) ^ e_5/ell.
- dark-energy.imported-henneaux-teitelboim-promotion 5 -> 6: technical and lay still said the transcription is an open decision, against the formal (series keeps Lambda fixed by the frozen point, promotion read as the Clausius route's variational form) and the 2026-10-23 adoption.
- synthesis.imported-large-scale-potential-and-sachs-wolfe-relations 1 -> 2: technical "isocurvature six times more visible at the same amplitude" contradicted the formal -(1/5)(zeta + 2 Omega_c S_c); now 2 Omega_c ~ 1.7, the six being at the same potential.
- synthesis.imported-nielsen-olesen-string-tension 1 -> 2: bare i in D = partial - ieA (missed by the unit detectors) now I_4, source form in source_formal.
- synthesis.imported-maxwell-stress-spacetime-algebra 1 -> 2: cross product E x B now -I<EB>_2 (exact check v1.py), source form in source_formal.
- interior.imported-kerr-schild-form-kerr-gauge 1 -> 2 and interior.unipotency-across-kerr-family 5 -> 6: k^2 written Q(k) (house style).
- synthesis.crossing-transport-tipler-threshold-sharp 4 -> 5: undeclared unit I in the complex exponents 1/2 +- I omega now I_4.
- synthesis.de-sitter-static-boost-frozen-point 5 -> 6: proof step 5 "e^{tN} X(x)" (N undefined, and N = M_P/H in this subject) now e^{-tB_0/2} X e^{tB_0/2} = X(x - t e_0) (exact check v2.py).
- synthesis.frozen-phase-spectrum-not-red 3 -> 4: proof (i) translation rotor sign: 1 + n_inf a/2 maps X(x) to X(x - a); now 1 - n_inf a/2 (exact check v2.py). Its check accepts either sandwich, which is why it did not catch this.
- synthesis.tangential-derivative-transport-bound 3 -> 4: proof pointer to the filed sharpness example made exact (tau^{1/2} phi(x/tau^2), not phi(x/tau)).
- pred.dark-energy-w-minus-one 3 -> 4: cited Proposition vacuum-region-registration-condition as "Theorem".

## For Leon (not changed; evidence and proposed fix)
1. odd-extensions.transport-constrains-frozen-point-only-through, formal (i) and technical: "the null partner phi of I with Q(I,phi) = 1, ... phi perp {I}^perp cap W". Since W = I_0^perp, {I}^perp cap W = W contains I, so the condition contradicts Q(I,phi) = 1. The proof uses only the isometry fixing W; clause (ii) uses "orthogonal to the Lorentz frame". Proposed: "phi orthogonal to the Lorentz frame of W".
2. synthesis.frozen-point-geometry-reads-descent-as-vacuum formal (ii) and technical, and standard-model.dating-descent formal (iii): "the same [observed] modes sit inside the frozen phase's Hubble length by k/(a_d H_Lambda) > 7 x 10^9 at 1 MeV". The proof derives it for k >= a_0H_0 only; the observed range starts at k = 2/eta_0 (k/a_0H_0 in (0.627, 0.631)), where the ratio is below 4.6 x 10^9 (exact upper bound, v3.py) and about 4.5 x 10^9. Proposed: "> 4 x 10^9 at 1 MeV (> 7 x 10^9 for k >= a_0H_0)". The conclusion (every observed mode inside) is unaffected.
3. Promotion status: the store adopted the Henneaux-Teitelboim promotion (2026-10-23; programme.n-parameter-of-the-laws, synthesis.number-n-registered-free-input, standard-model.dating-descent), but standard-model.trichotomy-what-kind-number clause (4) (formal, technical, lay: "a decision for the series, recorded open") and standard-model.what (ii) ("the decision ... records open") still read as undecided; the T10 notes (what-clause-3-requires-what-it, setting-levels-results, setting-successor-problems) do too, as paper text. Proposed: add "which the store adopts (programme.n-parameter-of-the-laws)" after each "recorded open"; leave the notes as dated paper text.
4. dark-energy.acoustic-no-go-one-way-grip, formal: "the reduced theory proves there is no other channel through which to couple" while the same formal says that in the thermal state the whole C-even neutral subalgebra, strictly larger than T's conformal family, can couple. Proposed: "... no channel outside the C-even neutral sector".
5. Duplicate: sheaf.kasner-data-interior (status imported, Kasner 1921) states the Schwarzschild Kasner exponents that interior.kasner-form-interior proves with rates; its own provenance says so. Proposed: make it a restatement (proved, uses interior.kasner-form-interior) or retire it in favour of interior.kasner-form-interior (the better one).
6. Same names: "(P1)", "(P2)" are the Kasner-exit premises (synthesis.pre-descent-*-premise), but synthesis.frozen-point-geometry-reads-descent-as-vacuum's formal says "the reading of the dating and of P1: one frozen point" and odd-extensions.cosmological-constant-undetermined-within-series cites "the dark-matter paper's Premise P2". Proposed: a "Same names" line in conventions.md, or rename the Kasner-exit premises (K1), (K2).
7. GA language in entities not owned by the rewriters (more than small stand-ins, so not rewritten here): dark-energy.imported-macdowell-mansouri-theorem-stelle-west (differential forms primary, GA form secondary; imported, so the forms could move to source_formal); dark-energy.gravity-pre-metric-forces-degenerate-exactly (tr(F ^ *F), Hodge star in components); synthesis.promoted-norm-one-global-pair (3-form T, de Rham cohomology); synthesis.promoted-norm-weyl-clock-flat-weight (forms, Weyl components); dark-energy.imported-frozen-point-geometry and dark-energy.stelle-west-vector-frozen-point (tractor slots with g_ab, P_ab beside the GA gauge field). Decide whether they go to the rewriters.

## Duplicates
- sheaf.kasner-data-interior duplicates interior.kasner-form-interior (For Leon 5).
- The "Imported: ..." restatements (dark-energy.imported-frozen-point-geometry, dark-matter.imported-frozen-point-de-sitter-radius, odd-extensions.imported-frozen-point, standard-model.imported-frozen-point-dictionary, sheaf.weighted-limit, dark-energy.imported-weighted-limit-schwarzschild-singularity-matching, singularity.imported-interior-collar-kasner-form, standard-model.imported-norm-frozen-point-not-field, dark-matter.imported-trichotomy-descents-data) are restatements by design (restates), consistent with their originals after the fixes above.

## Known open items
None of the listed open items falls in R07. The I_6 item touches note.mass.what-nullity-fixes only as a dependency (xsubject-R07.md).

## Checked and found consistent (selection)
Stelle-West algebra (e ^ W action, [e^W, e^W] = (Lambda/3) e^e, Q(I)Q(V) = -1); Kasner curvature, Kretschmann -16 p1p2p3 tau^-4 and Gauss-Bonnet density; Bianchi I residue series (h_{i,1}, no resonance); the store's Einstein-equation sign (G = -8piG T - Lambda g, p = -rho); I_g norm R/12; Schwarzschild interior series (-2/15, -8/105); de Sitter conformal factor and frozen point; dictionary m^2 = Delta(3 - Delta)H^2 and its bounds; finite-range bound, rho(1 MeV) ~ 5.2e7, K > 460, 9.5e-6; frozen-phase index arithmetic; holographic amplitudes; quasi-free shot term ~7e-78; Pati-Salam G mu and f_10; tree-level coupling windows; instanton actions; Kerr scale, disc value, windings -3; Taub-NUT kappa = cot(phi/2); Vaidya Schouten tensor and focusing sign; plane-wave Schouten sign.

## Counts
Read 171; fixed 19 (all with version + 1); For Leon 7; duplicates 1 (plus restatements by design); GA issues for the rewriters 9 entities; cross-subject 2; known open items settled 0 (none in R07).
