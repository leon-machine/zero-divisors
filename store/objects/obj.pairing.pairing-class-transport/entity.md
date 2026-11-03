---
id: obj.pairing.pairing-class-transport
kind: object
version: 1
title: The pairing class of the transport
status: defined
region: pairing
subject: thermality
tags: [pairing-and-bogoliubov]
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
locators:
  paper: T05-pairing
  number: Def 4.1
  label: def:class
  line: 287
extraction:
  env: definition
  context_refs:
  - pairing.pairing-functional-pair-creation-amplitude
  - pairing.stabiliser-parabolic-algebra-null-direction
  typing:
    by: ai-typing-pass
    note: Definition only; levels written, no edge changes (the propositions it cites are context for
      the definition).
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - pairing.displacement-pairs-point-mode-vacuum-parallel
    added_about: []
    verdict: connected
    note: A definition cannot carry uses or assumes; the added links are about edges from the claims whose
      statements use the defined notion.
---

## formal
The pairing class of the transport along $X$, relative to the vacuum field, is $\pv(\Omega(X)) = \ip{\Omega(X)\cdot\ell}{m}$. The transport preserves the vacuum ray along $X$ if and only if $\pv(\Omega(X)) = 0$ (Proposition \claimref{pairing.stabiliser-parabolic-algebra-null-direction}), and by Proposition \claimref{pairing.pairing-functional-pair-creation-amplitude} the spin transport $\exp(s\,\Omega(X))$ carries the vacuum, to first order in $s$ and up to a scalar, to $\ket{0} - s\,\pv(\Omega(X))\,\ket{12}$: the class is the Thouless amplitude of the mismatch. (Comparing the vacuum field against the transported frame instead reverses the sign; nothing below depends on the convention.)

## technical
Along a direction $X$ the Levi-Civita connection acts on the Clifford fibre by a bivector $\Omega(X)$, in the sense that $\nabla_X v = \tfrac12[\Omega(X), v]$ for vectors of constant frame components. Relative to a vacuum field with null direction $\ell$ and transverse complex null vector $m$, the pairing class of the transport along $X$ is $\pv(\Omega(X)) = \ip{\Omega(X)\cdot\ell}{m}$.

The transport preserves the vacuum ray along $X$ exactly when $\pv(\Omega(X)) = 0$, and to first order in $s$ the spin transport $\exp(s\,\Omega(X))$ carries the vacuum, up to a scalar, to $\ket{0} - s\,\pv(\Omega(X))\,\ket{12}$: the class is the Thouless amplitude of the mismatch. Comparing against the transported frame instead reverses the sign, and nothing depends on that convention.

## lay
A vacuum state of the fermion fields can be pictured as a choice of light-like direction at each point. Carrying that choice along a path using the geometry of spacetime may tilt it away from where the vacuum field says it should be. The pairing class measures that tilt, and it is the amplitude for the move to create a pair of particles out of the vacuum.

## one-liner
The pairing class of the transport along $X$ is $\pv(\Omega(X)) = \ip{\Omega(X)\cdot\ell}{m}$, which vanishes exactly when the transport preserves the vacuum ray and is, to first order, the pair-creation (Thouless) amplitude of the mismatch.
