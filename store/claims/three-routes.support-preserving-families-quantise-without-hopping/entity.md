---
id: three-routes.support-preserving-families-quantise-without-hopping
kind: claim
version: 4
title: Support-preserving families quantise without hopping
status: proved
region: three-routes
subject: walls
tags: [ladder-pairs]
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
about:
- obj.three-routes.ladder-bundle-even-subbundle
derivations:
- name: main
  uses:
  - three-routes.function-linear-maps-preserve-supports@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_three_routes.py
  tags:
  - num:4.2
- kind: check
  ref: check.py::check_bundle_maps_conserve_every_occupation
- kind: check
  ref: check.py::check_cross_components_hop
- kind: check
  ref: check.py::check_cross_point_diagonal_products_are_not_hopping
locators:
  paper: T05-three-routes
  number: Prop 4.2
  label: prop:quantise
  line: 240
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: dGamma of bundle maps conserves every occupation, cross components hop (0,1) to (1,0) exhaustively, sigma_x sigma_y conserves. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    added:
    - three-routes.function-linear-maps-preserve-supports
    note: 'Added the support lemma, invoked in the hypothesis to make the endomorphism a bundle map.'
  env: proposition
  context_refs:
  - three-routes.function-linear-maps-preserve-supports
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - three-routes.function-linear-maps-preserve-supports
---

## formal
Let $a$ be a $C^\infty$-linear endomorphism of the ladder bundle, hence by Lemma \claimref{three-routes.function-linear-maps-preserve-supports} a bundle map, acting fibrewise as $a_x : \Aa_x \to \Aa_x$. On any finite truncation $F = \{x_1, \dots, x_N\}$ its second quantisation is the sum of single-point bilinears
\[
d\Gamma(a) \;=\; \sum_{j} \psi^{\dagger}_{x_j}\, a_{x_j}\, \psi_{x_j},
\]
which commutes with every occupation number $N_{x_j}$: no such generator moves occupation between points. By contrast a one-particle map with a nonzero cross component $a_{x y}$, $x \neq y$, quantises to a generator containing $\psi^{\dagger}_x \psi_y$, which maps the occupation sector $(N_x, N_y) = (0,1)$ onto $(1,0)$.

## technical
Let $a$ be a $C^\infty$-linear endomorphism of the ladder bundle, hence a bundle map acting fibrewise as $a_x$. On any finite truncation $F = \{x_1, \dots, x_N\}$ its second quantisation is a sum of single-point bilinears, $d\Gamma(a) = \sum_j \psi^{\dagger}_{x_j} a_{x_j} \psi_{x_j}$, which commutes with every occupation number $N_{x_j}$, so it moves no occupation between points.

By contrast, a one-particle map with a nonzero cross component $a_{xy}$, $x \neq y$, quantises to a generator containing $\psi^{\dagger}_x \psi_y$, which maps the sector $(N_x, N_y) = (0,1)$ onto $(1,0)$. Cross-point products diagonal in occupation, such as $\sigma_x\sigma_y$, conserve both occupations and are not hopping.

## lay
An operation that acts separately at each point, when turned into an operation on many particles, never moves a particle from one point to another. Only an operation that links different points can do that. Operations that link points without moving particles, such as correlated sign flips, are still allowed.

## one-liner
A function-linear endomorphism of the ladder bundle second-quantises to a sum of single-point terms that conserves every occupation number, so it never moves occupation between points.
