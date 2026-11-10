---
id: standard-model.automorphisms-preserve-slot-pair-split-are
kind: claim
version: 7
title: The automorphisms that preserve the slot/pair split are Pati-Salam
status: proved
region: standard-model
subject: standard-model
tags: [gauge-fields, hypercharge-and-anomalies, representation-theory]
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
  role: 'consistency pass, Q(i) written as Q(I_4); the rung parity named where first used'
  version: 7
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - standard-model.imported-fock-representation-clifford-algebra-bogoliubov@1
  - standard-model.imported-pati-salam-representation-theory-survival@1
  - standard-model.under-s-composites-state-space-spinor@6
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_split_bivectors_close
- kind: check
  ref: check.py::check_left_right_and_pati_salam_generators
- kind: check
  ref: check.py::check_commutant_on_sixteen
locators:
  paper: T12
  number: Prop 10.2
  label: prop:split
  line: 1890
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The proof''s field Q(i) is written Q(I_4) = span_Q{1, I_4}, and the formal level names chi as the rung parity (+1 on slot doublets, -1 on slot singlets, as the proof computes) where it first appears; no mathematics changed.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the 21 split-preserving bivectors in Cl(10) and on the five-mode module, su(2)_L + su(2)_R + su(4) with Y = T_3R + (B - L)/2, and the commutant span{1, chi} on the sixteen. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 5 -> 6.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Formal level and proof have no twistor language; only the lay level''s twistor slots were reworded.'
  source_title: |-
    The automorphisms that preserve the slot/pair split are Pati-Salam
  source_formal: |-
    Under Hypothesis (S), the bivectors $\tfrac12\gamma_{m}\gamma_{n}$ of the ten that preserve the split of the ten Majoranas into four slot and six pair generators are $6 + 15 = 21$ of the $45$. They close under the commutator and form $\su(2)_{L} \oplus \su(2)_{R} \oplus \su(4)$, with
    \[
    \su(2)_{L} = \operatorname{span}\bigl\{v_{4}w_{5},\ v_{5}w_{4},\ \tfrac12(N_{4} - N_{5})\bigr\}, \qquad
    \su(2)_{R} = \operatorname{span}\bigl\{v_{4}v_{5},\ w_{5}w_{4},\ \tfrac12(N_{4} + N_{5} - 1)\bigr\},
    \]
    and $\su(4)$ the fifteen pair bivectors, which contain $\su(3)$ and $B - L$. The weak $\su(2)$ of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite} is $\su(2)_{L}$, the slot mixing, and
    \[
    Y \;=\; T_{3R} + \tfrac12\,(B - L)
    \]
    exactly, with $T_{3R} = \tfrac12(N_{4} + N_{5} - 1)$. The other $24$ bivectors mix slots with pairs. On the sixteen, the commutant of the $21$ is spanned by $1$ and $\chi$. Hence the automorphisms of the five-mode state space induced by orthogonal maps of the ten that preserve the slot/pair split, but not the mode number, form $\mathrm{Spin}(4) \times \mathrm{Spin}(6)$, the Pati-Salam group, the stabiliser of the rung parity; preserving the mode number as well gives the $U(2) \times U(3)$ of Proposition \claimref{standard-model.under-s-composites-state-space-spinor}(2).
  env: proposition
  context_refs:
  - standard-model.gauge-algebra-minimal-massive-composite
  typing:
    by: ai-typing-pass
    note: 'Kept the three edges; did not add the gauge-algebra theorem from context_refs, cited only to
      identify su(2)_L with the weak su(2); no standard-route derivation, since the paper credits Pati
      and Salam with the group but not with this derivation, and no imported claim states the standard
      result. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics added because its statement
      holds under Hypothesis (S). Levels pass: conditions already kept.'
    added:
    - standard-model.hyp-s-slot-statistics
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under Hypothesis (S), the bivectors $\tfrac12\gamma_{m}\gamma_{n}$ of the ten that preserve the split of the ten Majoranas into four slot and six pair generators are $6 + 15 = 21$ of the $45$. They close under the commutator and form $\su(2)_{L} \oplus \su(2)_{R} \oplus \su(4)$, with
\[
\su(2)_{L} = \operatorname{span}\bigl\{v_{4}w_{5},\ v_{5}w_{4},\ \tfrac12(N_{4} - N_{5})\bigr\}, \qquad
\su(2)_{R} = \operatorname{span}\bigl\{v_{4}v_{5},\ w_{5}w_{4},\ \tfrac12(N_{4} + N_{5} - 1)\bigr\},
\]
and $\su(4)$ the fifteen pair bivectors, which contain $\su(3)$ and $B - L$. The weak $\su(2)$ of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite} is $\su(2)_{L}$, the slot mixing, and
\[
Y \;=\; T_{3R} + \tfrac12\,(B - L)
\]
exactly, with $T_{3R} = \tfrac12(N_{4} + N_{5} - 1)$. The other $24$ bivectors mix slots with pairs. On the sixteen, the commutant of the $21$ is spanned by $1$ and the rung parity $\chi$ ($+1$ on the slot-doublet states, $-1$ on the slot-singlet states). Hence the automorphisms of the five-mode state space induced by orthogonal maps of the ten that preserve the slot/pair split, but not the mode number, form $\mathrm{Spin}(4) \times \mathrm{Spin}(6)$, the Pati-Salam group, the stabiliser of the rung parity; preserving the mode number as well gives the $U(2) \times U(3)$ of Proposition \claimref{standard-model.under-s-composites-state-space-spinor}(2).

## technical
Under (S), write the ten Majorana generators of the five modes as four slot and six pair Majoranas. The bivectors $\tfrac12\gamma_{m}\gamma_{n}$ that preserve this split are $6 + 15 = 21$ of the $45$; they close into $\su(2)_{L} \oplus \su(2)_{R} \oplus \su(4)$, with $\su(2)_{L}$ the slot mixing, $\su(4)$ the fifteen pair bivectors, containing $\su(3)$ and $B - L$, and hypercharge exactly $Y = T_{3R} + \tfrac12(B - L)$ with $T_{3R} = \tfrac12(N_{4} + N_{5} - 1)$.

The other $24$ bivectors mix slots with pairs. On the sixteen, the commutant of the $21$ is spanned by $1$ and the rung parity $\chi$. So the automorphisms induced by split-preserving orthogonal maps of the ten form $\mathrm{Spin}(4) \times \mathrm{Spin}(6)$, the Pati-Salam group, the stabiliser of the rung parity; preserving the mode number as well gives $U(2) \times U(3)$.

## lay
Under the slot-statistics hypothesis, the composite's states are built from ten basic generators, four belonging to the slots of its two basic spinor states and six to the pairs. The symmetries that never mix the two groups form the Pati-Salam group, a known candidate for unifying quarks and leptons in which lepton number acts as a fourth colour. Within it, hypercharge comes out as an exact combination of a right-handed charge and baryon minus lepton number.

## one-liner
Under (S), the automorphisms of the five-mode state space that preserve the slot/pair split form the Pati-Salam group $\mathrm{Spin}(4) \times \mathrm{Spin}(6)$, with $Y = T_{3R} + \tfrac12(B - L)$ exactly.
