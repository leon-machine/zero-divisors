---
id: synthesis.counted-unit-energy-at-half-offset
kind: claim
version: 2
title: 'A counted unit''s Killing energy at the weights of (Q)'
status: proved
region: synthesis
subject: entropy
tags: [boundary-modes, mode-counting, hawking-temperature, bosonisation, undetermined-input, needs-continuum]
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
  role: notation pass, imaginary units resolved by the unit principle (U1 to U6)
  version: 2
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
derivations:
- name: main
  uses:
  - synthesis.boundary-mode-thermal-entropy@2
  - synthesis.half-integer-weight-array-carries-half-ln2@5
  - synthesis.imported-theta-function-identities@2
  - synthesis.residue-from-mode-entropy@4
  - synthesis.quarter-from-temperature@1
  - synthesis.hole-mass-is-ground-energy-label@3
  assumes:
  - singularity.q-joint-quasi-freeness-s-wave@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_array_thermal_energy
- kind: check
  ref: check.py::check_sea_energy_zeta
- kind: check
  ref: check.py::check_counted_unit_against_mass
- kind: check
  ref: check.py::check_heat_capacity_distinguishes
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.hole-mass-is-ground-energy-label
  - synthesis.central-label-carries-mass-at-zero-weight
  - synthesis.half-integer-weight-array-carries-half-ln2
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle (U1) the modular parameter of the array''s torus is read in span{1, I_4}, as for theta functions and modular forms: tau = I_4 beta kappa/2 pi and the self-dual point tau = I_4; the outside_ga declaration is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the i of the modular parameter tau = i beta kappa/2 pi, of the self-dual point tau = i and of the theta-function argument is complex analysis of modular forms; declared (version and levels unchanged).'
  open_problem: op.counted-mode-energy
  note: >-
    The problem's second line of attack: the energy of the counted units at the weights of (Q) version 3, which the
    open problem records as not yet recomputed against M. The exact value comes from the step f'(2 pi) = 0 of the
    stored half-offset proof (the S-invariance of theta_3/eta at tau = i, imported Fact), which is the statement that
    the array's thermal energy above its sea is exactly 1/24 of the weight spacing; equivalently the classical
    identity sum over odd n of n/(e^{n pi} + 1) = 1/24 (cited from memory; the check bounds the sum rigorously
    without it). The sea value kappa zeta(-1, 1/2) = kappa/24 is computed exactly. Transport-absent: a computation
    in the series' own variables. It decides nothing about which ordering of the generator is physical, nor what
    supplies the label. An independent recomputation by rigorous rational bounds gives the same values (within
    10^-57 of 1/24 for the array energy in units of kappa, and of (1/2) ln 2 - pi/12 for ln Z above the sea).
    The premise (Q) version 3 (singularity.q-joint-quasi-freeness-s-wave) is cited in the text and enters through
    the half-offset theorem's cone; with a direct assumes edge to it.
---

## formal
Assume (Q) version 3 (Premise \claimref{singularity.q-joint-quasi-freeness-s-wave}): one s-wave array $\{\psi_{k}\}_{k \in \Z}$ has weights $\omega_{k} = \kappa(k + \tfrac12)$ and is in the quasi-free state at $\beta = 2\pi/\kappa$, so that mode $k$ has $x_{k} = 2\pi(k + \tfrac12)$ and occupation $n(x) = 1/(e^{x} + 1)$ above the sea (holes below it); a counted unit, the bookkeeping unit of the total horizon count per light ray, is two arrays, carrying $\ln 2$ (Theorem \claimref{synthesis.half-integer-weight-array-carries-half-ln2}(i), (iii)). Measure the Killing energy $E$ from the filled sea (the normal-ordered generator, ground energy $0$). Then:
\begin{enumerate}
\item[(i)] (one array) $\beta E = 2\sum_{k \geq 0}x_{k}n(x_{k}) = \pi/12$ exactly, that is $E = \kappa/24$, by the imported theta-function identities (Fact \claimref{synthesis.imported-theta-function-identities}); without them $|\beta E - \pi/12| < 10^{-55}$ by rigorous rational bounds. For the zero offset $\omega_{k} = \kappa k$ the same sum is $\beta E \in (0.02351, 0.02352)$: the value is specific to the half offset;
\item[(ii)] (the sea) the zeta-regularised energy of the filled sea is $-\kappa\,\zeta(-1, \tfrac12) = -\kappa/24$ per array, the finite part of $-\kappa\sum_{n \geq 0}(n + \tfrac12)e^{-\epsilon(n + 1/2)}$ as $\epsilon \to 0$. Hence with the symmetric generator $\sum_{k}\omega_{k}(\psi_{k}^{\dagger}\psi_{k} - \tfrac12)$ of Theorem \claimref{synthesis.hole-mass-is-ground-energy-label}(ii), summed over the whole array and zeta-regularised, one array has $\beta E = 0$ and $\ln Z = \tfrac12\ln 2$, and one counted unit has $Z = 2$, $E = 0$, $S = \ln 2$ at the Hawking temperature, the values of one zero-weight mode;
\item[(iii)] (against the hole) per counted unit $\beta E = \pi/6$ and $E/(TS) = \pi/(6\ln 2) \in (0.75539, 0.75540)$, below one as clause (v) of Theorem \claimref{synthesis.residue-from-mode-entropy} requires. Under the area-law hypothesis ($N = A/(4\ln 2)$ counted units, $T = 1/8\pi M$, Theorem \claimref{synthesis.quarter-from-temperature}) the counted units carry $E_{\mathrm{c}} = \pi M/(12\ln 2) \in (0.37769, 0.37770)\,M$, below $TS = M/2$; if the hole is the Gibbs state of hypothesis (H) of Theorem \claimref{synthesis.hole-mass-is-ground-energy-label} with the counted units as its excitations, its ground energy is $E_{0}(M) = M(1 - \pi/(12\ln 2)) \in (0.62230, 0.62231)\,M$, inside the interval $(M/2, M]$ of that theorem's (ii) and strictly below the zero-weight value $M$ of its (iii). This value is independent of the ordering, since $E_{0}$ is the bottom of the spectrum; in the symmetric ordering of (ii) the same Hamiltonian is a c-number of exactly $M$ plus counted units of mean energy zero, and the Smarr relation reads $\beta M = 2N\ln 2$ as in the zero-weight case;
\item[(iv)] (what distinguishes the two realisations of $\ln 2$) the energy fluctuation of one counted unit is $\beta^{2}\operatorname{Var}(E) \in (1.5964, 1.5965)$, against $0$ for one zero-weight mode.
\end{enumerate}
Remark (not a further clause): the exact values in (i) and (ii) come from the self-dual point $\tau = I_4$ of the modular parameter (read, as for every modular form, in $\mathrm{span}\{1, I_4\}$), where the real-time recurrence period $2\pi/\kappa$ of the array's Killing flow equals the thermal period $\beta$; the zero offset has no comparable simplification.
So at the adopted weights the counted units carry about $0.378\,M$ of excitation energy above their sea and the label carries the rest, about $0.622\,M$. Whether the counted units carry any energy at all is a matter of how the sea's energy is ordered: in the zeta-regularised symmetric ordering they carry none and the label is all of $M$. Which ordering is physical, and what structure supplies the label, are not decided here.

## technical
The open problem asks how the hole's mass $M$ is carried, given that boundary modes holding the entropy $A/4$ carry less than $TS = M/2$ of Killing energy, and notes that the energy of the counted units at the adopted half-integer weights had not been recomputed. It is exact. At the Hawking temperature one array of weights $\kappa(k + \tfrac12)$ is at the self-dual point of its period torus, where the stored proof of its entropy shows that the derivative of $\log(\vartheta_{3}/\eta)$ vanishes; what remains of the energy is the Casimir factor, so one array's thermal energy above its sea is exactly $\kappa/24$, and a counted unit of two arrays carries $\kappa/12$ with entropy $\ln 2$.

Against the hole: the counted units together carry $\pi M/(12\ln 2)$, about $0.378\,M$, three quarters of $TS$, so under the Gibbs reading the ground-energy label is about $0.622\,M$. The zeta-regularised energy of the filled sea is exactly $-\kappa/24$ per array, the same size with the opposite sign. With the symmetric ordering of the generator the counted unit therefore has partition function $2$, mean energy $0$ and entropy $\ln 2$, exactly the values of one zero-weight mode, and the label is all of $M$. The two realisations of the registered residue (one zero-weight mode, or two half-offset arrays) agree at the Hawking temperature in partition function, entropy and, with this ordering, mean energy; they differ in the energy fluctuation, about $1.6$ against $0$, and so in the bottom of the spectrum, $M$ against $0.622\,M$.

## lay
The series counts quantum modes at a black hole's boundary, and its adopted rule groups them into units that each hold one bit of entropy at the hole's temperature. A standing puzzle is where the hole's mass sits, since these modes cannot hold much energy. This result computes their energy exactly at the adopted rule: each unit holds one twelfth of the basic energy step, which adds up to about 38 percent of the hole's mass, so the rest, about 62 percent, has to be a fixed baseline energy of the whole system. If the energy of the modes' filled sea is counted in the standard regularised way, the units hold no energy at all and the baseline is the whole mass; the units then behave, at that temperature, exactly like the idealised zero-energy modes of the original count, except that their energy fluctuates.

## one-liner
At (Q) version 3's weights a counted unit of two arrays carries Killing energy exactly $\kappa/12$ above its sea at the Hawking temperature ($\beta E = \pi/6$), so under the area law the counted units carry $\pi M/(12\ln 2) \approx 0.378\,M$ and a Gibbs hole's ground-energy label is $M(1 - \pi/(12\ln 2))$; the sea's zeta-regularised energy cancels it exactly, so in the symmetric ordering the unit has $Z = 2$, $E = 0$, $S = \ln 2$ like a zero-weight mode, differing only in energy fluctuation.
