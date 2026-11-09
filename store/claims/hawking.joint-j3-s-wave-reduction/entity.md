---
id: hawking.joint-j3-s-wave-reduction
kind: claim
version: 2
title: 'Joint J3: the s-wave reduction (modelling)'
status: postulate
region: hawking
subject: thermality
tags: [thermal-premises, bosonisation, schwarzschild]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
- name: Claude Opus 5.5
  role: restatement of the premise, the channel-reduction clause narrowed to spin 2 since spins 0, 1/2 and 1 are derived
  version: 2
  source: maintainer pass of 2026-11-09
review: typed
locators:
  paper: T07
  number: within Asm 5.3
  label: ''
extraction:
  maintainer_pass_2026_11_09:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Version 1 -> 2 (Leon''s decision of 9 November 2026): restated, the channel-reduction clause narrowed to spin 2 (the graviton''s channels), since synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional derives it at the horizon for spins 0, 1/2 and 1 (conditional on completeness of the angular harmonics and the exact/co-exact split, cited from memory there); the current-boson identification and the partial-wave lift stay premise for every massless field, since that result does not derive them.'
  env: named premise inside an assembly
  repair:
    notes:
    - 'created after review: a named non-theorem joint, stated inside the assembly'
  typing:
    by: ai-typing-pass
    note: Postulate; no edges to review.
---

## formal
The current boson of the s-wave theory is the s-wave reduction of each four-dimensional massless field, and the lift from the boundary modes to the field is the standard partial-wave reconstruction (the current-boson identification, for every massless field). For the massless spin-$2$ field, the graviton, the near-horizon reduction of field theory on the Schwarzschild exterior identifies each $(\omega, \ell, m, s)$ channel with a two-dimensional mode (the channel-reduction clause, assumed for spin $2$ only). For spins $0$, $\tfrac12$ and $1$ the channel-reduction clause is not part of the premise: Theorem \claimref{synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional} derives it at the horizon for the scalar, Dirac and Maxwell fields, given the classical facts on angular harmonics stated there; that theorem does not derive the current-boson identification, which stays premise for these fields too.

## technical
This modelling premise identifies the current boson of the s-wave theory with the s-wave reduction of each four-dimensional massless field, and takes the lift from the boundary modes to the field to be the standard partial-wave reconstruction. Its second part, that the near-horizon reduction of field theory on the Schwarzschild exterior identifies each channel $(\omega, \ell, m, s)$ with a two-dimensional mode, is now assumed only for the graviton (spin $2$). For scalar, Dirac and Maxwell fields that channel reduction is derived in Gauge Theory Gravity (\claimref{synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional}), with couplings that vanish at the horizon as $1 - 2M/r$ for spins $0$ and $1$ and as its square root for spin $\tfrac12$; the identification of the current boson with these channels is not derived and remains premise for every field.

## lay
Near a black hole, a four-dimensional field can be broken into spherical-wave pieces, each behaving like a simple wave in one space dimension. This premise assumes that the framework's horizon modes are exactly these pieces. For scalar fields, electrons and light the breaking into one-dimensional waves has since been derived, so the premise now assumes it only for gravitational waves; that the framework's horizon modes are these pieces is still assumed for every field. It is a modelling assumption, not a theorem.

## one-liner
Premise: the current boson of the s-wave theory is the s-wave reduction of each massless field on the Schwarzschild exterior, and each $(\omega, \ell, m, s)$ channel of the spin-$2$ field is a two-dimensional boundary mode (for spins $0$, $\tfrac12$ and $1$ that channel reduction is derived).
