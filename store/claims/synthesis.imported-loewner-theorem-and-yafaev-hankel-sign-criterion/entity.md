---
id: synthesis.imported-loewner-theorem-and-yafaev-hankel-sign-criterion
kind: claim
version: 1
title: 'Imported: Loewner''s theorem and Yafaev''s Hankel sign criterion'
status: imported
region: synthesis
subject: thermality
tags: [modular-theory, classical-theorem]
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
outside_ga:
  kind: imported
  why: 'two theorems of real and complex analysis (Pick functions on the upper half-plane, Laplace transforms of measures), quoted in their sources'' language'
imported_from:
- citation: 'K. Loewner, Ueber monotone Matrixfunktionen, Math. Z. 38 (1934), 177--216.'
  key: Loewner1934
  locator: 'the characterisation of operator monotone functions on an interval by positivity of all Loewner matrices and by analytic continuation to Pick functions; cited from memory'
  doi: 10.1007/BF01170633
- citation: 'D. R. Yafaev, Criteria for Hankel operators to be sign-definite, Anal. PDE 8 (2015), 183--221; arXiv:1303.4040.'
  key: Yafaev2015
  locator: 'Theorem 4.7 of the arXiv version, Theorem 4.9 of the journal version: a nonnegative Hankel form has a kernel that is the Laplace transform of a positive measure; abstract: the sign-function criterion'
  doi: 10.2140/apde.2015.8.183
extraction:
  note: >-
    Imported so that the result on field-level geometric modular conjugations on a horizon generator can pin the
    two analytic theorems its positivity step uses (Loewner's theorem, and Yafaev's representation as an
    alternative route). Checked on 6 November 2026: the bibliographic data of Loewner 1934 (author, journal,
    volume 38, issue 1, pages 177-216, DOI) against the Crossref record; the bibliographic data of Yafaev 2015
    (Anal. PDE 8, no. 1, pages 183-221) against the Crossref record; the abstract of arXiv:1303.4040 (the
    multiplicities of the positive and negative spectrum of a self-adjoint Hankel operator equal those of
    multiplication by its sign-function, so the operator is sign-definite exactly when the sign-function is, and
    the kernel has an exponential representation); and the theorem giving the Laplace representation of a
    nonnegative Hankel kernel, numbered 4.7 in the arXiv PDF and 4.9 in the journal PDF (read through a
    summarising fetch, not line by line). Cited from memory, not checked against the source: the statement of
    Loewner's theorem in clause (a), including the closed form of the Pick extension and the continuation across
    the interval; this is the textbook form (for example in Donoghue's or Simon's monographs, also not checked).
  maintainer_pass:
    by: maintainer-2026-11-06
    date: '2026-11-06'
    note: 'Created so that synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state cites Loewner''s theorem and Yafaev''s criterion as a Fact rather than from memory; partly verified (see note).'
---

## formal
\begin{enumerate}
\item[(a)] (Loewner.) Let $I$ be an open interval of $\R$ and $f : I \to \R$. The following are equivalent: $f$ is operator monotone on $I$ ($A \le B$ implies $f(A) \le f(B)$ for self-adjoint matrices of every size with spectra in $I$); every Loewner matrix $\big[(f(x_{k}) - f(x_{l}))/(x_{k} - x_{l})\big]_{k,l}$, with $f'(x_{k})$ on the diagonal, for finitely many distinct points $x_{k} \in I$, is positive semidefinite (for $f$ continuously differentiable); $f$ is the restriction to $I$ of a Pick function, analytic on the upper half-plane with nonnegative imaginary part there, which continues analytically across $I$ into the lower half-plane by reflection.
\item[(b)] (Yafaev.) Let $h$ be a distribution on $(0, \infty)$ in the class of the source, defining the Hankel form $\int_{0}^{\infty}\int_{0}^{\infty}h(t + s)f(s)\overline{f(t)}\,ds\,dt$ on test functions $f$ on $(0, \infty)$. If the form is nonnegative, then $h(t) = \int_{0}^{\infty}e^{-t\lambda}\,dm(\lambda)$ with a positive measure $m$ of at most polynomial growth. More generally the numbers of positive and negative eigenvalues of the Hankel operator equal those of multiplication by its sign-function $s$, so the operator is nonnegative exactly when $s \ge 0$.
\end{enumerate}
\emph{Provenance:} \cite{Loewner1934}; \cite[Theorem 4.7 (arXiv), Theorem 4.9 (journal)]{Yafaev2015}.

## technical
Loewner's theorem characterises the real functions that preserve the order of self-adjoint matrices on an interval: they are exactly those whose divided-difference (Loewner) matrices are all positive semidefinite, and exactly the restrictions of Pick functions, analytic in the upper half-plane with nonnegative imaginary part, that continue across the interval. Yafaev's criterion characterises sign-definite Hankel operators on the half-line: a Hankel form is nonnegative exactly when the sign-function attached to its kernel is, and a nonnegative Hankel kernel is the Laplace transform of a positive measure, so the associated function is a Stieltjes function, a special Pick function. Both are taken from the literature; in the store they turn a positivity condition on a reflection-positivity form along a light ray into a condition on occupation numbers.

## lay
Two classical results from analysis. One says which functions keep the ordering of matrices: those that extend to a particular kind of function in the complex plane whose imaginary part is never negative. The other says when a certain kind of infinite matrix, built from one function along a half-line, is positive: exactly when that function is an average of decaying exponentials with positive weights. They are taken from the literature.

## one-liner
A real function on an open interval is operator monotone, equivalently has all Loewner matrices positive, exactly when it extends to a Pick function continuing across the interval (Loewner 1934); a nonnegative Hankel form on the half-line has a kernel that is the Laplace transform of a positive measure, and sign-definiteness is that of its sign-function (Yafaev 2015).
