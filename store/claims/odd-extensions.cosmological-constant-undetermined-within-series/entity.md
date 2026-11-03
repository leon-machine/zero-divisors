---
id: odd-extensions.cosmological-constant-undetermined-within-series
kind: claim
version: 1
title: The cosmological constant is undetermined within the series
status: proved
region: odd-extensions
subject: dark-energy
tags: [undetermined-input, cosmological-constant, transport-algorithm, frozen-point]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
review: typed
derivations:
- name: main
  uses:
  - odd-extensions.transport-constrains-frozen-point-only-through@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
locators:
  paper: T14a
  number: Cor 8.3
  label: cor:uncaused
  line: 662
extraction:
  env: corollary
  outside_pilot_cites:
  - ButlerT14
  typing:
    by: ai-typing-pass
    note: 'Kept the single use (the theorem whose clauses (iii) and (iv) the proof cites); the citation
      of the dark-matter paper''s Premise P2 is for the analogy of status only, not a premise, so no edge
      was added for it. Levels pass: conditions already kept.'
---

## formal
The transport, run on the wall, returns the rung and a canonical null frame in its new plane, and stops; the frozen point's position in that plane is data the transport receives, not data it produces, and the one invariant of that position is the norm $\Lambda/3$, sign and magnitude together. Within the series the sign is a choice between two options that the construction makes inequivalent (Theorem \claimref{odd-extensions.transport-constrains-frozen-point-only-through}(iv)) and that nothing in the construction decides, which is the status the dark-matter paper's Premise P2 gives to the choice of which oriented tower is the visible one; the analogy is one of status, since P2's choice is binary and this one is a real modulus. Nothing here says the sign has no cause: only that the transport is not it.

## technical
When the transport is run on the wall at $\Lambda = 0$ it returns the rung $\Cl(2,4)$ and a canonical null frame $\{I, \varphi\}$ in its new hyperbolic plane, and stops. A frozen point of cosmological constant $\Lambda$ is a vector $aI + b\varphi$ of that plane with $Q(aI + b\varphi) = 2ab = \Lambda/3$; its position is data the transport receives, not data it produces, and under the symmetries the transport supplies its one invariant is the norm $\Lambda/3$, sign and magnitude together.

Within the series the sign is a choice between two options that the construction makes inequivalent and that nothing in the construction decides. This is the status the dark-matter paper's Premise P2 gives to the choice of which oriented tower is the visible one, with the difference that that choice is binary and this one is a real modulus. The result does not say the sign has no cause, only that the transport is not it.

## lay
The series has a procedure, the transport, for dealing with places where its algebra breaks down. Running it at the point where the cosmological constant would be zero produces a definite structure, but it leaves the value of the cosmological constant, including whether it is positive or negative, entirely open. So within the series the cosmological constant is an input rather than an output. This does not mean nothing could fix it, only that the transport does not.

## one-liner
Run on the wall, the transport fixes the rung and a canonical null frame but leaves the cosmological constant, sign and magnitude, as data it receives, so within the series $\Lambda$ is undetermined.
