---
id: standard-model.proton-decay-only-through-slot-pair
kind: claim
version: 5
title: Proton decay only through the slot-pair mixing generators
status: proved
region: standard-model
subject: standard-model
tags: [running-and-unification, gauge-fields]
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
  ref: check.py::check_baryon_and_lepton_number_from_chi
- kind: check
  ref: check.py::check_chi_commutes_with_21_and_anticommutes_with_24
- kind: check
  ref: check.py::check_proton_channel_needs_mixing
locators:
  paper: T12
  number: Prop 10.6
  label: prop:protonchannel
  line: 1938
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: n_B and n_L from chi and B - L on the sixteen, chi commuting with the 21 and anticommuting with the 24 bivectors, and Delta(3 n_B + n_L) = -4 for p -> e+ pi0. Version 4 -> 5.'
  env: proposition
  context_refs:
  - standard-model.automorphisms-preserve-slot-pair-split-are
  typing:
    by: ai-typing-pass
    added:
    - standard-model.automorphisms-preserve-slot-pair-split-are
    - standard-model.hyp-s-slot-statistics
    note: 'Added the Pati-Salam split proposition, whose 21 generators the statement takes as given; the
      rest is a direct computation on the sixteen. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: conditions already kept.'
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
Under Hypothesis (S), write $n_{B}$ and $n_{L}$ for baryon and lepton number. On the sixteen
\[
n_{B} \;=\; \tfrac14\bigl((B - L) + \chi\bigr), \qquad n_{L} \;=\; \tfrac14\bigl(\chi - 3\,(B - L)\bigr), \qquad 3n_{B} + n_{L} \;=\; \chi,
\]
reproducing every species' baryon and lepton number. The $21$ generators of Proposition \claimref{standard-model.automorphisms-preserve-slot-pair-split-are} commute with $\chi$, and the $24$ slot-pair mixing generators anticommute with it. The decay $p \to e^{+}\pi^{0}$ has $\Delta(B - L) = 0$ and $\Delta(3n_{B} + n_{L}) = -4$, so it is mediated only by the mixing generators, whose gauge bosons are massive at $M_{U}$.

## technical
Under Hypothesis (S), on the sixteen, baryon and lepton number are $n_{B} = \tfrac14\bigl((B-L) + \chi\bigr)$ and $n_{L} = \tfrac14\bigl(\chi - 3(B-L)\bigr)$, so that $3n_{B} + n_{L} = \chi$, and these reproduce every species' values. The $21$ Pati-Salam generators preserving the slot/pair split commute with $\chi$, and the $24$ slot-pair mixing generators anticommute with it.

The decay $p \to e^{+}\pi^{0}$ has $\Delta(B-L) = 0$ but $\Delta(3n_{B} + n_{L}) = -4$, so it changes $\chi$ and can be mediated only by the mixing generators, whose gauge bosons are massive at $M_{U}$.

## lay
In this framework each particle of a generation is a pattern of filled modes, and one operator counts a combination of baryon and lepton number. The symmetries that keep the two kinds of mode apart leave that count unchanged, while those that mix them flip it. The decay of a proton into a positron and a pion changes the count, so only the mixing symmetries, whose carriers are very heavy, can cause it. This holds under the paper's hypothesis about the composite's modes.

## one-liner
Under Hypothesis (S), $p \to e^{+}\pi^{0}$ changes $3n_{B} + n_{L} = \chi$, which the Pati-Salam generators conserve, so it is mediated only by the slot-pair mixing generators, massive at $M_{U}$.
