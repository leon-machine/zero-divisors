---
id: scrambling.spreading-law-chaos-bound-saturated
kind: claim
version: 6
title: The spreading law, and the chaos bound met, not saturated
status: conjectured
region: scrambling
subject: entropy
tags: [boundary-modes, recovers-known-physics]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, status lowered to conjectured at Leon''s decisions'
  version: 6
  source: maintainer pass 2026-11-07 (decisions)
- name: Claude Opus 5.5
  role: 'maintainer pass, status lowered to conjectured at Leon''s decisions'
  version: 6
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  note: the argument as stored, an order-of-magnitude estimate; its 'follows from' text is kept in proof-main.tex, no longer attached as a proof since the status is conjectured
  uses:
  - scrambling.area-law-test@5
  - scrambling.clock-inventory-boundary-modes@6
  - scrambling.imported-modes-modular-inventory@5
  - scrambling.mode-count@3
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - label:asm:spreading
- kind: check
  ref: check.py::check_boost_flow_scales_ladders_exponentially
- kind: check
  ref: check.py::check_spreading_threshold_is_log_n
- kind: check
  ref: check.py::check_rate_is_modular_rate
lineage:
  motivated_by:
  - scrambling.clock-inventory-boundary-modes
  - scrambling.imported-modes-modular-inventory
  - scrambling.mode-count
locators:
  paper: T08
  number: Asm 6.1
  label: asm:spreading
  line: 910
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: scrambling.area-law-test repinned 4 -> 5 after reviewing its A15 correction (the 1-nat convention, and nu Delta t = M/(2 ln 2) in the capacity convention, are now stated in the formal); the use here holds as cited.'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 5 -> 6. Leon''s answer 4 (B1): status lowered from proved to conjectured. The spreading law is an order-of-magnitude estimate (the standard doubling estimate under a generic quadratic coupling, ''Tier, declared'' in its own formal level) and its proof is ''Follows from ..., as the source states'', so the proof does not reach the strict standard of proved. The four proved results that cited it as a premise for comparison (synthesis.phase-flow-is-time-rotor-flow-kms-continuation, synthesis.number-diagonal-dynamics-spreads-nothing, synthesis.affine-cell-boost-spreads-without-scrambling, synthesis.boost-evolution-on-generators-is-one-unitary-group) analyse its growth step and do not rest on its truth; their uses edges become text mentions. Status change at Leon''s decision; statement unchanged. Layer-1 consequence of the status change: a conjecture carries no proof text (E108) and needs lineage.motivated_by (E107), so derivation main keeps its premises and a note but no longer attaches proof-main.tex (the file is kept, unchanged), and lineage.motivated_by names the inventory, the modular inventory and the mode count that prompted it.'
  maintainer_pass_2:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Chaos-bound sentence reworded at Leon''s decision of 2026-10-26: "saturates the chaos bound by construction" replaced at every level by the reviewed statement that the boost group''s support-dilation rate equals its KMS rate (kappa beta = 2 pi, under (N+)) while the real-time Lyapunov exponent of the quasi-free dynamics is 0, so the bound is met, not saturated, citing synthesis.boost-evolution-on-generators-is-one-unitary-group (text only: that result uses this one, so it is not a premise here). Title changed to match; spreading law, derivation, checks and premises unchanged. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: boost rotor scales the ladder operators by e^(-+kappa t) as a one-parameter group in Cl(1,1) and Cl(2,2), the threshold e^(kappa t_*) = N, and kappa = 1/(4M) = 2 pi T. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Wording: the equality of the expansion rate with 2 pi T is premise (R) restated (the rotor rate kappa and the temperature are fixed by the same regularity condition), not a chaos result; under the phase flow the real-time Lyapunov exponent is zero (argued in the analysis of op.which-boost-flow-is-time). Version 1 -> 2.'
  env: assembly
  context_refs:
  - scrambling.area-law-test
  - scrambling.clock-inventory-boundary-modes
  - scrambling.imported-modes-modular-inventory
  - scrambling.mode-count
  flags:
  - no proof environment found
  typing:
    by: ai-typing-pass
    added:
    - scrambling.area-law-test
    - scrambling.clock-inventory-boundary-modes
    - scrambling.imported-modes-modular-inventory
    - scrambling.mode-count
    note: 'Assembly with no proof environment: given the source''s ''follows from'' proof with the four
      context refs its step-by-step names; the source recovers the fast-scrambling law and the Maldacena-Shenker-Stanford
      bound as points of contact, but neither is an imported claim in the store, so no standard route
      was added. Levels pass: conditions already kept.'
  flow_note: rotor flow exp(lambda sigma/2) (T05 Thm 6.3, T08 Lem 4.2). The scrambling law runs on the boost's
    real weights, ladder operators scaled by e^{+-kappa t}, which is the rotor flow; the identification
    kappa^{-1} = beta/2 pi takes beta from the phase flow's KMS period.
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 4
    note: 'The two boost flows: flow_note recorded.'
---

## formal
Three framework-internal facts fix the window's internal dynamics. First, the intrinsic flows of a Clifford boundary-mode algebra are bivector-generated, quadratic in the pair operators (Lemma \claimref{scrambling.clock-inventory-boundary-modes}(i)). Second, the distinguished bivector flow is the boost (Fact \claimref{scrambling.imported-modes-modular-inventory}). Third, the boost is the translation clock of the window itself: the Killing flow that displaces modes along the window is the boost at rate $\kappa$, with the accrual rate of Theorem \claimref{scrambling.mode-count}. Boost-hyperbolic one-body dynamics expands operator amplitudes as $e^{\kappa t}$, so support deposited on a single mode spans the $N$-mode window at
\[
t_* \;=\; \kappa^{-1}\ln N \;=\; \frac{\beta}{2\pi}\,\ln S :
\]
the fast-scrambling law, with the logarithm the signature of hyperbolic dynamics rather than an assumption. Every intrinsic clock it has runs at the modular rate, and the expansion rate is exactly $2\pi T$: the boost group's support-dilation rate equals its KMS rate, $\kappa\beta = 2\pi$, which holds under (N$_{+}$) (\claimref{synthesis.n-plus-null-ground-state}). The real-time Lyapunov exponent of this quasi-free dynamics is $0$: the one unitary group that dilates the support has bounded anticommutators on linear elements (Theorem \claimref{synthesis.boost-evolution-on-generators-is-one-unitary-group}). So the Maldacena-Shenker-Stanford chaos bound is met, not saturated. \emph{Tier, declared:} what is derived is the free-fermion operator-spreading timescale under a generic quadratic coupling, in the rate-model normalisation; genuine chaotic saturation beyond free-fermion spreading is open, and is named as such in Section \ref{sec:scope}.

\smallskip
\noindent\emph{The derivation, step by step.} The inventory clauses are Lemma \claimref{scrambling.clock-inventory-boundary-modes} (proved) and its import (Fact \claimref{scrambling.imported-modes-modular-inventory}). The expansion computation: a quadratic generator containing the boost scales ladder operators by $e^{\pm\kappa t}$ (Fact \claimref{scrambling.imported-modes-modular-inventory}'s weight clause, exponentiated), so under a generic quadratic coupling the amplitude reaching a mode at mode distance $d$ grows as $e^{\kappa t}$ against an initial suppression of order $1/N$; support spans all the boundary modes when $e^{\kappa t} \sim N$, i.e.\ at $t_* = \kappa^{-1}\ln N$, and $N \sim S$ over an epoch of order $M$ (Proposition \claimref{scrambling.area-law-test}). The identification $\kappa^{-1} = \beta/2\pi$ is arithmetic ($\beta = 2\pi/\kappa$), checked by the script along with the Schwarzschild value $\beta/2\pi = 4M$. The MSS statement that no system exceeds the growth rate $2\pi T$ is the point of contact \cite{MSS2016}: the rate $\kappa$ at which support dilates is one group's rate set against its own KMS period $2\pi/\kappa$, while the out-of-time-order growth that the bound limits is absent from the quasi-free dynamics, so the bound is met and not saturated.

## technical
Three facts fix the window's internal dynamics: the intrinsic flows of the boundary-mode algebra are bivector-generated, quadratic in the pair operators; the distinguished bivector flow is the boost; and the boost is the translation clock of the window, at rate $\kappa$. Boost-hyperbolic one-body dynamics grows operator amplitudes as $e^{\kappa t}$, so support on one mode spans the $N$-mode window at $t_* = \kappa^{-1}\ln N = (\beta/2\pi)\ln S$, with $N \sim S$ over an epoch of order $M$.

Since every intrinsic clock runs at the modular rate, the expansion rate is exactly $2\pi T$: the boost group's support-dilation rate equals its KMS rate ($\kappa\beta = 2\pi$, under (N$_{+}$)), an equality that restates premise (R) (the rotor rate and the temperature are fixed by the same regularity condition; on the continuum, the rapidity period $2\pi$ that (N$_{+}$) gives), not a chaos result. The real-time Lyapunov exponent of the quasi-free dynamics is $0$, so the Maldacena-Shenker-Stanford chaos bound is met, not saturated. What is derived is the free-fermion operator-spreading timescale under a generic quadratic coupling, in the rate-model normalisation; genuine chaotic saturation beyond that is open.

## lay
A disturbance entering the black hole's interior modes spreads through them exponentially fast, because the modes' only clock is a stretching motion. Assuming a generic coupling between the modes, it reaches every mode after a time that grows with the logarithm of the entropy, the fast-scrambling time. Under the series' premise that the modes on each light ray are in their lowest-energy state, the spreading rate equals the rate named by a known general bound on chaos, but the dynamics is not chaotic: disturbances spread without growing in real time, so the bound is met rather than saturated.

## one-liner
Boost-hyperbolic spreading covers the whole window at $t_* = \kappa^{-1}\ln N = (\beta/2\pi)\ln S$; the support dilates at the chaos-bound rate $2\pi T$ ($\kappa\beta = 2\pi$, under (N$_{+}$)) while the real-time Lyapunov exponent of the quasi-free dynamics is $0$, so the bound is met, not saturated.
