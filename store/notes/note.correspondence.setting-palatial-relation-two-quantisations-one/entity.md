---
id: note.correspondence.setting-palatial-relation-two-quantisations-one
kind: note
version: 2
title: 'The palatial relation: two quantisations, one core'
status: setting
subject: conformal-spacetime
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, sign of the quoted realisation of the palatial relations stated against the displayed relation'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
comments_on:
- correspondence.statistics-no-go
locators:
  paper: T09
  number: Setting
  section: 'The palatial relation: two quantisations, one core'
  line: 634
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. The note displayed [Z, Zbar] = +hbar and said it is realised by Zbar = hbar d/dZ, which gives -hbar ([z, hbar d/dz] f = -hbar f); the sentence now says so and names the realisation Zbar = -hbar d/dZ used by correspondence.symmetrised-quadratics-palatial-algebra and its check.'
---

## formal
Palatial twistor theory \cite{Penrose15} is Penrose's current approach to the full Einstein equations: it replaces holomorphic functions on twistor space by a \emph{noncommutative} algebra of twistor operators, with $\bar Z$ realised as a derivative and the googly data expected to reside in ordering ambiguities. The transport framework independently produces noncommutative pair structure, the completed ladder pairs with their CAR relations, as the mandatory replacement for classical values at the singular locus \cite{ButlerT1}. It is natural to conjecture that the two structures are the same object. This section proves that the naive form of that conjecture is \emph{false}, for a reason of statistics that admits a one-line proof, and then proves the corrected picture: the two algebras are the two storeys of one tower, meeting at the conformal algebra.

Throughout, the \emph{palatial algebra} $\mathcal{P}$ is the unital associative $\C$-algebra with generators $Z^\alpha, \bar Z_\beta$ ($\alpha, \beta = 1, \dots, 4$) and relations
\[
[Z^\alpha, Z^\beta] = 0, \qquad [\bar Z_\alpha, \bar Z_\beta] = 0, \qquad [Z^\alpha, \bar Z_\beta] = \hbar\,\delta^\alpha_\beta ,
\]
the twistor canonical commutation relations of \cite{Penrose15} (there realised on holomorphic functions by $\bar Z_\beta = \hbar\,\partial/\partial Z^\beta$, which gives the commutator in the opposite order, $[Z^\alpha, \bar Z_\beta] = -\hbar\,\delta^\alpha_\beta$; the sign displayed is realised by $\bar Z_\beta = -\hbar\,\partial/\partial Z^\beta$, as in Lemma \claimref{correspondence.symmetrised-quadratics-palatial-algebra}); $\hbar \neq 0$ is a fixed constant.

## technical
pending

## lay
pending

## one-liner
pending
