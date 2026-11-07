---
id: synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard
kind: claim
version: 3
title: 'Massive Dirac: instantaneous vacua and non-smooth descents are not Hadamard'
status: proved
region: synthesis
subject: quantum-fields
tags: [car-algebra, no-go, pairing-and-bogoliubov, frozen-point, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-01-deposit-state
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.imported-microlocal-hadamard-condition@2
  - synthesis.sudden-descent-feature-not-tilt@3
  - synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard@2
  - synthesis.imported-ford-parker-infrared-divergence@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_pauli_two_level_bloch_form
- kind: check
  ref: check.py::check_adiabatic_series_solves_the_bloch_equation
- kind: check
  ref: check.py::check_instantaneous_vacuum_differs_at_order_k_minus_two
- kind: check
  ref: check.py::check_deposits_diagonal_over_the_instantaneous_vacuum_keep_the_gap
- kind: check
  ref: check.py::check_jump_law
- kind: check
  ref: check.py::check_stored_sudden_start_differs_from_bunch_davies_unboundedly
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise
  - synthesis.frozen-point-geometry-reads-descent-as-vacuum
  - synthesis.imported-propagation-of-hadamard-form
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit of the two-level mode equation I u'' = Hu is now written as the Pauli pseudoscalar I = sigma_1 sigma_2 sigma_3 (I_4 read in the even subalgebra), as the proof already identified it, and the Bunch-Davies mode u = e^{-I_4 z}(1 - I_4/z) with the instantaneous data chi_z = -I_4 use the field theory''s unit I_4 (numbers read in span{1, I_4}); no bare i remains.'
  open_problem: op.deposit-state-is-hadamard
  note: >-
    Sets outside state-selection principles against the descent's deposit on the deposit's own field, the
    Dirac field, and records which choices fail. The stored deposit result
    (synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise) takes the vacuum to be any pure quasi-free state
    and bounds the deposit by the number of quanta above it. For a massless Dirac field the conformal vacuum is
    exact (every correction of the adiabatic series vanishes at M = 0). For a massive field this result shows
    three ways to fail the Hadamard property: taking the instantaneous vacuum (diagonalising the Hamiltonian at
    one instant, where ma' is nonzero), any deposit diagonal over it whatever its occupations, and any state
    carried through a descent across which M = ma is not smooth. The Hadamard property belongs to the deposit,
    not to its reference vacuum: an adiabatic state of infinite order is itself a state with finitely many
    pair-coherent quanta over the instantaneous vacuum, so no claim is made that a Hadamard deposit's vacuum
    must be adiabatic, and no massive analogue of the occupation-moment criterion (synthesis.deposit-over-the-conformal-vacuum-is-hadamard-exactly-when-every-occupation-moment-is-finite), the
    primary statement that the number of quanta does not decide the Hadamard property) is claimed. Outside
    principles that give Hadamard states on Robertson-Walker fields: adiabatic states of infinite order
    (Hollands 2001 for the Dirac field), states of low energy (Olbermann 2007, scalar field), the Bunch-Davies
    state that the frozen point's invariance selects on a de Sitter stage, the Brum-Fredenhagen modification
    of the Sorkin-Johnston state (scalar field). Not Hadamard: the instantaneous vacuum (here for the Dirac
    field; Degner and Verch 2010 for the scalar field) and the unmodified Sorkin-Johnston state in general
    (Fewster and Verch 2012). Bearing on the premise that the deposited state is Hadamard on a Cauchy collar of
    the descent: under it the deposit is none of the three failing kinds. At a radiation-type origin M = ma
    vanishes linearly in conformal time and is smooth, so the jump law does not fire there. A join with the
    scale factor continuous and its logarithmic derivative jumping (the second reading of the join in
    synthesis.frozen-point-geometry-reads-descent-as-vacuum) is the case n = 1. Clause (iv) records that the
    stored sudden-descent model's instantaneous start (synthesis.sudden-descent-feature-not-tilt) is not
    Hadamard; its late-time spectrum statement is unaffected. Transport-absent: the content is the standard
    adiabatic expansion of the Dirac field on Robertson-Walker fields, re-derived in the Bloch form; the series
    supplies the setting (the descended field, the deposit's open choice of vacuum, the Pauli pseudoscalar as
    the unit, i = I4 on the even subalgebra). Literature: Hollands, Commun. Math. Phys. 216 (2001), imported as
    synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard (clause (c), adiabatic states of infinite
    order are Hadamard; only this direction is used); Ford and Parker (1977) on the infrared divergence of the
    massless Bunch-Davies state, imported as synthesis.imported-ford-parker-infrared-divergence; Landete, Navarro-Salas and Torrenti, arXiv
    1305.7374 (the two-component mode equations, checked); Degner and Verch, arXiv 0904.1273; Olbermann,
    arXiv 0704.2986; Fewster and Verch, arXiv 1206.1562; Brum and Fredenhagen, arXiv 1307.0482 (abstracts
    checked); the Hadamard property of an infrared-regularised Bunch-Davies state of the massless minimally
    coupled scalar and the pseudolocality of pseudodifferential operators, cited from memory.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, at Leon''s decisions of 2026-11-01 (deposit-state imports): uses edges to the imported Facts on Dirac Hadamard states (Hollands 2001, adiabatic states of infinite order are Hadamard, clause (c)) and on the infrared divergence (Ford and Parker) replace the citations in the proof; the pins move to the microlocal Fact version 2, whose clause (a) now states the scalar smooth-difference property used in (iv), and to the sudden-descent result version 3 (an added note citing this result, not used here). Statement, proof steps and checks otherwise unchanged; the Hadamard property of the infrared-regularised comparison state in (iv) stays cited from memory.'
  flags:
  - 'the reduction of the Dirac field on a spatially flat Robertson-Walker field to the two-level system is standard and cited, not derived in the spacetime algebra'
  - 'the Hadamard conclusions of (ii), (iii) are given Hollands 2001 (adiabatic states of infinite order of the Dirac field are Hadamard; imported Fact synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard, clause (c)); that of (iv) is given the smooth-difference property of scalar Hadamard states and the Hadamard property of an infrared-regularised Bunch-Davies comparison state'
---

## formal
Let the descended field be a spatially flat Robertson-Walker gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with conformal time $\eta$ and scale factor $a(\eta)$, and let $\psi$ be a free Dirac field of mass $m \ge 0$. With $\chi = a^{3/2}\psi$, each momentum $\vec k$, $k = |\vec k|$, and helicity sector is the two-level system $I u' = Hu$, $H = M\sigma_{3} + k\sigma_{1}$, $M = ma(\eta)$, in the Pauli algebra with unit its pseudoscalar $I = \sigma_{1}\sigma_{2}\sigma_{3}$ ($I_{4}$ read in the even subalgebra); for a pure state $\rho = \tfrac12(1 + s)$, $s$ a unit vector, it reads $s' = 2h \times s$ with $h = k\sigma_{1} + M\sigma_{3}$. Write $M_{j} = d^{j}M/d\eta^{j}$, $\hat h = h/|h|$, and $|\beta_{k}|^{2} = \tfrac12(1 - s\cdot s')$ for the Bogoliubov coefficient between the pure states of Bloch vectors $s$ and $s'$.
\begin{enumerate}
\item[(i)] \emph{(Adiabatic series.)} The equation has a unique formal solution $s_{\mathrm{ad}} = \sum_{j \ge 0}k^{-j}c_{j}$ with $c_{0} = \sigma_{1}$, each $c_{j}$ a vector polynomial in $M_{0}, \dots, M_{j-1}$, homogeneous of weight $j$ when $M_{i}$ has weight $i + 1$, and $|s_{\mathrm{ad}}| = 1$ order by order: $c_{1} = M\sigma_{3}$, $c_{2} = -\tfrac12 M^{2}\sigma_{1} + \tfrac12 M_{1}\sigma_{2}$. The only monomial of $c_{n+1}$ containing $M_{n}$ is $\lambda_{n}M_{n}v_{n}$ with $v_{n} = \sigma_{3}$ for $n$ even, $\sigma_{2}$ for $n$ odd, and $\lambda_{n} = (-1)^{\lfloor n/2\rfloor}2^{-n}$; $M_{n}$ does not occur in $c_{j}$ for $j \le n$. At $m = 0$ every $c_{j}$ with $j \ge 1$ vanishes.
\item[(ii)] \emph{(The instantaneous vacuum.)} $\hat h$ agrees with $s_{\mathrm{ad}}$ through order $k^{-1}$ and differs from it at order $k^{-2}$ by $\tfrac12M_{1}\sigma_{2}$; $1 - s_{\mathrm{ad}}\cdot\hat h = M_{1}^{2}/(8k^{4}) + \bigl(\tfrac1{32}M_{2}^{2} - \tfrac1{16}M_{1}M_{3} - \tfrac38M^{2}M_{1}^{2}\bigr)k^{-6} + O(k^{-8})$. So, at an instant where $M_{1} = ma' \neq 0$, the instantaneous vacuum has $|\beta_{k}|^{2} = M_{1}^{2}/(16k^{4}) + O(k^{-6})$ against an adiabatic state of infinite order: a finite number density of quanta above that state, but a point-split energy density relative to it that diverges to $-\infty$ logarithmically. Given that adiabatic states of infinite order of the Dirac field are Hadamard (Fact \claimref{synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard}(c)), the instantaneous vacuum is not Hadamard. Every gauge-invariant quasi-free deposit diagonal over it, whatever its occupations, has the same $\sigma_{2}$ gap $\tfrac14M_{1}k^{-2} + O(k^{-4})$ in its one-particle symbol against the adiabatic state, and is not Hadamard either.
\item[(iii)] \emph{(Jump law.)} If $M$ is of class $C^{n-1}$ at $\eta_{d}$ and its $n$-th derivative jumps by $\Delta M_{n}$, a state equal to an adiabatic state of infinite order before $\eta_{d}$ has after it, against the adiabatic states there,
\[
|\beta_{k}|^{2} \;=\; \frac{(\Delta M_{n})^{2}}{(2k)^{2n+2}} + O\bigl(k^{-2n-3}\bigr).
\]
For $n = 0$ (the mass switched on at once) the number density of quanta diverges; for $n = 1$ (a kink, such as a jump of $a'/a$ with $a$ continuous) it is finite and the energy density diverges logarithmically; for $n \ge 2$ the energy density is finite. Given the same theorem, the state is not Hadamard for any finite $n$.
\item[(iv)] \emph{(The stored sudden start.)} For the massless scalar of Proposition \claimref{synthesis.sudden-descent-feature-not-tilt} the instantaneous start falls below the Bunch-Davies state at the descent by $1/(2k^{3}\eta_{d}^{2})$ per mode in $\langle\chi^{2}\rangle$ and by $1/(4k^{3}\eta_{d}^{4})$ per mode in the energy $\tfrac12(|\chi'|^{2} + k^{2}|\chi|^{2})$, with $|\beta_{k}|^{2} = 1/(4k^{4}\eta_{d}^{4})$; both mode sums diverge logarithmically, so, given that an infrared-regularised Bunch-Davies state is Hadamard and that scalar Hadamard states differ by smooth kernels (Fact \claimref{synthesis.imported-microlocal-hadamard-condition}(a)), that start is not Hadamard.
\end{enumerate}
Consequently a massive Dirac deposit equal to, or diagonal over, the instantaneous vacuum at an instant where $ma' \neq 0$, or carried through a descent that is not smooth in $M = ma$, is not Hadamard; the instantaneous vacuum has finitely many quanta above a Hadamard state, so the number of quanta does not decide the Hadamard property.

## technical
The stored deposit result reads the descent's deposit as a vacuum plus shot noise, with the vacuum any pure quasi-free state. The Hadamard condition concerns the ultraviolet tail of the deposit relative to a Hadamard reference, and the outside literature offers several principles for picking a vacuum. This result tests the simplest one, and the smoothness of the descent, on the massive Dirac field, the deposit's own field, on the descended Robertson-Walker field. Each momentum and helicity sector is a two-level system, and in the Pauli algebra a pure state is a unit Bloch vector precessing about $h = k\sigma_{1} + M\sigma_{3}$, $M = ma$. Its adiabatic expansion is a formal series in $1/k$ whose coefficients are polynomials in the derivatives of $M$; the recursion is $\sigma_{1} \times c_{n+1} = \tfrac12(c_{n}' - 2M\sigma_{3} \times c_{n})$ with the $\sigma_{1}$ part fixed by the norm, and it is computed exactly to order nine.

Three facts follow. The instantaneous eigenvector $h/|h|$, the vacuum obtained by diagonalising the Hamiltonian at one instant, misses the term $\tfrac12M'\sigma_{2}/k^{2}$, so where $ma' \neq 0$ its Bogoliubov coefficient against an adiabatic state of infinite order is $|\beta_{k}|^{2} = M'^{2}/(16k^{4})$: few enough quanta for a finite number density, too many for a finite energy density (the energy moment is logarithmic). Since adiabatic states of infinite order are Hadamard (Hollands) and two Hadamard states differ by a smooth kernel, the instantaneous vacuum is not Hadamard. A deposit diagonal over it, with any occupations, has a one-particle symbol commuting with $h$, so it keeps the same $\sigma_{2}$ gap and fails too. Second, a derivative $M^{(n)}$ first enters the series at order $k^{-(n+1)}$, alone and with coefficient of size $2^{-n}$, so a descent across which $M^{(n)}$ jumps leaves $|\beta_{k}| = |\Delta M^{(n)}|/(2k)^{n+1}$: a sudden switch-on of the mass gives infinitely many quanta, a kink in the scale factor's growth rate a logarithmically infinite energy, and any finite smoothness a power-law tail, never a Hadamard state. At a radiation-type origin $M$ vanishes linearly in conformal time and is smooth, so this clause does not fire there. The stored sudden-descent model's instantaneous start of a massless scalar is the scalar instance: at the descent it differs from the Bunch-Davies state by logarithmically divergent mode sums already in $\langle\chi^{2}\rangle$.

What is not claimed: that a Hadamard deposit's reference vacuum must be adiabatic. An adiabatic state of infinite order is itself a finite number of pair-coherent quanta over the instantaneous vacuum, so the Hadamard property is a property of the deposit as a whole. For the massless Dirac field the conformal vacuum is exact and the question reduces to the occupation profile. The content is standard adiabatic theory; the series supplies the question.

## lay
The series needs the quantum state left behind by the descent to be of a regular kind, called Hadamard, so that energies can be computed. An earlier result described that state as a vacuum plus a sprinkling of particles, without saying which vacuum. For electrons and their kin, on an expanding universe, the vacuum is not unique: different recipes give different answers. This result tests the most naive recipe, taking the lowest-energy state at a single instant, and finds that it fails: compared with a regular state it carries a thin spray of extra particles at high energies, few in number but with infinite energy, and adding particles on top of it does not repair this. The same calculation shows that any abrupt descent fails too: a sudden change, even only in how fast the universe grows, leaves a high-energy tail that spoils the regularity. A simpler model stored earlier, with a sudden start, fails in the same way.

## one-liner
For a massive Dirac field on a Robertson-Walker field, at an instant where $ma' \neq 0$ the instantaneous vacuum differs from an adiabatic state of infinite order at order $k^{-2}$ by $M'/2$ ($|\beta_{k}|^{2} = M'^{2}/16k^{4}$: finite number, logarithmically divergent energy) and is not Hadamard, nor is any deposit diagonal over it; a descent across which the $n$-th derivative of $M = ma$ jumps leaves $|\beta_{k}| = |\Delta M^{(n)}|/(2k)^{n+1}$ and no Hadamard state; the stored sudden start is not Hadamard either; the number of quanta does not decide.
