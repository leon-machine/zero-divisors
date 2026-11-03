---
id: note.primer.setting-products-vectors-one-rule
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
  line: 203
---

## formal
Adding vectors causes no trouble. Two displacements compose into a third, the picture and the algebra agree, and there is nothing to explain. What is wanted next is a product: a way of multiplying two vectors that is associative, that keeps the geometry of the pair, and that can be undone, so that knowing $a$ and the product $ab$ recovers $b$. Multiplication and division of vectors, on the same footing as multiplication and division of numbers. That is the whole demand, and it is worth being precise about how the products a reader already knows fall short of it, because the geometric product is built to repair exactly those faults.

Ordinary vector algebra in three dimensions offers two products. The inner product $a \cdot b = |a|\,|b| \cos\theta$ returns a number. It knows lengths and angles, which is most of Euclidean geometry, but it is symmetric in its two arguments and retains nothing about the plane they span. The cross product $a \times b$ returns a vector perpendicular to both, of length $|a|\,|b| \sin\theta$. It does record that plane, but it records it by pointing away from it, and that device is available in three dimensions only: in a plane there is no perpendicular direction to point along, and in four dimensions there are too many, since the vectors orthogonal to a given pair form a plane rather than a line.

Both products have a second limitation, and for this series it is the decisive one. Neither can be undone. Knowing $a$ and the number $a \cdot b$ does not determine $b$, and knowing $a$ and the vector $a \times b$ does not either. There is no division, and no candidate for one. A subject whose question is what happens where division fails cannot start there.

## technical
pending

## lay
pending

## one-liner
pending
