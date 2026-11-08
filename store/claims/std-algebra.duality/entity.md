---
id: std-algebra.duality
kind: claim
version: 1
title: Duality
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- pseudoscalar-and-centre
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
- obj.std-algebra.blade
derivations:
- name: main
  uses:
  - std-algebra.pseudoscalar-commutation@1
  - std-algebra.product-decomposition@1
  - std-algebra.contraction-expansion@1
  - std-algebra.blade-subspace@2
  - std-algebra.grade-decomposition@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_duality_identities_all_signatures
- kind: check
  ref: check.py::check_dual_blade_is_orthogonal_complement
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
Let $I$ be the unit pseudoscalar of $\Cl(p, q, r)$. For every signature, right multiplication by $I$ maps $\Cl^{k}$ into $\Cl^{n-k}$, and for $a \in V$
\begin{equation}
a \rfloor (X I) = (a \wedge X) I, \qquad a \wedge (X I) = (a \rfloor X) I .
\end{equation}
If $r = 0$, $I$ is invertible and $X \mapsto X I$ is a linear isomorphism $\Cl^{k} \to \Cl^{n-k}$ (the \emph{duality}); for a nonzero $k$-blade $A$, $A I$ is a nonzero $(n-k)$-blade with $[A I] = [A]^{\perp}$. So outer and inner products are exchanged by duality.

## technical
Multiplying by the pseudoscalar sends grade $k$ to grade $n - k$ and swaps the two products: contraction of a dual is the dual of an outer product, and the reverse. In a nondegenerate algebra this is an isomorphism, and it sends the blade of a subspace to the blade of its orthogonal complement. In a degenerate algebra the identities still hold but duality is no longer invertible.

## lay
Multiplying by the unit volume trades an element for its complement: a plane in three dimensions for the line perpendicular to it. Under this exchange, adding a direction and removing one swap roles.

## one-liner
$X \mapsto XI$ sends $\Cl^{k} \to \Cl^{n-k}$ with $a \rfloor (XI) = (a \wedge X)I$, $a \wedge (XI) = (a \rfloor X)I$; for $r = 0$ it is an isomorphism and $[AI] = [A]^{\perp}$.
