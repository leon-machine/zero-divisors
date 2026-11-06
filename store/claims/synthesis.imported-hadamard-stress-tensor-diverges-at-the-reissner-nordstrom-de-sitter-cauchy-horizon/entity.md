---
id: synthesis.imported-hadamard-stress-tensor-diverges-at-the-reissner-nordstrom-de-sitter-cauchy-horizon
kind: claim
version: 1
title: 'Imported: the Cauchy-horizon stress divergence (Hollands, Wald and Zahn 2020)'
status: imported
region: synthesis
subject: quantum-fields
tags: [horizons, curvature-and-field-equations, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
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
- citation: 'S. Hollands, R. M. Wald and J. Zahn, Quantum instability of the Cauchy horizon in Reissner-Nordstrom-deSitter spacetime, Class. Quantum Grav. 37 (2020), 115009; arXiv:1912.06047.'
  key: HollandsWaldZahn2020
  doi: 10.1088/1361-6382/ab8052
extraction:
  note: >-
    Imported so that the wall result's reading, which notes that the propagation of a Hadamard deposit stops
    at Cauchy horizons and that the renormalised stress tensor generically diverges there, cites a Fact
    instead of citing from memory. Checked on 2026-11-01 against the arXiv record of 1912.06047: title,
    authors, DOI, and the abstract (a quantum scalar field on Reissner-Nordstrom-de Sitter; for any state
    that is Hadamard within the domain of dependence of the initial data, the expected stress tensor blows up
    with the affine parameter V along a radial null geodesic crossing the Cauchy horizon as T_VV ~ C/V^2,
    with C independent of the state and C != 0 generically; stronger than the classical divergence, and
    argued to be sufficient to turn the Cauchy horizon into a strong curvature singularity). Cited from
    memory, not checked: the journal volume and article number, and the range of parameters of the field
    for which the coefficient was evaluated.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created at Leon''s decisions of 2026-11-01 (routine imports for the deposit-state results: Hollands, Wald and Zahn 2020, cited by the wall result), checked against the arXiv record as recorded in the note.'
  flags:
  - 'beyond one flat chart: the maximal extension of the Reissner-Nordstrom-de Sitter field through the black-hole interior to its Cauchy horizon'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric is the Reissner-Nordstr\"om-de Sitter metric of a charged hole with positive cosmological constant, and let $\phi$ be a free real scalar field on it. For every state of $\phi$ that is Hadamard (Fact \claimref{synthesis.imported-microlocal-hadamard-condition}(a)) in the domain of dependence of an initial Cauchy surface, the expected renormalised stress tensor along a radial null geodesic crossing the Cauchy horizon of the hole's interior satisfies $\langle T_{VV}\rangle \sim C/V^{2}$ as $V \to 0$, where $V$ is an affine parameter vanishing at the Cauchy horizon and $C$ is independent of the state and generically nonzero. This divergence is stronger than that of the classical field. \emph{Beyond one flat chart:} the statement concerns the maximal extension of the field through the hole's interior to its Cauchy horizon, read on several charts. \emph{Provenance:} \cite{HollandsWaldZahn2020}.

## technical
A charged black hole in a universe with a positive cosmological constant has, inside, a Cauchy horizon beyond which the future is no longer fixed by the initial data. Classically, perturbations may stay mild there. Hollands, Wald and Zahn showed that a quantum scalar field in any regular (Hadamard) state behaves worse: its expected energy density, measured along a light ray falling through the Cauchy horizon, diverges as the inverse square of the affine distance to it, with a coefficient that does not depend on the state and is generically nonzero. They argue that this makes the Cauchy horizon a strong curvature singularity. For a state set on a collar of an earlier surface, the propagation of the Hadamard form reaches only the domain of dependence of that collar, and at such a Cauchy horizon its stress tensor diverges.

## lay
Inside a charged black hole there is a boundary beyond which the laws of physics no longer predict what happens from the past. Hollands, Wald and Zahn showed that the energy of a quantum field becomes infinite as one approaches that boundary, whatever regular state the field starts in, which suggests the boundary is destroyed and replaced by a singularity. This is taken from the literature.

## one-liner
On the Reissner-Nordstr\"om-de Sitter field, for a free scalar field in any state Hadamard in the domain of dependence of the initial data, $\langle T_{VV}\rangle \sim C/V^{2}$ at the Cauchy horizon in an affine parameter $V$, with $C$ state-independent and generically nonzero (Hollands, Wald and Zahn 2020).
