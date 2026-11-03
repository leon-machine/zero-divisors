---
id: synthesis.r-lambda-regularity-cosmological-horizon
kind: claim
version: 4
title: '(R$_{\Lambda}$): regularity at the cosmological horizon''s fixed locus'
status: postulate
region: synthesis
subject: thermality
tags: [thermal-premises, horizons, modular-theory]
proposed_by:
  kind: ai
  session: de-sitter-temperature-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.cosmological-horizon-boundary-modes
- obj.synthesis.gtg-flat-spacetime-gauge-fields
lineage:
  derived_from:
  - singularity.r-regularity-fixed-locus
extraction:
  maintainer_pass_gtg_l0:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'de Sitter chart sign corrected: beta = -rH (expanding chart, free fall dr/dt = Hr), so that the chart contains the future cosmological horizon the note sentence names; with beta = +rH it is the contracting chart and contains the past horizon. Checked exactly in verify/dictionary_identities.py.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 2 (Leon''s decisions 1 and 13 of 23 October): adds a note that the continuum restatement of (R_Lambda) follows from the new postulate synthesis.n-plus-null-ground-state by synthesis.positive-null-energy-gives-r-premises (iii), and that this point-spectrum wording is its discretisation; the premise keeps postulate status and its statement is unchanged. Version 1 -> 2.'
  flow_note: phase flow e^{-i omega_j t} on the modes (the T05 Thm 7.16 sense).
  note: Premise (R) of T05 (Premise 7.19) transplanted from the Schwarzschild horizon to the cosmological horizon. As there, it is not derived from the transport principle, and Theorem synthesis.cosmological-horizon-completed-pair (iv) shows that its locus is regular; no de Sitter counterpart of singularity.why-calibration-cannot-be-internal is proved. It is the premise every derivation of the Gibbons-Hawking temperature uses.
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity per Leon 2026-10-23 (DICTIONARY, Bifurcation surfaces): the Euclidean section is that of the static de Sitter field on flat spacetime, smooth at its tip; the bifurcation sphere replaced by a cross-section of the horizon locus r = 1/H in the static Painleve-Gullstrand chart (area 4 pi/H^2, surface gravity H), with the note sentence that the bifurcation surface itself lies beyond one flat chart; the closed Euclidean section noted as not used. Premise content, scope and postulate status unchanged. Fix (Leon 2026-10-23, referee GR1): the regularity wording "equivalently, the state is regular across the horizon locus" replaced by "for a state that is KMS for the Killing flow, this is also the period at which it is regular across the horizon locus in the PG chart"; clauses, scope and status unchanged.'
---

## formal
For every mode $j$ of the boundary modes of the cosmological horizon (Definition \claimref{obj.synthesis.cosmological-horizon-boundary-modes}) and every pair $a, b$ of elements of its ladder $\{v_{j}, v_{j}^{*}\}$, the correlation function $F_{a,b}(t) := \omega\bigl(a\,\alpha_{t}(b)\bigr)$ of the static Killing flow $\alpha_{t} = \operatorname{Ad}(e^{it\omega_{j}K_{j}})$, an entire function of $t$, continues in imaginary Killing time to a single-valued function on the regular Euclidean section of the static patch of the de Sitter gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}; its static Painlev\'e-Gullstrand chart, Wick-rotated), and its two orderings meet after one period:
\[
F_{a,b}\bigl(t + i\,p\bigr) \;=\; \omega\bigl(\alpha_{t}(b)\,a\bigr), \qquad p \;=\; \frac{2\pi}{\kappa_{\Lambda}} ,
\]
the period at which the Euclidean section is smooth at its tip (Proposition \claimref{synthesis.de-sitter-static-boost-frozen-point}(iii)); for a state that is KMS for the Killing flow, this is also the period at which it is regular across the horizon locus in the Painlev\'e-Gullstrand chart. The horizon locus is met on a cross-section of the cosmological horizon locus $r = 1/H$ in the static Painlev\'e-Gullstrand chart of de Sitter space ($\hb = 1 - \beta P$, $\beta = -rH$, the expanding chart, whose free-fall observers have $dr/dt = Hr$ and which contains the static observer's future horizon), of area $4\pi/H^{2}$, on which the static Killing field is null and normal with surface gravity $H$. In words: each single-mode marginal is KMS for the static Killing flow at exactly the period the smoothness of the Euclidean de Sitter section at its tip dictates; the condition is local, posed at the tip, and the closed Euclidean section as a whole is not used.

\emph{Note (continuum restatement).} Posed on the continuum of the cosmological horizon's null generators (Definition \claimref{obj.hawking.continuum-mode-space}), the content of (R$_{\Lambda}$) follows from Premise \claimref{synthesis.n-plus-null-ground-state}: by Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(iii) the generators' modes are then jointly KMS for the static Killing flow at $\beta = 2\pi/H$. The wording above, on the ladders $\{v_{j}, v_{j}^{*}\}$ with a phase-acting flow, is a discretisation of that statement, recovered only for modes of vanishing Mellin width; (N$_{+}$) itself cannot be posed on point spectrum. (R$_{\Lambda}$) remains a premise.

The bifurcation surface itself, where the boost flow has its fixed points, lies beyond one flat chart (it is the meeting of the four regions of the maximal extension); the chart contains the future horizon, on whose cross-sections the area, the surface gravity and the boost flow are those stated.

## technical
This is the singularity paper's regularity premise (R), moved from the black hole's horizon to the cosmological one. Continue the static Killing flow to imaginary time. The Euclidean section of the static patch of the de Sitter field on flat spacetime is smooth at its tip only if imaginary time has period $2\pi/\kappa_{\Lambda}$. The premise asks that each mode's correlation functions be single valued on that smooth section. Equivalently, each single-mode marginal is a KMS state of the static flow at that period. It is a premise, not derived here; its locus, met on the cross-sections of the horizon locus $r = 1/H$ in the static Painlev\'e-Gullstrand chart (area $4\pi/H^{2}$, surface gravity $H$), is regular ($\sigma = 2$), as at Schwarzschild, where the singularity paper proves the transport principle cannot supply (R). On the continuum of the horizon's light rays its content follows from the null ground-state premise (N$_{+}$), which has no temperature in it; the ladder wording here is its discretisation. The bifurcation sphere itself lies beyond one flat chart; the chart's horizon cross-sections carry the same area, surface gravity and boost flow.

## lay
The black-hole temperature in this series rests on one assumption: the quantum state looks smooth when time is continued into the imaginary direction, at the period the gravitational field needs in order to describe a geometry with no sharp point. This is the same assumption made for the horizon of a universe with a positive cosmological constant. It is the assumption behind the standard calculation of that horizon's temperature, and the series does not derive it.

## one-liner
(R$_{\Lambda}$): each mode of the cosmological horizon is KMS for the static Killing flow at the period $2\pi/\kappa_{\Lambda}$ at which the Euclidean section of the de Sitter field is smooth at its tip.
