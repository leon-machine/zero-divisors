---
id: synthesis.imported-maxwell-stress-spacetime-algebra
kind: claim
version: 1
title: 'Imported: the stress of an electromagnetic field $F$ is $T(a) = -\tfrac12 FaF$ (Hestenes; Doran and Lasenby)'
status: imported
region: synthesis
subject: interior
tags: [gauge-fields, curvature-and-field-equations, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-31
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'D. Hestenes, Space-Time Algebra, Gordon and Breach (1966).'
  key: Hestenes1966
- citation: 'C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003), Section 7.4.'
  key: DoranLasenby2003
extraction:
  note: >-
    Imported so that the matter-wall classification of Kasner walls can pin the stress of its aligned
    Maxwell field instead of citing it from memory. Units with the vacuum permittivity one. The
    formula is cited from memory (Hestenes 1966; Doran and Lasenby 2003, Section 7.4, section number
    from memory) and not checked against the sources; its content was checked by a numerical
    computation in a Dirac-matrix representation of the spacetime algebra, signature (+,-,-,-): for
    random E and B, T(e_0) . e_0 = (E^2 + B^2)/2, the momentum density is E x B, the frame
    components T(e_a) . e_b are symmetric and trace-free, and for E and B along one axis they are
    diag(rho, -rho, rho, rho) with rho = (E^2 + B^2)/2.
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created by the maintainer pass of 2026-10-31 (literature cited from memory by an accepted result; Leon''s list of imports).'
---

## formal
Let $F$ be the electromagnetic field, a bivector-valued field of the spacetime algebra $\Cl(1,3)$, signature $(+,-,-,-)$, in units with the vacuum permittivity one, and in a frame with $e_{0}^{2} = 1$ write $F = \mathbf{E} + I\mathbf{B}$ with $I = e_{0}e_{1}e_{2}e_{3}$ and $\mathbf{E}$, $\mathbf{B}$ relative vectors (bivectors $e_{i}e_{0}$). Its stress, the energy-momentum flux through the hypersurface with normal $a$, is the vector-valued linear map
\[
T(a) \;=\; -\tfrac12\,F a F,
\]
symmetric ($T(a) \cdot b = a \cdot T(b)$) and trace-free, with $T(e_{0}) \cdot e_{0} = \tfrac12(\mathbf{E}^{2} + \mathbf{B}^{2})$ the energy density and the relative vector of $T(e_{0}) \wedge e_{0}$ the Poynting vector $\mathbf{E} \times \mathbf{B}$. For a field aligned with one axis, $F = (E + IB)\,e_{1}e_{0}$ with scalars $E$, $B$, the frame components are $T(e_{a}) \cdot e_{b} = \mathrm{diag}(\rho, -\rho, \rho, \rho)$ with $\rho = \tfrac12(E^{2} + B^{2})$. On a gravitational field the same formula holds with $a$ and $F$ physical. \emph{Provenance:} \cite{Hestenes1966}; \cite[Section 7.4]{DoranLasenby2003}.

## technical
In the spacetime algebra the electromagnetic field is one bivector $F = \mathbf{E} + I\mathbf{B}$, and its energy-momentum tensor is the single product $T(a) = -\tfrac12 FaF$: feeding in the time direction gives the energy density $\tfrac12(E^{2} + B^{2})$ and the Poynting momentum $\mathbf{E} \times \mathbf{B}$; the map is symmetric and trace-free. For a field along one axis it is the familiar tension along the field lines and pressure across them, $\mathrm{diag}(\rho, -\rho, \rho, \rho)$.

## lay
An electric or magnetic field carries energy and momentum and pushes on its surroundings: it pulls along its field lines and pushes sideways. Geometric algebra writes all of this as one short product of the field with itself, which is the standard formula the series uses whenever an electromagnetic field enters gravity's equations.

## one-liner
The electromagnetic stress in the spacetime algebra is $T(a) = -\tfrac12 FaF$: symmetric, trace-free, with energy density $\tfrac12(E^{2} + B^{2})$ and, for an axis-aligned field, components $\mathrm{diag}(\rho, -\rho, \rho, \rho)$ (Hestenes; Doran and Lasenby).
