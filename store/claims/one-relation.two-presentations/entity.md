---
id: one-relation.two-presentations
kind: claim
version: 4
title: The two presentations
status: proved
region: one-relation
subject: one-relation
tags: [two-readings, car-algebra, witt-index]
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
  - one-relation.imported-pure-spinors-incidence-chart@5
  - std-algebra.vector-squares@1
  - std-algebra.witt-basis-car@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T16.py
  tags:
  - label:prop:twopresentations
- kind: check
  ref: check.py::check_orthogonal_reading_is_the_metric
- kind: check
  ref: check.py::check_witt_reading_is_the_car
- kind: check
  ref: check.py::check_fock_module_from_the_vacuum
locators:
  paper: T16
  number: Prop 3.1
  label: prop:twopresentations
  line: 552
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.vector-squares, std-algebra.witt-basis-car where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: orthogonal anticommutators 2 g_ab; Witt bases of Cl(1,1), Cl(1,3)_C, Cl(2,4)_C (real and complex pairs) satisfy the CAR exactly and are bases over Q(i); the vacuum wbar_1 ... wbar_r generates a Fock module of dimension 2, 4, 8 closed under the generators, with an r-dimensional annihilator. Version 2 -> 3.'
  env: proposition
  context_refs:
  - interior.covariant-form-vacuum-equations
  - one-relation.imported-pure-spinors-incidence-chart
  - tower.witt-index-quantum-capacity
  typing:
    by: ai-typing-pass
    added: [one-relation.imported-pure-spinors-incidence-chart]
    note: 'Added the pure-spinor Fact, which the statement names as supplying the Fock module; the T03 capacity theorem and T06 vacuum-equation theorem in context_refs are context only.'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$(e_2 \pm ie_3)/2$ in $\Cl(1,3)_\C$ and $V_\C$: complexified vector space, $i$ next to spacetime
      vectors (complexified space); indices $i, j$ (index)'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - one-relation.imported-pure-spinors-incidence-chart
---

## formal
The defining relation of a Clifford algebra, $\{e_{a}, e_{b}\} = 2g_{ab}\mathbf{1}$, carries both theories as its two canonical presentations. On an orthogonal basis the relation displays a metric: the geometric reading, which the geometry paper carries to the vacuum Einstein equations and proves there equivalent to parallelism of the scale tractor \cite[Thm.~4.5]{ButlerT6}. On a Witt basis, a maximal isotropic decomposition $V_{\C} = W \oplus \bar{W}$ with the cross pairing normalised to $\ip{w_{i}}{\bar{w}_{j}} = \tfrac12\delta_{ij}$, the same relation reads
\[
\{c(w_{i}), c(w_{j})\} = 0, \qquad \{c(w_{i}), c(\bar{w}_{j})\} = \delta_{ij},
\]
verbatim the canonical anticommutation relations of $\dim W$ fermionic modes, with the Fock module supplied by the pure-spinor construction (Fact \claimref{one-relation.imported-pure-spinors-incidence-chart}). Over $\R$ the same reading is available on the real null pairs alone, and Fact \claimref{tower.witt-index-quantum-capacity} counts them. The metric is the anticommutator and the anticommutator is the metric; geometric versus quantum is a choice of chart on one object, not a choice of object. The claim is kinematic: it identifies the metric datum with the CAR algebra, and says nothing about dynamics, states, and measurement, which carry their own levels below.

## technical
The Clifford relation $\{e_{a}, e_{b}\} = 2g_{ab}\mathbf{1}$ has two canonical presentations. On an orthogonal basis it displays a metric, the geometric reading. On a Witt basis $V_{\C} = W \oplus \bar{W}$ with $\ip{w_{i}}{\bar{w}_{j}} = \tfrac12\delta_{ij}$ it reads $\{c(w_{i}), c(w_{j})\} = 0$ and $\{c(w_{i}), c(\bar{w}_{j})\} = \delta_{ij}$, the canonical anticommutation relations of $\dim W$ fermionic modes, with the Fock module supplied by the pure-spinor construction.

Both bases generate the same algebra, so geometric versus quantum is a choice of chart on one object. The claim is kinematic only: it identifies the metric datum with the CAR algebra and says nothing about dynamics, states or measurement.

## lay
The basic rule of a Clifford algebra can be written in two ways. In one it describes distances and angles, the language of geometry and gravity; in the other it is exactly the rule obeyed by fermions, the language of quantum theory. The paper takes this to mean that geometry and quantum structure are two views of one object, though only at the level of structure, not of how things evolve.

## one-liner
Read on an orthogonal basis the Clifford relation is a metric, and read on a Witt basis it is the canonical anticommutation relations, so the geometric and quantum readings are two charts on one algebra.
