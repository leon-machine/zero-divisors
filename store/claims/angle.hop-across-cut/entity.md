---
id: angle.hop-across-cut
kind: claim
version: 5
title: A hop across the cut
status: proved
region: angle
subject: thermality
tags: [finite-models, entanglement]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-angle, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - singularity.class-relative-no-go-no-supplied@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_spectrum_and_unique_ground_state
- kind: check
  ref: check.py::check_generator_outside_supplied_class
- kind: check
  ref: check.py::check_parity_and_marginals
- kind: check
  ref: check.py::check_boost_eigenvector_statements
locators:
  paper: T05-angle
  number: Prop 4.2
  label: prop:hop
  line: 180
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: spectrum, unique ground state 3/5|10> + 4/5|01>, parity, marginals at 9/16, the boost eigenvector statements, and the hop outside the supplied class. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: STRUCTURE L9
    open_problem: op.small-findings
    note: 'An odd vector of definite parity defines an even state (its expectation vanishes on the odd sector), which is what T05 Premise 7.8 (P) requires; the wording now says that the state it defines is even, so it no longer reads against (P).'
  source_formal: 'On two modes, let $H = 7N_{0} - 12(a^{\dagger}_{0}a_{1} + a^{\dagger}_{1}a_{0})$, the second quantisation of the one-particle operator $\begin{psmallmatrix} 7 & -12 \\ -12 & 0\end{psmallmatrix}$, which is not in the supplied class.
\begin{enumerate}
\item[(i)] $H$ is Hermitian and conserves the total number; its spectrum is $0$ on $\ket{00}$, $7$ on $\ket{11}$, and $16, -9$ on the one-particle sector, so its ground state is unique: $\psi = \tfrac35\ket{10} + \tfrac45\ket{01}$ with eigenvalue $-9$.
\item[(ii)] $\psi$ is odd, hence of definite parity and physical under the univalence rule, and entangled across the cut: its left marginal is $\operatorname{diag}(\tfrac{16}{25}, \tfrac{9}{25})$, the Gibbs state for $N_{0}$ at $e^{-\omega/T} = \tfrac{9}{16}$, the singularity paper''s sample point, and its right marginal is $\operatorname{diag}(\tfrac{9}{25}, \tfrac{16}{25})$.
\item[(iii)] $\psi$ is an eigenvector of $N_{0} + N_{1}$ and not of $N_{0} - N_{1}$: it is invariant under the boost flow in which the two modes have equal frequency, and not under the number-difference boost of the vacuum form.
\end{enumerate}'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'No edges: the singularity paper''s sample point and the univalence rule are cited for comparison
      and vocabulary only; the proof is a self-contained finite computation. Levels pass: conditions already
      kept.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - singularity.class-relative-no-go-no-supplied
    added_dependants:
    - angle.hop-sea-filled-pairing
    added_about: []
    verdict: connected
    note: The clause that the hop is not in the supplied class rests on the singularity paper's ultralocality
      theorem; the sample point and the univalence rule remain vocabulary.
  flow_note: phase flow e^{-i omega t} on the modes (T05 Thm 7.16, T07 Def 2.7), the Euclidean rotation
    of T05 Prop 7.21. 'The boost flow in which the two modes have equal frequency' is the phase flow generated
    by N_0 + N_1; the eigenvector condition that makes psi invariant is the same for the rotor flow of that
    generator.
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 4
    note: 'The two boost flows: flow_note recorded.'
---

## formal
On two modes, let $H = 7N_{0} - 12(a^{\dagger}_{0}a_{1} + a^{\dagger}_{1}a_{0})$, the second quantisation of the one-particle operator $\begin{psmallmatrix} 7 & -12 \\ -12 & 0\end{psmallmatrix}$, which is not in the supplied class.
\begin{enumerate}
\item[(i)] $H$ is Hermitian and conserves the total number; its spectrum is $0$ on $\ket{00}$, $7$ on $\ket{11}$, and $16, -9$ on the one-particle sector, so its ground state is unique: $\psi = \tfrac35\ket{10} + \tfrac45\ket{01}$ with eigenvalue $-9$.
\item[(ii)] $\psi$ is an odd vector, hence of definite parity, so the state it defines is even (it vanishes on the odd sector) and is physical under the univalence rule, and entangled across the cut: its left marginal is $\operatorname{diag}(\tfrac{16}{25}, \tfrac{9}{25})$, the Gibbs state for $N_{0}$ at $e^{-\omega/T} = \tfrac{9}{16}$, the singularity paper's sample point, and its right marginal is $\operatorname{diag}(\tfrac{9}{25}, \tfrac{16}{25})$.
\item[(iii)] $\psi$ is an eigenvector of $N_{0} + N_{1}$ and not of $N_{0} - N_{1}$: it is invariant under the boost flow in which the two modes have equal frequency, and not under the number-difference boost of the vacuum form.
\end{enumerate}

## technical
On two fermionic modes, the generator $H = 7N_{0} - 12(a^{\dagger}_{0}a_{1} + a^{\dagger}_{1}a_{0})$ contains a hop, a term that moves occupation between the modes, so it lies outside the supplied class of number-diagonal generators. It is Hermitian and conserves the total number. The vacuum $\ket{00}$ and the filled state $\ket{11}$ have energies $0$ and $7$, and the one-particle block has eigenvalues $16$ and $-9$, so the ground state is unique: $\psi = \tfrac35\ket{10} + \tfrac45\ket{01}$ at energy $-9$.

The vector $\psi$ is odd, so it has definite parity; the state it defines is therefore even and physical under the univalence rule, and it is entangled across the cut. Its left marginal is $\operatorname{diag}(\tfrac{16}{25}, \tfrac{9}{25})$, the Gibbs state for $N_{0}$ at Boltzmann factor $e^{-\omega/T} = \tfrac{9}{16}$, and its right marginal is $\operatorname{diag}(\tfrac{9}{25}, \tfrac{16}{25})$. It is an eigenvector of $N_{0} + N_{1}$ but not of $N_{0} - N_{1}$: it is invariant under the boost flow in which the two modes have equal frequency, and not under the number-difference boost of the vacuum form.

## lay
Take a toy model with one fermion mode on each side of a horizon, and add a term that lets a particle hop from one side to the other. The lowest-energy state is then unique and is shared between the two sides, rather than having each side definitely full or definitely empty. Seen from one side alone it looks thermal, at exactly the sample temperature used in the earlier analysis of the singularity.

## one-liner
A two-mode generator with a hop across the cut has a unique, odd, entangled ground state whose left marginal is Gibbs for $N_{0}$ at the sample point $e^{-\omega/T} = \tfrac{9}{16}$.
