---
id: synthesis.eviction-deficit-against-page-deficit
kind: claim
version: 5
title: 'The eviction deficit against the Page deficit'
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
- name: Claude Opus 5.5
  role: 'GA rewrite (the complex field named by its unit)'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Fable 5.2
  role: 'clause (i) restated on a parity sector (the sector deficit and its bounds first, the abstract tensor-product value kept beside it; the lower bound (m-1)/(2n) fails on a sector at m = 2), with its proof and a check'
  version: 5
  source: maintainer pass of 2026-11-10
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
- kind: check
  ref: check.py::check_sector_deficit_bounds
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - note.singularity.island-dictionary-one-dissonance
  - singularity.assembled-page-curve-up-typicality
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 4 -> 5, by decision 13 of 9 November 2026 (the random-state column of the eviction comparisons is the parity sector, with the abstract tensor-product value kept beside it): clause (i) is restated with the sector deficit first, its bounds being those of clause (vii) of synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product, and says that the lower bound (m-1)/(2n) of version 4 holds on a sector for m >= 4 and fails at m = 2; the abstract value and its bounds are kept unchanged beside it. Clauses (ii) and (iii) are unchanged. The proof of (i) derives the sector value from Page''s Fact, so that the result has no premise that cites it; one check function is added.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. The complex-field stand-in \C is tied to its unit, span{1, I_4} (U1, an abstract Hilbert space), by one parenthetical at its first use (readers R02 and R08: the language check does not flag the macro). Notation only; the mathematics is unchanged.'
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
    The sector column (10 November 2026). The states the comparison is about are even pure states of the modes,
    which lie in one parity sector of the mode algebra and not in an abstract tensor product
    (synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product, clause (iv)); the
    random-state value on a sector is clause (vii) of that result. It is not listed as a premise here, because
    that result cites this one for its table of stored comparisons; the proof of clause (i) therefore rederives
    the sector mean entropy from Page's imported average and two standard properties of the invariant measure
    (the block weight of a normalised Gaussian vector follows a Beta law and is independent of the normalised
    blocks), which are background and are not stored. The sector formula is the two-block case of a published
    formula for random states on a direct sum of tensor products, as that result's note records. The sector
    column is stated for dimensions that are powers of two, the dimensions of mode algebras.
---

## formal
Let $L$ be the window, with $|W(t)|$ members and capacity $C = |W(t)|\ln 2$, and $R$ the radiation, under the hypotheses of Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy}, whose clause (4) gives the eviction deficit
\[
\delta_{\mathrm{ev}}(t) \;:=\; C(t) - S_{R}(t) \;=\; \sum_{k \in W(t)}\bigl(\ln 2 - h_{k}\bigr) ,
\]
with $h_{k} = s(x_{k})$ the mode entropy at $x_{k} = 2\pi\omega_{k}/\kappa$ (Theorem \claimref{synthesis.boundary-mode-thermal-entropy}). For a pure state on $\C^{m} \otimes \C^{n}$ (an abstract Hilbert space, its numbers read in $\mathrm{span}\{1, I_4\}$, conventions, the unit principle), $m \le n$, drawn from the unitarily invariant measure, let $\delta_{\mathrm{P}}(m, n) := \ln m - \langle S_{A}\rangle$ be the Page deficit, with $\langle S_{A}\rangle$ as in Fact \claimref{singularity.imported-page-average-entropy-subsystem}; the Page-typical falling branch of Fact \claimref{singularity.assembled-page-curve-up-typicality} has $\dim L = m$ after the crossing. The states compared are even pure states of the modes (fixed by the total-parity average), and these lie in one parity sector of the mode algebra, not in an abstract tensor product (Theorem \claimref{synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product}(iv)). For $m = 2^{a} \le n = 2^{b}$, $a \ge 1$, a \emph{parity sector} is the subspace $(\C^{m/2}\otimes\C^{n/2}) \oplus (\C^{m/2}\otimes\C^{n/2})$ of $\C^{m}\otimes\C^{n}$ on which the parities of the two sides agree (or the one on which they differ), of dimension $mn/2$; let $\langle S_{A}\rangle_{\mathrm{sector}}$ be the mean entropy of the $m$-dimensional side for a unit vector drawn from the unitarily invariant measure of the sector, and $\delta_{\mathrm{sec}}(m, n) := \ln m - \langle S_{A}\rangle_{\mathrm{sector}}$ the sector deficit. Then:
\begin{enumerate}
\item[(i)] (the typical deficit; the sector value first, the abstract tensor-product value beside it) On a parity sector, for $m = 2^{a} \le n = 2^{b}$,
\[
\langle S_{A}\rangle_{\mathrm{sector}} = \sum_{k = n/2 + 1}^{mn/2}\frac1k - \frac{m - 2}{2n}, \qquad
\frac{m-2}{2n} + \frac{2(m-1)}{2mn + m + 1} \;<\; \delta_{\mathrm{sec}}(m,n) \;<\; \frac{m}{2n} - \frac{1}{mn} \;<\; \frac12
\]
(the formula and the bounds are those of clause (vii) of Theorem \claimref{synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product}). For the abstract tensor product, for all $2 \le m \le n$,
\[
\frac{m - 1}{2n} \;<\; \delta_{\mathrm{P}}(m, n) \;<\; \frac{m - 1}{2n} + \frac{m - 1}{mn + 1} \;<\; 1 ,
\]
and $\delta_{\mathrm{sec}} = \delta_{\mathrm{P}} - \Delta$ with $\Delta(m, n)$ rational, $\tfrac{1}{2mn} < \Delta < \tfrac{1}{2(mn+1)} + \tfrac{1}{2n(n+1)}$. The lower bound $(m-1)/(2n)$ of the abstract column holds on a sector for $m \ge 4$ and fails there at $m = 2$, where $\delta_{\mathrm{sec}}(2, n) < \tfrac{1}{2n}$ (at $m = n = 2$: $\ln 2 - \tfrac12$ on the sector against $\ln 2 - \tfrac13$). In both columns the Page-typical falling branch lies strictly below capacity at every stage, by about $\tfrac12$ nat at the crossing $m = n$, and for fixed $m$ the bounds are of order $1/n$, so the deficit falls by about half with each further radiated qubit;
\item[(ii)] (zero weight) if every window member has zero weight, $\delta_{\mathrm{ev}} = 0$ at every stage: the eviction falling branch is the capacity exactly, and differs from the Page-typical one by $\delta_{\mathrm{P}} > 0$ at every stage, most at the crossing;
\item[(iii)] (weights bounded away from zero) if every window member has $|x_{k}| \ge x_{*} > 0$, then $\delta_{\mathrm{ev}} \ge \tfrac12|W(t)|\tanh^{2}(x_{*}/2)$, linear in the window size; for (Q)'s weights $x_{k} = 2\pi|k|$ every member with $k \neq 0$ contributes more than $\tfrac12$ nat, so two such members already put $\delta_{\mathrm{ev}}$ above every Page deficit.
\end{enumerate}
Hence for neither uniform zero weight nor weights bounded away from zero does the eviction falling branch coincide with the Page-typical one at any stage with $\dim L \ge 2$ (respectively, once $|W(t)| > 2/\tanh^{2}(x_{*}/2)$, and for (Q)'s weights once two members of nonzero weight are in the window): in these two regimes the two are distinct mechanisms below leading order. Small windows with nonzero weights, and mixed or small weights, are not covered: there $\delta_{\mathrm{ev}}$ can take intermediate values. At the registered calibration (zero weight) the eviction branch is the sharp $\min(\Sth, C)$ with no rounding, and the quantity separating it from the typical branch is the deficit at the crossing, $0$ against $\delta_{\mathrm{sec}}(m, m) \in (\tfrac25, \tfrac12)$ on a parity sector, and against $\delta_{\mathrm{P}}(m, m) \in (\tfrac25, \tfrac12 + \tfrac1m)$ for the abstract tensor product, for $m \ge 4$. Clauses (ii) and (iii) and this paragraph hold with $\delta_{\mathrm{sec}}$ in place of $\delta_{\mathrm{P}}$, since $0 < \delta_{\mathrm{sec}} < \tfrac12$.

## technical
The store holds two accounts of the falling branch of the Page curve. The eviction theorem gives it exactly, with no typicality: the radiation entropy equals the capacity minus the sum of the window members' shortfalls from $\ln 2$. The typicality Fact assembles it from Page's theorem, which says a random pure state sits a definite amount below the maximum: for an abstract tensor product more than $(m-1)/2n$ and less than one nat, about one half at the crossing and halving with each further qubit radiated. The states in question are even states of fermionic modes, which lie in one parity sector and not in a tensor product; the random state is therefore drawn from a sector, and that is the primary column. There the deficit is smaller by a rational amount between $1/(2mn)$ and $1/(2mn) + 1/(2n^{2})$: it lies between $(m-2)/(2n)$ and $m/(2n)$, stays below half a nat, is between $\tfrac25$ and $\tfrac12$ at the crossing from $m = 4$ on, and at $m = 2$ falls below the abstract column's lower bound $(m-1)/(2n)$. The two deficits behave differently in the two regimes treated here. With all weights zero the eviction deficit vanishes identically, so the eviction curve is the sharp minimum of the thermal and capacity curves; the typical curve is rounded at the crossing by about half a nat. With weights bounded away from zero the eviction deficit grows in proportion to the window, by Pinsker's inequality, while the typical deficit stays below one nat. So the eviction mechanism and the typicality mechanism, the latter being the falling branch that replica-wormhole computations reproduce, are not one mechanism in two languages in either regime: they agree at leading order only at zero weight, and the half nat at the crossing is a quantity on which they differ. Small windows with nonzero weights, and mixed weights, are left open.

## lay
Two stories in the series explain how information comes back out of an evaporating black hole. One, the series' own, says the information sits in a small set of boundary modes that are pushed out in order; it gives an exact answer. The other uses the statistics of random quantum states, the same statistics that the recent "island" calculations reproduce. This result compares the small corrections the two stories predict. The series' story predicts either no correction at all, if its modes carry no energy, or, once enough modes are in play, a correction that keeps growing, if they carry energy. The random-state story predicts a correction that is always present but never larger than about half a unit at the turning point; this holds whether the random state is drawn with the restriction that the particles' parity imposes, which is the version that applies here, or without it, and the two versions differ only in small terms. So the two are different mechanisms, and the size of the correction at the turning point would tell them apart.

## one-liner
The eviction falling branch sits below capacity by zero (zero weight) or by an amount linear in the window (weights bounded away from zero), the Page-typical one, on a parity sector, by more than $(m-2)/2n$ and less than half a nat (for an abstract tensor product by more than $(m-1)/2n$ and less than one nat, a lower bound that fails on a sector at $m = 2$); in both regimes they never coincide, and at zero weight they differ by about half a nat at the crossing.
