---
id: note.dark-matter.where-flag-defined-what-it-carries
kind: note
version: 2
title: Where the flag is defined, and what it carries
status: remark
subject: clifford-structure
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
comments_on:
- dark-matter.residue-soldered-invariant-not-algebraic-one
- dark-matter.imported-eight-towers-mod-8-clock
- obj.dark-matter.witt-flag
locators:
  paper: T14
  number: Rem 3.7
  label: rem:flaglives
  line: 212
extraction:
  source_formal: |-
    Every tower has rungs, the $(1,1)$ ascent adjoining a hyperbolic plane at each floor (Fact \claimref{dark-matter.imported-eight-towers-mod-8-clock}), so at tower level every residue is flaggable (Definition \claimref{obj.dark-matter.witt-flag}) and flaggability selects nothing. The flag counts no towers; it orients them (Section \ref{sec:arrow}), and it equips them: a flag on $H_{k}$ is equivalently the complex structure $J_{k}$ on $H_{k} \otimes \C$ whose $-i$ eigenline is the annihilated half (it lives in the complexification, since no real endomorphism squaring to $-1$ has the two real null lines as eigenlines), and the ladder pair's number operator generates a $U(1)$ commuting with the rest of the rung. So every flagged tower carries rung-level abelian charges, one per rung, whatever its ground type, as this tower's derived content acquires its $U(1)$ from three ladder pairs \cite{ButlerT12}.
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted:
    - "the complexification of the tower plane, $H_k \\otimes \\C$, read as $H_k \\oplus I_4H_k$, and the eigenvalue $-i$ of $J_k$ as $-I_4$ (a Witt-pair complex structure on a plane orthogonal to spacetime)"
    kept: []
---

## formal
Every tower has rungs, the $(1,1)$ ascent adjoining a hyperbolic plane at each floor (Fact \claimref{dark-matter.imported-eight-towers-mod-8-clock}), so at tower level every residue is flaggable (Definition \claimref{obj.dark-matter.witt-flag}) and flaggability selects nothing. The flag counts no towers; it orients them (Section \ref{sec:arrow}), and it equips them: a flag on $H_{k}$ is equivalently the complex structure $J_{k}$ on the complexification $H_{k} \oplus I_4H_{k}$ (the plane $H_{k} \otimes \C$, with the field theory's imaginary unit $I_4$, which commutes with every vector of the plane) whose $-I_4$ eigenline is the annihilated half (it lives in the complexification, since no real endomorphism squaring to $-1$ has the two real null lines as eigenlines), and the ladder pair's number operator generates a $U(1)$ commuting with the rest of the rung. So every flagged tower carries rung-level abelian charges, one per rung, whatever its ground type, as this tower's derived content acquires its $U(1)$ from three ladder pairs \cite{ButlerT12}.

## technical
pending

## lay
pending

## one-liner
pending
