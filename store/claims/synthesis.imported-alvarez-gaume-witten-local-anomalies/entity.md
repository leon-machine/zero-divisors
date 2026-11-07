---
id: synthesis.imported-alvarez-gaume-witten-local-anomalies
kind: claim
version: 2
title: 'Imported: local anomalies from the A-hat genus (Alvarez-Gaume and Witten 1984)'
status: imported
region: synthesis
subject: dark-matter
tags: [hypercharge-and-anomalies, chirality, classical-theorem]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle
  version: 2
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'L. Alvarez-Gaum''e and E. Witten, Gravitational anomalies, Nucl. Phys. B 234 (1984), 269--330.'
  key: AGW1984
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 kept (already raised in this pass). Restated by U4: the anomaly polynomial tr e^{iF/2 pi} and its pure-gauge part are written with I_4, the default scalar unit of an abstract complex matrix algebra (U1), the representation''s numbers read in span{1, I_4}; the source''s form (the formal level as first stored) moves to extraction.source_formal, and the source writes i for I_4. Status stays imported. Declaration removed.'
  source_formal: |-
    Let $\psi$ be a chiral (Weyl) spin-$\tfrac12$ field in even dimension $n$, coupled to a gravitational field (the rotation-gauge field, with field strength $\mathcal{R}$, the curvature) and to a gauge field with field strength $F$ acting in a representation $\rho$. Its local anomalies, the failure of the effective action to be invariant under infinitesimal rotation-gauge (local Lorentz and coordinate) and gauge transformations, are given by descent from the anomaly polynomial
    \[
    I_{n+2} \;=\; \Bigl[\hat{A}(\mathcal{R})\,\mathrm{tr}_{\rho}\,e^{iF/2\pi}\Bigr]_{n+2},
    \qquad
    \hat{A} \;=\; \prod_{i}\frac{x_{i}/2}{\sinh(x_{i}/2)} \;=\; 1 - \frac{p_{1}}{24} + \frac{7p_{1}^{2} - 4p_{2}}{5760} - \dots,
    \]
    the degree-$(n+2)$ part of the $\hat{A}$ genus (in the Chern roots $x_{i}$ of the curvature, Pontryagin classes $p_{j}$) times the Chern character, which is the index density of the Dirac operator in dimension $n+2$; the opposite chirality contributes with the opposite sign. The pure-gauge part is $\mathrm{tr}_{\rho}(iF/2\pi)^{(n+2)/2}/((n+2)/2)!$ and the purely gravitational part is $\dim\rho$ times the degree-$(n+2)$ part of $\hat{A}$, which is nonzero only when $n + 2 \equiv 0 \pmod 4$. So purely gravitational anomalies occur only in dimensions $n = 4k + 2$, where Weyl fields of spin $\tfrac12$ and $\tfrac32$ and self-dual antisymmetric tensor fields carry them, and such fields cannot be coupled to gravity in those dimensions unless the contributions of the different fields cancel. A chiral content is free of local anomalies when the sum of its anomaly polynomials vanishes. \emph{Provenance:} \cite{AGW1984}; the polynomial's normalisation as remembered.
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (imported): the anomaly polynomial tr e^{iF/2 pi} is quoted as Alvarez-Gaume and Witten state it, with F a Lie-algebra-valued curvature in their conventions.'
  note: >-
    Imported so that synthesis.residues-zero-four-real-chirality-anomaly can cite the local-anomaly
    theorem it names as part of its hypothesis (A). Checked on 2026-10-26 against the published paper's
    first pages (scan hosted by IFT Madrid): the journal reference (Nucl. Phys. B 234, received
    7 October 1983, pages 269-330), the statement that purely gravitational anomalies occur for Weyl
    fermions of spin 1/2 and 3/2 in 4k+2 dimensions, the analogous anomaly of self-dual antisymmetric
    tensor fields, the conclusion that such fields cannot be coupled to gravity in 4k+2 dimensions without
    cancellation between spins, and the link to the Dirac index density in 4k+4 dimensions. The explicit
    anomaly polynomial, its normalisation and the A-hat coefficients are standard and cited from memory
    (the coefficients are recomputed exactly in the check of the residue result); the cancellation by a
    two-form field when the polynomial factorises is the Green-Schwarz mechanism (1984), cited from
    memory and not imported.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Created by the maintainer pass (fix round of 26 October: the local-anomaly theorem, cited from memory by the residue-zero-four anomaly result, to be imported as a Fact).'
---

## formal
Let $\psi$ be a chiral (Weyl) spin-$\tfrac12$ field in even dimension $n$, coupled to a gravitational field (the rotation-gauge field, with field strength $\mathcal{R}$, the curvature) and to a gauge field with field strength $F$ acting in a representation $\rho$, whose matrices, like all numbers here, have entries in $\mathrm{span}\{1, I_4\}$, the scalar field of an abstract complex matrix algebra. Its local anomalies, the failure of the effective action to be invariant under infinitesimal rotation-gauge (local Lorentz and coordinate) and gauge transformations, are given by descent from the anomaly polynomial
\[
I_{n+2} \;=\; \Bigl[\hat{A}(\mathcal{R})\,\mathrm{tr}_{\rho}\,e^{I_4F/2\pi}\Bigr]_{n+2},
\qquad
\hat{A} \;=\; \prod_{i}\frac{x_{i}/2}{\sinh(x_{i}/2)} \;=\; 1 - \frac{p_{1}}{24} + \frac{7p_{1}^{2} - 4p_{2}}{5760} - \dots,
\]
the degree-$(n+2)$ part of the $\hat{A}$ genus (in the Chern roots $x_{i}$ of the curvature, Pontryagin classes $p_{j}$) times the Chern character, which is the index density of the Dirac operator in dimension $n+2$; the opposite chirality contributes with the opposite sign. The pure-gauge part is $\mathrm{tr}_{\rho}(I_4F/2\pi)^{(n+2)/2}/((n+2)/2)!$ and the purely gravitational part is $\dim\rho$ times the degree-$(n+2)$ part of $\hat{A}$, which is nonzero only when $n + 2 \equiv 0 \pmod 4$. So purely gravitational anomalies occur only in dimensions $n = 4k + 2$, where Weyl fields of spin $\tfrac12$ and $\tfrac32$ and self-dual antisymmetric tensor fields carry them, and such fields cannot be coupled to gravity in those dimensions unless the contributions of the different fields cancel. A chiral content is free of local anomalies when the sum of its anomaly polynomials vanishes. \emph{Provenance:} \cite{AGW1984}; the polynomial's normalisation as remembered.

## technical
The theorem says which field contents can be consistently coupled to gravity and to gauge fields at the quantum level. Each chiral fermion contributes a characteristic polynomial in the curvature and the gauge field strength, of total degree two more than the dimension, read from the index theorem for the Dirac operator in that higher dimension. The theory is consistent only if the contributions of all its fields add to zero. Because the curvature enters only through Pontryagin classes, of degree a multiple of four, a purely gravitational anomaly needs the dimension plus two to be a multiple of four: dimensions two, six, ten and so on. In Gauge Theory Gravity the gravitational part is the anomaly of the rotation-gauge field. The series uses it to ask whether the matter of a tower of dimension two or six can be of one chirality.

## lay
Some quantum theories that look consistent turn out to break their own symmetries once quantum effects are included; these breakdowns are called anomalies. Alvarez-Gaume and Witten worked out exactly when a particle with a handedness spoils the consistency of its coupling to gravity: it can happen only in two, six, ten and so on dimensions, and a theory is safe only if the contributions of its particles cancel.

## one-liner
Local gauge and rotation-gauge anomalies of a chiral spin-$\tfrac12$ field in dimension $n$ come from the degree-$(n+2)$ part of $\hat{A}(\mathcal{R})\,\mathrm{ch}(F)$, so purely gravitational anomalies occur only for $n = 4k + 2$ (Alvarez-Gaume and Witten 1984).
