---
id: pairing.stabiliser-parabolic-algebra-null-direction
kind: claim
version: 4
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
Then a bivector $B$ stabilises $W$ (that is, $B\cdot W \subseteq W$, which is the condition for the spin action of $B$ to fix the vacuum ray) if and only if $\pv(B) = 0$. On the basis, $\pv(e_{01}) = \pv(e_{23}) = 0$, $\pv(e_{02}) = 1$, $\pv(e_{03}) = i$, $\pv(e_{12}) = -1$, $\pv(e_{13}) = -i$; the stabiliser has complex dimension five, and its real points form the four-dimensional parabolic algebra of the null direction $\ell$,
\[
\mathfrak{p}(\ell) = \operatorname{span}_{\R}\{\,e_{01},\ e_{23},\ \ell e_{2},\ \ell e_{3}\,\},
\]
the boost in the plane of $\ell$, the rotation about its axis, and the two null rotations fixing $\ell$. The null rotations about $n$ move the vacuum: $\pv(n e_{2}) = 2$, $\pv(n e_{3}) = 2i$. The class of $B$ is the $\mb$-component of $B\cdot\ell$: $\pv(B) = 0$ exactly when $B\cdot\ell \in \operatorname{span}\{\ell, m\}$.

## technical
Let $W = \operatorname{span}\{\ell, m\} \subset \C^4$ and $\pi(B) = \ip{B \cdot \ell}{m}$ on $\so(4, \C)$. A bivector $B$ stabilises $W$, which is the condition for its spin action to fix the vacuum ray, exactly when $\pi(B) = 0$; equivalently, $\pi(B)$ is the $\bar m$-component of $B \cdot \ell$.

The stabiliser has complex dimension five, and its real points form the four-dimensional parabolic algebra $\mathfrak{p}(\ell) = \operatorname{span}_\R\{e_{01}, e_{23}, \ell e_2, \ell e_3\}$: the boost in the plane of $\ell$, the rotation about its axis, and the two null rotations fixing $\ell$. The null rotations about $n$ move the vacuum, with $\pi(n e_2) = 2$ and $\pi(n e_3) = 2i$.

## lay
A vacuum here is labelled by a light-like direction. This result identifies exactly which Lorentz transformations leave it unchanged: a boost along that direction, a rotation about it, and two null rotations that keep the direction fixed. Every other transformation moves the vacuum, and a single number measures by how much.

## one-liner
A Lorentz bivector fixes the vacuum ray exactly when $\pi(B) = \ip{B \cdot \ell}{m}$ vanishes, and the real solutions form the four-dimensional parabolic algebra of the null direction $\ell$.
