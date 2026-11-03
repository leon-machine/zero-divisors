---
id: neutrino.h-second-stage-hierarchical
kind: claim
version: 1
title: 'H: the second stage is hierarchical'
status: postulate
region: neutrino
subject: neutrinos
tags: [neutrino-premises, flavour-and-mixing]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T15, deposited version
review: typed
locators:
  paper: T15
  number: Premise 4.5
  label: prem:H
  line: 642
extraction:
  env: premise
  context_refs:
  - neutrino.breaking-relation
  unresolved_refs:
  - rem:currency
  typing:
    by: ai-typing-pass
    note: 'postulate: no edges; levels only.'
---

## formal
The breaking $S_{3} \to S_{2} \to 1$ lifts $m_{1}$ by a factor small compared with the factor that lifts $m_{2}$: $m_{1}/m_{2} \lesssim 0.01$, that is $m_{1} \lesssim 0.1$ meV. The charged sectors supply the analogy at $m_{e}/m_{\mu} \approx 0.005$ and $m_{u}/m_{c} \approx 0.002$ \cite{PDG2024}; by Lemma \claimref{neutrino.breaking-relation} the light masses go as the \emph{squared} singular values of the compressed breaking where the charged masses go as the singular values themselves, so a shared direction would give $m_{1}/m_{2} \approx (m_{e}/m_{\mu})^{2}$, far below what (H) needs, and if the directions are not shared the analogy is only that hierarchies are the rule. Under (H) the sum is the floor to within about $0.1$ meV ($0.1007$ meV at the premise's boundary, the residue being $m_{1}$ plus the small lift of $m_{2}$ and $m_{3}$), and the double-beta values of (3) hold to within $0.1$ meV; without it the sum is a lower bound, with $m_{1}$ free up to order $m_{2}$, where it would reach roughly $0.07$ eV.

## technical
Premise (H) states that the second stage of the breaking $S_{3} \to S_{2} \to 1$ lifts the lightest mass far less than the first stage lifts the middle one: $m_{1}/m_{2} \lesssim 0.01$, so $m_{1} \lesssim 0.1$ meV. The charged sectors are hierarchical ($m_{e}/m_{\mu} \approx 0.005$, $m_{u}/m_{c} \approx 0.002$), and since the light neutrino masses go as the squared singular values of the compressed breaking, a shared breaking direction would give $m_{1}/m_{2} \approx (m_{e}/m_{\mu})^{2}$; if the directions are not shared, the analogy says only that hierarchies are the rule.

Under (H) the mass sum is the floor to within about $0.1$ meV and the double-beta values hold to the same accuracy; without it the sum is only a lower bound, with $m_{1}$ free up to order $m_{2}$, where the sum would reach roughly $0.07$ eV.

## lay
This is an assumption, not a result: the lightest neutrino gets almost no mass, less than a hundredth of the next one. Other particle families show steep mass hierarchies of this kind, which makes the assumption plausible without proving it. With it, the framework's total neutrino mass becomes a sharp number rather than a lower limit.

## one-liner
Premise: the second stage of the breaking leaves the lightest neutrino nearly massless, $m_{1}/m_{2} \lesssim 0.01$.
