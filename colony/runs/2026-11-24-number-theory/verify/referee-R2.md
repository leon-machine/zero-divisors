# Referee R2: synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear (v1), line by line, and prior art

**Verdict: SOUND WITH FIXES.** The fixes are to wording and labels only (prior-art attribution, stale clause labels in
check.py). I found no gap in the mathematics of clause (iii). Every step is either proved on paper or carried by a
finite exact computation, and I re-verified each of those computations with my own code. Status "proved" is justified.
The novelty claim for clause (iii) is **supportable but unconfirmed**. No source I could read contradicts it. Two
sources that would settle it, the full texts of Mushtari 1995 and 1998, could not be read; see Part 2.

Scope of my own work. All scratch files are in `verify/scratch-R2/`:
- `r2_verify.py` and its log: the finite steps of (iii), with my own quaternion code.
- `r2_box.py`, `box4.log`, `box5.log`: the box test.
- `r2_classes.py` and `classes.log`: class-function refutation attempts.
- `r2_clause_iv.py`: clause (iv) by a 4 by 4 matrix route.
- `pert_*/check.py`: the perturbed copies of the stored check.

I did not read the findings, work, RUN.md, REPORT.md or referee-R1. I did not edit `store/`, and I did not run check4 or `tp check`.

## 1. Skeleton of clause (iii)

| Step | Content | How it is carried |
|---|---|---|
| S0 | An additive weight is the same thing as a function f on rays of Q^4 with constant frame sums ((i)). Rays are G = nonzero rational quaternions mod Q^x. Frames are exactly the left cosets {x, ax, bx, abx} of Klein groups of half turns ((ii)). So a weight with frame sum 0 is a linear map Q[G] -> V that kills J = span{kappa_{a,b}[x]}. J is a two-sided ideal. R: Q[G] -> M_3(Q) (rotation representation) kills J, because 1 + R(a) + R(b) + R(ab) = 0. | Proved on paper (a few lines each). |
| S1 | W = image of Q[O] in A = Q[G]/J. The 24 frame relations inside O have rank 15, so dim W <= 9. R(O) spans M_3, so R: W -> M_3 is an isomorphism. G_W = {x : [x] in W} is a subgroup. | Finite computation in check; subgroup argument on paper. |
| S2 | A 34-frame identity puts [2 + B_1] in W. Conjugation by O gives all six 2 +- B_k. | Finite exact computation (certificate). |
| S3 | Every integer quaternion of norm 5^t is a product of the six rotors 2 +- B_k and a unit, so it lies in G_W. | Table mod 5 in the check; induction on paper. |
| S4 | For any rational half turn n, some power g = (2 + B_1)^s is conjugated by n to an integer rotor of norm 5^(2e+s), so it lies in G_W. Hence v_n = R(n)[n] commutes with R(g). Likewise with B_2. Two rotations about different axes generate M_3, so v_n commutes with W. | Proved on paper (existence of s from the finiteness of (Z[i]/N')^x; the mod-5 argument gives sin(phi) != 0). Sampled in check. |
| S5 | The frame relation of an orthogonal triple, multiplied by P_a, P_b, P_c, gives three equations forcing v_a = v_b = 1. So [n] = R(n) for all bivectors. | Proved on paper (no commutativity of v_a, v_b needed). |
| S6 | Bivectors generate G (x = (xm) m^-1 with m orthogonal to the vector part of x). So A = W = M_3, and f = Lambda o R, a quadratic form over r.r. | Proved on paper. |

## 2. Step-by-step decisions (Part 1 point 2)

**(a) Weights to frame functions to Q[G]/J. Correct.**
- Both directions of (i) are proved. Basis independence uses one fixed orthogonal basis of the complement, which is rational.
- The identification of frames with cosets in (ii) is correct. a and b are orthogonal pure quaternions, so ab is pure and orthogonal to both. The fourth quotient c is orthogonal to a and b, hence a multiple of ab.
- I checked all 34 certificate frames are cosets of this form.
- A function with frame sums 0 is exactly a linear functional on Q[G] vanishing on J. Nothing is lost in this passage.

**(b) The octahedral span. Correct, recomputed.**
- O is the 24 rays with entries in {0, +-1} and norm 1, 2 or 4. It is closed under product and conjugation mod scalars. It has 9 bivectors and 4 orthogonal triples.
- These give 24 distinct cosets. They are also all the orthogonal frames among the 24 rays; I checked all C(24,4).
- The rank of the incidence matrix is 15 (exact Fractions). R(O) spans M_3 (rank 9), and R kills each relation.
- The quotient meant is A = Q[G]/J, and W is the image of Q[O] in it. dim W <= 24 - 15 = 9 uses only relations lying in J. dim W >= 9 because R(W) = M_3. Precise and correct.
- Side observation: frame sums on O alone already pin the 24 values to the 10 quadratic forms. With the constant column the solution space is 25 - 15 = 10.

**(c) The 34-frame certificate. Verified independently.**
- I parsed the certificate from proof-main.tex, not from check.py, and it agrees with check.py's CERT.
- Every set is four distinct primitive, pairwise orthogonal vectors, and each is a coset.
- The q_F sum to 2/5. (2,1,0,0) gets total 1. Exactly 43 other non-O rays occur, all with total 0. The 18 nonzero O totals equal the t_s listed in the tex, value by value.
- As a consistency test, the identity holds for all 10 quadratic forms.
- The conjugates of 2 + B_1 by the 24 O-rotors are exactly the six rays 2 +- B_k.

**(d) Factorisation into 2 +- B_k. Correct.**
- Divisibility of the conjugate pi~ y by 5 depends only on y mod 5. I recomputed the 145 classes of norm 0 mod 5 (including y = 0), and each has a left divisor among the six.
- The induction is sound. The quotient y' = pi~ y / 5 is integral with norm N(y)/5.
- As an extra test beyond the stored check, which only covers norms 25 and 125: all 6248 integer quaternions of norm 625 (= 8 sigma(625)) factor into four of the six and a unit.
- The six are distinct classes mod right units, so the left-divisor statement is not vacuous.

**(e) Existence of the exponent for every rational bivector. Proved, including 2 | N and 5 | N.**
- Scale n to be integral and write N = 5^e N' with 5 not dividing N'. Then 2 + B_1 is a unit of the finite ring Z[B_1]/(N'), because (2 + B_1)(2 - B_1) = 5 is prime to N'. So some power is 1 mod N'. This holds for N' even, and N' = 1 is trivial (s = 1).
- The factor 5^e is absorbed by y = 5^e alpha - (beta/N') n B_1 n, which is integral with norm 5^(2e+s).
- (2 + B_1)^2 = 4(2 + B_1) mod 5 gives alpha beta != 0 mod 5, so sin(phi) != 0 and the projector formula for E_11 is legitimate (cos(phi) != 1).
- I ran this exact construction for all 2017 primitive integer bivectors with entries up to 8, for both B_1 and B_2. Of these, 372 have 5 | N and 834 have 2 | N. In every case the conjugate has the claimed class and norm and factors (largest s = 136). The stored check samples only 10.

**(f) Commutant argument. Correct.**
- [n][g] = [g'][n] in A, with g' = n g n^-1 in G.
- With [g] = R(g) and [g'] = R(n)R(g)R(n) in W, and R(n)^2 = 1, we get v_n R(g) = R(g) v_n.
- The matrix-unit identities are right; I checked each product. E_11, E_22, E_32 - E_23 and E_13 - E_31 generate M_3.
- No finite-dimensionality of A is needed at this step.

**(g) Central factor equal to 1. Correct.**
- v_c = v_a v_b follows from [a] = R(a) v_a and v_a commuting with W.
- Left multiplication by P_a, with P_a R(a) = P_a and P_a R(b) = P_a R(c) = -P_a, gives P_a(1 + v_a - v_b - v_a v_b) = 0. The bracket commutes with W, so it is 0. This uses 1 = sum X_k P Y_k in the simple algebra M_3, and that [1] is the unit of W.
- Solving the three equations needs no commutation between v_a and v_b. Every rational bivector lies in an orthogonal triple.

**(h) Generators to all rays. Correct.**
- Step 6 shows every x is (pure)(pure)^-1. So G_W = G, and A, which is spanned by the [x], equals W.
- The conclusion f(r) = Lambda(R(x_r)) is a quadratic form over r.r because the entries of R(x_r) are (quadratic in r)/(r.r).
- The ten functions r_i r_j/(r.r) are independent on rays, which gives uniqueness of rho.

## 3. Values in an arbitrary rational vector space V (point 3)
Justified. Every step is Q-linear: extend f Q-linearly to Q[G] -> V, factor through A, and Lambda: M_3(Q) -> V. The only divisions are by rationals (q_F, the 1/4 of mu(1)), which is legitimate in a Q-vector space. Nothing uses a basis or an order on V. The statement would fail for arbitrary abelian groups, because of the divisions, but it is not claimed for them.

## 4. Refutation attempts (point 4)
Kill condition, registered before computing: a nonconstant class function with constant frame sums on the frames used, or an inner set of rays whose projected solution space stays above 10 as the box grows. No kill.

**Box test.** f on all primitive rays with |entries| <= B, and c, with sum_F f = c on every orthogonal frame inside the box. The rank is computed mod a prime p (exact integer arithmetic), so dim_p >= dim_Q. Primes used: 33554393, plus 16777213 at B = 3 and B = 5 (identical results).

| B | rays | frames | dim of solutions (10 = quadratic forms) | projection onto box-1 rays + c | onto box-2 rays + c | onto box-3 rays + c |
|---|---|---|---|---|---|---|
| 1 | 40 | 32 | 19 | 19 | - | - |
| 2 | 272 | 380 | 88 | 19 | 88 | - |
| 3 | 1120 | 2652 | 253 | 19 | 67 | 253 |
| 4 | 2928 | 8756 | 568 | **10** | 34 | 196 |
| 5 | BOX5 |

Reading:
- The total excess over 10 grows with the box (9, 78, 243, 558). No ray is in zero frames. The excess sits on rays near the box boundary, which lie in few frames.
- On a fixed inner set it shrinks:
  - The 40 rays of box 1 (O plus the 16 rays of norm 3) carry a 9-dimensional excess up to B = 3, which is killed exactly at B = 4. This matches the certificate needing entries up to 4.
  - The box-2 projection falls 88 -> 67 -> 34.
- This is the behaviour the theorem predicts: excess killed by frames reaching further out. It is consistent with the entity's "pinned from entries up to 4".
- The projection dimensions are computed mod p and are not exact-rational bounds in either direction. Agreement of two primes at B = 3 makes a mod-p artefact very unlikely, but I label them computed (mod p), not proved.

**Class functions.** These were tested on 6000 random frames {x, ax, bx, abx} with entries up to 9, so many rays lie far outside the boxes. I solved for g on the classes and c. Since rank_p <= rank_Q, a mod-p dimension of 1 proves exactly that only constants solve, for those frames. Result: only the constants, every time, for functions of:
- the primitive vector mod 2 (15 classes), mod 3 (40), mod 4 (120) and mod 5 (312);
- v_2(r.r), v_3(r.r) and v_5(r.r);
- the class of r.r mod squares at the primes 2, 3, 5, 7, 11 (32 classes).
MOD8LINE

**Not a counterexample, but a check of the hypothesis's role.** The parity weight of (v) is non-quadratic on the unit atoms. By (iii) it has no extension to all rays with constant frame sums. No contradiction arises: the extra frames through non-unit rays are exactly what (iii) uses.

## 5. The stored check (point 5)
- `python3 colony/runcheck.py store/claims/.../check.py`: all 9 functions PASS (0.6 s).
- Coverage reading: coverage.yaml is accurate about what is complete and what is sampled.
  - The functions for Steps 1, 2 and 3 are complete for the finite facts the proof cites.
  - Step 4 is sampled on 10 bivectors.
  - Step 5's 169-point grid is only an illustration, and coverage says so.
  - The general arguments are correctly assigned to the proof.
- Perturbations (copies in `scratch-R2/pert_*`), all caught:

| Perturbation | Failing functions |
|---|---|
| coefficient 3/10 -> 1/10 in the first certificate frame | certificate |
| one ray in a certificate frame changed (2,-1,-1,0) -> (2,1,-1,0) | certificate, frames-are-cosets, linear-functionals |
| one of the six primes duplicated (2,0,0,-1) -> (2,0,0,1) | factorisation, conjugate-of-a-power |
| sign error in the quaternion product (a2 b3 - a3 b2 -> -a2 b3 + a3 b2) | 5 functions, incl. octahedral, factorisation, frames |
| TARGET (2,1,0,0) -> (1,2,0,0) | certificate |
| CERT_WEIGHT 2/5 -> 3/5 | certificate |
| last certificate frame deleted | certificate |
| signature of Cl(3,0) changed to (1,1,-1) | frames-are-cosets (GA product comparison) |

- Defect: check.py's comments carry stale clause labels from an earlier numbering:
  - "certificate of clause (ii)";
  - AXES "for ... clause (iv)";
  - TRIPLES "clause (v)";
  - UNIT_BOX "clause (vii)";
  - FACTOR_BOX "clause (iii)";
  - POWER_RANGE "clause (iv)".

  In the entity these are Steps 2, 4, 5 of (iii), clause (v), Step 3 and Step 4. These are comments only and do not affect the evidence.
- In `check_linear_functionals...` the "leading minors" line computes ranks, not minors. The determinants 3, 5, 17 and 62 are checked separately in the same function, so the claim in coverage.yaml stands.

## 6. Clauses (i), (ii), (iv), (v) (point 6)
- **(i)** Sound. The check covers the 16 blades and five atoms; the general statements are proved.
- **(ii)** Sound. See (a).
- **(iv)** Sound.
  - Positivity of L(xx^dagger) follows from r^T rho r >= 0 on rational vectors, because the columns of m(x) are rational. Uniqueness follows from self-adjointness.
  - I recomputed the CHSH functional by a separate route: 4 by 4 Fraction matrices built from m of the generators. I checked the Clifford relations, multiplicativity on all 16 blades, that dagger is the transpose, and that <x>_0 = tr m(x)/4. Then C is symmetric, traceless, and satisfies C^3 = 8C (so its eigenvalues lie in {0, +-2sqrt2}). Values: lambda(1) = 1, lambda(C) = 4, lambda(Pi_(1,0,0,1)) = -1/4, lambda(Pi_(2,1,-1,2)) = -9/20, all as stored.
- **(v)** Sound.
  - Squares mod 8 force t in {1, 4} odd coordinates. The orthogonality parity argument is right.
  - For the non-quadratic step, the four rays (1, +-2, +-2, 0) give 2 alpha_i = alpha_j + alpha_k for all distinct i, j, k, hence all alpha are equal (= 1/4, the constant quadratic). The phrase "with alpha_i != 1/4" in the proof is unnecessary but harmless.

## Exact fixes
1. **Entity note and technical level: Problem G attribution.** Mushtari 2001 does not originate Problem G. The paper states the question for Pi(Q^n) and Pi_0(Q^n) and refers to it as Problem G of its reference [2], Mushtari, IJTP 34 (1995) 1627. Suggested wording: "Mushtari (2001), restating Problem G of Mushtari (1995), asks whether every measure ([0, infinity)-valued and additive on orthogonal pairs) on the orthogonal rational projections Pi(Q^n), or on the sublogic Pi_0(Q^n) generated by the unit atoms, has the form tr(TP), and does not resolve it."
2. **Proposition 4 is a partition, not the colouring.** In Mushtari 2001, Proposition 4 is a partition of S(Q^4) into three parity classes. The regular four-colouring of S(Q^4) is stated as its Corollary, and the two-valued measure on the unit atoms is a consequence the paper does not spell out. Suggested: "(Mushtari 2001, Proposition 4 and its corollary, a regular four-colouring of the rational unit sphere of Q^4, which gives a two-valued weight on the unit atoms)".
3. **Reading level in the note.** The note says the paper was read "through abstracts and a summarising fetch only". The 2001 text is now readable at math-net.ru in English; see Part 2. The reading level should be updated once the maintainer reads it.
4. **check.py comments.** Relabel the stale clause references listed in section 5.
5. **Optional.** coverage.yaml for `check_conjugate...` could note that the proof's existence argument covers N' even and 5 | N. The proof already says so; I tested 2017 cases.

## Part 2: prior art

| Source | What I read | Finding |
|---|---|---|
| D. Kh. Mushtari, Lobachevskii J. Math. 9 (2001) 47-53 | **Full text in English** (math-net.ru getFT, paperid 128). Read through the fetch tool's summarising model with targeted questions, not verbatim by me. Abstract pages: EMIS, math-net, eudml, CORE. | Defines Pi(Q^n) (all orthogonal rational projections) and Pi_0(Q^n) (the sublogic generated by projections onto rays through S(Q^n)). Measures are "[0, inf)-valued", additive on orthogonal pairs. The question "admit the Gleason representation?" is attributed to "Problem G in [2]" (Mushtari 1995); the paper does not resolve it and does not explicitly call it open. Prop 1 (attributed to Kochen): no {0,1}-measures on Pi(Q^3). Prop 2: none on Pi_0(Q^n), n >= 6. Prop 3: none on Pi(Q^n), n >= 4. Prop 4: a parity partition of S(Q^4) into three sets, with Corollary a regular colouring of S(Q^4). Its n = 3 example (a {0,1}-measure on Pi_0(Q^3) from the three-colouring) is said not to touch Pi(Q^n), or Pi_0(Q^n) for n > 3. **Nothing in it proves a trace form for any measure on Pi(Q^4)**, so no overlap with clause (iii). |
| D. Mushtari, Int. J. Theor. Phys. 34 (1995) 1627-1635 | **Abstract and reference list only** (Springer 10.1007/BF00676275); full text not accessible. Plus the author's later slides (maths.ucd.ie Fq9Talks). | Per the slides (secondary, by the author): any Q-valued measure on the rational idempotent n by n matrices, n >= 3, is tr(TP), first proved with computer calculations. The domain is all idempotents (a "linear projector logic", no inner product), where orthogonality of P and Q is PQ = QP = 0. Clause (iii) does not follow: a weight on the symmetric idempotents need not extend additively to all idempotents, and the domain of (iii) has fewer additivity conditions. I could not read the statement of Problem G in this paper itself. |
| D. Kh. Mushtari, Mat. Zametki 64 (1998) 584-591 = Math. Notes 64 (1998) 506-512 | **Abstract only** (mathnet mzm1433, geodesic, CORE). The Russian PDF is unreadable through the fetch tool (font encoding); the English version is paywalled. | Field-valued charges on the logic of all projectors of a finite-dimensional space over F, for F = Q or a residue field, have the form tr(T P). Keywords say "linear projector logic", so all idempotents. Same conclusion as for 1995. |
| Havlicek, Krenn, Summhammer, Svozil, quant-ph/9911040 | **Paper** (ar5iv HTML, via summarising fetch). | Colourings of the rational unit sphere: S(Q^3) has chromatic number 3 (Godsil-Zaks). Higher-dimensional colourability (d < 6) is cited to unpublished work of Ovchinnikov, Okunev and Mushtari. No Gleason or linear-measure result. |
| Godsil and Zaks; D. A. Meyer (1999) | Not read; known from HKSS's description (secondary). | Kochen-Specker colourings, two-valued only. Not relevant to linearity. |
| Hamhalter, Dvurecenskij | **Abstract only** of Dvurecenskij, IJTP 42 (2003) 1403. | Gleason property for real or complex inner product spaces. Nothing over Q found. |
| Other searches | Abstracts of arXiv 2001.06738 (Benedetto-Koprowski-Nolan) and 2611.05656 (Aubone-Iovino). | Neither treats measures on rational orthogonal projections or Problem G. zbMATH and Google Scholar citation lists were not reachable (fetch errors), so I could not enumerate works citing Mushtari 2001. The 1995 paper shows one citation on Springer, which I could not identify. |

**Novelty conclusion: supportable, not established.**
- Nothing I read solves Problem G for Pi(Q^4), signed or non-negative. The 2001 paper itself proves only {0,1}-results on Pi(Q^n).
- The 1995 and 1998 trace-form theorems are on a larger domain (all idempotents) and do not imply (iii).
- The claim must stay conditional on two things I could not do:
  1. read the 1995 IJTP paper, which is where Problem G is stated and which might contain partial results on orthogonal projections;
  2. search the citations of the 2001 and 1995 papers.
- Note also that Mushtari's own Corollary to Proposition 4 already answers the Pi_0(Q^4) half of the question negatively, implicitly. So "answers Problem G for n = 4" should say "for Pi(Q^4)".
- The stored text claims priority only "pending a reading". With fix 1, that is appropriate.

## What only the maintainer can decide
1. Whether to obtain and read Mushtari, IJTP 34 (1995) 1627 (the statement of Problem G and any partial results) and the English Math. Notes 64 (1998) 506, before any public novelty claim.
2. Whether to raise review from "draft". On mathematical grounds this reviewer finds no obstacle.
3. The wording of fixes 1-3 (attribution of Problem G, Proposition 4 versus its corollary, reading level).
4. Whether to extend the stored check's Step 4 sample, for example to the 2017 bivectors used here, at a cost of about 4 s.
