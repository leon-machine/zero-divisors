---
id: singularity.imported-page-average-entropy-subsystem
kind: claim
version: 1
title: 'Imported: the average entropy of a subsystem (Page)'
status: imported
region: singularity
subject: entropy
tags: [entanglement, classical-theorem]
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
imported_from:
- citation: D. N. Page, Average entropy of a subsystem, Phys. Rev. Lett. 71 (1993), 1291--1294.
  key: Page1993
- citation: S. K. Foong and S. Kanno, Proof of Page's conjecture on the average entropy of a subsystem, Phys. Rev. Lett. 72 (1994), 1148--1151.
  key: FoongKanno1994
- citation: J. Sanchez-Ruiz, Simple proof of Page's conjecture on the average entropy of a subsystem, Phys. Rev. E 52 (1995), 5653--5655.
  key: SanchezRuiz1995
- citation: S. Sen, Average entropy of a quantum subsystem, Phys. Rev. Lett. 77 (1996), 1--3.
  key: Sen1996
locators:
  paper: T05
  number: Fact 11.1
  label: thm:pagecurve
  line: 2225
extraction:
  env: fact
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 8
    note: Created so that the assembled Page curve (T05 Fact 11.1) can be a proved assembly whose one outside ingredient is this import; T05 cites Page's theorem inside that Fact and in its introduction ("Page's curve and typicality theorem").
---

## formal
Let $\mathcal{H} = \mathcal{H}_A \otimes \mathcal{H}_B$ with $\dim\mathcal{H}_A = m \leq n = \dim\mathcal{H}_B$, and let $\psi$ be a pure state drawn from the unitarily invariant measure on the unit sphere of $\mathcal{H}$. The average entanglement entropy of the subsystem $A$ is
\[
\langle S_A \rangle \;=\; \sum_{k=n+1}^{mn} \frac{1}{k} \;-\; \frac{m-1}{2n} \;\simeq\; \ln m - \frac{m}{2n} \qquad (1 \ll m \leq n),
\]
so a typical pure state's smaller marginal is within $m/2n \leq 1/2$ nat of the maximum $\ln m$. Page conjectured the formula \cite{Page1993}; it was proved by Foong and Kanno, by Sanchez-Ruiz, and by Sen.

## technical
For a pure state of a bipartite system of dimensions $m \leq n$, chosen at random with respect to the unitarily invariant measure, the average entropy of the smaller subsystem is $\sum_{k=n+1}^{mn} 1/k - (m-1)/2n$, which for large $m$ is $\ln m - m/2n$. A typical state therefore nearly saturates the bound $\ln m$ on the smaller side's entropy, missing it by at most half a nat. The series uses it for saturation in the assembled Page curve.

## lay
If a large quantum system in a pure state is split into two parts, and the state is picked at random, the smaller part is almost always as mixed as it can possibly be: its entropy falls short of the maximum by at most half a unit. Don Page worked out the average in 1993, and others proved his formula soon after. The series uses this to say that the entropy of a black hole's radiation reaches the largest value its counting allows.

## one-liner
A random pure state of a bipartite system leaves the smaller part within half a nat of maximal entropy: $\langle S_A\rangle \simeq \ln m - m/2n$ (Page).
