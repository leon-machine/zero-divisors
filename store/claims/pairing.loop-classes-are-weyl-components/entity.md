---
id: pairing.loop-classes-are-weyl-components
kind: claim
version: 4
title: The loop classes are Weyl components
status: proved
region: pairing
subject: einstein
tags: [curvature-and-field-equations, pairing-and-bogoliubov, null-directions]
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
about:
- obj.pairing.pairing-class-transport
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - pairing.imported-weyl-scalars-petrov-type-schwarzschild@2
  - synthesis.imported-gtg-dictionary@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_six_loop_classes
- kind: check
  ref: check.py::check_null_cone_classes_vanish_iff_repeated_pnd
- kind: check
  ref: check.py::check_schwarzschild_type_d
locators:
  paper: T05-pairing
  number: Lem 5.7
  label: lem:weylclasses
  line: 360
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: on the 10-dim space of algebraic Weyl maps: the six loop classes against Psi0..Psi2, null-cone classes vanish iff Psi0 = Psi1 = 0, Schwarzschild type D with Psi2 = -M/r^3. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    added:
    - pairing.imported-weyl-scalars-petrov-type-schwarzschild
    note: 'Added the imported Weyl-scalar fact, whose definitions of the Psi and repeated-principal-direction criterion the proof and statement use; the pairing-class definition went into about.'
  env: lemma
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - pairing.imported-weyl-scalars-petrov-type-schwarzschild
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: a Ricci-flat spacetime is a vacuum gravitational field on flat spacetime (R(a) = 0), the curvature bivector R(u, v) of a loop is the covariant field strength on the physical plane u ^ v, R(hb(u ^ v)) = -R(u ^ v) in the store''s sign (as in pairing.curvature-which-loops-move-vacuum), and the pairing <.,.> is the flat product of physical vectors. Classes, identities and conclusions unchanged; the dictionary Fact added to uses for the identification; proof given a pointer.'
---

## formal
For a vacuum gravitational field on flat spacetime, $\mathcal{R}(a) = 0$ (Ricci-flat; Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), let $R(u, v) = R(\hb(u \wedge v)) = -\mathcal{R}(u \wedge v)$ be the curvature bivector of the loop $(u, v)$ of physical vectors, the covariant field strength on the plane $u \wedge v$, and write
\[
C(u, v, w, z) := \ip{R(u, v)\cdot w}{z},
\]
with the flat product of physical vectors, so that the class of the loop $(u, v)$ is $C(u, v, \ell, m)$. The six loops of the null tetrad then have classes
\[
(\ell, m) : \Psi_{0}, \quad (\ell, \mb) : 0, \quad (m, \mb) : -\Psi_{1}, \quad (\ell, n) : \Psi_{1}, \quad (n, m) : 0, \quad (n, \mb) : -\Psi_{2},
\]
up to the tetrad's normalisation. Hence every loop in the null cone of $\ell$ has zero class if and only if $\Psi_{0} = \Psi_{1} = 0$, that is, if and only if $\ell$ is a repeated principal null direction; the radial loop then has zero class as well, and only $\Psi_{2}$ remains.

## technical
For a vacuum gravitational field on flat spacetime set $C(u, v, w, z) = \ip{R(u, v)\cdot w}{z}$, with $R(u, v) = -\mathcal{R}(u \wedge v)$ the field strength on the plane of the loop, so that the class of the loop $(u, v)$ is $C(u, v, \ell, m)$. From the definitions of the Weyl scalars, the pair symmetry and the tracelessness of $C$ in the null tetrad, the six tetrad loops have classes $(\ell, m): \Psi_0$, $(\ell, \mb): 0$, $(m, \mb): -\Psi_1$, $(\ell, n): \Psi_1$, $(n, m): 0$ and $(n, \mb): -\Psi_2$, up to the tetrad's normalisation.

Hence every loop in the null cone of $\ell$ has zero class if and only if $\Psi_0 = \Psi_1 = 0$, that is, if and only if $\ell$ is a repeated principal null direction; the radial loop then has zero class as well, and only $\Psi_2$ remains.

## lay
Whether carrying the vacuum around a small loop moves it can be read directly off the standard components of the tidal part of the gravitational field strength. Loops lying in the light cone of the vacuum's direction leave it unmoved exactly when that direction is one of the curvature's doubly special directions. In that case only one component of the field strength can move the vacuum.

## one-liner
For a vacuum gravitational field on flat spacetime the pairing classes of the six null-tetrad loops are Weyl scalars, so every loop in the null cone of $\ell$ has zero class exactly when $\ell$ is a repeated principal null direction.
