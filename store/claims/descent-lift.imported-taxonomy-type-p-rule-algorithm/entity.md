---
id: descent-lift.imported-taxonomy-type-p-rule-algorithm
kind: claim
version: 3
title: 'Imported: the taxonomy, the type-P rule, and the algorithm'
status: proved
region: descent-lift
subject: zero-divisors
tags: [obstruction-types, transport-algorithm, idempotents, hyperbolic-plane]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-descent-lift, the series'' standard disclaimer'
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - transport.exhaustiveness-every-zero-divisor-annihilated-idempotent@3
  - transport.no-transport-terminates@4
  - transport.rule-1-morita-trivial@6
  - transport.transport-algorithm@3
  - transport.type-p-self-repairing@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_zero_divisors_annihilated_by_idempotents
- kind: check
  ref: check.py::check_type_n_hyperbolic_idempotent
- kind: check
  ref: check.py::check_step_two_diagnosis
- kind: check
  ref: check.py::check_step_three_rules
- kind: check
  ref: check.py::check_self_adjoint_idempotent_needs_definite_form
- kind: check
  ref: check.py::check_one_one_ascent
locators:
  paper: T05-descent-lift
  number: Fact 6.2
  label: fact:taxonomy
  line: 277
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: annihilating idempotents of sample zero divisors, the wv idempotent, Step 2 diagnosis, Step 3 repairs and pseudo-inverses, self-adjoint generators, and the (1,1) ascent matrix units and reflection. Version 2 -> 3.'
  env: fact
  context_refs:
  - transport.exhaustiveness-every-zero-divisor-annihilated-idempotent
  - transport.no-go-level-elements
  - transport.no-transport-terminates
  - transport.rule-1-morita-trivial
  - transport.type-p-self-repairing
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    removed:
    - transport.no-go-level-elements
    added:
    - transport.transport-algorithm
    note: Removed the element-level no-go, which the provenance cites but which supports no clause of
      the statement; added the transport algorithm, whose table the diagnosis and repair clauses restate;
      the reflection and Moore-Penrose clauses come from remarks with no store entity.
---

## formal
Every zero divisor of a nondegenerate real Clifford algebra is annihilated on each side by a nontrivial idempotent; in a simple algebra the idempotent is non-central and the obstruction is type P, refined to type N exactly when the annihilating idempotent is $wv$ for a hyperbolic pair $(v, w)$ of null vectors, $vw + wv = 1$. Step 2 of the algorithm diagnoses by three tests in order: a vector of square zero is type N; a central idempotent is type C; otherwise type P, with the caution that nilpotence alone does not diagnose N. Step 3 adjoins a hyperbolic plane for type N, one generator for type C, and nothing for type P, the identity being the repair of an idempotent; a general type-P element has von Neumann pseudo-inverses, and among the idempotents with a given image the self-adjoint one is canonical exactly where a definite form is available. In the $(1,1)$ ascent the adjoined ladder pair $f, f^{*}$ and its occupation projectors are a system of matrix units, the adjoined pair is itself null, and the reflection in an adjoined direction is an automorphism of the ascent. \emph{Provenance:} \cite[Def.~3.1, Ex.~3.5, Thm.~3.9, Thm.~4.2, Rem.~5.8, Prop.~6.1, Rem.~6.6, Thm.~7.1, Prop.~7.8, Table~1]{ButlerT1}.

## technical
Imported from the root transport paper. Every zero divisor of a nondegenerate real Clifford algebra is annihilated on each side by a nontrivial idempotent; in a simple algebra that idempotent is non-central, so the obstruction is type P, refined to type N exactly when the idempotent is $wv$ for a hyperbolic pair $(v, w)$ of null vectors with $vw + wv = 1$. The algorithm diagnoses by three tests in order: a vector with $Q(v) = 0$ is type N, a central idempotent is type C, and anything else is type P; nilpotence alone does not diagnose type N.

The repair step adjoins a hyperbolic plane for type N, one generator for type C and nothing for type P, the identity being the repair of an idempotent. A general type-P element has von Neumann pseudo-inverses, and among the idempotents with a given image the self-adjoint one is canonical exactly where a definite form is available. In the $(1,1)$ ascent the adjoined ladder pair $f, f^{*}$ and its occupation projectors form a system of matrix units, $Q(f) = Q(f^{*}) = 0$, and the reflection in an adjoined direction is an automorphism of the ascent.

## lay
This collects, from the series' founding paper, the rules for sorting the ways division can fail in a Clifford algebra and what to do about each. Every failure is pinned to an element that equals its own square, the three kinds are told apart by simple tests, and the prescribed repair is a new plane, one new direction, or nothing at all. It also records some facts about the smallest enlargement that the note goes on to use.

## one-liner
Every zero divisor of a nondegenerate real Clifford algebra is annihilated by a nontrivial idempotent, the transport algorithm diagnoses it as type N, C or P and adjoins a hyperbolic plane, one generator or nothing accordingly, and the $(1,1)$ ascent's ladder pair is null and yields matrix units.
