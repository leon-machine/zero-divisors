---
id: simulations.imported-mirror
kind: claim
version: 8
title: 'Imported: the mirror'
status: proved
region: simulations
subject: dark-matter
tags: [mirror-sector]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14b, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass on Leon''s decisions, the cold-mirror exception stated at P2''s version-1 reach, with P2 as scoped leaving xi free'
  version: 6
  source: maintainer pass 2026-11-07 (decisions)
- name: Claude Fable 5.2
  role: 'restatement of the quoted gravitational floor after the production coefficients were corrected, with the composition at the floor marked as computed at the printed floor only'
  version: 7
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-navigate)'
- name: Claude Fable 5.2
  role: 'restatement of the quoted gravitational floor (5.2e-4 -> 6.6e-4) after the floor was defined with the mean energy per creation event; share, hot deposit, helium interval and cross-sections unchanged; then the composition at the present floor stated from the rerun recorded in the composition Computation (still neutron-rich for L <= 0, 83 to 96 percent neutrons)'
  version: 8
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-leads)'
amendments:
- version: 8
  kind: restatement
  defect: 'the formal and technical levels and the proof text quoted the gravitational floor as 5.2e-4, its value at the convention of energy 3T per creation event; with the mean energy per event of the rate integral, about 7.9 T, the floor is 6.6e-4 and the mirror''s baryon-to-photon ratio at the floor is 2.1 where the check had 4.36. Follow-up of the same day: the statement said the neutron-rich composition was not recomputed at the present floor; it is now, and at 6.6e-4 the mirror ends 83 to 96 percent neutrons for L <= 0 and is only moderately degenerate, where 96 to 100 percent and a degenerate plasma hold at the printed floor'
  evidence: check.py::check_temperature_ratio_interval
- version: 7
  kind: restatement
  defect: 'the restated range of the mirror''s temperature ratio began at the gravitational floor 2.8 to 3.2e-4, the dark-matter paper''s printed value, computed with production coefficients that were too small; at the derived coefficients the floor is 5.2e-4, and the neutron-rich composition quoted at the floor was computed at the printed value'
  evidence: check.py::check_temperature_ratio_interval
review: typed
derivations:
- name: main
  uses:
  - dark-matter.mirror-share-one-how-fragile@10
  - dark-matter.mirror-tower-copy-one@11
  - dark-matter.radiation-audit-what-theorem-closes-what@10
  - dark-matter.stored-asymmetry-charge-not-number@13
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_mirror_share_from_mass_per_baryon
- kind: check
  ref: check.py::check_temperature_ratio_interval
- kind: check
  ref: check.py::check_eta_prime
- kind: check
  ref: check.py::check_atomic_cross_section_per_mass
locators:
  paper: T14b
  number: Fact 2.3
  label: fact:mirror
  line: 100
extraction:
  maintainer_pass_2026_11_18_energy:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 7 -> 8, at Leon''s decision of 18 November 2026, 14:04 (adopt the computed mean energy per creation event in the gravitational floor). The gravitational floor is 6.6e-4 (dark-matter.stored-asymmetry-charge-not-number (iii), version 13) where 5.2e-4 stood, at the formal and technical levels and in the proof text; the check computes it with the mean energy per event (eta'' at the floor 2.11, where 4.36 stood). Unchanged: the share 0.995 to 1, the hot deposit, the helium interval, the cross-sections (the statement that the neutron-rich composition was computed at the printed floor and not at the present one stood on this pass; see the follow-up below). The two premises restated the same day are repinned. Follow-up, same day, version kept at 8: the composition at the present floor is no longer ''not recomputed''. At 6.6e-4 the mirror ends 83 (L = 0) to 96 (L/B = -51/28) percent neutrons and is only moderately degenerate (dark-tower-matter.mirrors-composition (i), version 5 as extended the same day); stated at the formal, technical and lay levels and in the one-liner. No number of this entity''s check is involved. The figures at the present floor are decimal results of the supplementary scripts behind dark-tower-matter.mirrors-composition, run again on 18 November 2026 with 6.6e-4 added to their grids (that entity''s proof text and note give the details); the scripts are not in the store and no check is added.'
  maintainer_pass_2026_11_18:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 6 -> 7, at Leon''s decision of 18 November 2026 (restate the numbers that used the first published production coefficients). The gravitational floor is 5.2e-4 (dark-matter.stored-asymmetry-charge-not-number (iii), version 12) where the printed 2.8 to 3.2e-4 stood, at the formal and technical levels and in the proof text; the check computes it from the derived coefficients (eta'' at the floor 4.36, where 19 to 26 stood). The neutron-rich composition is stated at the printed floor, where dark-tower-matter.mirrors-composition computed it, and is not recomputed at the present floor. Unchanged: the share 0.995 to 1, the hot deposit, the helium interval, the cross-sections. The provenance still cites the dark-matter paper, whose printed floor differs. The two premises restated the same day are repinned.'
  maintainer_pass_2026_11_12:
    by: maintainer-2026-11-12
    date: '2026-11-12'
    note: 'Scope note, version kept, no statement changed (Leon''s decision of 12 November 2026: the inherited charge is B - L). The mirror''s baryon-to-photon ratio eta'' = eta/xi^3 takes the mirror''s baryon number equal to this tower''s, which holds under the hypothesis of equal conversion (the mirror''s ratio of baryon number to B - L equals this tower''s; not shown; attack item (d) of op.matter-asymmetry-origin; Proposition dark-matter.stored-asymmetry-charge-not-number (i), version 11). The simulation statements are unchanged.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-matter.mirror-share-one-how-fragile repinned 6 -> 7 after reviewing its C1 restatement ((i) now rests on the common-ceiling-coupling premise, with an assumes edge, where it said P2-protected; the values are unchanged); the use here holds as cited. Pin review: dark-matter.mirror-tower-copy-one repinned 8 -> 9 after reviewing its C1 restatement (clause (iv): the common ceiling and coupling are now Premise synthesis.common-ceiling-coupling-premise, P2 equating labels and not couplings; the share of one rests also on that premise; the caveat is reworded for P2''s version-1 reach), clauses (i) to (iii) and (v) unchanged in content; the use here holds as cited. Pin review: dark-matter.radiation-audit-what-theorem-closes-what repinned 7 -> 8 after reviewing its G1 restatement (the cold mirror is an exception to P2 at its version-1 reach, P2 as scoped leaves xi free, and the cold mirror then needs a non-equilibrium descent; the numbers are unchanged); the use here holds as cited. Pin review: dark-matter.stored-asymmetry-charge-not-number repinned 8 -> 9 after reviewing its G1 restatement (the cold mirror is an exception to P2 at its version-1 reach, P2 as scoped leaves xi free, and the cold mirror then needs a non-equilibrium descent; the charge reading and the numbers are unchanged); the use here holds as cited.'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'G1 (DECISIONS; R05 item 2): the cold-mirror exception now says that it is an exception to P2 at its version-1 reach, that P2 as scoped (version 2, labels not states) leaves xi free (synthesis.tower-charge-sector-label-temperature-not), and that the cold mirror then needs a non-equilibrium descent (synthesis.cold-mirror-needs-non-equilibrium-descent); P2 is unchanged by Leon''s answer 2, so the sentence stands.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the mass-per-baryon ratio 0.995, the floor and hot-deposit temperature ratios, eta prime = eta/xi^3 and the atomic cross-sections per mass, by exact interval arithmetic on the T14 inputs. Version 3 -> 4. Check strengthened: c, eta and n_B/s pinned exactly by hand; floor ends, hot deposit, eta'' and atomic cross-sections pinned to one-decimal enclosures with both interval ends tested; sample inputs moved to module level. Version 4 -> 5.'
  superseded_in_part_by:
  - dark-tower-matter.mirrors-composition
  - dark-tower-matter.mirrors-temperature-p2
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 1
    note: 'Superseded in part by T14c. Comp 8.3 (dark-tower-matter.mirrors-composition): the restated
      "on the expected (burning) branch it is helium" fails at the floor, where the mirror is degenerate
      and 96 to 100 percent neutrons for L <= 0; it is helium for xi about 3e-3 to 2e-2, which contains
      the hot-deposit estimate. The 0.995 to 1 share range is now tied to the helium and proton compositions.
      Prop 8.2 (dark-tower-matter.mirrors-temperature-p2): the cold interval is a free datum, an exception
      to P2. Formal and levels narrowed; the proof (the T14b Fact text with provenance) is unchanged. The
      galaxy and cluster simulations that model a helium mirror are not changed: they compute a helium
      mirror, which T14c places at xi about 3e-3 to 2e-2, not at the floor. Original in source_formal.'
  source_formal: |-
    The mirror tower is a copy of ours, populated at $\Omega_{b'} = 0.995$ to $1$ times $\Omega_{b}$. Its temperature ratio $\xi = T'/T$ lies between the gravitational floor, $2.8$ to $3.2 \times 10^{-4}$, and the hot-deposit estimate, about $4 \times 10^{-3}$; its baryon-to-photon ratio is $\eta' = \eta/\xi^{3}$; on the expected (burning) branch it is helium, on the alternative it is protons. As neutral atoms its elastic cross-section per mass is of order $2 \times 10^{8}$ (hydrogen) or $5 \times 10^{7}$ (helium) $\cmg$, and inside a halo it is a plasma, collisional and dissipative like our gas. \emph{Provenance:} \cite[Thm.~4.3, Props.~4.6 and 4.7, Prop.~6.2]{ButlerT14}.
  typing:
    by: ai-typing-pass
    note: 'All four uses match the cited provenance (the mirror copy theorem, the stored-asymmetry and
      mirror-share propositions, the radiation audit), so they were kept; the E204 comes from the stored-asymmetry
      premise, outside this list. Levels pass: lay no longer says the mirror plasma sinks, which the formal
      does not state.'
  env: fact
  context_refs:
  - dark-matter.mirror-share-one-how-fragile
  - dark-matter.mirror-tower-copy-one
  - dark-matter.radiation-audit-what-theorem-closes-what
  - dark-matter.stored-asymmetry-charge-not-number
  flags:
  - 'fact restating several series results: derived from them'
---

## formal
The mirror tower is a copy of ours, populated at $\Omega_{b'} = 0.995$ to $1$ times $\Omega_{b}$ where its matter is helium or protons. Its temperature ratio $\xi = T'/T$ lies between the gravitational floor, $6.6 \times 10^{-4}$ (at the production coefficients and the mean energy per creation event since derived in the store; T14 printed $2.8$ to $3.2 \times 10^{-4}$), and the hot-deposit estimate, about $4 \times 10^{-3}$, a free datum of the descent that is an exception to P2 at its version-1 reach (Proposition \claimref{dark-tower-matter.mirrors-temperature-p2}; P2 as scoped leaves $\xi$ free, Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}, and the cold mirror then needs a non-equilibrium descent, Proposition \claimref{synthesis.cold-mirror-needs-non-equilibrium-descent}); its baryon-to-photon ratio is $\eta' = \eta/\xi^{3}$. T14 takes it to be helium on the expected (burning) branch and protons on the alternative; T14c finds it helium for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$, an interval containing the hot-deposit estimate, and at $\xi = 2.8$ to $3.2 \times 10^{-4}$, T14's printed floor, degenerate and, for a copied lepton number $L \leq 0$, $96$ to $100$ percent neutrons; at the present floor, $6.6 \times 10^{-4}$, it is still neutron-rich for $L \leq 0$, $83$ to $96$ percent neutrons, and only moderately degenerate (Computation \claimref{dark-tower-matter.mirrors-composition}). As neutral atoms its elastic cross-section per mass is of order $2 \times 10^{8}$ (hydrogen) or $5 \times 10^{7}$ (helium) $\cmg$, and inside a halo it is a plasma, collisional and dissipative like our gas. \emph{Provenance:} \cite[Thm.~4.3, Props.~4.6 and 4.7, Prop.~6.2]{ButlerT14}.

## technical
The mirror tower carries a copy of our matter content, populated at $\Omega_{b'} = 0.995$ to $1$ times $\Omega_{b}$ where its matter is helium or protons. Its temperature ratio $\xi = T'/T$ lies between a gravitational floor of $6.6 \times 10^{-4}$ (the dark-matter paper printed $2.8$ to $3.2 \times 10^{-4}$, from production coefficients and an energy per creation event since corrected) and a hot-deposit estimate of about $4 \times 10^{-3}$, a free datum that the T14c note shows to be an exception to indifference (P2) at its version-1 reach (as scoped, indifference leaves it free and the cold mirror then needs a non-equilibrium descent), and its baryon-to-photon ratio is $\eta' = \eta/\xi^{3}$. The dark-matter paper takes it to be helium on the expected (burning) branch and protons on the alternative; T14c finds it helium for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$, which contains the hot-deposit estimate, but degenerate and neutron-rich at the printed floor, $2.8$ to $3.2 \times 10^{-4}$, and still neutron-rich ($83$ to $96$ percent neutrons for a copied lepton number $L \leq 0$), though only moderately degenerate, at the present one, $6.6 \times 10^{-4}$.

As neutral atoms it has an elastic cross-section per mass of order $2 \times 10^{8}\ \cmg$ (hydrogen) or $5 \times 10^{7}\ \cmg$ (helium); inside a halo it is a plasma, collisional and dissipative like our gas. These are results of the series' dark-matter paper restated for the simulations.

## lay
One of the hidden sectors is a mirror copy of ordinary matter with almost exactly as much matter as ours, but much colder. The series' dark-matter paper expected its early-universe chemistry to leave it mostly helium; a later note (T14c) finds that true only if it is moderately warm, and at the coldest temperature that paper considered it would end mostly as neutrons (the minimum temperature has since been revised upwards, and there too it ends mostly as neutrons, a little less completely). That note also shows that keeping it cold is an unstated exception to the paper's indifference principle as first stated. As the principle is now scoped, it applies to labels such as charges and not to temperatures, so it leaves the mirror's temperature free; a cold mirror then needs the descent to have left the towers out of equilibrium. Inside galaxies it is a plasma that, like our own gas, collides and radiates energy away.

## one-liner
The mirror tower is a cold copy of ours with $\Omega_{b'} = 0.995$ to $1$ times $\Omega_{b}$, helium on the expected branch (T14c: helium for $\xi$ about $3 \times 10^{-3}$ to $2 \times 10^{-2}$, neutron-rich at T14's printed floor and at the present one), and inside halos a collisional, dissipative plasma.
