---
id: std-algebra.tensor-rules
kind: claim
version: 1
title: The tensor product rules
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- clifford-classification
- classical-theorem
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
- obj.std-algebra.clifford-algebra
derivations:
- name: main
  uses:
  - std-algebra.existence-uniqueness@1
  - std-algebra.blade-basis@1
  - std-algebra.orthogonal-anticommute@1
  - primer.sign@2
  - std-algebra.pseudoscalar-commutation@1
  - std-algebra.cl11-matrix@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_tensor_rule
locators:
  sources:
  - key: Lam2005
    locator: 'Ch. V (Clifford algebras: the tensor product rules)'
  - key: Lounesto2001
    locator: Ch. 16 (matrix representations and periodicity of 8)
  - key: ABS1964
    locator: the periodicity of Clifford algebras
extraction:
  referee_fixes: '2026-10-26: std-algebra.cl11-matrix, cited in the proof, added to uses (referee part 2, point 6).'
  by: algebra-core-2026-10-26
---

## formal
Let $(V, Q)$ be any real quadratic space (degenerate allowed) and $(W, Q_W)$ a nondegenerate one of even dimension, with pseudoscalar $\omega_W$ and $\omega_W^{2} = \epsilon \in \{1, -1\}$. Then
\begin{equation}
\Cl(V \perp W,\ \epsilon Q \oplus Q_W) \;\cong\; \Cl(V, Q) \otimes_{\R} \Cl(W, Q_W), \qquad v \mapsto v \otimes \omega_W, \quad w \mapsto 1 \otimes w .
\end{equation}
For the planes and for $\R^{0,8}$, $\R^{8,0}$ this gives, with $\Cl(1,1) \cong \Cl(2,0) \cong \Mat_2(\R)$:
\begin{equation}
\Cl(p{+}1, q{+}1) \cong \Mat_2(\Cl(p,q)), \quad \Cl(q{+}2, p) \cong \Cl(p,q) \otimes \Cl(2,0), \quad \Cl(q, p{+}2) \cong \Cl(p,q) \otimes \Cl(0,2),
\end{equation}
and $\Cl(p, q{+}8) \cong \Cl(p,q) \otimes \Cl(0,8)$, $\Cl(p{+}8, q) \cong \Cl(p,q) \otimes \Cl(8,0)$; all of these hold with a radical $\R^{0,0,r}$ added to $(p, q)$.

## technical
A Clifford algebra of an orthogonal sum is a tensor product of the two algebras, provided one factor has even dimension and its vectors in the other factor are dressed with that factor's pseudoscalar. Dressing multiplies their squares by $\omega^{2}$, which is $+1$ for $\R^{1,1}$ and $-1$ for $\R^{2,0}$ and $\R^{0,2}$. So adding a hyperbolic plane doubles the matrix size, and adding a Euclidean or anti-Euclidean plane swaps the roles of $p$ and $q$. These rules drive the classification.

## lay
Adding two extra directions to a space has a predictable effect on its algebra: the new algebra is the old one combined with a small two-dimensional algebra, at the cost of possibly swapping which directions count as space-like and which as time-like. Repeating this explains why the algebras repeat with period eight.

## one-liner
For $W$ even-dimensional with $\omega_W^{2} = \epsilon$, $\Cl(V \perp W, \epsilon Q \oplus Q_W) \cong \Cl(V) \otimes \Cl(W)$; hence $\Cl(p{+}1,q{+}1) \cong \Mat_2(\Cl(p,q))$, $\Cl(q{+}2,p) \cong \Cl(p,q) \otimes \Cl(2,0)$, $\Cl(q,p{+}2) \cong \Cl(p,q) \otimes \Cl(0,2)$.
