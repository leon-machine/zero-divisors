---
id: obj.hawking.continuum-mode-space
kind: object
version: 2
title: Continuum mode space
status: defined
region: hawking
subject: thermality
tags: [car-algebra, limits]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
review: typed
about:
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics
locators:
  paper: T07
  number: Def 4.1
  label: def:continuum
  line: 535
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By Leon''s ruling R2 (7 November 2026) the complex unit of the one-particle space h is the field theory''s unit I_4: the dynamics is a(e^{I_4 th}f), numbers read in span{1, I_4}; the sentence on the countable case now says that the boundary-mode algebra keeps its own unit (ruling R1). Nothing stays; the earlier declaration is removed.'
  env: definition
  typing:
    by: ai-typing-pass
    note: Definition only; levels written, no edge changes.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - hawking.imported-ideal-fermi-gas-uniqueness
    - hawking.imported-quasi-free-kms-reduces-two
    added_about: []
    verdict: connected
    note: A definition cannot carry uses or assumes; the added links are about edges from the claims whose
      statements use the defined notion. Also linked from the thermal-representation import.
---

## formal
Let $\mathfrak{h}$ be a separable complex Hilbert space (the one-particle space, its complex unit the field theory's unit $I_{4}$, numbers read in $\mathrm{span}\{1, I_{4}\}$; for the Schwarzschild s-wave sector, $L^2(\R_+, d\omega)$; with angular channels, a direct sum of copies indexed by $(\ell, m)$ and species), and let $h$ be self-adjoint on $\mathfrak{h}$ (the one-particle Hamiltonian of Schwarzschild time; for the s-wave sector, multiplication by the frequency $\omega$; self-adjointness, not positivity, is what the theorems below use, and Section \ref{sec:seam}'s bilateral ladder is an instance with spectrum unbounded below). The \emph{continuum mode space} is the CAR algebra $\CAR(\mathfrak{h})$ with the quasi-free (Bogoliubov) dynamics $\tau_t(a(f)) = a(e^{I_{4}th}f)$. The countable mode space of Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics} is the case $\mathfrak{h} = \ell^2(J)$, read as an abstract complex space: the boundary-mode algebra keeps its own complex unit, which the store does not identify with $I_{4}$ (its modes descend from T05's atom and anticommute with $I_{4}$); the CAR functor turns isometric inclusions of one-particle spaces into unital embeddings of algebras, so refining the tower's mode set into a dense subset of the continuum realises $\CAR(\mathfrak{h})$ as the completed union of tower-type subalgebras: the continuum is the tower's limit re-parametrised, not a new object.

## technical
Given a separable complex Hilbert space $\mathfrak{h}$ (the one-particle space, its complex unit the field theory's unit $I_{4}$; for the Schwarzschild s-wave sector $L^2(\R_+, d\omega)$, and with angular channels a direct sum of copies indexed by $(\ell, m)$ and species) and a self-adjoint one-particle Hamiltonian $h$ on it, the continuum mode space is the CAR algebra $\CAR(\mathfrak{h})$ with the quasi-free dynamics $\tau_t(a(f)) = a(e^{I_{4}th}f)$. Only self-adjointness of $h$ is required, not positivity, so a spectrum unbounded below is allowed.

The countable mode space of the boundary-mode algebra is the case $\mathfrak{h} = \ell^2(J)$, as an abstract complex space; the boundary-mode algebra keeps its own complex unit, not identified with $I_{4}$. Because the CAR functor turns isometric inclusions of one-particle spaces into unital embeddings of algebras, refining the tower's mode set into a dense subset of the continuum realises $\CAR(\mathfrak{h})$ as the completed union of tower-type subalgebras: the continuum is the tower's limit re-parametrised, not a new object.

## lay
The boundary modes of a black hole can be labelled either by a countable list or by a continuous range of frequencies. This definition sets up the continuous version: the standard algebra of fermion operators built on a space of one-particle wavefunctions, with time evolution given by a one-particle energy operator. The countable version is a special case, and refining it fills out the continuous one, so nothing new is being introduced.

## one-liner
The continuum mode space is the CAR algebra of a one-particle Hilbert space with the quasi-free dynamics of a self-adjoint one-particle Hamiltonian, the countable mode space being the case $\mathfrak{h} = \ell^2(J)$ and the continuum the completed union of its refinements.
