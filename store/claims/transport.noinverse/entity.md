---
id: transport.noinverse
kind: claim
version: 4
title: A null vector has no inverse
status: proved
region: transport
subject: zero-divisors
tags: [null-directions, no-go]
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
derivations:
- name: main
  uses:
  - std-algebra.vector-squares@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_null_vector_squares_to_zero_and_multiplication_has_half_rank
- kind: check
  ref: check.py::check_no_inverse_in_larger_algebras
locators:
  paper: T01
  number: Lem 2.1
  label: lem:noinverse
  line: 454
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.vector-squares where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: null vectors in every mixed signature with n <= 5 square to zero and multiply with half rank, and in Cl(p+1, q+1) or with a degenerate generator v(vw) = (wv)v = 0. Version 1 -> 2. Check strengthened: half rank checked in both extensions (was hyperbolic only) and the number of rank cases (24) pinned; samples moved to module level. Version 2 -> 3.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: self-contained two-line proof, no edges
---

## formal
A null vector $v \neq 0$ has no left inverse and no right inverse in $\Cl(p,q)$, nor in any associative unital algebra containing $\Cl(p,q)$ as a unital subalgebra.

## technical
If $v \neq 0$ is null then $v^2 = Q(v) = 0$, and this relation persists in any associative unital algebra containing $\Cl(p,q)$ as a unital subalgebra, since the multiplication restricts. A right inverse with $vw = 1$ would give $v = v(vw) = v^2 w = 0$, and a left inverse with $wv = 1$ would give $v = (wv)v = w v^2 = 0$, both contradicting $v \neq 0$.

So no associative unital enlargement of the algebra can make a nonzero null vector invertible on either side.

## lay
A null vector is a nonzero direction whose square is zero. Such an element can never be divided by: if it had an inverse on either side, multiplying through would force the vector itself to be zero. The argument uses only the fact that its square is zero, so it still applies in any larger algebra of the same kind that contains the original one.

## one-liner
A nonzero null vector of $\Cl(p,q)$ has no left and no right inverse, either in $\Cl(p,q)$ or in any associative unital algebra containing it as a unital subalgebra.
