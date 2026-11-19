---
id: synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands
kind: claim
version: 2
title: 'The unit-ball clauses hold at one epoch unless the hidden direction co-expands'
status: proved
region: synthesis
subject: dark-matter
tags: [counting-rules, dark-matter-ratio, confronted-with-data]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Fable 5.2
  role: 'clause (v): the same test for Premise E'
  version: 2
  source: maintainer pass of 2026-11-19
amendments:
- version: 2
  kind: restatement
  defect: 'the statement tests R2 and R3 across epochs; since 19 November 2026 the total rests on Premise E in place of R1 and R2, and the statement did not say whether E holds at more than one epoch or what then fixes the thickness'
  evidence: check.py::check_premise_e_epoch
review: draft
derivations:
- name: main
  uses:
  - dark-matter.projection-every-towers-content-dilutes-ones@3
  - dark-matter.unit-ball-rule@6
  - dark-matter.thickness-not-gravitational-quantity@5
  - dark-matter.imported-inverse-square-law-short-range@1
  assumes:
  - dark-matter.e-equal-mass-per-unit-ball@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_unit_ball_clauses_epoch
- kind: check
  ref: check.py::check_premise_e_epoch
- kind: proof
  derivation: main
extraction:
  maintainer_pass_2026_11_19:
    by: maintainer-2026-11-19
    date: '2026-11-19'
    note: 'Version 1 -> 2. Leon''s decision of 19 November 2026: the total rests on Premise E (dark-matter.e-equal-mass-per-unit-ball) in place of R1 and R2. New clause (v) applies the same test to E: its length goes as a for the sheet towers and as b for the five-dimensional towers, so one length serves at more than one epoch exactly under co-expansion, and E by itself gives the counted thickness no value. Clauses (i) to (iv) are unchanged and remain statements about R2 and R3. One check function added, and an assumes edge to Premise E for clause (v).'
  open_problem: op.thickness-deposit-rule
  note: >-
    Adversarial consistency test of R2 and R3 across cosmic time, in the setting of the dilution
    lemma (dark-matter.projection-every-towers-content-dilutes-ones), which allows the extra
    direction to co-expand or to be static. Exact exponent bookkeeping (transport-absent). The
    observational remarks in the proof (the dust bound on dark matter's equation of state) are
    cited from memory and are not used by the statement. It bears on the problem's framing: unless
    co-expansion is a premise, the thickness is a property of the deposit, not of the sourcing rule.
---

## formal
Work in the setting of Lemma \claimref{dark-matter.projection-every-towers-content-dilutes-ones}: one shared scale factor $a$; a five-dimensional tower whose hidden direction has scale $b \propto a^{\beta}$ (the derived metric of the diagonal field $\hb^{-1}(e_{y}) = b\,e_{y}$, $\beta = 1$ co-expanding, $\beta = 0$ static), its quanta conserved and homogeneous along the hidden extent; a three-dimensional tower's sheets comoving, one per unit comoving length. Read R2 and R3 (Proposition \claimref{dark-matter.unit-ball-rule}) either as standing clauses, holding at every epoch with the current cell radii, or as deposit clauses, fixing the count once at the descent with the counted thickness thereafter comoving with $b$. Then:
\begin{enumerate}
\item[(i)] The ratio of a three-dimensional tower's cell radius to ours is constant in time for every $\beta$; that of a five-dimensional tower goes as $a^{(\beta - 1)/4}$. So R2's common radius holds at more than one epoch exactly when $\beta = 1$.
\item[(ii)] With R3 standing, the five-dimensional towers' projected density goes as $a^{-3(3 + \beta)/4}$, an effective equation of state $w = (\beta - 1)/4$ read from the dilution exponent (no pressure is derived): dust exactly when $\beta = 1$, and $w = -\tfrac14$ for a static hidden direction, where the five-dimensional share grows as $(1 + z)^{3/4}$ toward the present, by a factor between $189$ and $190$ from $1 + z = 1090$ and between $1.68$ and $1.69$ from $1 + z = 2$. At the unit-ball value (itself a fit to the observed ratio, Propositions \claimref{dark-matter.unit-ball-rule} and \claimref{dark-matter.status-rule}) these towers hold a fraction $16/(11\pi + 16)$, between $0.316$ and $0.317$, of the dark matter.
\item[(iii)] With R2 and R3 as deposit clauses the projected density is dust for every $\beta$ and the shares fixed at the descent persist.
\item[(iv)] For a static hidden direction under the deposit reading, the counted thickness today is the deposit-epoch cell radius, $d_{b,0}\,a_{\mathrm{dep}} \le d_{b,0}\,T_{0}/T_{\mathrm{desc}}$; for any descent above $1$ MeV it is below $2.4 \times 10^{-10}$ m, more than $10^{5}$ times under the $40$ micrometre bound of Fact \claimref{dark-matter.imported-inverse-square-law-short-range}. The step of Proposition \claimref{dark-matter.thickness-not-gravitational-quantity} that takes today's baryon spacing $d_{b} \approx 0.98$ m as the extent holds under co-expansion; under a static hidden direction the relevant thickness is this deposit-epoch length.
\item[(v)] \emph{(Premise E.)} With Premise E (\claimref{dark-matter.e-equal-mass-per-unit-ball}) in place of R1 and R2 the test gives the same answer. The length at which a three-dimensional tower and this world hold equal mass per ball goes as $a$ for every $\beta$, and the length at which a five-dimensional tower and this world do goes as $b$. So E holds in one length at more than one epoch exactly when $\beta = 1$, and that length is then comoving; for $\beta \neq 1$ E with R3 is a deposit clause, and (iii) holds for it. Clause (iv) does not carry over: it takes the deposit-epoch cell radius from R2, and E by itself gives the counted thickness no value.
\end{enumerate}
So R2 and R3 can be standing clauses only with a co-expanding hidden direction, a direction the four-dimensional metric does not see (Proposition \claimref{dark-matter.thickness-not-gravitational-quantity}), so nothing in the sourcing rule makes it co-expand. Without that premise, R3 is a rule for the descent's deposit, as the open problem frames it, and its value is set at the deposit epoch.

## technical
Follow each tower's cell radius through the expansion. A sheet tower's own two-dimensional density falls as $a^{-2}$, so its cell radius grows as $a$, like ours, and its sheets, comoving, stay one radius apart: for the three-dimensional towers R2 and R3 are automatically epoch-independent. A five-dimensional tower's own four-dimensional density falls as $(a^{3}b)^{-1}$; with the hidden scale $b \propto a^{\beta}$ its cell radius grows as $a^{(3+\beta)/4}$, so its ratio to ours is constant only for $\beta = 1$. If R3 is a standing clause, counting through the current cell radius, the projected density goes as $a^{-3(3+\beta)/4}$, an effective equation of state $w = (\beta - 1)/4$, which is $-\tfrac14$ for a static hidden direction: the five-dimensional share would grow by $(1+z)^{3/4}$, about $190$ since last scattering. If R2 and R3 fix the count at the deposit, everything dilutes as dust whatever $\beta$ is.

So either the hidden direction co-expands with ours, which the four-dimensional metric does not drive and which would be a further premise, or R2 and R3 are statements about the deposit epoch. In the second case the counted thickness today is the deposit-epoch cell radius, below $2.4 \times 10^{-10}$ m for any descent above $1$ MeV, so the argument that compares today's baryon spacing ($0.98$ m) with short-range tests of gravity applies only under co-expansion.

The same test applies to Premise E, which since 19 November 2026 takes the place of R1 and R2 under the total: the length at which a sheet tower and this world hold equal mass per ball goes as $a$, and the one for a five-dimensional tower goes as $b$, so E holds in one length at more than one epoch only under co-expansion. E by itself gives that length no value; the deposit-epoch figure above uses R2.

## lay
The dark-matter formula counts hidden matter in "cells" whose size is tied to the spacing of ordinary matter. This result follows those cells through the expansion of the universe. For the hidden sectors with fewer dimensions than ours the rule keeps working automatically. For those with an extra dimension it keeps working only if that extra dimension stretches exactly as ours does; if it does not stretch, then either that dark matter would thin out unlike ordinary matter, growing in relative amount by a factor of nearly two hundred since the early universe, which is not what is seen, or the rule describes only the moment the matter was laid down. In that second case the thickness in the formula is a microscopic length from the birth of the universe, not today's one metre. The same holds when the formula is stated with equal mass per ball in place of the two assumptions about particles; that weaker assumption does not say how long the length in the formula is.

## one-liner
R2 and R3 hold at more than one epoch only if the five-dimensional towers' hidden direction co-expands with ours; otherwise they are deposit clauses (a standing R3 would give 31.6 percent of the dark matter, at the fitted unit-ball value, an effective equation of state w = -1/4), and the counted thickness today is the deposit-epoch cell radius, below 2.4e-10 m for any descent above 1 MeV. The same holds for Premise E in place of R1 and R2, which by itself gives the thickness no value.
