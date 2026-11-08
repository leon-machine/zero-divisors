---
id: std-algebra.pauli-algebra
kind: claim
version: 4
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
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle (U1 to U6)
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: 'GA rewrite (the Pauli reading stated by matrix units inside the algebra)'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: typed
trust: ai-proposed
about:
- obj.std-algebra.clifford-algebra
derivations:
- name: main
  uses:
  - std-algebra.existence-uniqueness@1
  - std-algebra.blade-basis@1
  - primer.centre@3
  - primer.sign@3
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
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. The formal, technical and proof levels now state the GA side first: the centre span{1, I} of Cl(3,0) and the matrix units 1/2(1 +- e_3), e_1 1/2(1 -+ e_3) over it, with e_1, e_2, e_3 expanded in them; the Pauli matrices are the entries read off, as before a labelled reading. Verified exactly with lib/GA.py in Cl(3,0) (matrix-unit table, the expansions of e_k, centrality of I). The bridge declaration stays: the result connects Cl(3,0) with the Pauli matrices.'
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
The centre of $\Cl(3,0)$ is $\mathrm{span}\{1, I\}$, $I = e_1e_2e_3$, $I^{2} = -1$, and the four elements
\[
\epsilon_{11} = \tfrac12(1 + e_3), \qquad \epsilon_{22} = \tfrac12(1 - e_3), \qquad \epsilon_{12} = e_1\epsilon_{22} = \tfrac12(e_1 + Ie_2), \qquad \epsilon_{21} = e_1\epsilon_{11} = \tfrac12(e_1 - Ie_2)
\]
are $2 \times 2$ matrix units over the centre ($\epsilon_{ij}\epsilon_{kl} = \delta_{jk}\epsilon_{il}$, $\epsilon_{11} + \epsilon_{22} = 1$), with $e_1 = \epsilon_{12} + \epsilon_{21}$, $e_2 = -I\epsilon_{12} + I\epsilon_{21}$, $e_3 = \epsilon_{11} - \epsilon_{22}$. Hence $\Cl(3,0) \cong \Mat_2(\C)$ by $e_k \mapsto \sigma_k$, where (as a labelled reading) $\sigma_1 = \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix}$, $\sigma_2 = \begin{psmallmatrix} 0 & -I_4 \\ I_4 & 0 \end{psmallmatrix}$, $\sigma_3 = \begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix}$ are the Pauli matrices, with entries in the complex field read as $\mathrm{span}\{1, I_4\}$ (conventions, the unit principle, U1 and U5). Under it the pseudoscalar $I = e_1 e_2 e_3$ goes to $I_4\,1$: the centre $\R 1 \oplus \R I$ is a copy of $\C$, and the complex unit of the matrix reading is the pseudoscalar of space.

## technical
The algebra of three-dimensional space is the algebra of $2 \times 2$ complex matrices, because it contains its own matrix units over its centre $\mathrm{span}\{1, e_1e_2e_3\}$, built from the idempotents $\tfrac12(1 \pm e_3)$ and $e_1$; reading off the entries turns the basis vectors into the Pauli matrices. The pseudoscalar, the unit oriented volume, is central and squares to minus one, and it is what the matrix reading calls the imaginary unit, $I_4$ when the entries are read in $\mathrm{span}\{1, I_4\}$. So the complex structure of nonrelativistic spin is the volume element of space.

## lay
The Pauli spin matrices of quantum mechanics are a way of writing the three directions of space as matrices. The imaginary unit that appears in them is the oriented unit volume of space.

## one-liner
$\Cl(3,0) \cong \Mat_2(\C)$ with $e_k \mapsto \sigma_k$, and the pseudoscalar $e_1e_2e_3$ maps to the matrices' imaginary unit $I_4\,1$ (entries read in $\mathrm{span}\{1, I_4\}$).
