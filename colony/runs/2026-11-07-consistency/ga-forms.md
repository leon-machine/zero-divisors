# GA rewrite: differential forms (run 2026-11-07-consistency)

Owner: the forms rewriter. Entities: ga_forms.txt (26) plus two added by the coordinator,
dark-energy.wall-counterterm and standard-model.connection-forced. Every equivalence that is more than
notation was checked exactly with lib/GA.py and lib/gtg.py in the maintainer scratch; each entity's
`extraction.maintainer_pass_ga_rewrite` note says what was checked. No status, link, pin, assumes edge,
ledger or check.py was changed. Pins of dependants on the bumped entities are now stale (no repin done).

A tool used throughout: the first structure equation in GA, the torsion equation of the Definition (f)
read on a constant physical frame, hb^T(grad ^ f^a) = sum_b gamma^b ^ (omega(gamma_b) . gamma^a), with
hb^T(f^a) = gamma^a and omega(gamma_b) = Omega(hb(gamma_b)). Checked exactly against the stored
connections of the PG, interior, static-Schwarzschild, Rosen and variable-exponent Kasner fields (the
opposite sign fails every time).

## Rewritten (old -> new version)

- interior.interior-connection-exactly 7 -> 8: proof solves the GA torsion equation; Cartan forms a labelled reading.
- singularity.connection-bivector-computed 4 -> 5: clause (2) states omega(gamma_c) as bivectors
  (omega(gamma_1) = -beta' sigma_r, omega(gamma_2) = (beta gamma_0 + gamma_1) ^ gamma_2 / r, ...), sigma_r = gamma_1 gamma_0 stated; proof in GA.
- dark-energy.cosmological-constant-does-not-change-residue 6 -> 7: gauge field hb^{-1}(e_i) = a_i gamma_i; forms and line element as readings.
- dark-energy.frozen-point-datum-kasner-wall 7 -> 8: datum as Cl(2,4) vectors and Omega_T; pole Omega(hb(e_i)) = -(p_i/tau) B_i;
  calR(B_i) = p_i(p_i-1) tau^-2 B_i, calR(e_i ^ e_j) = p_i p_j tau^-2 e_i ^ e_j; Ricci map; densities E det(hb)^-1 etc.; proof in GA.
- dark-energy.variable-exponents-residue-pointwise-corrections-are 4 -> 5: omega(gamma_i) = -(p_i/tau) B_i - log(tau) hb^T(grad p_i) ^ gamma_i; proof in GA.
- dark-energy.wall-counterterm 5 -> 6: CS(Omega) and the topological density built from Omega with <X, Y>_eps = 4 <X I_4^-1 Y>; d = grad ^; slice value computed in GA.
- dark-matter.mirror-tower-copy-one 8 -> 9: Hodge star as duality with I; reversal invariance of <F^2>_0, <I F^2>_0.
- dark-matter.no-coupling-rule-odd-towers-follows 4 -> 5: scaling of det(hb)^-1 <(hb^T F)^2>_0.
- note.singularity.setting-curvature-operator-cartan-structure-equations 1 -> 2: static gauge field, Omega and calR in GA; Cartan computation kept as labelled reading; eigenvalues now exact.
- note.dark-energy.setting-machine-verification 2 -> 3: GA names for the Kasner, variable-exponent and counterterm checks (Q -> CS); rest declared (below).
- synthesis.charged-vaidya-cauchy-horizon-tractor-threshold 1 -> 2: Schouten map with N = hb^T(grad v), projections P_2, P_S; conormal N/w; P(k) = S nu n + R.
- synthesis.collar-kms-extension-completion-locus 3 -> 4: proof (i): synchronous gauge field, F_K = (D ^ K)/2 = a' B_1.
- synthesis.euler-entropy-first-order-rate-on-local-patches 2 -> 3: plane waves as gauge fields; signature sentence fixed (R03).
- synthesis.euler-term-horizon-entropy-shift 4 -> 5: Euler form E[X] = 2 <X(a^b) I^-1 X(I d_b ^ d_a)>; l^2 E[calR - s l^-2] = -4s(R - 2 Lambda + alpha E_4); proof bilinear in E; conformal factor renamed varrho.
- synthesis.infinity-vacuum-incidence-is-a-property-of-the-scale 3 -> 4: tractors as Cl(2,4) vectors, Omega_T, Schouten map; dilation field for the example.
- synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching 3 -> 4: (iii) curvature operator and Kretschmann in GA.
- synthesis.kasner-wall-matter-maxwell-bounces-stiff-moves-residue 2 -> 3: Maxwell as DF = 0, forms as reading.
- synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons 2 -> 3: Weyl sign in (iii) (R03); base forms declared (below).
- synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise 2 -> 3: dilation slot beta(a) = a . b; dust as hb^{-1}(a) = tau^2 a; T - (tau/3) id; vector A renamed u (R03).
- synthesis.plane-wave-weak-null-crossing-null-shell-ambiguity 4 -> 5: gauge named; n = hb^T(grad u); Omega(hb(gamma_A)) = -(a_u/a) n ^ gamma_A; P(v) = (a_uu/a)(v . n) n.
- synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall 1 -> 2: calR(a) = -8 pi G (a . hat-grad phi) hat-grad phi; exact Ricci map in the proof (was "up to sign").
- synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point 3 -> 4: store-sign eigenvalues, no "up to sign".
- synthesis.unit-boost-residue-needs-nonpositive-exponent 3 -> 4: (3) gauge field, kinetic term Q(hb^T(grad phi))/2, proof with the Ricci map.
- standard-model.connection-forced 4 -> 5 (one bump, shared with reader R04's edit): proof speaks of the gauge field, so(2,4) as bivectors acting with 1/2.

## Not rewritten

- pairing.displacement-pairs-point-mode-vacuum-parallel: false positive; dx = dx^a e_a is the displacement vector, already GA.
- synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling: only the derived-metric line element (the conventions' sanctioned reading) and an already labelled component perturbation h_ab.
- synthesis.pre-descent-contracting-kasner-stage-premise: postulate; only "whose derived metric is" a line element.
- synthesis.loc-independent-of-clausius-and-killing-data: line element of the Einstein static universe, beyond one flat chart and already flagged; tensors already GTG readings.
- Declared outside_ga (other): synthesis.macdowell-mansouri-... (the base forms of a five-dimensional Chern-Simons five-form, from imported form theorems); note.dark-energy.setting-machine-verification (describes the legacy script's own component and form computations).

## Possible errors found

- synthesis.euler-term-horizon-entropy-shift: the formal level wrote E_4 = -2 <calR(a^b) I calR(I d_b ^ d_a)> in a statement covering Euclidean signature; that form gives -E_4 when I^2 = +1. Replaced by the I^{-1} form (checked in Cl(1,3) and Cl(4,0)).
- dark-energy.wall-counterterm sign (R09): not an error. omega^{ab} are the components of Omega = (1/2) omega^{ab} gamma_a ^ gamma_b in the Definition's sign (on Kasner, -(p_i/tau) B_i); the coefficient +8 p1 p2 p3 belongs to this; the right-action values would give -8. Now explicit.
- synthesis.scalar-kasner-wall... and synthesis.tree-level...: proofs gave Kasner Ricci/field-strength values only "up to sign"; the exact store-sign values are now stated.
- Concurrency: another agent had declared outside_ga on dark-energy.wall-counterterm with a second maintainer_pass_ga_rewrite key (duplicate YAML key); merged into one note, declaration withdrawn.

## Reader issues addressed

R01 (collar-kms proof (i)); R03 #3 (macdowell Weyl sign), #4 (parallel-frozen-point A clash), #5 (euler-entropy signature sentence);
R04 (connection-forced); R05 #1, #4 (mirror, no-coupling: done in an equivalent GA form; the |<pi^1 pi^2>|^2 unit question and the
"structural level vs proved" status are left for Leon); R06 #8 (sigma_r orientation stated); R07 (frozen-point, variable-exponents,
interior rewritten, W222 cleared; cosmological-constant kept as reading); R08 (euler-term); R09 (wall-counterterm sign, above).

## Validation

tp check layers 1-3 filtered to these ids: 0 errors, 0 warnings (I213 subject notes only). galang.unexcused empty on all 28.
