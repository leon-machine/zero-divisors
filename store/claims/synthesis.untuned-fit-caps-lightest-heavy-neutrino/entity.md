---
id: synthesis.untuned-fit-caps-lightest-heavy-neutrino
kind: claim
version: 1
title: 'The untuned fit caps the lightest heavy neutrino'
status: proved
region: synthesis
subject: neutrinos
tags: [seesaw-and-majorana, matter-asymmetry, running-and-unification]
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
review: draft
derivations:
- name: main
  uses:
  - standard-model.fits-record-level@6
  - standard-model.chain@8
  - dark-matter.imported-massless-graviton-production-rate@3
  assumes:
  - neutrino.r-descent-reheats-below-lower-heavy@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_untuned_fit_caps_lightest_heavy_neutrino
- kind: proof
  derivation: main
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.imported-massless-graviton-production-rate repinned 1 -> 2 after reviewing the F14 change writing the rate with the reduced Planck mass bar M_P, the source''s M_P (any M_P here that is evaluated is 2.435e18 GeV, the reduced mass); the use here holds as cited.'
  open_problem: op.pre-descent-theory
  note: >-
    Filed alongside synthesis.seeding-remainder-excludes-perturbative-pati-salam. Kept separate
    because the Standard-Model paper's fits rest on Premise (EW), which the store records as
    contradicting Hypothesis (U), used in that proposal's clauses (ii) and (iii) (its clause (i) does
    not use (U)), and because the stored dark-matter claims that carry the seeding yield, the remainder
    and the coefficients rest on (U) through the ceiling range. Here no perturbativity bound and no (U)
    enters: a norm inequality on the seesaw and the largest Dirac entry of one representative fit
    bound the lightest heavy neutrino mass. The fit's Dirac entries (0.04 GeV) lie inside the chain's
    perturbative range (m_D < 5.2 GeV), so the two results agree. Premise (R) of T15
    (neutrino.r-descent-reheats-below-lower-heavy) is recorded as an assumes edge, as in
    synthesis.mirror-temperature-measures-deposit-under-r; the edge awaits the maintainer's
    confirmation. Reading T15's alpha as the lightest heavy mass of T12's fit
    identifies objects of two papers, which T15 Rem 4.7 leaves unsettled. The allowance m_3(M_I) >=
    25 meV (a factor two for running from M_Z to M_I) is a stated margin, not a computed running.
    Transport-absent.
---

## formal
For any complex $3 \times 3$ Dirac matrix $M_{D}$ and complex symmetric invertible Majorana matrix $M_{R}$ with smallest Takagi value $\alpha$ (the lightest heavy neutrino mass), the light matrix $m_{\nu} = M_{D}^{\mathsf{T}}M_{R}^{-1}M_{D}$ has largest Takagi value $m_{3} \le \lVert M_{D}\rVert^{2}/\alpha$, so
\[
\alpha \;\le\; \frac{\lVert M_{D}\rVert^{2}}{m_{3}} \;\le\; \frac{9\,e^{2}}{m_{3}}, \qquad e = \max_{ij}\,|(M_{D})_{ij}|.
\]
On the untuned fit among the representative fits of Proposition \claimref{standard-model.fits-record-level}, which rest on Premise (EW) (Dirac entries at most $0.04$ GeV at $M_{I}$, nothing cancelling), with $e \le 0.045$ GeV and $m_{3}(M_{I}) \ge 25$ meV (a factor two below the record's lower end, as allowance for running), $\alpha < 7.3 \times 10^{8}$ GeV, which lies below the chain's $M_{I} = 1.9 \times 10^{10}$ GeV (Proposition \claimref{standard-model.chain}) by a factor above $26$. Under Premise \claimref{neutrino.r-descent-reheats-below-lower-heavy}, $T_{\mathrm{desc}} \le \alpha$, with $\alpha$ read as the fit's lightest heavy mass, the descent on that fit reheats below $7.3 \times 10^{8}$ GeV and below the intermediate scale. Then the dark-matter remainder $\Omega h^{2} = \Omega_{c}h^{2} - \Omega_{b}h^{2}$ cannot be a relic of gravitational production from the plasma at the rate of Fact \claimref{dark-matter.imported-massless-graviton-production-rate}, with quanta no heavier than the bath (the odd towers' seeding signpost of the dark-matter paper), unless the summed production coefficient $c$ of its light content exceeds $3.9 \times 10^{12}$; for any $c \le 1$ the seeding temperature exceeds the cap more than $1400$-fold. The fit's tuned rows (Dirac entries $2.2$, $2.9$, $4.0$ GeV) give by the same bound only $\alpha < 8.9$, $15.4$, $29.2 \times 10^{11}$ GeV at $m_{3} = 49.4$ meV, which with the running allowance do not decide even at $c = 1$.

## technical
In any seesaw, the heaviest light neutrino mass is bounded by the square of the Dirac matrix's norm divided by the lightest heavy neutrino mass, so the lightest heavy mass is at most the Dirac norm squared over $m_{3}$, and the norm of a three-by-three matrix is at most three times its largest entry. One representative fit of the Standard-Model paper, the untuned one, made under Premise (EW), keeps every Dirac neutrino entry below $0.04$ GeV at the intermediate scale. Allowing a factor two for the running of $m_{3}$ to that scale, the lightest heavy neutrino lies below $7.3 \times 10^{8}$ GeV, more than twenty-six times below the intermediate scale $1.9 \times 10^{10}$ GeV.

If the descent reheats below the lightest heavy neutrino, as the neutrino paper's Premise (R) states, then on that fit it reheats below $7.3 \times 10^{8}$ GeV and below the Pati-Salam breaking scale. The odd towers' remainder of the dark matter then cannot have been made by gravitational production from the plasma with quanta no heavier than the bath unless the hidden light content's summed production coefficient exceeds $3.9 \times 10^{12}$; for any content with coefficient up to one (several hundred vector species) the required temperature exceeds the cap more than a thousandfold. The fit's tuned rows, with Dirac entries of $2$ to $4$ GeV, give weaker bounds that do not decide. The fits rest on Premise (EW), not on Hypothesis (U), and identifying the neutrino paper's lower heavy scale with the fit's lightest heavy mass joins two papers' objects.

## lay
In the seesaw picture, the ordinary neutrino masses are tiny because they are suppressed by very heavy partner neutrinos. A simple matrix inequality turns this around: given how large the neutrinos' ordinary (Dirac) mass terms are, the lightest heavy partner cannot be heavier than a definite amount. In one representative fit of the Standard-Model paper, the one that needs no fine cancellation, those mass terms are small, at most a few hundredths of a GeV, which puts the lightest heavy partner below about a billion GeV. The neutrino paper assumes the early universe never got hotter than that partner's mass, so on this fit the early universe stayed below about a billion GeV, far too cool for gravity alone to have made the hidden matter that would account for the rest of the dark matter.

## one-liner
Since $\alpha \le \lVert M_{D}\rVert^{2}/m_{3}$, a representative untuned Pati-Salam fit under Premise (EW) (Dirac entries $\le 0.04$ GeV) puts the lightest heavy neutrino below $7.3 \times 10^{8}$ GeV, so under Premise (R) the descent reheats below the intermediate scale and the odd-tower remainder cannot be a gravitational-seeding relic unless $c > 3.9 \times 10^{12}$.
