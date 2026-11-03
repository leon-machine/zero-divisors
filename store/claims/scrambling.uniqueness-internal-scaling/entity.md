---
id: scrambling.uniqueness-internal-scaling
kind: claim
version: 3
title: Uniqueness of the internal scaling
status: proved
region: scrambling
subject: entropy
tags: [mode-counting, forcing-and-uniqueness, entropy-premises]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
review: typed
about:
- obj.scrambling.stretched-singularity
derivations:
- name: main
  uses:
  - scrambling.slice-volume-exactly-per-unit-killing@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - label:prop:unique
- kind: check
  ref: check.py::check_internal_cutoff_gives_linear_volume
- kind: check
  ref: check.py::check_alternatives_fail_and_p_one_is_unique
locators:
  paper: T08
  number: Prop 3.6
  label: prop:unique
  line: 656
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: exact monomial exponents for the three internal cutoffs (p = 1), the sphere-only (2/3) and fixed-radius (1/2) counts, and p = 1 as the only exponent with an admissible timescale. Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    removed:
    - scrambling.area-law-test
    note: 'Removed the area-law test: the proof says only that the exact coefficient is handled there,
      and the uniqueness claim is about exponents, which come from the slice-volume proposition alone.'
---

## formal
Call a timescale \emph{admissible} when the Schwarzschild geometry supplies it without tuning: the light-crossing, causal-epoch, and modular scales, $\Delta t \propto M$ up to logarithmic dressings, and the evaporation lifetime, $\Delta t \propto M^3$. Write the count as $N \propto M^p\,\Delta t$ with $p$ determined by the cutoff scheme. Then $p = 1$, produced by the framework's own curvature cutoff, is the \emph{unique} power for which an admissible timescale of order $M$ delivers the area law $N \propto M^2$: a sphere-only count (cells of the $r_c$-sphere, no $t$-stretch) gives $4\pi r_c^2 \propto M^{2/3}$, hence $p = 2/3$ and $N \sim M^{5/3}$; a fixed (mass-independent) cutoff radius gives volume per unit time $\propto \sqrt{M}$, hence $p = 1/2$ and $N \sim M^{3/2}$; and no admissible infrared choice repairs either: matching $M^{p + q} = M^2$ with $p \in \{2/3, 1/2\}$ requires $q \in \{4/3, 3/2\}$, and no admissible timescale has those exponents (a logarithmic dressing changes no exponent). The scaling test could have failed and did not.

## technical
Write the mode count as $N \propto M^p\,\Delta t$, with $p$ fixed by the cutoff scheme, and call a timescale admissible when the Schwarzschild geometry supplies it without tuning: the light-crossing, causal-epoch and modular scales, $\Delta t \propto M$ up to logarithmic dressings, and the evaporation lifetime, $\Delta t \propto M^3$. The framework's curvature cutoff gives $p = 1$, and with an admissible timescale of order $M$ this yields the area law $N \propto M^2$.

This power is unique among the schemes compared: a sphere-only count gives $p = 2/3$ and $N \sim M^{5/3}$, a fixed cutoff radius gives $p = 1/2$ and $N \sim M^{3/2}$, and repairing either would need a timescale exponent $q \in \{4/3, 3/2\}$, which no admissible timescale has, since a logarithmic dressing changes no exponent.

## lay
The number of quantum modes counted near a black hole's singularity grows with the mass in a way that depends on where the count is cut off. Only the framework's own cutoff, combined with a natural timescale of the order of the black hole's mass, gives a count that grows like the horizon area, as black-hole entropy should. The other cutoffs considered give the wrong growth, and no natural choice of timescale repairs them.

## one-liner
Among the schemes compared, only the framework's curvature cutoff, with an admissible timescale of order $M$, gives a mode count obeying the area law $N \propto M^2$.
