---
id: std-algebra.blade-basis
kind: claim
version: 1
title: The blade basis, degenerate forms included
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
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
  - std-algebra.existence-uniqueness@1
  - std-algebra.vector-squares@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_symbol_images_independent
locators:
  sources:
  - key: Chevalley1954
    locator: Ch. II (the Clifford algebra of a quadratic space)
  - key: Chevalley1997
    locator: the symbol map
  - key: Lounesto2001
    locator: Ch. 14 (definitions of the Clifford algebra)
extraction:
  by: algebra-core-2026-10-26
---

## formal
Let $e_1, \dots, e_n$ be any basis of $V$. The $2^{n}$ ordered products $e_I = e_{i_1} e_{i_2} \cdots e_{i_k}$, for $I = \{i_1 < \dots < i_k\} \subseteq \{1, \dots, n\}$ (with $e_{\emptyset} = 1$), form a basis of $\Cl(V, Q)$. Hence $\dim \Cl(V, Q) = 2^{n}$, the map $\iota : V \to \Cl(V, Q)$ is injective, and $\Cl(V, Q) \ne 0$. This holds for every real quadratic space, degenerate or not.

## technical
For any basis of $V$, orthogonal or not, the increasing products of basis vectors (including the empty product $1$) form a basis of the Clifford algebra, which therefore has dimension $2^{n}$. They span because the relation $e_i e_j = -e_j e_i + 2B(e_i, e_j)$ reorders any word and $e_i^{2} = Q(e_i)$ shortens it. They are independent because, in the exterior model, $e_I$ applied to $1$ is $e_{i_1} \wedge \dots \wedge e_{i_k}$ plus terms of lower degree. Nothing here needs the form to be nondegenerate.

## lay
Every element of the algebra is a combination of products of distinct basis arrows, and no such product can be written in terms of the others. In $n$ dimensions there are $2^{n}$ of them: the number, the arrows, the planes, the volumes and so on. This stays true even when some directions have zero length.

## one-liner
For any basis of $V$ the $2^{n}$ increasing products $e_I$ form a basis of $\Cl(V, Q)$, degenerate forms included; so $V \hookrightarrow \Cl(V, Q)$.
