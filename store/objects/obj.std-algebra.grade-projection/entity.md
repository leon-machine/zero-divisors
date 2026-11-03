---
id: obj.std-algebra.grade-projection
kind: object
version: 1
title: Grades and grade projection
status: defined
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
- obj.std-algebra.clifford-algebra
locators:
  sources:
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
  - key: Lounesto2001
    locator: Ch. 14 (definitions of the Clifford algebra)
extraction:
  by: algebra-core-2026-10-26
---

## formal
For $v_1, \dots, v_k \in V$ the \emph{antisymmetrised product} is $[v_1, \dots, v_k] = \frac{1}{k!} \sum_{\sigma \in S_k} \operatorname{sgn}(\sigma)\, v_{\sigma(1)} \cdots v_{\sigma(k)}$. The \emph{grade-$k$ subspace} $\Cl^{k}(V, Q)$ is the span of all antisymmetrised products of $k$ vectors ($\Cl^{0} = \R$). An element of $\Cl^{k}$ is a $k$-vector; a sum of $k$-vectors over several $k$ is a \emph{multivector}. By \claimref{std-algebra.grade-decomposition}, $\Cl(V, Q) = \bigoplus_{k=0}^{n} \Cl^{k}$, and $\langle x \rangle_k$ denotes the component of $x$ in $\Cl^{k}$, the \emph{grade-$k$ projection}. Grade $0$ is the \emph{scalar part}.

## technical
Grade is defined without choosing a basis: the grade-$k$ part of the algebra is spanned by the fully antisymmetrised products of $k$ vectors. For mutually orthogonal vectors the antisymmetrised product is just the product. The algebra is the direct sum of its grades, and $\langle x \rangle_k$ picks out the grade-$k$ component: scalars, vectors, bivectors and so on.

## lay
Elements of the algebra come in grades: numbers are grade zero, arrows grade one, oriented plane pieces grade two, oriented volumes grade three, and so on. Any element is a sum of parts of definite grade, and projecting picks out one of them.

## one-liner
$\Cl^{k}$ is spanned by antisymmetrised products of $k$ vectors, $\Cl = \bigoplus_k \Cl^{k}$, and $\langle x \rangle_k$ is the grade-$k$ component.
