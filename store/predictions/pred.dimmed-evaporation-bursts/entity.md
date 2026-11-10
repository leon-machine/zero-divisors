---
id: pred.dimmed-evaporation-bursts
kind: prediction
version: 6
title: Dimmed final evaporation bursts
status: live
subject: dark-matter
tags:
- live-prediction
- radiation-spectrum
region: programme
proposed_by:
  kind: extraction
  session: full-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
- name: Claude Fable 5.2
  role: 'pointer to the open problem on processes of a quantised gravitational field; prediction unchanged'
  version: 6
  source: maintainer pass of 2026-11-10
review: typed
kill_condition:
  threshold: An undimmed final burst at the standard luminosity
  data_source: Primordial-black-hole burst searches
  registered: 2026-08 (T17 stance table, row 11)
observations:
- date: 2026-09
  dataset: LHAASO burst search; KM3-230213A interpretations
  result: No final evaporation burst detected. LHAASO limits the local rate below 181 per cubic parsec
    per year (99%), assuming a standard burst; a dimmed burst is seen over a smaller volume, so the limit
    is weaker here. Reading the 220 PeV KM3NeT event as a standard explosion is strongly disfavoured;
    dark-charge variants keep it open. Nothing yet measures a dimming factor.
  verdict: pending
  source: LHAASO, PRL 135, 181005 (2025); Airoldi et al., arXiv:2505.24666 (2026); Baker et al., PRL 136
    (2026), arXiv:2505.22722; Dey et al., arXiv:2609.11511 (2026)
- date: 2026-08
  dataset: Primordial-black-hole burst searches
  result: 'Primordial-black-hole burst searches: registered as a minor prediction; the towers degree-of-freedom
    counts are not derived.'
  verdict: pending
  source: T17 stance table, row 11
locators:
  paper: T14
  number: T17 stance 11
  label: tab:stances
extraction:
  maintainer_pass_2026_11_10_graviton:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 5 -> 6, by Leon''s decision of 10 November 2026 (flag now, derive later): one sentence added to the formal and technical levels pointing to open problem op.graviton-rate-as-classical-field-process. The prediction, its status, its kill condition and every number are unchanged.'
  env: table row
  source: T17 tab:stances
  flags:
  - 'basis not linked: no store claim clearly carries it yet'
  typing:
    by: ai-typing-pass
    note: 'No derivations to review; the basis is the infall proposition on parallel boundary mode spaces, which
      states the dimming, not linked here. Basis linked at the end of the build, as the dark-matter typing pass
      proposed. Levels pass: conditions already kept.'
  source_formal: 'Dimmed final evaporation bursts: the hole radiates into all six populated towers, five of them
    dark, so the visible burst is dimmed by the ratio of total to visible light degrees of freedom.'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: correction-2026-10-22
    note: 'Corrected ''all six populated towers, five of them dark'': only this tower (by observation) and the mirror
      (under P2, by the copy theorem) are populated by the series'' own results; the four odd towers are inferred
      from the observed dark remainder at observation level (dark-matter.which-towers-are-populated, conjectured).
      The dimming is now stated as at least the mirror''s factor, more if the odd towers are populated. The kill
      condition is unchanged.'
  maintainer_pass_2026_10_31:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 4 -> 5. Scope note added to the formal and technical levels: with a populated five-dimensional tower the time-rescaled copy holds only for masses well above the crossover M_x of synthesis.five-dimensional-tower-kaluza-klein-channels-steepen-burst (under the interface premise); below it M^4 = 4 B tau and the primary tail steepens to E^-4. The basis pin to synthesis.dimmed-burst-time-rescaled-copy moves to @2, its version after the same scope note. The kill condition is unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Version 3 -> 4. Restated on synthesis.dimmed-burst-time-rescaled-copy, added to the basis: "dimmed by the ratio" now holds only for the primary high-energy tail and for the visible fraction of the power at fixed mass; the visible energy in a fixed final window dims by D^(2/3) and the temperature at fixed time to the end by D^(1/3); against the standard expectation (this tower plus gravitons) the factor is D = (2 + g + o)/(1 + g), at least 2 only if the odd towers emit at least as much as the gravitational sector, replacing "at least a factor of about two". The kill condition is unchanged.'
derivations:
- name: basis
  uses:
  - dark-matter.parallel-boundary-mode-spaces-one-wall@5
  - synthesis.dimmed-burst-time-rescaled-copy@2
---

## formal
Dimmed final evaporation bursts: the hole radiates into every populated tower, so it loses mass faster than the standard expectation (this tower plus gravitons) by the factor $D = \Psi_{\mathrm{tot}}/\Psi_{0}$ of total to standard emission, and the visible burst of its last $\tau$ is the standard burst of its last $D\tau$ divided by $D$ (Theorem \claimref{synthesis.dimmed-burst-time-rescaled-copy}). Dimming by the full ratio holds for the primary high-energy tail and for the visible fraction of the power at fixed mass; the visible energy in a fixed final window is dimmed by $D^{2/3}$, and the temperature at a fixed time before the end is lowered by $D^{1/3}$. The populated towers are this one and, under P2, the mirror, whose light content copies ours (Theorem \claimref{dark-matter.mirror-tower-copy-one}), so $D = (2 + g + o)/(1 + g)$, with $g$ and $o$ the gravitational and odd-tower emission relative to this tower's: $D \ge 2$ if and only if $o \ge g$, and $D = 2 - g/(1 + g)$ if the odd towers emit nothing. If the four odd towers hold matter, as Observation \claimref{dark-matter.which-towers-are-populated} infers from the observed dark remainder, then $o > 0$ and the dimming is larger. \emph{Scope note.} The time-rescaled copy assumes constant emission coefficients; if a five-dimensional tower is populated, its Kaluza-Klein levels are emission channels under the interface premise and the copy holds only for holes well above the crossover mass $M_{\times}$ of \claimref{synthesis.five-dimensional-tower-kaluza-klein-channels-steepen-burst}(ii): below it $M^{4} = 4B\tau$ and the primary high-energy tail steepens from $E^{-3}$ to $E^{-4}$, so a search for the final burst then tests that law, not the rescaled copy. The baseline ``this tower plus gravitons'' counts emission into the helicity-2 channels of the gravitational field as standard physics does, through the term $g$; the series holds no quantum of that field (conventions, section ``Gravity and the graviton''), and whether $g$ is kept is part of open problem op.graviton-rate-as-classical-field-process ($g = 0$ gives $D = 2 + o$), the prediction being unchanged until that is settled.

## technical
An evaporating black hole radiates into every populated tower, in proportion to each tower's light degrees of freedom once its temperature exceeds their gaps, because barriers and greybody factors belong to the shared exterior metric. The hole therefore passes through the same masses, with the same visible spectrum at each, as in the standard case (this tower plus gravitons), but faster by the ratio $D$ of total to standard emission: the visible burst of its last $\tau$ is the standard burst of its last $D\tau$ divided by $D$. At a fixed time before the end, the primary high-energy tail is dimmed by the full $D$, the visible energy only by $D^{2/3}$, and the temperature is lower by $D^{1/3}$.

The series populates two towers by its own results, this one by observation and the mirror under P2, whose light content copies ours, so $D = (2 + g + o)/(1 + g)$ with $g$ the gravitational and $o$ the odd towers' emission relative to this tower's. $D$ is at least two only if the odd towers emit at least as much as the gravitational sector; with no odd-tower emission it is $2 - g/(1 + g)$, just below two. The towers' degree-of-freedom counts are not derived, so $o$, and with it the size of the dimming above the mirror's share, is not fixed. If a five-dimensional tower is populated, these laws hold only for holes well above the crossover mass of \claimref{synthesis.five-dimensional-tower-kaluza-klein-channels-steepen-burst}; below it the burst follows $M^{4} = 4B\tau$, with a steeper high-energy tail. The baseline ``this tower plus gravitons'' counts emission into the helicity-2 channels of the gravitational field as standard physics does, through the term $g$; the series holds no quantum of that field (conventions, section ``Gravity and the graviton''), and whether $g$ is kept is part of open problem op.graviton-rate-as-classical-field-process ($g = 0$ gives $D = 2 + o$), the prediction being unchanged until that is settled.

## lay
A small black hole ends its life in a final flash of radiation. In this framework the hole radiates into the dark towers as well as into ours, so it loses mass faster and runs through its final stages in less time than standard physics expects. The mirror world alone, whose particles copy ours, roughly doubles the rate. The very high energy light emitted directly by the hole is then dimmed by the full factor, about two, while the total light seen in the last seconds is dimmed less, by that factor to the power two thirds, and the burst looks cooler at a given time before its end. If the other dark towers also hold matter, every one of these effects is larger.

## one-liner
Final black-hole evaporation bursts are the standard burst rescaled in time by $D = (2 + g + o)/(1 + g)$, the ratio of total emission to that of this tower plus gravitons: the primary high-energy tail dims by $D$, the energy in a fixed final window by $D^{2/3}$; $D$ is about two from the mirror under P2 (at least two only if the odd towers emit at least as much as gravity), and more if the odd towers are populated.
