---
id: std-algebra.sta-matrix
kind: claim
version: 1
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
  by: algebra-core-2026-10-26
  note: 'Deviation from the plan: the plan said Cl(1,3) = M4(R). In signature (+,-,-,-), Cl(1,3) = M2(H);
    M4(R) is Cl(3,1). Dirac matrices represent the complexification.'
---

## formal
(i) $\Cl(1,3) \cong \Mat_2(\HH)$: with quaternion units $\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3$, the assignment $\gamma_0 \mapsto \begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix}$, $\gamma_k \mapsto \begin{psmallmatrix} 0 & \mathbf{q}_k \\ \mathbf{q}_k & 0 \end{psmallmatrix}$ extends to an isomorphism. (ii) As a labelled reading, the Dirac matrices $\gamma^{D}_0 = \begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix}$, $\gamma^{D}_k = \begin{psmallmatrix} 0 & \sigma_k \\ -\sigma_k & 0 \end{psmallmatrix}$ ($2 \times 2$ blocks) give a faithful representation $\Cl(1,3) \to \Mat_4(\C)$ whose complex span is all of $\Mat_4(\C)$: $\C \otimes \Cl(1,3) \cong \Mat_4(\C)$. (iii) The relative vectors $\sigma_k = \gamma_k \gamma_0$ satisfy $\sigma_j \sigma_k + \sigma_k \sigma_j = 2\delta_{jk}$ and $\sigma_1 \sigma_2 \sigma_3 = I$, and generate the even subalgebra: $\Cl^{+}(1,3) \cong \Cl(3,0)$, so the spacetime pseudoscalar is the pseudoscalar of the observer's space.

## technical
In the store's signature the spacetime algebra is the algebra of $2 \times 2$ quaternion matrices, as the classification predicts for $p - q \equiv 6$. The familiar Dirac matrices are complex, so they represent the complexified algebra, $4 \times 4$ complex matrices; the real spacetime algebra sits inside as a real form. The spacetime split identifies the even part of the spacetime algebra with the algebra of the observer's three-dimensional space, and the two pseudoscalars coincide.

## lay
The algebra of spacetime arrows can be written with $2 \times 2$ arrays of quaternions, or, after allowing complex numbers, with the $4 \times 4$ Dirac matrices of relativistic quantum mechanics. Its even part is exactly the algebra of an observer's ordinary three-dimensional space.

## one-liner
$\Cl(1,3) \cong \Mat_2(\HH)$, the Dirac matrices represent $\C \otimes \Cl(1,3) \cong \Mat_4(\C)$, and $\sigma_k = \gamma_k\gamma_0$ give $\Cl^{+}(1,3) \cong \Cl(3,0)$ with $\sigma_1\sigma_2\sigma_3 = I$.
