---
id: synthesis.imported-raychaudhuri-null-congruence
kind: claim
version: 2
title: 'Imported: the Raychaudhuri and Sachs equations for null congruences'
status: imported
region: synthesis
subject: einstein
tags: [curvature-and-field-equations, horizons, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'A. Raychaudhuri, Relativistic cosmology. I, Phys. Rev. 98 (1955), 1123--1126.'
  key: Raychaudhuri1955
  doi: 10.1103/PhysRev.98.1123
- citation: 'R. K. Sachs, Gravitational waves in general relativity. VI. The outgoing radiation condition, Proc. R. Soc. Lond. A 264 (1961), 309--338.'
  key: Sachs1961
  doi: 10.1098/rspa.1961.0202
- citation: R. M. Wald, General Relativity, University of Chicago Press (1984).
  key: Wald1984
extraction:
  note: >-
    Imported so that the conditional derivation of Einstein's equations from the local-horizon
    premise can pin the null focusing and shear equations instead of citing them from memory; the
    shear equation is the one step of that derivation not covered by the imported Clausius Fact.
    Bibliographic data for Raychaudhuri 1955 and Sachs 1961 (optical scalars and the null
    Raychaudhuri equation) checked against the review of S. Kar and S. SenGupta, gr-qc/0611123, on
    2026-10-22; the null form, with coefficient 1/2 on the squared expansion in four dimensions and
    the sign of the Ricci term in the round-sphere-positive convention, checked against the same
    review (its equation (17)); Wald 1984 Section 9.2 is cited without an equation number. The
    page range of Sachs 1961 and both DOIs are from memory.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Created by the maintainer pass, by Leon''s acceptance of the conditional Einstein derivation (the fix round asked for this import).'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity (DICTIONARY section 9): the congruence is a physical null vector field k of a gravitational field on flat spacetime with (k.D)k = 0, d/dlambda is k.D, expansion, shear and twist are the parts of A -> A.D k on the screen space, the Ricci term is -Ric^o(k,k) = k.R(k) with the store-sign curvature operator, and the shear source is the Weyl map read as the round-sphere-positive Weyl tensor C(k, a, k, b) = (k ^ b).W(k ^ a) in the store''s sign (signature (+,-,-,-)). The tensor forms are kept as readings; content unchanged.'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime with covariant derivative $D$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric is $C^{2}$, and let $k$ be a physical null vector field ($Q(k) = 0$) tangent to an affinely parametrised congruence of null geodesics, $(k \cdot D)\,k = 0$, with parameter $\lambda$, so that $d/d\lambda = k \cdot D$ (components $k^{a}$). Let $\theta$, $\sigma_{ab}$ and $\omega_{ab}$ be its expansion, shear and twist: the trace, symmetric trace-free part and antisymmetric part of the map $A \mapsto A \cdot D k$ on a two-dimensional screen space of physical vectors orthogonal to $k$. Write $\Ric^{\circ}$ for the Ricci tensor of the convention in which the round sphere has positive Ricci curvature, so that $\Ric^{\circ}(k,k) = -k \cdot \mathcal{R}(k)$ with the store's curvature operator, and $C$ for the Weyl tensor of that convention, read from the Weyl map $\mathcal{W}$ of the field strength. Then
\[
\frac{d\theta}{d\lambda} = -\tfrac12\,\theta^{2} - \sigma_{ab}\sigma^{ab} + \omega_{ab}\omega^{ab} - \Ric^{\circ}_{ab}k^{a}k^{b},
\qquad
\frac{d\sigma_{ab}}{d\lambda} = -\theta\,\sigma_{ab} - \widehat{C_{cadb}k^{c}k^{d}},
\]
the hat denoting the trace-free projection onto the screen space; the twist vanishes for the generators of a null hypersurface. In the store's sign the focusing equation reads $(k \cdot D)\,\theta = -\tfrac12\theta^{2} - \sigma_{ab}\sigma^{ab} + \omega_{ab}\omega^{ab} + k \cdot \mathcal{R}(k)$, and in signature $(+,-,-,-)$ the shear source $C_{cadb}k^{c}k^{d}$ is the form $(a, b) \mapsto (k \wedge b) \cdot \mathcal{W}(k \wedge a)$ on the screen space. \emph{Provenance:} \cite{Raychaudhuri1955} (the focusing equation, timelike case), \cite{Sachs1961} (the optical scalars and the null equations), \cite{Wald1984} (Section 9.2).

## technical
These are the standard propagation equations for a bundle of light rays; in Gauge Theory Gravity they are written for a field of physical null vectors on flat spacetime, with the covariant derivative along the rays. The expansion measures how fast the cross-sectional area of the bundle grows, the shear how it is distorted, the twist how it rotates. Along the rays the expansion decreases by half its square, by the squared shear and by the Ricci curvature along the ray (the term $-k \cdot \mathcal{R}(k)$ of the field strength in the store's sign), and increases with the twist, which is zero for the generators of a null hypersurface such as a horizon. The shear is sourced by the Weyl part of the field strength along the ray and damped by the expansion. In a horizon patch whose expansion and shear vanish at a point, the area change to leading order is set by the Ricci term alone, which is how Jacobson's argument turns heat flux into curvature.

## lay
Light rays travelling side by side can converge or spread out. Raychaudhuri and Sachs found the equations that say how a bundle of rays changes as it travels: matter and the gravitational field along the rays focus them together, and a separate part of the field strength squeezes the bundle out of shape. These equations are standard textbook geometry; the series uses them in the step where the energy flowing through a small horizon is converted into the strength of the gravitational field.

## one-liner
For a null geodesic congruence of physical vectors, $(k \cdot D)\theta = -\theta^{2}/2 - \sigma^{2} + \omega^{2} - \Ric^{\circ}(k,k)$, with $-\Ric^{\circ}(k,k) = k \cdot \mathcal{R}(k)$ in the store's sign, and $d\sigma/d\lambda = -\theta\sigma - C(\cdot,k,\cdot,k)$ on the screen space (Raychaudhuri 1955, Sachs 1961).
