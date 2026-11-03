---
id: note.hawking.setting-machine-verification
kind: note
version: 1
title: Machine verification
status: setting
subject: descent
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
comments_on:
- hawking.modular-structure-completed-pair
- hawking.gibbs-states-are-kms-conversely-finite
- hawking.i-state
- hawking.imported-quasi-free-kms-reduces-two
locators:
  paper: T07
  number: Setting
  section: Machine verification
  line: 728
---

## formal
The computational identities asserted in this paper are verified by the script deposited with it, \texttt{verify\_T07.py} \cite{ButlerVerifyT7}. The script imports the series' shared exact-arithmetic library \texttt{GA.py}, runs entirely in exact arithmetic (rational numbers and rational functions in a formal Boltzmann variable, no floating point anywhere), and so certifies each check as an identity, or as an exactly evaluated inequality, rather than an approximation. Twenty-five checks pass. Not scripted, and stated as such where they occur: the imported Facts, certified by their source papers' scripts or by the literature; the continuum passage beyond its window content; the assembly joints of Section \ref{sec:lift}; the classical Penrose transform; and the geometric inputs $\kappa = 1/4M$ and $\TH = \kappa/2\pi$, proved and scripted in T5.

The coverage, section by section.

\begin{description}
\item[Section \ref{sec:setting}, the single mode (Proposition \claimref{hawking.modular-structure-completed-pair}).] All five clauses in the basis-blade arithmetic over $\Cl(1,1)$: the null pair's squares and anticommutator, $\sigma = e_0e_1$ with $\sigma^2 = 1$, the one-sided weight relations, the finite conjugation at the rational rotor $R = \tfrac53 + \tfrac43\,\sigma$ (that is, $\cosh(\lambda/2) = \tfrac53$) with scale factors $\tfrac19$ and $9$, the projector identities, and the one-dimensionality of the bivector space; plus the Fock identity $\tfrac12\sigma = N - \tfrac12$.
\item[Section \ref{sec:state}, the state (Lemma \claimref{hawking.gibbs-states-are-kms-conversely-finite}, Theorem \claimref{hawking.i-state}).] The Gibbs KMS identity on all sixteen matrix-unit pairs of the mode algebra, as identities of rational functions in the formal Boltzmann factor; the uniqueness solve, performed symbolically, the KMS constraints on an arbitrary density matrix having a one-dimensional kernel spanned by the Gibbs matrix. Then the symbol itself: the Fermi-Dirac detailed-balance identity $n/(1-n) = e^{-\beta\omega}$; the Fermi-Dirac product state on a three-mode window confirmed equal to the Gibbs matrix of $H_F$, the two sides built independently, then confirmed KMS on all $4096$ matrix-unit pairs; and, on a two-mode window, the full KMS constraint system solved for an arbitrary density matrix against independently supplied dynamics, with one-dimensional kernel, vanishing pairing, and the Fermi-Dirac symbol.
\item[Section \ref{sec:continuum}, the continuum.] No separately computable identity: its exact content is the window case, scripted under Section 3, and its remaining steps are the imported calculus of Facts \claimref{hawking.imported-quasi-free-kms-reduces-two} and \claimref{hawking.imported-ideal-fermi-gas-uniqueness}, certified by their sources.
\item[Section \ref{sec:lift}, the lift (Proposition \claimref{hawking.homogeneity-ordering-shift}).] The operator identity $q(\id) = -\hbar(\Upsilon + 2)$ on all twistor monomials of degree at most three, and the homogeneity table $-2s-2 \mapsto (-4, 0, -6, +2)$ at $s = \pm 1, \pm 2$.
\item[Section \ref{sec:seam}, the finite window (Propositions \claimref{hawking.current-commutator-exactly-edge-split} and \claimref{hawking.bose-einstein-occupancy-quantified-window-corrections}).] The edge identity $[a_m, a_m^\dagger] = B_m - T_m$ as an operator identity on all $256$ states of an eight-mode window for $m = 1, 2, 3$; the exact free-boson relation on every edge-clean state; the exact vanishing of $[a_m, a_{m'}]$ and the vanishing of the cross commutator on edge-clean states. Then the ladder: the detailed-balance identity of Proposition \claimref{hawking.bose-einstein-occupancy-quantified-window-corrections}(1) in the formal $x^{-k}$ at three values of $x^{-m}$, with the Bose-Einstein form $\bar n/(1 + \bar n) = e^{-\beta\omega}$ of the clause-(2) occupancy, at $\omega = \epsilon m$ on the ladder; the window sums' approach to the exact Planck factor from below, within the proven tail bound, as exact rational inequalities at two temperatures and three $m$; and the Wick formula checked against the direct density-matrix expectation on the full $256$-state window, the ladder in the paper's occupancy convention.
\end{description}

The script exits nonzero on any failure and prints one line per check, tagged by the statement it certifies.

## technical
pending

## lay
pending

## one-liner
pending
