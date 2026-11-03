---
id: standard-model.imported-invariant-forms-simple-lie-algebra
kind: claim
version: 1
title: 'Imported: invariant forms on a simple Lie algebra'
status: imported
region: standard-model
subject: standard-model
tags: [classical-theorem, representation-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
imported_from:
- citation: 'W. Fulton and J. Harris, Representation Theory: A First Course, Graduate Texts in Mathematics
    129, Springer (1991).'
  key: FultonHarris1991
  locator: Ch.~14, App.~C
locators:
  paper: T12
  number: Fact 8.3
  label: fact:killing
  line: 1290
extraction:
  env: fact
  context_refs:
  - standard-model.imported-one-loop-running-trace-ratio
  typing:
    by: ai-typing-pass
    note: Imported fact; levels only, no edges to review.
---

## formal
A simple complex Lie algebra carries, up to a scalar, exactly one invariant symmetric bilinear form; for any finite-dimensional representation $\rho$ the form $(X, Y) \mapsto \tr(\rho(X)\rho(Y))$ is invariant, hence a multiple $c_{\rho}$ of the Killing form, with $c_{\rho} > 0$ on a compact real form for $\rho$ nontrivial. \emph{Provenance:} \cite[Ch.~14, App.~C]{FultonHarris1991}; this is the clause Fact \claimref{standard-model.imported-one-loop-running-trace-ratio}(b) invokes to fix the normalisation.

## technical
A simple complex Lie algebra carries, up to a scalar, exactly one invariant symmetric bilinear form. Hence for any finite-dimensional representation $\rho$ the trace form $(X, Y) \mapsto \tr(\rho(X)\rho(Y))$ is a multiple $c_{\rho}$ of the Killing form, with $c_{\rho} > 0$ on a compact real form when $\rho$ is nontrivial. This uniqueness is what fixes the normalisation of the couplings inside a simple unifying group. The result is imported from standard Lie theory.

## lay
On a simple symmetry algebra there is essentially only one natural way to measure the size of its elements, up to an overall scale. Any representation of the algebra produces such a measure by taking traces, so all of them agree up to a positive factor. This is what fixes the relative normalisation of force strengths when the forces sit inside one simple group. It is a standard result taken from the literature.

## one-liner
A simple Lie algebra carries a unique invariant symmetric form up to scale, so every trace form $\tr(\rho(X)\rho(Y))$ is a multiple of the Killing form, positive on a compact form for nontrivial $\rho$.
