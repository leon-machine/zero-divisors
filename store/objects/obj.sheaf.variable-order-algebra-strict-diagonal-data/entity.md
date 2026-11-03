---
id: obj.sheaf.variable-order-algebra-strict-diagonal-data
kind: object
version: 1
title: Variable-order algebra; strict diagonal data
status: defined
region: sheaf
subject: walls
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
  source: authorship disclosure of T04, deposited version
review: typed
locators:
  paper: T04
  number: Def 9.1
  label: def:varorder
  line: 1176
extraction:
  env: definition
  context_refs:
  - sheaf.kasner-data-interior
  typing:
    by: ai-typing-pass
    note: "Object: levels only."
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [sheaf.variable-weight-boundary-tameness-completion-forced, sheaf.stability-reduction-strict-diagonal-case, sheaf.log-obstruction, sheaf.differential-closure-filtration-conormality, obj.sheaf.relatively-admissible-perturbation]
    added_about: []
    verdict: connected
    note: 'About from every Section 9 statement written over the algebra A or strict diagonal data; the collision census concerns the Kasner constraint variety only and was not linked.'
---

## formal
Let $E$ be a smooth $3$-manifold and $\Mt = [0,\varepsilon)_\tau \times E$. An \emph{admissible exponent family} is a countable family $\{e_j\}$ of smooth nonnegative functions on $E$ such that, on each compact $K \subseteq E$ and for each level $N$, only finitely many $e_j$ have $\inf_K e_j \leq N$. The \emph{variable-order algebra} $\mathcal{A}$ is the algebra of sums $\sum_j f_j(x,\tau)\,\tau^{e_j(x)}$ over admissible exponent families, with $f_j$ smooth up to $\tau = 0$; on each compact and each interval $[0, \tau_0]$, the terms below any level are finitely many and the remainder is $O(\tau^{N})$ locally uniformly, so the sums converge locally uniformly and the class is closed under products (exponent families add, and the sum family is again admissible). Two conventions: an element is identified with the function it defines, and the representation-sensitive notions used later (exponent sets, log degree) rest on the non-membership statements of Section \ref{subsec:smoothstructure}, which are proved for exactly this class. \emph{Strict diagonal data} on $\Mt$ is a local coframe $(d\tau, \sigma^1, \sigma^2, \sigma^3)$ and a cometric whose Gram in it is
\[
\operatorname{diag}\bigl(1,\ -\tau^{-2p_1(x)}c_1,\ -\tau^{-2p_2(x)}c_2,\ -\tau^{-2p_3(x)}c_3\bigr),
\]
with $p_i$ smooth, $p_1 < 0 < p_2 \leq p_3$ pointwise, and $c_i(x,\tau)$ smooth and positive up to $\tau = 0$. The Kasner constraints are \emph{not} hypotheses of anything in this section: the sheaf theory is kinematic, and the constraints enter only through the Einstein-flow provenance of Fact \claimref{sheaf.kasner-data-interior}.

## technical
On $\Mt = [0,\varepsilon)_\tau \times E$, with $E$ a smooth $3$-manifold, an admissible exponent family is a countable family of smooth nonnegative functions $e_j$ on $E$ with only finitely many below any level on each compact. The variable-order algebra $\mathcal{A}$ consists of the sums $\sum_j f_j(x,\tau)\,\tau^{e_j(x)}$ with $f_j$ smooth up to $\tau = 0$; these converge locally uniformly and the class is closed under products, since exponent families add.

Strict diagonal data are a local coframe $(d\tau, \sigma^1, \sigma^2, \sigma^3)$ and a cometric with Gram $\operatorname{diag}(1, -\tau^{-2p_1(x)}c_1, -\tau^{-2p_2(x)}c_2, -\tau^{-2p_3(x)}c_3)$, where the $p_i$ are smooth with $p_1 < 0 < p_2 \leq p_3$ and the $c_i$ are smooth and positive up to $\tau = 0$. The Kasner constraints are not assumed: the theory is kinematic.

## lay
Near a singularity, geometric quantities often behave like powers of the time remaining, with exponents that change from place to place. The variable-order algebra is the class of functions built from such powers, restricted enough that they can be added, multiplied and summed reliably. Strict diagonal data describe, in this language, a geometry whose three spatial directions scale with their own powers of time, one exponent negative and two positive, allowed to vary across space.

## one-liner
The variable-order algebra $\mathcal{A}$ consists of locally finite sums $\sum_j f_j\,\tau^{e_j(x)}$ with smooth coefficients, and strict diagonal data are a cometric with Gram $\operatorname{diag}(1, -\tau^{-2p_i(x)}c_i)$, $p_1 < 0 < p_2 \leq p_3$.
