---
id: note.interior.convention-note-sign-norm
kind: note
version: 1
title: Convention note on the sign of the norm
status: remark
subject: einstein
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
comments_on:
- interior.sign-fixed-internally
- interior.non-null-stabilisers-section-they-act
- interior.scale-tractor-leaves-cone
- interior.stabiliser-rotates-parabolic-reductive
locators:
  paper: T06
  number: Rem 4.9
  label: rem:signZD
  line: 552
---

## formal
In the labelling fixed here (tractor signature $(2,4)$ meaning two plus, four minus, forced by \eqref{eq:tractormetric} with $g$ mostly minus), the norm of the frozen point is proportional to $+\Lambda$, and that sign is the series' convention throughout. It is not a free choice: the stabiliser of a \emph{negative}-norm vector in $O(2,4)$ is $O(2,3)$, the anti-de Sitter group, by Proposition \claimref{interior.non-null-stabilisers-section-they-act}(1), so a norm proportional to $-\Lambda$ could not carry the de Sitter stabiliser that Theorem \claimref{interior.scale-tractor-leaves-cone} and Proposition \claimref{interior.stabiliser-rotates-parabolic-reductive} establish for $\Lambda > 0$. The invariant content is what those two results prove: nullity exactly at $\Lambda = 0$, reductive rotation, and de Sitter for $\Lambda > 0$. The verification script checks the complement signatures exactly.

## technical
pending

## lay
pending

## one-liner
pending
