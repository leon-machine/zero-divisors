---
id: singularity.pseudo-inverse-identities-hyperbolic-atom
kind: claim
version: 4
title: Pseudo-inverse identities, and the hyperbolic atom
status: proved
region: singularity
subject: zero-divisors
tags:
- hyperbolic-plane
- ladder-pairs
- finite-models
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
  - std-algebra.orthogonal-anticommute@1
  - std-algebra.vector-squares@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:4.1
- kind: check
  ref: check.py::check_pseudo_inverse_identities
- kind: check
  ref: check.py::check_atom_is_car_and_zero_divisor
locators:
  paper: T05
  number: Lem 4.1
  label: lem:atom
  line: 1506
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Extraction only (DECISIONS G13, R11 item 9): the unit_note said ''the imaginary unit here stays a scalar i'', though no i remains in the levels; it is marked superseded and kept as history. No version change.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.orthogonal-anticommute, std-algebra.vector-squares where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: v v* v = v and v* v v* = v* on six CAR realisations, the hyperbolic atom in Cl(1,1) and its non-invertibility; the uniqueness citation is not checked. Version 2 -> 3.'
  env: lemma
  eqrefs: 3
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    note: 'Removed the mechanically added transport-algorithm edge: the identities follow from the anticommutation
      relations alone; the uniqueness of the hyperbolic atom is cited to a remark with no store entity,
      so no edge was added.'
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  unit_note: 'Superseded (7 November 2026): no imaginary unit remains in this entity''s levels or proof; the note below is history. The imaginary unit here stays a scalar i: this atom is built in the spacetime radial plane
    sigma = e0 e1, where the field theory''s unit I4 anticommutes with the mode operators, so the convention
    i = I4 (which needs a plane orthogonal to spacetime) does not apply. Recorded 21 October 2026; see
    store/conventions.md, known limit 1.'
---

## formal
From \eqref{eq:car} alone: $v v^* v = v$ and $v^* v v^* = v^*$, so each member of the pair is a von Neumann pseudo-inverse of the other, with no genuine inverse existing ($v$ is a zero divisor). The pair is realisable inside a single $(1,1)$ block: in $\Cl(1,1)$ with $e_0^2 = 1$, $e_1^2 = -1$, the vectors
\[
v = \tfrac12(e_0 + e_1), \qquad v^* = \tfrac12(e_0 - e_1)
\]
satisfy \eqref{eq:car} exactly. This block, the \emph{hyperbolic atom}, is the unique unit of transport that, at the level of elements, needs no ascent of its own \cite[Rem.~4.5]{ButlerT1}.

## technical
Let $v, v^*$ satisfy the canonical anticommutation relations $v^2 = (v^*)^2 = 0$ and $v v^* + v^* v = 1$. These relations alone give $v v^* v = v$ and $v^* v v^* = v^*$, so each member of the pair is a von Neumann pseudo-inverse of the other, although no genuine inverse exists because $v$ is a zero divisor.

The pair is realised exactly inside a single $(1,1)$ block: in $\Cl(1,1)$ with $Q(e_0) = 1$ and $Q(e_1) = -1$, take $v = \tfrac12(e_0 + e_1)$ and $v^* = \tfrac12(e_0 - e_1)$. This block, the hyperbolic atom, is the unique unit of transport that, at the level of elements, needs no ascent of its own.

## lay
Two elements that each square to zero can still act as partial inverses of one another: multiplying one by the other and then by the first again returns the first. Neither has a true inverse. Such a pair already lives in the algebra of a single plane with one space-like and one time-like direction, called the hyperbolic atom, which is the one building block of transport that, at the level of elements, needs no ascent of its own.

## one-liner
A null pair obeying the canonical anticommutation relations consists of mutual von Neumann pseudo-inverses that are zero divisors, and it is realised exactly in $\Cl(1,1)$ by $v = \tfrac12(e_0 + e_1)$, $v^* = \tfrac12(e_0 - e_1)$, the hyperbolic atom.

