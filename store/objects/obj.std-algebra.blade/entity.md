---
id: obj.std-algebra.blade
kind: object
version: 2
title: Blades
status: defined
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- grading-and-parity
proposed_by:
  kind: ai
  session: algebra-core-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'maintainer pass, foundation layer'
  version: 2
  source: run 2026-11-08-foundation-layer
review: typed
trust: ai-proposed
about:
- obj.std-algebra.outer-product
founded_on:
- synthesis.continuum-completion-premise@2
locators:
  sources:
  - key: HestenesSobczyk1984
    locator: Ch. 1 (geometric algebra)
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
extraction:
  maintainer_pass_2026_11_08_foundation:
    by: ai-maintainer-pass
    note: >-
      Version 1 -> 2. Leon's decision of 8 November 2026: the foundation layer. Founded on synthesis.continuum-completion-premise: the algebra it is stated in rests on the foundation. Foundation postulates are reported as what a result rests on, separately from the premises it holds given (store/conventions.md, "The foundation").
  by: algebra-core-2026-10-26
---

## formal
A \emph{$k$-blade} is an outer product $A = v_1 \wedge \dots \wedge v_k$ of $k$ vectors ($k \ge 1$); scalars are $0$-blades. The \emph{subspace} of a nonzero blade is $[A] = \{ x \in V : x \wedge A = 0 \}$. A nonzero $n$-blade is a \emph{pseudoscalar}.

## technical
A blade is an outer product of vectors. A nonzero blade determines the subspace of vectors whose outer product with it vanishes; by \claimref{std-algebra.blade-subspace} this is the span of its factors, so blades stand for oriented, weighted subspaces.

## lay
A blade is an oriented piece of a line, plane or higher flat, with a size. It is the algebra's way of holding a whole subspace as a single element.

## one-liner
A $k$-blade is $v_1 \wedge \dots \wedge v_k$; a nonzero one has subspace $[A] = \{x : x \wedge A = 0\}$.
