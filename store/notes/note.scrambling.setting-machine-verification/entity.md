---
id: note.scrambling.setting-machine-verification
kind: note
version: 1
title: Machine verification
status: setting
subject: entropy
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
comments_on:
- scrambling.no-recount-reaches-quarter
- scrambling.scheme-robustness-cutoff
- scrambling.uniqueness-internal-scaling
- scrambling.exact-factorisation-thinning
locators:
  paper: T08
  number: Setting
  section: Machine verification
  line: 971
---

## formal
The computational identities asserted in this paper are verified by \texttt{verify\_T08.py}, the script deposited with the paper \cite{ButlerVerifyT8}; it imports the series' shared exact-arithmetic library \texttt{GA.py} and runs entirely in exact arithmetic: dimensional quantities are exact monomials $c\cdot 2^a 3^b \pi^p M^e$ with rational coefficients and exponents (normalised so equal quantities have equal representations), so every scaling claim is an identity of exponents rather than a numerical estimate; the representation-theoretic and Fock computations are over the rationals. Forty-seven checks pass. Not scripted, and stated as such where they occur: the imported Facts, certified by their source papers' scripts or by the literature (Fact \ref{fact:curvature}'s displayed Kretschmann arithmetic included); the transcendence of $\ln 2$ (Hermite-Lindemann) that Proposition \claimref{scrambling.no-recount-reaches-quarter} imports, which no script certifies; the assembly steps of Section \ref{sec:dynamics} beyond their exact coefficients; and the observational Records.

The coverage, by section. \emph{The count} (Lemma \claimref{scrambling.scheme-robustness-cutoff} through Proposition \claimref{scrambling.uniqueness-internal-scaling}): the three cutoff schemes solved exactly, with the constants $2^{1/3}$, $48^{1/6} = 2^{2/3}3^{1/6}$, $3^{2/3}2^{-1/3}$ and the common $M^{1/3}$ exponent; the exact slice-volume identity $4\pi r_c^2\sqrt{2M/r_c} = 8\pi M$; the rate identity $dN/dt = \nu/\TH$; the area-law equivalence at $\nu\Delta t = M/2$; and the uniqueness arithmetic, driven by the computed exponents against the admissible set (sphere-only $M^{2/3}$, fixed-radius $M^{1/2}$, the unavailable matching timescales $M^{4/3}$, $M^{3/2}$). \emph{The calibration} (Section \ref{subsec:calibration}): the factorisation $16\pi = 4\pi \times 4$ and its ingredients as exact monomials; the scheme ratios $\tfrac32$ and $12^{1/4}$ on the prime factorisations; the horizon-normalised coframe values at $r = 0$; the ten anticommutation relations of two ladder pairs in $\Cl(2,4)$; the two cutoff-free scales and their residues $\tfrac14$ and $1$; the two calibrations with $\ln 2$ a formal indeterminate; the homogeneity table of the helicity lift; the natural rules' residues $4\pi$ and $1$ against the target $\tfrac14$; and the rationality closure of a counting rule's residue on eighty rules built from the paper's objects, none reaching $1/(4\ln 2)$ as a formal expression in $\ln 2$ while one reaches $\tfrac14$ (Propositions \claimref{scrambling.exact-factorisation-thinning} to \claimref{scrambling.no-recount-reaches-quarter}; the step from the formal to the numerical exclusion at $k = 0$ is the imported transcendence). \emph{The clock inventory} (Lemma \claimref{scrambling.clock-inventory-boundary-modes}): the adjoint spectra of the inventory's representatives classified exactly from their $2\times2$ rational blocks, transcribed from the proof's computation, and the same conclusions re-derived from a two-mode CAR representation built in the script (mode operators as exact Fock matrices, the pairing generators built rather than asserted, $\operatorname{ad}_X$ computed by commutator and the criterion read off it); the clock criterion run on each case (the atom, rotated-pair, opposed, common and paired boosts admitted; the compact, nilpotent, unequal-magnitude and complex-spectrum elements excluded), the pairing trichotomy certified by the sign of $cd$, and the discriminating cases $E_{11} + E_{12} - E_{21}$ (every adjoint eigenvalue of modulus one, none real: the modulus-only variant the script also runs admits it, the stated criterion excludes it) and $E_{11} + E_{12} + E_{22}$ (real adjoint eigenvalues, all nonzero of modulus one, excluded by semisimplicity alone). \emph{The epoch} (Theorem \claimref{scrambling.epoch-modular-period-two-unknowns-become}, Corollary \claimref{scrambling.integer-holographic-form-identification}): $\beta = 2\pi/\kappa = 8\pi M$; the conversion $\nu = 1/16\pi$ in the 1-nat convention; the epoch three-volume $V = 64\pi^2M^2 = \beta^2\lP$; $\nu V = 4\pi M^2 = \SBH$; and the $16\pi$ overshoot identified with the horizon-area coefficient, all as exact monomial identities, with $\SBH$ and the horizon area derived from $r_s = 2M$ and anchored by their own check rather than typed in. \emph{The sphere} (Theorem \claimref{scrambling.principality-indifference-sphere}, Propositions \claimref{scrambling.boundary-mode-space-matrix}, \claimref{scrambling.consistency-car-construction-i-states-insensitivity}, \claimref{scrambling.per-slice-verification-two-failed-aggregations}): an integer principal $\mathfrak{sl}_2$ triple in $\Mat_3$ with its bracket table verified exactly; the adjoint kernel of $\operatorname{ad}_e$ of dimension exactly three (multiplicity-free $1 + 3 + 5$) against dimension five for a non-principal block embedding (partition data made visible); the $\operatorname{ad}_h$ weight multiset $\{0,0,0,\pm2,\pm2,\pm4\}$; the $\mathfrak{gl}(n)$ bilinear commutator identities on the full five-mode Fock space and the one-particle restriction onto matrix units; the second-quantised rational rotation ($U$ orthogonal with entries in fifths) verified exact and particle-number preserving, the equal-occupancy quasi-free product state verified invariant under it entrywise, and a control at unequal occupancies verified to break the invariance, the degeneracy hypothesis made visible: the I-state's embedding-insensitivity certified on the state itself; the slice-count and spheres-per-time exponents, and the $M^{5/3}$ failure of fundamental-per-slice aggregation. \emph{The dynamics} (Assemblies \claimref{scrambling.spreading-law-chaos-bound-saturated} and \claimref{scrambling.return-delay-scrambling-log-recovered}): the scrambling coefficient $4M$, as the arithmetic of $\beta$ and $\kappa$ already fixed. The script exits nonzero on any failure and prints one line per check, tagged by the statement or section it certifies.

## technical
pending

## lay
pending

## one-liner
pending
