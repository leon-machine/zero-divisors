---
id: note.one-relation.two-presentations-differ-over-the-integers
kind: note
version: 1
title: The two presentations differ over the integers
status: remark
subject: one-relation
proposed_by:
  kind: ai
  session: 2026-11-06-edge-normality
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-06-edge-normality
comments_on:
- one-relation.two-presentations
- std-algebra.cl11-matrix
extraction:
  note: >-
    From Leon's working document "Scalars and the Continuum: Review and Extensions" (6 November 2026),
    the item on integral orders of the (1,1) plane. Recorded as a remark because the content is classical (the Clifford algebra of the hyperbolic quadratic module over the
    integers is the integer matrix ring, as for any hyperbolic module over a commutative ring, Bass,
    Amer. J. Math. 96 (1974), and Knus, Quadratic and Hermitian Forms over Rings (1991); the integer
    matrices are a maximal order, Reiner, Maximal Orders; all cited from memory) and new to the store
    only as a reading of Proposition one-relation.two-presentations. Every statement was verified in
    exact arithmetic with GA.py (closure and integer structure constants of both
    spans, the matrix isomorphism, change-of-basis determinant 4, twice the null order inside the
    orthogonal one, no idempotents but 0 and 1 in the orthogonal order on a box, the ten nontrivial
    idempotents of the null order with coordinates in {-1, 0, 1} all of scalar part 1/2), and recomputed independently with plain integer matrices. A note carries no check. Ledger: transport-convenient
    reading (the null pair is the ascent's hyperbolic pair).
---

## formal
Proposition \claimref{one-relation.two-presentations} says that an orthogonal basis and a Witt basis generate the same algebra; this holds over every ring containing $\tfrac12$, and over the integers it fails. In $\Cl(1,1)$ let $e_{+}, e_{-}$ be orthonormal with $Q(e_{+}) = 1$, $Q(e_{-}) = -1$, and $a = \tfrac12(e_{+} + e_{-})$, $a' = \tfrac12(e_{+} - e_{-})$, so $a^{2} = a'^{2} = 0$ and $aa' + a'a = 1$. The integer span $\Lambda_{W}$ of the products of $a, a'$ is $\Z \oplus \Z a \oplus \Z a' \oplus \Z aa'$, and with $a, a', aa', a'a$ as the matrix units $E_{12}, E_{21}, E_{11}, E_{22}$ it is $\Mat_{2}(\Z)$, the integer form of Proposition \claimref{std-algebra.cl11-matrix}, with the integral idempotents $aa'$ and $a'a$. The integer span $\Lambda_{O}$ of the products of $e_{+}, e_{-}$ is $\Z \oplus \Z e_{+} \oplus \Z e_{-} \oplus \Z e_{+}e_{-}$, the matrices $\begin{psmallmatrix} \alpha & \beta \\ \gamma & \delta \end{psmallmatrix}$ with $\alpha \equiv \delta$ and $\beta \equiv \gamma \bmod 2$, a subring of index $4$ with $2\Lambda_{W} \subset \Lambda_{O}$, so $\Lambda_{O}[\tfrac12] = \Lambda_{W}[\tfrac12]$. Writing $x = \alpha + \beta e_{+} + \gamma e_{-} + \delta e_{+}e_{-}$, $x^{2} = (\alpha^{2} + \beta^{2} - \gamma^{2} + \delta^{2}) + 2\alpha(\beta e_{+} + \gamma e_{-} + \delta e_{+}e_{-})$, so every idempotent other than $0, 1$ has scalar part $\tfrac12$, and $\Lambda_{O}$, whose elements have integer scalar parts, has no idempotent other than $0$ and $1$; the idempotents $\tfrac12(1 \pm e_{+})$ of the orthogonal reading need $\tfrac12$. On the vector lattices the two presentations agree over $\Z[\tfrac12]$; over $\Z$ the null lattice $\Z a + \Z a'$, with $Q(xa + ya') = xy$ and the polar form $Q(u + v) - Q(u) - Q(v)$, is the even unimodular lattice $\mathrm{II}_{1,1}$ (the hyperbolic quadratic module, nonsingular), while the orthonormal lattice $\Z e_{+} + \Z e_{-}$, of index $2$ in it, is unimodular only for the half-polar form $B$, the odd lattice $\mathrm{I}_{1,1}$, and as a quadratic module it is singular at $2$ (polar determinant $-4$). So the metric chart and the CAR chart of the one relation are one object over the rationals and two different orders over the integers, and only the CAR chart contains the matrix units.

## technical
Over any ring containing one half, the orthogonal pair $e_{\pm}$ and the null pair $a, a'$ of the hyperbolic plane generate the same algebra. Over the integers they generate different rings: the null pair gives all integer $2 \times 2$ matrices, with $aa'$ and $a'a$ as integral idempotents, while the orthogonal pair gives a subring of index $4$ with no idempotents at all, because every nontrivial idempotent of the plane has scalar part one half. On the vectors this is the difference between the even unimodular lattice $\mathrm{II}_{1,1}$ in the polar normalisation and the odd unimodular lattice $\mathrm{I}_{1,1}$ in the half-polar one.

## lay
The flat plane with one time-like and one space-like direction can be described with two directions of opposite sign or with two light-like directions. With fractions allowed both descriptions build the same structure. With only whole numbers they do not: the light-like description builds all whole-number $2 \times 2$ matrices, including the elements that act as projections, while the other builds a smaller ring with no projections at all, because those need a factor of one half.

## one-liner
Over $\Z$ the null pair of the hyperbolic plane generates $\Mat_{2}(\Z)$ with integral idempotents $aa'$, $a'a$, while the orthonormal pair generates an index-$4$ suborder with no idempotents; the two presentations of the one relation agree only once $\tfrac12$ is allowed ($\mathrm{II}_{1,1}$ versus $\mathrm{I}_{1,1}$).
