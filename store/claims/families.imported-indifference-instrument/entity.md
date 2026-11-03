---
id: families.imported-indifference-instrument
kind: claim
version: 2
title: 'Imported: the indifference instrument'
status: proved
region: families
subject: programme
tags: [indifference]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
review: typed
derivations:
- name: main
  assumes:
  - scrambling.indifference-structural-premise-series@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
locators:
  paper: T13
  number: Fact 2.5
  label: fact:indifference
  line: 597
extraction:
  typing:
    by: ai-typing-pass
    removed:
    - scrambling.principality-indifference-sphere
    note: 'The sphere theorem is cited only as an application of the principle, not a premise of this
      restatement; the principle itself is declared a structural premise rather than a theorem, so its
      proved status (and hence this Fact''s) is a doubt left for review, and no standard route applies.
      Hypothesis pass: moved scrambling.indifference-structural-premise-series from uses to assumes, now
      that it is a postulate. Levels pass: technical, lay and one-liner now say the instrument reading
      is the families paper''s own; the review''s point that this premise-plus-reading Fact carries status
      proved is left for review, since this pass does not change status.'
  env: fact
  context_refs:
  - scrambling.indifference-structural-premise-series
  - scrambling.principality-indifference-sphere
  flags:
  - 'fact restating several series results: derived from them'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - scrambling.indifference-structural-premise-series
---

## formal
The framework forbids uncaused structure: a construction may not carry distinctions (partitions, assignments, orderings) that nothing in the framework determines; it is a structural premise of the series, not a theorem, and is flagged as such wherever it is used. The reading this paper makes of it, stated here so that it can be examined: the instrument equates weights along symmetry orbits and forbids selections nothing causes; it never equates norms between inequivalent irreducible components, which no symmetry relates. \emph{Provenance:} \cite[Principle~5.4]{ButlerT8}, with the principality of the fuzzy sphere \cite[Thm.~5.5]{ButlerT8} as the use of it that the proof there requires; the reading is this paper's.

## technical
Indifference is the series' structural premise, not a theorem: no construction may carry a distinction (a partition, an assignment, an ordering) that nothing in the framework determines. This Fact imports that premise and fixes how it is read when used as an instrument on weights.

The reading has two halves. Positively, it equates weights along symmetry orbits: if a symmetry $g$ of the framework relates components $c$ and $g \cdot c$, then $w(g \cdot c) = w(c)$, and it forbids any selection among them that nothing causes. Negatively, it never equates norms between inequivalent irreducible components, since no symmetry relates them. The reading is the families paper's own, stated so that it can be examined, and every use of it is flagged as resting on the premise.

## lay
The series assumes that nature does not make arbitrary choices: if nothing in the theory tells two things apart, the theory may not treat them differently. This entry says how the families paper itself reads that assumption in practice. Things related by a symmetry must be given equal weight, but things that are genuinely different are never forced to match. It is an assumption of the programme, not something it proves.

## one-liner
On the families paper's reading, indifference, a structural premise, equates weights only along symmetry orbits and never equates inequivalent irreducible components.
