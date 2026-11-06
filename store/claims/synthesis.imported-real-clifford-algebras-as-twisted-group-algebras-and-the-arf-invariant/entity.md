---
id: synthesis.imported-real-clifford-algebras-as-twisted-group-algebras-and-the-arf-invariant
kind: claim
version: 1
title: 'Imported: real Clifford algebras as twisted group algebras and the Arf invariant'
status: imported
region: synthesis
subject: clifford-structure
tags: [clifford-classification, grading-and-parity, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-06
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'V. Ovsienko, Real Clifford algebras and quadratic forms over F_2: two old problems become one, arXiv:1601.07664 (2016).'
  key: Ovsienko2016
  locator: 'Proposition 3.1 (after Albuquerque and Majid: Cl(p,q) is the twisted group algebra of F_2^n with the bilinear twisting function f(x,y) = sum_{j<i} x_i y_j + sum_{i>p} x_i y_i); Theorem 1 (two such twisted group algebras with bilinear twisting functions are isomorphic if and only if the quadratic forms alpha(x) = f(x,x) are equivalent); introduction (the difference between real and quaternionic matrix algebras is measured by the Arf invariant)'
- citation: 'A. Elduque and A. Rodrigo-Escudero, Clifford algebras as twisted group algebras and the Arf invariant, Adv. Appl. Clifford Algebras 28 (2018), no. 2, article 41; arXiv:1801.07002.'
  key: ElduqueRodrigoEscudero2018
  locator: 'abstract: connections between quadratic forms over the two-element field, real Clifford algebras, real graded division algebras and twisted group algebras; real Clifford algebras revisited through the Arf invariant of the associated quadratic forms, with new proofs of classical results'
  doi: 10.1007/s00006-018-0862-y
extraction:
  note: >-
    Imported so that the result on blade square signs as a quadratic form over the two-element field can pin the
    published statements it restates. Checked on 6 November 2026 against the arXiv text of 1601.07664 (title,
    author, Proposition 3.1 with its twisting function, Theorem 1, and the introduction's statement on the Arf
    invariant) and the arXiv abstract of 1801.07002 (title, authors), with the journal data of the latter
    (Adv. Appl. Clifford Algebras 28, no. 2, article 41, 2018, DOI) checked against the University of Zaragoza
    repository record. Not checked: a journal reference for Ovsienko's paper (none was found), and whether either
    paper states the Gauss-sum or trace-form formula of the result that uses this Fact; the explicit form of the
    quadratic form in clause (a) is the twisting function evaluated on the diagonal, with x_i^2 = x_i.
  maintainer_pass:
    by: maintainer-2026-11-06
    date: '2026-11-06'
    note: 'Created so that synthesis.blade-square-signs-f2-quadratic-form cites its published prior art as a Fact; verified against the arXiv texts (see note).'
---

## formal
Let $\Cl(p,q)$, $n = p + q$, have orthonormal generators $e_{1}, \dots, e_{n}$ with $Q(e_{i}) = +1$ for $i \le p$ and $Q(e_{i}) = -1$ for $i > p$, and identify $x \in \mathbb{F}_{2}^{n}$ with the blade $e_{x}$, the increasing product of the $e_{i}$ with $x_{i} = 1$.
\begin{enumerate}
\item[(a)] (Twisted group algebra; Ovsienko, after Albuquerque and Majid.) $\Cl(p,q)$ is the twisted group algebra of $\mathbb{F}_{2}^{n}$ over $\R$ with $e_{x}e_{y} = (-1)^{f(x,y)}e_{x+y}$ and the bilinear twisting function $f(x, y) = \sum_{1 \le j < i \le n}x_{i}y_{j} + \sum_{p < i \le n}x_{i}y_{i}$; the associated quadratic form is $\alpha(x) = f(x, x) = \sum_{j < i}x_{i}x_{j} + \sum_{i > p}x_{i}$, so $e_{x}^{2} = (-1)^{\alpha(x)}$, and its polar form $\alpha(x + y) + \alpha(x) + \alpha(y) = f(x, y) + f(y, x)$ records anticommutation.
\item[(b)] (Ovsienko, Theorem 1.) Two twisted group algebras of $\mathbb{F}_{2}^{n}$ over $\R$ with bilinear twisting functions are isomorphic if and only if their quadratic forms are equivalent over $\mathbb{F}_{2}$. In particular the classification of the real Clifford algebras is the classification of the forms $\alpha_{(p,q)}$.
\item[(c)] (The Arf invariant; Ovsienko; Elduque and Rodrigo-Escudero.) For nondegenerate polar form the Arf invariant of $\alpha_{(p,q)}$ separates the real matrix algebras (Arf invariant $0$) from the quaternionic ones (Arf invariant $1$); Elduque and Rodrigo-Escudero revisit the classification of real Clifford algebras, with new proofs of classical results, through the Arf invariant of these forms.
\end{enumerate}
\emph{Provenance:} \cite{Ovsienko2016}; \cite{ElduqueRodrigoEscudero2018}.

## technical
A real Clifford algebra is a twisted group algebra of a vector space over the two-element field: the basis blades are indexed by subsets of the generators, multiplication adds the index sets, and a sign is given by a bilinear function on the index sets. Evaluated on the diagonal it gives a quadratic form over the two-element field that records which blades square to minus one, and its polar form records which pairs anticommute. Ovsienko proved that two such twisted group algebras are isomorphic exactly when their quadratic forms are equivalent, so the classification of real Clifford algebras and that of quadratic forms over the two-element field are one problem, and that the Arf invariant distinguishes real from quaternionic matrix algebras; Elduque and Rodrigo-Escudero revisit the classification through the Arf invariant. Both are taken from the literature.

## lay
Whether the products of basic directions in one of these algebras square to plus or to minus one can be written as a yes-or-no table, and published work shows that this table, read as a simple algebraic form, already determines which algebra one has, including whether it is built on real numbers or quaternions. The results are taken from the literature.

## one-liner
$\Cl(p,q)$ is the twisted group algebra of $\mathbb{F}_{2}^{n}$ with twisting $f(x,y) = \sum_{j<i}x_{i}y_{j} + \sum_{i>p}x_{i}y_{i}$, so $e_{x}^{2} = (-1)^{\alpha(x)}$ with $\alpha(x) = f(x,x)$; two such algebras are isomorphic exactly when their quadratic forms are equivalent, and the Arf invariant separates real from quaternionic matrix algebras (Ovsienko 2016; Elduque and Rodrigo-Escudero 2018).
