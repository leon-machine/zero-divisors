---
id: note.sheaf.conservation-degeneracy-boundary-sharp-example
kind: note
version: 1
title: Conservation of degeneracy at a boundary, and a sharp example
status: remark
subject: singularity
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
comments_on:
- sheaf.one-sided-completion-singularity
- sheaf.conservation-degeneracy-absolute-form
locators:
  paper: T04
  number: Rem 8.13
  label: rem:schwconservation
  line: 983
---

## formal
Theorem \claimref{sheaf.conservation-degeneracy-absolute-form} forbids completions nondegenerate on \emph{both} sides of an interior wall; at a boundary there is one side, the theorem's hypothesis fails, and the completion closes with no residue. The degeneracy has not been removed; it has been displaced out of the manifold: the would-be shadow wall is at $r < 0$. There is a sharper way to see that the conservation principle survives with its boundary at exactly the right place. Take the coupling \emph{global}: bump $\equiv 1$ everywhere and $\mu\nu = -\tfrac{m^2}{2}$ (at $2M = 1$, the value $-\tfrac12$). Then, exactly,
\[
\det h \;=\; m^2 \quad \text{at every radius,}
\]
and $h$ has signature $(2,4)$ from the deep interior through the horizon to the far exterior: a \emph{globally} nondegenerate completion of the Schwarzschild degeneration, with constant determinant. This does not contradict Theorem \claimref{sheaf.conservation-degeneracy-absolute-form}, because that theorem only forbids completions that are \emph{standard outside a neighbourhood of the wall}, and this one is not: its coupling never switches off, so it fails standardness at infinity. The example exhibits the conservation theorem's hypothesis as exactly sharp: give up standardness at infinity and the obstruction moves to infinity; keep standardness and, at an interior wall, it moves to the shadow wall; at a boundary wall, it moves out of the manifold. Degeneracy is moved, never destroyed, in all three regimes.

## technical
pending

## lay
pending

## one-liner
pending
