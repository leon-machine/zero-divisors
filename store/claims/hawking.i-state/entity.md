---
id: hawking.i-state
kind: claim
version: 3
title: The I-state
status: proved
region: hawking
subject: thermality
tags: [modular-theory, car-algebra, recovers-known-physics, forcing-and-uniqueness]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
review: typed
outside_ga:
  kind: complex-analysis
  why: 'the KMS continuation alpha_{i beta} is taken in the boundary-mode algebra, which its definition builds over the complex numbers (windows End(Lambda C^F)); its modes descend from the atom of the spacetime radial plane, with which I_4 anticommutes (conventions, known limits 1 and 2), so I_4 is not shown to be that algebra''s unit'
about:
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics
derivations:
- name: main
  uses:
  - hawking.gibbs-states-are-kms-conversely-finite@2
  - hawking.imported-kms-passes-inductive-limits@1
  - hawking.imported-quasi-free-states-car-algebra@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T07.py
  tags:
  - label:thm:istate
- kind: check
  ref: check.py::check_window_gibbs_fd_kms_quasifree_consistent
- kind: check
  ref: check.py::check_full_kms_forces_gibbs_gauge_invariance_and_fd_symbol
- kind: check
  ref: check.py::check_one_particle_kms_symbol_and_pairing
locators:
  paper: T07
  number: Thm 3.6
  label: thm:istate
  line: 485
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: alpha_{i beta} in the proof is the KMS continuation in the complex boundary-mode algebra of T07 Def 2.7, whose unit the store does not identify with I_4 (conventions, known limits 1 and 2); the formal-level "i.e." is a false positive. Declared complex-analysis; left for Leon to rule with the definition.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the FD product state equals the window Gibbs matrix, is KMS on all matrix-unit pairs, quasi-free and window-consistent; the full KMS system forces the Gibbs state, zero pairing and the FD symbol; at one-particle level (1 - A)E = A and PE = -P force A = E(1 + E)^{-1} and P = 0. Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'All three uses are genuine premises: the Gibbs lemma for window KMS, the inductive-limit fact for the full algebra, and the quasi-free fact for the window product state and for determination by two-point data.'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - $\alpha_{i\beta}$ in the KMS identity (complex analysis)
  flow_note: phase flow e^{-i omega t} on the modes (T05 Thm 7.16, T07 Def 2.7), the Euclidean rotation
    of T05 Prop 7.21. It is stated for the boost dynamics of T07 Def 2.7, tau_t(a_j) = e^{-i omega_j t}
    a_j, and the I-state is KMS for that flow.
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 4
    note: 'The two boost flows: flow_note recorded; lay now name the flow.'
---

## formal
Consider the boundary-mode algebra with its boost dynamics (Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics}) at inverse temperature $\beta = 1/\TH = 2\pi/\kappa$.
\begin{enumerate}
\item \emph{(Existence, exactly on windows.)} The quasi-free state $\omega_I$ with the Fermi-Dirac symbol
\[
A_I \;=\; \bigl(1 + e^{\beta h}\bigr)^{-1}, \qquad\text{i.e.}\qquad n_j = \frac{1}{e^{\omega_j/\TH} + 1},
\]
restricts on every window to the Gibbs state of $H_F = \sum_{j \in F}\omega_j N_j$ and is KMS there, exactly (Lemma \claimref{hawking.gibbs-states-are-kms-conversely-finite}); it is the unique quasi-free extension of these window states, and it is $\tau$-KMS at $\beta$ on the full algebra by Fact \claimref{hawking.imported-kms-passes-inductive-limits}.
\item \emph{(Gauge invariance is forced.)} If a quasi-free state of $\mathfrak{A}$ is $\tau$-KMS at $\beta$, its pairing vanishes: the state is gauge-invariant automatically.
\item \emph{(The symbol is derived.)} Its symbol then satisfies the operator identity $A(1 + e^{-\beta h}) = e^{-\beta h}$, equivalently $A = e^{-\beta h}(1 - A)$, whence $A = A_I$: within the quasi-free class, the state whose modular clock is the geometry's clock is unique, and its two-point data are forced.
\end{enumerate}

## technical
Take the boundary-mode algebra $\mathfrak{A}$ with its boost dynamics $\tau$ at $\beta = 1/\TH = 2\pi/\kappa$. The quasi-free state $\omega_I$ with Fermi-Dirac symbol $A_I = (1+e^{\beta h})^{-1}$, that is occupancies $n_j = 1/(e^{\omega_j/\TH}+1)$, restricts on every window $F$ to the Gibbs state of $H_F = \sum_{j\in F}\omega_j N_j$ and is KMS there exactly; it is the unique quasi-free extension of these window states, and it is $\tau$-KMS at $\beta$ on the whole algebra.

Within the quasi-free class the converse holds. Applying the KMS identity to two creation operators shows that the pairing vanishes, so a quasi-free $\tau$-KMS state at $\beta$ is automatically gauge-invariant. Applying it to a creation and an annihilation operator, with the CAR, gives $A(1+e^{-\beta h}) = e^{-\beta h}$, hence $A = A_I$: the two-point data are forced, and $\omega_I$ is the unique quasi-free state whose modular clock is the geometry's clock.

## lay
The boundary modes in this black-hole setting can be placed in a thermal state at the Hawking temperature, each mode filled according to the Fermi-Dirac rule. This result shows that this state exists and is thermal in the precise algebraic sense, both on every finite set of modes and on the whole system. It also shows that among the simple Gaussian (quasi-free) states it is the only one that is thermal for the geometry's boost time evolution, which turns the phase of each mode at its own frequency, so its occupation numbers are derived rather than chosen.

## one-liner
At the Hawking temperature the Fermi-Dirac quasi-free state on the boundary-mode algebra is KMS for the boost dynamics, and it is the only quasi-free state that is, with gauge invariance and its symbol both forced.
