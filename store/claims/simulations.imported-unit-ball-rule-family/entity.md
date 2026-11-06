---
id: simulations.imported-unit-ball-rule-family
kind: claim
version: 4
title: 'Imported: the unit-ball rule and its family'
status: proved
region: simulations
subject: dark-matter
tags: [dark-matter-ratio, counting-rules, needs-continuum]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14b, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-matter.reduced-response-gravity-needs-supporting-stress@3
  - dark-matter.total-function-thickness@5
  - dark-matter.unit-ball-rule@5
  assumes:
  - dark-matter.r1-equal-mass-per-quantum@1
  - dark-matter.r2-one-quantum-per-unit-ball@2
  - dark-matter.r3-one-cell-per-unshared-direction@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_unit_ball_shares_and_total
- kind: check
  ref: check.py::check_thickness_family
- kind: check
  ref: check.py::check_floor_of_the_family
locators:
  paper: T14b
  number: Fact 2.2
  label: fact:rule
  line: 88
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: unit-ball shares and the total (11 pi + 16)/(3 pi) in Q(pi), the thickness family T(c) with its symmetry and floor, and the numerical figures from rational bounds on pi. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.r2-one-quantum-per-unit-ball
    note: 'The statement is made under R1, R2 and R3 and cites Premises 7.2 to 7.4, so R2 was added to
      assumes alongside the existing R1 and R3; the three proposition uses match the provenance. Levels
      pass: lay now names R1 to R3, and no longer says varying the thickness moves the total only slightly
      (the family is unbounded above; only its floor of 5.255 is stated).'
  env: fact
  context_refs:
  - dark-matter.reduced-response-gravity-needs-supporting-stress
  - dark-matter.total-function-thickness
  - dark-matter.unit-ball-rule
  flags:
  - 'fact restating several series results: derived from them'
---

## formal
Under Premises R1 (equal mass per quantum), R2 (one quantum per unit ball of each tower's space, with a common Wigner-Seitz radius $d_{b}$) and R3 (one cell radius per unshared direction), the share of a tower whose space has $D$ dimensions is $V_{3}/V_{D}$, and
\[
\frac{\Omega_{\mathrm{dark}}}{\Omega_{b}} \;=\; 1 + 2\cdot\frac{4}{3} + 2\cdot\frac{8}{3\pi} \;=\; \frac{11\pi + 16}{3\pi} \;=\; 5.364 .
\]
With the thickness of the unshared direction left as $c\,d_{b}$ the total is
\[
T(c) \;=\; 1 + \frac{8}{3c} + \frac{16c}{3\pi},
\]
which equals $5.364$ at $c = 1$ and $c = \pi/2$ and has its floor $5.255$ at $c = \sqrt{\pi/2}$. The three-dimensional towers' sheets are stacked one cell radius apart along the direction they lack, and they move with the matter. \emph{Provenance:} \cite[Prems.~7.2 to 7.4, Props.~7.6, 7.15 and 7.28]{ButlerT14}.

## technical
Under premises R1 (equal mass per quantum), R2 (one quantum per unit ball of each tower's space, with a common Wigner-Seitz radius $d_{b}$) and R3 (one cell radius per unshared direction), a tower whose space has $D$ dimensions has share $V_{3}/V_{D}$, and summing over the populated towers gives $\Omega_{\mathrm{dark}}/\Omega_{b} = 1 + 2\cdot\tfrac{4}{3} + 2\cdot\tfrac{8}{3\pi} = (11\pi + 16)/(3\pi) = 5.364$.

Leaving the thickness of the unshared direction as $c\,d_{b}$, the total is $T(c) = 1 + 8/(3c) + 16c/(3\pi)$, equal to $5.364$ at $c = 1$ and $c = \pi/2$, with its floor $5.255$ at $c = \sqrt{\pi/2}$. The three-dimensional towers' sheets are stacked one cell radius apart along the direction they lack, and move with the matter.

## lay
Assuming three premises, that every particle has the same mass (R1), that one particle fills one unit ball of its sector's space (R2) and that each direction a sector lacks counts one cell radius (R3), a counting rule gives each hidden sector a share of matter according to how much room one particle takes up in that sector's space. Added up over the sectors, it gives about $5.36$ times as much dark matter as ordinary matter. If the thickness of the missing direction is left free instead, the totals form a family whose smallest value is about $5.26$, with $5.36$ reached at two different thicknesses.

## one-liner
Under premises R1 to R3 the unit-ball rule gives $\Omega_{\mathrm{dark}}/\Omega_{b} = (11\pi + 16)/(3\pi) = 5.364$, and its thickness family $T(c)$ has floor $5.255$ at $c = \sqrt{\pi/2}$.
