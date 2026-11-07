---
id: neutrino.real-breaking-assumption
kind: claim
version: 2
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
- name: Claude Opus 5.5
  role: 'maintainer pass, restatement adding the real charged-lepton clause at Leon''s decisions'
  version: 2
  source: maintainer pass 2026-11-07 (decisions)
review: typed
locators:
  paper: T15
  number: Prop 5.3(3)
  label: prop:leptogenesis
  line: 744
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Leon''s answer 3 (C2): the assumption now adds ''and the charged-lepton matrix is real in the same basis'', which delta_CP in {0, pi} also needs: synthesis.circulant-charged-leptons-excluded-with-real-neutrino-sectors (iv)(c) shows the complex Koide circulant as charged-lepton matrix, the electron on the democratic line and a real P_12-breaking neutrino sector give cos delta_CP = 0; the stored tau placement is excluded by its (iv)(b), so no stored result changes. Restatement of the postulate at Leon''s decision; plain levels to match.'
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
\emph{The real-breaking assumption.} The breaking is real in the vacuum's basis: the Dirac and Majorana matrices are both built from one real geometric vacuum and one flavour-independent flag, and after the breaking $\delta$ of Lemma \claimref{neutrino.breaking-relation} both are real in the vacuum's basis, so that no relative phase $\varphi$ between them arises (T15, Proposition 5.3(3): ``if the breaking is real in the vacuum's basis the relative phases vanish and the injection is zero to all orders in it''); and the charged-lepton matrix is real in the same basis. The last clause is what $\delta_{CP} \in \{0, \pi\}$ also needs: with a real $P_{12}$-breaking neutrino sector, the complex Koide circulant as charged-lepton matrix, with the electron on the democratic line, gives $\cos\delta_{CP} = 0$ (Proposition \claimref{synthesis.circulant-charged-leptons-excluded-with-real-neutrino-sectors}(iv)(c)).

## technical
The real-breaking assumption takes the second-order breaking $\delta$ of the democratic neutrino matrices to be real in the basis of the one real geometric vacuum from which the Dirac and Majorana matrices are built. Since the flag that also enters them is flavour-independent, no relative phase arises between the two family matrices after the breaking. The assumption also takes the charged-lepton matrix to be real in the same basis, which the triviality of the Dirac phase needs as well: a complex circulant charged-lepton matrix with a real neutrino sector can give a maximal phase. Then the non-thermal injection of asymmetry by descent-populated heavy states then vanishes to all orders in $\delta$, and the Dirac phase of lepton mixing is trivial, $\delta_{CP} \in \{0, \pi\}$.

It is an assumption, not a result of the series: the paper flags the CP stance and the two-valued double-beta prediction as conditional on it, and without it the double-beta values revert to their hull. Confirmed leptonic CP violation with normal ordering established would show it false.

## lay
This is an assumption, not a result: the small distortion that gives the lighter neutrinos their masses is taken to involve no complex phase, and the charged leptons' mass matrix is taken to be real in the same basis. If it holds, the framework predicts no matter-antimatter difference in how neutrinos mix and two sharp values for a rare nuclear decay rate; if it fails, those sharper predictions are lost.

## one-liner
Assumption: the neutrino sector's second-order breaking is real in the vacuum's basis, so no relative CP phase arises between the Dirac and Majorana matrices, and the charged-lepton matrix is real in the same basis.
