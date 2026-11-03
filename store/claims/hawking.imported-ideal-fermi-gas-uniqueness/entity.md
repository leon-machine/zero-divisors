---
id: hawking.imported-ideal-fermi-gas-uniqueness
kind: claim
version: 2
title: 'Imported: ideal-Fermi-gas uniqueness'
status: imported
region: hawking
subject: descent
tags: [classical-theorem, modular-theory, car-algebra]
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
imported_from:
- citation: O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd
    ed., Springer, Berlin (1997).
  key: BratteliRobinson1997
  locator: Ex.~5.3.2 and \S 5.3
- citation: H. Araki, On quasifree states of CAR and Bogoliubov automorphisms, Publ. RIMS Kyoto Univ.
    6 (1971), 385--442.
  key: Araki1971
about:
- obj.hawking.continuum-mode-space
locators:
  paper: T07
  number: Fact 3.7
  label: fact:fermigas
  line: 513
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: imported with provenance (Bratteli-Robinson, Araki); levels written, nothing else changed.
---

## formal
For the CAR algebra over a one-particle space with self-adjoint $h$ and the induced quasi-free dynamics, the $\beta$-KMS state is unique and equals the quasi-free state with symbol $(1 + e^{\beta h})^{-1}$. \emph{Provenance:} \cite[Ex.~5.3.2 and \S 5.3]{BratteliRobinson1997}; the quasi-free calculus is \cite{Araki1971}.

## technical
For the CAR algebra over a one-particle space with self-adjoint one-particle Hamiltonian $h$ and the induced quasi-free dynamics, the $\beta$-KMS state is unique and is the quasi-free state with symbol $(1 + e^{\beta h})^{-1}$, the Fermi-Dirac distribution. This is the ideal-Fermi-gas result of Bratteli and Robinson, with Araki's quasi-free calculus.

## lay
For a gas of non-interacting fermions with a given energy rule, there is exactly one equilibrium state at each temperature, and its occupation numbers follow the Fermi-Dirac law. This is a textbook result of quantum statistical mechanics.

## one-liner
For free fermions with quasi-free dynamics the $\beta$-KMS state is unique and is the quasi-free state with Fermi-Dirac symbol $(1 + e^{\beta h})^{-1}$.
