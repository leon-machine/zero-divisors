---
id: correspondence.imported-stabilisers-flat-model
kind: claim
version: 3
title: 'Imported: stabilisers in the flat model'
status: proved
region: correspondence
subject: conformal-spacetime
tags: [conformal-model, rotors-and-stabilisers]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
derivations:
- name: main
  uses:
  - interior.stabilisers-flat-model@5
  - transport.no-go-level-elements@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_stabiliser_is_poincare
- kind: check
  ref: check.py::check_ray_stabiliser_is_parabolic
- kind: check
  ref: check.py::check_nilradical_translations_and_two_step
locators:
  paper: T09
  number: Fact 4.3
  label: fact:parabolic
  line: 475
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: in Cl(2,4), the stabiliser of nInf as an exact kernel of dimension 10 = Lambda^2 W + nInf W with Poincare brackets, the ray stabiliser of dimension 11 with the grading element, and translations T_a X(x) = X(x + a) with two-step nilpotent ad. Version 2 -> 3.'
  env: fact
  context_refs:
  - interior.stabilisers-flat-model
  - transport.no-go-level-elements
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: Fact restating earlier series results; both existing edges are the cited sources and were kept.
---

## formal
In $\Lambda^2 V \cong \mathfrak{so}(2,4)$, the stabiliser of the null vector $\nInf$ is $\Lambda^2 W_{1,3} \oplus (\nInf\wedge W_{1,3}) \cong \mathfrak{so}(1,3)\ltimes\R^4$, the Poincar\'e algebra; the stabiliser of the ray $\R^+\nInf$ adds the grading element $\nInf\wedge\nO$ and is the eleven-dimensional maximal parabolic; the nilradical acts on the point space as the translations and consists of the two-step nilpotent transvections of the series' no-go theorem. \emph{Provenance:} \cite[Prop.~4.3]{ButlerT6}; the transvection identification \cite[Thm.~4.2]{ButlerT1}.

## technical
In $\Lambda^2 V \cong \mathfrak{so}(2,4)$ the stabiliser of the null vector $\nInf$ is $\Lambda^2 W_{1,3}\oplus(\nInf\wedge W_{1,3}) \cong \mathfrak{so}(1,3)\ltimes\R^4$, the Poincar\'e algebra. The stabiliser of the ray $\R^+\nInf$ adds the grading element $\nInf\wedge\nO$ and is the eleven-dimensional maximal parabolic.

Its nilradical acts on the point space as the translations and consists of the two-step nilpotent transvections of the series' no-go theorem. Both facts are carried over from earlier papers in the series.

## lay
In the completed algebra, the symmetries that fix one special lightlike direction, the point at infinity, are exactly the symmetries of flat spacetime: rotations, boosts and translations. Allowing that direction to be rescaled adds one more symmetry, overall scaling. The translations are the same special transformations that appear in the series' earlier no-go theorem.

## one-liner
In $\mathfrak{so}(2,4)$ the stabiliser of the null vector at infinity is the Poincar\'e algebra, the stabiliser of its ray is the eleven-dimensional maximal parabolic, and its nilradical is the translations, which are the no-go theorem's transvections.
