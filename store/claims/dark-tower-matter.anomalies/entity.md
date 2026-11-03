---
id: dark-tower-matter.anomalies
kind: claim
version: 3
title: Chern-Simons levels of the odd towers' content
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [hypercharge-and-anomalies, chirality]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - dark-tower-matter.five-dimensional-content@5
  - dark-tower-matter.three-dimensional-content@4
  - rule2.imported-parity-anomaly@1
  - rule2.imported-five-dimensional-chern-simons-shift@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:G1
  - id:G2
  - id:G3
- kind: check
  ref: check.py::check_three_dimensional_parity_anomaly
- kind: check
  ref: check.py::check_five_dimensional_chern_simons_integrality
locators:
  paper: T14c
  number: Prop 6.5
  label: prop:anomaly
  line: 636
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: one unit-charge fermion per U(1) and half-integral bare levels; sum q''^3 = -6, sum q'' = 0 and integral 5D Chern-Simons coefficient for all 16 sign choices. Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - dark-tower-matter.three-dimensional-content
    - rule2.imported-five-dimensional-chern-simons-shift
    - rule2.imported-parity-anomaly
    note: 'Added the three-dimensional content (one unit-charge fermion per factor, clause (i)) and the
      two imported Chern-Simons facts the statement cites (Redlich for (i), Intriligator, Morrison and
      Seiberg for (ii)), which are already in the store from the rule-two note. Levels pass: levels written
      from scratch, keeping every condition and level qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-tower-matter.three-dimensional-content
    - rule2.imported-five-dimensional-chern-simons-shift
    - rule2.imported-parity-anomaly
---

## formal
\begin{enumerate}
\item[(i)] In the three-dimensional towers each $U(1)_{\pm}$ couples to exactly one unit-charge two-component fermion, which shifts its Chern-Simons level by $\tfrac{1}{2}\mathrm{sign}(m)$ \cite{Redlich1984}; integrality of the effective level forces the bare levels into $\mathbb{Z} + \tfrac{1}{2}$. Parity is therefore broken by the gauge sector.
\item[(ii)] In the five-dimensional towers, in units $q' = 3Y$, the content of Proposition \claimref{dark-tower-matter.five-dimensional-content} has $\sum q'^{3} = -6$ and $\sum q' = 0$ (with multiplicities), and the induced abelian cubic Chern-Simons coefficient, $\tfrac{1}{2}\sum \mathrm{sign}(m)\,q'^{3}$, is integral for every choice of mass signs \cite{IMS1997}. The $SU(3)$ and mixed levels, which on $U(3)$ are tied to the abelian one, are not analysed here.
\end{enumerate}

## technical
In the three-dimensional towers each abelian factor $U(1)_\pm$ couples to exactly one unit-charge two-component fermion, which shifts its Chern-Simons level by $\tfrac12\,\mathrm{sign}(m)$ (the parity anomaly). Integrality of the effective level then forces the bare levels into $\mathbb{Z} + \tfrac12$, never zero, so the gauge sector breaks parity.

In the five-dimensional towers, in units $q' = 3Y$, the species $U, D, E, N$ (the content found under Hypothesis (S)) have $\sum q'^3 = -6$ and $\sum q' = 0$ with multiplicities, and the induced abelian cubic Chern-Simons coefficient $\tfrac12\sum \mathrm{sign}(m)\,q'^3$ is an integer for every choice of mass signs. The $SU(3)$ and mixed levels are not analysed.

## lay
Each charged particle in a three-dimensional tower shifts a topological term in its force by half a unit, and consistency then requires that term never to vanish, so these towers' forces distinguish left from right. In the five-dimensional towers the corresponding abelian term is a whole number for any choice of mass signs, for the particle content found there under the slot hypothesis. The non-abelian terms are not examined.

## one-liner
The three-dimensional towers' bare Chern-Simons levels are forced into $\mathbb{Z} + \tfrac12$, breaking parity, while in the five-dimensional towers the abelian cubic level of the content under (S) is integral for every choice of mass signs.
