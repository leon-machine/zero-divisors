---
id: synthesis.imported-mehler-formula-hermite-rank-and-power-law-spectra
kind: claim
version: 1
title: 'Imported: Mehler''s formula, Hermite rank and power-law spectra'
status: imported
region: synthesis
subject: dark-energy
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
- citation: 'F. G. Mehler, Ueber die Entwicklung einer Function von beliebig vielen Variablen nach Laplaceschen Functionen hoeherer Ordnung, J. Reine Angew. Math. 66 (1866), 161--176.'
  key: Mehler1866
- citation: 'M. S. Taqqu, Weak convergence to fractional Brownian motion and to the Rosenblatt process, Z. Wahrscheinlichkeitstheorie verw. Gebiete 31 (1975), 287--302.'
  key: Taqqu1975
- citation: 'R. L. Dobrushin and P. Major, Non-central limit theorems for non-linear functionals of Gaussian fields, Z. Wahrscheinlichkeitstheorie verw. Gebiete 50 (1979), 27--52.'
  key: DobrushinMajor1979
  locator: 'eq. (1.11) and Theorem 1'
- citation: 'V. I. Kolyada, Fractional integrals and Fourier transforms, arXiv:1709.07195.'
  locator: 'Section 3 (Riesz potentials)'
  url: https://arxiv.org/abs/1709.07195
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the Fourier kernel e^{-i k.x} is quoted from the sources; declared (version and levels unchanged).'
  note: >-
    Imported so that synthesis.local-conversion-cannot-redden-a-gaussian-spectator can pin the
    Gaussian identities it cited from memory. Checked on 2026-11-01 against Dobrushin and Major 1979
    (the authors' PDF): the bibliographic data, the identity E[H_k(xi) H_j(eta)] = delta_kj k! r^k
    for jointly Gaussian unit-variance variables with correlation r (their eq. (1.11)), the index k
    as the smallest index with a nonzero coefficient in the Hermite expansion (their Theorem 1), the
    hypothesis r(n) ~ n^-alpha L(n), and their reference to Taqqu 1975 with its bibliographic data.
    The definition of the Hermite rank as the index of the first nonzero coefficient was also
    checked against arXiv:1802.05626. The three-dimensional Fourier constant was checked against the
    Riesz-potential constant of Kolyada (arXiv:1709.07195, Section 3) and its reduction to 4 pi
    Gamma(2 - beta) sin(pi(2 - beta)/2) recomputed at six values of beta; the Abelian statement for
    a correlation that is a power law only at large separation is standard and cited from memory.
    Mehler 1866 is cited from memory (bibliographic data not checked). The correlation of a
    Hermite-rank-q function falling as the q-th power of the field's correlation is the consequence
    of the identity used by both papers, written out here.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Leon approved the import of Mehler''s formula, the Hermite-rank result and the Fourier asymptotics of a power-law correlation as routine Facts).'
outside_ga:
  kind: imported
  why: 'the Fourier convention P(k) = int e^{-i k.x} xi(x) d^3x is quoted as the sources state it, Fourier analysis of scalar functions'
---

## formal
Let $(X, Y)$ be jointly Gaussian with mean $0$, variance $1$ and correlation $\rho$, and let $\mathrm{He}_{n}$ be the Hermite polynomials orthogonal for the standard Gaussian weight ($\mathrm{He}_{0} = 1$, $\mathrm{He}_{1}(x) = x$, $\mathrm{He}_{2}(x) = x^{2} - 1$). Then
\[
E\bigl[\mathrm{He}_{m}(X)\,\mathrm{He}_{n}(Y)\bigr] = \delta_{mn}\, n!\, \rho^{n}.
\]
Consequently, for $f$ square-integrable against the Gaussian weight with expansion $f = \sum_{n \ge 0} c_{n}\mathrm{He}_{n}$, $\mathrm{Cov}(f(X), f(Y)) = \sum_{n \ge 1} c_{n}^{2}\, n!\, \rho^{n}$, a series with nonnegative coefficients. The Hermite rank of $f$ is the least $q \ge 1$ with $c_{q} \ne 0$. For a stationary Gaussian field of unit variance whose correlation is $\rho(r) = A r^{-m}(1 + o(1))$ as $r \to \infty$, $m > 0$, the correlation of $f$ of the field is therefore $c_{q}^{2}\, q!\, A^{q} r^{-qm}(1 + o(1))$: the rank-$q$ term dominates at large separation, and the limit theorems for sums of such functionals (non-central when $qm$ is below the dimension) are governed by $q$. In three dimensions, the Fourier transform of $r^{-\beta}$, $0 < \beta < 3$, is $C(\beta)\,k^{\beta - 3}$ with
\[
C(\beta) = \pi^{3/2}\,2^{3 - \beta}\,\frac{\Gamma\bigl(\tfrac{3 - \beta}{2}\bigr)}{\Gamma\bigl(\tfrac{\beta}{2}\bigr)} = 4\pi\,\Gamma(2 - \beta)\,\sin\bigl(\tfrac{\pi}{2}(2 - \beta)\bigr) > 0
\]
(the second form read by continuity at $\beta = 1$ and $\beta = 2$, where $C = 4\pi$ and $2\pi^{2}$), in the convention $P(k) = \int e^{-i\mathbf{k}\cdot\mathbf{x}}\xi(\mathbf{x})\,d^{3}x$; and a locally integrable correlation equal to $B r^{-\beta}(1 + O(r^{-\delta}))$ at large $r$, $\delta > 0$, has $P(k) = B\,C(\beta)\,k^{\beta - 3}(1 + o(1))$ as $k \to 0$. \emph{Provenance:} \cite{Mehler1866}, \cite{Taqqu1975}, \cite{DobrushinMajor1979} (eq. (1.11), Theorem 1); the Fourier constant is the Riesz-potential constant (Kolyada, arXiv:1709.07195, Section 3).

## technical
Functions of a Gaussian variable are expanded in Hermite polynomials, and Mehler's formula says that the polynomials of two correlated Gaussian variables are uncorrelated unless their degrees agree, with covariance $n!\rho^{n}$ at degree $n$. So the covariance of any function of a Gaussian field is a power series in the field's correlation with nonnegative coefficients, and its leading term at large separation is the power set by the first nonzero Hermite coefficient, the Hermite rank. This is the basis of the classical limit theorems for functionals of long-range dependent Gaussian sequences (Taqqu; Dobrushin and Major). The companion fact is the Fourier transform of a power law in three dimensions: a correlation falling as $r^{-\beta}$ has a spectrum rising as $k^{\beta - 3}$ at small $k$, with a positive constant for $0 < \beta < 3$.

## lay
If a quantity is a fixed function of a randomly fluctuating field with the bell-curve statistics, how its values at two places are related follows from how the field's values are related, through a simple formula found by Mehler in 1866. The upshot, used by probabilists since the 1970s, is that such a function can only make long-distance correlations weaker, never stronger. A second standard formula turns a correlation that falls off as a power of distance into the corresponding power law in wavenumber.

## one-liner
$E[\mathrm{He}_{m}(X)\mathrm{He}_{n}(Y)] = \delta_{mn}n!\rho^{n}$, so $\mathrm{Cov}(f(X), f(Y)) = \sum_{n \ge 1} c_{n}^{2}n!\rho^{n}$ and a rank-$q$ function of a field with correlation $r^{-m}$ has correlation $r^{-qm}$; in three dimensions $r^{-\beta}$ transforms to $4\pi\Gamma(2 - \beta)\sin(\tfrac{\pi}{2}(2 - \beta))\,k^{\beta - 3}$ for $0 < \beta < 3$.
