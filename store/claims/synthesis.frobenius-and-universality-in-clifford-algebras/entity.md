---
id: synthesis.frobenius-and-universality-in-clifford-algebras
kind: claim
version: 2
title: "Frobenius in GA; every finite-dimensional associative real algebra in a corner of Cl(k,k)"
status: proved
region: synthesis
subject: clifford-structure
tags: [clifford-classification, forcing-and-uniqueness, needs-continuum, classical-theorem]
proposed_by:
  kind: ai
  session: 2026-11-07-bit-root
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-07-bit-root
- name: Claude Opus 5.5
  role: 'maintainer pass, foundation layer'
  version: 2
  source: run 2026-11-08-foundation-layer
review: draft
about:
- obj.std-algebra.clifford-algebra
founded_on:
- synthesis.continuum-completion-premise@2
derivations:
- name: main
  uses:
  - std-algebra.complex-numbers@3
  - std-algebra.quaternions@1
  - std-algebra.orthogonal-anticommute@1
  - std-algebra.blade-basis@1
  - transport.exceptional-division-algebras@3
  - std-algebra.witt-basis-car@1
  - std-algebra.fock-representation@1
  - std-algebra.matrix-units@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_real_polynomials_have_roots_in_the_plane_algebra
- kind: check
  ref: check.py::check_pure_part_and_minimal_polynomial
- kind: check
  ref: check.py::check_the_bivector_bounds_the_dimension
- kind: check
  ref: check.py::check_every_algebra_embeds_in_some_cl_kk
- kind: check
  ref: check.py::check_the_number_systems_inside
- kind: proof
  derivation: main
locators:
  paper: T00a
  number: Thm 6.4
  label: thm:bitfrobenius
  line: 328
extraction:
  maintainer_pass_2026_11_08_foundation:
    by: ai-maintainer-pass
    note: >-
      Version 1 -> 2. Leon's decision of 8 November 2026: the foundation layer. Founded on synthesis.continuum-completion-premise: the algebra it is stated in rests on the foundation. Foundation postulates are reported as what a result rests on, separately from the premises it holds given (store/conventions.md, "The foundation").
  note: >-
    From Leon's working document "From the Bit to the Numbers" (7 November 2026), Step 4 (the number
    systems inside, Frobenius and universality), proved and checked here; not an attack on an open
    problem. Stated for a complete ordered field, the store's real numbers under premise (F4) (filed
    alongside as synthesis.continuum-completion-premise; the maintainer may add the assumes edge at
    acceptance). The proof uses completeness only for square roots of positive elements and for a root of each odd-degree polynomial, so (i) and (ii) hold over any real closed field, for example the real algebraic numbers. Completeness is used, and not only the Euclidean property: clause (i) needs a root of
    every real polynomial of odd degree. Over a Euclidean field that is not real closed the
    classification fails (from memory, not used: over the field of real constructible numbers the cubic
    extension by a cube root of 2 is a commutative division algebra of dimension 3). Derived, not
    imported: clause (i) is the real form of the fundamental theorem of algebra by Laplace's argument
    (induction on the power of 2 in the degree), clause (ii) is Frobenius' theorem (1878) by the
    classical route through the pure part, here read as a negative definite quadratic space whose
    Clifford algebra maps onto the division algebra; the bivector e_1 e_2 does the work that the cross
    product does in textbook proofs. Clause (iii) is the regular representation composed with the Fock
    matrix units of std-algebra.fock-representation; as the source document says, this containment
    holds equally for matrix algebras, so it is a statement about where the algebras sit, not about
    what geometric algebra adds. The number systems of clause (iv) are stored results except the
    explicit split-complex idempotents and the dual numbers on a null vector, which are restated for
    completeness (std-algebra.periodicity has Cl(1,0) = R + R; std-algebra.matrix-units and
    conformal.minimal-nondegenerate-completion carry the dual numbers Cl(0,0,1)). The integer and
    rational algebras that precede this result are filed alongside
    (synthesis.signed-directions-and-the-integer-clifford-algebra, synthesis.division-gives-the-rationals).
    Ledger: transport-absent. Prior art, cited from memory and not used: Frobenius (1878); Palais, "The
    classification of real division algebras", Amer. Math. Monthly 75 (1968); Laplace's proof of the
    fundamental theorem of algebra (1795), as in standard algebra texts. The octonions are not
    associative and are outside the statement.
---

## formal
Let $\R$ be a complete ordered field, as premise (F4) takes the coefficients to be. $\Cl(0,1) = \mathrm{span}\{1, e_{1}\}$, $e_{1}^{2} = -1$, is the complex field $\C$ (\claimref{std-algebra.complex-numbers}), and $\Cl(0,2)$ is the quaternions $\HH$ (\claimref{std-algebra.quaternions}).
\begin{enumerate}
\item[(i)] \emph{(Real polynomials have their roots in $\Cl(0,1)$.)} Every nonconstant polynomial with coefficients in $\R$ has a root in $\Cl(0,1)$. Hence every irreducible polynomial over $\R$ has degree $1$ or $2$. (Completeness is used only for square roots of positive elements and a root of each odd-degree polynomial, so (i) and (ii) hold over any real closed field.)
\item[(ii)] \emph{(Frobenius, in geometric algebra.)} Let $D \ne 0$ be a finite-dimensional associative unital $\R$-algebra without zero divisors. Then $V = \{x \in D : x^{2} \in \R,\ x^{2} \le 0\}$ is a subspace, $D = \R 1 \oplus V$, and $Q(v) = v^{2}$ is a negative definite quadratic form on $V$ with polar form $B(u, v) = \tfrac12(uv + vu)$. The inclusion $V \subseteq D$ extends to a surjective homomorphism $\Cl(0,k) \to D$, $k = \dim V$. If $k \ge 2$, the bivector $e_{1}e_{2}$ of an orthonormal basis lies in $V$, is orthogonal to $e_{1}$ and $e_{2}$, and commutes with every $e_{j}$, $j \ge 3$, which forces $e_{j} = \pm e_{1}e_{2}$; so $k \in \{0, 1, 3\}$ and $D$ is isomorphic to $\R$, $\Cl(0,1)$ or $\Cl(0,2)$ (for $k = 3$, $e_{3} = \pm e_{1}e_{2}$: the quaternionic quotient of $\Cl(0,3)$). Conversely these three have no zero divisors (\claimref{transport.exceptional-division-algebras}).
\item[(iii)] \emph{(Every finite-dimensional real algebra sits in some $\Cl(k,k)$.)} Let $v_{i}$, $w_{i}$ ($1 \le i \le k$) be a Witt basis of $\R^{k,k}$, $f = v_{1}w_{1}v_{2}w_{2}\cdots v_{k}w_{k}$, and for $I, J \subseteq \{1, \dots, k\}$ let $E_{I,J} = w_{I}\,f\,v_{J}^{\leftarrow}$, with $w_{I}$ the increasing and $v_{J}^{\leftarrow}$ the decreasing product. The $E_{I,J}$ are a complete system of $2^{k} \times 2^{k}$ matrix units of $\Cl(k,k)$. If $A$ is an associative unital $\R$-algebra of finite dimension $d \le 2^{k}$, $L(a)$ the matrix of left multiplication by $a$ in a basis of $A$, and $I_{1}, \dots, I_{d}$ distinct index sets, then $\varphi(a) = \sum_{s,t}L(a)_{st}E_{I_{s},I_{t}}$ is an injective algebra homomorphism $A \to \Cl(k,k)$ whose image of $1$ is the idempotent $\epsilon = \sum_{s}E_{I_{s},I_{s}}$: $A$ is a subalgebra of the corner $\epsilon\,\Cl(k,k)\,\epsilon \cong \Mat_{d}(\R)$.
\item[(iv)] \emph{(The number systems inside.)} $\R = \Cl(0,0)$; $\C = \Cl(0,1)$, also the even part of $\Cl(2,0)$ (\claimref{std-algebra.complex-numbers}); the split-complex numbers $\Cl(1,0) = \R\epsilon_{+} \oplus \R\epsilon_{-}$, $\epsilon_{\pm} = \tfrac12(1 \pm e_{1})$, $\cong \R \oplus \R$; the dual numbers $\mathrm{span}\{1, n\} \cong \Cl(0,0,1)$ for a nonzero null vector $n$ of $\Cl(1,1)$; $\HH = \Cl(0,2)$, also the even part of $\Cl(3,0)$; and $\Mat_{2^{k}}(\R) \cong \Cl(k,k)$. By (ii) no other finite-dimensional associative real division algebra exists, and by (iii) every finite-dimensional associative real algebra is a subalgebra of a corner $\epsilon\,\Cl(k,k)\,\epsilon$ of some $\Cl(k,k)$ (in general not a unital subalgebra of $\Cl(k,k)$: $\Mat_{3}(\R)$ has no unital embedding in any $\Mat_{2^{k}}(\R)$).
\end{enumerate}

## technical
Assuming the coefficients are a complete ordered field (premise (F4)), Frobenius' theorem has a short proof in geometric algebra. First, every real polynomial has a root in $\Cl(0,1)$, the plane algebra of one direction squaring to $-1$: odd degrees have a real root by the least-upper-bound property, square roots exist in $\Cl(0,1)$, and Laplace's induction on the power of $2$ in the degree does the rest; so real irreducible polynomials have degree at most $2$. In a finite-dimensional real division algebra every element therefore satisfies a quadratic, which splits it into a real part and a pure part whose square is a negative real. The pure parts form a negative definite quadratic space, so the division algebra is a quotient of the Clifford algebra $\Cl(0,k)$. In that algebra the bivector $e_{1}e_{2}$ is itself pure and orthogonal to $e_{1}, e_{2}$, and it commutes with every further generator; in a division algebra this forces each further generator to equal $\pm e_{1}e_{2}$. Only $k = 0, 1, 3$ survive, giving the real numbers, $\Cl(0,1)$ and the quaternions $\Cl(0,2)$. Separately, every finite-dimensional associative real algebra embeds, through its action on itself, into a corner of $\Cl(k,k)$, using the explicit matrix units $w_{I}fv_{J}$ built from the vacuum idempotent of $k$ null pairs; the split-complex numbers, the dual numbers on a null vector, and the matrix algebras all sit inside in this way. This containment holds for matrices as much as for geometric algebra.

## lay
If the number line has no gaps, then the only finite-dimensional number systems in which one can always divide, and in which multiplication is associative though not necessarily commutative, are the real numbers, the complex numbers and the quaternions. All three are algebras of directions: the complex numbers come from one direction whose square is minus one, the quaternions from two. The proof finds the quaternions as the most such directions can give, because a third direction is forced to be the product of the first two. Every other finite associative number system, including split-complex and dual numbers and all matrices, sits inside one of these algebras of directions, though the same could be said of matrices.

## one-liner
If $\R$ is a complete ordered field (premise (F4)): real polynomials have roots in $\Cl(0,1)$; a finite-dimensional associative real division algebra is a quotient of $\Cl(0,k)$, $k$ the dimension of its pure part, and the bivector $e_{1}e_{2}$ forces $k \in \{0,1,3\}$, so it is $\R$, $\Cl(0,1)$ or $\Cl(0,2)$; and every finite-dimensional associative real algebra embeds in a corner of $\Cl(k,k)$ through the matrix units $w_{I}fv_{J}^{\leftarrow}$.
