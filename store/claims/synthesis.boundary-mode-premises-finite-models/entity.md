---
id: synthesis.boundary-mode-premises-finite-models
kind: claim
version: 4
title: 'Finite models separate the boundary-mode premises'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, car-algebra, grading-and-parity, entropy-premises]
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
  role: 'unit resolution pass, the model flows and phases written with the transverse unit J'
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
about:
- obj.singularity.grading-parity-automorphism
- obj.singularity.geometric-modular-condition-g
derivations:
- name: main
  uses:
  - hawking.imported-quasi-free-states-car-algebra@2
  - singularity.kms-uniqueness-factor@6
  - singularity.chains-state-class-stability@7
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_q_contains_p_and_r
- kind: check
  ref: check.py::check_odd_resonance_criterion
- kind: check
  ref: check.py::check_not_p_models
- kind: check
  ref: check.py::check_not_r_model
- kind: check
  ref: check.py::check_not_le_model
- kind: check
  ref: check.py::check_not_q_model
- kind: check
  ref: check.py::check_chains_needs_pairing_clause
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - singularity.p-univalence
  - singularity.r-regularity-fixed-locus
  - singularity.l-boundary-mode-locality
  - singularity.q-joint-quasi-freeness-s-wave
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U2: the finite models are windows of boundary modes, so the stationarity flow, the Killing flow, the single-mode flows, the gauge phases and the modular group are written with J = e_2 e_3, the modes'' complex unit (synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom, cited as a mention), with the matrix entries read in span{1, J}; the remaining detector hits are index letters (v_i^* v_j, omega_i). Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: Ad(e^{i t omega_k K_k}) and e^{i theta}v_k act on T05''s atoms Mat_2(C), whose modes anticommute with I_4; the index letters i, j are false positives. Declared complex-analysis.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 1 -> 2, note only, statement and proof unchanged. The examples on (Q) windows in (iii), (iv), (v) and (vii) use Premise (Q) version 2''s weights kappa k, with the zero-weight mode k = 0. Premise (Q) version 3 (Leon''s decision of 23 October) takes kappa(k + 1/2). Every odd signed sum of weights in kappa(Z + 1/2) is nonzero, so by (ii) every state on a window of the array that is stationary under the Killing flow is even: the first example of (iii), which needs the zero-weight mode, has no analogue on the array, and there (P) follows from stationarity under the Killing flow. The second example of (iii), on positive weights 1, 2, 3, still shows that (P) does not follow from (R), (L_E) and stationarity in general, so the independence statement is unchanged. The examples of (iv), (v) and (vii) were computed at kappa k and were not recomputed at the new offset, where the particle-hole partners are k and -1-k. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  open_problem: pr.minimal-premise-basis
  note: >-
    Independence by model for one block of the premise basis. The four boundary-mode premises
    are read on finite models (finitely many modes, weights, a state, a dynamics under which the
    state is stationary). (Q) implies (P) and (R); otherwise each premise fails in a model that
    satisfies the other three, or all the others it does not imply. The premises are about the
    models, not assumed by the result, so they appear as lineage rather than as assumes.
    Transport-absent: finite CAR algebra and linear algebra; the series enters through the
    premises' statements.
---

## formal
A \emph{finite boundary-mode model} is a set of $n$ modes with ladders $\{v_k, v_k^{*}\}$ generating $\CAR \cong \Mat_{2^{n}}(\C)$, real weights $\omega_k$ with Killing generator $K_{\mathrm{geo}} = \sum_k \omega_k K_k$ (the constants in $K_k = v_k^{*}v_k - \tfrac12$ drop out of every flow), a state $\omega = \tr(\varrho\,\cdot\,)$, and an even self-adjoint generator $H$ of the dynamics with $\omega \circ \Ad(e^{JtH}) = \omega$ (stationarity); the flows and phases are written with the boundary modes' complex unit $J = e_{2}e_{3}$, which commutes with every mode, and numbers, including the matrix entries of $\Mat_{2^{n}}(\C)$, are read in $\mathrm{span}\{1, J\}$ (\claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}). Read on such a model: (P) is $\omega \circ \alpha = \omega$ for the grading $\alpha = \Ad(\Gamma)$ of Definition \claimref{obj.singularity.grading-parity-automorphism}; (R) is the KMS condition of Premise \claimref{singularity.r-regularity-fixed-locus} for each single-mode marginal at $\beta = 2\pi/\kappa$, in the full reading (the marginal is the Gibbs state of $\omega_k K_k$, so also $\omega(v_k) = 0$), which contains the literal reading on ladder pairs; (L$_E$) is that $H$ lies in the algebra generated by the $v_k^{*}v_k$ (Premise \claimref{singularity.l-boundary-mode-locality}); (Q) is Premise \claimref{singularity.q-joint-quasi-freeness-s-wave}: $\omega$ is the gauge-invariant quasi-free state with diagonal symbol, KMS at $\beta$ for $K_{\mathrm{geo}}$ with $\omega_k = \kappa k$. Write $u = e^{-2\pi}$, the Boltzmann factor of one unit of weight. Then:
\begin{enumerate}
\item[(i)] (Q) implies (P) and (R). The geometric modular condition (G) of Definition \claimref{obj.singularity.geometric-modular-condition-g} also implies (P) on finitely many modes, at any weights.
\item[(ii)] (odd resonance) Every state stationary under the Killing flow $\Ad(e^{JtK_{\mathrm{geo}}})$ is even if and only if the weights have no odd signed resonance, that is no odd-size set $T$ of modes and signs $\epsilon_k = \pm 1$ with $\sum_{k \in T}\epsilon_k\omega_k = 0$. A zero-weight mode is such a resonance, as is any relation $\omega_a + \omega_b = \omega_c$. When there is one and $n \geq 2$, there are Killing-stationary odd states whose every single-mode marginal is the Gibbs state at $\beta$.
\item[(iii)] (not (P)) On the (Q) modes $k = 0, 1$ the state $\varrho_{A} = \tfrac12\id \otimes \operatorname{diag}(1, u)/(1 + u) + \tfrac{u}{4(1 + u)}\,X_0 Z_1$ (Jordan-Wigner, $X_0 = v_0 + v_0^{*}$, $Z_1 = 1 - 2v_1^{*}v_1$) is positive, stationary under $K_{\mathrm{geo}}$, satisfies (R) and (L$_E$) with $H = K_{\mathrm{geo}}$, and has $\omega(X_0 Z_1) = u/(1 + u) \neq 0$ for the odd element $X_0Z_1$. On positive weights $1, 2, 3$ the Gibbs state plus half its population times $|110\rangle\langle 001| + |001\rangle\langle 110|$ does the same, with $\omega(v_3^{*}v_2v_1) \neq 0$. So (P) does not follow from (R), (L$_E$) and stationarity.
\item[(iv)] (not (R)) On the (Q) window $k = -1, 0, 1$ the gauge-invariant quasi-free state at the doubled period, occupations $u^{2k}/(1 + u^{2k})$, is even, stationary under $K_{\mathrm{geo}}$ and violates (R) at $k = \pm 1$. So (R) does not follow from (P), (L$_E$), stationarity and quasi-freeness with (Q)'s weights.
\item[(v)] (not (L$_E$)) On the (Q) window the pairing generator $G = v_{1}v_{-1} + v_{-1}^{*}v_{1}^{*}$ is even, commutes with $K_{\mathrm{geo}}$ and with the (Q) state, and does not commute with $v_1^{*}v_1$; on the window $k = -1, 0, 1, 2$ so does the weight-conserving quartic hop $v_2^{*}v_{-1}^{*}v_1v_0 + \text{h.c.}$, which conserves number. So (L$_E$) does not follow from (P), (R), (Q) and stationarity. On the window $k = -j, \ldots, j$ the quadratic generators that leave the (Q) state stationary are exactly the span of the $v_k^{*}v_k$ and of the pairings $v_kv_{-k}$, $v_{-k}^{*}v_{k}^{*}$, $1 \leq k \leq j$: (Q) with stationarity excludes quadratic hopping, not pairing.
\item[(vi)] (not (Q)) On weights $1, 2$ the Gibbs state plus $c\,Z_0Z_1$, $c$ half the population of $|11\rangle$, is even, diagonal (so stationary under every (L$_E$) generator), satisfies (R), and has connected density correlation $c \neq 0$. So (Q) does not follow from (P), (R), (L$_E$) and stationarity.
\item[(vii)] Clause (2) of Corollary \claimref{singularity.chains-state-class-stability} needs the pairing exclusion of (L$_E$): the pairing rotation $\exp\theta(v_1^{*}v_{-1}^{*} - v_{-1}v_1)$ at $(\cos\theta, \sin\theta) = (\tfrac35, \tfrac45)$ fixes the (Q) state but maps an even state with Gibbs marginals (the (Q) state plus a pairing coherence) to one whose $k = 1$ marginal is not Gibbs.
\end{enumerate}
So in the block $\{$(P), (R), (L$_E$), (Q)$\}$ the only implications are (Q) $\Rightarrow$ (P) and (Q) $\Rightarrow$ (R): $\{$(P), (R), (L$_E$)$\}$ is an independent set, (Q) is an independent strengthening of (P) and (R), and in any derivation that assumes (Q) the premises (P) and (R) are redundant.

## technical
The four premises that govern the boundary-mode state and dynamics are tested on finite models: finitely many fermion modes with weights, a density matrix, and a dynamics under which that density matrix is stationary. Requiring stationarity links state and dynamics, so the models are not vacuous.

The store words (Q) on top of (P) and (R), as the quasi-free state with the marginal data they fix, so the first two implications are expected; read as a self-contained condition on the state, quasi-freeness with the s-wave weights, (Q), implies both univalence (P) (a gauge-invariant state is invariant under the gauge rotation by $\pi$, which is the grading) and the regularity premise (R) (the marginals of the product Gibbs state are Gibbs states). The geometric modular condition implies (P) as well, since its state is the Gibbs state of an even generator. Stationarity under the Killing flow gives (P) for free exactly when the weights have no odd signed resonance; (Q)'s weights have one (the zero mode, and relations such as $1 + 2 = 3$), and explicit odd states then satisfy (R), (L$_E$) and stationarity. A state at twice the period violates (R) and nothing else. A pairing of the modes $\pm k$ commutes with (Q)'s Killing generator, because their weights cancel, so it preserves the (Q) state while violating (L$_E$); a weight-conserving quartic hop does the same. A correlated state with Gibbs marginals violates (Q) alone. The pairing rotation that preserves the (Q) state still moves other states of the premises' class, so the stability corollary does need (L$_E$)'s pairing clause.

## lay
The series assumes four separate things about the quantum bits at a black hole's boundary: that their state never mixes even and odd particle numbers, that each bit on its own looks thermal at the Hawking temperature, that the bits evolve only by phase changes, and (for one step) that the bits are as uncorrelated as possible with a fixed energy ladder. This result asks whether any of these follows from the others. It builds small, exactly computable examples, each obeying all but one assumption, and finds that the last assumption implies the first two, while otherwise none can be dropped. One example shows that pairs of bits with opposite energies can be created and destroyed without disturbing the steady thermal state, so the ban on such pair creation is a genuine extra assumption.

## one-liner
On finite stationary models (Q) implies (P) and (R), and otherwise (P), (R), (L$_E$) and (Q) are independent: explicit exact models, including an odd stationary state at (Q)'s resonant weights and a $\pm k$ pairing that preserves the (Q) state, violate each one while satisfying the rest.
