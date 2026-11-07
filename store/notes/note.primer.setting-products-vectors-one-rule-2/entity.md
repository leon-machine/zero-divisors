---
id: note.primer.setting-products-vectors-one-rule-2
kind: note
version: 2
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
- name: Claude Opus 5.5
  role: 'GA rewrite (declared: the primer motivates the geometric product against the cross product)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
comments_on:
- primer.commutation-rule
locators:
  paper: T00
  number: Setting
  section: Products of vectors, and the one rule
  line: 211
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Not rewritten: the passage compares what the inner and cross products keep and discard; the cross product is the subject, so the text stays and is declared outside_ga (bridge).'
outside_ga:
  kind: bridge
  why: 'the passage is the primer''s motivation of the geometric product, which compares it with the inner and cross products of three-dimensional vector algebra that it replaces; the cross product is the subject of the comparison, not a stand-in'
---

## formal
\textbf{What each product throws away, the other keeps.} The inner product keeps the cosine and discards the plane; the cross product keeps the plane and the sine. Each fails to be invertible exactly where it returns zero, and they return zero in complementary places: $a \cdot b$ vanishes when $b$ is perpendicular to $a$, $a \times b$ when $b$ is parallel to it, and for $a \neq 0$ both vanish only when $b = 0$. Between them they hold everything about the pair. So a single product that carried both pieces at once, the number and the plane, would have lost nothing, and would have a chance of being invertible. That is the product to build, and two questions stand in the way. What should record the plane of $a$ and $b$ in dimensions above three, where no perpendicular vector is available to stand in for it? And what does it mean to add a plane element to a number?

## technical
pending

## lay
pending

## one-liner
pending
