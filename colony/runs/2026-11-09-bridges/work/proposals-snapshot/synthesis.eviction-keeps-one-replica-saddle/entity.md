---
id: synthesis.eviction-keeps-one-replica-saddle
kind: claim
version: 4
title: 'At Renyi index two, eviction keeps one of two replica saddles'
status: proved
region: synthesis
subject: entropy
tags: [boundary-modes, entanglement, dictionaries]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'GA rewrite (the complex field named by its unit)'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Fable 5.2
  role: 'restatement on the mode split of the Clifford algebra; random-state column on a parity sector'
  version: 4
  source: run 2026-11-09-bridges
amendments:
- version: 4
  kind: restatement
  defect: 'Window and radiation were split by a tensor product of abstract spaces and the random-state value of clauses (iii), (iv) was the one for such a product; the modes are fermionic, the states fixed by the total-parity average are even and lie in one parity sector, which is not a tensor product, and there the mean purity is (m + n)/(mn + 2), not (m + n)/(mn + 1). Leading terms and every eviction-side clause are unchanged. The claimref to synthesis.imported-haar-average-purity is removed from the proof.'
  evidence: check.py::check_mode_split_and_parity_sector_column
review: draft
derivations:
- name: main
  uses:
  - singularity.eviction-window-thermal-product-radiation-entropy@7
  - synthesis.eviction-deficit-against-page-deficit@4
  - singularity.imported-page-average-entropy-subsystem@1
  - tower.commuting-copies@5
  - singularity.descent-parity-average@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_member_purity_in_pauli_algebra
- kind: check
  ref: check.py::check_eviction_purity_is_one_saddle
- kind: check
  ref: check.py::check_haar_purity_against_two_saddles
- kind: check
  ref: check.py::check_crossing_ratios
- kind: check
  ref: check.py::check_mode_split_and_parity_sector_column
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - note.singularity.island-dictionary-one-dissonance
  - synthesis.eviction-deficit-against-page-deficit
extraction:
  restatement_mode_split:
    by: ai-contributor
    date: '2026-11-09'
    note: >-
      Version 3 -> 4, at Leon's request (his decision of 9 November 2026) that the tensor product of the eviction comparisons be replaced by the
      split in the algebra. The modes are null pairs of a Clifford algebra, a subsystem is the sub-Clifford
      algebra of its modes, reduction is the projection onto its blades; the relation to the tensor product is
      the stored commuting-copies twist, and for even states the two splits give the same reduced states. The
      eviction clauses (i), (ii), (v) are unchanged. The random-state value of (iii), (iv) is now stated for the
      even states (one parity sector), with the value for an abstract tensor product kept beside it for
      comparison; the gap at the crossing changes from ln 2 - ln(1 + m^{-2}) to ln 2 - ln(1 + 2 m^{-2}). The
      claimref to synthesis.imported-haar-average-purity is removed (Leon's decision to retire that Fact); both
      second moments are obtained in the proof from Schur's lemma on a symmetric square, as before. Intended
      citations, not made because they are proposals of the same session: the split, the twist and the sector
      values are synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product (the
      preliminary paragraph of the proof repeats what is needed from it and can be cut to a reference once it
      is accepted); the sector purity is also clause (iv) of
      synthesis.finite-normaliser-averages-leave-the-haar-moments-at-order-four-and-on-a-parity-sector; the
      second moment derived without Schur's lemma is
      synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three. Kill condition
      registered before computing: a leading term changes on the split (did not fire).
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3. The complex-field stand-in \C is tied to its unit, span{1, I_4} (U1, an abstract Hilbert space), by one parenthetical at its first use (readers R02 and R08: the language check does not flag the macro). Notation only; the mathematics is unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'The two literature sources are now stored Facts and are cited by claimref in the proof: Lubkin''s Haar purity at clause (iii) (synthesis.imported-haar-average-purity; through version 3; removed at version 4) and the replica-wormhole purity and Page agreement in the Reading (synthesis.imported-replica-wormhole-two-saddle-purity). Text only: clause (iii) is proved in the proof, and the replica computation enters only the Reading, so neither is a premise and uses is unchanged. Version 1 -> 2.'
  open_problem: op.island-dictionary
  note: >-
    The problem asks for a term-by-term map between eviction and the island computation, or a quantity on which
    they differ, and notes that the store has no Fact saying the island computation reproduces the Page-typical
    branch below leading order. At Renyi index two the replica computation is a sum of two saddles, which makes
    the comparison exact and rational. Literature, checked against the source: Penington, Shenker,
    Stanford and Yang, Replica wormholes and the black hole interior, arXiv:1911.11977, Sec. 2.2 Eq. (2.13),
    Tr rho_R^2 = 1/k + Z_2/Z_1^2 (disconnected saddle plus replica wormhole), Eq. (2.15), schematically
    1/k + e^{-S_0}, and Sec. 2.5.1 Eq. (2.38), whose microcanonical resolvent equations are "precisely the same
    ones found by Page"; Sec. 2.5.2 and Fig. 7, the canonical transition smoothed over a region of size
    G_N^{-1/2} in log k. Kawabata, Nishioka, Okuyama and Watanabe, arXiv:2102.02425, abstract and Sec. 2.1: the
    radiation's capacity of entanglement peaks near the Page time. Lubkin (1978) for the Haar average purity,
    recomputed exactly in the check. The two-saddle purity (2.13)/(2.15) with the microcanonical agreement with
    Page (Sec. 2.5.1) is the Fact synthesis.imported-replica-wormhole-two-saddle-purity, and the Haar purity the
    Fact synthesis.imported-haar-average-purity (through version 3; removed at version 4). The
    theorem's statements are proved without them; the literature enters only in reading the two-saddle value as
    the island computation's. Transport-absent.
---

## formal
Work under the hypotheses of Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy}, with window $W(t)$, capacity $C(t) = |W(t)|\ln 2$, member marginals $\operatorname{diag}(c_{k}^{2}, s_{k}^{2})$, and the radiation $R$ purifying the window. The modes of window and radiation are the null pairs $v_{k} = \tfrac12(e_{k} + f_{k})$, $w_{k} = \tfrac12(e_{k} - f_{k})$ of a Clifford algebra with generators $e_{k}, f_{k}$, $Q(e_{k}) = 1$, $Q(f_{k}) = -1$, with mode parity $p_{k} = 1 - 2w_{k}v_{k} = f_{k}e_{k}$; a subsystem is the sub-Clifford algebra generated by its modes, reduction to it is the projection onto its blades times the dimension of the complementary subsystem, the trace of a subsystem of $a$ modes is $2^{a}\langle\cdot\rangle_{0}$, and the states are even: they commute with the product $\Gamma$ of all $p_{k}$, that is, they are fixed by $x \mapsto \tfrac12(x + \Gamma x\Gamma)$, the total-parity form of the single-mode average of Theorem \claimref{singularity.descent-parity-average}. No tensor product is used; for even states this split gives the same reduced states as the tensor product obtained from it by the twist of Theorem \claimref{tower.commuting-copies} (shown in the proof). A member's marginal is $\rho_{k} = \tfrac12(1 + r_{k}p_{k})$, $r_{k} = c_{k}^{2} - s_{k}^{2}$, in the algebra of its mode, with trace $2\langle\cdot\rangle_{0}$. Then:
\begin{enumerate}
\item[(i)] (purity at every weight) $\operatorname{tr}\rho_{R}^{2} = \operatorname{tr}\rho_{L}^{2} = \prod_{k \in W(t)}(c_{k}^{4} + s_{k}^{4})$, with $c_{k}^{4} + s_{k}^{4} = 2\langle\rho_{k}^{2}\rangle_{0} = \tfrac12(1 + r_{k}^{2})$; one product, the purity of the current window;
\item[(ii)] (zero weight: one saddle) if every member has zero weight, after $j$ radiated quanta (radiation dimension $k = 2^{j}$) at a stage where the capacity bound on the window (the stretched-singularity capacity of the rate model) is $n_{\mathrm{cap}}\ln 2$, so that $|W(t)| = \min(j, n_{\mathrm{cap}})$ and $C(t) = \min(j, n_{\mathrm{cap}})\ln 2$, the radiation purity is exactly
\[
\operatorname{tr}\rho_{R}^{2} = \max\bigl(1/k,\ e^{-n_{\mathrm{cap}}\ln 2}\bigr) ,
\]
the larger of the two terms of the two-saddle value $P_{2} := 1/k + e^{-n_{\mathrm{cap}}\ln 2}$, and never their sum;
\item[(iii)] (the random-state average) for a pure even state of $a + b$ modes, $m = 2^{a}$, $n = 2^{b}$, $a, b \ge 1$ (numbers read in $\mathrm{span}\{1, I_4\}$, conventions, the unit principle), drawn from the unitarily invariant measure of its parity sector, the reduction to the $a$ modes has $\langle\operatorname{tr}\rho_{A}^{2}\rangle = (m + n)/(mn + 2)$, which lies strictly between the one-saddle value $\max(1/m, 1/n)$ and the two-saddle value $1/m + 1/n$, below the latter by $2(m + n)/(mn(mn + 2))$. Without the parity condition, for a pure state of an abstract tensor product of spaces of dimensions $m$ and $n$, the value is $(m + n)/(mn + 1)$, which lies between the sector value and the two-saddle value, below the latter by $(m + n)/(mn(mn + 1))$;
\item[(iv)] (the crossing) at $j = n_{\mathrm{cap}}$ ($m = n$): eviction purity $1/m$, two-saddle $2/m$, random even state $2m/(m^{2} + 2)$ (abstract tensor product: $2m/(m^{2} + 1)$). In Renyi-2 entropy $S_{2} = -\ln\operatorname{tr}\rho^{2}$, the eviction branch sits at the capacity exactly, the two-saddle value exactly $\ln 2$ below it, and the random-state value below it by $\ln 2 - \ln(1 + 2m^{-2}) \in (\ln 2 - 2m^{-2}, \ln 2)$ (abstract tensor product: $\ln 2 - \ln(1 + m^{-2}) \in (\ln 2 - m^{-2}, \ln 2)$). At distance $d = |j - n_{\mathrm{cap}}|$ from the crossing the two-saddle value lies below the eviction one by $\ln(1 + 2^{-d})$;
\item[(v)] (baseline) at every weight the falling branch $S_{R} = \sum_{k \in W(t)}h_{k}$ is the thermal entropy of the window, with no correction; the deficit of clause (iii) of Theorem \claimref{synthesis.eviction-deficit-against-page-deficit}, linear in the window when the weights are bounded away from zero (as every member's is under the weights $\kappa(k + \tfrac12)$ of (Q) version 3, $|x_{k}| \geq \pi$), is measured against the window's maximal entropy $C$, which is its thermal entropy only at zero weight.
\end{enumerate}
So at Renyi index two the dictionary is term by term: the rising branch of eviction is the disconnected saddle $1/k$, the falling branch the replica-wormhole saddle $2^{-n_{\mathrm{cap}}}$, and eviction keeps whichever dominates where the replica computation adds them. The quantity on which they differ is the subdominant saddle, $\ln(1 + 2^{-d})$ in $S_{2}$, largest ($\ln 2$) at the crossing, and the random-state branch, on a parity sector or on an abstract tensor product, agrees with the two-saddle one there to $O(m^{-2})$. That the two-saddle value is the island computation's is the literature reading of the note, not a premise of the theorem.

## technical
The island computations of the Page curve are replica computations: the $n$-th Renyi entropy of the radiation is a gravitational path integral summed over geometries joining $n$ copies. At $n = 2$ only two saddles matter at leading order, the disconnected one, giving purity $1/k$ for $k$ radiation states, and the replica wormhole, giving $e^{-S}$ with $S$ the black hole's entropy; the island answer adds them. Reading the black hole's entropy as the capacity bound of the window, $e^{S} = 2^{n_{\mathrm{cap}}}$, is the identification that makes the comparison below; it is a reading of the dictionary, not a result. The eviction mechanism of the series, at zero weight, gives exactly the larger of the two at every stage: on the rising branch the radiation is maximally mixed on its $k$ states, on the falling branch the window, filled to its capacity bound, is maximally entangled with it, and the purity is never the sum. So the two mechanisms map onto each other saddle by saddle, and differ by the subdominant saddle, worth exactly $\ln 2$ of Renyi-2 entropy at the crossing and falling off as $\ln(1 + 2^{-d})$ with the distance $d$ in qubits from it. The split of window from radiation is made in the Clifford algebra of the modes (each side the sub-Clifford algebra of its modes, reduction by projection onto its blades), not by a tensor product; for the even states, those fixed by the total-parity average, the two give the same reduced states, so every eviction statement here is unchanged. A random even state, the Page-typical branch on one parity sector, has the exact average purity $(m + n)/(mn + 2)$ (it would be $(m + n)/(mn + 1)$ for an abstract tensor product with no parity condition); either agrees with the two-saddle value to order $m^{-2}$ at the crossing. At any weights, eviction's falling branch is exactly the thermal entropy of the window; the store's earlier comparison at weights bounded away from zero, which covers every mode of the adopted half-integer weights, measured it against the window's maximal entropy instead, so the extensive difference found there is a choice of baseline, not of mechanism.

## lay
Modern calculations of how information comes back out of an evaporating black hole compare two ways the geometry can join copies of the system, and add their contributions. The series has its own mechanism, in which the boundary modes hand their entanglement to the outgoing radiation. Measured with a convenient entropy (the second Renyi entropy), the series' mechanism turns out to follow exactly whichever of the two contributions is larger at each moment, while the standard calculation adds both. The two descriptions therefore line up piece by piece, once the black hole's entropy in the standard calculation is identified with the series' capacity (an identification, not a derivation), and they differ by exactly the smaller piece, which is largest, one bit's worth, at the halfway point of evaporation. A random quantum state, the usual benchmark, agrees with the standard calculation there, whether or not it is restricted, as the series' states are, to a definite even or odd particle number.

## one-liner
At Renyi index two eviction keeps one replica saddle: at zero weight its radiation purity is exactly $\max(2^{-j}, 2^{-n})$ ($j$ radiated quanta, capacity bound $n\ln 2$) where the two-saddle value $2^{-j} + 2^{-n}$ (the replica-wormhole purity, read with $e^{S_{0}} = 2^{n}$) and the random even state $(2^{j} + 2^{n})/(2^{j + n} + 2)$ (split in the Clifford algebra of the modes, one parity sector), so at the crossing eviction sits exactly $\ln 2$ of Renyi-2 entropy above the two-saddle value; at every weight its falling branch is the window's thermal entropy.
