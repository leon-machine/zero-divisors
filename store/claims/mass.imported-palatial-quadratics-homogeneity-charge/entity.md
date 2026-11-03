---
id: mass.imported-palatial-quadratics-homogeneity-charge
kind: claim
version: 4
title: "Imported: the palatial quadratics and the homogeneity charge"
status: proved
region: mass
subject: conformal-spacetime
tags: [conformal-spinors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
review: typed
derivations:
- name: main
  uses:
  - correspondence.shared-core-ordering-dictionary@4
  - correspondence.symmetrised-quadratics-palatial-algebra@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_palatial_quadratics_represent_gl4
- kind: check
  ref: check.py::check_identity_quadratic_is_homogeneity_shifted_by_two
locators:
  paper: T11
  number: Fact 2.4
  label: fact:palatial
  line: 426
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: [q(M), q(N)] = hbar q([M,N]) on all gl(4) matrix units in the Laurent-polynomial realisation, faithfulness, and q(id) = -(h+2) hbar with the -2 hbar ordering shift. Version 3 -> 4.'
  env: fact
  context_refs:
  - correspondence.shared-core-ordering-dictionary
  - correspondence.symmetrised-quadratics-palatial-algebra
  unresolved_refs:
  - rem:quantum
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: Both uses are the cited sources and kept; the homogeneity -2s-2 is Penrose's, but no imported
      claim in the store states the operator identity (the Penrose-transform import states only the homogeneity
      classification), so no standard-route derivation.
  source_title: "Imported: the palatial quadratics and the homogeneity charge"
  source_formal: |-
    The symmetrised quadratics $q(M)$ in the twistor oscillators represent $\mathfrak{su}(2,2)$ with $[q(M), q(M')] = \hbar\, q([M,M'])$, and, in that paper's realisation $\bar{Z}_{\beta} = -\hbar\partial_{\beta}$, the symmetrised identity quadratic $q(\mathrm{id})$ acts on functions of homogeneity $h$ as $-(h+2)\hbar$ (Penrose's $-2s-2$, proved in the series as an exact identity in the proof of that theorem); the lemma represents all of $\mathfrak{gl}(4,\C)$, of which $\mathfrak{su}(2,2)$ is the real form used here. \emph{Provenance:} \cite[Lem.~5.5, Thm.~5.7]{ButlerT9}. Used here only in Remark \ref{rem:quantum}, to place the classical computation of Section \ref{sec:join} against its quantisation.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed the twistor oscillators to the palatial oscillators (the conformal spinor coordinates), named once, in all levels and the restating proof; Penrose's homogeneity rule keeps its name."
---

## formal
The symmetrised quadratics $q(M)$ in the palatial oscillators $Z^\alpha$, $\bar Z_\beta$ (twistor oscillators: the conformal spinor coordinates and their conjugates) represent $\mathfrak{su}(2,2)$ with $[q(M), q(M')] = \hbar\, q([M,M'])$, and, in that paper's realisation $\bar{Z}_{\beta} = -\hbar\partial_{\beta}$, the symmetrised identity quadratic $q(\mathrm{id})$ acts on functions of homogeneity $h$ as $-(h+2)\hbar$ (Penrose's $-2s-2$, proved in the series as an exact identity in the proof of that theorem); the lemma represents all of $\mathfrak{gl}(4,\C)$, of which $\mathfrak{su}(2,2)$ is the real form used here. \emph{Provenance:} \cite[Lem.~5.5, Thm.~5.7]{ButlerT9}. Used here only in Remark \ref{rem:quantum}, to place the classical computation of Section \ref{sec:join} against its quantisation.

## technical
The symmetrised quadratics $q(M)$ in the palatial oscillators represent $\mathfrak{gl}(4, \C)$, and hence its real form $\mathfrak{su}(2,2)$, with $[q(M), q(M')] = \hbar\, q([M, M'])$.

In the realisation $\bar Z_\beta = -\hbar\partial_\beta$, the symmetrised identity quadratic acts on functions homogeneous of degree $h$ as $q(\mathrm{id}) = -(h+2)\hbar$, which is Penrose's homogeneity $-2s-2$. Here it is used only to set a classical computation against its quantisation.

## lay
When the coordinates of the four-component conformal spinors are turned into quantum operators, certain quadratic combinations of them reproduce the conformal symmetry algebra. One of them, built from the identity, measures how a function on the spinor space scales, shifted by two because of operator ordering. This matches Penrose's rule relating scaling weight to helicity.

## one-liner
Imported: the symmetrised palatial quadratics represent $\mathfrak{su}(2,2)$ with bracket $\hbar\, q([M, M'])$, and $q(\mathrm{id})$ acts on functions of homogeneity $h$ as $-(h+2)\hbar$.
