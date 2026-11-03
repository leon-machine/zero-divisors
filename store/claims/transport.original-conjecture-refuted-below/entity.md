---
id: transport.original-conjecture-refuted-below
kind: claim
version: 2
title: The original conjecture, refuted below
status: refuted
refuted_by:
- transport.no-go-level-elements
region: transport
subject: zero-divisors
tags: [refutation, null-directions]
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
- obj.transport.equivariance
locators:
  paper: T01
  number: Conj 4.1
  label: conj:original
  line: 678
  refutation_row: 1
extraction:
  env: conjecture
  typing:
    by: ai-typing-pass
    note: the paper states this conjecture in order to refute it; refuted by the element-level no-go (T01
      Thm 4.2)
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: []
    added_about: [obj.transport.equivariance]
    verdict: standalone
    note: 'A conjecture the paper states in order to refute it: it hangs from refuted_by the element-level no-go, and nothing may rest on it; about added to the equivariance it concerns.'
---

## formal
Division by zero promotes the element. For every null vector $v$ of $\Cl(p,q)$ there is, in the minimal ascent $\Cl(p{+}1,q{+}1)$, a canonically chosen partner $\sigma(v)$ satisfying $v\,\sigma(v)\,v = v$, the choice equivariant under the symmetries of the original algebra: the impossible division is repaired, element by element, one ascent up.

## technical
For every null vector $v$ of $\Cl(p,q)$ one could hope for a partner $\sigma(v)$ in the minimal ascent $\Cl(p{+}1,q{+}1)$ with $v\,\sigma(v)\,v = v$, chosen equivariantly under the symmetries of the original algebra, so that the failed division is repaired element by element. The paper states this to refute it: no equivariant element-level partner exists, and the repair happens at the level of points instead.

## lay
The first guess was that a vector you cannot divide by could be given a partner in a slightly larger algebra, one vector at a time, in a way that respects all the symmetries. That guess is wrong, and the series records it as refuted: the repair works for points of the geometry, not for individual elements.

## one-liner
Element-by-element repair of a null vector by an equivariant partner one ascent up: refuted.
