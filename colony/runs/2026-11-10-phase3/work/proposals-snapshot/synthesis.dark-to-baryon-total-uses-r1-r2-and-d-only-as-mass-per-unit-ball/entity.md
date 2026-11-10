---
id: synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball
kind: claim
version: 1
title: 'The dark-to-baryon total uses R1, R2 and democracy only as mass per unit ball'
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
review: draft
derivations:
- name: main
  uses:
  - dark-matter.unit-ball-rule@5
  - dark-matter.total-function-thickness@5
  - dark-matter.democracy-de-sitter-radius-unit-ball@4
  - dark-matter.population-count-one-share-half-percent@6
  - dark-matter.mirror-share-one-how-fragile@7
  - dark-matter.projection-every-towers-content-dilutes-ones@3
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
  open_problem: op.thickness-deposit-rule
  note: >-
    A premise reduction, not a derivation of the ratio: it says which of the dark-matter postulates the stored total
    uses and in what combination. Overlap with stored results, cited and not re-proved: the closed form is
    dark-matter.unit-ball-rule; the family in the thickness is dark-matter.total-function-thickness and
    synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3 (whose clause (i) is the independence of R3); that the
    ball and sphere forms are one relation is recorded in dark-matter.status-rule (iii) and in the note
    note.dark-matter.equivalent-forms-assignment-not (the hat-box identity). What is added: that R1 and R2 enter
    every share only through their product, with a model in which both fail and every share is kept; that the
    democracy premise is that product law in the unit of the de Sitter radius, and that neither it nor the pair
    R1, R2 implies the other; that the mirror's term is obtained twice, from disjoint sets of dark-matter premises,
    which disagree by one part in two hundred on the burning branch; and the audit of clause (v). The audit was
    read from the dependence edges (uses, assumes, founded_on, specialises, derived_from) of the built graph at the
    pinned versions; it is a statement about what the store records, labelled audited, not proved, and it does not
    cover conditions that the store holds only as text (the costed single-ideal clause and the inference that all
    six towers are populated, both named in clause (v)).
---

## formal
\emph{Setting.} Under the representatives of Premise \claimref{dark-matter.p3-nearest-dimension-representatives} the populated towers have space dimension $D_{r} = 3$ for this world ($r = 6$) and the mirror ($r = 2$), $D_{r} = 2$ for $r = 1, 7$ and $D_{r} = 4$ for $r = 3, 5$. A \emph{filling} gives each of them a quantum mass $m_{r} > 0$ and a number $\nu_{r} > 0$ of quanta per unit volume of its own space, in one unit of length $d$. The stored sourcing rule (Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones}), read with a length $\lambda d$ of the extra direction of a five-dimensional tower and with a three-dimensional tower's sheets $\mu d$ apart, gives the shares and the total
\[
f_{r} \;=\; \frac{m_{r}\nu_{r}}{m_{6}\nu_{6}} \times
\begin{cases} \lambda d & D_{r} = 4, \\ 1 & D_{r} = 3, \\ 1/(\mu d) & D_{r} = 2, \end{cases}
\qquad
T \;=\; \sum_{r \neq 6} f_{r} .
\]
Premise R1 (\claimref{dark-matter.r1-equal-mass-per-quantum}) is $m_{r} = m$ for all $r$; R2 (\claimref{dark-matter.r2-one-quantum-per-unit-ball}) is $\nu_{r} V_{D_{r}} d^{D_{r}} = 1$, with $V_{D}$ the volume of the unit ball $\B^{D}$; R3 (\claimref{dark-matter.r3-one-cell-per-unshared-direction}) is $\lambda = \mu = 1$. Write (E), \emph{equal mass per unit ball}, for the statement that $m_{r}\nu_{r}V_{D_{r}}d^{D_{r}}$ takes one value on all populated towers.
\begin{enumerate}
\item[(i)] \emph{(One density law; proved.)} R1 and R2 together imply (E). Under (E) and R3, $f_{r} = V_{3}/V_{D_{r}}$ and $T = (11\pi + 16)/3\pi$, the total of Proposition \claimref{dark-matter.unit-ball-rule}; with the thicknesses free, $T = 1 + 8/3\mu + 16\lambda/3\pi$ as in Proposition \claimref{dark-matter.total-function-thickness}. (E) implies neither R1 nor R2: for positive numbers $s_{r}$, not all equal, the filling $m_{r} = s_{r}m$, $\nu_{r} = 1/(s_{r}V_{D_{r}}d^{D_{r}})$ satisfies (E), violates R1 and R2, and has every share and the total unchanged. So every share, and the total, depends on R1 and R2 only through (E). The stored results that use R1 or R2 separately (the common mass and the cell radius in the cluster bound, R2's number density in the odd towers' population and survival) are not statements of the total.
\item[(ii)] \emph{(Democracy of the total mass; proved, given the reading of the stored sphere form.)} Read a tower's mass per unit measure of its Euclidean de Sitter sphere $\Sph^{D_{r}+1}$ as its mass per unit volume of its space divided by one length common to all towers, as the stored sphere form does. Then the total mass of tower $r$ on the sphere of radius $\ell$ is a common factor times $m_{r}\nu_{r}V_{D_{r}}\ell^{D_{r}}$, by $|\Sph^{D+1}| = 2\pi V_{D}$. Hence the democracy premise (\claimref{dark-matter.d-democracy-total-mass}) is (E) with the unit of length set to the de Sitter radius, $d = \ell$, and with the thickness in the same unit it gives the same shares (Proposition \claimref{dark-matter.democracy-de-sitter-radius-unit-ball}); the shares do not depend on the unit, since $d$ cancels in $f_{r}$ under (E). Neither implies the other: the democracy premise leaves $m_{r}$ and $\nu_{r}$ separately free, and under R1 and R2 at $d \neq \ell$ the total masses are in the ratio $(\ell/d)^{D_{r}}$, unequal across dimensions. For the total, R1, R2 and the democracy premise supply one premise, (E).
\item[(iii)] \emph{(The mirror's term is obtained twice; the premise sets are audited.)} At $D_{r} = 3$, (E) gives $f_{2} = 1$ with no further premise. Proposition \claimref{dark-matter.population-count-one-share-half-percent}(i) gives $f_{2} = 1$ from Premises P1, P2, the common ceiling coupling and the copy of content, with P4 discharged for the mirror, and without R1, R2 or R3. So restricted to the reversal pair $\{2, 6\}$, (E) is a consequence of the population count, and it is a premise only on the four odd towers. The two derivations agree exactly on the proton-only branch; on the burning branch of Proposition \claimref{dark-matter.mirror-share-one-how-fragile}(i) the population count gives $f_{2} = 199/200$ (the stored $0.995$), so R1 read as equal mean mass per baryon fails there by one part in two hundred and the total is $(11\pi + 16)/3\pi - 1/200$; both values lie within one standard deviation ($0.065$) of the record's $5.364$.
\item[(iv)] \emph{(What still moves the total; proved.)} With (E) kept: thicknesses $(\lambda, \mu) = (2, 1)$ and $(1, 2)$ give $11/3 + 32/3\pi$ and $7/3 + 16/3\pi$, each more than five standard deviations from the record; one quantum per cube of side $2d$ in place of the unit ball, with thickness one side, gives exactly $5$, more than five standard deviations below; a three-dimensional tower read at $D_{r} = 4$ gives $7/3 + 8/\pi$. So R3, the shape of the cell in (E) and the dimensions of P3 are each used.
\item[(v)] \emph{(Count; audited on the stored dependence edges.)} Of the twenty-three postulates of the dark-matter subject, the past cone of Proposition \claimref{dark-matter.unit-ball-rule} contains five: P2, P3, R1, R2, R3. The past cone of Proposition \claimref{dark-matter.total-function-thickness}, which takes the mirror's term from the population count, contains seven, P1, P2, P3, P4, R1, R2 and the common ceiling coupling, and the stored total adds R3 as the choice $\lambda = \mu = 1$: eight. These eight are also the union over the stored statements of the total (the two above and the restatements \claimref{dark-tower-matter.imported-unit-ball-rule} and \claimref{simulations.imported-unit-ball-rule-family}). Of the other fifteen, four lie under stored results that vary the conditions of the total and under no statement of it: P5 (\claimref{synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3}), H1 (\claimref{synthesis.lowest-causal-residues-zero-four-content}), and H1, H2 and Premise U (\claimref{synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free}); the democracy premise lies under the two results on the de Sitter reading, which give other totals; the remaining ten (CPT covariance, the flag as datum, Hypothesis (S) carried to every tower, the six modelling premises of the cluster simulations and the registered asymmetry) lie under no stored result whose text contains the value $5.364$ or its closed form. By (i) to (iii) the eight reduce, for the total, to: P3 for the dimensions; (E) on the four odd towers; R3; and for the mirror's term either (E) on the reversal pair or P1, P2 and the common ceiling coupling. Two conditions of the total are stored as text and not as postulates: the costed single-ideal clause and the inference that all six towers are populated (Observation \claimref{dark-matter.status-rule}(vi), Observation \claimref{dark-matter.which-towers-are-populated}). The total remains a fit: (E) and R3 fix the two odd shares $4/3$ and $8/3\pi$ against one measured number.
\end{enumerate}

## technical
The stored total of dark to baryonic matter is a sum of shares, each the ratio of a tower's mass density, read per unit of this world's volume, to ours. A mass density is a quantum mass times a number density, so the shares see R1 (equal quantum masses) and R2 (one quantum per unit ball) only through their product: equal mass per unit ball, called (E) here. A filling in which each tower's quanta are heavier by its own factor and rarer by the same factor violates both R1 and R2 and has the same shares. The democracy premise, equal total mass on each tower's de Sitter sphere, is the same law (E) with the unit of length set to the de Sitter radius, by the identity $|\Sph^{D+1}| = 2\pi V_{D}$ and given the stored reading of the sphere form; the shares do not depend on the unit, so for the total the three postulates supply one premise, although none of them follows from the others as a statement. The mirror's share of one is obtained twice: from (E) at dimension three, and from the population count under P1, P2 and the common ceiling coupling, with no premise of the dark-matter subject in common. On the burning branch the second gives $0.995$, so the two disagree there by half a percent, inside the error bar. The thickness R3, the ball shape of the cell and the dimensions of P3 each move the total when changed. On the stored dependence edges, five of the subject's twenty-three postulates lie under the closed form and eight under the total with the mirror's term taken from the population count; fifteen lie under no stored statement of the total (four of them under results that vary its conditions).

## lay
The series fits the measured ratio of dark matter to ordinary matter, 5.364, with a rule built on several assumptions. This result sorts out which assumptions the number really uses. Two of them, that all hidden worlds have quanta of the same mass and that each holds one quantum per unit ball, matter for the number only through their product, the mass per unit ball; a third assumption, equal total mass in every world, is the same statement in other units, given the stored reading of it. The share of the mirror world is derived twice, by two unrelated routes that agree to within half a percent. Of the twenty-three assumptions filed under dark matter, at most eight stand under the number, and fifteen serve other results. Assuming all of this, the ratio is still fitted, not predicted: two shares are chosen and one number is matched.

## one-liner
Under the stored sourcing rule, every share of the dark-to-baryon total depends on R1 and R2 only through equal mass per unit ball (E); the democracy premise is (E) in the unit of the de Sitter radius, given the stored sphere reading; the mirror's term follows twice, from (E) or from P1, P2 and the common ceiling; five of the subject's twenty-three postulates lie under the closed form, eight under the total, and it remains a fit.
