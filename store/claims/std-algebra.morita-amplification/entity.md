---
id: std-algebra.morita-amplification
kind: claim
version: 1
title: An algebra and its matrix amplification
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- idempotents
- representation-theory
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
  - std-algebra.matrix-units@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_centre_and_ideals_of_the_amplification
locators:
  sources:
  - key: Lam1999
    locator: matrix rings, idempotents and Morita theory
extraction:
  by: algebra-core-2026-10-26
---

## formal
Let $A$ be a unital real algebra and $m \ge 1$, and let $E_{ij}$ be the matrix units of $\Mat_m(A)$. Then:
\begin{enumerate}
\item[(i)] the centre of $\Mat_m(A)$ is $\{z \cdot 1_m : z \in \Zc(A)\}$;
\item[(ii)] the two-sided ideals of $\Mat_m(A)$ are exactly the $\Mat_m(I)$ with $I$ a two-sided ideal of $A$;
\item[(iii)] $M \mapsto M^{m}$ (columns, acted on by matrix multiplication) and $N \mapsto E_{11} N$ are mutually inverse equivalences between left $A$-modules and left $\Mat_m(A)$-modules, so $A$ and $\Mat_m(A)$ are Morita equivalent.
\end{enumerate}
With \claimref{std-algebra.matrix-units}: an algebra with a full $m \times m$ system of matrix units has the centre, the ideals and the modules of its corner.

## technical
Passing from an algebra to its $m \times m$ matrices changes nothing structural: the centre is the old centre placed on the diagonal, the ideals are the matrices with entries in an old ideal, and the modules correspond one to one (column vectors one way, the first-row corner the other). This is Morita equivalence. Combined with matrix units, a Clifford algebra and its corner have the same centre, ideals and representations.

## lay
Taking square arrays of elements of an algebra gives a bigger algebra with the same essential structure: the same central elements, the same ways of being cut down, and the same ways of acting on things.

## one-liner
$\Zc(\Mat_m(A)) = \Zc(A)$, the ideals of $\Mat_m(A)$ are $\Mat_m(I)$, and $A$ and $\Mat_m(A)$ have equivalent module categories.
