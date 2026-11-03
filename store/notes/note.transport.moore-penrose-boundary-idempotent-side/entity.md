---
id: note.transport.moore-penrose-boundary-idempotent-side
kind: note
version: 1
title: The Moore--Penrose boundary, idempotent side
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
- transport.pair-canonical-label-bit
- transport.group-null-rotations
locators:
  paper: T01
  number: Rem 6.6
  label: rem:MPboundary
  line: 1414
---

## formal
One refinement of the type-P question does carry content, and it traces the boundary of Section \ref{subsec:mp} from the other side. Within the idempotents sharing a fixed image $W$, is there a canonical one? They are in bijection with the complements of $W$, hence form a torsor under $\mathrm{Hom}(V/W, W)$ on which the stabiliser of $W$ acts by unipotent transvections, the same shear mechanism as the null rotations of Lemma \claimref{transport.group-null-rotations}. A definite Hermitian form resolves it, the orthogonal projection $P_W$ being the unique self-adjoint member; an indefinite one fails exactly on the degenerate subspaces, where no self-adjoint member exists at all: were $e$ self-adjoint with image $W$, any nonzero $z \in W \cap W^{\perp}$ would give $\langle x, z\rangle = \langle x, ez\rangle = \langle ex, z\rangle = 0$ for every $x$, against nondegeneracy of the ambient form. So the two sides agree: canonical selection is available exactly where a definite structure is. The transport-theoretic point is the division of labour. For type P the ambiguity concerns only \emph{which} idempotent to use, and the repair theorem needs no choice at all, since $\sigma(e) = e$ is asked about a given $e$; for type N the same ambiguity affects the repair itself, which is why the null cone needs the ascent and the idempotent variety does not.

## technical
pending

## lay
pending

## one-liner
pending
