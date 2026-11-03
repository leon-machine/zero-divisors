---
id: families.imported-squeezed-vacuum-bosonic-pairing-external
kind: claim
version: 1
title: 'Imported: the squeezed vacuum of a bosonic pairing (external ingredients)'
status: imported
region: families
subject: generations
tags: [classical-theorem, pairing-and-bogoliubov]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
review: typed
imported_from:
- citation: R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd ed., Cambridge University Press (2013).
  key: HornJohnson
  locator: Cor.~4.4.4
- citation: F. A. Berezin, The Method of Second Quantization, Academic Press (1966).
  key: Berezin1966
  locator: Ch.~2-3
- citation: C. Weedbrook, S. Pirandola, R. Garc'ia-Patr'on, N. J. Cerf, T. C. Ralph, J. H. Shapiro and
    S. Lloyd, Gaussian quantum information, Rev. Mod. Phys. 84 (2012), 621.
  key: Weedbrook2012
  locator: \S II
locators:
  paper: T13
  number: Fact 2.6
  label: ''
  line: 601
extraction:
  env: fact
  context_refs:
  - correspondence.shared-core-ordering-dictionary
  flags:
  - external ingredients of families.imported-squeezed-vacuum-bosonic-pairing
  typing:
    by: ai-typing-pass
    note: Imported literature stub with no derivations; only the levels were written.
---

## formal
The results from outside the series on which \claimref{families.imported-squeezed-vacuum-bosonic-pairing} draws, as cited there: R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd ed., Cambridge University Press (2013)., Cor.~4.4.4; F. A. Berezin, The Method of Second Quantization, Academic Press (1966)., Ch.~2-3; C. Weedbrook, S. Pirandola, R. Garc'ia-Patr'on, N. J. Cerf, T. C. Ralph, J. H. Shapiro and S. Lloyd, Gaussian quantum information, Rev. Mod. Phys. 84 (2012), 621., \S II.

## technical
This entry collects the results from outside the series on which the squeezed-vacuum fact draws: the Takagi factorisation of a complex symmetric matrix, $\xi = U\Sigma U^{\mathsf{T}}$ with $U$ unitary and $\Sigma$ the diagonal of singular values (Horn and Johnson); bosonic Bogoliubov transformations, squeezed vacua and Wick's theorem for quasi-free states (Berezin); and the covariance-matrix form of Gaussian states (Weedbrook and collaborators). None of them is proved in the series.

## lay
This entry records the textbook sources behind the description of squeezed states: a standard way of factorising symmetric matrices, the classic treatment of paired bosonic particles, and a modern review of such states in quantum information. They are imported as established results.

## one-liner
The Takagi factorisation, bosonic Bogoliubov transformations with Wick's theorem, and the covariance-matrix form of Gaussian states are imported from the literature.
