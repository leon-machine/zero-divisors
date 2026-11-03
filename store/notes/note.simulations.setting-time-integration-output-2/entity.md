---
id: note.simulations.setting-time-integration-output-2
kind: note
version: 1
title: Time integration and output
status: setting
subject: dark-matter
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14b, deposited version
comments_on:
- simulations.merger
locators:
  paper: T14b
  number: Setting
  section: The simulation code
  line: 339
  subsection: Time integration and output
---

## formal
\textbf{Tests.} Two tests (\file{tpsim\_tests.py}, output deposited) check the sheet fluid and the code's stability. A uniform sphere of hot sheet fluid ($2000$ particles) with every normal along $z$ grows in rms extent by factors $1.49$ and $1.47$ in $x$ and $y$ over $0.1$ time units and stays at $1.00$ in $z$; with random normals it grows by $1.33$ to $1.35$ along all three axes. An isolated main-cluster halo with the unit-ball composition as written ($20{,}000$ particles, every species) keeps its $10$ and $50$ percent mass radii within $1.3$ percent over $1$ time unit ($0.98$ Gyr).

## technical
pending

## lay
pending

## one-liner
pending
