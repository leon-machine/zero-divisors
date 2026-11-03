---
id: tower.wall-package
kind: claim
version: 5
title: The wall package
status: proved
region: tower
subject: walls
tags: [degenerate-algebras, hyperbolic-plane, transport-algorithm]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T03, deposited version
review: typed
about:
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - sheaf.conservation-degeneracy-absolute-form@4
  - sheaf.conservation-degeneracy-located@3
  - sheaf.infinite-wall-sequence@4
  - sheaf.one-sided-completion@4
  - sheaf.tame-wall-induction@5
  - transport.totality@3
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_completion_nondegenerate_up_to_the_wall
- kind: check
  ref: check.py::check_degeneracy_relocated_to_shadow_wall
- kind: check
  ref: check.py::check_iterated_walls_tame_one_plane_each
locators:
  paper: T03
  number: Fact 6.1
  label: fact:walls
  line: 460
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: in the iterated collar model, the completion is (2,4) up to the wall, degeneracy moves to the shadow wall and every coupling degenerates somewhere, and each shadow wall is tame with signature (2+k, 4+k). Version 4 -> 5.'
  typing:
    by: ai-typing-pass
    note: 'Fact restating cited series results; all six premises are the cited sources and were kept,
      with tameness remaining in assumes. Levels pass: the lay level now keeps the trivial-radical-line
      condition and the good-couplings condition for the iteration; the one-liner adds good couplings.'
  env: fact
  context_refs:
  - sheaf.conservation-degeneracy-absolute-form
  - sheaf.conservation-degeneracy-located
  - sheaf.infinite-wall-sequence
  - sheaf.one-sided-completion
  - sheaf.tame-wall-induction
  - transport.totality
  flags:
  - 'fact restating several series results: derived from them'
---

## formal
Let $(M, G)$ be a tame corank-one degeneration in the sense of \cite[Hyp.~2.1]{ButlerT4}, with wall $\Sigma$ and radical line bundle $\mathcal{L}$. Assume the radical line bundle is trivial, $w_1(\mathcal{L}) = 0$, so that collar data exist. Then the one-sided completion of \cite[Thm.~4.4]{ButlerT4} is nondegenerate up to and including the wall; the transported reciprocal divides totally there, by \cite[Thm.~4.10]{ButlerT1}; and conservation of degeneracy \cite[Thm.~5.1, Prop.~5.2]{ButlerT4} relocates the degeneration to a shadow wall. Assume further that $\Sigma$ is compact. Then the shadow wall is itself tame for good couplings \cite[Lem.~5.3]{ButlerT4}, and the resulting infinite wall sequence adjoins exactly one hyperbolic plane to the ambient fibre form per wall \cite[Rem.~5.4, Cor.~5.5]{ButlerT4}, each shadow wall's radical line being trivial automatically. \emph{Provenance:} as cited, all in reviewable papers of this series.

## technical
Let $(M, G)$ be a tame corank-one degeneration with wall $\Sigma$ and radical line bundle $\mathcal{L}$, and assume $w_1(\mathcal{L}) = 0$, so that collar data exist. Then the one-sided completion is nondegenerate up to and including the wall, the transported reciprocal divides totally there, and conservation of degeneracy relocates the degeneration to a shadow wall.

If in addition $\Sigma$ is compact, the shadow wall is itself tame for good couplings, and iterating gives an infinite wall sequence that adjoins exactly one hyperbolic plane to the ambient fibre form per wall, each shadow wall's radical line being trivial automatically. These results are carried over from earlier papers in the series.

## lay
When a geometry degenerates along a wall in a controlled, tame way, and the dying direction can be oriented consistently along the wall, adding two extra directions removes the degeneracy at the wall. The degeneracy does not disappear, though; it reappears at a nearby shadow wall. If the wall is compact, and the couplings are suitably chosen, the process can be repeated indefinitely, each step adding one more pair of directions. This summary is carried over from earlier work in the series and holds under the tameness assumption.

## one-liner
Under tameness and a trivial radical line bundle the one-sided completion is nondegenerate through the wall and relocates the degeneracy to a shadow wall; for a compact wall and good couplings this iterates, adding one hyperbolic plane per wall.
