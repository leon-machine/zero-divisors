---
id: synthesis.eviction-deficit-against-page-deficit
kind: claim
version: 3
title: At zero weight, and at large windows with weights bounded away from zero, the eviction falling branch and the Page-typical one differ, by a deficit that is zero or extensive against one that is positive and below one nat
status: proved
region: synthesis
subject: entropy
tags: [boundary-modes, entanglement, dictionaries]
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
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics
derivations:
- name: main
  uses:
  - singularity.eviction-window-thermal-product-radiation-entropy@7
  - singularity.imported-page-average-entropy-subsystem@1
  - singularity.assembled-page-curve-up-typicality@3
  - synthesis.boundary-mode-thermal-entropy@2
  - synthesis.imported-pinsker-inequality@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_page_deficit_bounds
- kind: check
  ref: check.py::check_eviction_deficits
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - note.singularity.island-dictionary-one-dissonance
  - singularity.assembled-page-curve-up-typicality
extraction:
  maintainer_pass_2:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'check_eviction_deficits strengthened: s(0) = ln 2 and zero deficit sum computed; Pinsker bound equals (1/2) tanh^2(x_*/2) and the window threshold computed at sample weights. Version 2 -> 3.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Maintainer pass: Pinsker''s inequality, cited from memory in (iii), is now the imported Fact synthesis.imported-pinsker-inequality, added to uses and cited in the proof and check. Version 1 -> 2.'
  open_problem: op.island-dictionary
  note: >-
    Compares the subleading structure of the two falling branches the store holds: the
    eviction theorem's exact one and the Page-typical one assembled in the typicality Fact,
    which is the falling branch replica-wormhole computations reproduce. The deficit below
    capacity is zero (zero weight) or grows linearly with the window (weights bounded away
    from zero) for eviction, and is strictly positive and below one nat, about one half at the
    crossing, for typical states. So in both regimes the two never coincide stage by stage: at the registered
    calibration they agree at leading order and differ by about half a nat at the crossing.
    Transport-convenient: the eviction side is the series' theorem; the Page side is imported.
---

## formal
Let $L$ be the window, with $|W(t)|$ members and capacity $C = |W(t)|\ln 2$, and $R$ the radiation, under the hypotheses of Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy}, whose clause (4) gives the eviction deficit
\[
\delta_{\mathrm{ev}}(t) \;:=\; C(t) - S_{R}(t) \;=\; \sum_{k \in W(t)}\bigl(\ln 2 - h_{k}\bigr) ,
\]
with $h_{k} = s(x_{k})$ the mode entropy at $x_{k} = 2\pi\omega_{k}/\kappa$ (Theorem \claimref{synthesis.boundary-mode-thermal-entropy}). For a pure state on $\C^{m} \otimes \C^{n}$, $m \le n$, drawn from the unitarily invariant measure, let $\delta_{\mathrm{P}}(m, n) := \ln m - \langle S_{A}\rangle$ be the Page deficit, with $\langle S_{A}\rangle$ as in Fact \claimref{singularity.imported-page-average-entropy-subsystem}; the Page-typical falling branch of Fact \claimref{singularity.assembled-page-curve-up-typicality} has $\dim L = m$ after the crossing. Then:
\begin{enumerate}
\item[(i)] (the typical deficit) for all $2 \le m \le n$,
\[
\frac{m - 1}{2n} \;<\; \delta_{\mathrm{P}}(m, n) \;<\; \frac{m - 1}{2n} + \frac{m - 1}{mn + 1} \;<\; 1 ,
\]
so the Page-typical falling branch lies strictly below capacity at every stage, by about $\tfrac12$ nat at the crossing $m = n$ and by a deficit halving with each further radiated qubit;
\item[(ii)] (zero weight) if every window member has zero weight, $\delta_{\mathrm{ev}} = 0$ at every stage: the eviction falling branch is the capacity exactly, and differs from the Page-typical one by $\delta_{\mathrm{P}} > 0$ at every stage, most at the crossing;
\item[(iii)] (weights bounded away from zero) if every window member has $|x_{k}| \ge x_{*} > 0$, then $\delta_{\mathrm{ev}} \ge \tfrac12|W(t)|\tanh^{2}(x_{*}/2)$, linear in the window size; for (Q)'s weights $x_{k} = 2\pi|k|$ every member with $k \neq 0$ contributes more than $\tfrac12$ nat, so two such members already put $\delta_{\mathrm{ev}}$ above every Page deficit.
\end{enumerate}
Hence for neither uniform zero weight nor weights bounded away from zero does the eviction falling branch coincide with the Page-typical one at any stage with $\dim L \ge 2$ (respectively, once $|W(t)| > 2/\tanh^{2}(x_{*}/2)$, and for (Q)'s weights once two members of nonzero weight are in the window): in these two regimes the two are distinct mechanisms below leading order. Small windows with nonzero weights, and mixed or small weights, are not covered: there $\delta_{\mathrm{ev}}$ can take intermediate values. At the registered calibration (zero weight) the eviction branch is the sharp $\min(\Sth, C)$ with no rounding, and the quantity separating it from the typical branch is the deficit at the crossing, $0$ against $\delta_{\mathrm{P}}(m, m) \in (\tfrac25, \tfrac12 + \tfrac1m)$ for $m \ge 4$.

## technical
The store holds two accounts of the falling branch of the Page curve. The eviction theorem gives it exactly, with no typicality: the radiation entropy equals the capacity minus the sum of the window members' shortfalls from $\ln 2$. The typicality Fact assembles it from Page's theorem, which says a random pure state sits a definite amount below the maximum: more than $(m-1)/2n$ and less than one nat, about one half at the crossing and halving with each further qubit radiated. The two deficits behave differently in the two regimes treated here. With all weights zero the eviction deficit vanishes identically, so the eviction curve is the sharp minimum of the thermal and capacity curves; the typical curve is rounded at the crossing by about half a nat. With weights bounded away from zero the eviction deficit grows in proportion to the window, by Pinsker's inequality, while the typical deficit stays below one nat. So the eviction mechanism and the typicality mechanism, the latter being the falling branch that replica-wormhole computations reproduce, are not one mechanism in two languages in either regime: they agree at leading order only at zero weight, and the half nat at the crossing is a quantity on which they differ. Small windows with nonzero weights, and mixed weights, are left open.

## lay
Two stories in the series explain how information comes back out of an evaporating black hole. One, the series' own, says the information sits in a small set of boundary modes that are pushed out in order; it gives an exact answer. The other uses the statistics of random quantum states, the same statistics that the recent "island" calculations reproduce. This result compares the small corrections the two stories predict. The series' story predicts either no correction at all, if its modes carry no energy, or, once enough modes are in play, a correction that keeps growing, if they carry energy. The random-state story predicts a correction that is always present but never larger than about half a unit at the turning point. So the two are different mechanisms, and the size of the correction at the turning point would tell them apart.

## one-liner
The eviction falling branch sits below capacity by zero (zero weight) or by an amount linear in the window (weights bounded away from zero), the Page-typical one by more than $(m-1)/2n$ and less than one nat; in both regimes they never coincide, and at zero weight they differ by about half a nat at the crossing.
