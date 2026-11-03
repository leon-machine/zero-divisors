---
id: std-algebra.polarisation
kind: claim
version: 1
title: Polarisation
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- classical-theorem
proposed_by:
  kind: ai
  session: algebra-core-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: typed
trust: ai-proposed
about:
- obj.std-algebra.quadratic-space
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_polarisation
locators:
  sources:
  - key: Lam2005
    locator: Ch. I and II (quadratic forms; the real case)
extraction:
  by: algebra-core-2026-10-26
---

## formal
Let $(V, Q)$ be a real quadratic space with polar form $B$. Then $B$ is symmetric and $B(v, v) = Q(v)$ for all $v \in V$. Conversely, for every symmetric bilinear form $B'$ on $V$, the map $v \mapsto B'(v, v)$ is a quadratic form with polar form $B'$. Quadratic forms and symmetric bilinear forms on $V$ therefore determine each other. In a basis $e_1, \dots, e_n$ with Gram matrix $G_{ij} = B(e_i, e_j)$, $Q(\textstyle\sum_i x_i e_i) = \sum_{i,j} G_{ij} x_i x_j$.

## technical
The polar form $B$ of a quadratic form $Q$ is symmetric, and it returns $Q$ on the diagonal: $B(v, v) = Q(v)$. Conversely any symmetric bilinear form $B'$ defines a quadratic form $v \mapsto B'(v, v)$ whose polar form is $B'$ again. So a quadratic form and a symmetric bilinear form carry the same information, and in coordinates the form is $Q(x) = x^{\mathsf T} G x$ with $G$ the Gram matrix.

## lay
Knowing the square length of every arrow is the same as knowing the "dot product" of every pair of arrows. Each can be recovered from the other by a short formula.

## one-liner
The polar form is symmetric with $B(v,v) = Q(v)$, every symmetric bilinear form arises this way, and in a basis $Q(x) = x^{\mathsf T} G x$.
