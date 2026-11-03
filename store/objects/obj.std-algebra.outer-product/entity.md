---
id: obj.std-algebra.outer-product
kind: object
version: 1
title: The outer product
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
- obj.std-algebra.grade-projection
locators:
  sources:
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
  - key: HestenesSobczyk1984
    locator: Ch. 1 (geometric algebra)
extraction:
  by: algebra-core-2026-10-26
---

## formal
The \emph{outer product} on $\Cl(V, Q)$ is the bilinear product defined on homogeneous elements by
\begin{equation}
A_r \wedge B_s = \langle A_r B_s \rangle_{r+s}, \qquad A_r \in \Cl^{r},\ B_s \in \Cl^{s},
\end{equation}
and extended bilinearly to all multivectors. Scalars act by ordinary multiplication: $\lambda \wedge B = \lambda B$.

## technical
The outer product of an $r$-vector and an $s$-vector is the top-grade part, grade $r + s$, of their geometric product; it is extended to general multivectors by bilinearity. It is defined directly from the geometric product and the grade projection, so it lives in the same algebra.

## lay
The outer product of two arrows is the oriented piece of plane they span; of an arrow and a plane, the oriented piece of volume. It keeps only the "new directions" part of the full product, and it vanishes when the factors share a direction.

## one-liner
$A_r \wedge B_s = \langle A_r B_s \rangle_{r+s}$, extended bilinearly.
