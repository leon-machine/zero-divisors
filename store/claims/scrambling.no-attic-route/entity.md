---
id: scrambling.no-attic-route
kind: claim
version: 1
title: The no-attic route
status: proved
region: scrambling
subject: entropy
tags: [open-problem, entropy-premises]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
  uses:
  - sheaf.one-sided-completion-singularity@4
  - singularity.no-attic-derived-model@6
  - tower.answers-iteration-question@5
checked_by:
- kind: proof
  derivation: main
locators:
  paper: T08
  number: Asm 6.3
  label: asm:noattic
  line: 932
extraction:
  env: assembly
  context_refs:
  - tower.answers-iteration-question
  outside_pilot_cites:
  - ButlerT4
  - ButlerT5
  flags:
  - no proof environment found
  typing:
    by: ai-typing-pass
    added:
    - sheaf.one-sided-completion-singularity
    - singularity.no-attic-derived-model
    - tower.answers-iteration-question
    note: 'Assembly with no proof environment: given the source''s ''follows from the three cited imports''
      proof; the section-level citations of the sheaf and singularity papers were mapped to the singularity
      completion theorem (localised ladder pair, no shadow wall) and the singularity paper''s no-attic
      proposition, which is the mapping least certain. Levels pass: conditions already kept.'
---

## formal
T5's eviction theorem runs on an axiom (A), that modes exiting the window deposit their correlations in the window-radiation accounting, with no third sector. The derivation route, assembled from the series' theorems: by the localisation provided by the wall results, operator-valued degrees of freedom exist within the physical closure only where division fails (the window mode space and the radiation's partner modes are the only q-number sectors) \cite[\S 5 and \S 8]{ButlerT4}, \cite[\S 10--11]{ButlerT5}; and by the iteration corollary of the tower paper T3, one ascent completes the description on the physical closure, with no further rungs demanded there \cite[Cor.~6.2]{ButlerT3}: there is no further completion in which a third sector (an attic) could lie. Hence (A)'s content reduces to the \emph{exhaustiveness} of the localisation (the no-remnant, closure-completeness claim), exactly as T5's own derivation records; that exhaustiveness remains the conjectural core, inherited and named, and this assembly's contribution is to have isolated it: everything else in (A) is theorem-backed.

\smallskip
\noindent\emph{The derivation, step by step.} A violation of (A) requires a q-number sector outside the localisation's inventory, which the cited theorems forbid on the physical closure given exhaustiveness; the three imports are cited in the statement.

## technical
The eviction theorem for the boundary modes rests on an axiom (A): modes leaving the window deposit their correlations in the window and radiation accounting, with no third sector. The wall results localise operator-valued degrees of freedom on the physical closure to where division fails, the window modes and the radiation's partner modes, and one ascent completes the description on the physical closure, leaving no further completion where a third sector (an attic) could lie.

Assembled, these reduce the content of (A) to the exhaustiveness of the localisation, the no-remnant or closure-completeness claim. That exhaustiveness remains the conjectural core; everything else in (A) is backed by theorems.

## lay
A key step in the framework's account of black-hole evaporation assumes there is no hidden attic where information could be stored apart from the hole's interior modes and the outgoing radiation. Combining earlier results shows that this assumption comes down to one remaining question: whether the known places where quantum degrees of freedom can live are the only ones. That question is still open, but it is now isolated.

## one-liner
Assembled theorems reduce the no-third-sector axiom (A) to the exhaustiveness of the wall localisation, which remains the conjectural core.
