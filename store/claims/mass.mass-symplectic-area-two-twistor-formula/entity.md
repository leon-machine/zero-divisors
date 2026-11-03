---
id: mass.mass-symplectic-area-two-twistor-formula
kind: claim
version: 3
title: 'Mass as symplectic area: the two-spinor formula'
status: proved
region: mass
subject: mass
tags: [conformal-spinors, mass-generation]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T11.py
  tags:
  - label:prop:area
- kind: check
  ref: check.py::check_single_spinor_is_null
- kind: check
  ref: check.py::check_two_spinor_mass_is_symplectic_area
- kind: check
  ref: check.py::check_aligned_null_and_mass_grows_with_misalignment
locators:
  paper: T11
  number: Prop 4.1
  label: prop:area
  line: 512
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: null single-spinor momentum, p^2 = 2|<pi1 pi2>|^2 with the Cauchy-Binet identity behind it, aligned spinors null and mass growing with misalignment. Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'The paper says the result is classical (Hughston), but the store has no imported claim stating the two-twistor mass formula (the external chart import cites Hughston only for the bracket and null momentum), so no standard-route was added.'
  source_title: 'Mass as symplectic area: the two-twistor formula'
  source_formal: |-
    On the real slice, where $\varepsilon^{A'B'}$ is the complex conjugate of $\varepsilon^{AB}$ and $\bar\pi$ the conjugate of $\pi$: a single twistor carries null momentum $p_{AA'} = \pi_{A}\bar\pi_{A'}$ and is massless, and a two-twistor system with momentum
    \[
    p_{AA'} = \pi^{1}_{A}\bar\pi^{1}_{A'} + \pi^{2}_{A}\bar\pi^{2}_{A'}
    \]
    has
    \begin{equation}
    m^{2} = p^{2} = 2\,\bigl|\br{\pi^{1}\pi^{2}}\bigr|^{2},
    \end{equation}
    the squared symplectic area between the two spinor parts. Aligned spinors (vanishing bracket) give a null composite, and mass grows with the misalignment.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Statement and proof now speak of conformal spinors and read complex conjugation as the conjugation reversing I6; the two-spinor bracket computation in the components pi_A is kept as in the paper.'
---

## formal
On the real slice, where $\varepsilon^{A'B'}$ is the conjugate of $\varepsilon^{AB}$ and $\bar\pi$ the conjugate of $\pi$ (the conjugation reverses the complex unit $I_{6}$): a single conformal spinor (twistor) carries null momentum $p_{AA'} = \pi_{A}\bar\pi_{A'}$ and is massless, and a system of two conformal spinors with momentum
\[
p_{AA'} = \pi^{1}_{A}\bar\pi^{1}_{A'} + \pi^{2}_{A}\bar\pi^{2}_{A'}
\]
has
\begin{equation}
m^{2} = p^{2} = 2\,\bigl|\br{\pi^{1}\pi^{2}}\bigr|^{2},
\end{equation}
the squared symplectic area between the two spinor parts. Aligned spinors (vanishing bracket) give a null composite, and mass grows with the misalignment.

## technical
On the real slice a single conformal spinor carries null momentum $p_{AA'} = \pi_{A}\bar\pi_{A'}$ and is massless. For a system of two conformal spinors with total momentum $p_{AA'} = \pi^{1}_{A}\bar\pi^{1}_{A'} + \pi^{2}_{A}\bar\pi^{2}_{A'}$, the mass is $m^{2} = p^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$, twice the squared symplectic area between the two spinor parts.

Aligned spinor parts, with vanishing bracket, give a null composite, and the mass grows with their misalignment.

## lay
A single spinor of the conformal geometry describes a massless particle travelling at light speed. Two of them together can describe a massive particle, and its mass depends only on how far apart their two light-like directions point. When they line up the composite stays massless; the more they disagree, the heavier it is.

## one-liner
Two conformal spinors with momentum $\pi^{1}\bar\pi^{1} + \pi^{2}\bar\pi^{2}$ have $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$, the squared symplectic area of their spinor parts.
