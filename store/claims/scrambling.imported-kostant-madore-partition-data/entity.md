---
id: scrambling.imported-kostant-madore-partition-data
kind: claim
version: 1
title: 'Imported: Kostant, Madore, and the $\mathfrak{sl}_2$ partition data'
status: imported
region: scrambling
subject: entropy
tags: [classical-theorem, representation-theory, classification]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
review: typed
imported_from:
- citation: J. Madore, The fuzzy sphere, Class. Quantum Grav. 9 (1992), 69--87.
  key: Madore1992
- citation: B. Kostant, The principal three-dimensional subgroup and the Betti numbers of a complex simple
    Lie group, Amer. J. Math. 81 (1959), 973--1032.
  key: Kostant1959
locators:
  paper: T08
  number: Fact 5.3
  label: fact:kostant
  line: 863
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported Fact with no edges; levels explain the classical results it imports.
---

## formal
(i) Embeddings of $\mathfrak{sl}_2$ into $\mathfrak{gl}_n$ are classified, up to conjugation, by the partition of $n$ given by the restriction of the defining representation; the \emph{principal} embedding is the one with a single part (the irreducible $n$-dimensional representation), and it is essentially unique. (ii) For the principal embedding the adjoint decomposition of $\Mat_n$ is multiplicity-free: $\Mat_n \cong \bigoplus_{\ell=0}^{n-1}(2\ell + 1)$, one spin-$\ell$ multiplet for each $\ell < n$ (Kostant). (iii) $\Mat_n$ with this $\mathfrak{su}(2)$ structure is Madore's fuzzy sphere, whose large-$n$ limit is the round $S^2$ \cite{Madore1992}, radius excluded: the radius is scale. \emph{Provenance:} \cite{Kostant1959} (the principal three-dimensional subgroup and the multiplicity-free adjoint decomposition) and \cite{Madore1992} (the fuzzy sphere and its large-$n$ limit); the $\mathfrak{sl}_2$ classification is classical representation theory.

## technical
Embeddings of $\mathfrak{sl}_2$ into $\mathfrak{gl}_n$ are classified up to conjugation by partitions of $n$, read off from how the defining representation splits; the principal embedding is the one with a single part, the irreducible $n$-dimensional representation, and it is essentially unique. For it the adjoint decomposition is multiplicity-free, $\Mat_n \cong \bigoplus_{\ell=0}^{n-1}(2\ell+1)$, one spin-$\ell$ multiplet for each $\ell < n$ (Kostant).

With this $\mathfrak{su}(2)$ structure, $\Mat_n$ is Madore's fuzzy sphere, whose large-$n$ limit is the round $S^2$; the radius is not fixed by the algebra and is a separate scale.

## lay
There are several ways to make matrices of a given size behave like rotations, and they are labelled by ways of splitting the size into smaller pieces. The principal way uses no splitting at all. Then the matrices form a fuzzy sphere, a finite approximation to an ordinary sphere that becomes the round sphere as the matrices grow. These are established results of Kostant and Madore.

## one-liner
Embeddings of $\mathfrak{sl}_2$ in $\mathfrak{gl}_n$ are classified by partitions of $n$; the principal one decomposes $\Mat_n$ without multiplicity and makes it Madore's fuzzy sphere, tending to the round $S^2$.
