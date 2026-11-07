---
id: standard-model.imported-frozen-point-dictionary
kind: claim
version: 8
title: 'Imported: the frozen point and the dictionary'
status: proved
region: standard-model
subject: dark-energy
tags: [frozen-point, dictionaries, the-number-n, mass-generation]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 8
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - interior.covariant-form-vacuum-equations@5
  - interior.scale-tractor-leaves-cone@7
  - mass.de-sitter-scale-frozen-point@6
  - mass.mass-weight-dictionary@4
  - mass.weight-polynomial-two-series@6
  - standard-model.imported-frozen-point-dictionary-external@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_frozen_point_and_flat_chart
- kind: check
  ref: check.py::check_dictionary_is_klein_gordon_in_de_sitter_chart
- kind: check
  ref: check.py::check_weight_polynomial_and_complex_weights
- kind: check
  ref: check.py::check_number_n_is_planck_over_hubble
locators:
  paper: T12
  number: Fact 2.5
  label: fact:dictionary
  line: 883
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The de Sitter weight -3/2 +- i nu, a physical number, is written -3/2 +- I_4 nu with numbers read in span{1, I_4} (formal, technical, proof), as in the restated mass.weight-polynomial-two-series; the source record under extraction is left as it was; no bare i remains.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the frozen point and its flat chart, the dictionary as the exact identity (box_g + m^2) sigma^-w f = -sigma^(1-w) I.Df for w = 0..-3, the weight polynomial and complex weights, and N = 1.03e61 from PDG 2024 values. Version 6 -> 7.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Einstein region is that of a gravitational field on flat spacetime and the frozen point the parallel scale tractor of the tractor gauge field; the flat chart of the conformal model is the flat background. Content unchanged.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'A5 largeness follow-up: N = M_P/H is about 1.0e61 (1.03e61 for G = M_P^-2 at the measured H), not of order 1e60; all levels and the proof restatement corrected (the T12 source text still says 1e60 and needs the same fix).'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'the de Sitter weight -3/2 +- i nu (a complex number labelling a principal-series representation, not an operator unit)'
  env: fact
  context_refs:
  - interior.covariant-form-vacuum-equations
  - interior.scale-tractor-leaves-cone
  - mass.de-sitter-scale-frozen-point
  - mass.mass-weight-dictionary
  - mass.weight-polynomial-two-series
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: All six uses are the stated provenance (interior Theorems 4.5 and 4.7, mass Theorem 3.1, Corollary
      3.2 and Lemma 5.1, and the external record value) and were kept; the formula is the familiar de
      Sitter mass-dimension relation, but this paper does not say it is also obtained by the standard
      route, so no standard-route derivation.
  source_title: 'Imported: the frozen point and the dictionary'
  source_formal: |-
    On the Einstein region with $\Lambda \neq 0$ the frozen point $I$ is the parallel scale tractor, of squared norm $\ip{I}{I} = \Lambda/3 = H^{2}$, and in the flat twistor chart its frozen point is $I_{\Lambda} = n_{\infty} + (\Lambda/6)\,n_{0}$. Mass is conformal weight read against it: a density of weight $w$ coupled to the frozen point obeys the Klein-Gordon equation with
    \[
    m^{2} = -\,w(w+3)\,\frac{\Lambda}{3} = \Delta(3-\Delta)\,H^{2}, \qquad \Delta = -w,
    \]
    so a real weight gives $m^{2} \ge 0$ only on $w \in [-3, 0]$, where $m \le 3H/2$, and every heavier field has complex weight $w = -\tfrac32 \pm i\nu$ with $\nu \approx m/H$. In particular the weight of the Planck mass is complex, and its imaginary part is
    \[
    N := \operatorname{Im} w(M_{P}) \approx M_{P}/H, \qquad\text{of order } 10^{60}.
    \]
    Throughout this paper $N$ means $M_{P}/H$, the number the dictionary attaches to the Planck mass. \emph{Provenance:} \cite[Thms.~4.5, 4.7]{ButlerT6} for the frozen point and its norm; \cite[Thm.~3.1, Cor.~3.2]{ButlerT11} for the dictionary and the complex weights; \cite[Lem.~5.1]{ButlerT11} for the chart form of $I_{\Lambda}$. The value $10^{60}$ is the measured ratio $M_{P}/H$ and carries the record's status \cite{PDG2024}.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the flat twistor chart to the flat chart of the conformal model (formal, technical, restated proof). The complex conformal weight $w = -\tfrac32 \pm i\nu$ is a complex eigenvalue, not twistor machinery, and is kept.'
---

## formal
On the Einstein region with $\Lambda \neq 0$ of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), the frozen point $I$ is the scale tractor parallel for the tractor gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, of squared norm $Q(I) = \Lambda/3 = H^{2}$, and in the flat chart of the conformal model (the flat twistor chart, the flat background itself) its frozen point is $I_{\Lambda} = n_{\infty} + (\Lambda/6)\,n_{0}$. Mass is conformal weight read against it: a density of weight $w$ coupled to the frozen point obeys the Klein-Gordon equation with
\[
m^{2} = -\,w(w+3)\,\frac{\Lambda}{3} = \Delta(3-\Delta)\,H^{2}, \qquad \Delta = -w,
\]
so a real weight gives $m^{2} \ge 0$ only on $w \in [-3, 0]$, where $m \le 3H/2$, and every heavier field has complex weight $w = -\tfrac32 \pm I_4\nu$ (numbers are read in $\mathrm{span}\{1, I_4\}$) with $\nu \approx m/H$. In particular the weight of the Planck mass is complex, and its imaginary part is
\[
N := \operatorname{Im} w(M_{P}) \approx M_{P}/H, \qquad\text{about } 1.0 \times 10^{61}.
\]
Throughout this paper $N$ means $M_{P}/H$, the number the dictionary attaches to the Planck mass. \emph{Provenance:} \cite[Thms.~4.5, 4.7]{ButlerT6} for the frozen point and its norm; \cite[Thm.~3.1, Cor.~3.2]{ButlerT11} for the dictionary and the complex weights; \cite[Lem.~5.1]{ButlerT11} for the chart form of $I_{\Lambda}$. The value, about $1.0 \times 10^{61}$ for $G = M_{P}^{-2}$, is the measured ratio $M_{P}/H$ and carries the record's status \cite{PDG2024}.

## technical
For a gravitational field on flat spacetime, on its Einstein region with $\Lambda \neq 0$ the frozen point is the scale tractor $I$ parallel for the tractor gauge field, with $Q(I) = \Lambda/3 = H^{2}$, which in the flat chart of the conformal model is $I_{\Lambda} = n_{\infty} + (\Lambda/6)\,n_{0}$. A density of conformal weight $w$ coupled to the frozen point obeys the Klein-Gordon equation with $m^{2} = -w(w+3)\Lambda/3 = \Delta(3-\Delta)H^{2}$, where $\Delta = -w$.

A real weight gives $m^{2} \ge 0$ only for $w \in [-3,0]$, where $m \le 3H/2$; every heavier field has complex weight $w = -\tfrac32 \pm I_4\nu$ (numbers are read in $\mathrm{span}\{1, I_4\}$) with $\nu \approx m/H$. For the Planck mass this defines $N := \operatorname{Im} w(M_{P}) \approx M_{P}/H$, about $1.0 \times 10^{61}$, the value being the measured ratio.

## lay
In this framework the mass of a field is read off from how it scales, measured against the frozen point whose length sets the cosmological constant. Only extremely light fields, no heavier than about the present expansion rate of the universe, get an ordinary real scaling number; everything heavier gets a complex one. For the Planck mass the imaginary part is a number of about $10^{61}$, called $N$, which later results treat as the theory's single large number.

## one-liner
Mass is conformal weight read against the frozen point, $m^{2} = \Delta(3-\Delta)H^{2}$, so heavy fields have complex weight and the Planck mass's imaginary weight is $N \approx M_{P}/H$, about $10^{61}$.
