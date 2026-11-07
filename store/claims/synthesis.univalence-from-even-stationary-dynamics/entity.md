---
id: synthesis.univalence-from-even-stationary-dynamics
kind: claim
version: 3
title: 'Univalence from even stationary dynamics'
status: proved
region: synthesis
subject: descent
tags: [univalence, grading-and-parity, superselection, car-algebra]
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
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
about:
- obj.singularity.geometric-modular-condition-g
derivations:
- name: main
  uses:
  - rungs.imported-fock-representation-bogoliubov-group@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_grading_is_rotation_by_pi_in_every_mode_plane
- kind: check
  ref: check.py::check_even_hamiltonian_commutes_with_parity
- kind: check
  ref: check.py::check_stationary_states_even_iff_no_odd_resonance
- kind: check
  ref: check.py::check_counter_states_at_resonance_and_zero_weight
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - singularity.p-univalence
outside_ga:
  kind: complex-analysis
  why: 'the boundary modes are realised on a complex Fock space (e_{2k} = i(a_k^* - a_k), e^{i theta N_k}, the modular group rho^{it}); I_4 anticommutes with the atom mode operators (conventions, known limit 1), so it is not their unit'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the boundary modes are realised on a complex Fock space (e_{2k} = i(a_k^* - a_k), e^{i theta N_k}, the modular group rho^{it}); I_4 anticommutes with the atom mode operators (conventions, known limit 1), so it is not their unit.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 1 -> 2.'
  open_problem: pr.p-univalence
  note: >-
    Derives the univalence premise (P) for two classes of states from a superselection mechanism internal
    to the mode algebra: the grading is the rotation by pi in every mode plane, implemented by the
    product of the mode-plane bivectors, so any state invariant under a flow containing that rotation is
    even. Exact criterion for an even generator H: every H-stationary state is even iff the spectra of H on
    the even and odd Fock sectors are disjoint; for H a weighted number operator iff no signed sum of an
    odd number of weights vanishes (all weights odd multiples of one nonzero unit suffices, a common
    weight in particular). Every Gibbs state of an even generator is even, at every temperature,
    zero weight included. The residue of (P) is located: zero-weight modes and odd resonances such as
    w_3 = w_1 + w_2 admit stationary states that are not even, and (P) also constrains non-stationary
    states. The Wick-Wightman-Wigner mechanism is used in its internal form (a symmetry implemented on
    the algebra whose action is the grading) and is not imported. Complements the split of (P) into
    single-mode and cross-mode parts and its independence models (filed alongside,
    synthesis.univalence-even-extension-split, whose single-mode full-factor KMS clause is the one-mode case of
    (2) here): the cross-mode part follows from joint stationarity or the joint Gibbs form. Corollary:
    the geometric modular condition (G) implies (P).
    Transport-convenient: the mode planes are the transported ladder planes, but the argument is
    finite-dimensional fermionic algebra.
---

## formal
Let the boundary modes $a_1, \dots, a_n$ generate the CAR algebra, realised on Fock space as the spinor module of the Clifford algebra of their $2n$ Majorana generators $e_{2k-1} = a_k + a_k^*$, $e_{2k} = i(a_k^* - a_k)$, with parity the chirality (Fact \claimref{rungs.imported-fock-representation-bogoliubov-group}), and let $\alpha$ be the grading.
\begin{enumerate}
\item The grading is inner and is the rotation by $\pi$ in every mode plane: with $B_k = e_{2k-1}e_{2k}$ and $R_k(\theta) = \cos(\theta/2) - B_k\sin(\theta/2)$, $R_k(\pi) = -B_k$ negates the two generators of the $k$-th plane and fixes the others, and $\alpha = \operatorname{Ad}(B_1 \cdots B_n)$, the volume element of the mode space; on Fock space it is implemented by $\Gamma = \prod_k (1 - 2N_k)$.
\item If $H = H^*$ is even, $\alpha(H) = H$, every state with density a function of $H$, in particular every Gibbs state $e^{-\beta H}/Z$ at real $\beta$ ($\beta = 0$ included), is even: $\omega \circ \alpha = \omega$.
\item Every state invariant under the flow $\operatorname{Ad}(e^{itH})$ of an even $H$ is even if and only if the spectra of $H$ on the even and odd Fock sectors are disjoint. For $H = \sum_k \omega_k N_k$ this holds if and only if no signed sum $\sum_{k \in S} \varepsilon_k\omega_k$, $\varepsilon_k = \pm 1$, over a set $S$ of odd size vanishes. It holds when every weight is an odd multiple of one $\omega_0 \neq 0$ (a common nonzero weight in particular), and then $\alpha$ is the flow itself at time $\pi/\omega_0$.
\item It fails at a zero-weight mode, where $\tfrac12(1 + \tfrac12(a + a^*))$ is stationary and not even, and at an odd resonance: for weights $(1,2,3)$ the state $\tfrac18(1 + \tfrac12(x + x^*))$, $x = a_1a_2a_3^*$, is stationary, positive and not even.
\end{enumerate}
For the boundary modes' boost generator $K_{\mathrm{geo}} = \sum_k \omega_k K_k$ of the geometric modular condition (G) (Definition \claimref{obj.singularity.geometric-modular-condition-g}), with mode-dependent weights $\omega_k$, every stationary state is even if and only if no signed sum of an odd number of the $\omega_k$ vanishes; zero-weight modes violate this, and a common nonzero weight is an example that satisfies it. Every faithful state satisfying (G) is a Gibbs state of the even generator $K_{\mathrm{geo}}$, hence even by (2): (G) implies Premise \claimref{singularity.p-univalence}. Beyond these classes the premise excludes exactly the odd coherences at zero weight and at odd resonances, and it constrains states that are not stationary.

## technical
The grading of a fermionic mode algebra is not an outer symmetry that must be postulated: it is the rotation by $\pi$ in every mode plane, implemented by the product of the plane bivectors, which is the volume element of the mode space (on Fock space, the parity operator). Any state invariant under a flow that contains this rotation is therefore even, which is the superselection mechanism of Wick, Wightman and Wigner in an internal form: the symmetry that acts as the grading is part of the dynamics.

Two consequences follow for an even generator $H$, and a corollary for the geometric modular condition (G): a faithful state whose modular flow is the boost generated by $K_{\mathrm{geo}}$ is a Gibbs state of that even generator, so (G) implies (P). Gibbs states, being functions of $H$, commute with the parity and are even at every temperature, including the tracial state at zero weight. Stationary states are even for every such state exactly when the even and odd sectors share no energy; for a weighted number operator this is the absence of a vanishing signed sum of an odd number of weights, and a common nonzero weight suffices (the flow at time $\pi/\omega_0$ is then the grading). The premise adds content only at zero weight, at odd resonances such as $\omega_3 = \omega_1 + \omega_2$, and for non-stationary states; explicit stationary non-even states exist in the first two cases. Because the conditions are on the joint state, they deliver the cross-mode part of (P), the vanishing of odd correlations between modes, which no condition on single-mode marginals can supply.

## lay
The series assumes that physical states of its boundary modes never mix an even with an odd number of fermions. This result shows that the assumption follows from equilibrium. Flipping the sign of every fermion turns out to be the same as letting each mode's internal clock run half a turn. A state that is unchanged by the modes' own time evolution is therefore unchanged by that sign flip as well, provided no combination of an odd number of mode frequencies cancels out. Thermal states always qualify, and so does any state satisfying the series' geometric modular condition. The assumption still says something new only for modes of exactly zero frequency, for special frequency coincidences, and for states that change in time.

## one-liner
The grading of the mode algebra is the rotation by $\pi$ in every mode plane, so (P) holds for every Gibbs state of an even generator (hence (G) implies (P)) and for every state stationary under the boost $K_{\mathrm{geo}}$ when no signed sum of an odd number of its weights vanishes; zero weights and odd resonances are where (P) adds content.
