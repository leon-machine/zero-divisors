---
id: singularity.area-law-test
kind: claim
version: 5
title: The area-law test
status: proved
region: singularity
subject: entropy
tags: [mode-counting, boundary-modes]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
derivations:
- name: main
  uses:
  - singularity.stretched-singularity-count@8
  - singularity.causal-epoch-computed-exactly@4
  assumes:
  - singularity.c1-curvature-cutoff@4
  - singularity.c2-cell-density@4
  - singularity.c3-counted-epoch@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:10.7
- kind: check
  ref: check.py::check_capacity_matches_entropy_iff_calibration
- kind: check
  ref: check.py::check_leading_order_and_epoch_scale
- kind: check
  ref: check.py::check_lifetime_scalings
locators:
  paper: T05
  number: Prop 10.7
  label: prop:arealaw
  line: 2181
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: C = 4 pi M^2 iff nu Delta t = M/(2 ln 2) with ln 2 an indeterminate, the old calibration off by ln 2, the leading-order factor, the M-independence of nu, and the lifetime degrees 4 and 5. Version 4 -> 5.'
  env: proposition
  context_refs:
  - singularity.assembled-page-curve-up-typicality
  - singularity.causal-epoch-computed-exactly
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    added:
    - singularity.causal-epoch-computed-exactly
    - singularity.c1-curvature-cutoff
    - singularity.c2-cell-density
    - singularity.c3-counted-epoch
    note: 'Removed the mechanically added transport-algorithm edge (section framing, not a premise of
      the arithmetic); added the postulates (C1)-(C3) the statement assumes and the causal-epoch lemma
      through which it says (C3) supplies the order-M epoch; no standard route, since the match to Bekenstein-Hawking
      is a calibration and that entropy is not an imported claim in the store. Levels pass: the lay level
      now names the postulates (C1) to (C3) and the leading-order qualifier.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - singularity.c1-curvature-cutoff
    - singularity.c2-cell-density
    - singularity.c3-counted-epoch
    stated_role:
    - singularity.causal-epoch-computed-exactly
---

## formal
Assume (C1)-(C3), write $N_{\mathrm{6a}} = (dN_{\mathrm{6a}}/dt)\,\Delta t$ for the mode count of the counted epoch, and let $C := N_{\mathrm{6a}}\ln 2$ be its boundary-mode capacity in nats, $\ln 2$ per fermionic mode. Then, at leading order in $M$, $C = S_{\mathrm{BH}} = 4\pi M^2$ if and only if $\nu\,\Delta t = M/(2\ln 2)$: the capacity matches the Bekenstein-Hawking entropy \cite{Bekenstein1973, Hawking1975}, the coefficient calibrated by $\nu\,\Delta t$ rather than predicted (the closing paragraph of this section quantifies the conventions), exactly when the counted epoch is of order one Schwarzschild time, which is what (C3) supplies via Lemma \claimref{singularity.causal-epoch-computed-exactly}, the $\ln 2$ being absorbed into the order-one calibration of $\nu\,\Delta t$. It is the capacity, not the bare count, that premise (C) and Fact \claimref{singularity.assembled-page-curve-up-typicality} compare with $S_{\mathrm{BH}}$; the count itself then reads $N_{\mathrm{6a}} = S_{\mathrm{BH}}/\ln 2$. Counting over the hole's whole lifetime instead gives $N_{\mathrm{6a}} \sim M^4$, which shares with the interior-volume growth of Christodoulou-Rovelli \cite{CR2015} the linearity in advanced time and the unresolved tension with the constancy of the horizon entropy, though not the mass scaling: their $dV/dv \propto M^{2}$ gives $V \sim M^{5}$ over the lifetime, while $dN_{\mathrm{6a}}/dt \propto M$ gives $M^{4}$ here.

## technical
Under the postulates (C1) to (C3), let $N_{\mathrm{6a}} = (dN_{\mathrm{6a}}/dt)\,\Delta t$ be the mode count of the counted epoch and $C = N_{\mathrm{6a}}\ln 2$ its boundary-mode capacity in nats. Using the stretched-singularity count, $dN_{\mathrm{6a}}/dt = 8\pi\nu M$ at leading order, the capacity equals the Bekenstein-Hawking entropy, $C = \SBH = 4\pi M^2$, if and only if $\nu\,\Delta t = M/(2\ln 2)$.

The match therefore holds exactly when the counted epoch is of order one Schwarzschild time, which is what (C3) supplies through the causal-epoch computation; the coefficient is calibrated through $\nu\,\Delta t$, not predicted. Counting over the whole lifetime instead gives $N_{\mathrm{6a}} \sim M^4$.

## lay
The framework counts quantum modes on a surface just outside a black hole's singularity. Granting the paper's three counting postulates (C1) to (C3), a curvature cutoff, a cell density and a counted epoch, and for large black holes (at leading order in the mass), if those modes are counted over a span of time comparable to the black hole's natural time scale, their total information capacity matches the standard black-hole entropy, which grows with the horizon area. The overall number is set by one order-one constant rather than predicted. Counting over the hole's whole life would instead give far too many modes.

## one-liner
Under (C1) to (C3), the boundary-mode capacity equals $\SBH = 4\pi M^2$ at leading order exactly when $\nu\,\Delta t = M/(2\ln 2)$, an epoch of order one Schwarzschild time.
