---
id: synthesis.division-gives-the-rationals
kind: claim
version: 2
title: Division in the integer Clifford algebra gives the rationals
status: proved
region: synthesis
subject: clifford-structure
tags: [forcing-and-uniqueness, null-directions, clifford-classification]
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
founded_on:
- synthesis.premise-superposition-over-the-integers@2
lineage:
  motivated_by:
  - std-algebra.orthogonal-anticommute
  - std-algebra.inverse-of-vector
derivations:
- name: main
  uses: []
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_blade_product_is_the_twisted_rule
- kind: check
  ref: check.py::check_vector_invertible_exactly_when_its_square_is_a_unit
- kind: check
  ref: check.py::check_the_smallest_ring_of_division_is_the_rationals
- kind: check
  ref: check.py::check_invertibility_over_the_integers_mod_six
- kind: check
  ref: check.py::check_null_vectors_and_zero_divisors_survive_division
- kind: proof
  derivation: main
extraction:
  maintainer_pass_2026_11_08_foundation:
    by: ai-maintainer-pass
    note: >-
      Version 1 -> 2. Leon's decision of 8 November 2026: the foundation layer. Founded on synthesis.premise-superposition-over-the-integers: the algebra it is stated in rests on the foundation. Foundation postulates are reported as what a result rests on, separately from the premises it holds given (store/conventions.md, "The foundation").
  note: >-
    From Leon's working document "From the Bit to the Numbers" (7 November 2026), Step 4, the row
    "Q: inverses of non-unit vectors, v^{-1} = v/Q(v)", proved and checked here; not an attack on an
    open problem. The ring Cl_Z(p,q) is the integer Clifford algebra of the ladder's superposition step
    (the twisted group ring Z[G]/(c + 1) of clause (v) of
    synthesis.signed-directions-and-the-integer-clifford-algebra, filed alongside with the premises
    synthesis.premise-the-bit, synthesis.premise-minimal-non-commutativity and
    synthesis.premise-superposition-over-the-integers; the same twisting function f); it is defined
    here directly by its blade product, which is the product of Proposition
    std-algebra.orthogonal-anticommute with squares +-1, so the result does not depend on how that ring
    is reached. The product and the inverse are proved here directly; the stored propositions with the
    same rule and the same formula over the reals (std-algebra.orthogonal-anticommute,
    std-algebra.inverse-of-vector) are lineage and comparisons, not premises, so no real result enters
    the past cone of this integer and rational layer. When the entities filed alongside are accepted,
    the maintainer may add the integer-algebra result as a use or as lineage; the proof does not need
    it. Clause (ii) does not take Q as an ambient field: it shows that the coefficient rings in which
    the non-null integer vectors become invertible are exactly the Q-algebras, so Q is produced as the
    initial one. Clause (iii) is the rational counterpart of Theorem
    transport.exceptional-division-algebras (the same three exceptional signatures, now over Q, with
    integral witnesses). Ledger: transport-absent (elementary arithmetic of the integer and rational
    Clifford algebras).
---

## formal
Let $n = p + q \ge 1$, $N = \{p + 1, \dots, n\}$, and for a commutative ring $R$ let $\Cl_{R}(p,q)$ be the free $R$-module with basis the blades $e_{S}$, $S \subseteq \{1, \dots, n\}$ ($e_{\emptyset} = 1$), with the blade product
\[
e_{S}e_{T} = (-1)^{f(S,T)}\,e_{S \triangle T}, \qquad f(S,T) = \#\{(i,j) \in S \times T : i > j\} + |S \cap T \cap N| ,
\]
the same rule as Proposition \claimref{std-algebra.orthogonal-anticommute} gives over the reals for squares $Q(e_{i}) = 1$ ($i \le p$), $Q(e_{i}) = -1$ ($i \in N$). It is an associative unital $R$-algebra, $\Cl_{R}(p,q) = R \otimes_{\Z} \Cl_{\Z}(p,q)$, and for $v = \sum_{i} a_{i}e_{i}$ in $V_{R} = \bigoplus_{i} R\,e_{i}$, $v^{2} = Q(v) = \sum_{i \le p}a_{i}^{2} - \sum_{i \in N}a_{i}^{2}$.
\begin{enumerate}
\item[(i)] \emph{(Inverses.)} For a commutative ring $R$ and $v \in V_{R}$: $v$ has a left or a right inverse in $\Cl_{R}(p,q)$ if and only if $Q(v)$ is a unit of $R$, and then $v^{-1} = Q(v)^{-1}v$ is a two-sided inverse (the formula of Proposition \claimref{std-algebra.inverse-of-vector}).
\item[(ii)] \emph{(Division produces $\Q$.)} For a commutative ring $R$, every $v \in V_{\Z}$ with $Q(v) \ne 0$ becomes invertible in $\Cl_{R}(p,q)$ if and only if every nonzero integer is a unit of $R$, that is, $R$ is a $\Q$-algebra. So $\Q$ is the initial such ring, $\Cl_{\Q}(p,q)$ is the localisation of $\Cl_{\Z}(p,q)$ at the nonzero integers, and no subring of $\Q$ other than $\Q$ itself will do. Already the multiples $m e_{1}$, $m \ge 1$, force it: $Q(me_{1}) = \pm m^{2}$ and $e_{1}(me_{1})^{-1} = 1/m$, so every rational $a/m$ is the scalar $(ae_{1})(me_{1})^{-1}$, a product of an integer vector and the inverse of one. In $\Cl_{\Q}(p,q)$ every $v \in V_{\Q}$ with $Q(v) \ne 0$ is invertible, and the grade-$0$ part is $\Q\,1$.
\item[(iii)] \emph{(What division leaves.)} $V_{\Q}$ contains a nonzero null vector ($v^{2} = 0$, a zero divisor of $\Cl_{\Q}(p,q)$) if and only if $p \ge 1$ and $q \ge 1$, for example $e_{1} + e_{p+1}$. The algebra $\Cl_{\Q}(p,q)$ contains zero divisors if and only if $(p, q) \notin \{(0,0), (0,1), (0,2)\}$, with integral witnesses $(1 + e_{1})(1 - e_{1}) = 0$ for $p \ge 1$ and $(1 + e_{1}e_{2}e_{3})(1 - e_{1}e_{2}e_{3}) = 0$ for $p = 0$, $q \ge 3$; for $(p, q) \in \{(0,0), (0,1), (0,2)\}$, $x\bar{x} = \bar{x}x$ is the sum of the squares of the coefficients of $x$ ($\bar{x}$ the Clifford conjugate), so $\Cl_{\Q}(p,q)$ is a division ring. This is the list of Theorem \claimref{transport.exceptional-division-algebras}, now over $\Q$.
\end{enumerate}

## technical
Start from the integer Clifford algebra: integer combinations of the blades, multiplied by the usual sign rule with every direction squaring to $+1$ or $-1$. A vector $v$ squares to the integer $Q(v)$, so $v/Q(v)$ is its inverse wherever $Q(v)$ can be divided by; conversely, over any commutative ring of coefficients, an inverse of $v$ makes $v^{2} = Q(v)$ invertible and so forces $1/Q(v)$ into the ring. Since $m e_{1}$ squares to $\pm m^{2}$ and $e_{1}(me_{1})^{-1} = 1/m$, making every vector that is not null invertible makes every nonzero integer invertible: the rings that do this are exactly those containing the rationals, the rationals are the smallest, and every rational number is a product of an integer vector and the inverse of another. The rationals are thus produced by division, not assumed. Division does not remove null directions or zero divisors: over $\Q$ the indefinite algebras keep their null vectors, and the only rational Clifford algebras of $\pm 1$ forms without zero divisors are those of signatures $(0,0)$, $(0,1)$ and $(0,2)$, the same three as over the reals.

## lay
In the algebra built from whole-number combinations of directions, an arrow multiplied by itself gives a whole number. Undoing that multiplication means dividing by the number, and asking that every arrow which can be undone actually be undone forces in every fraction: dividing by an arrow three times as long as a unit arrow already produces one third. So the fractions are what division makes of the whole numbers. Division does not get rid of everything, though: in some of these algebras light-like arrows, which square to zero, survive it, and in all but three of them so do other elements whose product is zero.

## one-liner
In the integer Clifford algebra of a $\pm 1$ form, $v$ is invertible over a commutative ring $R$ exactly when $Q(v)$ is a unit of $R$, with $v^{-1} = v/Q(v)$; making every non-null integer vector invertible forces $R$ to be a $\Q$-algebra ($e_{1}(me_{1})^{-1} = 1/m$); null vectors remain exactly in the indefinite signatures ($p, q \ge 1$), and zero divisors in all but $\Cl_{\Q}(0,0)$, $\Cl_{\Q}(0,1)$, $\Cl_{\Q}(0,2)$.
