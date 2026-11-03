---
id: singularity.c2-cell-density
kind: claim
version: 4
title: 'C2: cell density'
status: postulate
region: singularity
subject: entropy
tags:
- entropy-premises
- mode-counting
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
locators:
  paper: T05
  number: Axiom 10.2
  label: ax:cell
  line: 2137
extraction:
  env: axiom
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Version 4 adds a scope sentence, at Leon's decision of 23 October (cutoff premises as a Schwarzschild calibration only), that (C2) with (C1) and (IC) is read as a calibration on the Schwarzschild family, since read literally the count fails the area law on Schwarzschild-de Sitter (u/(3u-2) times A_b/4 over the hole's modular period, synthesis.cutoff-count-is-not-a-local-density-on-sds) and on Kerr (synthesis.kerr-ring-count-misses-area-law); away from Schwarzschild the horizon placement with a flat-data density is the count. The premise itself is unchanged on the Schwarzschild family.
  maintainer_pass_2026_10_22:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: Version 3 adds a note, at Leon's decision to keep (C1) and (C2) rather than replace them by (C2'), that their forms are forced by an algebraic curvature criterion plus isometry invariance leaving one constant (synthesis.c1-c2-forms-forced-one-number) and that (C2') on the exceptional set is equivalent at leading order (synthesis.exceptional-boundary-measure-one-calibration); the premise itself is unchanged.
  context_refs:
  - sheaf.schwarzschild-degeneration-boundary-tame
  unresolved_refs:
  - rem:weights
  typing:
    by: ai-typing-pass
    note: Postulate; no edges.
  source_formal: 'The boundary mode space carries $\nu$ fermionic modes per Planck cell of the stretched singularity,
    with $\nu$ an order-one constant (its corank factor is fixed at one: the forced weighted completion gives exactly
    one ladder pair per point of the blown-up singular boundary, Remark \ref{rem:weights} and \cite[Thm.~8.7, \S
    8.9]{ButlerT4}; what remains in $\nu$ is the Planck-cell calibration).'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: correction-2026-10-22
    note: 'Corrected ''nu an order-one constant'': the entropy paper''s area-law condition with the counted epoch
      at the modular period requires nu = 1/(16 pi ln 2), about 0.029, in the capacity convention (1/16 pi, about
      0.020, in the 1-nat convention), the registered prediction pred.boundary-mode-density. The premise itself
      still leaves nu free.'
---

## formal
The boundary mode space carries $\nu$ fermionic modes per Planck cell of the stretched singularity, with $\nu$ a constant that this premise leaves free (the entropy paper's area-law condition with the counted epoch at the modular period requires $\nu = 1/(16\pi\ln 2) \approx 0.029$ in the capacity convention, $1/16\pi \approx 0.020$ in the 1-nat convention, Prediction \claimref{pred.boundary-mode-density}, so not of order one; its corank factor is fixed at one: the forced weighted completion gives exactly one ladder pair per point of the blown-up singular boundary, Remark \ref{rem:weights} and \cite[Thm.~8.7, \S 8.9]{ButlerT4}; what remains in $\nu$ is the Planck-cell calibration).

\emph{Note (form and calibration).} The form of this premise is forced, not chosen: a density invariant under the isometries of the slice, which act transitively, is a constant multiple $\nu$ of the induced volume, and with the slice family $r_c^{3} = 2M/\lambda$ that an algebraic, mass-independent curvature criterion forces for Premise \claimref{singularity.c1-curvature-cutoff}, the leading count sees $\nu$ and the threshold $\lambda$ only through the one number $\kappa_{s} = \nu\lambda^{-1/2}$ (Theorem \claimref{synthesis.c1-c2-forms-forced-one-number}); the registered density is a value of $\kappa_{s}$, equal to $\nu$ at $\lambda = 1$. At leading order this premise together with (C1) is equivalent to (C2$'$), the modes carried by the exceptional set itself with $\nu' = \tfrac23\kappa_{s}$ modes per Planck area of its Kasner measure $\mu_{E} = 12\pi M$ per unit Killing time; the two differ only at relative order $(2M)^{-2/3}$ (Theorem \claimref{synthesis.exceptional-boundary-measure-one-calibration}). The premise is kept as stated.

\emph{Scope (Schwarzschild calibration).} This premise, with Premise \claimref{singularity.c1-curvature-cutoff} and the intrinsic-clock premise (IC) (Premise \claimref{scrambling.intrinsic-clock-ic-flagged-premise}), is read as a calibration of the count on the Schwarzschild family only: the density it calibrates there does not carry over to other holes through the cutoff placement. Read literally on a Schwarzschild-de Sitter hole, with the counted epoch read as the hole's modular period and the density fixed at $\Lambda = 0$, the count is $u/(3u - 2)$ times $A_{b}/4$, $u = 2M/r_{b}$, for every $\Lambda > 0$, and no horizon's period gives $A_{b}/4$ (Theorem \claimref{synthesis.cutoff-count-is-not-a-local-density-on-sds}); for a spinning hole with $a \ge 2(2M)^{2/3}$ the literal count misses the area law by a factor of order $M^{-1/3}$ (Theorem \claimref{synthesis.kerr-ring-count-misses-area-law}). Away from the Schwarzschild family the count is read through the horizon placement, the modes on the horizon with a density fixed by flat tangent data, as clause (Loc) of Premise \claimref{synthesis.c-loc-local-horizon-premise} states.

## technical
Postulate: the boundary mode space carries $\nu$ fermionic modes per Planck cell of the stretched singularity, with $\nu$ a constant the premise leaves free. The entropy paper's area-law condition, with the counted epoch at the modular period, requires $\nu = 1/(16\pi\ln 2) \approx 0.029$ in the capacity convention, about $0.020$ in the 1-nat convention, which is the registered boundary-mode prediction.

The corank factor in $\nu$ is fixed at one, since the forced weighted completion gives exactly one ladder pair per point of the blown-up singular boundary; what remains in $\nu$ is the Planck-cell calibration.

Its form is forced: a density invariant under the isometries of the slice is uniform, and with the slice family any algebraic, mass-independent curvature criterion selects, the leading count depends on (C1) and (C2) only through one number, $\nu\lambda^{-1/2}$. At leading order the pair is equivalent to counting the modes on the exceptional set itself with its Kasner measure, with a single calibration constant, the premise (C2$'$). The series keeps (C1) and (C2) as they are.

The premise is read as a calibration on the Schwarzschild family only. With the density fixed there, the literal count on a Schwarzschild-de Sitter hole, over the hole's own modular period, exceeds a quarter of the horizon area by the factor $u/(3u - 2)$, $u = 2M/r_{b}$, and on fast-spinning holes it misses the area law by a factor of order $M^{-1/3}$. Elsewhere the count is the placement of the modes on the horizon with a density fixed by flat data.

## lay
This assumption fixes how densely the quantum modes are packed on the surface near the singularity: a fixed number of modes per Planck-sized cell, which the area law, as the series later computes, needs to be about one for every thirty-five cells. Part of that number is settled by the framework, one ladder pair per point, but how points convert into Planck cells is left as a calibration. That calibration is made on non-rotating black holes in otherwise empty space; on spinning black holes, or with a positive cosmological constant, the same rule read literally gives the wrong entropy.

## one-liner
Postulate: the stretched singularity carries $\nu$ fermionic modes per Planck cell, with $\nu$ a constant whose remaining freedom is the cell calibration; the area law needs $\nu = 1/(16\pi\ln 2) \approx 0.029$; read as a Schwarzschild calibration only.
