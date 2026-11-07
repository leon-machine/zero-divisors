---
id: dark-matter.imported-trichotomy-descents-data
kind: claim
version: 6
title: 'Imported: the trichotomy and the descent''s data'
status: proved
region: dark-matter
subject: dark-energy
tags:
- the-number-n
- undetermined-input
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'consistency pass, clause (2) worded as the cited clause'
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - dark-energy.under-action-written-norm-parameter-laws@4
  - standard-model.trichotomy-what-kind-number@11
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
locators:
  paper: T14
  number: Fact 2.8
  label: fact:trichotomy
  line: 124
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Clause (2) read "the frozen action is N-insensitive", which is not what the cited clause (2) of standard-model.trichotomy-what-kind-number says and is not true of the action (its prefactor is 3/Lambda); it now states the cited content, the norm fixed by a constraint with pure-gauge fluctuations and no equation of motion; the paper wording stays in source_formal.'
  open_problem: op.trichotomy-exhaustiveness
  correction:
    by: ai-correction
    date: '2026-10-22'
    note: 'Version 5 brings the proof text into line with the formal and technical levels, which the 2026-10-22 maintainer pass already corrected: the seventeenth refutation (v6) no longer uses clause (3) for its last step. Statement unchanged.'
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'A5 follow-up: the corrected seventeenth refutation (v6) no longer cites clause (3); formal and technical now say so instead of naming clause (3) as its last step.'
  source_formal: "\\cite[Prop.~7.6]{ButlerT12}: (1) \\emph{kinematic}: the rescaling covariance fixes every discrete invariant (proved), and no construction from the conformal class and pair structure alone fixes $N$ (observation level); (2) \\emph{non-dynamical}: the frozen action is $N$-insensitive (imported); (3) \\emph{conditional}: if kinematic, dynamical and initial-data are exhaustive (not proved), $N$ is initial data, located at the origin at observation level; (4) \\emph{parameter of the laws} (imported): the three are not exhaustive, since under the action as written $N$ is constant on every solution and varies across $\\Lambda$, a parameter of the laws \\cite[Prop.~5.8]{ButlerT10}, so that (3) holds only if the frozen point's norm is promoted to the value of a Lagrange-multiplier field, a decision that paper records open. Wherever this paper calls a datum initial data of the descent ($\\epsilon$, Proposition \\claimref{dark-matter.asymmetry-arrow-counted-fifteenth-refutation}, clause (1) only, as a stance; the orientation bit, Proposition \\claimref{dark-matter.orientation-arrow-seventeenth-refutation}, clause (3) for its last step), these clauses are premises of the sentence, and clause (4) names the alternative for each, a parameter of the laws rather than data of the event: for the bit that would require the laws to distinguish the two orientations, for which the CPT covariance of the structures Proposition \\claimref{dark-matter.orientation-arrow-seventeenth-refutation} lists leaves no room within them, so the bit is data if it is anything; for $\\epsilon$ the paper takes no position."
  typing:
    by: ai-typing-pass
    note: 'Kept both premises, the restated classification and the parameter-of-the-laws proposition;
      the two dark-matter propositions it mentions are consumers of this fact, not premises. Levels pass:
      the lay level now keeps the observation-level status of the kinematic clause, the unproved exhaustiveness
      and the Lagrange-multiplier alternative; the one-liner keeps the observation level.'
  env: fact
  context_refs:
  - dark-energy.under-action-written-norm-parameter-laws
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
  - dark-matter.orientation-arrow-seventeenth-refutation
  - standard-model.trichotomy-what-kind-number
  flags:
  - 'fact restating several series results: derived from them'
about:
- obj.dark-energy.four-ways-number-enters-theory-shape
---

## formal
\cite[Prop.~7.6]{ButlerT12}: (1) \emph{kinematic}: the rescaling covariance fixes every discrete invariant (proved), and no construction from the conformal class and pair structure alone fixes $N$ (observation level); (2) \emph{non-dynamical}: the norm of the frozen point is not a field, being fixed by a constraint with pure-gauge fluctuations and no equation of motion (imported); (3) \emph{conditional}: if kinematic, dynamical and initial-data are exhaustive (not proved), $N$ is initial data, located at the origin at observation level; (4) \emph{parameter of the laws} (imported): the three are not exhaustive, since under the action as written $N$ is constant on every solution and varies across $\Lambda$, a parameter of the laws \cite[Prop.~5.8]{ButlerT10}, so that (3) holds only if the frozen point's norm is promoted to the value of a Lagrange-multiplier field, a decision that paper records open. Wherever this paper calls a datum initial data of the descent ($\epsilon$, Proposition \claimref{dark-matter.asymmetry-arrow-counted-fifteenth-refutation}, clause (1) only, as a stance; the orientation bit, Proposition \claimref{dark-matter.orientation-arrow-seventeenth-refutation}, which as corrected cites none of these clauses and in particular not clause (3): it reaches clause (I) of Definition \claimref{obj.dark-energy.four-ways-number-enters-theory-shape} directly from CPT covariance, with no exhaustiveness), these clauses are premises of the sentence, and clause (4) names the alternative for each, a parameter of the laws rather than data of the event: for the bit that would require the laws to distinguish the two orientations, for which the CPT covariance of the structures Proposition \claimref{dark-matter.orientation-arrow-seventeenth-refutation} lists leaves no room within them, so the bit is data if it is anything; for $\epsilon$ the paper takes no position.

## technical
The Standard-Model paper classifies $N = M_P/H$ in four clauses: it is not kinematic, since the rescaling covariance fixes every discrete invariant (proved) and no construction from the conformal class and pair structure alone fixes $N$ (observation level); it is not dynamical, the norm of the frozen point being fixed by a constraint, with pure-gauge fluctuations and no equation of motion (imported); if kinematic, dynamical and initial data were exhaustive, which is not proved, $N$ would be initial data; and the three are not exhaustive, since under the action as written $N$ is constant on every solution and varies across $\Lambda$, a parameter of the laws, so the third clause holds only if the frozen point's norm is promoted to a Lagrange-multiplier field.

Wherever the dark-matter paper calls a datum initial data of the descent, these clauses are premises of the sentence, and the fourth names the alternative; the orientation proposition, as corrected, no longer uses the conditional third clause, deriving initial data from CPT covariance directly. For the orientation bit that alternative would need the laws to distinguish the two orientations, which the CPT covariance of the listed structures leaves no room for, so the bit is data if it is anything; for $\epsilon$ no position is taken.

## lay
How does a number such as the ratio of the Planck mass to the Hubble scale enter the theory? An earlier result says that, as far as anyone has found (an observation, not a proof), it is not fixed by geometry alone, that it is not fixed by the dynamics, and that it would be initial data if those were the only options, which is not proved; another result shows that, under the action as written, it is in fact a setting of the laws, unless the frozen point's size is promoted to a field. The dark-matter paper relies on this classification whenever it calls something initial data, and names the alternative each time.

## one-liner
The number $N = M_P/H$ is not dynamical and, at observation level, not kinematic, and under the action as written it is a parameter of the laws rather than initial data, which qualifies each place the dark-matter paper calls a datum initial data of the descent.
