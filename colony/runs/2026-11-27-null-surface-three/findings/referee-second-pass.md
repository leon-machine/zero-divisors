# Second-pass referee: the three null-surface entries

I read RUN.md, the three first-round reports, the "Fix round" sections of the three attack files (only those sections), and the three entries' entity.md files in full. I read the proof-main.tex paragraphs that changed and the check functions that were added or reworked. I did not read the first referees' scripts or the authors' work folders. My scripts are in /home/claude/scratch/referee-second/ and import nothing from any check.py:

- common.py: my own truncated-epsilon ring, my own first-order Einstein operator written from the displayed formula, and gtg's own torsion solver (solve_omega), patched only to pick unit pivots.
- s1 to s5: one script per test, described below.

I ran `python -m tp.checkone` once per entry. Entry 1: all 12 checks passed. Entry 2: all 10 passed. Entry 3: all 7 passed. I ran no lint, no mutation test, no full-store check and no git command, and I edited nothing under store/.

For about a minute the entry folders were moved aside while the orchestrator compared the store against main. One grep failed in that window; I repeated it after the files were back, and every result below comes from the restored files.

## Entry 1: synthesis.second-order-stress-of-the-first-order-gravitational-field

### (A) Fixes from the first round

All nine required fixes are applied as specified:

- 1: formal (iv) takes the proving option, with the scaling argument and the displaced flat field. The technical level and the one-liner were changed to match, and the proof of (iv) carries the argument ("Not invariant").
- 2: the source is renamed chi; the sentence was replaced as specified; "where F != 0" is in place.
- 3(a), 3(b): applied.
- 4: applied.
- 5(a), 5(b) (with the optional parenthesis), 5(c): applied.
- 6(a), 6(b): applied.
- 7(a), 7(b): applied; X is named.
- 8(a), 8(b): applied in the Source paragraph and in the note.
- 9: `premise(R1_ID)` and `premise(WEYL_FLAT_ID)` are present in both functions.

One small slip in the note, next to fix 8. The note now says of Chandrasekaran2026 that "the question asked here is not posed in it". Only the paper's abstract was read for this entry, so this is a claim about an unread text, the converse of the overclaim that fix 8 removed. Required fix E1-2 below.

### (B) Additions

- **Formal (iv), "at every point some displacement changes it": sound.**
  - The algebra is right. X_{s xi} = s(-(xi.grad)H1 + xi_ H1) - s^2 xi_ xi_, so the change of t at a point is A s - B s^2 with B = G1[xi_ xi_]/8 pi G. Where B != 0 some s makes it nonzero.
  - The proof's step from one point to every point is valid. G1[xi_ xi_] is a constant-coefficient expression in the jets of xi, so translating xi carries the example to any point.
  - Displaced flat field: the law with H1 = 0 gives G2[-xi_] = -G1[xi_ xi_]. This also follows from the exact flatness of id - eps xi_ + eps^2 xi_ xi_.
  - Independent test (s2): my own cubic xi at two fresh points; Omega solved by gtg; my eps ring. G1 = 0, G2 = -G1[xi_ xi_] exactly, and G2 is nonzero in all 16 components at both points.
- **Reading, the Kerr-Schild instance: the mathematics is sound; one statement needs a fix (E1-1).**
  - Independent test (s1), with my own profile (quartic plus cubic), fresh points, the field built from hb, and Omega from gtg's solver:
    - For three finite values of eps (1/3, 1, 7/2) at two points, with and without a trace, the Einstein map of id + (eps/2) W (a.l) l equals eps (tr w)(a.l) l exactly, and the curvature is nonzero. So the map is exactly linear in eps, and the quadratic part vanishes in every parametrisation (H1 H1 = 0).
    - In the eps ring: G2 of the Kerr-Schild field is 0. G2 of the transverse trace-free field is nonzero and equals clause (vii)'s formula at r = 0.
    - H1KS = H1TT - xi_ + beta, as jets.
    - G2_KS - G2_TT = G1[X_xi[H1TT] + X_B[H1TT - xi_]] exactly. With X_xi alone the identity FAILS. So the rotation gauge change is needed, as the entry says.
    - xi has nonzero second transverse derivatives.
    - n.G2_TT(n) = <sigma,sigma> + (1/8) d_n^2 <h,h>, as clause (vi) gives.
  - I also checked the proof's displacement algebra by hand: xi_ + xi_^T = -F + (1/2)(y.F''(y)) l l, so -F/2 - sym(xi_) = (1/2) W l l.
  - The labelling is correct. The instance is marked proved and computed, and the last sentence (where the focusing is carried in the Kerr-Schild gauge) is marked argued. That sentence is consistent with the fact that the planes n.x = const are not even null there: Q(hb^T(n)) = W.
  - **Defect (fix E1-1).** The entry states the flux comparison for P_n, the integral over the whole plane N. For a plane wave the integrand does not depend on y, so P_n = (1/8 pi G) int_N <sigma,sigma> diverges in the transverse trace-free gauge; (v) itself defines P_c only "when it converges". So the statements "P_n is (1/8 pi G) int_N <sigma,sigma> in the first gauge and zero in the second" and "the fluxes do differ" are not correct as written. What the instance shows is that the integrals of n.t(n) along each generator (the flux per unit transverse area) are (1/8 pi G) int <sigma,sigma> d lambda and 0. That still supports the conclusion that the fall-off condition cannot be dropped.
- **New check `check_null_null_identity_holds_in_the_light_cone_gauge_off_solutions`: sound.** It runs on a polynomial gauge field that is not a solution (G1 nonzero in 16 components), for r = 0, 1, 1/2, with the three values distinct.
- **New check `check_plane_wave_in_the_kerr_schild_gauge_has_no_quadratic_part`: sound.** It tests what its label says. "Identically" is tested at the sample point (the jets are truncated to order 2 before the solve); the proof covers every point.
- **Reworked check of (v): it is a finite proof.**
  - Each side of each identity is linear in the symmetric map and homogeneous quadratic in the momentum, and linear in the direction a, which runs over the four frame vectors.
  - The ten unit symmetric maps are a basis. The values of a quadratic form at e_i and at e_i + e_j fix it. So the 100 pairs fix both identities for all maps and momenta.
  - The Einstein symbol used is built from the stored curvature symbol R_p[h](B) = -1/2 p ^ h(B.p), not from the displayed formula. The equality of constant-coefficient operators is equality of their symbols.
  - The proof says so correctly ("a second proof").

### Required fixes, entry 1

- **E1-1.** Replace the plane-wave flux statements with integrals along the generators, in four places:
  - entity.md, Reading, the Kerr-Schild instance. Replace "and the fluxes do differ. Under (F) for $F$, $P_{n}$ is $\tfrac{1}{8\pi G}\int_{N}\ip{\sigma}{\sigma}$ in the first gauge and zero in the second." with "and the integrals of $n \cdot t(n)$ along the generators do differ: under (F) for $F$ they are $\tfrac{1}{8\pi G}\int\ip{\sigma}{\sigma}\,d\lambda$ on each generator in the first gauge and zero in the second ($P_{n}$ itself diverges for a plane wave, whose integrand does not depend on $y$)."
  - entity.md, formal (v), last sentence. Replace "(the Reading gives an instance in which it fails and the fluxes differ)" with "(the Reading gives an instance, a plane wave, in which it fails and the integrals of $n \cdot t(n)$ along the generators differ)".
  - proof-main.tex, last sentence of "Reading, the instance". Replace "(vi) gives $P_{n} = \tfrac{1}{8\pi G}\int_{N}\ip{\sigma}{\sigma}$ with $\sigma = \tfrac12 F'$ for the first field, and $t = 0$ gives $P_{c} = 0$ for the second." with "(vi) gives, on each generator, $\int n \cdot t(n)\,d\lambda = \tfrac{1}{8\pi G}\int\ip{\sigma}{\sigma}\,d\lambda$ with $\sigma = \tfrac12 F'$ for the first field, and $t = 0$ gives zero for the second; $P_{n}$ over the whole plane diverges for a plane wave."
  - extraction note: "It shows that the fall-off condition of clause (v) cannot be dropped." becomes "It shows, for the integrals along the generators, that the fall-off condition of clause (v) cannot be dropped."
- **E1-2.** extraction note, credit sentence. Replace "and the question asked here is not posed in it" with "and the question asked here is one it prompted".

## Entry 2: synthesis.corner-area-variation-of-a-null-plane-pair-is-the-charge-of-the-relative-boost

### (A) Fixes from the first round

All thirteen required fixes are applied as specified, at every place required:

- 1: the preamble.
- 2: the label of (v) and the magnitude sentence of (iv).
- 3: the definition in "Fluxes and generators", "the part of the generator linear in h", and the two added sentences.
- 4: both one-liner replacements.
- 5: the Reading, with a wording consistent with fix 6.
- 6: the heading of (vi), the sentence added to (a), (c), the technical level, the lay level and the note.
- 7: the note and the Reading.
- 8: "pin no imported Fact" and the past-cone paragraph. The paragraph adds the dual-plane theorem as a third path, which is correct (see below).
- 9(a), 9(b), 9(c).
- 10: e^{-A/4G hbar}.
- 11: Abbott and Deser.
- 12: the lay level.
- 13: the technical level.

### (B) Additions

- **`check_bivectors_bilinear_in_the_field_and_the_flow_with_one_derivative_are_six` and its proof paragraph: sound. "Span" is proved, and the inequality from the prime is in the right direction.**
  - A rank modulo p is at most the rank over Q, since a minor nonzero mod p is nonzero. So nullity_Q <= nullity_p = 6: an upper bound on the dimension, which is the direction "span" needs.
  - The check then exhibits six invariants independent over Q (the three built with the product and their duals). So the dimension is exactly 6.
  - Three are reflection-even and three odd, so the even subspace is exactly the span of the three.
  - Placing the derivative on h or on xi gives the two triples of the six listed. The derivative-on-xi triple is three_bivectors(h, q, xi), the same space with the vector slots relabelled.
  - I checked the covariance rows: the action on the symmetric pair, with the indices sorted, is the correct derivation on the basis e_a (.) e_b, and the sign is right on the blade slot.
  - Independent test (s3), set up differently, in equivariance form G x T(s,u,v) = T(G x s, u, v) + T(s, G x u, v) + T(s, u, G x v), with an exact rational rank: 960 unknowns, rank 954, **nullity 6 over Q**. Adding reflection-evenness under v -> e_1 v e_1 gives **nullity 3**.
  - This agrees with the representation count: S^2 V (x) V (x) V contains (1,0) and (0,1) three times each.
- **`check_corner_term_for_a_vacuum_field_found_by_elimination_and_off_the_solutions`: sound.**
  - It is a genuine vacuum field: E[h] = 0, not in the gauge, with a nonzero curvature component, which rules out a displacement.
  - The off-shell remainder 2 int n.E[h](xi) is pinned. It tests (iv) on data not built from plane waves.
- **`check_modular_hamiltonian_of_a_source_about_a_cut_against_the_area_combination`: sound, and correctly labelled.**
  - With T = -E/(8 pi G) held times pi G, the comparison 2K = area/4 is 2 pi K_true = area/(4G).
  - It tests the first law about two cuts and the factor 2 pi/(8 pi G) only. The label and the proof say so.
- **Sentence added to (v), the first law about any cut, and its proof: sound.**
  - xi' = (x - lambda_0 n).B = xi_B - lambda_0 n has Delta_{xi'} = 0, and on N it equals (lambda - lambda_0) n.
  - The integration by parts in the proof is correct.
  - Independent test (s5): n.E[h](n) = (1/2) d_n^2 tau as a jet for two generic polynomial gauge fields (my own operator). The identity int_{lambda_0}^{L} (lambda - lambda_0) n.T(n) = (1/8 pi G)[(a_1 - (lambda - lambda_0) a_1')|_L - a_1|_{lambda_0}] holds exactly for three cuts on a quintic tau.
- **Restated hypothesis (S): sound.** It is stated in full, with K written out and "not a consequence of any stored result".
- **New title: fix required (E2-1).** "First-order corner charge of the boost on a null-plane pair: area variation over $8\pi G$". The part after the colon is the statement of the result, and RUN.md requires "a name for the result and not its statement".
- **Past-cone paragraph: spot-checked by walking `uses` over the store.**
  - corner entry -> null-plane first-order theorem -> two-free-directions result -> gravitational-pair-production-from-the-operator-source-at-first-order -> synthesis.imported-einstein-cartan-matter-coupling: present.
  - corner entry -> null-plane theorem -> two-free-directions -> dimmed-burst-time-rescaled-copy -> hawking.greybody-inheritance-under-interface-premise -> hawking.imported-exterior-exactly-general-relativity: present.
  - Lovelock: reached through the Weyl-flat result. interior.imported-equivalence-einstein-equations: reached through the dual-plane theorem.
  - synthesis.imported-wald-noether-charge-entropy: not reachable, as stated.
  - One remark, optional: hawking.imported-exterior-exactly-general-relativity has `status: proved`, although its title begins "Imported". Calling it an imported Fact is the store's own naming, so this is not a defect.

### Required fix, entry 2

- **E2-1.** entity.md, front matter: change the title to `'First-order corner charge of the relative boost of a null-plane pair'` (68 characters; the first referee proposed the same title). The id and folder are unchanged.

## Entry 3: synthesis.null-surface-data-at-any-field-strength-the-focusing-equation-integrated

### (A) Fixes from the first round

All thirteen required fixes are applied as specified:

- 1: the note, the Reading and the lay level.
- 2: (iv) and its proof. The proof now says plainly that how the stretch ends is not shown in general.
- 3: the technical level, the lay level and the one-liner.
- 4: the lay level, the technical level and the one-liner.
- 5 and 6: the lay level.
- 7: the proof of (vi)(c), E = E_b C.
- 8: (i) and (viii).
- 9: (iii), the technical level, the lay level, and also the note and the Reading.
- 10: formal (iii), the note and the one-liner.
- 11: `shape_rate`. G is computed from the gauge field with E(lambda_0) = ((3,-1),(2,1)), so rho^4 = 25 and G is not the identity. det G = rho^4, tr G^{-1}G' = 2 theta, and (1/4) tr((G^{-1}G' - theta)^2) = <sigma,sigma> are all pinned.
- 12: the label is changed, and a second sample point is added (12 waves: 8 curved, 4 flat).
- 13: formal (i).

### (B) Additions

- **The exact vacuum example in (vii) and case (3) of the check: sound.**
  - Trace-free: w = diag(6/q, -6/q).
  - Sign convention: E' = S E with S' = w - S^2 gives E'' = wE, so the second column obeys b'' = w_22 b = -(6/q) b. This is correct.
  - q b'' + 6 b = 0 as polynomials (s4). In fact b = (1 - lambda) q / 2.
  - b(0) = 1 and b'(0) = 0, so S(0) = 0 and the hypersurface is a null plane there. b(1) = 0 and b'(1) = -3/2, a simple zero.
  - q = 3 - (lambda - 1)^2 >= 2 on [0, 1], with roots 1 +- sqrt 3. So the field is smooth there and b > 0 on [0, 1).
  - Independent test (s4): I built my own field hb(a) = a + (1/2) W (a.l) l with this w, at lambda = 0, 1/2 and 1 at generic y, with Omega from gtg's solver. It is torsion-free and Ricci-flat, and (n ^ e_2).R(n ^ e_2) = -6/q: -3, -24/11 and -2.
  - The convexity argument for the other column is in the proof and is correct, though terse: while f > 0, f'' = (6/q) f > 0, so f' >= f'(0) = 0 and f >= 1, so f cannot reach zero on [0, 1]. Hence det E = f b first vanishes at lambda = 1.
  - The proof is needed: the Taylor series of f at 0 has radius sqrt 3 - 1 < 1, so the check's series (which pins its first five coefficients, 1, 0, 3/2, -1/2, 3/4) cannot reach lambda = 1. The check's comment says this rests on the proof.
- **Reworded (iv) and the proofs of (iv) and (vii): sound.**
  - (vii) now rests on (iv) only through "the stretch ends by lambda_1 + 2/|theta(lambda_1)|". Ending by det E = 0 is argued correctly from the linear equation E'' = wE with smooth coefficients on [lambda_0, lambda_2].
  - The hypothesis lambda_1 + 2/|theta| <= lambda_2 is stated.
- **New shape-shear test in the area-density check: sound.**
  - G' = -(B(X_i).X_j + X_i.B(X_j)) = 2GS, with GS = S^T G. So G^{-1}G' = 2S, and qbar^{-1} qbar' = G^{-1}G' - theta = 2 sigma.
  - The check also requires qrate[0][1] != qrate[1][0]: the basis is not orthonormal.
- **New test of form (beta) with rho as the variable: sound.**
  - lambda is reverted as a series in x = rho - 1, with p0 != 0 asserted through the slopes.
  - d(p^2)/d rho = -rho(<sigma,sigma> - K.R(K)) agrees with the formal form, because <sigma,sigma>_rho = <sigma,sigma>/p^2.
  - In vacuum both p = p0 e^{-Xi} and lambda - lambda_0 = (1/p0) int e^{Xi} d rho are tested in the rho variable. This is the test the first referee asked for.

No required fixes. Optional: the proof of (i) still writes the Gram matrix by entries (G_ij' = ...). These are matrix entries of a map of the screen, which fix 13 allows, but they could be worded as in the formal level.

## (C) Cross-consistency

- **Entry 1 against entry 3 on the plane wave: consistent.**
  - Entry 1's Kerr-Schild field H1(a) = (1/2) W (a.l) l, W = -y.w(y), and Omega(a) = eps (a.l) l ^ w(y) are entry 3's (vi)(a) at amplitude eps.
  - Entry 3's Ricci map (tr w)(a.l) l is its Einstein map too (scalar (tr w) Q(l) = 0), which is entry 1's eps (tr w)(a.l) l.
  - Entry 3's Reading and note say: exactly linear in the profile, the quadratic part vanishes identically, the hypersurfaces crossing the wave focus at second order, and the change to the transverse trace-free form is a displacement growing quadratically together with a rotation gauge change. All of this agrees with entry 1, and with my s1, where the rotation part was necessary.
  - Entry 3's curvature "h = 2w at p = l" agrees with entry 1's "F'' = 2w, h = F".
- **Entry 1 (vi) against entry 3: consistent.** Entry 3's second order is theta' = -<sigma,sigma> (from S(lambda_0) = 0), and its Reading's rho'' = -4 pi G (epsilon + K.T(K)) rho, with epsilon = <sigma,sigma>/8 pi G read only as the first-order identification and explicitly not as a local second-order term, match entry 1's null-null component <sigma,sigma> + theta^2/2 + ..., per generator.
- **Entry 2 (vi)(b) against entry 3 (i), (ii): consistent in sign and factors.**
  - a^2 = det G = rho^4, so a = rho^2, entry 3's "area density". Entry 2's note says "the square of its rho".
  - K = hb^T(n) = n in entry 2's gauge, so lambda is affine.
  - With a = rho^2: theta = a'/a = 2 rho'/rho, and a'' = 2 rho'^2 + 2 rho rho'' = a(theta^2/2 - <sigma,sigma> + n.R(n)), which is exactly entry 2 (vi)(b).
- **Entry 2's -theta^2/2 against entry 1's +theta^2/2: different quantities, and neither entry claims otherwise.**
  - Entry 2's H^(2) comes from the symplectic pairing omega(h, L_B h). Entry 1's n.t(n) comes from the Einstein map.
  - Entry 2's note says explicitly that clause (vi) does not use the second-order stress result.
  - I checked that the two second-order area statements agree, in the exponential parametrisation. There a = exp(tau/2 to second order) gives a_2 = tau_2/2 + tau_1^2/8, so a_2'' = tau_2''/2 + theta_1^2. Entry 1's tau_2''/2 = -<sigma,sigma> - theta^2/2 then gives a_2'' = theta^2/2 - <sigma,sigma>, which is entry 2's sign.
- **Field-equation sign: the same in all three.** Entry 1 uses G = -8 pi G T. Entry 2 uses E[h] + 8 pi G T = 0 and (F): n.R(n) = -8 pi G n.T(n). Entry 3 uses G(a) + Lambda a = -8 pi G T(a). All agree with lib/gtg.py C6.
- **Rule scan of all three entries: no breach introduced by the fix round.**
  - No em dashes, "honest", "load-bearing", "curved spacetime", Christoffel, or bare imaginary unit.
  - Run and agent names appear only in the front-matter session and credit fields.
  - Index notation appears only in labelled quotations (T_uu in entry 2; the paper's qbar^{AB} in entry 3) and as matrix entries of 2 by 2 maps of a plane.
  - No level claims more than its formal statement, apart from the flux wording of E1-1.

## Final verdicts

- **Entry 1, synthesis.second-order-stress-of-the-first-order-gravitational-field: FIX REQUIRED.** E1-1: the plane-wave P_n statements become integrals along the generators, in the Reading, the last sentence of formal (v), the proof's last sentence and the note. E1-2: one clause in the note. The mathematics of every addition is confirmed independently.
- **Entry 2, synthesis.corner-area-variation-of-a-null-plane-pair-is-the-charge-of-the-relative-boost: FIX REQUIRED.** E2-1: the title only. Every addition is sound, including the count of six (confirmed exactly over Q) and the first law about any cut.
- **Entry 3, synthesis.null-surface-data-at-any-field-strength-the-focusing-equation-integrated: ACCEPT.**
