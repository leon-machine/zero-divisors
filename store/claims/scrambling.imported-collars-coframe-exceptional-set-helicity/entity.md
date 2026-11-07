---
id: scrambling.imported-collars-coframe-exceptional-set-helicity
kind: claim
version: 6
title: 'Imported: the collar''s coframe at the exceptional set, and the helicity lift'
status: proved
region: scrambling
subject: interior
tags: [schwarzschild, kasner, conformal-spinors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T08, deposited version
review: typed
about:
- obj.interior.weighted-blow-up-hubble-normalisation-admissible
- obj.sheaf.weighted-coframe-module
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - hawking.helicity-lift-joints-itemised@5
  - hawking.homogeneity-ordering-shift@6
  - hawking.imported-penrose-transform@3
  - interior.interior-connection-exactly@8
  - interior.kasner-form-interior@7
  - sheaf.weights-are-forced-are-kasner-exponents@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_weighted_coframe_on_the_exceptional_set
- kind: check
  ref: check.py::check_orders_become_kasner_exponents
- kind: check
  ref: check.py::check_helicity_homogeneities
locators:
  paper: T08
  number: Fact 4.7
  label: fact:collarframe
  line: 768
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: weighted coframe of the interior gauge field and its orders, conversion to Kasner exponents in proper time, helicity homogeneities -2s-2. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6.'
  typing:
    by: ai-typing-pass
    note: 'Fact restating series results: kept the restated sources (weights from the interior lemmas
      and the forced sheaf weights, the lift from the Hawking paper); the lift enters at modelling tier,
      which the edge to the itemised-joints assembly carries. Levels pass: conditions already kept.'
  env: fact
  context_refs:
  - hawking.helicity-lift-joints-itemised
  - hawking.homogeneity-ordering-shift
  - hawking.imported-penrose-transform
  - interior.interior-connection-exactly
  - interior.kasner-form-interior
  - sheaf.weights-are-forced-are-kasner-exponents
  flags:
  - 'fact restating several series results: derived from them'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the weighted coframe is named as the rescaled components of the physical-vector map hb^{-1} of the Schwarzschild interior gravitational field on flat spacetime (the coframe of its derived metric). Weights, normalisation and the helicity lift unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact.'
---

## formal
In units $2M = 1$ the weighted coframe of the Schwarzschild interior gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), the components of its physical-vector map $\hb^{-1}$ in the orthonormal frame adapted to $(t, \theta, \varphi)$, rescaled, carries the weights $r^{1/2}$ on $\sqrt{A}\,dt$ and $r^{-1}$ on $r\,d\theta$, $r\sin\theta\,d\varphi$: these are the Kasner exponents $(-\tfrac13, \tfrac23, \tfrac23)$ of the proper-time variable $\tau \propto r^{3/2}$ rewritten in the variable $r$, where they read $(-\tfrac12, 1, 1)$, normalised to one at $r = r_h$; the horizon-normalised coframe on the exceptional set is therefore $(dt,\ r_h\,d\theta,\ r_h\sin\theta\,d\varphi)$ exactly, $(r^{1/2}\sqrt{A})^2 = 1 - r \to 1$ and $r^{-1}\cdot r = 1$. In the Hawking paper's lift, each channel $(\omega, \ell, m, s)$ of the near-horizon reduction is one two-dimensional mode, and the two helicities of a massless species are two channels at distinct homogeneities $-2s - 2$ ($-4$ and $0$ for the photon, $-6$ and $+2$ for the graviton); the channel identification is that paper's joint J3, its one modelling joint, which it assigns to this paper as an open successor problem, so the lift enters here at modelling tier and not at theorem tier. \emph{Provenance:} \cite[Lemmas 5.1 to 5.3, Def.~5.5]{ButlerT6} and \cite[Thm.~8.16]{ButlerT4} for the weights; \cite[Fact~5.1, Prop.~5.2, Assembly~5.3]{ButlerT7} for the lift, Assembly 5.3 there itemising J3 as modelling.

## technical
In units $2M = 1$ the weighted coframe of the Schwarzschild interior gravitational field on flat spacetime, the rescaled components of $\hb^{-1}$, carries weights $r^{1/2}$ on $\sqrt A\,dt$ and $r^{-1}$ on $r\,d\theta$ and $r\sin\theta\,d\varphi$. These are the Kasner exponents $(-\tfrac13, \tfrac23, \tfrac23)$ of proper time $\tau \propto r^{3/2}$, rewritten in the variable $r$ as $(-\tfrac12, 1, 1)$ and normalised at $r = r_h$, so the horizon-normalised coframe on the exceptional set is exactly $(dt, r_h\,d\theta, r_h\sin\theta\,d\varphi)$.

In the Hawking paper's lift each channel $(\omega, \ell, m, s)$ of the near-horizon reduction is one two-dimensional mode, and the two helicities of a massless species are two channels at homogeneities $-2s-2$ ($-4$ and $0$ for the photon, $-6$ and $+2$ for the graviton). The channel identification is a modelling joint left open there, so the lift enters at modelling tier, not theorem tier. The statement collects results proved earlier in the series.

## lay
This collected result fixes two pieces of bookkeeping used later. First, it says how the natural measuring directions inside a black hole look when rescaled to the singular boundary: they become ordinary time and angle directions at the size of the horizon. Second, it recalls how the two helicities of light and of gravitational waves were assigned to separate modes in the series' account of Hawking radiation, an assignment that is a modelling step rather than a theorem.

## one-liner
The horizon-normalised weighted coframe on the Schwarzschild exceptional set is exactly $(dt, r_h\,d\theta, r_h\sin\theta\,d\varphi)$, and the two helicities of a massless species enter as two channels at homogeneities $-2s-2$, at modelling tier.
