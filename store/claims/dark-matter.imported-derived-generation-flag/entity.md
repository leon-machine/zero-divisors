---
id: dark-matter.imported-derived-generation-flag
kind: claim
version: 6
title: 'Imported: the derived generation and the flag'
status: proved
region: dark-matter
subject: standard-model
tags: [witt-index, matter-asymmetry, chirality]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
about:
- obj.dark-matter.witt-flag
derivations:
- name: main
  uses:
  - correspondence.fock-model-complexified-ascended-algebra@9
  - correspondence.twistors-are-states-three-ladder-pairs@6
  - families.alignment-computed-thirteenth-refutation-democracy-one@4
  - standard-model.chirality-two-halves-spinor-module-conjugation@6
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_witt_decomposition_two_real_one_complex
- kind: check
  ref: check.py::check_listing_choice_is_particle_antiparticle
locators:
  paper: T14
  number: Fact 2.9
  label: fact:flag
  line: 128
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Witt decomposition of the complexified ambient in Cl(2,4) (two real hyperbolic pairs, real Witt index 2, the third pair only complex) and the two listings of the five-mode module as mutually conjugate. Version 5 -> 6.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the twistor Fock structure to the Fock structure of a conformal spinor at every level and in the proof. Kept the complexified ambient V_C, in which the third Witt pair lives: TWGA supplies no algebra element as its complex unit (I6 anticommutes with vectors), so the lay level''s ''only once complex numbers are allowed'' is kept.'
  source_title: |-
    Imported: the derived generation and the flag
  source_formal: |-
    The visible matter is the derived Standard Model generation \cite{ButlerT12}; the twistor Fock structure's three pairs are a Witt decomposition of the complexified conformal ambient \cite[Thm.~5.3]{ButlerT9}, two realised by real hyperbolic planes of $\R^{2,4}$, the third only in $V_{\C}$ \cite[proof of Thm.~3.1]{ButlerT9}; the one-handed listing choice on it is the particle-antiparticle orientation \cite[Prop.~5.6]{ButlerT12}, under that paper's Hypothesis (S), carried here; the condensate's alignment is \cite[Prop.~4.3]{ButlerT13}. Reading the listing choice as the descent's flag is this paper's (Definition \claimref{obj.dark-matter.witt-flag}).
  typing:
    by: ai-typing-pass
    note: 'Kept all four series premises, each matching a cited result; Hypothesis (S) has no postulate
      entity in the store, so it is carried in the text only, and the E204 comes from the chirality premise
      outside this list. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics added because its
      statement holds under Hypothesis (S). Levels pass: lay now names Hypothesis (S).'
    added:
    - standard-model.hyp-s-slot-statistics
  env: fact
  context_refs:
  - correspondence.fock-model-complexified-ascended-algebra
  - correspondence.twistors-are-states-three-ladder-pairs
  - families.alignment-computed-thirteenth-refutation-democracy-one
  - standard-model.chirality-two-halves-spinor-module-conjugation
  outside_pilot_cites:
  - ButlerT12
  flags:
  - 'fact restating several series results: derived from them'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
The visible matter is the derived Standard Model generation \cite{ButlerT12}; the three pairs of the Fock structure of a conformal spinor (the twistor Fock structure) are a Witt decomposition of the complexified conformal ambient \cite[Thm.~5.3]{ButlerT9}, two realised by real hyperbolic planes of $\R^{2,4}$, the third only in $V_{\C}$ \cite[proof of Thm.~3.1]{ButlerT9}; the one-handed listing choice on it is the particle-antiparticle orientation \cite[Prop.~5.6]{ButlerT12}, under that paper's Hypothesis (S), carried here; the condensate's alignment is \cite[Prop.~4.3]{ButlerT13}. Reading the listing choice as the descent's flag is this paper's (Definition \claimref{obj.dark-matter.witt-flag}).

## technical
This fact gathers series results the dark-matter paper relies on. The visible matter is the derived Standard Model generation. The three ladder pairs of the Fock structure of a conformal spinor form a Witt decomposition of the complexified conformal ambient $V_{\C}$: two of the pairs are realised by real hyperbolic planes of $\R^{2,4}$, the third only in $V_{\C}$.

The one-handed listing choice on this structure is the particle-antiparticle orientation, under Hypothesis (S) of the Standard-Model paper, which is carried here as a premise; the condensate's alignment is the one computed in the families paper. The only new step is to read the listing choice as the descent's flag, the Witt flag.

## lay
The dark-matter paper borrows several earlier results of the series. The ordinary matter we see is one generation of the Standard Model as derived earlier. A basic spinor state of the conformal algebra carries three paired ladder operations; two of the pairs can be seen in real geometry and the third only once complex numbers are allowed. Choosing which member of each pair counts as particle rather than antiparticle is a single orientation choice, resting on the Standard-Model paper's Hypothesis (S), which is carried here, and the dark-matter paper reads that choice as a flag on the structure.

## one-liner
Under Hypothesis (S), the derived generation's three-pair Witt structure carries a one-handed listing choice, the particle-antiparticle orientation, which the dark-matter paper reads as the descent's flag.
