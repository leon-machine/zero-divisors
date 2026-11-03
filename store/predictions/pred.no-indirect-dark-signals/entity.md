---
id: pred.no-indirect-dark-signals
kind: prediction
version: 3
title: No indirect dark-sector signals
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
  threshold: Any confirmed indirect signal
  data_source: Indirect-detection surveys
  registered: 2026-08 (T17 stance table, row 8)
observations:
- date: 2026-10
  dataset: Fermi-LAT, AMS-02, XRISM
  result: 'No confirmed signal, but two claimed excesses are live: the Galactic Centre gamma-ray excess
    persists in 17.7 years of Fermi-LAT data, though dwarf-galaxy limits now exclude most of its dark-matter
    interpretations except some tau channels; a 20 GeV halo excess needs a cross-section 4 to 5 times
    above dwarf limits and ten times above AMS-02 antiproton limits. XRISM does not see the 3.5 keV line.'
  verdict: consistent
  source: Kim, Kang and Shin, arXiv:2610.26648 (2026); Di Mauro, arXiv:2605.22913 (2026); Stenhouse, Ghag
    and Deppisch, arXiv:2607.08552 (2026); XRISM, arXiv:2510.24560 (2025)
- date: 2026-08
  dataset: Indirect-detection surveys
  result: 'Indirect-detection surveys: null to date.'
  verdict: consistent
  source: T17 stance table, row 8
locators:
  paper: T14
  number: T17 stance 8
  label: tab:stances
extraction:
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: VALUES M6
    open_problem: op.small-findings
    note: 'VALUES M6: the gravity-only coupling behind this stance is the imported acoustic no-go, which holds within the s-wave current algebra at its mixed level, conditional on the Indifference premise and premise (Q); the levels now name that scope, those conditions and the first-order qualifier next to P1 for readability; once the gravity-only Fact is stored as a restatement of the series'' acoustic no-go (its correction filed alongside), the conditions also reach holds_given through the graph. Fix round: the gravity-only clause is first order, and the stance now rests on decay being excluded by the superselected tower charge and on graviton-mediated annihilation being suppressed by powers of E/M_P on a charge-asymmetric relic, not on the absence of an annihilation channel.'
  env: table row
  source: T17 tab:stances
  typing:
    by: ai-typing-pass
    note: 'No derivations to review; a plausible basis is the superselection and exact-stability proposition,
      not linked here. Basis linked at the end of the build, as the dark-matter typing pass proposed.
      Levels pass: all levels now say the stance is conditional on P1 through its basis, and the stale
      basis-not-linked flag was removed.'
derivations:
- name: basis
  uses:
  - dark-matter.superselected-hence-dark-exactly-stable@5
  - dark-matter.stored-asymmetry-charge-not-number@8
---

## formal
No indirect dark-sector signals: no decay products, since the tower charge is superselected, and annihilation products only at the rate of graviton exchange, suppressed by powers of $E/M_{P}$ on a charge-asymmetric relic.

## technical
In the framework dark matter couples to ordinary matter through gravity alone at first order. It cannot decay into ordinary particles, because its tower charge is superselected, and its only annihilation channel into them is graviton exchange, suppressed by powers of $E/M_{P}$ and acting on a charge-asymmetric relic with negligible anti-dark density (the mirror's stored asymmetry is a charge fixed by the descent, Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}). Indirect-detection surveys, which look for such annihilation or decay products, should see no dark-sector signal. This is registered as a conditional stance: its basis, the superselection and exact-stability result, rests on the single-frozen-point premise P1 and on the wall-sequence theorem's hypotheses, and its gravity-only clause, a first-order coupling statement, on the series' acoustic no-go, which holds within the s-wave current algebra and is conditional on the Indifference premise and premise (Q).

## lay
Some searches look for the leftovers of dark-matter particles destroying each other or breaking down, such as unexpected gamma rays. This framework says dark matter can turn into ordinary particles only through gravity, far too weakly to be seen, and that there is almost no anti-dark matter for it to meet, so those searches should find nothing. This expectation is conditional: it rests on the framework's premise of a single frozen point, from which exact stability follows, and on a result carried over from earlier work for the gravity-only coupling, which holds in a spherically averaged description and under two further assumptions of that work.

## one-liner
Conditionally on the single-frozen-point premise, and on the series' acoustic no-go (s-wave current algebra, Indifference premise, premise (Q)), indirect-detection surveys should see no dark-sector decay products, and no annihilation products above the gravitationally suppressed rate of a charge-asymmetric relic.
