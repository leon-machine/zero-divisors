---
id: note.sheaf.only-product-coupling-constants-matters
kind: note
version: 1
title: Only the product of the coupling constants matters
status: remark
subject: walls
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
- sheaf.localised-transport
- sheaf.wall-gram
- sheaf.determinant-identity-blow-up-expansion
- sheaf.one-sided-completion
locators:
  paper: T04
  number: Rem 4.6
  label: rem:signchoice
  line: 643
---

## formal
Lemma \claimref{sheaf.wall-gram} shows the wall signature depends only on $\operatorname{sign}(\mu\nu)$, and Lemma \claimref{sheaf.determinant-identity-blow-up-expansion} shows the collar behaviour depends only on the product $\mu\nu$; the individual constants are gauge (rescaling $\nO, \nInf$ hyperbolically absorbs them). The choice $\mu\nu > 0$ selects the ascent of the physical side, $(p,q) \to (p{+}1,q{+}1)$; the opposite sign selects $(p,q{+}2)$ on the wall, which is the Rule-1 ascent of the \emph{far} side's algebra $\Cl(p{-}1,q{+}1)$. The two signs are the two competing completions of the two sides of a signature-change wall, and the impossibility of achieving both at once is the subject of the next section. The determinant factor
\[
F \;:=\; 1 + 2\mu\nu\beta^2 s
\]
of Lemma \claimref{sheaf.determinant-identity-blow-up-expansion}(1) is the single function on which everything depends: $F \geq 1$ on the physical collar side (proof of Theorem \claimref{sheaf.one-sided-completion}), and its zero set on the far side is the shadow wall.

## technical
pending

## lay
pending

## one-liner
pending
