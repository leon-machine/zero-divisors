---
id: note.transport.setting-introduction
kind: note
version: 1
title: Introduction
status: setting
subject: zero-divisors
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
comments_on:
- transport.noinverse
- transport.no-go-level-elements
locators:
  paper: T01
  number: Setting
  section: Introduction
  line: 384
---

## formal
In ordinary arithmetic, division fails at exactly one number, and the failure is handled by prohibition: division by zero is forbidden, and every calculation routes around it. This paper is about the same failure in a richer setting. A Clifford algebra is the algebra of a geometry: its elements are built from the vectors of a space, and its one rule is that a vector times itself is its squared length. In such an algebra most elements can be divided by. Every vector of nonzero length has an exact inverse, and these invertible elements are plentiful enough to build every symmetry of the underlying space \cite{HestenesSobczyk1984, DoranLasenby2003}. But with three exceptions (the real numbers, the complex numbers and the quaternions, the three Clifford algebras that are themselves division algebras), every real Clifford algebra also contains nonzero elements that cannot be inverted at all: elements that multiply with some partner to give exactly zero, the \emph{zero divisors}. Where they occur, division fails, and the standard response is arithmetic's response: exclude them and work around the exclusion.

The response examined here is the opposite one, and it is the founding idea of the programme this paper begins: read each failure of division as an instruction. A failure, precisely located, tells you what the algebra is missing. The theorems of this paper show that it also tells you the smallest thing that can be added to supply it, and that the addition is forced, not chosen.

The stance has a precedent in the foundations of mathematics, and the precedent was in fact the founding idea's model. G\"odel proved that any consistent system strong enough for arithmetic contains true statements it cannot prove. The famous part is the impossibility; the instructive part is its precision. The unprovable statement is informative: it names, exactly, the stronger system in which it becomes a theorem, and that stronger system contains new unprovable statements of its own, without end. This paper proves that division by zero in a Clifford algebra has the same structure. The impossibility is internal and exact: an inverse of a null vector $v$ would satisfy $vv^{-1} = 1$, and multiplying by $v$ reduces it to $v = 0$ (Lemma \claimref{transport.noinverse}). The failure determines its own repair, exactly one hyperbolic plane, which is the minimality half of the type-N theorems. And the completed algebra carries a new null cone of its own, so the ascent never terminates; the resulting tower is the subject of T3 \cite{ButlerT3}. The parallel is structural, not a theorem, since provability and invertibility belong to different categories, and nothing below depends on it. What it supplies is the right way to read what follows: the limit of a system indicates the system that removes it, and mathematics has met this kind of obstruction before.

The failures come in exactly three kinds, each with a concrete description. A \emph{null vector} is a direction whose squared length is zero; in spacetime these are the directions light travels, and no algebra containing such a vector can invert it. An \emph{idempotent} is an element with $e^2 = e$, one of the algebra's projections; every projection other than $0$ and $1$ annihilates its complementary projection, so each is a zero divisor. And in certain signatures the algebra splits into two independent halves that annihilate each other; the \emph{central} idempotents that effect this split are the deepest failure of the three, because no symmetry of the algebra can even exchange the halves. We prove this list complete: every zero divisor belongs to one of the three kinds. For each kind the paper then proves the repair. The null vector cannot be repaired as an element: once the space has more than two dimensions, no assignment of pseudo-inverses (the standard weakened substitute for an inverse, recalled in Section \ref{sec:prelim}) can respect the symmetries of the space, whether valued in the algebra itself, in the Clifford algebra of any extension of the space, or in a matrix algebra over one (the scope of Theorem \claimref{transport.no-go-level-elements} and Remark \claimref{note.transport.obstruction-parabolic}); the two-dimensional hyperbolic plane is the only exception, and an instructive one. What can be repaired is the space of points itself, by a completion that costs exactly one new plane and makes the reciprocal total; no smaller completion works. The split algebra is repaired by one added generator, which fuses its two halves into a single simple algebra, again minimally. The ordinary projection turns out to need no repair at all: it is its own pseudo-inverse. And the repairs compose cleanly, so a repair never creates a failure it cannot finish.

The plan of the paper is the plan just sketched, now with theorems attached. First classify: the three kinds have sharp existence loci, and the classification is exhaustive (Section \ref{sec:taxonomy}). Then repair, one kind per section. \emph{Isotropic vectors} exist precisely in mixed signature; they are the most geometric of the obstructions and the only genuinely hard one, and their treatment takes the longest section of the paper (Section \ref{sec:typeN}). \emph{Central idempotents} exist precisely in the split signatures $p - q \equiv 1 \pmod 4$, where the algebra splits into two ideals that no inner symmetry can exchange, and where, on the one-dimensional extensions of the even-dimensional algebras, the repair turns out to coincide with the first rule's ascent (Section \ref{sec:rules}). \emph{Non-central idempotents} exist everywhere else, and demand nothing at all (Section \ref{sec:typeP-rule}). Each repair comes with the theorem that makes it forced rather than convenient, the bookkeeping of iterated repairs is settled in Section \ref{sec:clock}, and Section \ref{sec:principle} states what it all amounts to: a general principle, and a six-step procedure whose every step is licensed by a theorem proved earlier in the paper. Table \ref{tab:algorithm} there is the paper's contribution list in operational form.

## technical
pending

## lay
pending

## one-liner
pending
