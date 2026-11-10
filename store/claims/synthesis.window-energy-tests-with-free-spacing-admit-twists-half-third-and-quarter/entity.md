---
id: synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter
kind: claim
version: 1
title: 'Window energy tests with free spacing also admit the half-arrays and an array at twist 1/3'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, boundary-modes, mode-counting, undetermined-input]
proposed_by:
  kind: ai
  session: 2026-11-10-phase2
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase2
review: draft
derivations:
- name: main
  uses:
  - synthesis.null-ordering-of-counted-units-is-zeta-symmetric@4
  - synthesis.half-integer-weight-array-carries-half-ln2@5
  - synthesis.imported-theta-function-identities@2
  - synthesis.q-splits-maximum-entropy-affine-weights@6
  - synthesis.univalence-from-even-stationary-dynamics@5
  - synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r@1
  - synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_ground_test_is_a_conic
- kind: check
  ref: check.py::check_thermal_test_holds_at_three_points
- kind: check
  ref: check.py::check_entropies_at_the_three_points
- kind: check
  ref: check.py::check_parity_clause_leaves_the_half_array_and_its_two_halves
- kind: check
  ref: check.py::check_odd_resonance_at_twist_one_third
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.window-reading-array-killing-energy
  - synthesis.null-ordering-of-counted-units-is-zeta-symmetric
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version kept at 1. The question left in the note, whether an assumes edge to (Q) is needed, is decided: none, the clauses of (Q) being hypotheses of clause (iv) and (Q) being in the cone through the null-ordering result.'
  open_problem: op.residue-killing-weights
  note: >-
    Attack item 4 of op.residue-killing-weights (which object's entropy the count compares with A/4), adversarial
    side: a test of whether the energy matching behind the adopted window reading fixes the array, and with it the
    entropy per window, once the array's spacing is not taken from (Q). Registered before computing: the objection
    "the window length and the boundary condition are put in by hand" would be dead if the two energy tests (the
    sea against the boost ground state, the thermal state against the null ground state) held only at spacing
    kappa and twist one half. It is not dead: further arrays pass both tests, of which only the one at twist one third is
    independent of the stored array (the twist one quarter arrays are its even and odd sublattices). The result does not contradict
    the stored uniqueness of the half offset, which is stated at spacing kappa; it says which clause of (Q) does the
    selecting. That (Q) makes two choices the framework does not make, the offset class and the slope y = 2 pi, is
    already stored (synthesis.q-splits-maximum-entropy-affine-weights (iv)); what is new here is only that the two
    energy equalities, which single out the offset at y = 2 pi, do not fix the slope. The window reading is not
    assumed at clause level (argued, not audited over the cone): the two tests are stated as equalities of numbers,
    as clauses (i) to (iii) of the null-ordering result are, but the cone through that result contains (Q), (N+),
    J3 and the window reading. (Q) is named for the wording of its parity and particle-hole
    clauses only, which enter clause (iv) as explicitly stated hypotheses; no assumes edge to (Q) is declared
    (maintainer decision of 10 November 2026): the clauses are hypotheses of clause (iv) and not premises of the
    result, and (Q) is in the cone already through the null-ordering result. The comparison at twist one half for every window length is cited from
    synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r (ii), and the product of the
    stored array into its two halves, with their values, from
    synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages (iii);
    neither is re-proved here. Exhaustiveness of the
    three points without the parity clause is computed (a floating scan along the conic), not proved, and is
    stated as a remark outside the theorem. Prior art, cited from memory and not premises: the fixed points of
    Fricke involutions of eta quotients (G. Koehler, Eta Products and Theta Series Identities, Springer 2011);
    characters of twisted free fermions (P. Ginsparg, Applied conformal field theory, Les Houches 1988).
    Transport-absent: classical modular identities placed on the stored arrays.
---

## formal
Units $\hbar = c = 1$; $\kappa$ a surface gravity, $\beta = 2\pi/\kappa$. For $r > 0$ and $0 < \delta < 1$ let the \emph{array of ratio $r$ and twist $\delta$} be the set of modes with weights $\omega_{k} = (\kappa/r)(k + \delta)$, $k \in \Z$: the spectrum of one chiral complex component on a Killing-time window of $r$ thermal periods with a twisted condition, the arrays of Premise \claimref{singularity.q-joint-quasi-freeness-s-wave} version 3 being $r = 1$, $\delta = \tfrac12$. Energies are in the zeta-regularised symmetric ordering of Theorem \claimref{synthesis.null-ordering-of-counted-units-is-zeta-symmetric}(ii), with $B_{2}(a) = a^{2} - a + \tfrac16$. Call the \emph{ground test} the equality of the array's sea energy $\tfrac{\kappa}{2r}B_{2}(\delta)$ with the null-ordered energy of the continuum's boost ground state over the window, $-\kappa r/24$ (the density $-\kappa^{2}/(48\pi)$ of clause (i) there times $2\pi r/\kappa$), and the \emph{thermal test} the vanishing of the array's mean energy in its Gibbs state at inverse temperature $\beta$, the null ground state's value on every window. Both tests are equalities of numbers; at clause level they assume no reading (argued: the cone of the cited theorem contains (Q), (N$_{+}$), J3 and the window reading). Then:
\begin{enumerate}
\item[(i)] \emph{(The ground test is a conic.)} $\tfrac{\kappa}{2r}B_{2}(\delta) + \tfrac{\kappa r}{24} = \tfrac{\kappa}{2r}\bigl[(\delta - \tfrac12)^{2} - \tfrac{1}{12}(1 - r^{2})\bigr]$. So the ground test holds exactly on $(\delta - \tfrac12)^{2} = (1 - r^{2})/12$: no window longer than one thermal period passes, at $r = 1$ only $\delta = \tfrac12$ does (the stored uniqueness), and every $r < 1$ has two mirror twists $\delta$, $1 - \delta$, the same array up to the relabelling $k \mapsto -1 - k$.
\item[(ii)] \emph{(Besides the stored array, its two halves and one independent array pass both tests.)} The thermal test holds on the conic at
\[
(r, \delta) = (1, \tfrac12), \qquad (\tfrac12, \tfrac14), \qquad (\sqrt{2/3}, \tfrac13),
\]
and at the mirror twists $\tfrac34$, $\tfrac23$. The second is one particle-hole half of the first (its even or odd sublattice; the stored array is the product of the two halves, Theorem \claimref{synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages}(iii)), not an independent array; the third is the only new one. The thermal excitation energies above the sea are $\kappa/24$, $\kappa/48$ and $\kappa\sqrt{6}/72$, each equal to minus the sea energy. The first is Theorem \claimref{synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r}(ii), by which at twist $\tfrac12$ the comparisons hold exactly when $r = 1$; the second follows from Theorem \claimref{synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages}(iii), the product of the stored array into its two halves with their values; the third is the fixed point of an involution of the array's partition function: with numbers in $\mathrm{span}\{1, I_{4}\}$ and the functions of Fact \claimref{synthesis.imported-theta-function-identities}, $\Phi_{1/3} = \eta(2\sigma)\eta(3\sigma)/(\eta(\sigma)\eta(6\sigma))$ at $\sigma = \tau/3$, $\tau = I_{4}/r$, invariant under $\sigma \mapsto -1/(6\sigma)$.
\item[(iii)] \emph{(Their entropies differ.)} At these points the entropy at the Hawking temperature is $\ln\Phi_{\delta}$: $\tfrac12\ln 2$ (Theorem \claimref{synthesis.half-integer-weight-array-carries-half-ln2}), $\tfrac14\ln 2$ (Theorem \claimref{synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages}(iii)), and a value in $(0.29379, 0.29380)$. Per thermal period of Killing time these are $\tfrac12\ln 2 < 0.3466$, again $\tfrac12\ln 2$, and a value in $(0.3598, 0.3599)$; the continuum's entropy rate times one thermal period, $\pi/6 > 0.5235$, is none of them. At twist $\tfrac13$ the number of arrays carrying $\ln 2$ lies in $(2.35, 2.36)$.
\item[(iv)] \emph{(What the clauses of (Q) select.)} Under the parity clause of (Q) version 3 alone (the Killing flow at one modular period is $\psi \mapsto -\psi$: every $\beta\omega_{k}$ an odd multiple of $\pi$), $r = 1/m$ and $\delta = (j + \tfrac12)/m$ with integers $m \ge 1$, $0 \le j < m$; the ground test is then the Pell equation $m^{2} - 3p^{2} = 1$ with $p = 2j + 1 - m$ ($m = 1, 2, 7, 26, 97, \dots$), and the thermal test fails for every $m \ge 7$. So exactly the stored array and its two halves, weights $2\kappa(k + \tfrac14)$ and $2\kappa(k + \tfrac34)$, pass both tests with the parity clause; at twist $\tfrac13$ the flow at one modular period is not a constant phase at all ($1/r$ is not an integer), so the parity clause fails. Under the particle-hole clause of (Q) (one array's weights symmetric under $k \mapsto -1 - k$, so $\delta = \tfrac12$), or with the spacing $\kappa$ taken from (Q), only $(1, \tfrac12)$ remains.
\end{enumerate}
So the two energy equalities that single out the half offset at the slope $\beta c = 2\pi$ (spacing $c = \kappa$) do not fix the slope: they admit $\beta c = 2\pi$, $4\pi$ and $2\pi\sqrt{3/2}$. That the slope is a choice of (Q) which the framework does not make is stored (Theorem \claimref{synthesis.q-splits-maximum-entropy-affine-weights}(iv)); the statement here is only that the energy equalities do not make it either. The entropy per unit Killing time differs among the passing arrays only through the single point $(\sqrt{2/3}, \tfrac13)$, $0.3598$ against $0.3466$ per thermal period, an array that fails the parity clause of (Q) and for which evenness of stationary states is no longer automatic (Remark 2).

\emph{Remark 1 (computed, not part of the theorem).} A floating-point scan along the conic at step $0.005$ in $r$ finds no further zero of the thermal test; that there is no fourth point without the parity clause is computed, not proved.

\emph{Remark 2 (evenness of stationary states).} By clause 3 of Theorem \claimref{synthesis.univalence-from-even-stationary-dynamics}, for finitely many modes every stationary state is even if and only if no signed sum of an odd number of weights vanishes. At twists $\tfrac12$ and $\tfrac14$ all weights are odd multiples of one number and the criterion holds. At twist $\tfrac13$ the weights $k + \tfrac13$ have the odd resonance $\tfrac13 + \tfrac43 - \tfrac53 = 0$ ($k = 0, 1, -2$), so the criterion fails: stationary states that are not even exist. This does not exclude the array, whose Gibbs state is even by clause 2 of the same theorem; it says that at this twist univalence is not a consequence of stationarity.

## technical
The stored null-ordering result compares an array with a light ray's continuum over the array's recurrence window in two ways: the array's filled sea against the continuum's boost ground state, and the array's thermal state against the null ground state. At the spacing $\kappa$ of Premise (Q) version 3 both agree only at the half offset. Here the spacing is left free, assuming nothing beyond those two equalities: an array of spacing $\kappa/r$ is compared with the continuum over its own window of $r$ thermal periods. The first comparison holds on a conic, $(\delta - \tfrac12)^{2} = (1 - r^{2})/12$, and the second picks out three points on it: the stored array; an array of twice the spacing at twist one quarter, which is half of the stored array (the odd multiples of $\pi$ split into $1, 5, 9, \dots$ and $3, 7, 11, \dots$); and an array of spacing $\kappa\sqrt{3/2}$ at twist one third, the fixed point of the level-six involution of an eta quotient. Only the last is independent of the stored array. The entropies per unit Killing time are $0.3466$, $0.3466$ and $0.3598$ per thermal period, differing only at the twist one third point, and none is the continuum's $\pi/6$. Given the parity clause of (Q) the twist one third drops out and the half-arrays remain; given the particle-hole clause or the spacing itself only the stored array remains. At twist one third the flow at one modular period is not a constant phase, and three of its weights sum to zero with signs, so stationary states need not be even there (the Gibbs state still is). So, assuming only the two energy comparisons, the slope is not fixed: that the slope is a choice of (Q) is already stored, and what is added is that the energy equalities do not make that choice. Whether further points exist without the parity clause is examined by a numerical scan only, not proved.

## lay
The series counts a black hole's entropy with evenly spaced sets of modes on the horizon's light rays, and an earlier result showed that, given the spacing the series assumes, only one such set has the same average energy as the light ray itself in two different states. This result asks what happens if the spacing is not assumed. Under those two energy comparisons alone, at least three sets qualify, not one (a numerical scan finds no more, which is not a proof): the stored set, a set made of every second mode of it, and a third with an irrational spacing. The second is only half of the stored set, not a new one; the third is the only new one, and it alone carries a different entropy for the same stretch of time on the horizon. None carries the entropy rate of the light ray itself. Given the series' other conditions on the modes, the stored set is the only one left. So, given only the energy comparison, the spacing is not decided; that the spacing is an assumption of the series was already recorded, and this result adds that the energy comparison does not remove it.

## one-liner
With the spacing left free, an array of spacing $\kappa/r$ and twist $\delta$ meets the continuum's window energies in both the boost and the null ground state at $(r, \delta) = (1, \tfrac12)$, $(\tfrac12, \tfrac14)$ and $(\sqrt{2/3}, \tfrac13)$ (fixed points of involutions of eta quotients), with entropies $\tfrac12\ln 2$, $\tfrac14\ln 2$ and about $0.2938$ at the Hawking temperature; the second is one particle-hole half of the first, not an independent array, and the third is the only new one; no fourth point is found by a numerical scan (computed, not proved); given the parity clause of (Q) the first two remain, and given its particle-hole clause or its spacing only the first, so the two energy equalities do not fix the slope.
