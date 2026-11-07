# GTG proofs, prover P3 (run 2026-11-07-consistency)

Entities: gtg_3.txt (12). Every new check is exact (Fractions, lib/GA.py and lib/gtg.py), calls premise() for
the premises it uses, and was run with colony/runcheck.py and then colony/check4.py on a proposals/ copy (each
copy deleted afterwards): 0 errors, no W413 on any new function (two first drafts were weak and were tightened by
moving data out of the function bodies). Versions: every entity was already above its locked version in this run
and kept it, except synthesis.positive-structure-... (2 = lock), bumped to 3 because decision A3 changes its formal.
Each changed entity has a credit entry and an `extraction.maintainer_pass_gtg_proof` note. No status, link, pin,
assumes edge or formal statement changed except A3. Validation: `python3 -m tp check --store store --layers 1,2,3
--keep-going --author leon`: 0 errors, 0 warnings store-wide (my ids: only I213 subject notes).

| Entity | GTG proof | Check added | outside_ga | Items |
|---|---|---|---|---|
| obj.interior.weighted-blow-up-hubble-normalisation-admissible | no (definition) | none | kept, narrowed | none |
| pairing.curvature-which-loops-move-vacuum | yes | check_gtg_connection_and_field_strength | removed | none |
| pairing.loop-classes-are-weyl-components | yes | check_gtg_trace_and_pair_symmetry | removed | none |
| synthesis.boundary-mode-first-law-of-entanglement | no | none | kept, narrowed | none |
| synthesis.diagonal-kasner-momentum-constraint | yes | check_gtg_rotation_gauge_field_and_mixed_ricci | removed | none |
| synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared | partial | check_gtg_weyl_square_of_weyl_maps | kept, narrowed | none |
| synthesis.frozen-point-unique-where-weyl-has-no-kernel | yes | check_gtg_tractor_field_strength_is_minus_weyl | removed | none |
| synthesis.kasner-curvature-wall-is-negative-weight-helicity | partial | check_gtg_slice_and_bianchi_ii_field_strength | kept, narrowed | none |
| synthesis.kasner-field-is-weyl-flat-only-at-the-milne-and-isotropic-points | yes | check_gtg_kasner_field_strength_and_weyl_map | removed | none |
| synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale | yes ((ii), (iii)) | check_gtg_dilation_field_scalar_and_tractor_dirichlet | removed | A3 applied (2 -> 3) |
| synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state | yes (curvature content) | check_gtg_wall_field_strengths | removed | none |
| synthesis.tractor-transport-weak-null-crossing | yes | check_gtg_tractor_transport_in_cl24 | removed | none |

## Per entity

- **pairing.curvature-which-loops-move-vacuum** (v6). Static gauge field, Omega from the torsion equation
  (Omega(e_t) = -(M/r^2) e01, Omega(e_theta) = sqrt f e12, Omega(e_phi) = sqrt f sin e13 + cos e23), field strength on
  the six background planes, frame loops R(e_c, e_d) = -calR(e_c ^ e_d), classes and loops by bilinearity with
  m = e2 + I5 e3. Cartan route kept as a labelled reading.
- **pairing.loop-classes-are-weyl-components** (v5). C(u,v,w,z) = -W(u ^ v) . (w ^ z); pair symmetry from the symmetry
  of W; tracelessness as d_a . W(a ^ u) = 0 read in the null tetrad's reciprocal frame, which gives the source's trace
  formula exactly (no normalisation fudge for l . n = 2, m . mbar = -2). eta^{ab} form kept as reading;
  orig-proof-main.tex kept.
- **synthesis.diagonal-kasner-momentum-constraint** (v4). Synchronous gauge field A_i e_i; Omega(e_{x^i}) =
  -d_tau A_i B_i - sum_j (d_j A_i/A_j) e_i ^ e_j; boost row of the field strength; R_0i = -g_0 . calR(g_i) from the
  symmetric Ricci map gives the formula. Cross product in (i) written as -I3((1,1,1) ^ p). Check uses exponent jets
  exactly on the circle and two values of log tau. Christoffel route kept as reading.
- **synthesis.kasner-field-is-weyl-flat-...** (v2). Torsion-solved Omega = -p_i t^{p_i-1} B_i; calR(B_i) = p_i(p_i-1)/t^2,
  calR(e_i ^ e_j) = p_i p_j/t^2; Ricci, scalar, Weyl map with eigenvalue lambda_i on B_i and I4 B_i; the sign of the
  (-,+,+,+) mixed component derived from C11; (ii), (iv) read flatness off the field strength.
- **synthesis.frozen-point-unique-where-weyl-has-no-kernel** (v5). On the Einstein region Omega_T(a) = Omega(a) +
  u ^ hb^{-1}(a), u = (Lambda/6) n0 - ninf; F_T(hb(X)) = -calR(X) + (Lambda/3) X = -W(X), no Cotton or ninf block;
  kernel argument on Cl(2,4) vectors; check uses the library's tractor field strength of static Schwarzschild-de
  Sitter (Lambda = 3/7 and 0) and a type N Weyl map.
- **synthesis.positive-structure-...** (2 -> 3). (ii): dilation field hb^{-1}(a) = phi a, Omega(a) = a ^ grad ln phi,
  Kulkarni-Nomizu field strength, store-sign scalar 6 box phi/phi^3; (iii): D_a D sigma in Cl(2,4) with Omega_T(a) =
  -ninf ^ a. A3 applied to formal (ii) and proof (ii) (store sign, Euler-Lagrange equation box phi = (2/3) Lambda phi^3,
  action int(-6 eta(d phi, d phi) - 2 Lambda phi^4)); the Christoffel check now asserts the store-sign identity
  sqrt|g| calR = 6 phi box phi; evidence in a maintainer_pass_decisions note.
- **synthesis.radical-normal-tame-wall-...** (v3). Diagonal gauge fields N e0, A_i e_i: calR(B_i) = d_t(dA_i/N)/(N A_i),
  calR(e_i ^ e_j) = dA_i dA_j/(N^2 A_i A_j); (i) flat bracket, (iii) R = (b/2)(b+2-a) t^(a-2), (iv) Friedmann exponent
  from the Einstein map and the radiation Ricci square 3/4 t^-4. The Dirac and scalar analysis was already GA.
- **synthesis.tractor-transport-weak-null-crossing** (v5). Transport from Omega_T in a D-parallel frame: E =
  (ninf ^ gamma') ., N_v = -(n0 ^ v) .; facts (a)-(c) as Cl(2,4) identities; (4) from the Schouten map.
- **synthesis.kasner-curvature-wall-...** (v2), partial. The field and slices are stated as gauge fields (slice field
  in Cl(0,3), store-sign scalar = R^(3)); the frame formula of (i) is verified against the torsion-solved slice field
  strength; (iv)'s Bianchi II equations are read off the gauge field's Ricci map. Not achieved: a GA derivation of the
  Ellis-MacCallum formula (cited from memory) from the torsion equation; the statement is posed on structure
  functions of a coframe. Declaration narrowed to that.
- **synthesis.frozen-point-integrand-...** (v3), partial. Two-forms read as linear maps on bivectors; (iii)'s identity
  eps_X(F1, F2) = (1/2)<W1(a ^ b) W2(d_b ^ d_a)> verified on ten library Weyl maps and all 55 pairs; (v) pointwise from
  the Cl(4,0) product operator, with the Beyond-one-flat-chart sentence for the integrals. Not achieved without a
  formal change: the statement is written in two-forms, four-forms and a Chern-Simons form, and (v) is a global
  integral. Declaration narrowed.
- **synthesis.boundary-mode-first-law-of-entanglement** (v7), not achieved. Clause (iv) is stated in the components of
  its own (-,+,...,+) convention (formal, unchanged) and its geometric step is the classical small-ball volume and
  area expansion cited from memory; a GTG proof needs the second-order normal gauge of hb and angular integrals in
  every dimension, new derivations not verified exactly here. Declaration kept, reason narrowed.
- **obj.interior.weighted-blow-up-...** (v3), not applicable (definition). The old reason misdescribed the Einstein
  condition (the formal writes calR(a) = Lambda a); narrowed to the coframe display B_i (x) theta^i of the
  Hubble-normalised field.

## For Leon

1. Formal restatements I did not make (they would change formal text): the object's tau Omega = -sum p_i B_i (x) theta^i
   as tau omega(e_j) = -p_j B_j + E_tau(e_j) on unit tangential physical vectors; the frozen-point-integrand's two-form
   and four-form definitions as maps on bivectors with the I4 pairing.
2. Uses edges: the GTG proofs of synthesis.kasner-field-is-weyl-flat-... and synthesis.frozen-point-unique-... cite
   Fact synthesis.imported-gtg-dictionary (Weyl decomposition), which is not in their uses; adding it is a link change.
3. synthesis.frozen-point-integrand-... (v) integrates over closed S^2 x S^2: the proof now has the Beyond-one-flat-chart
   sentence, but the formal has no flag sentence and extraction.flags no entry.
4. Stale pins: pairing.curvature-which-loops-move-vacuum pins pairing.imported-schwarzschild-connection-curvature@5
   (now 6) and pairing.loop-classes-are-weyl-components@4 (now 5); not repinned. Dependants of
   synthesis.positive-structure-... (now 3) are stale.
5. Not achieved without new mathematics: the Ellis-MacCallum frame formula in GA (kasner-curvature-wall), the
   small-ball expansions in GTG (boundary-mode (iv)).
