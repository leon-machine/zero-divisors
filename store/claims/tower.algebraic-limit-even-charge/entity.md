---
id: tower.algebraic-limit-even-charge
kind: claim
version: 3
title: The algebraic limit, even charge
status: proved
region: tower
subject: tower
tags: [limits]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T03, deposited version
review: typed
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - tower.commuting-copies@5
  - tower.compatibility-connecting-maps-transported@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_transported_connecting_map_is_corrected_doubling
- kind: check
  ref: check.py::check_intertwiners_make_the_embeddings_block_doublings
- kind: check
  ref: check.py::check_limit_is_clifford_algebra_of_the_union
- kind: proof
  derivation: main
locators:
  paper: T03
  number: Thm 5.3
  label: thm:alglimit
  line: 385
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the transported connecting maps as corrected block doublings for k <= 2 (failing for odd charge) and the intertwiners W_k making every tower embedding a block doubling. Version 2 -> 3.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'Both edges are genuine premises; the second description rests on a general universal-property argument with no store reference.'
---

## formal
Let $p - q$ be even. The algebraic direct limit of the tower $(T_k, \iota_k)$ is canonically isomorphic to
\[
\varinjlim T_k \;\cong\; \Cl(p,q) \otimes \Mat_{2^\infty}, \qquad \Mat_{2^\infty} := \varinjlim \Mat_{2^k}(\R) \ \ (m \mapsto \operatorname{diag}(m,m)),
\]
the ground algebra tensored with the algebraic $2^\infty$ matrix algebra. Equivalently, $\varinjlim T_k$ is the Clifford algebra of the infinite-dimensional quadratic space $\R^{p,q} \perp H_1 \perp H_2 \perp \cdots$.

## technical
For $p - q$ even, the algebraic direct limit of the tower $(T_k, \iota_k)$ is canonically $\varinjlim T_k \cong \Cl(p,q) \otimes \Mat_{2^\infty}$, where $\Mat_{2^\infty} = \varinjlim \Mat_{2^k}(\R)$ along $m \mapsto \operatorname{diag}(m,m)$. The proof transports the connecting maps to $\psi_k = \operatorname{Ad}(V_k) \circ \theta_k$, block doubling followed by conjugation, and removes the correctors stagewise with the invertible elements $W_{k+1} = \theta_k(W_k)\, V_k^{-1}$, so that the comparison squares commute exactly.

Equivalently, the limit is the Clifford algebra of the infinite-dimensional quadratic space $\R^{p,q} \perp H_1 \perp H_2 \perp \cdots$.

## lay
Keep adding planes to the tower forever and take the union, purely algebraically. When the numbers of positive and negative directions differ by an even amount, the result has a clean description: the original algebra with entries in an infinite matrix algebra built by repeated doubling. Equivalently, it is the Clifford algebra of the infinite-dimensional space obtained by adding all the planes at once.

## one-liner
For even charge the algebraic direct limit of the tower is canonically $\Cl(p,q) \otimes \Mat_{2^\infty}$, equivalently the Clifford algebra of $\R^{p,q} \perp H_1 \perp H_2 \perp \cdots$.
