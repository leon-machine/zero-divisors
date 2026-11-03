---
id: standard-model.imported-coefficient-sum-indices
kind: claim
version: 1
title: 'Imported: the coefficient as a sum of indices'
status: imported
region: standard-model
subject: standard-model
tags: [classical-theorem, running-and-unification]
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
- citation: 'S. Weinberg, The Quantum Theory of Fields, Vol. 2: Modern Applications, Cambridge University
    Press (1996).'
  key: WeinbergQFT2
  locator: Ch.~18
locators:
  paper: T12
  number: Fact 8.1
  label: fact:index
  line: 1278
extraction:
  env: fact
  context_refs:
  - standard-model.hypercharge-global-form-pair-counting-consistency
  typing:
    by: ai-typing-pass
    note: 'Imported fact; levels only, no edges to review. Levels pass: conditions already kept.'
---

## formal
For a gauge factor $G_{i}$ with content consisting of Weyl fermions and complex scalars in representations $\rho$,
\[
b_{i} \;=\; -\tfrac{11}{3}\,C_{2}(G_{i}) \;+\; \tfrac23 \sum_{\text{Weyl}} T_{i}(\rho) \;+\; \tfrac13 \sum_{\text{scalars}} T_{i}(\rho),
\]
with $T_{i}(\rho)$ the index of $\rho$ under $G_{i}$ ($\tfrac12$ for the fundamental of $SU(N)$, $N$ for its adjoint, each weighted by the dimension of the representation's other factors), $C_{2}(SU(2)) = 2$, $C_{2}(SU(3)) = 3$, and for the abelian factor $C_{2} = 0$ and $T_{1}(\rho) = \tfrac35 \sum Y^{2}$ over the components of $\rho$. A Majorana fermion in a real representation counts as one Weyl fermion. \emph{Provenance:} \cite[Ch.~18]{WeinbergQFT2}; assembly level. With three copies of the derived generation of Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency} and one Higgs doublet the formula returns $(\tfrac{41}{10}, -\tfrac{19}{6}, -7)$, and with the minimal supersymmetric listing $(\tfrac{33}{5}, 1, -3)$; both are recomputed from the component listings by the script.

## technical
The one-loop coefficient of a gauge factor $G_{i}$ is
$b_{i} = -\tfrac{11}{3}C_{2}(G_{i}) + \tfrac23 \sum_{\text{Weyl}} T_{i}(\rho) + \tfrac13 \sum_{\text{scalars}} T_{i}(\rho)$,
with $T_{i}(\rho)$ the index ($\tfrac12$ for the fundamental of $SU(N)$, $N$ for its adjoint, weighted by the dimension of the other factors), $C_{2}(SU(2)) = 2$, $C_{2}(SU(3)) = 3$, and for the abelian factor $C_{2} = 0$ and $T_{1}(\rho) = \tfrac35 \sum Y^{2}$. A Majorana fermion in a real representation counts as one Weyl fermion.

With three generations and one Higgs doublet the formula returns $(\tfrac{41}{10}, -\tfrac{19}{6}, -7)$, and with the minimal supersymmetric content $(\tfrac{33}{5}, 1, -3)$. The formula is imported from the quantum field theory literature at assembly level.

## lay
How fast each force's strength changes with energy is set, at the first approximation, by one number per force. This standard formula builds that number from the particles present: the force carriers push one way, and fermions and scalars push the other, in proportion to how strongly each feels the force. For the Standard Model and for its simplest supersymmetric extension it gives well-known values. It is taken from the textbook literature.

## one-liner
Each one-loop gauge coefficient is $-\tfrac{11}{3}C_{2}(G_{i})$ plus two thirds of the Weyl-fermion indices plus one third of the complex-scalar indices.
