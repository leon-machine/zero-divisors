---
id: pred.no-dark-radiation
kind: prediction
version: 4
title: No dark radiation
status: live
subject: dark-matter
tags: [live-prediction]
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
  role: 'maintainer pass on Leon''s decisions, the cold-mirror exception stated at P2''s version-1 reach, with P2 as scoped leaving xi free'
  version: 3
  source: maintainer pass 2026-11-07 (decisions)
- name: Claude Fable 5.2
  role: 'pointer to the open problem on the imported graviton-exchange rate; prediction unchanged'
  version: 4
  source: maintainer pass of 2026-11-10
review: typed
kill_condition:
  threshold: One confirmed massless dark species
  data_source: CMB constraints (Planck 2018)
  registered: 2026-08 (T17 stance table, row 9)
observations:
- date: 2026-03
  dataset: BBN + Planck/ACT/SPT CMB + DESI BAO
  result: N_eff = 2.990 +- 0.070, consistent with the Standard Model 3.044; Delta N_eff below 0.107 at
    95%. One fully thermalised extra species is excluded, and so is the Delta N_eff a hot mirror would
    give, so the prediction still rests on the cold-mirror exception to P2.
  verdict: consistent
  source: Goldstein and Hill, arXiv:2603.13226 (2026); ACT DR6, arXiv:2503.14454 (2025)
- date: 2026-08
  dataset: CMB constraints (Planck 2018)
  result: 'CMB constraints (Planck 2018): consistent.'
  verdict: consistent
  source: T17 stance table, row 9
locators:
  paper: T14
  number: T17 stance 9
  label: tab:stances
extraction:
  maintainer_pass_2026_11_10_graviton:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 3 -> 4, by Leon''s decision of 10 November 2026 (flag now, derive later): one sentence added to the formal and technical levels pointing to open problem op.graviton-rate-as-classical-field-process. The prediction, its status, its kill condition and every number are unchanged.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.radiation-audit-what-theorem-closes-what repinned 7 -> 8 after reviewing its G1 restatement (the cold mirror is an exception to P2 at its version-1 reach, P2 as scoped leaves xi free, and the cold mirror then needs a non-equilibrium descent; the numbers are unchanged); the use here holds as cited.'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'G1 (DECISIONS; R05 item 2): the cold-mirror exception now says that it is an exception to P2 at its version-1 reach, that P2 as scoped (version 2, labels not states) leaves xi free (synthesis.tower-charge-sector-label-temperature-not), and that the cold mirror then needs a non-equilibrium descent (synthesis.cold-mirror-needs-non-equilibrium-descent); P2 is unchanged by Leon''s answer 2, so the sentence stands.'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 1
    note: 'Wording narrowed after decision 1 (T14 against T14c, CONTRADICTIONS_VALUES H1). The basis
      (the radiation audit) closes the mirror channel only if the mirror is cold, and T14c Prop 8.2
      (dark-tower-matter.mirrors-temperature-p2) shows that a cold mirror is an exception to P2, which
      is in this prediction''s holds_given: applied with the copy theorem''s reach, P2 gives xi = 1 and
      Delta N_eff = 7.45, which is the kill condition. The levels now state that the stance needs that
      exception. The kill condition, its threshold and data source, and the basis edge are unchanged.
      Original in source_formal.'
  source_formal: |-
    No dark radiation: $\Delta N_{\mathrm{eff}} \approx 0$, conditionally on the dark towers\' open channels closing, which holds if the descent\'s deposit is no hotter than the dark-matter paper\'s estimate.
  env: table row
  source: T17 tab:stances
  typing:
    by: ai-typing-pass
    note: 'Kept the basis edge to the radiation audit, which states the effective-species bound and its
      conditions. Levels pass: lay now keeps the open-channels condition as well as the deposit estimate.'
derivations:
- name: basis
  uses:
  - dark-matter.radiation-audit-what-theorem-closes-what@8
---

## formal
No dark radiation: $\Delta N_{\mathrm{eff}} \approx 0$, conditionally on the dark towers\' open channels closing, which holds if the descent\'s deposit is no hotter than the dark-matter paper\'s estimate, and only with the mirror\'s seeded temperature taken as a free datum: applied with the reach of the copy theorem, P2 gives the mirror $\xi = 1$ and $\Delta N_{\mathrm{eff}} = 7.45$ (Proposition \claimref{dark-tower-matter.mirrors-temperature-p2}), so the stance rests on an exception to P2 for the mirror. This is an exception to P2 at its version-1 reach; P2 as scoped leaves $\xi$ free (Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}), and the cold mirror then needs a non-equilibrium descent (Proposition \claimref{synthesis.cold-mirror-needs-non-equilibrium-descent}). The seeding floor behind the radiation audit imports a rate computed with a quantised gravitational field (Fact \claimref{dark-matter.imported-massless-graviton-production-rate}, flagged), which the series does not hold; whether the classical gauge field gives that rate, another or none is open problem op.graviton-rate-as-classical-field-process, and the prediction is unchanged until that is settled.

## technical
The prediction is $\Delta\Neff \approx 0$: the dark towers add no relativistic species to the radiation content measured in the cosmic microwave background. It is conditional on the dark towers' open channels closing, which holds if the descent's deposit is no hotter than the dark-matter paper's estimate. It also needs the mirror to be cold, which the T14c note shows is an exception to indifference (P2): applied with the copy theorem's reach, P2 makes the mirror as hot as our tower, $\Delta N_{\mathrm{eff}} = 7.45$, which would meet the kill condition. That is an exception to indifference at its version-1 reach; indifference as scoped (labels, not states) leaves $\xi$ free (Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}), and the cold mirror then needs a non-equilibrium descent (Proposition \claimref{synthesis.cold-mirror-needs-non-equilibrium-descent}). The seeding floor behind the radiation audit imports a rate computed with a quantised gravitational field (Fact \claimref{dark-matter.imported-massless-graviton-production-rate}, flagged), which the series does not hold; whether the classical gauge field gives that rate, another or none is open problem op.graviton-rate-as-classical-field-process, and the prediction is unchanged until that is settled.

## lay
The afterglow of the early universe records how many kinds of light, fast-moving particles existed at the time. The framework predicts that the dark towers add none, provided the remaining ways of heating them stay closed, which holds if the descent left them no hotter than the paper estimates. It also needs the mirror world to have started cold, which a later note (T14c) shows is an unstated exception to the framework's own indifference principle; applied evenly, that principle would make the mirror as hot as our world and the prediction would fail. As the principle is now scoped, it applies to labels such as charges and not to temperatures, so it leaves the mirror's temperature free; a cold mirror then needs the descent to have left the towers out of equilibrium.

## one-liner
The framework predicts no dark radiation, $\Delta\Neff \approx 0$, conditionally on the dark towers' open channels closing, which holds if the descent's deposit is no hotter than estimated, and on a cold mirror, an exception to P2 (T14c).
