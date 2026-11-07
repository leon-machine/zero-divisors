---
id: pred.leptonic-cp-trivial
kind: prediction
version: 2
title: The leptonic CP phase is trivial
status: live
subject: neutrinos
tags: [live-prediction, flavour-and-mixing]
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
  threshold: Confirmed CP violation in the leptonic sector under normal ordering
  data_source: Joint long-baseline analyses allow CP conservation at three sigma under normal ordering
    and exclude it under inverted ordering.
  registered: 2026-08 (T17 stance table, row 5)
observations:
- date: 2025-10
  dataset: T2K + NOvA joint fit
  result: For normal ordering the 3 sigma interval for delta_CP is [-1.38 pi, 0.30 pi], containing both
    0 and pi. For inverted ordering CP conservation is excluded at 3 sigma, so the prediction needs normal
    ordering, which cosmology favours. No newer joint fit or JUNO ordering result as of November 2026.
  verdict: consistent
  source: T2K and NOvA, Nature (2025), arXiv:2510.19888; T2K, arXiv:2604.08259 (2026)
- date: 2026-08
  dataset: Joint long-baseline analyses allow CP conservation at three sigma under normal ordering and
    exclude it under inverted ordering.
  result: Joint long-baseline analyses allow CP conservation at three sigma under normal ordering and
    exclude it under inverted ordering.
  verdict: consistent
  source: T17 stance table, row 5
locators:
  paper: T15
  number: T17 stance 5
  label: tab:stances
extraction:
  env: table row
  source: T17 tab:stances
  flags:
  - 'basis not linked: no store claim clearly carries it yet'
  typing:
    by: ai-typing-pass
    added:
    - neutrino.leptogenesis-suppressed-alignment-reheating-premise-new
    note: 'linked the basis to the leptogenesis proposition, whose corollary registers this stance; the
      real-breaking assumption it rests on has no store postulate. Levels pass: the lay level and one-liner
      now name the real-breaking assumption, and the lay level replaces "stand or fall together", which
      overstated the link, with the one-directional dependence on the inverted ordering being excluded.'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 8
    note: "Assumes the real-breaking assumption, a new postulate: the stance is the corollary of the leptogenesis analysis under it, as the technical, lay and one-liner levels say. Predictions carry no proof text, so no citation is needed."
derivations:
- name: basis
  uses:
  - neutrino.leptogenesis-suppressed-alignment-reheating-premise-new@8
  assumes:
  - neutrino.real-breaking-assumption@1
---

## formal
The leptonic CP phase is trivial: $\delta_{CP} \in \{0, \pi\}$.

## technical
The prediction is $\delta_{CP} \in \{0, \pi\}$ for the Dirac phase of lepton mixing. It is the corollary of the leptogenesis analysis under the real-breaking assumption: the Dirac and Majorana matrices are built from one real vacuum and one flavour-independent flag, so no relative phase arises between them. It would fail on confirmed leptonic CP violation with normal ordering established; current joint long-baseline analyses allow CP conservation within three sigma for normal ordering and exclude it at three sigma for inverted ordering.

## lay
If the small symmetry breaking in the lepton sector is real (the paper's real-breaking assumption), the framework predicts that neutrinos and antineutrinos oscillate in the same way, with no CP violation in lepton mixing. Current long-baseline experiments still allow this if the masses have the normal ordering, which the framework also predicts, but exclude it at three sigma for the inverted ordering, so establishing the inverted ordering would refute this prediction along with that one.

## one-liner
Under the real-breaking assumption, the Dirac CP phase of lepton mixing is trivial, $\delta_{CP} \in \{0, \pi\}$.
