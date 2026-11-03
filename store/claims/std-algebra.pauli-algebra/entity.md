---
id: std-algebra.pauli-algebra
kind: claim
version: 1
title: 'The Pauli algebra: Cl(3,0) and 2 x 2 complex matrices'
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- dictionaries
- pseudoscalar-and-centre
- clifford-classification
proposed_by:
  kind: ai
  session: algebra-core-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: typed
trust: ai-proposed
about:
- obj.std-algebra.clifford-algebra
derivations:
- name: main
  uses:
  - std-algebra.existence-uniqueness@1
  - std-algebra.blade-basis@1
  - primer.centre@2
  - primer.sign@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_pauli_reading_and_the_pseudoscalar
locators:
  sources:
  - key: DoranLasenby2003
    locator: Ch. 2 (geometric algebra in two and three dimensions)
  - key: Lounesto2001
    locator: Ch. 16 (matrix representations and periodicity of 8)
extraction:
  by: algebra-core-2026-10-26
---

## formal
$\Cl(3,0) \cong \Mat_2(\C)$ by $e_k \mapsto \sigma_k$, where (as a labelled reading) $\sigma_1 = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix}$, $\sigma_2 = \begin{psmallmatrix} 0 & -\mathrm{i} \\ \mathrm{i} & 0 \end{psmallmatrix}$, $\sigma_3 = \begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix}$ are the Pauli matrices. Under it the pseudoscalar $I = e_1 e_2 e_3$ goes to $\mathrm{i}\,1$: the centre $\R 1 \oplus \R I$ is a copy of $\C$, and the complex unit of the matrix reading is the pseudoscalar of space.

## technical
The algebra of three-dimensional space is the algebra of $2 \times 2$ complex matrices, with the basis vectors read as the Pauli matrices. The pseudoscalar, the unit oriented volume, is central and squares to minus one, and it is what the matrix reading calls $\mathrm{i}$. So the complex structure of nonrelativistic spin is the volume element of space.

## lay
The Pauli spin matrices of quantum mechanics are a way of writing the three directions of space as matrices. The imaginary unit that appears in them is the oriented unit volume of space.

## one-liner
$\Cl(3,0) \cong \Mat_2(\C)$ with $e_k \mapsto \sigma_k$, and the pseudoscalar $e_1e_2e_3$ maps to $\mathrm{i}$.
