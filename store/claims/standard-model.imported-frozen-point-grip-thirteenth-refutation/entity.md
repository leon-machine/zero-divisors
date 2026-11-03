---
id: standard-model.imported-frozen-point-grip-thirteenth-refutation
kind: claim
version: 6
title: 'Imported: the frozen point, the grip, and the thirteenth refutation'
status: proved
region: standard-model
subject: mass
tags: [frozen-point, mass-generation, refutation]
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
  - families.alignment-computed-thirteenth-refutation-democracy-one@4
  - mass.exact-join@7
  - mass.imported-frozen-point-tractor-connection@6
  - mass.mass-symplectic-area-two-twistor-formula@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_frozen_point_in_its_own_scale
- kind: check
  ref: check.py::check_two_spinor_mass_is_symplectic_area
- kind: check
  ref: check.py::check_exact_join_grip_mass
- kind: check
  ref: check.py::check_thirteenth_refutation_magnitudes
locators:
  paper: T12
  number: Fact 9.5
  label: fact:frozen
  line: 1547
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the frozen point (1, 0, J/4) with Q(I) = Lambda/3, the two-spinor mass 2|<pi1 pi2>|^2, the exact join from the moment-map definition of the grip, and the orders of ten of the refutation. Version 5 -> 6.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the conformal structure is that of a gravitational field on flat spacetime, the canonical connection its tractor gauge field, the background the vacuum Einstein field; mass, grip and refutation unchanged.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: fact
  context_refs:
  - families.alignment-computed-thirteenth-refutation-democracy-one
  - mass.exact-join
  - mass.imported-frozen-point-tractor-connection
  - mass.mass-symplectic-area-two-twistor-formula
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Kept the four edges to the series results the Fact restates (its proof text repeats the statement);
      status left proved since the restated results are in the store. Levels pass: the lay and one-liner
      now keep the vacuum Einstein background, and the lay keeps ''at the levels declared there''.'
  source_title: 'Imported: the frozen point, the grip, and the thirteenth refutation'
  source_formal: |-
    The ambient (tractor) bundle of a conformal structure has fibre $V = \R^{1,3} \oplus H_{1}$, $H_{1}$ the hyperbolic plane of the first completion, and carries the canonical connection; on a vacuum Einstein background with cosmological constant $\Lambda$ it carries a distinguished parallel section, the frozen point $I$, which in its own scale has components $(1, 0, \rho_{I})$, the $\R^{1,3}$ slot vanishing, with $\ip{I}{I} = \Lambda/3$; at $\Lambda = 0$ it is the null point at infinity $\nInf^{(1)}$. Mass is coupling to $I$: the mass of a composite is the length of its grip $P = M(I)$, defined through the sesquilinear moment map; for two twistors $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$ at $\Lambda = 0$, and at general $\Lambda$ the exact join gives $m^{2} = 2|B_{\Lambda}|^{2} + (\Lambda/3)\,C$ with $B_{\Lambda} = \br{\pi^{1}\pi^{2}} + (\Lambda/6)[\omega^{1}\omega^{2}]$ and $C$ the internal $\mathfrak{su}(2)$ Casimir of the constituents' Gram matrix. The families paper shows that the bracket's magnitude, fixed by the exact join, cannot reach the weak scale. \emph{Provenance:} \cite[Fact~2.1, Def.~5.4, Prop.~4.1, Thm.~5.6]{ButlerT11}; \cite[Prop.~4.3]{ButlerT13}; at the levels declared there.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'The two constituents are now conformal spinors in all levels and the restated proof; nothing kept in twistor form.'
---

## formal
For a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), the ambient (tractor) bundle of the conformal structure of its derived metric has fibre $V = \R^{1,3} \oplus H_{1}$, $H_{1}$ the hyperbolic plane of the first completion, and carries the canonical connection, on flat spacetime the $\Cl(2,4)$ gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}; for a vacuum Einstein field with cosmological constant $\Lambda$ it carries a distinguished parallel section, the frozen point $I$, which in its own scale has components $(1, 0, \rho_{I})$, the $\R^{1,3}$ slot vanishing, with $Q(I) = \Lambda/3$; at $\Lambda = 0$ it is the null point at infinity $\nInf^{(1)}$. Mass is coupling to $I$: the mass of a composite is the length of its grip $P = M(I)$, defined through the sesquilinear moment map; for two conformal spinors (twistors) $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$ at $\Lambda = 0$, and at general $\Lambda$ the exact join gives $m^{2} = 2|B_{\Lambda}|^{2} + (\Lambda/3)\,C$ with $B_{\Lambda} = \br{\pi^{1}\pi^{2}} + (\Lambda/6)[\omega^{1}\omega^{2}]$ and $C$ the internal $\mathfrak{su}(2)$ Casimir of the constituents' Gram matrix. The families paper shows that the bracket's magnitude, fixed by the exact join, cannot reach the weak scale. \emph{Provenance:} \cite[Fact~2.1, Def.~5.4, Prop.~4.1, Thm.~5.6]{ButlerT11}; \cite[Prop.~4.3]{ButlerT13}; at the levels declared there.

## technical
For a vacuum Einstein gravitational field on flat spacetime with cosmological constant $\Lambda$, the ambient (tractor) bundle, whose connection is the tractor gauge field, with fibre $V = \R^{1,3} \oplus H_{1}$, carries a distinguished parallel section, the frozen point $I$, with components $(1, 0, \rho_{I})$ in its own scale and $Q(I) = \Lambda/3$; at $\Lambda = 0$ it is the null point at infinity. The mass of a composite is the length of its grip $P = M(I)$, defined through the sesquilinear moment map.

For two conformal spinors, $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$ at $\Lambda = 0$, and at general $\Lambda$ the exact join gives $m^{2} = 2|B_{\Lambda}|^{2} + (\Lambda/3)\,C$, with $B_{\Lambda} = \br{\pi^{1}\pi^{2}} + (\Lambda/6)[\omega^{1}\omega^{2}]$ and $C$ the internal $\su(2)$ Casimir of the constituents' Gram matrix. The families result adds that the bracket's magnitude, fixed by the exact join, cannot reach the weak scale. All of this is restated from the mass and families papers at the levels declared there.

## lay
This collects earlier results of the series that the mass section builds on. The geometry of an empty-space (vacuum Einstein) spacetime with a cosmological constant singles out a fixed reference point, the frozen point, and mass is defined as how strongly a composite grips it. For two conformal spinors the mass is given by an area formula, with a correction when the cosmological constant is nonzero. An earlier paper showed that this bracket alone cannot be as large as the weak scale. Each result holds at the level declared where it was established.

## one-liner
On a vacuum Einstein background the frozen point is a parallel ambient section with $Q(I) = \Lambda/3$, mass is the length of a composite's grip on it, and the resulting two-spinor bracket cannot reach the weak scale.
