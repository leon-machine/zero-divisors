---
id: singularity.bundle-maps-quantise-without-hopping
kind: claim
version: 3
title: Bundle maps quantise without hopping
status: proved
region: singularity
subject: entropy
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_bundle_map_quantises_to_multiplication_operator
- kind: check
  ref: check.py::check_controlled_z_conserves_occupations
- kind: check
  ref: check.py::check_cross_component_hops
locators:
  paper: T05
  number: Prop C.7
  label: prop:quantiseT5
  line: 2698
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: on a three-point Jordan-Wigner Fock space, dGamma of bundle maps is the multiplication operator sum a_j N_j, sigma_x sigma_y conserves occupations, and cross components carry (0,1) to (1,0). Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: No store premises; the proof applies the definition of second quantisation directly.
---

## formal
On a finite truncation the second quantisation of a bundle map $\{a_x\}$ of the mode line bundle is the sum of single-point bilinears $d\Gamma(a) = \sum_j \psi^{\dagger}_{x_j} a_{x_j} \psi_{x_j} = \sum_j a_{x_j} N_{x_j}$, a multiplication operator in the joint number basis, commuting with every occupation number. A one-particle map with a cross component $a_{xy} \neq 0$, $x \neq y$, quantises instead to a generator containing $\psi^{\dagger}_x\psi_y$, which carries the sector $(N_x, N_y) = (0,1)$ onto $(1,0)$.

## technical
On a finite truncation, the second quantisation of a bundle map $\{a_x\}$ of the mode line bundle is a sum of single-point terms, $d\Gamma(a) = \sum_j a_{x_j} N_{x_j}$. It is therefore a multiplication operator in the joint number basis and commutes with every occupation number.

By contrast, a one-particle map with a cross component $a_{xy} \neq 0$, $x \neq y$, quantises to a generator containing $\psi^{\dagger}_x\psi_y$, which carries the sector $(N_x, N_y) = (0,1)$ onto $(1,0)$: that is hopping.

## lay
A bundle map acts separately at each point and never mixes different points. When such a map is turned into an operator on many-particle states, the result simply weighs each point by how many particles sit there, so it never moves a particle from one point to another. A map that does link two points, by contrast, produces exactly such a move.

## one-liner
The second quantisation of a bundle map is a sum of single-point number operators and never hops, whereas any cross-point component produces hopping.
