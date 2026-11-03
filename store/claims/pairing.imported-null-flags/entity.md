---
id: pairing.imported-null-flags
kind: claim
version: 1
title: 'Imported: null flags'
status: imported
region: pairing
subject: conformal-spacetime
tags: [classical-theorem, null-directions]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-pairing, the series'' standard disclaimer'
review: typed
imported_from:
- citation: 'R. Penrose, W. Rindler, Spinors and Space-Time, Vol. 1: Two-Spinor Calculus and Relativistic
    Fields, Cambridge University Press (1984).'
  key: PenroseRindler1
  locator: Sec.~1.4
locators:
  paper: T05-pairing
  number: Fact 1.3
  label: fact:flags
  line: 192
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported from Penrose and Rindler; no edges.
---

## formal
A nonzero Weyl spinor $o$ of $\mathrm{Spin}(1,3)$ determines a future null direction $\ell = o\bar o$ and a flag plane through it, and the projective Weyl spinor $[o]$ is the null direction: the celestial sphere is $\mathbb{P}^1$. A rotation of the frame by an angle $\phi$ about an axis acts on the spinor by the half angle $\phi/2$. \emph{Provenance:} \cite[Sec.~1.4]{PenroseRindler1}.

## technical
A nonzero Weyl spinor $o$ of $\mathrm{Spin}(1,3)$ determines a future null direction $\ell = o\bar o$ and a flag plane through it. The projective spinor $[o]$ is exactly that null direction, so the celestial sphere is $\mathbb{P}^1$, and a rotation of the frame by an angle $\phi$ acts on the spinor by the half angle $\phi/2$. This is standard two-spinor calculus.

## lay
In relativity a single two-component spinor encodes a light-like direction together with a flag attached to it. Spinors taken up to scale correspond exactly to points of the sky, the celestial sphere. Rotating space by some angle turns the spinor by only half that angle.

## one-liner
Imported: a Weyl spinor $o$ determines the null direction $o\bar o$ with a flag, $[o]$ is a point of the celestial sphere $\mathbb{P}^1$, and frame rotations act on spinors by half angles.
