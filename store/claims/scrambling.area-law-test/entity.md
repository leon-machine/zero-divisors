---
id: scrambling.area-law-test
kind: claim
version: 5
title: The area-law test
status: proved
region: scrambling
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
  source: authorship disclosure of T08, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass on Leon''s decisions, the 1-nat convention of the coefficient stated in the formal level (restatement)'
  version: 5
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  proof: proof-main.tex
  uses:
  - scrambling.mode-count@3
  - singularity.causal-epoch-computed-exactly@4
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - label:prop:arealaw
- kind: check
  ref: check.py::check_area_law_iff_half_mass
- kind: check
  ref: check.py::check_causal_epoch_order_m
- kind: check
  ref: check.py::check_lifetime_scaling
locators:
  paper: T08
  number: Prop 3.5
  label: prop:arealaw
  line: 648
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Formal correction (DECISIONS A15, R08; restatement): ''reproduces the Bekenstein-Hawking entropy, coefficient included'' holds in the 1-nat convention only; scrambling.residue-each-convention (iii) says that convention over-credits each mode, and with ln 2 per mode the condition is nu Delta t = M/(2 ln 2) (singularity.area-law-test). The formal now says so, as its one-liner already did. The equivalence N = 4 pi M^2 iff nu Delta t = M/2 is unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: N = 8 pi M nu Delta t equals S_BH exactly at nu Delta t = M/2; causal epoch of order M up to a logarithm with exact ln 2 bounds; lifetime exponents 4 and 5. Version 2 -> 3. Check strengthened: constant margin 2 ln(1/eps) - Delta t/M = 16/3 - 4 ln 2 pinned exactly and asserted positive; samples and bracket widths moved to module level. Version 3 -> 4.'
  env: proposition
  context_refs:
  - singularity.causal-epoch-computed-exactly
  typing:
    by: ai-typing-pass
    added:
    - scrambling.mode-count
    - singularity.causal-epoch-computed-exactly
    note: Added the causal-epoch Fact (context ref, quoted in the statement) and the mode-count theorem
      whose formula $N = 8\pi\nu M\Delta t$ the equivalence is about; the Christodoulou-Rovelli comparison
      is context only, and the Bekenstein-Hawking match is the claim itself rather than a standard route
      to it.
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - scrambling.mode-count
    - singularity.causal-epoch-computed-exactly
---

## formal
$N = \SBH = 4\pi M^2$ if and only if $\nu\,\Delta t = M/2$: the count reproduces the Bekenstein-Hawking entropy, coefficient included, precisely when the counted epoch is of order one Schwarzschild time (in the 1-nat convention; with each mode credited its $\ln 2$ the condition is $\nu\,\Delta t = M/(2\ln 2)$, Proposition \claimref{singularity.area-law-test}). The scale has an independent causal meaning: the span of singularity in the causal future of a single horizon-crossing epoch is $\Delta t(\varepsilon) = 2M\bigl(\ln(1/\varepsilon) - \tfrac83 + 2\ln 2\bigr) + O(\varepsilon)$, of order $M$ up to a logarithm (Fact \claimref{singularity.causal-epoch-computed-exactly}). Counting instead over the hole's whole lifetime, $\Delta t \sim M^3$, gives $N \sim M^4$: the count then shares with the interior-volume growth of \cite{ChristodoulouRovelli2015} the linearity in time and the unresolved tension with the constancy of the horizon entropy, though not the growth law (their $dV/dv \propto M^2$ gives $V \sim M^5$ over the lifetime). The framework does not resolve that tension; it reproduces it from an independent starting point, which is evidence the count tracks real structure; the confrontation is recorded.

## technical
With the mode count $N = 8\pi\nu M\,\Delta t$ (Planck units), the count equals the Bekenstein-Hawking entropy $\SBH = 4\pi M^2$ exactly when $\nu\,\Delta t = M/2$. This is the 1-nat convention, one nat per mode; in the singularity paper's capacity convention, $\ln 2$ per fermionic mode, the capacity $N\ln 2$ equals $\SBH$ exactly when $\nu\,\Delta t = M/(2\ln 2)$ (\claimref{singularity.area-law-test}). Either way the epoch must be of order one Schwarzschild time. That scale has an independent causal meaning: the span of singularity in the causal future of one horizon-crossing epoch is $\Delta t(\varepsilon) = 2M\bigl(\ln(1/\varepsilon) - \tfrac83 + 2\ln 2\bigr) + O(\varepsilon)$, of order $M$ up to a logarithm.

Counting over the whole lifetime, $\Delta t \sim M^3$, gives $N \sim M^4$. The count then shares with the Christodoulou-Rovelli interior-volume growth its linearity in time and its tension with the constant horizon entropy, though not the growth law; the tension is recorded, not resolved.

## lay
The framework counts quantum modes that accumulate at a black hole's inner surface over some span of time. The count matches the Bekenstein-Hawking entropy, numerical factor included, only if that span is about one natural time unit of the hole, which is also the span causality singles out. Counting over the hole's whole lifetime instead gives far too much, a puzzle shared with other interior-volume pictures and not resolved here.

## one-liner
The mode count equals $\SBH = 4\pi M^2$ if and only if $\nu\,\Delta t = M/2$ (in the 1-nat convention; $M/(2\ln 2)$ when each mode is credited its $\ln 2$), an epoch of order one Schwarzschild time.
