---
id: std-algebra.contraction-expansion
kind: claim
version: 1
title: Contraction by a vector is a derivation
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- grading-and-parity
proposed_by:
  kind: ai
  session: algebra-core-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: typed
trust: ai-proposed
about:
- obj.std-algebra.left-contraction
- obj.std-algebra.outer-product
derivations:
- name: main
  uses:
  - std-algebra.product-decomposition@1
  - std-algebra.exterior-isomorphism@1
  - std-algebra.involution-properties@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_contraction_derivation_and_expansion
locators:
  sources:
  - key: HestenesSobczyk1984
    locator: Ch. 1 (geometric algebra)
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
  - key: Chevalley1954
    locator: Ch. II (the Clifford algebra of a quadratic space)
extraction:
  by: algebra-core-2026-10-26
---

## formal
For $a \in V$ and $X, Y \in \Cl(V, Q)$:
\begin{align}
a \rfloor (X Y) &= (a \rfloor X) Y + \hat{X} (a \rfloor Y), \\
a \rfloor (X \wedge Y) &= (a \rfloor X) \wedge Y + \hat{X} \wedge (a \rfloor Y), \\
a \rfloor (a \rfloor X) &= 0 .
\end{align}
Under the isomorphism $\Phi$ of \claimref{std-algebra.exterior-isomorphism}, $a \rfloor$ is the interior product of $\Lambda V$ with the linear form $B(a, \cdot)$. Consequently
\begin{equation}
a \rfloor (b_1 \wedge \dots \wedge b_k) = \sum_{i=1}^{k} (-1)^{i-1} B(a, b_i)\, b_1 \wedge \dots \wedge \check{b}_i \wedge \dots \wedge b_k,
\end{equation}
where $\check{b}_i$ means $b_i$ is omitted.

## technical
Contraction by a vector obeys a graded Leibniz rule, both for the geometric product and for the outer product, and applying it twice gives zero. Seen through the exterior algebra it is the familiar interior product with the form $B(a, \cdot)$. For a blade, contraction by $a$ produces the alternating sum over its factors, each term pairing $a$ with one factor and deleting it.

## lay
Contracting an arrow onto a product of arrows works one factor at a time: pair the arrow with each factor in turn, remove that factor, and add up with alternating signs, as in expanding a determinant along a row.

## one-liner
$a \rfloor$ is a graded derivation of both products with $(a \rfloor)^{2} = 0$, so $a \rfloor (b_1 \wedge \dots \wedge b_k) = \sum_i (-1)^{i-1} B(a, b_i)\, b_1 \wedge \dots \check{b}_i \dots \wedge b_k$.
