---
id: note.conformal.setting-introduction
kind: note
version: 1
title: Introduction
status: setting
subject: completion
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T02, deposited version
comments_on:
- conformal.minimal-nondegenerate-completion
- conformal.principal-case
locators:
  paper: T02
  number: Setting
  section: Introduction
  line: 133
---

## formal
Two algebras dominate applied geometric algebra. Projective (plane-based) geometric algebra, $\mathrm{PGA} = \Cl(3,0,1)$, models Euclidean rigid motions with a degenerate metric whose null direction $e_0$ encodes the plane at infinity \cite{Gunn2017, Selig2005}. Conformal geometric algebra, $\mathrm{CGA} = \Cl(4,1)$, embeds Euclidean space on a null quadric and adds inversions and dilations to the versor group \cite{HLR2001, DFM2007}. The two are normally introduced as alternative modelling decisions with different trade-offs. This note proves a sharper statement: CGA is the \emph{unique minimal nondegenerate completion} of PGA. The relationship is a theorem, an instance of the general minimal-completion theorem for degenerate Clifford algebras, which this note states and proves in full (Theorem \claimref{conformal.minimal-nondegenerate-completion}), with the PGA case as its principal corollary (Corollary \claimref{conformal.principal-case}).

The theorem belongs to a series. The root paper \cite{ButlerT1} proved the transport principle, that the failure of division at null vectors of $\Cl(p,q)$ is repaired minimally and uniquely by one hyperbolic plane, $\Cl(p,q) \to \Cl(p{+}1,q{+}1)$, and classified all zero-divisor obstructions and their transport rules; the sheaf paper \cite{ButlerT4} handled metrics that degenerate along a locus, where the radical generates a canonical square-zero ideal (the corank-one case), and proved that any nondegenerate completion converts that ideal into the unit ideal. The present note is the degenerate-algebra instance of the same programme: a radical of dimension $r$ requires exactly $r$ hyperbolic planes, and the minimal completion is unique. What is new here is the full rigor: the minimality argument is completed, the signature is forced by a Witt-splitting argument, and uniqueness is proved by the Witt extension theorem, none of which the applied literature states in this generality.

## technical
pending

## lay
pending

## one-liner
pending
