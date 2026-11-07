---
id: synthesis.imported-gauss-bonnet-with-corners-poincare-hopf-and-edge-term
kind: claim
version: 2
title: 'Imported: Gauss-Bonnet with corners, Poincare-Hopf and the edge term'
status: imported
region: synthesis
subject: einstein
tags: [horizons, curvature-and-field-equations, classical-theorem]
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
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'M. P. do Carmo, Differential Geometry of Curves and Surfaces, Prentice-Hall, Englewood Cliffs (1976).'
  key: doCarmo1976
  locator: 'Sec. 4-5'
- citation: 'H. Hopf, Vektorfelder in n-dimensionalen Mannigfaltigkeiten, Math. Ann. 96 (1927), 225--249.'
  key: Hopf1927
  doi: 10.1007/BF01209164
- citation: 'J. W. Milnor and J. D. Stasheff, Characteristic Classes, Annals of Mathematics Studies 76, Princeton University Press (1974).'
  key: MilnorStasheff1974
- citation: 'J. W. York, Role of conformal three-geometry in the dynamics of gravitation, Phys. Rev. Lett. 28 (1972), 1082--1085.'
  key: York1972
  doi: 10.1103/PhysRevLett.28.1082
- citation: 'G. W. Gibbons and S. W. Hawking, Action integrals and partition functions in quantum gravity, Phys. Rev. D 15 (1977), 2752--2756.'
  key: GibbonsHawking1977
  doi: 10.1103/PhysRevD.15.2752
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (imported) and left in its language: Gauss-Bonnet with corners, Poincare-Hopf and clutching are quoted as their sources state them, for a compact surface with a Riemannian metric and an orthonormal coframe with its rotation one-form; the Euler characteristic and the clutching of frames are global data of the closed surface, and the local identity d omega = K e^2 ^ e^3 is the two-dimensional rotation-gauge field written as a form.'
  note: >-
    Imported for the result that the Euler part of a horizon patch's entropy is an edge term, which
    uses Gauss-Bonnet with edge and corners, Poincare-Hopf and the clutching number of the sphere, and
    names its edge term the two-dimensional Gibbons-Hawking term. Checked on 2026-10-31: Hopf 1927 (title,
    journal, volume, pages, DOI) against the publisher's record; York 1972 and Gibbons-Hawking 1977
    (titles, journals, volumes, first pages) against the encyclopedia article on the Gibbons-Hawking-York
    boundary term, which states that the term, the integral of the trace of the boundary's extrinsic
    curvature, is what makes the variational principle well defined with the induced boundary metric held
    fixed. Cited from memory, not checked against the source: the last pages and DOIs of York and of
    Gibbons-Hawking, the locator in do Carmo (the same book and section as in
    synthesis.imported-chern-gauss-bonnet), Milnor and Stasheff as the reference for the clutching
    description, and the two-dimensional specialisation of (c). Clause (a) generalises (a) of
    synthesis.imported-chern-gauss-bonnet from closed surfaces to surfaces with edge.
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created at Leon''s decision of 2026-10-31 approving the imports of Gauss-Bonnet with boundary and corners, Poincare-Hopf with clutching, and the two-dimensional Gibbons-Hawking term, merged into one Fact on surfaces; partly verified (see note).'
  flags:
  - 'beyond one flat chart: Euler characteristic of a closed surface and the clutching of two caps'
outside_ga:
  kind: imported
  why: 'Gauss-Bonnet with corners, Poincare-Hopf and clutching are quoted as their sources state them, for a compact surface with a Riemannian metric and an orthonormal coframe with its rotation one-form; the Euler characteristic and the clutching of frames are global data of the closed surface, and the local identity d omega = K e^2 ^ e^3 is the two-dimensional rotation-gauge field written as a form.'
---

## formal
Let $P$ be a compact oriented surface with piecewise smooth edge $\partial P$ and a Riemannian metric, with Gauss curvature $K$, area element $dA$, and Euler characteristic $\chi(P)$; in the series $P$ is a patch of a spacelike two-surface in the invertible region of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), such as a cut of a horizon, with the Riemannian metric $-h$, $h$ the metric that the derived metric induces.
\begin{enumerate}
\item[(a)] (Gauss-Bonnet with edge and corners.) $\int_{P}K\,dA + \oint_{\partial P}k_{g}\,ds + \sum_{j}\varepsilon_{j} = 2\pi\chi(P)$, with $k_{g}$ the geodesic curvature of the edge taken with respect to the inward normal and $\varepsilon_{j}$ the exterior turning angles at its corners. Locally, for an orthonormal coframe $(e^{2}, e^{3})$ with rotation one-form $\omega$, $d\omega = K\,e^{2} \wedge e^{3}$, so $\int_{P}K\,dA = \oint_{\partial P}\omega$ for a frame smooth on $P$.
\item[(b)] (Poincare-Hopf and clutching.) A tangent vector field with isolated zeros on a closed surface $\Sigma$ has indices summing to $\chi(\Sigma)$; in particular a sphere ($\chi = 2$) carries no nowhere-vanishing tangent field and no smooth tangent frame. Cutting the sphere along a circle into two caps with tangent frames smooth on each, the rotation relating the two frames along the circle winds $\chi(S^{2}) = 2$ times (the clutching number of its tangent bundle).
\item[(c)] (The two-dimensional Gibbons-Hawking term.) For a functional of the metric with Einstein-Hilbert density, a region with edge needs the edge term $2\oint k\,ds$, $k$ the trace of the extrinsic curvature of the edge (the Gibbons-Hawking, or York, term), for its variational principle to be well posed with the edge metric held fixed. On a surface the extrinsic curvature of the edge is its geodesic curvature, so the two-dimensional term is $2\oint_{\partial P}k_{g}\,ds$, and by (a) the two-dimensional Einstein-Hilbert functional with it, $\int_{P}{}^{(2)}\!R\,dA + 2\oint_{\partial P}k_{g}\,ds$ with ${}^{(2)}\!R = 2K$, equals $4\pi\chi(P) - 2\sum_{j}\varepsilon_{j}$, a topological constant.
\end{enumerate}
\emph{Beyond one flat chart.} The Euler characteristic of a closed surface in (b) and the clutching of two caps are global: they are read on the surface assembled from charts of flat spacetime, each with its own gravitational field, glued by gauge transformations; (a) on a patch with a smooth frame and (c) are local.

\emph{Provenance:} \cite[Sec.~4-5]{doCarmo1976} for (a); \cite{Hopf1927} for the index theorem and \cite{MilnorStasheff1974} for the clutching description in (b); \cite{York1972, GibbonsHawking1977} for the edge term in (c).

## technical
Three classical facts about surfaces. Gauss-Bonnet for a patch with an edge: the total curvature inside, plus the total turning of the edge measured by its geodesic curvature, plus the turning angles at its corners, is $2\pi$ times the Euler characteristic of the patch; locally the curvature is the exterior derivative of the frame's rotation form, so the curvature inside equals the frame's rotation around the edge. Poincare and Hopf: on a closed surface the zeros of any tangent field, counted with their indices, add up to the Euler characteristic, so the sphere has no smooth tangent frame, and two frames smooth on two caps differ along the dividing circle by a rotation winding twice. Gibbons, Hawking and York: an action with the Einstein-Hilbert density needs a boundary term, twice the integral of the trace of the boundary's extrinsic curvature, to have a good variational principle; on a surface this term is twice the edge's geodesic curvature, and with it the two-dimensional action is topological. Taken from the literature.

## lay
However a patch of surface is curved, its total curvature plus the bending of its edge and the turns at its corners always add up to a fixed amount set by how many holes it has. A related fact says that on a sphere any arrangement of arrows tangent to the surface must have somewhere a point where it fails, the hairy-ball theorem. And the standard extra edge term of Einstein's action principle, on a surface, is exactly the edge's bending that makes the total fixed. These are classical results taken from the literature.

## one-liner
$\int_{P}K\,dA + \oint k_{g}\,ds + \sum\varepsilon_{j} = 2\pi\chi(P)$ (Gauss-Bonnet with corners); tangent-field indices on a closed surface sum to $\chi$, and two cap frames on the sphere differ by winding $2$ (Poincare-Hopf, clutching); on a surface the Gibbons-Hawking edge term is $2\oint k_{g}\,ds$, which makes the Einstein-Hilbert functional topological.
