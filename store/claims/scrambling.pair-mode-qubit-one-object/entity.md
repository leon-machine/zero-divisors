---
id: scrambling.pair-mode-qubit-one-object
kind: claim
version: 5
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
- name: Claude Opus 5.5
  role: 'maintainer pass, citation of the exceptional-set count corrected with a uses edge at Leon''s decisions'
  version: 5
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  uses:
  - tower.fock-module-one-qubit-per-rung@6
  - tower.ladder-pairs-satisfy-car-vectors@4
  - tower.witt-index-quantum-capacity@4
  - std-algebra.witt-basis-car@1
  - sheaf.schwarzschild-degeneration-boundary-tame@6
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
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. Decision item D7 (routine): ''one ladder pair per point of the exceptional set'' was attributed to tower.witt-index-quantum-capacity, which states only the vector capacity min(p,q); it is T04 Thm 8.7, sheaf.schwarzschild-degeneration-boundary-tame (corank exactly one at every point of the blown-up boundary), now cited in the formal, technical and proof with a uses edge (@6); the Witt-index edge stays for the capacity the proof and check use.'
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
The tower's ladder pair $(v_i, w_i)$, the singularity paper's ``fermionic mode'', and the ``one ladder pair per point of the exceptional set'' (the degeneration there has corank exactly one at every point, Theorem \claimref{sheaf.schwarzschild-degeneration-boundary-tame}(2), so the completion adds one ladder pair per point) are the same object: one creation and one annihilation operator, a two-dimensional state space, one qubit, maximal entropy $\ln 2$ nats. In particular $\Cl(2,4)$ carries exactly two such pairs, its Witt index, and the count of pairs is the count of modes: no factor of two enters between the tower and this paper's count.

## technical
The tower's ladder pair $(v_i, w_i)$, the singularity analysis's fermionic mode, and the one ladder pair per point of the exceptional set (the singular boundary degenerates with corank exactly one at every point) are one object: one creation and one annihilation operator, a two-dimensional state space $\{\ket{0}, v_i\ket{0}\}$, one qubit, of maximal entropy $\ln 2$ nats.

In particular $\Cl(2,4)$ carries exactly two such pairs, its Witt index, and the count of pairs is the count of modes, with no factor of two between the tower's count and the entropy count.

## lay
Three things in the series that sound different, a pair of null directions in the tower, a fermionic mode in the singularity analysis and a unit of quantum capacity, are the same thing. Each is one fermion mode with two states, empty or filled, which is one qubit and can hold at most $\ln 2$ nats of entropy. The conformal algebra has room for exactly two of them, and counting pairs or counting modes gives the same number.

## one-liner
A tower ladder pair, a fermionic mode and a unit of Witt-index capacity are one object, one qubit of maximal entropy $\ln 2$, and $\Cl(2,4)$ carries exactly two.
