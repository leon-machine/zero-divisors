---
id: synthesis.imported-fayet-iliopoulos-level-only-for-abelian-factors
kind: claim
version: 1
title: 'Imported: Fayet-Iliopoulos levels only for abelian factors'
status: imported
region: synthesis
subject: standard-model
tags: [gauge-fields, symmetry-breaking, classical-theorem]
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
imported_from:
- citation: 'P. Fayet and J. Iliopoulos, Spontaneously broken supergauge symmetries and Goldstone spinors, Phys. Lett. B 51 (1974), 461--464.'
  key: FayetIliopoulos1974
  doi: 10.1016/0370-2693(74)90310-4
- citation: 'Y. Shadmi and Y. Shirman, Dynamical supersymmetry breaking, arXiv:hep-th/9907225, Section II.C.2, equation (14).'
  key: ShadmiShirman1999
extraction:
  note: >-
    Imported so that the level result can pin the standard fact its clause (2) makes explicit on the rung
    summand, instead of citing it from memory. Checked on 2026-11-01: the bibliographic data of Fayet and
    Iliopoulos (title, authors, Phys. Lett. B 51, 461-464, 1974, DOI) against its INSPIRE record; the
    statement against Shadmi and Shirman, arXiv:hep-th/9907225, Section II.C.2 ("Fayet-Iliopoulos
    breaking"), which cites Fayet and Iliopoulos 1974 and states that in an abelian theory the D-term of
    the vector superfield is invariant under the gauge and supersymmetry transformations by itself, the
    term xi V of its equation (14). The journal reference of Shadmi and Shirman is not stated here. The
    one-line reason given in the formal statement (a linear term in the moment maps is invariant exactly
    when its coefficient is fixed by the adjoint action) is standard Lie algebra, written out here.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Fayet-Iliopoulos 1974 as a Fact, by Leon''s further imports).'
---

## formal
Let a compact gauge algebra $\mathfrak{g}$ act on a scalar field space with moment maps $\mu_{a}$, so that the D-term potential is $V_{D} = \tfrac12\sum_{a}g_{a}^{2}\mu_{a}^{2}$. A Fayet-Iliopoulos term, a level $\zeta$ shifting the moment maps as $V_{D} = \tfrac12\sum_{a}g_{a}^{2}(\mu_{a} - \zeta_{a})^{2}$ (equivalently a term linear in the auxiliary fields $D^{a}$, $\xi V$ in the vector superfield), is gauge invariant (and, in a supersymmetric theory, supersymmetric) exactly when $\zeta_{a}\mu_{a}$ is invariant, that is when $\zeta$ is fixed by the adjoint action, i.e. lies in the centre of $\mathfrak{g}$. Hence a D-term level exists only for the abelian $\mathfrak{u}(1)$ factors of the gauge algebra and vanishes on every simple factor. \emph{Provenance:} \cite{FayetIliopoulos1974}; the statement as in \cite{ShadmiShirman1999}, Section II.C.2.

## technical
In a gauge theory whose scalar potential is built from the gauge moment maps (the D-terms, as in supersymmetric theories), one may add a constant to a moment map, which shifts where the potential is minimised. Such a constant is allowed only if it is unchanged by the gauge transformations, and the moment maps of a non-abelian factor rotate into each other, so the constant must vanish there; only for an abelian factor, whose moment map is gauge invariant, can it be nonzero. This is the Fayet-Iliopoulos term.

## lay
In some theories of particle forces the energy of the Higgs-like fields can be shifted by a fixed constant, which then decides where the fields settle. Fayet and Iliopoulos introduced this constant; it is allowed only for the simplest, electromagnetism-like kind of force, not for the forces whose charges rotate into one another.

## one-liner
A D-term level (Fayet-Iliopoulos term) must be fixed by the adjoint action, so it lies in the centre of the gauge algebra and exists only for abelian factors (Fayet and Iliopoulos 1974).
