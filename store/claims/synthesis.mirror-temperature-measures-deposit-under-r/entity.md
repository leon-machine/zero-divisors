---
id: synthesis.mirror-temperature-measures-deposit-under-r
kind: claim
version: 2
title: 'Under (R) the mirror temperature measures the deposit'
status: proved
region: synthesis
subject: dark-matter
tags: [mirror-sector, dark-tower-premises]
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
  role: 'restatement of the bounds on the floor under (R) and of the accuracy without (R), from the floors at the derived production coefficients; the deposit law and its window unchanged'
  version: 2
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-navigate)'
amendments:
- version: 2
  kind: restatement
  defect: 'clause (i) and the closing sentence scaled the floors 3.2e-4 (mirror) and 3.5e-4 (nine vectors) of the coefficients proposition, computed with production coefficients that were too small; the floors are 5.2e-4 and 6.4e-4, so under (R) the mirror''s floor is below 2.5e-5 and not 1.5e-5, 120 and not 200 times below the helium edge, and without (R) the law holds to 9.1e-4 and not 1.3e-4 of xi^4 at that edge'
  evidence: check.py::check_mirror_temperature_measures_deposit
review: draft
derivations:
- name: main
  uses:
  - dark-matter.seeding-gravity-floor-dark-towers-temperature@5
  - dark-matter.coefficients-floors-they-give-what-gravity@5
  - dark-matter.stored-asymmetry-charge-not-number@12
  - dark-tower-matter.mirrors-composition@4
  - dark-matter.open-channels-their-costs@6
  - dark-matter.mirror-tower-copy-one@11
  assumes:
  - neutrino.r-descent-reheats-below-lower-heavy@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_mirror_temperature_measures_deposit
- kind: proof
  derivation: main
extraction:
  maintainer_pass_2026_11_18:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 1 -> 2, at Leon''s decision of 18 November 2026 (restate the numbers that used the first published production coefficients). From the floors of dark-matter.coefficients-floors-they-give-what-gravity version 5 (mirror 5.2e-4, nine vectors 6.4e-4 at 6e14 GeV): under (R) the mirror''s floor below 1.5e-5 -> 2.5e-5, 200 -> 120 times below the helium edge; nine vectors below 1.7e-5 -> 3.0e-5, 184 to 185 -> 101 to 102 times; without (R) the floor''s share of xi^4 at the helium edge below 1.3e-4 -> 9.1e-4. Clauses (ii) and (iii), and the conclusion that under (R) the floor drops out, are unchanged (the floor still changes xi^4 by less than 1e-8 at the helium edge under (R)). The four premises restated the same day are repinned after this review.'
  maintainer_pass_2026_11_12:
    by: maintainer-2026-11-12
    date: '2026-11-12'
    note: 'Scope note, version kept, no statement changed (Leon''s decision of 12 November 2026: the inherited charge is B - L). The hot-deposit arithmetic uses this tower''s baryons per unit entropy as the charge per unit entropy. With the charge named as B - L, the charge per unit entropy is larger by 1/c, c the anomalous weak equilibrium coefficient (not a stored Fact; 28/79 for one light doublet, 8/23 for two), if that process equilibrated. An estimate, not computed in the store and not checked: at fixed energy per unit charge the deposit''s xi would then be larger by about (1/c)^(1/4), roughly 1.3 for either value of c. The statement, its numbers and its check are unchanged.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.stored-asymmetry-charge-not-number repinned 8 -> 9 after reviewing its G1 restatement (the cold mirror is an exception to P2 at its version-1 reach, P2 as scoped leaves xi free, and the cold mirror then needs a non-equilibrium descent; the charge reading and the numbers are unchanged); the use here holds as cited. Pin review: dark-matter.mirror-tower-copy-one repinned 8 -> 9 after reviewing its C1 restatement (clause (iv): the common ceiling and coupling are now Premise synthesis.common-ceiling-coupling-premise, P2 equating labels and not couplings; the share of one rests also on that premise; the caveat is reworded for P2''s version-1 reach), clauses (i) to (iii) and (v) unchanged in content; the use here holds as cited.'
  open_problem: op.pre-descent-theory
  note: >-
    Addresses the second entry of the problem, the energy with which the descent deposits each
    tower's charge. Under Premise (R) the floor drops out, the deposit enters the mirror's
    temperature only through one dimensionless number, and the record and the mirror's composition
    bound that number without fixing the reheating temperature. Complements the conjunction no-go
    filed in the same run against this problem (odd-tower remainder not a seeding relic on the
    Pati-Salam branch). Transport-absent: arithmetic on stored cosmology.
---

## formal
Assume Premise \claimref{neutrino.r-descent-reheats-below-lower-heavy} ($T_{\mathrm{desc}} \leq \alpha$), with $\alpha \leq 10^{13}$ GeV at either end of Hypothesis (U) (Remark \claimref{note.neutrino.branch-m-3}), the charge reading of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}, and the mirror's copied content (Theorem \claimref{dark-matter.mirror-tower-copy-one}). Write $\xi = T'/T$ and $Y_{B} = n_{B}/s = 8.7 \times 10^{-11}$.
\begin{enumerate}
\item[(i)] \emph{(The floor drops out.)} The gravitational floor has $\xi_{\mathrm{floor}}^{4} \propto T_{\mathrm{desc}}^{3}$ (Proposition \claimref{dark-matter.seeding-gravity-floor-dark-towers-temperature}), so from its values at $6 \times 10^{14}$ GeV (Proposition \claimref{dark-matter.coefficients-floors-they-give-what-gravity}) it is below $2.5 \times 10^{-5}$ for the mirror, more than $120$ times below the lower edge $\xi = 3 \times 10^{-3}$ of the interval in which the mirror is helium (Computation \claimref{dark-tower-matter.mirrors-composition}(ii)); for a nine-vector five-dimensional tower it is below $3.0 \times 10^{-5}$. These bounds use the energy convention of that proposition ($3T$ for each creation event); at the mean energy per event noted there the two floors are about $3.1 \times 10^{-5}$ and $3.8 \times 10^{-5}$, nearly a hundred and about eighty times below the edge, and the bounds of (iii) grow by about $2.6$ (computed in the review of 18 November 2026).
\item[(ii)] \emph{(The deposit law.)} Let the descent deposit in the mirror an energy $\varepsilon\,T_{\mathrm{desc}}$ per unit of its charge, and assume that the deposit is thermalised at once among the mirror's light content, that $g' = g = 106.75$ at the deposit ($T_{\mathrm{desc}}$ above the electroweak scale), and that neither tower receives entropy afterwards beyond its own copied history, which then preserves the ratio (Proposition \claimref{dark-matter.open-channels-their-costs}). Then
\[
\xi^{4} \;=\; \tfrac{4}{3}\,Y_{B}\,\varepsilon \;+\; \xi_{\mathrm{floor}}^{4},
\]
with no other dependence on $T_{\mathrm{desc}}$. This tower holds $\tfrac{3}{4}T_{\mathrm{desc}}/Y_{B} = 8.6 \times 10^{9}\,T_{\mathrm{desc}}$ per unit charge, so $\xi^{4}$ is, up to the floor, the ratio of the two towers' deposits per unit charge; equal deposits give $\xi = 1$.
\item[(iii)] \emph{(The window.)} The $\Neff$ cap $\xi < 0.448$ gives $\varepsilon < 3.5 \times 10^{8}$; T14's hot deposit, $\varepsilon = 3$, gives $\xi = 4.3 \times 10^{-3}$; and the mirror is helium, $3 \times 10^{-3} \leq \xi \leq 2 \times 10^{-2}$, exactly when $0.70 \leq \varepsilon \leq 1.4 \times 10^{3}$. Below $\varepsilon \approx 0.7$ the mirror is colder than the helium interval, down to the floor of (i).
\end{enumerate}
So under (R) the mirror's temperature fixes the deposit per unit charge in units of the reheating temperature and says nothing about the reheating temperature itself. (R) only removes the floor: at the ceiling $T_{\mathrm{desc}} = 6 \times 10^{14}$ GeV the mirror's floor changes $\xi^{4}$ at the helium edge by less than $9.1 \times 10^{-4}$ of its value, so (ii) and (iii) hold to that accuracy without (R).

## technical
Under Premise (R), which keeps the descent's reheating temperature below about $10^{13}$ GeV, the gravitational heating of the dark towers is negligible: it leaves the mirror below $2.5 \times 10^{-5}$ of the visible temperature, more than a hundred and twenty times colder than the interval $3 \times 10^{-3} \leq \xi \leq 2 \times 10^{-2}$ in which the mirror burns to helium. The mirror's temperature is then set by the energy the descent deposited per unit of its charge. Writing that energy as $\varepsilon T_{\mathrm{desc}}$, and assuming the deposit thermalises at once with the mirror's copied light content and no later entropy injection, the reheating temperature cancels: $\xi^{4} = \tfrac43 Y_{B}\varepsilon$ with $Y_{B} = 8.7 \times 10^{-11}$. The dark-radiation cap allows $\varepsilon$ up to $3.5 \times 10^{8}$; a helium mirror needs $\varepsilon$ between $0.70$ and $1.4 \times 10^{3}$, which contains T14's hot deposit $\varepsilon = 3$. Without (R) the same law holds to about one part in a thousand in $\xi^{4}$ at the helium edge.

## lay
The descent that started the universe left each family of worlds with a stored charge. If the descent happened below the temperature that the series' neutrino paper assumes, then gravity afterwards heated the mirror world by a negligible amount, so the mirror's temperature today records only how much energy the descent put into it per unit of charge. Measured in units of the descent's own temperature, that energy is the one number that matters: if the mirror world burned its matter to helium, as one of the series' scenarios needs, it lies between about 0.7 and 1400; the limit on extra radiation only caps it near 350 million. The descent's temperature itself drops out and is left unconstrained by the mirror.

## one-liner
Under Premise (R) the mirror's gravitational floor is below $2.5 \times 10^{-5}$, so its temperature measures only the deposit per unit charge $\varepsilon T_{\mathrm{desc}}$, with $\xi^{4} = \tfrac43 Y_{B}\varepsilon$; a helium mirror needs $0.70 \leq \varepsilon \leq 1.4 \times 10^{3}$, and the reheating temperature drops out.
