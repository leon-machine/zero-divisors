---
id: scrambling.mode-count
kind: claim
version: 3
title: The mode count
status: proved
region: scrambling
subject: entropy
tags: [mode-counting, boundary-modes]
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
- name: Claude Fable 5.2
  role: 'scope note: the wording "accrual rate nu/T_H" is a Schwarzschild coincidence; on Kerr the three forms of the rate differ'
  version: 3
  source: maintainer pass of 2026-11-10
review: draft
derivations:
- name: main
  uses:
  - scrambling.slice-volume-exactly-per-unit-killing@5
  - singularity.stretched-singularity-count@9
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_mode_count_placement
- kind: legacy
  script: verify_T08.py
  tags:
  - label:thm:count
locators:
  paper: T08
  number: Thm 3.4
  label: thm:count
  line: 634
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 2 -> 3. Scope note added at Leon''s decision of 10 November 2026; the statement on Schwarzschild is unchanged. The wording ''the accrual rate is set by the Hawking temperature'', rate nu/T_H, is a Schwarzschild coincidence: on Kerr the three forms of the rate that agree on Schwarzschild give counts M/s, M r_+/(2 s^2) and 1 times A_+/4 (clause (v) of synthesis.stretched-horizon-count-on-kerr-is-a-multiple-of-the-area-by-construction).'
  open_problem: op.boundary-mode-provenance
  correction:
    by: colony-2026-10-22
    version: 2
    note: >-
      The count places nu modes on each Planck cell of the slice r = r_c, which is (C1) (support on
      the stretched singularity) and (C2) (nu modes per Planck cell) verbatim, yet version 1 cited
      the Witt-index capacity Fact for it. That Fact counts mode pairs per rung of the tower and says
      nothing about cells or slices, so it supplied neither premise and left (C1), (C2) out of the
      past cone of everything built on the count (the area-law test, the integer-holographic form,
      the spreading law, the epoch and return-delay results). Version 2 takes the placement from
      T05's count (Proposition 10.6), of which this is the leading order and which holds under (C1)
      and (C2), so both premises become visible without a new assumes edge, and the modes' provenance
      is the one (C2) states (one ladder pair per point of the blown-up boundary, T04), not rungs.
      The store provenance here departs from the paper's own citation: T08 Thm 3.4 (the locator)
      cites the capacity Fact; the store follows the premises the count actually needs.
  env: theorem
  unresolved_refs:
  - rem:nu
  typing:
    by: ai-typing-pass
    note: 'Both uses (the slice volume and the capacity Fact supplying modes per cell) are premises and
      are kept; the stretched-singularity definition is recorded under about. Levels pass: the lay level
      and one-liner now keep the leading-order qualifier in $r_c/2M$. Superseded in version 2: the
      capacity Fact is replaced by the T05 count that carries (C1) and (C2).'
about:
- obj.scrambling.stretched-singularity
---

## formal
Assume (C1) and (C2) (Postulates \claimref{singularity.c1-curvature-cutoff} and \claimref{singularity.c2-cell-density}, through Proposition \claimref{singularity.stretched-singularity-count}): the boundary modes lie on the stretched singularity, $\nu$ fermionic modes per Planck cell (the calibration factor, Remark \ref{rem:nu}), and let $\Delta t$ be the counted span of Killing time. Then, to leading order in $r_c/2M$ (Proposition \claimref{scrambling.slice-volume-exactly-per-unit-killing}),
\[
N \;=\; 8\pi\,\nu\,M\,\Delta t\,/\,\lP^2,
\qquad\text{equivalently}\qquad
\frac{dN}{dt} \;=\; 8\pi\nu M \;=\; \frac{\nu}{\TH}:
\]
the accrual rate is set by the Hawking temperature. The count $N = 8\pi\nu M\,\Delta t$ needs only (C1) and (C2); the form $\nu/\TH$ reads $8\pi M$ as $1/\TH$, the temperature that modular descent fixes under (R) (Premise \claimref{singularity.r-regularity-fixed-locus}, through Proposition \claimref{singularity.stretched-singularity-count}). The coefficient depends on $\nu$, whose corank factor (C2) fixes at one, so what remains in it is the Planck-cell calibration and the bit or nat convention ($1/(16\pi\ln 2)$ against $1/16\pi$ at the area law); the proportionality $dN/dt \propto 1/\TH$ does not depend on $\nu$.

\emph{Scope (Schwarzschild).} The equality of the forms $8\pi\nu M$ and $\nu/\TH$ of the rate, and with it the wording that the accrual rate is set by the Hawking temperature, is a Schwarzschild coincidence. Carried to the Kerr field with the epoch $2\pi/\kappa_{+}$ and $\nu = 1/16\pi$, the three forms of the rate that agree on Schwarzschild, $8\pi\nu M$, $\nu/\TH$ and $2\nu\kappa A$, give counts $M/s$, $Mr_{+}/(2s^{2})$ and $1$ times $A_{+}/4$, $s = \sqrt{M^{2} - a^{2}}$, and the third agrees only because it is the rate of that result's horizon hypothesis itself (Theorem \claimref{synthesis.stretched-horizon-count-on-kerr-is-a-multiple-of-the-area-by-construction}, clause (v)). So on Kerr the three forms differ, and the Schwarzschild count does not fix which of them is carried.

## technical
Assume, as the singularity paper's postulates (C1) and (C2) state, that the boundary modes sit on the stretched singularity with $\nu$ fermionic modes per Planck cell, and let $\Delta t$ be the counted span of Killing time. Since the slice volume is $8\pi M$ per unit Killing time at leading order in $r_c/2M$, the count is $N = 8\pi\nu M\,\Delta t/\lP^2$.

Equivalently $dN/dt = 8\pi\nu M = \nu/\TH$, so the accrual rate is set by the Hawking temperature $\TH = 1/8\pi M$, the temperature fixed by the regularity premise (R). The coefficient depends on $\nu$, which still carries the Planck-cell calibration and the bit or nat convention; the proportionality $dN/dt \propto 1/\TH$ does not.

That the rate can be written $\nu/\TH$ is a Schwarzschild coincidence: on a spinning hole the mass form $8\pi\nu M$, the temperature form $\nu/\TH$ and the area form $2\nu\kappa A$ of the rate differ, giving counts $M/s$, $Mr_{+}/(2s^{2})$ and $1$ times a quarter of the horizon area, $s = \sqrt{M^{2} - a^{2}}$.

## lay
Granting the singularity paper's two placement assumptions (the modes sit on the black hole's inner surface, a fixed number per smallest cell), modes accumulate there as time runs on. To leading order in the ratio of that surface's radius to the hole's size, the number gathered per unit time is proportional to the mass, or equivalently inversely proportional to the hole's Hawking temperature. The overall factor depends on how densely modes are packed, which is left open here.

## one-liner
To leading order in $r_c/2M$, the boundary-mode count over a Killing-time span $\Delta t$ is $N = 8\pi\nu M\,\Delta t/\lP^2$, accruing at the rate $\nu/\TH$.
