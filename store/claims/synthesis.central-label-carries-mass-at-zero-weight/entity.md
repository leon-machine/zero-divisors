---
id: synthesis.central-label-carries-mass-at-zero-weight
kind: claim
version: 2
title: 'A microcanonical hole with its mass on a central label'
status: proved
region: synthesis
subject: entropy
tags: [boundary-modes, finite-models, superselection, mode-counting, needs-continuum]
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
  - hawking.modular-structure-completed-pair@3
  - scrambling.boundary-mode-space-matrix@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_tension_both_orderings
- kind: check
  ref: check.py::check_central_label_model
- kind: check
  ref: check.py::check_no_gibbs_state
- kind: check
  ref: check.py::check_moved_mode_ratio
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
    note: 'Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 1 -> 2.'
  open_problem: op.counted-mode-energy
  note: >-
    The explicit microcanonical model of the canonical reading filed alongside,
    synthesis.hole-mass-is-ground-energy-label (a consistency model, not a derivation). The
    tension of clause (v) holds under both operator orderings, so the ordering does not decide it.
    In a direct sum over the number m of counted modes, each sector a Fock space of m zero-weight
    pairs, with the Hamiltonian a function of the central label m, the counted modes carry
    A/4 with zero Killing excitation energy and the hole is a microcanonical system of energy M
    at the series' temperature, with Clausius and Smarr holding, and M sits on the label, not on the modes (the edge-mode pattern). The label's energy function
    is fixed by the area law, so the model restates it and derives nothing about it; the canonical
    ensemble does not exist for it (negative heat capacity). Transport-absent apart from the
    completed pairs as modes.
---

## formal
Assume (P) and (R) as in Theorem \claimref{synthesis.quarter-from-temperature}, so that a boundary mode of Killing weight $\omega$ is thermal at $T(M) = 1/8\pi M$ with occupancy $n = 1/(e^{x} + 1)$, $x = 2\pi\omega/\kappa$, and entropy $s(x)$ (Theorem \claimref{synthesis.boundary-mode-thermal-entropy}).
\begin{enumerate}
\item[(i)] (the tension does not depend on the ordering) with the normal-ordered generator $\omega N$ a mode carries $\beta E = x\,n < s(x)$; with the symmetric generator $\omega K = \omega(N - \tfrac12)$ of Proposition \claimref{hawking.modular-structure-completed-pair}(4) it carries $\beta E = x(n - \tfrac12) = -\tfrac{x}{2}\tanh\tfrac{x}{2} \le 0 < s(x)$. Under both, clause (v) of Theorem \claimref{synthesis.residue-from-mode-entropy} holds, $E < TS = M/2$, and $E = 0$ exactly at zero weight;
\item[(ii)] (the model) let $\mathcal{H} = \bigoplus_{m \ge 0}\mathcal{H}_{m}$, with $\mathcal{H}_{m}$ the Fock module of $m$ completed pairs (dimension $2^{m}$; Proposition \claimref{scrambling.boundary-mode-space-matrix}), every pair of Killing weight zero, and let the Hamiltonian be the central element $H = \mu(\hat m)$, $\hat m = m$ on $\mathcal{H}_{m}$, with $4\pi\mu(m)^{2} = m\ln 2$. On $\mathcal{H}_{m}$ the counted modes' Killing generator vanishes, so their Killing excitation energy is $0$ under either ordering; (R) at zero weight fixes each marginal at $n = \tfrac12$, and with the joint state $2^{-m}\mathbf{1}$ the counted modes carry $S = m\ln 2$. With $M := \mu(m)$ and $A = 16\pi M^{2}$, $S = A/4$, which is the equality case of Theorem \claimref{synthesis.residue-from-mode-entropy}(ii), and the microcanonical entropy at energy $M$ is $\ln\dim\mathcal{H}_{m} = 4\pi M^{2}$, so along the family $dS/dM = 8\pi M = 1/T(M)$, $S \to 0$ as $M \to 0$, and $M = 2TS$. The hypotheses of Theorem \claimref{synthesis.quarter-from-temperature} (a thermodynamic system of internal energy $M$ at $T(M)$ obeying Clausius) and those of the equality case of Theorem \claimref{synthesis.residue-from-mode-entropy} (counted modes carrying $A/4$, all of weight zero) hold together. The internal energy is the value of the central label, which commutes with every counted mode operator and is invisible to their Killing flow; each added counted mode raises it by $dM = T\ln 2$. At fixed $M$ the sector $\mathcal{H}_{m}$ with the state $2^{-m}\mathbf{1}$ is the zero-weight case of the canonical reading filed alongside (synthesis.hole-mass-is-ground-energy-label), a Hamiltonian equal to $M$ on a space of dimension $2^{|J|}$, so this model realises that reading's c-number label explicitly;
\item[(iii)] (microcanonical only) $H$ has no Gibbs state: $\sum_{m} 2^{m}e^{-\beta\mu(m)}$ diverges for every $\beta > 0$, since $\mu(m) < \sqrt{m}/4$, and $dM/dT = -8\pi M^{2} < 0$; this is the negative heat capacity that the canonical reading meets as the statement that no fixed Hamiltonian is Gibbs along the family;
\item[(iv)] (moved modes do not change the carrier) a counted mode at $x = 2\pi$ carries $\beta E/s(2\pi) = 2\pi n(2\pi)/s(2\pi) \in (0.8625, 0.8627)$ of its entropy share in normal order, so at any mixture of zero-weight modes and modes at $x = 2\pi$ the counted modes carry less than $TS$ and the remainder of $M$ is carried elsewhere.
\end{enumerate}
So the carrier of $M$ can be a central label, a function of the number of counted modes, with the counted modes at zero weight; what follows from this for the registered residue is drawn in the canonical reading filed alongside. The function $\mu$ is fixed by the area law, so the model is a consistency statement about the area law, not a derivation of it, and it does not show that the series' boundary modes realise it.

## technical
The residue reformulation found a tension. If the counted boundary modes carry the hole's entropy $A/4$, their Killing excitation energy is below $TS = M/2$, and zero at the registered residue, where every counted mode has zero weight; yet Hawking's argument treats the hole as a system of internal energy $M$. The tension holds whichever operator ordering is used, so it is not an artefact of normal ordering.

The canonical reading filed alongside (synthesis.hole-mass-is-ground-energy-label) shows that a hole read as a Gibbs state carries its mass as a c-number ground energy. This result builds that picture explicitly in the microcanonical ensemble. Take the counted modes in sectors labelled by their number $m$, each sector the Fock space of $m$ zero-weight pairs, and let the energy be a function of the label alone, $4\pi\mu(m)^{2} = m\ln 2$. The modes then carry $m\ln 2 = A/4$ and no Killing energy, while the system as a whole has energy $M = \mu(m)$, microcanonical entropy $4\pi M^{2}$, temperature $1/8\pi M$, and obeys Clausius and Smarr. The mass sits on the label, the pattern of edge modes, and each added mode costs $T\ln 2$. The canonical ensemble does not exist for this Hamiltonian (negative heat capacity), and the energy function is the area law written backwards, so this is consistency only.

## lay
If the boundary modes that hold a black hole's entropy carry no energy, where is the black hole's mass? A companion result shows that the mass must be a single number attached to the state rather than carried by excitations; this one builds a concrete example. A model is given in which the modes hold all the entropy and none of the energy, and the mass is a single number attached to how many modes there are, much as the charge of a sector is attached to the sector rather than to any particle in it. The model reproduces the black hole's temperature and its first law. It does not explain why the mass depends on the number of modes in the way it does: that dependence is put in by hand from the area law.

## one-liner
The counted modes' energy is below $M/2$ under either ordering; a microcanonical model with zero-weight counted modes carrying $A/4$ and the mass $M$ on a central label obeys Clausius and Smarr at the series' temperature, realising explicitly the c-number mass label of the canonical reading.
