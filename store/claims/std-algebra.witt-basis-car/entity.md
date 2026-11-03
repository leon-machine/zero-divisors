---
id: std-algebra.witt-basis-car
kind: claim
version: 1
title: Null pairs satisfy the canonical anticommutation relations
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- car-algebra
- ladder-pairs
- hyperbolic-plane
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
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_null_pairs_satisfy_the_car
locators:
  sources:
  - key: DoranLasenby2003
    locator: Ch. 9 (multiparticle states)
  - key: LawsonMichelsohn1989
    locator: Ch. I, Sections 2 and 5
  - key: Chevalley1954
    locator: Ch. II and III (spinors, pure spinors)
extraction:
  by: algebra-core-2026-10-26
---

## formal
Let $v_1, \dots, v_k, w_1, \dots, w_k \in V$ be a \emph{Witt basis} of their span: $B(v_i, v_j) = B(w_i, w_j) = 0$ and $B(v_i, w_j) = \tfrac12 \delta_{ij}$. Then in $\Cl(V, Q)$
\begin{equation}
v_i v_j + v_j v_i = 0, \qquad w_i w_j + w_j w_i = 0, \qquad v_i w_j + w_j v_i = \delta_{ij},
\end{equation}
the canonical anticommutation relations for $k$ modes (read $v_i$ as annihilators, $w_i$ as creators). The elements $N_i = w_i v_i$ are mutually commuting idempotents with $N_i + v_i w_i = 1$. In particular, for orthogonal hyperbolic planes $\operatorname{span}(e_i, e_{k+i})$ of $\R^{k,k}$, $v_i = \tfrac12(e_i + e_{k+i})$ and $w_i = \tfrac12(e_i - e_{k+i})$ form such a basis. The form need not be nondegenerate outside the span.

## technical
Pairs of null vectors with polar form one half between partners and zero otherwise satisfy, at the level of vectors and with nothing else assumed, the anticommutation relations of fermionic modes. Each hyperbolic plane supplies one such pair, $v = \tfrac12(e_+ + e_-)$ and $w = \tfrac12(e_+ - e_-)$. The number elements $w_i v_i$ are commuting projections. The algebra outside the pairs plays no role.

## lay
Inside a Clifford algebra, a direction of space paired with a direction of time produces two zero-length arrows that obey exactly the rules for creating and destroying a fermion. With several such pairs you get several independent fermion modes, without building any Hilbert space first.

## one-liner
For a Witt basis ($B(v_i,v_j) = B(w_i,w_j) = 0$, $B(v_i,w_j) = \tfrac12\delta_{ij}$), $\{v_i,v_j\} = \{w_i,w_j\} = 0$ and $\{v_i,w_j\} = \delta_{ij}$ in $\Cl(V,Q)$.
