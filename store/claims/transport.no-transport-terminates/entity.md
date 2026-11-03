---
id: transport.no-transport-terminates
kind: claim
version: 4
title: No transport terminates
status: proved
region: transport
subject: zero-divisors
tags: [transport-algorithm, obstruction-types, no-go]
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
- obj.transport.transport
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - transport.existence-locus-type-n@5
  - transport.matrix-units-peirce-isomorphism@3
  - transport.rule-2-ideal-fusion-sharp-form@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:7.8
- kind: check
  ref: check.py::check_rule_one_completion_carries_type_n
- kind: check
  ref: check.py::check_rule_two_completion_carries_type_p
- kind: check
  ref: check.py::check_no_completion_is_a_division_algebra
locators:
  paper: T01
  number: Prop 7.8
  label: prop:noterminate
  line: 1547
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Rule 1 completions of all 15 bases with n <= 4 have mixed signature and a null ladder pair with f f* + f* f = 1 and half-rank f; Rule 2 completions of the six type-C bases with n <= 5 have matrix units, a non-central idempotent, a nonzero nilpotent and a corner of dimension 2^(n-1). Version 2 -> 3. Check strengthened: Rule-1 left rank pinned at exactly half (was an inequality), f null and eps_+ idempotent asserted, Rule 2 run with both signs of nu^2; samples moved to module level. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'Edges kept: all three premises are invoked in the proof.'
---

## formal
No algebra reachable by a nonempty transport history is free of zero divisors. Every Rule-1 completion has mixed signature and so carries type N; indeed the adjoined pair $f, f^*$ is itself null: the repair of the old null cone is effected by adjoining new members of it. Every Rule-2 completion is a matrix algebra $\Mat_2(\Cl^0(p,q))$ and so carries type P: the fusion's own matrix units supply the non-central idempotents and nilpotents. Transport never reaches a division algebra; each completion carries fresh obstructions of its own.

## technical
No algebra reachable by a nonempty transport history is free of zero divisors. A Rule 1 completion adjoins a hyperbolic plane, so its signature $(p+1, q+1)$ is mixed and it carries type N; indeed the adjoined pair satisfies $Q(f) = Q(f^{*}) = 0$, so the old null cone is repaired by adjoining new members of it.

A Rule 2 completion is $\Mat_2(\Cl^0(p,q))$, whose matrix units supply the non-central idempotent $E_{11}$ and the nonzero nilpotent $E_{12}$, so it carries type P. Transport never reaches a division algebra.

## lay
Each repair in the transport programme enlarges the algebra to fix a failure of division. This result shows that the enlarged algebra always has failures of its own: one repair adds new light-like directions, the other produces projections and elements that square to zero. So the process never ends in an algebra where every nonzero element can be divided by.

## one-liner
Every algebra reached by at least one transport step has zero divisors, of type N after Rule 1 and of type P after Rule 2, so transport never reaches a division algebra.
