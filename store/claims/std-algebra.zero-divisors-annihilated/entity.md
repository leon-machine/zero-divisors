---
id: std-algebra.zero-divisors-annihilated
kind: claim
version: 1
title: Zero divisors are annihilated by idempotents (nondegenerate case)
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- idempotents
- degenerate-algebras
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
- obj.std-algebra.primitive-idempotent
derivations:
- name: main
  uses:
  - std-algebra.blade-basis@1
  - primer.classification-real-clifford-algebras@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_nondegenerate_zero_divisors_kill_idempotents
- kind: check
  ref: check.py::check_degenerate_annihilators_hold_no_idempotent
locators:
  sources:
  - key: Lam1999
    locator: matrix rings, idempotents and Morita theory
  - key: Lounesto2001
    locator: Ch. 16 (matrix representations and periodicity of 8)
extraction:
  referee_fixes: '2026-10-26: right ideals of Mat_k(D): columns, not rows, in a subspace (referee part 2, point 3).'
  by: algebra-core-2026-10-26
---

## formal
Let $A = \Cl(V, Q)$ and $x \in A$. The following are equivalent: (a) $x$ is not invertible; (b) $xy = 0$ for some $y \ne 0$; (c) $yx = 0$ for some $y \ne 0$. If $(V, Q)$ is nondegenerate they are also equivalent to: (d) $xe = 0$ for a nonzero idempotent $e$; (e) $fx = 0$ for a nonzero idempotent $f$. For degenerate $(V, Q)$, (d) and (e) can fail: in $\Cl(0,0,1)$ the null generator $e_1$ is a zero divisor and $0$, $1$ are the only idempotents.

## technical
In a finite-dimensional algebra an element fails to be invertible exactly when it kills something from one side, and then from the other side too. When the form is nondegenerate the Clifford algebra is semisimple, a matrix algebra or a sum of two, and then every element that kills something kills a nonzero idempotent: it annihilates a whole projection. With a degenerate form this fails, because nilpotent elements such as a null generator of the radical kill only other nilpotents.

## lay
An element that cannot be divided by always destroys something when multiplied. In the algebras of nondegenerate spaces, what it destroys always includes a whole "projection", a piece of the algebra that behaves like a projector. In degenerate spaces this can fail: a zero-length direction perpendicular to everything destroys only things like itself.

## one-liner
In $\Cl(V, Q)$, $x$ is non-invertible iff it is a zero divisor; if $Q$ is nondegenerate it then annihilates nonzero idempotents on both sides, which fails for degenerate $Q$.
