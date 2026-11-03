---
id: singularity.imported-descent-one-way-conditional-expectation
kind: claim
version: 7
title: 'Imported: the descent is a one-way conditional expectation'
status: proved
region: singularity
subject: descent
tags: [descent-map, no-go]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
derivations:
- name: main
  uses:
  - singularity.imported-descent-one-way-conditional-expectation-external@1
  - transport.door-one-way@5
  - transport.pinching-kernel@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_pinching_is_conditional_expectation
- kind: check
  ref: check.py::check_kernel_is_ladder_sector
- kind: check
  ref: check.py::check_no_return_homomorphism
- kind: check
  ref: check.py::check_trace_preserving_expectation_is_unique
locators:
  paper: T05
  number: Fact 5.9
  label: fact:oneway
  line: 1605
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the pinching as a conditional expectation with kernel the ladder sector (p+q <= 2), the block sizes of B (p+q <= 3), and uniqueness of the (trace-preserving) conditional expectation by an exact linear solve for p+q <= 1. Version 4 -> 5. Sample inputs moved to module level; no change to what is tested. Version 5 -> 6. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 6 -> 7.'
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'W503 was a false positive: the hyphenated word conditional-expectation in the provenance matched the condition pattern, though the result holds unconditionally; the hyphen is now a space and no level changed. Version 3 -> 4.'
  env: fact
  context_refs:
  - singularity.descent-parity-average
  - transport.door-one-way
  - transport.pinching-kernel
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    note: 'kept the T1 pinching-kernel and one-way-door results and the external Takesaki ingredient,
      which are the fact''s cited sources; the parity-average theorem is cited as an alternative route
      to uniqueness in the order-two case, not as a premise, so it was not added; removed the mechanical
      repair edge to the transport algorithm, which the fact does not use Levels pass: conditions already
      kept.'
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
---

## formal
$E$ is a conditional expectation onto the commutant of $P$, its kernel is exactly the adjoined ladder sector, and no unital algebra homomorphism from the completed algebra back to its base exists at all: ascent is two-way for what was lifted from the original space, one-way for what was built in the completion. It is moreover the unique conditional expectation onto that subalgebra preserving the trace. \emph{Provenance:} the conditional expectation property, the kernel and the non-existence of a return homomorphism are \cite[Prop.~7.5, Thm.~7.6]{ButlerT1}; the uniqueness of the trace-preserving conditional expectation onto a von Neumann subalgebra is Takesaki's theorem \cite{Takesaki1972}, and in the present order-two case it is also Theorem \claimref{singularity.descent-parity-average}.

## technical
The descent $E$ is a conditional expectation onto the commutant of the occupation projector $P$, and its kernel is exactly the adjoined ladder sector. No unital algebra homomorphism from the completed algebra back to its base exists at all: ascent is two-way for what was lifted from the original space and one-way for what was built in the completion.

Moreover $E$ is the unique trace-preserving conditional expectation onto that subalgebra. This is Takesaki's theorem on conditional expectations onto von Neumann subalgebras, and in the present order-two case it also follows from the identification of $E$ with the parity average.

## lay
Stepping down from the enlarged algebra to the original one is a well-behaved averaging projection that keeps the occupation data and discards exactly the newly added ladder sector. There is no way back: what was built only in the enlarged algebra cannot be returned to the original by any structure-preserving map. Among such projections that preserve the trace, it is the only one.

## one-liner
Imported: the descent is the unique trace-preserving conditional expectation onto the commutant of $P$, its kernel is the adjoined ladder sector, and no unital homomorphism returns the completion to its base.
