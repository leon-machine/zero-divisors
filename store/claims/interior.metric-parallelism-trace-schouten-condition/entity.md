---
id: interior.metric-parallelism-trace-schouten-condition
kind: claim
version: 6
title: Metric parallelism, and the trace of the Schouten condition
status: proved
region: interior
subject: einstein
tags: [tractors, curvature-and-field-equations]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
review: typed
derivations:
- name: main
  uses:
  - interior.imported-tractor-connection@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:4.2
- kind: check
  ref: check.py::check_tractor_gauge_field_preserves_tractor_metric
- kind: check
  ref: check.py::check_derivative_of_q_along_a_tractor_field
- kind: check
  ref: check.py::check_opposite_schouten_sign_breaks_metric_preservation
- kind: check
  ref: check.py::check_trace_of_schouten_condition
locators:
  paper: T06
  number: Lem 4.2
  label: lem:elementary
  line: 451
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Cl(2,4) tractor gauge field built from hb, Omega and the computed Schouten map preserves Q on six GTG fields and for a non-symmetric P, with the stored slots and d Q = 2 V . D^T V on jet tractor fields; one-slot sign flip control; Ric -> P injective with inverse 2P + tr P, P = c id forces c = R/24. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the connection is the tractor gauge field on flat spacetime (a bivector-valued field, so metric preservation is the rotation property), and the Schouten condition is read on the field strength of a gravitational field with derived metric g. Proof prefixed.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: lemma
  eqrefs: 3
  typing:
    by: ai-typing-pass
    added: [interior.imported-tractor-connection]
    note: 'Added the tractor-connection fact: the lemma is about its displayed connection and Schouten formula (cited by equation reference, not claimref), and the proof computes with both.'
---

## formal
Let $g$ be the derived metric of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). (i) The connection \eqref{eq:tractorconn}, which on flat spacetime is the $\Cl(2,4)$ gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, preserves the tractor metric \eqref{eq:tractormetric}, the square $Q$ of $\Cl(2,4)$. (ii) If $\Sch_{ab} = c\, g_{ab}$ for a function $c$, that is $\Sch(A) = c\,A$ for the Schouten map of the field strength, then $c = \tfrac{R}{24}$ and $\Ric_{ab} = \tfrac{R}{4} g_{ab}$, that is $\mathcal{R}(A) = \tfrac14\mathcal{R}\,A$; in particular $\Sch_{ab} = 0$ if and only if $\Ric_{ab} = 0$.

## technical
(i) The tractor connection preserves the tractor metric. On flat spacetime the connection is a $\Cl(2,4)$ bivector-valued gauge field acting by the commutator product, an infinitesimal rotation, so it preserves $Q$; in index form, differentiating $Q(T)$ along any direction and substituting the connection, the genuine derivative terms reassemble the derivative of $Q(T)$, and the remaining terms cancel in pairs; the two Schouten terms are one contraction written with the index raised on either side, so no symmetry of $\Sch$ is needed.

(ii) For a gravitational field with derived metric $g$, if $\Sch_{ab} = c\,g_{ab}$ for a function $c$, tracing gives $c = R/24$, and substituting back gives $\Ric_{ab} = \tfrac{R}{4}g_{ab}$. In particular $\Sch_{ab} = 0$ if and only if $\Ric_{ab} = 0$.

## lay
This lemma records two elementary facts behind the tractor form of the gravitational field equations. First, the natural derivative on the tractor bundle, which on flat spacetime is a field of rotations of the six-dimensional conformal model, respects that model's own notion of length. Second, if the Schouten tensor, a rearranged form of the gravitational field strength, is a multiple of the metric then the field is Einstein, and the Schouten tensor vanishes exactly when the Ricci curvature does.

## one-liner
The tractor gauge field preserves the tractor metric, and a Schouten map proportional to the identity forces the factor to be $R/24$ and the field to be Einstein, so $\Sch = 0$ exactly when $\Ric = 0$.
