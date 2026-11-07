---
id: standard-model.lifted-components-read-vevs
kind: claim
version: 8
title: The lifted components read as vevs
status: proved
region: standard-model
subject: mass
tags: [frozen-point, symmetry-breaking, flavour-and-mixing]
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
  - standard-model.one-vev-vector-relations-breaking-pattern@7
  - standard-model.transported-frozen-point@6
  - standard-model.yukawa-pattern-two-rung-module@6
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_reading_through_the_conjugate
- kind: check
  ref: check.py::check_reading_through_c_itself
- kind: check
  ref: check.py::check_the_unit_is_the_lifts
- kind: check
  ref: check.py::check_ground_frozen_point_gives_no_dirac_mass
- kind: proof
  derivation: main
locators:
  paper: T12
  number: Cor 9.28
  label: cor:read
  line: 1782
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: lift components computed from the conformal lift and read as vevs in the five-mode module through c* and through c, the unit of any lift, and the triplet-only couplings of a ground vector. Version 5 -> 6. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 6 -> 7. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 7 -> 8.'
  env: corollary
  context_refs:
  - standard-model.transported-frozen-point
  - standard-model.yukawa-pattern-two-rung-module
  typing:
    by: ai-typing-pass
    added:
    - standard-model.transported-frozen-point
    - standard-model.yukawa-pattern-two-rung-module
    - standard-model.hyp-s-slot-statistics
    note: 'Added the transported-frozen-point proposition, whose components supply the values (a, b) fed
      to the one-vev corollary, and the Yukawa-pattern theorem, which the statement cites for the ground
      frozen point''s triplet couplings. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: the lay level now states Hypothesis
      (S), as the formal and the other levels do (review item 1).'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.transported-frozen-point
    - standard-model.yukawa-pattern-two-rung-module
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 5 (Leon''s decision 10 of 2026-10-23): repinned to version 4 of the one-vev corollary, which reads the up-type and neutrino masses through the conjugate c*; under that reading each lift gives equal up-type and down-type entries (1 for X(I), Lambda/3 for the reciprocal, 1 + Lambda/3 for the sum), so the H_d-type and H_u-type reading of the two lifts, which belonged to the reading through c, is recorded as that reading''s and is not the series''; the lift''s unit and the ground frozen point''s triplet couplings are unchanged. Version 4 note follows. Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under Hypothesis (S), read the second-rung components of Proposition \claimref{standard-model.transported-frozen-point} as the vector $c$ of Corollary \claimref{standard-model.one-vev-vector-relations-breaking-pattern}, with the up-type and neutrino masses read through the conjugate $c^{*}$ as that corollary does. The lift $X(I)$, with $c = \tfrac{\Lambda}{3}v_{4} - w_{4}$, gives $m_{\nu} = m_{u} = m_{e} = m_{d} = 1$ in the lift's normalisation; the reciprocal's lift, with $c = v_{4} - \tfrac{\Lambda}{3}w_{4}$, gives all four equal to $\Lambda/3$; the two together give every Dirac entry the magnitude exactly $1 + \Lambda/3$, with $m_{u}/m_{d} = 1$ exactly. Read through $c$ itself instead, the lift $X(I)$ would give $m_{e} = m_{d} = 1$ and $m_{\nu} = m_{u} = \Lambda/3$, an $H_{d}$-type vev with an $H_{u}$ admixture of order $\Lambda$, and the reciprocal's lift the reverse, $H_{u}$-type; that is not the series' reading (Theorem \claimref{synthesis.rung-field-on-the-lift-locus}(5)), and under the reading through $c^{*}$ neither lift separates up-type from down-type masses. The unit is the lift's: the same magnitudes arise from the lift of any vector of the ground completion, and what the frozen point contributes is the $O(\Lambda)$ admixture alone, so the tree relations are a statement about the pairing and the lift, and the overall scale of the entries is not fixed by anything here. The ground frozen point itself, a vector of $V$, read through the same pairing gives no Dirac mass at all: its couplings are the triplet ones of Theorem \claimref{standard-model.yukawa-pattern-two-rung-module}(ii).

## technical
Under Hypothesis (S), read the second-rung components of the transported frozen point as a vev vector $c = a\,v_{4} + b\,w_{4}$ of the rung plane, with the up-type and neutrino masses read through the conjugate $c^{*}$, for which the tree-level masses are all $|b|$. The lift $X(I)$ then gives all four Dirac masses $1$ and the reciprocal's lift all four $\Lambda/3$; together every Dirac entry has magnitude exactly $1 + \Lambda/3$, with $m_{u}/m_{d} = 1$ exactly. Read through $c$ itself, the lift would be an $H_{d}$-type vev with an $H_{u}$ admixture of order $\Lambda$ and the reciprocal's lift $H_{u}$-type, but that reading is not the series'.

The unit is the lift's normalisation: the lift of any vector of the ground completion gives the same magnitudes, and the frozen point contributes only the $O(\Lambda)$ admixture, so the overall scale of the entries is not fixed here. The ground frozen point itself, a vector of $V$, gives no Dirac mass through the same pairing, only triplet couplings.

## lay
Under Hypothesis (S), that the composite's slots carry fermionic statistics, when the frozen point is carried up into the larger structure, it acquires components that can be read as the Higgs field's vacuum value. With the up-type quarks reading the mirror image of that value, as in the Standard Model, the lifted frozen point gives the up quark, the down quark, the electron and the neutrino one common mass, and its reciprocal another, much smaller one; neither separates up-type from down-type masses. The sizes come from a normalisation convention, so the actual mass scale is left undetermined; what the frozen point itself supplies is a small piece proportional to the cosmological constant.

## one-liner
Under Hypothesis (S), with up-type masses read through the conjugate, the lifted frozen point and its reciprocal give all four tree Dirac masses equal ($1$ and $\Lambda/3$), with $O(\Lambda)$ admixtures, in a unit set by the lift rather than by the frozen point.
