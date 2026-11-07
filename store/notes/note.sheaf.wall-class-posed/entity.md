---
id: note.sheaf.wall-class-posed
kind: note
version: 2
title: The wall class, posed
status: remark
subject: walls
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass on Leon''s decisions, a dated bracket on the clock: the rung leaves both clock positions unchanged'
  version: 2
  source: maintainer pass 2026-11-07 (decisions)
comments_on:
- sheaf.infinite-wall-sequence
- sheaf.tame-wall-induction
locators:
  paper: T04
  number: Rem 5.6
  label: rem:wallclass
  line: 744
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Dated bracket added to the paper text (DECISIONS A10): the note says the iteration ''advances the clock''; the rung (+1,+1) leaves d = p - q mod 8 unchanged ((p+1) - (q+1) = p - q), as tower.rigidity-clock-frozen and synthesis.wall-class-one-rung-obstruction say. The paper sentence is kept.'
---

## formal
Degeneracy is conserved: it can be pushed off the physical region, never annihilated globally. This is the first geometric instance of the conservation principle conjectured at the fibre level in \cite[Conj.~7.9]{ButlerT1} (obstructions are moved, never destroyed), and the sharpest open question this paper poses is its measure: to construct a cohomological invariant on $\Sig$, presumably a relative class built from the mod-8 residues of the two competing ascents on the two sides of the wall, whose nonvanishing forces the shadow wall's existence, and whose behaviour under the iteration of Lemma \claimref{sheaf.tame-wall-induction} advances the clock of \cite[\S7]{ButlerT1}. The precise formulation is given in Section \ref{sec:dictionary} among the successor problems. (Status now, 7 November 2026: the rung $(+1,+1)$ shifts both signatures by $(1,1)$ and leaves both clock positions $d = p - q \bmod 8$ unchanged, Theorem \claimref{tower.rigidity-clock-frozen} and Proposition \claimref{synthesis.wall-class-one-rung-obstruction}; the iteration transfers the class to the next shadow wall without advancing the clock, as Conjecture \claimref{sheaf.wall-class} (b) now states.)

## technical
pending

## lay
pending

## one-liner
pending
