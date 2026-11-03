---
id: transport.totality
kind: claim
version: 3
title: Totality
status: proved
region: transport
subject: completion
tags: [transport-algorithm, conformal-model, forcing-and-uniqueness]
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
derivations:
- name: main
  uses:
  - transport.density@3
  - std-algebra.reflection@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_iota_well_defined_total_involution
- kind: check
  ref: check.py::check_reciprocal_on_invertible_vectors
- kind: check
  ref: check.py::check_null_points_go_to_ideal_points_continuously
locators:
  paper: T01
  number: Thm 4.10
  label: thm:totality
  line: 886
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.reflection where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: e+ conjugation total and involutive on null vectors, the reciprocal on invertible vectors, and ideal-point values with the polynomial limit, five base signatures. Version 1 -> 2.'
  env: theorem
  eqrefs: 5
  typing:
    by: ai-typing-pass
    note: 'Kept the single premise, density, used for uniqueness; the paper says this theorem reproduces the classical resolution of 1/0 by conformal compactification, but no imported claim for that result is in the store, so no standard-route derivation was added.'
about:
- obj.std-algebra.conformal-algebra
---

## formal
Let $(\mathbb{V}, Q)$ be nondegenerate, with the completion $\Cl(p{+}1,q{+}1)$ and quadric $\mathcal{Q}$ of Section \ref{sec:model}. Define $\iota : \mathcal{Q} \to \mathcal{Q}$ by $\iota[N] = [\,e_+ N e_+\,]$. Then:
\begin{enumerate}
\item $\iota$ is well defined, total and continuous on $\mathcal{Q}$, and an involution.
\item For every $x$ with $Q(x) \neq 0$, \; $\iota[X(x)] = [X(x/Q(x))]$: on invertible vectors $\iota$ is the geometric reciprocal $\rho$.
\item For every $x_0$ with $Q(x_0) = 0$, that is, a null vector or the origin, $\iota[X(x_0)] = [\, x_0 + \tfrac12 \nInf \,]$, an ideal point (for $x_0 = 0$, the classical point at infinity $[\nInf]$), and this value is the limit of $\iota[X(x)]$ along every path of invertible $x \to x_0$. Consequently $\iota$ is the unique continuous map $\mathcal{Q} \to \mathcal{Q}$ agreeing with the lifted reciprocal $[X(x)] \mapsto [X(\rho(x))]$ on the lifted invertible locus.
\end{enumerate}

## technical
Let $(\mathbb{V}, Q)$ be nondegenerate, with completion $\Cl(p{+}1,q{+}1)$ and quadric $\mathcal{Q}$ of null rays, and define $\iota[N] = [\, e_+ N e_+ \,]$. Then $\iota$ is well defined, total, continuous and an involution on $\mathcal{Q}$, and for $Q(x) \neq 0$ it is the geometric reciprocal: $\iota[X(x)] = [X(x/Q(x))]$.

For $Q(x_0) = 0$, a null vector or the origin, $\iota[X(x_0)] = [\, x_0 + \frac12 \nInf \,]$, an ideal point ($[\nInf]$ when $x_0 = 0$), and this value is the limit of $\iota[X(x)]$ along every path of invertible $x \to x_0$. Consequently $\iota$ is the unique continuous map of $\mathcal{Q}$ that agrees with the lifted reciprocal on the lifted invertible locus.

## lay
In a Clifford algebra with vectors of zero length, the reciprocal of a vector is undefined on exactly those vectors. After moving to the enlarged space of points, a single reflection-like operation gives a reciprocal everywhere: it agrees with the usual one on ordinary vectors and sends zero-length vectors to points at infinity. Those values are the limits one would expect, and no other continuous rule matches the usual reciprocal.

## one-liner
On the quadric of the completion, $\iota[N] = [e_+ N e_+]$ is a total continuous involution that equals the reciprocal $x \mapsto x/Q(x)$ on invertible vectors and sends each $x_0$ with $Q(x_0) = 0$ to $[x_0 + \frac12 \nInf]$, and it is the only such continuous extension.
