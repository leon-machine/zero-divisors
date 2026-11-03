---
id: std-algebra.quaternions
kind: claim
version: 1
title: The quaternions inside Clifford algebras
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- dictionaries
- rotors-and-stabilisers
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
- obj.std-algebra.even-subalgebra
derivations:
- name: main
  uses:
  - std-algebra.orthogonal-anticommute@1
  - std-algebra.z2-grading@1
  - std-algebra.blade-basis@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_hamilton_relations
locators:
  sources:
  - key: DoranLasenby2003
    locator: Ch. 2 (geometric algebra in two and three dimensions)
  - key: Lounesto2001
    locator: Ch. 16 (matrix representations and periodicity of 8)
extraction:
  by: algebra-core-2026-10-26
---

## formal
(i) In $\Cl^{+}(3,0)$ the bivectors $\mathbf{i} = e_3 e_2$, $\mathbf{j} = e_1 e_3$, $\mathbf{k} = e_2 e_1$ satisfy Hamilton's relations $\mathbf{i}^{2} = \mathbf{j}^{2} = \mathbf{k}^{2} = \mathbf{i}\mathbf{j}\mathbf{k} = -1$, and $\Cl^{+}(3,0) = \operatorname{span}\{1, \mathbf{i}, \mathbf{j}, \mathbf{k}\} \cong \HH$. (ii) In $\Cl(0,2)$, $\mathbf{i} = e_1$, $\mathbf{j} = e_2$, $\mathbf{k} = e_1 e_2$ satisfy the same relations and $\Cl(0,2) \cong \HH$.

## technical
The quaternions are the even part of the algebra of three-dimensional space: the three unit bivectors, with a choice of orientation, square to minus one and multiply as Hamilton's $\mathbf{i}, \mathbf{j}, \mathbf{k}$. They are also the whole algebra of two directions that both square to minus one. Unit quaternions are the rotors of three-dimensional space.

## lay
Hamilton's quaternions, invented to describe rotations, are the oriented unit planes of ordinary space together with the ordinary numbers. Their strange multiplication rules are the geometric product of planes.

## one-liner
$\Cl^{+}(3,0) = \operatorname{span}\{1, e_3e_2, e_1e_3, e_2e_1\} \cong \HH$ and $\Cl(0,2) \cong \HH$, by Hamilton's relations.
