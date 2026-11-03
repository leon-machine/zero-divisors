---
id: note.primer.setting-products-vectors-one-rule-4
kind: note
version: 1
title: Products of vectors, and the one rule
status: setting
subject: clifford-structure
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T00, deposited version
comments_on:
- primer.commutation-rule
locators:
  paper: T00
  number: Setting
  section: Products of vectors, and the one rule
  line: 243
---

## formal
\textbf{Clifford's step answers the second.} Keep both parts, and add them:
\[
ab \;=\; a \cdot b \;+\; a \wedge b .
\]
The objection is immediate: a number and a plane element are different kinds of object, and adding them looks like a mistake. The sum claims nothing about numbers and areas being the same kind of thing. It is bookkeeping: the two parts are kept in one symbol because they travel together and the pair is more useful than the pieces, in the way a real part and an imaginary part are kept together in one complex number. Elements that combine objects of several kinds in this way are called \emph{multivectors}.

What the sum buys is division. Take $b = a$: the outer part vanishes, and the product of a vector with itself is the pure number $a \cdot a$, its squared length. So whenever that number is not zero the vector has a two-sided inverse,
\[
a^{-1} \;=\; \frac{a}{a \cdot a} ,
\]
which is what neither the inner nor the outer product could supply alone. Clifford, in 1878, joined Grassmann's outer product to Hamilton's quaternions in exactly this way, and the algebra that results is the subject of this primer.

## technical
pending

## lay
pending

## one-liner
pending
