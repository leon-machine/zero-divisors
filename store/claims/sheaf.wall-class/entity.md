---
id: sheaf.wall-class
kind: claim
version: 4
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
- name: Claude Fable 5.2
  role: 'restatement of clauses (a) and (c) at Leon''s decision: the coarse part named as the signature jump with the clock mismatch as its residue, clause (c) as the wall''s instance of the eigenbundle class of the transfer clause, with what is proved towards it'
  version: 4
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-leads)'
amendments:
- version: 4
  kind: restatement
  defect: 'clause (c) referred to the first paper''s conservation-of-obstruction conjecture, which is refuted as stated (its invariant is not built from residues modulo eight, the fibre-level content the clause named); clause (a) named the coarse part as the clock mismatch, which is the residue of the signature jump and not the jump'
review: typed
lineage:
  motivated_by:
  - sheaf.conservation-degeneracy-absolute-form
  - synthesis.wall-class-one-rung-obstruction
  - sheaf.tame-wall-induction
  - transport.obstructions-are-moved-never-destroyed
  - synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump
  - synthesis.wall-rung-count-is-height-of-dying-line-class
  - synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line
about:
- obj.sheaf.collar-data-coupling
locators:
  paper: T04
  number: Conj 7.2
  label: conj:wallclass
  line: 835
extraction:
  maintainer_pass_2026_11_18_leads:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 3 -> 4. Leon''s decision D4 of 18 November 2026: clauses (a) and (c) restated as drafted, checked against synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line as accepted (version 1). Where the draft said more than the stored result the stored result is followed: the clock mismatch 2 is cited from clause (1) of the one-rung theorem, the signature jump (1,-1) is stated for side signatures (p,q) and (p-1,q+1), the collar comparison is stated under that result''s hypotheses (compact wall, product collar, corank one), and the sheaf-level sentence quotes clause (4) of the rung-count theorem. Clause (b) and the status (conjectured) unchanged; the three cited results added to lineage; the version-2 formal stays under source_formal.'
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
There is a natural invariant of tame walls, built from $w(\Sig)$ and the torsion of the pair $(\shL, N^*\Sig)$, with the properties: (a) its torsion part vanishes iff the wall admits a one-rung completion, a smooth symmetric form on the one-rung bundle $T^*M \oplus \underline{\R}^2$, nondegenerate at every point of $M$, equal to $G \perp H$ outside a collar on one side ($H$ the hyperbolic form on the added plane) and to $G$ plus a definite plane on the other, while its coarse part, the signature jump across the wall ($(1,-1)$ on a wall whose sides have signatures $(p,q)$ and $(p-1,q+1)$), whose residue is the clock mismatch $2$ of clause (1) of Theorem \claimref{synthesis.wall-class-one-rung-obstruction}, obstructs the strict two-sided completion (Theorem \claimref{sheaf.conservation-degeneracy-absolute-form}) and is nonzero on every tame wall with two nonempty sides; (b) it is conserved under the wall induction of Lemma \claimref{sheaf.tame-wall-induction}, each iteration transferring it to the next shadow wall, the rung shifting both signatures by $(1,1)$ and leaving both clock positions unchanged; (c) it is the wall's instance of the eigenbundle class of clause (4) of Theorem \claimref{synthesis.strict-completions-exist-exactly-when-the-signature-does-not-jump}, the class whose opposite every completion that is nondegenerate at every point must carry on the eigenbundles of its exterior forms (transfer). Clause (c) in this form takes the place of its first form, a refinement at sheaf level of the conservation-of-obstruction conjecture of \cite[Conj.~7.9]{ButlerT1}, which is refuted as stated (\claimref{transport.obstructions-are-moved-never-destroyed}). At the level of the Clifford sheaves the jump across the wall depends on $\shL$ only through $\shL \oplus \shL$, the pair $W(\Sig)$ determines that jump, and on the torus wall the pair is strictly finer than it (clause (4) of Theorem \claimref{synthesis.wall-rung-count-is-height-of-dying-line-class}). Theorem \claimref{synthesis.wall-class-one-rung-obstruction} proves (a) for the pair $W(\Sig) = (w(\Sig), w_{1}(\shL))$ on one rung (a one-rung completion, one-sided or two-sided, exists iff $w_{1}(\shL) = 0$), and shows that the clause as first posed, vanishing iff some completion standard outside a collar is nondegenerate on both sides, can be met by no torsion-sensitive class in either reading of ``standard''; the conjecture is that this pair, or a finer torsion-sensitive class that agrees with it on one rung, is natural and satisfies (b) and (c). Towards (c): on a compact wall with a product collar, where the form has corank one and the two sides have signatures $(p,q)$ and $(p-1,q+1)$, the eigenbundles of the cometric on the two sides, compared across the collar, differ by the dying line $\shL$, whose rank is the signature jump and whose isomorphism class is $w_{1}(\shL)$, and every two-sided completion that is nondegenerate at every point and standard outside the interior of the collar carries the opposite on the eigenbundles of its exterior forms (Theorem \claimref{synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line}); so, relative across the collar, the class of (c) carries exactly the information of the pair $W(\Sig)$, with $w(\Sig)$ read as the clock mismatch. Not shown: the class relative to the whole base, which can carry further information from the exterior; that the pair is natural; and conservation under the wall induction, clause (b).

## technical
Conjecture: tame walls carry a natural invariant, built from $w(\Sig)$ and the torsion of the pair $(\shL, N^*\Sig)$, which (a) has a torsion part that vanishes exactly when the wall admits a one-rung completion (a form on the cotangent bundle plus one hyperbolic plane, nondegenerate everywhere and standard outside a collar, hyperbolic on one side and definite on the other) and a coarse part, the signature jump across the wall (its residue is the clock mismatch $2$), that obstructs the strict two-sided completion and is never zero on a two-sided wall; (b) is conserved under the wall induction, passing to each shadow wall, the rung shifting both signatures by $(1,1)$ and leaving both clock positions unchanged; and (c) is the wall's instance of the eigenbundle class of the transfer clause of the strict-completions theorem, the class whose opposite every completion that is nondegenerate everywhere carries on the eigenbundles of its exterior forms. Clause (c) in this form replaces its first form, a refinement of the first paper's conservation-of-obstruction conjecture, which is refuted as stated.

The one-rung obstruction theorem proves (a) on one rung for the pair of the signature mismatch and $w_{1}(\shL)$, and shows that the clause as first posed (vanishing exactly when some completion standard outside a collar is nondegenerate on both sides) can be met by no torsion-sensitive class. The conjecture is that this pair, or a finer torsion-sensitive class agreeing with it on one rung, is natural and satisfies (b) and (c).

Towards (c), proved for compact corank-one walls with a product collar and side signatures $(p,q)$ and $(p-1,q+1)$: compared across the collar the eigenbundle class is the dying line $\shL$ (rank the signature jump, isomorphism class $w_{1}(\shL)$), two-sided completions that are nondegenerate everywhere carry its opposite on their exterior forms, and so the class relative across the collar carries exactly the information of the pair. The class relative to the whole base, naturality and conservation under the wall induction remain conjectured.

## lay
At a mild (tame) wall whose two sides are both present, every repair that keeps the original setting leaves degeneracy somewhere, and a mismatch of signatures explains why; a twisting invariant cannot change that. Adding one extra pair of directions (a rung) changes the picture: a later result shows such a one-rung repair succeeds exactly when a particular twisting of the wall is absent. This conjecture proposes that the signature mismatch and that twisting together form a natural invariant of the wall, that it is carried unchanged from each wall to the next shadow wall, and that it is the wall's share of the twist that every repair of a degenerating geometry must carry, in mirror image, in what it adds. A later result shows that, compared across a wall, the invariant and that twist carry the same information; the rest is conjectured. The first paper's conservation-of-obstruction conjecture is false as first worded, and this is the form in which it is conjectured to survive.

## one-liner
Conjecturally, tame walls carry a natural class, the signature jump with a torsion part, whose torsion part vanishes exactly when a one-rung completion exists (proved on one rung) which is conserved under wall induction, the rung leaving both clock positions unchanged, and which is the wall's instance of the eigenbundle class that completions carry in mirror image (relative across the collar the two carry the same information, proved).
