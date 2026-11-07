---
id: synthesis.imported-bochner-theorem-moment-lemma-and-whitney-even-functions
kind: claim
version: 1
title: 'Imported: Bochner''s theorem, the moment lemma and Whitney''s even functions'
status: imported
region: synthesis
subject: quantum-fields
tags: [classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'S. Bochner, Monotone Funktionen, Stieltjessche Integrale und harmonische Analyse, Math. Ann. 108 (1933), 378--410.'
  key: Bochner1933
- citation: 'E. Lukacs, Characteristic Functions, 2nd ed., Griffin, London (1970).'
  key: Lukacs1970
  locator: 'ch. 2'
- citation: 'H. Whitney, Differentiable even functions, Duke Math. J. 10 (1943), 159--160.'
  key: Whitney1943
outside_ga:
  kind: imported
  why: 'Bochner''s theorem for complex-valued functions on the line, f(tau) = int e^{-i nu tau} d mu(nu), is quoted as its source states it: Fourier analysis of scalar functions in their own right'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: Bochner''s theorem for functions R -> C, f(tau) = int e^{-i nu tau} d mu, is quoted as its source states it, Fourier analysis of scalar functions in their own right; the results that use it read the numbers in span{1, I_4}. Declared imported (version and levels unchanged).'
  note: >-
    Imported so that the occupation-moment criterion (the necessity of finite moments) and the wall result
    (the smoothness in t of solutions even in the proper time) cite these classical lemmas as a Fact instead
    of from memory. Checked on 2026-11-01: Bochner's theorem (a function is a characteristic function if and
    only if it is continuous, positive definite and equal to one at the origin) and the moment property (if
    the derivative of order 2n of a characteristic function exists at zero, the moment of order 2n is
    finite), both against the Encyclopedia of Mathematics article "Characteristic function", which lists
    Lukacs 1970 among its references; Whitney's theorem (every smooth even function f(x) is g(x^2) with g
    smooth, proved by Whitney in the early 1940s) against the introduction of E. Bierstone and P. Milman,
    arXiv:alg-geom/9506001. Cited from memory, not checked: the bibliographic data of Bochner 1933 and of
    Whitney 1943, and the theorem number in Lukacs (Thm. 2.3.1 of the second edition). The finite-measure
    forms below are the probability statements scaled by the total mass.
  unit_note: 'Fourier transforms keep a scalar i: complex analysis on the real line, not the field theory''s unit I4.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created at Leon''s decisions of 2026-11-01 (routine imports for the deposit-state results: the moment lemma, Bochner and Lukacs, and Whitney 1943 on even functions), grouped as one Fact of classical analysis; checked as recorded in the note.'
---

## formal
\begin{enumerate}
\item[(a)] \emph{(Bochner.)} A function $f: \R \to \mathbb{C}$ is of the form $f(\tau) = \int e^{-i\nu\tau}\,d\mu(\nu)$ for a finite positive Borel measure $\mu$ on $\R$ exactly when it is continuous and positive definite ($\sum_{j,l}\bar c_{j}c_{l}f(\tau_{l} - \tau_{j}) \ge 0$ for all finite families); then $\mu(\R) = f(0)$.
\item[(b)] \emph{(The moment lemma; Lukacs, ch.~2.)} If $\mu$ is a finite positive Borel measure on $\R$ and its Fourier transform $f$ has a derivative of order $2k$ at $\tau = 0$, then $\int \nu^{2k}\,d\mu(\nu) < \infty$; then $f$ is of class $C^{2k}$ and $f^{(2k)}(0) = (-1)^{k}\int\nu^{2k}\,d\mu$.
\item[(c)] \emph{(Whitney.)} If $f$ is a smooth even function on an open interval symmetric about $0$, there is a smooth $g$ with $f(x) = g(x^{2})$; if $f$ is smooth and odd, $f(x) = x\,g(x^{2})$ with $g$ smooth (apply the even case to $f(x)/x$, smooth and even by Hadamard's lemma).
\end{enumerate}
\emph{Provenance:} \cite{Bochner1933}; \cite[ch.~2]{Lukacs1970}; \cite{Whitney1943}.

## technical
Three classical lemmas of analysis. Bochner's theorem says that the functions of one real variable that are continuous and positive definite are exactly the Fourier transforms of finite positive measures. The moment lemma of probability theory says that smoothness of such a transform at the origin controls the measure's tail: a derivative of even order $2k$ at the origin forces the moment of order $2k$ to be finite. Whitney's theorem says that a smooth even function of one variable is a smooth function of the square of that variable, and so a smooth odd one is the variable times such a function.

## lay
These are three standard results of mathematical analysis. One says which functions arise as averages of waves with positive weights; another says that if such an average is smooth at its centre, the weights must fall off fast at high frequencies; the third says that a smooth function that is symmetric about zero can be written as a smooth function of the square of its argument. They are taken from the literature.

## one-liner
Bochner: continuous positive-definite functions on $\R$ are the Fourier transforms of finite positive measures; the moment lemma (Lukacs): a derivative of order $2k$ of the transform at $0$ gives a finite moment of order $2k$; Whitney (1943): a smooth even function is $g(x^{2})$ with $g$ smooth, a smooth odd one $x\,g(x^{2})$.
