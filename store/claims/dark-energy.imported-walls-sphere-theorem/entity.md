---
id: dark-energy.imported-walls-sphere-theorem
kind: claim
version: 6
title: 'Imported: walls, and the sphere theorem'
status: proved
region: dark-energy
subject: walls
tags: [degenerate-algebras, witt-index, boundary-modes]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
review: typed
about:
- obj.sheaf.clifford-sheaf
derivations:
- name: main
  uses:
  - scrambling.boundary-mode-space-matrix@4
  - scrambling.consistency-car-construction-i-states-insensitivity@5
  - scrambling.principality-indifference-sphere@4
  - sheaf.degeneration-sheaf@6
  - sheaf.localised-transport@5
  - sheaf.metrics-residue-square-root-twist@5
  - std-algebra.vector-squares@1
  assumes:
  - sheaf.tameness@1
  - scrambling.indifference-structural-premise-series@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_radical_and_simple_pole
- kind: check
  ref: check.py::check_clifford_algebra_continues_with_square_zero_ideal
- kind: check
  ref: check.py::check_witt_partner_exactly_at_the_wall
- kind: check
  ref: check.py::check_principal_su2_carried_by_boundary_bilinears
locators:
  paper: T10
  number: Fact 2.4
  label: fact:walls
  line: 652
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.vector-squares where the proof uses them. Version 5 -> 6.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: radical and simple pole on model walls, the Clifford algebra across the wall with square-zero ideal, the Witt partner, and the principal su(2) carried by boundary-mode bilinears. Version 4 -> 5.'
  env: fact
  context_refs:
  - dark-energy.sheaf-papers-wall-soldering-variables
  - dark-energy.walls-free-sector
  - scrambling.boundary-mode-space-matrix
  - scrambling.consistency-car-construction-i-states-insensitivity
  - scrambling.indifference-structural-premise-series
  - scrambling.principality-indifference-sphere
  - sheaf.degeneration-sheaf
  - sheaf.localised-transport
  - sheaf.metrics-residue-square-root-twist
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    added:
    - sheaf.tameness
    note: 'Added the tameness hypothesis as an assumption, since the fact is stated at a tame corank-one
      wall; kept all seven provenance premises, including the Indifference principle, which its source
      declares a premise but which the store holds as proved, so it stays in uses rather than assumes;
      the two parenthetical references to the soldering-variables proposition and the free-sector theorem
      are comparisons and were left out. Hypothesis pass: moved scrambling.indifference-structural-premise-series
      from uses to assumes, now that it is a postulate. Levels pass: lay now names the tameness condition
      and the Indifference principle.'
---

## formal
At a tame corank-one wall the cometric on covectors acquires a one-dimensional radical $\mathcal{L}$, the Clifford sheaf continues across the wall, the physical metric has a simple pole along $\mathcal{L}\otimes\mathcal{L}$ with $\mathcal{L}^{\otimes 2} \cong N^*\Sigma$, and the completion adjoins the Witt partner $k^*$ of the radical covector $k$ exactly there, with $kk^* + k^*k = 1$, that is $\ip{k}{k^*} = \tfrac12$ (the ambient basis of Proposition \claimref{dark-energy.sheaf-papers-wall-soldering-variables}(iii) rescales $k^*$ to $\ip{k}{k^*} = 1$, which changes nothing); the transverse sphere is carried by the bilinear matrix algebra of the boundary modes through the principal embedding, so that every angular operator of the lift is a boundary-mode bilinear under the adjoint $\mathfrak{su}(2)$; this last clause, the sphere theorem, is derived in the entropy paper under its Indifference principle (\cite[Principle~5.4]{ButlerT8}: a construction may not carry distinctions that nothing in the framework determines), which that paper declares a premise and not a theorem, and it is conditional on that premise wherever it is used here. \emph{Provenance:} \cite[Thm.~3.1, Cor.~4.5, Thm.~6.2]{ButlerT4}; \cite[Prop.~5.2, Principle~5.4, Thm.~5.5, Prop.~5.6]{ButlerT8}. (The degeneration of the soldering form used in Theorem \claimref{dark-energy.walls-free-sector} is the dual type, a metric on tangent vectors with a radical; Proposition \claimref{dark-energy.sheaf-papers-wall-soldering-variables} states the relation.)

## technical
At a tame corank-one wall $\Sigma$ the cometric on covectors acquires a one-dimensional radical $\mathcal{L}$, spanned by a covector $k$. The Clifford sheaf continues across the wall, and the physical metric has a simple pole along $\mathcal{L}\otimes\mathcal{L}$ with $\mathcal{L}^{\otimes 2} \cong N^*\Sigma$, so the dying line is a square root of the conormal bundle. Exactly there the completion adjoins a Witt partner $k^*$ of the radical covector, with $kk^* + k^*k = 1$, that is $\ip{k}{k^*} = \tfrac12$; rescaling $k^*$ to $\ip{k}{k^*} = 1$ changes nothing.

The imported sphere theorem adds that the transverse sphere is carried by the bilinear matrix algebra of the boundary modes through the principal embedding, so every angular operator of the lift is a boundary-mode bilinear under the adjoint $\mathfrak{su}(2)$. This clause is derived under the Indifference principle (a construction may not carry distinctions that nothing in the framework determines), which its source declares a premise and not a theorem, so it holds only conditionally on that premise.

## lay
Where geometry degenerates in the mildest, tame way, along a wall where one direction stops being measurable, the algebraic description of geometry does not break but carries on through the wall. The metric blows up there in a controlled way, and the completion adds exactly one partner to the dying direction. A further imported result, which rests on an assumed principle (the Indifference principle) rather than a proof, says that the sphere of directions around the wall is built from pairings of the wall's boundary modes.

## one-liner
At a tame corank-one wall the Clifford sheaf continues, the metric has a simple pole with $\mathcal{L}^{\otimes 2} \cong N^*\Sigma$, the completion adjoins a Witt partner of the radical covector, and, under the Indifference principle, the transverse sphere is carried by boundary-mode bilinears.
