---
id: pairing.imported-weyl-scalars-petrov-type-schwarzschild
kind: claim
version: 2
title: 'Imported: the Weyl scalars, and the Petrov type of Schwarzschild'
status: imported
region: pairing
subject: einstein
tags: [classical-theorem, schwarzschild, curvature-and-field-equations, null-directions]
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
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'R. Penrose, W. Rindler, Spinors and Space-Time, Vol. 2: Spinor and Twistor Methods in Space-Time
    Geometry, Cambridge University Press (1986).'
  key: PenroseRindler2
  locator: Ch.~8
- citation: E. Newman, R. Penrose, An approach to gravitational radiation by a method of spin coefficients,
    J. Math. Phys. 3 (1962) 566--578.
  key: NewmanPenrose1962
locators:
  paper: T05-pairing
  number: Fact 5.6
  label: fact:weyl
  line: 356
extraction:
  typing:
    by: ai-typing-pass
    note: Imported classical result; levels only.
  env: fact
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Weyl tensor is the Weyl map W of the field strength of a gravitational field on flat spacetime, its five complex components are taken on the bivectors of a null tetrad of physical vectors, Schwarzschild is the Schwarzschild field, and Ricci-flat reads R(a) = 0 (vacuum), where the curvature operator equals its Weyl map. Components, criteria and values unchanged.'
---

## formal
For a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) and a null tetrad $(\ell, n, m, \mb)$ of physical vectors, the Weyl map $\mathcal{W}$ of the field strength, read as the Weyl tensor $C$ of the derived metric on the tetrad's bivectors $\ell \wedge m$, $\ell \wedge n$ and $n \wedge \mb$, has five complex components, $\Psi_{0} = C(\ell, m, \ell, m)$, $\Psi_{1} = C(\ell, n, \ell, m)$, $\Psi_{2} = C(\ell, m, \mb, n)$, $\Psi_{3} = C(\ell, n, \mb, n)$, $\Psi_{4} = C(n, \mb, n, \mb)$, up to normalisation and sign convention; $\ell$ is a principal null direction if and only if $\Psi_{0} = 0$ and a repeated one if and only if $\Psi_{0} = \Psi_{1} = 0$. The Schwarzschild field is of Petrov type D with the outgoing and ingoing radial null directions as its repeated principal directions, $\Psi_{2} = -M/r^{3}$ in the unit-normalised tetrad and all other $\Psi$ zero. For a vacuum field, $\mathcal{R}(a) = 0$ (Ricci-flat), the curvature operator is its Weyl map, $\mathcal{R} = \mathcal{W}$. \emph{Provenance:} \cite[Ch.~8]{PenroseRindler2}; \cite{NewmanPenrose1962}.

## technical
For a gravitational field on flat spacetime and a null tetrad $(\ell, n, m, \mb)$ of physical vectors, the Weyl map of the field strength (the Weyl tensor of the derived metric) has five complex components $\Psi_0, \dots, \Psi_4$, for instance $\Psi_0 = C(\ell, m, \ell, m)$ and $\Psi_2 = C(\ell, m, \mb, n)$, up to normalisation and sign convention. The direction $\ell$ is principal if and only if $\Psi_0 = 0$, and repeated principal if and only if $\Psi_0 = \Psi_1 = 0$.

The Schwarzschild field is of Petrov type D, its repeated principal directions being the outgoing and ingoing radial null directions, with $\Psi_2 = -M/r^3$ in the unit-normalised tetrad and all other $\Psi$ zero. For a vacuum field, $\mathcal{R}(a) = 0$, the curvature operator is its Weyl map. Imported from Penrose and Rindler and from Newman and Penrose.

## lay
The part of the gravitational field strength that describes tidal forces and gravitational waves can be summarised by five complex numbers relative to a frame of light-like directions. Black holes like Schwarzschild are especially simple: in the natural frame only one of the five is nonzero, and the radial light rays are the field strength's special directions. This standard result is imported.

## one-liner
The Weyl map of the field strength has five complex null-tetrad components $\Psi_0, \dots, \Psi_4$, and the Schwarzschild field is of Petrov type D with only $\Psi_2 = -M/r^3$ nonzero, its repeated principal directions radial.
