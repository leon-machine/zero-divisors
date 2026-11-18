---
id: pred.leptonic-cp-trivial
kind: prediction
version: 3
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
- name: Claude Opus 5.5
  role: 'maintainer pass, real charged-lepton clause carried into the plain levels at Leon''s decisions'
  version: 3
  source: maintainer pass 2026-11-07 (decisions)
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
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3. Leon''s answer 3 (C2): the plain levels (technical, lay, one-liner) now carry ''with a real charged-lepton matrix'', the clause the real-breaking assumption gains at its version 2, and the assumes pin moves to neutrino.real-breaking-assumption@2; the formal and the kill condition are unchanged.'
  env: table row
  source: T17 tab:stances
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
  - neutrino.real-breaking-assumption@2
---

## formal
The leptonic CP phase is trivial: $\delta_{CP} \in \{0, \pi\}$.

## technical
The prediction is $\delta_{CP} \in \{0, \pi\}$ for the Dirac phase of lepton mixing. It is the corollary of the leptogenesis analysis under the real-breaking assumption, with a real charged-lepton matrix: the Dirac and Majorana matrices are built from one real vacuum and one flavour-independent flag, so no relative phase arises between them, and the assumption takes the charged-lepton matrix real in the same basis (without that clause a complex circulant charged-lepton matrix can give a maximal phase). It would fail on confirmed leptonic CP violation with normal ordering established; current joint long-baseline analyses allow CP conservation within three sigma for normal ordering and exclude it at three sigma for inverted ordering.

## lay
If the small symmetry breaking in the lepton sector is real and the charged leptons' mass matrix is real in the same basis (the real-breaking assumption), the framework predicts that neutrinos and antineutrinos oscillate in the same way, with no CP violation in lepton mixing. Current long-baseline experiments still allow this if the masses have the normal ordering, which the framework also predicts, but exclude it at three sigma for the inverted ordering, so establishing the inverted ordering would refute this prediction along with that one.

## one-liner
Under the real-breaking assumption, with a real charged-lepton matrix, the Dirac CP phase of lepton mixing is trivial, $\delta_{CP} \in \{0, \pi\}$.
