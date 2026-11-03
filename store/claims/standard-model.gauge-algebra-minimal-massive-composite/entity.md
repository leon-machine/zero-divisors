---
id: standard-model.gauge-algebra-minimal-massive-composite
kind: claim
version: 4
title: The gauge algebra of the minimal massive composite
status: proved
region: standard-model
subject: standard-model
tags: [refutation, gauge-fields, recovers-known-physics, conformal-spinors]
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
derivations:
- name: main
  uses:
  - mass.mass-symplectic-area-two-twistor-formula@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12.py
  tags:
  - label:thm:algebra
- kind: check
  ref: check.py::check_maximal_hierarchy_is_seventeen
- kind: check
  ref: check.py::check_mass_first_at_two_constituents
- kind: check
  ref: check.py::check_minimal_massive_is_standard_model
locators:
  paper: T12
  number: Thm 4.1
  label: thm:algebra
  line: 973
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the automorphism algebras of C^3 x C^3 and C^2 x C^3 (dimension, derived algebra, centre, kernel) and mass first at two constituents. Version 3 -> 4.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the three-twistor hierarchy and ''two twistors of three pairs'' to conformal spinors at every level; the proof had no twistor language.'
  source_title: |-
    The gauge algebra of the minimal massive composite
  source_formal: |-
    The maximal three-twistor hierarchy $\C^{3} \otimes \C^{3}$ has automorphism algebra $\su(3) \oplus \su(3) \oplus \uu(1)$, of dimension seventeen, which is not the Standard Model's. The minimal massive one is: mass first exists at two constituents (Fact \claimref{mass.mass-symplectic-area-two-twistor-formula}), so matter's \emph{minimal massive} hierarchy is $\C^{2} \otimes \C^{3}$, two twistors of three pairs each, and its automorphisms form $(U(2) \times U(3))/U(1)$, with Lie algebra
    \begin{equation}
    \su(2) \oplus \su(3) \oplus \uu(1),
    \end{equation}
    of dimension $4 + 9 - 1 = 12 = 3 + 8 + 1$: the Standard Model Lie algebra exactly. The global group is determined by Theorem \claimref{standard-model.global-form-quotient-determined}.
  env: theorem
  context_refs:
  - mass.mass-symplectic-area-two-twistor-formula
  - standard-model.global-form-quotient-determined
  eqrefs: 1
  typing:
    by: ai-typing-pass
    added: [mass.mass-symplectic-area-two-twistor-formula]
    note: 'Added the mass-as-area theorem, which supplies "mass first exists at two constituents" and so selects the minimal massive hierarchy; left out the global-form theorem, cited only as where the global group is settled.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - mass.mass-symplectic-area-two-twistor-formula
---

## formal
The maximal hierarchy of three conformal spinors (the three-twistor hierarchy) $\C^{3} \otimes \C^{3}$ has automorphism algebra $\su(3) \oplus \su(3) \oplus \uu(1)$, of dimension seventeen, which is not the Standard Model's. The minimal massive one is: mass first exists at two constituents (Fact \claimref{mass.mass-symplectic-area-two-twistor-formula}), so matter's \emph{minimal massive} hierarchy is $\C^{2} \otimes \C^{3}$, two conformal spinors of three pairs each, and its automorphisms form $(U(2) \times U(3))/U(1)$, with Lie algebra
\begin{equation}
\su(2) \oplus \su(3) \oplus \uu(1),
\end{equation}
of dimension $4 + 9 - 1 = 12 = 3 + 8 + 1$: the Standard Model Lie algebra exactly. The global group is determined by Theorem \claimref{standard-model.global-form-quotient-determined}.

## technical
An automorphism of the hierarchy $\C^{m} \otimes \C^{k}$ acts as $A \otimes B$ with $(A, B) \in U(m) \times U(k)$; the kernel of this action is the scalars $(\lambda I_{m}, \lambda^{-1}I_{k})$, a single $U(1)$, so the automorphism algebra is $\su(m) \oplus \su(k) \oplus \uu(1)$. For the maximal hierarchy of three conformal spinors, $\C^{3} \otimes \C^{3}$, this is $\su(3) \oplus \su(3) \oplus \uu(1)$, of dimension seventeen, not the Standard Model's.

Since mass first exists at two constituents, the minimal massive hierarchy is $\C^{2} \otimes \C^{3}$, whose automorphisms form $(U(2) \times U(3))/U(1)$ with Lie algebra $\su(2) \oplus \su(3) \oplus \uu(1)$, of dimension $4 + 9 - 1 = 12 = 3 + 8 + 1$: the Standard Model Lie algebra exactly.

## lay
A composite of basic spinor states of the conformal algebra has a two-level internal structure: which spinor state, and which of its three internal pairs. The rotations that respect both levels form a symmetry algebra. For the smallest composite that can have mass, two spinor states of three pairs each, that algebra is exactly the one behind the strong, weak and hypercharge forces; for three spinor states it is too large.

## one-liner
The automorphism algebra of the minimal massive hierarchy $\C^{2} \otimes \C^{3}$ is $\su(2) \oplus \su(3) \oplus \uu(1)$, exactly the Standard Model's, while that of $\C^{3} \otimes \C^{3}$ is seventeen-dimensional.
