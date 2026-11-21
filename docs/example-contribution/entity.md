---
id: example.null-vector-zero-divisor
kind: claim
version: 1
title: A nonzero null vector is a zero divisor
status: proved
subject: zero-divisors
proposed_by:
  kind: ai
  author: A. Researcher, with Claude
ai_involved: 'yes'
credit:
- name: A. Researcher
  role: idea and direction
  orcid: 0000-0002-1825-0097
- name: Claude Opus 5.5
  role: proof and drafting
derivations:
- name: main
  uses:
  - std-algebra.vector-squares@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_null_vectors_square_to_zero
---

## formal
In $\Cl(p,q)$ with $p, q \geq 1$, every nonzero vector $v$ with $Q(v) = 0$ satisfies $v v = 0$, so $v$ is a two-sided zero divisor.

## technical
A null vector squares to its quadratic form, which is zero, so a nonzero null vector multiplied by itself gives zero: it is a zero divisor on both sides.

## lay
In an algebra with both kinds of direction, some nonzero directions multiply by themselves to give exactly zero.

## one-liner
A nonzero null vector squares to zero, so it is a zero divisor.
