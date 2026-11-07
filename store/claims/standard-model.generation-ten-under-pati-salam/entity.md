---
id: standard-model.generation-ten-under-pati-salam
kind: claim
version: 7
title: The generation and the ten under Pati-Salam
status: proved
region: standard-model
subject: standard-model
tags: [representation-theory, gauge-fields]
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
  - standard-model.automorphisms-preserve-slot-pair-split-are@7
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_casimirs_and_b_minus_l
- kind: check
  ref: check.py::check_sixteen_is_2_1_4_plus_1_2_4bar
- kind: check
  ref: check.py::check_majoranas_span_bidoublet_and_six
locators:
  paper: T12
  number: Prop 10.4
  label: prop:pscontent
  line: 1915
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Casimirs and B - L on the sixteen, the (2,1,4) + (1,2,4bar) split, and the slot and pair Majoranas spanning the (2,2,1) and the (1,1,6). Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 6 -> 7.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Formal level and proof have no twistor language; only the lay level''s twistor slots were reworded.'
  source_title: |-
    The generation and the ten under Pati-Salam
  source_formal: |-
    Under Hypothesis (S), the sixteen decomposes as $(2,1,4) \oplus (1,2,\bar{4})$ under $\su(2)_{L} \oplus \su(2)_{R} \oplus \su(4)$. The Casimirs are $(C_{L}, C_{R}) = (\tfrac34, 0)$ on $Q$ and $L$ and $(0, \tfrac34)$ on $u^{c}$, $d^{c}$, $e^{c}$, $\nu^{c}$; and $B - L$ is $\tfrac13$ and $-1$ on $Q$ and $L$, and $-\tfrac13$, $-\tfrac13$, $1$, $1$ on the four singlets. The four slot Majoranas, the rung directions of Proposition \claimref{standard-model.ten-transported-ambient-space-doublets-are}, span the bidoublet $(2,2,1)$, and the six pair Majoranas span the $(1,1,6)$.
  env: proposition
  context_refs:
  - standard-model.ten-transported-ambient-space-doublets-are
  typing:
    by: ai-typing-pass
    added:
    - standard-model.automorphisms-preserve-slot-pair-split-are
    - standard-model.hyp-s-slot-statistics
    note: 'Added the slot/pair split proposition (not a context_ref), which supplies the 21 generators
      and the Pati-Salam algebra the decomposition is taken under; did not add the ten proposition, cited
      only to name the slot Majoranas; the decomposition is standard Pati-Salam representation theory,
      but no imported claim states it. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics added
      because its statement holds under Hypothesis (S). Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.automorphisms-preserve-slot-pair-split-are
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under Hypothesis (S), the sixteen decomposes as $(2,1,4) \oplus (1,2,\bar{4})$ under $\su(2)_{L} \oplus \su(2)_{R} \oplus \su(4)$. The Casimirs are $(C_{L}, C_{R}) = (\tfrac34, 0)$ on $Q$ and $L$ and $(0, \tfrac34)$ on $u^{c}$, $d^{c}$, $e^{c}$, $\nu^{c}$; and $B - L$ is $\tfrac13$ and $-1$ on $Q$ and $L$, and $-\tfrac13$, $-\tfrac13$, $1$, $1$ on the four singlets. The four slot Majoranas, the rung directions of Proposition \claimref{standard-model.ten-transported-ambient-space-doublets-are}, span the bidoublet $(2,2,1)$, and the six pair Majoranas span the $(1,1,6)$.

## technical
Under (S), the sixteen states of the generation decompose under $\su(2)_{L} \oplus \su(2)_{R} \oplus \su(4)$ as $(2,1,4) \oplus (1,2,\bar{4})$. The Casimirs $(C_{L}, C_{R})$ are $(\tfrac34, 0)$ on $Q$ and $L$ and $(0, \tfrac34)$ on $u^{c}$, $d^{c}$, $e^{c}$, $\nu^{c}$, and $B - L$ takes the values $\tfrac13$ and $-1$ on $Q$ and $L$ and $-\tfrac13, -\tfrac13, 1, 1$ on the four singlets.

The four slot Majoranas, the rung directions, span the bidoublet $(2,2,1)$, and the six pair Majoranas span the $(1,1,6)$.

## lay
Under the slot-statistics hypothesis, one generation of matter fills sixteen states. Under the Pati-Salam symmetry these form two groups of eight: the left-handed quarks and leptons together, and the right-handed ones together, with the lepton as a fourth colour. The ten basic generators split into a four-dimensional piece from the slots and a six-dimensional piece from the pairs.

## one-liner
Under (S), the generation decomposes under Pati-Salam as $(2,1,4) \oplus (1,2,\bar{4})$, and the ten Majoranas split into the slot bidoublet $(2,2,1)$ and the pair $(1,1,6)$.
