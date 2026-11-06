---
id: synthesis.imported-ford-parker-infrared-divergence
kind: claim
version: 1
title: 'Imported: infrared divergence of red scalar spectra (Ford and Parker 1977)'
status: imported
region: synthesis
subject: dark-energy
tags: [frozen-point, cosmological-constant, classical-theorem]
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
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'L. H. Ford and L. Parker, Infrared divergences in a class of Robertson-Walker universes, Phys. Rev. D 16 (1977), 245--250.'
  key: FordParker1977
  doi: 10.1103/PhysRevD.16.245
- citation: 'A. Higuchi and N. Rendell, Infrared divergences for free quantum fields in cosmological spacetimes, arXiv:1711.03964.'
  key: HiguchiRendell2017
  locator: 'Sec. 3'
extraction:
  note: >-
    Imported so that the results on the deposit's infrared data, on the stored sudden start and on the de
    Sitter-invariant state can cite the infrared divergence of the massless Bunch-Davies state as a Fact
    instead of as standard. Checked on 2026-11-01: Ford and Parker 1977 against the Crossref record of DOI
    10.1103/PhysRevD.16.245 (title, authors, Physical Review D 16, issue 2, pages 245-250, 15 July 1977); its
    content (the infrared divergence of the two-point function of massless minimally coupled fields in a
    class of power-law Robertson-Walker universes) is cited from memory, the abstract not being available.
    The general criterion, divergence of the momentum integral at small momentum when the mode index is at
    least (n - 1)/2 in n spacetime dimensions, and the infrared divergence of the massless minimally coupled
    scalar's two-point function, checked against Higuchi and Rendell, arXiv:1711.03964 (ar5iv text, Sec. 3);
    their journal reference is not recorded. The variance statements for smeared slice fields are elementary
    consequences of the mode integral, stated here for the use the store makes of them.
  unit_note: 'Complex mode functions and Fourier transforms keep a scalar i: they are numbers of the imported Hilbert space, not the field theory''s unit I4.'
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created at Leon''s decisions of 2026-11-01 (routine import for the deposit-state results: Ford and Parker 1977), checked as recorded in the note.'
---

## formal
Let $\phi$ be a free real scalar field on a spatially flat Robertson-Walker gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with conformal time $\eta$ and scale factor $a(\eta)$, and $\omega$ a homogeneous isotropic quasi-free state with mode functions $\chi_{k}(\eta)$ of $a\phi$ (Wronskian normalised), so that on a slice $\eta = \eta_{d}$ the smeared field $\phi(g) = \int g(\vec x)\phi(\eta_{d}, \vec x)\,d^{3}x$ has
\[
\omega(\phi(g)^{2}) = a(\eta_{d})^{-2}\int\frac{d^{3}k}{(2\pi)^{3}}\,|\hat g(\vec k)|^{2}\,|\chi_{k}(\eta_{d})|^{2}.
\]
\begin{enumerate}
\item[(a)] \emph{(The criterion; Higuchi and Rendell, Sec.~3, four dimensions.)} If $|\chi_{k}(\eta_{d})|^{2} \ge c\,k^{-2\nu}$ on some $(0, k_{0})$ with $c > 0$ and $\nu \ge \tfrac32$, the momentum integral of the equal-time two-point function diverges at small $k$.
\item[(b)] \emph{(Ford and Parker.)} The massless minimally coupled field on the de Sitter field ($a = -1/(H\eta)$, mode index $\nu = \tfrac32$) in its Bunch-Davies state, and on a class of power-law Robertson-Walker fields in the corresponding homogeneous states, has an infrared-divergent two-point function.
\item[(c)] \emph{(Smeared slice fields; elementary.)} Under (a), $\omega(\phi(g)^{2}) = \infty$ for every test function $g$ of nonzero mean, $\int g \neq 0$, since $|\hat g|^{2}$ is continuous with value $|\int g|^{2}$ at $k = 0$; for $\tfrac32 \le \nu < \tfrac52$, $|\chi_{k}|^{2} \le C k^{-2\nu}$ near $k = 0$ and $|\chi_{k}|^{2}$ polynomially bounded at large $k$, every test function of zero mean gives a finite value, since then $|\hat g(\vec k)|^{2} \le C' k^{2}$. So such a state is not a state on the algebra of slice fields of nonzero mean; restricted to fields smeared with test functions of zero mean (or to derivatives of the field) it is.
\end{enumerate}
\emph{Provenance:} \cite{FordParker1977}; \cite[Sec.~3]{HiguchiRendell2017}.

## technical
For a massless field with no coupling to the curvature, the natural homogeneous states of an expanding universe can carry so much power at the longest wavelengths that the field's correlation function does not exist: the integral over momenta diverges at small momenta. Ford and Parker found this in a class of power-law expanding universes, and it holds for the massless minimally coupled field in its Bunch-Davies state on de Sitter, where the mode functions grow as the inverse three-halves power of the momentum. In terms of smeared fields on a slice, a field averaged with a profile of nonzero total weight then has infinite variance, while profiles of zero total weight, or derivatives of the field, have finite variance. So, if the mode power grows at least that fast, the divergence is a statement about which observables the state is defined on.

## lay
In an expanding universe, a field of massless particles that ignores the curvature of space can pile up fluctuations on ever larger scales; if it does so fast enough, so much that the average value of the field over any region fluctuates infinitely. Ford and Parker found this in 1977. Differences of the field between nearby places stay finite, so the problem concerns only averages over regions. This is taken from the literature.

## one-liner
On spatially flat Robertson-Walker fields, if a homogeneous scalar state's modes grow as $k^{-\nu}$, $\nu \ge \tfrac32$, at small momentum, it has an infrared-divergent two-point function, as the massless minimally coupled Bunch-Davies state does (Ford and Parker 1977): slice fields of nonzero mean have infinite variance, those of zero mean finite variance for $\nu < \tfrac52$.
