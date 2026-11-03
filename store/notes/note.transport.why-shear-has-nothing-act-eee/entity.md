---
id: note.transport.why-shear-has-nothing-act-eee
kind: note
version: 1
title: 'Why the shear has nothing to act on: $eee = e$ versus $vvv = 0$'
status: remark
subject: zero-divisors
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
comments_on:
- transport.type-p-self-repairing
- transport.no-go-level-elements
- transport.pseudo-inverse-torsor
locators:
  paper: T01
  number: Rem 6.2
  label: rem:fixedpoint
  line: 1373
---

## formal
The proposition looks too easy to be the analogue of Theorem \claimref{transport.no-go-level-elements}, so it is worth locating exactly where the difficulty of type N disappears. It is not in the shear, which is present on both sides: the pseudo-inverses of a null vector form a torsor under the null rotations (Proposition \claimref{transport.pseudo-inverse-torsor}), and the idempotents sharing the image of $e$ form one under $\mathrm{Hom}$-groups that the stabiliser of $e$ shears in exactly the same unipotent manner (Remark \claimref{note.transport.moore-penrose-boundary-idempotent-side} below). The difference is what the torsor contains. The null vector is not a member of its own repair family, since $v\,v\,v = 0 \neq v$, so equivariance must select from a set with no invariant point; the idempotent is a member of its own, since $eee = e$, so the repair need not lie in the sheared directions at all. One identity separates the two cases. The taxonomy's three transport costs, namely a hyperbolic plane for N (and even then only at the level of points), one generator for C, and nothing for P, are thus not a graded scale of difficulty but three different answers to the same equivariance question, each carrying its own theorem.

## technical
pending

## lay
pending

## one-liner
pending
