---
id: dark-tower-matter.mirrors-composition
kind: claim
version: 3
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
review: typed
derivations:
- name: main
  uses:
  - dark-matter.stored-asymmetry-charge-not-number@11
  - dark-matter.seeding-gravity-floor-dark-towers-temperature@4
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
Decimal. Supplementary scripts: the mirror's (folder \file{MIR}, checks D1, D2 and E0 to E7) and the cosmology check's (folder \file{CHECK\_COS}). T14 carries $\xi$ from the gravitational floor ($2.8$ to $3.2 \times 10^{-4}$ at the top of the ceiling range) to the $\Neff$ cap ($0.448$), with a hot-deposit estimate near $4 \times 10^{-3}$.
\begin{enumerate}
\item[(i)] At the floor the mirror is charge-dominated and degenerate from the moment it is seeded: the Fermi energy its deposited baryon number must carry exceeds the floor's thermal deposit by $49$ to $84$, and at its weak freeze-out the quark chemical potential is $18$ to $23$ times its temperature. Beta equilibrium persists into the hadron phase, and for a copied lepton number $L \leq 0$ (our tower's sphaleron value $L/B = -51/28$, or zero) the mirror ends $96$ to $100$ percent neutrons. Its endpoint is cold, dense, neutron-rich matter; the composition after decay and capture needs a dense-matter network and is not computed here.
\item[(ii)] Between $\xi \approx 3 \times 10^{-3}$ and $2 \times 10^{-2}$, an interval containing T14's hot-deposit estimate, the mirror is helium ($Y' = 0.94$ to $1.00$).
\item[(iii)] Above that interval the helium fraction falls ($Y' = 0.85$ at $\xi = 0.1$) and towards the cap the mirror is hydrogen-rich ($Y' = 0.58$ at $\xi = 0.448$).
\end{enumerate}
T14 does not print a mirror $\eta'$ at freeze-out; its floor value $19$ to $26$ is the late-time ratio, and the thermal up-down ratio T14 assumes there is inconsistent with its own $\eta' > 1$.

## technical
A decimal computation across the dark-matter paper's range of the mirror temperature ratio $\xi = T'/T$, from the gravitational floor ($2.8$ to $3.2 \times 10^{-4}$ at the top of the ceiling range) to the $\Neff$ cap ($0.448$), with a hot-deposit estimate near $4 \times 10^{-3}$. (i) At the floor the mirror is charge-dominated and degenerate from the moment it is seeded: the Fermi energy its baryon number must carry exceeds the floor's thermal deposit by $49$ to $84$, the quark chemical potential at weak freeze-out is $18$ to $23$ times the temperature, and for a copied lepton number $L \leq 0$ it ends $96$ to $100$ percent neutrons, cold, dense and neutron-rich; the composition after decay and capture is not computed. (ii) For $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$ the mirror is helium, $Y' = 0.94$ to $1.00$. (iii) Above that the helium fraction falls, to $Y' = 0.85$ at $\xi = 0.1$ and $0.58$ at $\xi = 0.448$.

The dark-matter paper's floor value of $\eta'$ is a late-time ratio, and the thermal up-down ratio it assumes there is inconsistent with its own $\eta' > 1$.

## lay
The mirror tower copies our physics, so what its matter becomes depends mainly on how hot it was compared with our world. These decimal estimates show that if it was as cold as gravity alone allows, it ends as dense neutron-rich matter; if it was moderately warm, it is almost pure helium; and if it was near the radiation limit, it is mostly hydrogen. The coldest case is not followed to its final composition.

## one-liner
In decimal estimates the mirror ends neutron-rich at the gravitational floor (for $L \leq 0$), helium for $\xi$ between about $3 \times 10^{-3}$ and $2 \times 10^{-2}$, and hydrogen-rich towards the $\Neff$ cap.
