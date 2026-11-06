---
id: synthesis.affine-cell-boost-spreads-without-scrambling
kind: claim
version: 1
title: 'The boost spreads affine cells without scrambling'
status: proved
region: synthesis
subject: thermality
tags:
- modular-theory
- horizons
- car-algebra
- finite-models
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.hawking.continuum-mode-space
derivations:
- name: main
  uses:
  - synthesis.phase-flow-is-time-rotor-flow-kms-continuation@2
  - scrambling.spreading-law-chaos-bound-saturated@5
  - angle.imported-theorems-deliver-their-hypotheses@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_affine_cells_spread_at_rate_kappa
- kind: check
  ref: check.py::check_log_cells_are_displaced_and_generator_hops
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.phase-flow-is-time-rotor-flow-kms-continuation
extraction:
  open_problem: op.which-boost-flow-is-time
  note: Bears on the open item left by the stored decision (real-time spreading needs a mode-displacing generator). It exhibits that generator, the boost itself acting on affine cells of a horizon generator, and shows that it gives the count t = kappa^{-1} ln N in real time as support growth, with decaying local anticommutators; so the stored conclusion stands (no real-time chaos-bound saturation is shown), and the real-time reading of the count is basis-dependent (affine cells spread, log cells are displaced). Transport-absent (free-field kinematics on one null generator). The Borchers relation (modular flow dilates null translations) is taken from the store's imported fact. Spreading here is one-particle spread in the affine-cell basis; the evolved operator stays linear in the modes.
---

## formal
On one generator of a Killing horizon of surface gravity $\kappa$ with affine parameter $U > 0$, let the one-particle space be $L^{2}(\R_{+}, dU)$ (half-densities) and let the boost at Killing time $t$ act as the unitary dilation $(D_{t}f)(U) = e^{-\kappa t/2}f(e^{-\kappa t}U)$, the action of the modular flow on null translations of Fact \claimref{angle.imported-theorems-deliver-their-hypotheses}; on the CAR algebra over this space (a continuum mode space in the sense of Definition \claimref{obj.hawking.continuum-mode-space}) it is the quasi-free real-time flow $a(f) \mapsto a(D_{t}f)$, a phase flow in the sense of Theorem \claimref{synthesis.phase-flow-is-time-rotor-flow-kms-continuation}. Let $\chi_{j}$ be the normalised indicator of the affine cell $[j\delta, (j+1)\delta)$.
\begin{enumerate}
\item[(i)] \emph{(Support grows at rate $\kappa$.)} If $e^{\kappa t} = m$ is an integer, $D_{t}\chi_{j} = m^{-1/2}\sum_{l=0}^{m-1}\chi_{mj+l}$: one cell is spread uniformly over $e^{\kappa t}$ cells with amplitude $e^{-\kappa t/2}$ and norm one. The mode operator $a(\chi_{j})$ therefore covers $N$ cells at real Killing time $t = \kappa^{-1}\ln N$.
\item[(ii)] \emph{(Local anticommutators decay.)} For every fixed cell $k$, $\{a(D_{t}\chi_{j}), a^{*}(\chi_{k})\} = \langle\chi_{k}, D_{t}\chi_{j}\rangle \in \{0, e^{-\kappa t/2}\}$; every anticommutator of the evolved mode operator with a fixed cell operator is bounded by $e^{-\kappa t/2}$, and the squares over all cells sum to one.
\item[(iii)] \emph{(Basis dependence.)} On log cells $[m^{i}\delta, m^{i+1}\delta)$ the same flow at $e^{\kappa t} = m$ maps the normalised indicator of cell $i$ to that of cell $i+1$: it displaces without spreading.
\item[(iv)] \emph{(It hops.)} In the affine-cell basis the generator is not diagonal: it moves one-particle weight from cell $j$ to cells $mj, \dots, mj + m - 1$.
\end{enumerate}
So, in the affine-cell basis, the count $t_{*} = \kappa^{-1}\ln N$ of Assumption \claimref{scrambling.spreading-law-chaos-bound-saturated} has a real-time reading under the phase flow, as the number of affine cells one cell is spread over by the boost, with amplitudes falling as $e^{-\kappa t/2}$ rather than growing; it is free dilation, with no growth of local anticommutators, so it is not the out-of-time-order growth the chaos bound concerns, and on boost-adapted (log) cells it disappears.

## technical
On a horizon generator the boost is a dilation of the affine parameter. Acting on modes localised in equal affine cells, it spreads one cell over $e^{\kappa t}$ cells in real time, unitarily and quadratically, with amplitude $e^{-\kappa t/2}$ in each. A single mode thus covers $N$ cells after $\kappa^{-1}\ln N$, the fast-scrambling count, but its overlap with any fixed cell decays, so every local anticommutator decays: one-particle support grows (the evolved operator stays linear in the modes) while no local anticommutator grows. On cells equally spaced in the logarithm of the affine parameter, which are adapted to the boost, the same flow merely shifts each cell to the next. The spreading generator moves occupation between affine cells, the kind of generator boundary-mode locality excludes on the exceptional set.

## lay
A black hole's horizon stretches what falls along it. A quantum mode confined to one small stretch of the horizon is smeared, as time passes, over exponentially many stretches, reaching N of them after a time proportional to the logarithm of N, the famous fast-scrambling time. But it is smeared thinner as it spreads, so its influence on any one stretch fades: this is spreading, not the scrambling that the chaos bound is about.

## one-liner
On affine cells of a horizon generator the real-time boost spreads one cell over $e^{\kappa t}$ cells (covering $N$ at $\kappa^{-1}\ln N$, a basis-dependent count) while every local anticommutator decays as $e^{-\kappa t/2}$; on log cells the same flow only displaces.
