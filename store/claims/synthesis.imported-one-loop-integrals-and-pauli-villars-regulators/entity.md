---
id: synthesis.imported-one-loop-integrals-and-pauli-villars-regulators
kind: claim
version: 1
title: 'Imported: one-loop integrals and Pauli-Villars regulators'
status: imported
region: synthesis
subject: quantum-fields
tags: [scattering-amplitudes, gauge-fields, classical-theorem, recovers-known-physics]
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
- citation: 'W. Pauli and F. Villars, On the invariant regularization in relativistic quantum theory, Rev. Mod. Phys. 21 (1949), 434--444.'
  key: PauliVillars1949
  doi: 10.1103/RevModPhys.21.434
- citation: 'M. E. Peskin and D. V. Schroeder, An Introduction to Quantum Field Theory, Addison-Wesley (1995), chapters 6 and 7.'
  key: PeskinSchroeder1995
- citation: 'S. Weinzierl, Introduction to Feynman integrals, arXiv:1005.1855, equations (50) and (61).'
  key: Weinzierl2010
extraction:
  note: >-
    Imported so that one-loop electrodynamics in the spacetime algebra can pin its loop machinery instead of
    citing it from memory. Checked on 2026-11-01: the bibliographic data of Pauli and Villars (title, Rev. Mod.
    Phys. 21, 434-444, 1949, DOI) against the INSPIRE record; the Feynman-parameter formula (product of
    propagator powers as a Gamma-weighted integral over the simplex with the delta function) against Weinzierl,
    arXiv:1005.1855, equation (50), and the Wick rotation of a Minkowski integral to a Euclidean one against the
    same text, equation (61). Cited from memory, not checked against the source: the closed forms of the
    integrals in (ii) (they are the standard Gamma-function evaluation, recomputed in the citing result), the
    content of Pauli and Villars beyond the title (regulator fields with the conditions of (iii)), the
    gauge-parameter independence of on-shell amplitudes and the Feynman-gauge propagator, and the equation
    numbers of Peskin and Schroeder ((6.47), (7.90)) quoted by the citing result.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (the one-loop machinery as a Fact, by Leon''s list of imports).'
---

## formal
Signature $(+,-,-,-)$, $\ell^{2} = Q(\ell)$, units $\hbar = c = 1$.
\begin{enumerate}
\item[(i)] \emph{(Feynman parametrisation.)} For nonzero $D_{1}, \ldots, D_{n}$ of one sign, $\dfrac{1}{D_{1}\cdots D_{n}} = (n-1)!\displaystyle\int_{0}^{1}\!dx_{1}\cdots dx_{n}\,\frac{\delta(1 - \sum_{j}x_{j})}{(\sum_{j}x_{j}D_{j})^{n}}$ \cite{Weinzierl2010}.
\item[(ii)] \emph{(Wick-rotated integrals.)} After the rotation $\ell_{0} = i\ell_{E,0}$, which takes $\int d^{4}\ell\,f(-\ell^{2})$ to $i\int d^{4}\ell_{E}\,f(\ell_{E}^{2})$ \cite{Weinzierl2010}, for $\Delta > 0$: $\int\frac{d^{4}\ell}{(2\pi)^{4}}(\ell^{2} - \Delta)^{-3} = \frac{-i}{32\pi^{2}\Delta}$; with the Euclidean cut-off $\ell_{E}^{2} \le L$, $\int\frac{d^{4}\ell}{(2\pi)^{4}}(\ell^{2} - \Delta)^{-2} = \frac{i}{16\pi^{2}}\bigl(\ln(L/\Delta) - 1 + O(\Delta/L)\bigr)$. Terms odd in $\ell$ integrate to zero and $\ell^{\alpha}\ell^{\beta} \to \tfrac14 Q(\ell)g^{\alpha\beta}$ under the integral (symmetric integration) \cite{PeskinSchroeder1995}.
\item[(iii)] \emph{(Pauli-Villars regulators.)} Each internal line of mass $m$ is replaced by a weighted sum over fields of masses $M_{i}$ and weights $c_{i}$, $c_{0} = 1$, $M_{0} = m$, with $\sum_{i}c_{i} = \sum_{i}c_{i}M_{i}^{2} = 0$; the weights take both signs, and a field of negative weight is quantised with a negative metric. At one loop these conditions make the integrals of (ii) finite, the regularisation is Lorentz invariant and keeps the Ward identity of electrodynamics, and the physical limit is $M_{i} \to \infty$ for $i \ge 1$ \cite{PauliVillars1949}. A regulator of a single Weyl fermion is a Dirac field of mass $M_{i}$, so the scheme does not preserve chirality.
\item[(iv)] \emph{(Covariant photon.)} In the covariant (Gupta-Bleuler) quantisation the photon propagator in the gauge with parameter $\xi$ is $\frac{-i}{k^{2} + i0}\bigl(g_{\mu\nu} - (1 - \xi)\frac{k_{\mu}k_{\nu}}{k^{2}}\bigr)$, $\xi = 1$ the Feynman gauge, and on-shell amplitudes between physical external states are independent of $\xi$ by the Ward identity \cite{PeskinSchroeder1995}.
\item[(v)] \emph{(On-shell external states.)} Scattering amplitudes are evaluated between on-shell spinors, $(p - m)u(p) = 0$, so between external states a Dirac line carries the projector $(p + m)/(2m)$ (LSZ reduction) \cite{PeskinSchroeder1995}.
\end{enumerate}

## technical
These are the standard tools for computing one-loop corrections in a relativistic quantum field theory. Feynman's trick combines a product of propagator denominators into one power of a weighted sum over the simplex. The loop momentum is then shifted, the integral rotated to Euclidean signature, and terms odd in the momentum dropped while products of two momenta are replaced by a quarter of the square times the metric; the remaining integrals are elementary, finite for three denominators and logarithmically divergent for two. Pauli and Villars regulate by adding heavy copies of each field with weights of both signs, chosen so that the weights and the weighted squared masses sum to zero: this is relativistically invariant and respects the conservation of charge, but the copies of negative weight are fields of negative norm, and a regulated chiral fermion acquires a mass. In covariant quantisation the photon propagator carries a gauge parameter on which physical on-shell amplitudes do not depend, and external lines are on-shell spinors.

## lay
To compute the first quantum corrections in a theory such as electrodynamics, physicists use a standard toolkit: a trick for combining denominators, a rotation of the time direction into an imaginary one that turns the integrals into ordinary ones, and a way of taming their infinities with heavy auxiliary particles, some of which count negatively. These tools are textbook material; the series takes them as given.

## one-liner
Feynman parametrisation, the Wick-rotated integrals ($-i/(32\pi^{2}\Delta)$ for three denominators, $\tfrac{i}{16\pi^{2}}(\ln(L/\Delta) - 1)$ for two) with symmetric integration, Pauli-Villars regulators with $\sum c_{i} = \sum c_{i}M_{i}^{2} = 0$ and weights of both signs, the covariant photon propagator with gauge-parameter independence of on-shell amplitudes, and on-shell external states.
