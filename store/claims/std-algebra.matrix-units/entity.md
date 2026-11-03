---
id: std-algebra.matrix-units
kind: claim
version: 1
title: Matrix units give a matrix algebra over the corner
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- idempotents
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
- obj.std-algebra.primitive-idempotent
derivations:
- name: main
  uses:
  - std-algebra.orthogonal-anticommute@1
  - std-algebra.blade-basis@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_matrix_units_and_isomorphism
locators:
  sources:
  - key: Lam1999
    locator: matrix rings, idempotents and Morita theory
  - key: Lounesto2001
    locator: Ch. 16 (matrix representations and periodicity of 8)
extraction:
  referee_fixes: '2026-10-26: A assumed associative; corner dimensions counted from dim A = m^2 dim C rather than left to the check (referee part 1, point 6).'
  by: algebra-core-2026-10-26
---

## formal
Let $A$ be an associative unital real algebra containing elements $E_{ij}$, $1 \le i, j \le m$, with
\begin{equation}
E_{ij} E_{kl} = \delta_{jk} E_{il}, \qquad \textstyle\sum_{i} E_{ii} = 1 .
\end{equation}
Then $C = E_{11} A E_{11}$ is a unital algebra (with unit $E_{11}$) and
\begin{equation}
\Phi : A \to \Mat_m(C), \qquad \Phi(b)_{ij} = E_{1i}\, b\, E_{j1},
\end{equation}
is an isomorphism of unital algebras with inverse $(c_{ij}) \mapsto \sum_{i,j} E_{i1} c_{ij} E_{1j}$. In $\Cl(1,1)$, with $f = e_1 e_2$ ($f^{2} = 1$) and $\varepsilon_{\pm} = \tfrac12(1 \pm f)$, the elements $E_{11} = \varepsilon_+$, $E_{12} = \varepsilon_+ e_1$, $E_{21} = \varepsilon_- e_1$, $E_{22} = \varepsilon_-$ are such a system with $C = \R$, so $\Cl(1,1) \cong \Mat_2(\R)$; in $\Cl(1,1,1)$ the same system has a two-dimensional corner $C \cong \Cl(0,0,1)$, so $\Cl(1,1,1) \cong \Mat_2(\Cl(0,0,1))$.

## technical
A full system of $m \times m$ matrix units inside an algebra, elements multiplying like the elementary matrices and summing to $1$ on the diagonal, exhibits the algebra as $m \times m$ matrices over its corner $E_{11} A E_{11}$: an element $b$ goes to the matrix of its pieces $E_{1i} b E_{j1}$. In a Clifford algebra the units come from an idempotent built on a square-one bivector and a vector that swaps the two idempotents. This is how the hyperbolic plane $\Cl(1,1)$ becomes $2 \times 2$ real matrices, and how a degenerate direction is carried along unchanged in the corner.

## lay
If an algebra contains elements that behave exactly like the basic building blocks of matrices, then the algebra is a matrix algebra: every element can be written as a square array of entries from a smaller algebra. The plane with one space and one time direction gives the simplest example, ordinary $2 \times 2$ matrices.

## one-liner
A full $m \times m$ system of matrix units $E_{ij}$ in $A$ gives $A \cong \Mat_m(E_{11} A E_{11})$ via $b \mapsto (E_{1i} b E_{j1})$; e.g. $\Cl(1,1) \cong \Mat_2(\R)$.
