# Referee R-P, run 2026-11-24-three-routes

Blind referee. I read REFEREE.md, `conventions`, the three proposals (entity, proof, check, coverage), the cited
store entities at their pinned versions, and the check4 logs. All three logs: 0 errors, 0 findings, check
pass, no W413. I did not read findings/, work/, RUN.md, ROUTES.md or other referees' reports. My own scripts
are in `verify/work-R-P/` (indep1.py, indep23.py, indep2b.py; perturbed copies p1a to p3c). All evidence is
Fraction or GA.py arithmetic.

---

## 1. synthesis.additive-weights-on-the-rational-projectors-of-two-or-more-modes-are-linear

**Verdict: SOUND WITH FIXES** (two small fixes; the mathematics is complete).

### Premises at pinned versions
- `synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear@1` (stored v1). Its formal
  statement is what the proof needs: (i) the isomorphism m of Cl_Q(2,2) onto Mat_4(Q), with the transpose as
  adjoint and m(Pi_r) = rr^T/(r.r); (ii) <x_r x~_r'>_0 = r.r'; (iii) linearity of additive weights **with values
  in any rational vector space V**, no sign condition. So it applies to V-valued weights as used.
- `synthesis.signed-directions-and-the-integer-clifford-algebra@2`, `tower.ladder-pairs-satisfy-car-vectors@4`,
  `std-algebra.quaternions@1`: current versions, used for what they say.

### Step-by-step check of the reduction (points the orchestrator raised)
1. **Subspaces the stored theorem is applied to.** The proof never needs "similar"; it uses the image
   W = R(Q^S) of a coordinate four-space under a rational orthogonal R (a reflection). The pulled-back weight
   mu'(E) = mu(R iota(E) R^T) is an additive weight on the projectors of Mat_4(Q): R iota(E) R^T is a
   symmetric idempotent, sums and EE' = 0 are preserved. So the stored theorem applies exactly as stated at
   v1, through its own m. Correct.
2. **Reflection (iii).** m.m = -2 s.m from s.s = r.r, so R(s) = r; W lies in Q^S + Q r. Verified
   independently on 12 random vectors with full support in Q^5 to Q^8, with S a random set of four
   coordinates (not the first four, as in the check) and s from a brute-force four-square search (not the
   rotor induction): R orthogonal, R s = r, conjugated projectors symmetric idempotent (indep1.py).
3. **Every rational vector is reached.** The induction runs on the support size k over all of Q^N: k <= 4 is
   a coordinate four-space (N >= 4 used); for k >= 5, S is taken inside the support of r, W has all supports
   inside supp(r), the coordinate functionals lambda_i (i in supp r) are nonzero on W and span W* (they have
   no common zero), so at least four are pairwise non-proportional; their kernels are distinct hyperplanes of
   W whose vectors have support <= k - 1. Complete. My computation: in every trial there were 5 classes of
   proportionality and the quadratic evaluations at kernel vectors had full rank 10, and every kernel vector
   indeed had smaller support.
4. **Hyperplane lemma.** Correct: polarisation on H1, H2; W = K + Qx + Qy; q = 2 alpha gamma beta(x,y); a
   vector of H3 outside H1 union H2 has alpha gamma != 0. Three hyperplanes suffice, the check also shows two
   do not (rank 9).
5. **Four squares (ii).** Complete as written and self-contained: Gamma (norms of nonzero rational rotors) is
   closed under products and inverses; for odd p the two sets {a^2}, {-1 - b^2}, 0 <= a, b <= h, each have
   h + 1 pairwise incongruent elements, so they meet (p + 1 > p); a^2 + b^2 + 1 = mp with 1 <= m < p; m in Gamma
   by induction (m = 1 trivially); p = (mp) m^{-1}. Inverses in Q replace Lagrange's descent. No unstated
   classical fact is used; it rests only on multiplicativity of the quaternion norm (stored). No
   representation theorem for rational quadratic forms, no Hasse-Minkowski: the number-theoretic input is
   derived, not imported or assumed.
6. **Counterexample (iv).** Determinant (u.u)(v.v) - (u.v)^2 = 1 * 7 - 0 = 7 for u = e_1,
   v = (0,1,1,1,2,0,...). I verified the obstruction by a route independent of the quaternion identity: for
   a, b in Q^4, (a.a)(b.b) - (a.b)^2 = sum of the six Pluecker squares, and the Pluecker relation
   p01 p23 - p02 p13 + p03 p12 = 0 turns that into (p01+p23)^2 + (p02-p13)^2 + (p03+p12)^2 (checked on 200
   random rational pairs). Under a similarity with factor c, 7c^2 would be a sum of three rational squares,
   so 7 would be; exhaustive search finds no 7n^2 = a^2+b^2+c^2 for n <= 60, and the mod-8 argument excludes
   all n. So the pair lies in no four-dimensional rational subspace similar to the standard one, in Q^5 and
   hence in Q^8 (padding by zeros). The proof shows exactly this necessity statement; sufficiency is
   correctly marked as argued only.
7. **(vii)** Correct: blocks of size 2^{l-1} >= 4 from l = 3; mu splits as mu_+ + mu_- through the orthogonal
   pair E_+ + 0, 0 + E_-. The l = 2 failure is correct (a {0,1}-valued rational function of one rational
   parameter is constant). This settles the question left open in the stored
   `synthesis.no-two-valued-weights-...` ("whether three suffice is not shown").

### Check
Runs (6 PASS). Perturbations, each caught: v -> (0,1,1,1,1,...) (det 4) fails the det-7 check; sign of B_1
flipped fails (ii); m < p - 100 fails 3 functions; reflection without the factor 2 fails (iii). The check
tests the finite parts as claimed, and its coverage names what is left to the proof.

### Hunt
- Novelty: none claimed. The note explicitly makes no priority claim for the reduction and records that the
  Mushtari 2001 text was not read beyond its abstract. Nothing in the title, one-liner, technical or lay level
  says "new" or "answers Problem G". Licensed. (If a later version wants to say that (v) with (vi) answers
  Mushtari's Problem G for every n >= 4 in signed form, that needs the paper read first.)
- Gleason citation (J. Math. Mech. 6 (1957) 885) is correct as far as I know; flagged from memory anyway.
- Conditional on the stored theorem: stated in (v) and the one-liner ("given the stored theorem for two
  modes"). Fine.

### Fixes
1. Proof (iv): "Clearing denominators, 7n^2 = a1^2 + a2^2 + a3^2 with integers n >= 1, a1, a2, a3 of greatest
   common divisor 1" needs one line: take n minimal (if all a_i are even then 4 | 7n^2, so n is even and
   (n/2, a_i/2) is a smaller solution), or note d^2 | 7n^2 implies d | n.
2. Extraction note and coverage of `check_every_positive_rational_is_the_norm_of_a_rational_rotor` say "every
   integer below 300"; the loop covers 1 to 293. Write "up to 293".

---

## 2. synthesis.under-rp-record-weights-bound-the-chsh-sum-of-correlators-on-two-modes

**Verdict: SOUND WITH FIXES.**

### Hypothesis placement
(RP) is in the title and the one-liner, defined in the formal level as "a hypothesis of this result, not a
premise of the series", and no `assumes` edge is drawn. It is never worded as a premise of the store. Good.

### Is an additivity across non-commuting parts hidden in S = L(C)?
No. S is by definition the sum of four numbers, each kappa(T_ij) = mu(E) - mu(1 - E) for one orthogonal pair
(E_ij, 1 - E_ij) recorded in its own context. Summing four numbers needs no additivity of values. The step
kappa_mu(T) = L(T) uses only that mu is the restriction of a linear L, which the stored two-mode theorem
derives from additivity on orthogonal projectors plus the single-valuedness of mu across contexts. The
assumption that carries the weight is therefore the context independence inside (RP) (one function on all
projectors of Cl_Q(2,2), including the ones that are not products of local outcomes), and the entity states
it in (RP) and in its note ("by the theorem for two modes that is equivalent to (P) on the projectors"). The
Gleason-type theorem is exactly what replaces von Neumann's additivity, and the note credits Bell's criticism
correctly. Nothing is hidden.

### Is the strict inequality proved?
Yes. Record weights are rational-valued by definition; by clause (iv) of the stored theorem mu is the
restriction of a state L; L((C - tau)^2) >= 0 at tau = L(C) gives L(C)^2 <= L(C^2) = 4 + 4L(K), and
(1 - K)^2 = 2(1 - K) gives L(K) <= 1; S rational and 8 not a rational square gives S^2 < 8. Note the
strictness is only irrationality of sqrt 8 (same as the stored bounds over Q); it is proved, and not more
than that.

### Other steps
- (ii) Correct: joint idempotents F_sigma of commuting projectors diagonalise C with rational eigenvalues,
  so C would satisfy a split rational polynomial g; gcd(g, t^3 - 8t) divides t, forcing C = 0. Independent
  check: C^2 = 4 + 4K, C^3 = 8C, and the left-multiplication matrix of C on the 16-dimensional algebra has
  trace 0 and tr L_C^2 = 64, consistent with eigenvalues 0 (x8) and +-2 sqrt2 (x4 each).
- 14/5 at the ray (-1,2,-2,-1): recomputed by my own atom builder, correlators 3/5, 4/5, 4/5, -3/5,
  S = 14/5 (indep2b.py).
- P2's C, A_i, B'_j are literally X_1, Z_1, X_2 = e_2 p_1, Z_2 = p_2 of the stored local-weights result and
  of proposal 3 (verified: P2's C equals P3's C_0).

### Check
Runs (3 PASS). Perturbations: B'_2 = e_2 f_2 instead of f_2 e_2 fails all three; the sign of T_22 in C fails
all three; the state normalised by 5 instead of 4 fails the bound function. (A perturbation 4<Pi x> -> 4<x Pi>
is invisible, as it must be: the scalar part is cyclic.) Weakness to note, not a fix: clause (iii) is tested
only on linear functionals (states of atoms), where S = L(C) is a tautology; the content of (iii) is the
stored theorem, and coverage says so.

### Fixes
1. Formal (RP): "a reading of the residual postulate that weights exist and add" names a stored postulate
   in words only. Add the `\claimref` to the entity that states it
   (`one-relation.measure-indifference-borns-rule-located`, already in `motivated_by`), or drop the phrase.
2. Formal (ii): "The only spectral projector of C with rational coefficients, apart from 0 and 1, is that of
   its kernel" is false as worded if spectral projectors of sets of eigenvalues count: the complement
   (1/8)C^2 = (1/2)(1 + K), the projector of {+2sqrt2, -2sqrt2}, is also rational. Write "the only spectral
   projector of a single eigenvalue with rational coefficients is that of the kernel, 1/2(1 - K); with its
   complement 1/2(1 + K) these are the only rational ones besides 0 and 1".
3. Lay: "the total of the four correlations is below 2.83 with nothing further assumed" should read "with
   nothing assumed beyond that reading", to match the last sentence and the one-liner.
4. Cross-cite proposal 3 (see Overlaps): the note's "what is new" should say that the one-line route
   ((RP) gives a state by the two-mode theorem, then the bound) is the core of (iv), and that the use of
   projectors that are not products of local ones is essential to (RP), as proposal 3 (iv) to (vi) shows.

---

## 3. synthesis.local-records-give-the-chsh-bound-without-positivity-and-reversal-on-one-party-keeps-them

**Verdict: SOUND WITH FIXES** (one clause sentence is overstated and must be narrowed; named hypothesis
missing from the one-liner; one uncited use).

### Certificate (i), verified independently
On l = 3 modes, m = 2, n = 1, with A_0 = 1 - 2E_1 and A_1 = 1 - 2E_2 for rational projectors E_i of party 1's
two-mode algebra (A_0, A_1 neither commute nor anticommute), B_0 = 3/5 X_3 + 4/5 Z_3 and B_1 = Z_3 in the
algebra of the twisted generators gamma e_3, gamma f_3 (gamma = p_1 p_2), the identity
4 + 2t^2 - 2tC = (S - t)^2 F_+ + (S + t)^2 F_- + (D - t)^2 G_+ + (D + t)^2 G_- holds at t = 0, 1, -7/3, 5/2
(degree two in t, so for all t). Observation: the identity itself uses only A_i^2 = 1 and F_+ +- F_- = 1, B_j;
I checked that it still holds with a B_0 from party 1 that does not commute with A_i. Commutation and
self-adjointness are needed only for each term to be yy^dagger. The sentence "The identity uses only that the
four elements are self-adjoint of square 1 and that each A_i commutes with each B_j" is therefore true but
over-lists; harmless (optional fix 5).

### Reversal on one party: well defined and linear
The Preliminaries' bijection argument is correct: a blade a_T of A times an ordered product of r twisted
generators is +-a_T g_R (r even) or +-a_{T^c} g_R (r odd), each blade of Cl(l,l) once. I rebuilt theta for
l = 2 from scratch (solving for the coordinates of each blade in the 16 products A-basis x B-basis and
defining theta(ab) = a b^dagger): rank 16, theta^2 = 1, theta(x^dagger) = theta(x)^dagger on all blades,
lambda_c o theta = lambda_{-c} at c = -1, 1/3, 2. theta is not multiplicative (theta(X_2 Z_2) !=
theta(X_2) theta(Z_2)), and the entity correctly never claims it is. For l = 4 I confirmed X_3, Z_3, X_4, Z_4
lie in the algebra of gamma e_j, gamma f_j (j = 3, 4) with gamma = p_1 p_2.

### Each claim about what lambda^theta preserves
- linear, normalised, real if lambda is, even if lambda is: correct.
- lambda^theta(ab) = lambda(ab) for a in A, b self-adjoint in B: correct.
- palindromic sequences of local self-adjoint idempotents: correct (the B-subsequence of a palindrome is a
  palindrome, hence self-adjoint); checked on a five-step sequence (both give 9/130).
- (CP) preserved, sector averages commute: correct.
- **"Hence lambda^theta and lambda have the same values on every product of local observables": overstated.**
  It holds for a product with one local observable of party 2 (or any palindrome of them), not for products
  with two non-commuting observables of party 2. Counterexample in the entity's own notation:
  X_1 Z_1 X_2 Z_2 is a product of four local observables and equals -K; lambda_{-1} gives 1, its reversal
  lambda_1 gives -1 (theta negates it). The stored `synthesis.local-weights-...` states the same fact
  (K = -(X_1 Z_1)(X_2 Z_2) is a product of one anti-self-adjoint element of each party). The same overstatement
  is in the technical level ("with the state's values on every product of local observables"). It also makes
  clause (vii) read oddly: K is already a product of local observables without I_4; what (vii) adds is that
  with I_4 it is a product of one self-adjoint element per party.
- (v): lambda_1 weights -1/2, 1/2, 1/2, 1/2 on the joint outcomes of U, V recomputed; two-copy formula
  (1/16)(1 + ss' + tt' + ss'tt' c^2) recomputed at c = 1/2, 3, -2 and all 16 sign choices; correct.
- (vi): instance recomputed (u self-adjoint, u^2 = 1, carries the local atom to 1/4(1+U)(1+V); weights 1/4,
  -1/2 for lambda_1 and 1/4, 0 for lambda_{-1}). The general equivalence (orbit of one atom, density of a
  norm class via rotors, continuity of a quadratic form) is correct.
- (iii) checked step by step: E -> mu(EF) is an additive weight on party 1's algebra, which is literally
  Cl_Q(2,2) with its own adjoint, so the stored theorem applies; L_F(s^2) >= 0 by the column decomposition;
  marginal consistency gives L_{F+} + L_{F-} = L_1 on self-adjoint elements; the sum is 4 + 2t^2 - 2tV.
  Correct. Note it needs m = 2 (party 1 of two modes); for m = 1 the two-mode theorem is not available.
- (ii), (L) implies (CP): density of the k-points of the unit circle and linearity of g give
  |g| <= w nu; correct.

### Statements about stored premises
The only one is Reading (b) on `one-relation.recording-irreversible-stated-so-it-can` and
`one-relation.recorded-sectors-superselected-premise`, and it is labelled "is a reading" inside a Reading
headed "argued, not proved". Compliant. Reading (c) "(P) is independent of the conditions on local records"
is also inside the argued Reading. Good.

### Check
Runs (6 PASS). Perturbations: c^2 -> c in the two-copy formula fails (v); outcome projector built from b_0 for
all four terms fails (i) and (iii); s with an extra A_0 A_1 term fails (i) and (iii).

### Fixes
1. Formal (iv), and the technical level: replace "Hence lambda^theta and lambda have the same values on every
   product of local observables" by "Hence lambda^theta and lambda have the same values on every product ab of
   an element of A with one local observable b of party 2 (in particular on every product of one local
   observable of each party); they can differ on products with two observables of party 2 that do not commute,
   for example (X_1 Z_1)(X_2 Z_2) = -K in (v)". Same in the technical level. The lay sentence ("agrees ... on
   everything the two can record separately") is fine because records are the palindromes.
2. Named hypothesis (CP) is in no title or one-liner. The one-liner gives its content in words; add the name:
   "... so non-negative values of one party given the other's outcomes (Hypothesis (CP)) give
   lambda(C)^2 <= 8 ...". Title could stay, but "Local records bound CHSH" is only true under (CP) or the
   conditions of (iii); consider "Under (CP), local records bound CHSH without (P) ...".
3. Proof (v) uses `synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values` clause
   (iv) ("the cited Theorem, clause (iv)") for the weights 1/4(1 - u - v - cuv), and the formal says "of which
   exactly lambda_{-1} satisfies (P)", with no uses edge (deliberately, since that result holds given (P)).
   Either prove the two facts needed directly (lambda_{-1} = 4<P_s x>_0 with P_s an atom is a state; the four
   weights are a four-term scalar-part computation, already in the check) and mark "exactly" as recalled for
   comparison, or draw the edge. As written it is an uncited use.
4. (vii) and Reading (d): say "a product of one self-adjoint element of each party" rather than "a product of
   local observables" (see fix 1; without I_4 it already is a product of four local observables).
5. Optional: (i) "The identity uses only ..." should say the identity uses only A_i^2 = 1, and the yy^dagger
   form uses self-adjointness and the commutation.

---

## Overlaps and conflicts

- **Proposals 2 and 3 do not duplicate, but they overlap at one point and should cross-cite.** Both bound
  the CHSH value at the same element (P2's C is P3's C_0: same settings X_1, Z_1, X_2 = e_2 p_1, Z_2 = p_2,
  same K = e_1 f_2, verified) without assuming positivity of a linear functional on the whole algebra. The
  hypotheses differ:
  - P2, (RP): non-negative, context-independent rational weights on **every** projector of Cl_Q(2,2), including
    projectors that are not products of local outcomes; linearity then comes from the stored two-mode theorem.
    Setting: two modes, one per party. By that theorem (RP) equals (P) on projectors, so P2 is in substance
    "(RP) gives a state, a state gives the bound", plus genuinely separate content: (ii) (C is not a
    combination of commuting rational projectors) and the reading of what of (P) is still a convention.
  - P3, (CP) or (iii)'s record conditions: non-negativity only on one party's squares times the other party's
    outcomes; no non-local projector is used; (iii) needs party 1 to hold two modes (so at least three modes
    in all) and does not cover P2's two-mode setting. P3's note already states P2's route in one sentence
    ("under that reading the weights on two modes are the restriction of a state ..., which gives the bound at
    once").
  - Consistent, not conflicting: P2 (v) says the box functional is non-negative on the sixteen joint outcomes
    and fails the sign elsewhere; P3 (ii) locates where: -1/2 on each of the four certificate elements s^2 F.
    P3 (iv) to (vi) show that the non-local projectors in (RP) are exactly what separates a state from its
    reversal, which sharpens P2's own note ("the hypothesis is strong").
  Recommendation: keep both, separately. P2 should cite P3 (iv) to (vi) for why (RP) must include projectors
  that are not products of local ones, and P3's sentence on "the reading that every projector ... can label a
  record" should cite P2 by id. No merge: different hypotheses, different settings (two modes vs a party of
  two modes), and P3 contains the reversal results that P2 lacks.
- **Proposal 1 and proposal 2.** P2's note says the general-mode version holds "once the theorem on additive
  weights is available there (it is not stored at this version)". P1 is that theorem. If P1 is accepted, P2's
  note can say its (iii) and (iv) extend to commuting pairs of square-one self-adjoint elements in any number of
  modes via P1; P2 should not be changed to rest on P1 unless it actually uses it.
- **Proposal 1 and proposal 3.** P3 (iii) uses the stored two-mode theorem on party 1's algebra, hence needs
  m = 2 exactly. With P1, (iii) extends to every m >= 2 (party 1's algebra Cl_Q(m,m) is Mat_{2^m}(Q)), which P3
  could note as a remark; P3's "Not done" does not mention it.
- **P1 clause (vii) and the stored `synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them`.**
  P1 answers the stored entity's open sentence ("whether three suffice is not shown here"): three modes
  suffice for the even subalgebra. Not a conflict; the stored entity's reading could cite P1 after acceptance.
- No contradictions found among the three proposals or with the stored results they cite.
