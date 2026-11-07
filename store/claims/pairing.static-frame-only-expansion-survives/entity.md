---
id: pairing.static-frame-only-expansion-survives
kind: claim
version: 6
title: 'The static frame: only the expansion survives'
status: proved
region: pairing
subject: thermality
tags: [pairing-and-bogoliubov, schwarzschild, null-directions]
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
outside_ga:
  kind: other
  why: 'the pairing classes are coordinates on the complexified tangent space of the complex null vector m = e_2 + i e_3, so the value -i sqrt(f)/r carries an i that must commute with the spacetime vectors, which no pseudoscalar does'
about:
- obj.pairing.pairing-class-transport
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - pairing.imported-schwarzschild-connection-curvature@5
  - pairing.imported-spin-coefficients-null-tetrad@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_omega_reproduces_covariant_derivatives
- kind: check
  ref: check.py::check_pairing_classes_and_optical_scalars
- kind: check
  ref: check.py::check_transport_along_l_and_the_stabiliser
- kind: check
  ref: check.py::check_horizon_limit_and_sample_value
locators:
  paper: T05-pairing
  number: Prop 5.1
  label: prop:schwarzschild
  line: 311
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: -i sqrt(f)/r and e_2 + i e_3 belong to the complexified tangent space. Declared other.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: static Schwarzschild gauge fields: Omega reproduces all (e_c.D)e_b; classes, tetrad classes and expansion; (l.D)l; horizon limit and the sample value -48/125. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6.'
  env: proposition
  context_refs:
  - pairing.imported-schwarzschild-connection-curvature
  typing:
    by: ai-typing-pass
    added:
    - pairing.imported-schwarzschild-connection-curvature
    - obj.pairing.pairing-class-transport
    note: Added the Schwarzschild connection Fact, which the statement takes as its hypothesis; the paper's
      reading of the classes as Newman-Penrose spin coefficients is a dictionary, not a second derivation,
      so no standard route was added.
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$-i\sqrt f/r$ and $e_2 + ie_3$: complex null vector of the complexified tangent space (complexified
      space, $i$ next to spacetime vectors)'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - pairing.imported-schwarzschild-connection-curvature
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: static frame = orthonormal physical frame of the static gauge of the Schwarzschild field on flat spacetime; Omega(e_c) named as Omega(hb(e_c)); nabla -> D. Formulas and values unchanged; proof given a pointer.'
---

## formal
For the Schwarzschild gravitational field on flat spacetime in the static gauge (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with the connection of Fact \claimref{pairing.imported-schwarzschild-connection-curvature} read along the static orthonormal frame of physical vectors $\{e_a\}$, and $\Omega(e_c)$ written for the rotation-gauge field along the physical vector $e_c$ (the bivector $\Omega(\hb(e_c))$ of item (b) of the definition), the bivectors $\Omega(e_{c})$ reproduce the covariant derivatives $(e_{c} \cdot D)\, e_{b} = \omega^{a}{}_{b}(e_{c})e_{a}$ for all $b, c$, and the pairing classes are
\[
\pv(\Omega(e_{0})) = \pv(\Omega(e_{1})) = 0, \qquad \pv(\Omega(e_{2})) = -\frac{\sqrt f}{r}, \qquad \pv(\Omega(e_{3})) = -\,i\,\frac{\sqrt f}{r},
\]
so that on the null tetrad $\pv(\Omega(\ell)) = \pv(\Omega(n)) = \pv(\Omega(m)) = 0$ and $\pv(\Omega(\mb)) = -2\sqrt f/r$: the congruence is geodesic, $\tau = 0$, shear-free, and its only optical scalar is the transverse expansion $2\sqrt f/r$. Along its own direction $(\ell \cdot D)\ell = (f'/2\sqrt f)\,\ell$, a rescaling. In particular $\Omega(e_{0})$ is a multiple of $e_{01}$ and $\Omega(e_{1}) = 0$: the transports along the $t$-line and the $r$-line lie in the stabiliser. Every class vanishes at $F = 0$, and at $r = 25/16$ ($F = \tfrac35$) the transverse class is $-\tfrac{48}{125}$.

## technical
For the Schwarzschild field on flat spacetime in the static gauge, with the connection of the imported Schwarzschild data read along the static orthonormal frame of physical vectors and $F = \sqrt f$, the rotation-gauge bivectors $\Omega(e_c)$ reproduce every covariant frame derivative, and the pairing classes of the outgoing vacuum are $\pv(\Omega(e_0)) = \pv(\Omega(e_1)) = 0$, $\pv(\Omega(e_2)) = -\sqrt f/r$ and $\pv(\Omega(e_3)) = -i\sqrt f/r$. On the null tetrad only $\pv(\Omega(\mb)) = -2\sqrt f/r$ survives, so the congruence is geodesic, has $\tau = 0$, is shear-free, and its only optical scalar is the transverse expansion $2\sqrt f/r$; along its own direction $(\ell \cdot D)\ell = (f'/2\sqrt f)\,\ell$, a rescaling.

In particular $\Omega(e_0)$ is a multiple of $e_{01}$ and $\Omega(e_1) = 0$, so the transports along the $t$-line and the $r$-line lie in the stabiliser. Every class vanishes at $F = 0$, and at $r = 25/16$ ($F = \tfrac35$) the transverse class is $-\tfrac{48}{125}$.

## lay
In the usual axes of an observer hovering at a fixed distance from a non-rotating black hole, carrying the fermion vacuum forward in time or along the radial direction leaves it unchanged. The only disturbance comes from moving sideways, and it is exactly the spreading of the outgoing light rays. That spreading shrinks to zero at the horizon.

## one-liner
For the Schwarzschild field in the static gauge the only nonzero pairing classes of the outgoing vacuum are the transverse ones, $-\sqrt f/r$ and $-i\sqrt f/r$, so the congruence's only optical scalar is its expansion $2\sqrt f/r$ and the $t$-line and $r$-line transports lie in the stabiliser.
