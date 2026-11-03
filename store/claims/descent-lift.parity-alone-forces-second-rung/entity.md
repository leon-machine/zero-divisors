---
id: descent-lift.parity-alone-forces-second-rung
kind: claim
version: 3
title: Parity alone forces the second rung
status: proved
region: descent-lift
subject: descent
tags: [ladder-pairs, univalence, forcing-and-uniqueness]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-descent-lift, the series'' standard disclaimer'
review: typed
about:
- obj.descent-lift.lift
derivations:
- name: main
  uses:
  - descent-lift.lift-costs-one-rung-per-mode@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_one_rung_candidates_induce_descent
- kind: check
  ref: check.py::check_both_one_rung_candidates_are_odd
- kind: check
  ref: check.py::check_two_rung_occupation_copy_is_even_lift
locators:
  paper: T05-descent-lift
  number: Cor 4.3
  label: cor:onerung
  line: 221
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the one-rung Stinespring dilation (2E) and occupation copy (E) on the even sector, their oddness, the one-line even sector of a rung, and the even two-rung occupation copy equal to the lift in the record basis |00> +- |11>. Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  env: corollary
  typing:
    by: ai-typing-pass
    note: 'the single edge to the lift theorem is the premise the proof invokes for clauses (i) to (iii)
      and is kept; Stinespring''s minimal dilation is named in the statement as a candidate map checked
      directly, not used as a premise. Levels pass: conditions already kept.'
---

## formal
For the pair, both one-rung candidates exist as maps: Stinespring's minimal dilation $\psi \otimes \ket{0} + \G_{0}\psi \otimes \ket{1}$ and the occupation copy $P_{00}\psi \otimes \ket{0} + P_{11}\psi \otimes \ket{1}$ each induce the descent on the even sector. Both are odd: the first because its record states $\ket{0} \pm \ket{1}$ mix the parities, the second because it sends the even state $\ket{11}$ to a joint state of odd parity. Neither is an operation the univalence rule allows, and there is no other obstruction.

## technical
For the pair, two one-rung maps do induce the descent on the even sector: Stinespring's minimal dilation $\psi\otimes\ket{0} + \G_{0}\psi\otimes\ket{1}$ and the occupation copy $P_{00}\psi\otimes\ket{0} + P_{11}\psi\otimes\ket{1}$. Both are odd: the first has record states $\ket{0}\pm\ket{1}$ of mixed parity, and the second sends the even state $\ket{11}$ to a joint state of odd parity.

Neither is an operation the univalence rule allows, and parity is the only obstruction: the even two-rung occupation copy $P_{00}\otimes(\ket{00} + \ket{11}) + P_{11}\otimes(\ket{00} - \ket{11})$ is a lift.

## lay
For an entangled pair of modes, a single extra record mode would be enough to store what the descent discards if parity did not matter. Both natural one-mode recipes work as maps, but both break the rule that fermion parity is conserved. Restoring parity is the only thing the second record mode is needed for.

## one-liner
For the pair both one-rung dilations of the descent exist but are odd, so the univalence rule alone forces the second rung.
