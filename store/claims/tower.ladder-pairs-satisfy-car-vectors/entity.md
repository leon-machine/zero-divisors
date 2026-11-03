---
id: tower.ladder-pairs-satisfy-car-vectors
kind: claim
version: 4
title: The ladder pairs satisfy the CAR, as vectors
status: proved
region: tower
subject: tower
tags: [ladder-pairs, car-algebra, two-readings]
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
  - std-algebra.vector-squares@1
  - std-algebra.witt-basis-car@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T03.py
  tags:
  - num:4.1
- kind: check
  ref: check.py::check_car_as_vectors
- kind: check
  ref: check.py::check_new_rung_touches_nothing
locators:
  paper: T03
  number: Prop 4.1
  label: prop:car
  line: 284
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.vector-squares, std-algebra.witt-basis-car where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: all CAR relations as vector identities for n <= 3, k <= 3, and the new rung anticommuting with everything earlier. Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: "no claim edges, the proof uses only the Clifford relation on vectors and the construction of the tower; obj.tower.tower would fit in about but was not added"
payload:
- kind: identity
  clause: CAR at k = 3 on the ground (1,3)
  python: '(lambda vs, ws, S: all(GA.is_zero(anti(vs[i], vs[j], S)) and GA.is_zero(anti(ws[i], ws[j],
    S)) and GA.eq(anti(vs[i], ws[j], S), GA.sc(1 if i == j else 0)) for i in range(3) for j in range(3)))(*pairs(4,
    3), floor(1, 3, 3))'
  note: v_i v_j + v_j v_i = 0, w_i w_j + w_j w_i = 0, v_i w_j + w_j v_i = delta_ij in T_3 = Cl(4,6)
---

## formal
In $T_k$, the adjoined null pairs satisfy, exactly and at the level of vectors,
\[
v_i v_j + v_j v_i = 0, \qquad w_i w_j + w_j w_i = 0, \qquad v_i w_j + w_j v_i = \delta_{ij}\,,
\]
for all $1 \leq i, j \leq k$: a system of $k$ fermionic modes, with no normal-ordering, no completion, and no representation chosen. Adding a rung adds one mode and touches none of the existing relations.

## technical
In the $k$-th algebra of the tower, $T_k = \Cl(p{+}k, q{+}k)$, each adjoined hyperbolic plane carries a normalised null pair $(v_i, w_i)$. These vectors satisfy $v_i v_j + v_j v_i = 0$, $w_i w_j + w_j w_i = 0$ and $v_i w_j + w_j v_i = \delta_{ij}$ for all $1 \leq i, j \leq k$, which are the canonical anticommutation relations of $k$ fermionic modes. The relations hold exactly, among vectors of the algebra, with no normal ordering, no completion and no choice of representation.

Each relation is an instance of the Clifford relation $ab + ba = 2\langle a, b\rangle$ for vectors: the null vectors have $Q(v_i) = Q(w_i) = 0$, distinct planes are orthogonal, and the hyperbolic normalisation gives $\langle v_i, w_i\rangle = \tfrac12$. The vectors of a new rung are orthogonal to all earlier generators, so adding a rung adds one mode and leaves the existing relations untouched.

## lay
Each step up the tower adds a new pair of special zero-length directions to the space. Taken together, these pairs obey exactly the algebraic rules that quantum theory uses for fermionic modes, the kind of states occupied by particles such as electrons, with one mode per step. The rules hold for the directions themselves, so nothing has to be added or chosen to make them work, and a new step never disturbs the modes already present.

## one-liner
In the $k$-th tower algebra the $k$ adjoined null pairs satisfy the canonical anticommutation relations of $k$ fermionic modes exactly, as vectors, and each new rung adds one mode without altering the existing relations.
