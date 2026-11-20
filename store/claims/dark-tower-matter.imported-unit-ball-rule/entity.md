---
id: dark-tower-matter.imported-unit-ball-rule
kind: claim
version: 5
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
- name: Claude Opus 5.5
  role: 'restated to the deposited text of T14c version 1.0 (10.5281/zenodo.24403592)'
  version: 5
  source: maintainer pass of 2026-11-20
review: typed
derivations:
- name: main
  uses:
  - dark-matter.unit-ball-rule@7
  assumes:
  - dark-matter.e-equal-mass-per-unit-ball@1
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
  line: 159
extraction:
  maintainer_pass:
    by: maintainer-2026-11-20
    date: '2026-11-20'
    note: 'The formal level restated: T14c deposited as version 1.0 on 20 November 2026 (10.5281/zenodo.24403592), after an independent review: T14''s rule stated on its premises E and R3, the particle model R1 and R2 implying E and not used by the rule (T14 version 2.1); edge to E added. Version 4 -> 5. The technical level restated: as the formal level. The lay level restated: as the formal level. The one-liner level restated: as the formal level.'
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
T14's unit-ball rule rests on two premises: E, one length $d$ common to every populated tower at which each holds the same mass per ball of radius $d$ of its own space, and R3, a three-dimensional tower's sheets stacked one $d$ apart and a five-dimensional tower's matter counted through one $d$ of its extra direction. Under E and R3 the shares are $1$, $2 \times 4/3$, $2 \times 8/(3\pi)$, with total $(11\pi + 16)/(3\pi)$ \cite[Prem.~7.2, Prem.~7.4, Prop.~7.6(i)]{ButlerT14}. T14's particle model, R1 (every quantum of every populated tower has the same mass) and R2 (one quantum per unit ball of each tower's own space, so a common Wigner-Seitz radius $d$), implies E and is not used by the rule \cite[Prem.~7.3, Prop.~7.6(ii)]{ButlerT14}; in it $d$ is this world's baryon spacing, $d_{b} \approx 0.98$ m, and the mass the nucleon's \cite[Rem.~7.9, Cor.~7.26]{ButlerT14}. E alone fixes neither. As fractions of the dark matter: mirror $18.6$ percent, each three-dimensional tower $24.9$, each five-dimensional tower $15.8$.

## technical
The dark-matter paper's unit-ball rule rests on two premises: E, one length $d$ common to every populated tower at which each holds the same mass per ball of radius $d$ of its own space, and R3, a three-dimensional tower's sheets stacked one $d$ apart and a five-dimensional tower's matter counted through one $d$ of its extra direction. Under E and R3 the shares relative to our baryons are $1$, $2 \times 4/3$ and $2 \times 8/(3\pi)$, with total $(11\pi + 16)/(3\pi)$. The particle model, R1 (every quantum has the same mass) and R2 (one quantum per unit ball of each tower's own space), implies E and is not used by the rule; in it $d$ is this world's baryon spacing, about a metre, and the mass the nucleon's. E alone fixes neither. As fractions of the dark matter: the mirror $18.6$ percent, each three-dimensional tower $24.9$ and each five-dimensional tower $15.8$.

## lay
The dark-matter paper divides the dark matter among the five dark towers by assuming that, at one common length, every populated tower holds the same mass in a ball of that size, with a rule for how thick the lower- and higher-dimensional towers count. The mirror then holds under a fifth, each three-dimensional tower about a quarter and each five-dimensional tower about a sixth. The older picture, in which every dark particle has the nucleon's mass, also gives this, but the rule does not need it.

## one-liner
Under E (equal mass per unit ball at one length) and R3 the mirror holds $18.6$ percent of the dark matter, each three-dimensional tower $24.9$ and each five-dimensional tower $15.8$, total share $(11\pi + 16)/(3\pi)$; the particle model R1 and R2 implies E and is not used.
