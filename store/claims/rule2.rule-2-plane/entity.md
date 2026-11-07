---
id: rule2.rule-2-plane
kind: claim
version: 4
title: Rule 2 in the plane
status: proved
region: rule2
subject: completion
tags: [transport-algorithm, obstruction-types, finite-models, grading-and-parity]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T17-rule2, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'consistency pass, the time-negative labelling of the plane stated against the store signature'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
outside_ga: {kind: bridge, why: 'clause (i) compares the two ideals with the two two-component representations of planar physics, which fix the time gamma matrix as minus or plus the spatial bivector; the algebra itself is worked in GA'}
review: typed
derivations:
- name: main
  uses:
  - rule2.even-subalgebra-one-dimensional-extension@4
  - rule2.imported-classification-centre-type-c@3
  - rule2.imported-rule-2-matrix-units-forgotten@3
  - rule2.rule-2-kaluza-klein-algebra@7
  - rule2.where-obstruction-sits-commuting-square@6
  - std-algebra.cl11-matrix@2
  - primer.classification-real-clifford-algebras@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T17_rule2.py
  tags:
  - label:prop:planar
- kind: check
  ref: check.py::check_planar_split_and_outer_reflection
- kind: check
  ref: check.py::check_two_repairs_mat4r_inner_parity
- kind: check
  ref: check.py::check_time_positive_form_complex_type
locators:
  paper: T17-rule2
  number: Prop 4.3
  label: prop:planar
  line: 245
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. Convention mixing: the entity labels Cl(2,1) with time of square -1 (the mirror''s labelling, stated only in note.rule2.setting-planar-fermions), while the theorem it cites calls generators of square -1 spacelike; the technical level and the proof now say which reading acts where. outside_ga declared (bridge), as in rule2.rule-2-kaluza-klein-algebra, for the comparison with the gamma matrices of planar physics that clause (i) already made. Mathematics unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.cl11-matrix, primer.classification-real-clifford-algebras where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: type C of Cl(2,1) with ideals Mat_2(R) and the outer planar reflection, the repairs Cl(3,1) and Cl(2,2) = Mat_4(R) with the parity inner, the Rule 1 reading, and the complex type of Cl(1,2). Version 1 -> 2.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: "Kept the Kaluza-Klein theorem as a premise although the proof reuses its argument and computations rather than its Cl(1,4) result; the identification of the ideals with the two-component representations is not cited to the odd-dimension gamma-matrix Fact in the proof, so that edge was not added; the parity-anomaly and graphene Facts are physical readings, not a standard route."
---

## formal
In $A_3 = \Cl(2,1)$:
\begin{enumerate}
\item[(i)] $\omega = e_xe_ye_t$ is central with $\omega^2 = +1$; $A_3 = \varepsilon_+ A_3 \oplus \varepsilon_- A_3$ with each ideal a copy of $\Cl^0(2,1) \cong \Cl(2,0) \cong \Mat_2(\R)$, and $\varepsilon_+ e_t = -\varepsilon_+ e_xe_y$, $\varepsilon_- e_t = +\varepsilon_- e_xe_y$: the two ideals are the two inequivalent two-component representations, which fix the time gamma matrix as $\mp$ the spatial bivector; the reflection of one spatial axis is $\hat{\cdot}\circ\Ad_{e_x}$, negates $\omega$, exchanges the ideals, and is outer;
\item[(ii)] the Rule 2 repairs are $\Cl(3,1)$ ($\nu^2 = +1$, a third spatial direction) and $\Cl(2,2)$ ($\nu^2 = -1$, a second time), both $\cong \Mat_2(\Mat_2(\R)) = \Mat_4(\R)$, in which $\Ad_\nu$ is the grade involution of $A_3$ and $\Ad_{\nu e_x}$ is the planar reflection: a rotation into the third direction, $(\nu e_x)^2 = -1$, in $\Cl(3,1)$, and a boost, $(\nu e_x)^2 = +1$, in $\Cl(2,2)$; $\Cl(3,1)$ is the Rule 1 ascent of $\Cl(2,0)$ and the residues run $2 \to 1 \to 2$ or $2 \to 1 \to 0$;
\item[(iii)] the time-positive form $\Cl(1,2)$ has central volume element of square $-1$: complex type, $\Cl(1,2) \cong \Mat_2(\C)$, no real splitting; the splitting appears on complexification.
\end{enumerate}

## technical
In $A_3 = \Cl(2,1)$, with $Q(e_x) = Q(e_y) = +1$ and $Q(e_t) = -1$ (the mirror's labelling, time of square $-1$, note.rule2.setting-planar-fermions; in the store signature, where spacelike means square $-1$, the words space and time below are exchanged), the volume element $\omega = e_xe_ye_t$ is central with $\omega^2 = +1$, so $A_3 = \varepsilon_+A_3 \oplus \varepsilon_-A_3$, each ideal a copy of $\Cl^0(2,1) \cong \Cl(2,0) \cong \Mat_2(\R)$. Since $\varepsilon_\pm e_t = \mp\varepsilon_\pm e_xe_y$, the ideals are the two inequivalent two-component representations, and the reflection of one spatial axis, $\hat{\cdot}\circ\mathrm{Ad}_{e_x}$, negates $\omega$, exchanges them and is outer.

The Rule 2 repairs are $\Cl(3,1)$, where $Q(\nu) = +1$ is a third spatial direction, and $\Cl(2,2)$, where $Q(\nu) = -1$ is a second time, both $\cong \Mat_4(\R)$. In them conjugation by $\nu$ is the grade involution of $A_3$ and conjugation by $\nu e_x$ is the planar reflection: a rotation in $\Cl(3,1)$ and a boost in $\Cl(2,2)$. $\Cl(3,1)$ is the Rule 1 ascent of $\Cl(2,0)$, with residues $2 \to 1 \to 2$ or $2 \to 1 \to 0$. The time-positive form $\Cl(1,2) \cong \Mat_2(\C)$ has $\omega^2 = -1$ and no real splitting; the splitting appears on complexification.

## lay
For a flat two-dimensional world plus time, with time given negative square, the geometric algebra splits into two halves, matching the two mirror-image kinds of two-component planar fermion. Reflecting one spatial axis swaps them, and this cannot be done from inside the algebra. Adding a third direction, either space-like or a second time, merges the halves and makes the reflection an internal rotation or boost. With the opposite sign convention for time the algebra does not split over the real numbers.

## one-liner
In $\Cl(2,1)$ the central volume element splits the algebra into the two inequivalent two-component representations, exchanged by an outer spatial reflection; the Rule 2 repairs $\Cl(3,1)$ and $\Cl(2,2)$, both $\Mat_4(\R)$, make that reflection inner, and the time-positive $\Cl(1,2)$ is of complex type with no real splitting.
