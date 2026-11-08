---
id: obj.std-algebra.reversion
kind: object
version: 2
title: Reversion
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
- obj.std-algebra.clifford-algebra
founded_on:
- synthesis.continuum-completion-premise@2
locators:
  sources:
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
  - key: Lounesto2001
    locator: Ch. 14 (definitions of the Clifford algebra)
extraction:
  maintainer_pass_2026_11_08_foundation:
    by: ai-maintainer-pass
    note: >-
      Version 1 -> 2. Leon's decision of 8 November 2026: the foundation layer. Founded on synthesis.continuum-completion-premise: the algebra it is stated in rests on the foundation. Foundation postulates are reported as what a result rests on, separately from the premises it holds given (store/conventions.md, "The foundation").
  by: algebra-core-2026-10-26
---

## formal
The \emph{reversion} $x \mapsto \tilde{x}$ of $\Cl(V, Q)$ is the unique anti-automorphism with $\tilde{v} = v$ for $v \in V$: $(v_1 \cdots v_k)^{\sim} = v_k \cdots v_1$. It is the homomorphism $\Cl(V, Q) \to \Cl(V, Q)^{\mathrm{op}}$ given by the universal property applied to $V \to \Cl(V, Q)^{\mathrm{op}}$.

## technical
Reversion reverses the order of every product of vectors and leaves vectors alone. It is an anti-automorphism, $(xy)^{\sim} = \tilde{y}\tilde{x}$, obtained from the universal property applied to the opposite algebra.

## lay
Reversion writes every product of arrows backwards. It is used to undo rotations: a rotation's reverse is its inverse.

## one-liner
Reversion $\tilde{\cdot}$ is the anti-automorphism with $\tilde{v} = v$, so $(v_1 \cdots v_k)^{\sim} = v_k \cdots v_1$.
