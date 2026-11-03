---
id: synthesis.imported-renormalised-stress-tensor-of-hadamard-dirac-states
kind: claim
version: 1
title: 'Imported: for the Dirac field on a globally hyperbolic gravitational field, Wick polynomials defined by Hadamard point splitting give Hadamard states a covariantly conserved renormalised stress-energy tensor, whose trace anomaly is computed (Dappiaggi, Hack and Pinamonti 2009)'
status: imported
region: synthesis
subject: quantum-fields
tags: [car-algebra, curvature-and-field-equations, classical-theorem]
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
- citation: 'C. Dappiaggi, T.-P. Hack and N. Pinamonti, The extended algebra of observables for Dirac fields and the trace anomaly of their stress-energy tensor, Rev. Math. Phys. 21 (2009), 1241--1312; arXiv:0904.0612.'
  key: DappiaggiHackPinamonti2009
  doi: 10.1142/S0129055X09003864
extraction:
  note: >-
    Imported so that the deposit premise can state what a Hadamard deposit supplies to the gravitational
    side (the expected stress tensor, the source of the field equations) with a Fact instead of a citation
    from memory. Checked on 2026-11-01 against the arXiv record of 0904.0612: title, authors, DOI, and the
    abstract (Dirac fields on arbitrary globally hyperbolic Lorentzian spacetimes in the locally covariant
    framework; the associated notion of Hadamard states; Wick polynomials for spinor fields; with them a
    covariantly conserved stress-energy tensor suited for back-reaction computations; its trace anomaly
    computed explicitly). Cited from memory, not checked: the journal volume and pages, and that the
    renormalised tensor is fixed up to local covariant terms built from the curvature and the mass (the
    renormalisation freedom of Wick polynomials in the locally covariant framework).
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created at Leon''s decisions of 2026-11-01 (routine import for the deposit-state results: the renormalised stress tensor for Hadamard Dirac states), checked against the arXiv record as recorded in the note.'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric is smooth and globally hyperbolic, and let $\psi$ be the free Dirac field on it, formulated as a locally covariant quantum field theory. Wick polynomials of $\psi$ are defined by point splitting with the Hadamard parametrix subtracted (the extended algebra of observables). On every Hadamard state $\omega$ (Fact \claimref{synthesis.imported-microlocal-hadamard-condition}(b)) they give an expected stress-energy tensor $\langle T_{ab}\rangle_{\omega}$, a smooth symmetric tensor field of the derived metric, which is covariantly conserved, $\nabla^{a}\langle T_{ab}\rangle_{\omega} = 0$; its trace anomaly is computed explicitly there. \emph{Provenance:} \cite{DappiaggiHackPinamonti2009}. Cited from memory, not part of the checked statement: that the trace anomaly is a local polynomial in the curvature and the mass, the same for every state; that the renormalised tensor is fixed up to local covariant terms built from the curvature and the mass; and that the difference of the tensors of two Hadamard states, the coincidence limit of a differential operator applied to their smooth difference kernel, needs no renormalisation.

## technical
A quantum field's energy density cannot be read off its two-point function directly, since the coincidence limit is infinite; on Hadamard states the infinite part is the same universal singularity for every state and can be subtracted geometrically. Dappiaggi, Hack and Pinamonti carried this out for the Dirac field on any globally hyperbolic gravitational field, in the locally covariant framework: they defined Wick polynomials of the spinor field by subtracting the Hadamard parametrix, and with them a stress-energy tensor that is covariantly conserved on Hadamard states and so can act as the source of the gravitational field equations. Its trace is the trace anomaly, which they computed. The tensor is defined only on Hadamard states, and the remaining freedom is in local curvature terms common to all states.

## lay
In a gravitational field the energy carried by a quantum field can be computed only for well-behaved quantum states, called Hadamard states, by removing an infinite part that is the same for all of them. For electrons and the other particles of spin one half this was worked out by Dappiaggi, Hack and Pinamonti, who showed that the resulting energy and momentum are conserved, so they can serve as the source in the equations of gravity. This is taken from the literature.

## one-liner
For the Dirac field on a globally hyperbolic gravitational field, Hadamard point splitting defines Wick polynomials and a covariantly conserved renormalised stress-energy tensor on every Hadamard state, with an explicitly computed, state-independent trace anomaly (Dappiaggi, Hack and Pinamonti 2009).
