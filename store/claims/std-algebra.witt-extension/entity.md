---
id: std-algebra.witt-extension
kind: claim
version: 1
title: Witt's extension theorem
status: imported
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- classical-theorem
- rotors-and-stabilisers
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
review: typed
trust: ai-proposed
about:
- obj.std-algebra.quadratic-space
- obj.std-algebra.hyperbolic-plane
imported_from:
- citation: E. Witt, Theorie der quadratischen Formen in beliebigen Koerpern, J. Reine Angew. Math. 176
    (1937).
  key: Witt1937
  locator: Satz 4
- citation: T. Y. Lam, Introduction to Quadratic Forms over Fields, AMS (2005).
  key: Lam2005
  locator: Ch. I (Witt's extension and cancellation theorems)
checked_by:
- kind: check
  ref: check.py::check_extension_by_reflections
- kind: check
  ref: check.py::check_null_line_extends_and_radical_obstructs
locators:
  sources:
  - key: Lam2005
    locator: Ch. I (hyperbolic planes, the Witt decomposition, Witt's theorems)
extraction:
  referee_fixes: '2026-10-26: dropped the misleading condition on U: any extension is a product of reflections because V is nondegenerate (referee part 2, point 4).'
  by: algebra-core-2026-10-26
  note: Imported, with a check of its finite core, as Leon decided on 2026-10-26 for the long classical
    proofs.
---

## formal
Let $(V, Q)$ be a nondegenerate real quadratic space, $U \subseteq V$ any subspace and $f : U \to V$ an injective isometry. Then $f$ extends to an isometry of $V$, that is an element of $\mathrm{O}(V, Q)$. Equivalently (Witt cancellation): if $A \perp B$ and $A' \perp B'$ are nondegenerate with $A \cong A'$ and $A \perp B \cong A' \perp B'$, then $B \cong B'$. Every such extension is a product of reflections $x \mapsto x - 2\frac{B(x, a)}{Q(a)}\, a$, since $V$ is nondegenerate (\claimref{std-algebra.cartan-dieudonne}). The hypothesis that $V$ is nondegenerate cannot be dropped: an isometry of $V$ maps $\operatorname{rad} V$ to itself.

## technical
In a nondegenerate quadratic space, any length-preserving embedding of a subspace, null or not, is the restriction of a global isometry. For a nondegenerate subspace the global isometry can be built from reflections one basis vector at a time. Over the reals cancellation also follows from the law of inertia. In a degenerate space the theorem fails, because isometries must preserve the radical.

## lay
If two configurations of arrows have the same lengths and angles, some symmetry of the whole space carries one to the other. This holds even for configurations of light-like arrows, as long as the space has no invisible directions.

## one-liner
In a nondegenerate quadratic space every isometric embedding of a subspace extends to an isometry of the whole space (Witt).
