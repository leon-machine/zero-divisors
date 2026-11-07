---
id: standard-model.raw-representation-content-state-space
kind: claim
version: 3
title: The raw representation content of the state space
status: proved
region: standard-model
subject: standard-model
tags: [representation-theory]
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
  - standard-model.imported-cauchy-decomposition-exterior-power@1
  - standard-model.imported-pair-systems-two-chirality-halves@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12.py
  tags:
  - label:prop:raw
- kind: check
  ref: check.py::check_cauchy_table_by_degree
- kind: check
  ref: check.py::check_cauchy_characters
- kind: check
  ref: check.py::check_single_spinor_sector
locators:
  paper: T12
  number: Prop 5.1
  label: prop:raw
  line: 1027
outside_ga:
  kind: other
  why: 'the complex unit of the representation spaces on which U(2) x U(3) acts: the slot space C^2 and the pair space W = C^3, a maximal isotropic subspace of the complexified conformal space V_C = W + W-bar whose vectors include the spacetime directions; that unit must commute with the conformal vectors, which no pseudoscalar does, so the scalar e^{i theta} I_3 of the pair slot keeps the plain i'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pass made, nothing replaced: the scalar e^{i theta} I_3 of the pair slot and its action e^{ik theta} on Lambda^k C^3 use the unit of the pair space W, kept as the plain complexification and declared.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Cauchy table of Lambda^d(C^2 x C^3) by hook-content dimensions, confirmed by the Cauchy character identity at rational points, and the single-spinor sector. Version 2 -> 3.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'the scalar e^{i theta} I_3 of the pair slot acting on Lambda^k C^3 by e^{ik theta}: a complex matrix on the multiplicity space C^3 in the Cauchy decomposition (doubtful; left)'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the single-twistor sector and the two-twistor composite to conformal-spinor language at every level and in the proof; the Cauchy decomposition is untouched.'
  source_title: |-
    The raw representation content of the state space
  source_formal: |-
    Under $\su(2) \oplus \su(3) \oplus \uu(1)$, with the abelian charge the pair number, the full Fock space of the minimal massive hierarchy decomposes as
    \begin{equation}
    \Lambda^{\bullet}(\C^{2} \otimes \C^{3}) = (1,1) \oplus (2,3) \oplus \bigl[(3,\bar{3}) \oplus (1,6)\bigr] \oplus \bigl[(4,1) \oplus (2,8)\bigr] \oplus \bigl[(3,3) \oplus (1,\bar{6})\bigr] \oplus (2,\bar{3}) \oplus (1,1),
    \end{equation}
    graded by pair number $0$ through $6$; and the single-twistor (massless) sector decomposes as $\Lambda^{\bullet}\C^{3} = 1 \oplus 3 \oplus \bar{3} \oplus 1$, graded $0$ through $3$.
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'Both imported edges are the proof''s sources and are kept; representation theory with no completion
      dependence, so no standard-route derivation. Levels pass: conditions already kept.'
---

## formal
Under $\su(2) \oplus \su(3) \oplus \uu(1)$, with the abelian charge the pair number, the full Fock space of the minimal massive hierarchy decomposes as
\begin{equation}
\Lambda^{\bullet}(\C^{2} \otimes \C^{3}) = (1,1) \oplus (2,3) \oplus \bigl[(3,\bar{3}) \oplus (1,6)\bigr] \oplus \bigl[(4,1) \oplus (2,8)\bigr] \oplus \bigl[(3,3) \oplus (1,\bar{6})\bigr] \oplus (2,\bar{3}) \oplus (1,1),
\end{equation}
graded by pair number $0$ through $6$; and the sector of a single conformal spinor (the single-twistor sector, massless) decomposes as $\Lambda^{\bullet}\C^{3} = 1 \oplus 3 \oplus \bar{3} \oplus 1$, graded $0$ through $3$.

## technical
Under $\su(2) \oplus \su(3) \oplus \uu(1)$, with the abelian charge the pair number, the Cauchy decomposition of $\Lambda^{k}(A \otimes B)$ with $A = \C^{2}$ and $B = \C^{3}$ gives the full Fock space of the minimal massive hierarchy degree by degree: $(1,1)$, $(2,3)$, $(3,\bar{3}) \oplus (1,6)$, $(4,1) \oplus (2,8)$, $(3,3) \oplus (1,\bar{6})$, $(2,\bar{3})$ and $(1,1)$ for pair numbers $0$ to $6$, of dimensions $1, 6, 15, 20, 15, 6, 1$. The upper degrees are the duals of the lower ones.

The sector of a single conformal spinor (massless) is $\Lambda^{\bullet}\C^{3} = 1 \oplus 3 \oplus \bar{3} \oplus 1$, graded $0$ to $3$.

## lay
The paper's composite of two basic spinor states has six internal cells, two slots times three pairs, each of which can be empty or filled, giving 64 states. This result sorts those states by how they behave under the weak and colour symmetries and by how many cells are filled. A single spinor state has only three cells and eight states, which sort into a colourless state, a colour triplet, an antitriplet and a second colourless state.

## one-liner
The $64$-state Fock space $\Lambda^{\bullet}(\C^{2} \otimes \C^{3})$ decomposes under $\su(2) \oplus \su(3) \oplus \uu(1)$ into the displayed sum graded by pair number, and the sector of a single conformal spinor into $1 \oplus 3 \oplus \bar{3} \oplus 1$.
