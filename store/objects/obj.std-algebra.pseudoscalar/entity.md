---
id: obj.std-algebra.pseudoscalar
kind: object
version: 1
title: The pseudoscalar
status: defined
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- pseudoscalar-and-centre
proposed_by:
  kind: ai
  session: algebra-core-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: typed
trust: ai-proposed
about:
- obj.std-algebra.grade-projection
- obj.std-algebra.blade
locators:
  sources:
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
  - key: HestenesSobczyk1984
    locator: Ch. 1 (geometric algebra)
extraction:
  by: algebra-core-2026-10-26
---

## formal
For $\R^{p,q,r}$ with its standard orthogonal basis, the \emph{unit pseudoscalar} is $I = e_1 e_2 \cdots e_n = e_1 \wedge \dots \wedge e_n$, written $\omega$ in \claimref{primer.sign} and \claimref{primer.centre}. $\Cl^{n}$ is one-dimensional, so every pseudoscalar of $\Cl(p, q, r)$ is a nonzero multiple of $I$; reordering the basis or reversing an axis changes $I$ by a sign.

## technical
The unit pseudoscalar is the product of the standard basis vectors in order: the oriented unit volume element of the whole space. The top grade is one-dimensional, so it is unique up to scale and its sign fixes an orientation.

## lay
The pseudoscalar is the oriented unit volume of the whole space. In three dimensions it is the unit cube with a handedness; in spacetime, the unit four-volume.

## one-liner
The unit pseudoscalar is $I = e_1 \cdots e_n$, spanning the one-dimensional top grade.
