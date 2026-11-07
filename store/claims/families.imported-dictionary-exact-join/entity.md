---
id: families.imported-dictionary-exact-join
kind: claim
version: 6
title: 'Imported: the dictionary and the exact join'
status: proved
region: families
subject: mass
tags: [frozen-point, conformal-spinors, dictionaries]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 6
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - mass.exact-join@7
  - mass.mass-weight-dictionary@4
  - mass.weight-composite@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T13.py
  tags:
  - label:fact:dictionary
- kind: check
  ref: check.py::check_dictionary_sign
- kind: check
  ref: check.py::check_exact_join_and_casimir
- kind: check
  ref: check.py::check_massless_locus_and_pure_residue
- kind: check
  ref: check.py::check_principal_series_expansion
locators:
  paper: T13
  number: Fact 2.2
  label: fact:dictionary
  line: 581
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The de Sitter weight -3/2 +- i nu, a physical number, is written -3/2 +- I_4 nu with numbers read in span{1, I_4}; no bare i remains.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the dictionary sign, B_Lambda and the exact join on grip-computed composites, C zero iff scalar Gram, the massless locus with pure-residue composites, and the nu expansion. Version 3 -> 4. Check strengthened: the massless example is asserted not doubled (Z1 ^ Z2 != 0) and with scalar Gram matrix (C = 0); lam and sample twistors moved to module level. Version 4 -> 5.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'the de Sitter weight -3/2 +- i nu (a complex number labelling a principal-series representation, not an operator unit)'
  env: fact
  context_refs:
  - mass.exact-join
  - mass.mass-weight-dictionary
  - mass.weight-composite
  outside_pilot_cites:
  - ButlerT11
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: All three uses are the cited sources of this restating Fact and are kept; no standard-physics
      route is claimed for it.
  source_title: 'Imported: the dictionary and the exact join'
  source_formal: |-
    Mass is conformal weight read against the frozen point: a density of weight $w$ coupled to the frozen point $I$ obeys the Klein-Gordon equation with $m^{2} = -w(w+3)\,\Lambda/3 = -w(w+3)H^{2}$. For the two-twistor composite the deformed bracket is $B_{\Lambda} = \br{\pi^{1}\pi^{2}} + \tfrac{\Lambda}{6}[\omega^{1}\omega^{2}]$ and the exact join is
    \[
    m^{2} \;=\; 2|B_{\Lambda}|^{2} + \frac{\Lambda}{3}\,C, \qquad C \ge 0,
    \]
    with $C$ the internal $\mathfrak{su}(2)$ Casimir of the pair, vanishing exactly when the Gram matrix of the two twistors is scalar; the massless composites for $\Lambda > 0$ are exactly those with $B_{\Lambda} = 0$ and scalar Gram matrix, and there are composites with $B_{\Lambda} = 0$ and $m^{2} = \Lambda C/3 \ne 0$. The induced weight of a composite heavier than $3H/2$ lies on the principal series, $w = -\tfrac32 \pm i\nu$ with $\nu = m/H - \tfrac98 H/m + O((H/m)^{3})$: the mass sits in the imaginary part. \emph{Provenance:} \cite[Thm.~3.1, Thm.~5.6, Prop.~5.9]{ButlerT11}, with $C$ defined at \cite[eq.~(9)]{ButlerT11} and read in \cite[Rem.~5.10]{ButlerT11}.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'The imported statement and its restated proof now speak of two conformal spinors; the principal-series i is the complex weight of a density and is kept.'
---

## formal
Mass is conformal weight read against the frozen point: a density of weight $w$ coupled to the frozen point $I$ obeys the Klein-Gordon equation with $m^{2} = -w(w+3)\,\Lambda/3 = -w(w+3)H^{2}$. For the composite of two conformal spinors (twistors) the deformed bracket is $B_{\Lambda} = \br{\pi^{1}\pi^{2}} + \tfrac{\Lambda}{6}[\omega^{1}\omega^{2}]$ and the exact join is
\[
m^{2} \;=\; 2|B_{\Lambda}|^{2} + \frac{\Lambda}{3}\,C, \qquad C \ge 0,
\]
with $C$ the internal $\mathfrak{su}(2)$ Casimir of the pair, vanishing exactly when the Gram matrix of the two spinors is scalar; the massless composites for $\Lambda > 0$ are exactly those with $B_{\Lambda} = 0$ and scalar Gram matrix, and there are composites with $B_{\Lambda} = 0$ and $m^{2} = \Lambda C/3 \ne 0$. The induced weight of a composite heavier than $3H/2$ lies on the principal series, $w = -\tfrac32 \pm I_4\nu$ (numbers are read in $\mathrm{span}\{1, I_4\}$) with $\nu = m/H - \tfrac98 H/m + O((H/m)^{3})$: the mass sits in the imaginary part. \emph{Provenance:} \cite[Thm.~3.1, Thm.~5.6, Prop.~5.9]{ButlerT11}, with $C$ defined at \cite[eq.~(9)]{ButlerT11} and read in \cite[Rem.~5.10]{ButlerT11}.

## technical
Two imported results. The dictionary: a density of weight $w$ coupled to the frozen point $I$ obeys the Klein-Gordon equation with $m^{2} = -w(w+3)\Lambda/3 = -w(w+3)H^{2}$. The exact join: for a two-spinor composite with deformed bracket $B_{\Lambda} = \br{\pi^{1}\pi^{2}} + \tfrac{\Lambda}{6}[\omega^{1}\omega^{2}]$, $m^{2} = 2|B_{\Lambda}|^{2} + \tfrac{\Lambda}{3}C$, with $C \ge 0$ the internal $\mathfrak{su}(2)$ Casimir of the pair, zero exactly when the Gram matrix of the two spinors is scalar.

For $\Lambda > 0$ the massless composites are exactly those with $B_{\Lambda} = 0$ and scalar Gram matrix, and some composites have $B_{\Lambda} = 0$ but $m^{2} = \Lambda C/3 \neq 0$. A composite heavier than $3H/2$ has induced weight $w = -\tfrac32 \pm I_4\nu$ (numbers are read in $\mathrm{span}\{1, I_4\}$) with $\nu = m/H - \tfrac98 H/m + O((H/m)^{3})$, so its mass sits in the imaginary part.

## lay
This gathers two earlier results for later use. First, a field's mass is fixed by a number called its weight, read against the single scale that the cosmological constant provides. Second, a particle made of two conformal spinors has an exact mass formula: a term measuring how misaligned its parts are, plus a small correction proportional to the cosmological constant. For any ordinary particle the weight is a complex number whose imaginary part carries the mass.

## one-liner
Mass is weight read against the frozen point, $m^{2} = -w(w+3)H^{2}$, and for two conformal spinors $m^{2} = 2|B_{\Lambda}|^{2} + \Lambda C/3$, which puts a heavy composite's mass in the imaginary part of its weight.
