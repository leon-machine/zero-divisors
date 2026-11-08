---
id: obj.std-algebra.pseudoscalar
kind: object
version: 2
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
- name: Claude Opus 5.5
  role: 'maintainer pass, foundation layer'
  version: 2
  source: run 2026-11-08-foundation-layer
review: typed
trust: ai-proposed
about:
- obj.std-algebra.grade-projection
- obj.std-algebra.blade
founded_on:
- synthesis.continuum-completion-premise@2
locators:
  sources:
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
  - key: HestenesSobczyk1984
    locator: Ch. 1 (geometric algebra)
extraction:
  maintainer_pass_2026_11_08_foundation:
    by: ai-maintainer-pass
    note: >-
      Version 1 -> 2. Leon's decision of 8 November 2026: the foundation layer. Founded on synthesis.continuum-completion-premise: the algebra it is stated in rests on the foundation. Foundation postulates are reported as what a result rests on, separately from the premises it holds given (store/conventions.md, "The foundation").
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
