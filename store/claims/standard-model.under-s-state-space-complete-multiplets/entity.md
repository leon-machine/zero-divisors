---
id: standard-model.under-s-state-space-complete-multiplets
kind: claim
version: 5
title: Under (S) the state space is complete multiplets, and which splits move the condition
status: proved
region: standard-model
subject: standard-model
tags: [running-and-unification, representation-theory]
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
  - standard-model.complete-multiplets-shift-all-three-coefficients@3
  - standard-model.one-threshold-exact-criterion@3
  - standard-model.under-s-composites-state-space-spinor@6
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_halves_have_sixteen_states
- kind: check
  ref: check.py::check_hypercharge_multisets
- kind: check
  ref: check.py::check_each_half_shifts_equally_and_is_inert
- kind: check
  ref: check.py::check_exactly_eight_inert_splits
locators:
  paper: T12
  number: Prop 8.13
  label: prop:ledger
  line: 1416
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the 16 + 16 split, the hypercharge multisets, equal shifts 4/3 and inertness of each half, and exactly eight inert sub-multisets of 64. Version 4 -> 5.'
  env: proposition
  context_refs:
  - standard-model.direction-demanded-content-doublet-heavy
  - standard-model.table-exact
  - standard-model.under-s-composites-state-space-spinor
  typing:
    by: ai-typing-pass
    removed:
    - standard-model.gauge-algebra-minimal-massive-composite
    added:
    - standard-model.under-s-composites-state-space-spinor
    - standard-model.hyp-s-slot-statistics
    note: 'Added the spinor proposition the hypothesis clause and clause (2) rest on; removed the gauge-algebra
      theorem, which the proof says enters only a reading in the last two sentences. Hypothesis pass:
      assumes standard-model.hyp-s-slot-statistics added because its statement holds under Hypothesis
      (S). Levels pass: lay now names Hypothesis (S) and the one-loop level.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.under-s-composites-state-space-spinor
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Assume Hypothesis (S), so that the composite's state space is $\Lambda^{\bullet}(\C^{2} \oplus \C^{3})$ with the weights of Proposition \claimref{standard-model.under-s-composites-state-space-spinor}. Then:
\begin{enumerate}
\item[(1)] The even half (total mode number even) has sixteen states and the odd half sixteen.
\item[(2)] The even half's hypercharge multiset is the derived generation's, $\tfrac16$ six times, $-\tfrac12$ twice, $-\tfrac23$ and $\tfrac13$ three times each, $1$ and $0$ once, and the odd half's is its negative: the halves are the $16$ and the $\overline{16}$.
\item[(3)] Each half, taken as Weyl content with a common threshold, shifts the three coefficients equally, by $\tfrac43$: every state in the state space is in a complete $\mathrm{Spin}(10)$ multiplet, and the state space with degenerate thresholds is inert for the meeting condition.
\item[(4)] Among the $2^{6}$ sub-multisets of the generation's six $S(U(2) \times U(3))$ components, exactly eight are inert: the unions of the $SU(5)$ pieces $10 = \{Q, u^{c}, e^{c}\}$, $\bar{5} = \{L, d^{c}\}$ and $1 = \{\nu^{c}\}$. Every other split moves the meeting condition.
\end{enumerate}
Consequently the content Proposition \claimref{standard-model.table-exact} demands cannot be drawn from the state space's states with $\mathrm{Spin}(10)$-degenerate masses, nor from copies of the state space so placed: it must be split content, a multiplet some of whose members are light between $M_{Z}$ and $M_{U}$ while the rest are not, and the split must cut across the $SU(5)$ pieces. The series' one derived structure that distinguishes members of a $\mathrm{Spin}(10)$ multiplet is the distinction between the two slot modes and the three pair modes of $\C^{2} \oplus \C^{3}$, the distinction (S) itself sets aside; $SU(2)$ acts on the slots and $SU(3)$ on the pairs, so ``doublet-heavy'' in Corollary \claimref{standard-model.direction-demanded-content-doublet-heavy} reads, in the framework's language, ``slot-heavy''.

## technical
Under Hypothesis (S), the composite's thirty-two states split into even and odd halves of sixteen, carrying the hypercharges of the $16$ and the $\overline{16}$. Each half, as Weyl content at a common threshold, shifts all three one-loop coefficients by $\tfrac43$, so the state space with degenerate thresholds is inert for the meeting condition; of the $2^{6}$ unions of the generation's six components, exactly the eight unions of the $SU(5)$ pieces $10$, $\bar{5}$ and $1$ are inert.

Consequently the content the meeting condition demands must be split content, a multiplet some of whose members are light between $M_{Z}$ and $M_{U}$, with the split cutting across the $SU(5)$ pieces. The one derived distinction inside a $\mathrm{Spin}(10)$ multiplet is that between the two slot modes and the three pair modes, so ``doublet-heavy'' reads, in the framework's language, as ``slot-heavy''.

## lay
Adding a complete family of particles at one mass shifts the running of all three force strengths equally at one loop, so it never helps them meet. This result shows that every state the paper's composite can hold comes in such complete families, so to help, some members of a family must be lighter than the others. The only distinction the framework derives inside a family is between its two kinds of mode, so that is where any such split would have to come from. This assumes the paper's hypothesis about the composite's modes, Hypothesis (S).

## one-liner
Under Hypothesis (S), the composite's state space consists of complete $\mathrm{Spin}(10)$ multiplets and is inert for unification, so the demanded content must be split across the $SU(5)$ pieces.
