---
id: pred.no-objective-collapse
kind: prediction
version: 2
title: No objective-collapse signature
status: live
subject: one-relation
tags: [live-prediction, measurement-and-records]
region: programme
proposed_by:
  kind: extraction
  session: full-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
review: typed
kill_condition:
  threshold: One confirmed collapse signature
  data_source: Collapse-model tests
  registered: 2026-08 (T17 stance table, row 12)
observations:
- date: 2026-01
  dataset: XENONnT; nanoparticle interferometry
  result: No collapse signature. XENONnT bounds Markovian CSL at lambda/rC^2 below 3.0e-3 per second per
    square metre (90%), excluding the originally proposed CSL range; sodium-cluster interferometry above
    170,000 amu shows full quantum behaviour. Only a detection would decide the prediction.
  verdict: consistent
  source: XENON, arXiv:2506.05507 (2025); Pedalino et al., Nature (2025)
- date: 2026-08
  dataset: Collapse-model tests
  result: 'Collapse-model tests: null to date.'
  verdict: consistent
  source: T17 stance table, row 12
locators:
  paper: T16
  number: T17 stance 12
  label: tab:stances
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: one-relation.record-chain-votes-measurement-without-collapse repinned 6 -> 7 after reviewing its B3 restatement (it now assumes the postulate one-relation.recorded-sectors-superselected-premise where it cited Remark rem:recording; the conclusion is unchanged); the use here holds as cited.'
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: VALUES L8
    open_problem: op.small-findings
    note: 'One-liner now says the prediction rests on the record-chain account and its premises (including irreversible recording, indifference and Hypothesis (S); the full list is the derived holds_given), as the technical and lay levels already do.'
  env: table row
  source: T17 tab:stances
  typing:
    by: ai-typing-pass
    note: 'Basis edge to the record-chain proposition kept; kill condition untouched. Levels pass: the
      formal is unconditional; the lay level now says, as the technical does, that the prediction rests
      on the record-chain account under its premises.'
derivations:
- name: basis
  uses:
  - one-relation.record-chain-votes-measurement-without-collapse@8
---

## formal
No objective-collapse signature: no spontaneous-localisation noise, no gravitationally induced collapse.

## technical
The prediction is that no objective-collapse signature will be found at any sensitivity: no spontaneous-localisation noise and no gravitationally induced collapse. It rests on the record-chain account of measurement, under its premises, in which all branches are occupied and a collapse mechanism would be the uncaused selector the framework forbids. Null results are consistent with it, and one confirmed collapse signature refutes it together with the counting argument behind it.

## lay
Some proposed theories say quantum superpositions collapse on their own, perhaps because of gravity, and these would leave tiny detectable traces such as extra random noise. This framework predicts that no such traces exist at any level of sensitivity. The prediction rests on the framework's account of measurement, under that account's premises. Experiments so far have found none, and a single confirmed detection would refute the prediction together with the argument behind it.

## one-liner
Under the record-chain account of measurement and its premises, including irreversible recording, indifference and Hypothesis (S), no objective-collapse signature, neither spontaneous-localisation noise nor gravitationally induced collapse, will be found at any sensitivity.
