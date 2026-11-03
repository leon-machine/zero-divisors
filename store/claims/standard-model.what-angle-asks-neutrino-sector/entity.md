---
id: standard-model.what-angle-asks-neutrino-sector
kind: claim
version: 4
title: What the angle asks of the neutrino sector
status: proved
region: standard-model
subject: neutrinos
tags: [seesaw-and-majorana, running-and-unification]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
derivations:
- name: main
  uses:
  - standard-model.chain@8
  - standard-model.imported-clebsch-structure-seesaw@1
  - standard-model.matching-traces@4
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_triplet_vev
- kind: check
  ref: check.py::check_effective_dirac_mass
locators:
  paper: T12
  number: Prop 11.2
  label: prop:requirement
  line: 2036
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: at the record values, v_R = M_I/g_R = 4.154e10 (displayed 4.2e10) GeV and m_D = sqrt(m_3 f_J v_R) = 1.44 sqrt(f_J) GeV on the seesaw M_R = f_J v_R. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'edges unchanged (chain, matching traces, Clebsch seesaw, all real premises); its E204 comes
      from the chain, outside this group. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: the lay and one-liner now state
      Hypothesis (S), which both had dropped, and the conditional seesaw route; both now name the chain
      with the $(15,2,2)$ at central values.'
    added:
    - standard-model.hyp-s-slot-statistics
  source_title: 'What the angle asks of the neutrino sector'
  source_formal: |-
    Under Hypothesis (S), on the chain of Proposition \claimref{standard-model.chain} with the $(15,2,2)$, at the record's central values: $M_{I} = 1.95 \times 10^{10}$ GeV and $g_{R}(M_{I}) = 0.469$, so the triplet vev is $v_{R} = M_{I}/g_{R} = 4.15 \times 10^{10}$ GeV. If the heaviest light neutrino, $m_{3} = 0.050$ eV \cite{PDG2024}, takes its mass through the seesaw from the heavy family direction, with Majorana coupling $f_{J}$ there, the effective Dirac mass along that direction is
    \[
    m_{D} \;=\; \sqrt{m_{3}\,f_{J}\,v_{R}} \;=\; 1.44\,\sqrt{f_{J}}\ \text{GeV}.
    \]
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Only the lay level named twistors (in glossing Hypothesis (S)); it now speaks of the slots of the conformal spinors. Formal level and proof unchanged.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - standard-model.hyp-s-slot-statistics
    note: "Proof is an exact or record-level run with no step naming (S); stated its role, the lepton doublet of the derived content, from Theorem hypercharge-global-form and Proposition weak-angle, which put the lepton doublet under (S)."
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
payload:
- kind: value
  clause: M_I, g_R and v_R as displayed
  python: sig_round(MI, 3) == (195, 10) and sig_round(GR, 3) == (469, -1) and sig_round(MI / GR, 3) ==
    (415, 10)
  note: 1.95e10 GeV, 0.469 and 4.15e10 GeV from the record's 1.948e10 and 0.4690
- kind: value
  clause: m_D = 1.44 sqrt(f_J) GeV
  quantity: quantity.heaviest-neutrino-mass
  python: M3_STATED == F('0.050') * EV and round_sqrt(M3_STATED * MI / GR * 10 ** 4) == 144
---

## formal
Under Hypothesis (S), on the chain of Proposition \claimref{standard-model.chain} with the $(15,2,2)$, at the record's central values: $M_{I} = 1.95 \times 10^{10}$ GeV and $g_{R}(M_{I}) = 0.469$, so the triplet vev is $v_{R} = M_{I}/g_{R} = 4.15 \times 10^{10}$ GeV. If the heaviest light neutrino, $m_{3} = 0.050$ eV \cite{PDG2024}, takes its mass through the seesaw from the heavy family direction, with Majorana coupling $f_{J}$ there, the effective Dirac mass along that direction is
\[
m_{D} \;=\; \sqrt{m_{3}\,f_{J}\,v_{R}} \;=\; 1.44\,\sqrt{f_{J}}\ \text{GeV}.
\]

## technical
Under Hypothesis (S), on the symmetry-breaking chain with the $(15,2,2)$ at the record's central values, $M_{I} = 1.95 \times 10^{10}$ GeV and $g_{R}(M_{I}) = 0.469$, so the triplet vev is $v_{R} = M_{I}/g_{R} = 4.15 \times 10^{10}$ GeV. If the heaviest light neutrino, $m_{3} = 0.050$ eV, takes its mass through the seesaw from the heavy family direction with Majorana coupling $f_{J}$ there, the effective Dirac mass along that direction is $m_{D} = \sqrt{m_{3}f_{J}v_{R}} = 1.44\sqrt{f_{J}}$ GeV.

## lay
Assuming the slots of the conformal spinors behave like the pairs (Hypothesis (S)), and given the intermediate energy scale that the unified model's running couplings produce on the chain with the extra $(15,2,2)$ field, at the measured couplings' central values, this result works out how large the neutrino's ordinary (Dirac) mass must be, along the heaviest family direction, if the observed heaviest neutrino mass comes through the seesaw from that direction. The answer is about 1.4 GeV times the square root of a coupling that is not yet known.

## one-liner
Under (S), on the chain with the $(15,2,2)$ at the record's central values, if $m_{3}$ comes through the seesaw from the heavy family direction, the Dirac mass there is $m_{D} = 1.44\sqrt{f_{J}}$ GeV.
