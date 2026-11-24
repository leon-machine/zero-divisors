---
id: synthesis.imported-stolz-level-of-real-projective-spaces-under-the-quarter-turn
kind: claim
version: 1
title: 'Imported: the level of real projective spaces under the quarter turn (Stolz 1989)'
status: imported
region: synthesis
subject: walls
tags: [classical-theorem]
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
imported_from:
- citation: 'S. Stolz, The level of real projective spaces, Comment. Math. Helv. 64 (1989), 661--674.'
  key: Stolz1989
  locator: 'the main theorem (stated for m >= 2); not read: taken from the zbMATH review (Zbl 0697.55009, by A. Pfister) and from the two quotations below; of the paper itself only the opening lines were seen, as an excerpt'
- citation: 'M. Furuta, Y. Kametani, H. Matsue and N. Minami, Homotopy theoretical considerations of the Bauer--Furuta stable homotopy Seiberg--Witten invariants, Geom. Topol. Monogr. 10 (2007), 155--166.'
  key: FurutaKametaniMatsueMinami2007
  locator: 'Definition 2.1 (the level of a free involution) and Example 2.2(ii), where the theorem is quoted; read on 24 November 2026 (arXiv:0903.4462)'
- citation: 'D. M. Meyer, Z/p-equivariant maps between lens spaces and spheres, Math. Ann. 312 (1998), 197--214.'
  key: Meyer1998
  locator: 'the introduction, where the theorem is quoted with s(1) = 2 and the three cases for m >= 2; read on 24 November 2026 in the author''s accepted manuscript'
extraction:
  note: >-
    Imported by Leon's decision of 24 November 2026, so that the rung count on the definite side of every
    quarter-turn lens wall is a stored theorem given it. NOT checked against the source: Stolz's paper was not
    read. The statement is taken from three secondary sources that agree: the published review of the paper,
    already quoted in the note of
    synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five (which gives the range
    $m \ge 2$ and remarks that the paper's two bounds do not coincide at $m \equiv 4$ modulo $8$ while the
    theorem lists $m + 2$), and Example 2.2(ii) of Furuta, Kametani, Matsue and Minami, read on 24 November 2026,
    which gives the same three cases for the level of $\mathbb{R}P^{2m-1} = S(\mathbb{C}^{m})/\langle i^{2}\rangle$ with the
    involution induced by multiplication by $i$ and states no range; and the introduction of Meyer (1998), read
    on 24 November 2026, which quotes the theorem as $s(1) = 2$ and the same three cases for $m \ge 2$, as exact
    values. The case $m \equiv 4$ modulo $8$ is the one to watch: the review says the paper's general lower and
    upper bounds do not coincide there, and how the paper settles that residue was not seen; all three sources
    list $m + 2$ there, and the second uses that value in a further estimate. The opening lines of the paper,
    seen as an excerpt only, announce the determination of the level and say in a footnote that M. C. Crabb
    proved the result by different arguments (Periodicity in Z/4-equivariant stable homotopy theory, Contemp.
    Math. 96 (1989), 109--124; not read). The range matters: at $m = 1$ the least $k$
    is $2$ (the map $z \mapsto z^{2}$ of the circle), not $3$, so the formula is imported for $m \ge 2$ only.
    Independent support in the store, which is not a check of the source: the values at $m = 2$ and $m = 3$ are
    stored theorems ($3$ on $L(4,1)$ with a definite side; $5$ on $L^{5}(4)$, given the imported Steenrod Fact),
    and for every $m \ge 2$ the formula lies between the stored lower bound from complex K-theory and the stored
    upper bound $\lceil 3m/2 \rceil$ from explicit maps, which it meets at $m = 2, 3, 4, 6$. Not part of this
    Fact: any statement on indefinite sides, on groups other than the quarter turn, or on how the theorem is
    proved. Topological: a statement about continuous maps of spheres, written in its source's language except
    that the involution is written with the quarter-turn bivector.
outside_ga:
  kind: imported
  why: 'A theorem of equivariant homotopy theory (the least dimension of a sphere receiving a map that changes sign under the quarter turn), taken from the literature; the quarter turn is written in geometric algebra, the theorem and its proof have no geometric-algebra form here.'
---

## formal
Taken from secondary sources and not checked against the source (see the note). Let $m \ge 2$, let $J(v) = v \cdot B$ with $B = e_{1}e_{2} + e_{3}e_{4} + \dots + e_{2m-1}e_{2m}$ in $\Cl(2m, 0)$ be the quarter turn in every coordinate plane of $\R^{2m}$, and let $s(m)$ be the least $k$ for which there is a continuous map
\[
F : S^{2m-1} \to \R^{k} \setminus \{0\}, \qquad F(J(v)) = -F(v).
\]
Equivalently (since $F(-v) = F(J(J(v))) = F(v)$, and after dividing $F$ by its length) $s(m)$ is the \emph{level} of the real projective space $\mathbb{R}P^{2m-1} = S^{2m-1}/\{\pm 1\}$ with the free involution induced by $J$: the least $k$ with a continuous map $\mathbb{R}P^{2m-1} \to S^{k-1}$ that carries the involution to the antipodal map. Then
\[
s(m) = \begin{cases} m + 1 & m \equiv 0, 2 \pmod 8, \\ m + 2 & m \equiv 1, 3, 4, 5, 7 \pmod 8, \\ m + 3 & m \equiv 6 \pmod 8. \end{cases}
\]
At $m = 1$ the least $k$ is $2$, and the formula is not asserted there. The published review of the paper reports that the paper's general lower and upper bounds do not coincide for $m \equiv 4 \pmod 8$, while it lists the value $m + 2$ there, as do the two later papers that quote the theorem; how the paper settles that case was not seen.

## technical
A free involution on a space has a level: the least dimension, plus one, of a sphere with the antipodal map that receives an equivariant map from it. The Borsuk-Ulam theorem says the level of the $d$-sphere with the antipodal map is $d + 1$. Real projective space of odd dimension $2m - 1$ carries the free involution induced by a complex structure of $\R^{2m}$, here the quarter turn in every coordinate plane, and Stolz computed its level: $m + 1$, $m + 2$ or $m + 3$ according to the residue of $m$ modulo $8$, for $m \ge 2$. In the store's terms this is the least number of components of a map of the sphere $S^{2m-1}$ that changes sign under the quarter turn. The statement is taken from the published review of the paper and from two later papers that quote it; the paper itself was not read, and the residue $m \equiv 4$ modulo $8$, where by the review the paper's general bounds differ, is taken as listed.

## lay
Take a sphere in a space of even dimension and turn it by a quarter turn in every coordinate plane at once. How many numbers must a continuous, never-vanishing list of numbers on the sphere have, if the whole list is to change sign under that turn? A theorem of Stolz from 1989 gives the answer in every dimension: roughly half the dimension of the space plus one, two or three, in a pattern that repeats with period eight. The store takes this theorem from the literature without re-proving it.

## one-liner
Imported (Stolz 1989, through its review and two later quotations; the paper not read; the case $m \equiv 4$ modulo $8$ as listed, the review noting that the paper's general bounds differ there): for $m \ge 2$ the least $k$ with a continuous $F : S^{2m-1} \to \R^{k} \setminus \{0\}$, $F(J(v)) = -F(v)$, $J$ the quarter turn in every coordinate plane, equivalently the level of $\mathbb{R}P^{2m-1}$ under the involution induced by $J$, is $m + 1$ for $m \equiv 0, 2$, $m + 2$ for $m \equiv 1, 3, 4, 5, 7$ and $m + 3$ for $m \equiv 6$ modulo $8$.
