---
id: synthesis.positive-rationals-are-the-squares-of-the-even-subalgebra-of-cl-three
kind: claim
version: 1
title: 'Positive rationals are the squares x x~ of the even subalgebra of Cl(3,0); the order of Q'
status: proved
region: synthesis
subject: clifford-structure
tags: [classical-theorem, finite-models, forcing-and-uniqueness]
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
  why: "The statement is about the even subalgebra of Cl(3,0) and its product, and those parts are computed with the Clifford product. The descent uses congruences of integers (modulo a prime, modulo 4 and 8) and the last clause uses the diagonalisation of a rational quadratic form; these are elementary arithmetic and linear algebra of scalars."
derivations:
- name: main
  uses:
  - std-algebra.quaternions@1
  - synthesis.division-gives-the-rationals@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_norm_of_the_even_subalgebra_is_a_sum_of_four_squares_and_multiplicative
- kind: check
  ref: check.py::check_descent_writes_every_odd_prime_below_two_hundred_as_a_square_of_an_integer_even_element
- kind: check
  ref: check.py::check_integers_to_three_thousand_are_sums_of_four_squares_and_three_fail_exactly_on_the_sevens
- kind: check
  ref: check.py::check_seven_times_a_square_is_never_a_sum_of_three_squares
- kind: check
  ref: check.py::check_positive_rationals_are_squares_and_positive_semidefinite_matrices_are_sums_of_squares
lineage:
  motivated_by:
  - synthesis.premise-positivity-of-values
  - synthesis.continuum-completion-premise
  - synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear
extraction:
  open_problem: op.positivity-of-values
  note: >-
    Written for two uses: the reflection step of the theorem on additive weights in every size from four needs,
    for a rational vector $r$, a vector of a coordinate four-space with the same square, which is clause (ii);
    and the premise of positivity of values is stated over an ordered field, for which clause (iii) says what
    the rational foundation already supplies. A test fixed before computing: that the positive
    rationals are exactly the squares $x\tilde{x}$ of the nonzero even elements; it held. Clause (ii)
    is Lagrange's four-square theorem (1770) and the multiplicativity of the norm is Euler's four-square
    identity; clause (iv) is the easy half of Legendre's three-square theorem; clause (iii), that $\Q$ has one
    ordering and its positive cone is the sums of squares, is classical (Artin and Schreier, 1927, for the general
    theory; from memory). Nothing here is new mathematics. The proofs are written out so that the store does not
    import them, and so that they use the product of the even subalgebra: the descent's key step is one product
    $x\tilde{y}$. What is machine-verified: the multiplicativity on samples, the descent run to the end for the $45$
    odd primes below $200$, four squares for every integer up to $3000$ with the three-square failures exactly at
    $4^{a}(8b+7)$ in that range (the converse half of Legendre's theorem is computed there, not proved), the tables
    modulo $8$ and $4$ behind clause (iv), and one instance of clause (v). Ledger: transport-absent. Not treated:
    fields with more than one ordering, such as $\Q(\sqrt{2})$, over which the stored CHSH element reaches its
    largest value; there the squares of the even subalgebra give the elements positive in every ordering, and
    choosing one ordering is a further datum (classical, not proved here).
---

## formal
Let $e_{1}, e_{2}, e_{3}$ generate $\Cl_{\Q}(3,0)$, $B_{1} = e_{3}e_{2}$, $B_{2} = e_{1}e_{3}$, $B_{3} = e_{2}e_{1}$ its unit bivectors, and $\Cl^{+}_{\Q}(3,0) = \{x = x_{0} + x_{1}B_{1} + x_{2}B_{2} + x_{3}B_{3}\}$ its even subalgebra (\claimref{std-algebra.quaternions}); $\tilde{x}$ is the reverse and $N(x) = x\tilde{x}$. An even element is \emph{integral} if its four components are integers.
\begin{enumerate}
\item[(i)] \emph{(The square of an even element; proved.)} $N(x) = x_{0}^{2} + x_{1}^{2} + x_{2}^{2} + x_{3}^{2}$, a scalar; $N(xy) = N(x)N(y)$; $N(x) = 0$ only for $x = 0$; and $x^{-1} = \tilde{x}/N(x)$ for $x \ne 0$ (the even subalgebra has no zero divisors, as stored for $\Cl_{\Q}(0,2)$ in \claimref{synthesis.division-gives-the-rationals}).
\item[(ii)] \emph{(Four squares; proved; Lagrange's theorem, by the classical descent written with the product of the even subalgebra.)} Every positive integer is $N(x)$ for an integral $x$. Hence every positive rational $t$ is $N(x)$ for some $x \in \Cl^{+}_{\Q}(3,0)$: if $t = a/b$ and $ab = N(y)$ with $y$ integral, then $t = N(y/b)$.
\item[(iii)] \emph{(The order of the rationals; proved.)} Let $\mathsf{P} = \{N(x) : x \in \Cl^{+}_{\Q}(3,0),\ x \ne 0\}$. Then $\mathsf{P}$ is closed under sums, products and inverses, and $\Q$ is the disjoint union of $\mathsf{P}$, $\{0\}$ and $-\mathsf{P}$; it is the set of positive rationals. If $\mathsf{P}'$ is any subset of $\Q$ closed under sums and products with $\Q \setminus \{0\}$ the disjoint union of $\mathsf{P}'$ and $-\mathsf{P}'$ (an ordering of the field), then $\mathsf{P}' = \mathsf{P}$. So the rational field has exactly one ordering, and it is read off the algebra: $s < t$ exactly when $t - s = x\tilde{x}$ for a nonzero even $x$.
\item[(iv)] \emph{(Three squares do not suffice; proved.)} $a^{2} + b^{2} + c^{2} = 7d^{2}$ has no solution in integers with $d \ne 0$. So $7$ is not $N(x)$ for an even $x$ with $x_{0} = 0$: no bivector $B$ of $\Cl_{\Q}(3,0)$ has $B^{2} = -7$, and the four components of (ii) are all needed.
\item[(v)] \emph{(Positive elements are sums of squares; proved.)} Let $A$ be a symmetric matrix in $\Mat_{n}(\Q)$ with $r^{T}Ar \ge 0$ for every $r \in \Q^{n}$. Then $A$ is a sum of at most $4n$ matrices $yy^{T}$ with $y \in \Q^{n}$. So in a rational matrix algebra with the transpose as adjoint (for instance the algebra of two modes; a remark, by clause (i) of \claimref{synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear}), the elements that are non-negative in this sense are exactly the finite sums of elements $xx^{\dagger}$.
\end{enumerate}
\emph{Reading.} The premise of positivity of values (\claimref{synthesis.premise-positivity-of-values}) is stated for a Clifford algebra over an ordered field. Over the rationals, the scalars of the foundation before the completion (\claimref{synthesis.continuum-completion-premise}), the order is not a further datum: by (iii) there is one ordering and its positive scalars are the squares $x\tilde{x}$ of the even subalgebra of $\Cl_{\Q}(3,0)$, four rational components being needed by (iv). After the completion a positive scalar is the square of a scalar; over $\Q$ it is the square of an even element. By (v) the condition $\omega(xx^{\dagger}) \ge 0$ of the premise is, on a rational matrix algebra, the condition that $\omega$ is non-negative on every symmetric element that is non-negative on all rational vectors. Nothing here derives the premise.

## technical
Lagrange's four-square theorem, written in the series' algebra. The even subalgebra of the Clifford algebra of three-dimensional space over the rationals has a multiplicative square $x\tilde{x}$, the sum of the four squared components. The theorem says every positive integer is such a square with integer components, hence every positive rational is one with rational components. The proof is the classical one: for an odd prime $p$ some multiple $mp$ with $m < p$ is a square, and if $m > 1$ one reduces the components modulo $m$, multiplies by the reverse of the reduced element and divides by $m$, which lowers $m$. Three consequences are drawn. The rational field has exactly one ordering, and its positive elements are these squares, so an ordered rational Clifford algebra carries no choice of order. Three components are not enough: $7$ is not a sum of three rational squares, equivalently no rational bivector of three-dimensional space squares to $-7$. And in a rational matrix algebra with the transpose as adjoint every positive semidefinite element is a sum of at most $4n$ squares $yy^{T}$, by diagonalising the form and writing each diagonal entry as four squares. All of this is classical (Lagrange, Euler, Legendre for the three-square statement, Artin and Schreier for orderings); it is proved here so that the two results that use it do not rest on an import. Transport-absent.

## lay
Every positive whole number is a sum of four squares: $7 = 4 + 1 + 1 + 1$. This old theorem has a natural home in the algebra of three-dimensional space, where the rotations live in a four-component part and the "size" of such an element is exactly a sum of four squares, with the size of a product equal to the product of the sizes. So the positive fractions are precisely the sizes of these elements. That gives a way to say which numbers are positive using only the algebra, with no separate rule; and three components would not be enough, because $7$ is not a sum of three squares of fractions.

## one-liner
In $\Cl^{+}_{\Q}(3,0)$ the square $x\tilde{x} = x_{0}^{2} + x_{1}^{2} + x_{2}^{2} + x_{3}^{2}$ is multiplicative and (Lagrange's theorem, proved here by the descent $x \mapsto x\tilde{y}/m$) takes every positive rational value; so $\Q$ has exactly one ordering and its positive cone is $\{x\tilde{x} : x \ne 0\}$, three components do not suffice (no rational bivector squares to $-7$), and every positive semidefinite element of $\Mat_{n}(\Q)$ is a sum of at most $4n$ squares $yy^{T}$.
