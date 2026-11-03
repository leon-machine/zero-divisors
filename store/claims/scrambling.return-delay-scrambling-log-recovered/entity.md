---
id: scrambling.return-delay-scrambling-log-recovered
kind: claim
version: 2
title: 'The return delay: the scrambling log recovered'
status: proved
region: scrambling
subject: entropy
tags: [recovers-known-physics, boundary-modes]
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
  proof: proof-main.tex
  uses:
  - scrambling.epoch-modular-period-two-unknowns-become@5
  - scrambling.spreading-law-chaos-bound-saturated@5
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_round_duration_is_4m
- kind: check
  ref: check.py::check_epidemic_doubling_count
locators:
  paper: T08
  number: Asm 6.2
  label: asm:delay
  line: 921
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: beta = 2 pi/kappa = 8 pi M and beta/(2 pi) = 4M exactly in Q[pi], and the epidemic doubling count ceil(log2 N) giving T_return = 4M log2 S. Version 1 -> 2.'
  env: assembly
  context_refs:
  - scrambling.epoch-modular-period-two-unknowns-become
  - scrambling.spreading-law-chaos-bound-saturated
  flags:
  - no proof environment found
  typing:
    by: ai-typing-pass
    added:
    - scrambling.epoch-modular-period-two-unknowns-become
    - scrambling.spreading-law-chaos-bound-saturated
    note: 'Assembly with no proof environment: given the source''s ''follows from'' proof with the epoch
      theorem (dwell floor) and the spreading assembly (causal rate) as premises; the source says it recovers
      the Hayden-Preskill and Sekino-Susskind fast-scrambling time, but no imported fast-scrambling claim
      is in the store, so no standard route was added. Levels pass: the lay level now keeps the rate-model
      scope and the (IC) condition on the dwell floor, and the one-liner adds (IC).'
---

## formal
In the rate model, deposited information cannot return before the dwell time of the window (the epoch of Section \ref{sec:epoch}, the correct power of $M$); and charging the window-internal re-encoding at the framework's causal rate (one pairwise operation per boost e-fold $\kappa^{-1}$ per mode, spreading epidemically over the $N \sim S$ modes) requires of order $\ln S$ rounds of duration $\beta/2\pi$, giving a return delay
\[
T_{\mathrm{return}} \;\approx\; \frac{\beta}{2\pi}\,\ln S \;=\; 4M\,\ln S :
\]
the fast-scrambling time \cite{HaydenPreskill2007, SekinoSusskind2008}, recovered from the framework's own clock. This removes the instant-return artefact of T5's rate model; the first-principles account of the spreading exponent is Assembly \claimref{scrambling.spreading-law-chaos-bound-saturated}, and genuine chaotic dynamics beyond it remains open.

\smallskip
\noindent\emph{The derivation, step by step.} The dwell floor is the epoch (Theorem \claimref{scrambling.epoch-modular-period-two-unknowns-become}, conditional on (IC)); the epidemic count is the standard doubling estimate, $\log_2 S$ rounds to reach $S$ modes from one, each round one causal step of the window's clock, the $\ln 2$ absorbed into the displayed approximation; the clock and its rate are the theorems cited. The coefficient $4M$ is exact arithmetic from $\beta = 8\pi M$, script-checked.

## technical
In the rate model, information deposited in the window cannot return before the window's dwell time, which is the epoch. Charging the window's internal re-encoding at the framework's causal rate, one pairwise operation per boost e-fold $\kappa^{-1}$ per mode, spreading epidemically over the $N \sim S$ modes, takes of order $\ln S$ rounds of duration $\beta/2\pi$.

The return delay is therefore $T_{\mathrm{return}} \approx (\beta/2\pi)\ln S = 4M\ln S$, the fast-scrambling time, recovered from the framework's own clock. This removes the instant-return artefact of the earlier rate model; the dwell floor is conditional on the intrinsic-clock premise, and genuine chaotic dynamics beyond the model remains open.

## lay
Within the paper's rate model, information that falls into a black hole cannot begin to come back out before a minimum dwell time, a floor that is conditional on the intrinsic-clock premise (IC). Using the framework's own internal clock, the delay comes out approximately as the known fast-scrambling time, which grows only with the logarithm of the black hole's entropy. This removes an unphysical feature of an earlier simplified model, in which information came back instantly; genuinely chaotic dynamics beyond the model remains open.

## one-liner
In the rate model, with the dwell floor conditional on (IC), the return delay is $T_{\mathrm{return}} \approx (\beta/2\pi)\ln S = 4M\ln S$, the fast-scrambling time.
