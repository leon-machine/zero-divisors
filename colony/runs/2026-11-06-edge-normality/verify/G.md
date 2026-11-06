# Referee G (algebra), run 2026-11-06-edge-normality

Blind referee. Read: REFEREE.md, BRIEF.md "Role: referee", the three proposals, their check4 logs, and the
store entities they cite or that the brief names. Not read: findings/, work/, RUN.md, scalars-context.md, other
referee reports. Own scripts and perturbed copies: `verify/work-G/` (perturb.py applies one textual change to a
copy of a check and runs runcheck on it; own_*.py are my independent recomputations). Each check was run once
with `colony/runcheck.py` (all PASS, as in the check4 logs: 0 errors, 0 findings).

## 1. synthesis.blade-square-signs-f2-quadratic-form

**Verdict: SOUND WITH FIXES.** The mathematics of (i) to (v) is correct, but clauses (ii) to (iv) are a
published result that the entity does not cite, the lay level contains a false statement about the anisotropic
plane, and clause (i)'s closing sentence says less than it seems to.

### What I checked and how
- Premises at pinned versions: std-algebra.orthogonal-anticommute@1 (blade product e_I e_J = +/- prod Q e_{I xor J}),
  transport.classification-real-clifford-algebras@3 (the d-table), primer.sign@2 (omega^2), tower.commuting-copies@5
  (twisted generators x Omega_k, Cl(p+k,q+k) = Cl(p,q) (x) Mat(R)), tower.rigidity-clock-frozen@5 (division-ring type
  constant along the tower). Each says what the proof uses.
- Proof steps, by hand: (ii) q(S) = C(|S|,2) + |S cap N|, b(S,T) = |S||T| + |S cap T|, polar identity from
  (e_S e_T)^2 = (-1)^b e_S^2 e_T^2: correct. (iii) radical: correct. (iv) (-1)^C(k,2) = <(1 - j) j^k>_0 for k = 0..3 and
  period 4; values <(1 - j)(1 + j)^s>_0 = 1, 2, 2, 0, -4, -8, -8, 0 and <(1 + j)^t>_0 = 1, 1, 0, -2, -4, -4, 0, 8
  recomputed by hand; the table follows for both signs of r. (v) omega = ef, omega^2 = 1, (x_i omega)^2 = x_i^2, x_i omega
  commutes with e and f; q_(1,1) = (0, 0, 1, 0), Gauss sum 2: correct.
- Check perturbations (all made the check FAIL, as they should):
  `TYPE[2] = "H"` fails check_radical_gauss_sum_and_type; closed form `k(k+1)/2` in place of `k(k-1)/2` fails
  check_blade_signs_are_a_quadratic_form; untwisted ground generators (no omega) fail check_ascent_adds_a_hyperbolic_plane;
  `(1 + j)` in place of `(1 - j)` as the first factor fails check_radical_gauss_sum_and_type.
- Own route (work-G/own_p1.py): the Gauss sum sum_S e_S^2 is the signature of the trace form x -> <x^2>_0, which is
  diagonal in the blade basis. From the matrix models alone, that signature is +k on Mat_k(R), 0 on Mat_k(C) and -2k on
  Mat_k(H) (symmetric versus antisymmetric, Hermitian versus anti-Hermitian parts). With k fixed by dimension this
  reproduces the proposal's table exactly for all 119 signatures with n <= 14, and agrees with the closed-form count
  and with Re[(1 - i)(1 + i)^p (1 - i)^q] in the Gaussian integers. Arf by majority equals 1 exactly for p - q = 4, 6
  (mod 8), even n <= 12. GA squares agree with the closed form for n <= 6.
- Literature (WebSearch/WebFetch, abstracts and first pages read): V. Ovsienko, "Real Clifford algebras and quadratic
  forms over F_2: two old problems become one", arXiv:1601.07664, realises Cl(p,q) as a twisted group algebra of F_2^n,
  proves that Cl(p,q) and Cl(p',q') are isomorphic iff the associated F_2 quadratic forms are equivalent, and says the
  difference between real and quaternionic matrices is measured by the Arf invariant. A. Elduque and A. Rodrigo-Escudero,
  "Clifford algebras as twisted group algebras and the Arf invariant", arXiv:1801.07002, DOI 10.1007/s00006-018-0862-y
  (Adv. Appl. Clifford Algebras, 2018), revisits real Clifford algebras through the Arf invariant of the associated F_2
  form. I could not confirm a journal reference for Ovsienko's paper, nor whether either paper uses the Gauss-sum or
  trace-form formula; I did not check the Salingaros, Lounesto or Quillen citations.

### Problems found
1. **Uncited prior art for (ii) to (iv).** The extraction note says (i) to (iv) are transport-absent and a
   reformulation of the classification, which is right, but the two papers that state exactly this (F_2 quadratic
   form, polar form = commutator, Arf invariant separating real from quaternionic) are not cited; the cited ones
   (Salingaros, Lounesto, Arf, Quillen) are "from memory". The Gauss-sum formula is the trace-form signature, also
   classical.
2. **False lay sentence.** "while adding a pair of directions that both square to minus one switches between the real
   and quaternionic kinds" is false: Cl(2,0) = Mat_2(R) goes to Cl(2,2) = Mat_4(R), and Cl(0,2) = H goes to
   Cl(0,4) = Mat_2(H) (own GA computation, work-G/own_p1_lay.py: Arf 0 -> 0 and 1 -> 1). The reason: the twist by the
   volume element of an anisotropic plane, which squares to -1, sends x_i to x_i omega with (x_i omega)^2 = -x_i^2, so
   Cl(p,q+2) carries q_(q,p) (perp) q_(0,2), not q_(p,q) (perp) q_(0,2). The formal (v) only states Arf(q_(0,2)) = 1, which
   is true; the technical paragraph's "while the anisotropic plane ... carries Arf invariant 1", placed after "the type
   never changes up the tower", invites the same misreading.
3. **Clause (i) is thinner than its wording.** Under its own hypotheses (relation for all i != j, both orders) c^2 = 1
   is already forced, so the "Moreover" (x_i^2 commutes with x_j iff c^2 = 1) is automatically true, and the closing
   "anticommutation of distinct directions and centrality of their squares are one condition" is not what was shown:
   centrality of the squares is equivalent to c^2 = 1 (c = +1 or -1), and c = -1 needs the separate input c != 1 (and
   char k != 2, else c = -1 = 1). The content that is not trivial is the one-relation (quantum-plane) statement the check
   actually tests: with only x_1 x_2 = c x_2 x_1 imposed, x_1^2 is central iff c^2 = 1.
4. **Minor proof gap in (iv), r < 0.** t = |r| + 1 runs over 1..8 modulo 8, but only t = 0..7 is tabulated; add
   "(1 + j)^8 = 16, so the values repeat with a factor 16 per period".
5. **(v) duplicates stored results.** The type statement is tower.rigidity-clock-frozen; the isometry is
   tower.commuting-copies at k = 1 read in F_2 language. The proposal says so (transport-convenient); fine as a corollary.

### Exact fixes
- extraction.note: add "Clauses (ii) to (iv) are stated and proved in V. Ovsienko, arXiv:1601.07664 (Cl(p,q) as a
  twisted group algebra of F_2^n; isomorphism iff the F_2 forms are equivalent; Arf invariant separates real from
  quaternionic) and A. Elduque, A. Rodrigo-Escudero, Adv. Appl. Clifford Algebras (2018), arXiv:1801.07002; the
  Gauss sum sum_S e_S^2 is the signature of the trace form x -> <x^2>_0, +k, 0, -2k on Mat_k(R), Mat_k(C), Mat_k(H)."
  Add tag or wording "classical, restated".
- lay: replace the last sentence by "Adding a pair of directions of opposite type, the basic step the series uses to
  repair division, never changes that answer; adding two directions that both square to minus one is different,
  because it also swaps the roles of the existing positive and negative directions."
- technical, last sentence: replace "while the anisotropic plane $(0,2)$, whose algebra is the quaternions, carries
  Arf invariant $1$" by "while the anisotropic plane $(0,2)$, whose algebra is the quaternions, carries Arf invariant
  $1$; adding it is not an orthogonal sum with the ground form, since the twist by its volume element, of square $-1$,
  exchanges $p$ and $q$: $\Cl(p, q{+}2)$ carries $q_{(q,p)} \perp q_{(0,2)}$." Same sentence appended to formal (v).
  (Check: one line, e.g. assert Arf(q_(2,2)) == Arf(q_(0,2) (perp) q_(0,2)) == 0 != Arf(q_(2,0)) + 1.)
- formal (i): replace the last two sentences by "Moreover, if only the single relation $x_{1}x_{2} = c\,x_{2}x_{1}$ is
  imposed ($c \ne 0$), then $x_{1}^{2}x_{2} = c^{2}x_{2}x_{1}^{2}$, so wherever $x_{2}x_{1}^{2} \ne 0$ the square
  $x_{1}^{2}$ commutes with $x_{2}$ exactly when $c^{2} = 1$. Over a field of characteristic other than $2$, with
  $c \ne 1$ this gives $c = -1$: the symmetry of the relation and the centrality of the squares each force
  $c \in \{1, -1\}$." Or drop (i) as a remark; it is a two-line classical observation.
- proof (iv): after the t-table add "and $(1 + j)^{8} = 16$, so for $|r| + 1 \ge 8$ the value is $16^{m}$ times the
  tabulated one".

## 2. synthesis.hyperbolic-plane-integral-orders-and-partner-inverse

**Verdict: SOUND WITH FIXES.** Every clause is correct. Clause (iii) duplicates three stored entities, one of
which (singularity.pseudo-inverse-identities-hyperbolic-atom) the proposal does not name; clause (iv) and the
dual-number half of (v) duplicate clause (i) of synthesis.limits-as-null-steps; (i) and (ii) are classical
(Clifford algebra of the hyperbolic Z-module = Mat_2(Z); of <1, -1> over Z = an index-4 non-maximal order); the
lattice sentence in (ii) mixes two normalisations.

### What I checked and how
- Premises at pinned versions: std-algebra.witt-basis-car@1 (null pairs obey the CAR, N = wv idempotent with
  N + vw = 1), std-algebra.cl11-matrix@1 (Cl(H) = Mat_2(R) with u, w the off-diagonal matrix units, uw, wu the
  diagonal idempotents), one-relation.two-presentations@4, transport.regularity-localises-zero-divisors-idempotents@2
  (nondegenerate real Clifford algebras are von Neumann regular), std-algebra.radical-ideal-and-quotient@1,
  conformal.minimal-nondegenerate-completion@6 (Cl(p,q,r) embeds in Cl(p+r,q+r)). Each supports the step it is cited
  for. Note: (v) says the completion is regular "by (iii) and Lemma ...": the Lemma alone gives it.
- Proof steps by hand: word reduction in a, a'; matrix units; e+ = a + a', e- = a - a', e+e- = a'a - aa'; the span
  of 1, e+, e-, e+e- is {[[A,B],[C,D]] : A = D, B = C mod 2}, index 4; x^2 for x = alpha + beta e+ + gamma e- + delta e+e-
  is (alpha^2 + beta^2 - gamma^2 + delta^2) + 2 alpha (rest), so a nontrivial idempotent has alpha = 1/2; nmn = n,
  mnm = m; dagger is an anti-automorphism exchanging a and a'; f(x + n) = f(x) + f'(x) n incl. the quotient rule;
  rho x rho = 0. All correct. For (v) the cleaner argument is that a radical vector anticommutes with every vector
  and squares to 0, so rho x rho = +/- x rho^2 = 0 for every product x of vectors; the blade argument as written
  presumes rho is a basis vector (harmless: any nonzero radical vector extends to an orthogonal basis).
- Check perturbations (all FAIL as they should): dagger replaced by plain reversion fails
  check_partner_is_a_generalised_inverse; `abs(det(change)) == 2` fails the index check; f'(5) = 154 in place of
  155 fails check_derivative_through_the_partner; the orthogonal basis replaced by the Witt basis fails
  check_orthogonal_order_has_index_four_and_no_idempotents (it then finds idempotents); Cl(p,q+r) in place of the
  degenerate Cl(p,q,r) fails check_radical_vector_has_no_generalised_inverse.
- Own route (work-G/own_p2.py), plain integer 2x2 matrices, no GA: membership in Lambda_O is exactly A = D, B = C
  (mod 2) on a box; Lambda_O hits 4 of the 16 residues mod 2, so index 4; no nontrivial idempotent (trace of a
  nontrivial idempotent is 1, trace on Lambda_O is 2 alpha, even); the box count of nontrivial idempotents of Lambda_W
  with Witt coordinates in {-1, 0, 1} is 10, each of scalar part 1/2 (also by hand: trace 1 and det 0 force
  (s, d) = (0, 1) or (1, -1) and bc = 0, 5 + 5); dagger is the transpose under the matrix map (e+ symmetric, e- and its
  sign flip antisymmetric), so (iii) is the textbook Moore-Penrose inverse of E_12.
- Observation for (iv): any generalised inverse g of n (n g n = n) gives g(f(x + n) - f(x)) = f'(x) gn with gn
  idempotent (checked on a box); the partner is the choice for which the idempotent is dagger-self-adjoint. So (iv) is
  not specific to the partner, and is the dual-number expansion multiplied on the left by any generalised inverse.
- Literature: not web-verified. The Bass/Knus statement (Clifford algebra of a hyperbolic module is End of the
  exterior algebra of a Lagrangian) and Reiner (Mat_n(Z) maximal in Mat_n(Q)) are standard and the entity says they
  are cited from memory and unused; I did not check page-level references.

### Duplicates against the store
- (iii) first sentence = singularity.pseudo-inverse-identities-hyperbolic-atom@4 (v v* v = v, v* v v* = v*, with the
  same v = (e_0 + e_1)/2, v* = (e_0 - e_1)/2 in Cl(1,1)) plus std-algebra.witt-basis-car (the complementary idempotents);
  (iii) second sentence = note.transport.setting-hyperbolic-atom-matrix-algebra-moore (Moore-Penrose with transpose) and
  descent-lift.pairing-creator-under-transport-algorithm (ii). The entity cites the last two but not the first.
- (i) = std-algebra.cl11-matrix restricted to integer coefficients (same matrix units).
- (iv) and the expansion in (v) = synthesis.limits-as-null-steps (i) under rho -> n, then multiplied by m.

### Exact fixes
- (ii), replace "the two presentations of the one relation are the same over $\Z[\tfrac12]$ and differ over $\Z$ as a
  unimodular quadratic form and a unimodular bilinear form" by "the two presentations agree over $\Z[\tfrac12]$; over
  $\Z$ the null lattice with the polar form is the even unimodular lattice $\mathrm{II}_{1,1}$ (the hyperbolic quadratic
  module, nonsingular), while the orthonormal lattice is unimodular only for the half-polar form $B$, the odd lattice
  $\mathrm{I}_{1,1}$, and as a quadratic module it is singular at $2$ (polar determinant $-4$)". Same change in the
  technical level ("two different unimodular lattices" -> "an even and an odd unimodular lattice, in the polar and the
  half-polar normalisation respectively").
- (iii): add Proposition \claimref{singularity.pseudo-inverse-identities-hyperbolic-atom} to `uses` and to the proof
  ("the first statement is ..."), and to the extraction note's list of restated results; better, shorten (iii) to a
  pointer, since it adds only "for every Witt pair of any Clifford algebra", which is the same two-line computation.
- (iv): add after the display "The same holds with $m$ replaced by any generalised inverse $g$ of $n$, with $gn$ in
  place of $P$; the partner is the choice for which the idempotent is $\dagger$-self-adjoint." Lay "acts as its best
  available inverse" is fine given the Moore-Penrose reading.
- (v), proof: "that algebra is regular by Lemma \claimref{transport.regularity-localises-zero-divisors-idempotents}"
  (drop "(iii) and"); replace the blade argument by "a radical vector anticommutes with every vector and squares to
  $0$, so $\rho x \rho = \pm x\rho^{2} = 0$ for every product $x$ of vectors".
- extraction note: replace "What is new against the store is (i), (ii) and (iv)" by "New to the store, classical in
  the literature: (i), (ii); (iv) is the dual-number expansion of synthesis.limits-as-null-steps (i) read through the
  partner".

## 3. synthesis.limits-as-null-steps

**Verdict: OVERSTATED.** The exact identities (i) to (iv) are correct and the checks are exact (no floats; the
nested-root field is implemented as iterated quadratic extensions). But the title, one-liner, technical and lay
levels say that limits of analysis become identities; what is proved is that the formal derivative of a rational
function and the exponential of a nilpotent element (a finite polynomial) are algebraic identities. No limit is
removed: the bracketing of pi in (iv) still uses sin < id < tan and the exponential chart, which the proposal itself
says. In addition the proof of (iii) misuses a citation and conflates two reversions, the extraction note's
"correction to the source" is wrong as a general statement, and (iv), (v) are not about null steps at all.

### What I checked and how
- Premises at pinned versions: std-algebra.radical-ideal-and-quotient@1 (rho^2 = 0; J^2 = 0 for r = 1), std-algebra.
  witt-basis-car@1 (orthogonal null vectors anticommute and square to 0), std-algebra.bivector-exponential@1 (e^A for
  A in Cl^2 with A^2 scalar). The last is used correctly in (iv) (R_k = exp(theta_k I)) but not in (iii): dB =
  s rho_1 rho_2 e_t e_r is of grade 4, outside the proposition's hypothesis; the series stops simply because
  (dB)^2 = d^2 B^2 = 0.
- Proof steps by hand: (i) quotient rule over the dual numbers: correct. (ii) eps^k = k! e_k(b) for commuting
  square-zero b_i, product expansion: correct; realisations in Cl(0,0,2N) and Cl(2N,2N): correct. (iii) B l+ = -l+,
  l+ B = l+, so R l+ = (alpha - beta) l+ = l+ (alpha - beta B) for scalar alpha, beta: correct; R^2 = 5/4 + 3/4 B gives
  factors 1/2 and 2: correct (R itself has entries 3/(2 sqrt 2), 1/(2 sqrt 2), only R^2 enters). (iv) (1 + R)^2 =
  2(1 + c) R, c_{k+1}^2 = (1 + c_k)/2, r_{k+1}^2 = 2 + r_k, the harmonic-mean and geometric-mean steps of Archimedes:
  all correct; 4^k (U_k - L_k) -> pi^3/8 from tan - sin = theta^3/2 + O(theta^5): correct.
- The reversion in (iii). The proof plugs beta = d/2 into "R l+ R~ = (alpha - beta)^2 l+", which was derived with
  R~ = alpha - beta B for scalar beta. In Cl(1,1,2) the reversion of R = 1 + (1/2) dB is R itself (dB has grade 4), and
  then R l+ R~ = l+, no scaling (GA, own computation). The formal statement avoids this by writing exp(-dB/2), the
  inverse, and the check computes exactly that, so the displayed identity is right; but exp(dB/2) is not a rotor of
  Cl(1,1,2) (R R~ = 1 + dB), and "boost of nilpotent rapidity" is a boost of Cl(1,1) over the ring R[d]/(d^2) with
  R[d]-linear reversion.
- Check perturbations (all FAIL as they should): anticommuting steps b_i = rho_i fail
  check_product_of_null_steps_is_the_exponential; 1/k in place of 1/k! fails the same; r_{k+1}^2 = 3 + r_k fails
  check_half_angle_rotors_and_archimedes; the arithmetic mean in place of the harmonic mean fails the same; (1 + d) in
  place of (1 - d) on l+ fails check_boost_scales_the_null_vector.
- Own route (work-G/own_p3.py): independent float values L_6 = 3.14128, U_6 = 3.14222, 4^6 (U_6 - L_6) = 3.8764,
  pi^3/8 = 3.8758 (proposal: 3.876; illustration only). Tan coefficients recomputed by my own power-series inversion to
  degree 61: all denominators odd, and the 2-adic valuation of the x^(2n-1) coefficient equals s_2(n) - 1 (binary digit
  sum minus 1) for every n checked, which is what von Staudt-Clausen gives for all n (coefficient
  2^(2n)(2^(2n) - 1)|B_2n|/(2n)!, v_2(B_2n) = -1, v_2((2n)!) = 2n - s_2(n)); the degree-21 denominator
  194896477400625 = 3^9 5^4 7^3 11 13 17 19 confirmed.
- The "correction to the source" (extraction note): "N commuting square-zero products of pairs of orthogonal null
  vectors need 2N mutually orthogonal null vectors, so Cl(2N,2N), not Cl(N,N)". True for steps that are products of
  disjoint pairs from one mutually orthogonal null family, false as a statement about Cl(N,N): with Witt pairs
  v_i, w_i of Cl(N,N) and parities pi_j = v_j w_j - w_j v_j, the Jordan-Wigner steps b_i = v_i pi_1 ... pi_{i-1} commute,
  square to 0, have nonzero product, and satisfy prod(1 + b_i) = exp(sum b_i); verified exactly in GA for N = 2 and 3
  (own_p3.py). (Equivalently Cl(N,N) = Mat_2(R)^(x)N with b_i = E_12 in the i-th factor.) Whether the source meant
  products of null pairs I cannot tell blind; the formal (ii) itself only claims existence in Cl(2N,2N), which is true.

### The true weaker statement, level by level
- title: "Nilpotent steps: dual-number derivative, nilpotent exponential and nilpotent boost" (and move (iv), (v) out).
- one-liner: "For a square-zero step the first-order expansion is exact: $f(x + \rho) = f(x) + f'(x)\rho$ for rational
  $f$ in $\Cl(0,0,1)$; for commuting square-zero $b_{i}$, $\prod(1 + b_{i}) = \exp(\sum b_{i})$, a finite sum (realised by
  orthogonal null vectors in $\Cl(2N,2N)$, or by twisted null vectors already in $\Cl(N,N)$); and over $\R[d]/(d^{2})$ a
  boost of rapidity $d$ scales a null vector by $1 - d$. No limit is removed: derivatives of non-rational functions and
  the exponential of a non-nilpotent element still need analysis."
- technical, first sentence: "Several limits of analysis are exact identities once the small step is a nilpotent
  element" -> "The first-order truncations behind two limits of analysis, the derivative and the exponential, are
  exact identities when the step is nilpotent; this covers rational functions and nilpotent arguments only."
- lay: "using one of them as the step makes the shrinking unnecessary" -> "using one of them as the step gives the
  derivative of any formula built from arithmetic, and the exponential of such a step, exactly; for other functions,
  and for the number pi, a limit is still needed".

### Exact fixes besides the restatement
- (iii) proof: replace "by Proposition \claimref{std-algebra.bivector-exponential} (the series stops)" by "since $d$ is
  central with $d^{2} = 0$, $(dB)^{2} = 0$ and the series stops", drop std-algebra.bivector-exponential from the
  premises of check_boost_scales_the_null_vector, and add to the formal statement: "here $d$ is a scalar of the ring
  $\R[d]/(d^{2})$, and $\exp(-\tfrac12 dB)$ is the inverse of $\exp(\tfrac12 dB)$; the reversion of $\Cl(1,1,2)$ fixes
  the grade-$4$ element $dB$, and conjugation by $R$ and $\widetilde{R}$ with that reversion leaves $l_{\pm}$ fixed".
  In the proof, compute directly: $(1 + \tfrac12 dB)\,l_{+}(1 - \tfrac12 dB) = (1 - \tfrac12 d)^{2}l_{+} = (1 - d)l_{+}$.
- extraction note, the correction: replace by "Products of disjoint pairs from one family of mutually orthogonal null
  vectors need $2N$ such vectors, so $\Cl(2N,2N)$; with Jordan-Wigner twisted null vectors
  $b_{i} = v_{i}\pi_{1}\cdots\pi_{i-1}$, $\pi_{j} = v_{j}w_{j} - w_{j}v_{j}$, $N$ steps with nonzero product already exist in
  $\Cl(N,N)$." Optionally add this realisation to (ii) and the check (the code in work-G/own_p3.py, part (a), is ten
  lines).
- extraction note: "the bounds on pi and the rate of the gap are numerical" -> "are proved from the classical
  inequalities $\sin\theta < \theta < \tan\theta$ and the Taylor expansion of $\tan - \sin$ (imported), and illustrated
  numerically; the check does not cover them". House rule: the import should be a Fact with provenance or stated as
  imported in the proof.
- (v): either drop it (it is not about null steps and not used), or state it for all degrees: "every Taylor
  coefficient of $\tan$ at $0$ has odd denominator, its $x^{2n-1}$ coefficient having 2-adic valuation $s_{2}(n) - 1$"
  with von Staudt-Clausen imported, and checked to degree 21. "checked to degree 21 only" for a classical all-degree
  fact undersells and invites the reader to think it open.
- (iv): move to its own note (half-angle rotors and Archimedes' recursion), ledger transport-absent; it shares nothing
  with nilpotent steps except the theme of the source document.

## Overlaps and conflicts

- **Proposal 2 (iv), (v) and proposal 3 (i) state the same identity**: $f(x + \rho) = f(x) + f'(x)\rho$ for rational
  $f$ over the dual numbers, with the same test function $(x^{3} + 3x)/(x^{2} + 1)$ and the same hand values in both
  checks. Proposal 2 adds only the left multiplication by the partner and the map $\rho \mapsto a$. One home: proposal
  3 (i) for the expansion; proposal 2 should cite it and keep only the partner reading (and, per my fix, note that any
  generalised inverse works).
- **Proposal 2 (v) and proposal 3 (ii)** both lean on the degenerate algebra and the completion: proposal 3's
  Cl(0,0,2N) versus Cl(2N,2N) is the same "degenerate step realised by null vectors after the ascent" reading as
  proposal 2 (v). Not a conflict; should cross-reference.
- **Proposal 1 (v) and proposal 2** both use the (1,1) plane with Q(e) = 1, Q(f) = -1, but proposal 1 names it
  e, f, omega = ef and proposal 2 e_+, e_-, a, a'. Consistent conventions (same signs); no conflict.
- **Proposal 1 lay versus proposal 1 formal**: the lay claim that a (0,2) plane switches real and quaternionic
  contradicts the classification (counterexamples above); the formal level does not claim it.
- **Duplicates of stored entities**: proposal 1 (v) = tower.commuting-copies (k = 1) + tower.rigidity-clock-frozen in
  F_2 language; proposal 2 (iii) = singularity.pseudo-inverse-identities-hyperbolic-atom + std-algebra.witt-basis-car +
  note.transport.setting-hyperbolic-atom-matrix-algebra-moore + descent-lift.pairing-creator-under-transport-algorithm
  (ii); proposal 2 (i) = std-algebra.cl11-matrix over Z. Nothing in the three overlaps
  transport.regularity-localises-zero-divisors-idempotents beyond citing it, one-relation.two-presentations beyond
  refining it over Z, or synthesis.plane-commutant-even-ground (which classifies by the commutant, not by the F_2
  form; the two are compatible: both see the class of r only through the type).
- **Novelty against the literature**: all three are classical in substance. Proposal 1 (ii) to (iv) is in Ovsienko
  (arXiv:1601.07664) and Elduque and Rodrigo-Escudero (arXiv:1801.07002), uncited. Proposal 2 (i), (ii) are the
  Clifford algebras of the hyperbolic Z-module and of <1, -1> over Z (cited, from memory). Proposal 3 is dual numbers,
  the nilpotent exponential, the half-angle formula and Archimedes (cited, from memory). Proposals 1 and 3 label
  themselves transport-absent for these parts; proposal 2's "new against the store" is accurate only as "new to the
  store".

## Recommendation

| id | store? |
|---|---|
| synthesis.blade-square-signs-f2-quadratic-form | Store entity, after the fixes: one claim holding (ii) to (iv) as a cited classical restatement plus (v) as the transport-convenient corollary; (i) dropped or a remark. |
| synthesis.hyperbolic-plane-integral-orders-and-partner-inverse | Not a separate claim. (i), (ii) as a note (remark) on one-relation.two-presentations ("the two presentations differ over Z"); (iii) dropped as a duplicate; (iv), (v) merged into the narrowed proposal 3. |
| synthesis.limits-as-null-steps | Narrowed claim (i) to (iii) under the new title, absorbing proposal 2 (iv) and the radical-vector part of (v) and the Cl(N,N) realisation; (iv) and (v) to a separate note or dropped. |

## Summary

| id | verdict | one-line reason |
|---|---|---|
| synthesis.blade-square-signs-f2-quadratic-form | SOUND WITH FIXES | Correct throughout (my own trace-form-signature route reproduces the table for n <= 14), but (ii) to (iv) are published (Ovsienko; Elduque and Rodrigo-Escudero) and uncited, the lay claim that a (0,2) plane switches real and quaternionic is false (Cl(2,0) -> Cl(2,2) stays real), and (i)'s closing sentence overreads a two-line fact. |
| synthesis.hyperbolic-plane-integral-orders-and-partner-inverse | SOUND WITH FIXES | Correct; (iii) duplicates singularity.pseudo-inverse-identities-hyperbolic-atom (uncited) and two other stored items, (iv)/(v) duplicate proposal 3 (i), the lattice sentence mixes the polar and half-polar normalisations (II_{1,1} versus I_{1,1}), and (i)/(ii) are classical. |
| synthesis.limits-as-null-steps | OVERSTATED | Identities exact and checks exact, but no limit is removed (rational derivatives and nilpotent exponentials only; pi still needs analysis); (iii) misapplies bivector-exponential and the R~ formula (Cl(1,1,2) reversion fixes dB); the "Cl(2N,2N) not Cl(N,N)" correction is false in general (Jordan-Wigner steps in Cl(N,N)); (iv), (v) are unrelated to null steps. |
