---
id: field-theory.second-quantisation
kind: claim
version: 5
title: Second quantisation
status: proved
region: field-theory
subject: quantum-fields
tags: [chirality, pseudoscalar-and-centre]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of FT, the series'' standard disclaimer'
review: typed
about:
- obj.field-theory.single-algebra-field
derivations:
- name: main
  uses:
  - field-theory.imported-tower-limit@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_GA2Q.py
  tags:
  - id:Q1.0
  - id:Q1.1
  - id:Q1.2
  - id:Q2.1
  - id:Q2.2
  - id:Q2.3
  - id:Q3.1
  - id:Q3.2
  - id:Q3.3
  - id:Q3.4
  - id:Q4.1
  - id:Q5
  - id:Q6.1
  - id:Q6.2
  - id:Q6.3
  - id:Q6.4
  - id:Q7
- kind: check
  ref: check.py::check_lambda_is_orthogonal_projector_onto_ker_k
- kind: check
  ref: check.py::check_field_anticommutator_is_local_kernel
- kind: check
  ref: check.py::check_bilinears_are_second_quantised_operators
- kind: check
  ref: check.py::check_mixed_chirality_split_forced_by_i_equals_I4
locators:
  paper: FT
  number: Prop 5.2
  label: prop:secondq
  line: 140
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Lambda(k) as the orthogonal projector onto ker k, the field anticommutator as the local kernel with no tower part, bilinears as d Gamma(M) with the antiparticle c-number removed by normal ordering, and the mixed-chirality split. Version 2 -> 3. check_field_anticommutator_is_local_kernel: explicit cos-Lambda sum now asserted for eps = -1 as well as +1 (fix round 2026-10-23). Version 3 -> 4. Sample inputs moved to module level; no change to what is tested. Version 4 -> 5.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - field-theory.imported-tower-limit
    note: 'Kept the definition as about; added the tower-limit fact, since the field''s modes are tower
      planes whose CAR the anticommutator computation uses. The continuum Pauli-Jordan import of Q4 is
      not in the store. Levels pass: levels written from scratch, keeping every condition and level qualifier
      of the formal statement.'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - '$i = \IS$: Hestenes'' alternative unit, named only to compare with the chosen $i = I_4$ (deliberately
      kept)'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - field-theory.imported-tower-limit
---

## formal
With Definition \claimref{obj.field-theory.single-algebra-field}:
\begin{enumerate}
\item $\Lambda(k) = k\gamma_0/(2k_0)$ is the orthogonal projector onto $\ker k$.
\item The field's anticommutator has no tower part and equals $\ip{\phi_1}{\sum_j 2\alpha_j\cos(k_j\cdot\xi)\Lambda(k_j)\chi\,\phi_2}$; in the continuum it is $\chi(\nabla D)\gamma_0$ with $D$ the Pauli-Jordan function, so the field is local.
\item The span$\{1, I_4\}$ part of $\Psi^*M\Psi$ is the second-quantised $d\Gamma(M)$ on particle modes; antiparticle terms need normal ordering.
\item With $i = I_4$ a field carrying both chiralities gives the right-handed part complex-linearly and the left-handed part conjugated. With Hestenes' $i = \IS$ the same field quantises as a whole Dirac field, at the cost of a frame-dependent unit. The split is forced by the choice $i = I_4$, not by the algebra.
\end{enumerate}

## technical
With the single-algebra field, $\Lambda(k) = k\gamma_0/(2k_0)$ is the orthogonal projector onto $\ker k$, and the field's anticommutator has no tower part and equals $\ip{\phi_1}{\sum_j 2\alpha_j\cos(k_j\cdot\xi)\Lambda(k_j)\chi\,\phi_2}$; in the continuum it is $\chi(\nabla D)\gamma_0$ with $D$ the Pauli-Jordan function, so the field is local. The $\mathrm{span}\{1, I_4\}$ part of $\Psi^*M\Psi$ is the second-quantised $d\Gamma(M)$ on particle modes, with antiparticle terms needing normal ordering.

With $i = I_4$ a field carrying both chiralities gives the right-handed part complex-linearly and the left-handed part conjugated; with Hestenes' $i = \IS$ the same field quantises as a whole Dirac field, at the cost of a frame-dependent unit. The split is forced by the choice $i = I_4$, not by the algebra.

## lay
Fields whose values are elements of the spacetime algebra and whose modes are tower planes can be quantised inside one algebra, with the volume element as imaginary unit. The resulting field is local, and its observables are the standard second-quantised ones. The price of this unit is that a field's two chiralities enter differently, one directly and one conjugated; Hestenes' unit avoids that at the cost of choosing a frame.

## one-liner
With the single-algebra field and $i = I_4$, second quantisation gives a local field and the standard $d\Gamma(M)$, one chirality entering complex-linearly and the other conjugated.
