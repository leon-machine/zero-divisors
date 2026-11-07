---
id: std-algebra.complexification-is-the-odd-extension
kind: claim
version: 2
title: 'Complexification is the odd extension'
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags: [pseudoscalar-and-centre, clifford-classification]
proposed_by:
  kind: ai
  session: maintainer-2026-11-07
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: maintainer pass 2026-11-07
- name: Claude Opus 5.5
  role: 'consistency pass, even subalgebra written Cl^+ as in the standard-algebra objects'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - odd-extensions.volume-element-odd-dimension@4
  - primer.centre@2
  - odd-extensions.doubling-or-complexification@6
  - std-algebra.complexification@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_added_vector_makes_a_central_unit
- kind: check
  ref: check.py::check_complexification_map_is_an_isomorphism
- kind: check
  ref: check.py::check_complex_vectors_and_shifted_squares
- kind: check
  ref: check.py::check_relation_to_the_right_unit
- kind: proof
  derivation: main
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Notation: the even subalgebra was written Cl^0(W), against obj.std-algebra.grade-projection (Cl^0 = R, grade zero) and obj.std-algebra.even-subalgebra (Cl^+); now Cl^+, with the cited T14a theorem''s Cl^0 named once. Mathematics unchanged.'
  note: >-
    The complexification of a Clifford algebra of even dimension, written inside real geometric
    algebra: adjoining one orthogonal vector of the right square makes the new pseudoscalar a
    central element of square -1, and the algebra of the extended space is the complexification with
    that pseudoscalar as its unit. It is the unit the store uses wherever a complex number must
    commute with vectors (complexified spaces, complex null vectors, tube points, shifts of a
    spacetime vector). The spacetime instance of (ii) is stored as
    odd-extensions.four-extensions-oriented-pair (row this world + time) and
    odd-extensions.mirror-inside-complexified-extension-absent-doubled (iii); this result is its
    general even-dimensional form, with (iii), (iv), the conformal instance and the odd-dimensional
    remark (vi) added. Pure algebra on four stored results of Clifford structure; no physical premise.
    Transport-absent. Literature cited from memory, as orientation only: that an odd-dimensional
    Clifford algebra whose pseudoscalar squares to -1 is a complexification is classical (Porteous,
    Clifford Algebras and the Classical Groups, 1995; Lounesto, Clifford Algebras and Spinors, 2001).
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Created at Leon''s instruction of 7 November 2026 to resolve every imaginary unit (colony/runs/2026-11-07-ga-units/RESOLVE.md, unit principle U3): the core result the sweep cites when it writes a complexification that must commute with vectors with the unit I_5 = I_4 e of Cl(2,3) or I_7 = I_6 e of Cl(3,4). Clause (iv) states, and does not assume, how I_5 and I_7 relate to the field theory''s unit I_4 and the conformal spinors'' unit I_6: through a choice of idempotent, so with a sign, and never by identification. Referee fixes of 7 November 2026, folded into version 1: the stored spacetime instance is named in the note; formal (ii) says the splitting is of real vector spaces with Cl(V) a real subalgebra commuting with I_W; clause (vi), complexification in odd dimension through V + Rf, is added with a check on Cl(1,2) in Cl(2,3).'
---

## formal
Let $(V, Q)$ be a nondegenerate real quadratic space of even dimension $n \geq 2$, with an orthonormal basis $e_{1}, \dots, e_{n}$ ($Q(e_{k}) = \pm 1$, $q$ of them $-1$) and pseudoscalar $I_{V} = e_{1}\cdots e_{n}$, so that $I_{V}^{2} = \varepsilon_{V} := (-1)^{n(n-1)/2 + q}$. Let $W = V \oplus \R e$ with $e$ orthogonal to $V$ and $Q(e) = -\varepsilon_{V}$, and $I_{W} = I_{V}e$. Then:
\begin{enumerate}
\item[(i)] \emph{(The unit.)} $I_{W}^{2} = -1$, and this is the only sign of $Q(e)$ that gives it ($Q(e) = +\varepsilon_{V}$ gives $I_{W}^{2} = +1$). $I_{W}$ commutes with every vector of $W$, so it is central in $\Cl(W)$, and the centre of $\Cl(W)$ is $\mathrm{span}\{1, I_{W}\}$, a field isomorphic to $\C$.
\item[(ii)] \emph{(The complexification.)} The multiplication map $\Cl(V) \otimes_{\R} \mathrm{span}\{1, I_{W}\} \to \Cl(W)$, $a \otimes z \mapsto az$, is an isomorphism of real algebras; equivalently $\Cl(W) = \Cl(V) \oplus \Cl(V)I_{W}$ as real vector spaces, with $\Cl(V)$ a real subalgebra commuting with $I_{W}$, and $e_{k} \mapsto e_{k}$ with the complex unit sent to $I_{W}$ extends to an isomorphism from the complexification of $\Cl(V)$ onto $\Cl(W)$. So $\Cl(W)$ is the complexification of $\Cl(V)$ with complex unit $I_{W}$, a full matrix algebra of size $2^{n/2}$ over the field $\mathrm{span}\{1, I_{W}\}$ (Theorem \claimref{std-algebra.complexification}(i)). Also $\Cl(W) = \Cl^{+}(W) \oplus \Cl^{+}(W)I_{W}$ (Theorem \claimref{odd-extensions.doubling-or-complexification}(ii)): the even subalgebra of $W$ is a second real form with the same complexification.
\item[(iii)] \emph{(Complex vectors and shifted squares.)} Write $V_{\C} = V \oplus I_{W}V$. For $a, b \in V$, $(a + I_{W}b)^{2} = Q(a) - Q(b) + 2\ip{a}{b}\,I_{W}$, so squaring in $\Cl(W)$ is the complex-bilinear extension of $Q$ to $V_{\C}$, with values in $\mathrm{span}\{1, I_{W}\}$; $a + I_{W}b$ is null if and only if $Q(a) = Q(b)$ and $\ip{a}{b} = 0$. In particular, for $y, a \in V$ and real $\epsilon$, $(y + \epsilon I_{W}a)^{2} = Q(y) - \epsilon^{2}Q(a) + 2\epsilon\ip{y}{a}\,I_{W}$: a scalar function of the square of a shifted vector (a polynomial, a quotient, or a power series in that square with coefficients in $\mathrm{span}\{1, I_{W}\}$) is the same function evaluated at a number of the field $\mathrm{span}\{1, I_{W}\}$, the shift written in that field, and since $I_{W}$ is central it may be read as the complex unit of any such scalar computation.
\item[(iv)] \emph{(Relation to the unit of $V$.)} Suppose $\varepsilon_{V} = -1$, so $Q(e) = +1$, and let $P_{\pm} = \tfrac12(1 \pm e)$. These are idempotents commuting with $I_{V}$; $x \mapsto xP_{\pm}$ is an injective map of left $\Cl(V)$-modules from $\Cl(V)$ onto the left ideal $\Cl(W)P_{\pm}$, and
\[
(xP_{\pm})\,I_{W} = \pm (xI_{V})\,P_{\pm} \qquad (x \in \Cl(V)) .
\]
So under $x \mapsto xP_{\pm}$ the unit $I_{W}$ is the right unit $x \mapsto \pm xI_{V}$; on even $x$ it is also the left unit $\pm I_{V}x$, and on a vector $x$, $(I_{V}x)P_{\pm} = \mp(xP_{\pm})I_{W}$. The sign is fixed only by the choice of idempotent, so $I_{W}$ and $I_{V}$ are two units and are not identified.
\item[(v)] \emph{(Instances.)} For spacetime $\Cl(1,3)$, $I_{4}^{2} = -1$: $Q(e) = +1$, $\Cl(W) = \Cl(2,3)$, the unit is $I_{5} = I_{4}e$; $e_{2} + I_{5}e_{3}$ is a complex null vector, $(y + \epsilon I_{5}e_{0})^{2} = Q(y) - \epsilon^{2} + 2\epsilon y_{0}I_{5}$ with $y_{0} = \ip{y}{e_{0}}$, and under $x \mapsto xP_{+}$, $I_{5}$ is the right unit $x \mapsto xI_{4}$, which is $I_{4}$ on even values. For conformal space $\Cl(2,4)$ with $I_{6} = I_{4}e_{+}e_{-}$, $I_{6}^{2} = -1$: $Q(e) = +1$, $\Cl(W) = \Cl(3,4)$, the unit is $I_{7} = I_{6}e$, and under $x \mapsto xP_{+}$, $I_{7}$ is right multiplication by $I_{6}$.
\item[(vi)] \emph{(Odd dimension.)} If $\dim V$ is odd, choose $f$ orthogonal to $V$ with $Q(f) = \pm 1$ and apply the above to $V' = V \oplus \R f$, with unit $I_{W'}$, $W' = V' \oplus \R e$: the multiplication map $\Cl(V) \otimes_{\R} \mathrm{span}\{1, I_{W'}\} \to \Cl(W')$ is an injective homomorphism, so the complexification of $\Cl(V)$ is the subalgebra $\Cl(V) \oplus \Cl(V)I_{W'}$ of $\Cl(W')$, with unit $I_{W'}$.
\end{enumerate}

## technical
Complexifying a Clifford algebra needs no imaginary unit from outside. If $V$ has even dimension, adjoin one vector $e$ orthogonal to it with $Q(e) = -I_{V}^{2}$. The pseudoscalar $I_{W} = I_{V}e$ of the larger space then squares to $-1$ and commutes with every vector, so it is central, and the centre is exactly $\mathrm{span}\{1, I_{W}\}$, a copy of the complex numbers. The algebra of the larger space splits as $\Cl(V) \oplus \Cl(V)I_{W}$, which is the complexification of $\Cl(V)$ with $I_{W}$ as its unit. Complex vectors are $a + I_{W}b$, whose square is the complex-bilinear extension of $Q$, so complex null vectors such as $e_{2} + I_{5}e_{3}$ and shifted vectors such as $y + \epsilon I_{5}e_{0}$ are elements of the real algebra, and every scalar function of such a square is computed in the field $\mathrm{span}\{1, I_{W}\}$. For spacetime the extension is $\Cl(2,3)$ with $I_{5} = I_{4}e$; for conformal space it is $\Cl(3,4)$ with $I_{7} = I_{6}e$. The new unit is not the old one: through the idempotent $\tfrac12(1 + e)$ it acts as right multiplication by $I_{4}$ (or $I_{6}$), and through $\tfrac12(1 - e)$ as its negative, so the relation carries a sign and the units are kept apart.

## lay
Complex numbers enter physics wherever something must rotate by a quarter turn and square to minus one. In geometric algebra such elements can be built from directions alone, but in four-dimensional spacetime none of them commutes with every direction, as an ordinary number must. Adding one extra direction of the right kind fixes this: the oriented volume of the five directions together squares to minus one and commutes with everything, so it behaves exactly as the imaginary unit does. This result proves that, shows that the algebra of the five directions is precisely the complexified algebra of the four, and works out the same construction for the six-dimensional conformal space used elsewhere in the graph.

## one-liner
For $V$ of even dimension, adjoining $e \perp V$ with $Q(e) = -I_{V}^{2}$ makes $I_{W} = I_{V}e$ central with square $-1$ and $\Cl(V \oplus \R e) = \Cl(V) \oplus \Cl(V)I_{W}$ the complexification of $\Cl(V)$ with unit $I_{W}$ ($I_{5} = I_{4}e$ in $\Cl(2,3)$, $I_{7} = I_{6}e$ in $\Cl(3,4)$), which acts through $\tfrac12(1 \pm e)$ as the right unit $\pm I_{V}$.
