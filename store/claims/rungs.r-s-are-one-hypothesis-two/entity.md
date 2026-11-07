---
id: rungs.r-s-are-one-hypothesis-two
kind: claim
version: 5
title: (R) and (S) are one hypothesis in two languages
status: proved
region: rungs
subject: standard-model
tags: [hypotheses-s-r-c, spinor-modules, pairing-and-bogoliubov]
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
  - rungs.imported-fock-representation-bogoliubov-group@4
  - rungs.imported-ladder-automorphism-group-no-lepton@4
  - rungs.imported-tower-one-qubit-per-rung@4
  - rungs.ladder-group-rung-mixing-group-one@4
  - rungs.mass-bracket-frozen-points-grip-slot@3
  - rungs.rung-spinor-module-mixings@5
  - standard-model.under-s-composites-state-space-spinor@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12_rungs.py
  tags:
  - label:prop:equiv
- kind: check
  ref: check.py::check_r_and_s_are_the_same_module
- kind: check
  ref: check.py::check_constituent_sector_and_generation
- kind: check
  ref: check.py::check_bogoliubov_spin10
locators:
  paper: T12-rungs
  number: Prop 2.6
  label: prop:equiv
  line: 283
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the (R) and (S) Fock models are one CAR system under the slot-rung identification (actions, grading, chirality), the j = 1 sector and the generation, and the so(10) bilinears. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted ''each twistor occupies one rung'' (proof) and the two-twistor wording of the lay and one-liner to conformal spinors; the formal level had no twistor language.'
  source_title: |-
    (R) and (S) are one hypothesis in two languages
  source_formal: |-
    Given Facts \claimref{rungs.imported-tower-one-qubit-per-rung} and \claimref{rungs.imported-fock-representation-bogoliubov-group}, Hypothesis (R) at $n = 2$ implies Hypothesis (S); and (S), together with the identification of the two slots with the two rungs, implies (R) at $n = 2$. At $n = 2$ that identification is a relabelling of two basis vectors, so (R) and (S) are equivalent up to it. Under either, the constituent hypothesis of T12's successor problem (6), a slot vector times a Dirac state with the slot mixing acting once, holds as the $j = 1$ sector; the derived generation is the even half of the module (Fact \claimref{standard-model.under-s-composites-state-space-spinor}); the mass bracket is the pairing of Lemma \claimref{rungs.mass-bracket-frozen-points-grip-slot}; and $\mathrm{Spin}(10)$ is the Bogoliubov group of the composite's modes.
  env: proposition
  context_refs:
  - rungs.imported-fock-representation-bogoliubov-group
  typing:
    by: ai-typing-pass
    added:
    - rungs.imported-fock-representation-bogoliubov-group
    note: 'Added the Fock-representation fact, named in the statement''s hypotheses ("Given Facts"); kept
      all six existing edges, each cited in the proof. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - rungs.imported-fock-representation-bogoliubov-group
---

## formal
Given Facts \claimref{rungs.imported-tower-one-qubit-per-rung} and \claimref{rungs.imported-fock-representation-bogoliubov-group}, Hypothesis (R) at $n = 2$ implies Hypothesis (S); and (S), together with the identification of the two slots with the two rungs, implies (R) at $n = 2$. At $n = 2$ that identification is a relabelling of two basis vectors, so (R) and (S) are equivalent up to it. Under either, the constituent hypothesis of T12's successor problem (6), a slot vector times a Dirac state with the slot mixing acting once, holds as the $j = 1$ sector; the derived generation is the even half of the module (Fact \claimref{standard-model.under-s-composites-state-space-spinor}); the mass bracket is the pairing of Lemma \claimref{rungs.mass-bracket-frozen-points-grip-slot}; and $\mathrm{Spin}(10)$ is the Bogoliubov group of the composite's modes.

## technical
Given the tower's one-qubit-per-rung structure and the Fock representation with its Bogoliubov group, the rung reading (R) at $n = 2$ implies the slot-statistics hypothesis (S), and (S) together with the identification of the two slots with the two rungs implies (R) at $n = 2$. At $n = 2$ that identification relabels two basis vectors, so the hypotheses are equivalent up to it: they share the module $\Lambda^{\bullet}(W \oplus \C^{2})$, its $(j,k)$ grading, the group action and the chirality $(-1)^{j+k}$.

Under either hypothesis, the constituent hypothesis (a slot vector times a Dirac state, with the slot mixing acting once) holds as the $j = 1$ sector, the derived generation is the even half of the module, the mass bracket is the frozen-point pairing, and $\mathrm{Spin}(10)$ is the Bogoliubov group of the composite's modes.

## lay
The rung note offers two ways of saying what the internal states of a composite of two basic spinor states are: one in the language of the algebraic tower, one in the language of fermionic modes. This result shows that they say the same thing, apart from one relabelling that matches the two slots with the two new rungs. Either way, one generation of matter is the even half of the state space.

## one-liner
At two conformal spinors the rung reading (R) and the slot-statistics hypothesis (S) are equivalent up to identifying slots with rungs, and under either the derived generation is the even half of the module and $\mathrm{Spin}(10)$ is the Bogoliubov group.
