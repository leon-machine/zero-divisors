# GTG proofs, prover P1 (run 2026-11-07-consistency)

Entities: gtg_1.txt (11). For each: proof-main.tex rewritten (or kept), new exact check functions in the entity's
check.py (lib/GA.py and lib/gtg.py, Fractions only, premise() for each premise used), runcheck pass, check4 on a
proposals/ copy (deleted after) with 0 errors and no W413, coverage.yaml entry, credit entry and
`extraction.maintainer_pass_gtg_proof` note. lib/ was not edited. Versions: all were already lock + 1 in this
run except synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet, bumped 2 -> 3 (E206 otherwise).
Where an entity had no orig-proof-main.tex, the pre-pass proof (HEAD) was saved as orig-proof-main.tex; existing
ones were kept. No status, link or assumes changed except item D2 below.

Validation: `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon`: 0 errors, 0 warnings
store-wide; for these ids only the pre-existing I213 on synthesis.black-hole-data-do-not-fix-field-equations.
GA language scan (tp.galang): no hits on any of the 11.

## Per entity

| entity | GTG proof | checks added | outside_ga | items |
|---|---|---|---|---|
| dark-energy.gravity-pre-metric-forces-degenerate-exactly (v5) | yes | check_gtg_star_free_density_is_a_divergence, check_gtg_hodge_star_is_the_cometric_duality, check_gtg_star_has_no_limit_at_a_corank_one_wall | removed | none |
| dark-energy.stelle-west-vector-frozen-point (v6) | yes | check_tractor_gauge_field_slots_and_bracket | removed | none |
| dark-energy.walls-free-sector (v6) | no (kept) | none | kept, narrowed | none |
| synthesis.black-hole-data-do-not-fix-field-equations (v7) | yes | check_gtg_black_hole_data | removed | none |
| synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet (v2 -> 3) | yes, clause (ii) (rest already GTG) | check_gtg_ingoing_generator_is_affine_and_horizon_rate | removed | H5 |
| synthesis.cosmological-horizon-completed-pair (v4) | yes, Step 1 (Steps 2-5 already Cl(2,4)) | check_gtg_dilation_field_curvature_selects_no_plane | removed | H5 |
| synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff (v3) | yes (setting and readings; arguments already Cl(2,4)) | check_gtg_readings_of_the_curvature_operator | removed | none |
| synthesis.killing-horizon-value-factor-is-the-generator-boost (v2) | yes, clause (iv) (i)-(iii) already GA | check_gtg_pg_torsion_equation_and_killing_line | removed | A6, D2 |
| synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons (v3) | yes (base forms as multivector fields) | check_gtg_reduction_with_base_forms_as_background_multivectors | kept, narrowed | A11 (nothing to do) |
| synthesis.nondiagonal-kasner-residue-weighted-shear (v4) | yes | check_gtg_torsion_equation_gives_the_boost_block | removed | none |
| synthesis.two-frozen-points-conformally-flat (v4) | yes | check_gtg_parallel_tractors_flat_strength_and_einstein_scale | removed | none |

## What was proved how

- **gravity-pre-metric.** Forms as multivector fields (d = grad ^, wedge = outer product, internal Lie algebra as
  bivectors of an internal Clifford algebra, trace = internal scalar part): Bianchi, <F ^ F> = grad ^ CS, variation a
  boundary term. The Hodge star derived as the physical duality read back: *_g F = |det hb|^-1 I G(F), G = hb hb^T
  the cometric map; scale and rotation-gauge invariant, squares to -1 (G(I G(F)) = det(G) I F); at a corank-one
  wall G -> G_0 of rank 3, det hb -> 0, so no limit and |det hb| * -> I G_0 of rank 3. Checked against the component
  star on three fields (one with det hb < 0).
- **stelle-west.** The Fact's slot connection shown in the proof (not cited from the tractor theorem, which rests on
  this lemma) to be Omega_T(a) = Omega(a) - ninf ^ A + n0 ^ P(A); Theta(A) = A ^ W at P = (Lambda/6) id;
  D^T X = (A ^ W) . n0 = A; bracket = commutator product.
- **black-hole-data.** Variation of hb at torsion-free Omega with P_f = df/dcalR(a); Schwarzschild and RN as PG
  fields (curvature operator, Ricci map, Kretschmann, radial eigenvalue 2M/r^3 = sqrt(K/12), (K.D)K = K/4M). The
  Wald contraction E^{abcd} eps_ab eps_cd read as the derivative of the Lagrangian along S(B) = -<B sigma> sigma
  (Ricci map -P_sigma, scalar -2): sign fixed by the Einstein term (A/4G) and confirmed against the component
  contraction for beta Ric^2 at the RN horizon (-8 pi beta Q^2 A/r_+^4).
- **collapsing-hole (ii).** k = hb^{-1}(x') = (gamma_1 - gamma_0)/(1 + beta) and D_{x'} k = 0 with the PG
  connection; (K.D)K = K/4M on the horizon. Gamma^r_rr, Gamma^v_vv kept as reading (the formal's parenthesis is
  unchanged).
- **cosmological-horizon Step 1.** Dilation field hb^{-1}(a) = a/sigma; torsion equation solved by
  omega(A) = grad sigma ^ A; R(a ^ b) = -(Lambda/3) sigma^-2 a ^ b in GA, so calR = (Lambda/3) id, Weyl 0;
  -Lambda/3 of the round-sphere-positive convention via C11.
- **frozen-point stiffness.** Readings made GA: curvature operator without pair symmetry, Ricci map
  d_a . calR(a ^ b) (equal to the index contraction also with torsion, checked), Schouten/Einstein/Weyl maps, traces,
  slot derivative as a map, Weyl square and Euler density in GA, all checked against the index values.
- **killing-horizon (iv).** Torsion equation solved for general beta(r) on the constant physical frame; both sides
  computed from the coframe jets; Omega(e_t) = -beta beta' sigma_r = (f'/2) sigma_r.
- **macdowell-mansouri.** Language paragraph: base forms as multivector fields of a flat 5D background (d-dim GTG),
  exterior product = outer product, d = grad ^; (i) recomputed with the outer product of Cl(1,4). The added check
  records the reading (outer product of disjoint blades equals the Grassmann product) more than it tests new content;
  said so in coverage.yaml.
- **nondiagonal-kasner.** Torsion equation: its a = 0 part forces no boost in omega(gamma_0) and a symmetric boost
  block; the gamma^0-legs give omega(gamma_m) = -(1/tau) sym(B) and omega(gamma_0) = (1/tau) antisym(B) (the
  statement's "up to the sign convention" now has its definite GTG sign), also for x-dependent theta0; (iv) through
  gamma_0 . calR(gamma_0) = d_tau tr K + tr K^2 and -2 gamma_0 . calG(gamma_0) = (tr K)^2 - tr K^2 + s R3 (both
  checked exactly on flat slices). The coverage judge's "connection identification argued only" is now computed.
- **two-frozen-points.** Flat-scale connection as -ninf ^ a; parallel tractors sigma ninf + (m - r x) + r n0; norm in
  one line; flat strength; the Einstein claim for sigma^-2 eta now checked exactly (the coverage judge had it
  untested); stabilisers as bivectors of Cl(2,4).

## Declarations kept (and why)

- **dark-energy.walls-free-sector**: not achieved. The result is a rank and symbol-rank count of the Einstein-Cartan
  equations in components at a point where hb^{-1} has corank one. hb does not exist there, so the GTG definition
  (stated on the invertible region, reading omega(A) = Omega(hb(A)) and the physical frame through hb) does not
  apply; a GTG proof needs an extension of the definition to degenerate soldering that the store does not have. The
  equations could be written as GA expressions in hb^{-1} and Omega, but the counts would remain component ranks.
  Component proof and checks unchanged; why narrowed.
- **synthesis.macdowell-mansouri-...**: narrowed to the imported transgression and variation formulas of 5D
  Chern-Simons forms (theorems about differential forms in the imported Facts), read through the multivector
  dictionary; nothing else in the proof is a stand-in.

## Items applied

- **A6** (killing-horizon): (iv) beta = +sqrt(1 - f); -H is the de Sitter value in this chart (past cosmological
  horizon), +H in the expanding chart on the future one; (iii) "future and past horizons"; proof and technical
  aligned; (K.D)K = beta(r_h) f'(r_h)/2 K checked exactly at three PG horizons (1/4, -2/3, +2/3).
- **D2** (killing-horizon): uses pins on boost-evolution@4, affine-cell@3, positive-null-energy@7 replaced by
  synthesis.null-vacuum-on-a-horizon-generator@1; claimrefs in the formal and proof to the old three turned into text
  mentions, null-vacuum (i) cited for the weight-1/2 dilation; check.py premise() calls changed (one per function);
  the untouched-premise entry for positive-null-energy removed from coverage.yaml. Note in
  `maintainer_pass_decisions`.
- **A11** (macdowell-mansouri): already applied at v3; text kept.
- **H5** (added to items-for-gtg.md during the run): cosmological-horizon (iii) and proof Step 3 name the unit of the
  phase, span{1, hat-I}; collapsing-hole formal states its normalisation (rho = r/2M) against the companion's
  (rho = r - 2M, U = -rho e^{rho/2M}). Notes in `maintainer_pass_decisions`.

## For Leon

- The formal levels of black-hole-data, frozen-point stiffness and collapsing-hole still carry index expressions as
  labelled readings (allowed by the conventions; not changed, as no item decided it).
- macdowell-mansouri's new check is close to a tautology (it confirms the reading); if a stronger GA check is wanted,
  it would have to re-derive the transgression formula, i.e. restate the imported Chern-Weil Fact.
