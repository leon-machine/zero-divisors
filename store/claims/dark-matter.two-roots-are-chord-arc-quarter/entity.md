---
id: dark-matter.two-roots-are-chord-arc-quarter
kind: claim
version: 4
title: The two roots are the chord and the arc of a quarter turn
status: proved
region: dark-matter
subject: dark-matter
tags: [counting-rules, dark-matter-ratio]
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
derivations:
- name: main
  uses:
  - dark-matter.total-function-thickness@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_chord_and_arc
- kind: check
  ref: check.py::check_totals_agree_compositions_differ
- kind: check
  ref: check.py::check_both_poles_excluded
locators:
  paper: T14
  number: Prop 7.16
  label: prop:pole
  line: 1011
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: chord and arc of a quarter turn, equal totals with exchanged compositions, and the both-pole totals 5.729 and 7.182 excluded. Version 2 -> 3. Check entries synced with check.py: +0, -1 (removed check_cells_measure_the_radius). Version 3 -> 4.'
  env: proposition
  context_refs:
  - dark-matter.total-function-thickness
  unresolved_refs:
  - rem:forms
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.total-function-thickness
    note: 'Added the total-as-a-function-of-thickness result because the agreement of the two totals is
      its exchange symmetry and the both-pole values are its evaluations; R2 not added, since the claim
      describes what R2 selects rather than assuming it. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.total-function-thickness
---

## formal
In the sphere form of the rule, represent the five-dimensional tower's spacetime by a sphere of radius $R$ with our spacetime as its equator. The region between the equator and one pole has extent $R$ along the polar axis (the chord) and $\tfrac{\pi R}{2}$ along the surface (the arc). With $R = d_{b}$: counting the tower's matter per unit chord over that region is the unit-ball rule, $c = 1$; counting it per unit arc is the exchanged assignment, $c = \tfrac{\pi}{2}$; and the two totals agree because Proposition \claimref{dark-matter.total-function-thickness}(i) exchanges them, while their compositions differ (Remark \ref{rem:forms}). R2 selects the chord: its cells are unit balls of the tower's flat space, whose measure along the added direction is the radius. Between the equator and both poles the values are $c = 2$ and $c = \pi$, giving $5.729$ and $7.182$, both excluded.

## technical
In the sphere form of the rule the five-dimensional tower's spacetime is a sphere of radius $R$ with ours as its equator. Between the equator and one pole the region has extent $R$ along the polar axis (the chord) and $\pi R/2$ along the surface (the arc). With $R = d_{b}$, counting the tower's matter per unit chord is the unit-ball rule, thickness $c = 1$, and per unit arc is the exchanged assignment, $c = \pi/2$. The totals agree because
$$T(c) = 1 + \frac{8}{3c} + \frac{16c}{3\pi}$$
satisfies $T(c) = T(\pi/(2c))$, while the compositions differ. R2's cells are unit balls of the tower's flat space, whose measure along the added direction is the radius, so R2 selects the chord. Counting to both poles gives $c = 2$ and $c = \pi$, with $T(2) = 5.729$ and $T(\pi) = 7.182$, both excluded.

## lay
The paper's dark-matter formula has one free length, and two different values of it give exactly the same total. This result shows that the two values are the straight-line distance and the curved distance from the equator of a sphere to its pole. The paper's counting rule, built from flat unit balls, picks the straight line; measuring to both poles instead gives totals well away from what is observed.

## one-liner
The two thicknesses that reproduce the unit-ball total, $c = 1$ and $c = \pi/2$, are the chord and the arc from equator to pole of a sphere of radius $d_{b}$, and R2's unit-ball cells select the chord.
