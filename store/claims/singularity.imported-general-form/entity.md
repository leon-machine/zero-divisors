---
id: singularity.imported-general-form
kind: claim
version: 1
title: 'Imported: the general form'
status: imported
region: singularity
subject: descent
tags: [classical-theorem, modular-theory]
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
imported_from:
- citation: 'O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2: Equilibrium
    States. Models in Quantum Statistical Mechanics, 2nd ed., Springer (1997).'
  key: BR2
  locator: Thm.~5.3.30
- citation: R. Haag, N. M. Hugenholtz and M. Winnink, On the equilibrium states in quantum statistical
    mechanics, Commun. Math. Phys. 5 (1967), 215--236.
  key: HHW1967
- citation: A. Connes, Une classification des facteurs de type III, Ann. Sci. 'Ec. Norm. Sup'er. (4) 6
    (1973), 133--252.
  key: Connes1973
  locator: Thm.~1.2.1
locators:
  paper: T05
  number: Fact 7.14
  label: fact:kmsgeneral
  line: 1818
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: external import; no edges to review
---

## formal
For a $C^{*}$-dynamical system the $(\alpha,\beta)$-KMS states at fixed $\beta$ form a weak$^{*}$-compact convex simplex whose extreme points are exactly those whose GNS von Neumann algebra is a factor, distinct extremal KMS states being disjoint; a factor state is therefore extremal, and uniqueness at fixed $\beta$ is the statement that the simplex is a point. \emph{Provenance:} Bratteli and Robinson \cite[Thm.~5.3.30]{BR2}, the KMS condition itself being \cite{HHW1967}. The companion statement that two faithful normal states with the same modular automorphism group differ by an element affiliated to the centre, hence coincide on a factor, is Connes' Radon-Nikodym cocycle theorem \cite[Thm.~1.2.1]{Connes1973}.

## technical
For a $C^{*}$-dynamical system the $(\alpha,\beta)$-KMS states at fixed $\beta$ form a weak$^{*}$-compact convex simplex. Its extreme points are exactly the KMS states whose GNS von Neumann algebra is a factor, and distinct extremal KMS states are disjoint; so a factor state is extremal, and uniqueness of the KMS state at fixed $\beta$ is the statement that the simplex is a single point.

The companion statement is Connes' Radon-Nikodym cocycle theorem: two faithful normal states with the same modular automorphism group differ by an element affiliated to the centre, and hence coincide on a factor.

## lay
The equilibrium states of a quantum system at a given temperature form a convex set, and its corners are the states that cannot be split into simpler equilibria. These corners are exactly the states whose associated algebra has a trivial centre. A related theorem says that on such an algebra a faithful state is determined by its intrinsic time evolution.

## one-liner
Imported: the KMS states at fixed $\beta$ form a simplex whose extreme points are the factor states, and on a factor two faithful normal states with the same modular group coincide.
