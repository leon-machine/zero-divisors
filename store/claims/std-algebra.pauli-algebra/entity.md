---
id: std-algebra.pauli-algebra
kind: claim
version: 2
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
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
outside_ga:
  kind: bridge
  why: 'the result connects Cl(3,0) with the Pauli matrices, matrices with entries in span{1, I_4} whose unit is the image of the pseudoscalar e_1e_2e_3; no bare i remains'
extraction:
  source_formal: |-
    $\Cl(3,0) \cong \Mat_2(\C)$ by $e_k \mapsto \sigma_k$, where (as a labelled reading) $\sigma_1 = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix}$, $\sigma_2 = \begin{psmallmatrix} 0 & -\mathrm{i} \\ \mathrm{i} & 0 \end{psmallmatrix}$, $\sigma_3 = \begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix}$ are the Pauli matrices. Under it the pseudoscalar $I = e_1 e_2 e_3$ goes to $\mathrm{i}\,1$: the centre $\R 1 \oplus \R I$ is a copy of $\C$, and the complex unit of the matrix reading is the pseudoscalar of space.

    The source writes $\mathrm{i}$ for the complex unit of the matrix entries, read in the store as $I_4$ (span{1, I_4}).
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle (U1, U5) the Pauli matrices'' entries are read in span{1, I_4}: sigma_2 and the image I_4 1 of the pseudoscalar are written with I_4 in the formal, technical and one-liner levels and the proof; the source''s form moves to source_formal; the bridge declaration is kept, narrowed to the Pauli matrices.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (bridge): the result connects Cl(3,0) with the Pauli matrices, whose complex entries carry i, and shows that i is the image of the pseudoscalar e_1e_2e_3.'
  by: algebra-core-2026-10-26
---

## formal
$\Cl(3,0) \cong \Mat_2(\C)$ by $e_k \mapsto \sigma_k$, where (as a labelled reading) $\sigma_1 = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix}$, $\sigma_2 = \begin{psmallmatrix} 0 & -I_4 \\ I_4 & 0 \end{psmallmatrix}$, $\sigma_3 = \begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix}$ are the Pauli matrices, with entries in the complex field read as $\mathrm{span}\{1, I_4\}$ (conventions, the unit principle, U1 and U5). Under it the pseudoscalar $I = e_1 e_2 e_3$ goes to $I_4\,1$: the centre $\R 1 \oplus \R I$ is a copy of $\C$, and the complex unit of the matrix reading is the pseudoscalar of space.

## technical
The algebra of three-dimensional space is the algebra of $2 \times 2$ complex matrices, with the basis vectors read as the Pauli matrices. The pseudoscalar, the unit oriented volume, is central and squares to minus one, and it is what the matrix reading calls the imaginary unit, $I_4$ when the entries are read in $\mathrm{span}\{1, I_4\}$. So the complex structure of nonrelativistic spin is the volume element of space.

## lay
The Pauli spin matrices of quantum mechanics are a way of writing the three directions of space as matrices. The imaginary unit that appears in them is the oriented unit volume of space.

## one-liner
$\Cl(3,0) \cong \Mat_2(\C)$ with $e_k \mapsto \sigma_k$, and the pseudoscalar $e_1e_2e_3$ maps to the matrices' imaginary unit $I_4\,1$ (entries read in $\mathrm{span}\{1, I_4\}$).
