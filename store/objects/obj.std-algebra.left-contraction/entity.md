---
id: obj.std-algebra.left-contraction
kind: object
version: 1
title: The left contraction
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
  - key: HestenesSobczyk1984
    locator: Ch. 1 (geometric algebra)
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
extraction:
  by: algebra-core-2026-10-26
---

## formal
The \emph{left contraction} is the bilinear product defined on homogeneous elements by
\begin{equation}
A_r \rfloor B_s = \begin{cases} \langle A_r B_s \rangle_{s-r} & s \ge r, \\ 0 & s < r, \end{cases}
\end{equation}
extended bilinearly. It is the store's inner product. For vectors, $a \rfloor b = B(a, b)$; for a scalar, $\lambda \rfloor B = \lambda B$. (Doran and Lasenby use the symmetric inner product $\langle A_r B_s \rangle_{|r-s|}$ with scalars excluded; the two agree when $1 \le r \le s$.)

## technical
The left contraction of an $r$-vector onto an $s$-vector is the grade $s - r$ part of their geometric product, and zero when $r > s$. It is the inner product used throughout the store; between two vectors it is the polar form. It differs from Doran and Lasenby's symmetric inner product only when the left factor has higher grade, or is a scalar.

## lay
Contracting an arrow onto a plane removes the arrow's direction from the plane, leaving the arrow in the plane perpendicular to it. Contraction is the opposite of the outer product: it takes directions away rather than adding them.

## one-liner
$A_r \rfloor B_s = \langle A_r B_s \rangle_{s-r}$ for $s \ge r$, and $0$ otherwise; $a \rfloor b = B(a, b)$.
