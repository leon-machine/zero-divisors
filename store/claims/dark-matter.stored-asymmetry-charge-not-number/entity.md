---
id: dark-matter.stored-asymmetry-charge-not-number
kind: claim
version: 8
title: The stored asymmetry is a charge, not a number
status: proved
region: dark-matter
subject: dark-matter
tags: [matter-asymmetry, mirror-sector, dark-matter-ratio, needs-continuum]
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
derivations:
- name: main
  uses:
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation@5
  - dark-matter.coefficients-floors-they-give-what-gravity@4
  - dark-matter.imported-trichotomy-descents-data@5
  - dark-matter.mirror-tower-copy-one@8
  - dark-matter.parallel-boundary-mode-spaces-one-wall@5
  - dark-matter.seeding-gravity-floor-dark-towers-temperature@4
  assumes:
  - dark-matter.p1-single-frozen-point@1
  - dark-matter.p5-boundary-modes-hold-entropy-not@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:prop:charge
- kind: check
  ref: check.py::check_charge_reading_against_thermal_reading
- kind: check
  ref: check.py::check_origin_gravity_cannot_supply_the_charge
- kind: check
  ref: check.py::check_eta_prime_and_radiation_over_the_interval
- kind: check
  ref: check.py::check_bottom_of_ceiling_range_factor
locators:
  paper: T14
  number: Prop 4.6
  label: prop:charge
  line: 399
extraction:
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'P1 parenthetical reworded at all four levels (decision of 2026-10-31): N = M_P/H fixes a count of light rays, about pi N^2/ln 2, common to the towers; the boundary-mode arrays per light ray are tower-dependent, and a five-dimensional field counts one array set per Kaluza-Klein level, equivalently per resolution cell. Previously the parenthetical said N fixes the boundary mode count. The argument, which uses only that N is common, is unchanged. Version 7 -> 8.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: charge against thermal reading (0.448^3 and below 1e-7), gravitational shortfall above 1e4, eta and its cube root, eta'' at the floor and hot deposit, eta''/eta above 1e7, N_eff eight orders below the cap. Version 5 -> 6. Check strengthened: eta exact; crossover, eta'' at the floor ends and hot deposit, eta''/eta and the Delta N_eff margin pinned to six or seven figures. Version 6 -> 7.'
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'A5 largeness follow-up: N here is the series number M_P/H, which fixes the boundary mode count (about pi N^2/ln 2) without being it; all four levels no longer call N the mode count. Q = eps N unchanged.'
  superseded_in_part_by:
  - dark-tower-matter.mirrors-temperature-p2
  - dark-tower-matter.mirrors-composition
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 1
    note: 'Superseded in part by T14c. Prop 8.2 (dark-tower-matter.mirrors-temperature-p2): P2 with the
      reach of Thm 4.3(iv), (v) fixes xi = 1, so clause (iii)''s free temperature datum is an exception
      to P2; (iii) now says so. Comp 8.3 (dark-tower-matter.mirrors-composition): at the floor the mirror
      is degenerate and 96 to 100 percent neutrons for L <= 0, helium only for xi about 3e-3 to 2e-2,
      so the closing level sentence no longer carries the burning branch as the floor''s expectation.
      (i), (ii), (iv) unchanged. Original in source_formal.'
  source_formal: |-
    Under the classification of Proposition \claimref{dark-matter.asymmetry-arrow-counted-fifteenth-refutation}, with $\epsilon$ initial data of the descent, inherited rather than generated, and the boundary mode count $N$ common to the towers under P1:
    \begin{enumerate}
    \item[(i)] \emph{(Charge.)} The asymmetry stored in an oriented tower is the charge $Q = \epsilon N$, fixed by the descent's data and independent of the tower's temperature; it is not a thermal number $n - \bar{n} \propto g\,\mu T^{2}$. So the mirror share $f_{2} = 1$ holds at any mirror temperature: a cold mirror carries the same baryon charge as this tower in the same number of baryons, with negligible mirror radiation.
    \item[(ii)] \emph{(Origin.)} The charge is the descent's and cannot be produced afterwards: the one channel superselection leaves open, gravitational production from the visible plasma (Appendix \ref{app:seeding}), yields $1.8$ to $2.7 \times 10^{-15}$ mirror quanta per unit entropy at the ceiling reheating against the $8.7 \times 10^{-11}$ baryons per unit entropy that our baryon number requires, more than four orders too few even counting every produced quantum as a baryon. Black holes are a sink for $Q$, not a source (Proposition \claimref{dark-matter.parallel-boundary-mode-spaces-one-wall}(iv), under P5): a mass-preserving rearrangement that erodes each tower's free baryon count and moves no share.
    \item[(iii)] \emph{(Temperature.)} The mirror's temperature ratio $\xi = T'/T$ is a datum of the descent, bounded below by the gravitational floor, $\xi$ between $2.8$ and $3.2 \times 10^{-4}$ at the ceiling reheating (Proposition \claimref{dark-matter.coefficients-floors-they-give-what-gravity}(ii), the bracket the species-counting ambiguity; four parts in a thousand of this at the bottom of the ceiling range), and above by the $\Neff$ cap at $0.448$; a deposit of each unit of baryon number with energy of order the reheating temperature puts it at $\xi \approx 4 \times 10^{-3}$. The paper carries the whole interval. With $\eta = n_{B}/n_{\gamma} = 6.1 \times 10^{-10}$ here and equal baryon number,
    \[
    \eta' \;=\; \frac{\eta}{\xi^{3}}
    \]
    runs from $19$ to $26$ at the floor down to about $0.008$ at the hot deposit, crossing one at $\xi = \eta^{1/3} = 8.5 \times 10^{-4}$: at least $10^{7}$ times ours throughout, with $\Delta\Neff$ eight orders or more below the cap.
    \item[(iv)] \emph{(The two readings.)} The thermal reading would give $f_{2} \sim \xi_{2}^{3}$ instead, at most $0.090$ under the $\Neff$ cap ($0.448^{3}$) and $10^{-7}$ or less anywhere in the interval; the two readings cannot both hold, and the paper's own classification decides for the charge.
    \end{enumerate}
    Level: the classification is Fact \claimref{dark-matter.imported-trichotomy-descents-data}'s; the incompatibility is arithmetic. The mirror's nucleosynthesis, which is not a copy of ours and on which the burning branch of Proposition \claimref{dark-matter.mirror-share-one-how-fragile}(i) and the composition caveat of refutation item 6 rest, follows the proof, at assembly level.
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
    - dark-matter.imported-trichotomy-descents-data
    - dark-matter.parallel-boundary-mode-spaces-one-wall
    - dark-matter.p1-single-frozen-point
    - dark-matter.p5-boundary-modes-hold-entropy-not
    note: 'Added the classification it is stated under (the fifteenth-refutation proposition and the trichotomy
      Fact whose level it carries), the black-hole sink clause (the infall proposition, under P5, possible
      now that its edge back here was removed) and P1 for the common mode count; the fragility proposition
      is downstream context. Levels pass: the lay level now states the classification, P1 and P5, all
      of which it had dropped; the one-liner adds P1.'
  env: proposition
  context_refs:
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
  - dark-matter.imported-trichotomy-descents-data
  - dark-matter.mirror-share-one-how-fragile
  - dark-matter.parallel-boundary-mode-spaces-one-wall
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
    - dark-matter.imported-trichotomy-descents-data
    - dark-matter.parallel-boundary-mode-spaces-one-wall
    - dark-matter.p1-single-frozen-point
    - dark-matter.p5-boundary-modes-hold-entropy-not
---

## formal
Under the classification of Proposition \claimref{dark-matter.asymmetry-arrow-counted-fifteenth-refutation}, with $\epsilon$ initial data of the descent, inherited rather than generated, and the number $N$ common to the towers under P1 ($N = M_{P}/H$, which fixes a count of light rays, about $\pi N^{2}/\ln 2$, without being it: Observation \claimref{standard-model.largeness-number-universes-boundary-modes}; the number of boundary-mode arrays per light ray depends on the tower's content, and a five-dimensional field counts one array set per Kaluza-Klein level, equivalently one per resolution cell of the extra direction, so the common count is that of light rays, not of boundary modes; the argument uses only that $N$ is common):
\begin{enumerate}
\item[(i)] \emph{(Charge.)} The asymmetry stored in an oriented tower is the charge $Q = \epsilon N$, fixed by the descent's data and independent of the tower's temperature; it is not a thermal number $n - \bar{n} \propto g\,\mu T^{2}$. So the mirror share $f_{2} = 1$ holds at any mirror temperature: a cold mirror carries the same baryon charge as this tower in the same number of baryons, with negligible mirror radiation.
\item[(ii)] \emph{(Origin.)} The charge is the descent's and cannot be produced afterwards: the one channel superselection leaves open, gravitational production from the visible plasma (Appendix \ref{app:seeding}), yields $1.8$ to $2.7 \times 10^{-15}$ mirror quanta per unit entropy at the ceiling reheating against the $8.7 \times 10^{-11}$ baryons per unit entropy that our baryon number requires, more than four orders too few even counting every produced quantum as a baryon. Black holes are a sink for $Q$, not a source (Proposition \claimref{dark-matter.parallel-boundary-mode-spaces-one-wall}(iv), under P5): a mass-preserving rearrangement that erodes each tower's free baryon count and moves no share.
\item[(iii)] \emph{(Temperature.)} Taken as a free datum of the descent, which by Proposition \claimref{dark-tower-matter.mirrors-temperature-p2} is an exception to P2 (applied with the reach of Theorem \claimref{dark-matter.mirror-tower-copy-one}(iv), (v), P2 gives $\xi = 1$, which the record excludes), the mirror's temperature ratio $\xi = T'/T$ is bounded below by the gravitational floor, $\xi$ between $2.8$ and $3.2 \times 10^{-4}$ at the ceiling reheating (Proposition \claimref{dark-matter.coefficients-floors-they-give-what-gravity}(ii), the bracket the species-counting ambiguity; four parts in a thousand of this at the bottom of the ceiling range), and above by the $\Neff$ cap at $0.448$; a deposit of each unit of baryon number with energy of order the reheating temperature puts it at $\xi \approx 4 \times 10^{-3}$. The paper carries the whole interval. With $\eta = n_{B}/n_{\gamma} = 6.1 \times 10^{-10}$ here and equal baryon number,
\[
\eta' \;=\; \frac{\eta}{\xi^{3}}
\]
runs from $19$ to $26$ at the floor down to about $0.008$ at the hot deposit, crossing one at $\xi = \eta^{1/3} = 8.5 \times 10^{-4}$: at least $10^{7}$ times ours throughout, with $\Delta\Neff$ eight orders or more below the cap.
\item[(iv)] \emph{(The two readings.)} The thermal reading would give $f_{2} \sim \xi_{2}^{3}$ instead, at most $0.090$ under the $\Neff$ cap ($0.448^{3}$) and $10^{-7}$ or less anywhere in the interval; the two readings cannot both hold, and the paper's own classification decides for the charge.
\end{enumerate}
Level: the classification is Fact \claimref{dark-matter.imported-trichotomy-descents-data}'s; the incompatibility is arithmetic. The mirror's nucleosynthesis, which is not a copy of ours and on which the burning branch of Proposition \claimref{dark-matter.mirror-share-one-how-fragile}(i) and the composition caveat of refutation item 6 rest, follows the proof, at assembly level. Caveat (T14c): the proof's thermal up-down ratio at freeze-out fails at the floor, where the mirror is degenerate and, for a copied lepton number $L \leq 0$, ends $96$ to $100$ percent neutrons; it is helium only for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$, an interval containing the hot-deposit estimate (Computation \claimref{dark-tower-matter.mirrors-composition}). The burning branch is therefore not the floor's composition.

## technical
Under the classification in which the asymmetry $\epsilon$ is inherited initial data of the descent, with the number $N = M_{P}/H$ common to the towers under P1 (it fixes a count of light rays, about $\pi N^{2}/\ln 2$, rather than being it; the boundary-mode arrays per light ray depend on the tower), (i) the asymmetry stored in an oriented tower is the charge $Q = \epsilon N$, independent of temperature, not a thermal excess $n - \bar{n} \propto g\,\mu T^{2}$, so the mirror share $f_{2} = 1$ holds at any mirror temperature. (ii) The charge cannot be produced afterwards: gravitational production yields $1.8$ to $2.7 \times 10^{-15}$ quanta per unit entropy at the ceiling reheating against the $8.7 \times 10^{-11}$ baryons per unit entropy required, and black holes are a sink for $Q$, not a source, under P5.

(iii) Taken as a free datum of the descent, the mirror's temperature ratio $\xi$ lies between the gravitational floor, about $3 \times 10^{-4}$, and the $N_{\mathrm{eff}}$ cap at $0.448$, with a hot deposit putting it near $4 \times 10^{-3}$; the mirror baryon-to-photon ratio $\eta' = \eta/\xi^{3}$ is then at least $10^{7}$ times ours throughout. (iv) The thermal reading would give $f_{2} \sim \xi^{3} \le 0.090$, so the two readings cannot both hold, and the classification decides for the charge.

Caveats from the T14c note: a free $\xi$ is an exception to P2, which applied with the reach of the copy theorem gives $\xi = 1$ and $\Delta N_{\mathrm{eff}} = 7.45$ (Proposition \claimref{dark-tower-matter.mirrors-temperature-p2}); and the mirror is helium only for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$, while at the floor it is degenerate and neutron-rich (Computation \claimref{dark-tower-matter.mirrors-composition}), so the burning branch does not describe the floor.

## lay
Under the paper's classification, in which the mirror sector's small excess of matter over antimatter is inherited from the descent as initial data, and with the large number that fixes how many light rays the horizon has the same for every tower (Premise P1; how many boundary modes each light ray carries depends on the tower's content), that excess is fixed at the start, like a stored charge, rather than depending on how hot the sector is. That is why the mirror sector can hold exactly as much matter as ours while being far colder. Nothing that happens later can create more of it: gravitational production falls short by more than four orders of magnitude, and black holes, under Premise P5, can only remove it. A later note (T14c) adds two corrections: leaving the mirror's temperature free is an unstated exception to the paper's indifference principle, and at its coldest the mirror would end mostly as neutrons rather than helium.

## one-liner
Under the inherited-asymmetry classification, with the number $N$ (which fixes a count of light rays) common to the towers under P1, an oriented tower's asymmetry is the temperature-independent charge $Q = \epsilon N$, so the mirror share $f_{2} = 1$ holds at any mirror temperature.
