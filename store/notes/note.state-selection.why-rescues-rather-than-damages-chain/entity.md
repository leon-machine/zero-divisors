---
id: note.state-selection.why-rescues-rather-than-damages-chain
kind: note
version: 2
title: Why this rescues rather than damages the chain
status: remark
subject: descent
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-state-selection, the series'' standard disclaimer'
comments_on:
- singularity.exact-equilibrium-over-determines-boundary-modes
- singularity.ascended-marginals-are-diagonal
locators:
  paper: T05-state-selection
  number: Rem 7.2
  label: rem:rescue
  line: 351
extraction:
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: The state-selection note's duplicates of T05 entities were retired to tombstones.yaml (merged into the T05
      entities). References moved from the retired state-selection.ascended-marginals-are-diagonal, state-selection.exact-equilibrium-over-determines-ledger
      to singularity.ascended-marginals-are-diagonal, singularity.exact-equilibrium-over-determines-boundary-modes;
      version 1 -> 2.
---

## formal
Read carelessly, Theorem \claimref{singularity.exact-equilibrium-over-determines-boundary-modes} looks like an obstruction: the state that thermality wants is the state that has no information in it. Read carefully, it is the reason the architecture of this note matters. Had per-mode thermality been derived from the exact equilibrium condition, as hypothesis (ii) suggests, then thermality and correlation would have been in direct competition and the chain could not have had both. Theorem \claimref{singularity.ascended-marginals-are-diagonal} shows that per-mode thermality does not rest on equilibrium at all: it rests on parity, which survives an arbitrary non-stationary history. The correct state class for the chain is therefore
\[
\bigl\{\ \text{even states, per-mode populations at } \beta = 2\pi/\kappa, \ \text{correlations free}\ \bigr\},
\]
a class in which every single quantum is exactly thermal and the joint state is free to carry everything the evaporation writes. That is exactly the class the finite-ledger model of \cite[\S 12]{ButlerT5} inhabits, and \cite[Lem.~12.1]{ButlerT5} is the model's proof that it does.

## technical
pending

## lay
pending

## one-liner
pending
