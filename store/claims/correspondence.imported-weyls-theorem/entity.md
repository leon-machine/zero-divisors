---
id: correspondence.imported-weyls-theorem
kind: claim
version: 2
title: 'Imported: Weyl''s theorem'
status: imported
region: correspondence
subject: einstein
tags: [classical-theorem, curvature-and-field-equations]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: H. Weyl, Reine Infinitesimalgeometrie, Math. Z. 2 (1918), 384--411.
  key: Weyl1918
locators:
  paper: T09
  number: Fact 6.3
  label: fact:weyl
  line: 795
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: G1s reading adopted: for a gravitational field on flat R^{p,q} (d >= 4, d-dimensional clause), the derived metric is locally conformally flat, i.e. a gauge with hb^{-1}(a) = e^{omega} a exists locally, iff the Weyl curvature W vanishes; the classical theorem kept as stated.'
  typing:
    by: ai-typing-pass
    note: 'Imported classical result; levels only.'
  env: fact
---

## formal
A pseudo-Riemannian metric in dimension at least four is locally conformally flat if and only if its Weyl tensor vanishes. In Gauge Theory Gravity (the $d$-dimensional clause of Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}, $d \geq 4$): for a gravitational field $(\hb, \Omega)$ on flat $\R^{p,q}$, its derived metric is locally conformally flat, that is, about each point of the invertible region there is a gauge in which $\hb^{-1}(a) = e^{\omega}a$ for a scalar function $\omega$, if and only if its Weyl curvature $\mathcal{W}(a \wedge b) = \mathcal{R}(a \wedge b) - \Sch(a) \wedge b - a \wedge \Sch(b)$ vanishes. \emph{Provenance:} \cite{Weyl1918}.

## technical
For a pseudo-Riemannian metric $g$ in dimension $n \geq 4$: $g$ is locally conformally flat, that is locally of the form $e^{2\omega}\eta$ with $\eta$ flat, if and only if its Weyl tensor vanishes. For a gravitational field on flat $\R^{p,q}$ this says: locally there is a gauge with $\hb^{-1}(a) = e^{\omega}a$, a pure rescaling of the flat background, exactly when the trace-free part $\mathcal{W}$ of the field strength vanishes. Imported from Weyl (1918).

## lay
In four or more dimensions, a gravitational field on flat spacetime amounts locally to nothing more than a change of scale exactly when one particular part of its strength, the Weyl curvature, is zero. This classical result is imported.

## one-liner
In dimension at least four a gravitational field on flat spacetime is locally a pure rescaling, $\hb^{-1}(a) = e^{\omega}a$ in some gauge, if and only if its Weyl curvature vanishes (Weyl 1918).
