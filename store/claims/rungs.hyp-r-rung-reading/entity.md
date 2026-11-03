---
id: rungs.hyp-r-rung-reading
kind: claim
version: 2
title: 'Hypothesis (R): the rung reading'
status: postulate
region: rungs
subject: standard-model
tags: [hypotheses-s-r-c, ladder-pairs, spinor-modules]
proposed_by:
  kind: human
  author: leon (stated in the paper); entered by the build
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-rungs, the series'' standard disclaimer'
review: typed
locators:
  paper: T12-rungs
  number: Hypothesis (R)
  label: ''
  line: 280
extraction:
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the n-twistor composite to a composite of n conformal spinors at every level; the tower, its rungs and the spinor module are unchanged.'
  source_title: |-
    Hypothesis (R): the rung reading
  source_formal: |-
    \emph{Hypothesis (R), the rung reading.} The internal state space of an $n$-twistor composite is the spinor module of the $n$-th rung of the tower above $\Cl(2,4)$, $\Lambda^{\bullet}(W \oplus R_{n})$, on which the transported algebra acts as in Fact \claimref{rungs.imported-tower-one-qubit-per-rung}: each twistor of the composite occupies one new rung, and the constituents are the states with one rung occupied.
  env: hypothesis
  typing:
    by: ai-typing-pass
    note: Stated in a quote block as the note's hypothesis; formal text is the quote verbatim with the
      Fact reference written as a claimref.
---

## formal
\emph{Hypothesis (R), the rung reading.} The internal state space of a composite of $n$ conformal spinors (an $n$-twistor composite) is the spinor module of the $n$-th rung of the tower above $\Cl(2,4)$, $\Lambda^{\bullet}(W \oplus R_{n})$, on which the transported algebra acts as in Fact \claimref{rungs.imported-tower-one-qubit-per-rung}: each conformal spinor of the composite occupies one new rung, and the constituents are the states with one rung occupied.

## technical
Hypothesis (R) reads the internal state space of a composite of $n$ conformal spinors as the spinor module $\Lambda^{\bullet}(W \oplus R_{n})$ of the $n$-th rung of the tower above $\Cl(2,4)$, with the transported algebra acting as it does on the tower. Each conformal spinor of the composite occupies one new rung, and the constituents are the states with one rung occupied.

It is a structural premise phrased in the language of the tower rather than of the composite's slots, and is taken as given by the results stated under it.

## lay
This is an assumption, not a result: a composite of several basic spinor states is described by climbing the series' tower of algebras, one rung for each of them. Its states are then those of a standard quantum system with one extra mode per rung. The results stated under it hold only if it does.

## one-liner
Premise (R): the internal state space of a composite of $n$ conformal spinors is the spinor module of the tower's $n$-th rung, each spinor occupying one new rung.
