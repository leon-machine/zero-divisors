---
id: sheaf.imported-classification-values
kind: claim
version: 5
title: 'Imported: classification values'
status: proved
region: sheaf
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
- name: Claude Opus 5.5
  role: 'consistency pass, the complex field written with the declared macro'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - primer.classification-real-clifford-algebras@3
  - sheaf.imported-classification-values-external@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_five_values
- kind: check
  ref: check.py::check_centres_of_the_odd_values
locators:
  paper: T04
  number: Fact 2.9
  label: fact:classvalues
  line: 457
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. Notation: \mathbb{C} written with the declared macro \C, as in the technical level; the entry names the type of an algebra in the classification, not a complex structure, so no unit is involved.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the five stated Clifford algebra types through the primer classifier, and the centres of the odd ones. Version 3 -> 4.'
  env: fact
  context_refs:
  - primer.classification-real-clifford-algebras
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Re-reviewed: both edges kept, the primer classification it restates and its external references;
      levels from the earlier pass kept.'
  repair:
    note: 'imported -> proved: restates series results now in the store; derivation assembled from them,
      not yet reviewed'
subject: clifford-structure
tags: [clifford-classification]
---

## formal
Among the nondegenerate real Clifford algebras: $\Cl(1,3) \cong \Mat_2(\HH)$, $\Cl(0,4) \cong \Mat_2(\HH)$, $\Cl(0,3) \cong \HH \oplus \HH$, $\Cl(2,4) \cong \Mat_4(\HH)$, and $\Cl(1,2) \cong \Mat_2(\C)$. \emph{Provenance:} the classification of real Clifford algebras, proved in the primer \cite[Thm.~9.3]{ButlerT0}; classical references \cite{Porteous1995, Lounesto2001}.

## technical
Five values from the classification of nondegenerate real Clifford algebras: $\Cl(1,3) \cong \Mat_2(\HH)$, $\Cl(0,4) \cong \Mat_2(\HH)$, $\Cl(0,3) \cong \HH \oplus \HH$, $\Cl(2,4) \cong \Mat_4(\HH)$ and $\Cl(1,2) \cong \Mat_2(\C)$. They are imported from the classification theorem proved in the series' primer, with classical references.

## lay
The Clifford algebra of any non-degenerate geometry is, up to relabelling, a familiar algebra of matrices. This imported fact lists five such identifications; for example, the algebra of four-dimensional spacetime is the algebra of two-by-two matrices of quaternions. They come from the standard classification of real Clifford algebras.

## one-liner
The real Clifford algebras $\Cl(1,3)$, $\Cl(0,4)$, $\Cl(0,3)$, $\Cl(2,4)$ and $\Cl(1,2)$ are isomorphic to $\Mat_2(\HH)$, $\Mat_2(\HH)$, $\HH \oplus \HH$, $\Mat_4(\HH)$ and $\Mat_2(\C)$ respectively.
