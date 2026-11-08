---
id: transport.no-fourth-rule
kind: claim
version: 4
title: No fourth rule
status: proved
region: transport
subject: completion
tags: [transport-algorithm, obstruction-types, classification]
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
- obj.transport.equivariance
derivations:
- name: main
  proof: proof-main.tex
  uses:
  - transport.embedding-independent-minimality-fusion@4
  - transport.exhaustiveness-every-zero-divisor-annihilated-idempotent@4
  - transport.minimality@5
  - transport.no-go-level-elements@5
  - transport.one-generator-minimal-minimal-completions-classified@6
  - transport.representation-independent-minimality-completion@4
  - transport.rule-2-ideal-fusion-sharp-form@4
  - transport.totality@3
  - transport.type-p-self-repairing@2
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_type_sites_by_signature
- kind: check
  ref: check.py::check_exhaustiveness_on_lattice
- kind: check
  ref: check.py::check_each_rule_repairs_its_type
locators:
  paper: T01
  number: Cor 6.7
  label: cor:norule
  line: 1418
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: where types C, N and P occur for n <= 6, exhaustiveness on a full coefficient lattice in dimension <= 2 with annihilating idempotents, and each rule repairing its type. Version 2 -> 3. Check strengthened: v null asserted (type N), e^2 = e for the type P idempotents, type P case count pinned at 2; samples moved to module level. Version 3 -> 4.'
  env: corollary
  flags:
  - no proof environment found
  repair:
    notes:
    - 'proof text supplied in the store (the source has none): the derivation is the theorems cited in
      the statement'
  typing:
    by: ai-typing-pass
    note: 'Kept all nine cited theorems: the corollary has no separate proof and is the conjunction of
      the results its statement names. Levels pass: the lay level now restricts the claim to nondegenerate
      real Clifford algebras, as the formal does.'
---

## formal
The taxonomy of Definition \claimref{obj.transport.obstruction-types} is transport-complete with two nontrivial rules. Type N: ascend by one hyperbolic plane, with the repair delivered at the level of points (Theorems \claimref{transport.no-go-level-elements}, \claimref{transport.totality}, \claimref{transport.minimality}, \claimref{transport.representation-independent-minimality-completion}). Type C: ascend by one generator, with the fused algebra unique up to isomorphism (Theorems \claimref{transport.rule-2-ideal-fusion-sharp-form}, \claimref{transport.one-generator-minimal-minimal-completions-classified}, \claimref{transport.embedding-independent-minimality-fusion}). Type P: no ascent; the identity is an equivariant repair (Proposition \claimref{transport.type-p-self-repairing}). By the exhaustiveness theorem (Theorem \claimref{transport.exhaustiveness-every-zero-divisor-annihilated-idempotent}), every zero divisor of a nondegenerate real Clifford algebra falls under these three rules.

## technical
The obstruction taxonomy is transport-complete with two nontrivial rules. Type N, a null vector with $Q(v) = 0$, is handled by ascending one hyperbolic plane, with the repair delivered at the level of points, as the no-go, totality and the two minimality theorems establish. Type C, a central idempotent, is handled by ascending one generator, with the fused algebra unique up to isomorphism and minimal. Type P, a non-central idempotent, needs no ascent: the identity is an equivariant repair.

By the exhaustiveness theorem every zero divisor of a nondegenerate real Clifford algebra falls under one of these three rules, so no fourth rule is needed.

## lay
Division can fail in a nondegenerate real Clifford algebra in exactly three ways, and each has its own prescribed fix: add a pair of dimensions, add one dimension, or do nothing. Since every failure of division is one of the three, the list of fixes is complete.

## one-liner
Every zero divisor of a nondegenerate real Clifford algebra is of type N, C or P, handled respectively by a hyperbolic-plane ascent, a one-generator ascent, or no ascent, so there is no fourth rule.
