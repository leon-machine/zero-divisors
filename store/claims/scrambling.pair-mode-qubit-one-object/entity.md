---
id: scrambling.pair-mode-qubit-one-object
kind: claim
version: 4
title: 'Pair, mode, qubit: one object'
status: proved
region: scrambling
subject: tower
tags: [ladder-pairs, witt-index, two-readings]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
review: typed
derivations:
- name: main
  uses:
  - tower.fock-module-one-qubit-per-rung@6
  - tower.ladder-pairs-satisfy-car-vectors@4
  - tower.witt-index-quantum-capacity@4
  - std-algebra.witt-basis-car@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - num:4.11
- kind: check
  ref: check.py::check_two_pairs_satisfy_car_in_cl24
- kind: check
  ref: check.py::check_no_third_pair
- kind: check
  ref: check.py::check_pair_is_one_qubit
locators:
  paper: T08
  number: Prop 4.11
  label: prop:pair
  line: 808
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.witt-basis-car where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: two CAR pairs in Cl(2,4), no third (W-perp/W definite and an exhaustive lattice search), and one pair as one qubit with entropy ln 2 per pair. Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: All three uses are the tower results the proof cites and are kept.
---

## formal
The tower's ladder pair $(v_i, w_i)$, the singularity paper's ``fermionic mode'', and the ``one ladder pair per point of the exceptional set'' of Fact \claimref{tower.witt-index-quantum-capacity} are the same object: one creation and one annihilation operator, a two-dimensional state space, one qubit, maximal entropy $\ln 2$ nats. In particular $\Cl(2,4)$ carries exactly two such pairs, its Witt index, and the count of pairs is the count of modes: no factor of two enters between the tower and this paper's count.

## technical
The tower's ladder pair $(v_i, w_i)$, the singularity analysis's fermionic mode, and the one ladder pair per point of the exceptional set in the Witt-index capacity result are one object: one creation and one annihilation operator, a two-dimensional state space $\{\ket{0}, v_i\ket{0}\}$, one qubit, of maximal entropy $\ln 2$ nats.

In particular $\Cl(2,4)$ carries exactly two such pairs, its Witt index, and the count of pairs is the count of modes, with no factor of two between the tower's count and the entropy count.

## lay
Three things in the series that sound different, a pair of null directions in the tower, a fermionic mode in the singularity analysis and a unit of quantum capacity, are the same thing. Each is one fermion mode with two states, empty or filled, which is one qubit and can hold at most $\ln 2$ nats of entropy. The conformal algebra has room for exactly two of them, and counting pairs or counting modes gives the same number.

## one-liner
A tower ladder pair, a fermionic mode and a unit of Witt-index capacity are one object, one qubit of maximal entropy $\ln 2$, and $\Cl(2,4)$ carries exactly two.
