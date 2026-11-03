---
id: obj.transport.null-lift-completion
kind: object
version: 1
title: Null-lift completion
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
locators:
  paper: T01
  number: Def 4.12
  label: def:nulllift
  line: 915
extraction:
  env: definition
  typing:
    by: ai-typing-pass
    note: "Definition; levels explain it, stressing that no regularity of the map is assumed."
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [transport.minimality, rungs.imported-totality-minimality-completion, one-relation.imported-completion-ladder, transport.transport-algorithm, obj.transport.normalised-conformal-chart]
    added_about: []
    verdict: connected
    note: 'Linked by about from the minimality theorem and the two later Facts that restate it, whose statements quantify over null-lift completions, and from the algorithm step that cites the class; a definition has no premises.'
---

## formal
A \emph{null-lift completion} of the nondegenerate quadratic space $(\mathbb{V}, Q)$ is a pair $(\mathbb{W}, f)$ where $\mathbb{W}$ is a nondegenerate real quadratic space adjoined orthogonally to $\mathbb{V}$ and $f : \mathbb{V} \to \mathbb{W}$ is a map with $f(0) \neq 0$ such that
\[
X(x) \;=\; f(x) + x \ \in\ \mathbb{W} \perp \mathbb{V}
\]
is null for every $x \in \mathbb{V}$. The condition $f(0) \neq 0$ says only that the origin, like every point, is represented by a nonzero vector, hence by a ray. Nothing else is assumed of $f$: not linearity, not continuity, not injectivity.

## technical
A null-lift completion of a nondegenerate quadratic space $(\mathbb{V}, Q)$ is a pair $(\mathbb{W}, f)$, where $\mathbb{W}$ is a nondegenerate real quadratic space adjoined orthogonally to $\mathbb{V}$ and $f: \mathbb{V} \to \mathbb{W}$ is a map with $f(0) \neq 0$, such that $X(x) = f(x) + x \in \mathbb{W} \perp \mathbb{V}$ is null for every $x \in \mathbb{V}$.

The condition $f(0) \neq 0$ says that the origin, like every other point, is represented by a nonzero vector and hence by a ray. Nothing else is assumed of $f$: not linearity, continuity or injectivity.

## lay
A null-lift completion adds extra perpendicular directions to a space and attaches to each point a vector in those new directions, chosen so that the combined vector has zero length. Every point, the origin included, then becomes a light-like ray. The rule that attaches the extra vector can be any function at all.

## one-liner
A null-lift completion of a nondegenerate quadratic space adjoins an orthogonal nondegenerate space $\mathbb{W}$ and an arbitrary map $f$ with $f(0) \neq 0$ such that $f(x) + x$ is null for every $x$.
