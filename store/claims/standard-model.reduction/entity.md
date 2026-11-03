---
id: standard-model.reduction
kind: claim
version: 7
title: The reduction
status: proved
region: standard-model
subject: mass
tags:
- no-go
- running-and-unification
- mass-generation
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
  - standard-model.frozen-point-pair-mixing@4
  - standard-model.grip-mass-two-rung-module@7
  - standard-model.imported-grip-area-casimir-form@5
  - standard-model.invariant-operators-module@7
  - standard-model.mass-bracket-charged-singlet@4
  - standard-model.moment-map-grip-mass-are-insensitive@4
  - standard-model.under-s-bracket-direction-charged-not@7
  - standard-model.under-s-frozen-points-split-inverse@7
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_six_numbers_zero_on_singlets_area_on_doublets
- kind: check
  ref: check.py::check_frozen_point_not_pair_invariant
- kind: check
  ref: check.py::check_inverse_split_on_every_multiplet
- kind: check
  ref: check.py::check_bracket_charged_and_no_one_generation_operator
- kind: check
  ref: check.py::check_six_free_numbers
- kind: proof
  derivation: main
locators:
  paper: T12
  number: Prop 9.18
  label: prop:reduction
  line: 1657
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the six numbers (0, 0, m_Q, m_L, 0, 0) from the slot-component counts and the area formula, mass supported on slot doublets, the bracket direction charged and antisymmetric, six free invariant numbers. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 6 -> 7.'
  env: proposition
  typing:
    by: ai-typing-pass
    removed:
    - standard-model.configuration-sector-carries-higgs-doublets-quantum
    note: 'Removed the configuration-sector observation (a conjecture): the proof says the Higgs-origin
      identification is that observation stated as a problem, not a result, and what is proved does not
      rest on it; kept the eight other edges. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: the lay now names Hypothesis
      (S) and the Lambda = 0 setting of clause (1); the one-liner keeps Lambda = 0.'
    added:
    - standard-model.hyp-s-slot-statistics
  source_title: The reduction
  source_formal: 'Under (S), with the frozen point in $V$: (1) at $\Lambda = 0$ the framework''s mass
    mechanism gives the zero form on the four slot-singlet sectors of the generation and the area form
    of Theorem \claimref{standard-model.grip-mass-two-rung-module}(iii) on the two slot-doublet sectors,
    so that in the six-number language of Proposition \claimref{standard-model.invariant-operators-module}
    it is $(0, 0, m_{Q}, m_{L}, 0, 0)$ with $m_{Q}, m_{L}$ state-dependent and the four zeros exact: slot
    doublets massive, slot singlets massless; (2) this is the inverse of the demanded split for every
    multiplet cut along the slot/pair line; (3) the mass bracket, the series'' one other mass object,
    is defined on tuples and not on the module, is $e^{c}$-charged, and generates no one-generation mass
    operator (Proposition \claimref{standard-model.under-s-bracket-direction-charged-not}); (4) therefore
    no slot/pair mass split in the demanded direction follows from the series as it stands, and any such
    split is a choice of six numbers on the generation, or of the analogous numbers on a scalar multiplet,
    that the scalar sector must supply. The slot/pair mechanism the partner sector depends on is the scalar
    sector, and the partner sector''s successor problem is the same problem as the origin of the Higgs
    doublet.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: Only the technical level named the two-twistor area form, now the two-spinor area form; the
      formal level and proof had no twistor language.
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
---

## formal
Under (S), with the frozen point in $V$: (1) at $\Lambda = 0$ the framework's mass mechanism gives the zero form on the four slot-singlet sectors of the generation and the area form of Theorem \claimref{standard-model.grip-mass-two-rung-module}(iii) on the two slot-doublet sectors, so that in the six-number language of Proposition \claimref{standard-model.invariant-operators-module} it is $(0, 0, m_{Q}, m_{L}, 0, 0)$ with $m_{Q}, m_{L}$ state-dependent and the four zeros exact: slot doublets massive, slot singlets massless; (2) this is the inverse of the demanded split for every multiplet cut along the slot/pair line; (3) the mass bracket, the series' one other mass object, is defined on tuples and not on the module, is $e^{c}$-charged, and generates no one-generation mass operator (Proposition \claimref{standard-model.under-s-bracket-direction-charged-not}); (4) therefore no slot/pair mass split in the demanded direction follows from the series as it stands, and any such split is a choice of six numbers on the generation, or of the analogous numbers on a scalar multiplet, that the scalar sector must supply. The slot/pair mechanism the partner sector depends on is the scalar sector, and the partner sector's successor problem is the same problem as the origin of the Higgs doublet.

## technical
Under Hypothesis (S), with the frozen point in $V$: at $\Lambda = 0$ the mass mechanism is the zero form on the four slot-singlet sectors of the generation and the two-spinor area form on the two slot-doublet sectors, so in the six-number language of the invariant operators it is $(0, 0, m_{Q}, m_{L}, 0, 0)$, with $m_{Q}, m_{L}$ state-dependent and the zeros exact. This is the inverse of the demanded split for every multiplet cut along the slot/pair line.

The mass bracket, the series' other mass object, is defined on tuples rather than on the module, is $e^{c}$-charged, and generates no one-generation mass operator. Hence no slot/pair mass split in the demanded direction follows from the series as it stands: any such split is a choice of six numbers on the generation, or the analogue on a scalar multiplet, that a scalar sector must supply. The paper identifies this missing sector with the problem of the Higgs doublet's origin, as a statement of the problem rather than a result.

## lay
This result takes stock of what the series derives about mass on one generation of matter. Assuming the slots behave like the pairs (Hypothesis (S)), and with no cosmological constant, its own mechanism makes the doublets massive and the singlets massless, the opposite of what the unification analysis requires, and its other mass object cannot help. So the needed split is not derived anywhere in the series and has to come from a separate scalar sector, which the paper links to the open question of where the Higgs doublet comes from.

## one-liner
Under Hypothesis (S), at $\Lambda = 0$, the series' mass mechanisms give $(0, 0, m_{Q}, m_{L}, 0, 0)$ on the generation, the inverse of the demanded split, so that split must be supplied by a scalar sector the series does not derive.
