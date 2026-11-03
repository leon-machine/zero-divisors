---
id: hawking.imported-quasi-free-states-car-algebra
kind: claim
version: 2
title: 'Imported: quasi-free states of the CAR algebra'
status: imported
region: hawking
subject: thermality
tags: [classical-theorem, car-algebra]
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
  locator: \S 5.2
about:
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics
locators:
  paper: T07
  number: Fact 3.3
  label: fact:quasifree
  line: 473
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: 'Imported fact with no derivation; nothing to edge.'
---

## formal
For every operator $A$ on $\ell^2(J)$ with $0 \le A \le 1$ (the \emph{symbol}) there is a unique gauge-invariant state $\omega_A$ on $\mathfrak{A}$ with two-point function $\omega_A(a^\dagger(f)\,a(g)) = \ip{g}{Af}$ and all higher truncated functions zero (Wick determinants). More generally, a quasi-free state (all truncated functions beyond second order vanishing) is determined by its full two-point data, the symbol together with the pairing $P(f, g) := \omega(a^\dagger(f)\,a^\dagger(g))$, and gauge invariance is exactly $P = 0$. On a finite window with diagonal symbol this is the explicit product state $\bigotimes_j \rho_j$, $\rho_j = \mathrm{diag}(1 - n_j,\, n_j)$ in the occupation basis, which the script realises exactly. \emph{Provenance:} Araki \cite{Araki1971}; \cite[\S 5.2]{BratteliRobinson1997}.

## technical
For every operator $A$ on $\ell^2(J)$ with $0 \le A \le 1$ there is a unique gauge-invariant state $\omega_A$ on the CAR algebra $\mathfrak{A}$ with two-point function $\omega_A(a^\dagger(f)\,a(g)) = \ip{g}{Af}$ and all higher truncated functions zero, so that the higher correlators are Wick determinants. More generally, a quasi-free state is determined by its symbol together with its pairing $P(f,g) = \omega(a^\dagger(f)\,a^\dagger(g))$, and gauge invariance is exactly $P = 0$.

On a finite window with diagonal symbol the state is the explicit product $\bigotimes_j \rho_j$ with $\rho_j = \mathrm{diag}(1-n_j,\, n_j)$ in the occupation basis. This is standard material, imported from the literature.

## lay
For fermions there is a class of especially simple states, called quasi-free, in which every correlation is fixed by the two-point correlations alone. This imported result says that each admissible choice of occupation data gives exactly one such state that is invariant under phase rotations, and that a quasi-free state is invariant in this way exactly when a certain pairing term vanishes. On finitely many modes with no mixing these states simply occupy each mode independently.

## one-liner
Each symbol $0 \le A \le 1$ determines a unique gauge-invariant quasi-free state of the CAR algebra; quasi-free states are fixed by their symbol and pairing, and gauge invariance is the vanishing of the pairing.
