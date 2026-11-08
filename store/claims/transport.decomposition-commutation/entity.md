---
id: transport.decomposition-commutation
kind: claim
version: 3
title: Decomposition and commutation
status: proved
region: transport
subject: completion
tags: [grading-and-parity]
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
  - std-algebra.blade-basis@1
  - std-algebra.orthogonal-anticommute@1
  - primer.commutation-rule@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_direct_sum_decomposition
- kind: check
  ref: check.py::check_commutation_by_grade_involution
- kind: check
  ref: check.py::check_inverse_is_gamma_nu
locators:
  paper: T01
  number: Lem 5.1
  label: lem:BAdecomp
  line: 1125
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.blade-basis, std-algebra.orthogonal-anticommute, primer.commutation-rule where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: B = A + A nu, nu a = a^ nu on all blades, and nu^{-1} = gamma nu, for 13 base spaces and gamma = +1, -1, 0. Version 1 -> 2.'
  env: lemma
  eqrefs: 1
  typing:
    by: ai-typing-pass
    note: 'No premises; the proof is a blade count and the anticommutation of the adjoined generator, citing the literature only for the degenerate case.'
---

## formal
$B_\gamma = A \oplus A\nu$ as a vector space, and
\[
\nu\, a \;=\; \hat{a}\, \nu \qquad (a \in A),
\]
where $\hat{\cdot}$ is the grade involution of $A$. For $\gamma = \pm 1$, $\nu$ is invertible with $\nu^{-1} = \gamma\nu$.

## technical
Adjoin to $A = \Cl(\mathbb{V}, Q)$ one generator $\nu$ orthogonal to $\mathbb{V}$, with $Q(\nu) = \gamma$, giving the algebra $B_\gamma$. As a vector space $B_\gamma = A \oplus A\nu$, and $\nu$ moves past elements of $A$ by the grade involution: $\nu\, a = \hat a\, \nu$ for $a \in A$. When $\gamma = \pm 1$, $\nu$ is invertible with $\nu^{-1} = \gamma\nu$.

## lay
Adding one new direction to a Clifford algebra doubles its size: every element becomes an old element plus an old element times the new direction. Moving the new direction past an old element flips the sign of that element's odd parts. If the new direction has nonzero square, one can divide by it.

## one-liner
The one-generator ascent splits as $B_\gamma = A \oplus A\nu$ with $\nu a = \hat a\, \nu$, and $\nu^{-1} = \gamma\nu$ when $\gamma = \pm 1$.
