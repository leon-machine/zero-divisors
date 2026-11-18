---
id: synthesis.seeding-remainder-excludes-perturbative-pati-salam
kind: claim
version: 3
title: 'A seeding-relic remainder excludes perturbative Pati-Salam'
status: proved
region: synthesis
subject: dark-matter
tags: [matter-asymmetry, seesaw-and-majorana, hypothesis-u]
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
- name: Claude Fable 5.2
  role: 'restatement: the contents'' coefficients, the margins and the thresholds on the coupling and the Dirac mass recomputed with the derived production coefficients; the factor 2 identified as the two quanta of an event; the exclusion stands with smaller margins'
  version: 3
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-navigate)'
amendments:
- version: 3
  kind: restatement
  defect: 'the coefficients of the contents (0.051 for the odd towers'' vectors, 0.312 for four Standard-Model contents) and every margin computed from them used the first published per-species values, which are too small by about a factor ten; with the derived values the contents have c = 0.529 and 2.27, the margins over the perturbative cap fall from 4.0 and 2.5 to 2.2 and 1.5, and the threshold c* = 13.49 is about 560 vector species, not 5900'
  evidence: check.py::check_seeding_remainder_excludes_perturbative_pati_salam
review: draft
derivations:
- name: main
  uses:
  - dark-matter.seeding-gravity-floor-dark-towers-temperature@6
  - dark-matter.imported-massless-graviton-production-rate@4
  - dark-matter.population-count-one-share-half-percent@8
  - dark-matter.coefficients-floors-they-give-what-gravity@6
  - standard-model.what-angle-asks-neutrino-sector@4
  - dark-matter.ceiling-valued-inherited-success@5
  - synthesis.gauge-algebra-by-tower@1
  - standard-model.chain@8
  - synthesis.gravitational-pair-production-from-the-operator-source-at-first-order@2
  assumes:
  - neutrino.r-descent-reheats-below-lower-heavy@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_seeding_remainder_excludes_perturbative_pati_salam
- kind: proof
  derivation: main
extraction:
  maintainer_pass_2026_11_18:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 2 -> 3, at Leon''s decision of 18 November 2026 (restate the direct users of the corrected production rate). The conditions on c are unchanged (c* = 13.49, c > 63.7, A^(1/4) = 1.217e12 GeV). Recomputed from the contents'' c with the coefficients of synthesis.gravitational-pair-production-from-the-operator-source-at-first-order, clause (v): odd towers'' vectors 0.051 -> 0.529, four Standard-Model contents 0.312 -> 2.27; c* in vector species 5900 -> 560; margins over the cap 4.0 and 2.5 -> 2.2 and 1.5; f_J > 32 -> 19.6; m_D > 8.2 -> 6.4 GeV against 5.2; tolerance in v_R 2.5 -> 1.5; one-liner bound 1.36e12 GeV at c <= 0.312 -> 8.3e11 GeV at c <= 2.28. The exclusion in (i) and (ii) stands. In (iii) the clause with the factor 66 at the ceiling reading still fails at the vectors'' c but now holds at four Standard-Model contents'' c, which is stated. The factor 2 is now the two quanta of each creation event and no longer a bracket. The seeding and coefficients propositions are repinned to their restated versions of the same day.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.imported-massless-graviton-production-rate repinned 1 -> 2 after reviewing the F14 change writing the rate with the reduced Planck mass bar M_P, the source''s M_P (any M_P here that is evaluated is 2.435e18 GeV, the reduced mass); the use here holds as cited. Pin review: dark-matter.population-count-one-share-half-percent repinned 5 -> 6 after reviewing its C1 restatement (the share of one now rests also on the common-ceiling-coupling premise, with an assumes edge; the numbers are unchanged); the use here holds as cited.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'The formal level restated: c*/0.0023 computes to 5867: ''about 5800'' corrected to ''about 5900'' (rounding). Version 1 -> 2. The technical level restated: c*/0.0023 computes to 5867: ''about 5800'' corrected to ''about 5900'' (rounding).'
  open_problem: op.pre-descent-theory
  note: >-
    A consistency test of the window op.pre-descent-theory asks for. It joins four statements the
    store holds separately: the seeding signpost of T14's successor problem (3) (odd towers as
    gravitational-seeding relics of the remainder, quanta no heavier than the bath), Premise (R)
    of T15, the triplet vev of T12 Prop 11.2 on the chain with the (15,2,2), and a perturbative
    Majorana coupling. T14's rung M_R is the seesaw quotient m_D^2/m_3; on T12's route the
    Majorana matrix is v_R f (T15 Rem 4.7), so M_3 = f_J v_R there. Hypothesis (U) is not needed
    for (i). Transport-absent: imported production rate, record-level running and cosmological
    bookkeeping. The proton mass is the PDG value; the perturbativity bound f_J <= 4 pi is a
    stated condition, not a premise of the series. Premise (R) (neutrino.r-descent-reheats-below-lower-heavy)
    is used in its weakest consequence T_desc <= M_3 and recorded as an assumes edge, as in
    synthesis.mirror-temperature-measures-deposit-under-r; the edge awaits the maintainer's
    confirmation. Filed alongside synthesis.untuned-fit-caps-lightest-heavy-neutrino, which reaches
    the same conclusion on a representative fit under Premise (EW) without the perturbativity bound.
---

## formal
Let the remainder $\Omega h^{2} = 0.0976 \pm 0.0012$, that is $4.364\,\Omega_{b}$ (Proposition \claimref{dark-matter.population-count-one-share-half-percent}(ii)), consist of odd-tower relics of gravitational seeding with quanta no heavier than the bath, produced at the rate of Theorem \claimref{synthesis.gravitational-pair-production-from-the-operator-source-at-first-order}(v) (Fact \claimref{dark-matter.imported-massless-graviton-production-rate} for the published values), under that theorem's hypothesis (OS), or on the standard account of the Fact, with summed coefficient $c$ over the produced light content, with the yield of Proposition \claimref{dark-matter.seeding-gravity-floor-dark-towers-temperature} (the two antecedents of T14's seeding signpost, not asserted by T14). Then $c\,T_{\mathrm{desc}}^{4} \ge A/2$ with $A^{1/4} = 1.217 \times 10^{12}$ GeV, the factor $2$ being the two quanta of each creation event that the rate counts. Assume Premise \claimref{neutrino.r-descent-reheats-below-lower-heavy}, $T_{\mathrm{desc}} \le \alpha = \min(\alpha, M_{3})$, of which only the consequence $T_{\mathrm{desc}} \le M_{3}$ is used.
\begin{enumerate}
\item[(i)] On the chain of Proposition \claimref{standard-model.what-angle-asks-neutrino-sector} with the $(15,2,2)$ at the record's central values, $M_{3} = f_{J}v_{R}$ with $v_{R} = 4.2 \times 10^{10}$ GeV. If $f_{J} \le 4\pi$, then $M_{3} < 5.35 \times 10^{11}$ GeV and the four conditions are jointly satisfiable only if $c > c^{*} = 13.49$, about $560$ vector species at the per-vector coefficient $2.4055 \times 10^{-2}$, or more than $23$ copies of the Standard Model's content. The four odd towers' gauge vectors (Theorem \claimref{synthesis.gauge-algebra-by-tower}: $2 + 2 + 9 + 9$) give $c = 0.529$, and four towers each with the mirror's Standard-Model coefficient $0.568$ (Proposition \claimref{dark-matter.coefficients-floors-they-give-what-gravity}(ii)) give $2.27$; at these the seeding temperature exceeds the largest allowed $M_{3}$ by factors above $2.2$ and $1.5$. Satisfying the signpost on this chain at $c = 2.27$ needs $f_{J} > 19.6$, a Dirac mass $m_{D} > 6.4$ GeV against the perturbative cap $5.2$ GeV.
\item[(ii)] Without the chain, at the bottom end of Hypothesis (U) read at a common low scale (Proposition \claimref{dark-matter.ceiling-valued-inherited-success}), $M_{3} = m_{b}^{2}/m_{3} < 3.63 \times 10^{11}$ GeV and the conjunction needs $c > 63.7$.
\item[(iii)] The top end of (U) at a common low scale, $M_{3} = m_{t}^{2}/m_{3} > 5.8 \times 10^{14}$ GeV, satisfies the signpost for any $c \ge 0.529$ (the odd towers' vectors alone) even with $T_{\mathrm{desc}} \le M_{3}/66$, and on the chain it needs $f_{J} > 4000\pi$. The clause with $M_{3}/66$ depends on that reading for the vectors alone: read at the ceiling, both ends of (U) fall by about an order of magnitude and $(M_{3}/66)^{4} < A/(2c)$ at $c = 0.529$, while $T_{\mathrm{desc}} \le M_{3}$ alone is still met; at $c = 2.27$ the inequality is reversed when the ceiling reading lowers $M_{3}$ by a factor $10$, with a margin of about $7$ percent in $M_{3}$ (a fall by a factor $11$ restores the failure), so for four Standard-Model contents the clause with $66$ holds on both readings only if the fall is no more than about that factor; the stored reading says only ``about an order of magnitude'', so this case is not decided.
\end{enumerate}
So under (R) the odd-tower remainder is a seeding relic only off the perturbative Pati-Salam branch and only at the top end of (U); on the perturbative chain, whose cap lies near the bottom end of (U), the remainder must come from the descent's deposit, or (R), or the seeding antecedents, fail. The margin in (i) at $c = 2.27$ survives an increase of $v_{R}$ by a factor up to $1.5$; the same chain at one loop (Proposition \claimref{standard-model.chain}(2)), $M_{I} = 3.2 \times 10^{11}$ GeV, exceeds that, so (i) holds at the two-loop record level only.

## technical
Assume the remainder of the dark matter, $4.364$ times the baryons, consists of odd-tower relics produced gravitationally from the visible plasma, with quanta no heavier than the bath, which are the two antecedents of T14's seeding signpost. With the stored yield, the remainder then needs $c\,T_{\mathrm{desc}}^{4} \ge A/2$ with $A^{1/4} = 1.217 \times 10^{12}$ GeV, where $c$ sums the production coefficients derived in the store over the produced light species (under that derivation's hypothesis (OS), or on the standard account of the imported rate) and the $2$ counts the two quanta of each creation event. Premise (R), assumed, gives $T_{\mathrm{desc}} \le M_{3}$ in its weakest form.

On the Standard-Model paper's chain with the $(15,2,2)$, the heavy neutrino mass is $M_{3} = f_{J}v_{R}$ with $v_{R} = 4.2 \times 10^{10}$ GeV, so a perturbative $f_{J} \le 4\pi$ caps $M_{3}$ below $5.35 \times 10^{11}$ GeV. All four conditions then hold only if $c > 13.49$, about $560$ vector species or more than $23$ copies of the Standard Model's content. The odd towers' gauge vectors give $c = 0.529$, and four towers with Standard-Model-sized content give $2.27$; at these the seeding temperature exceeds the cap by factors above $2.2$ and $1.5$, and meeting the signpost would need $f_{J} > 19.6$. At the bottom end of Hypothesis (U), with no chain input, $M_{3} < 3.63 \times 10^{11}$ GeV and the conjunction needs $c > 63.7$. At the top end of (U), read at a common low scale, the signpost is met, for content at least the odd towers' vectors, even with the fitted factor $66$ below $M_{3}$ (read at the ceiling, without that factor; with it, not at the vectors' $c = 0.529$, and at four Standard-Model contents' $2.27$ only if the ceiling reading lowers $M_{3}$ by no more than a factor of about $10.7$, which the stored reading does not fix), but on the chain that end needs $f_{J}$ above $10^{4}$.

So under (R) the odd towers' remainder can be a seeding relic only off the perturbative Pati-Salam branch, at the top end of (U); on the perturbative chain, whose cap lies near the bottom end of (U), it must come from the descent's deposit, or (R) or the seeding antecedents fail. The margin holds at the two-loop record level only; the one-loop intermediate scale of the same chain would dissolve it. A representative fit of the Standard-Model paper under Premise (EW) reaches the same conclusion without the perturbativity bound (filed alongside, synthesis.untuned-fit-caps-lightest-heavy-neutrino).

## lay
The series leaves open where the part of the dark matter not explained by the mirror world comes from. One suggestion in the dark-matter paper is that it was made by gravity alone from the hot early universe, which would need that early universe to have been at least about a trillion GeV hot. A separate assumption in the neutrino paper says the early universe never got hot enough to make the heavy neutrinos, and the Standard-Model paper's preferred unification route, with a reasonably sized coupling, puts those neutrinos below about half a trillion GeV. This result checks the arithmetic, assuming the leftover dark matter was made by gravity in that way and using the Standard-Model route's couplings as computed at two loops: the three cannot all hold for the hidden matter the series considers. With the rate of gravitational production as the collection now derives it, they could hold only if the hidden worlds held the equivalent of more than twenty-three copies of the Standard Model's light particles, where the series has at most four hidden worlds of that size; the margin is smaller than with the published rate used before, a factor of about one and a half in temperature at the largest content. Something has to give: the heavy neutrinos are heavier than that route allows, the early universe was hotter than the neutrino assumption allows, or the leftover dark matter was laid down directly at the universe's origin rather than made by gravity afterwards.

## one-liner
If the odd towers' remainder is a gravitational-seeding relic (quanta no heavier than the bath) and the descent reheats below $M_{3}$ (Premise (R)), then $M_{3} > 8.3 \times 10^{11}$ GeV for any content with $c \le 2.28$ (four towers of Standard-Model content, at the derived production coefficients), beyond the Pati-Salam chain's perturbative cap $4\pi v_{R} < 5.35 \times 10^{11}$ GeV and the bottom end of (U); only the top end of (U), off the perturbative branch, survives; at the two-loop record level.
