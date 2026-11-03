---
id: singularity.c3-counted-epoch
kind: claim
version: 1
title: 'C3: counted epoch'
status: postulate
region: singularity
subject: entropy
tags: [entropy-premises, schwarzschild]
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
locators:
  paper: T05
  number: Axiom 10.3
  label: ax:epoch
  line: 2141
extraction:
  env: axiom
  context_refs:
  - singularity.causal-epoch-computed-exactly
  typing:
    by: ai-typing-pass
    note: Postulate; no edges (the causal-epoch lemma it cites is picked up by the claims that assume
      it).
---

## formal
The span of Killing time counted at any one moment of the exterior hole is the causal epoch: the portion of the singularity in the causal future of a single horizon-crossing, of order one Schwarzschild time by Lemma \claimref{singularity.causal-epoch-computed-exactly}.

## technical
Postulate: the span of Killing time counted at any one moment of the exterior hole is the causal epoch, the portion of the singularity in the causal future of a single horizon crossing.

By the exact causal-epoch computation this span is of order one Schwarzschild time, $\Delta t \propto M$ up to a logarithm of the horizon regulator.

## lay
The count of modes near the singularity depends on how much of the singularity is counted at once. This assumption says to count only the part that a single crossing of the horizon can causally reach. That stretch of time is about one natural time unit of the black hole.

## one-liner
Postulate: the Killing-time span counted at one moment is the causal epoch of a single horizon crossing, of order one Schwarzschild time.
