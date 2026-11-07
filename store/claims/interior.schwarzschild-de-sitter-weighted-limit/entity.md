---
id: interior.schwarzschild-de-sitter-weighted-limit
kind: claim
version: 7
title: Schwarzschild-de Sitter weighted limit
status: proved
region: interior
subject: interior
tags: [schwarzschild, kasner, limits, cosmological-constant]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
review: typed
about:
- obj.interior.weighted-blow-up-hubble-normalisation-admissible
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - interior.boosts-generate-exactly-levi-factor@5
  - interior.exact-parallelism-convergence-rate@6
  - interior.kasner-form-interior@6
  - interior.non-null-stabilisers-section-they-act@4
  - interior.scale-tractor-leaves-cone@8
  - interior.weighted-limit-theorem@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:5.9
- kind: check
  ref: check.py::check_sds_field_is_schwarzschild_plus_de_sitter
- kind: check
  ref: check.py::check_corrections_relative_order_lambda_r3
- kind: check
  ref: check.py::check_holonomy_inside_reductive_stabiliser
locators:
  paper: T06
  number: Thm 5.9
  label: thm:sds
  line: 711
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the SdS gauge fields giving Schwarzschild plus de Sitter curvature, corrections of relative order Lambda r^3 in the series, and the holonomy inside the reductive stabiliser in Cl(2,4). Version 5 -> 6. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 6 -> 7.'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Tractor wording completed by the lead: the non-null parallel tractor is the scale tractor of the Cl(2,4) tractor gauge field of the gravitational field. Content unchanged.'
  typing:
    by: ai-typing-pass
    note: 'All six uses are premises of the proof (series manipulations, the connection statement, the tractor and stabiliser clauses).'
  env: theorem
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the Schwarzschild-de Sitter interior is named as a gravitational field (hb, Omega) on flat spacetime, and its metric functions as the functions of its derived metric; the connection is the rotation-gauge field. Orders, exponents and the holonomy clause unchanged (tractor wording left to the lead). Proof: one opening sentence pointing to the GTG dictionary Fact.'
---

## formal
For the Schwarzschild-de Sitter interior gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), in the synchronous gauge with $A(r) = 2M/r + \Lambda r^2/3 - 1 > 0$ near $r = 0$, every function of its derived metric expressed in Kasner time acquires relative corrections of order $\Lambda r^3/M \propto \Lambda\tau^2$ against the Schwarzschild case. Consequently the Hubble-normalised connection differs from the Schwarzschild one by $O(\Lambda\tau^2)$, strictly subdominant to the $O(\tau^{2/3})$ recovery rate, and Theorem \claimref{interior.weighted-limit-theorem} holds verbatim: identical Kasner exponents $(-\tfrac13, \tfrac23, \tfrac23)$, identical boundary data, identical convergence rate. The holonomy clause is upgraded rather than weakened: for $\Lambda > 0$ the limit algebra $\mathfrak{so}(1,3)$ now lies inside the \emph{reductive} stabiliser $\mathfrak{so}(1,4)$ of the non-null parallel tractor (parallel for the $\Cl(2,4)$ tractor gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}) of Theorem \claimref{interior.scale-tractor-leaves-cone}, and the vanishing of the nilradical component is automatic: there is no nilradical.

## technical
For the Schwarzschild-de Sitter interior gravitational field on flat spacetime, with $A(r) = 2M/r + \Lambda r^2/3 - 1 > 0$ near $r = 0$, every function of the derived metric written in Kasner time acquires relative corrections of order $\Lambda r^3/M \propto \Lambda\tau^2$ against Schwarzschild. Hence the Hubble-normalised connection differs from the Schwarzschild one by $O(\Lambda\tau^2)$, below the $O(\tau^{2/3})$ recovery rate, and the weighted limit theorem holds verbatim: the same exponents $(-\tfrac13, \tfrac23, \tfrac23)$, the same boundary data and the same convergence rate.

The holonomy clause is strengthened rather than weakened: for $\Lambda > 0$ the limit algebra $\mathfrak{so}(1,3)$ lies inside the reductive stabiliser $\mathfrak{so}(1,4)$ of the non-null parallel scale tractor, so the vanishing of the nilradical component is automatic, there being no nilradical.

## lay
A cosmological constant, the ingredient behind the accelerating expansion of the universe, changes a black hole's gravitational field only very slightly near its centre. This result shows that the limiting behaviour at the singularity is the same as without it, with the same powers and the same rates. The one change is algebraic, and it makes the picture simpler rather than more complicated.

## one-liner
In the Schwarzschild-de Sitter interior the corrections are $O(\Lambda\tau^2)$, so the weighted limit holds with the same exponents, data and rate, and for $\Lambda > 0$ the limit algebra lies in the reductive stabiliser $\mathfrak{so}(1,4)$.
