---
id: hawking.imported-twistor-storey-ordering-shift
kind: claim
version: 6
title: 'Imported: the conformal storey (twistor storey), and the ordering shift'
status: proved
region: hawking
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
review: typed
derivations:
- name: main
  uses:
  - correspondence.clifford-side-ordering-shift@3
  - correspondence.fock-model-complexified-ascended-algebra@8
  - correspondence.shared-core-ordering-dictionary@4
  - correspondence.symmetrised-quadratics-palatial-algebra@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_conformal_spinor_space_has_complex_dimension_four
- kind: check
  ref: check.py::check_palatial_symmetric_ordering_shift
- kind: check
  ref: check.py::check_clifford_storey_shift_matches
locators:
  paper: T07
  number: Fact 2.6
  label: fact:rent
  line: 424
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the conformal spinor space as a 4-dimensional complex module of Cl(2,4), the palatial ordering shift -tr(M)/2, and the Clifford shift N - 1/2. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6.'
  env: fact
  context_refs:
  - correspondence.clifford-side-ordering-shift
  - correspondence.fock-model-complexified-ascended-algebra
  - correspondence.shared-core-ordering-dictionary
  - correspondence.symmetrised-quadratics-palatial-algebra
  - hawking.homogeneity-ordering-shift
  outside_pilot_cites:
  - ButlerT9
  flags:
  - 'fact restating several series results: derived from them'
  repair:
    note: 'imported -> proved: restates series results now in the store; derivation assembled from them,
      not yet reviewed'
  typing:
    by: ai-typing-pass
    note: 'Reviewed the four edges added when this fact was promoted from imported: each is a twistor-paper
      result the fact restates (Fock model, symmetrised quadratics, Clifford-side shift, ordering dictionary),
      so all are kept.'
  source_title: 'Imported: the twistor storey, and the ordering shift'
  source_formal: |-
    The spinor module of the completed algebra $\Cl(2,4)$ is twistor space $\T$, with $\dim_\C \T = 4$ (a \emph{storey} is the series' word for one level of the completion tower, as in \cite{ButlerT9}), the palatial commutation relation $[Z^\mu, \bar Z_\nu] = \hbar\,\delta^\mu_\nu$ on the quadratic (palatial) quantisation of the storey, and, for $M \in \mathfrak{gl}(\T)$, the symmetrised quadratic $q(M) := \tfrac12\bigl(Z^\mu M_\mu^{\ \nu}\bar Z_\nu + \bar Z_\nu M_\mu^{\ \nu} Z^\mu\bigr)$. (Twistor-spinor indices are written $\mu, \nu$ throughout; $\alpha$ and $\beta$ are reserved for the modular dynamics and its inverse temperature.) Symmetric ordering shifts the distinguished $\mathfrak{u}(1)$ generator $q(\id)$ by $-\hbar/2$ per complex dimension of $\T$, totalling $-2\hbar$ (equivalently, $q(M) = \sum M_\mu^{\ \nu} Z^\mu \bar Z_\nu - \tfrac{\hbar}{2}\tr M$); on the Clifford storey, the boost generator of each adjoined plane is $N - \tfrac12$, a shift of minus one half per fermionic mode: the two storeys carry the same signed ordering shift. \emph{Provenance:} the twistor paper \cite[Thm.~3.1, Rem.~3.2, \S 5, Lem.~5.5, Prop.~5.6, Thm.~5.7]{ButlerT9}; the homogeneity consequence is computed inside the proof of its Theorem 5.7 and is promoted to a stated result as Proposition \claimref{hawking.homogeneity-ordering-shift} below.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted twistor space $\T$ to the conformal spinor space $\CS$ over $I_6$, $\mathfrak{gl}(\T)$ to $\mathfrak{gl}(\CS)$, and read $\bar Z$ as the dual under the reversion form (formal, all levels, proof). The palatial quantisation is kept by name, as Penrose''s programme.'
subject: thermality
tags: [conformal-spinors, spinor-modules]
---

## formal
The spinor module of the completed algebra $\Cl(2,4)$ is the conformal spinor space $\CS = \Cl^+(2,4)P$ (twistor space), of dimension $4$ over the complex unit $I_6$ (a \emph{storey} is the series' word for one level of the completion tower, as in \cite{ButlerT9}), the palatial commutation relation $[Z^\mu, \bar Z_\nu] = \hbar\,\delta^\mu_\nu$ on the quadratic (palatial) quantisation of the storey ($\bar Z$ the dual of $Z$ under the reversion form $h$), and, for $M \in \mathfrak{gl}(\CS)$, the symmetrised quadratic $q(M) := \tfrac12\bigl(Z^\mu M_\mu^{\ \nu}\bar Z_\nu + \bar Z_\nu M_\mu^{\ \nu} Z^\mu\bigr)$. (Indices on $\CS$ are written $\mu, \nu$ throughout; $\alpha$ and $\beta$ are reserved for the modular dynamics and its inverse temperature.) Symmetric ordering shifts the distinguished $\mathfrak{u}(1)$ generator $q(\id)$ by $-\hbar/2$ per complex dimension of $\CS$, totalling $-2\hbar$ (equivalently, $q(M) = \sum M_\mu^{\ \nu} Z^\mu \bar Z_\nu - \tfrac{\hbar}{2}\tr M$); on the Clifford storey, the boost generator of each adjoined plane is $N - \tfrac12$, a shift of minus one half per fermionic mode: the two storeys carry the same signed ordering shift. \emph{Provenance:} the correspondence paper \cite[Thm.~3.1, Rem.~3.2, \S 5, Lem.~5.5, Prop.~5.6, Thm.~5.7]{ButlerT9}; the homogeneity consequence is computed inside the proof of its Theorem 5.7 and is promoted to a stated result as Proposition \claimref{hawking.homogeneity-ordering-shift} below.

## technical
The spinor module of the completed algebra $\Cl(2,4)$ is the conformal spinor space $\CS$, of dimension $4$ over the complex unit $I_6$. Its quadratic (palatial) quantisation carries $[Z^{\mu}, \bar Z_{\nu}] = \hbar\,\delta^{\mu}_{\nu}$, with $\bar Z$ dual to $Z$ under the reversion form, and for $M \in \mathfrak{gl}(\CS)$ the symmetrised quadratic is $q(M) = \tfrac12(Z^{\mu}M_{\mu}{}^{\nu}\bar Z_{\nu} + \bar Z_{\nu}M_{\mu}{}^{\nu}Z^{\mu})$.

Symmetric ordering shifts the distinguished $\mathfrak{u}(1)$ generator $q(\id)$ by $-\hbar/2$ per complex dimension, $-2\hbar$ in total; equivalently $q(M) = \sum M_{\mu}{}^{\nu}Z^{\mu}\bar Z_{\nu} - \tfrac{\hbar}{2}\tr M$. On the Clifford storey the boost generator of each adjoined plane is $N - \tfrac12$, a shift of minus one half per fermionic mode, so the two storeys carry the same signed ordering shift.

## lay
The framework's completed algebra contains a four-dimensional space of spinors whose complex unit is the algebra's own pseudoscalar. When its coordinates are quantised, the symmetric way of ordering operators shifts a basic charge by a fixed amount, half a unit per dimension. The fermionic level of the framework shows the same kind of shift, half a unit per mode, with the same sign.

## one-liner
The spinor module of $\Cl(2,4)$ is the conformal spinor space, and symmetric ordering shifts its $\mathfrak{u}(1)$ charge by $-\hbar/2$ per complex dimension, matching the shift of $-\tfrac12$ per fermionic mode on the Clifford storey.
