# GTG proofs, prover P2 (run 2026-11-07-consistency)

Entities: gtg_2.txt (11). Each new check is exact: Fractions, lib/GA.py and lib/gtg.py, premise() for each
premise used. Each was run with colony/runcheck.py and then with colony/check4.py on a proposals/ copy, and every
copy was deleted afterwards. All 11 finish at 0 errors and no W413. Three first drafts were weak (W413 on
einstein-condition and macdowell-mansouri-principle, W413 on euler-entropy, E408 on frozen-point), and all were
tightened: sample data moved out of the function bodies, and a value that depends on the data pinned.

Versions follow store/.tp-lock.json:
- Bumped: pairing.static-frame (7 -> 8), pairing.regular-frame (6 -> 7) and synthesis.taub-nut (2 -> 3). Each was at its locked version.
- Kept: the other eight, which were already above their locked versions in this run.

Bookkeeping:
- Each entity has a credit entry for its version and an `extraction.maintainer_pass_gtg_proof` note saying what was proved and checked.
- Every changed proof keeps its original as orig-proof-main.tex. Where that file did not exist, the pre-GTG proof was copied into it.
- No status, link, pin, assumes edge or formal statement was changed.
- The orchestrator's checkpoint commits picked up the edits; I made no commit.

Validation: `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon` gives 0 errors and 0
warnings store-wide, with no finding on my ids. `tp.galang.unexcused` is empty on all 11.

| Entity | GTG proof | Checks added | outside_ga | Items |
|---|---|---|---|---|
| dark-energy.frozen-point-makes-stelle-west-vector | yes | check_gtg_stelle_west_datum_on_einstein_fields_both_branches, check_gtg_tractor_field_strength_in_the_lorentz_algebra_of_i_v_perp | narrowed | none |
| pairing.regular-frame-class-vanishes-horizon-changes | yes | check_gtg_torsion_solution_is_the_pg_gauge_field, check_gtg_classes_and_loop_class_in_cl23 | removed | none |
| pairing.static-frame-only-expansion-survives | yes | check_gtg_torsion_solution_is_the_stated_gauge_field, check_gtg_classes_with_the_central_unit_of_cl23 | removed | none |
| singularity.transport-schwarzschild-fibre | yes | check_gtg_dual_norm_of_the_dying_direction_from_the_engine | narrowed | none |
| synthesis.einstein-condition-is-infinity-vacuum-incidence | yes | check_gtg_tractor_gauge_field_moves_ig_and_x, check_gtg_own_ray_classes_on_gauge_fields, check_gtg_infinity_vacua_with_the_unit_i7 | narrowed | none |
| synthesis.euler-entropy-of-a-horizon-patch-is-an-edge-term | yes for (i) computation and (ii); the (i) reading stays in forms | check_gtg_cut_gauge_field_transgression_gauge_law_and_edge_curvature, check_gtg_binormal_contraction_is_four_times_the_cut_component | narrowed | none |
| synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part | yes ((i) to (iii); (iv) algebra unchanged) | check_gtg_frame_trivector_is_twice_dual_einstein_plus_lambda, check_gtg_frame_equation_on_gauge_fields_and_dilation_trace | removed | none |
| synthesis.promoted-norm-one-global-pair | yes for (i), (ii); (iii) is global and stays in forms | check_gtg_pointwise_count_in_cl24, check_gtg_multiplier_equation_is_grad_lambda_zero | narrowed | none |
| synthesis.promoted-norm-weyl-clock-flat-weight | yes | check_gtg_instantons_as_euclidean_gauge_fields, check_gtg_kasner_and_flrw_densities_from_gauge_fields | narrowed | none |
| synthesis.series-wald-entropy-changes-without-flux-on-local-horizons | yes (curvature content; Gauss and Sachs equations kept in components) | check_gtg_sds_field_strength_on_radial_generators, check_gtg_horizon_cross_section_surface_gravity_and_value | narrowed | G6 applied |
| synthesis.taub-nut-cauchy-horizon-is-taub-point-with-complex-residue | yes ((i); (ii) to (iv) were rational algebra and GA already) | check_gtg_bianchi_ix_torsion_solution_and_field_strength, check_gtg_taub_nut_is_a_vacuum_gauge_field | removed | none |

## Per entity

- **pairing.static-frame-only-expansion-survives** (7 -> 8).
  - Proof:
    - The static gauge field. The rotation-gauge field is solved from the torsion equation hb^T(grad ^ f^a) = sum_b e^b ^ (Omega(e_b) . e^a), which is unique (rank 24): Omega(e_0) = (f'/2 sqrt f) e_1 e_0, Omega(e_1) = 0, Omega(e_2) = (sqrt f/r) e_1 ^ e_2, Omega(e_3) = (sqrt f/r) e_1 ^ e_3 + (cot/r) e_2 ^ e_3.
    - The classes are symmetric products in Cl(2,3) with the central unit I_5, which replaces the Gaussian rationals.
    - Connection forms and spin coefficients are kept as a labelled reading.
  - Checks: the solve from the coframe alone at four points; I_5 central with square -1; classes on e_c and on the tetrad; -48/125 at r = 25/16.
  - outside_ga: removed.

- **pairing.regular-frame-class-vanishes-horizon-changes** (6 -> 7).
  - Proof:
    - The PG gauge field. The solved Omega is Omega(e_0) = 0, Omega(e_1) = -beta' e_1 e_0, Omega(e_2) = (beta e_0 + e_1) ^ e_2/r, and so on.
    - Classes come from (u ^ e_2) . l = -(u . l) e_2 in Cl(2,3) with I_5.
    - Covariance uses the static frame built inside the same gauge. The loop class comes from the field strength of the solved field.
    - Structure equations are kept as a labelled reading.
  - Checks: the solve (rank 24) at five points β = 4/5, 1, 2, 1/3, 3/5; outgoing and ingoing classes; (l.D)l; the values 144/125, 2, 12; the loop class 2M/r^3.
  - outside_ga: removed.

- **singularity.transport-schwarzschild-fibre** (9 kept).
  - Proof:
    - (1) to (3) in Cl(2,4). The lift n0 + hb^{-1}(x) + Q_p(x) ninf/2 is null. iota is the reflection N -> e+ N e+ = -(2t n0 + X + (s/2) ninf), a versor: it preserves the quadric and is an involution.
    - (4) Read the one-forms as background gradients. hb^T(xi) = (sqrt(2M) - beta sqrt r) e_t - sqrt r e_r = -sqrt r e_r, so Q* = -r. The static labels give the same value.
    - The cometric components are kept as a labelled reading.
  - Check: hb^T taken from the shared engine's PG and static gauge fields; 3 masses x 4 radii inside, on and outside the horizon; Q*(grad t_s) = 1/f.
  - outside_ga: narrowed. Only the definition of xi by the imported weighted coframe of T4 Thm 8.7 remains, a construction at E outside the invertible region.

- **synthesis.taub-nut-cauchy-horizon-is-taub-point-with-complex-residue** (2 -> 3).
  - Proof of (i): coframe f^0 = N grad T, f^l = a_l sigma_l, with grad ^ sigma_k = -sigma_i ^ sigma_j. The torsion equation has left side H_k e^0 ^ e^k - mu_k e^i ^ e^j. It is solved by the displayed Omega, and the field equations come from the field strength's Ricci map.
  - Checks:
    - The shared engine builds the Bianchi IX gauge field on second-order jets in Euler labels. It finds rank 24, the solved Omega equal to the display, N^2 Ric^o(e_l, e_l) = alpha_l'' + (G^-1 dV)_l, N^2 Ric^o(e_0, e_0) = -sum alpha'' + 2C, and off-diagonal values zero.
    - The Taub region is a Ricci-flat gauge field at five rational (m, l, t), and not Ricci-flat when alpha_3'' is shifted.
  - The Christoffel route is kept as a labelled reading.
  - outside_ga: removed.
  - coverage.yaml: none existed, and none was added. Adding one would put W124 on the four old functions.

- **synthesis.einstein-condition-is-infinity-vacuum-incidence** (4 kept).
  - Proof, all clauses in GTG:
    - Tractors as Cl(2,4) vectors with the flat product as the tractor form. Omega_T(hb(v)) = Omega(hb(v)) - ninf ^ v + n0 ^ P(v), so D_v ninf = -P(v) and D_v n0 = v.
    - P, Ric and T are symmetric linear maps. The one-vacuum argument: P vanishes on A + conj(A), which is the complexified l-perp, so P(a) = c (a.l) l.
    - Contracted Bianchi as dot-calR(dot-D) = D calR/2.
    - Complexification with the central unit I_7 of Cl(3,4) (U3).
    - Index components are kept as a labelled reading.
  - Checks:
    - Omega_T on five gauge fields (de Sitter, SdS, Schwarzschild, FLRW, Kasner), with P from each field strength.
    - Own-ray classes zero on the Einstein fields, nonzero on FLRW, and equal to (1/2) l . T~(l).
    - W = span(I_g, l, s1 + I_7 s2) is totally isotropic in Cl(3,4), with the classes on it.
  - outside_ga: narrowed to the formal level's unnamed unit of T_x (x) C and T_xM (x) C. The formal text is not mine to change; see For Leon.

- **synthesis.series-wald-entropy-changes-without-flux-on-local-horizons** (3 kept).
  - Proof:
    - Store signature. K = <calR(B) B^{-1}>, K - Lambda/3 and the vanishing contractions are the same numbers in the statement's (-,+,+,+).
    - SdS in the PG chart: calR(B) = (M/2r^3)(B + 3 sigma B sigma) + (Lambda/3) B and calR(k ^ A) = (Lambda/3 - M/r^3) k ^ A, so R(k,A,k,B) = R(k,A,B,C) = 0.
    - k_+ = (e_0 + e_1)/(1 - beta). The transverse frame is D-parallel along both radial null directions.
  - Item G6 applied: proof (i) is now evaluated on a cross-section {t = t_0, r = r_b} of the horizon locus in the PG chart, with (xi.D)xi = kappa_b xi there. It is recorded in a separate `maintainer_pass_decisions` note.
  - Checks: three points of the static region; three rational horizons (beta = 1, xi null, kappa_b = f'/2, 4 r_b^2 s = r_b^2 - 3/Lambda); de Sitter planes.
  - outside_ga: narrowed to the component Gauss and Sachs equations, which are used as the standard Gauss equation and the imported Raychaudhuri Fact state them.

- **synthesis.promoted-norm-weyl-clock-flat-weight** (7 kept).
  - Proof:
    - Q(X, Y) = 2 <X(a ^ b) I^{-1} Y(I d_b ^ d_a)>. D is the unit sphere's operator, which is -id in the store sign on Cl(4,0), and s(X) = Q(X, D)/2. Identity (1) follows by bilinearity.
    - On Einstein fields F = W, and Q(W) = |W|^2 by W(IB) = I W(B).
    - The instantons are gauge fields on flat Cl(4,0): stereographic S^4 and S^2 x S^2, and CP^2 in a cohomogeneity-one gauge with the SU(2) fields. Vol = 32 pi^2 chi/E.
  - Checks (all three instantons solved from the torsion equation):
    - Einstein with Lambda = 3, 1, 6; Q(F) = |W|^2 = 0, 16/3, 96; E = 24, 8, 192.
    - I_MM/pi N^2 = 0, 4/3, 3/4 and I_EH/pi N^2 = -1, -2/3, -3/4. These reproduce the stored values, and the volumes they imply (8/3, 16, 1/2 times pi^2) are the cited ones.
    - The Kasner |W|^2 = 64/(27 tau^4) and the FLRW display, from gauge fields.
  - outside_ga: narrowed to the formal level's form notation from the imported Fact.

- **synthesis.promoted-norm-one-global-pair** (5 kept).
  - Proof:
    - (i) in Cl(2,4), with bivector images B . I, B . V.
    - (ii) T is a trivector field and dT = grad ^ T. The T-variation gives -c int <(grad lambda ^ dT) I^{-1}>, so grad lambda = 0.
    - (iii) is global (compact slice, de Rham H^0 x H^3) and stays in forms, read on the assembled manifold. (iv) and (v) are unchanged.
  - Checks: I and V from the shared engine at Lambda = 3, 12, 3/4, -6 give ranks 3, 9, 10. The map dT -> <(g ^ dT) I^{-1}> has rank 1 for g = timelike, spacelike and null, and 0 for g = 0.
  - outside_ga: narrowed to clause (iii).
  - Not achievable in GTG: clause (iii). It is topology of a compact slice, beyond one flat chart, so a GTG proof is not possible in principle. That is a property of the clause, not missing mathematics.

- **synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part** (3 kept).
  - Proof:
    - E(a) = 2 d_b ^ F(I(a ^ b)), using the GA identities d_b ^ calR(I(a ^ b)) = calG(a) I and d_b ^ (I(a ^ b)) = -3 a I. Hence E(a) = 2(calG(a) + Lambda a) I.
    - Rank 10 because E factors through the Einstein map. The dilation trace is d_a ^ E(a) = 2(4 Lambda - calR) I.
  - Checks:
    - The identity operator and the ten Kulkarni-Nomizu operators.
    - The Weyl part: duality and d_b ^ W(I(a ^ b)) = 0 on three gauge fields' Weyl operators.
    - The component three-form of the Fact equals the trivector on the three sample curvatures.
    - The de Sitter gauge field; rank 10; the dilation trace on FLRW and Schwarzschild.
  - outside_ga: removed. The formal level was already GA-primary, with the components as labelled readings.

- **dark-energy.frozen-point-makes-stelle-west-vector** (6 kept).
  - Proof:
    - D_a I = 0, because the two (Lambda/6) A terms cancel.
    - F_T . I = 0, so F_T lies in Lambda^2 I-perp.
    - V = n0/2 - (3/Lambda) ninf, with I ^ V = e+ ^ e- on both branches, and D_a V = hb^{-1}(a).
    - Omega_T = Omega - hb^{-1}(a) ^ V/l^2 exactly. (A ^ V) x (B ^ V) = l^2 A ^ B gives the Lorentz block.
    - eps(I, V, X, Y) = <(X ^ Y) I_4^{-1}>, which is the Stelle-West contraction.
    - The Gauss-Bonnet variation goes through dot-D ^ dot-R = 0.
  - New checks:
    - Kottler fields in the PG chart with Lambda = 3/4, 3 and -3/4 from the shared engine: P = (Lambda/6) id, D I = 0, D V = hb^{-1}(a), the reduced form, Q(I) Q(V) = -1.
    - The tractor field strength with derivatives equals -W, commutes with I and V, and is pinned to -(2M/r^3) e2 ^ e3 on the transverse plane.
    - This covers the anti-de Sitter branch and a field with Weyl curvature, which coverage.yaml listed as untested.
  - outside_ga: narrowed to the four-form display of consequence (2), which is the imported Fact's expansion.

- **synthesis.euler-entropy-of-a-horizon-patch-is-an-edge-term** (3 kept).
  - Proof of (i) and (ii):
    - The cut is a 2D gauge field, with Omega_S = -omega_S J (Cartan sign).
    - The field strength has no commutator term, so calR_S(J) = K J is d omega_S = K e^2 ^ e^3. The holonomy rotor is exp((1/2) J oint omega_S).
    - A frame rotation is the gauge transformation with R = exp(-J theta/2), giving omega_S -> omega_S - d theta.
    - k_g = -((T.D)T) . N, and eps_abcd lambda^ab Y^cd = 4 <lambda I^{-1} Y> = 4 Y^23.
  - Checks: five profiles x three points (solved Omega_S, K = -rho''/rho, k_g, the gauge law for three rotations) and the binormal contraction.
  - Stays in forms:
    - The (i) reading: the Chern-Simons variation and the Gauss-equation identity with the extrinsic forms.
    - Gauss-Bonnet with corners (imported). (iii) and (iv) are unchanged.
  - outside_ga: narrowed accordingly.

## Not achieved, with the reason

- Nothing that could be done in GTG was left undone.
- Parts that stay in forms or components are kept under a narrowed declaration:
  - promoted-norm-one-global-pair (iii): de Rham cohomology of a compact slice, beyond one flat chart.
  - euler-entropy (i) reading: Cartan-form identities for the Chern-Simons variation and the Gauss equation. A GA proof would mean re-deriving the Chern-Simons variation of dark-energy.wall-counterterm in GA and checking the signs again. That is beyond notation, so it was left as the verified form identity.
  - series-wald: the Gauss and Sachs equations in components, as imported.

## For Leon

- The formal statement of synthesis.einstein-condition-is-infinity-vacuum-incidence still writes T_x (x) C and T_xM (x) C with no unit named. By U3 the unit is I_7 of Cl(3,4), now used in its proof and check. Naming it in the formal is a restatement, and none was decided.
- In the store sign on the Euclidean background Cl(4,0), the unit sphere's operator is D(B) = -B (Ricci -3a). The weyl-clock proof states this explicitly. The sign convention for Euclidean GTG is not written in docs/gtg-dictionary.md; it may deserve a line there.
- Memory: nothing new worth saving.
