---
id: synthesis.imported-bardeen-zumino-consistent-covariant-anomalies
kind: claim
version: 1
title: 'Imported: consistent and covariant anomalies differ by the divergence of a local polynomial in the potentials, and for gravitational anomalies they belong to different stress tensors (Bardeen and Zumino 1984)'
status: imported
region: synthesis
subject: dark-matter
tags: [hypercharge-and-anomalies, classical-theorem]
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
- citation: 'W. A. Bardeen and B. Zumino, Consistent and covariant anomalies in gauge and gravitational theories, Nucl. Phys. B 244 (1984), 421--453.'
  key: BardeenZumino1984
extraction:
  note: >-
    Imported so that synthesis.residues-zero-four-real-chirality-anomaly can cite the relation
    between the consistent and the covariant form of an anomaly, which it uses as part of its hypothesis
    (A) (the covariant form is the one that enters the covariant divergence of the stress). Checked on
    2026-10-26 against the Lawrence Berkeley Laboratory preprint of April 1984 (scan in the Fermilab
    library archive): that both forms are correct for the covariant divergences of different currents,
    that the consistent anomaly satisfies the Wess-Zumino condition and is not covariant, that adding a
    local polynomial in the potentials to the consistent current gives a covariant current whose
    divergence is the covariant anomaly, and that for gravitational anomalies the two forms belong to
    different energy-momentum tensors. The journal reference is cited from memory.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Created by the maintainer pass (fix round of 26 October: Bardeen-Zumino, cited from memory by the residue-zero-four anomaly result, to be imported as a Fact).'
---

## formal
For a chiral field coupled to a gauge field $A$ and to a gravitational field (the rotation-gauge field), the anomaly appears in two forms. The \emph{consistent} anomaly is the variation of the effective action under the infinitesimal symmetry; it satisfies the Wess-Zumino consistency condition and is in general not covariant. The \emph{covariant} anomaly is the covariant divergence of a current (or stress tensor) that transforms covariantly. The covariant current is the consistent current plus a local polynomial $X(A)$ in the potentials (the Bardeen-Zumino polynomial), so both forms are correct, for the covariant divergences of different currents; the covariant anomaly is read from the anomaly polynomial $I_{n+2}$ directly and vanishes exactly when the consistent one does. For gravitational anomalies the two forms correspond to two different energy-momentum tensors, the covariant one being the stress that enters a covariantly conserved source. \emph{Provenance:} \cite{BardeenZumino1984}.

## technical
An anomaly can be written in two ways that look different. The consistent form comes from how the quantum effective action changes under a symmetry and obeys an integrability condition but is not covariant; the covariant form is the divergence of a current or stress that transforms properly. Bardeen and Zumino showed that the two currents differ by a local polynomial in the potentials, so the two forms describe the same obstruction, and that for gravity they belong to different stress tensors. A field theory's matter can source covariant field equations only through a covariantly conserved stress, so the covariant form is the one that decides whether it can.

## lay
When a quantum symmetry breaks down, physicists can describe the breakdown in two ways. Bardeen and Zumino showed how the two descriptions are related, and which one matters when asking whether a kind of matter can act as a source of gravity.

## one-liner
Consistent and covariant anomalies differ by the divergence of a local polynomial in the potentials and vanish together; for gravity they belong to different stress tensors, the covariant one being the conserved source (Bardeen and Zumino 1984).
