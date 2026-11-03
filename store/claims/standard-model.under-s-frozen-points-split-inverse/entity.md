---
id: standard-model.under-s-frozen-points-split-inverse
kind: claim
version: 7
title: Under (S), the frozen point's split of the $5$ is the inverse of the demanded one
status: proved
region: standard-model
subject: mass
tags:
- frozen-point
- running-and-unification
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
derivations:
- name: main
  uses:
  - standard-model.direction-demanded-content-doublet-heavy@7
  - standard-model.grip-mass-two-rung-module@7
  - standard-model.under-s-composites-state-space-spinor@6
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_one_mode_states_are_the_split_five
- kind: check
  ref: check.py::check_doublet_massive_triplet_massless
- kind: check
  ref: check.py::check_mass_supported_on_slot_doublets_everywhere
- kind: proof
  derivation: main
locators:
  paper: T12
  number: Cor 9.12
  label: cor:five
  line: 1609
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the one-mode states as doublet plus triplet, slot-component counts with the null and area masses, and mass support on the slot doublets in every sector. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 6 -> 7.'
  env: corollary
  typing:
    by: ai-typing-pass
    removed:
    - standard-model.table-exact
    note: 'Removed the table proposition, which enters only through the doublet-heavy corollary (the proof
      says this corollary uses only the direction of the demand); the remaining E204 traces to that corollary
      and the table-exact cycle, outside this list. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: the lay level now states Hypothesis
      (S) and the flat-space condition $\Lambda = 0$; the one-liner adds $\Lambda = 0$.'
    added:
    - standard-model.hyp-s-slot-statistics
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
about:
- obj.standard-model.two-rung-module-sectors-slot-components
- obj.mass.grip-mass-composite
---

## formal
Under Hypothesis (S), the one-mode states of the module form $5 = R_{2} \oplus W = (2,1)_{1/2} \oplus (1,3)_{-1/3}$, a slot doublet and a pair triplet, the fundamental of $SU(5)$ split exactly along the slot/pair line. Under the grip at $\Lambda = 0$ the doublet, having two slot components, carries the area mass $2|\br{\pi^{1}\pi^{2}}|^{2}$, while each triplet state, having one, is massless. The frozen point therefore assigns whatever mass it assigns to the doublet and none to the triplet: the opposite of the split the running demands, in which the doublets are the light members and the colour triplets the heavy ones. The same holds for every $\mathrm{Spin}(10)$ multiplet realised in the module: the frozen-point mass is supported on the slot-doublet sectors and vanishes on the slot-singlet ones, whatever their colour.

## technical
Under Hypothesis (S), the one-mode states of the module form the $5$ of $SU(5)$, $R_{2} \oplus W = (2,1)_{1/2} \oplus (1,3)_{-1/3}$, a slot doublet and a pair triplet. Under the grip at $\Lambda = 0$ the doublet, with two slot components, carries the area mass $2|\br{\pi^{1}\pi^{2}}|^{2}$, while each triplet state, with one component, is massless.

So the frozen point gives whatever mass it gives to the doublet and none to the triplet, the opposite of the split the running demands, in which the doublets are light and the colour triplets heavy. The same holds for every $\mathrm{Spin}(10)$ multiplet realised in the module: the frozen-point mass is supported on the slot-doublet sectors and vanishes on the slot-singlet ones, whatever their colour.

## lay
Grand unified theories need the Higgs doublet to stay light while its colour-triplet partners become heavy. Under Hypothesis (S), that the composite's slots carry fermionic statistics, and in flat space ($\Lambda = 0$), this result shows that the series' own mass mechanism does the reverse: it can give mass to the doublet but leaves the triplet massless. So that mechanism cannot be what produces the required split.

## one-liner
Under Hypothesis (S) and at $\Lambda = 0$, the frozen point's grip mass falls on the doublet of the $5$ and not on the triplet, the inverse of the demanded split.
