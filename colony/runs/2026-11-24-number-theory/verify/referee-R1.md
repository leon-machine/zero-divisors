# Referee report R1, run 2026-11-24-number-theory (blind)

Scope: the five proposals A to E under `proposals/`. I read REFEREE.md, BRIEF.md (standards, role: referee), each
proposal's entity.md, proof-main.tex, check.py and coverage.yaml, the check4 logs, and every cited stored premise
at its pinned version (formal levels; for the two-mode theorem the whole entity). I did not read `findings/`,
`work/` or `RUN.md`. Scratch work is in `verify/scratch/` (my own scripts `A_indep.py`, `B_indep.py`, `B_mod4.py`,
`C_indep.py`, `D_indep.py`, `D_count.py`, `E_indep.py`, and perturbed copies of the checks in `A1..A3`, `B1..B3`,
`C1, C2`, `D1..D4`, `E1..E3`). Every check runs and passes as filed (B with `TP_LAB=/home/claude/lab-overlay`).

Summary of verdicts:

| | verdict | the main point |
|---|---|---|
| A | SOUND WITH FIXES | classical and correct; one wrong formula in the proof of (v); a premise cited in (v) is not in `uses` |
| B | SOUND WITH FIXES | the reduction from n to 4 is correct; the title, one-liner and lay level overclaim ("every number of modes"), and clause (iv) is false as worded at one mode (counterexample below) |
| C | SOUND WITH FIXES | correct for every n; a sign slip at M = 1 in (iv); a run name in the note; the prior-art source is described wrongly |
| D | SOUND WITH FIXES | the enclosure library is sound and the proof is complete; only the title needs a qualifier (five points, three up to the mirror) |
| E | SOUND WITH FIXES | the identities are correct; the hypothesis "|D| divides 4M" in (v) is wrong (should be 2M); (H3) needs "b in Z" |

---

## A. synthesis.positive-rationals-are-the-squares-of-the-even-subalgebra-of-cl-three

**Verdict: SOUND WITH FIXES.**

### Points of REFEREE.md

1. *The descent.* Correct, and nothing is missing for p = 2 or composite m.
   - Even m: if the sum of the four squares is even, the number of odd components is 0, 2 or 4, so they pair into two pairs of equal parity. The half sums and half differences are integers with N(y) = N(x)/2 = (m/2)p. Since m >= 2, m/2 >= 1 and is smaller than m. This contradicts minimality, so the least m is odd.
   - Odd m > 1: residues |y_i| < m/2 exist because m is odd. Then N(y) < m^2 and N(y) is congruent to N(x), which is 0 mod m.
   - The components of x y~ are integer polynomials in the x_i and y_i that are bilinear in (x, y~). Replacing y_i by x_i changes them by multiples of m. So they are congruent mod m to the components of x x~ = (mp, 0, 0, 0). Right.
   - m' = 0: then y = 0, so m divides every x_i, so m^2 divides mp, so m divides p with 1 < m < p. That is impossible. Right.
   - p = 2 is covered by 2 = N(1 + B_1). Composite targets follow from multiplicativity, and composite m inside the descent needs no primality: only p is assumed prime.
   - Step 1 (pigeonhole on a^2 and -1 - b^2) is correct, with 0 < mp <= 2((p-1)/2)^2 + 1 < p^2.
   - I reran the descent with my own quaternion product, independent of GA.py, for all 668 odd primes below 5000. Every step met the divisibility claimed.
2. *Clause (iii).* Complete. An ordering P' contains s^2 for every s != 0, because either s or -s is in P' and P' is closed under products. Closure under sums then puts every nonzero sum of four squares in P', which is all of P by (ii). If t were in P' but not in P, then -t is in P, which is contained in P'. That contradicts the disjointness of P' and -P'. Nothing is missing.
3. *Clause (v).*
   - Pivots: the claim that a non-negative form with a zero diagonal entry has that whole row zero is right. If A_ii = 0 and A_ij != 0, then (t e_i + e_j)^T A (t e_i + e_j) = 2t A_ij + A_jj, which is negative for a suitable rational t. The same holds for each Schur complement, which is congruent to a restriction of the form. I ran an LDL^T with this zero-pivot rule on 300 random rational semidefinite matrices of rank below n, which met 431 zero pivots. A = L D L^T held every time.
   - **One formula is wrong.** The proof writes D_jj = (L^{-1}e_j')^T A (L^{-1}e_j') for "the vectors e_j' with L^T e_j' = e_j". From A = L D L^T, the correct expression is e_j'^T A e_j' = (L^T e_j')^T D (L^T e_j') = D_jj with e_j' = (L^T)^{-1} e_j. The extra L^{-1} is wrong. The conclusion D_jj >= 0 is unaffected.
   - The count of at most 4n terms is right: four per nonzero pivot.
   - The identification of the sums of x x^dagger with the sums of y y^T is right, through the columns of x.
4. *Classical content and the reading.* The note says it plainly: nothing here is new (Lagrange, Euler, the easy half of Legendre, Artin and Schreier). The reading is accurate in substance. "the order is not a further datum" over Q is exactly (iii). Two small problems:
   - "four real components" should be "four rational components". Over the reals, one component suffices.
   - (v) rests on clause (i) of the stored two-mode theorem ("the algebra of two modes, by clause (i) of ..."), but that theorem is only in `lineage.motivated_by`, not in `uses`. Either add the uses edge or say the parenthesis is a remark. The main sentence of (v) is self-contained for Mat_n(Q), so the remark option is the cleaner one.
   - Separately, the uses edge to `synthesis.division-gives-the-rationals@2` supplies only the existence of Cl_Q(3,0) and a comparison. That is acceptable, but its premise() touch in the last check function is decorative.

### Fixes required
- proof-main.tex, (v): replace "$D_{jj} = (L^{-1}e_{j}')^{T}A\,(L^{-1}e_{j}') \ge 0$ for the vectors $e_{j}'$ with $L^{T}e_{j}' = e_{j}$" with "$D_{jj} = e_{j}'^{T}A\,e_{j}' \ge 0$ for the vectors $e_{j}' = (L^{T})^{-1}e_{j}$".
- entity.md, formal, Reading: replace "four real components being needed by (iv)" with "four rational components being needed by (iv)".
- entity.md, formal (v): either add `synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear@1` to `uses`, or replace "(the algebra of two modes, by clause (i) of \claimref{...two-modes...})" with "(for instance the algebra of two modes; a remark, by clause (i) of \claimref{...})".

### Recomputed and perturbed
- **Recomputed:** the descent for the 668 odd primes below 5000 (own quaternion code), and the zero-pivot LDL^T on 300 random semidefinite matrices.
- **A1:** the descent used x y in place of x y~. The descent check fails, as it should.
- **A2:** 7 d^2 replaced by 6 d^2. The (iv) check fails, finding solutions.
- **A3:** residues taken in [0, m) in place of (-m/2, m/2). The descent check fails.
- **Weakness:** the check4 W413 warnings are fair. The multiplicativity samples are a guard on conventions only, and clause (v) is sampled once, positive definite, with no zero pivot. That is acceptable given that the proof carries both.

---

## B. synthesis.additive-weights-on-the-rational-projectors-are-linear-for-every-number-of-modes

**Verdict: SOUND WITH FIXES.** The reduction from size n >= 4 to size 4 is correct. The title, one-liner and lay level overclaim, and clause (iv) is false as worded at one mode. The whole result is conditional on the stored theorem for size four, which I did not re-referee. Its review state is `draft`, and B adds nothing to it.

### Points of REFEREE.md

1. *Step 1 applies the stored theorem correctly.* Put G = g ι, an n by 4 rational matrix with G^T G = I_4.
   - For a projector E of Mat_4(Q), E^ = G E G^T is symmetric and idempotent, and E^ E'^ = G E E' G^T. So orthogonal pairs go to orthogonal pairs, and (E + E')^ = E^ + E'^.
   - Composed with the isomorphism m of clause (i) of the stored theorem, E -> mu(E^) is an additive weight on the projectors of Cl_Q(2,2) with values in the same V. That is exactly the class of clause (iii) at version 1, which assumes no sign condition, no normalisation and no continuity, with values in any Q-vector space.
   - The zero projector is harmless: additivity forces mu(0) = 0 in both settings. Normalisation is not needed.
   - Pi_x goes to Pi_{Gx}, and Gx . Gx = x . x, so q(G x) = sum rho'_ab x_a x_b. No hidden hypothesis.
2. *Clause (ii).*
   - The five functionals are always nonzero: c(r') = -1 and lambda_t(r') = r_t != 0, with no condition on r'.
   - Zero components of r' and the case r'_t = r_t are harmless. In the latter case lambda_t is the coordinate x_t.
   - The functionals have no common zero, so they span the 4-dimensional dual. Hence four of them are linearly independent, pairwise non-proportional, and so have distinct kernels. That is correct.
   - The supports are as claimed. On ker lambda_t, g_u(x) has support in (T \ {t}) union (S \ T) = S \ {t}. On ker c, g_u(x) = x lies in Q^T.
   - My own random search used 4000 rational vectors of support 5 to 8, with random T inside the support, random sign-shuffled four-square representations (zeros included) and denominators up to 3. It always found exactly 4 distinct kernels, never fewer, and g_u(r') = r every time. I found no vector for which the construction fails.
3. *The lemma.* Correct over Q, for values in V.
   - q vanishing on ker alpha_1 kills every monomial free of x_1. Over Q with char != 2, a V-valued quadratic form that vanishes as a function has zero coefficients, by polarisation. So q = alpha_1 gamma.
   - gamma vanishes on ker alpha_2 minus ker alpha_1, which spans ker alpha_2. So gamma = alpha_2 v.
   - ker alpha_3 is not the union of its two proper subspaces meeting ker alpha_1 and ker alpha_2. So v = 0.
   - The lemma implicitly needs dim U >= 2, which holds here (dim 4).
   - Random check: 500 random triples of distinct hyperplanes in Q^4. The rank of the 10 quadratic monomials at 18 points was always 10.
4. *Step 2.* rho is well defined: it is read from q at e_i and e_i + e_j alone, with no choice of T. For n >= 4 every support of size at most 4 lies in a coordinate four-space, and on that space q is a quadratic form agreeing with rho at the 10 determining points. So D = 0 on supports of size at most 4. Correct.
5. *Clause (v).*
   - Necessity: for u = phi(x), w = phi(y), (u.u)(w.w) - (u.w)^2 = c^2((x.x)(y.y) - (x.y)^2). The bracket is N(x y~) minus the square of its scalar part, which is the sum of the three squared bivector components. And c != 0, because the form is definite.
   - The example: u.u = 1, w.w = 7, u.w = 0, so the value is 7. Then 7/c^2 would be a sum of three rational squares, which A(iv) excludes.
   - "Similar" is the right reading of the stored note. A similarity phi with any factor c lets the four-mode theorem act on W through E -> phi E phi^T / c, which preserves projectors and orthogonality whether or not c is a square. So (v) does refute the first step as worded in the stored note.
   - (v) does not contradict (iii). (iii) never puts two arbitrary vectors in one similar four-space. It moves one vector at a time into the reflection of a coordinate four-space.
6. *Attempted counterexample in Q^5.*
   - Mod-4 parity construction: I tried weights depending only on the class of the primitive integer vector modulo 4 (in the manner of the stored parity weight). I collected 3000 rational frames of Q^5 (coordinate frames moved by one to three random reflections) and solved "frame sum = constant" modulo a large prime. The 120 classes met admitted only the constant solution (solution dimension 1).
   - Mod-8 attempt: under-determined at feasible size (2463 classes, 2500 frames), so it was not decisive.
   - Given points 1 to 4, I believe no counterexample exists. Since the step from n to 4 is proved, any failure would have to come from the stored theorem for size four.
7. *Overclaiming and prior art.*
   - The Mushtari sentences are worded as to-be-confirmed and claim no priority. I confirmed only that the citation Lobachevskii J. Math. 9 (2001) exists.
   - **The title is wrong for one mode.** "for every number of modes" includes l = 1, where Mat_2(Q) admits non-linear additive weights. The stored theorem's reading says so ("In size two no such theorem holds"). (iii) correctly says l >= 2, but the title, the one-liner ("of any number of modes") and the lay level ("for any number of modes") do not.
   - **Clause (iv) is false as worded.** It says "Let V = Q and n = 2^l" with no lower bound on l, and (i) allows every l.
     - Counterexample at l = 1: on the rays of Q^2, put f(r) = 1 for a primitive r = (a, b) with a odd and b even, f(r) = 0 for a even and b odd, and f(r) = 1/2 for both odd.
     - The orthogonal ray (-b, a) swaps the first two parity classes and fixes the third. So f is non-negative, sums to 1 on every frame, and defines an additive weight with mu(1) = 1.
     - The only candidate state has rho = diag(1, 0), from the values at e_1, e_2 and e_1 + e_2. But f(1, 2) = 1, while rho(r, r)/(r.r) = 1/5. So f is the restriction of no state.

### Minor points
- (i): the linear independence of the s_I (hence the injectivity of m) needs P_0 != 0. This is immediate but unstated. w_j v_j = (1 + e_j f_j)/2, so the scalar part of P_0 is 2^{-l}. Add it.
- (i) cites `tower.ladder-pairs-satisfy-car-vectors@4`, which is stated for the adjoined null pairs of the tower T_k. The identification with v_j = (e_j + f_j)/2 in Cl_Q(l, l) is the same reading the stored two-mode theorem makes, so there is precedent, but it is a reading.
- check4 W405: the main premise (the two-mode theorem) is declared but no check function touches it. Add `premise("synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear")`, or excuse it in coverage.yaml. The latter is more accurate, since the check never runs the four-mode theorem.
- The last check function's name says "the defect of a quadratic weight vanishes". It tests only that a linear weight is additive on one reflected frame and is recovered from its 21 values: the converse direction. Rename it, for example `check_linear_weights_sum_to_the_trace_on_a_reflected_frame_and_are_recovered_from_their_values`.

### Fixes required
- Title: replace "Additive weights on the rational projectors are linear for every number of modes" with "Additive weights on the rational projectors are linear in every size from four, so for two or more modes". The id may stay or be renamed by the maintainer.
- formal (iv): replace "Let $V = \Q$ and $n = 2^{\ell}$." with "Let $V = \Q$, $\ell \ge 2$ and $n = 2^{\ell}$."
- one-liner: replace "the algebra $\Cl_{\Q}(\ell,\ell) \cong \Mat_{2^{\ell}}(\Q)$ of any number of modes" with "the algebra $\Cl_{\Q}(\ell,\ell) \cong \Mat_{2^{\ell}}(\Q)$ of $\ell \ge 2$ modes".
- lay: replace "This result shows the same for any number of modes." with "This result shows the same for any number of modes from two on; for a single mode it is false."
- technical: replace "hence to the algebra of any number of modes" with "hence to the algebra of any number $\ell \ge 2$ of modes".
- formal Reading: replace "For the rational algebra of any number of modes" with "For the rational algebra of two or more modes".
- proof (i): after "$P_{0} = \prod_{j}p_{j}$ is a self-adjoint idempotent", add "and $P_{0} \ne 0$, since $p_{j} = \tfrac12(1 + e_{j}f_{j})$ and the scalar part of $P_{0}$ is $2^{-\ell}$".
- coverage.yaml: excuse the two-mode theorem under `untouched_premises` ("used by the proof's Step 1; its own check carries its finite computations"), or touch it.

### Recomputed and perturbed
- **Recomputed:** clause (ii) on 4000 random vectors, the lemma on 500 random hyperplane triples, and the mod-4 class-weight experiment (only constants).
- **B1:** r' built from three of the four squares, so r'.r' != r.r. The reflection check fails.
- **B2:** the sign of the reflection dropped (u x u^{-1}). The reflection check fails, since g(r') = -r.
- **B3:** only two hyperplanes fed to the lemma. The hyperplane check fails, since the rank drops below 10 and q = alpha_1 alpha_2 v survives. This is good: the check does test the three-hyperplane requirement.

---

## C. synthesis.order-of-the-doubled-dying-line-on-quarter-turn-lens-walls-is-a-valuation-in-the-ring-of-the-quarter-turn

**Verdict: SOUND WITH FIXES.**

### Points of REFEREE.md

1. *Clause (ii).* Correct in both directions.
   - f = sigma(sigma + 2)phi. Dividing 2^m sigma(sigma + 2) = A f + B sigma^{n+1} by sigma gives (sigma + 2)(2^m - A phi) = B sigma^n.
   - sigma is prime in the UFD Z[sigma] and does not divide sigma + 2, whose constant term is 2. So sigma^n divides 2^m - A phi.
   - The converse is the multiplication shown.
   - phi = (sigma + 1)^2 + 1 is monic, so Z[sigma]/(phi) is free on 1, sigma with (sigma + 1)^2 = -1, which is Z[J] via chi -> J. The image of the ideal (phi, sigma^n) is (J - 1)^n Z[J].
   - The sign 1 - chi^2 = -sigma(sigma + 2) is immaterial.
2. *Clause (i).* Correct.
   - (J - 1)^2 = -2J, so J(J - 1)^2 = 2.
   - The norm argument shows J - 1 is not a unit.
   - In the converse, cancellation in the domain Z[J] makes J - 1 divide the unit J^m. Hence (J - 1)^n divides 2^m if and only if 2m >= n.
3. *Clause (iv).*
   - d(1 - zeta) = Phi(1) = 2 is right: the characteristic polynomial of multiplication by zeta is x^M + 1, evaluated at 1.
   - (x - 1)^M = x^M + 1 + 2h(x) holds for M a power of 2, M = 1 included (with h = -1).
   - The exponent ceil(n/M) = ceil(2n/N) is right. The reduction mirrors (ii), with w = sigma w' and w'(0) = M != 0.
   - **One slip.** The proof says "Taking determinants, $2^{M} = 2^{M}d(h(\zeta))$, so $d(h(\zeta)) = 1$". But d(zeta - 1) = (-1)^M d(1 - zeta) = (-1)^M 2, so the left side is (-1)^M 2^M. At M = 1 (the half turn, zeta = -1), d(zeta - 1) = -2 and d(h(zeta)) = d(-1) = -1, not 1. The conclusion (h(zeta) invertible) is unaffected. The text already writes "d(zeta - 1) = ±2" later, so it is inconsistent with itself.
4. *Clause (iii).*
   - Clause (1) of `synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height` at version 2 says literally "k(Sig) >= 1 + log2 ord(1 - xi)", whatever the signature, given (L1). Clause (2) there gives xi = chi^2.
   - The stored K-ring is quoted correctly: clause (6) of the cohomology theorem at version 1, Z[chi]/(chi^4 - 1, (chi - 1)^{n+1}), proved given the imported Atiyah-Hirzebruch Fact.
   - So k - 1 >= ceil(n/2). "Replaces the pair of bounds" is accurate: ceil(n/2) = floor((n+1)/2), so the new bound is the second stored bound extended to every n, and it exceeds the first exactly at odd n.
   - Recomputation by my own route: membership of 2^m(chi^{N/2} - 1) in the ideal, worked in the truncated ring Z[s]/(s^{n+1}) as a triangular divisibility problem against f s^i. This is a different lattice from the check's, which works modulo f. It gives the order 2^{ceil(2n/N)} for N = 2, 4, 8, 16 and every n <= 60, with no mismatch. For N = 4, n = 1..14 the values are m = 1,1,2,2,3,3,4,4,5,5,6,6,7,7, which agrees with the stored record for n <= 14.
5. *The note on spectral asymmetries and on Stolz.*
   - Both are in the note and the technical level only. Nothing in the formal level or the proof rests on them.
   - The asymmetry route is labelled unfiled, and its literature from memory. But the note says "an unfiled exact computation of this run", a run reference in store text (house rule).
   - The technical level states a conclusion of that unfiled computation ("it also shows that those asymmetries see nothing more than the complex K-ring"). It should be marked as not part of the result.
   - The aside "L^5(4) has none [spin structure] (its stable tangent class 3 eta has w_2 != 0)" is right: w_2(3 eta) = w_2(eta), which is the reduction of the Euler class y, which is u != 0.
   - **Stolz.** The bibliographic data are right: S. Stolz, Comment. Math. Helv. 64 (1989) 661-674. The quoted values (m+1 for m = 0, 2; m+2 for m = 1, 3, 4, 5, 7; m+3 for m = 6 mod 8) are as quoted in Example 2.2(ii) of arXiv:0903.4462, Geom. Topol. Monogr. 10 (2007) 155. There the level is of RP^{2m-1} with the involution induced by multiplication by i, which is equivalent to maps S^{2m-1} -> S^{k-1} with f(iv) = -f(v), as the note says.
   - **But the source is misdescribed.** That paper is not a survey: it is M. Furuta, Y. Kametani, H. Matsue and N. Minami, "Homotopy theoretical considerations of the Bauer-Furuta stable homotopy Seiberg-Witten invariants".
   - The three agreements with stored values (3, 5, 6 at m = 2, 3, 4) are arithmetically right. The statement is worded as prior art, not imported, with Leon's decision asked. Good.

### Fixes required
- proof (iv): replace "Taking determinants, $2^{M} = 2^{M}d(h(\zeta))$, so $d(h(\zeta)) = 1$ and $h(\zeta)$ is invertible" with "Taking determinants, $(-1)^{M}2^{M} = 2^{M}d(h(\zeta))$, so $d(h(\zeta)) = \pm 1$ and $h(\zeta)$ is invertible".
- note: replace "(an unfiled exact computation of this run)" with "(an exact computation, not filed in the store)".
- note: replace "as quoted in Example 2.2 of the survey in Geom. Topol. Monogr. 10 (2007) 155 (arXiv:0903.4462)" with "as quoted in Example 2.2(ii) of M. Furuta, Y. Kametani, H. Matsue and N. Minami, Geom. Topol. Monogr. 10 (2007) 155 (arXiv:0903.4462), where it is the level of $\mathbb{R}P^{2m-1}$ with the involution induced by $i$".
- technical: replace "(unfiled; it also shows that those asymmetries see nothing more than the complex K-ring, so the spin class stays the input of the stored result on $L^{5}(4)$)" with "(not filed and not part of this result; computed for $n \le 8$, it indicates that those asymmetries see nothing more than the complex K-ring, so the spin class stays the input of the stored result on $L^{5}(4)$)".

### Recomputed and perturbed
- **Recomputed:** the order by the truncated-ring route for N in {2, 4, 8, 16} and n <= 60.
- **C1:** the relation (chi - 1)^{n+1} replaced by (chi - 1)^n. Both order checks fail.
- **C2:** J replaced by e_1 (square +1). The Z[J] check fails.

---

## D. synthesis.thermal-test-on-the-ground-conic-holds-at-exactly-three-points

**Verdict: SOUND WITH FIXES (the title only).** The interval library is sound as far as I can read. Every inequality checks out, and my own floating-point scan agrees.

### Points of REFEREE.md

1. *Is T the stored thermal test?* Yes.
   - The stored theorem (`synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter@1`) defines the thermal test as the vanishing of the Gibbs mean energy at beta = 2 pi/kappa. That mean energy is the sea energy (kappa/2r)B_2(delta) plus the thermal excitation over particles (a = k + delta) and holes (a = k + 1 - delta), with beta omega = 2 pi a/r.
   - On the conic, B_2 = -r^2/12, so in units of kappa/r the sea gives -r^2/24.
   - The cited null-ordering theorem (ii) at version 4 gives (kappa/2)B_2(delta) at spacing kappa. The rescaling to kappa/r is the one the window theorem itself makes.
   - The stored clause (ii) asserts that the test holds at (1, 1/2), (1/2, 1/4) and (sqrt(2/3), 1/3) and their mirrors. It does not assert "exactly"; Remark 1 there says "computed, not proved". The conic values are right: r^2 = 1/4, 2/3, 1.
   - The zero at 1/3 rests, in the stored theorem, on the imported theta identities. D's note says so.
2. *Step 1.* All correct.
   - 0.3^2 = 0.09 > 1/12 gives delta > 1/5. Also 1 - delta >= 1/2.
   - lambda >= 40 pi/3 > 8, and a e^{-lambda a} decreases for a >= 1/lambda.
   - The bracket: 2[1/5 + (6/5)(1/2000)/(1999/2000)^2] = 0.40120 < 0.41.
   - r^2 e^{c/r} has derivative e^{c/r}(2r - c) < 0 for r < pi/5. At r = 3/20, (9/400)e^{8 pi/3} >= (9/400)(2.718)^8 = 67.0 > 66 > 9.84.
   - At delta = 429/2000, r^2 = 0.021862 < 0.0225, and r increases with delta.
3. *Step 2.* All correct.
   - The bounds |g| <= a e^{-x}, |g'| <= e^{-x}(1 + aM(a+1)) and |g''| <= e^{-x}(2M(a+1) + aM^2(a+1)^2 + aM(a+2)) follow from g' = a's + a s_x x' and g'' = 2a's_x x' + a(s_xx x'^2 + s_x x''), with |x'| <= M(a+1) and |x''| <= M(a+2).
   - For a >= 2 and M >= 1, each bound is <= 4 M^2 a^3 e^{-x}, with equality for g'' at a = 2 and M = 1.
   - The next step weakens 4 to 11 for no reason. That is harmless, but it is why the constant is 223/10 and not about 8.03.
   - The ratio (10/9)^3 rho < 1/300 uses rho < 1/500 (e^{-2 pi} = 0.00187).
   - 22 x 300/299 = 22.07 < 22.3.
   - The check applies the bound exactly as stated: M = max(1, upper end of lambda, |ends of lambda'|, |ends of lambda''|), lambda_0 = the lower end of lambda, K = 8, factor 729. It widens all three jet components by it.
   - The widening is tiny: at most 3e-14 at delta = 1/2 and 1e-21 at delta = 429/2000.
4. *Step 3: the interval library.* I read every operation.
   - Representation: iv uses floor and ceil. iadd and isub are exact. imul uses floor of the minimum and ceil of the maximum of the four products. irecip is floor(P^2/hi), ceil(P^2/lo). isqrt is the floor and ceil of the integer square root (the Newton iteration returns the floor).
   - iexp:
     - It halves with ceil for the upper end and floor for the lower end. Repeated directed halving keeps t_s >= t/2^s (respectively <=), and exp is monotone, so this is valid.
     - The series to order 30 at |t| <= 1/2 uses outward-rounded terms. The remainder is below (1/2)^31/31! x 1.1, about 6e-44 < 2^{-140}, and the result is widened by one unit (2^{-128}).
     - Squaring back with imul on a positive interval is valid. The amplification, at most 2^10 units for x up to about 340, is far below the margins.
   - pi: consecutive partial sums of the alternating arctan series bracket the limit (the terms decrease). The combination 16a - 4b is taken with the correct ends.
   - Jet rules: the product, the reciprocal ((1/g)'' = -g''/g^2 + 2g'^2/g^3), the square root ((sqrt g)'' = g''/(2 sqrt g) - g'^2/(4 g^{3/2})) and jfermi (s' = -s(1 - s), s'' = s(1 - s)(1 - 2s), then the chain rule) are all correct formulae. They are evaluated by inclusion-isotone interval operations, so dependency over-approximations such as imul(h, h) are valid.
   - I found no place where an enclosure can fail to contain the true value.
5. *Steps 4 to 6.*
   - The mean-value form T(m) + T'([lo, hi])[-h, h] is correct, and sign_on returns False, never True, when undecided.
   - The six regions are (lower, 429/2000] (Step 1), [429/2000, 0.246], [0.246, 0.254], [0.254, 0.3233], [0.3233, 0.3433], [0.3433, 0.46] and [0.46, 1/2]. They are contiguous, and the check asserts the ordering of the cuts.
   - T'(1/2) = 0 follows from T(delta) = T(1 - delta) and the smoothness of r(delta) at r = 1.
   - T'' < 0 on [0.46, 1/2] gives T' > 0, hence T < 0 on [0.46, 1/2).
   - The count and the multiplicities follow. I reproduced the 73 intervals.
6. *Independent recomputation (double precision, 40 terms).*
   - Values: T(0.215) = -1.01e-3, T(0.23) = -1.41e-3, T(0.245) = -2.75e-4, T(1/4) = 2e-18, T(0.27) = 5.27e-4, T(0.29) = 4.95e-4, T(0.31) = 2.69e-4, T(1/3) = -5e-18, T(0.36) = -1.91e-4, T(0.40) = -2.32e-4, T(0.45) = -8.66e-5, T(0.49) = -3.84e-6.
   - A scan at 200000 points on (1/2 - 1/sqrt 12, 1/2] finds sign changes only at 0.25 and 0.333333 (and a rounding-level one at 0.5).
   - T'(1/4) = 0.0485 > 0, T'(1/3) = -0.0098 < 0 and T''(1/2) = -0.077 < 0, matching the proof's signs.

### Fixes required
- Title: replace "The thermal test holds on the ground conic at exactly three points: no fourth array" with "The thermal test holds on the ground conic at exactly three points up to the mirror twist: no fourth array". The formal level itself lists five points of the (r, delta) half-plane.
- Optional, for readability: in Step 2, replace "hence at most $11M^{2}a^{3}e^{-\lambda a}$" with "hence at most $4M^{2}a^{3}e^{-\lambda a}$ (we use the weaker $11M^{2}a^{3}e^{-\lambda a}$, which gives the constant below)". Or tighten the constant; 223/10 stays valid either way.

### Perturbed
- **D1:** K = 2 terms. The tail bound swamps the margins, and three checks fail.
- **D2:** the Fermi factor replaced by the Bose factor (e^x - 1). Three checks fail.
- **D3:** conic coefficient 12 replaced by 11.9. Only the zero-containment guard fails. The sign checks still pass, because the zeros move only slightly within the stretches. This is expected: zero existence comes from the stored clause, not from this check.
- **D4:** K = 4. The zero guard and the sign check fail.
- **Not testable by perturbation:** the outward rounding is not exercised by any margin at 128 bits, so its soundness rests on the reading in point 4.

---

## E. synthesis.character-sums-over-the-twist-fibres-of-an-array-are-dirichlet-l-values

**Verdict: SOUND WITH FIXES.**

### Points of REFEREE.md

1. *(H1) to (H3).*
   - (H1) is correct: zeta(0, a) = 1/2 - a, zeta(-1, a) = -B_2(a)/2, and L(s, chi) = (2M)^{-s} sum_{a=1}^{2M} chi(a) zeta(s, a/2M) for chi modulo 2M. The imprimitive case is covered because the formula holds for any character modulo 2M.
   - (H2) is correct: L(0, chi_D) = 2h(D)/w(D). Check: 1/2 at D = -4 and 1/3 at D = -3.
   - (H3) is the Siegel and Cohen formula for zeta_K(-1). **It needs b to run over all integers, positive and negative**, with b == D mod 2 and b^2 < D. The proof's numbers (5 for D = 8, 10 for D = 12) and the check (which counts b != 0 twice) use that reading, but the formal text writes "$\sum_{b \equiv D\,(2),\ b^{2} < D}$" without saying b in Z. With b >= 0 only, D = 8 would give 4, not 5.
   - Check values: zeta_{Q(sqrt 5)}(-1) = 1/30 and zeta_{Q(sqrt 2)}(-1) = 1/12, both correct.
2. *The clauses.*
   - (i): 1 - 2 delta is correct.
   - (ii): sum chi(2j+1)(1 - 2 delta_j) = 2L(0, chi) and sum chi B_2(delta_j) = -L(-1, chi)/M. The sea energy times beta is (pi/r)B_2, giving -(pi/(Mr)) L(-1, chi). All signs and factors are right.
   - (iii): the substitution a -> 2M - a is right.
   - (iv): chi_4(a) = <-J J^a>_0 gives 1, -1 at a = 1, 3. The halves are those of clause (iii) of the light-ray theorem (version 1) at r = 1/2, which states A(1/2, 1) = A(1/4, 1/2) x A(3/4, 1/2).
   - **(v): one hypothesis is wrong.** "read modulo $2M$ with $|D|$ dividing $4M$" should be "dividing 2M". chi_D is a character modulo 2M only if its conductor |D| divides 2M. Counterexample to the wording: D = -8, M = 2. Here |D| = 8 divides 4M = 8, but chi_{-8}(1) = 1 and chi_{-8}(5) = -1, so chi_{-8} is not periodic modulo 4. All the instances and all 14 cases of the check do satisfy |D| | 2M.
   - Also in (v): "The sums of (ii) are those of $\chi_{D}$ at its conductor times the factors" is loose. It is the L-values that factor, not the sums. The sums carry the 1/M of the modulus actually used.
   - Every instance value was recomputed:
     - By hand: D = -3, M = 3 (asymmetry 4 x (1/6) x 2 = 4/3); D = 5, M = 5 (energy -(1/5)(-2/5)(3) = 6/25); D = 13, M = 13 (divisor sum 4 + 4 + 1 + 1 = 10, L(-1) = -2, energy 6/13).
     - By my own code, with characters built from their definitions (Legendre symbols and explicit tables), not from the check's Kronecker routine: all twelve stated values (1, 2, 4, 4/3, 4, 0, 0, 0; 1/4, 1/3, 6/25, 6/13).
3. *The first check is a tautology, and the coverage record says so.*
   - The second check is independent evidence: class numbers by counting reduced forms, and the divisor-sum values, both against the generalised Bernoulli numbers.
   - For a result whose status is "proved given (H1)-(H3)", the evidence that matters is the proof, which is a short and correct derivation from (H1) plus Euler factors. The checks only guard conventions. That is enough for the stated status, provided (H1) to (H3) stay in-statement hypotheses. Whether to import them is a maintainer decision (below).
4. *Overclaiming.* None found. The note, the Reading, the technical level and the lay level all say that there is no constraint, no selection, no prediction and no link to zeros; only special values at 0 and -1 are used. The title is accurate.

### Fixes required
- formal (v): replace "read modulo $2M$ with $|D|$ dividing $4M$" with "read modulo $2M$, with $|D|$ dividing $2M$".
- formal (H3): replace "$\sum_{b \equiv D\,(2),\ b^{2} < D}$" with "$\sum_{b \in \Z,\ b \equiv D\,(2),\ b^{2} < D}$".
- formal (v): replace "The sums of (ii) are those of $\chi_{D}$ at its conductor times the factors" with "The L-values in (ii) are those of $\chi_{D}$ at its conductor times the factors".

### Perturbed
- **E1:** w(-3) = 2 in place of 6. The class-number check fails.
- **E2 (first try):** the Kronecker value at 2 changed from D == 1, 7 (mod 8) to 1, 3. All checks still pass. This is a vacuous perturbation: odd fundamental discriminants are 1 or 5 mod 8, so the edit changes nothing.
- **E2 (second try):** changed to 1, 5. The class-number and divisor check fails.
- **E3:** the asymmetry 1 - 2 delta replaced by 1 - delta. The fibre-sum check fails.

---

## Across

- **House style.**
  - No em dashes, no "honest", "load-bearing" or "clever" in any of the five entities or proofs.
  - Macros: all are in `store/notation.yaml` or standard (arctan, dagger, claimref).
  - Q(v) convention: no squared vector is written otherwise.
  - Run reference: one, in C's note ("of this run"); fix above.
  - The notes use "Kill condition registered before computing (D1/A1/C1/B2)" labels. The stored two-mode theorem's note does the same, so there is precedent. Strictly these are method vocabulary in store text, and the letter-number labels mean nothing to a reader of the store. The maintainer may want them dropped or reworded ("A test fixed in advance: ...").
- **outside_ga declarations.** All five are accurate.
  - A: other. The quaternion product is GA; congruences and the LDL^T are scalar.
  - B: other. The reflection is computed in Cl(n,0); the rest is rational linear algebra.
  - C: other. Z[J] is the integer even subalgebra of Cl(2,0); (iv) is in Z[x]/(x^{N/2} + 1), which correctly is not a subring of a rational Clifford algebra of the plane for N >= 8.
  - D: other, grade 0 only.
  - E: complex-analysis. The analytic continuation is outside GA; chi_4 is read off J.
- **Duplicates and contradictions.**
  - No stored entity proves four squares, generalised Bernoulli or L-values, or the order 2^{ceil(n/2)} for all n. I searched the store texts.
  - B(v) refutes a sentence in the note of the stored two-mode theorem ("Not done: ... the first step would be to show that any two rational vectors ... lie in a four-dimensional rational subspace similar to the standard one"). The maintainer should amend that note when B is accepted.
  - C supersedes the pair of bounds in clause (2) of `synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height`, and that entity's text should point to C.
  - D turns Remark 1 of the window-energy theorem from computed to proved, and that remark should point to D.
  - B uses A(ii), and A(iv) supplies B(v)'s arithmetic. These are consistent.
  - No proposal contradicts another.

## Only the maintainer can decide
1. Whether to accept B, which rests entirely on the stored two-mode theorem (review: draft, four finite computations carried by its check). Nothing in B re-proves it. Prior art (Mushtari 2001, Problem G) is still to be confirmed from the paper.
2. E: whether (H1) to (H3) should become imported Facts or stay in-statement hypotheses, cited from memory (I confirmed their normalisations).
3. C: whether to record Stolz (1989) as prior art for the definite-side rung count (citation verified through Furuta, Kametani, Matsue and Minami, Example 2.2(ii)). Also whether to file the unfiled spectral-asymmetry computation or drop its mention.
4. A: whether the reference in (v) to clause (i) of the two-mode theorem becomes a uses edge or a remark.
5. B: renaming the id to match the corrected title (the id says "for every number of modes").
6. D: nothing beyond the title. Note that the zero at twist 1/3 is inherited from the stored theorem through the imported theta identities.
7. Updates to the stored entities superseded or refuted in part: the note of the two-mode theorem, clause (2) of the lens-wall theorem, and Remark 1 of the window-energy theorem.
