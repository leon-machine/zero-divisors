---
id: obj.scrambling.stretched-singularity
kind: object
version: 2
title: Stretched singularity
status: defined
region: scrambling
subject: entropy
tags: [schwarzschild, entropy-premises]
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
review: draft
locators:
  paper: T08
  number: Def 3.1
  label: def:stretched
  line: 608
extraction:
  env: definition
  open_problem: op.boundary-mode-provenance
  correction:
    by: colony-2026-10-22
    version: 2
    note: >-
      Version 1 cited the Witt-index capacity Fact for the clause that the boundary-mode pairs lie on
      this slice. That Fact counts mode pairs per rung of the tower and places nothing; the placement
      is the singularity paper's Postulate (C1), now cited, and the density per cell is (C2). The
      definition itself (the slice r = r_c) is unchanged.
  context_refs:
  - singularity.c1-curvature-cutoff
  - singularity.c2-cell-density
  typing:
    by: ai-typing-pass
    note: Definition with no edges; the cited capacity Fact is a claim, so it cannot be an about target,
      and objects carry no derivations.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - scrambling.exact-factorisation-thinning
    - scrambling.exactness-excludes-cutoff-dependence
    - scrambling.per-slice-verification-two-failed-aggregations
    - scrambling.slice-volume-exactly-per-unit-killing
    - scrambling.uniqueness-internal-scaling
    added_about: []
    verdict: connected
    note: 'A definition cannot carry uses or assumes; the added links are about edges from the claims whose
      statements use the defined notion. Here: the T08 results computed on the slice r = r_c; the T05 axioms
      and count with the same cutoff are left alone, being earlier than the T08 definition.'
---

## formal
The \emph{stretched singularity} is the interior slice $r = r_c$ defined by the curvature-eigenvalue cutoff $2M/r^3 = 1$ in Planck units: $r_c = (2M)^{1/3}$. It is the working substitute for the exceptional boundary of the completion: the locus where the classical description is replaced by the completed one, on which, by Postulate (C1) of the singularity paper (\claimref{singularity.c1-curvature-cutoff}), the boundary-mode pairs lie, with $\nu$ fermionic modes (ladder pairs) per Planck cell by Postulate (C2), $\nu$ left free there (\claimref{singularity.c2-cell-density}). The definition places no modes; results that count modes on the slice hold under (C1) and (C2).

## technical
Inside a Schwarzschild black hole of mass $M$ (Planck units) the curvature operator has largest eigenvalue $2M/r^3$. The stretched singularity is the interior slice $r = r_c$ on which that eigenvalue reaches the Planck value, $2M/r_c^3 = 1$, so $r_c = (2M)^{1/3}$.

It is the working substitute for the exceptional boundary of the completion: the locus where the classical description is replaced by the completed one, and, under the singularity paper's placement postulates (C1) and (C2), the surface on which the boundary-mode pairs lie.

## lay
Deep inside a black hole the curvature of space-time grows without limit towards the centre. The stretched singularity is the surface where that curvature first reaches the Planck scale. The framework treats this surface as the place where ordinary geometry gives way to its completed description, and, by a stated assumption of the singularity paper, it is where the black hole's boundary modes sit.

## one-liner
The stretched singularity is the interior slice $r_c = (2M)^{1/3}$ on which the curvature eigenvalue $2M/r^3$ reaches the Planck value.
