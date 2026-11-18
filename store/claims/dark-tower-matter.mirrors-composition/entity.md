---
id: dark-tower-matter.mirrors-composition
kind: claim
version: 5
title: The mirror's composition across its temperature range
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [mirror-sector, matter-asymmetry]
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
  role: 'restatement: clause (i) is stated at the temperature ratio at which it was computed, which was the gravitational floor with the first imported production coefficients and is below the present floor; the quoted floor and its eta-prime corrected'
  version: 4
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-navigate)'
- name: Claude Fable 5.2
  role: 'restatement of the quoted present floor (5.2e-4 -> 6.6e-4) and of the quoted baryon-to-photon ratio at the floor (4.4 -> 2.1), after the floor was defined with the mean energy per creation event; no number of clauses (i) to (iii) changed; then clause (i) restated at the present floor from a second run of the supplementary scripts (still neutron-rich for L <= 0, 83 to 96 percent neutrons, only moderately degenerate)'
  version: 5
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-leads)'
amendments:
- version: 5
  kind: restatement
  defect: 'the statement quoted the present gravitational floor as 5.2e-4 and the mirror''s baryon-to-photon ratio there as 4.4, values at the convention of energy 3T per creation event; at the mean energy per event the floor is 6.6e-4 and the ratio 2.1. Clause (i) stays stated at xi = 2.8 to 3.2e-4, where it was computed, and is still not recomputed at the present floor. Follow-up of the same day: the supplementary scripts were run again with 6.6e-4 added to their grids, and clause (i) no longer says that it is not recomputed there; at the present floor the mirror is still neutron-rich for L <= 0 (96 percent neutrons at L/B = -51/28, 83 percent at L = 0) but the Fermi energy exceeds the thermal deposit by 2.7 and not by 49 to 84, and the quark chemical potential is 3.5 to 3.7 times the temperature and not 18 to 23, so charge-dominated and degenerate from seeding holds there only in a weaker form'
- version: 4
  kind: restatement
  defect: 'clause (i) and the one-liner placed the neutron-rich endpoint at the gravitational floor and quoted the floor as 2.8 to 3.2e-4 with eta'' = 19 to 26; those were the floor''s values at production coefficients that were too small, the floor at the top of the ceiling range is now 5.2e-4 with eta'' = 4.4, and the computation of (i) was made at 2.8 to 3.2e-4 and has not been repeated at 5.2e-4'
review: typed
derivations:
- name: main
  uses:
  - dark-matter.stored-asymmetry-charge-not-number@13
  - dark-matter.seeding-gravity-floor-dark-towers-temperature@6
  - dark-matter.mirror-tower-copy-one@11
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_sphaleron_lepton_to_baryon
lineage:
  supersedes:
  - dark-matter.mirror-share-one-how-fragile
  - dark-matter.stored-asymmetry-charge-not-number
  - simulations.imported-mirror
locators:
  paper: T14c
  number: Comp 8.3
  label: comp:mirror
  line: 770
extraction:
  maintainer_pass_2026_11_18_energy:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 4 -> 5, at Leon''s decision of 18 November 2026, 14:04 (adopt the computed mean energy per creation event in the gravitational floor). Quoted numbers only: the present floor 5.2e-4 -> 6.6e-4 at every level and in the proof text; the floor value of eta'' 4.4 -> 2.1. No number of clauses (i) to (iii) changed. Clause (i) remains stated at xi = 2.8 to 3.2e-4 (the floor for a reheating between about 1.9e14 and 2.3e14 GeV on the present formula) and was not recomputed at 6.6e-4 on this pass (see the follow-up below). The present floor still lies between the values computed in (i) and the helium interval of (ii). No check of this entity bears on the change, so no amendment evidence is named. The two premises restated the same day are repinned. Follow-up, same day, version kept at 5: clause (i) is now recomputed at the present floor. The papers suite''s two supplementary scripts (the mirror''s and the cosmology check''s) were staged and run in the workspace with one line changed in each, the grid of xi gaining 5.2e-4, 6.6e-4 and 8.1e-4 (the mirror''s script: 24 checks, 0 failures); the outputs are kept in that run''s work/housekeeping folder (MIR_rerun_extended_grid_output.txt, CHECK_COS_rerun_extended_grid_output.txt). At 6.6e-4: Fermi energy over thermal deposit 2.7; quark chemical potential over temperature 3.5 at seeding and 3.7 at T'' near 0.4 GeV; neutron fraction 0.957 (L/B = -51/28) and 0.832 (L = 0); on the helium branch the bottleneck at 0.185 MeV with eta'' = 2.13 and a burning reheat of 1.86. The clause keeps its figures at 2.8 to 3.2e-4 and adds these; the words charge-dominated and degenerate from the moment it is seeded are kept for the lower values and weakened at the present floor. The scripts are not in the store, so no check is added (coverage.yaml says so), and the composition after decay and capture is still not computed.'
  maintainer_pass_2026_11_18:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 3 -> 4, at Leon''s decision of 18 November 2026 (restate the numbers that used the first published production coefficients). The supplementary scripts behind clause (i) are not in the lab, so (i) could not be recomputed at the present floor 5.2e-4; it is restated as holding at xi = 2.8 to 3.2e-4, where it was computed, which is the floor for a reheating below the top of the ceiling range. No number of (i) to (iii) is changed. For the maintainer, not part of the statement: the two stored ends 49 and 84 of the Fermi-energy ratio follow xi^-4 ((3.2/2.8)^4 = 1.71 = 84/49), which would put that ratio near 7 at 5.2e-4; the freeze-out ratio 18 to 23 and the neutron fraction do not follow a simple power and need the scripts. No amendment evidence is named because the entity''s one check does not bear on the change. Premises repinned to their versions of the same day.'
  maintainer_pass_2026_11_12:
    by: maintainer-2026-11-12
    date: '2026-11-12'
    note: 'Scope note, version kept, no statement changed (Leon''s decision of 12 November 2026: the inherited charge is B - L). The computation takes the mirror''s baryon number equal to this tower''s and a copied lepton number L <= 0 (this tower''s equilibrium value L/B = -51/28 with one light doublet, or zero). With B - L the copied datum, both inputs are conditional: the equal baryon number is the hypothesis of equal conversion (the mirror''s ratio of baryon number to B - L equals this tower''s; not shown; attack item (d) of op.matter-asymmetry-origin; Proposition dark-matter.stored-asymmetry-charge-not-number (i), version 11), and the split of the mirror''s B - L between B and L is not fixed by the copy. The statement and the check are unchanged (the check keeps the one-doublet equilibrium; the number of light doublets, 28/79 against 8/23, is attack item (a) of the same open problem).'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.stored-asymmetry-charge-not-number repinned 8 -> 9 after reviewing its G1 restatement (the cold mirror is an exception to P2 at its version-1 reach, P2 as scoped leaves xi free, and the cold mirror then needs a non-equilibrium descent; the charge reading and the numbers are unchanged); the use here holds as cited. Pin review: dark-matter.mirror-tower-copy-one repinned 8 -> 9 after reviewing its C1 restatement (clause (iv): the common ceiling and coupling are now Premise synthesis.common-ceiling-coupling-premise, P2 equating labels and not couplings; the share of one rests also on that premise; the caveat is reworded for P2''s version-1 reach), clauses (i) to (iii) and (v) unchanged in content; the use here holds as cited.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the sphaleron value L/B = -51/28 from the equilibrium conditions. Version 2 -> 3.'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 1
    note: 'Lineage supersedes added (decision 1, CONTRADICTIONS_VALUES H2): the helium composition at the floor
      on the burning branch (the stored-asymmetry proposition''s nucleosynthesis, the T14b restatement of
      the mirror) and the 0.995 to 1 bracket of the fragility proposition (i) that rests on it, each narrowed
      and carrying a caveat that cites this result. Lineage is unpinned in the store schema; the uses pins
      are left for the maintainer.'
  env: computation
  flags:
  - no proof environment found
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.mirror-tower-copy-one
    - dark-matter.seeding-gravity-floor-dark-towers-temperature
    - dark-matter.stored-asymmetry-charge-not-number
    note: 'E107 fix: the computation has no proof environment; it is computed in the supplementary MIR
      and CHECK_COS scripts from the dark-matter paper''s temperature range (its asymmetry and gravitational-floor
      propositions) and its copy theorem, so those were made its edges with a provenance-only proof file.
      Kept proved as a decimal computation; no legacy evidence could be attached, because the paper''s
      script reaches MIR only through the untagged Part L line ''L MIR/verify_MIR.py runs cleanly''. Levels
      pass: levels written from scratch, keeping every condition and level qualifier of the formal statement.'
---

## formal
Decimal. Supplementary scripts: the mirror's (folder \file{MIR}, checks D1, D2 and E0 to E7) and the cosmology check's (folder \file{CHECK\_COS}). T14 carries $\xi$ from the gravitational floor to the $\Neff$ cap ($0.448$), with a hot-deposit estimate near $4 \times 10^{-3}$. At the top of the ceiling range the floor was $2.8$ to $3.2 \times 10^{-4}$ with the production coefficients first imported, and the computation below was first made there; with the derived coefficients and the mean energy per creation event it is $6.6 \times 10^{-4}$ (Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}(iii)), and the two scripts were run again on 18 November 2026 with that value added to their grids.
\begin{enumerate}
\item[(i)] At $\xi = 2.8$ to $3.2 \times 10^{-4}$, the floor when this was computed and now the floor for a reheating below the top of the ceiling range (the floor goes as $T_{\mathrm{desc}}^{3/4}$), the mirror is charge-dominated and degenerate from the moment it is seeded: the Fermi energy its deposited baryon number must carry exceeds the thermal deposit there by $49$ to $84$, and at its weak freeze-out the quark chemical potential is $18$ to $23$ times its temperature. Beta equilibrium persists into the hadron phase, and for a copied lepton number $L \leq 0$ (our tower's sphaleron value $L/B = -51/28$, or zero) the mirror ends $96$ to $100$ percent neutrons. At $\xi = 6.6 \times 10^{-4}$, the present floor at the top of the ceiling range, the same scripts give a mirror that is still neutron-rich for $L \leq 0$ but only moderately degenerate: the Fermi energy exceeds the thermal deposit by $2.7$, the quark chemical potential is $3.5$ times the temperature at seeding and $3.7$ times at $T' \approx 0.4$ GeV (the quantity that is $18$ to $23$ at the lower values), beta equilibrium still lasts into the hadron phase, and the mirror ends $96$ percent neutrons for $L/B = -51/28$ and $83$ percent for $L = 0$. So ``charge-dominated and degenerate from the moment it is seeded'' holds at $\xi = 2.8$ to $3.2 \times 10^{-4}$ and holds at the present floor only in this weaker form: the charge still dominates, by a factor near three and not by fifty or more. At either value the endpoint is cold, dense, neutron-rich matter; the composition after decay and capture needs a dense-matter network and is not computed here.
\item[(ii)] Between $\xi \approx 3 \times 10^{-3}$ and $2 \times 10^{-2}$, an interval containing T14's hot-deposit estimate, the mirror is helium ($Y' = 0.94$ to $1.00$).
\item[(iii)] Above that interval the helium fraction falls ($Y' = 0.85$ at $\xi = 0.1$) and towards the cap the mirror is hydrogen-rich ($Y' = 0.58$ at $\xi = 0.448$).
\end{enumerate}
T14 does not print a mirror $\eta'$ at freeze-out; its floor value ($19$ to $26$ as printed, $2.1$ with the derived coefficients and the mean energy per creation event) is the late-time ratio, and the thermal up-down ratio T14 assumes there is inconsistent with its own $\eta' > 1$.

## technical
A decimal computation across the dark-matter paper's range of the mirror temperature ratio $\xi = T'/T$, from the gravitational floor to the $\Neff$ cap ($0.448$), with a hot-deposit estimate near $4 \times 10^{-3}$; the floor at the top of the ceiling range was $2.8$ to $3.2 \times 10^{-4}$ when this was computed and is $6.6 \times 10^{-4}$ with the production coefficients and the energy per creation event since derived. (i) At $\xi = 2.8$ to $3.2 \times 10^{-4}$ the mirror is charge-dominated and degenerate from the moment it is seeded: the Fermi energy its baryon number must carry exceeds the thermal deposit there by $49$ to $84$, the quark chemical potential at weak freeze-out is $18$ to $23$ times the temperature, and for a copied lepton number $L \leq 0$ it ends $96$ to $100$ percent neutrons, cold, dense and neutron-rich. At the present floor, $6.6 \times 10^{-4}$ (the scripts rerun on 18 November 2026 with that value added), it is still neutron-rich for $L \leq 0$, $83$ to $96$ percent neutrons, but only moderately degenerate: the Fermi energy exceeds the thermal deposit by $2.7$ and the quark chemical potential is $3.5$ to $3.7$ times the temperature. The composition after decay and capture is not computed at either value. (ii) For $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$ the mirror is helium, $Y' = 0.94$ to $1.00$. (iii) Above that the helium fraction falls, to $Y' = 0.85$ at $\xi = 0.1$ and $0.58$ at $\xi = 0.448$.

The dark-matter paper's floor value of $\eta'$ ($19$ to $26$ as printed, $2.1$ with the derived coefficients and the mean energy per creation event) is a late-time ratio, and the thermal up-down ratio it assumes there is inconsistent with its own $\eta' > 1$.

## lay
The mirror tower copies our physics, so what its matter becomes depends mainly on how hot it was compared with our world. These decimal estimates show that if it was as cold as gravity alone was first estimated to allow, it ends as dense neutron-rich matter, and at the somewhat warmer minimum that the revised estimate gives it still ends mostly as neutrons (between about five in six and nearly all, depending on its leptons), though it is then squeezed far less tightly; if it was moderately warm, it is almost pure helium; and if it was near the radiation limit, it is mostly hydrogen. The coldest case is not followed to its final composition.

## one-liner
In decimal estimates the mirror ends neutron-rich for $L \leq 0$ both at $\xi = 2.8$ to $3.2 \times 10^{-4}$ (the gravitational floor when first computed; $96$ to $100$ percent neutrons, strongly degenerate) and at the present floor $6.6 \times 10^{-4}$ ($83$ to $96$ percent, moderately degenerate), helium for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$, and hydrogen-rich towards the $\Neff$ cap.
