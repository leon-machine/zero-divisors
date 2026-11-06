---
id: synthesis.imported-ikeda-taniguchi-spectra-of-the-hodge-laplacian-on-spheres
kind: claim
version: 1
title: 'Imported: Hodge Laplacian spectra on spheres (Ikeda and Taniguchi 1978)'
status: imported
region: synthesis
subject: einstein
tags: [mode-counting, representation-theory, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-02
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'A. Ikeda and Y. Taniguchi, Spectra and eigenforms of the Laplacian on $S^{n}$ and $P^{n}(\mathbb{C})$, Osaka J. Math. 15 (1978), no. 3, 515--546.'
  key: IkedaTaniguchi1978
  locator: 'Sec. 1 (decomposition of eigenforms into closed and coclosed parts); Thm. 4.2 (eigenvalues on the irreducible submodules of p-forms on S^n)'
extraction:
  note: >-
    Imported so that the result on the Krein quartet in induced gravity can pin the one-form spectra on S^3 and
    S^4 it uses instead of citing them from memory. Checked on 2 November 2026 against the copy of the paper in
    the Osaka University repository (ojm15_03_04.pdf): title, authors, journal, volume 15, issue 3, pages
    515--546, 1978; the decomposition of each nonzero eigenspace of p-forms into closed and coclosed parts,
    exchanged by d and its adjoint as isomorphisms of SO(n+1)-modules (Sec. 1); and the form of Thm. 4.2, which
    gives the eigenvalue on the irreducible submodule of highest weight lambda as the Casimir value
    <lambda + 2 delta, lambda> in the paper's normalisation, each submodule occurring once except in the middle
    degree of even n. The explicit coexact one-form eigenvalues and multiplicities stated here were not legible in
    the extracted table and are cited from memory (standard; the S^3 values are the photon spectrum of the
    Einstein static field); they are confirmed indirectly by the citing result, whose check reproduces from them
    the exact heat-kernel densities.
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Created by the maintainer pass of 2 November 2026, by Leon''s list of routine imports (Ikeda-Taniguchi 1978), for the result on the Krein quartet in the induced Einstein-Hilbert coefficient.'
---

## formal
On the round unit sphere $S^{n}$, $n \ge 2$, the Hodge Laplacian $\Delta = d\delta + \delta d$ on functions has eigenvalues $l(l + n - 1)$, $l \ge 0$, with multiplicity $\binom{n + l}{n} - \binom{n + l - 2}{n}$ (the harmonic polynomials of degree $l$). On one-forms every nonzero eigenspace splits into exact and coexact parts, which $d$ and $\delta$ exchange: the exact forms $d\phi$ carry the nonzero eigenvalues of functions, and the coexact forms carry the eigenvalues $(l + 1)(l + n - 2)$, $l \ge 1$, each on one irreducible $SO(n + 1)$-module. In particular the coexact eigenvalues are $(l + 1)^{2}$ with multiplicity $2l(l + 2)$ on $S^{3}$, and $(l + 1)(l + 2)$ with multiplicity $\tfrac12 l(l + 3)(2l + 3)$ on $S^{4}$, $l \ge 1$ \cite{IkedaTaniguchi1978}. The spheres here are closed Riemannian manifolds, not gravitational fields on flat spacetime; the store uses these spectra only through the local heat-kernel densities they reproduce, as a Euclidean reading.

## technical
The Laplacian on the round sphere is diagonalised by the representation theory of its rotation group: each eigenspace is an irreducible module, and its eigenvalue is a Casimir value. For one-forms the gradients of the scalar harmonics carry the scalar eigenvalues, and the divergence-free (coexact) forms carry $(l + 1)(l + n - 2)$. On the three-sphere these are the photon modes of the Einstein static universe, $(l + 1)^{2}$ with $2l(l + 2)$ states, two helicities; on the four-sphere they are $(l + 1)(l + 2)$ with $\tfrac12 l(l + 3)(2l + 3)$ states, the first level being the ten Killing vectors.

## lay
On a perfectly round sphere, waves of any kind can only vibrate at certain frequencies, fixed by the sphere's symmetry. Ikeda and Taniguchi listed these frequencies for the various kinds of waves, including the ones that describe light. The series uses their list when it counts how the light-like fields contribute to the strength of gravity induced by quantum fluctuations.

## one-liner
On the round $S^{n}$, functions have $\Delta$-eigenvalues $l(l + n - 1)$ and coexact one-forms $(l + 1)(l + n - 2)$, $l \ge 1$: $(l + 1)^{2}$ with multiplicity $2l(l + 2)$ on $S^{3}$, $(l + 1)(l + 2)$ with multiplicity $\tfrac12 l(l + 3)(2l + 3)$ on $S^{4}$ (Ikeda-Taniguchi 1978).
