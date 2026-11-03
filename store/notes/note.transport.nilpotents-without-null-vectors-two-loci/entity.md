---
id: note.transport.nilpotents-without-null-vectors-two-loci
kind: note
version: 1
title: 'Nilpotents without null vectors: the two loci differ'
status: example
subject: zero-divisors
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
comments_on:
- transport.existence-locus-type-n
locators:
  paper: T01
  number: Ex 3.5
  label: ex:cl20
  line: 598
---

## formal
$\Cl(2,0) \cong \Mat_2(\R)$ has definite signature: no null vectors, by Proposition \claimref{transport.existence-locus-type-n}. It nevertheless contains nilpotents, e.g.
\[
x = (1 + e_1)\,e_2, \qquad x^2 = (1+e_1)\,e_2\,(1+e_1)\,e_2 = (1+e_1)(1-e_1)\,e_2^2 = 0,
\]
using $e_2 e_1 = -e_1 e_2$ and $e_1^2 = e_2^2 = 1$. A loose reading of type N, as comprising null vectors and more generally the elements they generate, therefore needs care: the \emph{nilpotency} locus (nonzero $x$ with $x^k = 0$) is strictly larger than the locus of algebras with isotropic vectors, and it is the latter, the grade-one geometric obstruction, that defines type N and triggers Rule 1. The nilpotent $x$ above is instead type-P-generated: $x = 2\,\varepsilon\, e_2$ with $\varepsilon = \tfrac12(1 + e_1)$ a non-central idempotent, and $x$ is annihilated by the idempotent $1 - \varepsilon$ on the left. In matrix form ($e_1 \mapsto \mathrm{diag}(1,-1)$, $e_2 \mapsto \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix}$), $x \mapsto 2E_{12}$: the standard nilpotent matrix unit, built from idempotents and invertible vectors with no isotropic vector anywhere in $\mathbb{V}$.

## technical
pending

## lay
pending

## one-liner
pending
