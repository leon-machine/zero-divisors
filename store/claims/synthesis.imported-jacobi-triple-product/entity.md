---
id: synthesis.imported-jacobi-triple-product
kind: claim
version: 1
title: 'Imported: the Jacobi triple product identity'
status: imported
region: synthesis
subject: thermality
tags: [bosonisation, mode-counting, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'G. E. Andrews, The Theory of Partitions, Encyclopedia of Mathematics and its Applications 2, Addison-Wesley, Reading (1976).'
  key: Andrews1976
  locator: 'Thm.~2.8'
- citation: 'E. T. Whittaker and G. N. Watson, A Course of Modern Analysis, 4th ed., Cambridge University Press, Cambridge (1927).'
  key: WhittakerWatson1927
  locator: 'Sec.~21.3'
extraction:
  note: >-
    Imported for the charge-times-tower decomposition of the boundary-mode array. Cited from memory,
    not checked against the source. During filing the identity was evaluated in double precision at
    three sample points (q, z) = (0.3, 0.7), (0.5, -1.6), (0.1, 2.5), with agreement to rounding,
    and the two rewritten forms were derived from it by the substitutions stated in the formal
    level; the citing result's check also verifies the second form on a finite window, coefficient
    by coefficient.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Created by the maintainer pass so that the zero-mode doublet result can pin the triple product it cited from memory; statement confirmed numerically, references cited from memory.'
---

## formal
For complex $q$, $z$ with $|q| < 1$ and $z \neq 0$, and equally as an identity of formal series,
\[
\prod_{m \geq 1}(1 - q^{2m})(1 + zq^{2m - 1})(1 + z^{-1}q^{2m - 1}) \;=\; \sum_{n \in \Z}z^{n}q^{n^{2}}.
\]
Replacing $q$ by $q^{1/2}$, and then $z$ by $zq^{1/2}$ and multiplying by $z$, gives the two forms
\[
\prod_{m \geq 1}(1 + zq^{m - 1/2})(1 + z^{-1}q^{m - 1/2}) = \frac{\sum_{Q \in \Z}z^{Q}q^{Q^{2}/2}}{\prod_{m \geq 1}(1 - q^{m})}, \qquad (1 + z)\prod_{k \geq 1}(1 + zq^{k})(1 + z^{-1}q^{k}) = \frac{\sum_{Q \in \Z}z^{Q}q^{Q(Q-1)/2}}{\prod_{m \geq 1}(1 - q^{m})}.
\]
\emph{Provenance:} \cite[Thm.~2.8]{Andrews1976}; \cite[Sec.~21.3]{WhittakerWatson1927}.

## technical
Jacobi's triple product identity writes the theta series $\sum_{n}z^{n}q^{n^{2}}$ as an infinite product. Rescaled, it says that the generating function of a filled Dirac sea, counting charge with $z$ and energy with $q$, is a sum over charge sectors, each starting at its lowest energy ($Q^{2}/2$ with the sea between levels, $Q(Q-1)/2$ with a level at zero), times the partition generating function $\prod(1 - q^{m})^{-1}$ of a single tower of oscillators. This is the counting identity behind the boson-fermion correspondence.

## lay
The Jacobi triple product is a nineteenth-century identity that equates an infinite product with an infinite sum. In physics it says that counting the states of a sea of fermions is the same as counting a charge together with the states of a single ladder of vibrations. It is a classical result taken from the literature.

## one-liner
$\prod_{m \geq 1}(1 - q^{2m})(1 + zq^{2m-1})(1 + z^{-1}q^{2m-1}) = \sum_{n}z^{n}q^{n^{2}}$; rescaled, the fermion-sea generating function is $\sum_{Q}z^{Q}q^{Q(Q-1)/2}$ (or $q^{Q^{2}/2}$) times $\prod(1 - q^{m})^{-1}$.
