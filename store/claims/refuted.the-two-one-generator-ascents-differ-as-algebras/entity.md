---
id: refuted.the-two-one-generator-ascents-differ-as-algebras
kind: claim
version: 2
title: The two one-generator ascents differ as algebras
status: refuted
subject: completion
tags: [refutation, transport-algorithm, obstruction-types]
region: programme
refuted_by:
- transport.one-generator-minimal-minimal-completions-classified
proposed_by:
  kind: extraction
  session: full-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T17, deposited version
review: typed
about:
- obj.transport.transport
- obj.transport.obstruction-types
locators:
  paper: T17
  number: refutation 2
  label: tab:refutations
  carried_by: T1
extraction:
  env: table row
  source: T17 tab:refutations
  typing:
    by: ai-typing-pass
    note: "Refuted conjecture with no edges; replaced the mechanical technical text with a fuller statement of the correction, keeping its content."
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: []
    added_about: [obj.transport.transport, obj.transport.obstruction-types]
    verdict: standalone
    note: 'Refuted table row: hangs from refuted_by the one-generator classification; about added to the transport definition, whose type-C clause needs the two ascents to agree as algebras, and to the obstruction types.'
---

## formal
The two one-generator ascents differ as algebras

## technical
Refuted. The conjecture was that the two one-generator ascents of a type-C algebra, adjoining $\nu$ with $Q(\nu) = +1$ or with $Q(\nu) = -1$, are non-isomorphic algebras. The corrected statement is that the two ascents are always isomorphic as algebras; the sign of $Q(\nu)$ is a geometric bit that the algebra forgets.

## lay
It was once conjectured that the two ways of adding a single new direction, with positive or with negative square, give genuinely different algebras. This is false. The two algebras are the same, and only the geometry remembers which sign was used.

## one-liner
Refuted: the two one-generator ascents are always isomorphic as algebras, the sign of the adjoined generator being a geometric bit the algebra forgets.
