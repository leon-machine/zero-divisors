---
id: rungs.ladder-group-rung-mixing-group-one
kind: claim
version: 4
title: The ladder group is the rung-mixing group on the one-constituent sector
status: proved
region: rungs
subject: standard-model
tags: [refutation, ladder-pairs]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-rungs, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - rungs.imported-ladder-automorphism-group-no-lepton@4
  - rungs.rung-spinor-module-mixings@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12_rungs.py
  tags:
  - label:prop:ladderrung
- kind: check
  ref: check.py::check_rung_mixing_is_the_ladder_action
- kind: check
  ref: check.py::check_pair_mixing_acts_on_the_spinor_factor
locators:
  paper: T12-rungs
  number: Prop 2.4
  label: prop:ladderrung
  line: 267
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Fock rung-mixing equals X (x) 1 and pair mixing equals the Lambda^even derivation on C^n (x) CS for n = 1, 2, 3. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the twistor tuple and C^n (x) T to the conformal-spinor tuple and C^n (x) S at every level and in the proof; S is Lambda^even W, as the formal statement itself records.'
  source_title: |-
    The ladder group is the rung-mixing group on the one-constituent sector
  source_formal: |-
    The $U(n)$ of Fact \claimref{rungs.imported-ladder-automorphism-group-no-lepton} acts on the $n$-tuple $\Psi \in \C^{n} \otimes \T$ as $U \otimes 1$. Under Theorem \claimref{rungs.rung-spinor-module-mixings}(2) the rung-mixing $U(n)$ acts on the sector $\Lambda^{1}R_{n} \otimes \Lambda^{\mathrm{even}}W = \C^{n} \otimes \T$ as $A \otimes 1$. The two actions coincide: the ladder of the Standard-Model paper is the mixing of the new rungs of the tower, restricted to the states with exactly one new mode occupied and an even number of old pairs. The same holds for the pair-mixing $U(3)$, which acts on $\T$ by $\Lambda^{\mathrm{even}}(B)$ in both.
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'Kept both edges, the two actions the proof compares. Levels pass: lay now keeps the slot-rung
      identification and the even-pairs sector, and drops the unsupported claim that this is the one place
      the constructions coincide.'
---

## formal
The $U(n)$ of Fact \claimref{rungs.imported-ladder-automorphism-group-no-lepton} acts on the $n$-tuple $\Psi \in \C^{n} \otimes \CS$ of conformal spinors (twistors), $\CS$ the conformal spinor space, as $U \otimes 1$. Under Theorem \claimref{rungs.rung-spinor-module-mixings}(2) the rung-mixing $U(n)$ acts on the sector $\Lambda^{1}R_{n} \otimes \Lambda^{\mathrm{even}}W = \C^{n} \otimes \CS$ as $A \otimes 1$. The two actions coincide: the ladder of the Standard-Model paper is the mixing of the new rungs of the tower, restricted to the states with exactly one new mode occupied and an even number of old pairs. The same holds for the pair-mixing $U(3)$, which acts on $\CS$ by $\Lambda^{\mathrm{even}}(B)$ in both.

## technical
The ladder $U(n)$, derived from preserving momentum and helicity, acts on the conformal-spinor tuple $\Psi \in \C^{n} \otimes \CS$ as $U \otimes 1$. The tower's rung-mixing $U(n)$ acts on the sector $\Lambda^{1}R_{n} \otimes \Lambda^{\mathrm{even}}W = \C^{n} \otimes \CS$ of the rung module as $A \otimes 1$. Identifying the slot basis with the new rung modes $v_{1}, \ldots, v_{n}$, the two actions coincide.

So the ladder is the rung mixing restricted to the states with exactly one new mode occupied and an even number of old pairs, and the same holds for the pair-mixing $U(3)$, which acts on $\CS$ by $\Lambda^{\mathrm{even}}(B)$ in both. The content is that the identification of slots with rungs is available, not that it is forced.

## lay
Two independent constructions produce a group that mixes several basic spinor states: one from requiring that total momentum and helicity are unchanged, the other from the algebraic tower the programme builds. On the states with exactly one new mode occupied and an even number of old pairs, and once the slots those states occupy are matched with the tower's new rungs, the two groups act in exactly the same way. This shows that the match between slots and rungs is available, not that it is forced, and it holds only on that part of the state space.

## one-liner
On the one-constituent sector $\C^{n} \otimes \CS$ of the rung module, the ladder $U(n)$ and the tower's rung-mixing $U(n)$ act identically, as do the two pair-mixing $U(3)$ actions, once slots are identified with rungs.
