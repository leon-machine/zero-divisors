---
id: correspondence.shared-core-ordering-dictionary
kind: claim
version: 4
title: "The shared core, and the ordering dictionary"
status: proved
region: correspondence
subject: conformal-spacetime
tags: [conformal-spinors, dictionaries]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
derivations:
- name: main
  uses:
  - correspondence.clifford-side-ordering-shift@3
  - correspondence.reality-conjugation-twistor-form-factor@6
  - correspondence.spin-representation@6
  - correspondence.symmetrised-quadratics-palatial-algebra@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T09.py
  tags:
  - label:thm:core
- kind: check
  ref: check.py::check_palatial_quadratics_and_u22
- kind: check
  ref: check.py::check_bivectors_act_as_sl
- kind: check
  ref: check.py::check_klein_identification_is_lie_embedding
- kind: check
  ref: check.py::check_same_ordering_shift_both_storeys
locators:
  paper: T09
  number: Thm 5.7
  label: thm:core
  line: 728
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: u(2,2) as a computed 16-dimensional real kernel containing so(2,4), the injective Lie embedding beta -> q(rho(beta))/hbar with the adjoint action on Z and Zbar, and the two ordering shifts (-2 hbar; N - 1/2 per mode). Version 3 -> 4.'
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: STRUCTURE L5
    open_problem: op.small-findings
    note: 'Clause (4) now gives the ordering shift its sign: -hbar/2 per complex dimension, -2 hbar in all, matching N - 1/2 (minus one half per mode) on the Clifford storey, as T07 Fact 2.6 restates it.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'All four edges are cited premises and were kept; the paper calls the helicity and homogeneity
      computation classical (Penrose and Rindler), but no imported claim stating it is in the store, so
      no standard route. Levels pass: lay and one-liner now state the Klein identification under which
      the two copies coincide.'
  source_title: "The shared core, and the ordering dictionary"
  source_formal: |-
    \begin{enumerate}
    \item The symmetrised quadratics of the palatial algebra close under commutator on a copy of $\mathfrak{gl}(4,\C) = \mathfrak{gl}(\T)$ (Lemma \claimref{correspondence.symmetrised-quadratics-palatial-algebra}); the anti-Hermitian part with respect to the Hermitian form $\Sigma$ of Proposition \claimref{correspondence.reality-conjugation-twistor-form-factor} is $\mathfrak{u}(2,2)$, containing $\mathfrak{su}(2,2) \cong \mathfrak{so}(2,4)$.
    \item The bivectors of $\Cl(2,4)_\C$ close under commutator on $\mathfrak{so}(2,4)_\C$ and act on $\T$ as $\mathfrak{sl}(\T)$ (Proposition \claimref{correspondence.spin-representation}).
    \item Under the Klein identification the two copies coincide, compatibly with their actions: the assignment $\beta \mapsto q(\rho(\beta))/\hbar$ is an injective Lie algebra homomorphism $\mathfrak{so}(2,4)_\C \to \mathcal{P}$, and the adjoint action of $q(\rho(\beta))/\hbar$ on the linear twistor generators is the spinor action $\rho(\beta)$ of the Clifford bivector, in the dual pair of slots of Lemma \claimref{correspondence.symmetrised-quadratics-palatial-algebra}(1) ($-\rho(\beta)$ on the $Z$ slot, its transpose on the $\bar Z$ slot).
    \item Both quantisations incur the same ordering shift of one half per dimension: on the palatial storey, symmetric ordering shifts the distinguished $\mathfrak{u}(1)$ generator by $\tfrac{\hbar}{2}$ per complex dimension of $\T$, totalling $2\hbar$ (Lemma \claimref{correspondence.symmetrised-quadratics-palatial-algebra}(3)); on the Clifford storey, the boost generator of each adjoined plane is $N - \tfrac12$: one half per fermionic mode (Proposition \claimref{correspondence.clifford-side-ordering-shift}).
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor space to the conformal spinor space \\CS and the linear twistor generators to the linear palatial generators; Penrose's palatial algebra keeps its name. The complexified $\\mathfrak{so}(2,4)_\\C$ and $\\Cl(2,4)_\\C$ are kept as in the original."
---

## formal
\begin{enumerate}
\item The symmetrised quadratics of the palatial algebra close under commutator on a copy of $\mathfrak{gl}(4,\C) = \mathfrak{gl}(\CS)$, with $\CS$ the conformal spinor space (twistor space) (Lemma \claimref{correspondence.symmetrised-quadratics-palatial-algebra}); the anti-Hermitian part with respect to the Hermitian form $\Sigma$ of Proposition \claimref{correspondence.reality-conjugation-twistor-form-factor} is $\mathfrak{u}(2,2)$, containing $\mathfrak{su}(2,2) \cong \mathfrak{so}(2,4)$.
\item The bivectors of $\Cl(2,4)_\C$ close under commutator on $\mathfrak{so}(2,4)_\C$ and act on $\CS$ as $\mathfrak{sl}(\CS)$ (Proposition \claimref{correspondence.spin-representation}).
\item Under the Klein identification the two copies coincide, compatibly with their actions: the assignment $\beta \mapsto q(\rho(\beta))/\hbar$ is an injective Lie algebra homomorphism $\mathfrak{so}(2,4)_\C \to \mathcal{P}$, and the adjoint action of $q(\rho(\beta))/\hbar$ on the linear palatial generators $Z^\alpha$, $\bar Z_\beta$ is the spinor action $\rho(\beta)$ of the Clifford bivector, in the dual pair of slots of Lemma \claimref{correspondence.symmetrised-quadratics-palatial-algebra}(1) ($-\rho(\beta)$ on the $Z$ slot, its transpose on the $\bar Z$ slot).
\item Both quantisations incur the same ordering shift of one half per dimension: on the palatial storey, symmetric ordering shifts the distinguished $\mathfrak{u}(1)$ generator by $-\tfrac{\hbar}{2}$ per complex dimension of $\CS$, totalling $-2\hbar$ (Lemma \claimref{correspondence.symmetrised-quadratics-palatial-algebra}(3)); on the Clifford storey, the boost generator of each adjoined plane is $N - \tfrac12$: minus one half per fermionic mode, the same sign (Proposition \claimref{correspondence.clifford-side-ordering-shift}).
\end{enumerate}

## technical
The symmetrised quadratics of the palatial algebra close under commutator on a copy of $\mathfrak{gl}(\CS) = \mathfrak{gl}(4,\C)$, whose $\Sigma$-anti-Hermitian part is $\mathfrak{u}(2,2)$, containing $\mathfrak{su}(2,2) \cong \mathfrak{so}(2,4)$; the bivectors of $\Cl(2,4)_\C$ close on $\mathfrak{so}(2,4)_\C$ and act on $\CS$ as $\mathfrak{sl}(\CS)$. Under the Klein identification the two copies coincide compatibly with their actions: $\beta \mapsto q(\rho(\beta))/\hbar$ is an injective Lie algebra homomorphism $\mathfrak{so}(2,4)_\C \to \mathcal{P}$ whose adjoint action on the linear palatial generators is the spinor action $\rho(\beta)$, as $-\rho(\beta)$ on the $Z$ slot and its transpose on the $\bar Z$ slot.

Both quantisations carry the same ordering shift of one half per dimension: on the palatial storey symmetric ordering shifts the distinguished $\mathfrak{u}(1)$ generator by $-\tfrac{\hbar}{2}$ per complex dimension of $\CS$, $-2\hbar$ in all, and on the Clifford storey the boost generator of each adjoined plane is $N - \tfrac12$, minus one half per fermionic mode.

## lay
Two quite different quantum structures appear in the series: a bosonic algebra of operators on the conformal spinor coordinates, from Penrose's palatial programme, and the fermionic Clifford algebra of the completion. This result shows that, once the two are matched by the Klein identification, both contain the same core, the conformal symmetry algebra of spacetime, acting on the conformal spinors in the same way. Both also show the same offset, minus one half per dimension, which on the palatial side comes from symmetric ordering and on the Clifford side from each fermionic mode.

## one-liner
Under the Klein identification, the palatial algebra's symmetrised quadratics and the Clifford bivectors share the same $\mathfrak{so}(2,4)$ core acting compatibly on conformal spinors, and both storeys carry the same signed ordering shift of minus one half per dimension.
