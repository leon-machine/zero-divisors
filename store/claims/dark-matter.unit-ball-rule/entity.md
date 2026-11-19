---
id: dark-matter.unit-ball-rule
kind: claim
version: 7
title: The unit-ball rule
status: proved
region: dark-matter
subject: dark-matter
tags:
- dark-matter-ratio
- counting-rules
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
- name: Claude Fable 5.2
  role: 'the two registered conditions (single-ideal clause, population of the odd towers) assumed; the sourcing lemma used; statement of what the total rests on'
  version: 6
  source: maintainer pass of 2026-11-10
- name: Claude Fable 5.2
  role: 'restated on Premise E in place of R1 and R2; clauses (ii) to (iv) on what the two premises say'
  version: 7
  source: maintainer pass of 2026-11-19
amendments:
- version: 7
  kind: restatement
  defect: 'version 6 stated the rule under R1 and R2 with R3''s unit each tower''s own cell radius; by the decision of 19 November 2026 the unit is one common length and the rule rests on equal mass per unit ball, and the statement did not say that the two premises are then equivalent to the closed form'
  evidence: check.py::check_e_and_r3_are_the_closed_form
review: typed
derivations:
- name: main
  uses:
  - dark-matter.projection-every-towers-content-dilutes-ones@3
  - dark-matter.towers-are-residues-single-clock-filter@5
  assumes:
  - dark-matter.e-equal-mass-per-unit-ball@1
  - dark-matter.odd-towers-populated@1
  - dark-matter.r3-one-cell-per-unshared-direction@3
  - dark-matter.single-ideal-at-residues-zero-and-four@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_shares
- kind: check
  ref: check.py::check_dark_towers_and_dimensions
- kind: check
  ref: check.py::check_total
- kind: check
  ref: check.py::check_quanta_do_not_enter
- kind: check
  ref: check.py::check_e_and_r3_are_the_closed_form
- kind: check
  ref: check.py::check_one_length_only
locators:
  paper: T14
  number: Prop 7.6
  label: prop:rule
  line: 821
extraction:
  maintainer_pass_2026_11_19:
    by: maintainer-2026-11-19
    date: '2026-11-19'
    note: 'Version 6 -> 7. Leon''s decision of 19 November 2026 (reversing decision 9 of 10 November 2026): R3''s unit of thickness is one length common to all towers, and the rule is stated under Premise E (dark-matter.e-equal-mass-per-unit-ball) and R3 in place of R1, R2 and R3. Assumes edges: E added, R1 and R2 removed, R3 repinned to version 3. Clause (i) is the rule; its closed form and both shares are unchanged. New clauses: (ii) the quanta do not enter, and R1 with R2 implies E; (iii) E with R3, for some length, is equivalent to the two shares with equal thicknesses, and the three-dimensional share holds by the definition of the length; (iv) E holds in one length only. The paragraph on what the total rests on is brought up to date. Three check functions added.'
  maintainer_pass_2026_11_12:
    by: maintainer-2026-11-12
    date: '2026-11-12'
    note: 'Scope note, version kept, no statement changed (Leon''s decision of 12 November 2026: the inherited charge is B - L). The sentence that the mirror''s share of one is derived separately now reads: derived under the hypothesis of equal conversion (the mirror''s ratio of baryon number to B - L equals this tower''s; not shown; attack item (d) of op.matter-asymmetry-origin; Proposition dark-matter.stored-asymmetry-charge-not-number (i), version 11). The closed form and its two shares 4/3 and 8/(3 pi) are unchanged; the comparison of the total with the observed 5.364 takes the mirror''s unit as one and is conditional on the hypothesis.'
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 5 -> 6. Leon''s decision 5 of 10 November 2026: assumes edges added to the two conditions registered that day, dark-matter.single-ideal-at-residues-zero-and-four and dark-matter.odd-towers-populated, which the closed form held only as text. A uses edge to the sourcing lemma dark-matter.projection-every-towers-content-dilutes-ones is added: the proof and R3 are phrased in the sourcing rule, and without the edge P1 was missing from the cone. A paragraph ''What the total rests on'' states what the audit of the cone found (the postulates under the closed form, R2 entering twice, the total a fit of two shares against one measured number, and which ingredients were chosen with the number known, quoting dark-matter.status-rule and dark-matter.which-towers-are-populated only). R3 repinned 1 -> 2 after its unit was stated (each tower''s own cell radius; under R2 the common unit used here), the use holding as cited. Arithmetic and check unchanged; coverage.yaml records the three new premises as untouched.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the shares V_3/V_D under R1 to R3, the five dark towers'' dimensions, and the total (11 pi + 16)/(3 pi) against the record. Version 4 -> 5.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.r1-equal-mass-per-quantum
    - dark-matter.r2-one-quantum-per-unit-ball
    - dark-matter.r3-one-cell-per-unshared-direction
    - dark-matter.towers-are-residues-single-clock-filter
    note: 'R1 to R3 added as assumes since the statement is under them; the residue census added as the
      source of the representatives'' dimensions in the sum, a judgement call since the paper does not
      cite it in the proof. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.towers-are-residues-single-clock-filter
  small_findings_pass:
    by: ai-small-findings-pass
    date: '2026-10-22'
    finding: CONTRADICTIONS_VALUES M11
    note: 'Every level now says the agreement with 5.364 is a fit, as dark-matter.status-rule records
      (found by solving for the observed value; one of fourteen equally simple candidates). The arithmetic
      is unchanged: V3/V2 = 4/3, V3/V4 = 8/(3 pi), 1 + 8/3 + 16/(3 pi) = (11 pi + 16)/(3 pi). Suggested
      maintainer edge: dark-matter.status-rule comments_on this rule.'
    open_problem: op.small-findings
  open_problem: op.small-findings
---

## formal
Under Premises E (\claimref{dark-matter.e-equal-mass-per-unit-ball}) and R3 (\claimref{dark-matter.r3-one-cell-per-unshared-direction}), with the four odd towers populated (Premise \claimref{dark-matter.odd-towers-populated}) and residues $0$ and $4$ empty (Premise \claimref{dark-matter.single-ideal-at-residues-zero-and-four}):
\begin{enumerate}
\item[(i)] \emph{(The rule.)} The share of a tower whose space has $D$ dimensions is $f = \tfrac{V_{3}}{V_{D}}$, and
\[
\frac{\Omega_{\mathrm{dark}}}{\Omega_{b}} \;=\; V_{3}\sum_{\text{dark }r}\frac{1}{V_{D_{r}}}
\;=\; \frac{V_{3}}{V_{3}} + 2\,\frac{V_{3}}{V_{2}} + 2\,\frac{V_{3}}{V_{4}}
\;=\; 1 + \frac{8}{3} + \frac{16}{3\pi} \;=\; \frac{11\pi + 16}{3\pi} \;=\; 5.36432\ldots
\]
against the observed $5.364 \pm 0.065$.
\item[(ii)] \emph{(The quanta do not enter.)} Only the mass per unit ball enters. A filling that keeps E has the shares of (i) whatever its quanta weigh and however many they are. Premises R1 (\claimref{dark-matter.r1-equal-mass-per-quantum}) and R2 (\claimref{dark-matter.r2-one-quantum-per-unit-ball}), taken in E's length, imply E, so the rule holds under R1 to R3, as it was first stated; they are not needed.
\item[(iii)] \emph{(E and R3 are the closed form.)} Write $\rho_{2}$, $\rho_{3}$, $\rho_{4}$ for the mass densities of a three-dimensional tower, of this world and of a five-dimensional tower, each in its own space, let the three-dimensional towers' sheets be $s$ apart and let the five-dimensional towers' matter count through a length $t$ of the extra direction, so that in the sourcing rule
\[
f_{3\mathrm{D}} \;=\; \frac{\rho_{2}}{s\,\rho_{3}}, \qquad f_{5\mathrm{D}} \;=\; \frac{\rho_{4}\,t}{\rho_{3}} .
\]
Then there is a length $d$ for which E holds with $s = t = d$, as R3 requires, if and only if $s = t$, $f_{3\mathrm{D}} = \tfrac{V_{3}}{V_{2}}$ and $f_{5\mathrm{D}} = \tfrac{V_{3}}{V_{4}}$. In particular, for any $\rho_{2}$ and $\rho_{3}$ the length $d = \rho_{2}V_{2}/(\rho_{3}V_{3})$ is the only one at which a three-dimensional tower and this world hold equal mass per ball, and with the sheets that far apart $f_{3\mathrm{D}} = \tfrac{V_{3}}{V_{2}}$ whatever the two densities are; E then holds for the five-dimensional towers exactly when $f_{5\mathrm{D}} = \tfrac{V_{3}}{V_{4}}$. So across dimensions the two premises say what the closed form says, and that the two thicknesses are one length; they add nothing to it.
\item[(iv)] \emph{(One length.)} E cannot hold in two different lengths: equal mass per ball at $d$ and at $d' \neq d$ would make $(d'/d)^{D}$ take one value at $D = 2$, $3$ and $4$.
\end{enumerate}
The agreement of (i) with the observed value is built in, not predicted: the relation was found by solving for the observed value, and its clauses were chosen with it known, and the closed form is one of fourteen equally simple candidates within the error bar (Observation \claimref{dark-matter.status-rule}). By (iii) the premises carry no content beyond the closed form.

\emph{What the total rests on.} On the stored dependence edges the past cone of this closed form holds these postulates of the dark-matter subject: E and R3; P1 (\claimref{dark-matter.p1-single-frozen-point}), through the sourcing rule in which the shares are read (Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones}); P2 and P3, through the census of Proposition \claimref{dark-matter.towers-are-residues-single-clock-filter}; and the two conditions registered as premises on 10 November 2026, the single-ideal clause \claimref{dark-matter.single-ideal-at-residues-zero-and-four} and the population of the odd towers \claimref{dark-matter.odd-towers-populated}. Until 19 November 2026 the cone held R1 and R2 in place of E, with R3's unit each tower's own cell radius and R2 entering twice; one length now does both jobs, as the radius of E's ball and as R3's unit. The democracy premise (\claimref{dark-matter.d-democracy-total-mass}) is not among them: it is E at the de Sitter radius, a reading of its own. The total remains a fit. The mirror's share of one is derived separately (Proposition \claimref{dark-matter.population-count-one-share-half-percent}), so the closed form fixes two shares, $\tfrac{4}{3}$ and $\tfrac{8}{3\pi}$, against one measured number, the remainder $4.36 \pm 0.07$. Chosen with that number known, by the store's own record: the relation was found by solving for the observed value (Observation \claimref{dark-matter.status-rule}(i)); the clauses of the contact mechanism that returns R3's value were chosen with it known (the same, (ii)); the single-ideal clause was chosen knowing that the fit needs it (the same, (vi)); and the population of the odd towers is inferred from the remainder itself (Observation \claimref{dark-matter.which-towers-are-populated}). P1, P2 and P3 belong to the paper's earlier sections, written before the rule was proposed (Remark \claimref{note.dark-matter.setting-dark-matter-ratio-unit-ball}).

## technical
Under Premise E (one length $d$ at which every populated tower holds the same mass $\mu$ per ball of radius $d$ of its own space) and R3 (matter counts through one such length of each unshared direction), a tower whose space has $D$ dimensions has mass density $\mu/(V_{D}d^{D})$ and so contributes a share $f = V_{3}/V_{D}$ of our matter per unit of our volume, with $V_{n}$ the volume of the unit $n$-ball. Summing over the five dark towers at their nearest-dimension representatives (the four odd ones taken as populated and residues $0$ and $4$ as empty, two conditions registered as premises), the mirror with $D = 3$, two three-dimensional towers with $D = 2$ and two five-dimensional towers with $D = 4$, gives
$$\frac{\Omega_{\mathrm{dark}}}{\Omega_{b}} = 1 + \frac{8}{3} + \frac{16}{3\pi} = \frac{11\pi + 16}{3\pi} = 5.36432\ldots,$$
against the observed $5.364 \pm 0.065$. The agreement is a fit, not a prediction: the relation was found by solving for the observed value, its clauses chosen with it known, and it is one of fourteen equally simple values in the error bar (Observation \claimref{dark-matter.status-rule}).

Only the mass per unit ball enters, not what a tower's quanta weigh or how many they are; R1 (equal mass per quantum) and R2 (one quantum per unit ball) imply E and are not needed. E with R3, for some length, is equivalent to the two shares $4/3$ and $8/(3\pi)$ together with the equality of the two thicknesses: with the length defined by the sheet towers' density against ours, the three-dimensional share is $4/3$ by that definition, and E's one condition across dimensions is the five-dimensional share. So the two premises are the closed form in other words. E can hold in one length only.

What the total rests on, on the stored edges: E, R3 (whose unit is E's length), P1 through the sourcing rule, P2 and P3 through the census, the single-ideal clause and the population of the odd towers; not R1 or R2, and not the democracy premise. It remains a fit: two shares against one measured remainder, with the relation found by solving for the value, the contact clauses and the single-ideal clause chosen with it known, and the population of the odd towers inferred from the remainder itself.

## lay
This rule says that there is one length at which a ball of that radius holds the same mass in every tower, each ball taken in that tower's own space, and it compares the resulting density with ours. Towers with fewer or more spatial dimensions then contribute different amounts, fixed by the volumes of balls in two, three and four dimensions. With the assumptions that the four odd hidden sectors hold matter and that two further sectors hold none, the rule gives a dark-to-ordinary matter ratio of about 5.364, the observed value. It no longer assumes that particles in different sectors weigh the same or are equally numerous: only the mass per ball matters. The price of that weaker assumption is plain to state: together with the assumption about how thick a slice counts, it holds exactly when the formula's two shares do, so it is the formula put as one rule and not a separate reason for it. The relation was found by solving for the measured value, and many equally simple formulas land inside the measurement's error, so the agreement is a fit rather than a prediction.

## one-liner
Under Premises E (equal mass per unit ball) and R3, with the odd towers populated and residues 0 and 4 empty (both registered premises), a tower with $D$-dimensional space has share $V_{3}/V_{D}$, and the dark-to-baryon ratio is $(11\pi + 16)/(3\pi) \approx 5.3643$, against the observed $5.364 \pm 0.065$; the quanta's masses and numbers do not enter, E with R3 is equivalent to the two shares, and the agreement is built in by fitting, not predicted.
