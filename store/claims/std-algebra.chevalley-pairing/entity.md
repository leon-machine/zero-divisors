---
id: std-algebra.chevalley-pairing
kind: claim
version: 1
title: The invariant pairing on spinors
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- spinor-modules
- pairing-and-bogoliubov
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
- obj.std-algebra.minimal-left-ideal
derivations:
- name: main
  uses:
  - std-algebra.fock-representation@1
  - std-algebra.involution-properties@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_pairing_nondegenerate_symmetry_and_self_adjoint_vectors
- kind: check
  ref: check.py::check_elements_with_unit_norm_preserve_the_pairing
locators:
  sources:
  - key: Chevalley1954
    locator: Ch. II and III (spinors, pure spinors)
  - key: Lounesto2001
    locator: Ch. 18 (scalar products of spinors)
extraction:
  by: algebra-core-2026-10-26
---

## formal
In the Fock model of \claimref{std-algebra.fock-representation}, let $\tau$ be the reversal of $\Lambda W$ ($\tau(x_1 \wedge \dots \wedge x_m) = x_m \wedge \dots \wedge x_1$) and $\operatorname{top}(z)$ the coefficient of $w_1 \wedge \dots \wedge w_k$ in $z$. Set $\beta(x, y) = \operatorname{top}(\tau(x) \wedge y)$. Then:
\begin{enumerate}
\item[(i)] $\beta$ is nondegenerate and pairs $\Lambda^{m} W$ only with $\Lambda^{k-m} W$; so it pairs each parity with itself for $k$ even, and even with odd for $k$ odd;
\item[(ii)] $\beta(y, x) = (-1)^{k(k-1)/2}\, \beta(x, y)$;
\item[(iii)] every vector is self-adjoint: $\beta(u x, y) = \beta(x, u y)$ for $u \in V$; hence $\beta(a x, y) = \beta(x, \tilde{a} y)$ for all $a \in \Cl(V, Q)$, and $\beta(R x, R y) = \beta(x, y)$ whenever $\tilde{R} R = 1$.
\end{enumerate}

## technical
The spinor space carries a natural bilinear pairing: reverse the first spinor, wedge with the second and read off the top-degree coefficient. It is nondegenerate, matches degree $m$ with degree $k - m$, and is symmetric or antisymmetric according to $k(k-1)/2$. Every vector is its own adjoint, so the adjoint of a general element is its reverse, and every element with $\tilde{R} R = 1$, rotors among them, preserves the pairing. For $k = 3$ this is the antisymmetric pairing of the two twistor chiralities used in the series.

## lay
Two spinors can be combined into a single number in a way that every rotation respects. Depending on the dimension the combination is symmetric or changes sign when the spinors are swapped, and it may pair spinors of the same kind or of opposite kinds.

## one-liner
$\beta(x, y) = \operatorname{top}(\tau x \wedge y)$ is nondegenerate on $\Lambda W$, has symmetry $(-1)^{k(k-1)/2}$, and satisfies $\beta(ax, y) = \beta(x, \tilde{a}y)$, so $\tilde{R}R = 1$ preserves it.
