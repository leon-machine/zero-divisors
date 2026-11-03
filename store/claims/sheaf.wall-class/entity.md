---
id: sheaf.wall-class
kind: claim
version: 2
title: The wall class
status: conjectured
region: sheaf
subject: walls
tags: [degenerate-algebras]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
lineage:
  motivated_by:
  - sheaf.conservation-degeneracy-absolute-form
  - sheaf.tame-wall-induction
  - transport.obstructions-are-moved-never-destroyed
about:
- obj.sheaf.collar-data-coupling
locators:
  paper: T04
  number: Conj 7.2
  label: conj:wallclass
  line: 835
extraction:
  env: conjecture
  context_refs:
  - sheaf.conservation-degeneracy-absolute-form
  - sheaf.tame-wall-induction
  - transport.obstructions-are-moved-never-destroyed
  typing:
    by: ai-typing-pass
    note: 'Conjecture with lineage already set from its three context references; no edges or status change.
      Levels pass: the lay level no longer says every repair of any degenerate wall fails; it now keeps
      the tame-wall setting and the conditions (both sides nonempty, clock positions differ) under which
      the proved signature half applies.'
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: []
    added_about: [obj.sheaf.collar-data-coupling]
    verdict: standalone
    note: 'Open conjecture with its lineage already set; nothing proved may rest on it; about added for the completions standard outside a collar that clause (a) quantifies over.'
---

## formal
There is a natural invariant of tame walls, built from $w(\Sig)$ and the torsion of the pair $(\shL, N^*\Sig)$, with the properties: (a) it vanishes iff some completion standard outside a collar is nondegenerate on \emph{both} sides (by Theorem \claimref{sheaf.conservation-degeneracy-absolute-form}, it must therefore be nonvanishing whenever both sides are nonempty and the clock positions differ); (b) it is conserved under the wall induction of Lemma \claimref{sheaf.tame-wall-induction}, each iteration transferring it to the next shadow wall while shifting both clock coordinates by the rung; (c) it refines, at sheaf level, the conservation-of-obstruction conjecture of \cite[Conj.~7.9]{ButlerT1}, whose fibre-level content is the mod-8 obstruction of the transport rules. Theorem \claimref{sheaf.conservation-degeneracy-absolute-form} proves the existence half of (a) in signature terms; the conjecture is that the signature mismatch is the coarse part of a finer, torsion-sensitive class whose vanishing is also sufficient.

## technical
Conjecture: tame walls carry a natural invariant, built from $w(\Sig)$ and the torsion of the pair $(\shL, N^*\Sig)$, which (a) vanishes exactly when some completion standard outside a collar is nondegenerate on both sides, and so is nonzero whenever both sides are nonempty and the clock positions differ; (b) is conserved under the wall induction, passing to each shadow wall with both clock coordinates shifted by the rung; and (c) refines at sheaf level the conservation-of-obstruction conjecture, whose fibre-level content is the mod-8 obstruction of the transport rules.

The absolute form of conservation of degeneracy already proves one half of (a) in signature terms. The conjecture is that this signature mismatch is the coarse part of a finer, torsion-sensitive class whose vanishing is also sufficient.

## lay
At a mild (tame) wall whose two sides are both present and carry different clock positions, every repair leaves degeneracy somewhere, and a mismatch of signatures explains why. This conjecture proposes a finer invariant of the wall, sensitive to subtle topological twisting, that would detect exactly when a repair can succeed on both sides. It would be carried unchanged from each wall to the next shadow wall.

## one-liner
Conjecturally, tame walls carry a natural torsion-sensitive class, conserved under wall induction, whose vanishing is equivalent to the existence of a completion nondegenerate on both sides.
