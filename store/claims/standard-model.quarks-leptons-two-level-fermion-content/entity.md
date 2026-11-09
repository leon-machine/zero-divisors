---
id: standard-model.quarks-leptons-two-level-fermion-content
kind: claim
version: 5
title: 'Quarks and leptons: the two-level fermion content'
status: proved
region: standard-model
subject: standard-model
tags: [refutation, hypercharge-and-anomalies, recovers-known-physics, representation-theory]
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
  - standard-model.global-form-quotient-determined@4
  - standard-model.imported-cauchy-decomposition-exterior-power@1
  - standard-model.imported-pair-systems-two-chirality-halves@5
  - standard-model.raw-representation-content-state-space@4
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12.py
  tags:
  - label:prop:content
- kind: check
  ref: check.py::check_cells_are_quark_doublet
- kind: check
  ref: check.py::check_doublets_under_s
- kind: check
  ref: check.py::check_no_doublet_without_s
- kind: check
  ref: check.py::check_single_spinor_sector
locators:
  paper: T12
  number: Prop 5.3
  label: prop:content
  line: 1097
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the weights of the cells, the two doublets under (S), the quadruplet without (S), and the single-spinor sector, all from the hypercharge generator. Version 4 -> 5.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the single-twistor Fock space and sector, the complete twistor and the lone twistor to conformal-spinor language at every level and in the proof; the representation and lattice arithmetic is untouched.'
  source_title: |-
    Quarks and leptons: the two-level fermion content
  source_formal: |-
    Under $S(U(2) \times U(3))$, with $Y$ the hypercharge just defined:
    \begin{enumerate}
    \item (Unconditional.) The pair-level generators, the cells of the tensor state space, transform as $(2, 3)$ with abelian weight $q = 1$, so $Y = 1/6$: the quark doublet's representation. A single pair has one unit of hypercharge.
    \item (Under Hypothesis (S).) The states with one slot mode occupied and the pair modes in an $SU(3)$-invariant configuration are $\C^{2} \otimes \Lambda^{0}W$, weight $3$ ($Y = +1/2$, total mode number one, odd), and $\C^{2} \otimes \Lambda^{3}W$, weight $-3$ ($Y = -1/2$, total mode number four, even); both transform as $(2, 1)$. Without (S) neither exists in the state space, whose only row-filling states form the quadruplet $(4,1)$ of weight $+3$.
    \item (Unconditional as a computation on the single-twistor Fock space, with the pair-slot factor acting alone; that Fock space is not a subspace of the tensor state space, and under (S) it is the row $j = 0$.) In the single-twistor sector $\Lambda^{\bullet}W = \Lambda^{\bullet}\C^{3}$, the grade-$k$ states transform as $\Lambda^{k}\C^{3}$, that is as $1, 3, \bar{3}, 1$ for $k = 0, 1, 2, 3$, with weight $q = -2k$: $Y = 0, -1/3, -2/3, -1$.
    \end{enumerate}
    In particular, under (S), the fermion content of the composite at the particle handedness (Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency}) is
    \begin{equation}
    (2,3)_{1/6} \oplus (2,1)_{-1/2},
    \end{equation}
    quark doublet plus lepton doublet, with colour neutrality of the lepton the statement that a state with its pair modes full is an $SU(3)$ singlet: a lepton is a complete twistor, one slot with the pair system full, while a quark is one slot with one pair.
  env: proposition
  context_refs:
  - standard-model.hypercharge-global-form-pair-counting-consistency
  eqrefs: 1
  typing:
    by: ai-typing-pass
    note: 'All four edges are cited in the proof and kept; the hypercharge theorem named in the statement
      was not added because it depends on this claim. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: conditions already kept.'
    added:
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under $S(U(2) \times U(3))$, with $Y$ the hypercharge just defined:
\begin{enumerate}
\item (Unconditional.) The pair-level generators, the cells of the tensor state space, transform as $(2, 3)$ with abelian weight $q = 1$, so $Y = 1/6$: the quark doublet's representation. A single pair has one unit of hypercharge.
\item (Under Hypothesis (S).) The states with one slot mode occupied and the pair modes in an $SU(3)$-invariant configuration are $\C^{2} \otimes \Lambda^{0}W$, weight $3$ ($Y = +1/2$, total mode number one, odd), and $\C^{2} \otimes \Lambda^{3}W$, weight $-3$ ($Y = -1/2$, total mode number four, even); both transform as $(2, 1)$. Without (S) neither exists in the state space, whose only row-filling states form the quadruplet $(4,1)$ of weight $+3$.
\item (Unconditional as a computation on the Fock space of a single conformal spinor, with the pair-slot factor acting alone; that Fock space is not a subspace of the tensor state space, and under (S) it is the row $j = 0$.) In the sector of a single conformal spinor (the single-twistor sector) $\Lambda^{\bullet}W = \Lambda^{\bullet}\C^{3}$, the grade-$k$ states transform as $\Lambda^{k}\C^{3}$, that is as $1, 3, \bar{3}, 1$ for $k = 0, 1, 2, 3$, with weight $q = -2k$: $Y = 0, -1/3, -2/3, -1$.
\end{enumerate}
In particular, under (S), the fermion content of the composite at the particle handedness (Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency}) is
\begin{equation}
(2,3)_{1/6} \oplus (2,1)_{-1/2},
\end{equation}
quark doublet plus lepton doublet, with colour neutrality of the lepton the statement that a state with its pair modes full is an $SU(3)$ singlet: a lepton is a complete conformal spinor, one slot with the pair system full, while a quark is one slot with one pair.

## technical
Under $S(U(2) \times U(3))$, with hypercharge $Y$ the abelian weight divided by six: (1) unconditionally, the cells of the tensor state space, $\C^{2} \otimes \C^{3}$, transform as $(2,3)$ with weight $1$, so $Y = \tfrac16$, the quark doublet. (2) Under Hypothesis (S), the states with one slot mode occupied and the pair modes empty or full are $(2,1)$ with $Y = \pm\tfrac12$; without (S) the state space has no such states, its only row-filling states forming the $(4,1)$. (3) On the Fock space of a single conformal spinor, $\Lambda^{\bullet}\C^{3}$, the grade-$k$ states are $1, 3, \bar{3}, 1$ with $Y = 0, -\tfrac13, -\tfrac23, -1$.

So under (S) the fermion content at the particle handedness is $(2,3)_{1/6} \oplus (2,1)_{-1/2}$: a quark is one slot with one pair, and a lepton is one slot with the pair system full, which is why it is a colour singlet.

## lay
The paper builds composite particles from basic spinor states of the conformal algebra, which have two kinds of internal mode, slots and pairs. One slot with one pair gives exactly the quantum numbers of a quark doublet, with no extra assumption. One slot with all three pairs filled gives a colourless doublet with the lepton's charges, but only if the slots are assumed to behave as fermionic modes like the pairs; without that assumption no lepton appears. A lone spinor state's modes give colourless and coloured states with hypercharges 0, -1/3, -2/3 and -1.

## one-liner
The pair-level cells carry the quark doublet $(2,3)_{1/6}$ unconditionally, and under Hypothesis (S) one slot with the pairs full gives the lepton doublet $(2,1)_{-1/2}$.
