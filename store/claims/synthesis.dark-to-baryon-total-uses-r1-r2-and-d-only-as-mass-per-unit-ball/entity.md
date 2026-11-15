---
id: synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball
kind: claim
version: 2
title: 'Dark-to-baryon total uses R1, R2 only as mass per unit ball at a fixed common thickness'
status: proved
region: synthesis
subject: dark-matter
tags: [dark-matter-ratio, counting-rules, finite-models]
proposed_by:
  kind: ai
  session: 2026-11-10-phase3
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase3
- name: Claude Fable 5.2
  role: 'two stale sentences corrected (the reading of R3; the retired P4)'
  version: 2
  source: 'maintainer pass of 2026-11-11 (run 2026-11-11-contradictions)'
amendments:
- version: 2
  kind: restatement
  defect: 'clause (i) said the stored wording of R3 does not choose between the two readings, against the Status paragraph of the same result and R3 version 2; the model was called a model of the retired premise P4'
review: draft
derivations:
- name: main
  uses:
  - dark-matter.unit-ball-rule@6
  - dark-matter.total-function-thickness@6
  - dark-matter.democracy-de-sitter-radius-unit-ball@5
  - dark-matter.population-count-one-share-half-percent@7
  - dark-matter.mirror-share-one-how-fragile@8
  - dark-matter.projection-every-towers-content-dilutes-ones@3
  assumes:
  - dark-matter.odd-towers-populated@1
  - dark-matter.p1-single-frozen-point@3
  - dark-matter.single-ideal-at-residues-zero-and-four@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_total_depends_on_mass_times_number_only
- kind: check
  ref: check.py::check_sphere_law_is_the_ball_law_and_fixes_the_unit
- kind: check
  ref: check.py::check_mirror_term_is_obtained_twice
- kind: check
  ref: check.py::check_each_remaining_premise_moves_the_total
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - dark-matter.r1-equal-mass-per-quantum
  - dark-matter.r2-one-quantum-per-unit-ball
  - dark-matter.d-democracy-total-mass
  - dark-matter.status-rule
  - synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3
extraction:
  maintainer_pass_2026_11_12:
    by: maintainer-2026-11-12
    date: '2026-11-12'
    note: 'Scope note, version kept, no statement changed (Leon''s decision of 12 November 2026: the inherited charge is B - L). Where the text says that the population count gives f_2 = 1 from P1, P2, the common ceiling coupling and the copy of content, read: and under the hypothesis of equal conversion (the mirror''s ratio of baryon number to B - L equals this tower''s; not shown; attack item (d) of op.matter-asymmetry-origin; Proposition dark-matter.stored-asymmetry-charge-not-number (i), version 11). The dependence of the total on R1, R2 and d shown here is unchanged; the mirror''s unit of the total 5.364 is conditional on the hypothesis.'
  maintainer_pass_2026_11_11:
    by: maintainer-2026-11-11
    date: '2026-11-11'
    note: 'Version 1 -> 2. Two sentences of the formal level corrected; no clause changes. Not split, by Leon''s decision of 11 November 2026: the result is an audit setting the two readings side by side, and Premise D''s note names it as the exception.'
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'No version change requested (edges, citations and a status sentence only). Leon''s decisions 5, 9 and 10 of 10 November 2026. Assumes edges drawn, as this note asked: P1 (through the sourcing rule) and the two newly registered postulates, the single-ideal clause and the population of the odd towers. Decision 9 fixes R3''s unit as each tower''s own cell radius, so the fixed-common-length reading under which clause (i) holds is not adopted; every level now ends with the same sentence saying so. The counts of clause (v) are left as audited at the pinned versions; since then P4 is retired as a postulate and two postulates are registered, so the subject has twenty-four postulates and the closed form''s cone holds R1, R2, R3, P1, P2, P3 and the two new ones.'
  open_problem: op.thickness-deposit-rule
  note: >-
    A premise reduction, not a derivation of the ratio: it says which of the dark-matter postulates the stored total
    uses and in what combination, under one stated reading of R3. The reading: R3's thickness is one fixed length d
    common to all towers, the length in which the density law (E_d) is written, held fixed when the filling is varied. The store's
    wording of R3 is "one cell radius", and under R2 the two readings coincide; when R2 is varied they differ, and
    under the own-cell-radius reading clause (i) fails (alternative stated in (i), tested in the check). R3 version
    1 does not say whose cell radius its unit is when R2 is varied. Overlap with stored results, cited and not
    re-proved: the closed form is dark-matter.unit-ball-rule; the family in the thickness is
    dark-matter.total-function-thickness and synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3 (whose clause
    (i) is the independence of R3); that the ball and sphere forms are one relation is recorded in
    dark-matter.status-rule (iii), in dark-matter.democracy-de-sitter-radius-unit-ball and in the note
    note.dark-matter.equivalent-forms-assignment-not (the hat-box identity; "R2 is equivalent to one quantum per
    unit sphere"). What is added: the product observation with its model, under the stated reading; that the
    democracy premise and the pair R1, R2 do not imply each other; that the mirror's term is obtained twice, by
    derivations that share P1 (through the sourcing rule), P2 and P3 among the subject's premises and differ by
    about one part in two hundred on the burning branch; and the audit of clause (v). The audit was read from the
    dependence edges (uses, assumes, founded_on, specialises, derived_from) of the built graph at the pinned
    versions, and the stored statements of the total were found by a text pattern (the value and the closed form),
    which misses statements by reference; one such was added by hand
    (dark-matter.democracy-de-sitter-radius-unit-ball) and others may exist: the audit is labelled audited on that
    search, not proved. Premises used, assumes edge for the maintainer: the stored sourcing rule rests on P1
    (dark-matter.p1-single-frozen-point), which the closed form's stored edges do not record; and the two
    conditions of the closed form that the store holds as text and that are to be registered as postulates, the
    single-ideal clause at residues 0 and 4 (dark-matter.status-rule (vi)) and the population of the odd towers
    (dark-matter.which-towers-are-populated), named as conditions in the Setting and in clause (v). No assumes edge
    is drawn here.
---

## formal
\emph{Setting and conditions.} Assume the representatives of Premise \claimref{dark-matter.p3-nearest-dimension-representatives}, so that the towers that admit matter have space dimension $D_{r} = 3$ for this world ($r = 6$) and the mirror ($r = 2$), $D_{r} = 2$ for $r = 1, 7$ and $D_{r} = 4$ for $r = 3, 5$; assume, as the stored total does, that all six are populated (Observation \claimref{dark-matter.which-towers-are-populated}) and that residues $0$ and $4$ are empty (the single-ideal clause, Observation \claimref{dark-matter.status-rule}(vi)); and assume the stored sourcing rule (Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones}, which rests on Premise P1, \claimref{dark-matter.p1-single-frozen-point}). A \emph{filling} gives each populated tower a quantum mass $m_{r} > 0$ and a number $\nu_{r} > 0$ of quanta per unit volume of its own space. Fix one length $d$, common to all towers and independent of the filling. With the sourcing rule read through a length $\lambda d$ of the extra direction of a five-dimensional tower and with a three-dimensional tower's sheets $\mu d$ apart, the shares and the total are
\[
f_{r} \;=\; \frac{m_{r}\nu_{r}}{m_{6}\nu_{6}} \times
\begin{cases} \lambda d & D_{r} = 4, \\ 1 & D_{r} = 3, \\ 1/(\mu d) & D_{r} = 2, \end{cases}
\qquad
T \;=\; \sum_{r \neq 6} f_{r} .
\]
Premise R1 (\claimref{dark-matter.r1-equal-mass-per-quantum}) is $m_{r} = m$ for all $r$; R2 (\claimref{dark-matter.r2-one-quantum-per-unit-ball}) is $\nu_{r} V_{D_{r}} d^{D_{r}} = 1$, with $V_{D}$ the volume of the unit ball $\B^{D}$. \emph{Reading of R3.} R3 (\claimref{dark-matter.r3-one-cell-per-unshared-direction}) says ``one cell radius''. It is read here as $\lambda = \mu = 1$ in the fixed length $d$, not in each tower's own cell radius $a_{r}$, defined by $\nu_{r}V_{D_{r}}a_{r}^{D_{r}} = 1$. Under R2 the two readings coincide ($a_{r} = d$); they differ as soon as R2 is varied. Premise R3 as now stated chooses the second, each tower's own cell radius (the Status paragraph below); clause (i) is a statement about the first. Write $(\mathrm{E}_{d})$, \emph{equal mass per ball of radius $d$}, for the statement that $m_{r}\nu_{r}V_{D_{r}}d^{D_{r}}$ takes one value on all populated towers.
\begin{enumerate}
\item[(i)] \emph{(One density law; proved, under the fixed-length reading of R3.)} R1 and R2 together imply $(\mathrm{E}_{d})$. Under $(\mathrm{E}_{d})$ and R3 so read, $f_{r} = V_{3}/V_{D_{r}}$ and $T = (11\pi + 16)/3\pi$, the total of Proposition \claimref{dark-matter.unit-ball-rule}; with the thicknesses free, $T = 1 + 8/3\mu + 16\lambda/3\pi$, as in Proposition \claimref{dark-matter.total-function-thickness}. $(\mathrm{E}_{d})$ implies neither R1 nor R2: for positive numbers $s_{r}$ that are constant on the reversal orbits, with $s_{2} = s_{6} = 1$ and $s_{1} = s_{7}$, $s_{3} = s_{5}$ not both $1$, the filling $m_{r} = s_{r}m$, $\nu_{r} = 1/(s_{r}V_{D_{r}}d^{D_{r}})$ satisfies $(\mathrm{E}_{d})$, violates R1 and R2, and has every share and the total unchanged. It leaves the mirror pair as the population count has it and keeps every equality along the reversal orbits, so it is a model of P1, P2, P3, the common ceiling coupling and R3 in the fixed-length reading (argued for P2: the model equates along the orbits whatever counts as a sector label). So, under that reading, every share depends on R1 and R2 only through $(\mathrm{E}_{d})$. \emph{Under the other reading this fails.} If the thickness is one own cell radius $a_{r}$, then
\[
f_{r} \;=\; \frac{m_{r}}{m_{6}}\,\frac{V_{3}}{V_{D_{r}}}\,\Bigl(\frac{a_{6}}{a_{r}}\Bigr)^{3},
\]
which $(\mathrm{E}_{d})$ does not fix: with $s_{3} = s_{5} = 16$ and $s_{r} = 1$ elsewhere, $(\mathrm{E}_{d})$ holds and the total is $11/3 + 32/3\pi \approx 7.06$. On that reading R2 is used twice, once in the density and once to supply R3's unit, and the shares depend on $m_{r}/a_{r}^{3}$. The stored results that use R1 or R2 separately (the common mass and the cell radius in the cluster bound, R2's number density in the odd towers' population and survival) are not statements of the total.
\item[(ii)] \emph{(Democracy of the total mass; proved, given the reading of the stored sphere form.)} Read a tower's mass per unit measure of its Euclidean de Sitter sphere $\Sph^{D_{r}+1}$ as its mass per unit volume of its space divided by one length common to all towers, as the stored sphere form does. Then the total mass of tower $r$ on the sphere of radius $\ell$ is a common factor times $m_{r}\nu_{r}V_{D_{r}}\ell^{D_{r}}$, by $|\Sph^{D+1}| = 2\pi V_{D}$. Hence the democracy premise (\claimref{dark-matter.d-democracy-total-mass}) is $(\mathrm{E}_{\ell})$, the same kind of law at the de Sitter radius, and with the thickness $\ell$ it gives the same shares (Proposition \claimref{dark-matter.democracy-de-sitter-radius-unit-ball}). The law and the thickness are tied through one length: $(\mathrm{E}_{d})$ with thickness $d'$ gives $V_{3}/V_{D_{r}} \times (d'/d)^{D_{r}-3}$. $(\mathrm{E}_{d})$ and $(\mathrm{E}_{\ell})$ are different statements for $d \neq \ell$ and neither implies the other: under R1 and R2 in the length $d$ the total masses on the spheres are in the ratio $(\ell/d)^{D_{r}}$, unequal across dimensions, and the democracy premise leaves $m_{r}$ and $\nu_{r}$ separately free.
\item[(iii)] \emph{(The mirror's term is obtained twice; the premise sets are audited.)} At $D_{r} = 3$, $(\mathrm{E}_{d})$ gives $f_{2} = 1$ through the sourcing rule. Proposition \claimref{dark-matter.population-count-one-share-half-percent}(i) gives $f_{2} = 1$ from Premises P1, P2, the common ceiling coupling and the copy of content, with P4 discharged for the mirror, and without R1, R2 or R3. The two derivations share P1 (through the sourcing rule), P2 and P3 among the subject's postulates; the first does not have P4 or the common ceiling coupling under it, the second not R1, R2 or R3. So restricted to the reversal pair $\{2, 6\}$, $(\mathrm{E}_{d})$ is a consequence of the population count, and it is a premise only on the four odd towers. The two agree exactly on the proton-only branch; on the burning branch of Proposition \claimref{dark-matter.mirror-share-one-how-fragile}(i) the population count gives $f_{2} = 931.8/936.7 \approx 0.9948$ (the stored $0.995$), so R1 read as equal mean mass per baryon fails there by about one part in two hundred and the total is smaller by about $1/200$; both values lie within one standard deviation ($0.065$) of the record's $5.364$.
\item[(iv)] \emph{(What still moves the total; proved.)} With $(\mathrm{E}_{d})$ kept: thicknesses $(\lambda, \mu) = (2, 1)$ and $(1, 2)$ give $11/3 + 32/3\pi$ and $7/3 + 16/3\pi$, each more than five standard deviations from the record; one quantum per cube of side $2d$ in place of the ball, with thickness one side, gives exactly $5$, more than five standard deviations below; a three-dimensional tower read at $D_{r} = 4$ gives $7/3 + 8/\pi$. So R3, the shape of the cell and the dimensions of P3 are each used.
\item[(v)] \emph{(Count; audited on the stored dependence edges and a text search.)} Among the twenty-three postulates of the dark-matter subject: the past cone of Proposition \claimref{dark-matter.unit-ball-rule} contains five on its stored edges, P2, P3, R1, R2, R3, and six with P1, which enters through the sourcing rule that the proposition's proof uses and its edges do not record. The past cone of Proposition \claimref{dark-matter.total-function-thickness}, which takes the mirror's term from the population count, contains seven, P1, P2, P3, P4, R1, R2 and the common ceiling coupling, and eight with R3 as the choice $\lambda = \mu = 1$; the restatements \claimref{dark-tower-matter.imported-unit-ball-rule} and \claimref{simulations.imported-unit-ball-rule-family} have the same five and eight. A third stored statement of the same total, Proposition \claimref{dark-matter.democracy-de-sitter-radius-unit-ball}, has the democracy premise and R3. The union over these stored statements of the total is nine; fourteen of the twenty-three lie under none of them. Of the fourteen, four lie under stored results that vary the conditions of the total: P5 (\claimref{synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3}), H1 (\claimref{synthesis.lowest-causal-residues-zero-four-content}), and H1, H2 and Premise U (\claimref{synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free}); the remaining ten (CPT covariance, the flag as datum, Hypothesis (S) carried to every tower, the six modelling premises of the cluster simulations and the registered asymmetry) lie under no stored result whose text contains the value $5.364$ or its closed form. The statements of the total were found by that text pattern, which misses statements by reference (the third above was added by hand), so ``under none'' is audited on the search, not proved. The cones also contain postulates of other subjects: under the closed form the four foundation premises (\claimref{synthesis.premise-the-bit}, \claimref{synthesis.premise-minimal-non-commutativity}, \claimref{synthesis.premise-superposition-over-the-integers}, \claimref{synthesis.continuum-completion-premise}); the population-count route adds \claimref{dark-matter.hyp-u-equal-rank-one-eigenvalues} (subject neutrinos), \claimref{scrambling.indifference-structural-premise-series}, \claimref{sheaf.tameness}, \claimref{singularity.q-joint-quasi-freeness-s-wave} and \claimref{standard-model.slot-module-hypothesis}. Three conditions of the closed form are held as text and not as edges: the sourcing rule with P1, the single-ideal clause and the population of the odd towers. By (i) to (iii), under the fixed-length reading, the subject's premises of the total reduce to: P1 for the sourcing rule; P3 for the dimensions; $(\mathrm{E}_{d})$ on the four odd towers; R3; and for the mirror's term either $(\mathrm{E}_{d})$ on the reversal pair or P2 and the common ceiling coupling. The total remains a fit: $(\mathrm{E}_{d})$ and R3 fix the two odd shares $4/3$ and $8/3\pi$ against one measured number.
\end{enumerate}

\emph{Status of the reading.} This reading is not adopted: by Premise R3 as now stated the unit of thickness is each tower's own cell radius, so R2 also supplies R3's unit and stays a premise of the total, and the result holds only in the fixed-common-length reading. (Premise \claimref{dark-matter.r3-one-cell-per-unshared-direction}.) The premises used and held as text when this result was written are now edges: P1 (\claimref{dark-matter.p1-single-frozen-point}) for the sourcing rule, the single-ideal clause (\claimref{dark-matter.single-ideal-at-residues-zero-and-four}) and the population of the odd towers (\claimref{dark-matter.odd-towers-populated}). The counts of clause (v) are those of the stored edges at the pinned versions, before these two premises were registered and before Premise P4 was retired as a postulate.

## technical
The stored total of dark to baryonic matter is a sum of shares, each the ratio of a tower's mass density, read per unit of this world's volume by the sourcing rule (which rests on P1), to ours. Assume the counted thickness of R3 is one fixed length common to all towers, the length in which the cell of R2 is measured, and not each tower's own cell radius; under R2 the two are the same, and the store's wording, one cell radius, does not say which is meant when R2 is varied. Under that reading a share sees R1 (equal quantum masses) and R2 (one quantum per unit ball) only through their product, equal mass per ball of that radius: a filling in which the odd towers' quanta are heavier by a factor and rarer by the same factor violates both and has the same shares. Under the other reading the statement fails: the same kind of filling, with the five-dimensional towers' quanta sixteen times heavier and rarer, moves the total to about $7.06$. The democracy premise, equal total mass on each tower's de Sitter sphere, is the same kind of law at the de Sitter radius, by $|\Sph^{D+1}| = 2\pi V_{D}$ and given the stored reading of the sphere form; with the thickness equal to that radius it gives the same shares, and neither law implies the other. The mirror's share of one is obtained twice: from the density law at dimension three, and from the population count under P1, P2 and the common ceiling coupling; the two share P1, P2 and P3 among the subject's premises. On the burning branch the second gives about $0.995$, so they disagree there by about half a percent, inside the error bar. The thickness, the ball shape of the cell and the dimensions of P3 each move the total when changed. On the stored dependence edges, five of the subject's twenty-three postulates lie under the closed form (six with P1, held for it as text), eight under the total with the mirror's term taken from the population count, and the democracy premise with R3 under a third stored statement; fourteen lie under no stored statement of the total found by the search, four of them under results that vary its conditions. The cones also hold the four foundation premises and five postulates of other subjects, and the closed form assumes, as text, that the odd towers are populated and that residues $0$ and $4$ are empty. The total remains a fit.

Status of the reading. This reading is not adopted: by Premise R3 as now stated the unit of thickness is each tower's own cell radius, so R2 also supplies R3's unit and stays a premise of the total, and the result holds only in the fixed-common-length reading.

## lay
The series fits the measured ratio of dark matter to ordinary matter, 5.364, with a rule built on several assumptions. This result sorts out which assumptions the number uses. Two of them, that all hidden worlds have quanta of the same mass and that each holds one quantum per unit ball, matter for the number only through their product, the mass per unit ball, as long as the counted thickness is a fixed common length; if the thickness is instead each world's own spacing, this is no longer true and the same change of filling moves the number to about 7. A third assumption, equal total mass in every world, is the same kind of law with a cosmic unit of length, and gives the same shares given the stored reading of it. The share of the mirror world is derived twice, by two routes that agree to within about half a percent. Of the twenty-three assumptions filed under dark matter, at most eight stand under the number on either route, besides the series' foundation premises and five assumptions filed elsewhere, and assuming also that the hidden worlds are populated as the rule supposes. Under all of this the ratio is still fitted, not predicted: two shares are chosen and one number is matched. The series does not adopt that reading: it takes the counted thickness to be each world's own spacing, so the statement above holds only in a reading the series does not use.

## one-liner
Under the stored sourcing rule, and given R3's thickness read as one fixed common length $d$ (not each tower's own cell radius, where the claim fails and the same refilling gives $7.06$), every share of the dark-to-baryon total depends on R1 and R2 only through equal mass per ball of radius $d$; the democracy premise is that law at the de Sitter radius, given the stored sphere reading; the mirror's term follows twice; five (six with P1) of the subject's twenty-three postulates lie under the closed form, eight under the population-count route, and the total remains a fit. This reading is not adopted: by Premise R3 as now stated the unit of thickness is each tower's own cell radius, so R2 also supplies R3's unit and stays a premise of the total, and the result holds only in the fixed-common-length reading.
