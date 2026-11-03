---
id: note.interior.setting-flat-model-dictionary
kind: note
version: 2
title: The flat-model dictionary
status: setting
subject: einstein
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
comments_on:
- interior.stabilisers-flat-model
locators:
  paper: T06
  number: Setting
  section: 'Part two: the vacuum equations as a parallel ideal point'
  line: 465
  subsection: The flat-model dictionary
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
---

## formal
The interpretive content of the theorems below lies in the flat model, so we set it out completely; every statement here is proved, and the verification script checks each numerically in exact arithmetic. Let $V := \R^{2,4}$ with a quadratic form of signature $(2,4)$ written, in a scale, as $Q(\sigma,\mu,\rho) = \eta(\mu,\mu) + 2\sigma\rho$ with $\eta$ the Minkowski form. Points of conformal Minkowski space are null rays of $V$: the embedding is
\begin{equation}
X(x) \;=\; \bigl(1,\; x,\; -\tfrac12\,Q(x)\bigr), \qquad
\ip{X(x)}{X(y)} = -\tfrac12\,\eta(x - y,\, x - y),
\end{equation}
so $X(x)$ is null for every $x$ and the form recovers the flat conformal structure; the ideal point (``infinity'') is the null ray $\nInf := (0, 0, 1)$: the null rays with $\sigma \neq 0$ are exactly the points \eqref{eq:flatembed}, while $\{\sigma = 0,\ \eta(\mu,\mu) = 0\}$ is the light cone at infinity, a further three-parameter family of null rays, and $\nInf$ is its vertex: the unique null ray with $\sigma = 0$ and vanishing $\mu$-component. For a bivector $u \wedge v \in \Lambda^2 V \cong \mathfrak{so}(2,4)$ the action on vectors is
\begin{equation}
(u \wedge v)(w) \;=\; \ip{v}{w}\,u - \ip{u}{w}\,v ,
\end{equation}
which is the commutator action $\tfrac12[u\wedge v,\, w]$ of the corresponding bivector of $\Cl(2,4)$ under the identification of $\Lambda^2 V$ with the bivectors.

## technical
pending

## lay
pending

## one-liner
pending
