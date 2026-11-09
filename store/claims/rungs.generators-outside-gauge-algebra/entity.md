---
id: rungs.generators-outside-gauge-algebra
kind: claim
version: 8
title: The generators outside the gauge algebra
status: proved
region: rungs
subject: standard-model
tags: [gauge-fields, mode-counting, ladder-pairs, representation-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-rungs, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'maintainer pass, which-unit sentence in the proof at Leon''s decisions'
  version: 8
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  uses:
  - rungs.imported-fock-representation-bogoliubov-group@4
  - standard-model.hyp-s-slot-statistics@10
  assumes:
  - rungs.hyp-r-rung-reading@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_mode_number_preserving_is_u5
- kind: check
  ref: check.py::check_split_preserving_is_u2_u3
locators:
  paper: T12-rungs
  number: Prop 2.7
  label: prop:outside
  line: 291
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 7 -> 8. Decision item C3 (routine): the proof''s unit sentence (''the imaginary unit is I_4, which commutes with every mode operator'') now says which unit acts where: on the five-mode Fock module numbers, I_4 among them, act as scalars (U1); as Clifford elements I_4 commutes with the rung vectors, and the pair vectors of V_C (with which obj.standard-model.two-rung-module-sectors-slot-components and standard-model.ten-transported-ambient-space-doublets-are identify the ten) are complexified by I_7 (std-algebra.complexification-is-the-odd-extension), which is not used here. A which-unit sentence; it identifies nothing and the mathematics is unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the counts 25, 13, 12 and 20 as exact kernel dimensions of ad N, ad N_R and ad N_W on the 45 Majorana bilinears of the five-mode module. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 6 -> 7.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted:
    - 'proof: the Majorana generators gamma_{2i+1} = I4(a_i - a_i^dagger) of the five modes and the factors of I4 in the u(5) and pair-creating bilinears (CAR algebra of the tower)'
    - 'technical level: ''up to factors of I4'''
    kept:
    - 'every subscript i (mode index)'
  source_formal: |-
    Under (R) or (S), of the forty-five generators of $\mathfrak{so}(10)$ acting on the composite's modes, exactly thirteen preserve the slot-pair split and the mode number, spanning $\uu(2) \oplus \uu(3)$; exactly twenty-five preserve the mode number, spanning $\uu(5)$; so thirty-two lie outside $\uu(2) \oplus \uu(3)$, twelve of them inside $\uu(5)$, moving one excitation between a rung and a pair, and twenty changing the mode number by two.
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'Kept the Fock-representation edge, the only premise the proof cites; (R) and (S) are not in
      the store as postulates, so nothing was added to assumes. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S); assumes rungs.hyp-r-rung-reading added because
      its statement holds under (R) or (S); both are recorded, the disjunction being a relabelling. Levels
      pass: the lay level now states (R) or (S), which it had dropped, and no longer calls $\mathfrak{u}(2)
      \oplus \mathfrak{u}(3)$ the Standard Model''s symmetry outright, since it carries one abelian factor
      more.'
    added:
    - standard-model.hyp-s-slot-statistics
    - rungs.hyp-r-rung-reading
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.hyp-s-slot-statistics
    - rungs.hyp-r-rung-reading
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under (R) or (S), of the forty-five generators of $\mathfrak{so}(10)$ acting on the composite's modes, exactly thirteen preserve the slot-pair split and the mode number, spanning $\uu(2) \oplus \uu(3)$; exactly twenty-five preserve the mode number, spanning $\uu(5)$; so thirty-two lie outside $\uu(2) \oplus \uu(3)$, twelve of them inside $\uu(5)$, moving one excitation between a rung and a pair, and twenty changing the mode number by two.

## technical
Under the rung reading (R) or the slot-statistics hypothesis (S), the composite has five fermionic modes, two slots (the rungs) and three pairs, and the forty-five Majorana bilinears $\gamma_{p}\gamma_{q}$ span $\so(10)$. Twenty-five of them commute with the total mode number and span $\uu(5)$; of these, the thirteen that also preserve the slot number and the pair number separately span $\uu(2) \oplus \uu(3)$.

So thirty-two generators lie outside $\uu(2) \oplus \uu(3)$: twelve inside $\uu(5)$, each moving one excitation between a rung and a pair, and twenty of the form $a_{i}a_{j} \pm a_{i}^{\dagger}a_{j}^{\dagger}$ (up to factors of $I_{4}$), which change the mode number by two. The two centralisers are computed as exact kernels, of dimensions $25$ and $13$.

## lay
Under the paper's rung reading (R), or equivalently Hypothesis (S), the composite's internal states are built from five on-off modes, two of one kind and three of another. Of the forty-five basic symmetry moves available on such a system, thirteen keep the two kinds separately counted, and these form the Standard Model's symmetry together with one extra charge. The other thirty-two either move an excitation from one kind of mode to the other, or create or remove two excitations at once.

## one-liner
Under (R) or (S), of the forty-five $\so(10)$ generators on the composite's modes, thirteen span $\uu(2) \oplus \uu(3)$, twelve more complete $\uu(5)$ by moving an excitation between a rung and a pair, and twenty change the mode number by two.
