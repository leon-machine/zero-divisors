---
id: one-relation.imported-cartans-purity-theorem-thouless-form
kind: claim
version: 1
title: 'Imported: Cartan''s purity theorem and the Thouless form'
status: imported
region: one-relation
subject: one-relation
tags: [spinor-modules, witt-index, pairing-and-bogoliubov, classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
review: typed
imported_from:
- citation: '''E. Cartan, Lecons sur la th''eorie des spineurs, Hermann (1938).'
  key: Cartan1938
- citation: C. Chevalley, The Algebraic Theory of Spinors, Columbia University Press (1954).
  key: Chevalley1954
- citation: D. J. Thouless, Stability conditions and nuclear rotations in the Hartree-Fock theory, Nucl.
    Phys. 21 (1960) 225--232.
  key: Thouless1960
locators:
  paper: T16
  number: Fact 2.10
  label: fact:cartan
  line: 542
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported classical results; levels only.
---

## formal
A Weyl spinor of $\mathrm{Spin}(2\nu, \C)$ is \emph{pure} if it is the Fock vacuum of some maximal isotropic subspace, equivalently of some Witt decomposition of $\C^{2\nu}$. Every Weyl spinor is pure for $2\nu \leq 6$; in dimension $8$ purity is one quadratic condition, the $\mathrm{Spin}(8)$-invariant form on the half-spinor space, and in higher dimension it is more. The pure spinors form a single orbit, the spinor variety, of dimension $\nu(\nu - 1)/2$. For any antisymmetric $A$, the Thouless state $\exp(\sum_{i<j}A_{ij}a^{\dagger}_{i}a^{\dagger}_{j})|0\rangle$ is the vacuum of the Witt decomposition obtained from the standard one by the corresponding Bogoliubov rotation, and every vacuum with nonzero overlap with $|0\rangle$ is of this form. \emph{Provenance:} \cite{Cartan1938, Chevalley1954} for purity and the spinor variety; \cite{Thouless1960} for the exponential form.

## technical
A Weyl spinor of $\mathrm{Spin}(2\nu, \C)$ is pure if it is the Fock vacuum of some maximal isotropic subspace. Every Weyl spinor is pure when $2\nu \leq 6$; in dimension $8$ purity is one quadratic condition, and in higher dimension it is more. The pure spinors form a single orbit, the spinor variety, of dimension $\nu(\nu - 1)/2$.

For antisymmetric $A$, the Thouless state $\exp(\sum_{i<j}A_{ij}a^{\dagger}_{i}a^{\dagger}_{j})\ket{0}$ is the vacuum of the Bogoliubov-rotated Witt decomposition, and every vacuum with nonzero overlap with $\ket{0}$ has this form. Purity and the spinor variety are imported from Cartan and Chevalley, the exponential form from Thouless.

## lay
In a system of fermion modes, some states are the empty state, or vacuum, for some way of splitting the modes into creators and annihilators; these are called pure spinors. In small systems every state of fixed parity is of this kind, while in larger ones only special states are. These classical results also give an explicit formula for all such vacua that overlap a reference one.

## one-liner
Imported from Cartan, Chevalley and Thouless: pure spinors are Witt vacua forming one orbit of dimension $\nu(\nu-1)/2$, all Weyl spinors are pure for $2\nu \leq 6$, and vacua overlapping $\ket{0}$ have the exponential Thouless form.
