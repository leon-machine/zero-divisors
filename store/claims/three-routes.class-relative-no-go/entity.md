---
id: three-routes.class-relative-no-go
kind: claim
version: 6
title: The class-relative no-go
status: proved
region: three-routes
subject: walls
tags:
- no-go
- ladder-pairs
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-three-routes, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - sheaf.function-linearity-tame-constructions@2
  - three-routes.function-linear-maps-preserve-supports@2
  - three-routes.support-preserving-families-quantise-without-hopping@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_function_linear_maps_are_diagonal
- kind: check
  ref: check.py::check_bundle_maps_quantise_without_hopping
- kind: check
  ref: check.py::check_off_diagonal_generators_hop
locators:
  paper: T05-three-routes
  number: Thm 4.3
  label: thm:hopping
  line: 252
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: on a three-point model, function-linear maps are diagonal, their second quantisations and sigma_x sigma_y conserve all occupations, while off-diagonal and difference operators hop. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5. Check strengthened: support-preserving count and a commutator pinned; the difference operator checked against every occupation; sample maps moved to module level. Version 5 -> 6.'
  typing:
    by: ai-typing-pass
    removed:
    - singularity.p-reduced-metric-level-reading-many
    added:
    - sheaf.function-linearity-tame-constructions
    note: The proof uses only part (ii) of the imported composite fact, the function-linearity of the tame machinery,
      whose source is the T4 function-linearity proposition; the store claim the label map gives for that fact covers
      only part (i), so the edge was redirected.
  env: theorem
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - sheaf.function-linearity-tame-constructions
    note: The existing claimref to singularity.p-reduced-metric-level-reading-many(ii), in proof and statement,
      is the label-map error the typing pass recorded; the correct premise is cited beside it and the stale pointer
      is left for the maintainer.
  source_formal: 'Every generator the tame machinery supplies is $C^\infty$-linear (Fact \claimref{singularity.p-reduced-metric-level-reading-many}(ii):
    the machinery is algebra-linear in the coefficient functions and never differentiates them). Hence, by Lemma
    \claimref{three-routes.function-linear-maps-preserve-supports} and Proposition \claimref{three-routes.support-preserving-families-quantise-without-hopping},
    no generator supplied by the localisation, the completion, or any construction of the physical closure moves
    occupation from the ladder at one point of $\Sig$ to the ladder at another. Within the supplied class, the diagonality
    half of T5''s Premise 7.30 is a theorem: the available cross-point structure is exhausted by occupation-conserving
    products such as $\sigma_x\sigma_y$, which is exactly the class the premise permits and the finite-ledger model
    uses.'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 8
    note: The citation of the machinery's linearity pointed at singularity.p-reduced-metric-level-reading-many,
      which carries only part (i) of the note's Fact 1.3 (the composite proposition); part (ii), the linearity,
      is sheaf.function-linearity-tame-constructions, now the only citation.
---

## formal
Every generator the tame machinery supplies is $C^\infty$-linear (the note's Fact 1.3(ii), \claimref{sheaf.function-linearity-tame-constructions}: the machinery is algebra-linear in the coefficient functions and never differentiates them). Hence, by Lemma \claimref{three-routes.function-linear-maps-preserve-supports} and Proposition \claimref{three-routes.support-preserving-families-quantise-without-hopping}, no generator supplied by the localisation, the completion, or any construction of the physical closure moves occupation from the ladder at one point of $\Sig$ to the ladder at another. Within the supplied class, the diagonality half of T5's Premise 7.30 is a theorem: the available cross-point structure is exhausted by occupation-conserving products such as $\sigma_x\sigma_y$, which is exactly the class the premise permits and the finite-ledger model uses.

## technical
Every generator the tame machinery supplies is $C^\infty$-linear: its constructions are algebra-linear in the coefficient functions and never differentiate them. A $C^\infty$-linear endomorphism preserves supports and is therefore a bundle map, and a bundle map second-quantises to a sum of single-point bilinears that commutes with every occupation number. Hence no generator supplied by the localisation, the completion or any construction of the physical closure moves occupation from the ladder at one point of $\Sig$ to the ladder at another.

Within the supplied class, the diagonality half of the ledger-locality premise is thus a theorem: the available cross-point structure is exhausted by occupation-conserving products such as $\sigma_x\sigma_y$. The statement is relative to that class; generators outside it, such as differential operators, are not covered.

## lay
None of the constructions the series uses to describe the black-hole boundary can move a particle from one point of the boundary to another. This is because all of them act point by point and never compare neighbouring points. Correlations between points that leave each point's occupation unchanged are still allowed, and a dynamics that does compare neighbouring points lies outside the result.

## one-liner
Every generator supplied by the tame machinery is function-linear, so none moves occupation between the ladders at different points of $\Sig$.
