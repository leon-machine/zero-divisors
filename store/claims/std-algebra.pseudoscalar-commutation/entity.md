---
id: std-algebra.pseudoscalar-commutation
kind: claim
version: 1
title: How the pseudoscalar commutes
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- pseudoscalar-and-centre
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
- obj.std-algebra.pseudoscalar
derivations:
- name: main
  uses:
  - std-algebra.orthogonal-anticommute@1
  - std-algebra.grade-decomposition@2
  - primer.sign@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_pseudoscalar_commutation
locators:
  sources:
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
  - key: Lounesto2001
    locator: Ch. 22 (Chevalley's construction)
extraction:
  referee_fixes: '2026-10-26: wording in (i): "while" (referee part 2, point 5).'
  by: algebra-core-2026-10-26
---

## formal
In $\Cl(p, q, r)$, $n = p + q + r$, with unit pseudoscalar $I$:
\begin{enumerate}
\item[(i)] $I X_k = (-1)^{k(n-1)} X_k I$ for $X_k \in \Cl^{k}$; so $I$ commutes with $\Cl^{+}$, and with $\Cl^{-}$ when $n$ is odd, while it anticommutes with $\Cl^{-}$ when $n$ is even. Equivalently $I X = X I$ for $n$ odd and $I X = \hat{X} I$ for $n$ even.
\item[(ii)] $I \tilde{I} = \prod_{i} Q(e_i)$, which is $(-1)^{q}$ when $r = 0$ and $0$ when $r > 0$.
\item[(iii)] $I^{2} = (-1)^{n(n-1)/2} (-1)^{q}$ when $r = 0$ (\claimref{primer.sign}), and $I^{2} = 0$ when $r > 0$: in a degenerate algebra the pseudoscalar is nilpotent.
\end{enumerate}

## technical
The pseudoscalar commutes with every vector in odd dimension and anticommutes with every vector in even dimension, so it is central exactly in odd dimension. These relations hold in degenerate algebras as well. There the pseudoscalar contains a null generator, its square vanishes, and it is a nilpotent element rather than a unit.

## lay
The unit volume element commutes with everything in odd dimensions, and flips the sign of arrows in even dimensions. If the space has a direction of zero length, the volume element squares to zero.

## one-liner
$I X_k = (-1)^{k(n-1)} X_k I$; $I\tilde{I} = \prod_i Q(e_i)$, and $I^{2} = 0$ in a degenerate algebra.
