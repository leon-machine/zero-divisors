---
id: dark-matter.open-channels-their-costs
kind: claim
version: 6
title: The open channels, with their costs
status: proved
region: dark-matter
subject: dark-matter
tags: [mirror-sector, confronted-with-data, open-problem]
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
- name: Claude Opus 5.5
  role: 'maintainer pass on Leon''s decisions, the coefficient with the heaviest neutrino non-relativistic corrected to 6.43 with its check, and the cold-mirror exception sentence (correction)'
  version: 6
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  uses:
  - dark-matter.mirror-tower-copy-one@9
  - dark-matter.superselected-hence-dark-exactly-stable@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:prop:openchannel
- kind: check
  ref: check.py::check_mirror_radiation_and_threshold
- kind: check
  ref: check.py::check_five_dimensional_thresholds
- kind: check
  ref: check.py::check_route_a_colder_sector
locators:
  paper: T14
  number: Prop 6.3
  label: prop:openchannel
  line: 573
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.mirror-tower-copy-one repinned 8 -> 9 after reviewing its C1 restatement (clause (iv): the common ceiling and coupling are now Premise synthesis.common-ceiling-coupling-premise, P2 equating labels and not couplings; the share of one rests also on that premise; the caveat is reworded for P2''s version-1 reach), clauses (i) to (iii) and (v) unchanged in content; the use here holds as cited.'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Constant correction (DECISIONS A14): with the heaviest mirror neutrino non-relativistic the coefficient is (8/7)(11/4)^{4/3} + 2(3.044/3) = 4.4032046 + 2.0293333 = 6.4325379 (Fractions, by the check''s own brackets), not 6.40 (which counted the two relativistic neutrinos as 1 each, against the 3.044 used for the total); the threshold (0.3/6.43254)^{1/4} = 0.4647 is still 0.47. The formal says 6.43 (source_formal keeps the paper''s 6.40) and check_mirror_radiation_and_threshold asserted the old value: it now computes p + 2 NNU/3 in (6.432537, 6.432539) with threshold in (0.464712, 0.464713); runcheck passes. G1 (DECISIONS; R05 item 2): the cold-mirror exception now says that it is an exception to P2 at its version-1 reach, that P2 as scoped (version 2, labels not states) leaves xi free (synthesis.tower-charge-sector-label-temperature-not), and that the cold mirror then needs a non-equilibrium descent (synthesis.cold-mirror-needs-non-equilibrium-descent); P2 is unchanged by Leon''s answer 2, so the sentence stands.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: N_eff_tot 7.447 and threshold 0.448 (0.47 with one neutrino non-relativistic), five-dimensional thresholds 0.51 and 0.46, route (a) factor 2.51 and the 0.22/0.33 sums, by exact root brackets. Version 3 -> 4. Wording fix (Leon 2026-10-23): the margin of eight orders or more is stated up to the hot-deposit point estimate (xi = 4.24e-3), not across its whole bracket (formal). Check strengthened: thresholds, N_eff_tot, the hot-deposit margin and the route (a) values pinned to six figures; inputs moved to module level. Version 4 -> 5.'
  superseded_in_part_by:
  - dark-tower-matter.mirrors-temperature-p2
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 1
    note: 'Superseded in part by T14c Prop 8.2 (dark-tower-matter.mirrors-temperature-p2). The closing
      sentence of the mirror paragraph, "A cold mirror with our baryon number is what the framework predicts",
      is narrowed: the cold mirror holds only with its seeded temperature taken as a free datum, which
      is an exception to P2 (P2 with the copy theorem''s reach gives xi = 1, Delta N_eff = 7.45, excluded).
      The radiation formulas, thresholds and routes are unchanged. Original in source_formal.'
  source_formal: |-
    \emph{The mirror tower.} Its relativistic content is a copy of ours, so at recombination its radiation is $\rho'_{\mathrm{rad}} = (T'/T_{\gamma})^{4}\,\rho_{\mathrm{rad}}$ with $T'$ the mirror photon temperature and the same internal thermal history; in neutrino units the visible radiation is
    \[
    \Neff^{\mathrm{tot}} \;=\; \frac{8}{7}\left(\frac{11}{4}\right)^{4/3} + 3.044 \;=\; 7.447, \qquad\text{so}\qquad \Delta\Neff^{\mathrm{mirror}} \;=\; 7.447\left(\frac{T'}{T_{\gamma}}\right)^{4},
    \]
    and the Planck cap requires $T'/T_{\gamma} < 0.448$ (three relativistic mirror neutrinos; if the heaviest is non-relativistic at recombination, true for $T'/T_{\gamma}$ below about $0.3$ at our masses, the coefficient is $6.40$ and the threshold $0.47$; the paper carries the conservative figure). A copy releases the same entropy as ours at the same epochs, so this ratio is the ratio \emph{seeded at the descent} (the copied history fails at the mirror's nucleosynthesis near the floor, where burning reheats its plasma by $3.0$ to $3.2$, Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}; the bound is met by eight orders or more on either reading): route (a) below does not arise for the mirror, and the descent must have heated it to less than $0.448$ of the visible temperature, the standard requirement of mirror-matter cosmology \cite{FootMirror2004}. The structure meets it with one datum: after the descent the mirror is heated only through the shared metric (Proposition \claimref{dark-matter.superselected-hence-dark-exactly-stable}), which puts its temperature at a floor of about three parts in ten thousand of ours at the top of the ceiling range (Proposition \claimref{dark-matter.coefficients-floors-they-give-what-gravity}(ii); $1.1 \times 10^{-3}$ even for a coefficient of ten, beyond the mirror's content), and above the floor the deposit sets it, near four parts in a thousand on the paper's estimate (Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}). A cold mirror with our baryon number is what the framework predicts.

    \emph{The five-dimensional towers.} A massless abelian species surviving in tower $r$ at temperature $T_{r}$ with $g_{r}$ light polarisations contributes
    \[
    \Delta\Neff \;=\; g_{r}\,\frac{4}{7}\left(\frac{11}{4}\right)^{4/3}\left(\frac{T_{r}}{T_{\gamma}}\right)^{4} \;\approx\; 2.2\,g_{r}\left(\frac{T_{r}}{T_{\gamma}}\right)^{4}
    \]
    ($g_{r} = 2$ for a four-dimensional photon or a five-dimensional zero mode, $3$ if a fifth component is light). The cap $\Delta\Neff \lesssim 0.3$ is met by one such species if and only if $T_{r}/T_{\gamma} \lesssim (0.3/2.2\,g_{r})^{1/4}$, that is, $0.51$ for $g_{r} = 2$ and $0.46$ for $g_{r} = 3$, and by several jointly if their sum is under the cap.

    Three routes close a channel, none proved here. (a) The sector is colder than the photons by a factor of about two, as a sector decoupled and releasing less entropy than ours is: the visible entropy release from the GeV epoch to today heats the photons relative to such a sector by $(g_{*}(\mathrm{GeV})/g_{*}(\mathrm{now}))^{1/3} \approx 2.51$, giving $\Delta\Neff \approx 0.11$ per two-polarisation species, so the two five-dimensional towers sit at $0.22$ with two light polarisations each, under the cap, and at $0.33$ with three, over it; a sector decoupled since the descent is colder still. (b) The abelian factor is Higgsed by the tower's own condensate, whenever that condensate carries the charge (this tower's neutral condensate is the accident that leaves our photon massless). (c) The rung-level charges, or the intrinsic $U(1)$, are not gauged in that tower once its content is derived as this tower's was. Route (a) is a thermal-history computation, (b) and (c) content derivations; all three are successor problem (1).

    Observation level; the stance $\Delta\Neff \approx 0$ is registered conditional on them and on the mirror's seeded temperature.
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.mirror-tower-copy-one
    - dark-matter.superselected-hence-dark-exactly-stable
    note: 'Added the mirror-copy theorem (the mirror''s relativistic content) and superselection (heating
      only through the metric); the floor and deposit values from the coefficients and stored-asymmetry
      propositions are real premises of the mirror paragraph but were not added because the coefficients
      claim already uses this one, so either edge would close a cycle; the 0.448 bound is the standard
      mirror-matter requirement (Foot), which is not in the store as an imported claim, so no standard
      route. Levels pass: the lay level now marks the no-extra-radiation stance as conditional on the
      unproved routes and the mirror''s seeded temperature, at observation level, and says the mirror''s
      coldness rests on the paper''s estimates.'
  env: proposition
  context_refs:
  - dark-matter.coefficients-floors-they-give-what-gravity
  - dark-matter.stored-asymmetry-charge-not-number
  - dark-matter.superselected-hence-dark-exactly-stable
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.mirror-tower-copy-one
    stated_role:
    - dark-matter.superselected-hence-dark-exactly-stable
---

## formal
\emph{The mirror tower.} Its relativistic content is a copy of ours, so at recombination its radiation is $\rho'_{\mathrm{rad}} = (T'/T_{\gamma})^{4}\,\rho_{\mathrm{rad}}$ with $T'$ the mirror photon temperature and the same internal thermal history; in neutrino units the visible radiation is
\[
\Neff^{\mathrm{tot}} \;=\; \frac{8}{7}\left(\frac{11}{4}\right)^{4/3} + 3.044 \;=\; 7.447, \qquad\text{so}\qquad \Delta\Neff^{\mathrm{mirror}} \;=\; 7.447\left(\frac{T'}{T_{\gamma}}\right)^{4},
\]
and the Planck cap requires $T'/T_{\gamma} < 0.448$ (three relativistic mirror neutrinos; if the heaviest is non-relativistic at recombination, true for $T'/T_{\gamma}$ below about $0.3$ at our masses, the coefficient is $6.43$ and the threshold $0.47$; the paper carries the conservative figure). A copy releases the same entropy as ours at the same epochs, so this ratio is the ratio \emph{seeded at the descent} (the copied history fails at the mirror's nucleosynthesis near the floor, where burning reheats its plasma by $3.0$ to $3.2$, Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}; the bound is met on either reading, by eight orders or more up to the hot-deposit point estimate of that Proposition): route (a) below does not arise for the mirror, and the descent must have heated it to less than $0.448$ of the visible temperature, the standard requirement of mirror-matter cosmology \cite{FootMirror2004}. The structure meets it with one datum: after the descent the mirror is heated only through the shared metric (Proposition \claimref{dark-matter.superselected-hence-dark-exactly-stable}), which puts its temperature at a floor of about three parts in ten thousand of ours at the top of the ceiling range (Proposition \claimref{dark-matter.coefficients-floors-they-give-what-gravity}(ii); $1.1 \times 10^{-3}$ even for a coefficient of ten, beyond the mirror's content), and above the floor the deposit sets it, near four parts in a thousand on the paper's estimate (Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}). A cold mirror with our baryon number is what the framework predicts once that seeded temperature is taken as a free datum of the descent; by Proposition \claimref{dark-tower-matter.mirrors-temperature-p2} this is an exception to P2, which, applied with the reach of Theorem \claimref{dark-matter.mirror-tower-copy-one}(iv), (v), gives $T'/T_{\gamma} = 1$ and $\Delta\Neff = 7.45$, excluded by the cap above. This is an exception to P2 at its version-1 reach; P2 as scoped leaves $\xi$ free (Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}), and the cold mirror then needs a non-equilibrium descent (Proposition \claimref{synthesis.cold-mirror-needs-non-equilibrium-descent}).

\emph{The five-dimensional towers.} A massless abelian species surviving in tower $r$ at temperature $T_{r}$ with $g_{r}$ light polarisations contributes
\[
\Delta\Neff \;=\; g_{r}\,\frac{4}{7}\left(\frac{11}{4}\right)^{4/3}\left(\frac{T_{r}}{T_{\gamma}}\right)^{4} \;\approx\; 2.2\,g_{r}\left(\frac{T_{r}}{T_{\gamma}}\right)^{4}
\]
($g_{r} = 2$ for a four-dimensional photon or a five-dimensional zero mode, $3$ if a fifth component is light). The cap $\Delta\Neff \lesssim 0.3$ is met by one such species if and only if $T_{r}/T_{\gamma} \lesssim (0.3/2.2\,g_{r})^{1/4}$, that is, $0.51$ for $g_{r} = 2$ and $0.46$ for $g_{r} = 3$, and by several jointly if their sum is under the cap.

Three routes close a channel, none proved here. (a) The sector is colder than the photons by a factor of about two, as a sector decoupled and releasing less entropy than ours is: the visible entropy release from the GeV epoch to today heats the photons relative to such a sector by $(g_{*}(\mathrm{GeV})/g_{*}(\mathrm{now}))^{1/3} \approx 2.51$, giving $\Delta\Neff \approx 0.11$ per two-polarisation species, so the two five-dimensional towers sit at $0.22$ with two light polarisations each, under the cap, and at $0.33$ with three, over it; a sector decoupled since the descent is colder still. (b) The abelian factor is Higgsed by the tower's own condensate, whenever that condensate carries the charge (this tower's neutral condensate is the accident that leaves our photon massless). (c) The rung-level charges, or the intrinsic $U(1)$, are not gauged in that tower once its content is derived as this tower's was. Route (a) is a thermal-history computation, (b) and (c) content derivations; all three are successor problem (1).

Observation level; the stance $\Delta\Neff \approx 0$ is registered conditional on them and on the mirror's seeded temperature.

## technical
For the mirror tower, whose relativistic content copies ours, the radiation in neutrino units is $N_{\mathrm{eff}}^{\mathrm{tot}} = \frac{8}{7}\left(\frac{11}{4}\right)^{4/3} + 3.044 = 7.447$, so $\Delta N_{\mathrm{eff}}^{\mathrm{mirror}} = 7.447\,(T'/T_{\gamma})^{4}$ and the Planck cap requires $T'/T_{\gamma} < 0.448$, the standard requirement of mirror-matter cosmology. Since a copy releases entropy as ours does, this is the ratio seeded at the descent. After the descent the mirror is heated only through the shared metric, which puts it at a floor of about three parts in ten thousand of our temperature at the top of the ceiling range, with the deposit setting it near four parts in a thousand on the paper's estimate. Caveat (T14c): that cold mirror takes the seeded temperature as a free datum, an unstated exception to indifference, which applied with the copy theorem's reach gives $T'/T_{\gamma} = 1$ and $\Delta N_{\mathrm{eff}} = 7.45$, over the cap (Proposition \claimref{dark-tower-matter.mirrors-temperature-p2}). That is an exception to indifference at its version-1 reach; indifference as scoped (labels, not states) leaves $\xi$ free (Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}), and the cold mirror then needs a non-equilibrium descent (Proposition \claimref{synthesis.cold-mirror-needs-non-equilibrium-descent}).

For a massless abelian species in tower $r$ with $g_{r}$ light polarisations, $\Delta N_{\mathrm{eff}} \approx 2.2\,g_{r}(T_{r}/T_{\gamma})^{4}$, so the cap $\Delta N_{\mathrm{eff}} \lesssim 0.3$ needs $T_{r}/T_{\gamma} \lesssim 0.51$ for $g_{r} = 2$ and $0.46$ for $g_{r} = 3$. Three routes would close such a channel, none proved here: the sector is colder by the entropy-release factor of about $2.51$, its abelian factor is Higgsed by its own condensate, or its charges are not gauged. The stance $\Delta N_{\mathrm{eff}} \approx 0$ is registered conditional on these routes and on the mirror's seeded temperature, at observation level.

## lay
Hidden copies of ordinary matter would carry their own kinds of light, and the cosmic microwave background tightly limits how much extra light the early universe could hold. This result works out how cold each hidden sector must be to stay within that limit: a mirror copy of our world must be below about 45 per cent of our temperature, and on the paper's estimates, with the mirror heated after the descent only through gravity, it sits far below that; a later note (T14c) points out that this coldness is an unstated exception to the paper's indifference principle, which applied evenly would make the mirror as hot as our world. As the principle is now scoped, it applies to labels such as charges and not to temperatures, so it leaves the mirror's temperature free; a cold mirror then needs the descent to have left the towers out of equilibrium. For the five-dimensional sectors it lists three ways the problem could be avoided, none of them yet proved, so the expectation of no extra light is conditional on those routes and on the mirror's starting temperature, and is held at observation level.

## one-liner
The mirror tower adds $\Delta N_{\mathrm{eff}} = 7.447\,(T'/T_{\gamma})^{4}$, safe below $T'/T_{\gamma} = 0.448$, while a five-dimensional tower's light abelian species stays under the cap only if one of three unproved routes closes it.
