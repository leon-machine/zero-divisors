---
id: families.imported-one-derived-generation-hypothesis-s
kind: claim
version: 7
title: 'Imported: one derived generation, and Hypothesis (S)'
status: proved
region: families
subject: standard-model
tags: [hypercharge-and-anomalies, recovers-known-physics, hypotheses-s-r-c]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass on Leon''s decisions, Hypothesis (S) described as derived from the slot-module premise'
  version: 7
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  uses:
  - standard-model.chirality-two-halves-spinor-module-conjugation@6
  - standard-model.hypercharge-global-form-pair-counting-consistency@5
  - standard-model.quarks-leptons-two-level-fermion-content@5
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_unconditional_content
- kind: check
  ref: check.py::check_lepton_doublet_only_under_s
- kind: check
  ref: check.py::check_uniqueness_and_necessity
- kind: check
  ref: check.py::check_chirality_halves_inequivalent
locators:
  paper: T13
  number: Fact 2.3
  label: fact:generation
  line: 589
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Stale status wording (DECISIONS G3, R04 item 1): the levels said Hypothesis (S) is ''a structural premise, not a theorem'' / ''declared there and open'', while the pinned standard-model.hyp-s-slot-statistics@9 is a proved claim derived from the postulate standard-model.slot-module-hypothesis; they now say (S) is derived in the store from that weaker premise, on which the charged-lepton statements rest. The paper''s sentence stays in source_formal; status, edges and pins unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the pair-level (2,3)_{1/6} and the single-spinor singlets from exact characters, the lepton doublet present in the five-mode module and absent from the tensor ledger, uniqueness of the hypercharges with the necessity of both hypotheses, and the inequivalent chirality halves. Version 5 -> 6.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the single-twistor singlets, Fock space and twistor slots to those of conformal spinors at every level and in the provenance proof.'
  source_title: |-
    Imported: one derived generation, and Hypothesis (S)
  source_formal: |-
    Under the global group $S(U(2) \times U(3))$ of the minimal massive composite: unconditionally, the pair-level generators transform as $(2,3)$ with $Y = 1/6$, the quark doublet, and the single-twistor singlets carry the hypercharges $0, -\tfrac23, \tfrac13, 1$, the latter as a computation on the single-twistor Fock space, which is not a subspace of the tensor state space. Under Hypothesis (S) (the twistor slots are fermionic modes on the same footing as the pairs, so the composite's state space is the five-mode Fock space), and only under it, the lepton doublet $(2,1)$ with $Y = -\tfrac12$ exists, and, given the content (the two doublets and the singlets listed in one handedness, with a fourth singlet of hypercharge zero or none) and the normalisation $Y_{Q} = 1/6$, the hypercharge spectrum of the generation is unique from the four anomaly conditions, the pair $\{Y_{u^{c}}, Y_{d^{c}}\}$ as an unordered set; the fourth-singlet and common-handedness hypotheses are both necessary there, and without the lepton doublet the anomaly conditions are different equations and the uniqueness is not claimed. Chirality is the parity grading of the Fock module, whose two halves carry inequivalent content. Hypothesis (S) is a structural premise, not a theorem of the series, and every statement of this paper about the charged leptons carries it. \emph{Provenance:} \cite[\S4-\S5, in particular Prop.~5.3, Thm.~5.5, Prop.~5.6]{ButlerT12}.
  typing:
    by: ai-typing-pass
    note: 'Kept the three cited series results as premises; Hypothesis (S) has no postulate entity, and
      the E204 comes from the chirality premise outside this list. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: lay and one-liner now keep
      the content, handedness and normalisation hypotheses of the uniqueness clause, and lay the unordered
      antiquark pair.'
    added:
    - standard-model.hyp-s-slot-statistics
  env: fact
  context_refs:
  - standard-model.chirality-two-halves-spinor-module-conjugation
  - standard-model.hypercharge-global-form-pair-counting-consistency
  - standard-model.quarks-leptons-two-level-fermion-content
  flags:
  - 'fact restating several series results: derived from them'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under the global group $S(U(2) \times U(3))$ of the minimal massive composite: unconditionally, the pair-level generators transform as $(2,3)$ with $Y = 1/6$, the quark doublet, and the singlets of a single conformal spinor (the single-twistor singlets) carry the hypercharges $0, -\tfrac23, \tfrac13, 1$, the latter as a computation on the Fock space of a single conformal spinor, which is not a subspace of the tensor state space. Under Hypothesis (S) (the slots of the conformal spinors are fermionic modes on the same footing as the pairs, so the composite's state space is the five-mode Fock space), and only under it, the lepton doublet $(2,1)$ with $Y = -\tfrac12$ exists, and, given the content (the two doublets and the singlets listed in one handedness, with a fourth singlet of hypercharge zero or none) and the normalisation $Y_{Q} = 1/6$, the hypercharge spectrum of the generation is unique from the four anomaly conditions, the pair $\{Y_{u^{c}}, Y_{d^{c}}\}$ as an unordered set; the fourth-singlet and common-handedness hypotheses are both necessary there, and without the lepton doublet the anomaly conditions are different equations and the uniqueness is not claimed. Chirality is the parity grading of the Fock module, whose two halves carry inequivalent content. Hypothesis (S), a premise of the Standard-Model paper, is derived in the store from the weaker slot-module premise (\claimref{standard-model.hyp-s-slot-statistics}, from Premise \claimref{standard-model.slot-module-hypothesis}), on which every statement of this paper about the charged leptons rests. \emph{Provenance:} \cite[\S4-\S5, in particular Prop.~5.3, Thm.~5.5, Prop.~5.6]{ButlerT12}.

## technical
Under the global group $S(U(2) \times U(3))$ of the minimal massive composite, the pair-level generators are unconditionally the quark doublet $(2,3)$ with $Y = 1/6$, and the singlets of a single conformal spinor carry $Y = 0, -\tfrac23, \tfrac13, 1$, a computation on the Fock space of a single conformal spinor, which is not a subspace of the tensor state space.

Only under Hypothesis (S), which makes the slots of the conformal spinors fermionic modes so that the state space is the five-mode Fock space, does the lepton doublet $(2,1)$ with $Y = -\tfrac12$ exist. Then, given the content listed in one handedness with a fourth singlet of hypercharge zero or none, and $Y_{Q} = 1/6$, the four anomaly conditions fix the hypercharge spectrum uniquely, with $\{Y_{u^{c}}, Y_{d^{c}}\}$ as an unordered set; both the fourth-singlet and the common-handedness hypotheses are needed. Chirality is the parity grading of the Fock module, whose two halves carry inequivalent content. Hypothesis (S), a premise of the Standard-Model paper, is derived in the store from the weaker slot-module premise, on which every charged-lepton statement of the families paper rests.

## lay
The families paper imports what the series has derived about one generation of matter. The quark doublet and the charges of single free spinor states come out with no extra assumption; the lepton doublet appears only if one adopts a stated hypothesis about how the slots those states occupy behave. With that hypothesis, and given the generation's particle content listed with one handedness, at most one extra neutral singlet and the quark doublet's charge as the unit, requiring the theory to be free of quantum anomalies fixes all the hypercharges of the generation, up to which of the two antiquark singlets takes which value. The store derives that hypothesis from a weaker stated premise about the constituents, and everything that paper says about charged leptons depends on that premise.

## one-liner
The quark doublet and the singlet hypercharges follow unconditionally, while the lepton doublet, and, given the one-handed content and $Y_{Q} = 1/6$, the anomaly-fixed uniqueness of the generation's hypercharges, hold only under Hypothesis (S).
