---
id: transport.conformal-gram-matrix
kind: claim
version: 4
title: The conformal Gram matrix
status: proved
region: transport
subject: completion
tags: [conformal-model]
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
- name: Claude Opus 5.5
  role: 'maintainer pass, citation of the retired imported Fact repointed to its derivation in geometric algebra'
  version: 4
  source: run 2026-11-07-bit-root
review: typed
derivations:
- name: main
  uses:
  - synthesis.completion-recovers-the-real-clifford-algebras@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:4.18
- kind: check
  ref: check.py::check_rank_and_signature
- kind: check
  ref: check.py::check_gram_of_null_lifts
locators:
  paper: T01
  number: Lem 4.18
  label: lem:gram
  line: 975
extraction:
  maintainer_pass_2026_11_08:
    by: ai-maintainer-pass
    note: >-
      Version 3 -> 4. Leon's decision of 7 November 2026: the imported Fact std-algebra.sylvester-inertia is retired, replaced by synthesis.completion-recovers-the-real-clifford-algebras, whose clause (iii) derives Sylvester's law of inertia in geometric algebra over any Euclidean field, the reals included; the citation and edge now point there.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites synthesis.completion-recovers-the-real-clifford-algebras where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: rank n + 2 and signature (p+1, q+1) for every signature with n <= 6 and non-normalised bases, and M as the Gram of the null lifts. Version 1 -> 2.'
  env: lemma
  eqrefs: 1
  typing:
    by: ai-typing-pass
    note: 'No premises: the proof is a direct computation using the model identity of the conformal lift, which is an equation of the paper rather than a store claim.'
payload:
- kind: classification
  clause: rank n + 2, signature (p+1, q+1)
  python: all(GA.mat_rank(gram_points(p, q, None)) == p + q + 2 and GA.congruence_signature(gram_points(p,
    q, None)) == (p + 1, q + 1, 0) for (p, q) in SIGS if p + q <= 5)
  note: every (p,q) with n <= 5, unit basis
---

## formal
Fix an orthogonal basis $e_1, \dots, e_n$ of $\mathbb{V}$ and the $n + 2$ points
\[
p_0 = 0, \qquad p_i = e_i \ (1 \leq i \leq n), \qquad p_{n+1} = 2e_1 .
\]
Then the symmetric $(n{+}2) \times (n{+}2)$ matrix $M_{ij} = -\tfrac12 Q(p_i - p_j)$ has rank $n + 2$ and signature $(p{+}1,\, q{+}1)$.

## technical
Take an orthogonal basis $e_1, \dots, e_n$ of $\mathbb{V}$ and the $n + 2$ points $p_0 = 0$, $p_i = e_i$ for $1 \leq i \leq n$, and $p_{n+1} = 2e_1$. The symmetric $(n{+}2) \times (n{+}2)$ matrix $M_{ij} = -\frac12 Q(p_i - p_j)$ then has full rank $n + 2$ and signature $(p{+}1, q{+}1)$.

So a table built only from separations in the original space already has the rank and signature of the completed space two dimensions up.

## lay
Pick a few specific points in a space: the origin, one unit step along each axis, and a point two steps along the first axis. Write down a table of their squared separations, halved and with the sign reversed. Read as a quadratic form, that table has exactly one more positive and one more negative direction than the original space.

## one-liner
For the origin, the basis vectors and $2e_1$, the matrix $M_{ij} = -\frac12 Q(p_i - p_j)$ has rank $n + 2$ and signature $(p{+}1, q{+}1)$.
