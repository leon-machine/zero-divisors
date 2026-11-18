---
id: pred.no-indirect-dark-signals
kind: prediction
version: 6
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
- name: Claude Opus 5.5
  role: consistency pass, the asymmetric-relic clause restricted to the mirror
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Fable 5.2
  role: 'pointer to the open problem on the imported graviton-exchange rate; prediction unchanged'
  version: 5
  source: maintainer pass of 2026-11-10
- name: Claude Fable 5.2
  role: 'the sentence on graviton exchange reworded: the pair-to-pair transition and its rate are now derived in the store without a quantum of the gravitational field; prediction, kill condition and status unchanged'
  version: 6
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-navigate)'
amendments:
- version: 6
  kind: restatement
  defect: 'the formal and technical levels said that graviton exchange imports a process the series does not hold and left open whether the classical gauge field gives an annihilation channel at that rate, at another or at none; the pair-to-pair transition through the gravitational field is now derived in the store from the operator source, with corrected coefficients for the thermal rate'
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
  maintainer_pass_2026_11_18:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 5 -> 6, at Leon''s decision of 18 November 2026. The sentence of 10 November pointing to open problem op.graviton-rate-as-classical-field-process is replaced, at the formal and technical levels, by one saying that the pair-to-pair transition through the gravitational field and its rate are derived in the store (synthesis.gravitational-pair-production-from-the-operator-source-at-first-order, clauses (ii) and (v)), under that result''s hypothesis (OS) or on the standard account. The prediction, its status, its kill condition and its threshold are unchanged. The basis pin to dark-matter.stored-asymmetry-charge-not-number moves to its version of the same day (the charge reading used here is unchanged).'
  maintainer_pass_2026_11_10_graviton:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 4 -> 5, by Leon''s decision of 10 November 2026 (flag now, derive later): one sentence added to the formal and technical levels pointing to open problem op.graviton-rate-as-classical-field-process. The prediction, its status, its kill condition and every number are unchanged.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.stored-asymmetry-charge-not-number repinned 8 -> 9 after reviewing its G1 restatement (the cold mirror is an exception to P2 at its version-1 reach, P2 as scoped leaves xi free, and the cold mirror then needs a non-equilibrium descent; the charge reading and the numbers are unchanged); the use here holds as cited.'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The formal, technical and lay levels described all dark matter as a charge-asymmetric relic with negligible anti-dark density; that holds for the mirror only, the odd towers'' matter being symmetric (dark-matter.population-count-one-share-half-percent(ii)). The stance is unchanged, since graviton exchange alone suppresses visible annihilation; wording only, kill condition untouched.'
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
  - dark-matter.stored-asymmetry-charge-not-number@13
---

## formal
No indirect dark-sector signals: no decay products, since the tower charge is superselected, and annihilation products only at the rate of graviton exchange, suppressed by powers of $E/M_{P}$, and for the mirror, a charge-asymmetric relic, further by its negligible anti-mirror density. The words ``graviton exchange'' name the process as its sources compute it; the series holds no quantum of the gravitational field (conventions, section ``Gravity and the graviton''). The store now derives the transition of a pair of one species into a pair of another through the gravitational field from the operator source, with no such quantum, at a rate carrying $\bar{M}_{P}^{-4}$ and with corrected coefficients for the thermal rate (Theorem \claimref{synthesis.gravitational-pair-production-from-the-operator-source-at-first-order}(ii) and (v), under its hypothesis (OS); the standard account gives the same tree-level rate), so the annihilation channel is the gravitationally suppressed one this stance assumes, and the prediction is unchanged.

## technical
In the framework dark matter couples to ordinary matter through gravity alone at first order. It cannot decay into ordinary particles, because its tower charge is superselected, and its only annihilation channel into them is graviton exchange, suppressed by powers of $E/M_{P}$; for the mirror it acts on a charge-asymmetric relic with negligible anti-mirror density (the mirror's stored asymmetry is a charge fixed by the descent, Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}), while the odd towers' matter, if any, is a symmetric relic (Proposition \claimref{dark-matter.population-count-one-share-half-percent}(ii)) whose annihilation into this tower is held down by the graviton suppression alone. Indirect-detection surveys, which look for such annihilation or decay products, should see no dark-sector signal. This is registered as a conditional stance: its basis, the superselection and exact-stability result, rests on the single-frozen-point premise P1 and on the wall-sequence theorem's hypotheses, and its gravity-only clause, a first-order coupling statement, on the series' acoustic no-go, which holds within the s-wave current algebra and is conditional on the Indifference premise and premise (Q). The words ``graviton exchange'' name the process as its sources compute it; the series holds no quantum of the gravitational field (conventions, section ``Gravity and the graviton''). The store now derives the transition of a pair of one species into a pair of another through the gravitational field from the operator source, with no such quantum, at a rate carrying $\bar{M}_{P}^{-4}$ and with corrected coefficients for the thermal rate (Theorem \claimref{synthesis.gravitational-pair-production-from-the-operator-source-at-first-order}(ii) and (v), under its hypothesis (OS); the standard account gives the same tree-level rate), so the annihilation channel is the gravitationally suppressed one this stance assumes, and the prediction is unchanged.

## lay
Some searches look for the leftovers of dark-matter particles destroying each other or breaking down, such as unexpected gamma rays. This framework says dark matter can turn into ordinary particles only through gravity, far too weakly to be seen (and that in the mirror world there is almost no anti-matter for its matter to meet), so those searches should find nothing. This expectation is conditional: it rests on the framework's premise of a single frozen point, from which exact stability follows, and on a result carried over from earlier work for the gravity-only coupling, which holds in a spherically averaged description and under two further assumptions of that work.

## one-liner
Conditionally on the single-frozen-point premise, and on the series' acoustic no-go (s-wave current algebra, Indifference premise, premise (Q)), indirect-detection surveys should see no dark-sector decay products, and no annihilation products above the gravitationally suppressed rate of a charge-asymmetric relic.
