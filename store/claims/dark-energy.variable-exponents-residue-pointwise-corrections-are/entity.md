---
id: dark-energy.variable-exponents-residue-pointwise-corrections-are
kind: claim
version: 4
title: 'Variable exponents: the residue is pointwise, the corrections are subleading'
status: proved
region: dark-energy
subject: interior
tags: [kasner]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - dark-energy.frozen-point-datum-kasner-wall@7
  - dark-energy.wall-counterterm@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T10.py
  tags:
  - label:lem:varexp
- kind: check
  ref: check.py::check_displayed_connection_is_torsion_free
- kind: check
  ref: check.py::check_listed_correction_orders_positive_on_open_circle
- kind: check
  ref: check.py::check_kasner_relations_pointwise
locators:
  paper: T10
  number: Lem 4.12
  label: lem:varexp
  line: 953
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the displayed connection as the torsion-free GTG rotation-gauge field with placeholder gradients (opposite sign fails), the order count on the open Kasner circle, and pointwise Kasner relations from the gauge fields. Version 2 -> 3. Check entries synced with check.py: +1, -1 (added check_listed_correction_orders_positive_on_open_circle; removed check_corrections_subleading_on_open_circle). Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    note: 'Both uses are premises of the proof (the Kasner-wall curvature and Ricci terms, and the counterterm
      slice value); the source claims no standard route. Levels pass: lay now keeps the diagonal form
      and the open Kasner circle; one-liner adds the diagonal form.'
  env: lemma
  eqrefs: 1
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the Kasner-type metric with variable exponents becomes the derived metric of a gravitational field (hb, Omega) on flat spacetime; the Levi-Civita connection is the rotation-gauge field Omega, displayed as its connection one-forms in the orthonormal coframe of the derived metric; curvature terms are terms of the field strength. Formulas and orders unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact.'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) given by $\hb^{-1}(e_0) = \gamma_0$, $\hb^{-1}(e_i) = \tau^{p_i(x)}\gamma_i$ on the background frame of the labels $(\tau, x^i)$ (derived metric, in components, $g = d\tau^2 - \sum_i\tau^{2p_i(x)}(dx^i)^2$), with smooth exponents $p_i(x)$ taking values in the open Kasner circle ($\sum p_i = 1 = \sum p_i^2$, all $p_i < 1$), physical frame $\{\gamma_0, \gamma_i\}$, $B_i = \gamma_0\wedge\gamma_i$, and $\hat\nabla p_i := \hb^{T}(\nabla p_i) = -\sum_j \tau^{-p_j}(\partial_j p_i)\,\gamma_j$ the physical gradient of the exponent. Then the rotation-gauge field on the physical frame, $\omega(\gamma_a) := \Omega(\hb(\gamma_a))$ (its Levi-Civita connection), is
\[
\omega(\gamma_0) = 0, \qquad
\omega(\gamma_i) \;=\; -\frac{p_i(x)}{\tau}\,B_i \;-\; \log\tau\;\hat\nabla p_i\wedge\gamma_i
\]
(in components, a labelled reading: the connection one-forms $\omega^{i0} = (p_i(x)/\tau)\,e^i$ and $\omega^{ij} = \log\tau\,[(\partial_i p_j)\,\tau^{-p_i}\,e^j - (\partial_j p_i)\,\tau^{-p_j}\,e^i]$ of the coframe $e^0 = d\tau$, $e^i = \tau^{p_i(x)}dx^i$), so the boost block is the pointwise Kasner pole with no correction, and the tangential block is singular of order $\tau^{-p_{\max}}|\log\tau|$ with $p_{\max} := \max_j p_j < 1$: subleading to the pole. Every term of the field strength $\mathcal{R}(B)$ beyond the Kasner double pole of Proposition \claimref{dark-energy.frozen-point-datum-kasner-wall}(i) is of relative order $\tau^{1-p_{\max}}|\log\tau|^m$, $m \leq 2$, and tends to zero: the leading field equations at the wall are the Kasner relations pointwise in $x$, the residue of the datum's pole is the pointwise Kasner boost, and the wall counterterm of Proposition \claimref{dark-energy.wall-counterterm} has density $8\,p_1p_2p_3(x)\,\varepsilon^{-2}d^3x$ pointwise.

## technical
Take a gravitational field on flat spacetime with $\hb^{-1}(e_0) = \gamma_0$, $\hb^{-1}(e_i) = \tau^{p_i(x)}\gamma_i$ (derived metric $d\tau^2 - \sum_i \tau^{2p_i(x)}(dx^i)^2$), with smooth exponents in the open Kasner circle ($\sum_i p_i = 1 = \sum_i p_i^2$, all $p_i < 1$). On the physical frame its rotation-gauge field is $\Omega(\hb(\gamma_i)) = -(p_i(x)/\tau)\,\gamma_0\wedge\gamma_i - \log\tau\,\hb^{T}(\nabla p_i)\wedge\gamma_i$: a boost block that is the pointwise Kasner pole with no correction, and a tangential block built from $\log\tau$ times the physical gradients of the exponents, of order $\tau^{-p_{\max}}|\log\tau|$ with $p_{\max} = \max_j p_j < 1$, hence subleading to the pole.

Every term of the field strength beyond the Kasner double pole has relative order $\tau^{1 - p_{\max}}|\log\tau|^m$ with $m \leq 2$ and tends to zero. So the leading field equations at the wall are the Kasner relations pointwise in $x$, the residue of the datum's pole is the pointwise Kasner boost, and the wall counterterm has density $8\,p_1p_2p_3(x)\,\varepsilon^{-2}d^3x$ pointwise.

## lay
The Kasner description of a singularity normally uses fixed exponents, the same everywhere along the singular surface. Here, for gravitational fields whose metric reading has the simple diagonal form and with every exponent kept below one (the open Kasner circle), the exponents are allowed to vary smoothly from place to place. The result shows that the leading singular behaviour is then the fixed-exponent picture applied point by point, and that the extra terms caused by the variation are weaker and fade out at the singularity.

## one-liner
For a gravitational field with diagonal Kasner-type derived metric and smooth position-dependent exponents on the open Kasner circle, the boost block of the connection is the pointwise Kasner pole and every correction is subleading, so the wall field equations, the residue and the counterterm density all hold pointwise.
