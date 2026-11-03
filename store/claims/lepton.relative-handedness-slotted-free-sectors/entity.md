---
id: lepton.relative-handedness-slotted-free-sectors
kind: claim
version: 4
title: The relative handedness of the slotted and the free sectors
status: proved
region: lepton
subject: standard-model
tags: [chirality, hypercharge-and-anomalies, recovers-known-physics]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-lepton, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - lepton.content-constituent-space@4
  - lepton.imported-free-sector-anomaly-conditions@4
  assumes:
  - lepton.hyp-c-constituent@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12_lepton.py
  tags:
  - label:prop:orientation
- kind: check
  ref: check.py::check_first_listing_is_one_generation_anomaly_free
- kind: check
  ref: check.py::check_second_listing_is_anomalous
- kind: check
  ref: check.py::check_consistency_fixes_relative_handedness
locators:
  paper: T12-lepton
  number: Prop 3.3
  label: prop:orientation
  line: 282
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: both listings built from actions: the first is one generation with all four anomaly sums zero, the second gives 2/3 and -4/9, fixing epsilon = -1. Version 3 -> 4.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the halves T and T'' to S = Lambda^even W and S'' = Lambda^odd W, and the free and bare twistors to conformal spinors, at every level and in the proof; the anomaly arithmetic is untouched. S is glossed against the Dirac module Sp because the two macros render alike.'
  source_title: |-
    The relative handedness of the slotted and the free sectors
  source_formal: |-
    Assume (C), and list the doublets $Q = \Con_{1}$ and $L = \Con_{3}$ as particles of one handedness. (The arithmetic is that of \cite[Thm.~5.5(3), last clause]{ButlerT12}, with the signs of the two nonzero sums reversed, since T12 conjugates the doublets and this note conjugates the free sector, so the lists are overall conjugates; what is new is only its reading under (C).) There are two ways to list the free sector $\Sp = \Lambda^{\bullet}W$ with them.
    \begin{enumerate}
    \item If the $\T$ half of the free sector (grades $0$ and $2$) is listed with the $\T'$ half of the slot sector, the list is $Q, L, (1)_{0}, (\bar{3})_{-2/3}$, and the conjugates of the free $\T'$ half, $(\bar{3})_{+1/3}$ and $(1)_{+1}$: that is $Q, L, \nu^{c}, u^{c}, d^{c}, e^{c}$, one Standard Model generation with a right-handed neutrino, and all four anomaly conditions vanish.
    \item If the $\T'$ half of the free sector is listed with the slot sector's, the list is $Q, L, (3)_{-1/3}, (1)_{-1}$ and the conjugates $(1)_{0}, (3)_{+2/3}$, and the $[SU(3)]^{2}U(1)$ and cubic conditions read $+\tfrac23$ and $-\tfrac49$.
    \end{enumerate}
    So the consistency of gauging fixes the relative handedness, the bit $\epsilon$ of Hypothesis (C): the chirality half of a free twistor that is listed with the constituents' $\T'$ is $\T$, that is, $\epsilon = -1$, a slot reverses the half. Equivalently, in physical terms, the free-sector fields are $\nu^{c}$ and $u^{c}$ from $\T$ and $d_{R}$ and $e_{R}$ from $\T'$, four Weyl fields of the observed charges with no conjugation applied to any of them, and a bare free twistor is the neutrino singlet while a bare twistor in a slot is the antilepton.
  typing:
    by: ai-typing-pass
    added:
    - lepton.content-constituent-space
    - lepton.hyp-c-constituent
    note: 'Added the constituent-content proposition, which supplies the doublets Q, L and their hypercharges
      used in the sums; the Standard-Model hypercharge theorem in context_refs is cited only as having
      the same arithmetic, so it was not added, and no standard-route applies since the result is a reading
      under (C). Hypothesis pass: assumes lepton.hyp-c-constituent added because its statement assumes
      Hypothesis (C). Levels pass: the lay level now names Hypothesis (C) instead of ''a stated hypothesis''.'
  env: proposition
  context_refs:
  - standard-model.hypercharge-global-form-pair-counting-consistency
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - lepton.content-constituent-space
    stated_role:
    - lepton.hyp-c-constituent
    note: 'the assumed Hypothesis (C), not on the cite list, was also uncited; given a one-sentence role.'
---

## formal
Assume (C), and list the doublets $Q = \Con_{1}$ and $L = \Con_{3}$ as particles of one handedness. (The arithmetic is that of \cite[Thm.~5.5(3), last clause]{ButlerT12}, with the signs of the two nonzero sums reversed, since T12 conjugates the doublets and this note conjugates the free sector, so the lists are overall conjugates; what is new is only its reading under (C).) There are two ways to list the free sector $\Sp = \Lambda^{\bullet}W$ with them.
\begin{enumerate}
\item If the $\CS$ half of the free sector (grades $0$ and $2$) is listed with the $\CSm{}$ half of the slot sector, where $\CS = \Lambda^{\mathrm{even}}W$ is the conformal spinor space and $\CSm{} = \Lambda^{\mathrm{odd}}W$ its partner (twistor and dual twistor space), the two chirality halves of $\Sp$, the list is $Q, L, (1)_{0}, (\bar{3})_{-2/3}$, and the conjugates of the free $\CSm{}$ half, $(\bar{3})_{+1/3}$ and $(1)_{+1}$: that is $Q, L, \nu^{c}, u^{c}, d^{c}, e^{c}$, one Standard Model generation with a right-handed neutrino, and all four anomaly conditions vanish.
\item If the $\CSm{}$ half of the free sector is listed with the slot sector's, the list is $Q, L, (3)_{-1/3}, (1)_{-1}$ and the conjugates $(1)_{0}, (3)_{+2/3}$, and the $[SU(3)]^{2}U(1)$ and cubic conditions read $+\tfrac23$ and $-\tfrac49$.
\end{enumerate}
So the consistency of gauging fixes the relative handedness, the bit $\epsilon$ of Hypothesis (C): the chirality half of a free conformal spinor that is listed with the constituents' $\CSm{}$ is $\CS$, that is, $\epsilon = -1$, a slot reverses the half. Equivalently, in physical terms, the free-sector fields are $\nu^{c}$ and $u^{c}$ from $\CS$ and $d_{R}$ and $e_{R}$ from $\CSm{}$, four Weyl fields of the observed charges with no conjugation applied to any of them, and a bare free conformal spinor is the neutrino singlet while a bare conformal spinor in a slot is the antilepton.

## technical
Under Hypothesis (C), list the doublets $Q = \Con_{1}$ and $L = \Con_{3}$ in one handedness and add the free sector $\Sp = \Lambda^{\bullet}W$ in one of two ways. Listing the free half $\CS = \Lambda^{\mathrm{even}}W$ (grades $0$ and $2$) with the slot sector's $\CSm{} = \Lambda^{\mathrm{odd}}W$, and conjugating the free $\CSm{}$ half, gives $Q, L, \nu^{c}, u^{c}, d^{c}, e^{c}$ with hypercharges $(\tfrac16, -\tfrac12, 0, -\tfrac23, \tfrac13, 1)$, and all four anomaly sums vanish. The other listing gives $[SU(3)]^{2}U(1) = \tfrac23$ and a cubic sum of $-\tfrac49$.

So anomaly cancellation fixes the bit of (C) at $\epsilon = -1$: a slot reverses the chirality half. Physically the free fields are $\nu^{c}$ and $u^{c}$ from $\CS$ and $d_{R}$ and $e_{R}$ from $\CSm{}$, with no conjugation applied; a bare free conformal spinor is the neutrino singlet and a bare conformal spinor in a slot is the antilepton. The arithmetic is the Standard-Model paper's; what is new is its reading under (C).

## lay
Under Hypothesis (C), the quark and lepton doublets come from basic spinor states sitting in slots, while further particles come from free ones, and there are two ways to match the handedness of the two groups. Only one of them gives a theory free of quantum anomalies, and it is exactly one Standard Model generation with a right-handed neutrino. So a consistency requirement, rather than a separate assumption, fixes this one-bit choice.

## one-liner
Under Hypothesis (C), anomaly cancellation fixes the relative handedness of the slotted and free sectors at $\epsilon = -1$, giving one Standard Model generation with a right-handed neutrino.
