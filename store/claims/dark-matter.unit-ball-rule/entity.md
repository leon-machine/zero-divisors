---
id: dark-matter.unit-ball-rule
kind: claim
version: 5
title: The unit-ball rule
status: proved
region: dark-matter
subject: dark-matter
tags:
- dark-matter-ratio
- counting-rules
- confronted-with-data
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-matter.towers-are-residues-single-clock-filter@5
  assumes:
  - dark-matter.r1-equal-mass-per-quantum@1
  - dark-matter.r2-one-quantum-per-unit-ball@2
  - dark-matter.r3-one-cell-per-unshared-direction@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_shares
- kind: check
  ref: check.py::check_dark_towers_and_dimensions
- kind: check
  ref: check.py::check_total
locators:
  paper: T14
  number: Prop 7.6
  label: prop:rule
  line: 821
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the shares V_3/V_D under R1 to R3, the five dark towers'' dimensions, and the total (11 pi + 16)/(3 pi) against the record. Version 4 -> 5.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.r1-equal-mass-per-quantum
    - dark-matter.r2-one-quantum-per-unit-ball
    - dark-matter.r3-one-cell-per-unshared-direction
    - dark-matter.towers-are-residues-single-clock-filter
    note: 'R1 to R3 added as assumes since the statement is under them; the residue census added as the
      source of the representatives'' dimensions in the sum, a judgement call since the paper does not
      cite it in the proof. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.towers-are-residues-single-clock-filter
  small_findings_pass:
    by: ai-small-findings-pass
    date: '2026-10-22'
    finding: CONTRADICTIONS_VALUES M11
    note: 'Every level now says the agreement with 5.364 is a fit, as dark-matter.status-rule records
      (found by solving for the observed value; one of fourteen equally simple candidates). The arithmetic
      is unchanged: V3/V2 = 4/3, V3/V4 = 8/(3 pi), 1 + 8/3 + 16/(3 pi) = (11 pi + 16)/(3 pi). Suggested
      maintainer edge: dark-matter.status-rule comments_on this rule.'
    open_problem: op.small-findings
  open_problem: op.small-findings
---

## formal
Under R1 to R3, the share of a tower whose space has $D$ dimensions is $f = \tfrac{V_{3}}{V_{D}}$, and
\[
\frac{\Omega_{\mathrm{dark}}}{\Omega_{b}} \;=\; V_{3}\sum_{\text{dark }r}\frac{1}{V_{D_{r}}}
\;=\; \frac{V_{3}}{V_{3}} + 2\,\frac{V_{3}}{V_{2}} + 2\,\frac{V_{3}}{V_{4}}
\;=\; 1 + \frac{8}{3} + \frac{16}{3\pi} \;=\; \frac{11\pi + 16}{3\pi} \;=\; 5.36432\ldots
\]
against the observed $5.364 \pm 0.065$. The agreement is built in, not predicted: the relation was found by solving for the observed value, and its clauses were chosen with it known, and the closed form is one of fourteen equally simple candidates within the error bar (Observation \claimref{dark-matter.status-rule}).

## technical
Under premises R1 (equal mass per quantum), R2 (one quantum per unit ball of a tower's own space) and R3 (one cell per unshared direction), a tower whose space has $D$ dimensions has number density $1/V_{D}$ and so contributes a share $f = V_{3}/V_{D}$ of our matter per unit of our volume, with $V_{n}$ the volume of the unit $n$-ball. Summing over the five dark towers at their nearest-dimension representatives, the mirror with $D = 3$, two three-dimensional towers with $D = 2$ and two five-dimensional towers with $D = 4$, gives
$$\frac{\Omega_{\mathrm{dark}}}{\Omega_{b}} = 1 + \frac{8}{3} + \frac{16}{3\pi} = \frac{11\pi + 16}{3\pi} = 5.36432\ldots,$$
against the observed $5.364 \pm 0.065$. The agreement is a fit, not a prediction: the relation was found by solving for the observed value, its clauses chosen with it known, and it is one of fourteen equally simple values in the error bar (Observation \claimref{dark-matter.status-rule}).

## lay
This rule assigns every dark tower one particle of a common mass per unit-sized ball of its own space, and compares that density with ours. Towers with fewer or more spatial dimensions then contribute different amounts, fixed by the volumes of balls in two, three and four dimensions. Under its three premises the rule gives a dark-to-ordinary matter ratio of about 5.364, the observed value; but the relation was found by solving for that value, and many equally simple formulas land inside the measurement's error, so the agreement is a fit rather than a prediction.

## one-liner
Under premises R1 to R3 a tower with $D$-dimensional space has share $V_{3}/V_{D}$, and the dark-to-baryon ratio is $(11\pi + 16)/(3\pi) \approx 5.3643$, against the observed $5.364 \pm 0.065$, an agreement built in by fitting, not predicted.
