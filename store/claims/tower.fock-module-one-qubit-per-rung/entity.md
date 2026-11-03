---
id: tower.fock-module-one-qubit-per-rung
kind: claim
version: 6
title: Fock module; one qubit per rung
status: proved
region: tower
subject: tower
tags: [spinor-modules, ladder-pairs]
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
  - tower.ladder-pairs-satisfy-car-vectors@4
  - std-algebra.existence-uniqueness@1
  - std-algebra.witt-decomposition@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T03.py
  tags:
  - num:4.2
- kind: check
  ref: check.py::check_w_is_maximal_isotropic
- kind: check
  ref: check.py::check_chevalley_module_and_vacuum
- kind: check
  ref: check.py::check_irreducible
- kind: check
  ref: check.py::check_one_qubit_per_rung
locators:
  paper: T03
  number: Thm 4.2
  label: thm:fock
  line: 296
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.existence-uniqueness, std-algebra.witt-decomposition where the proof uses them. Version 5 -> 6.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: W_k maximal isotropic, the Chevalley action a Cl(k,k)-module with cyclic vacuum, irreducibility (rank 4^k and the vacuum criterion) and the doubling per rung, k <= 4. Version 3 -> 4. Sample inputs moved to module level; no change to what is tested. Version 4 -> 5.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'Both edges are genuine premises: isotropy of W_k from the ladder-pair proposition, and simplicity of B_k from commuting copies.'
---

## formal
Let $W_k := \operatorname{span}\{v_1, \dots, v_k\}$, a maximal isotropic subspace of $H_1 \perp \cdots \perp H_k$. The Chevalley action ($v_j$ by wedge, $w_j$ by contraction against the pairing) makes the exterior algebra $\Lambda^\bullet W_k$, of dimension $2^k$, an irreducible module over $B_k \cong \Mat_{2^k}(\R)$, with the vacuum $1 \in \Lambda^0$ annihilated by every $w_j$ and cyclic for the $v_j$. Each rung doubles the module: $\Lambda^\bullet W_{k+1} = \Lambda^\bullet W_k \otimes \Lambda^\bullet \R v_{k+1}$, one qubit per rung.

## technical
Let $W_k = \operatorname{span}\{v_1, \dots, v_k\}$, a maximal isotropic subspace of $H_1 \perp \cdots \perp H_k$. The Chevalley action, with each $v_j$ acting by wedge product and each $w_j$ by contraction against the pairing, makes the exterior algebra $\Lambda^\bullet W_k$, of dimension $2^k$, an irreducible module over $B_k \cong \Mat_{2^k}(\R)$. The vacuum $1 \in \Lambda^0$ is annihilated by every $w_j$ and is cyclic for the $v_j$.

Each rung doubles the module, $\Lambda^\bullet W_{k+1} = \Lambda^\bullet W_k \otimes \Lambda^\bullet \R v_{k+1}$: one qubit per rung.

## lay
The planes added in the tower act naturally on a space built like the state space of fermions: an empty vacuum state, with raising operators that fill slots and lowering operators that empty them. Nothing smaller carries this action, and after k planes the space has dimension 2 to the power k. Each new plane doubles it, adding one qubit per rung of the tower.

## one-liner
The Chevalley action makes the exterior algebra $\Lambda^\bullet W_k$ an irreducible $2^k$-dimensional module for $B_k \cong \Mat_{2^k}(\R)$ with a cyclic vacuum, and each rung doubles it.
