---
id: synthesis.imported-hurwitz-zeta-values-and-dirichlet-l-functions-as-hurwitz-sums
kind: claim
version: 1
title: 'Imported: Hurwitz zeta values at 0 and -1; Dirichlet L-functions as Hurwitz sums'
status: imported
region: synthesis
subject: thermality
tags: [classical-theorem]
proposed_by:
  kind: ai
  session: 2026-11-24-number-theory
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-24-number-theory
review: draft
imported_from:
- citation: 'A. Hurwitz, Einige Eigenschaften der Dirichlet''schen Functionen $F(s) = \sum(\frac{D}{n})\cdot\frac{1}{n^{s}}$, die bei der Bestimmung der Classenanzahlen bin\"arer quadratischer Formen auftreten, Z. Math. Phys. 27 (1882), 86--101.'
  key: Hurwitz1882
  locator: 'the continuation of the zeta function with a shift; cited from memory, not read'
- citation: 'T. M. Apostol, Introduction to Analytic Number Theory, Undergraduate Texts in Mathematics, Springer, New York (1976).'
  key: Apostol1976
  locator: 'Ch.~12: the continuation of the Hurwitz zeta function, its values at non-positive integers in terms of Bernoulli polynomials, and the expression of a Dirichlet L-function through it; cited from memory, not read for this entry'
extraction:
  note: >-
    Imported by Leon's decision of 24 November 2026, as hypothesis (H1) of
    synthesis.character-sums-over-the-twist-fibres-of-an-array-are-dirichlet-l-values, which before stated it
    in its own text. NOT checked against the sources: the statements and the bibliographic data are cited from
    memory. Support that is not a check of the sources: with these values the L-values of twelve real characters
    computed in the using result agree with class numbers counted directly and with a divisor-sum formula (two
    further imported Facts), and $\zeta(0) = -\tfrac12$, $\zeta(-1) = -\tfrac1{12}$ are the cases $a = 1$. The
    store already uses the value $\zeta(-1, a) = -\tfrac12 B_{2}(a)$ in its zeta-regularised sea energies
    (synthesis.null-ordering-of-counted-units-is-zeta-symmetric), where it is derived for the purpose; this
    Fact adds the value at $0$ and the decomposition of an L-function. Characters take values in
    $\mathrm{span}\{1, I_{4}\}$ by the unit principle; the sources write complex numbers. Not part of this Fact:
    functional equations, values at positive integers, anything about zeros.
outside_ga:
  kind: imported
  why: 'Classical analytic number theory: the analytic continuation of Dirichlet series in a scalar variable. Scalars only; the sources write complex values, read here in span{1, I_4}.'
---

## formal
Cited from memory and not checked against the sources. Numbers are read in $\mathrm{span}\{1, I_{4}\}$ (conventions, the unit principle, U1). For $0 < a \le 1$ the \emph{Hurwitz zeta function} is $\zeta(s, a) = \sum_{k \ge 0}(k + a)^{-s}$ for $\operatorname{Re}s > 1$.
\begin{enumerate}
\item[(i)] $\zeta(s, a)$ continues analytically to all $s \ne 1$.
\item[(ii)] $\zeta(0, a) = \tfrac12 - a$ and $\zeta(-1, a) = -\tfrac12 B_{2}(a)$, with $B_{2}(a) = a^{2} - a + \tfrac16$. (In general $\zeta(1 - k, a) = -B_{k}(a)/k$ for the Bernoulli polynomials $B_{k}$, $k \ge 1$, with $B_{1}(a) = a - \tfrac12$.)
\item[(iii)] Let $f \ge 1$ and let $\chi$ be a function on the integers with period $f$ and values in $\mathrm{span}\{1, I_{4}\}$. Then $L(s, \chi) = \sum_{m \ge 1}\chi(m)m^{-s}$ satisfies, for $\operatorname{Re}s > 1$,
\[
L(s, \chi) = f^{-s}\sum_{a = 1}^{f}\chi(a)\,\zeta\bigl(s, \tfrac{a}{f}\bigr),
\]
so it continues analytically to all $s \ne 1$, and to $s = 1$ as well when $\sum_{a = 1}^{f}\chi(a) = 0$; and
\[
L(0, \chi) = \sum_{a = 1}^{f}\chi(a)\bigl(\tfrac12 - \tfrac{a}{f}\bigr), \qquad L(-1, \chi) = -\frac{f}{2}\sum_{a = 1}^{f}\chi(a)\,B_{2}\bigl(\tfrac{a}{f}\bigr).
\]
\item[(iv)] If $\chi$ as in (iii) is completely multiplicative, $L(s, \chi) = \prod_{p}(1 - \chi(p)p^{-s})^{-1}$ for $\operatorname{Re}s > 1$; so if $\chi'$ agrees with $\chi$ at the integers prime to a finite set $P$ of primes and vanishes at the others, $L(s, \chi') = L(s, \chi)\prod_{p \in P}(1 - \chi(p)p^{-s})$ for all $s \ne 1$ by continuation.
\end{enumerate}

## technical
The Riemann zeta function with a shift, $\sum(k + a)^{-s}$, continues to the whole plane apart from $s = 1$, and its values at $0, -1, -2, \dots$ are Bernoulli polynomials in the shift, up to a factor. A Dirichlet series with periodic coefficients is a finite combination of such functions, one for each residue, so its values at non-positive integers are finite sums of Bernoulli polynomials weighted by the coefficients: the generalised Bernoulli numbers. Removing the Euler factors at finitely many primes multiplies the function by the corresponding factors. These are classical results (Hurwitz; a textbook account is in Apostol's chapter on the Hurwitz zeta function), cited from memory.

## lay
Sums like $1 + \tfrac14 + \tfrac19 + \dots$ can be given a meaning even where they do not converge, by a standard extension. For the sums that start at a shifted point, the extended values at $0$ and $-1$ are simple polynomials in the shift. The store uses these values and takes them from the classical literature.

## one-liner
Imported (Hurwitz 1882; Apostol, ch. 12; from memory): $\zeta(s, a) = \sum_{k \ge 0}(k + a)^{-s}$ continues analytically with $\zeta(0, a) = \tfrac12 - a$, $\zeta(-1, a) = -\tfrac12 B_{2}(a)$; a Dirichlet series with coefficients of period $f$ is $f^{-s}\sum_{a}\chi(a)\zeta(s, a/f)$, so $L(0, \chi) = \sum_{a}\chi(a)(\tfrac12 - \tfrac af)$ and $L(-1, \chi) = -\tfrac f2\sum_{a}\chi(a)B_{2}(\tfrac af)$; dropping the Euler factors at a finite set of primes multiplies $L(s, \chi)$ by $\prod(1 - \chi(p)p^{-s})$.
