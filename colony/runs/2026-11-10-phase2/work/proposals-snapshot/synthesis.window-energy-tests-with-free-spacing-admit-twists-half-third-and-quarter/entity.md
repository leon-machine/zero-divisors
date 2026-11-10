---
id: synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter
kind: claim
version: 1
title: 'Window energy tests with free spacing admit twists one half, one third and one quarter'
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
  - synthesis.counted-unit-energy-at-half-offset@3
  - synthesis.half-integer-weight-array-carries-half-ln2@5
  - synthesis.imported-theta-function-identities@2
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
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.window-reading-array-killing-energy
  - synthesis.null-ordering-of-counted-units-is-zeta-symmetric
extraction:
  open_problem: op.residue-killing-weights
  note: >-
    Attack item 4 of op.residue-killing-weights (which object's entropy the count compares with A/4), adversarial
    side: a test of whether the energy matching behind the adopted window reading fixes the array, and with it the
    entropy per window, once the array's spacing is not taken from (Q). Registered before computing: the objection
    "the window length and the boundary condition are put in by hand" would be dead if the two energy tests (the
    sea against the boost ground state, the thermal state against the null ground state) held only at spacing
    kappa and twist one half. It is not dead: two further arrays pass both tests. The result does not contradict
    the stored uniqueness of the half offset, which is stated at spacing kappa; it says which clause of (Q) does the
    selecting. The window reading is not assumed: the two tests are stated as equalities of numbers, as clauses
    (i) to (iii) of the null-ordering result are. (Q) is named for the wording of its parity and particle-hole
    clauses only, which enter clause (iv) as explicitly stated hypotheses; no edge to (Q) is declared, and whether
    an assumes edge should be added is a maintainer decision. Intended citation for the comparison at twist one half as a function of the window
    length (closed forms on the square torus, the entropy difference from the continuum at each window length):
    the base statement filed in the same run by the constructive side, not re-proved here. Exhaustiveness of the
    three points without the parity clause is computed (a floating scan along the conic), not proved, and is
    stated as a remark outside the theorem. Prior art, cited from memory and not premises: the fixed points of
    Fricke involutions of eta quotients (G. Koehler, Eta Products and Theta Series Identities, Springer 2011);
    characters of twisted free fermions (P. Ginsparg, Applied conformal field theory, Les Houches 1988).
    Transport-absent: classical modular identities placed on the stored arrays.
---

## formal
Units $\hbar = c = 1$; $\kappa$ a surface gravity, $\beta = 2\pi/\kappa$. For $r > 0$ and $0 < \delta < 1$ let the \emph{array of ratio $r$ and twist $\delta$} be the set of modes with weights $\omega_{k} = (\kappa/r)(k + \delta)$, $k \in \Z$: the spectrum of one chiral complex component on a Killing-time window of $r$ thermal periods with a twisted condition, the arrays of Premise \claimref{singularity.q-joint-quasi-freeness-s-wave} version 3 being $r = 1$, $\delta = \tfrac12$. Energies are in the zeta-regularised symmetric ordering of Theorem \claimref{synthesis.null-ordering-of-counted-units-is-zeta-symmetric}(ii), with $B_{2}(a) = a^{2} - a + \tfrac16$. Call the \emph{ground test} the equality of the array's sea energy $\tfrac{\kappa}{2r}B_{2}(\delta)$ with the null-ordered energy of the continuum's boost ground state over the window, $-\kappa r/24$ (the density $-\kappa^{2}/(48\pi)$ of clause (i) there times $2\pi r/\kappa$), and the \emph{thermal test} the vanishing of the array's mean energy in its Gibbs state at inverse temperature $\beta$, the null ground state's value on every window. Both tests are equalities of numbers and assume no reading. Then:
\begin{enumerate}
\item[(i)] \emph{(The ground test is a conic.)} $\tfrac{\kappa}{2r}B_{2}(\delta) + \tfrac{\kappa r}{24} = \tfrac{\kappa}{2r}\bigl[(\delta - \tfrac12)^{2} - \tfrac{1}{12}(1 - r^{2})\bigr]$. So the ground test holds exactly on $(\delta - \tfrac12)^{2} = (1 - r^{2})/12$: no window longer than one thermal period passes, at $r = 1$ only $\delta = \tfrac12$ does (the stored uniqueness), and every $r < 1$ has two mirror twists $\delta$, $1 - \delta$, the same array up to the relabelling $k \mapsto -1 - k$.
\item[(ii)] \emph{(Three arrays pass both tests.)} The thermal test holds on the conic at
\[
(r, \delta) = (1, \tfrac12), \qquad (\tfrac12, \tfrac14), \qquad (\sqrt{2/3}, \tfrac13),
\]
and at the mirror twists $\tfrac34$, $\tfrac23$. The thermal excitation energies above the sea are $\kappa/24$, $\kappa/48$ and $\kappa\sqrt{6}/72$, each equal to minus the sea energy. Each is the fixed point of an involution of the array's partition function $\Phi_{\delta}$: with numbers in $\mathrm{span}\{1, I_{4}\}$ and the functions of Fact \claimref{synthesis.imported-theta-function-identities}, $\Phi_{1/2} = \vartheta_{3}/\eta$ at $\tau = I_{4}/r$ under $\tau \mapsto -1/\tau$; $\Phi_{1/4}(\tau) = (\vartheta_{3}/\eta)^{1/2}(\tau/2)$; and $\Phi_{1/3} = \eta(2\sigma)\eta(3\sigma)/(\eta(\sigma)\eta(6\sigma))$ at $\sigma = \tau/3$, invariant under $\sigma \mapsto -1/(6\sigma)$.
\item[(iii)] \emph{(Their entropies differ.)} At these points the entropy at the Hawking temperature is $\ln\Phi_{\delta}$: $\tfrac12\ln 2$ (Theorem \claimref{synthesis.half-integer-weight-array-carries-half-ln2}), $\tfrac14\ln 2$, and a value in $(0.29379, 0.29380)$. Per thermal period of Killing time these are $\tfrac12\ln 2 < 0.3466$, again $\tfrac12\ln 2$, and a value in $(0.3598, 0.3599)$; the continuum's entropy rate times one thermal period, $\pi/6 > 0.5235$, is none of them. At twist $\tfrac13$ the number of arrays carrying $\ln 2$ lies in $(2.35, 2.36)$.
\item[(iv)] \emph{(What the clauses of (Q) select.)} Under the parity clause of (Q) version 3 alone (the Killing flow at one modular period is $\psi \mapsto -\psi$: every $\beta\omega_{k}$ an odd multiple of $\pi$), $r = 1/m$ and $\delta = (j + \tfrac12)/m$ with integers $m \ge 1$, $0 \le j < m$; the ground test is then the Pell equation $m^{2} - 3p^{2} = 1$ with $p = 2j + 1 - m$ ($m = 1, 2, 7, 26, 97, \dots$), and the thermal test fails for every $m \ge 7$. So exactly the stored array and its two halves, weights $2\kappa(k + \tfrac14)$ and $2\kappa(k + \tfrac34)$, pass both tests with the parity clause; the twist $\tfrac13$ fails the parity clause. Under the particle-hole clause of (Q) (one array's weights symmetric under $k \mapsto -1 - k$, so $\delta = \tfrac12$), or with the spacing $\kappa$ taken from (Q), only $(1, \tfrac12)$ remains.
\end{enumerate}
So the two energy equalities that single out the half offset at spacing $\kappa$ do not fix the array when the spacing is left free: the spacing, equivalently the window length, is an input taken from (Q), and the entropy per window, even the entropy per unit Killing time, depends on it. \emph{Remark (computed, not part of the theorem).} A floating-point scan along the conic at step $0.005$ in $r$ finds no further zero of the thermal test; exhaustiveness without the parity clause is not proved.

## technical
The stored null-ordering result compares an array with a light ray's continuum over the array's recurrence window in two ways: the array's filled sea against the continuum's boost ground state, and the array's thermal state against the null ground state. At the spacing $\kappa$ of Premise (Q) version 3 both agree only at the half offset. Here the spacing is left free, assuming nothing beyond those two equalities: an array of spacing $\kappa/r$ is compared with the continuum over its own window of $r$ thermal periods. The first comparison holds on a conic, $(\delta - \tfrac12)^{2} = (1 - r^{2})/12$, and the second picks out three points on it: the stored array; an array of twice the spacing at twist one quarter, which is half of the stored array (the odd multiples of $\pi$ split into $1, 5, 9, \dots$ and $3, 7, 11, \dots$); and an array of spacing $\kappa\sqrt{3/2}$ at twist one third, the fixed point of the level-six involution of an eta quotient. Their entropies per unit Killing time are not all equal, $0.3466$, $0.3466$ and $0.3598$ per thermal period, and none is the continuum's $\pi/6$. Given the parity clause of (Q) the twist one third drops out and the half-arrays remain; given the particle-hole clause or the spacing itself only the stored array remains. So under the energy comparisons alone the array, and the entropy the count uses, is not determined: the selecting input is the spacing of (Q). Whether further points exist without the parity clause is settled by a numerical scan only.

## lay
The series counts a black hole's entropy with evenly spaced sets of modes on the horizon's light rays, and an earlier result showed that, given the spacing the series assumes, only one such set has the same average energy as the light ray itself in two different states. This result asks what happens if the spacing is not assumed. Under those two energy comparisons alone, three sets qualify, not one: the stored set, a set made of every second mode of it, and a third with an irrational spacing. They do not all carry the same entropy for the same stretch of time on the horizon, and none carries the entropy rate of the light ray itself. Given the series' other conditions on the modes, the stored set is the only one left. So the energy comparison does not by itself decide which entropy is counted; the assumed spacing does.

## one-liner
With the spacing left free, an array of spacing $\kappa/r$ and twist $\delta$ meets the continuum's window energies in both the boost and the null ground state at $(r, \delta) = (1, \tfrac12)$, $(\tfrac12, \tfrac14)$ and $(\sqrt{2/3}, \tfrac13)$ (fixed points of involutions of eta quotients), with entropies $\tfrac12\ln 2$, $\tfrac14\ln 2$ and about $0.2938$ at the Hawking temperature; given the parity clause of (Q) the first two remain, and given its particle-hole clause or its spacing only the first.
