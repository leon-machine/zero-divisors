---
id: tower.witt-index-quantum-capacity
kind: claim
version: 5
title: Witt index is quantum capacity
status: proved
region: tower
subject: tower
tags: [witt-index, ladder-pairs, two-readings]
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
- name: Claude Opus 5.5
  role: 'consistency pass, Q(v) for the square of a vector in the proof'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.tower.tower
- obj.std-algebra.witt-index
derivations:
- name: main
  uses:
  - tower.ladder-pairs-satisfy-car-vectors@4
  - std-algebra.vector-squares@1
  - std-algebra.witt-decomposition@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T03.py
  tags:
  - num:4.3
- kind: check
  ref: check.py::check_mode_family_attains_witt_index
- kind: check
  ref: check.py::check_witt_subspace_is_maximal
- kind: check
  ref: check.py::check_each_rung_adds_one_mode
locators:
  paper: T03
  number: Thm 4.3
  label: thm:capacity
  line: 328
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. The upper-bound step wrote Q(v,v) for the square of a vector; it is now Q(v), the store''s notation; no change of content.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.vector-squares, std-algebra.witt-decomposition, obj.std-algebra.witt-index where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: min(p,q) mode pairs attained for n <= 7, maximality (W-perp/W definite, exhaustive lattice search for n <= 4), and one more mode per rung. Version 2 -> 3.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: "kept the CAR proposition as a premise because the mode families are defined by its displayed relations and the attainment step uses its null pairs; the upper bound itself is classical"
---

## formal
For any nondegenerate real quadratic space $(V, Q)$, the maximal number of pairwise-anticommuting fermionic mode pairs realisable by \emph{vectors} of $\Cl(V, Q)$ (families $(a_i, b_i)$ of vectors satisfying the displayed CAR of Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}) is exactly the Witt index $\min(p,q)$ of $Q$. Along the tower the Witt index is $\min(p,q) + k$: each rung raises the algebra's mode capacity by exactly one, and by no more.

## technical
Let $(V, Q)$ be a nondegenerate real quadratic space of signature $(p,q)$, and call a family of vectors $(a_i, b_i)_{i \leq m}$ of $\Cl(V,Q)$ a mode family if it satisfies $a_i a_j + a_j a_i = 0$, $b_i b_j + b_j b_i = 0$ and $a_i b_j + b_j a_i = \delta_{ij}$. The largest possible $m$ is exactly the Witt index $\min(p,q)$. For the upper bound, the relations force the $a_i$ to span a totally isotropic subspace, and pairing against the $b_j$ shows the $a_i$ are linearly independent; a totally isotropic subspace of a nondegenerate form of signature $(p,q)$ has dimension at most $\min(p,q)$. The bound is attained by the normalised null pairs of $\min(p,q)$ orthogonal hyperbolic planes split off by a Witt decomposition.

Along the tower, $T_k$ has signature $(p{+}k, q{+}k)$ and hence Witt index $\min(p,q) + k$, so each rung raises the number of vector-realised modes by exactly one and by no more.

## lay
Inside a Clifford algebra one can ask how many independent fermionic modes can be built directly from vectors. The answer is a classical number attached to the geometry, the Witt index: the largest number of independent zero-length directions that are all orthogonal to one another. For a space with p positive and q negative directions it is the smaller of p and q. Each step up the tower raises this number by exactly one, so each step adds precisely one mode of capacity and no more.

## one-liner
For a nondegenerate real quadratic space of signature $(p,q)$, the maximal number of fermionic mode pairs realisable by vectors of its Clifford algebra is the Witt index $\min(p,q)$, which rises by exactly one at each rung of the tower.
