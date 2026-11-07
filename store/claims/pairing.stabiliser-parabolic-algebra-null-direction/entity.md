---
id: pairing.stabiliser-parabolic-algebra-null-direction
kind: claim
version: 6
title: The stabiliser is the parabolic algebra of the null direction
status: proved
region: pairing
subject: conformal-spacetime
tags: [rotors-and-stabilisers, null-directions, pairing-and-bogoliubov]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-pairing, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 5
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle
  version: 6
  source: maintainer pass 2026-11-07 (resolve units)
review: typed
derivations:
- name: main
  uses:
  - pairing.imported-two-readings-capacities-vacuum-null@3
  - std-algebra.bivector-lie-algebra@1
  - std-algebra.orthogonal-anticommute@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_values_on_the_basis_and_null_rotations
- kind: check
  ref: check.py::check_stabiliser_is_the_kernel_of_one_functional
- kind: check
  ref: check.py::check_real_points_are_the_parabolic_algebra
- kind: check
  ref: check.py::check_spin_action_fixes_vacuum_ray_iff_pv_vanishes
locators:
  paper: T05-pairing
  number: Prop 3.1
  label: prop:stabiliser
  line: 239
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 5 -> 6. Every bare i was the scalar of the complexified spacetime C^4 on which the complex null tetrad m = e_2 + i e_3 lives; by U3 it is the central pseudoscalar I_5 = I_4 e of the odd extension Cl(2,3) (std-algebra.complexification-is-the-odd-extension, cited as a mention): m = e_2 + I_5 e_3, pv(e_03) = I_5, pv(e_13) = -I_5, pv(n e_3) = 2 I_5, so(4,C) with coefficients in span{1, I_5}. The check (Gaussian rationals) is unchanged and computes the same numbers. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (other): the values +-i and 2i are values of a complex functional on so(4,C) built on the complex null tetrad m = e_2 + i e_3 in C^4, where i stands next to a spacetime vector and no pseudoscalar can replace it.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.bivector-lie-algebra, std-algebra.orthogonal-anticommute where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the values of pv on the basis and the null rotations, stabiliser equals ker pv of dimension five, the four-dimensional real parabolic algebra, and the spin action on the two-mode vacuum. Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'The one use (the annihilator definition) is a real premise and kept; the note calls the geometric
      content the classical parabolic stabiliser of a celestial-sphere point, but no imported claim in
      the store states it (the null-flags fact gives only the celestial sphere), so no standard-route
      derivation was added. Levels pass: conditions already kept.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - "$\\pv(e_{03}) = i$, $\\pv(e_{13}) = -i$, $\\pv(n e_3) = 2i$ and the $i$ in $m = e_2 + ie_3$: complex numbers in $\\C^4$ and $\\so(4,\\C)$, a complexified spacetime with $i$ next to a spacetime vector, not the quantum unit"
---

## formal
Let $W = \operatorname{span}\{\ell, m\} \subset \C^{4}$ and define, on $\so(4,\C)$, the linear functional
\[
\pv(B) := \ip{B\cdot\ell}{m} .
\]
Here $\C^{4} = \R^{1,3} \oplus I_{5}\R^{1,3}$ is the complexification of spacetime by the central pseudoscalar $I_{5} = I_{4}e$ of the odd extension $\Cl(2,3)$ (\claimref{std-algebra.complexification-is-the-odd-extension}), which commutes with every vector; the complex null tetrad is $m = e_{2} + I_{5}e_{3}$, $\mb = e_{2} - I_{5}e_{3}$, $\so(4,\C)$ is the space of bivectors with coefficients in $\mathrm{span}\{1, I_{5}\}$, and $\pv$ takes values in that field. Then a bivector $B$ stabilises $W$ (that is, $B\cdot W \subseteq W$, which is the condition for the spin action of $B$ to fix the vacuum ray) if and only if $\pv(B) = 0$. On the basis, $\pv(e_{01}) = \pv(e_{23}) = 0$, $\pv(e_{02}) = 1$, $\pv(e_{03}) = I_{5}$, $\pv(e_{12}) = -1$, $\pv(e_{13}) = -I_{5}$; the stabiliser has complex dimension five, and its real points form the four-dimensional parabolic algebra of the null direction $\ell$,
\[
\mathfrak{p}(\ell) = \operatorname{span}_{\R}\{\,e_{01},\ e_{23},\ \ell e_{2},\ \ell e_{3}\,\},
\]
the boost in the plane of $\ell$, the rotation about its axis, and the two null rotations fixing $\ell$. The null rotations about $n$ move the vacuum: $\pv(n e_{2}) = 2$, $\pv(n e_{3}) = 2I_{5}$. The class of $B$ is the $\mb$-component of $B\cdot\ell$: $\pv(B) = 0$ exactly when $B\cdot\ell \in \operatorname{span}\{\ell, m\}$.

## technical
Let $W = \operatorname{span}\{\ell, m\} \subset \C^4$ and $\pi(B) = \ip{B \cdot \ell}{m}$ on $\so(4, \C)$, where $\C^4 = \R^{1,3} \oplus I_5\R^{1,3}$ is spacetime complexified by the central pseudoscalar $I_5$ of $\Cl(2,3)$ and $m = e_2 + I_5e_3$. A bivector $B$ stabilises $W$, which is the condition for its spin action to fix the vacuum ray, exactly when $\pi(B) = 0$; equivalently, $\pi(B)$ is the $\bar m$-component of $B \cdot \ell$.

The stabiliser has complex dimension five, and its real points form the four-dimensional parabolic algebra $\mathfrak{p}(\ell) = \operatorname{span}_\R\{e_{01}, e_{23}, \ell e_2, \ell e_3\}$: the boost in the plane of $\ell$, the rotation about its axis, and the two null rotations fixing $\ell$. The null rotations about $n$ move the vacuum, with $\pi(n e_2) = 2$ and $\pi(n e_3) = 2I_5$.

## lay
A vacuum here is labelled by a light-like direction. This result identifies exactly which Lorentz transformations leave it unchanged: a boost along that direction, a rotation about it, and two null rotations that keep the direction fixed. Every other transformation moves the vacuum, and a single number measures by how much.

## one-liner
A Lorentz bivector fixes the vacuum ray exactly when $\pi(B) = \ip{B \cdot \ell}{m}$ vanishes, and the real solutions form the four-dimensional parabolic algebra of the null direction $\ell$.
