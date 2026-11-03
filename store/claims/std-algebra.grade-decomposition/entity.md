---
id: std-algebra.grade-decomposition
kind: claim
version: 1
title: The grade decomposition
status: proved
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
review: typed
trust: ai-proposed
about:
- obj.std-algebra.grade-projection
derivations:
- name: main
  uses:
  - std-algebra.blade-basis@1
  - std-algebra.orthogonal-anticommute@1
  - std-algebra.sylvester-inertia@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_antisymmetrised_products_have_one_grade
locators:
  sources:
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
  - key: Chevalley1954
    locator: Ch. II (the Clifford algebra of a quadratic space)
extraction:
  by: algebra-core-2026-10-26
---

## formal
Let $e_1, \dots, e_n$ be an orthogonal basis of $V$. Then $\Cl^{k}(V, Q)$ is the span of the blades $e_I$ with $|I| = k$, so $\dim \Cl^{k} = \binom{n}{k}$ and
\begin{equation}
\Cl(V, Q) = \bigoplus_{k=0}^{n} \Cl^{k}(V, Q),
\end{equation}
with $\Cl^{0} = \R\,1$ and $\Cl^{1} = V$. The decomposition does not depend on the orthogonal basis. For $u, v \in V$, $\langle uv \rangle_0 = B(u, v)$ and $\langle uv \rangle_2 = \tfrac12(uv - vu)$.

## technical
In an orthogonal basis the grade-$k$ subspace is spanned by the blades with $k$ indices, so the grades have dimensions given by binomial coefficients and the algebra is their direct sum. Since grades were defined by antisymmetrised products, the decomposition is the same for every orthogonal basis. The product of two vectors has a scalar part, their polar form, and a bivector part, half their commutator.

## lay
In $n$ dimensions there is one number direction, $n$ arrow directions, $n(n-1)/2$ plane directions and so on, and every element splits uniquely into these parts. The split does not depend on which perpendicular axes are chosen.

## one-liner
In an orthogonal basis $\Cl^{k} = \operatorname{span}\{e_I : |I| = k\}$, so $\Cl = \bigoplus_k \Cl^{k}$ with $\dim \Cl^{k} = \binom{n}{k}$, independently of the basis.
