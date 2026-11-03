---
id: singularity.p-univalence
kind: claim
version: 2
title: '(P): univalence'
status: postulate
region: singularity
subject: descent
tags: [univalence, grading-and-parity]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
about:
- obj.singularity.grading-parity-automorphism
locators:
  paper: T05
  number: Premise 7.8
  label: prem:parity
  line: 1776
extraction:
  env: premise
  typing:
    by: ai-typing-pass
    note: 'Postulate with no derivation, so no edges; levels and typing record only.'
  merged_from:
  - id: state-selection.p-univalence
    version: 2
    locators:
      paper: T05-state-selection
      number: Premise 3.3
      label: prem:parity
      line: 183
    about:
    - obj.state-selection.grading-parity-automorphism
    lineage:
      motivated_by:
      - state-selection.imported-univalence-superselection-rule
    proof_files: []
    formal: |-
      Physical states of the ledger are even: $\omega \circ \alpha = \omega$, equivalently $\omega$ annihilates the odd sector $\Aod$.
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 7
    note: 'Merged the state-selection note''s Premise 3.3 (state-selection.p-univalence, retired to tombstones.yaml)
      into this entity: the same premise word for word, the note''s "ledger" being the boundary-mode algebra.
      Kept this statement and levels; no derivations on either side. The note''s about link (its own copy
      of the grading definition) and its lineage motivated_by the note''s univalence import are recorded
      above and not carried as links, so this entity''s substantive content and version (2) are unchanged
      and the dependants'' pins @2 stay valid.'
---

## formal
Physical states of the boundary modes are even: $\omega \circ \alpha = \omega$, equivalently $\omega$ annihilates the odd sector $\Aod$.

## technical
The premise (P) requires every physical state $\omega$ of the boundary modes to be even under the grading automorphism $\alpha$, that is $\omega \circ \alpha = \omega$. Equivalently, $\omega$ vanishes on the odd sector $\Aod$, so odd elements of the boundary-mode algebra have zero expectation value.

It is a premise, not a derived result: it restricts which states count as physical, and enters as an input wherever it is invoked.

## lay
This is an assumption, not a theorem. It says that the physical states of the modes living on the boundary give zero average to every quantity that changes fermion number by an odd amount. So expectation values never mix the even and odd parity sectors.

## one-liner
Premise: physical states of the boundary modes are even under the grading, $\omega \circ \alpha = \omega$, so they vanish on the odd sector.
