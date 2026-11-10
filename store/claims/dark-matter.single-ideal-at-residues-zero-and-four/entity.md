---
id: dark-matter.single-ideal-at-residues-zero-and-four
kind: claim
version: 1
title: 'SI: a single chiral spinor ideal at residues 0 and 4'
status: postulate
region: dark-matter
subject: dark-matter
tags: [counting-rules, dark-matter-ratio]
proposed_by:
  kind: ai
  session: maintainer-2026-11-10
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  version: 1
  source: maintainer pass of 2026-11-10
review: draft
lineage:
  motivated_by:
  - dark-matter.status-rule
  - synthesis.reversion-pairing-vanishes-residues-zero-four
  - synthesis.lowest-causal-residues-zero-four-content
  - synthesis.residues-zero-four-real-chirality-anomaly
  - synthesis.invariant-forms-on-spinor-ideal-factor-through-reversion
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'New postulate, registered at Leon''s decision 5 of 10 November 2026: the single-ideal clause, clause (vi) of dark-matter.status-rule, was a condition of the closed form for the dark-to-baryon total held only as text. It is registered here in the words of that clause, with its cost and the statement that it was chosen knowing that the fit needs it, so that the past cone of the total shows it. Nothing is added to the clause. Assumes edges are drawn from the stored statements of the total (dark-matter.unit-ball-rule, dark-matter.total-function-thickness, dark-matter.democracy-de-sitter-radius-unit-ball) and from synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball.'
---

## formal
\emph{Premise (SI), the single-ideal clause.} At the reversal-fixed residues $0$ and $4$ a constituent lies in one chiral spinor ideal, and its mass is read through the reversion pairing on that ideal (the pairing reading of mass), not through the total momentum of Premise \claimref{dark-tower-matter.h1-momentum} (the momentum reading). The reversion pairing on one ideal vanishes identically exactly at these residues (Theorem \claimref{synthesis.reversion-pairing-vanishes-residues-zero-four}), so under the premise the towers of residues $0$ and $4$ hold no massive matter and do not enter the dark-to-baryon count.

\emph{Where it comes from.} This is clause (vi) of Observation \claimref{dark-matter.status-rule}, a costed clause of the constituent definition, registered here as a premise in that clause's words. It was chosen knowing that the unit-ball fit needs it: the closed form $(11\pi + 16)/(3\pi)$ sums over the mirror and the four odd towers only.

\emph{What it costs.} With residue $4$ populated the ratio is about $6.16$ (Theorem \claimref{synthesis.lowest-causal-residues-zero-four-content}), and with both chiral ideals admitted at residues $0$ and $4$ about $8.254$, against the observed $5.364 \pm 0.065$.

\emph{Support, and its limits.} By Theorem \claimref{synthesis.invariant-forms-on-spinor-ideal-factor-through-reversion} every spin-invariant bilinear form on a single spinor ideal is a linear functional of the reversion pairing, so at these residues no other pairing could carry a mass term: the premise chooses between the pairing reading and the momentum reading, not among pairings. In the lowest-causal window a single ideal is also what anomaly freedom gives at $(1,1)$, and at $(1,5)$ and $(5,1)$ under the reading (G6) that a tower's own gauge fields live on its full six-dimensional space (Theorem \claimref{synthesis.residues-zero-four-real-chirality-anomaly}); (G6) is recorded as a general reading and was itself chosen knowing that the fit needs residue $4$ empty. Neither supplies the premise: the series does not derive the pairing reading at these residues.

\emph{Refutation condition.} The premise is false if the series' own structure gives matter at residue $0$ or $4$ a mass (the momentum reading there, or a second ideal), in which case the closed form's total moves to the values above; it becomes a theorem if the pairing reading is derived.

## technical
The towers of residues $0$ and $4$ must be empty for the unit-ball closed form to give the observed dark-to-baryon ratio. The series obtains this by a clause of the constituent definition: one chiral spinor ideal at those residues, with mass read through the reversion pairing, which vanishes identically there. The clause was adopted knowing that the fit needs it; with residue $4$ populated the ratio is about $6.16$, with both chiral ideals admitted about $8.254$. It is supported by the fact that no other invariant pairing exists on one ideal and, in the lowest-causal window, by anomaly freedom of a single ideal (at residue $4$ only under the reading (G6), itself chosen with the fit known), but it is not derived. It was held as text in the assessment of the rule; this entry registers it as a premise so that the total shows it among its conditions.

## lay
The formula for the amount of dark matter counts five hidden sectors and leaves out two others. For that to be right, those two must hold no matter. The series arranges this by a choice in how a particle and its mass are defined in those two sectors, a choice made knowing that the formula needs it. With the other choices the formula gives about 6.2 or 8.3 in place of the measured 5.4. This entry records that choice as an assumption in its own right.

## one-liner
Premise (SI): at residues 0 and 4 a constituent lies in one chiral spinor ideal with mass read through the reversion pairing, which vanishes there, so those towers are empty in the count; a costed clause chosen knowing that the unit-ball fit needs it (about $6.16$ or $8.254$ otherwise), supported but not derived.
