---
id: note.simulations.setting-machine-verification
kind: note
version: 1
title: Machine verification
status: setting
subject: dark-matter
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14b, deposited version
comments_on:
- simulations.effective-cross-section-sheet-matter
- simulations.cluster-bound-two-dimensions
- simulations.averaged-pair-operator
locators:
  paper: T14b
  number: Setting
  section: Machine verification
  line: 681
---

## formal
\textbf{The script.} \file{verify\_T14b.py} \cite{ButlerVerifyT14b} imports the series' shared library \file{GA.py} and checks the note's computational identities and derived numbers: $60$ checks, all passing, in eight parts. A few are arithmetic restatements of a quoted number rather than tests of a claim (D4, F3, R4, R7). Algebraic identities are checked in exact rational arithmetic; evaluations with physical constants, transcendental functions and integrals in double precision, with the tolerance stated beside each check.

\emph{Part A: composition.} $T(1) = (11\pi + 16)/(3\pi)$ between rational bounds; $T(\pi/2) = T(1)$; the three shares and their sum; the baryon, galaxy and gas fractions of every halo; the three colliding shares and their order against the bounds.

\emph{Part B: self-interaction.} Proposition \claimref{simulations.effective-cross-section-sheet-matter} as an exact identity; $n_{b}$ and $d_{b}$; the ratio $V_{3}/V_{2} = 4/3$ from the unit-ball volumes; the range of Table \ref{tab:sidm}; the bound on $\lambda$; Computation \claimref{simulations.cluster-bound-two-dimensions}, with Bessel functions by their series; the five-dimensional range; the mean free path.

\emph{Part C: the code's algebra.} The kernel's normalisation, derivative and continuity, exactly; Lemma \claimref{simulations.averaged-pair-operator}(ii) in the blade engine of $\Cl(3,0)$, (iii) in exact rationals, including $P_{ij}^{2} \ne P_{ij}$ for orthogonal normals, and (i) on a rational instance with distinct normals and viscosity; the cooling update as a polynomial identity; the units; the settling threshold at $\mu = 0.6$ and its temperature for the helium plasma, from the code's $u(T)$ formula and constants; the algebra of the bremsstrahlung coefficient (the electron and ion densities and $T(u)$ for He$^{++}$) against $du/dt = -\varepsilon/\rho$, with the code's constants.

\emph{Part D: initial conditions.} The Hernquist matching and $r_{200}$, exactly; the Jeans equation for $\sigma_{r}^{2}$ at three radii; the truncation fraction; the merger geometry, exactly.

\emph{Part E: the mirror's composition.} Freeze-out temperatures, $Y'$, $\eta'$, the recombination temperature and $\Delta N_{\mathrm{eff}}$.

\emph{Part F: cooling.} The metal-free $\Lambda_{N}$ at three temperatures; the cooling-time ratios of helium to our gas; the Tozzi-Norman conversion.

\emph{Part G: supernova energy.} The continuity of the IMF; our energy per unit mass; $F$ for our IMF's shape and the best shifted IMF.

\emph{Part R: recorded outputs.} Selected simulation and model outputs, carried as constants from the run summaries, and the comparisons the text draws from them: the mass-to-light change, ratio and sampling error; the merger separations; the halo ratios, with their seed-paired values; the Galaxy floors against the decisive limits and the three readings of the bulge room. The outputs themselves are reproduced by the deposited scripts, not by this one: Part R does not read \file{outputs/}, so a change to a deposited output would not fail the script.

\emph{What the script does not check:} the simulations and the Galaxy model themselves, which Section \ref{sec:running} shows how to rerun, and the imported Facts and published bounds.

## technical
pending

## lay
pending

## one-liner
pending
