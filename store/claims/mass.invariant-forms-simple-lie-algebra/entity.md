---
id: mass.invariant-forms-simple-lie-algebra
kind: claim
version: 2
title: Invariant forms on a simple Lie algebra
status: proved
region: mass
subject: mass
tags: [classical-theorem, representation-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_simple_algebras_have_one_invariant_form
- kind: check
  ref: check.py::check_non_simple_controls_have_two_forms
locators:
  paper: T11
  number: Lem 2.7
  label: lem:invforms
  line: 438
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the invariant symmetric forms on sl(2), sl(3), so(5), so(6) form the line of the Killing form, with gl(2) and so(4) as two-dimensional controls. Version 1 -> 2.'
  env: lemma
  typing:
    by: ai-typing-pass
    removed:
    - mass.casimir-form-join
    note: 'Resolved E301: the lemma cites the Casimir proposition only as the place it is used, so that edge was removed; the same standard fact is in the store as an imported Standard-Model claim, but this paper does not call it classical, so no standard-route was added.'
---

## formal
On a finite-dimensional simple Lie algebra over $\C$, any two nonzero invariant symmetric bilinear forms are proportional.

## technical
Let $\mathfrak{g}$ be a finite-dimensional simple Lie algebra over $\C$. If $B_{1}$ and $B_{2}$ are nonzero symmetric bilinear forms on $\mathfrak{g}$ that are invariant under the adjoint action, then $B_{2} = \kappa B_{1}$ for a constant $\kappa$.

In practice this means that any invariant form, for instance one built from traces in a representation, is a multiple of the Killing form, so its constant can be fixed by evaluating it on a single element.

## lay
A simple Lie algebra is the infinitesimal version of a basic symmetry group. This lemma says that, up to an overall factor, there is only one natural way to measure its elements that respects the symmetry. That uniqueness is what lets an unknown constant be fixed by one evaluation.

## one-liner
On a finite-dimensional simple complex Lie algebra any two nonzero invariant symmetric bilinear forms are proportional.
