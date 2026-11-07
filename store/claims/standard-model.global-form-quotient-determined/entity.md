---
id: standard-model.global-form-quotient-determined
kind: claim
version: 4
title: 'The global form: the quotient determined'
status: proved
region: standard-model
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
  source: authorship disclosure of T12, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 4
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - standard-model.gauge-algebra-minimal-massive-composite@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12.py
  tags:
  - label:thm:global
- kind: check
  ref: check.py::check_kernel_and_coset_rescaling
- kind: check
  ref: check.py::check_z6_kernel_exactly
- kind: check
  ref: check.py::check_su5_splitting_subgroup
- kind: check
  ref: check.py::check_charge_lattice
locators:
  paper: T12
  number: Thm 4.2
  label: thm:global
  line: 987
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By Leon''s ruling R3: the determinant phases e^{I_4 alpha}, the sixth root lambda = e^{2 pi I_4/6} and the central characters e^{2 pi I_4 t/3}, e^{2 pi I_4 (p_1 - p_2)/3} of the proof are written with I_4, the module C^2 tensor C^3 read over span{1, I_4} on the tower''s floors (stated once in the formal level; notational); no bare i remains, so the earlier declaration is removed.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the kernel and coset rescaling at the group level, the Z6 kernel in Q(zeta_6) with proper covers unfaithful, the C^2 + C^3 splitting in SU(5), and the charge lattice. Version 2 -> 3.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'e^{2 pi i/6}, e^{2 pi i/3}, exp 2 pi i(...), det A = e^{i alpha}: roots of unity and determinants of complex matrices in U(2) x U(3), numbers'
  env: theorem
  context_refs:
  - standard-model.gauge-algebra-minimal-massive-composite
  - standard-model.hypercharge-global-form-pair-counting-consistency
  typing:
    by: ai-typing-pass
    added:
    - standard-model.gauge-algebra-minimal-massive-composite
    note: 'Added the gauge-algebra theorem as premise because the statement is about its group and inherits
      its premise; the hypercharge context reference is a forward comment, and the standard reading of
      the Z6 quotient (Baez-Huerta, Tong) is cited but not in the store, so no standard-route. Levels
      pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.gauge-algebra-minimal-massive-composite
---

## formal
The global gauge group of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite} is determined exactly. The kernel of the $(U(2) \times U(3))$-action on $\C^{2} \otimes \C^{3}$ (numbers and the module's complex structure are read in $\mathrm{span}\{1, I_{4}\}$, the module read on the tower's floors, where $I_{4}$ commutes with the tower vectors; $I_{2}$ and $I_{3}$ are identity matrices) is $K = \{(\lambda I_{2}, \lambda^{-1} I_{3})\} \cong U(1)$, and
\begin{equation}
(U(2) \times U(3))/K \;\cong\; S(U(2) \times U(3)) \;\cong\; \bigl(SU(2) \times SU(3) \times U(1)\bigr)/\mathbb{Z}_{6}:
\end{equation}
the framework's group is the smallest of the Standard Model's global forms, the full $\mathbb{Z}_{6}$ quotient, not the naive product and not either intermediate quotient. Three consequences. (i) $S(U(2) \times U(3))$ is exactly the subgroup of $SU(5)$ preserving the splitting $\C^{5} = \C^{2} \oplus \C^{3}$, and none of the three proper covers $(SU(2) \times SU(3) \times U(1))/\Gamma$, $\Gamma \subsetneq \mathbb{Z}_{6}$, acts faithfully through it; so the framework's global form is the one that grand unification's embedding requires, and the trace ratio $3/8$ of Section \ref{sec:running} refers to the same normalisation from the other side. (ii) The representations of the group are confined to the $\mathbb{Z}_{6}$ charge lattice: on a representation of the covering product with colour triality $t \in \mathbb{Z}_{3}$, weak parity $\delta \in \mathbb{Z}_{2}$ (the class of the $SU(2)$ content: $1$ on a doublet, $0$ on a singlet or triplet) and abelian weight $q \in \mathbb{Z}$ (the integer such that the $U(1)$ factor $\lambda$ acts by $\lambda^{q}$), descent to the quotient holds if and only if $2t + 3\delta + q \equiv 0 \pmod 6$; writing $Y = q/6$ this is the condition that $t/3 + \delta/2 + Y$ be an integer. The content of Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency} lies on it (each of its representations is built as a representation of $S(U(2) \times U(3))$), and the lattice check is printed there. (iii) A structural stance, registered: the lattice forbids representations off it, so a confirmed discovery of, for example, a fractionally charged colour singlet would refute the identification of the gauge group with the automorphism group of minimal massive compositeness, a stance that current searches test \cite{PDG2024}. The stance inherits the conditionality of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}'s premise and is flagged at that level.

## technical
The automorphism group $U(2) \times U(3)$ of the minimal massive composite acts on $\C^{2} \otimes \C^{3}$ by $A \otimes B$, and the pairs acting trivially form $K = \{(\lambda I_{2}, \lambda^{-1} I_{3})\} \cong U(1)$. Each coset of $K$ contains exactly one pair with $\det A \det B = 1$, and $(a, b, \lambda) \mapsto (\lambda^{3}a, \lambda^{-2}b)$ maps $SU(2) \times SU(3) \times U(1)$ onto that subgroup with kernel a cyclic group of order six, so
$(U(2) \times U(3))/K \cong S(U(2) \times U(3)) \cong (SU(2) \times SU(3) \times U(1))/\mathbb{Z}_{6}$.

This group is exactly the stabiliser in $SU(5)$ of the splitting $\C^{5} = \C^{2} \oplus \C^{3}$, and no proper cover by a smaller quotient acts faithfully through it. A representation with colour triality $t$, weak parity $\delta$ and abelian weight $q$ descends to it if and only if $2t + 3\delta + q \equiv 0 \pmod 6$, that is $t/3 + \delta/2 + Y \in \mathbb{Z}$ with $Y = q/6$. A confirmed fractionally charged colour singlet would therefore refute the identification of the gauge group with this automorphism group; that stance carries the conditional status of the gauge-algebra result's premise.

## lay
The symmetries of the smallest composite that can carry mass have the algebra of the Standard Model forces. This result pins down the group itself, not only its algebra: it is the most economical of the possible global forms, the one in which a six-element subgroup is divided out. That choice restricts which combinations of colour, weak charge and hypercharge any particle can carry, and it is the form that grand unification requires. A free particle with no colour and a fractional electric charge would contradict the identification.

## one-liner
The global gauge group of the minimal massive composite is $S(U(2) \times U(3)) \cong (SU(2) \times SU(3) \times U(1))/\mathbb{Z}_{6}$, the smallest of the Standard Model's global forms.
