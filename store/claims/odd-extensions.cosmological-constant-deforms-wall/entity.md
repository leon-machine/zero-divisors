---
id: odd-extensions.cosmological-constant-deforms-wall
kind: claim
version: 2
title: The cosmological constant deforms the wall
status: proved
region: odd-extensions
subject: tower
tags: [cosmological-constant, degenerate-algebras, towers-by-residue]
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
  - odd-extensions.are-ascents-pair-signed@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_generator_square_is_minus_lambda_over_three
- kind: check
  ref: check.py::check_omega_square_is_lambda_over_three
- kind: check
  ref: check.py::check_lambda_zero_degenerate_algebra
- kind: proof
  derivation: main
locators:
  paper: T14a
  number: Cor 6.3
  label: cor:wall
  line: 591
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the ascent generator''s square -Lambda/3, I^perp signatures (1,4), (2,3), (1,3;1), omega^2 = Lambda/3 with doubling and complexification, and the nilpotent ideal at Lambda = 0. Version 1 -> 2.'
  env: corollary
  typing:
    by: ai-typing-pass
    note: 'The single use is the theorem whose clauses the proof cites and is kept. Levels pass: conditions
      already kept.'
---

## formal
The intermediate algebra of this world's ascent is a one-parameter family in $\Lambda$: the degenerate $\Cl(1,3;1)$ at $\Lambda = 0$, whose nilpotent generator is the zero divisor the transport is built to resolve, deformed to the doubled $\Cl(1,4)$ for $\Lambda > 0$ and the complexified $\Cl(2,3)$ for $\Lambda < 0$. The sign of $\Lambda$ fixes the sign given to the ascent's null generator (the generator's square is $-\Lambda/3$, the opposite sign), and the two odd extensions are the two ways of giving it one.

## technical
The intermediate algebra of this world's ascent is a one-parameter family in $\Lambda$. At $\Lambda = 0$ it is the degenerate $\Cl(1,3;1)$, whose nilpotent generator is the zero divisor the transport is built to resolve; for $\Lambda > 0$ it deforms to the doubled $\Cl(1,4)$ and for $\Lambda < 0$ to the complexified $\Cl(2,3)$.

The ascent's null generator acquires the square $Q = -\Lambda/3$, of sign opposite to $\Lambda$, and the two odd extensions are the two ways of giving it a sign.

## lay
The cosmological constant controls which algebra sits halfway up our world's completion step. When it is zero, that algebra contains a direction of zero length, exactly the kind of defect the completion exists to cure. A positive or negative value gives that direction a nonzero length of the opposite sign, turning the algebra into one of two different odd-dimensional forms.

## one-liner
The intermediate algebra of this world's ascent is the degenerate $\Cl(1,3;1)$ at $\Lambda = 0$, deformed to $\Cl(1,4)$ for $\Lambda > 0$ and to $\Cl(2,3)$ for $\Lambda < 0$, the sign of $\Lambda$ fixing the opposite sign of the null generator's square.
