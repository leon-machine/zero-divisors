---
id: std-algebra.determinant-pseudoscalar
kind: claim
version: 1
title: The determinant is the action on the pseudoscalar
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- classical-theorem
- pseudoscalar-and-centre
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
- obj.std-algebra.outermorphism
- obj.std-algebra.pseudoscalar
derivations:
- name: main
  uses:
  - std-algebra.exterior-isomorphism@1
  - std-algebra.grade-decomposition@1
  - std-algebra.functoriality@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_determinant_on_pseudoscalar
locators:
  sources:
  - key: HestenesSobczyk1984
    locator: Ch. 3 (linear and multilinear functions)
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
extraction:
  by: algebra-core-2026-10-26
---

## formal
Let $f : V \to V$ be linear and $I$ any nonzero element of $\Cl^{n}(V, Q)$. Then
\begin{equation}
\underline{f}(I) = \det(f)\, I ,
\end{equation}
so $\det(f g) = \det(f) \det(g)$ and $\underline{f g} = \underline{f}\,\underline{g}$. If $f$ is an isometry, $\underline{f} = \Cl(f)$, the algebra homomorphism of \claimref{std-algebra.functoriality}; in particular an isometry multiplies the pseudoscalar by $\det f = \pm 1$ when $V$ is nondegenerate.

## technical
The top grade is one-dimensional, so the outermorphism of a linear map acts on it by a number, and that number is the determinant. Multiplicativity of the determinant follows at once from composition of outermorphisms. For an isometry the outermorphism is the algebra homomorphism it induces, so it also respects the geometric product.

## lay
A linear map scales oriented volumes, and the scale factor is its determinant. In this algebra that is not a formula to memorise but the statement that the map multiplies the unit volume element by a number.

## one-liner
$\underline{f}(I) = \det(f)\, I$ for every pseudoscalar $I$; for an isometry $\underline{f} = \Cl(f)$.
