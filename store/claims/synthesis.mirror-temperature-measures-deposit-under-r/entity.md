---
id: synthesis.mirror-temperature-measures-deposit-under-r
kind: claim
version: 1
title: Under Premise (R) the gravitational floor is negligible, and the mirror's temperature measures the descent's deposit per unit charge in units of the reheating temperature
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
review: draft
derivations:
- name: main
  uses:
  - dark-matter.seeding-gravity-floor-dark-towers-temperature@4
  - dark-matter.coefficients-floors-they-give-what-gravity@4
  - dark-matter.stored-asymmetry-charge-not-number@8
  - dark-tower-matter.mirrors-composition@3
  - dark-matter.open-channels-their-costs@5
  - dark-matter.mirror-tower-copy-one@8
  assumes:
  - neutrino.r-descent-reheats-below-lower-heavy@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_mirror_temperature_measures_deposit
- kind: proof
  derivation: main
extraction:
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
\item[(i)] \emph{(The floor drops out.)} The gravitational floor has $\xi_{\mathrm{floor}}^{4} \propto T_{\mathrm{desc}}^{3}$ (Proposition \claimref{dark-matter.seeding-gravity-floor-dark-towers-temperature}), so from its values at $6 \times 10^{14}$ GeV (Proposition \claimref{dark-matter.coefficients-floors-they-give-what-gravity}) it is below $1.5 \times 10^{-5}$ for the mirror, more than $200$ times below the lower edge $\xi = 3 \times 10^{-3}$ of the interval in which the mirror is helium (Computation \claimref{dark-tower-matter.mirrors-composition}(ii)); for a nine-vector five-dimensional tower it is below $1.7 \times 10^{-5}$.
\item[(ii)] \emph{(The deposit law.)} Let the descent deposit in the mirror an energy $\varepsilon\,T_{\mathrm{desc}}$ per unit of its charge, and assume that the deposit is thermalised at once among the mirror's light content, that $g' = g = 106.75$ at the deposit ($T_{\mathrm{desc}}$ above the electroweak scale), and that neither tower receives entropy afterwards beyond its own copied history, which then preserves the ratio (Proposition \claimref{dark-matter.open-channels-their-costs}). Then
\[
\xi^{4} \;=\; \tfrac{4}{3}\,Y_{B}\,\varepsilon \;+\; \xi_{\mathrm{floor}}^{4},
\]
with no other dependence on $T_{\mathrm{desc}}$. This tower holds $\tfrac{3}{4}T_{\mathrm{desc}}/Y_{B} = 8.6 \times 10^{9}\,T_{\mathrm{desc}}$ per unit charge, so $\xi^{4}$ is, up to the floor, the ratio of the two towers' deposits per unit charge; equal deposits give $\xi = 1$.
\item[(iii)] \emph{(The window.)} The $\Neff$ cap $\xi < 0.448$ gives $\varepsilon < 3.5 \times 10^{8}$; T14's hot deposit, $\varepsilon = 3$, gives $\xi = 4.3 \times 10^{-3}$; and the mirror is helium, $3 \times 10^{-3} \leq \xi \leq 2 \times 10^{-2}$, exactly when $0.70 \leq \varepsilon \leq 1.4 \times 10^{3}$. Below $\varepsilon \approx 0.7$ the mirror is colder than the helium interval, down to the floor of (i).
\end{enumerate}
So under (R) the mirror's temperature fixes the deposit per unit charge in units of the reheating temperature and says nothing about the reheating temperature itself. (R) only removes the floor: at the ceiling $T_{\mathrm{desc}} = 6 \times 10^{14}$ GeV the mirror's floor changes $\xi^{4}$ at the helium edge by less than $1.3 \times 10^{-4}$ of its value, so (ii) and (iii) hold to that accuracy without (R).

## technical
Under Premise (R), which keeps the descent's reheating temperature below about $10^{13}$ GeV, the gravitational heating of the dark towers is negligible: it leaves the mirror below $1.5 \times 10^{-5}$ of the visible temperature, more than two hundred times colder than the interval $3 \times 10^{-3} \leq \xi \leq 2 \times 10^{-2}$ in which the mirror burns to helium. The mirror's temperature is then set by the energy the descent deposited per unit of its charge. Writing that energy as $\varepsilon T_{\mathrm{desc}}$, and assuming the deposit thermalises at once with the mirror's copied light content and no later entropy injection, the reheating temperature cancels: $\xi^{4} = \tfrac43 Y_{B}\varepsilon$ with $Y_{B} = 8.7 \times 10^{-11}$. The dark-radiation cap allows $\varepsilon$ up to $3.5 \times 10^{8}$; a helium mirror needs $\varepsilon$ between $0.70$ and $1.4 \times 10^{3}$, which contains T14's hot deposit $\varepsilon = 3$. Without (R) the same law holds to about one part in ten thousand in $\xi^{4}$ at the helium edge.

## lay
The descent that started the universe left each family of worlds with a stored charge. If the descent happened below the temperature that the series' neutrino paper assumes, then gravity afterwards heated the mirror world by a negligible amount, so the mirror's temperature today records only how much energy the descent put into it per unit of charge. Measured in units of the descent's own temperature, that energy is the one number that matters: if the mirror world burned its matter to helium, as one of the series' scenarios needs, it lies between about 0.7 and 1400; the limit on extra radiation only caps it near 350 million. The descent's temperature itself drops out and is left unconstrained by the mirror.

## one-liner
Under Premise (R) the mirror's gravitational floor is below $1.5 \times 10^{-5}$, so its temperature measures only the deposit per unit charge $\varepsilon T_{\mathrm{desc}}$, with $\xi^{4} = \tfrac43 Y_{B}\varepsilon$; a helium mirror needs $0.70 \leq \varepsilon \leq 1.4 \times 10^{3}$, and the reheating temperature drops out.
