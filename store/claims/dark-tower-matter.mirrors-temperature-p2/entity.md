---
id: dark-tower-matter.mirrors-temperature-p2
kind: claim
version: 6
title: The mirror's temperature and premise P2
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [premises-p1-p5, mirror-sector, confronted-with-data]
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
  - dark-matter.mirror-tower-copy-one@8
  - dark-matter.stored-asymmetry-charge-not-number@8
  - dark-matter.seeding-gravity-floor-dark-towers-temperature@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:K2
- kind: check
  ref: check.py::check_photon_term_derived
- kind: check
  ref: check.py::check_delta_neff_and_exclusion
lineage:
  supersedes:
  - dark-matter.mirror-tower-copy-one
  - dark-matter.stored-asymmetry-charge-not-number
  - dark-matter.open-channels-their-costs
  - simulations.imported-mirror
locators:
  paper: T14c
  number: Prop 8.2
  label: prop:P2
  line: 757
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: photon term derived from entropy counting; exact bounds put Delta N_eff at 7.45 and its ratio to 0.3 at about 25. Version 4 -> 5. Check strengthened: both ends of each bracket round exactly to 4.40, 7.45 and 25, and Delta N_eff/0.3 is pinned in (24.8, 24.9); (11/4)^4 computed rather than typed. Version 5 -> 6.'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 1
    note: 'Lineage supersedes added (decision 1, T14 against T14c, CONTRADICTIONS_VALUES H1): the copy theorem
      (its P2 reach in clauses (iv), (v)), the stored-asymmetry proposition (clause (iii), the free temperature
      datum), the open-channels proposition (the cold mirror the framework predicts) and the T14b restatement
      of the mirror, each narrowed and carrying a caveat that cites this result. Lineage is unpinned in
      the store schema. The uses pins to the narrowed T14 results are left for the maintainer to repin.'
  env: proposition
  context_refs:
  - dark-matter.mirror-tower-copy-one
  - dark-matter.stored-asymmetry-charge-not-number
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.mirror-tower-copy-one
    - dark-matter.seeding-gravity-floor-dark-towers-temperature
    - dark-matter.stored-asymmetry-charge-not-number
    note: 'Added the three dark-matter results the statement and proof read (the copy theorem''s P2 equalities,
      the asymmetry proposition and the gravitational floor). P2 itself was not made an assumption: the
      proposition analyses what P2 would give and concludes that the cold mirror is an exception to it,
      so it does not hold under P2. Levels pass: levels written from scratch, keeping every condition
      and level qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.seeding-gravity-floor-dark-towers-temperature
    - dark-matter.stored-asymmetry-charge-not-number
payload:
- kind: value
  clause: N_eff of the Standard Model
  quantity: quantity.effective-neutrino-number
  python: NEFF_SM == F('3.044')
- kind: inequality
  clause: Delta N_eff = 7.45
  python: LO ** 3 < F(11, 4) ** 4 < HI ** 3 and F(7445, 1000) <= F(8, 7) * LO + NEFF_SM and F(8, 7) *
    HI + NEFF_SM < F(7455, 1000)
  note: '(8/7)(11/4)^(4/3) + 3.044 lies in [7.445, 7.455): it rounds to 7.45'
- kind: inequality
  clause: excluded by a factor of about 25
  python: F(245, 10) <= (F(8, 7) * LO + NEFF_SM) / BOUND and (F(8, 7) * HI + NEFF_SM) / BOUND < F(255,
    10)
---

## formal
T14 applies P2 along the reversal orbit to equate the ceiling coupling and the asymmetry per mode, both data of the descent \cite[Thm.~4.3(iv), (v)]{ButlerT14}. The energy the descent deposits per unit charge is a datum of the same kind, and P2 declares which of $2$, $6$ is visible to be indexical. Applied with the same reach, P2 gives $\xi = T'/T = 1$ and $\Delta\Neff = \tfrac{8}{7}(\tfrac{11}{4})^{4/3} + 3.044 = 7.45$ at recombination, excluded by a factor of about $25$. T14's mirror, cold from the gravitational floor upward \cite[Prop.~4.6, Prop.~A.2]{ButlerT14}, is therefore an exception to P2 that T14 neither states nor costs. Assembly level.

## technical
At assembly level. The dark-matter paper applies P2 along the reversal orbit to equate the ceiling coupling and the asymmetry per mode, both data of the descent. The energy the descent deposits per unit charge is a datum of the same kind, and P2 declares indexical which of the residues $2$, $6$ is the visible one. Applied with the same reach, P2 gives $\xi = T'/T = 1$ and $\Delta\Neff = \tfrac87(\tfrac{11}{4})^{4/3} + 3.044 = 7.45$ at recombination, excluded by a factor of about $25$.

The dark-matter paper's mirror, cold from the gravitational floor upward, is therefore an exception to P2 that the paper neither states nor costs.

## lay
The dark-matter paper uses an indifference principle, P2, to argue that the mirror tower and ours received equal shares of certain initial quantities. This assembly-level argument shows that applying the same principle to the energy each tower received would make the mirror as hot as our world, adding far more radiation than observations allow. So the cold mirror the paper relies on is an unstated exception to its own principle.

## one-liner
At assembly level, P2 applied with the dark-matter paper's own reach makes the mirror as hot as our tower, $\Delta\Neff = 7.45$, so its cold mirror is an unstated exception to P2.
