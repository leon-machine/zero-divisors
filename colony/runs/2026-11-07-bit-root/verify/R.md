# Referee R report, run 2026-11-07-bit-root (the reals)

Blindness kept: I did not open `findings/`, `work/`, RUN.md or the other referee's report. I read the five
proposals, the store entities they cite (at the pinned versions), the gate's validate logs, and ran the two
checks once each plus perturbed copies in `verify/work-R/`. check4 was not rerun.

Side effect, reported: my two `runcheck.py` runs left `__pycache__/check.cpython-313.pyc` inside
`proposals/synthesis.completion-recovers-the-real-clifford-algebras/` and
`proposals/synthesis.frobenius-and-universality-in-clifford-algebras/`; I removed both directories, so those
proposal folders are as filed. (The `__pycache__` folders in the division and signed-directions proposals
predate my runs and are not mine.)

## Summary

| id | verdict | one-line reason |
|---|---|---|
| synthesis.continuum-completion-premise | SOUND WITH FIXES | Exact, labelled mathematical, assumes neither uniqueness nor Ostrowski; but says odd-degree roots and Frobenius "use completeness" where a real closed field suffices. |
| synthesis.completion-recovers-the-real-clifford-algebras | SOUND WITH FIXES | Every step re-derived and correct (incl. the (2,3) descent); cited std-algebra entities are stated over R but used over an ordered F without saying so; one uncited "outer product vanishes, so dependent" step; "(iii) holds over Q" imprecise. |
| synthesis.frobenius-and-universality-in-clifford-algebras | SOUND WITH FIXES | GA proof of Frobenius complete and correct; title, (iv) last sentence and lay overstate (no "finite-dimensional"/"associative", "subalgebra" where only a corner embedding holds: Mat_3(R) has no unital embedding in any Cl(k,k)); real closedness suffices. |
| note.synthesis.grading-of-the-bit-ladder | SOUND WITH FIXES | Placements correct except the Witt-pair/Fock "qubit reading" at step 3 (Z[G]/(c+1) is the orthogonal order, which has no matrix units over Z); "every other step is a theorem" contradicts step 8; lay says the reals are proved. |
| note.synthesis.geometric-algebra-as-the-algebra-of-physics | SOUND WITH FIXES | Marked argued at every level, citations accurate; but "rotation/spinor sign by step 3" contradicts premise (C) (2 pi needs the completion), "Nothing extra" is vacuous by Frobenius, "Pauli group" should be the real Pauli group, rotors misplaced at step 6. |

## 1. synthesis.continuum-completion-premise (postulate)

Exactness. The ordered-field axioms (total order, translation invariance, positivity of products) and the
least-upper-bound property for nonempty bounded-above sets are the standard definition of a complete ordered
field. The derived embedding of Q (1 = 1^2 > 0, m.1 > 0, characteristic 0, unique order-preserving map) is
correct and correctly not assumed.

Uniqueness and Ostrowski. Neither is assumed. Both appear only in the extraction, marked classical, from
memory, not part of the premise and not used. Point 1 of the brief is satisfied.

Labelling. "a mathematical primitive of the series' foundation, not a statement about the physical world" in
formal, lay and one-liner. The (N+) physical reading is explicitly excluded.

Minimality. The premise is more than the filed derivations use, and says so: Sylvester's normalisation needs
only a Euclidean field; Frobenius needs only a real closed field; completeness (LUB) proper is needed for the
limits (exponential of a bivector, pi). That is acceptable for a premise meant to carry the store's real
analysis, but one statement is wrong as worded:

- Formal, "Status and cost": "roots of real polynomials of odd degree, and with them Frobenius' classification
  of the real division algebras, use completeness". The Frobenius proposal's own proof uses completeness only
  for (a) square roots of positives and (b) a root of each odd-degree polynomial; a field with (a) and (b) is
  real closed, and the countable real algebraic numbers are one. The "What would retire it" paragraph already
  names real closed fields, so the text contradicts itself.

Lay. "Fractions are enough to describe every direction up to its sign once square roots are allowed" is loose
(fractions with square roots of positives are the Euclidean closure of Q, not "fractions").

Required fixes.
1. Formal and technical: replace "roots of real polynomials of odd degree, and with them Frobenius'
   classification of the real division algebras, use completeness" (and the technical "completeness itself is
   used ... by the roots of odd-degree polynomials behind Frobenius' theorem") with: "roots of real polynomials
   of odd degree, and with them Frobenius' classification, are obtained here from completeness, but hold in any
   real closed field (for example the real algebraic numbers); completeness proper is needed for limits such as
   the exponential of a bivector and the angle pi".
2. Lay: "Fractions together with square roots of positive numbers are enough to rescale every direction until
   its square is plus one, minus one or zero, ...".

## 2. synthesis.completion-recovers-the-real-clifford-algebras

Proof re-derived step by step.

- (i) S = {x >= 0 : x^2 <= a} contains min(1, a), is bounded by max(1, a). Case s^2 < a: with
  h = min(1, (a - s^2)/(2s+1)), (s+h)^2 <= s^2 + h(2s+1) <= a. Case s^2 > a: h = (s^2 - a)/(2s) lies in
  (0, s/2) because a > 0, (s-h)^2 > a, and s - h is a smaller upper bound. Correct. Hand values (a = 2:
  h = 1/3, 16/9; h = 1/12, 289/144) recomputed.
- (ii) Existence of u with Q(u) != 0 when B != 0 (Q(x+y) = 2B(x,y) for null x, y), the rejection
  x - B(x,u)u^{-1} = (x wedge u)u^{-1}, B(x_perp, u) = 0, induction: correct. Normalisation needs exactly
  square roots of positives.
- (iii) rad V = Z from B(v, u_j) = x_j Q(u_j); P positive definite; Q <= 0 on N + Z; maximality by
  dim W + dim(N+Z) > n. Correct. One step is phrased through an uncited fact: "the outer product of a basis of W
  with a basis of N + Z has more than n vectors and vanishes, so they are linearly dependent". Vanishing implies
  dependence is not cited; the dependence is plain dimension counting. The nonzero intersection vector from the
  dependence relation is fine (w = 0 would force all coefficients zero). Isometry criterion and the converse
  correct.
- (iv) Blade product sign (-1)^{#{(i,j) in S x T, i > j}} and the factor prod Q(e_i) agree with
  std-algebra.orthogonal-anticommute@1; structure constants in {0, +-1}; base change isomorphism correct. The
  embedding through e'_k + f'_k: Q = 1 - 1 = 0, orthogonal to everything else; injectivity by leading blades:
  the image of e_S contains e_{S_old} e'_K with coefficient +-1 and no other image contains that blade, so the
  images are independent. Correct; it restates the embedding of conformal.minimal-nondegenerate-completion@6
  (which is cited and says exactly "Cl(p,q,r) embeds in Cl(p+r, q+r)").
- (v) x xbar = a^2 - y^2 with the cross terms of the pairwise anticommuting e1, e2, e1e2 cancelling and
  (e1e2)^2 = -6: a^2 - 2b^2 - 3c^2 + 6d^2. Recomputed. Descent: mod 3 gives a^2 + b^2 = 0, so 3 | a, b; then
  3a'^2 - 6b'^2 - c^2 + 2d^2 = 0 gives c^2 + d^2 = 0 mod 3, so 3 | c, d. Correct. Own route: this is the
  quaternion algebra (2,3)_Q; the Hilbert symbol at 3 is the Legendre symbol (2/3) = -1, so it is ramified at 3,
  a division algebra. Brute force finds no nontrivial zero with |coefficients| <= 12. Contrast found: squares 2
  and 7 do split ((-6,-5,-4,-3) is a zero), so the example correctly illustrates that square classes, not only
  signs, decide.
- (vi) "Euclidean suffices" is right. It is also necessary over an ordered field: for a > 0 not a square, the
  line <a> is isometric to neither <1> (a = l^2) nor <-1> (a = -l^2 < 0). Worth adding, not required.

Cited entities at pinned versions. polarisation@1, orthogonal-anticommute@1, inverse-of-vector@1,
blade-basis@1, functoriality@1 are all stated for real quadratic spaces (obj.std-algebra.quadratic-space is
"finite-dimensional real vector space"). The proposal uses them over an arbitrary ordered field F, with only
"whose proof is the same over any field of characteristic 0" for two of them, and the Clifford algebra over F is
"defined by the universal property" without existence. The proofs do carry over (std-algebra.existence-uniqueness
is the tensor-algebra quotient, field-agnostic), so this is a citation gap, not an error.

Check. Ran: 5/5 PASS. Perturbations (copies in work-R/): hand signature of "mixed" set to (2,1,0) fails
inertia check; plane squares (2,-2) fail the square-class check (the form then has zeros); radical generators
sent to e'_k (not null) fail the embedding check; a wrong normalising root (1/3 for 1/4) fails the rejection
check. Own recomputation: signatures of all six Gram matrices by numpy eigenvalues (an independent route from
the rejection) agree: (1,1,0), (2,0,0), (1,2,0), (1,0,2), (2,1,1), (1,3,0).

Overlap. Clauses (ii)-(iii) derive over any ordered/Euclidean field what the imported Fact
std-algebra.sylvester-inertia states over R (r = dim rad, isometry iff equal triples; p + q = rank follows).
Declared; the maintainer should mark the Fact as restated by this result. No other duplicate found (no stored
entity on Euclidean fields or square classes).

Required fixes.
1. Proof preamble: add one sentence: "The stored Propositions std-algebra.polarisation, orthogonal-anticommute,
   inverse-of-vector, blade-basis and functoriality, and the existence of Cl(V,Q) (std-algebra.existence-uniqueness,
   the tensor-algebra quotient), are stated over R; their proofs use only field operations and 1/2, and are used
   here verbatim over F." Add std-algebra.existence-uniqueness@1 to `uses`.
2. (iii) proof: replace "the outer product of a basis of W with a basis of N + Z has more than n vectors and
   vanishes, so they are linearly dependent" with "a basis of W together with a basis of N + Z has more than n
   vectors of V, so they are linearly dependent".
3. (v) formal: "(ii) holds without the normalisation and (iii) holds" -> "(ii) holds without the normalisation,
   the invariance of (p, q, r) in (iii) holds, and the isometry criterion fails:".
4. Extraction: "roots of real polynomials of odd degree and Frobenius' theorem" -> add "(for which a real closed
   field suffices)".

## 3. synthesis.frobenius-and-universality-in-clifford-algebras

Proof re-derived.

- (i) step 1: Cauchy bound M = 1 + sum|c_i|; for |x| >= M, |lower terms| <= (M-1)|x|^{n-1} < |x|^n; Lipschitz
  constant; sup argument both cases. Correct (the p(s) < 0 case should intersect with [-M, M], trivial). "The
  same argument applied to X^2 - a" needs the interval [0, M], since X^2 - a is even: minor.
- Step 2: x^2 - y^2 = a, 2xy = sigma|b| = b. Correct.
- Step 3 (Laplace): deg g_t = 2^{m-1}u(n-1) with u(n-1) odd; real coefficients via symmetric functions (one-line
  sketch of the fundamental theorem on symmetric polynomials, acceptable); a root of g_t in C is one of the
  r_i + r_j + t r_i r_j because C sits in L; pigeonhole over t; quadratic. Correct. Irreducibles of degree 2:
  correct.
- (ii) invertibility; irreducible minimal polynomial; x - b in V; closure of V under addition in both cases
  (dependent: alpha beta = 0; independent: alpha = gamma = 0, then beta < 0 by the zero-divisor argument);
  B = (uv + vu)/2 bilinear and negative definite; Cl(0,k) -> D onto. Then u = e1e2: u^2 = -1, B(u, e1) =
  B(u, e2) = 0 so c1 = c2 = 0; k = 2 impossible; for j >= 3, 2ue_j = -2c_j, e_j = c_j u, so k <= 3 and
  e3 = +-e1e2. Correct and complete. Where completeness is used: only square roots of positives (orthonormal
  basis, sqrt(beta)) and odd-degree roots (step 1). So (i) and (ii) hold over any real closed field; the extraction
  says "Completeness is used, and not only the Euclidean property", which is true of this proof, and it must not
  be read as "needed".
- Constructible-reals counterexample: K = real constructible numbers is Euclidean; cbrt 2 has degree 3 over Q, so
  is not in K, and X^3 - 2 (its only real root being cbrt 2) is irreducible over K; K[X]/(X^3 - 2) is a 3-dimensional
  commutative division algebra. Correct, classical, labelled from memory and not used: prior art only.
- (iii) f idempotent; v_i f = 0, f w_i = 0; f v_J^rev w_K f = delta_JK f by the move argument; E_{I,J}E_{K,L}
  = delta_JK E_{I,L}; sum E_{I,I} = prod(w_i v_i + v_i w_i) = 1; corner R f by dimension; regular representation
  injective unital; composite injective with phi(1) = epsilon. Correct. I verified the closed form
  E_{I,I} = prod_{i in I} w_i v_i prod_{i not in I} v_i w_i for k = 2 in GA.py.
- Overstatement: the formal (iii) is precise (A is a subalgebra of the corner epsilon Cl(k,k) epsilon, unit to
  epsilon). But (iv)'s last sentence and the title say "subalgebra of some Cl(k,k)" / "every real algebra inside
  some Cl(k,k)". As a unital subalgebra this is false: a unital homomorphism Mat_3(R) -> Mat_{2^k}(R) = Cl(k,k)
  would make R^{2^k} a Mat_3(R)-module, whose dimension is a multiple of 3. The title also drops "finite-dimensional"
  and "associative" (octonions, infinite-dimensional algebras).
- Lay: "the only number systems in which one can always divide ... are the real numbers, the complex numbers and
  the quaternions" omits finite dimension; R(x), the rational functions, is an infinite-dimensional commutative
  real division algebra.
- One-liner: "a quotient of Cl(0,k) by its pure part" misreads (it is not a quotient by the pure part).
- Unit principle (minor): step 3 introduces an abstract root eta of X^2 + 1 in L; taking L as a splitting field of
  p over Cl(0,1) itself removes it.

Cited entities. complex-numbers@3 (Cl(0,1) and even Cl(2,0) as C, read with I_4), quaternions@1 (Cl(0,2) and
even Cl(3,0)), orthogonal-anticommute@1, blade-basis@1, exceptional-division-algebras@3 (Cl(p,q) zero-divisor free
iff (0,0),(0,1),(0,2)), witt-basis-car@1 (v_i w_j + w_j v_i = delta_ij), fock-representation@1 (f primitive,
Cl(k,k) = Mat_{2^k}(R)), matrix-units@1: each says what is used.

Duplicates. No Frobenius theorem in the store (searched); exceptional-division-algebras is only the Clifford case,
read off the classification, so (ii) is new and stronger. (iii) is new to the store but a direct corollary of
fock-representation and the regular representation, and the proposal says so. (iv) restates stored results and
says which.

Check. Ran: 5/5 PASS. Perturbations: v_J in increasing order fails the matrix-unit relations (sign); a
non-associative structure table for R[x]/(x^3) fails the homomorphism check; a root set not closed under
conjugation fails the real-coefficients check of g_t; Cl(1,1) in place of Cl(0,2) fails the bivector check.
Own recomputation: g_0 for roots +-e, +-2e: pair sums 0, 0, +-e, +-3e, so g_0 = X^2(X^2+1)(X^2+9) =
X^6 + 10X^4 + 9X^2, as stated; e1e2e3 in Cl(0,3) is central with square +1 (GA.py).

Literature. Palais, "The classification of real division algebras", Amer. Math. Monthly 75 (1968) 366-368:
verified (Palais' CV). Laplace 1795: date verified (ETSU history notes); method as stated is the standard
attribution, not verified against the original. Frobenius 1878 (J. reine angew. Math. 84): from memory, not
verified online.

Required fixes.
1. Title: "Frobenius' theorem in geometric algebra, and every finite-dimensional associative real algebra in a
   corner of some Cl(k,k)".
2. (iv) last sentence: "by (iii) every finite-dimensional associative real algebra is a subalgebra of a corner
   epsilon Cl(k,k) epsilon of some Cl(k,k) (in general not a unital subalgebra of Cl(k,k): Mat_3(R) has none)".
3. Lay first sentence: "the only finite-dimensional number systems in which ...".
4. One-liner: "is a quotient of Cl(0,k), k the dimension of its pure part,".
5. Extraction (and optionally formal (i)): add "the proof uses completeness only for square roots of positive
   elements and for a root of each odd-degree polynomial, so (i) and (ii) hold over any real closed field, for
   example the real algebraic numbers".
6. Step 1: "applied to X^2 - a on [0, M] (p(0) < 0 < p(M))". Optional: build L over Cl(0,1) to avoid eta.

## 4. note.synthesis.grading-of-the-bit-ladder

Placement checked against the cited entities: blade-square-signs-f2-quadratic-form (c^2 = 1 for n >= 2; signs as
an F2 quadratic form) at step 2, correct; inverse-of-vector at step 4, correct in content; sylvester-inertia at 5,
correct; periodicity and the division algebras at 6, correct; nilpotent-steps (its formal: rational coefficients,
finite sums) correctly said to need no completeness; central-limit at 7, correct and conditional on a state;
the "note on the two presentations over the integers" exists as note.one-relation.two-presentations-differ-over-the-integers.

Problems.
- Step 3 says the algebra is Z[G]/(c + 1) (the integer span of the orthogonal blades) and then that "the Witt pairs
  and the Fock representation, Cl(k,k) = Mat_{2^k}(R) ..., are the qubit reading". The stored note just cited shows
  that over Z the orthogonal order Lambda_O = Z[G]/(c+1) has no idempotents other than 0, 1 and no matrix units;
  the Witt pairs v = (e + f)/2 need 1/2, and the matrix units live in the different order Lambda_W. The stored Fock
  theorem is stated over R (step 5 by the note's own closing paragraph). So the qubit reading belongs at step 4
  (Z[1/2] or Q), or at step 3 only for the Witt order, not for Z[G]/(c+1).
- Formal opening "every other step is a theorem" contradicts step 8 (argued).
- Step 5: "Completeness proper is used ... by roots of odd-degree polynomials": as in section 1, a real closed
  field suffices.
- Lay: "Everything else follows by proof, from minus one and whole numbers through fractions to the real and complex
  numbers and the quaternions": the reals are assumption 4, not a consequence.

Required fixes.
1. Formal opening: "and every other step except the last (argued) is a theorem".
2. Step 3: replace the last sentence by "Over Z the orthogonal presentation Z[G]/(c+1) and the null (Witt)
   presentation generate different orders, and only the latter contains matrix units
   (note.one-relation.two-presentations-differ-over-the-integers); the Witt pairs need 1/2, so the qubit reading,
   Cl(k,k) = Mat_{2^k} (Theorem std-algebra.fock-representation, stated over R), sits at step 4 for the orthogonal
   presentation."
3. Step 5: "and by roots of odd-degree polynomials (for which a real closed field suffices)".
4. Lay: "... from minus one and whole numbers through fractions and, once the gaps are filled, to the complex numbers
   and the quaternions".

## 5. note.synthesis.geometric-algebra-as-the-algebra-of-physics

Marking. "Argued" appears in title, formal ("Status: argued, not proved"), technical, lay and one-liner. The
objections are substantive and fair (cheap universality, equivalent formalisms, bosons via (N+), which exists as
synthesis.n-plus-null-ground-state; octonions; coverage assembled with hindsight).

Problems.
- Internal inconsistency with premise (C): "Coverage: signs, rotation, a complex unit, spinors, ... all appear by
  step 3", and the spinor sign row is tagged step 2. The element -1 appears at step 2, but its reading as the result
  of a 2 pi rotation needs a rotor exp(-B theta/2) and the angle pi, which premise (C) and the grading note place at
  completion (step 5). Continuous rotations likewise.
- "Nothing extra: established physics uses no finite-dimensional associative division algebra outside R, Cl(0,1),
  Cl(0,2), and by Frobenius there is none": since by Frobenius none exists, physics could not use one; the point
  carries no evidential weight and should not be listed as part of the argument.
- "the Pauli group of qubits" as the extraspecial group: the group of Cl(k,k) generators is extraspecial 2^{1+2k}_+,
  which is the real Pauli group <X_i, Z_i>; the full k-qubit Pauli group has a centre of order 4 (it adds a unit
  squaring to -1) and is not extraspecial. Also Cl(k,k) = Mat_{2^k} on the Fock space is not available over Z for
  the orthogonal presentation (section 4), so "steps 2 and 3" should be "steps 2 to 4".
- "Rotors, the even part (step 6)": the even subalgebra is step 3; rotors as exponentials and Spin(1,3) as a Lie
  group need step 5. Step 6 is the number systems.

Literature. Werner, Colella, Overhauser, Eagen, Phys. Rev. Lett. 35, 1053 (1975): verified (the paper's PDF).
Rauch et al., "Verification of coherent spinor rotation of fermions", Phys. Lett. A (1975): title and year verified
via an index entry; volume and page (54A, 425) from memory. Hestenes, Space-Time Algebra (Gordon and Breach, 1966)
and Jordan and Wigner (Z. Phys. 47, 1928): consistent with my knowledge, not verified online. Jordan-Wigner "for the
qubit reading" is fair as the fermion-to-spin-chain map. Spencer-Brown is not cited in either note; it is cited only
in synthesis.premise-the-bit (Laws of Form, 1969, the law of crossing), which matches the book (crossing twice
returns the unmarked state, i.e. 1 + 1 = 0). Frobenius is not cited with a date here; the Frobenius proposal's 1878
is correct to my knowledge.

Required fixes.
1. Spinor row: "The sign bit -1 (step 2), read as the rotor of a rotation by 2 pi (step 5)". Coverage sentence:
   "signs, a complex unit, spinors (as an algebra), a Lorentzian form and anticommuting fermions appear by step 4;
   continuous rotations and the 2 pi sign of spinors need the completion (step 5)".
2. Remove "Nothing extra" from the parts of the argument, or reword: "That no other finite-dimensional associative
   division algebra is used is a theorem (Frobenius), not evidence; the substantive claim would be that physics needs
   no non-associative structure, which objection (5) leaves open".
3. "the Pauli group of qubits" -> "the real Pauli group <X_i, Z_i> of k qubits (extraspecial of order 2^{1+2k});
   the full Pauli group adds a central unit of square -1"; "(steps 2 and 3)" -> "(steps 2 to 4)".
4. Rotor row: "(steps 3 and 5)".
5. Give full citations for the two 1975 experiments (Phys. Lett. A 54, 425; Phys. Rev. Lett. 35, 1053).

## House style

No em dashes, no "honest"/"load-bearing", macros all in store/notation.yaml (\Cl, \Q, \R, \Z, \C, \HH, \Mat). No
bare imaginary unit at any level; the only abstract square root of -1 is eta inside the Laplace step (optional fix
above). Everything is in geometric algebra where a GA statement exists.

## Work files

`colony/runs/2026-11-07-bit-root/verify/work-R/`: c1..c4 (completion perturbations), f1..f4 (Frobenius
perturbations), own_route.py (Hilbert symbol and brute force for (2,3)_Q, (2,7)_Q zero, eigenvalue signatures,
E_{I,I} closed form, e1e2e3 in Cl(0,3)).
