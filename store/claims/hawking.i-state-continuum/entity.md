---
id: hawking.i-state-continuum
kind: claim
version: 5
title: The I-state on the continuum
status: proved
region: hawking
subject: thermality
tags: [modular-theory, car-algebra, limits]
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
about:
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics
- obj.hawking.continuum-mode-space
derivations:
- name: main
  uses:
  - hawking.i-state@3
  - hawking.imported-quasi-free-kms-reduces-two@2
  - hawking.imported-quasi-free-states-car-algebra@2
  - hawking.imported-ideal-fermi-gas-uniqueness@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_fermi_dirac_quasi_free_state_is_kms
- kind: check
  ref: check.py::check_pairing_of_kms_state_vanishes
- kind: check
  ref: check.py::check_two_point_kms_forces_the_fermi_dirac_symbol
locators:
  paper: T07
  number: Thm 4.2
  label: thm:continuum
  line: 539
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: window case: the Fermi-Dirac quasi-free state is the Gibbs state and KMS, the pairing vanishes, and the two-point KMS identity forces the symbol. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  env: theorem
  context_refs:
  - hawking.full-uniqueness-given-dynamics
  - hawking.imported-ideal-fermi-gas-uniqueness
  typing:
    by: ai-typing-pass
    added:
    - hawking.imported-ideal-fermi-gas-uniqueness
    - obj.hawking.continuum-mode-space
    note: Added the imported Fermi-gas uniqueness, on which the closing all-states clause rests, and the
      continuum mode space definition to about; the full-uniqueness corollary is cited as the countable-mode
      analogue and is not used as a premise.
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    stated_role:
    - hawking.imported-ideal-fermi-gas-uniqueness
---

## formal
For the continuum mode space at $\beta = 2\pi/\kappa$, with $h$ self-adjoint:
\begin{enumerate}
\item the quasi-free state $\omega_I$ with symbol $A_I = (1 + e^{\beta h})^{-1}$ is $\tau$-KMS at $\beta$: the two-point KMS identity is the computation of clause (3) run in reverse on the core, and Fact \claimref{hawking.imported-quasi-free-kms-reduces-two} lifts it from the two-point level to the state. When $h$ has pure point spectrum, the finite spectral windows (spans of finitely many eigenvectors) are literal instances of Section \ref{sec:state}'s exact window theorem, proved outright; this is the case of the tower's mode space, Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics};
\item the pairing of any quasi-free $\tau$-KMS state vanishes, by the computation of Theorem \claimref{hawking.i-state}(2) performed on the core of clause (3);
\item the symbol derivation holds verbatim on the core: for $f$ in a bounded spectral subspace of $h$ (their union over cut-offs is a dense, $\tau$-invariant core on which $e^{-\beta h}f$ is defined and $a^\dagger(f)$ is entire analytic for $\tau$), the KMS identity forces $\ip{g}{A(1 + e^{-\beta h})f} = \ip{g}{e^{-\beta h}f}$, hence $A = A_I$ on the core and, $A$ and $A_I$ both bounded, everywhere: within the quasi-free class the continuum I-state is unique with derived two-point data. ($e^{-\beta h}$ may be unbounded when $h$ is unbounded below; the identity is only ever used on the core, and $A_I$ is bounded for every self-adjoint $h$.)
\end{enumerate}
Fact \claimref{hawking.imported-ideal-fermi-gas-uniqueness} is stated for general self-adjoint $h$, so Corollary \claimref{hawking.full-uniqueness-given-dynamics} also holds verbatim for the continuum mode space: among all states, $\omega_I$ is the unique $\tau$-KMS state.

## technical
Let $\mathfrak{h}$ be a separable one-particle space with self-adjoint $h$, $\CAR(\mathfrak{h})$ the continuum mode algebra with the quasi-free dynamics $\tau$, and $\beta = 2\pi/\kappa$. The quasi-free state $\omega_{I}$ with symbol $A_{I} = (1 + e^{\beta h})^{-1}$ is $\tau$-KMS at $\beta$; when $h$ has pure point spectrum, its finite spectral windows are instances of the exact window theorem, as for the tower's mode space.

Any quasi-free $\tau$-KMS state has vanishing pairing, and on the dense $\tau$-invariant core of bounded spectral subspaces the KMS identity forces its symbol to equal $A_{I}$, so within the quasi-free class the continuum I-state is unique. Because the imported ideal-Fermi-gas uniqueness theorem holds for general self-adjoint $h$, $\omega_{I}$ is also the unique $\tau$-KMS state among all states.

## lay
The earlier result about the horizon's equilibrium state was proved for a countable list of modes. This result carries it over to a continuous range of frequencies, as real radiation needs. The same thermal state, at the Hawking temperature, is again the only equilibrium state, and the energies need not be positive for this to hold.

## one-liner
On the continuum mode space at $\beta = 2\pi/\kappa$, for any self-adjoint $h$, the quasi-free state with symbol $(1 + e^{\beta h})^{-1}$ is $\tau$-KMS and is the unique $\tau$-KMS state.
