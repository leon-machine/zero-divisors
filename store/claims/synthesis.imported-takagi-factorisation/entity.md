---
id: synthesis.imported-takagi-factorisation
kind: claim
version: 1
title: 'Imported: the Autonne-Takagi factorisation'
status: imported
region: synthesis
subject: generations
tags: [classical-theorem, flavour-and-mixing]
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd ed., Cambridge University Press (2013).'
  key: HornJohnson
  locator: 'Corollary 4.4.4'
extraction:
  note: >-
    Imported so that synthesis.complex-neutrino-stages-keep-the-solar-sum-rule and
    synthesis.circulant-charged-leptons-excluded-with-real-neutrino-sectors can pin the
    factorisation that defines the light neutrino states of a complex symmetric mass matrix. Checked
    on 2026-11-01 against lecture notes on Horn and Johnson, Chapter 4 (KTH, "Hermitian and
    symmetric matrices, congruence"): the statement A = U Sigma U^T for complex symmetric A, U
    unitary, Sigma real nonnegative diagonal, the sigma_i the square roots of the eigenvalues of A
    conj(A), and the columns of U orthonormal eigenvectors of A conj(A). The corollary number in
    Horn and Johnson (2nd ed.) is cited from memory; the notes did not give it. Autonne 1915 and
    Takagi 1925 as originators are named from memory.
    The complex numbers are those of the imported matrix theorem (a number convention), not the field theory's unit.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Leon approved the import of the Takagi factorisation as a routine Fact).'
---

## formal
Let $A$ be a complex $n \times n$ matrix with $A^{\mathsf T} = A$. Then $A = U\Sigma U^{\mathsf T}$ with $U$ unitary and $\Sigma = \mathrm{diag}(\sigma_{1}, \dots, \sigma_{n})$ real and nonnegative; the $\sigma_{i}$ are the singular values of $A$, the square roots of the eigenvalues of $A\bar{A} = AA^{\dagger}$, and the columns of $U$ (the Takagi vectors) are orthonormal eigenvectors of $AA^{\dagger}$, fixed up to a sign for a simple nonzero $\sigma_{i}$ and up to a real orthogonal change of basis within a degenerate one. For a symmetric mass matrix $M$ in a Lagrangian term $\tfrac12\psi^{\mathsf T}M\psi$ the masses are the $\sigma_{i}$ and the mass states are the Takagi vectors. Here the complex numbers are those of the imported mass matrices. \emph{Provenance:} \cite[Cor.~4.4.4]{HornJohnson}.

## technical
A complex symmetric matrix, such as a Majorana neutrino mass matrix, is diagonalised not by a unitary similarity but by a unitary congruence, $U^{\mathsf T}$ on one side and $U$ on the other. The diagonal entries can be taken real and nonnegative and are then the singular values. The vectors that do it are eigenvectors of the Hermitian matrix $AA^{\dagger}$; for a real symmetric matrix they are its real eigenvectors, with a factor $i$ on those of negative eigenvalue.

## lay
A standard theorem of matrix algebra says how to find the masses and the mass states when the masses of neutral particles are described by a symmetric table of complex numbers: the masses are the table's singular values, and the states are found from an associated table that is easier to handle.

## one-liner
A complex symmetric $A$ is $U\Sigma U^{\mathsf T}$, $U$ unitary, $\Sigma \ge 0$ the singular values, the columns of $U$ eigenvectors of $AA^{\dagger}$ (Takagi; Horn and Johnson, Cor. 4.4.4).
