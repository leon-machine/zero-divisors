---
id: dark-tower-matter.five-dimensional-towers
kind: claim
version: 6
title: The five-dimensional towers in cosmology and halos
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [halos-and-clusters, confronted-with-data]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
- name: Claude Fable 5.2
  role: 'the depth of the fifth direction named as the particle model''s length; R1 and R2 assumed'
  version: 5
  source: maintainer pass of 2026-11-19
- name: Claude Opus 5.5
  role: 'restated to the deposited text of T14c version 1.0 (10.5281/zenodo.24403592)'
  version: 6
  source: maintainer pass of 2026-11-20
amendments:
- version: 5
  kind: restatement
  defect: 'the statement took the fifth direction one cell radius deep, about a metre, on R3 alone; R3''s unit is the length of Premise E, which is this world''s baryon spacing only under R1 and R2'
review: typed
derivations:
- name: main
  uses:
  - dark-tower-matter.gauge-algebras@5
  - dark-tower-matter.five-dimensional-content@5
  assumes:
  - dark-tower-matter.u-transposition-rule@4
  - dark-matter.r1-equal-mass-per-quantum@1
  - dark-matter.r2-one-quantum-per-unit-ball@3
  - dark-matter.r3-one-cell-per-unshared-direction@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:K5
  - id:K6
  - id:K7
- kind: check
  ref: check.py::check_five_dimensional_at_every_epoch
- kind: check
  ref: check.py::check_confinement_scale_negligible
locators:
  paper: T14c
  number: Comp 9.3
  label: prop:fiveD
  line: 786
extraction:
  maintainer_pass:
    by: maintainer-2026-11-20
    date: '2026-11-20'
    note: 'The formal level restated: T14c deposited as version 1.0 on 20 November 2026 (10.5281/zenodo.24403592), after an independent review: the dependence on the particle model''s depth made a stated condition with edges to R1, R2 and R3 (it was a dated note); the plasma checks named I3 and I4; renumbered Computation 9.3. Version 5 -> 6. The technical level restated: as the formal level.'
  maintainer_pass_2026_11_19:
    by: maintainer-2026-11-19
    date: '2026-11-19'
    note: 'Version 4 -> 5. Leon''s decision of 19 November 2026 (R3''s unit is the length of Premise E): the statement used a depth of about a metre, this world''s baryon spacing, on R3 alone. Assumes edges to R1 and R2 are added, since that value is the particle model''s, and a marked note says so. No number changed.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: L T from 385-395 to 1150-1180 above 120 pi, and the K7 confinement exponent in (280, 290). Version 2 -> 3. Check strengthened: integer parts of L T today (1166), early (387) and early L T/pi (123) pinned against by-hand values; g_s inputs and stated brackets moved to module level. Version 3 -> 4.'
  env: proposition
  context_refs:
  - dark-matter.open-channels-their-costs
  - dark-tower-matter.five-dimensional-content
  outside_pilot_cites:
  - ButlerT14
  flags:
  - no proof environment found
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.r3-one-cell-per-unshared-direction
    - dark-tower-matter.five-dimensional-content
    - dark-tower-matter.gauge-algebras
    note: 'E107 fix: the proposition has no proof environment; it is a decimal assembly of the gauge algebra,
      the content, premise R3 and (for (vi)) Premise U, so these were made its edges with a cites-only
      proof file. The zero-mode formula of the dark-matter paper (open channels) is corrected here, not
      used, so it was not added; the two dark-matter remarks it cites are notes and cannot be premises.
      Referee: the 670 figure differs from CHECK_COS (1.6e3), and K7 prints exp(-287) against the stated
      e^-250 (true but loose). Levels pass: levels written from scratch, keeping every condition and level
      qualifier of the formal statement.'
---

## formal
Decimal, with imports as stated. With the fifth direction one $d$ deep and co-expanding (R3), and $d = d_{b}$ (the particle model, R1 and R2; \cite[Prem.~7.4, Rem.~7.9, Rem.~7.14]{ButlerT14}). Under E alone the depth has no stated value, and the numbers below are conditional on the particle model's:
\begin{enumerate}
\item[(i)] $LT$ runs from about $390$ (at $g_{s} = 106.75$) to $1170$ today: the Kaluza-Klein spacing is always below $T/120$, so the towers are five-dimensional at the visible temperature and at their matter's mass scale (K5); at T14's small dark temperatures the dark bath itself is only a few Kaluza-Klein levels deep.
\item[(ii)] Five-dimensional gauge theory is infrared free; reducing to four dimensions gives a confinement scale below $\pi/L$ by a factor smaller than $e^{-250}$ even at strong coupling (K7), and the $1/r^{2}$ potential binds nothing unless the theory is within a factor of about eight of strong coupling at the quark mass (supplementary \file{D5C}, H3; \cite{CLP2000}). There are no dark hadrons and no dark atoms.
\item[(iii)] With the Kaluza-Klein tower populated, $\Delta\Neff < 0.3$ needs $T_{D}/T_{\gamma} < 0.085$ for the nine vectors of $\uu(3)$ ($0.13$ for one photon), not the $0.46$ to $0.51$ of T14's zero-mode formula \cite[Prop.~6.3]{ButlerT14}; a sector decoupled at a GeV would give about $670$ (K6). T14's own temperature estimates meet the corrected bound by orders.
\item[(iv)] Two-body scattering is collisionless by geometry, $\sigma_{\mathrm{eff}}/m = \sigma_{5}/(Lm) < 10^{-8}\ \mathrm{cm^{2}\,g^{-1}}$ even for charged and coloured species (supplementary \file{D5C}, H9).
\item[(v)] With no boundary term in the series the gauge field's natural condition at the ends of the fifth direction keeps a four-dimensional zero mode, so beyond about a metre the charged species form a neutral dark plasma. Published plasma-instability limits \cite{SSS2024, PIC2024}, rescaled to a GeV, lie six to ten orders below the coupling a freeze-out relic needs and about two to five orders below a deposit at a natural five-dimensional coupling (supplementary \file{D5C}, checks I3 and I4, and \file{CHECK\_COS}). Whether such instabilities transfer bulk momentum in a merger is not established \cite{Lasenby2020}: an exposure, not an exclusion.
\item[(vi)] If the neutral species $N$ (Proposition \claimref{dark-tower-matter.five-dimensional-content}) carries the particle model's count as a deposit and the charged species annihilate at weak coupling, the tower carries no long-range charge and is collisionless whatever the zero modes do. Under Premise \claimref{dark-tower-matter.u-transposition-rule} this branch is open to both five-dimensional towers.
\end{enumerate}
The relic is a symmetric gas of free spin-$\tfrac{1}{2}$ dark quarks and leptons, or of $N$ alone. The lightest species is stable by fermion parity, the lightest quark and lepton by species numbers broken only at the rung scale.

## technical
Decimal estimates with imported physics, taking the fifth direction one cell radius deep and co-expanding (premise R3), the cell radius being this world's baryon spacing of about a metre, which is the particle model's value (R1 and R2) and not fixed by equal mass per unit ball alone. (i) $LT$ runs from about $390$ to $1170$, so the Kaluza-Klein spacing stays below $T/120$ and the towers are five-dimensional at the visible temperature and at their matter's mass scale, while at small dark temperatures the dark bath is only a few levels deep. (ii) Five-dimensional gauge theory is infrared free: the reduced confinement scale lies below $\pi/L$ by a factor smaller than $e^{-250}$ even at strong coupling, and the $1/r^2$ potential binds nothing unless the theory is within about a factor eight of strong coupling, so there are no dark hadrons or atoms. (iii) With the Kaluza-Klein tower populated, $\Delta\Neff < 0.3$ needs $T_D/T_\gamma < 0.085$ for the nine vectors of $\uu(3)$, not the zero-mode $0.46$ to $0.51$; a sector decoupled at a GeV would give about $670$.

(iv) Two-body scattering is collisionless by geometry, $\sigma_{\mathrm{eff}}/m < 10^{-8}\ \mathrm{cm^2\,g^{-1}}$. (v) With no boundary term a four-dimensional zero mode survives and the charged species form a neutral dark plasma, an exposure to plasma-instability limits, not an exclusion. (vi) If the neutral species $N$ carries the particle model's count and the charged species annihilate at weak coupling, the tower is collisionless; under Premise U this branch is open to both towers. The relic is a symmetric gas of free spin-$\tfrac12$ species, or of $N$ alone.

## lay
Assuming, with premise R3, that the extra direction is about one particle spacing deep and grows with the universe, these decimal estimates describe what the five-dimensional towers' matter does. Their forces never confine, so there are no dark nuclei or atoms; their radiation is small enough for the temperatures the dark-matter paper estimates; and their particles barely scatter. Their charged particles could form a dark plasma, a possible weakness, unless only the neutral species survives in the needed numbers, a branch open to both towers under the transposition rule.

## one-liner
Under R3 the five-dimensional towers stay five-dimensional, confine nothing, meet the radiation bound for $T_D/T_\gamma < 0.085$ and scatter negligibly, and under U both may hold only the neutral species.
