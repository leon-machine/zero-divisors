---
id: rule2.imported-parity-anomaly
kind: claim
version: 1
title: 'Imported: the parity anomaly'
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
- citation: A. J. Niemi, G. W. Semenoff, Axial-anomaly-induced fermion fractionization and effective gauge-theory
    actions in odd-dimensional space-times, Phys. Rev. Lett. 51 (1983) 2077--2080.
  key: NiemiSemenoff1983
- citation: A. N. Redlich, Gauge noninvariance and parity nonconservation of three-dimensional fermions,
    Phys. Rev. Lett. 52 (1984) 18--21; Parity violation and gauge noninvariance of the effective gauge
    field action in three dimensions, Phys. Rev. D 29 (1984) 2366--2374.
  key: Redlich1984
- citation: L. Alvarez-Gaum'e, E. Witten, Gravitational anomalies, Nucl. Phys. B 234 (1984) 269--330.
  key: AGW1984
locators:
  paper: T17-rule2
  number: Fact 4.1
  label: fact:parity
  line: 237
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: 'Imported physics result; levels describe the cited parity-anomaly statement only. Levels pass:
      conditions already kept.'
---

## formal
A single two-component Dirac fermion of mass $m$ in $2{+}1$ dimensions, coupled to a $U(1)$ gauge field, has an effective action containing a Chern-Simons term at level $\tfrac12\sgn(m)$ up to a sign that flips between the two inequivalent two-component representations; the term is odd under the reflection of one spatial axis, so a single species breaks parity, while two species, one in each representation with equal mass (equivalently the four-component fermion with its parity-invariant mass term), induce no net Chern-Simons term. \emph{Provenance:} \cite{NiemiSemenoff1983, Redlich1984, AGW1984}.

## technical
A single two-component Dirac fermion of mass $m$ in $2+1$ dimensions, coupled to a $U(1)$ gauge field, has an effective action with a Chern-Simons term at level $\tfrac12\sgn(m)$, up to a sign that flips between the two inequivalent two-component representations.

The term is odd under the reflection of one spatial axis, so a single species breaks parity, while two species of equal mass, one in each representation (equivalently the four-component fermion with its parity-invariant mass term), induce no net Chern-Simons term.

## lay
In a flat two-dimensional world plus time, a single charged massive fermion leaves behind a term in the electromagnetic response that is not mirror-symmetric, so it breaks parity. Such fermions come in two mirror-image versions, which give this term with opposite signs. Taking one of each, with equal mass, cancels the effect.

## one-liner
A single massive two-component Dirac fermion in $2+1$ dimensions induces a parity-odd Chern-Simons term at level $\tfrac12\sgn(m)$, which cancels for an equal-mass pair in the two inequivalent representations.
