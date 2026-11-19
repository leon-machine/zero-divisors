---
id: dark-tower-matter.imported-unit-ball-rule
kind: claim
version: 4
title: 'Imported: the unit-ball shares'
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [dark-matter-ratio, counting-rules]
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
  - dark-matter.unit-ball-rule@7
  assumes:
  - dark-matter.r1-equal-mass-per-quantum@1
  - dark-matter.r2-one-quantum-per-unit-ball@3
  - dark-matter.r3-one-cell-per-unshared-direction@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:K1
- kind: check
  ref: check.py::check_shares_and_total
- kind: check
  ref: check.py::check_fractions_of_the_dark_matter
locators:
  paper: T14c
  number: Fact 2.4
  label: fact:rule
  line: 210
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: shares 1, 4/3, 8/(3 pi) from unit-ball volumes in Q(pi), total (11 pi + 16)/(3 pi), and the fractions 18.6, 24.9 and 15.8 percent. Version 3 -> 4.'
  env: fact
  context_refs:
  - dark-matter.unit-ball-rule
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.r2-one-quantum-per-unit-ball
    note: 'Kept the unit-ball rule and premises R1, R3; added R2, which the statement names with the other
      two. Levels pass: levels written from scratch, keeping every condition and level qualifier of the
      formal statement.'
---

## formal
T14's premises R1 (every quantum of every populated tower has the same mass $m$, numerically the nucleon's), R2 (one quantum per unit ball of each tower's own space, with a common Wigner-Seitz radius $d_{b}$) and R3 (a three-dimensional tower's sheets stacked one cell radius apart; a five-dimensional tower's matter counted through one radius of its extra direction) give shares $1$, $2 \times 4/3$, $2 \times 8/(3\pi)$ and the total $(11\pi + 16)/(3\pi)$ \cite[Prem.~7.2 to 7.4, Prop.~7.6]{ButlerT14}. As fractions of the dark matter: mirror $18.6$ percent, each three-dimensional tower $24.9$, each five-dimensional tower $15.8$.

## technical
Under the dark-matter paper's premises R1 (every quantum of every populated tower has the same mass $m$, numerically the nucleon's), R2 (one quantum per unit ball of each tower's own space, with a common Wigner-Seitz radius $d_b$) and R3 (a three-dimensional tower's sheets stacked one cell radius apart, a five-dimensional tower's matter counted through one radius of its extra direction), the shares relative to our baryons are $1$, $2 \times 4/3$ and $2 \times 8/(3\pi)$, with total $(11\pi + 16)/(3\pi)$. As fractions of the dark matter: the mirror $18.6$ percent, each three-dimensional tower $24.9$ and each five-dimensional tower $15.8$.

## lay
Assuming every dark particle has the nucleon's mass and each tower holds one particle per unit-sized ball of its own space, the dark-matter paper predicts how the dark matter divides among the five dark towers. The mirror holds under a fifth, each three-dimensional tower about a quarter and each five-dimensional tower about a sixth.

## one-liner
Under R1 to R3 the mirror holds $18.6$ percent of the dark matter, each three-dimensional tower $24.9$ and each five-dimensional tower $15.8$, with total share $(11\pi + 16)/(3\pi)$.
