---
id: std-algebra.inverse-of-vector
kind: claim
version: 1
title: Which vectors and versors are invertible
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- null-directions
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
review: typed
trust: ai-proposed
about:
- obj.std-algebra.clifford-algebra
derivations:
- name: main
  uses:
  - std-algebra.vector-squares@1
  - std-algebra.blade-basis@1
  - std-algebra.involution-properties@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_invertible_iff_nonnull
- kind: check
  ref: check.py::check_versor_norm
locators:
  sources:
  - key: DoranLasenby2003
    locator: 'Ch. 4 (foundations of geometric algebra: rotors, versors)'
  - key: Lounesto2001
    locator: Ch. 17 (spin groups and spinor spaces)
extraction:
  by: algebra-core-2026-10-26
---

## formal
In $\Cl(V, Q)$, a vector $v$ is invertible if and only if $Q(v) \ne 0$, and then $v^{-1} = v / Q(v)$. A nonzero null vector satisfies $v^{2} = 0$: it is a zero divisor. A \emph{versor} is a product $g = u_1 u_2 \cdots u_k$ of invertible vectors; it satisfies
\begin{equation}
g \tilde{g} = \tilde{g} g = Q(u_1) Q(u_2) \cdots Q(u_k) \ne 0,
\end{equation}
so $g$ is invertible with $g^{-1} = \tilde{g} / \bigl(Q(u_1) \cdots Q(u_k)\bigr)$. None of this needs the form to be nondegenerate.

## technical
A vector has an inverse exactly when its square $Q(v)$ is nonzero, and the inverse is $v/Q(v)$. A null vector that is not zero squares to zero, so it is a zero divisor and has no inverse. A product of invertible vectors, a versor, times its reverse is the product of the squares of its factors, a nonzero scalar, which gives its inverse explicitly. This holds in degenerate algebras too.

## lay
An arrow can be "divided by" exactly when its square length is not zero. Arrows of zero length, like light rays, cannot be inverted: multiplying such an arrow by itself gives zero. Products of invertible arrows are always invertible, and their inverse is found by writing the product backwards and dividing by a number.

## one-liner
$v$ is invertible iff $Q(v) \ne 0$, with $v^{-1} = v/Q(v)$; a versor $g = u_1 \cdots u_k$ has $g\tilde{g} = \prod Q(u_i)$.
