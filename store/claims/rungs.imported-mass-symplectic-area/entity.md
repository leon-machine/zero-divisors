---
id: rungs.imported-mass-symplectic-area
kind: claim
version: 4
title: 'Imported: mass as symplectic area'
status: proved
region: rungs
subject: mass
tags: [conformal-spinors, frozen-point, mass-generation]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-rungs, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - mass.de-sitter-scale-frozen-point@6
  - mass.mass-symplectic-area-two-twistor-formula@3
  - standard-model.imported-frozen-point-dictionary@7
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_single_null_and_two_spinor_mass
- kind: check
  ref: check.py::check_frozen_point_in_the_flat_chart
locators:
  paper: T12-rungs
  number: Fact 1.4
  label: fact:area
  line: 213
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: null single momenta and m^2 = 2|<pi1 pi2>|^2, and I_Lambda = n_inf + (Lambda/6) n0 with norm Lambda/3 and scale function 1 - Lambda Q/12, unique. Version 3 -> 4.'
  env: fact
  context_refs:
  - mass.de-sitter-scale-frozen-point
  - mass.mass-symplectic-area-two-twistor-formula
  - standard-model.imported-frozen-point-dictionary
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: All three uses are the cited sources of this restating Fact and are kept.
  source_title: 'Imported: mass as symplectic area'
  source_formal: |-
    On the real slice a single twistor carries null momentum $p_{AA'} = \pi_{A}\bar\pi_{A'}$, and a two-twistor system with $p = \pi^{1}\bar\pi^{1} + \pi^{2}\bar\pi^{2}$ has $m^{2} = p^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$, with $\br{\pi^{1}\pi^{2}} = \varepsilon^{AB}\pi^{1}_{A}\pi^{2}_{B}$. In the flat twistor chart the frozen point is $I_{\Lambda} = n_{\infty} + (\Lambda/6)\,n_{0}$, so at $\Lambda = 0$ it is $n_{\infty}$. \emph{Provenance:} \cite[Prop.~4.1, Lem.~5.1]{ButlerT11}; \cite[Fact~2.5]{ButlerT12}.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'The imported statement and its restated proof now speak of conformal spinors and the flat chart of CS; nothing kept in twistor form.'
---

## formal
On the real slice a single conformal spinor (twistor) carries null momentum $p_{AA'} = \pi_{A}\bar\pi_{A'}$, and a system of two conformal spinors with $p = \pi^{1}\bar\pi^{1} + \pi^{2}\bar\pi^{2}$ has $m^{2} = p^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$, with $\br{\pi^{1}\pi^{2}} = \varepsilon^{AB}\pi^{1}_{A}\pi^{2}_{B}$. In the flat chart of the conformal spinor space $\CS$ the frozen point is $I_{\Lambda} = n_{\infty} + (\Lambda/6)\,n_{0}$, so at $\Lambda = 0$ it is $n_{\infty}$. \emph{Provenance:} \cite[Prop.~4.1, Lem.~5.1]{ButlerT11}; \cite[Fact~2.5]{ButlerT12}.

## technical
On the real slice a single conformal spinor carries null momentum $p_{AA'} = \pi_{A}\bar\pi_{A'}$, and a system of two conformal spinors with $p = \pi^{1}\bar\pi^{1} + \pi^{2}\bar\pi^{2}$ has $m^{2} = p^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$, where $\br{\pi^{1}\pi^{2}} = \varepsilon^{AB}\pi^{1}_{A}\pi^{2}_{B}$.

In the flat chart of $\CS$ the frozen point is $I_{\Lambda} = n_{\infty} + \tfrac{\Lambda}{6}n_{0}$, which is $n_{\infty}$ at $\Lambda = 0$.

## lay
This recalls two earlier facts. A particle built from two spinors of the conformal geometry has a mass set by how misaligned their light-like directions are. And in the flat picture the cosmological scale is a fixed vector which, when the cosmological constant is zero, is the familiar point at infinity.

## one-liner
Two conformal spinors have $m^{2} = 2|\br{\pi^{1}\pi^{2}}|^{2}$, and in the flat chart the frozen point is $I_{\Lambda} = n_{\infty} + \tfrac{\Lambda}{6}n_{0}$.
