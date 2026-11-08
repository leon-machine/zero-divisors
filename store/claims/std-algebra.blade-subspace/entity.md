---
id: std-algebra.blade-subspace
kind: claim
version: 2
title: Blades and subspaces
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- grading-and-parity
- degenerate-algebras
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
- name: Claude Opus 5.5
  role: 'maintainer pass, citation of the retired imported Fact repointed to its derivation in geometric algebra'
  version: 2
  source: run 2026-11-07-bit-root
review: typed
trust: ai-proposed
about:
- obj.std-algebra.blade
derivations:
- name: main
  uses:
  - std-algebra.exterior-isomorphism@2
  - synthesis.completion-recovers-the-real-clifford-algebras@1
  - std-algebra.involution-properties@1
  - std-algebra.grade-decomposition@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_blades_and_subspaces
locators:
  sources:
  - key: HestenesSobczyk1984
    locator: Ch. 1 (geometric algebra)
  - key: Lounesto2001
    locator: Ch. 3 (bivectors and the exterior algebra)
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
extraction:
  maintainer_pass_2026_11_08:
    by: ai-maintainer-pass
    note: >-
      Version 1 -> 2. Leon's decision of 7 November 2026: the imported Fact std-algebra.sylvester-inertia is retired, replaced by synthesis.completion-recovers-the-real-clifford-algebras, whose clause (iii) derives Sylvester's law of inertia in geometric algebra over any Euclidean field, the reals included; the citation and edge now point there. The check's premise() call names the new result; nothing else changed.
  referee_fixes: '2026-10-26: (iv) covers dependent factors and invertibility is stated for nonzero blades; check label says dim [A] = k, which is what it tests (referee part 1, point 3).'
  by: algebra-core-2026-10-26
---

## formal
Let $v_1, \dots, v_k \in V$ and $A = v_1 \wedge \dots \wedge v_k$.
\begin{enumerate}
\item[(i)] $A \ne 0$ if and only if $v_1, \dots, v_k$ are linearly independent; then $[A] = \operatorname{span}(v_1, \dots, v_k)$.
\item[(ii)] Two nonzero $k$-blades have the same subspace if and only if they are proportional; nonzero $k$-blades up to scale correspond to $k$-dimensional subspaces of $V$.
\item[(iii)] A nonzero $k$-vector $Y$ satisfies $\dim\{x \in V : x \wedge Y = 0\} \le k$, with equality if and only if $Y$ is a blade.
\item[(iv)] $A \tilde{A} = \det\bigl[B(v_i, v_j)\bigr]_{i,j=1}^{k}$, the Gram determinant (both sides are $0$ when the $v_i$ are dependent). So a nonzero blade $A$ is invertible, with $A^{-1} = \tilde{A} / (A\tilde{A})$, if and only if $[A]$ is nondegenerate; if $A \ne 0$ and $[A]$ is degenerate, then $A \tilde{A} = 0$ and $A$ is a zero divisor.
\end{enumerate}

## technical
An outer product of vectors vanishes exactly when they are dependent, and otherwise remembers their span and nothing more than an overall scale. A $k$-vector is a blade exactly when $k$ independent vectors have zero outer product with it. A blade times its reverse is the Gram determinant of its factors: so a blade is invertible precisely when its subspace is nondegenerate, and a blade of a degenerate subspace is a zero divisor.

## lay
A blade knows which flat it spans and nothing else except its size and orientation. Its square length is the familiar Gram determinant. If the flat contains a direction that is perpendicular to the whole flat, as a light ray lying in a plane can be, the blade has zero square length and cannot be inverted: it becomes one of the zero divisors that the Transport Papers study.

## one-liner
$v_1 \wedge \dots \wedge v_k \ne 0$ iff the $v_i$ are independent, blades up to scale are subspaces, and $A\tilde{A}$ is the Gram determinant, so a degenerate blade is a zero divisor.
