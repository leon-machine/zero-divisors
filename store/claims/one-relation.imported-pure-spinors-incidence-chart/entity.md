---
id: one-relation.imported-pure-spinors-incidence-chart
kind: claim
version: 5
title: "Imported: pure spinors and the incidence chart"
status: proved
region: one-relation
subject: conformal-spacetime
tags: [conformal-spinors, spinor-modules, conformal-model]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
review: typed
derivations:
- name: main
  uses:
  - correspondence.fock-model-complexified-ascended-algebra@9
  - correspondence.incidence-relation-chart@7
  - correspondence.spinor-identification@7
  - correspondence.twistors-are-states-three-ladder-pairs@6
  - mass.imported-flat-model-twistor-chart-infinity@7
  - std-algebra.pure-spinors@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_every_conformal_spinor_is_a_pure_vacuum
- kind: check
  ref: check.py::check_spin6_acts_as_sl4_with_open_vacuum_orbit
- kind: check
  ref: check.py::check_purity_is_one_quadric_at_dimension_eight
- kind: check
  ref: check.py::check_point_embedding_null_and_incidence_lines
locators:
  paper: T16
  number: Fact 2.3
  label: fact:purespinor
  line: 513
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.pure-spinors where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: purity and vacuum-determines-spinor on twelve samples, Spin(6,C) acting as sl(4,C) with open vacuum orbit, the nu = 4 purity quadric, and the point embedding, Klein bivectors and incidence lines. Version 3 -> 4.'
  env: fact
  context_refs:
  - correspondence.fock-model-complexified-ascended-algebra
  - correspondence.incidence-relation-chart
  - correspondence.spinor-identification
  - correspondence.twistors-are-states-three-ladder-pairs
  - mass.imported-flat-model-twistor-chart-infinity
  - one-relation.imported-cartans-purity-theorem-thouless-form
  unresolved_refs:
  - rem:quadric
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: All five uses are the cited sources and kept; the Cartan purity fact is named as the classical
      form of the purity clause only, so it was neither added to the main route nor made a standard-route
      derivation (it does not cover the incidence and chart clauses).
  source_title: "Imported: pure spinors and the incidence chart"
  source_formal: |-
    The complexified ascended algebra $\Cl(2,4)_{\C}$ acts irreducibly on the Fock space $\Lambda^{\bullet}W$ of a maximal isotropic $W \subset \C^{6}$, with twistor space $\T$ its even half; a nonzero twistor $u$ has annihilator $W_{u} = \{v : c(v)u = 0\}$ of dimension exactly three, so every twistor is the Fock vacuum of its own three-pair system, and $W_{u}$ determines $u$ up to scale. This is Cartan's purity theorem in the case $2\nu = 6$ (Fact \claimref{one-relation.imported-cartans-purity-theorem-thouless-form}): every Weyl spinor of $\mathrm{Spin}(6, \C)$ is pure, the vacuum orbit being open in $\mathbb{P}(\T) = \mathbb{P}^{3}$ by the exceptional isomorphism $\mathrm{Spin}(6, \C) \cong SL(4, \C)$, which is the transitivity on which the twistor correspondence rests; it is a low-dimensional coincidence and not a generic property of Fock vacua, purity becoming one quadratic condition at $2\nu = 8$ (Remark \ref{rem:quadric}). A point of conformally compactified spacetime is a null vector of $\C^{6}$, equivalently a simple bivector of $\Lambda^{2}\T$, that is, a line of projective twistor space; the point embedding $X(x) = n_{0} + x - \tfrac12 Q(x)n_{\infty}$, with $\ip{n_{0}}{n_{\infty}} = 1$, is null identically, with the slot coefficient $-\tfrac12$ the only value for which it is, and the incidence relation is the completion's own chart. The completion's fibre quadric double covers the real slice of the Klein quadric. \emph{Provenance:} \cite[Thm.~3.1, Thm.~3.4, Thm.~4.2, Thm.~5.3]{ButlerT9}; \cite[Fact~2.3, Rem.~5.2]{ButlerT11}.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor space and twistors to the conformal spinor space and conformal spinors (\\CS, \\PCS) in all levels and the restating proof; the complexified Fock model and the name of the twistor correspondence (the source paper's subject) are kept."
---

## formal
The complexified ascended algebra $\Cl(2,4)_{\C}$ acts irreducibly on the Fock space $\Lambda^{\bullet}W$ of a maximal isotropic $W \subset \C^{6}$, with the conformal spinor space $\CS$ (twistor space) its even half; a nonzero conformal spinor $u$ has annihilator $W_{u} = \{v : c(v)u = 0\}$ of dimension exactly three, so every conformal spinor is the Fock vacuum of its own three-pair system, and $W_{u}$ determines $u$ up to scale. This is Cartan's purity theorem in the case $2\nu = 6$ (Fact \claimref{one-relation.imported-cartans-purity-theorem-thouless-form}): every Weyl spinor of $\mathrm{Spin}(6, \C)$ is pure, the vacuum orbit being open in $\PCS = \mathbb{P}(\CS) = \mathbb{P}^{3}$ by the exceptional isomorphism $\mathrm{Spin}(6, \C) \cong SL(4, \C)$, which is the transitivity on which the twistor correspondence (of the conformal spinor space with spacetime) rests; it is a low-dimensional coincidence and not a generic property of Fock vacua, purity becoming one quadratic condition at $2\nu = 8$ (Remark \ref{rem:quadric}). A point of conformally compactified spacetime is a null vector of $\C^{6}$, equivalently a simple bivector of $\Lambda^{2}\CS$, that is, a line of the projective spinor space $\PCS$; the point embedding $X(x) = n_{0} + x - \tfrac12 Q(x)n_{\infty}$, with $\ip{n_{0}}{n_{\infty}} = 1$, is null identically, with the slot coefficient $-\tfrac12$ the only value for which it is, and the incidence relation is the completion's own chart. The completion's fibre quadric double covers the real slice of the Klein quadric. \emph{Provenance:} \cite[Thm.~3.1, Thm.~3.4, Thm.~4.2, Thm.~5.3]{ButlerT9}; \cite[Fact~2.3, Rem.~5.2]{ButlerT11}.

## technical
The complexified $\Cl(2,4)_\C$ acts irreducibly on $\Lambda^\bullet W$ for a maximal isotropic $W \subset \C^6$, with the conformal spinor space $\CS$ the even half. Each nonzero conformal spinor $u$ has a three-dimensional annihilator $W_u$, is the Fock vacuum of its own three-pair system, and is fixed up to scale by $W_u$. This is Cartan's purity theorem at $2\nu = 6$, a low-dimensional coincidence: at $2\nu = 8$ purity becomes one quadratic condition.

A point of compactified spacetime is a null vector of $\C^6$, equivalently a simple bivector of $\Lambda^2\CS$, equivalently a line of $\PCS = \mathbb{P}(\CS)$. The point embedding $X(x) = n_0 + x - \tfrac12 Q(x)\,n_\infty$ with $\ip{n_0}{n_\infty} = 1$ is null identically, $-\tfrac12$ being the only slot coefficient for which it is, and the incidence relation is the completion's own chart; the completion's fibre quadric double covers the real slice of the Klein quadric.

## lay
This collects earlier results that the one-relation paper needs. In six complex dimensions every four-component spinor of the conformal algebra is the vacuum of its own small system of fermionic operators, a coincidence special to this dimension. Each point of spacetime corresponds to a line of such spinors, and the standard way of placing spacetime points into the six-dimensional space makes every point a light-like vector.

## one-liner
Imported: every conformal spinor is a pure spinor, the Fock vacuum of its own three-pair system, and spacetime points are null vectors of $\C^6$, equivalently lines of the projective spinor space.
