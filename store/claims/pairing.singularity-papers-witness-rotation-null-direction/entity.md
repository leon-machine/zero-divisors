---
id: pairing.singularity-papers-witness-rotation-null-direction
kind: claim
version: 3
title: The singularity paper's witness is a rotation of the null direction
status: proved
region: pairing
subject: singularity
tags: [witt-index, null-directions, finite-models]
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
  - pairing.imported-null-flags@1
  - pairing.pairing-functional-pair-creation-amplitude@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_rotor_rotates_the_null_direction
- kind: check
  ref: check.py::check_rotated_state_is_the_rotated_witt_vacuum
- kind: check
  ref: check.py::check_rotation_acts_through_its_pairing_class
- kind: check
  ref: check.py::check_boost_rotor_fixes_the_ray
locators:
  paper: T05-pairing
  number: Cor 3.4
  label: cor:witness
  line: 271
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: R = 3/5 + 4/5 e12 rotates l to e0 - 7/25 e1 + 24/25 e2 with <R l R~, l> = 32/25, R|0> = 3/5|0> + 4/5|12> is annihilated by the rotated null vectors, pv(e12) = -1, and the boost rotor acts on |0> as 1/3. Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  typing:
    by: ai-typing-pass
    note: 'both uses edges are cited in the proof as premises; the stabiliser-tangent fact (context ref) is the object whose witness is being identified, not a premise of the computation, so it was not added.'
  env: corollary
  context_refs:
  - pairing.imported-stabiliser-tangent
---

## formal
The rotor $R = \tfrac35 + \tfrac45\, e_{12}$ acts on the Fock module by $R\ket{0} = \tfrac35\ket{0} + \tfrac45\ket{12}$, with no odd component, and on vectors by $\ell \mapsto R\ell\tilde R = e_{0} - \tfrac{7}{25}e_{1} + \tfrac{24}{25}e_{2}$, a null vector not proportional to $\ell$ ($\ip{R\ell\tilde R}{\ell} = \tfrac{32}{25}$). The state $R\ket{0}$ is annihilated by $R\ell\tilde R$ and $Rm\tilde R$, so it is the Witt vacuum of the rotated decomposition. The necessity witness of Fact \claimref{pairing.imported-stabiliser-tangent} is therefore the spin action of a real rotation of the frame about the $e_{3}$ axis, by the double angle with $(\cos, \sin) = (-\tfrac{7}{25}, \tfrac{24}{25})$: a mismatch of two Witt decompositions at a point is half the angle between two null directions, the half being Fact \claimref{pairing.imported-null-flags}'s and the instance the one computed. By contrast the boost rotor $\tfrac53 + \tfrac43\,e_{01}$ of the singularity paper's Step 4a acts on $\ket{0}$ as the scalar $\tfrac13$ and fixes the ray.

## technical
On the two-mode Fock module the rotor $R = \tfrac35 + \tfrac45\,e_{12}$ sends $\ket{0}$ to $\tfrac35\ket{0} + \tfrac45\ket{12}$, with no odd component, and rotates the null vector $\ell$ to $R\ell\tilde R = e_0 - \tfrac{7}{25}e_1 + \tfrac{24}{25}e_2$, a null vector not proportional to $\ell$, with $\ip{R\ell\tilde R}{\ell} = \tfrac{32}{25}$. Since $R\ket{0}$ is annihilated by $R\ell\tilde R$ and $Rm\tilde R$, it is the Witt vacuum of the rotated decomposition.

So the necessity witness of the imported stabiliser fact is the spin action of a real rotation of the frame about the $e_3$ axis, by the double angle with $(\cos, \sin) = (-\tfrac{7}{25}, \tfrac{24}{25})$: a mismatch of two Witt decompositions at a point is half the angle between two null directions. By contrast the boost rotor $\tfrac53 + \tfrac43\,e_{01}$ of the singularity analysis acts on $\ket{0}$ as the scalar $\tfrac13$ and fixes the vacuum ray.

## lay
In this algebraic picture a vacuum state is tied to a light-like direction. The result works through one explicit example: an ordinary spatial rotation turns that light-like direction into a different one and turns the vacuum into a new vacuum, mixing in a pair of excitations. By contrast, the boost used in the black-hole analysis leaves the vacuum's direction alone and only rescales the state.

## one-liner
The witness that two Witt decompositions can differ is the spin action of a real rotation, which moves the vacuum's null direction, whereas the boost of the singularity analysis only rescales the vacuum.
