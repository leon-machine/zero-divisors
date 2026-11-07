---
id: sheaf.blade-basis-degenerate-forms-included
kind: claim
version: 5
title: Blade basis, degenerate forms included
status: proved
region: sheaf
subject: clifford-structure
tags: [degenerate-algebras]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, blades of a non-orthogonal basis named as ordered products; proof wording on the two operations'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - std-algebra.blade-basis@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T04.py
  tags:
  - num:2.6
- kind: check
  ref: check.py::check_blades_are_a_basis
- kind: check
  ref: check.py::check_structure_constants
- kind: check
  ref: check.py::check_structure_constants_polynomial
locators:
  paper: T04
  number: Lem 2.6
  label: lem:blades
  line: 425
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. Notation: the paper calls the ordered products e_I blades; obj.std-algebra.blade reserves the word for outer products, which they are only for an orthogonal basis, so the formal level now says so. Proof: exterior multiplication is not an anti-derivation; the sentence now says contraction is. Statement unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.blade-basis where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: blade independence in the exterior model for eight Gram matrices (degenerate, non-orthogonal, zero), structure constants (Clifford relation, associativity, agreement with GA.mul) and their polynomiality in the Gram entries. Version 1 -> 2. Check strengthened: scalar constant of e_i e_j (i > j) pinned to 2 B_ij(t) for every pair (the old assert used a pair with B_ij(t) = 0); sample inputs moved to module level. Version 2 -> 3.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'no edges in the draft and none needed; the proof is self-contained. Levels pass: conditions
      already kept.'
---

## formal
Let $B$ be any symmetric bilinear form on $W$, $\dim W = n$, and let $e_1, \dots, e_n$ be \emph{any} basis of $W$ (orthogonality is not assumed and may be unavailable smoothly in families). Then the $2^n$ blades $e_I = e_{i_1} \cdots e_{i_k}$, $I = \{i_1 < \dots < i_k\}$ (ordered geometric products; for a non-orthogonal basis they are not the outer-product blades of \claimref{obj.std-algebra.blade}), form a linear basis of $\Cl(W, B)$. Moreover the structure constants of the algebra in this basis are polynomial in the entries $B(e_i, e_j)$.

## technical
For any symmetric bilinear form $B$ on an $n$-dimensional space $W$, degenerate or not, and any basis $e_1, \dots, e_n$ of $W$ (orthogonal or not), the $2^n$ ordered products $e_I = e_{i_1} \cdots e_{i_k}$ with $i_1 < \dots < i_k$ form a linear basis of $\Cl(W, B)$, and the structure constants in this basis are polynomial in the entries $B(e_i, e_j)$.

Spanning follows from the rewriting rules $e_j e_i = 2B(e_i, e_j) - e_i e_j$ and $e_i e_i = B(e_i, e_i)$. Independence comes from letting the algebra act on the exterior algebra $\Lambda W$ by $c(\alpha)\,\xi = \alpha \wedge \xi + \iota_{B(\alpha, \cdot)}\,\xi$, which satisfies $c(\alpha)^2 = Q(\alpha)\,\id$ with $Q(\alpha) = B(\alpha, \alpha)$: applied to $1$, each blade gives its wedge product plus terms of lower degree, so the images are triangular and hence independent. Nondegeneracy is never used.

## lay
A Clifford algebra is built from a space of directions together with a rule for multiplying lengths. This result says that the standard basis of the algebra, made from products of basis directions, still works when the rule is degenerate, so that some directions have zero length against everything, and even when the chosen directions are not perpendicular. The multiplication table depends polynomially, and so smoothly, on the rule.

## one-liner
For any symmetric bilinear form, degenerate or not, and any basis, the $2^n$ blades form a basis of the Clifford algebra, with structure constants polynomial in the entries of the form.
