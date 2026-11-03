---
id: dark-matter.p2-indifference
kind: claim
version: 2
title: 'P2: indifference, scoped to sector labels'
status: postulate
region: dark-matter
subject: dark-matter
tags: [premises-p1-p5, indifference, towers-by-residue]
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
locators:
  paper: T14
  number: Premise 2.2
  label: prem:indiff
  line: 100
extraction:
  source_formal: "The descent cannot instantiate uncaused distinctions \\cite[Principle~5.4]{ButlerT8}, \\cite[\\S2]{ButlerT13}: it equates along symmetry orbits and never equates inequivalent components. The residues are inequivalent as soldered algebras (Theorem \\claimref{dark-matter.residue-soldered-invariant-not-algebraic-one}) except along the reversal $r \\mapsto -r$ (exchanging $2 \\leftrightarrow 6$, $1 \\leftrightarrow 7$, $3 \\leftrightarrow 5$, fixing $0$, $4$), so P2 equates along that orbit only; which of $2$, $6$ is visible is declared indexical. Structural premise."
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Version 2 adds the scope Leon adopted, "labels, not states": P2 equates superselection labels of the descent (such as the tower charge), not thermal states within a sector, and the deposited mode set is declared finite, the case in which synthesis.tower-charge-sector-label-temperature-not shows the scoping well defined and the mirror temperature ratio free. The version 1 formal text is kept under source_formal.'
  typing:
    by: ai-typing-pass
    note: "Postulate: no edges to type; levels only."
  env: premise
  context_refs:
  - dark-matter.residue-soldered-invariant-not-algebraic-one
  - scrambling.indifference-structural-premise-series
  outside_pilot_cites:
  - ButlerT13
---

## formal
The descent cannot instantiate uncaused distinctions \cite[Principle~5.4]{ButlerT8}, \cite[\S2]{ButlerT13}: it equates along symmetry orbits and never equates inequivalent components. The residues are inequivalent as soldered algebras (Theorem \claimref{dark-matter.residue-soldered-invariant-not-algebraic-one}) except along the reversal $r \mapsto -r$ (exchanging $2 \leftrightarrow 6$, $1 \leftrightarrow 7$, $3 \leftrightarrow 5$, fixing $0$, $4$), so P2 equates along that orbit only; which of $2$, $6$ is visible is declared indexical. Structural premise.

\emph{Scope: labels, not states.} What P2 equates along the orbit are the sector labels the descent deposits, the superselection labels of the deposited algebra, such as the tower charge (Proposition \claimref{dark-matter.superselected-hence-dark-exactly-stable}); it does not equate thermal states within a selected sector, so it says nothing about the temperatures of the two members of a reversal pair. The deposited mode set is declared finite. In the boundary-mode model of a reversal pair (Hypothesis (B') of Theorem \claimref{synthesis.tower-charge-sector-label-temperature-not}) this scope is well defined: on every finite window the tower charge is a sector label and the temperature ratio $\xi = \beta/\beta'$ is not, so P2 reaches the stored charge and leaves $\xi$ free; a temperature becomes a label, in the disjointness sense, only on an algebra with infinitely many modes in one frequency band, which the finiteness declaration excludes.

## technical
The descent cannot instantiate uncaused distinctions: it equates components along symmetry orbits and never equates inequivalent ones. The residues are inequivalent as soldered algebras except along the reversal $r \mapsto -r$, which exchanges $2 \leftrightarrow 6$, $1 \leftrightarrow 7$, $3 \leftrightarrow 5$ and fixes $0$ and $4$, so the premise equates towers along that orbit only. Which of $2$ and $6$ is the visible tower is declared indexical.

The premise is scoped to labels, not states: it equates the superselection labels the descent deposits, such as the tower charge, and not the thermal state within a sector, and the deposited set of modes is declared finite. In the boundary-mode model of a reversal pair the charge is a label on every finite set of modes while the temperature is not, so under this scope P2 constrains the stored charge and leaves the mirror's temperature ratio free; only with infinitely many modes in a frequency band would the temperature become a label too, and the finiteness declaration rules that out.

## lay
This assumption says the birth of the universe treats alike only things that are genuinely alike. The only hidden sectors that count as alike are pairs related by a reflection, so only those pairs are forced to match. Which member of the matching pair we live in is simply a matter of where we stand. What must match are the sector's fixed labels, such as its stored charge, not how hot it is: the assumption leaves the temperature of the mirror sector open, and it takes the number of modes the birth deposits to be finite.

## one-liner
Premise: the descent equates towers only along the reversal orbit $r \mapsto -r$, the one symmetry of the soldered residues, and it equates sector labels such as the tower charge, not thermal states, over a finite deposited mode set.
