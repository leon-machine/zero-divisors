---
id: neutrino.real-breaking-assumption
kind: claim
version: 1
title: 'The real-breaking assumption'
status: postulate
region: neutrino
subject: neutrinos
tags: [flavour-and-mixing, matter-asymmetry]
proposed_by:
  kind: ai
  session: decision-pass-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: typed
locators:
  paper: T15
  number: Prop 5.3(3)
  label: prop:leptogenesis
  line: 744
extraction:
  env: assumption in a proposition clause
  also_stated:
  - 'T15 Prop 4.4(3) (the double-beta values): "If the breaking is real in the vacuum''s basis (the real-breaking assumption of Proposition prop:leptogenesis(3))", line 647'
  - 'T15 levels paragraph: "the real-breaking assumption of Proposition prop:leptogenesis(3)", line 761'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 8
    note: New postulate. The series uses the real-breaking assumption by name (T15 Prop 5.3(3) and its registered CP stance, the double-beta values of Prop 4.4(3)) but the store had no entity for it, so it never reached holds_given (CONTRADICTIONS_VALUES M5). The formal level is the paper's own wording of clause (3).
---

## formal
\emph{The real-breaking assumption.} The breaking is real in the vacuum's basis: the Dirac and Majorana matrices are both built from one real geometric vacuum and one flavour-independent flag, and after the breaking $\delta$ of Lemma \claimref{neutrino.breaking-relation} both are real in the vacuum's basis, so that no relative phase $\varphi$ between them arises (T15, Proposition 5.3(3): ``if the breaking is real in the vacuum's basis the relative phases vanish and the injection is zero to all orders in it'').

## technical
The real-breaking assumption takes the second-order breaking $\delta$ of the democratic neutrino matrices to be real in the basis of the one real geometric vacuum from which the Dirac and Majorana matrices are built. Since the flag that also enters them is flavour-independent, no relative phase arises between the two family matrices after the breaking; the non-thermal injection of asymmetry by descent-populated heavy states then vanishes to all orders in $\delta$, and the Dirac phase of lepton mixing is trivial, $\delta_{CP} \in \{0, \pi\}$.

It is an assumption, not a result of the series: the paper flags the CP stance and the two-valued double-beta prediction as conditional on it, and without it the double-beta values revert to their hull. Confirmed leptonic CP violation with normal ordering established would show it false.

## lay
This is an assumption, not a result: the small distortion that gives the lighter neutrinos their masses is taken to involve no complex phase. If it holds, the framework predicts no matter-antimatter difference in how neutrinos mix and two sharp values for a rare nuclear decay rate; if it fails, those sharper predictions are lost.

## one-liner
Assumption: the neutrino sector's second-order breaking is real in the vacuum's basis, so no relative CP phase arises between the Dirac and Majorana matrices.
