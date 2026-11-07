# Referee F3: blind review of ten new GTG proofs (run 2026-11-07-consistency)

Brief: REFEREE_GTG.md. List: referee_F3.txt. I did not read gtg-*.md or any maintainer_pass_gtg_proof
extraction note before my verdicts were written. My scratch scripts are my own code, not the check
functions. They use a symbolic GA layer (sympy coefficients, GA.blade_mul for the blade signs only),
an independent torsion solver, an independent field strength and store-sign curvature, and independent
Ricci, Schouten and Weyl maps:

- `/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/F3/sg.py` (the shared helper layer)
- `.../F3/mut.py` (mutation runner: it runs a check function on the stored check.py and on a scratch copy
  with one textual mutation; store/ is untouched)
- one script per entity, named below. Every path in this report starts with
  `/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/F3/`.

Verdicts: ACCEPT 2, ACCEPT WITH FIXES 8, REJECT 0.

Language (all ten): no em or en dashes, no "curved spacetime", and no bare imaginary unit in any level
or proof. The only bare `i` is in two check.py docstrings (pairing entities, `m = e2 + i e3`). That is
optional to fix, since the unit principle covers levels and proofs.

---

## 1. pairing.curvature-which-loops-move-vacuum: ACCEPT

- Script: `e1_loops.py`. I solved Omega symbolically from the torsion equation of the static field. It
  matches the displayed Omega(e_t) = -(M/r^2) e01, Omega(e_theta) = sqrt f e12,
  Omega(e_phi) = sqrt f sin e13 + cos e23. All six field strengths R(e_mu ^ e_nu) match. The store-sign
  spectrum is +2M/r^3 on e01 and e23 and -M/r^3 on the four mixed planes.
- Classes, with pv(B) = <B . l, m>, m = e2 + I5 e3: 0, M/r^3, I5 M/r^3, -M/r^3, -I5 M/r^3, 0.
  R(l, e2) = (M/r^3) l e2 with class 0. R(n, e2) has class 2M/r^3. The complex loops give 0, 0, 0, 0,
  4M/r^3 for (n, mbar), and 0 for (l, n). All as stated.
- check_gtg_connection_and_field_strength solves Omega from the coframe alone and compares it with the
  closed forms. Mutations Omega(e_theta) -> -sqrt f e12 and the e23 field strength -2M -> -M both FAIL.
- The "In components" reading (-f''/2 = 2M/r^3, -f'/2r = -M/r^3) agrees.
- Note for the build, not for the fix round: the uses are pinned at @5 and @1, while the current versions
  of the Facts are 6 and 2.

## 2. pairing.loop-classes-are-weyl-components: ACCEPT WITH FIXES

- Script: `e2_weyl_loops.py`. I used a random pair-symmetric operator, took its Weyl part (trace-free and
  symmetric confirmed), and a null tetrad rotated by a rational Cayley Lorentz transform. Psi0, Psi1 and
  Psi2 are all nonzero there. All six table residues are 0. T_{u,v} = 0 for (l,l), (m,l), (m,m) and
  (n,mbar). (B . w) . z = <B (w ^ z)> holds. A non-Weyl control fails (class(n, m) != 0).
- Every step of the proof is valid. It uses only antisymmetry, pair symmetry and trace-freeness, and no
  Bianchi identity.
- Mutations of check_gtg_trace_and_pair_symmetry (sign of the reciprocal of m, and the class of (m, mbar))
  both FAIL.
- **Fix 2a (citation).** The proof attributes the symmetry <A W(B)> = <W(A) B> to dictionary Fact clauses
  (iv) and (v). Neither clause states it: (v) gives the Weyl formula, trace-freeness and I-linearity.
  Write "symmetric (the pair symmetry of the Riemann tensor that calR reads in clause (iv); in GA the
  consequence of the first Bianchi identity, dictionary section 5)", or import it.

## 3. synthesis.diagonal-kasner-momentum-constraint: ACCEPT WITH FIXES

- Scripts: `e3_kasner_momentum.py` and `e3_christoffel_sign.py`.
- With general functions A_k(tau, x), the torsion solve gives exactly
  Omega(e_tau) = 0, Omega(e_{x^i}) = -d_tau A_i B_i - sum_j (d_j A_i/A_j) e_i ^ e_j.
- e0 . calR(e_i) = sum_{k != i} A_k^{-1} d_tau(d_i A_k/A_i) holds, and the Ricci map is symmetric there.
- With A_k = e^{b_k} tau^{p_k(u(x))}, p on the circle through the rational parametrisation and b_k
  arbitrary functions, tau R_0i = d_i p_i + sum_j (p_i - p_j) d_i b_j holds identically. The log tau terms
  cancel.
- -A_i e0 . calR(e_i) equals the MTW-convention Christoffel R_0i identically, which confirms the sign of
  R_0i = -g_0 . calR(g_i).
- (i) holds, including the dual form t = -I3(u ^ p) and the finiteness of the collision set.
- Mutations of the check (the sign of tau R_0i, the boost term of Omega, p_i - p_j -> p_j - p_i) all FAIL.
- **Fix 3a (link).** The proof rests on synthesis.imported-gtg-dictionary for R_0i = -g_0 . calR(g_i)
  and for the Ricci map, but that Fact is not in main `uses`. Add it, at the pinned version the other
  entities use.
- **Fix 3b (citation).** "The Ricci map ... is symmetric": cite the source, which is clause (iv): it is
  the Ricci tensor R_mu nu = g_mu . calR(g_nu).

## 4. synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared (partial GTG): ACCEPT WITH FIXES

**The GTG part is correct.** Script: `e4_weyl_square.py`.
- On three random Weyl maps (the Weyl parts of Kulkarni-Nomizu operators of random symmetric maps), I
  computed eps_X(F1, F2) fully in Cl(2,4) (i6 = e012345, X = n0, divided by <X, Y>), for three different Y
  and with a random Cotton block. In every pair it equals (1/2)<W1(a ^ b) W2(d_b ^ d_a)> and
  (1/4) W1_abcd W2^abcd exactly. It does not depend on Y.
- (v), symbolic in K1 and K2 on Cl(4,0): 2<W W> = (4/3)(K1 + K2)^2, and the Euler density is 8 K1 K2.
- Mutations of check_gtg_weyl_square_of_weyl_maps: the factor 1/2 -> 1/4 FAILS, the reciprocal order
  biv(b, a) -> biv(a, b) FAILS, and (K1 + K2) -> (K1 - K2) FAILS. Flipping F -> -F passes, as it must,
  since the form is bilinear.

**The declaration does not say exactly what remains.**
- **Fix 4a (wording, (iii)).** The proof says "the ten-dimensional space of Weyl maps (trace-free,
  d_a . W(a ^ b) = 0, and I-linear)". These conditions, with symmetry, cut out eleven dimensions:
  B -> I4 B is symmetric, I-linear and Ricci-trace-free (computed: ricci = 0), but it violates the first
  Bianchi identity. Add d_a ^ W(a ^ b) = 0. The identity itself also holds on I4 (both sides -6), so
  only the description is wrong.
- **Fix 4b (GA available).** The frame-leg argument of (iv) is still in two-form and component language
  (e^a ^ e^b ^ W_ab, the cyclic identity, "Einstein-Hilbert-type contraction"). In GA, with F = -calR on
  the Lorentz block (the Cotton block drops out), K(DX ^ DX, F) = -<I4 calR(a ^ b)(d_b ^ d_a)>, which
  vanishes by the first Bianchi identity, and eps_X(DX ^ DX, F) = -<calR(a ^ b)(d_b ^ d_a)> = -calR,
  the scalar, which vanishes for W by trace-freeness. Script: `e4_frame_legs.py`, with three cases:
  - a Kulkarni-Nomizu map with a Ricci part: K = 0, eps = 1981/18, <R . .> = -1981/18;
  - the I4 map: K = 12, <I R . .> = -12;
  - a Weyl map: both 0.

  Either write it this way, or name it in the declaration.
- **Fix 4c (declaration text).** Narrow the declaration to what is left:
  - the statement's two-forms and four-forms;
  - the Chern-Simons form of (iv) and its frame-component exactness proof;
  - (v)'s global integrals;
  - (v)'s signature-transfer argument, in which the Euler-Lagrange derivative is a polynomial in metric
    jets. The declaration does not mention this argument now.

  The current text omits the last item, and it omits the (iv) frame-leg item if 4b is not done.
- **Fix 4d (for Leon: formal change).** Dictionary section 14 asks for the "Beyond one flat chart"
  sentence at the end of the formal level and in technical, and for the entry
  `'beyond one flat chart: the closed Riemannian S^2 x S^2 and the integrals over it'` under
  extraction.flags. Today the sentence is only in the proof.

## 5. synthesis.frozen-point-unique-where-weyl-has-no-kernel: ACCEPT WITH FIXES

- Script: `e5_tractor_sds.py`. I built static Schwarzschild-de Sitter symbolically in M, Lambda and r.
  - The Schouten map is (Lambda/6) id.
  - The tractor field strength F_T(e_mu ^ e_nu) = -W(g_mu ^ g_nu) has spacetime blades only, with no n0 or
    ninf block.
  - W is (M/2r^3)(X + 3 s X s).
  - The kernel map has rank 4.
- The type N map is trace-free and I-linear, with k in its kernel.
- (u ^ A) . (sig ninf + rho n0) = -((Lambda/6) sig - rho) A, Q(u) = -Lambda/3 and u . I = 0.
- Every step holds: u ^ (torsion), the -Q(u) A ^ B term, rank lower semicontinuity, and the ODE uniqueness.
- Mutations (dropping the minus sign in F_T = -W, and the sign of Lambda/6 in u) both FAIL.
- **Fix 5a (link).** The proof cites synthesis.imported-gtg-dictionary(v) for the Weyl decomposition, but
  it is not in `uses`. Add it. The maintainer left this for Leon; I concur that it is needed.
- **Fix 5b (minor).** The proof computes with the field whose derived metric is the Einstein scale g. Add
  one sentence: another field with derived metric in [g] has its tractor gauge field related to this one by
  a parabolic gauge rotor (closing sentence of synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection),
  and that rotor carries parallel tractors to parallel tractors. Optional, for Leon (statement): the
  "Consequently" clauses need c != 0.

## 6. synthesis.kasner-curvature-wall-is-negative-weight-helicity (partial GTG): ACCEPT WITH FIXES

**The GTG part is correct.**
- The slice field in Cl(0,3) has the right sign: round S^3 gives store-sign scalar +6 (`e6_slice_sign.py`).
- (iv): `e6_bianchi2.py` solves Omega symbolically for the Bianchi II field, for all z, not only z = 0.
  The identities R_TT = -(E1 + E2 + E3)/2 + C/2, N^2 R(e_l, e_l) = E_l/2 and zero off-diagonal frame Ricci
  hold identically in alpha_l(T). The closed form is:
  - Omega(e_T) = 0;
  - Omega(e_x) = -(alpha1'/(a2 a3)) e01 + (a1^2/(2 a2 a3)) e23;
  - Omega(e_y) = z (alpha1'/(a2 a3)) e01 - (alpha2'/(a1 a3)) e02 + (a1/(2 a3)) e13 - z (a1^2/(2 a2 a3)) e23;
  - Omega(e_z) = -(alpha3'/(a1 a2)) e03 - (a1/(2 a2)) e12.
- The Ellis-MacCallum formula: `e6_ellis_maccallum.py` is a symbolic polynomial identity in the general
  2-jet of a coframe; `e6_ellis_maccallum_fast.py` checks random exact 2-jets. See the result line below.
- Mutations of check_gtg_slice_and_bianchi_ii_field_strength (the sign of a1^4 in E1, and R3 -> -R3)
  both FAIL.

**Fixes.**
- **Fix 6a.** (iv) now rests on "finds, exactly at two generic jets". That is a sampled check of an
  identity in nine jet variables, backed by Landau-Lifshitz cited from memory. Display the closed form of
  Omega above, from which the Ricci map follows identically, or say that the identity is polynomial and
  holds identically.
- **Fix 6b.** In (i), "It is not used as a premise" is inaccurate: the scaling argument of (i) is read off
  the Ellis-MacCallum formula. Either import it as a Fact with provenance (Ellis and MacCallum 1969;
  Wainwright and Ellis 1997) or derive it. The declaration correctly says that no GA derivation is given.
- **Fix 6c (declaration).** Add what else remains outside GA. (iii) uses the extrinsic-curvature matrix K
  and the Hamiltonian constraint (tr K)^2 - tr K^2 + R^(3) = 2 Lambda, quoted without derivation or
  citation, "up to the sign convention". In GTG this is the e0 component of the Einstein map. Either
  derive it so, or name it in the declaration.

## 7. synthesis.kasner-field-is-weyl-flat-only-at-the-milne-and-isotropic-points: ACCEPT WITH FIXES

- Script: `e7_kasner_weyl.py`, with symbolic exponents p1, p2 and p3 = 1 - p1 - p2.
  - The torsion-solved Omega is -p_i t^{p_i - 1} B_i.
  - calR(e0) = (S - 1) t^-2 e0 and calR(e_j) = 0.
  - W(B_i) = lambda_i B_i and W(I4 B_i) = lambda_i I4 B_i, with 3 t^2 lambda_1 = E1 and
    3 t^2 lambda_2 = -E2.
  - The resultant is -9 p1^2 (p1 - 1)(3 p1 - 1), with solutions exactly (0,0), (0,1), (1/3,1/3), (1,0).
  - The isotropic bracket has Omega = 0.
- The C11 sign derivation of C_0i^0i in (-,+,+,+) is correct.
- Mutation (1/3 -> 1/6 in lambda) FAILS.
- **Fix 7a (link).** The proof cites synthesis.imported-gtg-dictionary(v) for the Weyl formula, but it is
  not in `uses`. Add it.

## 8. synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale: ACCEPT WITH FIXES

- Script: `e8_dilation_tractor.py`, with general phi(x).
  - The torsion solve gives Omega(e_mu) = e_mu ^ w.
  - The store-sign scalar is 6 box phi/phi^3, and the de Sitter scale gives box phi = (2/3) Lambda phi^3.
  - D_a D sigma = H0(a) - (1/4)(a . grad box sigma) n0 holds in Cl(2,4) for general sigma.
  - The double divergence of H0 is (3/4) box^2 sigma.
- The KN form of R, the Ricci map and tr K = box phi/phi all hold.
- Mutations of the check (Q(w)/2 -> Q(w), and the sign of the n0 term) both FAIL.
- **Fix 8a (error, in formal (iii) and proof (iii)).** For sigma = (t + x_1)^2, H(a) = 2(a . n) n with
  n = grad(t + x_1) = e^0 + e^1 = e_0 - e_1, not l = e_0 + e_1. Computed: H(e_0) = 2(e_0 - e_1), while
  2(e_0 . l) l = 2(e_0 + e_1). The vector is still null, so H0 != 0 and H0 : H0 = 0 stand. Replace
  "l = e_0 + e_1" with "l = e_0 - e_1" (or with n) in the formal level and in the proof. The formal change
  goes to Leon or the fix round. (i) and (iv) are not GTG; I spot-checked the tube-point and tabulated
  scale formulas and found them correct.

## 9. synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state: ACCEPT

- Script: `e9_diag_field.py`, with general N(t) and A_i(t).
  - The torsion solve gives Omega(e_{x^i}) = -(dA_i/N) B_i.
  - The plane eigenvalues are d_t(dA_i/N)/(N A_i) and dA_i dA_j/(N^2 A_i A_j).
  - The scalars of the five (a, b) pairs match (b/2)(b + 2 - a) t^{a-2}, which is 3/2 t^-2 for (0, 1).
  - For A_i = t^p: calR(e0) = 3p(p - 1) t^-2, calR(e_j) = p(3p - 1) t^-2, and scalar 6p(2p - 1) t^-2.
  - P = w rho exactly at p = 2/(3(1 + w)).
  - At p = 1/2 the Ricci square is 3/4 t^-4.
- The sign argument for (-,+,+,+) is right.
- Mutation (b + 2 - a -> b + 2 + a) FAILS.
- The Dirac and scalar analysis is unchanged GA or scalar mathematics.

## 10. synthesis.tractor-transport-weak-null-crossing: ACCEPT WITH FIXES

- Script: `e10_tractor_transport.py`, symbolic in Cl(2,4).
  - -(Omega_T - Omega) . V gives sigma' = gamma' . mu, mu' = -rho gamma' + sigma p and rho' = -p . mu.
  - Omega(x') kills n0 and ninf.
  - (a) N_v N_w V = -sigma (v . w) n0.
  - (b) N_n E N_n = nu N_n.
  - (c) N_n N_R N_n = 0.
  - A preserves Q.
  - The gauge identity holds with f' = nu(S - f^2), symbolic in f and S.
- Mutations (the Riccati sign, and the sign of the soldering term in Omega_T) both FAIL.
- The analysis (Volterra, Wronskian) is unchanged.
- **Fix 10a (links).** The GTG proof's transport equation rests on
  synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection, which identifies Omega_T with the
  connection of the Fact, and on synthesis.imported-gtg-dictionary (ii), (iii) and (v). Main `uses` holds
  only interior.imported-tractor-connection@2. Add both.
