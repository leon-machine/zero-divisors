---
id: field-theory.imported-tower-limit
kind: claim
version: 3
title: 'Imported: the tower and its limit'
status: proved
region: field-theory
subject: quantum-fields
tags: [car-algebra, limits]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of FT, the series'' standard disclaimer'
review: typed
locators:
  paper: FT
  number: Fact 2.1
  label: fact:tower
  line: 74
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: adjoined planes give null v_j, w_j with {v_j, w_k} = delta_jk over the ground Cl(1,3), and each rung is the full matrix algebra Mat_(2^n) on its Fock space with w_j = v_j^T. Version 1 -> 2. Fix round: check_rungs_are_full_matrix_algebras tests the unital embedding of rung n in rung n + 1 for n = 1, 2. Version 2 -> 3.'
  env: fact
  flags:
  - citation taken from inline provenance (no \cite)
  source_imported_from:
  - citation: T03, Thm. thm:carlimit
  typing:
    by: ai-typing-pass
    added:
    - tower.car-limit-even-charge
    note: 'The fact restates the tower paper''s CAR-limit theorem, which is in the store, so it was made
      a restatement (status proved, uses that theorem). Levels pass: levels written from scratch, keeping
      every condition and level qualifier of the formal statement.'
derivations:
- name: main
  uses:
  - tower.car-limit-even-charge@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_planes_generate_car
- kind: check
  ref: check.py::check_rungs_are_full_matrix_algebras
---

## formal
The planes generate the CAR, $\{v_j, w_k\} = \delta_{jk}$, $v_j^2 = w_j^2 = 0$, and the tower's limit is the CAR algebra. \emph{Provenance:} T03, Thm.~thm:carlimit.

## technical
The adjoined tower planes generate the canonical anticommutation relations, $\{v_j, w_k\} = \delta_{jk}$ with $Q(v_j) = Q(w_j) = 0$, and the tower's limit is the CAR algebra.

## lay
Each plane added to the tower contributes one fermionic mode, with the anticommutation rules of fermion creation and annihilation. Adding planes without end gives the algebra of a free fermionic quantum field.

## one-liner
The tower planes generate the CAR, $\{v_j, w_k\} = \delta_{jk}$ with $Q(v_j) = Q(w_j) = 0$, and the tower's limit is the CAR algebra.
