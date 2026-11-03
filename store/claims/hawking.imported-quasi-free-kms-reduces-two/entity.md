---
id: hawking.imported-quasi-free-kms-reduces-two
kind: claim
version: 2
title: 'Imported: quasi-free KMS reduces to the two-point level'
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
- citation: H. Araki, On quasifree states of CAR and Bogoliubov automorphisms, Publ. RIMS Kyoto Univ.
    6 (1971), 385--442.
  key: Araki1971
- citation: O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd
    ed., Springer, Berlin (1997).
  key: BratteliRobinson1997
  locator: \S 5.3
about:
- obj.hawking.continuum-mode-space
locators:
  paper: T07
  number: Fact 3.5
  label: fact:twopoint
  line: 481
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: imported with provenance (Araki, Bratteli-Robinson); levels written, nothing else changed.
---

## formal
For the CAR algebra over a one-particle space with the quasi-free dynamics of a self-adjoint one-particle Hamiltonian, a gauge-invariant quasi-free state is KMS at $\beta$ if and only if its two-point function satisfies the two-point KMS identity: through the Wick-determinant structure, the analytic-continuation requirement for products of generators reduces to the two-point level. \emph{Provenance:} Araki \cite{Araki1971}; \cite[\S 5.3]{BratteliRobinson1997}.

## technical
For the CAR algebra over a one-particle space with the quasi-free dynamics of a self-adjoint one-particle Hamiltonian, a gauge-invariant quasi-free state is KMS at $\beta$ if and only if its two-point function satisfies the two-point KMS identity. Through the Wick-determinant structure of quasi-free states, the analytic-continuation requirement on products of generators reduces to the two-point level.

## lay
For free fermions in the simplest class of states, checking thermal equilibrium needs only the two-particle correlations, because all higher correlations are built from them. This is a standard result of quantum statistical mechanics.

## one-liner
A gauge-invariant quasi-free CAR state is KMS for quasi-free dynamics exactly when its two-point function satisfies the two-point KMS identity.
