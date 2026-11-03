---
id: dark-matter.status-rule
kind: claim
version: 4
title: The status of the rule
status: conjectured
region: dark-matter
subject: dark-matter
tags:
- counting-rules
- dark-matter-ratio
- confronted-with-data
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
lineage:
  motivated_by:
  - dark-matter.population-count-one-share-half-percent
  - dark-matter.total-function-thickness
  - dark-matter.unit-ball-rule
locators:
  paper: T14
  number: Obs 7.31
  label: obs:status
  line: 1222
extraction:
  typing:
    by: ai-typing-pass
    note: 'Conjectured observation that already had lineage.motivated_by (the population count and the
      thickness family); no edges to type, levels only. Levels pass: lay now names R1 to R3, the observation
      level and the one-Planck-column scope with the ACT caveat; one-liner says premises and observation
      level.'
  maintainer_pass_2026_10_31:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 3 -> 4. Note added to clause (vi): by synthesis.invariant-forms-on-spinor-ideal-factor-through-reversion every spin-invariant pairing on a single spinor ideal is a linear functional of the reversion pairing, so at residues 0 and 4 no other pairing exists; the clause is unchanged and remains chosen with the fit known.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Version 2 -> 3 (maintainer decision of 26 October on residues 0 and 4). New clause (vi): the emptiness of residues 0 and 4 that the fit needs is costed: the series adopts a single chiral spinor ideal at those residues with the pairing reading of mass (synthesis.reversion-pairing-vanishes-residues-zero-four), chosen knowing that the unit-ball fit needs it, and records the reading (G6), that a tower''s own gauge fields live on its full space, as the general reading and not a postulate (synthesis.residues-zero-four-real-chirality-anomaly). The concluding paragraph, the technical and lay levels and the one-liner name the clause. No number changes.'
  env: observation
  context_refs:
  - dark-matter.population-count-one-share-half-percent
  - dark-matter.total-function-thickness
  unresolved_refs:
  - rem:forms
  eqrefs: 1
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - dark-matter.unit-ball-rule (motivated_by)
    added_dependants: []
    added_about: []
    verdict: connected
    note: Conjectured meta-observation on the unit-ball rule; lineage now also names the rule it assesses;
      nothing derived relies on it.
---

## formal
\begin{enumerate}
\item[(i)] The relation was found by solving \eqref{eq:sum} for the observed value, not predicted.
\item[(ii)] Among all expressions $1 + 2a + 2b$ with $a$ and $b$ ratios of the eight measures $V_{2}$ to $V_{5}$ and $|\Sph^{1}|$ to $|\Sph^{4}|$ ($3136$ expressions), $54$ lie within one standard deviation of $5.364$, taking $14$ distinct values, and $85$ within two; neighbouring targets give comparable counts ($43$ at $5.322$, $33$ at $5.24$). The closed form is one of fourteen equally simple candidates in the error bar (script). The mechanism of Section \ref{subsec:free} adds a discrete look-elsewhere of the same kind: of the clause combinations Table \ref{tab:excludes} lists, only the chosen one reaches the observed value, and the clauses were chosen with it known.
\item[(iii)] The ball and sphere forms of Remark \ref{rem:forms} are one relation. The exchanged assignment and the clock reflection give the same total as the other root of $T(c) = 5.364$, with the three- and five-dimensional shares exchanged; none of them is independent evidence for the total, and the exchanged assignment is not physically consistent and differs from the rule in composition (Remark \ref{rem:forms}).
\item[(iv)] The relation rests on R1, R2 and R3, none supplied by the series; the contact mechanism explains R3's value and does not derive it, and the de Sitter reading, which replaces R2 by democracy and fixes the unit, gives thickness $\tfrac{3\pi}{8}$ or $\tfrac{\pi}{4}$ and totals of $5.000$, $5.667$ or $4.333$, none within four standard deviations.
\item[(v)] The comparison is with one Planck column; the others give $5.322$ to $5.376$, and the ACT DR6 combination gives about $5.22$, below the floor of Proposition \claimref{dark-matter.total-function-thickness}(ii). If that lower value holds, no thickness in the family fits.
\item[(vi)] The relation needs residues $0$ and $4$ empty: with residue $4$ populated the ratio is about $6.16$ (\claimref{synthesis.lowest-causal-residues-zero-four-content}), and with both chiral ideals admitted at residues $0$ and $4$ the total is about $8.254$. With one spinor ideal the emptiness of residues $0$ and $4$ is equivalent to the pairing reading of mass in dimensions $n \equiv 2 \pmod 4$, where the reversion pairing on one ideal vanishes identically (\claimref{synthesis.reversion-pairing-vanishes-residues-zero-four}); in the lowest-causal window it is also what anomaly freedom of a single ideal gives at $(1,1)$, and at $(1,5)$, $(5,1)$ under the reading (G6) that a tower's own gauge fields live on its full six-dimensional space and act on its constituents (\claimref{synthesis.residues-zero-four-real-chirality-anomaly}). The series adopts the single chiral ideal at residues $0$ and $4$ with the pairing reading of mass as a costed clause of the constituent definition, chosen knowing that the unit-ball fit needs it, and records (G6) as the general reading of where a tower's own gauge fields live, not as a postulate. The clause is part of what the relation rests on, beside R1 to R3. \emph{Note.} By Theorem \claimref{synthesis.invariant-forms-on-spinor-ideal-factor-through-reversion}, every spin-invariant bilinear form on a single spinor ideal is a linear functional of the reversion pairing, so at residues $0$ and $4$ no other pairing exists that could carry a mass term: the clause chooses between the pairing reading and the momentum reading of mass, not among pairings. It remains a clause chosen with the fit known.
\end{enumerate}
The relation is fitted: a closed form, a consistent mechanism inside the sourcing rule, and one length, fixed by R3 at one cell radius and returned by a contact mechanism on four clauses of its own. Its tier is observation level on R1 to R3 and on the costed clause (vi), and it supersedes nothing in Proposition \claimref{dark-matter.population-count-one-share-half-percent}: the mirror's share stays derived and the odd towers' shares stay underived, now with one candidate value each and its price stated.

## technical
The unit-ball relation $\Omega_{\mathrm{dark}}/\Omega_{b} = 1 + 2 \cdot \frac{4}{3} + 2 \cdot \frac{8}{3\pi}$ was found by solving the sum for the observed value, not predicted. Among the $3136$ expressions $1 + 2a + 2b$ with $a$, $b$ ratios of ball volumes and sphere measures, $54$ lie within one standard deviation of $5.364$, taking $14$ distinct values, and the mechanism's clause choices add a further look-elsewhere of the same kind. The ball and sphere forms are one relation, and the exchanged assignment and the clock reflection are not independent evidence.

The relation rests on R1, R2 and R3, none supplied by the series, and on residues $0$ and $4$ being empty, which the series obtains from a single chiral spinor ideal there with the pairing reading of mass, a costed clause adopted knowing that the fit needs it (with residue $4$ populated the ratio would be about $6.16$); the de Sitter reading misses by more than four standard deviations; and an ACT DR6 combination near $5.22$ lies below the family's floor, so if it holds no thickness fits. The relation is fitted, at observation level on R1 to R3, and leaves the derived mirror share untouched.

## lay
The paper's formula for the amount of dark matter matches the measured value closely, and this assessment explains why that match should not be over-read. The formula was found by working backwards from the measurement, and many equally simple formulas fit just as well. It rests on three unproved premises (R1 to R3), and on a further choice, made knowing the answer it needed, that two of the hidden families hold no matter; the match is to one Planck data set; another survey combination gives a lower value that no version of the formula can reach. So it is recorded as a fitted relation at observation level, not a prediction.

## one-liner
The unit-ball relation for the dark-to-baryon ratio is a fit resting on premises R1 to R3 and on the costed single-ideal clause that empties residues 0 and 4, at observation level, one of fourteen equally simple values within the error bar of one Planck column, not a prediction.
