---
id: hawking.joint-j3-s-wave-reduction
kind: claim
version: 3
title: 'Joint J3: the partial-wave reduction (modelling)'
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
- name: Claude Fable 5.2
  role: restatement of the premise, the channel-reduction clause narrowed to even-parity spin 2, the reduction worded per partial-wave channel, and the identification recorded as not injective
  version: 3
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
  maintainer_pass_2026_11_09b:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Version 2 -> 3 (Leon''s decisions of 9 November 2026, second pass): the channel-reduction clause is kept as premise for the even-parity channels of spin 2 only, since synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional derives the odd-parity channels (l >= 2, real nonzero frequency, static frame, given its stated hypotheses) and reaches even parity in one direction only; "s-wave reduction" is reworded to each partial-wave channel, l >= |s|, because a field of helicity s has no partial wave below l = |s| (the id is kept); and the identification of channels with current bosons of the arrays is recorded as not one array tower per helicity channel, citing synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free.'
  env: named premise inside an assembly
  repair:
    notes:
    - 'created after review: a named non-theorem joint, stated inside the assembly'
  typing:
    by: ai-typing-pass
    note: Postulate; no edges to review.
---

## formal
The current boson of the s-wave theory is each partial-wave channel, $\ell \geq |s|$, of each four-dimensional massless field of helicity $s$ (a field of helicity $s$ has no partial wave below $\ell = |s|$: the photon's channels begin at $\ell = 1$ and the graviton's at $\ell = 2$), and the lift from the boundary modes to the field is the standard partial-wave reconstruction (the current-boson identification, for every massless field). The identification of channels with current bosons of the arrays is not one array tower per helicity channel: it is not injective onto distinct array towers, and it is not to be read as requiring an array of its own for each helicity channel. Read injectively, with the bound of one helicity channel per array, it would give a capacity inequality on the content; that inequality is a reading, not a consequence of this premise, and it leaves the generation number free (Theorem \claimref{synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free}). For the even-parity channels of the massless spin-$2$ field, the graviton, the near-horizon reduction of field theory on the Schwarzschild exterior identifies each $(\omega, \ell, m)$ channel, $\ell \geq 2$, with a two-dimensional mode (the channel-reduction clause, assumed for even-parity spin $2$ only). For the other channels the channel-reduction clause is not part of the premise. Theorem \claimref{synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional} derives it at the horizon for the scalar, Dirac and Maxwell fields (spins $0$, $\tfrac12$ and $1$), given the classical facts on angular harmonics stated there. Theorem \claimref{synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional} derives it for the odd-parity channels of spin $2$ with $\ell \geq 2$ and real nonzero frequency, in the static frame and given the hypotheses stated there; for even parity it shows one direction only (the linearised vacuum equations imply the Zerilli equation, at sample points), which is why the even-parity clause stays premise. Neither theorem derives the current-boson identification, which stays premise for every massless field.

## technical
This modelling premise identifies the current boson of the s-wave theory with each partial-wave channel of each four-dimensional massless field, the channels of a field of helicity $s$ beginning at $\ell = |s|$, and takes the lift from the boundary modes to the field to be the standard partial-wave reconstruction. The identification is not one array tower per helicity channel: several channels may be currents of the same arrays, so the premise does not carry the capacity inequality that an injective reading would give, and the generation number stays free under it (\claimref{synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free}). Its second part, that the near-horizon reduction of field theory on the Schwarzschild exterior identifies each channel with a two-dimensional mode, is now assumed only for the even-parity channels of the graviton (spin $2$). For scalar, Dirac and Maxwell fields that channel reduction is derived in Gauge Theory Gravity (\claimref{synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional}), with couplings that vanish at the horizon as $1 - 2M/r$ for spins $0$ and $1$ and as its square root for spin $\tfrac12$. For the odd-parity channels of the graviton with $\ell \geq 2$ it is derived by linearising the gauge field about the Schwarzschild field (\claimref{synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional}), on channels of real nonzero frequency, in the static frame and given the hypotheses stated there; the even-parity equation is reached there in one direction only, and its converse is cited, not derived. The identification of the current boson with these channels is not derived and remains premise for every field.

## lay
Near a black hole, a four-dimensional field can be broken into spherical-wave pieces, each behaving like a simple wave in one space dimension; light has no piece with fewer than one lobe and gravity none with fewer than two. This premise assumes that the framework's horizon modes are exactly these pieces. It does not assume that each piece has a separate set of horizon modes of its own. For scalar fields, electrons and light the breaking into one-dimensional waves has since been derived, and so has one of the two kinds of gravitational wave; the premise now assumes it only for the other kind. That the framework's horizon modes are these pieces is still assumed for every field. It is a modelling assumption, not a theorem.

## one-liner
Premise: the current boson of the s-wave theory is each partial-wave channel, $\ell \geq |s|$, of each massless field on the Schwarzschild exterior (an identification that is not one array tower per helicity channel), and each even-parity $(\omega, \ell, m)$ channel of the spin-$2$ field is a two-dimensional boundary mode (for spins $0$, $\tfrac12$, $1$ and for odd-parity spin $2$ that channel reduction is derived).
