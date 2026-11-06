---
id: synthesis.pre-descent-state-carried-into-descended-phase-premise
kind: claim
version: 1
title: '(P2) of the Kasner exit: a rule carrying the pre-descent state across'
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
  - dark-energy.frozen-point-datum-kasner-wall
  - standard-model.dating-descent
extraction:
  open_problem: op.descent-state-and-spectrum
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: >-
      New postulate, adopted by Leon's decision of 2026-11-01 to take both hypotheses of a pre-descent Kasner
      stage as premises, (P1) in synthesis.pre-descent-contracting-kasner-stage-premise and (P2) here. The
      statement is the general form of (P2) in the reading of
      synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching (a rule into the descended
      phase, across the wall if the approach reaches it, or across whatever ends the approach before it); the
      decision's shorter wording, a matching across the singular wall into the descent, is its first case. By
      the same decision the two results have no assumes edge to it; this premise names them in its text
      and lineage. Its tension with the pre-metric reading of the dating (a conjecture) is recorded, not
      resolved. Cited from memory, not checked against the source: the compactified Milne geometry of the
      ekpyrotic and cyclic models and the open status of its matching (Khoury, Ovrut, Steinhardt and Turok
      2001; Tolley, Turok and Steinhardt 2004), as already flagged in the Kasner-exit result. Namesake: P2 of
      the dark sector (dark-matter.p2-indifference) is a different premise.
---

## formal
\emph{Premise (P2) of the Kasner exit, the state carried into the descended phase.} Assume Premise \claimref{synthesis.pre-descent-contracting-kasner-stage-premise} (P1). There is a rule, part of the laws, that takes the state of the fields on the contracting stage, including the modes that have left the Hubble length there, to a state of the same fields in the descended phase, so that the descended phase's state on scales outside its Hubble length is determined by the exited state. The rule acts in one of two cases:
\begin{enumerate}
\item[(a)] \emph{(Across the wall.)} If the approach reaches its wall, the rule is a matching across the wall into the descent. By Theorem \claimref{synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching}(iii) the wall is a curvature singularity at every stored Kasner point except the five-dimensional vacuum end $(0, 0, 0, 1)$, where the five-dimensional metric is flat and the hidden scale collapses while the Einstein-frame reduction is the isotropic disk point, singular in four dimensions; the frozen-point datum extends regularly across a singular wall in no chart (Theorem \claimref{dark-energy.frozen-point-datum-kasner-wall}(i)).
\item[(b)] \emph{(Across the descent.)} If the descent ends the approach at finite $\tau$, after the modes have left the Hubble length, the rule is a matching across the descent itself.
\end{enumerate}
In either case, under Einstein's equations a turn from contraction to expansion needs a singularity or a violation of the null energy condition (the argued reading of Theorem \claimref{synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching}), so a premise of this kind is needed whichever case holds.

\emph{What it does not fix.} The premise asserts that such a rule exists; it does not give its form. In particular it does not fix which quantity of the exited state is carried over unchanged, and so not how the exited spectrum of a field maps to the spectrum of the curvature perturbation in the descended phase; once a field's state is in the descended phase, its local conversion into the curvature perturbation is the subject of Theorem \claimref{synthesis.local-conversion-cannot-redden-a-gaussian-spectator}. It has no content without (P1).

\emph{What it is for.} With (P1) it is the second of the two hypotheses under which a Kasner approach can be a source of the primordial spectrum: on the expanding branch after a wall no mode exits and the state at the wall is initial data (Theorem \claimref{synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching}(i), (ii)), so a spectrum exited before the descent reaches the record only if it is carried across. It is stated as hypothesis (P2) in the reading of Theorem \claimref{synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching}, which has no assumes edge to it. At the five-dimensional Milne end the wall is the compactified Milne geometry of the ekpyrotic and cyclic models, whose matching is not settled there either (cited from memory).

\emph{What it does not give.} It does not supply the tilt: granting (P1) and (P2), at tree level every curvature coupling the series fixes (twelve values, the largest $\tfrac12$) leaves the exited spectrum blue at the Kasner points the store fixes (Theorem \claimref{synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point}), and the tilt-matching curvature coupling stays a free parameter.

\emph{Tension, recorded and not resolved.} The dating reads pre-descent physics as pre-metric (\claimref{standard-model.dating-descent}, reading (iii), a conjecture), which denies (P1) and so leaves this premise without a stage to carry from; reading (ii) takes the initial singularity to be a division event, with the classical era the descended phase. A rule that carries a metric state across the descent presupposes a metric stage before the classical era, which reading (iii) denies. Which gives way is not decided here.

\emph{Refutation condition.} The premise is false if, with (P1) granted, it is proved that no state of the descended phase depends on the exited modes of the contracting stage: for example, that the descent's map on states takes every state of the stage's fields to one independent of their exited modes, or that across a singular Kasner wall the series' field equations admit no continuation of data outside the Hubble length when the approach reaches the wall and the descent does not end it first. It falls with (P1) if (P1) is refuted.

## technical
If a contracting Kasner stage before the descent is granted (premise (P1)), the modes it stretches beyond the Hubble length still have to reach the universe we observe, which expands from the descent. This premise takes as given a rule that carries the stage's state into the descended phase: a matching across the wall if the approach runs into it, which at every stored Kasner point except one five-dimensional end is a true curvature singularity, or a matching across the descent itself if the descent cuts the approach short after the modes have left. Under Einstein's equations a turn from contraction to expansion needs a singularity or a violation of the null energy condition, so some such rule is needed in either case. The premise says the rule exists, not what it is: it does not fix which quantity passes through unchanged, and so not which spectrum the descended phase inherits. Even with both premises granted the tree-level couplings the series fixes leave the spectrum blue, so the tilt is not supplied. It stands against the dating's conjectured pre-metric reading of pre-descent physics; the tension is recorded, not resolved. It would be refuted by a proof that the descended phase's state cannot depend on the exited modes, for example that the descent's map on states erases them.

## lay
Suppose that before the framework's starting event, the descent, space was being squeezed toward a singularity, stretching the early ripples. Those ripples would still have to survive into the expanding universe we see, passing through either a true singularity or the descent itself. This assumption says that they do: some rule of nature carries them across. The framework does not say what the rule is, and its own account of the descent suggests there was no ordinary geometry before it, so the assumption sits uneasily with it. Even with this rule the fields the framework fixes give ripples tilted the wrong way.

## one-liner
Premise (P2), given (P1): a rule of the laws carries the state of the contracting pre-descent stage, its exited modes included, into the descended phase, across the wall if the approach reaches it (a curvature singularity at every stored Kasner point but the five-dimensional Milne end) or across the descent if the descent ends the approach; its form, and so which spectrum is inherited, is not fixed; stated as a hypothesis by the Kasner-exit result (no assumes edge); it does not supply the tilt; in tension with the dating's conjectured pre-metric reading, unresolved; refuted by a proof that the descended state cannot depend on the exited modes.
