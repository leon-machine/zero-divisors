---
id: obj.mass.grip-mass-composite
kind: object
version: 3
title: The grip, and the mass of a composite
status: defined
region: mass
subject: mass
tags:
- frozen-point
- conformal-spinors
- mass-generation
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
review: typed
locators:
  paper: T11
  number: Def 5.4
  label: def:grip
  line: 667
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: definition
  typing:
    by: ai-typing-pass
    note: Definition only; no edges to review.
  source_title: The grip, and the mass of a composite
  source_formal: 'Let $I$ be a nonzero ambient vector and $Z^{1}, \dots, Z^{N}$ a composite. The \emph{grip}
    of the composite on $I$ is the ambient vector $P = M(I)$ determined by

    \[

    \ip{P}{U} = M_{U\wedge I} \qquad\text{for all ambient } U,

    \]

    which exists and is unique because the pairing is nondegenerate. The \emph{mass-squared} of the composite
    relative to $I$ is $m^{2} := \ip{P}{P}$.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: The constituents of a composite are now conformal spinors in CS; the definition is otherwise
      unchanged.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - standard-model.grip-mass-two-rung-module (about)
    - standard-model.under-s-frozen-points-split-inverse (about)
    - one-relation.schr-odinger-slow-shadow (about)
    - mass.weight-composite (about)
    added_about: []
    verdict: connected
    note: 'Added about from the claims whose statements use the grip mass: the weight of a composite,
      the T12 grip-mass theorem and corollary, and the T16 slow-shadow proposition.'
---

## formal
Let $I$ be a nonzero ambient vector and $Z^{1}, \dots, Z^{N} \in \CS$ a composite of conformal spinors (twistors). The \emph{grip} of the composite on $I$ is the ambient vector $P = M(I)$ determined by
\[
\ip{P}{U} = M_{U\wedge I} \qquad\text{for all ambient } U,
\]
which exists and is unique because the pairing is nondegenerate. The \emph{mass-squared} of the composite relative to $I$ is $m^{2} := Q(P)$.

## technical
For a nonzero ambient vector $I$ and a composite $Z^{1}, \dots, Z^{N}$ of conformal spinors, the grip $P = M(I)$ is the ambient vector fixed by $\ip{P}{U} = M_{U\wedge I}$ for every ambient $U$, where $M_{U\wedge I}$ is the moment of the generator $A(U\wedge I)$ on the composite. It exists and is unique because the ambient pairing is nondegenerate.

The mass-squared of the composite relative to $I$ is then defined as the length of the grip, $m^{2} := Q(P)$.

## lay
A composite particle made of spinors of the conformal geometry carries charges under the conformal symmetries. Pairing those charges with a fixed ambient direction, in practice the cosmological scale, produces a single vector called the grip. The mass of the composite is defined to be the length of that vector.

## one-liner
The grip of a composite on $I$ is the vector $P$ with $\ip{P}{U} = M_{U\wedge I}$ for all ambient $U$, and its mass-squared relative to $I$ is $Q(P)$.
