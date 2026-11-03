---
id: scrambling.principality-indifference-sphere
kind: claim
version: 4
title: 'Principality from indifference: the sphere'
status: proved
region: scrambling
subject: entropy
tags: [indifference, representation-theory, forcing-and-uniqueness]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
review: typed
derivations:
- name: main
  uses:
  - scrambling.boundary-mode-space-matrix@4
  - scrambling.imported-kostant-madore-partition-data@1
  - scrambling.imported-time-plane-modular-data@1
  assumes:
  - scrambling.indifference-structural-premise-series@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - label:thm:sphere
- kind: check
  ref: check.py::check_triples_and_partition_data
- kind: check
  ref: check.py::check_principal_is_multiplicity_free
- kind: check
  ref: check.py::check_round_irreducible_sphere_only_for_principal
locators:
  paper: T08
  number: Thm 5.5
  label: thm:sphere
  line: 871
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: for every partition of n = 2..6: sl2 relations, Jordan type recovers the partition, adjoint summands and highest weights (multiplicity free only for the principal embedding), Casimir and commutant. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: theorem
  context_refs:
  - scrambling.boundary-mode-space-matrix
  - scrambling.imported-time-plane-modular-data
  - scrambling.indifference-structural-premise-series
  typing:
    by: ai-typing-pass
    added:
    - scrambling.boundary-mode-space-matrix
    - scrambling.imported-time-plane-modular-data
    - scrambling.indifference-structural-premise-series
    note: 'Added the indifference principle (the theorem is stated under it; it is recorded as proved,
      so it goes in uses, though the source calls it a premise and it arguably should be a postulate),
      the matrix proposition supplying the su(2)-carrying algebra, and the time-and-plane Fact behind
      the three-of-four-dimensions clause; that last addition is the least certain. Hypothesis pass: moved
      scrambling.indifference-structural-premise-series from uses to assumes, now that it is a postulate.
      Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - scrambling.boundary-mode-space-matrix
    - scrambling.indifference-structural-premise-series
    stated_role:
    - scrambling.imported-time-plane-modular-data
    note: 'the assumed indifference Principle, not on the cite list, was also uncited; cited where the proof applies it.'
---

## formal
Under Principle \claimref{scrambling.indifference-structural-premise-series}, the $\mathfrak{su}(2)$ structure carried by the matrix algebra of the boundary modes (Proposition \claimref{scrambling.boundary-mode-space-matrix}) is the principal embedding, uniquely: a non-principal embedding decomposes the $n$ modes into invariant blocks, a partition whose sizes and assignments nothing in the framework causes (Fact \claimref{scrambling.imported-kostant-madore-partition-data}(i)), and indifference forbids exactly such uncaused data; the principal embedding is the unique one carrying no partition data, its internal distinctions forced by the algebra once conjugation-gauge is fixed. Consequently the bilinear sector of the boundary modes is canonically Madore's fuzzy sphere, and its large-$n$ limit is the round transverse $S^2$, radius state-side: three of the four emergent dimensions now rest on the correlation structure (time and the plane from Fact \claimref{scrambling.imported-time-plane-modular-data}, the sphere from this theorem), the fourth being scale. The conclusion is conditional on Principle \claimref{scrambling.indifference-structural-premise-series} wherever this theorem is cited.

## technical
Assume the indifference principle, which forbids distinctions that nothing in the framework determines. The $\mathfrak{su}(2)$ structure carried by the matrix algebra of the boundary modes must then be the principal embedding: a non-principal embedding splits the $n$ modes into invariant blocks, a partition nothing causes, while the principal embedding is the unique one carrying no partition data.

The bilinear sector is then canonically Madore's fuzzy sphere, with the round transverse $S^2$ as its large-$n$ limit and the radius left to the state. With time and the plane obtained from modular data, three of the four emergent dimensions then rest on the correlation structure, the fourth being scale; all of this is conditional on indifference.

## lay
The matrix structure of the black hole's boundary modes can be arranged to behave like rotations in several ways. If the framework may not introduce arbitrary choices it has no reason for, only one arrangement survives, and it turns the modes into a fuzzy sphere that becomes an ordinary sphere when there are many modes. This lets the angular directions of space emerge from the modes, provided the no-arbitrary-choices principle holds.

## one-liner
Under the indifference principle the boundary modes' $\mathfrak{su}(2)$ structure is the principal embedding, so their bilinear sector is Madore's fuzzy sphere with the round $S^2$ as limit.
