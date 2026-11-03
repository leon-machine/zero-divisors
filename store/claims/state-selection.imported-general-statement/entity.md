---
id: state-selection.imported-general-statement
kind: claim
version: 2
title: 'Imported: the general statement'
status: imported
region: state-selection
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
  source: 'authorship disclosure of T05-state-selection, the series'' standard disclaimer'
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
  paper: T05-state-selection
  number: Fact 4.3
  label: fact:kmsgeneral
  line: 231
extraction:
  typing:
    by: ai-typing-pass
    note: 'Imported fact; levels only, explaining the cited Bratteli-Robinson and Connes results. Linked
      equivalent_to singularity.imported-general-form: the companion note restates it.'
  env: fact
equivalent_to:
- singularity.imported-general-form@1
---

## formal
For a $C^{*}$-dynamical system the $(\alpha,\beta)$-KMS states at fixed $\beta$ form a weak$^{*}$-compact convex simplex whose extreme points are exactly those whose GNS von Neumann algebra is a factor, distinct extremal KMS states being disjoint; in particular a factor state is extremal, and uniqueness of the $\beta$-KMS state is the statement that the simplex is a point. \emph{Provenance:} Bratteli and Robinson \cite[Thm.~5.3.30]{BR2}; the KMS condition itself is Haag, Hugenholtz and Winnink \cite{HHW1967}. The companion statement that two faithful normal states have the same modular automorphism group only if they differ by an element affiliated to the centre is Connes' Radon-Nikodym cocycle theorem \cite[Thm.~1.2.1]{Connes1973}, which for a factor forces the two states to be equal.

## technical
For a $C^{*}$-dynamical system, the $(\alpha, \beta)$-KMS states at fixed $\beta$ form a weak$^{*}$-compact convex simplex whose extreme points are exactly the states whose GNS von Neumann algebra is a factor; distinct extremal KMS states are disjoint, a factor state is extremal, and uniqueness of the $\beta$-KMS state is the statement that the simplex is a single point. This is Bratteli and Robinson's theorem, with the KMS condition itself due to Haag, Hugenholtz and Winnink.

The companion result is Connes' Radon-Nikodym cocycle theorem: two faithful normal states with the same modular automorphism group differ by an element affiliated to the centre, which on a factor forces them to be equal.

## lay
This is a standard result from the mathematics of quantum statistical mechanics. At a fixed temperature the possible equilibrium states form a well-behaved convex set, and its extreme points, the pure thermodynamic phases, are exactly the states whose algebra has trivial centre. A related theorem of Connes says that on such an algebra a faithful state is determined by its own modular time evolution.

## one-liner
At fixed $\beta$ the KMS states form a simplex whose extreme points are the factor states, and on a factor a faithful normal state is determined by its modular automorphism group.
