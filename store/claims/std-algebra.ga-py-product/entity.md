---
id: std-algebra.ga-py-product
kind: claim
version: 1
title: The library's product is the Clifford product
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- finite-models
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
  - std-algebra.existence-uniqueness@1
  - std-algebra.blade-basis@1
  - std-algebra.orthogonal-anticommute@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_product_associative_unital_and_relations
extraction:
  referee_fixes: '2026-10-26: proof replaced by the direct argument (each step of blade_mul is an identity in Cl(p,q,r), induction on the moves); the check is now a cross-check (referee part 1, point 1).'
  by: algebra-core-2026-10-26
---

## formal
For every diagonal signature $(p, q, r)$, the bilinear product \texttt{GA.mul} on the $2^{n}$-dimensional space with basis the blade tuples, with \texttt{GA.sig(p, q, r)}, is associative with unit $()$, and its generators satisfy $e_i^{2} = Q(e_i)$ and $e_i e_j = -e_j e_i$ for $i \ne j$. Consequently the linear map sending the basis blade $e_I$ of $\Cl(p, q, r)$ to the tuple $I$ is an algebra isomorphism: every exact check that computes with \texttt{GA.mul} computes in $\Cl(p, q, r)$. The same holds for \texttt{GA.grade\_inv} and \texttt{GA.reverse} by \claimref{std-algebra.involution-properties}.

## technical
The store's exact library multiplies blades by sorting indices and contracting repeats. This result certifies that it really implements the Clifford algebra: the product is associative, the empty blade is the unit, generators square to the signature and distinct generators anticommute. The universal property then identifies the library's algebra with $\Cl(p, q, r)$, so every check built on the library computes in the right algebra.

## lay
The computer checks in this store all rest on one small program that multiplies elements of the algebra. This result tests that program against the definition, so the checks built on it can be trusted to compute the right thing.

## one-liner
\texttt{GA.mul} is associative and unital with $e_i^{2} = Q(e_i)$, $e_i e_j = -e_j e_i$, so it is the product of $\Cl(p, q, r)$.
