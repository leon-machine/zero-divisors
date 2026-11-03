---
id: neutrino.invariant-symmetric-matrices
kind: claim
version: 2
title: $S_{3}$-invariant symmetric matrices
status: proved
region: neutrino
subject: neutrinos
tags: [representation-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T15, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T15.py
  tags:
  - label:lem:s3
- kind: check
  ref: check.py::check_characterisation
- kind: check
  ref: check.py::check_spectrum_and_determinant
- kind: check
  ref: check.py::check_inverse_and_projector_forms
locators:
  paper: T15
  number: Lem 4.3
  label: lem:s3
  line: 622
extraction:
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'elementary lemma with no premises; levels only.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the invariant subspace is span{1, J} (kernel of the six permutation conditions), the spectrum, det = alpha^2 (alpha + 3 beta) on a grid, the inverse against elimination, and the projector forms. Version 1 -> 2.'
---

## formal
Let $\J$ be the $3 \times 3$ all-ones matrix and $u' = (1,1,1)$. A real symmetric $3 \times 3$ matrix $S$ satisfies $PSP^{\mathsf{T}} = S$ for every permutation matrix $P$ if and only if $S = \alpha\mathbf{1} + \beta\J$ for real $\alpha, \beta$. Such an $S$ has $u'$ as an eigenvector with eigenvalue $M_{3} := \alpha + 3\beta$, the plane $u'^{\perp}$ as an eigenspace with eigenvalue $\alpha$, $\det S = \alpha^{2}(\alpha + 3\beta)$, hence is invertible if and only if $\alpha \neq 0$ and $\alpha \neq -3\beta$, with $S^{-1} = \alpha^{-1}\mathbf{1} - \beta\,\alpha^{-1}(\alpha + 3\beta)^{-1}\J$. Writing $\Pi = \mathbf{1} - \J/3$ for the projector on $u'^{\perp}$, $S = \alpha\Pi + M_{3}\J/3$, and $S^{-1} = \alpha^{-1}\Pi + M_{3}^{-1}\J/3$ when both are nonzero.

## technical
A real symmetric $3 \times 3$ matrix satisfies $PSP^{\mathsf{T}} = S$ for every permutation matrix $P$ exactly when $S = \alpha\mathbf{1} + \beta\J$, with $\J$ the all-ones matrix. Such an $S$ has eigenvalue $M_{3} = \alpha + 3\beta$ on $u' = (1,1,1)$ and $\alpha$ on the plane $u'^{\perp}$, so $\det S = \alpha^{2}(\alpha + 3\beta)$ and $S$ is invertible exactly when $\alpha \neq 0$ and $\alpha \neq -3\beta$.

With $\Pi = \mathbf{1} - \J/3$ the projector onto $u'^{\perp}$, $S = \alpha\Pi + M_{3}\J/3$, and when both eigenvalues are nonzero $S^{-1} = \alpha^{-1}\Pi + M_{3}^{-1}\J/3$.

## lay
If a three-by-three table of numbers must look the same however the three families are relabelled, it can contain only two independent numbers. That fixes its behaviour completely: one special direction in which all three families are equal, and a plane of directions all treated alike. Inverting such a table is then simple.

## one-liner
The permutation-invariant real symmetric $3 \times 3$ matrices are exactly $\alpha\mathbf{1} + \beta\J$, with eigenvalue $\alpha + 3\beta$ on $u'$ and $\alpha$ on $u'^{\perp}$.
