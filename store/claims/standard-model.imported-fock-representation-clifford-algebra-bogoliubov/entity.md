---
id: standard-model.imported-fock-representation-clifford-algebra-bogoliubov
kind: claim
version: 1
title: 'Imported: the Fock representation of a Clifford algebra, and its Bogoliubov group'
status: imported
region: standard-model
subject: one-relation
tags: [spinor-modules, pairing-and-bogoliubov, car-algebra, classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
imported_from:
- citation: 'W. Fulton and J. Harris, Representation Theory: A First Course, Graduate Texts in Mathematics
    129, Springer (1991).'
  key: FultonHarris1991
  locator: Lecture~20, \S 20.1
- citation: H. B. Lawson and M.-L. Michelsohn, Spin Geometry, Princeton University Press (1989).
  key: LawsonMichelsohn1989
  locator: Ch.~I, \S\S 2, 5
locators:
  paper: T12
  number: Fact 2.11
  label: fact:fock
  line: 919
extraction:
  env: fact
  context_refs:
  - standard-model.imported-pair-systems-two-chirality-halves
  typing:
    by: ai-typing-pass
    note: Imported textbook result; levels only.
---

## formal
Let $E$ be a complex vector space of dimension $n$ with a Hermitian inner product, and let $\Lambda^{\bullet}E$ be the Fock space of $n$ fermionic modes, with creation operators the exterior multiplications and annihilation operators the contractions. The $2n$ Majorana combinations of these operators generate an action of the complex Clifford algebra of a $2n$-dimensional orthogonal space on $\Lambda^{\bullet}E$, which is its irreducible spinor module; the parity grading $\Lambda^{\mathrm{even}} \oplus \Lambda^{\mathrm{odd}}$ is the chirality decomposition into the two half-spinor modules. The orthogonal transformations of the Majorana generators preserve the canonical anticommutation relations and are implemented on $\Lambda^{\bullet}E$ by the group $\mathrm{Pin}(2n)$, the connected component $SO(2n)$ by $\mathrm{Spin}(2n)$, which acts on each half-spinor module irreducibly for $n \ge 2$; the transformations preserving the complex structure of $E$, equivalently the mode number, form $U(n) \subset SO(2n)$, acting on $\Lambda^{\bullet}E$ as $\Lambda^{\bullet}(g)$ up to a determinant phase. For $n = 3$ this is the structure of Fact \claimref{standard-model.imported-pair-systems-two-chirality-halves}; for $n = 5$ it is $\Lambda^{\bullet}\C^{5}$ with $\mathrm{Spin}(10)$. \emph{Provenance:} \cite[Lecture~20, \S 20.1]{FultonHarris1991} for the spinor module as an exterior algebra and its half-spin decomposition; \cite[Ch.~I, \S\S 2, 5]{LawsonMichelsohn1989} for $\mathrm{Spin}(2n)$ as the double cover of $SO(2n)$ and its spin representation; the Fock-space form is the standard second-quantised reading of the same construction.

## technical
Let $E$ be an $n$-dimensional complex Hermitian space and $\Lambda^{\bullet}E$ the Fock space of $n$ fermionic modes, with creation by exterior multiplication and annihilation by contraction. The $2n$ Majorana combinations generate the complex Clifford algebra of a $2n$-dimensional orthogonal space, and $\Lambda^{\bullet}E$ is its irreducible spinor module, with $\Lambda^{\mathrm{even}} \oplus \Lambda^{\mathrm{odd}}$ the two half-spinor modules.

The orthogonal transformations of the generators are implemented by $\mathrm{Pin}(2n)$, and $SO(2n)$ by $\mathrm{Spin}(2n)$, irreducible on each half for $n \geq 2$; the mode-number-preserving ones form $U(n) \subset SO(2n)$, acting as $\Lambda^{\bullet}(g)$ up to a determinant phase. For $n = 3$ this is the pair-system structure used in the Standard-Model analysis, and for $n = 5$ it is $\Lambda^{\bullet}\C^{5}$ with $\mathrm{Spin}(10)$. The result is imported from Fulton and Harris and from Lawson and Michelsohn.

## lay
The possible states of a collection of fermions, particles like electrons that cannot share a state, can be organised as the spinor representation of a Clifford algebra. The transformations that preserve the rules fermions obey form a rotation group, and those that also keep the number of particles fixed form a unitary group. This is a standard textbook result that the series imports.

## one-liner
The Fock space $\Lambda^{\bullet}E$ of $n$ fermionic modes is the irreducible spinor module of the complex Clifford algebra on $2n$ generators, with $\mathrm{Pin}(2n)$ implementing the Bogoliubov group and $U(n)$ the number-preserving part.
