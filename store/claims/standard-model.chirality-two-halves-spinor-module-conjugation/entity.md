---
id: standard-model.chirality-two-halves-spinor-module-conjugation
kind: claim
version: 6
title: 'Chirality: the two halves of the spinor module, and conjugation as duality'
status: proved
region: standard-model
subject: standard-model
tags: [chirality, spinor-modules, representation-theory]
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
  - standard-model.quarks-leptons-two-level-fermion-content@5
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12.py
  tags:
  - label:prop:chirality
- kind: check
  ref: check.py::check_halves_inequivalent
- kind: check
  ref: check.py::check_conjugation_is_duality
locators:
  paper: T12
  number: Prop 5.6
  label: prop:chirality
  line: 1140
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the content and hypercharges of the two chirality halves from the generator, their inequivalence and one-handed colour, and the wedge-pairing duality with its weights. Version 5 -> 6.'
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: STRUCTURE M11
    open_problem: op.small-findings
    note: 'The extraction note called S and S'' the six-dimensional chirality halves; each is four-dimensional (the six is the dimension of the generating space of Cl(2,4)). Corrected there, and the technical level now says the chirality meant is that of the ascended algebra, not the spacetime chirality at a point (Som, Spi).'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted T, T'', the single-twistor sector and the twistor-level doublets to S = Lambda^even W, S'' = Lambda^odd W and the sector of a single conformal spinor, at every level. The halves here are the four-dimensional chirality halves of the eight-dimensional Dirac module of the ascended algebra (whose generating space is six-dimensional), not TWGA''s E = +-1 split inside S, so no E reading was added. The proof had no twistor language.'
  source_title: |-
    Chirality: the two halves of the spinor module, and conjugation as duality
  source_formal: |-
    The twistor space $\T = \Lambda^{\mathrm{even}}W$ and its partner $\T' = \Lambda^{\mathrm{odd}}W$ are the two chirality halves of the ascended Dirac module (Fact \claimref{standard-model.imported-pair-systems-two-chirality-halves}), and the single-twistor sector $\Lambda^{\bullet}W$ is their direct sum. Under $S(U(2) \times U(3))$ the two halves carry different content: $\T$ carries $(1)_{0} \oplus (\bar{3})_{-2/3}$ and $\T'$ carries $(3)_{-1/3} \oplus (1)_{-1}$ (Proposition \claimref{standard-model.quarks-leptons-two-level-fermion-content}(3)), so the two halves are inequivalent representations of the group: the chirality split is visible to the internal symmetry, not only to the grading. The singlet spectrum listed by a single handedness is Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency}(2)'s, and in particular the colour content $3 \oplus \bar{3}$ of the two halves becomes $\bar{3} \oplus \bar{3}$ under it, which is the conjugation of Remark \ref{rem:wound}. Moreover the conjugation is an operation inside the pair system: the dual of the grade-$k$ state is the grade-$(3-k)$ state with the full-system phase removed, $(\Lambda^{k}W)^{*} \cong \Lambda^{3-k}W \otimes (\Lambda^{3}W)^{*}$, of weight $+2k$; and the two twistor-level doublets of Proposition \claimref{standard-model.quarks-leptons-two-level-fermion-content}(2) are each other's duals, $(\C^{2} \otimes \Lambda^{0}W)^{*} \cong \C^{2} \otimes \Lambda^{3}W$, and under (S) have opposite parity. Under (S) they are therefore one doublet and its antiparticle, not two candidates, and Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency}(1)'s listing choice is the particle-antiparticle orientation of Remark \ref{rem:wound}.
  env: proposition
  unresolved_refs:
  - rem:wound
  typing:
    by: ai-typing-pass
    removed:
    - standard-model.hypercharge-global-form-pair-counting-consistency
    note: 'Removed the hypercharge theorem to break the E301 cycle: this proposition only reads that theorem''s
      one-handed listing as an identification, while its computations rest on the content proposition,
      the pair-system fact and the Cauchy decomposition, whereas the hypercharge theorem does use this
      proposition''s duality. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics added because
      its statement holds under Hypothesis (S). Levels pass: conditions already kept.'
    added:
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
The conformal spinor space $\CS = \Lambda^{\mathrm{even}}W$ (twistor space) and its partner $\CSm{} = \Lambda^{\mathrm{odd}}W$ are the two chirality halves of the ascended Dirac module (Fact \claimref{standard-model.imported-pair-systems-two-chirality-halves}), and the sector of a single conformal spinor $\Lambda^{\bullet}W$ is their direct sum. Under $S(U(2) \times U(3))$ the two halves carry different content: $\CS$ carries $(1)_{0} \oplus (\bar{3})_{-2/3}$ and $\CSm{}$ carries $(3)_{-1/3} \oplus (1)_{-1}$ (Proposition \claimref{standard-model.quarks-leptons-two-level-fermion-content}(3)), so the two halves are inequivalent representations of the group: the chirality split is visible to the internal symmetry, not only to the grading. The singlet spectrum listed by a single handedness is Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency}(2)'s, and in particular the colour content $3 \oplus \bar{3}$ of the two halves becomes $\bar{3} \oplus \bar{3}$ under it, which is the conjugation of Remark \ref{rem:wound}. Moreover the conjugation is an operation inside the pair system: the dual of the grade-$k$ state is the grade-$(3-k)$ state with the full-system phase removed, $(\Lambda^{k}W)^{*} \cong \Lambda^{3-k}W \otimes (\Lambda^{3}W)^{*}$, of weight $+2k$; and the two doublets at the level of one conformal spinor of Proposition \claimref{standard-model.quarks-leptons-two-level-fermion-content}(2) are each other's duals, $(\C^{2} \otimes \Lambda^{0}W)^{*} \cong \C^{2} \otimes \Lambda^{3}W$, and under (S) have opposite parity. Under (S) they are therefore one doublet and its antiparticle, not two candidates, and Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency}(1)'s listing choice is the particle-antiparticle orientation of Remark \ref{rem:wound}.

## technical
The conformal spinor space $\CS = \Lambda^{\mathrm{even}}W$ and its partner $\CSm{} = \Lambda^{\mathrm{odd}}W$ are the two chirality halves of the ascended Dirac module, the parity of the Fock grade, each four-dimensional (not the spacetime chiral halves $\Som$, $\Spi$ at a point, which split $\CS$). Under $S(U(2) \times U(3))$ they carry inequivalent content, $(1)_{0} \oplus (\bar{3})_{-2/3}$ on $\CS$ and $(3)_{-1/3} \oplus (1)_{-1}$ on $\CSm{}$, so the internal symmetry sees the chirality split, not only the grading. Listing by a single handedness turns the colour content $3 \oplus \bar{3}$ of the two halves into $\bar{3} \oplus \bar{3}$.

Conjugation is a duality inside the pair system: $(\Lambda^{k}W)^{*} \cong \Lambda^{3-k}W \otimes (\Lambda^{3}W)^{*}$, of weight $+2k$, and the two doublets at the level of one conformal spinor are each other's duals, $(\C^{2} \otimes \Lambda^{0}W)^{*} \cong \C^{2} \otimes \Lambda^{3}W$. Under (S) they have opposite parity, so they are one doublet and its antiparticle, and the choice of listing is the particle-antiparticle orientation.

## lay
The internal states of a single basic spinor state of the conformal algebra split into two halves of opposite handedness, and the Standard Model symmetry treats the two halves differently, so handedness is visible to the forces. Describing everything in one handedness, as is conventional in particle physics, turns the colour pattern into the observed one. Under the slot-statistics hypothesis, the two candidate doublets are mirror images of each other, a particle and its antiparticle, rather than two separate particles.

## one-liner
The two chirality halves of the sector of a single conformal spinor carry inequivalent $S(U(2) \times U(3))$ content, and conjugation is duality inside the pair system, so under (S) the two doublets at that level are one doublet and its antiparticle.
