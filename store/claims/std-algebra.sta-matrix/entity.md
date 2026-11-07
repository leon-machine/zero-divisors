---
id: std-algebra.sta-matrix
kind: claim
version: 2
title: The spacetime algebra as a matrix algebra, and the spacetime split
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- dictionaries
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
  role: 'GA rewrite (the quaternionic matrix algebra stated by matrix units and the quaternion subalgebra inside it)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
review: typed
trust: ai-proposed
about:
- obj.std-algebra.spacetime-algebra
derivations:
- name: main
  uses:
  - std-algebra.existence-uniqueness@1
  - std-algebra.blade-basis@1
  - std-algebra.z2-grading@1
  - primer.classification-real-clifford-algebras@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_quaternionic_and_dirac_readings
- kind: check
  ref: check.py::check_spacetime_split
locators:
  sources:
  - key: DoranLasenby2003
    locator: Ch. 5 (relativity and spacetime)
  - key: Lounesto2001
    locator: Ch. 16 (matrix representations and periodicity of 8)
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. The formal (i), technical and proof levels now state the GA side first: the spatial bivectors gamma_2gamma_3, gamma_3gamma_1, gamma_1gamma_2 as Hamilton''s units, J = -gamma_1gamma_2gamma_3, and the matrix units 1/2(1 +- gamma_0), 1/2(1 +- gamma_0) J commuting with them, with gamma_0 and gamma_k = J q_k expanded; the block matrices and the Dirac matrices stay as labelled readings, and the complexification is named as the store''s odd extension Cl(2,3) with unit I_5. Verified exactly with lib/GA.py in Cl(1,3) (Hamilton relations, the matrix-unit table, commutation with H, the expansions, rank 16). Declared outside_ga (bridge): the result identifies the spacetime algebra with matrix algebras and carries the Dirac matrices as a reading.'
  by: algebra-core-2026-10-26
  note: 'Deviation from the plan: the plan said Cl(1,3) = M4(R). In signature (+,-,-,-), Cl(1,3) = M2(H);
    M4(R) is Cl(3,1). Dirac matrices represent the complexification.'
outside_ga:
  kind: bridge
  why: 'the result identifies the spacetime algebra with the matrix algebra Mat_2(H) and its complexification with Mat_4(C), carrying the Dirac matrices as a labelled reading; the geometric-algebra side is stated by matrix units and Hamilton units inside Cl(1,3)'
---

## formal
(i) $\Cl(1,3) \cong \Mat_2(\HH)$. Inside the algebra: the even spatial bivectors $\mathbf{q}_1 = \gamma_2\gamma_3$, $\mathbf{q}_2 = \gamma_3\gamma_1$, $\mathbf{q}_3 = \gamma_1\gamma_2$ satisfy Hamilton's relations ($\mathbf{q}_k^{2} = -1$, $\mathbf{q}_1\mathbf{q}_2 = \mathbf{q}_3$ and cyclically) and span with $1$ a copy of $\HH$; with $J = -\gamma_1\gamma_2\gamma_3 = -\gamma_0 I$ ($J^{2} = 1$, $J\gamma_0 = -\gamma_0J$), the elements $\epsilon_{11} = \tfrac12(1 + \gamma_0)$, $\epsilon_{22} = \tfrac12(1 - \gamma_0)$, $\epsilon_{12} = \epsilon_{11}J$, $\epsilon_{21} = \epsilon_{22}J$ are $2 \times 2$ matrix units commuting with that $\HH$, and $\gamma_0 = \epsilon_{11} - \epsilon_{22}$, $\gamma_k = J\mathbf{q}_k = (\epsilon_{12} + \epsilon_{21})\mathbf{q}_k$. Reading off the entries, the assignment $\gamma_0 \mapsto \begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix}$, $\gamma_k \mapsto \begin{psmallmatrix} 0 & \mathbf{q}_k \\ \mathbf{q}_k & 0 \end{psmallmatrix}$ extends to an isomorphism. (ii) As a labelled reading, the Dirac matrices $\gamma^{D}_0 = \begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix}$, $\gamma^{D}_k = \begin{psmallmatrix} 0 & \sigma_k \\ -\sigma_k & 0 \end{psmallmatrix}$ ($2 \times 2$ blocks) give a faithful representation $\Cl(1,3) \to \Mat_4(\C)$ whose complex span is all of $\Mat_4(\C)$: $\C \otimes \Cl(1,3) \cong \Mat_4(\C)$ (the complexification, which the store writes as the odd extension $\Cl(2,3)$ with central unit $I_5$, the unit by which the matrices' entries are read). (iii) The relative vectors $\sigma_k = \gamma_k \gamma_0$ satisfy $\sigma_j \sigma_k + \sigma_k \sigma_j = 2\delta_{jk}$ and $\sigma_1 \sigma_2 \sigma_3 = I$, and generate the even subalgebra: $\Cl^{+}(1,3) \cong \Cl(3,0)$, so the spacetime pseudoscalar is the pseudoscalar of the observer's space.

## technical
In the store's signature the spacetime algebra is the algebra of $2 \times 2$ quaternion matrices, as the classification predicts for $p - q \equiv 6$: the spatial bivectors form the quaternions, and $\tfrac12(1 \pm \gamma_0)$ with the spatial trivector give the matrix units inside the algebra. The familiar Dirac matrices are complex, so they represent the complexified algebra, $4 \times 4$ complex matrices; the real spacetime algebra sits inside as a real form. The spacetime split identifies the even part of the spacetime algebra with the algebra of the observer's three-dimensional space, and the two pseudoscalars coincide.

## lay
The algebra of spacetime arrows can be written with $2 \times 2$ arrays of quaternions, or, after allowing complex numbers, with the $4 \times 4$ Dirac matrices of relativistic quantum mechanics. Its even part is exactly the algebra of an observer's ordinary three-dimensional space.

## one-liner
$\Cl(1,3) \cong \Mat_2(\HH)$, the Dirac matrices represent $\C \otimes \Cl(1,3) \cong \Mat_4(\C)$, and $\sigma_k = \gamma_k\gamma_0$ give $\Cl^{+}(1,3) \cong \Cl(3,0)$ with $\sigma_1\sigma_2\sigma_3 = I$.
