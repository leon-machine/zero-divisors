---
id: one-relation.two-capacities-three-consequences
kind: claim
version: 6
title: The two capacities, and three consequences
status: proved
region: one-relation
subject: one-relation
tags: [witt-index, two-readings, mode-counting]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
- name: Claude Opus 5.5
  role: notation pass, every imaginary unit resolved as a geometric-algebra pseudoscalar (unit principle)
  version: 6
  source: maintainer pass 2026-11-07 (resolve units)
review: typed
derivations:
- name: main
  uses:
  - one-relation.imported-witts-extension-theorem@2
  - one-relation.two-presentations@5
  - tower.witt-index-quantum-capacity@4
  - std-algebra.vector-squares@1
  - std-algebra.witt-decomposition@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T16.py
  tags:
  - label:prop:capacity
- kind: check
  ref: check.py::check_real_capacity_is_min_pq
- kind: check
  ref: check.py::check_complex_capacity_is_floor_half_d
- kind: check
  ref: check.py::check_agreement_locus_and_increments
- kind: check
  ref: check.py::check_boost_qubit_and_dirac_fock_space
- kind: check
  ref: check.py::check_ascended_capacity_three_complex_two_real
locators:
  paper: T16
  number: Prop 3.2
  label: prop:capacity
  line: 606
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U3: the complex null pairs (e + ie'')/2, -(e - ie'')/2 of V_C are written with I_hatV, the central pseudoscalar of the odd extension of V (of V + R f when d is odd), which squares to -1 and commutes with every vector, so V_C = V + I_hatV V (std-algebra.complexification-is-the-odd-extension, cited as a mention). No bare i remains, so the outside_ga declaration (other, for i only) is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Group F (found by the language check''s bare-unit detector): nothing replaced; the i stays and is declared outside_ga (other): the null pairs (e + ie'')/2, -(e - ie'')/2 are complex null vectors of the complexified space V_C; their i must commute with the vectors e, e'', which no pseudoscalar does.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.vector-squares, std-algebra.witt-decomposition where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: on all (p,q) with p, q <= 5 the min(p,q) real and floor(d/2) complex pairs with their pairings, definite W-perp/W and dim U-perp = d - dim U; agreement iff |p - q| <= 1 and increments by one; boost-plane complement negative definite and a four-dimensional Fock module for Cl(1,3); r_C(2,4) = 3, r_R(2,4) = 2. Version 2 -> 3. Check strengthened: signature (1,3), one real pair and two pairs pinned; boost-plane complement signature computed from its Gram matrix; Fock states over all subsets of the pairs; samples moved to module level. Version 3 -> 4.'
  env: proposition
  context_refs:
  - dark-matter.imported-derived-generation-flag
  - one-relation.imported-completion-ladder
  - one-relation.overlap-table-sorted
  - one-relation.two-presentations
  - standard-model.four-dimensions-forces-converse
  - standard-model.pair-count-dimension
  typing:
    by: ai-typing-pass
    removed:
    - one-relation.third-constant-conversion-constant-between-charts
    added:
    - one-relation.two-presentations
    note: 'Removed the later invariant-ratio lemma (a forward identification, and the E301 cycle); added
      the two-presentations proposition, whose quantum reading the statement''s mode counts are of; T12
      and T14 results in context_refs are comparisons. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - one-relation.two-presentations
---

## formal
Let $(V,Q)$ be real, nondegenerate, of signature $(p,q)$, $d = p+q$. The quantum presentation of Proposition \claimref{one-relation.two-presentations} supports two mode counts, which differ in general and must not be conflated:
\[
r_{\R}(p,q) = \min(p,q), \qquad r_{\C}(p,q) = \lfloor d/2 \rfloor,
\]
the \emph{real capacity}, the number of modes realisable by real null vectors (Fact \claimref{tower.witt-index-quantum-capacity}), and the \emph{complex capacity}, the maximal isotropic dimension of $V_{\C}$, the number of modes of the complexified reading. They agree exactly when $|p - q| \leq 1$, in particular on the split signatures $(k,k)$; for $(1,3)$ they are $1$ and $2$, for $(2,4)$ they are $2$ and $3$. Three consequences, each labelled with the capacity it uses.
\begin{enumerate}
\item \emph{(The boost qubit; real.)} $r_{\R}(1,3) = 1$: Lorentzian signature has one real hyperbolic plane, unique up to an isometry of the whole space (all such planes are conjugate under $O(1,3)$), and the anisotropic complement is definite, so pre-ascent spacetime natively supports exactly one \emph{real} quantum mode, the boost qubit. The complex capacity is two, which is the Dirac spinor of $\Cl(1,3)_{\C}$ as a two-mode Fock space of dimension $2^{2} = 4$. This clause counts the modes of $(1,3)$ and says nothing about the single-mode thermality theorem, whose mode is the ladder pair of the ascent and is counted by neither $r_{\R}(1,3)$ nor $r_{\C}(1,3)$; what is said about that theorem is a reading, Proposition \claimref{one-relation.overlap-table-sorted}(iii).
\item \emph{(Transport is capacity increment; both capacities.)} Each $(1,1)$ ascent adjoins one hyperbolic plane, hence one real null pair, hence one mode in either count: $r_{\R}$ and $r_{\C}$ each rise by exactly one per rung. The transport principle is capacity increment, and the tower's one-qubit-per-rung ladder (Fact \claimref{one-relation.imported-completion-ladder}) is its restatement.
\item \emph{(The ascended capacity is three; complex.)} $r_{\C}(2,4) = 3$: the complexified ascended $\C^{6}$ has maximal isotropic dimension three, which is the Standard-Model paper's pair count $(n+2)/2$ at spacetime dimension $n = 4$, the ambient signature being $(2,n)$, so that $d = n + 2$ and, for $n$ even, $\lfloor d/2 \rfloor = (n+2)/2$ \cite[Lem.~2.12]{ButlerT12}. Under that count the Standard-Model paper selects the strong force and four dimensions, on the two conditionalities it declares \cite[Prop.~4.3]{ButlerT12}. The real capacity of the ascended space is two: its third pair lies in the complexification, as the dark-matter paper's flag Fact records \cite[Fact~2.9]{ButlerT14}.
\end{enumerate}
Which capacity a physical count uses is therefore a statement to be made each time, not a residue: (1) is real, (3) is complex, (2) holds for both capacities. The successor problem is which of the two the state of Section \ref{sec:vacua} selects.

## technical
For a real nondegenerate signature $(p,q)$, $d = p + q$, the quantum reading supports two mode counts: the real capacity $r_{\R}(p,q) = \min(p,q)$, counting modes realised by real null vectors, and the complex capacity $r_{\C}(p,q) = \lfloor d/2 \rfloor$, the maximal isotropic dimension of $V_{\C}$. They agree exactly when $|p - q| \leq 1$; for $(1,3)$ they are $1$ and $2$, for $(2,4)$ they are $2$ and $3$.

Consequences: (1) Lorentzian spacetime has one real mode, the boost qubit, unique up to isometry, while the complex count two is the Dirac spinor as a two-mode Fock space. (2) Each $(1,1)$ ascent raises both capacities by exactly one. (3) $r_{\C}(2,4) = 3$, the Standard-Model pair count at spacetime dimension four, while the real capacity there is two. Which capacity a physical count uses must be stated each time.

## lay
Reading spacetime geometry as a system of fermion modes, there are two ways to count the modes: using only real directions, or allowing complex ones. The two counts usually differ, and for ordinary spacetime they give one and two. Each step up the tower of extended spaces adds exactly one mode to both counts, and the complex count of the extended six-dimensional space is three.

## one-liner
A real quadratic space of signature $(p,q)$ has real capacity $\min(p,q)$ and complex capacity $\lfloor (p+q)/2 \rfloor$, both rising by one per ascent, giving one boost qubit for $(1,3)$ and complex capacity three for $(2,4)$.
