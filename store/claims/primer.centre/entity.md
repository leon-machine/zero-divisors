---
id: primer.centre
kind: claim
version: 3
title: The centre
status: proved
region: primer
programme: standard
subject: standard-algebra
tags: [pseudoscalar-and-centre]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T00, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, foundation layer'
  version: 3
  source: run 2026-11-08-foundation-layer
review: typed
founded_on:
- synthesis.continuum-completion-premise@2
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_centre_by_linear_algebra
- kind: check
  ref: check.py::check_central_blades_higher_n
locators:
  paper: T00
  number: Lem 9.4
  label: tk:center
  line: 490
extraction:
  maintainer_pass_2026_11_08_foundation:
    by: ai-maintainer-pass
    note: >-
      Version 2 -> 3. Leon's decision of 8 November 2026: the foundation layer. Founded on synthesis.continuum-completion-premise: the algebra it is stated in rests on the foundation. Foundation postulates are reported as what a result rests on, separately from the premises it holds given (store/conventions.md, "The foundation").
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: centre of Cl(p,q) by exact kernel computation for n <= 6 and central blades for 6 <= n <= 9. Version 1 -> 2.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: Self-contained proof in the source; no edges.
---

## formal
For $n \geq 1$, the centre of $\Cl(p,q)$ is $\R \cdot 1$ if $n$ is even, and $\R \cdot 1 \oplus \R \cdot \omega$ if $n$ is odd, where $\omega = e_1 e_2 \cdots e_n$ is the pseudoscalar.

## technical
For $n = p + q \geq 1$, conjugation by a generator $e_j$ sends a grade-$k$ basis blade $e_I$ to $(-1)^{k - [j \in I]}\, e_I$, so a central element can only have components whose blades survive every such conjugation. For $0 < k < n$ a generator inside $I$ and one outside $I$ impose incompatible parity conditions, so the centre lies in $\R \oplus \R\,\omega$, and $\omega$ itself is central exactly when $n$ is odd.

Hence the centre of $\Cl(p,q)$ is $\R \cdot 1$ for even $n$ and $\R \cdot 1 \oplus \R \cdot \omega$ for odd $n$, with $\omega = e_1 \cdots e_n$ the pseudoscalar.

## lay
The centre of an algebra is the set of its elements that commute with everything in it. For the Clifford algebra of a space with an even number of dimensions, only the ordinary numbers do this. With an odd number of dimensions there is one more such element, the product of all the basis directions, so the centre becomes two-dimensional.

## one-liner
For $n \geq 1$ the centre of $\Cl(p,q)$ is $\R \cdot 1$ when $n$ is even and $\R \cdot 1 \oplus \R \cdot \omega$ when $n$ is odd.
