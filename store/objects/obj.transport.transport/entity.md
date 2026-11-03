---
id: obj.transport.transport
kind: object
version: 2
title: Transport
status: defined
region: transport
subject: completion
tags: [transport-algorithm, obstruction-types]
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
- obj.transport.obstruction-types
locators:
  paper: T01
  number: Def 8.1
  label: def:transport
  line: 1564
extraction:
  env: definition
  context_refs:
  - transport.minimality
  - transport.rule-2-ideal-fusion-sharp-form
  - transport.totality
  eqrefs: 1
  typing:
    by: ai-typing-pass
    note: "Definition; levels name the three cases without claiming more than the definition."
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [transport.transport-algorithm, transport.transport-principle, transport.no-transport-terminates, transport.fusion-occurs-most-once, refuted.the-two-one-generator-ascents-differ-as-algebras]
    added_about: [obj.transport.obstruction-types]
    verdict: connected
    note: 'About from the principle and algorithm that the definition names and from the two transport-history results; the definition is stated case by case on the obstruction types.'
---

## formal
The \emph{transport} of a nondegenerate $(\mathbb{V}, Q)$ is the pair consisting of the minimal completion $\Cl(p{+}1,q{+}1)$ of Theorem \claimref{transport.minimality} and the null-ray representation \eqref{eq:lift}; the \emph{transported reciprocal} is the total involution $\iota$ of Theorem \claimref{transport.totality}. For a type-C obstruction the corresponding transport is the one-generator ascent of Theorem \claimref{transport.rule-2-ideal-fusion-sharp-form}; for type P it is the identity.

## technical
The transport of a nondegenerate $(\mathbb{V}, Q)$ of signature $(p,q)$ is the pair formed by the minimal completion $\Cl(p,q) \hookrightarrow \Cl(p+1,q+1)$ and the null-ray representation of points. The transported reciprocal is the total involution $\iota$ on null rays.

For a type-C obstruction the transport is instead the one-generator ascent of Rule 2, and for a type-P obstruction it is the identity.

## lay
Transport is the series' name for its standard way of handling a failure of division in a geometric algebra. In the basic case one adds a pair of directions and represents points as light-like rays, on which a reciprocal is defined everywhere. For one other kind of failure a single direction is added, and for a third kind nothing changes.

## one-liner
The transport of a nondegenerate quadratic space is its minimal completion $\Cl(p+1,q+1)$ with the null-ray representation and the total transported reciprocal, replaced by the one-generator ascent for type-C obstructions and by the identity for type P.
