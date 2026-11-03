---
id: descent-lift.imported-stinespring-kraus-choi
kind: claim
version: 1
title: 'Imported: Stinespring, Kraus, Choi'
status: imported
region: descent-lift
subject: descent
tags: [classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-descent-lift, the series'' standard disclaimer'
review: typed
imported_from:
- citation: W. F. Stinespring, Positive functions on $C^*$-algebras, Proc. Amer. Math. Soc. 6 (1955) 211--216.
  key: Stinespring1955
- citation: 'K. Kraus, States, Effects, and Operations: Fundamental Notions of Quantum Theory, Lecture
    Notes in Physics 190, Springer (1983).'
  key: Kraus1983
- citation: M.-D. Choi, Completely positive linear maps on complex matrices, Linear Algebra Appl. 10 (1975)
    285--290.
  key: Choi1975
locators:
  paper: T05-descent-lift
  number: Fact 1.3
  label: fact:stinespring
  line: 159
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: imported with provenance (Stinespring, Kraus, Choi); levels written, nothing else changed.
---

## formal
A completely positive trace-preserving map $\Phi$ on the operators of a finite-dimensional space $H$ has a Kraus form $\Phi(\rho) = \sum_{k} K_{k}\rho K_{k}^{\dagger}$, and a dilation: an isometry $W : H \to H \otimes H_{R}$ with $\Phi(\rho) = \Tr_{R}(W\rho W^{\dagger})$, given by $W\psi = \sum_{k} K_{k}\psi \otimes \ket{k}$ for an orthonormal family $\ket{k}$ of $H_{R}$. The minimal number of Kraus operators, and the minimal dimension of $H_{R}$, is the rank of the Choi matrix $\sum_{ij}\Phi(\ket{i}\bra{j}) \otimes \ket{i}\bra{j}$; every dilation is the minimal one followed by an isometry on the environment, so every dilation has the form $W = \sum_{k} K_{k} \otimes \ket{r_{k}}$ with the $\ket{r_{k}}$ orthonormal and the $K_{k}$ a Kraus family of $\Phi$. \emph{Provenance:} \cite{Stinespring1955, Kraus1983, Choi1975}.

## technical
A completely positive trace-preserving map $\Phi$ on the operators of a finite-dimensional space $H$ has a Kraus form $\Phi(\rho) = \sum_{k}K_{k}\rho K_{k}^{\dagger}$ and a dilation, the isometry $W\psi = \sum_{k}K_{k}\psi\otimes\ket{k}$ with $\Phi(\rho) = \Tr_{R}(W\rho W^{\dagger})$.

The minimal number of Kraus operators, equal to the minimal environment dimension, is the rank of the Choi matrix $\sum_{ij}\Phi(\ket{i}\bra{j})\otimes\ket{i}\bra{j}$. Every dilation is the minimal one followed by an isometry on the environment, so every dilation has the form $W = \sum_{k}K_{k}\otimes\ket{r_{k}}$ with orthonormal $\ket{r_{k}}$ and a Kraus family $K_{k}$ of $\Phi$.

## lay
Any physically allowed quantum process can be viewed as a reversible interaction with an environment that is afterwards ignored. The smallest environment that does the job is fixed by a single matrix built from the process, and every other way of doing it is that smallest one with extra room added. These are the classical theorems of Stinespring, Kraus and Choi.

## one-liner
Every completely positive trace-preserving map has a Kraus form and an isometric dilation, the minimal environment dimension is the Choi rank, and every dilation is a Kraus family paired with orthonormal environment states.
