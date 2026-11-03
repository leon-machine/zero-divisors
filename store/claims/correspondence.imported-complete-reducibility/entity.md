---
id: correspondence.imported-complete-reducibility
kind: claim
version: 1
title: 'Imported: complete reducibility'
status: imported
region: correspondence
subject: conformal-spacetime
tags: [classical-theorem, representation-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
imported_from:
- citation: J. E. Humphreys, Introduction to Lie Algebras and Representation Theory, Graduate Texts in
    Mathematics 9, Springer (1972).
  key: Humphreys72
  locator: \S6.3, \S7
locators:
  paper: T09
  number: Fact 6.9
  label: fact:reducibility
  line: 840
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: Imported textbook result; levels only.
---

## formal
Every finite-dimensional representation of $\mathfrak{sl}(2,\C)$ is a direct sum of irreducible representations, and the decomposition of a representation into isotypic components (the sum of all subrepresentations isomorphic to a given irreducible) is canonical. \emph{Provenance:} Weyl's complete reducibility theorem, e.g.\ \cite[\S6.3, \S7]{Humphreys72}.

## technical
Weyl's complete reducibility theorem for $\mathfrak{sl}(2,\C)$: every finite-dimensional representation $U$ is a direct sum of irreducible representations. Its isotypic components, each the sum of all subrepresentations isomorphic to a given irreducible, are canonical, so the decomposition $U = \bigoplus_\lambda U_\lambda$ into isotypic parts does not depend on any choices.

## lay
A standard theorem about symmetries says that any finite-dimensional representation of the basic symmetry algebra $\mathfrak{sl}(2,\C)$ breaks apart cleanly into irreducible building blocks. Grouping together the blocks of the same type gives a decomposition that does not depend on any choices. The result is imported from the textbook literature.

## one-liner
Every finite-dimensional representation of $\mathfrak{sl}(2,\C)$ is a direct sum of irreducibles, and its decomposition into isotypic components is canonical.
