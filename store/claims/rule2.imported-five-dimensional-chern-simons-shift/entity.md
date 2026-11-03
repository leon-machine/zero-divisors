---
id: rule2.imported-five-dimensional-chern-simons-shift
kind: claim
version: 1
title: 'Imported: the five-dimensional Chern-Simons shift'
status: imported
region: rule2
subject: completion
tags: [hypercharge-and-anomalies, classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T17-rule2, the series'' standard disclaimer'
review: typed
imported_from:
- citation: E. Witten, Phase transitions in M-theory and F-theory, Nucl. Phys. B 471 (1996) 195--216.
  key: Witten1996
- citation: K. Intriligator, D. R. Morrison, N. Seiberg, Five-dimensional supersymmetric gauge theories
    and degenerations of Calabi-Yau spaces, Nucl. Phys. B 497 (1997) 56--100.
  key: IMS1997
locators:
  paper: T17-rule2
  number: Fact 3.3
  label: fact:CS5
  line: 217
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: 'Imported physics result; levels describe the cited effective-action statement only. Levels
      pass: conditions already kept.'
---

## formal
A five-dimensional Dirac fermion of mass $m$ charged under a gauge field, integrated out, shifts the coefficient of the five-dimensional Chern-Simons term by $\tfrac12\sgn(m)$ (times the representation's cubic index for a non-abelian field); the sign is odd under the reflection of one spatial direction, so that the parity-violating term is present for a single species and absent for a pair whose contributions cancel. \emph{Provenance:} \cite{Witten1996, IMS1997}.

## technical
Integrating out a five-dimensional Dirac fermion of mass $m$ charged under a gauge field shifts the coefficient of the five-dimensional Chern-Simons term by $\tfrac12\sgn(m)$, times the cubic index of the representation for a non-abelian field.

The sign is odd under the reflection of one spatial direction, so the parity-violating term is present for a single species and absent for a pair whose contributions cancel. This is a standard result of five-dimensional gauge theory.

## lay
In five-dimensional theories, removing a heavy charged fermion from the description leaves behind a particular term for the gauge field, whose sign follows the sign of the fermion's mass. That term is not symmetric under mirror reflection, so a single such fermion breaks parity. A pair whose contributions cancel does not.

## one-liner
Integrating out a massive five-dimensional Dirac fermion shifts the Chern-Simons coefficient by $\tfrac12\sgn(m)$, a parity-odd term present for one species and absent for a cancelling pair.
