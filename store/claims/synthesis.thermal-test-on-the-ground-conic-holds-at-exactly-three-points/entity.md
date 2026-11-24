---
id: synthesis.thermal-test-on-the-ground-conic-holds-at-exactly-three-points
kind: claim
version: 1
title: 'Thermal test on the ground conic: three points up to the mirror twist, no fourth array'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, boundary-modes, mode-counting, no-go]
proposed_by:
  kind: ai
  session: 2026-11-24-number-theory
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-24-number-theory
review: draft
outside_ga:
  kind: other
  why: "A statement of real analysis about scalar functions (grade 0): the zeros of one function of one real variable, settled by enclosures in integer arithmetic. No element of higher grade enters."
derivations:
- name: main
  uses:
  - synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter@1
  - synthesis.null-ordering-of-counted-units-is-zeta-symmetric@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_enclosures_contain_zero_at_the_three_stored_points_and_exclude_it_at_controls
- kind: check
  ref: check.py::check_no_zero_for_windows_shorter_than_three_twentieths_of_a_period
- kind: check
  ref: check.py::check_sign_of_the_thermal_test_on_the_three_open_stretches
- kind: check
  ref: check.py::check_monotone_near_one_quarter_and_one_third_and_concave_near_one_half
lineage:
  motivated_by:
  - singularity.q-joint-quasi-freeness-s-wave
  - synthesis.window-reading-array-killing-energy
extraction:
  open_problem: op.residue-killing-weights
  note: >-
    Remark 1 of synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter records that
    a floating-point scan finds no further zero of the thermal test on the conic and that the absence of a fourth
    point is "computed, not proved". This result proves it. A test fixed before computing: whether
    certified rational enclosures fail to isolate the zeros (a fourth zero, or an interval that cannot be
    decided at feasible cost). They do not fail: 73 intervals decide the three stretches, and the derivative
    enclosures hold on 16, 20 and 40 pieces near the three points. What is machine-verified: every sign in
    the proof's steps 3 to 5, by enclosures computed in integer arithmetic with outward rounding at 128 binary
    digits (interval values, first and second derivatives by the rules of differentiation applied to
    intervals, the exponential by its series with a remainder bound, pi by Machin's formula). What is argued on
    paper: the bound for short windows (step 1, whose arithmetic the check verifies), the bound on the omitted
    terms (step 2), and the passage from the signs to the count of zeros (step 6). That the three points are
    zeros is the stored theorem (through the imported theta identities at twist one third); the enclosures
    here contain zero at all three, which is consistent with it and does not prove it. A further test
    concerned whether invariance under the whole modular group of the window says more than the stored
    one-window and two-window recurrences; it does not (the generators are the stored $r \mapsto 1/r$ at the Hawking
    point and the one-window flow, so nothing new follows) and nothing is filed on it. Consequence for the
    open problem: none for the count unit. The energy equalities admit exactly the three stored slopes and no
    other, which is what the stored theorem said with "computed". Ledger: transport-absent.
---

## formal
Notation and units as in \claimref{synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter}: for $r > 0$ and $0 < \delta < 1$ the array of ratio $r$ and twist $\delta$ has weights $(\kappa/r)(k + \delta)$, $k \in \Z$; the \emph{ground test} is the equality of its zeta-regularised sea energy $\tfrac{\kappa}{2r}B_{2}(\delta)$ (\claimref{synthesis.null-ordering-of-counted-units-is-zeta-symmetric}(ii)) with $-\kappa r/24$, which holds exactly on the conic $(\delta - \tfrac12)^{2} = (1 - r^{2})/12$, $0 < r \le 1$; the \emph{thermal test} is the vanishing of the array's mean energy in its Gibbs state at $\beta = 2\pi/\kappa$. On the conic the sea energy is $-\kappa r/24$, so in units of $\kappa/r$ the thermal test is the vanishing of
\[
T(\delta) = -\frac{r^{2}}{24} + \sum_{k \ge 0}\Bigl[\frac{k + \delta}{e^{2\pi(k + \delta)/r} + 1} + \frac{k + 1 - \delta}{e^{2\pi(k + 1 - \delta)/r} + 1}\Bigr], \qquad r^{2} = 1 - 12\bigl(\delta - \tfrac12\bigr)^{2},
\]
a function on $\tfrac12 - \tfrac{1}{\sqrt{12}} < \delta < \tfrac12 + \tfrac{1}{\sqrt{12}}$ that is symmetric under $\delta \mapsto 1 - \delta$.

\emph{Theorem (proved, with the signs of the enclosures carried by the check).} On $\tfrac12 - \tfrac{1}{\sqrt{12}} < \delta \le \tfrac12$ the function $T$ vanishes exactly at $\delta = \tfrac14$, $\tfrac13$ and $\tfrac12$, with
\[
T < 0 \text{ on } \bigl(\tfrac12 - \tfrac{1}{\sqrt{12}}, \tfrac14\bigr), \qquad T > 0 \text{ on } \bigl(\tfrac14, \tfrac13\bigr), \qquad T < 0 \text{ on } \bigl(\tfrac13, \tfrac12\bigr),
\]
simple zeros at $\tfrac14$ and $\tfrac13$ and a double zero at $\tfrac12$. So the points of the $(r, \delta)$ half-plane at which an array passes both the ground test and the thermal test are exactly
\[
(1, \tfrac12), \qquad (\tfrac12, \tfrac14), \quad (\tfrac12, \tfrac34), \qquad (\sqrt{2/3}, \tfrac13), \quad (\sqrt{2/3}, \tfrac23),
\]
the three points of clause (ii) of the cited theorem and their mirror twists. There is no fourth point, with or without the parity clause of Premise (Q): Remark 1 of the cited theorem, stored as computed, is a theorem. That $T$ vanishes at the three twists is the cited clause (ii); what is proved here is that it vanishes nowhere else.

## technical
The stored theorem found three arrays whose sea energy matches the continuum's boost ground state over the window and whose thermal mean energy vanishes: the array of Premise (Q), its particle-hole half, and one more at twist one third. It recorded, from a floating-point scan, that there seemed to be no fourth. This result proves there is none. The ground test confines the pair of ratio and twist to a conic, on which the thermal test is the vanishing of one function $T$ of the twist. For windows shorter than three twentieths of a thermal period the thermal sum is too small to cancel the sea energy, by an explicit exponential bound. On the rest of the conic, $T$ and its first two derivatives are enclosed by interval arithmetic in integers with outward rounding: $T$ is negative from the short-window cut to just below one quarter, increasing through one quarter, positive up to just below one third, decreasing through one third, negative up to $0.46$, and concave from there to one half, where $T$ and its derivative vanish by the stored theorem and by the mirror symmetry of the twist. So the zeros are the three stored ones. The size of $T$ between the zeros is small, of order $10^{-4}$ to $10^{-3}$, which is why the scan could not settle it and why enclosures with a derivative term are used. Nothing changes for the open problem on the count unit: the two energy equalities still admit three slopes, and now provably only three.

## lay
An earlier result found three special arrangements of the horizon's modes whose energies balance in two different senses at once, and a computer scan suggested there were no others. A scan cannot prove that: it looks at finitely many points and uses rounded numbers. This result closes the gap with arithmetic that never rounds in the wrong direction. Every quantity is trapped between two exact fractions, and the trap is tight enough to show that the balance fails everywhere except at the three known arrangements.

## one-liner
On the ground conic $(\delta - \tfrac12)^{2} = (1 - r^{2})/12$ the thermal test $T(\delta) = 0$ holds only at $\delta = \tfrac14, \tfrac13, \tfrac12$ (and the mirror twists): for $r \le \tfrac{3}{20}$ the thermal sum is below $r^{2}/24$ by an exponential bound, and beyond it integer-arithmetic enclosures give $T < 0$, $T' > 0$ near $\tfrac14$, $T > 0$, $T' < 0$ near $\tfrac13$, $T < 0$, and $T'' < 0$ up to $\tfrac12$; so the arrays passing both energy tests are exactly the three stored ones, and "no fourth point" is proved, not only computed.
