---
id: obj.transport.normalised-conformal-chart
kind: object
version: 2
title: Normalised conformal chart
status: defined
region: transport
subject: completion
tags: [conformal-model]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
review: typed
about:
- obj.transport.null-lift-completion
locators:
  paper: T01
  number: Def 4.17
  label: def:chart
  line: 967
extraction:
  env: definition
  eqrefs: 1
  typing:
    by: ai-typing-pass
    note: "Definition; levels explain the metric-faithfulness identity and that no regularity is assumed."
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [transport.representation-independent-minimality-completion, angle.imported-conformal-model-null-rotations]
    added_about: [obj.transport.null-lift-completion]
    verdict: connected
    note: 'About from the chart-minimality theorem (its hypothesis is a normalised conformal chart) and from the angle note Fact that states the chart identity; the definition itself names the lift of the null-lift completion.'
---

## formal
Let $(\mathbb{V}'', Q'')$ be a nondegenerate real quadratic space. A \emph{normalised conformal chart} of $(\mathbb{V}, Q)$ in $\mathbb{V}''$ is a map $\Phi : \mathbb{V} \to \mathbb{V}''$ with
\[
\Phi(x) \cdot \Phi(y) \;=\; -\tfrac12\, Q(x - y) \qquad \text{for all } x, y \in \mathbb{V}
\]
(in particular every $\Phi(x)$ is null, and $\Phi$ is injective by nondegeneracy). This is exactly the metric-faithfulness identity \eqref{eq:nullity} of the conformal model; the lift $X$ of the completion is a normalised conformal chart, and any projective chart with a nowhere-vanishing scale is rescaled into this form. Nothing else is assumed of $\Phi$: not linearity, not continuity.

## technical
Let $(\mathbb{V}'', Q'')$ be a nondegenerate real quadratic space. A normalised conformal chart of $(\mathbb{V}, Q)$ in it is any map $\Phi: \mathbb{V} \to \mathbb{V}''$ with $\Phi(x)\cdot\Phi(y) = -\tfrac12 Q(x-y)$ for all $x, y$.

Taking $x = y$ shows that every $\Phi(x)$ is null, and nondegeneracy makes $\Phi$ injective. Neither linearity nor continuity is assumed. The lift of the conformal completion is such a chart, and any projective chart with a nowhere-vanishing scale can be rescaled into this form.

## lay
A normalised conformal chart places each point of a space on a light-like vector in a larger space, so that the inner product of the images of two points gives, up to a fixed factor, the squared separation of the points. Nothing else is required of the map. The usual conformal model of geometry is one such chart.

## one-liner
A normalised conformal chart is any map into a nondegenerate quadratic space with $\Phi(x)\cdot\Phi(y) = -\tfrac12 Q(x-y)$, so it sends points to null vectors whose inner products record squared separations.
