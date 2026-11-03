---
id: sheaf.imported-real-line-bundles
kind: claim
version: 1
title: 'Imported: real line bundles and $w_1$'
status: imported
region: sheaf
subject: walls
tags: [classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
imported_from:
- citation: J. W. Milnor and J. D. Stasheff, Characteristic Classes, Annals of Mathematics Studies 76,
    Princeton University Press (1974).
  key: MilnorStasheff1974
  locator: \S 4
locators:
  paper: T04
  number: Fact 2.10
  label: fact:linebundles
  line: 461
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: 'Imported classical fact with no derivation; only the levels were written. Levels pass: conditions
      already kept.'
---

## formal
A real line bundle is trivial exactly when its first Stiefel-Whitney class vanishes; $w_1$ is additive under tensor product of line bundles, so the square of any real line bundle has $w_1 = 0$; and a hypersurface is two-sided exactly when its normal bundle is trivial. \emph{Provenance:} classical bundle theory, \cite[\S 4]{MilnorStasheff1974}.

## technical
A classical fact from bundle theory: a real line bundle is trivial exactly when its first Stiefel-Whitney class $w_1$ vanishes; $w_1$ is additive under tensor product of line bundles, so $w_1(\ell \otimes \ell) = 2w_1(\ell) = 0$ for every real line bundle $\ell$; and a hypersurface is two-sided exactly when its normal bundle is trivial. It is imported from the standard treatment of characteristic classes by Milnor and Stasheff.

## lay
A line bundle attaches a line to every point of a space, and it may twist like a M\"obius band. A single invariant, the first Stiefel-Whitney class, detects whether it twists. Two twists cancel, so the square of any line bundle is untwisted, and a surface inside a space has two distinct sides exactly when its normal lines do not twist.

## one-liner
A real line bundle is trivial exactly when $w_1 = 0$, $w_1$ is additive so the square of any line bundle is trivial, and a hypersurface is two-sided exactly when its normal bundle is trivial.
