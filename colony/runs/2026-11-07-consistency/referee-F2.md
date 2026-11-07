# Referee F2: blind review of eleven GTG proofs (run 2026-11-07-consistency)

Brief: REFEREE_GTG.md. List: referee_F2.txt.

**Departure from the brief: I read the maintainer_pass_gtg_proof notes before my verdicts.** I did not read any gtg-*.md file. But entity 1's note came up in full when I printed its entity.md. For entities 2, 3, 5 to 11 I grepped the note (and the earlier ga_rewrite note) to see which outside_ga decisions had been taken. I then rebuilt every verdict from my own computations. Where a note's claim and my computation differ (entity 9's instanton check, entity 10's cross-section), my computation decides. Still, treat the review as not fully blind on those notes.

I did not edit store/, commit, spawn agents or run `tp check`. I ran every check.py function of the eleven entities directly, with bytecode writing off: all pass.

Scratch directory (all scripts are mine; they use GA.py blade products and sympy, not the check functions, and only `gtg` where marked):
`/tmp/claude-0/-home-claude/23cbb9be-73ca-5537-8211-47496476158a/scratchpad/F2/`

- `mygtg.py`: my own small symbolic GTG engine. It does its own torsion solve D_mu g_nu - D_nu g_mu = 0, its own field strength R(a ^ b) = a.grad Omega(b) - b.grad Omega(a) + Omega(a) x Omega(b), its own calR(B) = -R(hb(B)) and its own contractions.
- `sphere_own.py`, `sphere.py` (the second cross-checks with the gtg engine): the unit-sphere question.
- `e1_e7_cl24.py`: Cl(2,4) identities (entities 1, 7). `frame_eq_signs.py`, `e9_instantons.py`: frame trivector in both signatures (entities 7, 9).
- `e2_e3_e10.py`, `e10_fix.py`, `e10_kappa.py`: PG, static and SdS fields, solved symbolically.
- `e4_e5_e6_e8.py`: entities 4, 5, 6, 8. `e11_bianchi.py`, `e11_ricci.py`, `e11_taub.py`: entity 11, symbolic.
- `runchecks.py`: runs the store checks. `mutsign.py`: flips gtg.STORE_SIGN. `mutrun.py`: textual mutants in scratch copies.

## The unit sphere on Cl(4,0) in the store's sign

I computed this exactly from the definition with my own engine. The stereographic gauge is hb^{-1}(e_i) = 2/(1 + Q(x)) e_i, with Omega solved from torsion, at a symbolic point. The result:

**calR(B) = -B for every bivector, calR(a) = -3a, scalar calR = -12** (`sphere_own.py`; the gtg engine agrees at two rational points).

For S^2, the sign depends on the signature of the plane: on Cl(2,0), calR(J) = -J; on Cl(0,2), calR(J) = +J. So the store-sign eigenvalue of a round plane is -K when its vectors square to +1, and +K when they square to -1. The second case covers spacelike planes of Cl(1,3) and the cut of entity 6. Consequences on Cl(4,0):

- an Einstein field with Ric^o = Lambda g has calR(a) = -Lambda a;
- the store-sign field equation there is G(a) - Lambda a = 0, not G(a) + Lambda a = 0. On S^2 x S^2 I find G(e0) = +Lambda e0.

Consistency in my list:

- **Entity 6 (Cl(0,2), calR_S(J) = K J): consistent.**
- **Entity 10 (spacelike planes of Cl(1,3), K = <calR(B) B^{-1}>): consistent.**
- **Entity 9: consistent in (i), (ii) and its check** (D(B) = -B, calR(a) = -Lambda a, s = -d_a . calR(a)). **It is inconsistent in two places:**
  - (iii) quotes the frame equation as 2(G(a) + Lambda a) I = 0 on Cl(4,0);
  - (iv) writes the Lorentzian de Sitter curvature as (Lambda/3) D.
- The other eight entities are Lorentzian only.

## 1. dark-energy.frozen-point-makes-stelle-west-vector: ACCEPT WITH FIXES

The GTG proof proves (i) to (iii) and both consequences. I recomputed the following with symbolic Lambda (`e1_e7_cl24.py`):

- D_a I = 0 (the two (Lambda/6)A terms cancel);
- B . I = -Q(I) u;
- V = n0/2 - (3/Lambda) ninf, with Q(V) = -3/Lambda and I ^ V = e+ ^ e-;
- D_a V = A, and Omega_T - Omega = -A ^ V/l^2 with l^2 = 3/Lambda;
- (A ^ V) x (B ^ V) = l^2 A ^ B;
- eps(I, V, X, Y) = <(X ^ Y) I4^{-1}>;
- the bilinear expansion.

The checks call the engine, and every mutant I tried was killed: the sign of V, the sign of the soldering term, F_T = +W, and a flipped store sign. Fixes:

1. Proof (ii): the translational term is **minus** (D_a B - D_b A) ^ V/l^2, not plus. I computed the cross terms; the term vanishes either way.
2. Proof (iii) and "In components": with X = (1/2) X^{ab} e_a ^ e_b, I find eps_abcd X^{ab} Y^{cd} = 4 <(X ^ Y) I4^{-1}> = 4 eps(I, V, X, Y). The proof calls eps(I, V, X, Y) "the Stelle-West contraction eps_abcd X^ab Y^cd", and the reading writes eps_abcd F^ab F^cd = eps(I, V, F, F)/(|I| l). Both miss the factor 4. Entity 6 has the 4. The statement's "~" absorbs it; the proof text should not.
3. outside_ga is not exact. Formal (ii) also uses the form display "D + e ^ V/Q(V)" and "Lorentz curvature block R + l^{-2} e ^ e", and the technical level repeats the four-form expansion. Two options: restate (ii)'s block as -(calR(B) - l^{-2}B) (already in the proof) and name the technical level, or extend the declaration to those displays. The reason given (the imported Fact's own expansion) is acceptable for consequence (2).
4. Add synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection to `uses`. Its Omega_T is load-bearing in (i) and (ii). Repin dark-energy.stelle-west-vector-frozen-point@5 to v6; v6 states what the proof uses.

## 2. pairing.regular-frame-class-vanishes-horizon-changes: ACCEPT WITH FIXES

All of the following match the statement exactly (`e2_e3_e10.py`, symbolic in r, theta):

- my own torsion solve gives the four bivectors;
- beta' = -beta^3/4M;
- the outgoing classes -(1 - beta)/r and -I5(1 - beta)/r;
- the ingoing classes (1 + beta)/r and I5(1 + beta)/r;
- (l.D)l = (beta^3/4M) l;
- the expansion 2(1 - beta)/r;
- calR = 2M/r^3 on e0^e1 and e2^e3, and -M/r^3 on the four mixed planes;
- the loop class 2M/r^3.

The static covariance algebra and the values 144/125, 2, 12, -16/125 = (1/3)(-48/125) check. The checks kill mutants. Fix:

1. Language: the formal level still defines the field only by its coframe and connection one-forms. The declaration was removed, but the forms still do the work the bivectors Omega(e_c) do. State the four bivectors of the proof in the formal level, with the forms as a labelled reading. Also add std-algebra.complexification-is-the-odd-extension to `uses` (the I5 classes rest on it), and repin the three stale premises.

## 3. pairing.static-frame-only-expansion-survives: ACCEPT

My symbolic solve gives:

- the stated Omega(e_c);
- the classes 0, 0, -sqrt f/r and -I5 sqrt f/r;
- pv(Omega(m)) = 0 and pv(Omega(mb)) = -2 sqrt f/r;
- (l.D)l = (f'/2 sqrt f) l.

The horizon value -48/125 is right, and the checks kill mutants (the acceleration sign). Optional: say "as F -> 0" (the static gauge is not defined on the horizon locus), add std-algebra.complexification-is-the-odd-extension to `uses`, and repin.

## 4. singularity.transport-schwarzschild-fibre: ACCEPT WITH FIXES (declaration)

The following are exact, symbolically (`e4_e5_e6_e8.py`):

- n0 . ninf = -1 and N^2 = Q(X) - 2st;
- e+ N e+ = -(2t n0 + X + (s/2) ninf);
- hb^T(a) = a - beta(a.e_r)e_t, adjoint verified;
- hb^T(xi) = -sqrt(r) e_r and Q* = -r, in both PG and static labels.

The check kills the mutant hb^T(xi) = +sqrt(r) e_r. Fix:

1. outside_ga is not exact. On the invertible region, xi is the background gradient sqrt(r) grad r + sqrt(2M) grad t_PG, and the proof uses it that way. Only the name "the generator of the radical line of the weighted PG coframe of T4 Thm 8.7" is the source's language. Write xi with grad in formal (4), keep the T4 description as provenance, and either drop the declaration or reword its why to say exactly that.

## 5. synthesis.einstein-condition-is-infinity-vacuum-incidence: ACCEPT WITH FIXES

Every clause is proved. I recomputed:

- D_v ninf = -P(v) and D_v n0 = v;
- the null-cone lemma, solved symbolically: S = S00 eta;
- the one-vacuum kernel P_ab = c l_a l_b;
- the sign conversion calR + 8 pi G T = (Lambda + 4 pi G tau) id from Ric^o = 8 pi G(T - tau g/2) - Lambda g, with Ric^o = -u.calR(v).

The checks kill mutants (D_v ninf = +P(v), calR = -4 Lambda). Fixes:

1. outside_ga, narrowed to the unit, is incomplete. Formal (4), (6) and (7) still compute in index notation: Ric = (R/4) g, Sch = c l^flat (x) l^flat, g^{ab}T_ab, nabla^a T_ab. The proof does all of it in GA: Sch(a) = c(a.l)l, tau = d_a . T(a), dot-T(dot-D) = 0. Either restate those clauses, or add them to the declaration.
2. The why ("kept until a decided restatement") is a deferral, not a U6 reason: the proof shows that span{V + I7 V'} resolves the unit exactly. Also say explicitly that T_xM (x) C here is the mu slot of the tractor space, so its unit is I7, not U3's spacetime I5.
3. Add synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection and std-algebra.complexification-is-the-odd-extension to `uses`, and repin interior.imported-tractor-connection.

## 6. synthesis.euler-entropy-of-a-horizon-patch-is-an-edge-term: ACCEPT WITH FIXES

With a general profile rho(s) on Cl(0,2) (`e4_e5_e6_e8.py`):

- Omega(e_s) = 0 and Omega(e_phi) = rho' J;
- calR_S(J) = -(rho''/rho) J, which is K J and has the right Euclidean sign (see the sphere section);
- (e3.D)e3 = -(rho'/rho) e2, so k_g = -rho'/rho for N = +e2;
- the rotor R = e^{-J theta/2} gives Omega'(e_s) - Omega(e_s) = theta' J and R~ e2 R = cos e2 + sin e3;
- eps_abcd X^ab Y^cd = 4 <X I^{-1} Y> on random bivectors.

The Gauss-equation substitution checks by hand, and so do the disk and threshold values. The check kills the mutant K = +rho''/rho. Fixes:

1. Formal (i) calls omega_S "the rotation-gauge field of the cut". By C10 the rotation-gauge field is Omega_S = -omega_S J, and omega_S is its Cartan form. The proof says so; the statement should too.
2. The outside_ga why says the transgression and the gauge law are "computed in GTG". That is true of the proof, but formal (i) states them in forms (de^2 = -omega ^ e^3, d omega = K e^2 ^ e^3, omega -> omega - d theta). Either add Omega_S = -omega_S J and calR_S(J) = K J to the formal level, or name these displays in the declaration.
3. Add synthesis.imported-chern-weil-and-chern-simons-forms and synthesis.c-loc-local-horizon-premise to `uses` (cited), and repin the eight stale pins.

Not part of this rewrite: the old remark's "soldering part -(Lambda/3) e ^ e" has the opposite sign to the Fact's F = R + l^{-2} e ^ e. It is argued, not used.

## 7. synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part: ACCEPT WITH FIXES

I verified the two GA identities in both signatures with my own code (`frame_eq_signs.py`):

- d_b ^ (I(a ^ b)) = -3 a I;
- d_b ^ calR(I(a ^ b)) = G(a) I, on a random Kulkarni-Nomizu operator.

So E(a) = 2(G(a) + Lambda a) I on Cl(1,3). The rank and trace arguments and the algebra of (iv) all check. The checks kill the mutant -3 -> +3. Fixes:

1. The statement sets l^2 = 3/|Lambda| but displays A(a) = Omega(a) - hb^{-1}(a) ^ V/l^2. On the anti-de Sitter branch that gives D_a V = -hb^{-1}(a); I computed both branches. The proof (iv) cites entity 1 (ii), whose l^2 is 3/Lambda. Write V/l^2 as (Lambda/3) V (= -V/Q(V)), or let l^2 = 3/Lambda as in the Fact.
2. Optional: the declaration was removed, but the formal setup still defines Ric_bd = g^{ac} R_abcd, J = g^{ab} Sch_ab and F_abcd in indices. F(B) = calR(B) - (Lambda/3) B is available.

## 8. synthesis.promoted-norm-one-global-pair: ACCEPT WITH FIXES (declaration)

At Lambda = 3, 3/4 and -6, I find:

- constraint rank 3 and gauge image rank 9;
- both lie in the kernel, and so does the norm mode;
- gauge plus norm mode has rank 10;
- d/ds (sI, V/s, s^2 Lambda) at s = 1 is 2 Lambda n.

The T-variation is right. The check kills the mutant on the sign of the norm mode. Fix:

1. outside_ga names clause (iii) only. Clause (iv) also uses a global form fact: the lambda-equation c dT = -dL/d lambda is solvable because H^4(M) = 0 for the noncompact M = R x Sigma. Add it.

## 9. synthesis.promoted-norm-weyl-clock-flat-weight: ACCEPT WITH FIXES (substantive sign)

The following check (`e9_instantons.py`, own engine, S^2 x S^2 on Cl(4,0)):

- (1) and (i);
- the Einstein identity F = W with Q(W) = |W|^2;
- E = |W|^2 + 8 Lambda^2/3, with Q(D) = 24, Q(F) = |W|^2 = 16/3 and E = 8;
- the instanton values and volumes;
- (iii) dL/du;
- (v), including 24hq and the Friedmann algebra, by hand.

Fixes:

1. Proof (iii) quotes "the trivector-valued 2(G(a) + Lambda a) I = 0" as the frame equation and traces it to s(F) = 0. On Cl(4,0) with F = calR - l^{-2} D, D = -id, the frame trivector is **2(G(a) - Lambda a) I**. On S^2 x S^2 the quoted form gives 4 Lambda e0 I, not 0, and its trace gives s(F) = -8 Lambda. Replace it with the Euclidean form; its trace gives s = 4 Lambda and s(F) = 0, as the proof needs.
2. Proof (iv) is on Cl(1,3) and says "the whole curvature is (Lambda/3) D". With D(B) = -B that is the anti-de Sitter sign. Write (Lambda/3) B, the de Sitter operator of C6.
3. check_gtg_instantons_as_euclidean_gauge_fields does not pin the sign the proof cites: it still passes with gtg.STORE_SIGN flipped. It reads lam = -Ricci and uses only lam^2, but never asserts lam = 3, 1, 6 or calR(a) = -3a on S^4. Add those assertions.
4. Add synthesis.imported-gtg-dictionary (Weyl duality, row 5) and synthesis.imported-miskovic-olea-identity to `uses` if they are kept as citations, and repin.

## 10. synthesis.series-wald-entropy-changes-without-flux-on-local-horizons: ACCEPT WITH FIXES

The following check (`e10_fix.py`, `e10_kappa.py`, SdS PG field solved symbolically):

- calR = (M/2r^3)(B + 3 sigma B sigma) + (Lambda/3) B, with Ricci map Lambda a;
- K = 2M/r^3 + Lambda/3 on e2 ^ e3, unchanged on the tilted planes for all a, b;
- calR(k ^ A) = (Lambda/3 - M/r^3) k ^ A, so (k ^ B).calR(k ^ A) = 0;
- (xi.D)xi = (f'/2) xi on the horizon locus;
- the closed-form value A/4 - 3 pi/Lambda.

The checks kill mutants (the K sign, the kappa sign). Fixes:

1. Proof (i) says that on the cross-section {t = t0, r = r_b} "both null second fundamental forms vanish (Killing horizon)". This is false off the bifurcation surface: I find the expansion along n = e0 - e1 is -4/r_b there. Only chi along the generator xi vanishes, and that is all the step needs. Correct the sentence; it was introduced with item G6.
2. "K = <calR(B)B^{-1}> ... positive on round spheres in either convention" is loose. The sectional curvature flips sign with g -> -g. Say "the curvature of the plane with its positive-definite induced metric (minus the flat product)". The formula holds because spacelike planes of Cl(1,3) square to -1.
3. outside_ga names only the component Gauss and Sachs equations. The formal level also states F_abcd, R(k, A, k, B) and k_pm in components in signature (-,+,+,+), all of which have GA forms in the proof. Extend the declaration or restate. Also add synthesis.imported-gtg-dictionary (C11) and synthesis.c-loc-local-horizon-premise to `uses`, and repin.

## 11. synthesis.taub-nut-cauchy-horizon-is-taub-point-with-complex-residue: ACCEPT

The following check symbolically (`e11_*.py`, with a_l(T) as arbitrary functions):

- d sigma_k = -sigma_i ^ sigma_j;
- my own torsion solve gives Omega(e0) = 0 and the stated Omega(e_k);
- my own field strength gives N^2 Ric^o(e_l, e_l) = alpha_l'' + (G^{-1}dV)_l and N^2 Ric^o(e0, e0) = -sum alpha'' + 2C, with the off-diagonal values zero, and sum G^{-1}dV = -2V;
- Taub-NUT solves the equations;
- the rotation ratio tends to -t+/l, so kappa = t+/l = cot(phi/2);
- the limit is -(1 - kappa I)B3.

The checks kill mutants (the mu_k sign, the 2C sign). Removing outside_ga is justified. Repin the dictionary.

## Verdict counts

ACCEPT 2 (entities 3, 11); ACCEPT WITH FIXES 9 (1, 2, 4, 5, 6, 7, 8, 9, 10); REJECT 0.

No GTG step is wrong in a way that breaks a stated result. The two substantive errors are both one-line repairs:

- entity 9 (iii): the Euclidean frame-equation sign;
- entity 10 (i): "both second fundamental forms vanish".

All new check_gtg_* functions test the engine's computation, not a restatement. Every textual mutant I tried was killed. The one weakness is entity 9's instanton check: it is blind to the store sign.
