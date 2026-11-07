---
id: standard-model.imported-grip-area-casimir-form
kind: claim
version: 5
title: 'Imported: the grip, the area, and the Casimir form'
status: proved
region: standard-model
subject: mass
tags: [frozen-point, mass-generation, representation-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
about:
- obj.mass.grip-mass-composite
derivations:
- name: main
  uses:
  - mass.casimir-form-join@8
  - mass.mass-symplectic-area-two-twistor-formula@3
  - standard-model.imported-fock-model-twistor-space@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_grip_is_the_casimir_difference
- kind: check
  ref: check.py::check_flat_grip_is_the_momentum
- kind: check
  ref: check.py::check_spinor_momenta_and_area
locators:
  paper: T12
  number: Fact 9.3
  label: fact:grip
  line: 1539
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Q(P) = Q(I)(C_2(V) - C_2(I^perp)) for sample moments and frozen points, the flat grip as momentum, and the spinor momenta and area. Version 4 -> 5.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: fact
  context_refs:
  - mass.casimir-form-join
  - mass.mass-symplectic-area-two-twistor-formula
  - standard-model.imported-fock-model-twistor-space
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    added:
    - standard-model.imported-fock-model-twistor-space
    note: Added the Fock-model Fact from context_refs, which (iii) uses for the dual-twistor case; kept
      the two mass-paper results it restates. The E204 here traces to mass.casimir-form-join, outside
      this list.
  source_title: 'Imported: the grip, the area, and the Casimir form'
  source_formal: |-
    (i) For a nonzero ambient vector $I$ and a composite with conformal moment map $M$, the grip is the ambient vector $P = M(I)$ with $\ip{P}{U} = M_{U \wedge I}$ for all $U$, where $M_{U \wedge I}$ is the value on the composite of the generator $A(U \wedge I) \in \so(2,4)$; the mass-squared relative to $I$ is $m^{2} = \ip{P}{P}$. (ii) At $\Lambda = 0$ the frozen point is $I = n_{\infty}$, the $x$-slot part of $P$ is the total momentum and $m^{2}$ is the Poincar\'e Casimir $p^{2}$. (iii) A single twistor carries the null momentum $p_{AA'} = \pi_{A}\bar\pi_{A'}$ and is massless; a single dual twistor likewise, through the conjugation of Fact \claimref{standard-model.imported-fock-model-twistor-space}; and for two twistors $p^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$, the squared symplectic area of the spinor parts, with $\br{\pi^{1}\pi^{2}} = \det(\pi^{i}_{A})$ the determinant over the slot index. (iv) For $\Lambda > 0$, $\ip{P}{P} = \ip{I}{I}\bigl(C_{2}(\so(2,4)) - C_{2}(\so(1,4))\bigr)$, the difference of the conformal and de Sitter Casimirs evaluated on the composite, with $\ip{I}{I} = \Lambda/3 = H^{2}$. \emph{Provenance:} \cite[Def.~5.4, Prop.~4.1, Prop.~5.7]{ButlerT11}; proved there, (ii) and the Casimir normalisation at the levels declared there.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Single and dual twistors and the two-twistor area are now named by conformal spinors in all levels and the restated proof; nothing kept in twistor form.'
---

## formal
(i) For a nonzero ambient vector $I$ and a composite with conformal moment map $M$, the grip is the ambient vector $P = M(I)$ with $\ip{P}{U} = M_{U \wedge I}$ for all $U$, where $M_{U \wedge I}$ is the value on the composite of the generator $A(U \wedge I) \in \so(2,4)$; the mass-squared relative to $I$ is $m^{2} = Q(P)$. (ii) At $\Lambda = 0$ the frozen point is $I = n_{\infty}$, the $x$-slot part of $P$ is the total momentum and $m^{2}$ is the Poincar\'e Casimir $p^{2}$. (iii) A single conformal spinor (twistor) carries the null momentum $p_{AA'} = \pi_{A}\bar\pi_{A'}$ and is massless; a single dual conformal spinor likewise, through the conjugation of Fact \claimref{standard-model.imported-fock-model-twistor-space}; and for two conformal spinors $p^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$, the squared symplectic area of the spinor parts, with $\br{\pi^{1}\pi^{2}} = \det(\pi^{i}_{A})$ the determinant over the slot index. (iv) For $\Lambda > 0$, $Q(P) = Q(I)\bigl(C_{2}(\so(2,4)) - C_{2}(\so(1,4))\bigr)$, the difference of the conformal and de Sitter Casimirs evaluated on the composite, with $Q(I) = \Lambda/3 = H^{2}$. \emph{Provenance:} \cite[Def.~5.4, Prop.~4.1, Prop.~5.7]{ButlerT11}; proved there, (ii) and the Casimir normalisation at the levels declared there.

## technical
For a nonzero ambient vector $I$ and a composite with conformal moment map $M$, the grip is the ambient vector $P = M(I)$ with $\ip{P}{U} = M_{U \wedge I}$ for all $U$, and the mass squared relative to $I$ is $m^{2} = Q(P)$. At $\Lambda = 0$, with $I = n_{\infty}$, the spacetime part of $P$ is the total momentum and $m^{2}$ is the Poincar\'e Casimir $p^{2}$.

A single conformal spinor, or a single dual one, carries the null momentum $p_{AA'} = \pi_{A}\bar\pi_{A'}$ and is massless; two conformal spinors have $p^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$, the squared symplectic area of their spinor parts. For $\Lambda > 0$, $Q(P) = Q(I)\bigl(C_{2}(\so(2,4)) - C_{2}(\so(1,4))\bigr)$ with $Q(I) = \Lambda/3 = H^{2}$. These are restated from the mass paper at the levels declared there.

## lay
This restates how the series defines mass. A composite's grip on a chosen reference vector is itself a vector, and its length is the mass. With no cosmological constant this is the ordinary relativistic mass of the total momentum: one conformal spinor is massless, and two have a mass set by the area their spinor parts span. With a positive cosmological constant the same mass is a difference of two symmetry invariants.

## one-liner
The grip $P = M(I)$ defines mass by $m^{2} = Q(P)$, which is $p^{2}$ at $\Lambda = 0$, the two-spinor area for two conformal spinors, and a difference of conformal and de Sitter Casimirs for $\Lambda > 0$.
