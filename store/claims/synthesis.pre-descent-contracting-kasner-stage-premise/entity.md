---
id: synthesis.pre-descent-contracting-kasner-stage-premise
kind: claim
version: 1
title: '(P1) of the Kasner exit: a contracting Kasner stage before the descent'
status: postulate
region: synthesis
subject: dark-energy
tags: [kasner, matter-asymmetry]
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
lineage:
  motivated_by:
  - synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching
  - synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point
  - synthesis.kasner-approach-gives-horizon-exit-and-index-three
  - synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling
  - standard-model.dating-descent
extraction:
  open_problem: op.descent-state-and-spectrum
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: >-
      New postulate, adopted by Leon's decision of 2026-11-01 to take both hypotheses of a pre-descent Kasner
      stage as premises, (P1) here and (P2) in synthesis.pre-descent-state-carried-into-descended-phase-premise.
      Its statement is the hypothesis (P1) as stated in the reading of
      synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching and in the formal of
      synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point. By the same decision
      those two results have no assumes edge to it: each states it as a hypothesis, and this premise names them
      in its text and lineage. Its tension with the pre-metric reading of the dating (a conjecture) is recorded,
      not resolved. Namesake: P1 of the dark sector is the single frozen point
      (dark-matter.p1-single-frozen-point), a different premise.
---

## formal
\emph{Premise (P1) of the Kasner exit, a contracting metric stage before the descent.} Before the descent there is a stage on which the gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) has an invertible region whose derived metric, near a wall at $\tau = 0$, is synchronous and diagonal, $d\tau^{2} - \sum_{j}\tau^{2p_{j}}(dx^{j})^{2}$ over the three observed directions and any hidden ones, with $\sum_{j}p_{j} = 1$ (the setting of Theorem \claimref{synthesis.kasner-approach-gives-horizon-exit-and-index-three}), and on which $\tau$ decreases toward the wall: the volume, proportional to $\tau$, contracts as the wall is approached. The fields whose exited spectra the stored Kasner results compute propagate on that region.

\emph{What it does not fix.} It fixes no Kasner exponents, no duration of the approach, no matter content and no state of the fields on the stage; in particular it does not say that the approach lasts until the observed modes have left the Hubble length, nor whether the approach reaches the wall or is ended before it by the descent. It says nothing about the descended phase; carrying the stage's state into the descended phase is the separate Premise \claimref{synthesis.pre-descent-state-carried-into-descended-phase-premise} (P2).

\emph{What it is for.} The one geometry in the store in which modes leave the Hubble length is a Kasner approach to a wall, and modes of every Bessel order leave it only while the approach contracts toward the wall (Theorem \claimref{synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching}(i)). With the descent at the origin and the descended phase expanding monotonically from it, such an approach can only precede the descent; so the stored Kasner spectra (Theorems \claimref{synthesis.kasner-approach-gives-horizon-exit-and-index-three}, \claimref{synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling}, \claimref{synthesis.kasner-hidden-scale-coupled-scalars-stay-blue}), read as a source of the primordial spectrum, need this stage. It is stated as hypothesis (P1) in the reading of Theorem \claimref{synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching} and in the formal of Theorem \claimref{synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point}; neither has an assumes edge to this premise.

\emph{What it does not give.} It does not supply the tilt. At tree level every curvature coupling the series fixes (twelve values, the largest $\tfrac12$) leaves the exited spectrum blue at the Kasner points the store fixes, with index at least $3 - \sqrt{3}$ for a scalar with no hidden-scale weight and at least $3 - \sqrt{7}$ with the stored weights (Theorem \claimref{synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point}); the curvature coupling that matches the measured tilt (Theorem \claimref{synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling}) stays a free parameter, not fixed by the series and not adopted. It does not supply the amplitude.

\emph{Tension, recorded and not resolved.} The dating reads pre-descent physics as pre-metric, the polynomial action and the $\theta$-remnants alone (\claimref{standard-model.dating-descent}, reading (iii), a conjecture at observation level); on that reading there is no derived metric before the descent, and this premise is denied. No proved result in the store denies it, as far as the store has been searched: gravity's polynomial action is defined across the singular locus (Theorem \claimref{dark-energy.gravity-pre-metric-forces-degenerate-exactly}(2)). The two cannot both hold; which one gives way is not decided here.

\emph{Refutation condition.} The premise is false if either of the following is established: (a) the pre-metric reading of the dating is proved, that is, before the descent the gravitational field has no invertible region (no nondegenerate soldering, so no derived metric); (b) any other proved result of the series excludes a metric stage contracting toward a Kasner wall before the descent. It is idle, not refuted, if the descent is not at the origin or the descended phase does not expand monotonically from it, since then an exit stage need not precede the descent.

## technical
The only geometry in the store in which field modes are stretched beyond the Hubble length is an approach to a Kasner wall, and the stretching happens only while space contracts toward the wall. Since the series places the descent at the origin and the universe expands from it, such a stage, if it supplies anything, must come before the descent. This premise takes that stage as given: before the descent the gravitational field has an invertible region with a synchronous diagonal Kasner metric, exponents summing to one, contracting toward its wall. It fixes no exponents, duration, matter or state, and it does not say how the stage's state reaches the descended phase, which is the companion premise (P2). Even granted, it does not supply the tilt: at tree level the curvature couplings the series fixes leave the spectrum blue at the Kasner points the store fixes, so the coupling that would match the measured tilt remains a free parameter. It stands against the dating's conjectured reading of pre-descent physics as pre-metric, which denies it; no proved result does, and the tension is recorded, not resolved. It would be refuted by a proof that there is no derived metric before the descent, or by any other proved exclusion of such a stage.

## lay
In this framework the universe begins with an event called the descent, and nothing in it stretches the earliest ripples to cosmic size after that event. The one known way the framework could stretch them is a stage in which space is squeezed toward a singularity, and that squeezing would have to happen before the descent. This assumption says such a stage existed. It is put in by hand: the framework's own account of the descent suggests that before it there was no ordinary geometry at all, and the two views clash. Even with this assumption the fields the framework fixes give ripples tilted the wrong way, so it does not explain the measured tilt.

## one-liner
Premise (P1): before the descent the gravitational field has an invertible region with a synchronous diagonal Kasner metric, $\sum_{j}p_{j} = 1$, contracting toward its wall (exponents, duration, matter and state not fixed); it is the stage on which modes can leave the Hubble length, stated as a hypothesis by the Kasner-exit and tree-level coupling results (no assumes edges); it does not supply the tilt, since at tree level every coupling the series fixes stays blue and the tilt-matching coupling stays free; it conflicts with the dating's conjectured pre-metric reading, unresolved; refuted by a proof that no derived metric exists before the descent.
