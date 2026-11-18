---
id: scrambling.spreading-law-chaos-bound-saturated
kind: claim
version: 7
title: The spreading law, and the chaos bound met, not saturated
status: proved
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
- name: Claude Fable 5.2
  role: 'restatement on the proved scope (affine cells of a horizon generator, and the rotor''s count in rapidity), with a proof and a check; the window reading named as the unproved part'
  version: 7
  source: run 2026-11-18-leads
amendments:
- version: 7
  kind: restatement
  defect: 'the accepted statement gives the spreading of support over the window''s N counted modes at t_* = (beta/2 pi) ln S as following from amplitudes growing as e^(kappa t) under a generic quadratic coupling; that step is an order-of-magnitude estimate (the reason the status was lowered at version 6) and, by the stored phase-flow and number-diagonal theorems, it is the rotor flow''s growth and has no real-time reading on the windows. What is proved is narrower: the boost spreads one affine cell of a horizon generator over N cells at Killing time kappa^-1 ln N with falling amplitudes (the stored affine-cell theorem), and the rotor reaches the same count in rapidity on the ladder operators. The statement is restated on that scope and the window reading with N of the order of S is named as an estimate.'
  evidence: check.py::check_affine_cell_count_is_log_n
review: typed
derivations:
- name: main
  uses:
  - synthesis.affine-cell-boost-spreads-without-scrambling@4
  - synthesis.boost-evolution-on-generators-is-one-unitary-group@6
  - synthesis.phase-flow-is-time-rotor-flow-kms-continuation@4
  - synthesis.positive-null-energy-gives-r-premises@9
  - synthesis.number-diagonal-dynamics-spreads-nothing@3
  - scrambling.area-law-test@5
  - scrambling.clock-inventory-boundary-modes@6
  - scrambling.imported-modes-modular-inventory@5
  - scrambling.mode-count@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_affine_cell_count_is_log_n
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
  restatement_2026_11_18:
    by: run 2026-11-18-leads
    date: '2026-11-18'
    note: 'Version 6 -> 7, proposed, with a status change from conjectured to proved that is the maintainer''s to decide. The case: since 7 November the store holds a proved result (the affine-cell theorem) that gives the count kappa^-1 ln N exactly, in real time, for the boost on one generator of a Killing horizon, and this entity was left conjectured and outside every open problem. Three things were tested before restating. Circularity: the past cones of the affine-cell, phase-flow, one-unitary-group and (N+)-to-(R) theorems do not contain this entity (their former edges to it are text mentions since version 6). Object: the proved count is about affine cells of a horizon generator, not about the window''s counted modes, and only the cell at the edge covers the first N cells. Mechanism: the accepted derivation''s growth step is the rotor flow''s (count in rapidity), while the proved real-time count has amplitudes falling as e^(-kappa t/2). So the entity is restated, not only re-labelled: clauses (a) to (d) are what is proved, clause (e) lists what is not (the window reading with N of the order of S, and scrambling in the sense of the chaos bound). No listed open problem holds the unproved part; the settled problem on the two boost flows lists chaotic dynamics of the windows as not covered. The dependant scrambling.return-delay-scrambling-log-recovered (conjectured) cites this entity at version 6 and has to be read against the new statement before its pin moves; it stays an estimate.'
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
\emph{Scope.} The law $t_{*} = \kappa^{-1}\ln N$ is proved in two readings, (a) and (b): a statement about the boost on one generator of a Killing horizon, and a statement about the boost rotor on ladder operators. Its reading on the window's counted modes, with $N$ of the order of the entropy, is an estimate; it is stated in (e) and is not part of what is proved.
\begin{enumerate}
\item[(a)] \emph{(Real-time count on a generator; proved.)} On the continuum mode space of one generator of a Killing horizon of surface gravity $\kappa$, with affine parameter $U > 0$, the boost time evolution is the unitary dilation $(D_{t}f)(U) = e^{-\kappa t/2}f(e^{-\kappa t}U)$ (Theorem \claimref{synthesis.boost-evolution-on-generators-is-one-unitary-group}). In the basis of affine cells $[j\delta, (j+1)\delta)$ with normalised indicators $\chi_{j}$, at Killing time $t$ with $e^{\kappa t} = N$ an integer, $D_{t}\chi_{j} = N^{-1/2}\sum_{l=0}^{N-1}\chi_{Nj+l}$ (Theorem \claimref{synthesis.affine-cell-boost-spreads-without-scrambling}(i)). So the mode operator of one cell covers $N$ cells at
\[
t_{*} \;=\; \kappa^{-1}\ln N ;
\]
the cell at the edge, $j = 0$, covers the first $N$ cells, and a cell $j \ge 1$ covers $N$ cells further out. The amplitudes fall: every anticommutator of the evolved mode operator with a fixed cell operator is at most $e^{-\kappa t/2} = N^{-1/2}$ (clause (ii) there).
\item[(b)] \emph{(Count in rapidity on the ladder; proved.)} The intrinsic flows of a Clifford boundary-mode algebra are bivector-generated (Lemma \claimref{scrambling.clock-inventory-boundary-modes}(i)), and the boost rotor $\exp(\kappa t\,\sigma/2)$, $\sigma = e_{+}e_{-}$, scales the ladder operators of every mode by $e^{\mp\kappa t}$, with one rapidity for all modes, as a one-parameter group (the weight clause of Fact \claimref{scrambling.imported-modes-modular-inventory}); an amplitude $1/N$ carried by it reaches one exactly when $e^{\kappa t} = N$. This rotor flow is not a time evolution of the windows: it is the continuation of the phase flow to the KMS strip (Theorem \claimref{synthesis.phase-flow-is-time-rotor-flow-kms-continuation}). In this reading $\kappa t_{*} = \ln N$ counts rapidity, not Killing time.
\item[(c)] \emph{(The rate; proved given (N$_{+}$).)} Under (N$_{+}$) the state of the generator's modes is thermal for the boost at rapidity period $2\pi$ (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}), that is $\kappa\beta = 2\pi$ in Killing time. So in both readings $t_{*} = (\beta/2\pi)\ln N$, with $\beta/2\pi = 4M$ for the Schwarzschild field, and the rate at which the support of (a) dilates is $2\pi T$.
\item[(d)] \emph{(The chaos bound is met, not saturated; proved.)} The real-time Lyapunov exponent of the dynamics of (a) is $0$: it is one unitary group with bounded anticommutators on linear elements (Theorem \claimref{synthesis.boost-evolution-on-generators-is-one-unitary-group}). The equality of the dilation rate with $2\pi T$ is the equality of one group's rate with its own KMS rate, not growth of the out-of-time-order correlators that the Maldacena-Shenker-Stanford bound limits \cite{MSS2016}.
\item[(e)] \emph{(What is not proved; an estimate.)} The fast-scrambling form $t_{*} = (\beta/2\pi)\ln S$ for the $N$ counted modes of a window (Theorem \claimref{scrambling.mode-count}) needs three further steps, none of which is proved. First, that the window's modes are the affine cells of (a): the count depends on that basis, since on boost-adapted cells the same flow displaces without spreading (clause (iii) of Theorem \claimref{synthesis.affine-cell-boost-spreads-without-scrambling}), and every dynamics that Premise (L$_{E}$) admits on the windows spreads nothing along chains in real time (Theorem \claimref{synthesis.number-diagonal-dynamics-spreads-nothing}). Second, that $N$ equals $S$ up to a factor of order one, which Proposition \claimref{scrambling.area-law-test} gives only for an epoch of order $M$, with a calibration. Third, that covering the cells is scrambling, which by (d) it is not in the sense of the chaos bound. The earlier derivation's step, an amplitude growing as $e^{\kappa t}$ under a generic quadratic coupling against a suppression of order $1/N$, is reading (b) and not a real-time mechanism. Chaotic dynamics beyond the quasi-free flow is open.
\end{enumerate}

## technical
The spreading law $t_{*} = \kappa^{-1}\ln N$ is proved in two readings. On one generator of a Killing horizon the boost acts in real time as a unitary dilation of the affine parameter, and in the basis of affine cells it spreads the mode of one cell uniformly over $e^{\kappa t}$ cells: $N$ cells at Killing time $\kappa^{-1}\ln N$, with amplitudes falling as $e^{-\kappa t/2}$. On the ladder operators of a boundary-mode algebra the boost rotor scales every mode by $e^{\mp\kappa t}$, so an amplitude $1/N$ reaches one at the same value of $\kappa t$; but that rotor flow is the KMS-strip continuation of the time evolution, so there the count is in rapidity.

Under (N$_{+}$), $\kappa\beta = 2\pi$, so $t_{*} = (\beta/2\pi)\ln N$ and the support dilates at the rate $2\pi T$. The real-time Lyapunov exponent of this quasi-free dynamics is $0$, so the Maldacena-Shenker-Stanford chaos bound is met, not saturated: the equality is one group's rate against its own KMS rate.

Not proved, and kept as an estimate: the fast-scrambling form $(\beta/2\pi)\ln S$ for a window's counted modes. It needs the window's modes to be the affine cells (on boost-adapted cells nothing spreads, and under the locality premise (L$_{E}$) the windows' admissible dynamics does not spread along chains), $N$ of the order of $S$ (an epoch of order $M$, with a calibration), and a sense in which covering cells is scrambling. Chaotic dynamics beyond the quasi-free flow is open.

## lay
Along a single light ray of a black hole's horizon, the hole's own stretching motion spreads a disturbance that starts in one small cell over more and more cells, doubling their number at a steady pace. After a time that grows with the logarithm of the number of cells, it covers that many cells. This much is proved, together with the fact that the pace equals the rate named by a known general bound on chaos, under the series' premise that the modes on each light ray are in their lowest-energy state.

Two cautions are part of the statement. The spreading is not chaos: the disturbance thins out as it spreads and nothing grows, so the bound is met rather than saturated. And the step from this picture to the black hole's interior modes, which would give the fast-scrambling time in terms of the entropy, is an estimate and not a proof: it depends on how the interior modes are identified with cells along the ray, and under the series' locality premise those modes do not pass disturbances along in ordinary time at all.

## one-liner
The boost spreads one affine cell of a horizon generator over $N$ cells at Killing time $t_{*} = \kappa^{-1}\ln N = (\beta/2\pi)\ln N$, with amplitudes falling as $e^{-\kappa t/2}$, and its rotor reaches the same count in rapidity on the ladder operators (both proved; $\kappa\beta = 2\pi$ under (N$_{+}$)); the support dilates at $2\pi T$ while the real-time Lyapunov exponent is $0$, so the chaos bound is met, not saturated; the form $(\beta/2\pi)\ln S$ for a window's counted modes is an estimate.
