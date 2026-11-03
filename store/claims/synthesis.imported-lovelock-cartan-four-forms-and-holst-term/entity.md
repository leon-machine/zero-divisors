---
id: synthesis.imported-lovelock-cartan-four-forms-and-holst-term
kind: claim
version: 1
title: 'Imported: the Lorentz-invariant four-forms of a frame and a rotation-gauge field with no inverse frame (Mardones and Zanelli), and the Holst term, inert on the vacuum field equations (Holst)'
status: imported
region: synthesis
subject: einstein
tags: [curvature-and-field-equations, gauge-fields, classification, classical-theorem]
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
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'A. Mardones and J. Zanelli, Lovelock-Cartan theory of gravity, Class. Quantum Grav. 8 (1991), 1545--1558.'
  key: MardonesZanelli1991
- citation: 'S. Holst, Barbero''s Hamiltonian derived from a generalized Hilbert-Palatini action, Phys. Rev. D 53 (1996), 5966--5969; arXiv:gr-qc/9511026.'
  key: Holst1996
  doi: 10.1103/PhysRevD.53.5966
- citation: 'J. Zanelli, Lecture notes on Chern-Simons (super-)gravities, arXiv:hep-th/0502193 (second edition, 2008).'
  key: Zanelli2005
- citation: 'A. Perez and C. Rovelli, Physical effects of the Immirzi parameter, Phys. Rev. D 73 (2006), 044013; arXiv:gr-qc/0505081.'
  key: PerezRovelli2006
  doi: 10.1103/PhysRevD.73.044013
- citation: 'L. Freidel, D. Minic and T. Takeuchi, Quantum gravity, torsion, parity violation and all that, Phys. Rev. D 72 (2005), 104002; arXiv:hep-th/0507253.'
  key: FreidelMinicTakeuchi2005
  doi: 10.1103/PhysRevD.72.104002
extraction:
  note: >-
    Imported for the classification of curvature-only actions of the tractor gauge field, which
    compares its count with the Lovelock-Cartan list and names its inert term after Holst, and for
    the results that discuss the Holst coefficient and the spin coupling. Checked on 2026-10-31: the
    four-dimensional list in (a) against Zanelli's lecture notes, arXiv:hep-th/0502193 (the Lovelock
    terms of his Eq. (53), the three further terms e^a e^b R_ab, T^a T_a and R^ab R_ab of Eq. (64), the
    Nieh-Yan form of Eq. (65) and the exclusion of the Hodge dual and the inverse metric as building
    blocks), which attributes the general construction to Mardones and Zanelli; Holst's title, journal
    data, DOI and abstract (Barbero's real connection variables derived from a generalised
    Hilbert-Palatini action) against arXiv:gr-qc/9511026; the journal data, DOIs and abstracts of Perez
    and Rovelli (with fermions the term multiplying the Immirzi parameter does not vanish on shell and
    sets the strength of a four-fermion interaction) and of Freidel, Minic and Takeuchi (minimal coupling
    preserves parity, non-minimal coupling to torsion violates it) against their arXiv pages. The
    volume and page range of Mardones and Zanelli, the vacuum statement of (b) and the sign conventions
    are cited from memory, not checked against the source.
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created at Leon''s decision of 2026-10-31 approving the import of Mardones-Zanelli and Holst, merged into one Fact, with the Barbero-Immirzi contact-term readings recorded as a note; partly verified (see note).'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on four-dimensional flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with the frame and the rotation gauge field varied independently (first-order variables). Write $e(a) = \hb^{-1}(a)$ for the soldering form (a vector-valued one-form), $R$ for the field strength of $\Omega$ written as a bivector-valued two-form, and $T = De$ for the torsion (a vector-valued two-form); $I_{4}$ is the spacetime pseudoscalar.
\begin{enumerate}
\item[(a)] (Mardones and Zanelli.) The four-forms invariant under local rotations that are polynomial in $e$, $R$ and $T$, built with the exterior product of forms and the geometric product of their values, with no Hodge dual and no inverse frame, are, up to exact forms, combinations of: the scalar and $I_{4}$ parts of $R \wedge R$ (the Pontryagin density and the Euler density), of $(e \wedge e) \wedge R$ (the Holst-type density and the Einstein-Hilbert density), and of $(e \wedge e) \wedge (e \wedge e)$ (the $I_{4}$ part is the volume), and the torsion square, the scalar part of $T \wedge T$ with the vector values multiplied by the inner product (index readings: $R^{ab}R_{ab}$, $\epsilon_{abcd}R^{ab}R^{cd}$, $e^{a}e^{b}R_{ab}$, $\epsilon_{abcd}R^{ab}e^{c}e^{d}$, $\epsilon_{abcd}e^{a}e^{b}e^{c}e^{d}$, $T^{a}T_{a}$). The Pontryagin density and the Nieh-Yan combination $T^{a}T_{a} - e^{a}e^{b}R_{ab}$ are exact; the Euler density is locally exact. In $n$ dimensions the same construction gives the Lovelock series together with a finite list of torsional terms.
\item[(b)] (Holst.) Adding to the Einstein-Cartan (Palatini) functional with cosmological term the Holst term, a constant multiple $1/\gamma$ ($\gamma$ real and nonzero) of the Holst-type density $e^{a} \wedge e^{b} \wedge R_{ab}$, leaves the vacuum field equations unchanged: without matter the connection equation still forces zero torsion, and on torsion-free fields the Holst density's contribution to the frame equation vanishes by the cyclic (first Bianchi) identity of the curvature. The canonical analysis of the modified functional gives Barbero's real connection variables, with $\gamma$ the Barbero-Immirzi parameter.
\end{enumerate}
\emph{Note (the Barbero-Immirzi contact term; readings from the literature).} With spinning matter the torsion is fixed algebraically by the spin density (Fact \claimref{synthesis.imported-einstein-cartan-matter-coupling}), and the Holst term no longer drops out: with minimally coupled fermions $\gamma$ sets the strength of the resulting four-fermion contact interaction \cite{PerezRovelli2006}; with minimal coupling parity is preserved, and a non-minimal coupling of the fermions to torsion violates it \cite{FreidelMinicTakeuchi2005}.

\emph{Provenance:} \cite{MardonesZanelli1991} for (a), with the four-dimensional list as in \cite{Zanelli2005}; \cite{Holst1996} for (b).

## technical
When gravity is written with the frame and the rotation gauge field as independent fields, the possible actions in four dimensions that use only exterior products (no Hodge dual, no inverse frame) form a short list, worked out in general by Mardones and Zanelli: the Euler (Gauss-Bonnet), Einstein-Hilbert and volume terms, the Pontryagin density, the term pairing the frame square with the curvature without the alternating symbol (the Holst-type term), and the torsion square; the Pontryagin and Nieh-Yan combinations are total derivatives. Holst showed that adding the Holst-type term with coefficient $1/\gamma$ to the usual first-order action does not change the vacuum field equations, because it is inert on torsion-free fields, and that its Hamiltonian form gives Barbero's real connection variables with the Barbero-Immirzi parameter $\gamma$. As a note: with spinning matter the torsion is not zero, and the literature finds that the term then sets the strength of a four-fermion contact interaction (Perez and Rovelli), and that parity is kept for minimal coupling and broken by non-minimal coupling to torsion (Freidel, Minic and Takeuchi). Taken from the literature.

## lay
If gravity is described like the other forces, with two independent ingredients, only a handful of building blocks for its law are possible in four dimensions; Mardones and Zanelli listed them. One of them, studied by Holst, has no effect at all on gravity in empty space, which is why it is free to be added; it matters only when matter with spin is present, where it changes a very weak spin-spin force. These results are taken from the literature.

## one-liner
In first-order variables with no Hodge dual or inverse frame, the four-dimensional Lorentz-invariant four-forms are, up to exact forms, Euler, Einstein-Hilbert, volume, Pontryagin, the Holst-type $e^{a}e^{b}R_{ab}$ and $T^{a}T_{a}$ (Mardones and Zanelli 1991), and the Holst term leaves the vacuum equations unchanged (Holst 1996), entering with spinning matter through a contact term.
