---
id: note.dark-matter.r1-against-series-mass-formulas
kind: note
version: 2
title: R1 against the series' mass formulas
status: remark
subject: dark-matter
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
- name: Claude Opus 5.5
  role: 'GA rewrite (declared: a remark computed with explicit gamma matrices)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
comments_on:
- dark-matter.r3-one-cell-per-unshared-direction
locators:
  paper: T14
  number: Rem 7.5
  label: rem:massR1
  line: 796
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Not rewritten: the remark compares mass normalisations by an explicit computation with Hermitian gamma matrices of signature (1, n - 1), n = 3, 4, 5, built as matrices by the script (the current psi^dag gamma^0 gamma^mu psi and its bound); a GA form (the vector part of psi e_t psi~, as reader R05 notes) would change the class of the computation, not only its notation. Declared outside_ga (bridge).'
outside_ga:
  kind: bridge
  why: 'the remark compares mass normalisations by an explicit computation with Hermitian gamma matrices of signature (1, n - 1), n = 3, 4, 5, built as matrices by the script; the current psi^dag gamma^0 gamma^mu psi is the standard formalism''s, set beside the series'' mass formulas'
---

## formal
The odd-dimensional mass formulas can be written in a Pfaffian form or in the determinant form of this world's two-constituent formula \cite[Prop.~4.1]{ButlerT11}, and the two are normalised differently; compared across normalisations they make five-dimensional quanta appear at most half as heavy as ours, which would break R1 before it starts. In one normalisation the comparison is even. Let the tower have signature $(1, n-1)$, $n = 3, 4, 5$, with $\gamma^{0}$ Hermitian, $(\gamma^{0})^{2} = 1$, each spatial $\gamma^{k}$ anti-Hermitian, and define $j^{\mu} = \psi^{\dagger}\gamma^{0}\gamma^{\mu}\psi$ and $m^{2} = j_{\mu}j^{\mu}$. Then
\[
m^{2} \;=\; (\psi^{\dagger}\psi)^{2} - \sum_{k}(j^{k})^{2} \;\le\; (\psi^{\dagger}\psi)^{2},
\]
with equality exactly on the eigenvectors of $\gamma^{0}$, where every spatial current vanishes because $\gamma^{k}$ anticommutes with $\gamma^{0}$ and so maps each eigenspace to the other. So the heaviest quantum of unit norm has $m = 1$ in three, four and five dimensions alike (script: the three sets of matrices built exactly, the relations, the bound and its attainment in Gaussian-rational arithmetic). The five-dimensional spinor space is the four-dimensional Dirac space and the first four components of its current are the four-dimensional current, so one five-dimensional constituent is the same object as a four-dimensional Weyl pair, which is why mass begins at one in five dimensions and at two in four: the counts differ, the object does not. This compares the scale of the formulas, not actual masses, which each tower's dynamics sets and the series does not derive. R1 is not in conflict with the series; it is not derived.

## technical
pending

## lay
pending

## one-liner
pending
