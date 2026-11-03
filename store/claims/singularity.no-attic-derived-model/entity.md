---
id: singularity.no-attic-derived-model
kind: claim
version: 6
title: No attic, derived in the model
status: proved
region: singularity
subject: entropy
tags: [entropy-premises]
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
derivations:
- name: main
  assumes:
  - singularity.rate-models-kinematic-inputs-l-u@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:11.4
- kind: check
  ref: check.py::check_two_sectors_exhaust_the_qubits
- kind: check
  ref: check.py::check_sector_spectra_agree
- kind: check
  ref: check.py::check_evicted_correlations_stay_in_the_sectors
locators:
  paper: T05
  number: Prop 11.4
  label: prop:noattic
  line: 2255
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: two-sector exhaustiveness, equal sector trace moments, and the evicted qubit''s correlations kept inside L u R on two runs. Version 3 -> 4. check_sector_spectra_agree: full nonzero spectra of rho_R and rho_L compared (explicit orthogonal eigenvectors of rho_R) at all 13 stages, replacing moments m <= 3 with stages > 6 radiation qubits skipped; check_evicted_correlations_stay_in_the_sectors: complement spectrum {c^2, s^2} and mutual information 2 h_j computed (formal entropy combination); docstrings reworded. Version 4 -> 5. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 5 -> 6.'
  env: proposition
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    - sheaf.one-sided-completion-singularity
    - tower.answers-iteration-question
    added:
    - singularity.rate-models-kinematic-inputs-l-u
    note: 'The proof runs on (L), (U) and (C) alone, so the rate-model postulate was added; the tower
      and one-sided-completion citations bear on what the proof does not establish (exhaustiveness of
      the two sectors) and were removed with the transport-algorithm repair edge, the one-sided completion
      being the removal I am least sure of. Levels pass: the lay level now names the rate-model inputs
      (L), (U) and (C).'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - singularity.rate-models-kinematic-inputs-l-u
---

## formal
Under (L), (U) and (C): modes exiting the window carry no q-number content out of the two-sector decomposition; their correlations are placed, at eviction, in $L(t) \cup R(t)$. The no-attic axiom (A) is a theorem of the model's kinematics.

## technical
Under the rate-model inputs (L), (U) and (C), the state space at each stage is exactly $H_{L(t)} \otimes H_{R(t)}$, with no third tensor factor; an eviction transfers one mode's factor from $L$ to $R$, and a unitary step preserves all correlations. Hence modes leaving the window carry no q-number content out of the two-sector decomposition: their correlations remain in $L(t) \cup R(t)$.

The no-attic axiom is thus a theorem of the model's kinematics. Whether the two sectors exhaust real evaporation is not established here and stays inside premise (L).

## lay
An attic would be a hidden third place, besides the black hole's interior modes and its radiation, where information could end up. In the framework's model, granting its rate-model inputs (L), (U) and (C), the bookkeeping has only those two places, so information leaving the interior must go into the radiation. Whether real black holes have no such third place is still an assumption, now stated openly.

## one-liner
Under (L), (U) and (C), evicted modes keep their correlations within $L(t) \cup R(t)$, so the no-attic axiom holds in the model.
