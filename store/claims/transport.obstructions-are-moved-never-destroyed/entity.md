---
id: transport.obstructions-are-moved-never-destroyed
kind: claim
version: 2
title: Obstructions are moved, never destroyed
status: conjectured
region: transport
subject: zero-divisors
tags: [degenerate-algebras, obstruction-types]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
review: typed
lineage:
  motivated_by:
  - transport.fusion-occurs-most-once
  - transport.no-transport-terminates
  - sheaf.one-sided-completion
  - sheaf.conservation-degeneracy-located
about:
- obj.transport.obstruction-types
locators:
  paper: T01
  number: Conj 7.9
  label: conj:conservation
  line: 1555
extraction:
  env: conjecture
  context_refs:
  - transport.fusion-occurs-most-once
  - transport.no-transport-terminates
  typing:
    by: ai-typing-pass
    note: 'Conjecture: lineage already present; levels only.'
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: []
    added_about: [obj.transport.obstruction-types]
    verdict: standalone
    note: 'Open conjecture, so nothing proved rests on it (the wall-class conjecture already cites it in lineage); added to motivated_by the one-sided completion theorem and the located conservation of degeneracy, which the statement names as proving the tame corank-one case.'
---

## formal
Proposition \claimref{transport.no-transport-terminates} is the zero-dimensional instance of a principle the transport programme repeatedly meets: a completion never removes degeneracy, it relocates it. We conjecture the following family form. For any family of quadratic forms degenerating tamely along a locus (in the sense of the series' sheaf-theoretic paper \cite{ButlerT4}), any completion of the family that is nondegenerate of constant signature on one side of the locus degenerates on a displaced locus on the other side; no completion is nondegenerate globally. The one-sided completion theorem and shadow wall of that paper prove exactly this for tame corank-one degenerations; the conjecture asserts the pattern is not an artefact of the tame case, and asks for the cohomological invariant that measures it, presumably a class built from the mod-8 residues on the two sides of the wall, the state machine of Proposition \claimref{transport.fusion-occurs-most-once} evaluated in families.

## technical
Conjectured. The fact that no transport terminates is read as the zero-dimensional instance of a family statement: for any family of quadratic forms degenerating tamely along a locus, any completion that is nondegenerate of constant signature on one side of the locus degenerates on a displaced locus on the other side, so no completion is nondegenerate globally. The one-sided completion theorem and shadow wall of the sheaf paper prove this for tame corank-one degenerations.

The conjecture asserts that the pattern is not an artefact of that case, and asks for the cohomological invariant that measures it, presumably a class built from the mod-8 residues on the two sides of the wall.

## lay
Each repair of a failure of division seems to create a new failure somewhere else. This conjecture proposes that the same holds when the geometry varies from place to place: fixing a degeneration on one side of a boundary pushes it to a new boundary on the other side. It has been proved in the simplest cases, and the conjecture also asks what quantity keeps track of the moved obstruction.

## one-liner
Conjecturally, no completion of a degenerating family of quadratic forms is nondegenerate globally: completion relocates the degeneration to a displaced locus rather than removing it.
