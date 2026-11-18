---
id: scrambling.spreading-law-chaos-bound-saturated
kind: claim
version: 7
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
- name: Claude Fable 5.2
  role: 'restatement with the scope made explicit: the proved statements the estimate rests on are cited as stored theorems, the window law is named as the estimate; one check added; status unchanged'
  version: 7
  source: run 2026-11-18-leads
amendments:
- version: 7
  kind: restatement
  defect: 'the accepted statement gives the spreading of support over the window''s N counted modes at t_* = (beta/2 pi) ln S as following from amplitudes growing as e^(kappa t) under a generic quadratic coupling, without separating what the store proves from what is estimated. By the stored phase-flow and number-diagonal theorems that growth is the rotor flow''s and has no real-time reading on the windows; what the store proves is narrower and lies in other entities: the boost spreads one affine cell of a horizon generator over N cells in a lapse kappa^-1 ln N of Killing time, with falling amplitudes (the affine-cell and one-unitary-group theorems), and the rotor reaches the same count in rapidity on the ladder operators. The statement is restated so that those are cited as stored theorems and the window law with N of the order of S is named as the estimate this entity records. The status stays conjectured.'
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
  note: the window law is an order-of-magnitude estimate and the status is conjectured, so no proof is attached; the premises are the stored theorems that prove the statements (a) to (d) the estimate rests on, and those that bear on its unproved steps; proof-main.tex is kept as a record of where each cited statement is proved
checked_by:
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
  - synthesis.affine-cell-boost-spreads-without-scrambling
  - synthesis.boost-evolution-on-generators-is-one-unitary-group
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
    note: 'Version 6 -> 7, a restatement with the status kept at conjectured. A first draft of this version raised the status to proved on clauses (a) to (d); on review those clauses are stored theorems word for word (the affine-cell theorem, the phase-flow theorem, the (N+)-to-(R) theorem and the one-unitary-group theorem, whose closing paragraph already states the count and "met, not saturated"), so nothing new is proved here, and a status of proved on the entity that the paper''s Assembly points to would read as a proof of the window law, which is clause (e) and is not proved. The entity therefore records the paper''s estimate together with the proved statements it rests on, each cited as a stored theorem. Tested before restating: circularity (the past cones of the cited theorems do not contain this entity; their former edges to it are text mentions since version 6); object (the proved count is about affine cells of a horizon generator, not about the window''s counted modes, and only the cell at the edge covers the first N cells); mechanism (the accepted derivation''s growth step is the rotor flow''s, a count in rapidity, while the proved real-time count has amplitudes falling as e^(-kappa t/2)); orientation (the affine-cell theorem and the one-unitary-group theorem use opposite signs of the time parameter for the same dilation group, a difference between the two stored theorems; the count is the same). The word "saturated" survives only in the id, which is historical; the title says met, not saturated. No listed open problem holds the estimate; the settled problem on the two boost flows lists chaotic dynamics of the windows as not covered. The dependant scrambling.return-delay-scrambling-log-recovered (conjectured) cites this entity at version 6 and is to be read against the new statement before its pin moves.'
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
\emph{What this entity records.} The spreading law of the scrambling paper (its Assembly on spreading), $t_{*} = \kappa^{-1}\ln N = (\beta/2\pi)\ln S$ for the $N$ counted modes of a window, is an estimate: it is stated in (e) and it is what is conjectured here. It rests on four statements that are proved elsewhere in the store, (a) to (d), which are cited as stored theorems; this entity adds nothing to them.
\begin{enumerate}
\item[(a)] \emph{(Real-time count on a generator; stored, Theorem \claimref{synthesis.affine-cell-boost-spreads-without-scrambling}(i), (ii).)} On the continuum mode space of one generator of a Killing horizon of surface gravity $\kappa$, with affine parameter $U > 0$, let $(D_{t}f)(U) = e^{-\kappa t/2}f(e^{-\kappa t}U)$ be the unitary dilation group and $\chi_{j}$ the normalised indicators of the affine cells $[j\delta, (j+1)\delta)$. For $e^{\kappa t} = N$ an integer, $D_{t}\chi_{j} = N^{-1/2}\sum_{l=0}^{N-1}\chi_{Nj+l}$. The boost time evolution on the generator is this group (Theorem \claimref{synthesis.boost-evolution-on-generators-is-one-unitary-group}, which writes it $a(f) \mapsto a(D_{-\lambda}f)$, with the time parameter reversed relative to the theorem just cited, and notes that at a Killing horizon the flow acts on the affine parameter as $u \mapsto e^{\pm\kappa t}u$). So the mode operator of one cell covers $N$ cells after a lapse of Killing time
\[
|t_{*}| \;=\; \kappa^{-1}\ln N
\]
in the direction of time in which the flow dilates the affine parameter of that generator; in the other direction the same flow compresses the cell. The lapse does not depend on the sign convention. The cell at the edge, $j = 0$, covers the first $N$ cells, and a cell $j \ge 1$ covers $N$ cells further out. The amplitudes fall: every anticommutator of the evolved mode operator with a fixed cell operator is at most $N^{-1/2}$.
\item[(b)] \emph{(Count in rapidity on the ladder; stored.)} The intrinsic flows of a Clifford boundary-mode algebra are bivector-generated (Lemma \claimref{scrambling.clock-inventory-boundary-modes}(i)), and the boost rotor $\exp(\kappa t\,\sigma/2)$, $\sigma = e_{+}e_{-}$, scales the ladder operators of every mode by $e^{\mp\kappa t}$, with one rapidity for all modes, as a one-parameter group (the weight clause of Fact \claimref{scrambling.imported-modes-modular-inventory}); an amplitude $1/N$ carried by it reaches one exactly when $e^{\kappa t} = N$. This rotor flow is not a time evolution of the windows: it is the continuation of the phase flow to the KMS strip (Theorem \claimref{synthesis.phase-flow-is-time-rotor-flow-kms-continuation}). In this reading $\kappa t_{*} = \ln N$ counts rapidity, not Killing time.
\item[(c)] \emph{(The rate; stored, under (N$_{+}$).)} Under (N$_{+}$) the state of the generator's modes is thermal for the boost at rapidity period $2\pi$ (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}), that is $\kappa\beta = 2\pi$ in Killing time. So in both readings the lapse is $(\beta/2\pi)\ln N$, with $\beta/2\pi = 4M$ for the Schwarzschild field, and the rate at which the support of (a) dilates is $2\pi T$.
\item[(d)] \emph{(The chaos bound is met, not saturated; stored.)} The real-time Lyapunov exponent of the dynamics of (a) is $0$: it is one unitary group with bounded anticommutators on linear elements (Theorem \claimref{synthesis.boost-evolution-on-generators-is-one-unitary-group}(v), whose closing paragraph states the count of (a) and this conclusion). The equality of the dilation rate with $2\pi T$ is the equality of one group's rate with its own KMS rate, not growth of the out-of-time-order correlators that the Maldacena-Shenker-Stanford bound limits \cite{MSS2016}.
\item[(e)] \emph{(The estimate; conjectured.)} For the $N$ counted modes of a window (Theorem \claimref{scrambling.mode-count}), support deposited on one mode spans the window at $t_{*} = \kappa^{-1}\ln N = (\beta/2\pi)\ln S$, the fast-scrambling form. This is the paper's law. It needs three steps beyond (a) to (d), none of which is proved. First, that the window's modes are the affine cells of (a): the count depends on that basis, since on boost-adapted cells the same flow displaces without spreading (clause (iii) of Theorem \claimref{synthesis.affine-cell-boost-spreads-without-scrambling}), and every dynamics that Premise (L$_{E}$) admits on the windows spreads nothing along chains in real time (Theorem \claimref{synthesis.number-diagonal-dynamics-spreads-nothing}). Second, that $N$ equals $S$ up to a factor of order one, which Proposition \claimref{scrambling.area-law-test} gives only for an epoch of order $M$, with a calibration. Third, that covering the cells is scrambling, which by (d) it is not in the sense of the chaos bound. The paper's own step, an amplitude growing as $e^{\kappa t}$ under a generic quadratic coupling against a suppression of order $1/N$, is reading (b) and not a real-time mechanism. Chaotic dynamics beyond the quasi-free flow is open.
\end{enumerate}

## technical
This entity records the spreading law of the scrambling paper, which is an estimate, together with the proved statements it rests on; those are stored theorems, cited here, and nothing new is proved.

The estimate: support deposited on one of a window's $N$ counted modes spans the window at $t_{*} = \kappa^{-1}\ln N = (\beta/2\pi)\ln S$, the fast-scrambling form.

What the store proves. On one generator of a Killing horizon the boost acts in real time as a unitary dilation of the affine parameter, and in the basis of affine cells it spreads the mode of one cell uniformly over $N$ cells in a lapse $\kappa^{-1}\ln N$ of Killing time, in the direction of time in which the flow dilates, with amplitudes falling as $N^{-1/2}$. On the ladder operators of a boundary-mode algebra the boost rotor scales every mode by $e^{\mp\kappa t}$, so an amplitude $1/N$ reaches one at the same value of $\kappa t$; but that rotor flow is the KMS-strip continuation of the time evolution, so there the count is in rapidity. Under (N$_{+}$), $\kappa\beta = 2\pi$, so the lapse is $(\beta/2\pi)\ln N$ and the support dilates at the rate $2\pi T$. The real-time Lyapunov exponent of this quasi-free dynamics is $0$, so the Maldacena-Shenker-Stanford chaos bound is met, not saturated.

What the estimate adds, unproved: that the window's modes are the affine cells (on boost-adapted cells nothing spreads, and under the locality premise (L$_{E}$) the windows' admissible dynamics does not spread along chains), that $N$ is of the order of $S$ (an epoch of order $M$, with a calibration), and that covering cells is scrambling. Chaotic dynamics beyond the quasi-free flow is open.

## lay
This entry records an estimate made in the series' paper on scrambling, and the proved facts behind it. The estimate is that a disturbance entering a black hole's interior modes reaches all of them after a time that grows with the logarithm of the entropy, the fast-scrambling time. It is not proved.

What is proved, in other entries of the store, concerns a single light ray of the horizon. There the hole's own stretching motion spreads a disturbance that starts in one small cell over more and more cells, doubling their number at a steady pace, so that after a time growing with the logarithm of the number of cells it covers that many. The pace equals the rate named by a known general bound on chaos, under the series' premise that the modes on each light ray are in their lowest-energy state. But the spreading is not chaos: the disturbance thins out as it spreads and nothing grows, so the bound is met rather than saturated.

The step from that picture to the interior modes is where the estimate lies: it depends on how the interior modes are identified with cells along the ray, and under the series' locality premise those modes do not pass disturbances along in ordinary time at all.

## one-liner
Records the scrambling paper's estimate that support spans a window's $N$ counted modes at $t_{*} = \kappa^{-1}\ln N = (\beta/2\pi)\ln S$ (conjectured), with the stored theorems it rests on: the boost spreads one affine cell of a horizon generator over $N$ cells in a lapse $\kappa^{-1}\ln N$ of Killing time with falling amplitudes, its rotor reaches the same count in rapidity, $\kappa\beta = 2\pi$ under (N$_{+}$), and the real-time Lyapunov exponent is $0$, so the chaos bound is met, not saturated.
