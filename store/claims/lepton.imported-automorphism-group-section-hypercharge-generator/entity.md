---
id: lepton.imported-automorphism-group-section-hypercharge-generator
kind: claim
version: 3
title: 'Imported: the automorphism group, its section, and the hypercharge generator'
status: proved
region: lepton
subject: standard-model
tags: [gauge-fields, hypercharge-and-anomalies]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-lepton, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - standard-model.global-form-quotient-determined@4
  - standard-model.quarks-leptons-two-level-fermion-content@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_kernel_and_section
- kind: check
  ref: check.py::check_z6_quotient
- kind: check
  ref: check.py::check_centre_is_hypercharge_line
- kind: check
  ref: check.py::check_y_acts_by_the_abelian_weight
locators:
  paper: T12-lepton
  number: Fact 1.3
  label: fact:group
  line: 188
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the kernel K and the determinant section, the Z_6 kernel, the centre of s(u(2) + u(3)) as the line of (3, -2), and y acting by the abelian weight. Version 2 -> 3.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Formal level and proof have no twistor language (the i in y = (3i I_2, -2i I_3) is the unit of the Lie algebra of U(2) x U(3) and I_2, I_3 are identity matrices, not pseudoscalars); only the lay level was reworded.'
  source_title: |-
    Imported: the automorphism group, its section, and the hypercharge generator
  source_formal: |-
    The automorphisms of the hierarchy, the unitaries $A \otimes B$ of $\C^{2} \otimes \C^{3}$ with $(A, B) \in U(2) \times U(3)$, form $(U(2) \times U(3))/K$ with $K = \{(\lambda I_{2}, \lambda^{-1}I_{3})\}$, and each $K$-coset contains exactly one pair with $\det A \cdot \det B = 1$, so the group is $S(U(2) \times U(3)) \cong (SU(2) \times SU(3) \times U(1))/\mathbb{Z}_{6}$, the $U(1)$ factor acting as $(\lambda^{3}a, \lambda^{-2}b)$. The centre of its Lie algebra is spanned by $\mathsf{y} = (3iI_{2}, -2iI_{3})$; on an irreducible representation $\mathsf{y}$ acts as $iq$ with $q$ the abelian weight, and hypercharge is $Y = q/6$. Irreducible representations of $S(U(2) \times U(3))$ are determined by their $SU(2)$ content, $SU(3)$ content and weight. \emph{Provenance:} \cite[Thms.~4.1, 4.2, and the definition before Prop.~5.3]{ButlerT12}.
  typing:
    by: ai-typing-pass
    note: 'Kept the three cited series results; the quark-lepton content edge stands for the hypercharge
      definition placed just before that proposition in the source. Levels pass: conditions already kept.'
  env: fact
  context_refs:
  - standard-model.gauge-algebra-minimal-massive-composite
  - standard-model.global-form-quotient-determined
  - standard-model.quarks-leptons-two-level-fermion-content
  flags:
  - 'fact restating several series results: derived from them'
---

## formal
The automorphisms of the hierarchy, the unitaries $A \otimes B$ of $\C^{2} \otimes \C^{3}$ with $(A, B) \in U(2) \times U(3)$, form $(U(2) \times U(3))/K$ with $K = \{(\lambda I_{2}, \lambda^{-1}I_{3})\}$, and each $K$-coset contains exactly one pair with $\det A \cdot \det B = 1$, so the group is $S(U(2) \times U(3)) \cong (SU(2) \times SU(3) \times U(1))/\mathbb{Z}_{6}$, the $U(1)$ factor acting as $(\lambda^{3}a, \lambda^{-2}b)$. The centre of its Lie algebra is spanned by $\mathsf{y} = (3iI_{2}, -2iI_{3})$; on an irreducible representation $\mathsf{y}$ acts as $iq$ with $q$ the abelian weight, and hypercharge is $Y = q/6$. Irreducible representations of $S(U(2) \times U(3))$ are determined by their $SU(2)$ content, $SU(3)$ content and weight. \emph{Provenance:} \cite[Thms.~4.1, 4.2, and the definition before Prop.~5.3]{ButlerT12}.

## technical
The automorphisms of the hierarchy $\C^{2} \otimes \C^{3}$ are the unitaries $A \otimes B$, $(A, B) \in U(2) \times U(3)$, modulo the kernel $K = \{(\lambda I_{2}, \lambda^{-1}I_{3})\}$. Each $K$-coset contains exactly one pair with $\det A \cdot \det B = 1$, which gives the canonical section and the group $S(U(2) \times U(3)) \cong (SU(2) \times SU(3) \times U(1))/\mathbb{Z}_{6}$, the $U(1)$ factor acting as $(\lambda^{3}a, \lambda^{-2}b)$.

The centre of the Lie algebra is spanned by $\mathsf{y} = (3iI_{2}, -2iI_{3})$, which acts as $iq$ on an irreducible representation of abelian weight $q$, and hypercharge is $Y = q/6$. Irreducible representations are determined by their $SU(2)$ content, $SU(3)$ content and weight.

## lay
The symmetries of the structure of two spinor states with three internal pairs form exactly the Standard Model's gauge group in its smallest global form. Each symmetry can be written in many ways, and there is one canonical choice among them. The group's single abelian direction defines hypercharge as one sixth of a whole-number weight, and a particle type is fixed by three labels: its weak content, its colour content and that weight.

## one-liner
The automorphism group of the hierarchy is $S(U(2) \times U(3)) \cong (SU(2) \times SU(3) \times U(1))/\mathbb{Z}_{6}$, with a canonical determinant-one section and hypercharge $Y = q/6$ read from the central generator.
