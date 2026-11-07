---
id: synthesis.number-diagonal-dynamics-spreads-nothing
kind: claim
version: 2
title: 'Number-diagonal dynamics has no exponential operator spreading'
status: proved
region: synthesis
subject: entropy
tags: [boundary-modes, entropy-premises, no-go, finite-models]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle (U1 to U6)
  version: 2
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
derivations:
- name: main
  uses:
  - singularity.modular-structure-completed-pair@5
  - singularity.number-diagonal-dynamics-models-scrambling-derived@4
  - synthesis.phase-flow-is-time-rotor-flow-kms-continuation@3
  - scrambling.spreading-law-chaos-bound-saturated@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_diagonal_support_never_grows
- kind: check
  ref: check.py::check_real_time_dressing_exact
- kind: proof
  derivation: main
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle (U2) numbers on the completed pairs are read in span{1, J}, J = e_2 e_3 the complex unit of the radial atom (synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom, cited in the formal level): the phase flow e^{JtH}, the dressing e^{-2JtH_1}, e^{-2J h_j t}, the factors cos 2g t - J sin 2g t sigma_k, the terms e^{J omega t}, the check''s unitaries cos theta + J sin theta sigma_0 sigma_k and the spectral terms of the proof are written with J; the coupling constants, written J_{jk} and J in the source, are renamed g_{jk} and g so as not to clash with the unit; the outside_ga declaration is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the modes are the completed pairs of singularity.modular-structure-completed-pair, whose unit_note keeps a scalar i (atom in the plane e0e1, I_4 anticommuting with the modes, known limit 1); declared (version and levels unchanged). Declaration kind set to complex-analysis by Leon''s ruling R1 (atom, boundary-mode and window flows keep i).'
  open_problem: op.which-boost-flow-is-time
  flow_note: phase; every evolution here is the unitary phase flow Ad(e^{itH}) (see synthesis.phase-flow-is-time-rotor-flow-kms-continuation).
  tension_with:
  - id: scrambling.spreading-law-chaos-bound-saturated@1
    clause: the expansion computation (amplitude reaching a mode at mode distance d grows as e^{kappa t})
    note: >-
      Under (L_E) every generator is number-diagonal (singularity.number-diagonal-dynamics-models-scrambling-derived),
      and by (i)-(ii) here the amplitude at mode distance d >= 2 in the coupling graph is identically
      zero for all real t. The stored law's growth step therefore has no real-time reading inside
      (L_E), quadratic or not; synthesis.phase-flow-is-time-rotor-flow-kms-continuation already reads
      it as an imaginary-time (rotor-flow) step for quadratic generators.
  - id: singularity.number-diagonal-dynamics-models-scrambling-derived@3
    clause: the phrase "the diagonal scrambling of the finite-mode model" for the controlled-Z circuit
    note: >-
      Vocabulary, not mathematics. By (iii) here the controlled-Z (number-diagonal) dynamics does
      produce support growth: with all-to-all couplings the mean operator size reaches half the window
      at t = pi/(8J). It produces no exponential growth of support, of local commutators or of
      out-of-time-order correlators, which are almost periodic. If "scrambling" means the
      exponential-growth law, the stored phrase should be read as support growth (dressing), not
      scrambling; the maintainer should decide the wording.
  note: >-
    Closes the successor item left by synthesis.phase-flow-is-time-rotor-flow-kms-continuation
    (real-time spreading needs non-quadratic dynamics) in the negative for the whole class (L_E)
    admits, in this vocabulary: support growth means the operator size grows; exponential growth
    means size, local commutators or out-of-time-order correlators grow as e^{kappa t}. Number-diagonal
    generators, quadratic or not, give support growth only onto directly coupled modes (possibly all
    modes, in time O(1/J) independent of n) and never exponential growth, so the kappa^{-1} ln N law
    needs a generator that (L_E) excludes (hopping, pairing or an unsupplied generator). This is the
    obstruction pr.locality-and-interface records. The mathematics is elementary (commuting
    dynamics); it is transport-absent. The result says nothing about dynamics outside the diagonal
    algebra. Complementary result filed alongside, synthesis.affine-cell-boost-spreads-without-scrambling
    (support growth from a hopping generator, which (L_E) excludes at E, without exponential commutator
    growth); same vocabulary.
---

## formal
Let $v_{1}, \dots, v_{n}$ satisfy the CAR, let $\sigma_{k} = v_{k}^{*}v_{k} - v_{k}v_{k}^{*}$ (Theorem \claimref{singularity.modular-structure-completed-pair}), and let $\mathcal{D}$ be the abelian algebra the $\sigma_{k}$ generate, the joint-number-diagonal algebra. Numbers are read in $\mathrm{span}\{1, J\}$, $J = e_{2}e_{3}$ the complex unit of the completed pairs, which commutes with their mode operators (\claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}); the coupling constants are written $g_{jk}$. Let $H = H^{*} \in \mathcal{D}$ and, for a mode $j$, write uniquely $H = H_{0}^{(j)} + \sigma_{j}H_{1}^{(j)}$ with $H_{0}^{(j)}, H_{1}^{(j)}$ in the algebra of $\{\sigma_{k} : k \neq j\}$; let $N(j)$, the coupling neighbourhood of $j$, be the set of modes on which $H_{1}^{(j)}$ depends. Then:
\begin{enumerate}
\item[(i)] $\operatorname{ad}_{H}^{m}(v_{j}) = v_{j}(-2H_{1}^{(j)})^{m}$ for every $m \ge 0$, and the phase flow gives $e^{JtH}v_{j}e^{-JtH} = v_{j}\,e^{-2JtH_{1}^{(j)}}$ for every real $t$: the evolved mode operator is $v_{j}$ times a diagonal unitary of the modes of $N(j)$;
\item[(ii)] its support never leaves $\{j\}\cup N(j)$: for every mode $l \notin \{j\}\cup N(j)$ and every $t$, $e^{JtH}v_{j}e^{-JtH}$ anticommutes with $v_{l}$ and $v_{l}^{*}$, so every out-of-time-order correlator of $v_{j}$ with a mode outside its coupling neighbourhood is independent of $t$;
\item[(iii)] if $H_{1}^{(j)} = h_{j} + \sum_{k \in N(j)}g_{jk}\sigma_{k}$, then $e^{JtH}v_{j}e^{-JtH} = e^{-2Jh_{j}t}\,v_{j}\prod_{k \in N(j)}(\cos 2g_{jk}t - J\sin 2g_{jk}t\,\sigma_{k})$; in the trace inner product the operators $v_{j}\sigma_{S}$, $S \subseteq N(j)$, are orthogonal of equal norm, the weight on size $|S|$ is $\prod_{k \notin S}\cos^{2}2g_{jk}t\prod_{k \in S}\sin^{2}2g_{jk}t$, and the mean size $\sum_{k \in N(j)}\sin^{2}2g_{jk}t$ is an almost periodic function, at most $|N(j)|$, vanishing at $t = 0$; with $n - 1$ uniform couplings $g$ it is $(n-1)\sin^{2}2gt$, which first reaches half the window at $t = \pi/(8g)$ for every $n$;
\item[(iv)] by contrast a generator outside $\mathcal{D}$ does propagate: with a hop on the chain $1$-$2$-$3$ added to $\sigma_{0}\sigma_{1}$, $\operatorname{ad}^{m}(v_{0})$ first involves mode $m$ at order $m$.
\end{enumerate}
Since every generator (L$_{E}$) admits lies in $\mathcal{D}$ (Proposition \claimref{singularity.number-diagonal-dynamics-models-scrambling-derived}), no dynamics the locality premise admits, quadratic or not, carries operator support beyond direct couplings in real time, and none produces exponential growth: the mean size, the matrix elements of every local commutator and every out-of-time-order correlator of $v_{j}$ are finite sums of terms $e^{J\omega t}$, almost periodic and bounded. With all-to-all couplings the support does grow to the whole window, the mean size reaching half the window in time $\pi/(8g)$, independent of $n$. The exponential growth step of Proposition \claimref{scrambling.spreading-law-chaos-bound-saturated}, and with it the law $t_{*} = \kappa^{-1}\ln N$, therefore has no real-time reading inside (L$_{E}$); it needs a generator that (L$_{E}$) excludes.

## technical
Every generator the locality premise (L$_{E}$) allows is diagonal in the joint number basis. For such a generator the Heisenberg evolution of a mode operator is exact and elementary: $v_{j}(t) = v_{j}e^{-2JtH_{1}}$, where $H_{1}$ collects the terms of the generator that contain $\sigma_{j}$, stripped of it. The evolved operator is $v_{j}$ dressed by a diagonal unitary of the modes coupled directly to $j$, and nothing else.

So operator support never travels along chains: a mode that is reached only through a chain of couplings is never reached at any time, and out-of-time-order correlators with such modes stay constant. Support does grow onto the directly coupled modes: for two-body couplings the dressing is a product of single-mode rotations, and the average operator size is $\sum_{k}\sin^{2}2g_{jk}t$, bounded by the number of direct couplings and recurring towards zero. With uniform all-to-all couplings it reaches half the window at $t = \pi/(8g)$, independently of the number of modes: support growth in a time that does not grow with $n$, but no exponential growth of size, commutators or out-of-time-order correlators, all of which are almost periodic.

A hop, which (L$_{E}$) excludes, does propagate support one mode per order. Hence the fast-scrambling law's exponential growth step, already read as an imaginary-time rotor-flow step for quadratic generators, has no real-time reading for any dynamics (L$_{E}$) admits: the law $t_{*} = \kappa^{-1}\ln N$ in real time and (L$_{E}$) cannot both hold.

## lay
The series models a black hole's boundary as a collection of quantum bits and claims that information spreads through them as fast as physics allows. The series also assumes that the bits' internal dynamics never moves anything from one bit to another; it may only make each bit's phase depend on its neighbours' states. This result shows that such dynamics spreads a disturbance only to the bits it is directly wired to, which may be all of them, never onward to their neighbours in turn, and that its reach oscillates instead of growing exponentially. So the exponential spreading law the series describes cannot happen in real time under its own locality assumption; one of the two must give.

## one-liner
Under any number-diagonal generator, the only kind (L$_{E}$) admits, an evolved mode operator is the mode times a diagonal unitary of its direct couplings, so support reaches only directly coupled modes, size and out-of-time-order correlators are almost periodic, and the exponential $\kappa^{-1}\ln N$ spreading law in real time needs a generator (L$_{E}$) excludes.
