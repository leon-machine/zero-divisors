---
id: simulations.imported-mirror
kind: claim
version: 6
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
review: typed
derivations:
- name: main
  uses:
  - dark-matter.mirror-share-one-how-fragile@7
  - dark-matter.mirror-tower-copy-one@9
  - dark-matter.radiation-audit-what-theorem-closes-what@8
  - dark-matter.stored-asymmetry-charge-not-number@10
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
The mirror tower is a copy of ours, populated at $\Omega_{b'} = 0.995$ to $1$ times $\Omega_{b}$ where its matter is helium or protons. Its temperature ratio $\xi = T'/T$ lies between the gravitational floor, $2.8$ to $3.2 \times 10^{-4}$, and the hot-deposit estimate, about $4 \times 10^{-3}$, a free datum of the descent that is an exception to P2 at its version-1 reach (Proposition \claimref{dark-tower-matter.mirrors-temperature-p2}; P2 as scoped leaves $\xi$ free, Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}, and the cold mirror then needs a non-equilibrium descent, Proposition \claimref{synthesis.cold-mirror-needs-non-equilibrium-descent}); its baryon-to-photon ratio is $\eta' = \eta/\xi^{3}$. T14 takes it to be helium on the expected (burning) branch and protons on the alternative; T14c finds it helium for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$, an interval containing the hot-deposit estimate, and at the floor degenerate and, for a copied lepton number $L \leq 0$, $96$ to $100$ percent neutrons (Computation \claimref{dark-tower-matter.mirrors-composition}). As neutral atoms its elastic cross-section per mass is of order $2 \times 10^{8}$ (hydrogen) or $5 \times 10^{7}$ (helium) $\cmg$, and inside a halo it is a plasma, collisional and dissipative like our gas. \emph{Provenance:} \cite[Thm.~4.3, Props.~4.6 and 4.7, Prop.~6.2]{ButlerT14}.

## technical
The mirror tower carries a copy of our matter content, populated at $\Omega_{b'} = 0.995$ to $1$ times $\Omega_{b}$ where its matter is helium or protons. Its temperature ratio $\xi = T'/T$ lies between a gravitational floor of $2.8$ to $3.2 \times 10^{-4}$ and a hot-deposit estimate of about $4 \times 10^{-3}$, a free datum that the T14c note shows to be an exception to indifference (P2) at its version-1 reach (as scoped, indifference leaves it free and the cold mirror then needs a non-equilibrium descent), and its baryon-to-photon ratio is $\eta' = \eta/\xi^{3}$. The dark-matter paper takes it to be helium on the expected (burning) branch and protons on the alternative; T14c finds it helium for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$, which contains the hot-deposit estimate, but degenerate and neutron-rich at the floor.

As neutral atoms it has an elastic cross-section per mass of order $2 \times 10^{8}\ \cmg$ (hydrogen) or $5 \times 10^{7}\ \cmg$ (helium); inside a halo it is a plasma, collisional and dissipative like our gas. These are results of the series' dark-matter paper restated for the simulations.

## lay
One of the hidden sectors is a mirror copy of ordinary matter with almost exactly as much matter as ours, but much colder. The series' dark-matter paper expected its early-universe chemistry to leave it mostly helium; a later note (T14c) finds that true only if it is moderately warm, and at its coldest it would end mostly as neutrons. That note also shows that keeping it cold is an unstated exception to the paper's indifference principle as first stated. As the principle is now scoped, it applies to labels such as charges and not to temperatures, so it leaves the mirror's temperature free; a cold mirror then needs the descent to have left the towers out of equilibrium. Inside galaxies it is a plasma that, like our own gas, collides and radiates energy away.

## one-liner
The mirror tower is a cold copy of ours with $\Omega_{b'} = 0.995$ to $1$ times $\Omega_{b}$, helium on the expected branch (T14c: helium for $\xi$ about $3 \times 10^{-3}$ to $2 \times 10^{-2}$, neutron-rich at the floor), and inside halos a collisional, dissipative plasma.
