---
id: synthesis.imported-line-bundles-classified-and-cellular-approximation
kind: claim
version: 1
title: 'Imported: real line bundles are pulled back from the tautological bundle of RP^infinity, and by cellular approximation every real line bundle over a d-dimensional CW complex is a subbundle of the trivial bundle of rank d+1 (Milnor and Stasheff, Section 5; cellular approximation)'
status: imported
region: synthesis
subject: walls
tags: [obstruction-types, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'J. W. Milnor and J. D. Stasheff, Characteristic Classes, Annals of Mathematics Studies 76, Princeton University Press (1974).'
  key: MilnorStasheff1974
  locator: '\S 5'
- citation: 'A. Hatcher, Algebraic Topology, Cambridge University Press (2002).'
  key: Hatcher2002
  locator: 'Theorem 4.8'
extraction:
  note: >-
    Imported so that synthesis.wall-rung-count-is-height-of-dying-line-class can cite the
    classifying-map and cellular-approximation step behind its upper bound e(L) <= dim Sigma + 1, which
    its proof cites from memory. Topological: a statement about bundles over the wall's cross-section.
    Cited from memory, not checked against the sources (the statements are textbook; the section and
    theorem numbers are as remembered).
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Created by the maintainer pass (fix round of 26 October: cellular approximation and the classification of line bundles, cited from memory by the wall rung-count result, to be imported as a Fact).'
---

## formal
(i) \emph{(Classification.)} Every real line bundle $L$ over a paracompact space $X$ is isomorphic to $f^{*}\gamma$ for a map $f : X \to \mathbb{RP}^{\infty}$, $\gamma$ the tautological line bundle, unique up to homotopy, and $w_{1}(L) = f^{*}w_{1}(\gamma)$. (ii) \emph{(Cellular approximation.)} Every map between CW complexes is homotopic to a cellular map, one sending the $d$-skeleton into the $d$-skeleton. (iii) \emph{(Consequence.)} If $X$ is a CW complex of dimension $d$, $f$ may be taken with image in $\mathbb{RP}^{d}$, so $L \cong f^{*}\gamma_{d}$ with $\gamma_{d} \subset \mathbb{RP}^{d} \times \R^{d+1}$, and $L$ is a subbundle of the trivial bundle $X \times \R^{d+1}$. Topological statements, flagged as such. \emph{Provenance:} \cite[\S 5]{MilnorStasheff1974} (classifying spaces); \cite[Theorem 4.8]{Hatcher2002} (cellular approximation).

## technical
Line bundles over a space are classified by maps into infinite real projective space, the space of all lines. A map from a $d$-dimensional complex can always be deformed to land in the $d$-dimensional projective space, whose lines sit in a fixed $(d+1)$-dimensional space. So every line bundle over a $d$-dimensional base sits inside a trivial bundle of rank $d+1$. The series uses this as the upper bound on the number of rungs a wall needs.

## lay
Any twisting family of lines over a space can be fitted inside an untwisted family of slightly larger spaces, one dimension more than the space itself. This is the classical fact behind an upper limit the series puts on how much structure a degenerating wall needs.

## one-liner
Real line bundles are $f^{*}\gamma$ for $f : X \to \mathbb{RP}^{\infty}$, and by cellular approximation over a $d$-dimensional complex every real line bundle lies in the trivial bundle of rank $d+1$ (Milnor and Stasheff, Section 5; Hatcher, Theorem 4.8).
