---
id: scrambling.no-recount-reaches-quarter
kind: claim
version: 4
title: No recount reaches the quarter
status: proved
region: scrambling
subject: entropy
tags: [no-go, mode-counting]
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
derivations:
- name: main
  uses:
  - scrambling.candidate-principles-their-yields@2
  - scrambling.residue-each-convention@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T08.py
  tags:
  - num:4.13
- kind: check
  ref: check.py::check_residue_closure
- kind: check
  ref: check.py::check_targets
- kind: check
  ref: check.py::check_natural_rules
locators:
  paper: T08
  number: Prop 4.13
  label: prop:norecount
  line: 830
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: closure of residues q pi^k over 1440 counting rules, capacity target never reached formally, 1-nat target reached, natural rules 4 pi and 1. Version 2 -> 3. Redundant inequality (yields != 1/4) removed: implied by the exact equalities 4 pi and 1 in the same function; no change to what is tested. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - scrambling.residue-each-convention
    note: 'Kept the yields proposition and added the residue proposition, which defines the residue and
      both targets the statement compares against; the transcendence of ln 2 is a literature import not
      in the store; the remaining E204 traces to the collar-coframe Fact outside this list. Levels pass:
      conditions already kept; the lay level''s "physically meaningful convention", an evaluation the
      formal does not make, now names the capacity convention.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - scrambling.residue-each-convention
---

## formal
Let a counting rule assign to the exceptional set a tally that is a rational number of modes per cell, with cells whose areas are rational multiples of integer powers of $\pi$ in Planck units, over a rational number of ticks per modular period. Then its residue $\kappa_c$ is a rational multiple of an integer power of $\pi$, $\kappa_c = q\pi^k$ with $q \in \mathbb{Q}$ and $k \in \mathbb{Z}$. In the capacity convention the target is $\kappa_c = 1/(4\ln 2)$; equality would require $\pi^k\ln 2 \in \mathbb{Q}$, which is false for $k = 0$, $\ln 2$ being transcendental \cite[Thm.~1.4]{Baker1975}, so no rule with $k = 0$ reaches the target; for $k \neq 0$ it would contradict the expected algebraic independence of $\pi$ and $\ln 2$, which is not a theorem, so the exclusion of rules with $k \neq 0$ is conditional on that independence. In the 1-nat convention the target $\kappa_c = \tfrac14$ is rational, and the natural rules of Proposition \claimref{scrambling.candidate-principles-their-yields} return $\kappa_c = 4\pi$ (P1), $\kappa_c = 1$ (P3) and a broken scaling (P2), none of them $\tfrac14$.

## technical
Consider counting rules with a rational number of modes per cell, on cells whose areas are rational multiples of integer powers of $\pi$ in Planck units, over a rational number of ticks per modular period. Their residue is $\kappa_c = q\pi^k$ with $q \in \mathbb{Q}$ and $k \in \mathbb{Z}$. In the capacity convention the target $\kappa_c = 1/(4\ln 2)$ would need $\pi^k\ln 2 \in \mathbb{Q}$: false for $k = 0$, since $\ln 2$ is transcendental, and excluded for $k \neq 0$ only conditionally on the expected algebraic independence of $\pi$ and $\ln 2$.

In the 1-nat convention the target $\kappa_c = \tfrac14$ is rational, but the natural rules give $\kappa_c = 4\pi$, $\kappa_c = 1$ and a broken scaling, none of them $\tfrac14$.

## lay
One might hope to reach the black hole entropy simply by recounting the interior modes more cleverly. Any recount built from whole-number ratios and powers of $\pi$ cannot hit the required value in the capacity convention, where the target involves $\ln 2$: for one class of rules this is proved outright, and for the rest it assumes a widely expected but unproved fact about $\pi$ and $\ln 2$. In the other convention the natural recounts simply miss.

## one-liner
A rational recount with residue $q\pi^k$ cannot reach $1/(4\ln 2)$ when $k = 0$, nor when $k \neq 0$ if $\pi$ and $\ln 2$ are algebraically independent, and the natural rules miss the 1-nat target $\tfrac14$.
