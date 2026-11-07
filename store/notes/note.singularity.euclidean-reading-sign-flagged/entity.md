---
id: note.singularity.euclidean-reading-sign-flagged
kind: note
version: 4
title: The Euclidean reading of the sign, flagged
status: remark
subject: descent
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle (ruling on the Euclidean rotor)
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
comments_on:
- singularity.two-kms-functionals-sign
- singularity.euclidean-rotor-where-it-lies
locators:
  paper: T05
  number: Rem 7.24
  label: rem:spinstructure
  line: 1928
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. At the coordinator''s ruling (as for singularity.euclidean-rotor-where-it-lies (3)): the Euclidean rotation of the (rho, tau) plane acts on spacetime vectors, so by U3 its unit is I_5 = I_4 e of Cl(2,3) (std-algebra.complexification-is-the-odd-extension, cited as a mention): the rotor is R_{I_5 theta} = cos(theta/2) + I_5 sigma sin(theta/2), and the sign remark R_{2 pi I_5} = -1 holds; the text says it is not R_{J theta}, which equals e^{I_4 theta/2} in Cl(1,3). This replaces the R_{J theta} reading of the first resolve edit. Declaration stays removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): R_{i theta} is the boost rotor continued to imaginary rapidity, the Euclidean rotation of the (rho, tau) plane, which singularity.euclidean-rotor-where-it-lies (3) shows is realised by no real rotor of Cl(1,3); the dual-plane rotor I_4 B would be a different rotation.'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$R_{i\theta}$, $R_{2\pi i}$: rotor at imaginary rapidity, imaginary time (analytic continuation)'
---

## formal
Under continuation to imaginary time the ungraded identity is the antiperiodic boundary condition for the mode's Euclidean two-point function on a circle of circumference $\beta$, and the graded identity the periodic one: this is the Matsubara dichotomy, and it is quoted, not proved. On the smooth Euclidean section a spinor field expressed in the Killing frame, which is the polar frame of the $(\varrho, \tau)$ plane, is multiplied by the boost rotor of Proposition \claimref{singularity.euclidean-rotor-where-it-lies} continued to imaginary rapidity, the Euclidean rotation of the $(\varrho, \tau)$ plane $R_{I_{5}\theta} = \cos(\theta/2) + I_{5}\sigma\sin(\theta/2)$, with $I_{5} = I_{4}e$ the central pseudoscalar of the odd extension $\Cl(2,3)$, the unit of the continuation acting on spacetime vectors (\claimref{std-algebra.complexification-is-the-odd-extension}; not $R_{J\theta}$, which equals $e^{I_{4}\theta/2}$ in $\Cl(1,3)$), relative to a frame regular at the origin, and so reverses sign under one full turn: single-valuedness on the section, in the frame in which the modes are defined, is the antiperiodic condition, and hence the ungraded identity of (R). This is the standard spin-structure argument for the thermal, rather than parity-twisted, character of the Hartle-Hawking and Unruh states of fermions, and it is where $R_{2\pi I_{5}} = -1$ enters. The chain records it as the reason (R) is stated with the ungraded gluing; it does not derive (R) from it, and the dependence of the boundary condition on the choice of frame is exactly why the statement has to be made in the Killing frame.

## technical
pending

## lay
pending

## one-liner
pending
