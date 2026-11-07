---
id: standard-model.imported-norm-frozen-point-not-field
kind: claim
version: 5
title: 'Imported: the norm of the frozen point is not a field'
status: proved
region: standard-model
subject: dark-energy
tags: [frozen-point, cosmological-constant]
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
derivations:
- name: main
  uses:
  - dark-energy.point-infinity-has-no-physical-fluctuation@4
  - dark-energy.imported-frozen-point-geometry@7
  - interior.covariant-form-vacuum-equations@5
  - interior.scale-tractor-leaves-cone@8
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_unitary_gauge_exists_and_is_complete
- kind: check
  ref: check.py::check_stabiliser_is_lorentz_of_the_complement
locators:
  paper: T12
  number: Fact 2.10
  label: fact:rigidity
  line: 915
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (second round): dark-energy.imported-frozen-point-geometry repinned 6 -> 7 after reviewing its restatement (the sentence naming the tractor gauge-field theorem moved to a text-only remark); the parts cited here (parallel frozen point, Q(I) = Lambda/3, the stabilisers, the scale-g display and the Schouten tensor) are unchanged, and the use here holds as cited.'
  maintainer_pass_premise:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: The covariant constancy of the frozen point on the Einstein region is cited from the frozen-point geometry Fact directly, not through the registration result, whose clause (iii) now assumes the field-space premise; no change of content. Version 4 -> 5.
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the unitary-gauge core in Cl(2,4) at three Lam and three events, the 15 bivectors acting onto the 9-dimensional constrained fluctuation space of (I, V), with stabiliser so(1,3) of the (1,3) complement and image of rank 5 on I alone. Version 3 -> 4.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: fact
  context_refs:
  - dark-energy.point-infinity-has-no-physical-fluctuation
  - dark-energy.imported-frozen-point-geometry
  - interior.covariant-form-vacuum-equations
  - interior.scale-tractor-leaves-cone
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'All four uses are the stated provenance (dark-energy Propositions 5.4 and 4.2(i), interior
      Theorems 4.5 and 4.7) and were kept. Levels pass: lay now keeps the three-argument form and says
      the action, not the theory, has no equation for Lambda.'
---

## formal
In the three-argument form of the gravitational action the frozen point enters subject to the Stelle-West constraint $Q(I) = \Lambda/3$, every fluctuation of the constrained pair $(I, V)$ is a gauge transformation (unitary gauge $\delta I = \delta V = 0$ exists and is complete), and the second variation of the action involves only the connection. The action therefore carries no equation of motion for $\Lambda$: the norm is fixed by a constraint, not evolved by a field equation. \emph{Provenance:} \cite[Prop.~5.4]{ButlerT10}; covariant constancy of the frozen point of norm $\Lambda/3$ is \cite[Prop.~4.2(i)]{ButlerT10} and \cite[Thms.~4.5, 4.7]{ButlerT6}.

## technical
In the three-argument form of the gravitational action the frozen point $I$ enters subject to the Stelle-West constraint $Q(I) = \Lambda/3$. Every fluctuation of the constrained pair $(I,V)$ is a gauge transformation, so the unitary gauge $\delta I = \delta V = 0$ exists and is complete, and the second variation of the action involves only the connection.

The action therefore carries no equation of motion for $\Lambda$: the norm is fixed by a constraint, not evolved by a field equation. The covariant constancy of the frozen point of norm $\Lambda/3$ is imported alongside from the dark-energy and black-hole interior papers.

## lay
In the three-argument form of the gravitational action, the cosmological constant is the fixed squared length of a reference vector. Any attempt to wiggle that vector turns out to be only a change of description, not a physical change. So the action contains no equation that could make the cosmological constant vary: it is held fixed by a constraint.

## one-liner
In the three-argument gravitational action the frozen point's norm $\Lambda/3$ is fixed by the Stelle-West constraint and its fluctuations are pure gauge, so the action has no equation of motion for $\Lambda$.
