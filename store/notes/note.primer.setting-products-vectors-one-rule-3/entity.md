---
id: note.primer.setting-products-vectors-one-rule-3
kind: note
version: 1
title: Products of vectors, and the one rule
status: setting
subject: clifford-structure
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T00, deposited version
comments_on:
- primer.commutation-rule
locators:
  paper: T00
  number: Setting
  section: Products of vectors, and the one rule
  line: 213
---

## formal
\textbf{The outer product answers the first.} Grassmann's answer, published in 1844, was to let the plane element be the object itself rather than a perpendicular substitute for it. The \emph{outer product} $a \wedge b$ is the oriented parallelogram spanned by $a$ and $b$: a plane, an area $|a|\,|b| \sin\theta$, and a sense of circulation around it. Exchanging the factors reverses that sense, so the product is antisymmetric,
\[
a \wedge b \;=\; -\, b \wedge a , \qquad \text{and in particular} \qquad a \wedge a \;=\; 0 .
\]
Only the plane, the area and the sense are recorded, not the particular parallelogram: $a \wedge (b + \lambda a) = a \wedge b$ for every scalar $\lambda$, so sliding one edge along the other changes nothing. Because the definition never mentions a perpendicular direction, it makes sense in every dimension. The object it produces is a \emph{bivector}, and it is not a vector. In three dimensions a bivector carries the same information as $a \times b$, which is why the cross product serves so well there, and why it does not generalise.

The construction does not stop at two vectors. The outer product is associative, so three vectors give $a \wedge b \wedge c$, the oriented parallelepiped they span: a three-dimensional subspace, the volume of that parallelepiped, and a handedness. That object is a \emph{trivector}. Four vectors give an oriented four-dimensional volume, and so on, the outer product of $k$ independent vectors representing the oriented $k$-dimensional subspace they span, weighted by its $k$-dimensional content. The antisymmetry that gave $a \wedge a = 0$ makes the outer product of any linearly dependent set vanish, so in an $n$-dimensional space the sequence ends at $k = n$: scalars, vectors, bivectors, trivectors, and upward to a single top object with nothing above it. That ceiling is not a convention. It is the statement that any $n+1$ vectors of an $n$-dimensional space are dependent.

## technical
pending

## lay
pending

## one-liner
pending
