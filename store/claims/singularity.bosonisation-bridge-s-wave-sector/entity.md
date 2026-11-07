---
id: singularity.bosonisation-bridge-s-wave-sector
kind: claim
version: 8
title: The bosonisation bridge, s-wave sector
status: proved
region: singularity
subject: thermality
tags: [bosonisation, boundary-modes, radiation-spectrum]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass on Leon''s decisions, the weights kappa k labelled as version 2 of premise (Q); the Planck value holds at both offsets'
  version: 8
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  uses:
  - singularity.modular-structure-completed-pair@5
  assumes:
  - singularity.q-joint-quasi-freeness-s-wave@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:8.2
- kind: check
  ref: check.py::check_current_algebra_with_edge_operator
- kind: check
  ref: check.py::check_currents_are_weight_vectors_and_kms_restricts
- kind: check
  ref: check.py::check_planck_factor_and_role_of_q
locators:
  paper: T05
  number: Thm 8.2
  label: thm:bosonisation
  line: 2014
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version labels (DECISIONS G7; Leon''s 23 October ''note only'' decision; R01 item 2): Premise (Q) singularity.q-joint-quasi-freeness-s-wave is at version 3 with weights kappa(k + 1/2), while this entity states version 2''s weights kappa k (sea at a site); the displays now say ''version 2 of premise (Q)'' where they use kappa k. Statement content, edges and pins unchanged. The Planck value m/(e^{beta kappa m} - 1) holds at both offsets: with F(x) = (e^x + 1)^{-1}, F(x + m)(1 - F(x)) = (F(x) - F(x + m))/(e^m - 1), and the sum over x in Z + c telescopes to m for every offset c (checked by hand here; the reader''s planck_offset.py checked detailed balance and window sums exactly at both).'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the current algebra with its exact edge operator on all charge-zero states of a 10-site window, currents as weight vectors exactly for linear weights with the restricted KMS identity, and the Planck factor by detailed balance, exact telescoping and an exact tail bound, with the connected-correlator control for (Q). Version 5 -> 6. Check strengthened: k^2 control pinned hop by hop; zero-chemical-potential normalisation n_0 = 1/2 pinned; samples moved to module level. Version 6 -> 7.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: >-
      Version 4 -> 5, note only, statement and proof unchanged. Clauses (2) and (3) display the weights
      omega_k = kappa k of Premise (Q) version 2 (T05's Premise 8.1). Premise (Q) version 3 (Leon's decision
      of 23 October) takes kappa(k + 1/2). The weight difference of each bilinear is still kappa m, so (2)
      holds unchanged; the Planck occupancy of (3), m/(e^{beta kappa m} - 1), holds for every affine weight
      law (synthesis.q-splits-maximum-entropy-affine-weights (iii)), so it holds at the new offset with n_k =
      (e^{beta kappa (k + 1/2)} + 1)^{-1}. The content is unchanged; only the displayed weights refer to
      version 2.
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Clause (2) and its proof now say that the invariance of the span of the currents under the modular flow uses the weight clause of Premise (Q): each current is a weight vector only when the mode weights are affine in k (omega_k = kappa k under (Q)); the earlier text stated the invariance as if it held for any weights. (Q) was already among the assumes premises, so no edge changed. Version 3 -> 4.'
  env: theorem
  context_refs:
  - singularity.exact-equilibrium-over-determines-boundary-modes
  typing:
    by: ai-typing-pass
    removed:
    - tower.car-limit-even-charge
    - transport.transport-algorithm
    added:
    - singularity.q-joint-quasi-freeness-s-wave
    note: 'The CAR tower limit is cited only as the algebraic model of the filled-sea array (the statement
      says its provenance here is not a tower and the proof uses only the CAR), so it was removed; this
      is a judgement call. Premise (Q) is the explicit hypothesis of parts (2) and (3), so it was added
      to assumes; the over-determination theorem is cited only to explain why the joint form is rejected
      elsewhere and was not added; v2 review: removed the mechanical transport-algorithm edge, since the
      proof is a CAR computation and a KMS restriction; the boson-fermion correspondence is cited only
      for completeness and no standard derivation of the Planck factor is in the store, so no standard
      route was added. Levels pass: conditions already kept.'
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
---

## formal
Let $\{\psi_k, \psi^\dagger_k\}_{k \in \mathbb{Z}}$ be the boundary modes, as fermion operators on the filled-sea Fock space (the infinite filled-sea array whose algebraic model is the completed tower limit of \cite[Thm.~5.6]{ButlerT3}, cited for the structure; its provenance here is the s-wave aggregation declared above, not a tower, the mod-8 clock having stopped after one ascent), and define the currents $a_m := \sum_k :\psi^\dagger_k\,\psi_{k+m}:$ with $:\;:$ normal ordering at the sea level; with the sea filled below the level, $a_m$ annihilates the sea for $m > 0$ and $a_{-m} = a_m^{\dagger}$ creates particle-hole pairs. (The opposite index convention flips the sign of the central term; the verification script fixes the convention by computation.) Then:
\begin{enumerate}
\item (Current algebra.) $[a_m, a_n] = m\,\delta_{m+n,0}\,\id$ on the infinite array; on a finite window the commutator equals $m\,\delta_{m+n,0}\,\id$ plus an \emph{exactly identified} edge operator ($B_m - T_m - m$ in the proof's notation), supported on the bottom and top $m$ sites and vanishing on all bulk states: the number-conserving bilinears satisfy the canonical commutation relations of a free boson. A boson is a pair of the pair.
\item (KMS restriction.) Each bilinear $\psi^\dagger_k\psi_{k+m}$ carries a definite boost weight, fixed by the difference $\omega_{k+m} - \omega_k$ of its two modes' weights. Under (Q)'s weight clause, affine in $k$ ($\omega_k = \kappa k$ at version 2, $\kappa(k + \tfrac12)$ at version 3; the displays below use version 2's), that difference is $\kappa m$ for every $k$, so each current $a_m$ is itself a weight vector and the current subalgebra is globally invariant under the modular flow of Theorem \claimref{singularity.modular-structure-completed-pair}; for weights that are not affine in $k$ the summands of $a_m$ rotate at different rates and the span of the currents need not be invariant, so this invariance uses (Q). Under (Q) the joint state is KMS for that flow, and a KMS state restricted to a flow-invariant subalgebra is KMS at the same temperature for the restricted flow. Without (Q) no joint KMS state is available: (R) is imposed on the marginals alone, and Theorem \claimref{singularity.exact-equilibrium-over-determines-boundary-modes} is the reason its joint form is rejected elsewhere in the chain.
\item (The Planck factor.) Under (Q), with the marginal occupancies $n_k = (e^{\beta\omega_k} + 1)^{-1} = (e^{\beta\kappa k} + 1)^{-1}$ at the premise's linear weights (version 2's; at version 3's offset the sum telescopes to the same value), the current occupancy is, exactly,
\[
\langle a_{-m} a_m \rangle \;=\; \sum_{k \in \mathbb{Z}} n_{k+m}\,(1 - n_k) \;=\; \frac{m}{e^{\beta\kappa m} - 1} \qquad (m > 0) ,
\]
with no vacuum piece in this convention ($a_m$ annihilates the sea): Bose-Einstein occupancy at exactly $\TH$. The Planck spectrum of the bosonic Hawking flux is derived, not conjectured, for the s-wave sector, in the equilibrium reading (Q) fixes; for a general member of the chain's state class the left side acquires the connected correlators (Q) sets to zero, and no exact spectrum is claimed.
\end{enumerate}
The single assembly-level ingredient in the section is the charge-zero Fock isomorphism (the charge-zero sector of the fermionic Fock space is canonically the bosonic Fock space, with fermions recovered as vertex operators), cited to \cite{PressleySegal1986} and used only for the completeness statement that the two descriptions are one algebra; parts (1)-(3) are proved outright.

## technical
Take the boundary modes $\psi_k, \psi_k^\dagger$, $k \in \Z$, as fermion operators on the filled-sea Fock space, and the normal-ordered currents $a_m = \sum_k :\psi_k^\dagger \psi_{k+m}:$, so that $a_m$ annihilates the sea for $m > 0$ and $a_{-m} = a_m^\dagger$. On the infinite array $[a_m, a_n] = m\,\delta_{m+n,0}\,\id$, the free-boson relations; on a finite window the commutator differs from this by an exactly identified edge operator supported on the bottom and top $m$ sites, which vanishes on all bulk states. Each bilinear has definite boost weight, the difference of its two modes' weights; under the weight clause of Premise (Q), affine in $k$ ($\omega_k = \kappa k$ at version 2, $\kappa(k + \tfrac12)$ at version 3), that difference depends only on $m$, so each current is a weight vector and the current subalgebra is globally invariant under the modular flow (for weights not affine in $k$ it need not be).

Under Premise (Q) the joint state is KMS for that flow, so its restriction to the currents is KMS at the same temperature, and the marginal occupancies $n_k = (e^{\beta\kappa k} + 1)^{-1}$ (version 2's weights; the value is the same at version 3's) give exactly $\langle a_{-m} a_m \rangle = \sum_k n_{k+m}(1 - n_k) = m/(e^{\beta\kappa m} - 1)$ for $m > 0$: Bose-Einstein occupancy at $\TH$ for the s-wave sector. Without (Q) no joint KMS state is available, and for a general state of the class connected correlators enter and no exact spectrum is claimed.

## lay
Pairs of the fermion-like boundary modes, one created and one removed, behave exactly like a boson, apart from edge effects on any finite window that are identified precisely. If the boundary modes are assumed to be jointly in the simplest kind of thermal state, these boson-like pairs inherit the same temperature and follow the Bose-Einstein occupation law at the Hawking temperature. This derives the Planck spectrum of bosonic Hawking radiation for the spherically symmetric (s-wave) sector, under that assumption only.

## one-liner
Number-conserving bilinears of the boundary fermion modes satisfy free-boson commutation relations exactly, up to a precisely identified edge term on finite windows, and under Premise (Q) they carry Bose-Einstein occupancy at $\TH$ in the s-wave sector.
