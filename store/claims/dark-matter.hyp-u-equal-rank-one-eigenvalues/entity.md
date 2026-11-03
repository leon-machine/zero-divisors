---
id: dark-matter.hyp-u-equal-rank-one-eigenvalues
kind: claim
version: 3
title: 'Hypothesis (U): equal rank-one eigenvalues at the ceiling'
status: postulate
region: dark-matter
subject: neutrinos
tags:
- hypothesis-u
- mass-generation
proposed_by:
  kind: human
  author: leon (stated in the paper); entered by the build
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
locators:
  paper: T14
  number: Hypothesis (U)
  label: ''
  line: 596
extraction:
  env: hypothesis
  typing:
    by: ai-typing-pass
    note: Stated inline in the ceiling proposition as the paper's own hypothesis, attacked in its premises section;
      formal text is the defining clause verbatim.
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 11
    note: 'Linked as contradicting Premise (EW) of T12: (U) makes the neutrino''s Dirac entry in the heavy direction
      the common rank-one value m_t at the ceiling, while (EW) sets (M_nu)_33 = 0 in the top''s direction (seed/CONTRADICTIONS_VALUES.md
      M4). No result may rest on both.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Version 3 rewords the rationale of the contradicts link to standard-model.premise-ew-equal-weight; the link
      is kept and the formal level is unchanged. Rationale now: contradicts in the entry reading of (U), (M_nu)_33 = m_t;
      consistent in the eigenvalue reading, which is what the formal level states.'
  contradicts_rationale: 'Hypothesis (U) and Premise (EW) contradict in the entry reading of (U), (M_nu)_33 = m_t, since
    (EW) sets the neutrino Dirac entry in the top''s direction to zero; they are consistent in the eigenvalue reading
    (equal rank-one eigenvalues), with or without a rank-one presupposition. Sources: synthesis.hypothesis-u-under-ew-is-a-charged-fermion-condition
    (under (S) and (EW), without a 120, (U) is a condition on the down-minus-lepton matrix, with a rank-one witness
    for the eigenvalue reading) and synthesis.hypothesis-u-readings-on-the-rung-coupling-line (the top and bottom
    readings of (U) on the rung coupling line). If the sectors share their leading direction, (EW) excludes both
    readings. The link is kept to record the entry reading''s conflict, so a result resting on both is still flagged.'
contradicts:
- standard-model.premise-ew-equal-weight@1
---

## formal
\emph{Hypothesis (U)}, that the rank-one eigenvalues of the different sectors coincide at the ceiling, so that the neutrino's Dirac eigenvalue $m_{D}$ there is the common leading-order value, which the top retains and the second-order breaking splits for the down-type and charged-lepton sectors.

## technical
Hypothesis (U) states that the rank-one eigenvalues of the different fermion sectors coincide at the ceiling, so that the neutrino's Dirac eigenvalue $m_{D}$ there is the common leading-order value, which the top retains and the second-order breaking splits for the down-type and charged-lepton sectors.

The alignment of the families paper gives one rank-one Dirac mass per sector but never equates magnitudes across sectors; (U) supplies that equality as a hypothesis, not a theorem. Its two readings, the neutrino's Dirac mass retained like the top's or split like the bottom's, are the ends of the range in which the scales that depend on it are valued.

## lay
This is an assumption, not a result: at the highest energy the framework describes, the basic mass of each kind of matter particle is taken to be one common number. The top quark keeps that value, while smaller later effects pull the others apart. Because the assumption can be read in two ways, the quantities that rest on it come as ranges rather than single values.

## one-liner
Premise (U): the rank-one eigenvalues of the fermion sectors coincide at the ceiling, so the neutrino's Dirac eigenvalue there is the common leading-order value.
