---
id: synthesis.null-ordering-of-counted-units-is-zeta-symmetric
kind: claim
version: 4
title: 'The null ordering of counted units is zeta-symmetric'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, boundary-modes, mode-counting, hawking-temperature, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: unit pass, every imaginary unit resolved to the geometric-algebra unit it stands for
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: consistency pass, a garbled sentence of the technical level repaired and the cited edge-scaling result named as the Theorem it is
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: draft
about:
- obj.hawking.continuum-mode-space
derivations:
- name: main
  uses:
  - synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit@4
  - synthesis.collapse-in-vacuum-regular-at-future-horizon-selects-hawking-temperature@2
  - synthesis.counted-unit-energy-at-half-offset@2
  - synthesis.imported-theta-function-identities@2
  - synthesis.hole-mass-is-ground-energy-label@3
  - synthesis.residue-from-mode-entropy@4
  - synthesis.positive-null-energy-gives-r-premises@7
  assumes:
  - synthesis.window-reading-array-killing-energy@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_window_energy_of_the_boost_ground_state
- kind: check
  ref: check.py::check_zeta_sea_selects_the_half_offset
- kind: check
  ref: check.py::check_thermal_state_carries_zero_in_the_null_ordering
- kind: check
  ref: check.py::check_counted_unit_carries_no_mean_killing_energy
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.counted-unit-energy-at-half-offset
  - synthesis.n-plus-null-ground-state
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4: A garbled sentence of the technical level repaired and the cited edge-scaling result named as the Theorem it is; mathematics, links, pins, status and checks unchanged.'
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3. The one bare i, the twist phase of the window condition psi(tau + L) = e^{2 pi I_4 delta} psi(tau) in the proof, is the unit of a chiral component of the horizon continuum on a Killing-time window, so it is the field unit I_4 (U1; the continuum mode space carries I_4, as in synthesis.positive-null-energy-gives-r-premises). No i remains; declaration removed. Mathematics, links and checks unchanged.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced, by Leon''s ruling R1 (7 November 2026): the twist phase e^{2 pi i delta} of the chiral component on one window keeps i, since the boundary modes descend from T05''s atom, whose mode operators anticommute with I_4 (conventions, known limits 1 and 2). Declared (version and levels unchanged).'
  open_problem: op.counted-mode-energy
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Leon adopted the window reading on 2026-10-31; it is registered as synthesis.window-reading-array-killing-energy and this result now assumes it (assumes edge added), with clause (iv) citing it by claimref. Clauses (i) to (iii) are unconditional as before; statement unchanged. Version 1 -> 2.'
  note: >-
    The problem's second line of attack: decide the physical ordering of the sea's energy (sea-normal or
    zeta-regularised symmetric) from a premise of the series. The premise is (N+), whose state is the ground
    state of the affine null translations; the stored edge-scaling result already gives the Killing-frame
    density of the boost ground state in the ordering where that state has zero null energy,
    -kappa^2/(48 pi) per component, and the stored collapse result gives the same number as the Schwarzian of
    u = e^{kappa tau}. What is new: (a) over one real-time recurrence window of an array (Killing time
    2 pi/kappa, the array's spectrum being that of one chiral component on that window) this is -kappa/24,
    the array's zeta-regularised sea energy; (b) the sea energy of an evenly spaced array at offset delta
    is (kappa/2) B_2(delta), and (kappa/2) B_2(delta) + kappa/24 = (kappa/2)(delta - 1/2)^2, so the match holds
    at delta = 1/2 only; (c) the thermal energy above the sea at the half offset is the same kappa/24, so the
    symmetric value 0 is the null ground state's own value on the window. The reading that an array's Killing
    energy is the continuum's on one window is the discretisation reading of the stored continuum restatement
    (Theorem synthesis.positive-null-energy-gives-r-premises (iv)) applied to energy; it is stated as a
    hypothesis in clause (iv), not derived. Transport-absent in content (two-dimensional chiral fermion
    bookkeeping); it bears on op.residue-killing-weights: it is a reason for the half offset that is not the
    area law. Literature, from memory: the Hurwitz value zeta(-1, a) = -B_2(a)/2 (checked here by exact series
    inversion), the Casimir energy of a chiral fermion on a circle with antiperiodic condition, of which (b)
    is the array form.
---
## formal
Units $\hbar = c = 1$. On a half-generator of a horizon with surface gravity $\kappa$ let $u = e^{\kappa\tau}$, $\tau$ the Killing time. Call the \emph{null ordering} the normal ordering at the null ground state of Premise \claimref{synthesis.n-plus-null-ground-state}, in which that state has $\langle T_{uu}\rangle = 0$, and the \emph{boost ordering} the normal ordering at the boost ground state (the Mellin vacuum). An evenly spaced array with weights $\omega_{k} = \kappa(k + \delta)$, $k \in \Z$, $0 \le \delta < 1$, has the single-particle spectrum of one chiral complex component on a Killing-time interval of length $2\pi/\kappa$ with a twisted condition (its real-time recurrence window; that the array is that component on a window of the continuum is part of the window reading of (iv)), the offset $\delta = \tfrac12$ being the antiperiodic condition of Premise \claimref{singularity.q-joint-quasi-freeness-s-wave} version 3. Then:
\begin{enumerate}
\item[(i)] \emph{(The boost ground state on one window.)} The Schwarzian of $u = e^{\kappa\tau}$ is $\{u, \tau\} = -\kappa^{2}/2$, so the null ground state carries the Killing-frame energy density $\kappa^{2}/(48\pi)$ per complex component in the boost ordering, and the boost ground state $-\kappa^{2}/(48\pi)$ in the null ordering, the value of Theorem \claimref{synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit} at $c \to \infty$. Over one window of Killing time $2\pi/\kappa$ the boost ground state carries $-\kappa/24$ in the null ordering.
\item[(ii)] \emph{(The array's sea selects the offset.)} The zeta-regularised energy of the filled sea of the array in the symmetric ordering (half of each mode below and above, $\sum_{k}\omega_{k}(\psi_{k}^{\dagger}\psi_{k} - \tfrac12)$) is $\tfrac{\kappa}{2}B_{2}(\delta)$ for $0 < \delta < 1$, with $B_{2}(a) = a^{2} - a + \tfrac16$, and $+\kappa/12$ at $\delta = 0$. Since
\[
\tfrac{\kappa}{2}B_{2}(\delta) + \tfrac{\kappa}{24} = \tfrac{\kappa}{2}\bigl(\delta - \tfrac12\bigr)^{2},
\]
the array's sea in its symmetric ordering carries the boost ground state's null-ordered window energy $-\kappa/24$ exactly when $\delta = \tfrac12$, a double root, and at no other offset.
\item[(iii)] \emph{(The thermal state.)} At $\delta = \tfrac12$ and $\beta = 2\pi/\kappa$ the array's energy above its sea is $\kappa/24$ (Theorem \claimref{synthesis.counted-unit-energy-at-half-offset}(i)), equal to the null ground state's energy over one window in the boost ordering; in the symmetric ordering of (ii), which at this offset gives the null ground state's window value (the identification of the two orderings is the hypothesis of (iv)), it is $0$, the null ground state's value in every window. At $\delta = 0$ the energy above the sea is $\beta E \in (0.0235, 0.0236)$, not $\pi/12$, and the symmetric value is not $0$.
\item[(iv)] \emph{(The counted units, under the window reading.)} Suppose (the window reading, Premise \claimref{synthesis.window-reading-array-killing-energy}) the Killing energy of an array is the continuum's Killing energy over its recurrence window (the discretisation reading of Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(iv) applied to energy), measured, as (N$_{+}$) measures null energy, from the null ground state. Then at the weights of (Q) version 3 the physical ordering of the sea's energy is the zeta-regularised symmetric one; a counted unit of two arrays carries mean Killing energy $0$, the equality case of clause (v) of Theorem \claimref{synthesis.residue-from-mode-entropy}; in Theorem \claimref{synthesis.hole-mass-is-ground-energy-label}(iii) the constant of the hole's Hamiltonian is exactly $M$, and the label carries all of $M$, the counted units none. At the zero offset no ordering of the array is consistent with the null ordering window by window, since its symmetric sea is $+\kappa/12$, not $-\kappa/24$.
\end{enumerate}
So (N$_{+}$) decides the ordering question left open by the counted-unit energy result, given the window reading: the counted units carry no mean Killing energy, and the half offset of (Q) version 3 is the only offset at which the array's own zeta-regularised sea takes the continuum's null-ordered window value. Without the window reading, (i) to (iii) are equalities of numbers and the ordering is not decided.

## technical
The stored counted-unit result found that a counted unit at the weights of (Q) version 3 carries Killing energy $\kappa/12$ above its filled sea, and none in the zeta-regularised symmetric ordering, and left open which ordering is physical. (N$_{+}$) supplies the zero: the state of the horizon's light rays is the ground state of the affine null translations, and null energy is measured from it.

On one light ray, with Killing time $\tau$ and affine parameter $u = e^{\kappa\tau}$, the ground state of the affine translations and the ground state of the boost differ by the Schwarzian of the exponential map, $\{u, \tau\} = -\kappa^{2}/2$: measured from the null ground state the boost ground state has Killing-frame energy density $-\kappa^{2}/(48\pi)$, as the stored edge-scaling result found. An array with Killing-frequency spacing $\kappa$ has the spectrum of one chiral component on a Killing-time window of length $2\pi/\kappa$, and over that window the boost ground state carries $-\kappa/24$. The array's own boost ground state, its filled sea, has zeta-regularised symmetric energy $\tfrac{\kappa}{2}B_{2}(\delta)$, which equals $-\kappa/24$ exactly at the half offset: $\tfrac{\kappa}{2}B_{2}(\delta) + \tfrac{\kappa}{24} = \tfrac{\kappa}{2}(\delta - \tfrac12)^{2}$. At the half offset the array's thermal energy above its sea is also $\kappa/24$, so in the symmetric ordering the thermal array has energy zero, which is what the null ground state has on every window. The match is the standard modular relation between a chiral fermion's thermal state at temperature $\kappa/2\pi$ on the line and its antiperiodic vacuum on a circle of length $2\pi/\kappa$, whose Casimir energy is $-\tfrac{1}{24}\cdot\tfrac{2\pi}{L}$ (cited from memory); what is used here is that the antiperiodic, half-offset case is the only one where the array's zeta sea meets the continuum's null-ordered value. Under the window reading, which identifies the array's energy with the continuum's energy on its window, measured from the null ground state, the symmetric ordering is the physical one, the counted units carry no mean Killing energy, and the whole of $M$ sits in the constant of the hole's Hamiltonian.

## lay
The series counts the black hole's entropy in small units on its horizon, and an earlier result found that whether those units carry any energy depended on a bookkeeping choice: where to put the zero of energy. The series' own premise about the state on the horizon's light rays fixes that zero: energy is measured from the lowest state for motion along the light rays. Measured that way, a stretch of light ray as long as one unit's natural cycle carries exactly the amount of energy that the zero-point bookkeeping of a unit assigns, but only if the unit's energy levels sit halfway between whole steps, which is the choice the series made. If a unit's energy is taken to be the energy of that stretch of light ray, then with that zero the units carry no energy on average, and the hole's mass sits entirely in one overall constant rather than in the counted units.

## one-liner
Measured from the null ground state of (N$_{+}$), the boost ground state carries $-\kappa/24$ per component over an array's recurrence window, which equals the array's zeta-regularised sea energy $\tfrac{\kappa}{2}B_{2}(\delta)$ exactly at the half offset, $\tfrac{\kappa}{2}B_{2}(\delta) + \tfrac{\kappa}{24} = \tfrac{\kappa}{2}(\delta - \tfrac12)^{2}$; so, if an array's Killing energy is read as the continuum's over that window (the window reading), the symmetric ordering is the null ordering at (Q) version 3's weights, the counted units carry zero mean Killing energy and the constant of the hole's Hamiltonian is all of $M$.
