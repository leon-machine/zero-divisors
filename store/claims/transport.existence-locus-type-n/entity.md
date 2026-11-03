---
id: transport.existence-locus-type-n
kind: claim
version: 5
title: Existence locus of type N
status: proved
region: transport
subject: zero-divisors
tags: [obstruction-types, null-directions]
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
derivations:
- name: main
  uses:
  - transport.noinverse@4
  - std-algebra.orthogonal-anticommute@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:3.3
- kind: check
  ref: check.py::check_definite_forms_have_no_null_vectors
- kind: check
  ref: check.py::check_mixed_forms_have_a_null_cone_of_dimension_n_minus_one
- kind: check
  ref: check.py::check_null_vectors_are_non_invertible_zero_divisors
locators:
  paper: T01
  number: Prop 3.3
  label: prop:typeNlocus
  line: 582
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.orthogonal-anticommute where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: definite forms anisotropic (Gram +-id, rational net); 28 rational null vectors in the mixed signatures with n <= 5, gradient rank 1 (cone of dimension n - 1); null vectors have left rank 2^(n-1) and no left or right inverse in Cl(p,q) or its extensions. Version 2 -> 3. Sample inputs moved to module level; invertible control extended to both generators of Cl(1,1) on both sides. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: "kept the no-inverse lemma, which the proof cites for non-invertibility in every extension"
---

## formal
$\Cl(p,q)$ contains a null vector if and only if the signature is mixed, $pq \neq 0$. In that case the null vectors form a cone of dimension $n - 1$, and every null vector is a two-sided zero divisor without left or right inverse in any unital algebra containing $\Cl(p,q)$.

## technical
A null vector is a nonzero $v$ with $Q(v) = 0$. In $\Cl(p,q)$ such vectors exist exactly when the signature is mixed, $pq \neq 0$: a definite form is anisotropic, while for $p, q \geq 1$ the sum of a positive and a negative unit basis vector is null. When they exist, the null vectors form a cone of dimension $n - 1$, the zero set of the quadratic form with the origin removed.

Every null vector satisfies $v^2 = 0$ and so is a two-sided zero divisor, and it has neither a left nor a right inverse in any unital algebra containing $\Cl(p,q)$: from $vw = 1$ one would get $v = v^2 w = 0$.

## lay
In a space with both positive and negative directions, like the space-time of relativity, there are nonzero directions of zero length, called null directions. This result says they exist exactly when both kinds of direction are present, and that they then form a cone, much like a light cone. Each such direction multiplied by itself gives zero, so it can never be divided by, even in a larger algebra that contains the original one.

## one-liner
$\Cl(p,q)$ contains null vectors exactly when $pq \neq 0$; they then form a cone of dimension $n - 1$, and each is a two-sided zero divisor with no left or right inverse in any unital algebra containing $\Cl(p,q)$.
