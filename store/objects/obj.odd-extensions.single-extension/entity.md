---
id: obj.odd-extensions.single-extension
kind: object
version: 1
title: Single extension
status: defined
region: odd-extensions
subject: tower
tags: [towers-by-residue]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
review: typed
locators:
  paper: T14a
  number: Def 2.1
  label: def:single
  line: 429
extraction:
  env: definition
  context_refs:
  - transport.transport-algorithm
  typing:
    by: ai-typing-pass
    note: Definition; levels only.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - odd-extensions.four-extensions-oriented-pair
    - odd-extensions.doubling-or-complexification
    - odd-extensions.mirror-inside-complexified-extension-absent-doubled
    - odd-extensions.four-extensions-are-four-odd-towers
    - odd-extensions.copy-theorems-blind-spot
    - odd-extensions.are-ascents-pair-signed
    added_about: []
    verdict: connected
    note: 'A definition cannot carry uses or assumes; the added links are about edges from the claims whose
      statements use the defined notion. Here: the results stated on time and space extensions, the shadow
      and its volume element.'
---

## formal
The \emph{time extension} of $\Cl(p,q)$ is $\Cl(p+1, q)$ and its \emph{space extension} is $\Cl(p, q+1)$, each with the new generator written $e_{n+1}$ and the old generators, and the subalgebra they generate, called the \emph{shadow}. A single extension is not a transport in the series' sense: the transport adjoins a null pair $e_{+} + e_{-}$ because a zero divisor of vector type is resolved by a nilpotent, and a single generator squaring to $\pm 1$ supplies none \cite[\S 8]{ButlerT1}.

## technical
Given $\Cl(p,q)$, its time extension is $\Cl(p+1,q)$ and its space extension is $\Cl(p,q+1)$: one new generator $e_{n+1}$ is adjoined, and the old generators, together with the subalgebra they generate, are called the shadow.

A single extension is not a transport in the series' sense. The transport adjoins a null pair built from $e_+$ and $e_-$, because a zero divisor of vector type is resolved by a nilpotent, and a single generator with $Q(e_{n+1}) = \pm 1$ supplies none.

## lay
A single extension adds just one new direction to an algebra of directions, either of time type or of space type, and the original algebra survives inside it as its shadow. This differs from the series' basic completion step, which adds two directions at once so as to supply a direction of zero length. One new direction on its own cannot do that.

## one-liner
A single extension adjoins one generator to $\Cl(p,q)$, giving the time extension $\Cl(p+1,q)$ or the space extension $\Cl(p,q+1)$ over the original shadow, and is not a transport because it supplies no nilpotent.
