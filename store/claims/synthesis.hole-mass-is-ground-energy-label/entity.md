---
id: synthesis.hole-mass-is-ground-energy-label
kind: claim
version: 3
title: Read as a Gibbs state at the series' temperature, a hole carries more than half its mass as ground energy, all of it at zero weight
status: proved
region: synthesis
subject: entropy
tags: [boundary-modes, mode-counting, hawking-temperature, undetermined-input, needs-continuum]
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
derivations:
- name: main
  uses:
  - synthesis.quarter-from-temperature@1
  - synthesis.residue-from-mode-entropy@4
  - synthesis.boundary-mode-thermal-entropy@2
  - singularity.kms-uniqueness-factor@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_ground_energy_exceeds_free_energy
- kind: check
  ref: check.py::check_heat_capacity_sign
- kind: check
  ref: check.py::check_zero_weight_split
- kind: check
  ref: check.py::check_symmetric_ordering
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.residue-from-mode-entropy
  - synthesis.quarter-from-temperature
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'check_ground_energy_exceeds_free_energy widened to all 53 multi-state spectra with levels 0..3 and degeneracies <= 2; docstring (a) reworded from ''every spectrum'' to the spectra tested. Version 2 -> 3.'
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'W503: the lay level now states hypothesis (H), thermal equilibrium of the hole, as a condition. Version 1 -> 2.'
  open_problem: op.counted-mode-energy
  note: >-
    Necessity side of the energy tension. If the hole at mass M is a Gibbs state of some
    Hamiltonian at the series' temperature with mean energy M and entropy A/4, its free energy is
    M/2 and its partition function is e^{-A/4} < 1, which a Hamiltonian with zero ground energy can
    never give. So at least half of M, and at zero weight all of it, is the ground energy of the
    description, a c-number that must grow with M; no excitation sector (counted modes at any
    weights, or a normal-ordered exterior field) carries M. The equality case of the residue is
    therefore not excluded: it is the case in which the whole mass is that ground energy.
    Transport-absent (Gibbs thermodynamics); the series enters through T = 1/8 pi M and S = A/4.
---

## formal
Assume the hypotheses of Theorem \claimref{synthesis.quarter-from-temperature}, so that along the Schwarzschild family $T = 1/8\pi M$ and $S = A/4 = 4\pi M^{2}$, hence $TS = M/2$. Suppose further (hypothesis (H)) that at each mass $M$ the hole, counted modes together with whatever else it comprises, is in the Gibbs state $\varrho_M = e^{-\beta H_M}/Z_M$, $\beta = 8\pi M$, of a self-adjoint $H_M$ bounded below with $e^{-\beta H_M}$ of trace class, with $\tr(\varrho_M H_M) = M$ and von Neumann entropy $A/4$. Write $E_0(M) := \inf\operatorname{spec}H_M$, $H'_M := H_M - E_0(M) \geq 0$ and $Z'_M := \tr e^{-\beta H'_M}$. Then:
\begin{enumerate}
\item[(i)] the free energy is $F = M - TS = M/2$, so $\ln Z_M = -A/4$: $Z_M = e^{-A/4} < 1$, the value of the Euclidean action $I = \beta M/2 = A/4$ found by Gibbons and Hawking (1977);
\item[(ii)] $M/2 < E_0(M) \leq M$, and the excitation energy satisfies $\beta\,\tr(\varrho_M H'_M) = A/4 - \ln Z'_M < A/4$, that is $\tr(\varrho_M H'_M) < TS = M/2$. In particular no sector whose Hamiltonian has ground energy zero (the counted modes with $K_k = v_k^{*}v_k$, at any weights, or an exterior field normal-ordered to its Killing vacuum and regularised to trace class) carries energy $M$, or even $M/2$, in a Gibbs state at $\beta$ whose entropy is at most $A/4$; clause (v) of Theorem \claimref{synthesis.residue-from-mode-entropy} is the case of the counted modes. The conclusion does not depend on the ordering: with the symmetric generator $\omega_k(v_k^{*}v_k - \tfrac12)$ a counted mode carries $\beta E = x(n - \tfrac12) = -\tfrac{x}{2}\tanh\tfrac{x}{2} \leq 0 < s(x)$, and the shift of ordering only moves $E_0(M)$ by the constant $-\sum_j\omega_j/2$ (filed alongside, synthesis.central-label-carries-mass-at-zero-weight, which also gives the microcanonical model of the zero-weight case);
\item[(iii)] $E_0(M) = M$ if and only if $H_M$ is the scalar $E_0(M)$ on the support of $\varrho_M$. If the hole is the counted modes $J$ of Theorem \claimref{synthesis.residue-from-mode-entropy} with $H_M = E_0(M) + \sum_{j}\omega_j v_j^{*}v_j$, then $E_0(M) = M - E$ with $E$ the counted Killing energy, and $E_0(M) = M$ exactly in the equality case $\kappa_c = 1/(4\ln 2)$, every weight zero, where $Z'_M = 2^{|J|}$ and the Smarr relation $M = 2TS$ reads $\beta E_0 = 2|J|\ln 2$;
\item[(iv)] $E_0(M)/M \in (\tfrac12, 1]$ along the family, so the ground energy is unbounded and tends to $0$ with $M$: it is a function of the state's label $M$, not a constant offset; and $H_M$ cannot be independent of $M$ on any interval of masses, since for a fixed Hamiltonian $d\langle H\rangle_\beta/d\beta = -\operatorname{Var}_\beta(H) \leq 0$ while $dM/d\beta = 1/8\pi > 0$. This is the standard negative heat capacity of the Schwarzschild family, read as a statement about the Hamiltonian.
\end{enumerate}
So under (H) the carrier of the hole's internal energy is the ground energy $E_0(M)$ of its description, a c-number label carrying more than $M/2$ at every assignment of weights and all of $M$ at zero weight. The literal tension of clause (v) excludes the equality case only if $M$ is read as excitation energy; read under (H), the equality case is the case in which the counted modes carry all the entropy and none of the energy. Which physical structure supplies $E_0(M)$ (a horizon term of Smarr-Komar type is the natural candidate) is not decided here.

## technical
The energy tension says that counted modes holding the entropy $A/4$ carry less than $TS = M/2$ of Killing energy, and none at the registered zero weight, so something else must carry the hole's mass $M$. This result treats the hole at fixed mass as a thermal (Gibbs) state of some Hamiltonian at the series' temperature, with mean energy $M$ and entropy $A/4$. The free energy is then $M - TS = M/2$, so the partition function is $e^{-A/4}$, less than one. A Hamiltonian whose lowest energy is zero always has partition function at least one, so the Hamiltonian must contain a positive constant, its ground energy, larger than $M/2$. The excitations above that ground carry less than $M/2$; at zero weight they carry nothing and the ground energy is all of $M$. Because a fixed Hamiltonian's mean energy falls as the inverse temperature rises, while the hole's mass rises with it (the familiar negative heat capacity), the ground energy must change with the mass: it behaves as a label of the state. The partition function $e^{-A/4}$ is the Gibbons-Hawking value of the Euclidean action; what is new is the reading of it as a lower bound $M/2$ on the ground energy, reached by nothing and approached by the excitations only from below, with the whole mass in the ground energy exactly at zero weight. The bound does not depend on the ordering chosen for the counted modes' generator.

## lay
A black hole has a temperature, an entropy and a mass. The series' counted boundary modes can hold all of the entropy, but in its favoured case they carry no energy at all, which raised the question of where the mass lives. If the hole is assumed to be an ordinary system in thermal equilibrium at its own temperature (the result's hypothesis), that answers it: the numbers force more than half of the mass, and in the favoured case all of it, to be a fixed baseline energy of the whole system rather than the energy of any particles or excitations. That baseline grows with the hole, so it acts like a label saying which hole this is. No collection of particles at the hole's temperature holding at most the hole's entropy, outside or at the boundary, can supply half the mass or more.

## one-liner
If a hole of mass $M$ is a Gibbs state at $T = 1/8\pi M$ with mean energy $M$ and entropy $A/4$, then $Z = e^{-A/4} < 1$ forces a ground energy $E_0 \in (M/2, M]$ that varies with $M$: more than half the mass is a c-number ground energy, all of it at zero weight, where the registered residue is therefore not excluded.
