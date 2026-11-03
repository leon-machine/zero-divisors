---
id: pred.dark-matter-direct-detection-null
kind: prediction
version: 3
title: Direct detection stays null
status: live
subject: dark-matter
tags: [live-prediction, superselection]
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
  source: authorship disclosure of T14, deposited version
review: typed
kill_condition:
  threshold: Any confirmed dark-matter detection above the gravitational floor
  data_source: All direct-detection programmes
  registered: 2026-08 (T17 stance table, row 7)
observations:
- date: 2026-09
  dataset: LZ extended nuclear-recoil search (WS2024)
  result: One nuclear-recoil-like event at 248 +- 23 +- 23 keV in 220 live days; background-only disfavoured
    at 2.6 sigma global (3.4 sigma local). LZ claims no discovery; a rare background is still being sought,
    and no independent XENONnT or PandaX-4T check exists yet. Standard spin-independent searches stay
    null. A hint to watch, not a detection.
  verdict: consistent
  source: LZ Collaboration, arXiv:2609.02823 (2026)
- date: 2026-08
  dataset: All direct-detection programmes
  result: 'All direct-detection programmes: null to date.'
  verdict: consistent
  source: T17 stance table, row 7
locators:
  paper: T14
  number: T17 stance 7
  label: tab:stances
extraction:
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: VALUES M6
    open_problem: op.small-findings
    note: 'VALUES M6: the gravity-only coupling behind this stance is the imported acoustic no-go, which holds within the s-wave current algebra at its mixed level, conditional on the Indifference premise and premise (Q); the levels now name that scope, those conditions and the first-order qualifier next to P1 for readability; once the gravity-only Fact is stored as a restatement of the series'' acoustic no-go (its correction filed alongside), the conditions also reach holds_given through the graph. Fix round: the gravity-only clause is first order.'
  env: table row
  source: T17 tab:stances
  typing:
    by: ai-typing-pass
    note: 'No derivations to review; a plausible basis is the superselection and exact-stability proposition
      with the gravity-only coupling import, not linked here. Basis linked at the end of the build, as
      the dark-matter typing pass proposed. Levels pass: all levels now say the stance is conditional
      on P1 through its basis (review item 13), and the stale basis-not-linked flag was removed.'
derivations:
- name: basis
  uses:
  - dark-matter.superselected-hence-dark-exactly-stable@5
---

## formal
Permanent direct-detection nulls: dark matter couples through gravity alone, at first order.

## technical
In the framework dark matter sits in neighbouring towers that couple to this one only through the shared gravitational metric, with no portal interaction to ordinary matter. Direct-detection experiments, which look for non-gravitational scattering of dark matter off ordinary nuclei or electrons, should therefore return nulls permanently. This is registered as a conditional stance: its basis, the superselection and exact-stability result, rests on the single-frozen-point premise P1 and on the wall-sequence theorem's hypotheses, and its gravity-only clause, a first-order coupling statement, on the series' acoustic no-go, which holds within the s-wave current algebra and is conditional on the Indifference premise and premise (Q).

## lay
Experiments that try to catch dark-matter particles bumping into ordinary atoms should never see anything. In this framework dark matter lives in separate towers that touch ours only through gravity, which is far too weak to register in such detectors. This expectation is conditional: it rests on the framework's premise of a single frozen point, and on a result carried over from earlier work that holds in a spherically averaged description and under two further assumptions of that work.

## one-liner
Conditionally on the single-frozen-point premise, and on the series' acoustic no-go (s-wave current algebra, Indifference premise, premise (Q)), direct-detection searches should stay null permanently, because dark matter couples to ordinary matter through gravity alone at first order.
