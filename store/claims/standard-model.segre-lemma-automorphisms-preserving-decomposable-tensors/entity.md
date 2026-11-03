---
id: standard-model.segre-lemma-automorphisms-preserving-decomposable-tensors
kind: claim
version: 2
title: 'The Segre lemma: automorphisms preserving decomposable tensors'
status: proved
region: standard-model
subject: standard-model
tags: [classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_stabiliser_lie_algebra_is_gl_m_plus_gl_k
- kind: check
  ref: check.py::check_sum_of_two_decomposables
- kind: check
  ref: check.py::check_swap_and_product_form
- kind: check
  ref: check.py::check_unitary_rebalancing
locators:
  paper: T12
  number: Lem 2.13
  label: lem:segre
  line: 931
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Lie algebra preserving the Segre cone is gl(m) + gl(k) for five shapes, rank of sums of decomposables, the swap''s realignment rank, and unitary rebalancing. Version 1 -> 2.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: "Classical lemma proved in full in the source with no premises; pure algebra and not in the store as an import, so no standard-route derivation."
---

## formal
Let $m, k \ge 2$ with $m \neq k$. A linear automorphism $T$ of $\C^{m} \otimes \C^{k}$ that maps the set of decomposable tensors onto itself (equivalently, that preserves the Segre variety; $T^{-1}$ then preserves it too) is of the form $T = A \otimes B$, and if $T$ is unitary then $A$ and $B$ may be taken unitary. When $m = k$ the factor swap $u \otimes v \mapsto v \otimes u$ is a further symmetry of the decomposable tensors.

## technical
For $m, k \ge 2$ with $m \neq k$, a linear automorphism $T$ of $\C^{m} \otimes \C^{k}$ that maps the decomposable tensors $u \otimes v$ onto themselves is a product $T = A \otimes B$, and if $T$ is unitary then $A$ and $B$ can be taken unitary. The proof uses the maximal linear subspaces made of decomposable tensors, $u \otimes \C^{k}$ and $\C^{m} \otimes v$, which $T$ must permute and which are told apart by their dimensions when $m \neq k$.

When $m = k$ the factor swap $u \otimes v \mapsto v \otimes u$ is a further symmetry of the decomposable tensors, not of product form.

## lay
A tensor product of two spaces contains special simple elements, products of one vector from each side. This classical lemma says that if a transformation of the product sends simple elements to simple elements, and the two sides have different sizes, then it must act separately on each side. When the two sides have the same size, swapping them is one further possibility.

## one-liner
For $m \neq k$, every linear automorphism of $\C^{m} \otimes \C^{k}$ preserving decomposable tensors is $A \otimes B$, with unitary factors when it is unitary; for $m = k$ the factor swap is a further symmetry.
