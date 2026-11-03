---
id: pred.no-neutrinoless-double-beta
kind: prediction
version: 2
title: No neutrinoless double-beta signal at next-generation sensitivity
status: live
subject: neutrinos
tags: [live-prediction, seesaw-and-majorana]
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
  source: authorship disclosure of T15, deposited version
review: typed
kill_condition:
  threshold: A confirmed signal above the predicted window
  data_source: Double-beta programmes
  registered: 2026-08 (T17 stance table, row 10)
observations:
- date: 2025-12
  dataset: KamLAND-Zen (complete); GERDA + MAJORANA + LEGEND-200
  result: 'Xe-136: T1/2 above 3.8e26 yr (90%), m_bb below 28 to 122 meV. Ge-76 combined: T1/2 above 1.9e26
    yr. No signal. The predicted 1.3 to 3.9 meV lies below next-generation reach, so only a detection
    would be informative.'
  verdict: consistent
  source: KamLAND-Zen, PRL 135, 262501 (2025); LEGEND, arXiv:2509.21166, arXiv:2603.12884 (2026)
- date: 2026-08
  dataset: Double-beta programmes
  result: 'Double-beta programmes: the predicted values lie below the next generation projected 10 to
    20 meV band.'
  verdict: consistent
  source: T17 stance table, row 10
locators:
  paper: T15
  number: T17 stance 10
  label: tab:stances
extraction:
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: VALUES L3
    open_problem: op.small-findings
    note: 'The point values 1.5 and 3.7 meV are now given with the ranges of their basis (neutrino.rank-one-seesaw-ordering-sum-double (3)): 1.3 to 1.7 meV at relative phase pi and 3.5 to 3.9 meV at relative phase 0, over the oscillation-parameter ranges; the hull and the kill condition are unchanged.'
  source_formal: 'No neutrinoless double-beta signal at next-generation sensitivity: $m_{\beta\beta}$ at $1.5$ or $3.7$ meV under premise (H) and the real-breaking assumption, in the hull $1.3$ to $3.9$ meV without it.'
  env: table row
  source: T17 tab:stances
  typing:
    by: ai-typing-pass
    note: 'basis edges unchanged (rank-one seesaw, assuming (H)); the real-breaking assumption named in
      the statement has no store postulate. Levels pass: the lay level now states Premise (H) and the
      real-breaking assumption and gives the predicted window; it had presented the absence as unconditional
      (review item 3).'
derivations:
- name: basis
  uses:
  - neutrino.rank-one-seesaw-ordering-sum-double@8
  assumes:
  - neutrino.h-second-stage-hierarchical@1
---

## formal
No neutrinoless double-beta signal at next-generation sensitivity: $m_{\beta\beta}$ in $1.3$ to $1.7$ meV (relative phase $\pi$) or $3.5$ to $3.9$ meV (relative phase $0$) under premise (H) and the real-breaking assumption, the ranges spanning the measured mixing angles, and in the hull $1.3$ to $3.9$ meV without that assumption.

## technical
Under Premise (H) and the real-breaking assumption the effective double-beta mass is $1.3$ to $1.7$ meV or $3.5$ to $3.9$ meV (relative Majorana phase $\pi$ or $0$, the ranges spanning the measured mixing angles), and without the real-breaking assumption it lies in the hull $1.3$ to $3.9$ meV. Both lie below the next generation's projected sensitivity band near $10$ to $20$ meV, so no signal is predicted there; a confirmed signal above the predicted window would count against it.

## lay
Neutrinoless double-beta decay is a rare nuclear process that would show neutrinos are their own antiparticles. Assuming the framework's premise (H), that the lightest neutrino is nearly massless, the effective mass that sets the rate comes out at a few thousandths of an electronvolt, between about $1.3$ and $3.9$ meV, with the sharper windows $1.3$ to $1.7$ or $3.5$ to $3.9$ meV if the breaking is also assumed real. That is too small for the next generation of experiments to detect, so a clear signal there would count against the framework. The absence is conditional: it rests on premise (H).

## one-liner
Under Premise (H), $m_{\beta\beta}$ is a few meV, below next-generation double-beta sensitivity.
