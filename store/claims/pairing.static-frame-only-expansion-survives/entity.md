---
id: pairing.static-frame-only-expansion-survives
kind: claim
version: 7
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
- name: Claude Opus 5.5
  role: 'unit resolution pass, the pairing classes written with the central unit I_5 of Cl(2,3)'
  version: 7
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 7
  source: maintainer pass 2026-11-07 (consistency)
review: typed
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
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: The proof works with the block connection one-forms omega_{ab} of the static frame and frame components; the forms are the computation.'
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U3: the pairing classes are coordinates on the tangent space complexified with m = e_2 + i e_3, whose unit must commute with every spacetime vector; it is the central unit I_5 = I_4 e of Cl(2,3) (std-algebra.complexification-is-the-odd-extension, cited as a mention), so m = e_2 + I_5 e_3 and the class -I_5 sqrt(f)/r is a number of span{1, I_5}. Declaration removed.'
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
outside_ga:
  kind: other
  why: 'The proof works with the block connection one-forms omega_{ab} of the static frame and frame components; the forms are the computation.'
---

## formal
For the Schwarzschild gravitational field on flat spacetime in the static gauge (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with the connection of Fact \claimref{pairing.imported-schwarzschild-connection-curvature} read along the static orthonormal frame of physical vectors $\{e_a\}$, and $\Omega(e_c)$ written for the rotation-gauge field along the physical vector $e_c$ (the bivector $\Omega(\hb(e_c))$ of item (b) of the definition), the bivectors $\Omega(e_{c})$ reproduce the covariant derivatives $(e_{c} \cdot D)\, e_{b} = \omega^{a}{}_{b}(e_{c})e_{a}$ for all $b, c$, and the pairing classes are
\[
\pv(\Omega(e_{0})) = \pv(\Omega(e_{1})) = 0, \qquad \pv(\Omega(e_{2})) = -\frac{\sqrt f}{r}, \qquad \pv(\Omega(e_{3})) = -\,I_{5}\,\frac{\sqrt f}{r},
\]
numbers of $\mathrm{span}\{1, I_{5}\}$, with $I_{5} = I_{4}e$ the central unit of the odd extension $\Cl(2,3)$, in which the transverse complex null vector is $m = e_{2} + I_{5}e_{3}$ (\claimref{std-algebra.complexification-is-the-odd-extension}), so that on the null tetrad $\pv(\Omega(\ell)) = \pv(\Omega(n)) = \pv(\Omega(m)) = 0$ and $\pv(\Omega(\mb)) = -2\sqrt f/r$: the congruence is geodesic, $\tau = 0$, shear-free, and its only optical scalar is the transverse expansion $2\sqrt f/r$. Along its own direction $(\ell \cdot D)\ell = (f'/2\sqrt f)\,\ell$, a rescaling. In particular $\Omega(e_{0})$ is a multiple of $e_{01}$ and $\Omega(e_{1}) = 0$: the transports along the $t$-line and the $r$-line lie in the stabiliser. Every class vanishes at $F = 0$, and at $r = 25/16$ ($F = \tfrac35$) the transverse class is $-\tfrac{48}{125}$.

## technical
For the Schwarzschild field on flat spacetime in the static gauge, with the connection of the imported Schwarzschild data read along the static orthonormal frame of physical vectors and $F = \sqrt f$, the rotation-gauge bivectors $\Omega(e_c)$ reproduce every covariant frame derivative, and the pairing classes of the outgoing vacuum are $\pv(\Omega(e_0)) = \pv(\Omega(e_1)) = 0$, $\pv(\Omega(e_2)) = -\sqrt f/r$ and $\pv(\Omega(e_3)) = -I_{5}\sqrt f/r$, with $I_{5}$ the central unit of $\Cl(2,3)$ that complexifies the transverse null vector $m = e_{2} + I_{5}e_{3}$. On the null tetrad only $\pv(\Omega(\mb)) = -2\sqrt f/r$ survives, so the congruence is geodesic, has $\tau = 0$, is shear-free, and its only optical scalar is the transverse expansion $2\sqrt f/r$; along its own direction $(\ell \cdot D)\ell = (f'/2\sqrt f)\,\ell$, a rescaling.

In particular $\Omega(e_0)$ is a multiple of $e_{01}$ and $\Omega(e_1) = 0$, so the transports along the $t$-line and the $r$-line lie in the stabiliser. Every class vanishes at $F = 0$, and at $r = 25/16$ ($F = \tfrac35$) the transverse class is $-\tfrac{48}{125}$.

## lay
In the usual axes of an observer hovering at a fixed distance from a non-rotating black hole, carrying the fermion vacuum forward in time or along the radial direction leaves it unchanged. The only disturbance comes from moving sideways, and it is exactly the spreading of the outgoing light rays. That spreading shrinks to zero at the horizon.

## one-liner
For the Schwarzschild field in the static gauge the only nonzero pairing classes of the outgoing vacuum are the transverse ones, $-\sqrt f/r$ and $-I_{5}\sqrt f/r$ ($I_{5}$ the central unit of $\Cl(2,3)$), so the congruence's only optical scalar is its expansion $2\sqrt f/r$ and the $t$-line and $r$-line transports lie in the stabiliser.
