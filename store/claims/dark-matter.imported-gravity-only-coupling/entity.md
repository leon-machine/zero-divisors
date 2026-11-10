---
id: dark-matter.imported-gravity-only-coupling
kind: claim
version: 4
title: Gravity-only coupling at first order, restated from the acoustic no-go
status: proved
region: dark-matter
subject: dark-matter
tags: [no-go, bosonisation]
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
- name: Claude Opus 5.5
  role: 'maintainer pass, citation of the sector decomposition at Leon''s decisions'
  version: 4
  source: maintainer pass 2026-11-07 (decisions)
review: draft
about:
- obj.dark-matter.frozen-phase-operators
derivations:
- name: main
  uses:
  - dark-energy.acoustic-no-go-one-way-grip@6
  - dark-energy.lift-inherits-no-go-steps-itemised@2
  - dark-energy.conclusion-does-not-depend-ontology-level@1
  assumes:
  - dark-matter.p1-single-frozen-point@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
locators:
  paper: T14
  number: Fact 2.6
  label: fact:acoustic
  line: 116
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: dark-energy.acoustic-no-go-one-way-grip repinned 5 -> 6 after reviewing its H2 restatement (the converse of the equivalence principle now reads no channel outside the C-even neutral sector, where it said no other channel); the use here holds as cited.'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. Decision item D8 (routine): ''its only contact with us'' is the sector decomposition, Definition obj.dark-matter.frozen-phase-operators (the operational reading of P1), not P1''s formal (one metric and one flag); the formal and the proof now cite the Definition (about link added), and the assumes edge to P1 stays. Wording and an about link; statement unchanged.'
  open_problem: op.dark-sector-scopes
  env: fact
  outside_pilot_cites:
  - ButlerT10
  flags:
  - 'fact restating series results: derived from them'
  - citation taken from inline provenance (no \cite)
  typing:
    by: ai-typing-pass
    note: 'Imported; levels only. Levels pass: the one-liner now carries the mixed level and the Indifference
      and (Q) conditions it had dropped; the lay level names both premises and the s-wave restriction.'
  scopes_pass:
    by: ai-dark-sector-scopes-pass
    date: 2026-10-22
    session: 2026-10-22-toe
    open_problem: op.dark-sector-scopes
    ai_involved: 'yes'
    note: >-
      Version 1 typed this fact as an import with no premises, so the Indifference premise and
      premise (Q) that its own text names did not reach its dependants through the graph. Version 2
      retypes it as a restatement of the series' own acoustic chain (T10 Prop 5.2, the lift assembly
      and the ontology proposition), so every condition of that chain reaches holds_given of the
      dependants. The source states the coupling statement at first order, and that qualifier is
      restored. The closing "does nothing else observable" holds only with Premise P1, which makes
      the metric-forming correlations the sector's only contact with ours; P1 is not a premise of
      this fact and is named where the superselection theorem adds it.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Version 3 adds the assumes edge to dark-matter.p1-single-frozen-point: the closing clause ("does nothing else observable at first order") is conditional on P1, which the formal level and proof already named, and P1 reached this entity only through the superselection theorem; holds_given now tracks it. Statement unchanged; status kept at proved (derived from the T10 chain, as accepted).'
---

## formal
Under the entropy paper's Indifference premise (for the sphere step of the four-dimensional lift) and, wherever the thermal state is used, the singularity paper's premise (Q), and with the other hypotheses the acoustic chain carries: within the s-wave current algebra and its assembled four-dimensional lift, every gauge-charged or charge-conjugation-odd probe has zero linear overlap with the graviton mode, so at first order only the charge-conjugation-even neutral sector couples; in the conformal vacuum its overlap is carried by $T$ alone, and Proposition \claimref{dark-energy.conclusion-does-not-depend-ontology-level} reads it as the one coupling sector, stress-energy (Proposition \claimref{dark-energy.acoustic-no-go-one-way-grip}, Assembly \claimref{dark-energy.lift-inherits-no-go-steps-itemised}). Hence matter that gravitates on this metric and carries no gauge charge shared with us acts on us, through the metric-forming correlations, by its stress-energy alone, at first order. With Premise \claimref{dark-matter.p1-single-frozen-point}, read operationally as the sector decomposition of Definition \claimref{obj.dark-matter.frozen-phase-operators}, which makes these correlations its only contact with us, it does nothing else observable at first order. \emph{Provenance:} the series' acoustic no-go \cite[\S5]{ButlerT10} restated, at its mixed level.

## technical
Under the Indifference premise (sphere step of the lift) and premise (Q) (the induced thermal state), and with the further hypotheses of the acoustic chain: in the s-wave current algebra and its assembled four-dimensional lift, every gauge-charged or charge-conjugation-odd probe has zero linear overlap with the graviton mode, so at first order only the charge-conjugation-even neutral sector couples. In the conformal vacuum that overlap is carried by the stress tensor alone, and the ontology proposition reads it as the one coupling sector, stress-energy. Matter that gravitates on this metric and shares no gauge charge with us therefore acts on us through the metric-forming correlations by its stress-energy alone, at first order; with Premise P1, which makes these correlations its only contact with us, it does nothing else observable at first order. This is the series' acoustic no-go restated at its mixed level.

## lay
In the framework's spherically averaged (s-wave) description of fields near horizons, with an assembled four-dimensional lift, and under two assumptions of earlier papers in the series (one about how the horizon's spherical structure is built, one about the joint state of the near-horizon modes), the series showed that the structure from which spacetime's geometry is made can be gripped, at first order, only by probes that carry no charge and do not change sign under charge conjugation, which the series reads as energy and momentum. So matter that feels gravity but shares none of our other forces can affect us through that structure only by its weight, to first order. If, as the dark-matter paper's single-frozen-point premise says, that structure is its only contact with us, it has no other effect we could observe at that order.

## one-liner
Under the Indifference premise and premise (Q), matter that gravitates on this metric and shares no gauge charge with us acts on us through the metric-forming correlations only through its stress-energy, at first order, by the series' acoustic no-go restated; with P1 it does nothing else observable at that order.
