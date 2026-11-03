---
id: neutrino.imported-derived-content-singlets
kind: claim
version: 7
title: 'Imported: the derived content and its singlets'
status: proved
region: neutrino
subject: standard-model
tags: [hypercharge-and-anomalies, recovers-known-physics]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T15, deposited version
review: typed
derivations:
- name: main
  uses:
  - standard-model.global-form-quotient-determined@3
  - standard-model.hypercharge-global-form-pair-counting-consistency@5
  - standard-model.quarks-leptons-two-level-fermion-content@5
  - standard-model.raw-representation-content-state-space@3
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_doublet_content
- kind: check
  ref: check.py::check_single_spinor_singlets
- kind: check
  ref: check.py::check_anomaly_conditions_hold_and_determine
- kind: check
  ref: check.py::check_z6_lattice
locators:
  paper: T15
  number: Fact 2.1
  label: fact:content
  line: 554
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the doublet content and the single-spinor singlets from exact characters, the even-grade listing, anomaly freedom and uniqueness, and the Z_6 lattice. Version 5 -> 6. Check strengthened: the Z_6 condition asserted to have index six; off-lattice samples moved to module level. Version 6 -> 7.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the single-twistor sector and Fock space to those of a single conformal spinor at every level and in the provenance proof; the representations and hypercharges are untouched.'
  source_title: |-
    Imported: the derived content and its singlets
  source_formal: |-
    The minimal massive hierarchy's fermion content is $(2,3) \oplus (2,1)$, the doublets under the Standard-Model paper's Hypothesis (S); the single-twistor sector $\Lambda^{\bullet}\C^{3} = 1 \oplus 3 \oplus \bar{3} \oplus 1$, graded zero through three, carries the weight $q = -2k$ at grade $k$ and hence the hypercharge $Y = -k/3$, that is $0, -\tfrac13, -\tfrac23, -1$, unconditionally as a computation on the single-twistor Fock space with the pair-slot factor acting alone (that Fock space is not a subspace of the tensor state space, and under (S) it is the row $j = 0$); listed by the handedness that keeps the even grades, the singlet spectrum is $(1)_{0} \oplus (\bar{3})_{-2/3} \oplus (\bar{3})_{+1/3} \oplus (1)_{+1}$, that is $\nu^{c}, u^{c}, d^{c}, e^{c}$, with the hypercharge-zero singlet at grade zero; the four anomaly conditions hold on this spectrum, and determine it (up to the $u^{c}, d^{c}$ relabelling) given the content, $Y_{Q} = \tfrac16$, and a fourth singlet of hypercharge zero or none; and the physical representations are confined to the $\mathbb{Z}_{6}$ lattice. \emph{Provenance:} \cite[Prop.~5.1, Prop.~5.3, Thm.~5.5, Thm.~4.2]{ButlerT12}; Hypothesis (S) is declared there and is open.
  typing:
    by: ai-typing-pass
    note: 'Kept the four cited series results; Hypothesis (S) has no postulate entity, and the E204 comes
      from the hypercharge theorem outside this list. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: lay now states what the anomaly
      determination is given and that it holds up to the u^c, d^c relabelling.'
    added:
    - standard-model.hyp-s-slot-statistics
  env: fact
  context_refs:
  - standard-model.global-form-quotient-determined
  - standard-model.hypercharge-global-form-pair-counting-consistency
  - standard-model.quarks-leptons-two-level-fermion-content
  - standard-model.raw-representation-content-state-space
  flags:
  - 'fact restating several series results: derived from them'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
The minimal massive hierarchy's fermion content is $(2,3) \oplus (2,1)$, the doublets under the Standard-Model paper's Hypothesis (S); the sector of a single conformal spinor (the single-twistor sector) $\Lambda^{\bullet}\C^{3} = 1 \oplus 3 \oplus \bar{3} \oplus 1$, graded zero through three, carries the weight $q = -2k$ at grade $k$ and hence the hypercharge $Y = -k/3$, that is $0, -\tfrac13, -\tfrac23, -1$, unconditionally as a computation on the Fock space of a single conformal spinor with the pair-slot factor acting alone (that Fock space is not a subspace of the tensor state space, and under (S) it is the row $j = 0$); listed by the handedness that keeps the even grades, the singlet spectrum is $(1)_{0} \oplus (\bar{3})_{-2/3} \oplus (\bar{3})_{+1/3} \oplus (1)_{+1}$, that is $\nu^{c}, u^{c}, d^{c}, e^{c}$, with the hypercharge-zero singlet at grade zero; the four anomaly conditions hold on this spectrum, and determine it (up to the $u^{c}, d^{c}$ relabelling) given the content, $Y_{Q} = \tfrac16$, and a fourth singlet of hypercharge zero or none; and the physical representations are confined to the $\mathbb{Z}_{6}$ lattice. \emph{Provenance:} \cite[Prop.~5.1, Prop.~5.3, Thm.~5.5, Thm.~4.2]{ButlerT12}; Hypothesis (S) is declared there and is open.

## technical
The minimal massive hierarchy's fermion content is the doublets $(2,3) \oplus (2,1)$, under Hypothesis (S). Unconditionally, the sector of a single conformal spinor, $\Lambda^{\bullet}\C^{3} = 1 \oplus 3 \oplus \bar{3} \oplus 1$, carries weight $q = -2k$ at grade $k$, hence $Y = -k/3$, a computation on the Fock space of a single conformal spinor with the pair-slot factor acting alone.

Listed in the handedness that keeps the even grades, the singlets are $(1)_{0} \oplus (\bar{3})_{-2/3} \oplus (\bar{3})_{+1/3} \oplus (1)_{+1}$, that is $\nu^{c}, u^{c}, d^{c}, e^{c}$, with the hypercharge-zero singlet at grade zero. The four anomaly conditions hold on this spectrum and determine it, up to the $u^{c}, d^{c}$ relabelling, given the content, $Y_{Q} = \tfrac16$ and a fourth singlet of hypercharge zero or none; and the physical representations lie on the $\mathbb{Z}_{6}$ lattice.

## lay
The neutrino paper imports the series' derivation of one generation of matter. The quark and lepton doublets come from the structure of two basic spinor states, the lepton doublet only under a stated hypothesis that remains open, and four single-particle states come from one free spinor state. One of those singlets has zero charge, the right-handed neutrino, and it sits at the lowest grade. The anomaly conditions confirm this spectrum and fix it, up to swapping the two coloured singlets, once the doublets, the quark doublet's hypercharge and at most one neutral singlet are given.

## one-liner
The derived generation's singlets are $\nu^{c}, u^{c}, d^{c}, e^{c}$ with $Y = 0, -\tfrac23, \tfrac13, 1$, the hypercharge-zero $\nu^{c}$ at grade zero, while the lepton doublet rests on Hypothesis (S).
