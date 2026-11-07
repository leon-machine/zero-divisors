---
id: sheaf.kasner-data-interior
kind: claim
version: 3
title: Kasner data of the interior
status: imported
region: sheaf
subject: interior
tags: [classical-theorem, kasner, schwarzschild]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, duplicate link at Leon''s decisions'
  version: 3
  source: maintainer pass 2026-11-07 (decisions)
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: E. Kasner, Geometrical theorems on Einstein's cosmological equations, Amer. J. Math. 43 (1921),
    217--221.
  key: Kasner1921
locators:
  paper: T04
  number: Fact 8.2
  label: fact:kasner
  line: 867
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3. Decision item E4 (routine; no retirement): equivalent_to interior.kasner-form-interior@6 added. This imported Kasner form (Kasner 1921) is what interior.kasner-form-interior proves with rates, the proved home; both are kept (this one''s users pin it, and making it proved would be a status change), and the link marks the restatement so the two are counted once.'
  typing:
    by: ai-typing-pass
    note: 'Imported fact with no derivation; nothing to edge.'
  env: fact
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the metric is the derived metric of the Schwarzschild gravitational field (hb, Omega) on flat spacetime. Exponents and proper time unchanged.'
equivalent_to:
- interior.kasner-form-interior@7
---

## formal
Along the approach to the Schwarzschild singularity the derived metric of the gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) takes Kasner form \cite{Kasner1921} with exponents $(p_1, p_2, p_3) = (-\tfrac13, \tfrac23, \tfrac23)$, $\sum p_i = \sum p_i^2 = 1$, in proper time $\tau_{\mathrm{p}} \propto r^{3/2}$. \emph{Provenance:} classical; proved exactly, with rates, in the Kasner form lemma of \cite{ButlerT6}.

## technical
Along the approach to the Schwarzschild singularity the derived metric of the gravitational field on flat spacetime takes Kasner form, with exponents $(p_1, p_2, p_3) = (-\tfrac13, \tfrac23, \tfrac23)$ satisfying $\sum_i p_i = \sum_i p_i^2 = 1$, in proper time $\tau_{\mathrm p} \propto r^{3/2}$. This is classical, imported from Kasner's work; the series also proves it exactly, with rates, in its treatment of the interior.

## lay
Near the centre of a non-rotating black hole, space behaves like a Kasner universe: one direction stretches and the other two shrink, each as a fixed power of time. The powers are minus one third and two thirds twice. This is a classical result.

## one-liner
Near the Schwarzschild singularity the derived metric of the gravitational field is of Kasner form with exponents $(-\tfrac13, \tfrac23, \tfrac23)$ in proper time $\tau_{\mathrm p} \propto r^{3/2}$; imported as classical.
