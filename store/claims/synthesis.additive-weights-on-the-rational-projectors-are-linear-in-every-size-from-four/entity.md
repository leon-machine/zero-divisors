---
id: synthesis.additive-weights-on-the-rational-projectors-are-linear-in-every-size-from-four
kind: claim
version: 1
title: 'Additive weights on rational projectors are linear from size four: two or more modes'
status: proved
region: synthesis
subject: clifford-structure
tags: [finite-models, classical-theorem, measurement-and-records]
proposed_by:
  kind: ai
  session: 2026-11-24-number-theory
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-24-number-theory
review: draft
outside_ga:
  kind: other
  why: "The reduction is carried by one reflection, x -> -u x u^{-1}, and by the squares of the even subalgebra of Cl(3,0); those parts are computed with the Clifford product. The rest is linear algebra of rational vector spaces: supports of vectors, linear functionals on a four-dimensional space, and a quadratic form vanishing on three hyperplanes."
derivations:
- name: main
  uses:
  - synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear@1
  - synthesis.positive-rationals-are-the-squares-of-the-even-subalgebra-of-cl-three@1
  - std-algebra.reflection@1
  - std-algebra.quaternions@1
  - tower.ladder-pairs-satisfy-car-vectors@4
  - synthesis.signed-directions-and-the-integer-clifford-algebra@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_three_modes_are_the_rational_matrices_of_size_eight_and_the_adjoint_is_the_transpose
- kind: check
  ref: check.py::check_a_reflection_carries_a_coordinate_four_space_onto_one_through_the_vector
- kind: check
  ref: check.py::check_vectors_of_smaller_support_fill_at_least_three_hyperplanes_and_force_a_quadratic_form_to_vanish
- kind: check
  ref: check.py::check_two_rational_vectors_need_not_lie_in_a_four_space_similar_to_the_standard_one
- kind: check
  ref: check.py::check_linear_weights_sum_to_the_trace_on_a_reflected_frame_and_are_recovered_from_their_values
- kind: check
  ref: check.py::check_one_mode_admits_a_non_negative_additive_weight_that_is_not_linear
lineage:
  motivated_by:
  - synthesis.premise-positivity-of-values
  - synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects
  - one-relation.measure-indifference-borns-rule-located
extraction:
  open_problem: op.positivity-of-values
  note: >-
    Answers the item of the open problem left as "not done: more than two modes". The stored theorem for two
    modes named a first step for it: that any two rational vectors of $\Q^{2^{\ell}}$ lie in a four-dimensional
    rational subspace similar to the standard one. Tests fixed before computing. First, whether that first
    step is false. It is: clause (v), an obstruction at the prime $2$ (the square of the bivector $u \wedge w$
    must be a sum of three rational squares, and $7$ is not). Second, whether the replacement route fails, some rational
    vector lying in no reflected coordinate four-space in which the vectors of smaller support are not contained
    in a quadric. It does not: clause (ii) holds for every vector. Third, whether the replacement needs an input
    that cannot be proved in the store in a page. It does not: the one arithmetic input is Lagrange's four-square
    theorem, proved in synthesis.positive-rationals-are-the-squares-of-the-even-subalgebra-of-cl-three. The
    candidate import named in the open problem (positive definite rational forms of dimension at least four
    represent every positive rational, a consequence of the Hasse-Minkowski theorem) is true and classical, but
    it is not needed: the reflection step needs it only for the standard form in four variables, which is
    Lagrange's theorem. What the result rests on: the whole content beyond linear algebra is the stored theorem
    for two modes (size four), with its four finite exact computations; if that theorem fell, this one would
    fall with it, and nothing here re-proves it. What is machine-verified here: the identification of three
    modes with the rational matrices of size eight; the reflection step and the hyperplane count on ten sample
    vectors of support five to eight, among them the vector of eight ones (for which the square of the vector
    minus the square of any one component is $7$) and vectors whose square is of the form $4^{a}(8b+7)$; the
    counterexample pair of clause (v) and the three-square identity on $36$ pairs. The induction itself is the
    proof's. Prior art, to be confirmed from the papers by Leon (the stored theorem's note has the details):
    D. Kh. Mushtari, Lobachevskii J. Math. 9 (2001) 47, poses as Problem G whether non-negative finitely additive
    measures on the orthogonal rational projections of $\Q^{n}$ have the form $\operatorname{tr}(TP)$; read
    through a summary only. If the stored theorem for $n = 4$ stands, clause (iii) gives the trace form for every
    $n \ge 4$, in the signed form with values in a rational vector space. A search on 24 November 2026 found no
    later solution of Problem G and no earlier statement of this reduction, which is not proof that none
    exists; no claim of priority is made. The case $n = 3$ is not treated: the argument needs coordinate
    four-spaces. For one mode ($n = 2$) the statement is false: on the rays of $\Q^{2}$ a frame is a pair
    $\{(a, b), (-b, a)\}$, and the weight that is $1$ on primitive integer rays with first component odd and
    second even, $0$ on those with first even and second odd, and $\tfrac12$ on those with both odd, is
    non-negative, sums to $1$ on every frame and is not of the quadratic form (it is $1$ at $(1, 2)$, where the
    only candidate form gives $\tfrac15$); the stored result on the even subalgebra of two modes records the
    same phenomenon. Ledger: transport-absent; the series' content is where it places the premise (P).
---

## formal
Let $n \ge 4$. In $\Mat_{n}(\Q)$ with the transpose as adjoint, a \emph{projector} is a symmetric idempotent, and for nonzero $r \in \Q^{n}$, $\Pi_{r} = rr^{T}/(r \cdot r)$ is the projector onto the ray of $r$. Let $V$ be a vector space over $\Q$. An \emph{additive weight} with values in $V$ is a function $\mu$ from the projectors to $V$ with $\mu(E + E') = \mu(E) + \mu(E')$ whenever $EE' = 0$; no sign condition, normalisation or continuity is assumed. The \emph{support} of a vector is the set of indices of its nonzero components, and for a set $T$ of indices $\Q^{T}$ is the coordinate subspace of the vectors with support in $T$. Vectors of $\Q^{n}$ are read as vectors of $\Cl_{\Q}(n,0)$, and for a nonzero vector $u$, $g_{u}(x) = -uxu^{-1}$ is the reflection in $u$ (\claimref{std-algebra.reflection}).
\begin{enumerate}
\item[(i)] \emph{(The algebra of $\ell$ modes is a rational matrix algebra, $\ell \ge 1$; proved.)} Let $\Cl_{\Q}(\ell,\ell)$ be the algebra of $\ell$ modes: generators $e_{j}, f_{j}$, $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, the adjoint $\dagger$ the linear extension of the inverse on blades, $v_{j} = \tfrac12(e_{j} + f_{j})$, $w_{j} = \tfrac12(e_{j} - f_{j}) = v_{j}^{\dagger}$ (ladder pairs, \claimref{tower.ladder-pairs-satisfy-car-vectors}), $P_{0} = w_{1}v_{1}\cdots w_{\ell}v_{\ell}$ and, for a subset $I = \{i_{1} < \dots < i_{m}\}$, $s_{I} = v_{i_{1}}\cdots v_{i_{m}}P_{0}$. Then $s_{I}^{\dagger}s_{J} = \delta_{IJ}P_{0}$, and $s_{I}^{\dagger}xs_{J} = m(x)_{IJ}P_{0}$ defines an isomorphism $m$ of $\Cl_{\Q}(\ell,\ell)$ onto $\Mat_{2^{\ell}}(\Q)$ with $m(x^{\dagger}) = m(x)^{T}$. So the self-adjoint idempotents of $\ell$ modes are the projectors of $\Mat_{n}(\Q)$, $n = 2^{\ell}$, as stored for $\ell = 2$ (clause (i) of \claimref{synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear}).
\item[(ii)] \emph{(A reflected coordinate four-space through any vector; proved.)} Let $r \in \Q^{n}$ have support $S$ with at least five indices, and let $T \subset S$ have four. There is $r' \in \Q^{T}$ with $r' \cdot r' = r \cdot r$ (four squares: clause (ii) of \claimref{synthesis.positive-rationals-are-the-squares-of-the-even-subalgebra-of-cl-three}). Then $u = r - r' \ne 0$, $g_{u}$ is an isometry of $\Q^{n}$ with $g_{u}(r') = r$, and $W = g_{u}(\Q^{T})$ is a four-dimensional subspace through $r$ on which the form is carried from the standard one of $\Q^{T}$ by an isometry. Every vector of $W$ has support in $S$. For each $t \in T$ the vectors of $W$ whose $t$-th component vanishes form a hyperplane of $W$ and have support in $S \setminus \{t\}$; the vectors of $W$ with no component outside $T$ form a hyperplane of $W$ and lie in $\Q^{T}$; and at least four of these five hyperplanes are distinct.
\item[(iii)] \emph{(Additive weights are linear; proved, given the stored theorem for size four.)} For every additive weight $\mu$ with values in $V$ there are unique $\rho_{ij} = \rho_{ji} \in V$ with
\[
\mu(\Pi_{r}) = \frac{1}{r \cdot r}\sum_{i,j}\rho_{ij}r_{i}r_{j} \quad\text{for all } r, \qquad \mu(E) = \sum_{i,j}\rho_{ij}E_{ij} \quad\text{for every projector } E .
\]
So $\mu$ is the restriction to the projectors of a $\Q$-linear map on $\Mat_{n}(\Q)$, for every $n \ge 4$, and in particular on the algebra of $\ell$ modes for every $\ell \ge 2$. The proof uses the stored theorem (clause (iii) of \claimref{synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear}) on coordinate four-spaces and on their images under reflections, and induction on the size of the support by (ii).
\item[(iv)] \emph{(With the sign condition: the states of (P); proved.)} Let $V = \Q$, $\ell \ge 2$ and $n = 2^{\ell}$. An additive weight with $\mu(\Pi_{r}) \ge 0$ for all $r$ and $\mu(1) = 1$ is the restriction of exactly one linear $\omega$ on $\Cl_{\Q}(\ell,\ell)$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(x^{\dagger}) = \omega(x)$ (a state of the premise \claimref{synthesis.premise-positivity-of-values}), and every such state restricts to such a weight. As for two modes, of what the premise asserts about projectors only the sign is not implied by additivity; that an element whose spectral projectors are not rational takes the value of the linear extension remains part of the premise.
\item[(v)] \emph{(The pairwise route fails; proved.)} If two vectors $u, w \in \Q^{n}$ lie in a four-dimensional subspace $W$ that is similar to the standard $\Q^{4}$ (there is a linear bijection $\varphi : \Q^{4} \to W$ and $c \in \Q$ with $\varphi(x) \cdot \varphi(y) = c\,x \cdot y$), then
\[
-(u \wedge w)^{2} = (u \cdot u)(w \cdot w) - (u \cdot w)^{2}
\]
is a sum of three rational squares. For $u = e_{1}$, $w = e_{2} + e_{3} + e_{4} + 2e_{5}$ it is $7$, which is not (clause (iv) of \claimref{synthesis.positive-rationals-are-the-squares-of-the-even-subalgebra-of-cl-three}). So for every $n \ge 5$ there are two rational vectors that lie in no four-dimensional rational subspace similar to the standard one: the first step named in the note of the stored theorem is false, and (iii) is not proved through it.
\end{enumerate}
\emph{Reading.} For the rational algebra of two or more modes, a weight on the self-adjoint idempotents that does not depend on the context and adds on orthogonal ones is the restriction of a linear functional; with non-negativity and normalisation it is the restriction of one state of (P). The dependence on two modes in the stored account is removed; the dependence on the rational scalars, on all rational projectors (not only those of rational unit vectors) and on the stored theorem for size four is not. Nothing here derives (P).

## technical
The stored theorem says that on the four by four rational matrices, with the transpose as adjoint, a function on the symmetric idempotents that adds on orthogonal pairs is the restriction of a linear functional. This result extends it to every size $n \ge 4$, hence to the algebra of any number $\ell \ge 2$ of modes, which is the rational matrix algebra of size $2^{\ell}$. The route suggested earlier, to put any two rational vectors in a common four-dimensional subspace similar to the standard one, fails: in such a subspace the vectors are rational quaternions up to a scale, and the square of the bivector they span is then a sum of three rational squares, which $7$ is not; the vectors $e_{1}$ and $e_{2} + e_{3} + e_{4} + 2e_{5}$ are a counterexample. The proof given instead goes one vector at a time. On every coordinate four-space, and on its image under any rational reflection, the weight is a quadratic form, by the stored theorem. These forms agree on coordinate four-spaces, which gives one symmetric $\rho$, and the difference between the weight and $\rho$ vanishes on vectors with at most four nonzero components. Given a vector $r$ with more, choose four of its indices and a vector $r'$ of that coordinate four-space with the same square; it exists because every positive rational is a sum of four rational squares. The reflection that carries $r'$ to $r$ carries the coordinate four-space to a four-space through $r$ in which the vectors with fewer nonzero components than $r$ fill at least three distinct hyperplanes. A quadratic form on a four-space that vanishes on three distinct hyperplanes is zero, so the difference vanishes at $r$, by induction on the number of nonzero components. With non-negativity and normalisation the weights are the restrictions of the states of (P). The theorem rests on the stored theorem for size four and on the rational scalars; it does not cover size three, and it does not derive (P). Prior art is as for the stored theorem and is to be confirmed from the papers.

## lay
An earlier result showed, for the series' algebra of two modes with rational numbers, that if every yes-or-no question gets one number, the same in whichever set of compatible questions it is asked, and the numbers of mutually exclusive questions add up, then the numbers are given by a formula of the same form as the usual quantum rule. This result shows the same for any number of modes from two on; for a single mode it is false. The idea is to reach a general question from simpler ones by a single mirror reflection, chosen so that the question lands in a familiar four-dimensional setting where the earlier result applies. Choosing the mirror needs one old fact of number theory: every positive fraction is a sum of four squares of fractions. A more direct idea, to put any two questions in one four-dimensional setting, does not work, and the obstruction is again arithmetic: the number $7$ is not a sum of three squares.

## one-liner
For every $n \ge 4$, and so for the algebra $\Cl_{\Q}(\ell,\ell) \cong \Mat_{2^{\ell}}(\Q)$ of $\ell \ge 2$ modes, a function on the symmetric idempotents that adds on orthogonal ones, with values in a rational vector space and no sign condition, is the restriction of a linear functional (given the stored theorem for size four): every rational vector lies in the reflection $-u\,\Q^{T}u^{-1}$ of a coordinate four-space, found from four squares, in which vectors of smaller support fill three hyperplanes; the pairwise route fails ($e_{1}$ and $e_{2} + e_{3} + e_{4} + 2e_{5}$ lie in no four-space similar to the standard one, since $7$ is not a sum of three squares).
