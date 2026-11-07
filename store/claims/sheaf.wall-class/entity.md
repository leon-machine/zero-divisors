---
id: sheaf.wall-class
kind: claim
version: 3
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
- name: Claude Opus 5.5
  role: 'maintainer pass, restatement of clause (a) as the one-rung completion and clock wording of (b) at Leon''s decisions'
  version: 3
  source: maintainer pass 2026-11-07 (decisions)
review: typed
lineage:
  motivated_by:
  - sheaf.conservation-degeneracy-absolute-form
  - synthesis.wall-class-one-rung-obstruction
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
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3. Leon''s answer 7 (B4) with decision item A10: clause (a) is restated as the one-rung completion (its torsion part vanishes iff a one-rung completion exists; its coarse part, the clock mismatch, obstructs the strict two-sided completion), since synthesis.wall-class-one-rung-obstruction proves that clause (a) as first posed cannot see torsion in either reading of standard and proves the one-rung version for the pair (w(Sigma), w_1(L)); (b)''s clock wording fixed (A10, from AP1''s items): the rung (+1,+1) shifts both signatures by (1,1) and leaves d = p - q mod 8 unchanged, so both clock positions are unchanged ((p+1) - (q+1) = p - q), as tower.rigidity-clock-frozen and the obstruction theorem say. The obstruction theorem added to lineage; status stays conjectured; the version-2 formal kept under source_formal. Restatement at Leon''s decision.'
  source_formal: |-
    There is a natural invariant of tame walls, built from $w(\Sig)$ and the torsion of the pair $(\shL, N^*\Sig)$, with the properties: (a) it vanishes iff some completion standard outside a collar is nondegenerate on \emph{both} sides (by Theorem \claimref{sheaf.conservation-degeneracy-absolute-form}, it must therefore be nonvanishing whenever both sides are nonempty and the clock positions differ); (b) it is conserved under the wall induction of Lemma \claimref{sheaf.tame-wall-induction}, each iteration transferring it to the next shadow wall while shifting both clock coordinates by the rung; (c) it refines, at sheaf level, the conservation-of-obstruction conjecture of \cite[Conj.~7.9]{ButlerT1}, whose fibre-level content is the mod-8 obstruction of the transport rules. Theorem \claimref{sheaf.conservation-degeneracy-absolute-form} proves the existence half of (a) in signature terms; the conjecture is that the signature mismatch is the coarse part of a finer, torsion-sensitive class whose vanishing is also sufficient.
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
There is a natural invariant of tame walls, built from $w(\Sig)$ and the torsion of the pair $(\shL, N^*\Sig)$, with the properties: (a) its torsion part vanishes iff the wall admits a one-rung completion, a smooth symmetric form on the one-rung bundle $T^*M \oplus \underline{\R}^2$, nondegenerate at every point of $M$, equal to $G \perp H$ outside a collar on one side ($H$ the hyperbolic form on the added plane) and to $G$ plus a definite plane on the other, while its coarse part, the clock mismatch of Theorem \claimref{sheaf.conservation-degeneracy-absolute-form}, obstructs the strict two-sided completion and is nonzero on every tame wall with two nonempty sides; (b) it is conserved under the wall induction of Lemma \claimref{sheaf.tame-wall-induction}, each iteration transferring it to the next shadow wall, the rung shifting both signatures by $(1,1)$ and leaving both clock positions unchanged; (c) it refines, at sheaf level, the conservation-of-obstruction conjecture of \cite[Conj.~7.9]{ButlerT1}, whose fibre-level content is the mod-8 obstruction of the transport rules. Theorem \claimref{synthesis.wall-class-one-rung-obstruction} proves (a) for the pair $W(\Sig) = (w(\Sig), w_{1}(\shL))$ on one rung (a one-rung completion, one-sided or two-sided, exists iff $w_{1}(\shL) = 0$), and shows that the clause as first posed, vanishing iff some completion standard outside a collar is nondegenerate on both sides, can be met by no torsion-sensitive class in either reading of ``standard''; the conjecture is that this pair, or a finer torsion-sensitive class that agrees with it on one rung, is natural and satisfies (b) and (c).

## technical
Conjecture: tame walls carry a natural invariant, built from $w(\Sig)$ and the torsion of the pair $(\shL, N^*\Sig)$, which (a) has a torsion part that vanishes exactly when the wall admits a one-rung completion (a form on the cotangent bundle plus one hyperbolic plane, nondegenerate everywhere and standard outside a collar, hyperbolic on one side and definite on the other) and a coarse part, the clock mismatch, that obstructs the strict two-sided completion and is never zero on a two-sided wall; (b) is conserved under the wall induction, passing to each shadow wall, the rung shifting both signatures by $(1,1)$ and leaving both clock positions unchanged; and (c) refines at sheaf level the conservation-of-obstruction conjecture, whose fibre-level content is the mod-8 obstruction of the transport rules.

The one-rung obstruction theorem proves (a) on one rung for the pair of the signature mismatch and $w_{1}(\shL)$, and shows that the clause as first posed (vanishing exactly when some completion standard outside a collar is nondegenerate on both sides) can be met by no torsion-sensitive class. The conjecture is that this pair, or a finer torsion-sensitive class agreeing with it on one rung, is natural and satisfies (b) and (c).

## lay
At a mild (tame) wall whose two sides are both present, every repair that keeps the original setting leaves degeneracy somewhere, and a mismatch of signatures explains why; a twisting invariant cannot change that. Adding one extra pair of directions (a rung) changes the picture: a later result shows such a one-rung repair succeeds exactly when a particular twisting of the wall is absent. This conjecture proposes that the signature mismatch and that twisting together form a natural invariant of the wall, carried unchanged from each wall to the next shadow wall, and refining the series' conservation-of-obstruction conjecture.

## one-liner
Conjecturally, tame walls carry a natural class, the clock mismatch with a torsion part, whose torsion part vanishes exactly when a one-rung completion exists (proved on one rung) and which is conserved under wall induction, the rung leaving both clock positions unchanged.
