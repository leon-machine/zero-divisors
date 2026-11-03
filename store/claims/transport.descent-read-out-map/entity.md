---
id: transport.descent-read-out-map
kind: claim
version: 2
title: 'Descent: the read-out map'
status: proved
region: transport
subject: completion
tags: [conformal-model, descent-map]
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
  - transport.totality@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_descent_inverts_the_lift
- kind: check
  ref: check.py::check_descent_of_transported_point_is_reciprocal
- kind: check
  ref: check.py::check_composite_defined_exactly_off_the_null_cone
locators:
  paper: T01
  number: Lem 4.23
  label: lem:descent
  line: 1035
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: dsc well defined and inverse to the lift, dsc(iota X(x)) = x/Q(x), and the composite defined exactly off the null cone. Version 1 -> 2.'
  env: lemma
  eqrefs: 1
  typing:
    by: ai-typing-pass
    note: 'Kept the single premise, totality, used for clauses (2) and (3); the incidence condition the proof cites is an equation, not a store claim.'
---

## formal
Define $\dsc : \mathcal{Q} \setminus \{\text{ideal points}\} \to \mathbb{V}$ by
\[
\dsc\,[\, s\,\nO + x + t\,\nInf \,] \;=\; x/s .
\]
Then:
\begin{enumerate}
\item $\dsc$ is well defined and continuous, and it is inverse to the lift: $\dsc[X(x)] = x$ for every $x \in \mathbb{V}$, and $X(\dsc[N]) \in [N]$ for every non-ideal null ray $[N]$. Hence $x \mapsto [X(x)]$ and $\dsc$ are mutually inverse homeomorphisms between $\mathbb{V}$ and $\mathcal{Q} \setminus \{\text{ideal points}\}$.
\item On the invertible locus, descent returns the classical reciprocal: for every $x$ with $Q(x) \neq 0$,
\[
\dsc\bigl(\iota[X(x)]\bigr) \;=\; x/Q(x) \;=\; \rho(x).
\]
\item The composite $\dsc \circ \iota \circ [X(\cdot)]$ is defined exactly on $\{Q \neq 0\}$: for $Q(x_0) = 0$ the value $\iota[X(x_0)]$ is ideal by Theorem \claimref{transport.totality}(3) and lies outside the domain of $\dsc$. Descent is therefore partial precisely where the original reciprocal was, and necessarily so, since the ideal points are represented by no point of $\mathbb{V}$.
\end{enumerate}

## technical
The read-out $\dsc[\, s\,\nO + x + t\,\nInf \,] = x/s$ is defined on the quadric minus its ideal points, those with $s = 0$. It is well defined, continuous and inverse to the lift: $\dsc[X(x)] = x$, and $X(\dsc[N]) \in [N]$ for every non-ideal null ray, so the lift and $\dsc$ are mutually inverse homeomorphisms between $\mathbb{V}$ and the non-ideal part of $\mathcal{Q}$.

On the invertible locus, lifting, applying the transported reciprocal $\iota$ and reading out returns the classical reciprocal: $\dsc(\iota[X(x)]) = x/Q(x)$. The composite is defined exactly where $Q(x) \neq 0$; for $Q(x_0) = 0$, totality places $\iota[X(x_0)]$ at an ideal point, outside the domain of $\dsc$. Descent is therefore partial precisely where the original reciprocal was, and necessarily so, since ideal points are represented by no point of $\mathbb{V}$.

## lay
After computing in the enlarged space one needs a way back to the original one. The read-out map does this for every point not at infinity, and for ordinary invertible vectors it gives back the familiar reciprocal. For zero-length vectors the answer lies at infinity, and the read-out declines, because no point of the original space represents it.

## one-liner
The read-out $\dsc[s\,\nO + x + t\,\nInf] = x/s$ inverts the lift off the ideal points, returns $x/Q(x)$ after the transported reciprocal, and is undefined exactly where $Q(x) = 0$.
