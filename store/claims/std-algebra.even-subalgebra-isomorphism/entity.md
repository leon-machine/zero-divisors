---
id: std-algebra.even-subalgebra-isomorphism
kind: claim
version: 1
title: The even subalgebra is a Clifford algebra one dimension down
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- grading-and-parity
- clifford-classification
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
- obj.std-algebra.even-subalgebra
derivations:
- name: main
  uses:
  - std-algebra.z2-grading@1
  - std-algebra.existence-uniqueness@1
  - std-algebra.blade-basis@1
  - std-algebra.orthogonal-anticommute@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_even_subalgebra_is_clifford
locators:
  sources:
  - key: Lounesto2001
    locator: Ch. 16 (matrix representations and periodicity of 8)
  - key: Lam2005
    locator: 'Ch. V (Clifford algebras: the tensor product rules)'
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No version bump (plain levels or extraction only). One-liner: the chained isomorphism dropped the hypotheses q >= 1 and p >= 1 of the formal level; restored.'
  by: algebra-core-2026-10-26
---

## formal
Let $e \in V$ with $Q(e) = s \ne 0$ and $U = e^{\perp}$, so $V = \R e \perp U$ (the form on $U$ may be degenerate). Then $u \mapsto u e$ extends to an isomorphism
\begin{equation}
\Cl(U, -s\,Q|_U) \;\xrightarrow{\ \cong\ }\; \Cl^{+}(V, Q).
\end{equation}
In particular $\Cl^{+}(p, q, r) \cong \Cl(p, q{-}1, r)$ for $q \ge 1$ (take $Q(e) = -1$) and $\Cl^{+}(p, q, r) \cong \Cl(q, p{-}1, r)$ for $p \ge 1$ (take $Q(e) = 1$).

## technical
Fix a non-null vector $e$. Multiplying each vector of its orthogonal complement by $e$ gives even elements that anticommute and square to $-Q(e)$ times their old square. They generate the whole even subalgebra, which is therefore the Clifford algebra of the complement with the form rescaled by $-Q(e)$. Choosing $e$ time-like or space-like gives the two familiar forms.

## lay
The even part of the algebra of a space is itself the full algebra of a space with one fewer direction. In space-time, for instance, the even part, where rotations and boosts live, is the algebra of ordinary three-dimensional space.

## one-liner
For $Q(e) = s \ne 0$, $u \mapsto ue$ gives $\Cl(e^{\perp}, -sQ) \cong \Cl^{+}(V, Q)$; so $\Cl^{+}(p,q,r) \cong \Cl(p,q{-}1,r)$ for $q \ge 1$ and $\Cl^{+}(p,q,r) \cong \Cl(q,p{-}1,r)$ for $p \ge 1$.
