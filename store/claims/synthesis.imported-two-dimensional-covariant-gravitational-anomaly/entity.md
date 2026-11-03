---
id: synthesis.imported-two-dimensional-covariant-gravitational-anomaly
kind: claim
version: 1
title: 'Imported: in two dimensions a chiral field has covariant gravitational anomaly proportional to the gradient of the scalar curvature, with coefficient 1/96 pi per unit of central charge (Iso, Umetsu and Wilczek 2006)'
status: imported
region: synthesis
subject: dark-matter
tags: [hypercharge-and-anomalies, chirality, hawking-temperature, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-26
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
- citation: 'S. Iso, H. Umetsu and F. Wilczek, Hawking radiation from charged black holes via gauge and gravitational anomalies, Phys. Rev. Lett. 96 (2006), 151302; arXiv:hep-th/0602146.'
  key: IsoUmetsuWilczek2006
  doi: 10.1103/PhysRevLett.96.151302
- citation: 'S. P. Robinson and F. Wilczek, A relationship between Hawking radiation and gravitational anomalies, Phys. Rev. Lett. 95 (2005), 011303; arXiv:gr-qc/0502074.'
  key: RobinsonWilczek2005
extraction:
  note: >-
    Imported so that synthesis.residues-zero-four-real-chirality-anomaly can cite the
    two-dimensional covariant anomaly form that it uses at (1,1), part of its hypothesis (A). Checked on
    2026-10-26 against the arXiv abstract and the ar5iv rendering of arXiv:hep-th/0602146: authors,
    title, DOI, that the paper extends gr-qc/0502074 (Robinson and Wilczek), and its equations (13) and
    (14), the consistent anomaly (1/(96 pi sqrt(-g))) eps^{beta delta} d_delta d_alpha Gamma^alpha_{nu beta}
    for right-handed fields and the covariant anomaly -(1/(96 pi sqrt(-g))) eps_{mu nu} d^mu R. The
    statement for c_L left- and c_R right-moving fields (coefficient proportional to c_R - c_L, sign set
    by the orientation convention of eps and by the curvature sign convention) is the standard reading,
    from memory. Robinson and Wilczek's use of the consistent form, and their journal reference, are
    cited from memory.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Created by the maintainer pass (fix round of 26 October: the covariant two-dimensional anomaly form of Iso, Umetsu and Wilczek, cited from memory by the residue-zero-four anomaly result, to be imported as a Fact).'
---

## formal
Let a chiral field live on a two-dimensional gravitational field with derived metric $g$, scalar curvature $R$ and Christoffel symbols $\Gamma$. For right-handed (one-chirality) fields the consistent gravitational anomaly is
\[
\nabla_{\mu}T^{\mu}{}_{\nu} \;=\; \frac{1}{96\pi\sqrt{-g}}\,\epsilon^{\beta\delta}\partial_{\delta}\partial_{\alpha}\Gamma^{\alpha}_{\nu\beta},
\]
and the covariant anomaly, the covariant divergence of the covariant stress tensor $\tilde{T}$, is
\[
\nabla_{\mu}\tilde{T}^{\mu}{}_{\nu} \;=\; -\frac{1}{96\pi\sqrt{-g}}\,\epsilon_{\mu\nu}\,\partial^{\mu}R
\]
(in the paper's conventions for $\epsilon$ and $R$). For a content with central charges $c_{L}$ and $c_{R}$ of left- and right-moving fields the coefficient is proportional to $c_{R} - c_{L}$, so the covariant stress is conserved wherever $c_{L} = c_{R}$ or $R$ is constant, and not conserved where $c_{L} \neq c_{R}$ and $R$ varies. In the store's curvature sign convention the sign of $R$, and so the overall sign, may flip; whether the divergence vanishes does not depend on it. The covariant form is the one used to derive the Hawking flux from the anomaly near a horizon; Robinson and Wilczek's original derivation used the consistent form. \emph{Provenance:} \cite{IsoUmetsuWilczek2006} (equations (13) and (14)); \cite{RobinsonWilczek2005}.

## technical
In two dimensions a field that moves only one way (one chirality) cannot have a conserved stress tensor on a gravitational field whose scalar curvature varies: the covariant divergence of its stress is proportional to the gradient of the curvature, with coefficient $1/96\pi$ in the paper's normalisation, and to the difference of the left- and right-moving central charges. Iso, Umetsu and Wilczek wrote this covariant form and used it to derive the Hawking flux from the anomaly in the near-horizon two-dimensional sections of a black hole, extending Robinson and Wilczek's derivation, which used the consistent form. The series uses it to ask whether one-chirality matter on the planes of the one metric can source the field equations.

## lay
In a world with one space and one time dimension, particles that move only in one direction cannot carry a conserved energy and momentum if gravity bends that world unevenly. This result gives the precise formula. It is also a known route to Hawking radiation from black holes.

## one-liner
In two dimensions a one-chirality field has $\nabla_{\mu}\tilde{T}^{\mu}{}_{\nu} = -\epsilon_{\mu\nu}\partial^{\mu}R/(96\pi\sqrt{-g})$, proportional to $c_{R} - c_{L}$, so its covariant stress is not conserved where the curvature varies (Iso, Umetsu and Wilczek 2006).
