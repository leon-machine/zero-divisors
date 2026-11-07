---
id: correspondence.imported-tractor-connection-local-twistor-transport
kind: claim
version: 7
title: 'Imported: the tractor connection and its conformal spinor form'
status: proved
region: correspondence
subject: einstein
tags: [tractors, conformal-spinors]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 7
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - correspondence.imported-tractor-connection-local-twistor-transport-external@1
  - interior.imported-tractor-connection@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_tractor_connection_in_a_scale
- kind: check
  ref: check.py::check_conformal_spinor_space_and_its_planes
- kind: check
  ref: check.py::check_conformal_spinor_connection_block_form
- kind: check
  ref: check.py::check_change_of_scale_fixes_omega_and_shifts_pi
locators:
  paper: T09
  number: Fact 4.9
  label: fact:ltt
  line: 581
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The factors i of the conformal spinor connection (local twistor transport) in the formal and technical levels and the proof are now written as the conformal spinors'' unit, right multiplication by I_6, which the entity already said they stand for; the source''s form with i stays under extraction.source_formal; no bare i remains.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the tractor gauge field reproduces the displayed connection slots in a scale and is metric; CS = Cl^+(2,4) P is C^4 over I6, split into the pi-plane ker n0 and the omega-plane ker ninf; the spin action gives the block form of the conformal spinor connection; a change of scale fixes omega and shifts pi. Version 4 -> 5. Check strengthened: spin-form identity tested on all eight CS basis spinors (was four); sample points, by-hand inputs and spin-form vectors moved to module level. Version 5 -> 6.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the conformal class is that of the derived metric of a gravitational field on flat spacetime; clause (i) names the tractor connection as the flat-space Cl(2,4) gauge field, its index display kept as its reading in a scale; clause (ii) and the provenance unchanged.'
  typing:
    by: ai-typing-pass
    note: 'Both uses kept: the series tractor-connection fact supplies part (i) in the series conventions
      and the external literature supplies part (ii); no standard route applies since the entry is itself
      an import. Levels pass: conditions already kept.'
  env: fact
  context_refs:
  - interior.imported-tractor-connection
  flags:
  - 'fact restating several series results: derived from them'
  source_title: 'Imported: the tractor connection, and local twistor transport'
  source_formal: |-
    (i) The conformal class carries a canonical connection on the rank-six tractor bundle whose expression in a scale $g$ is
    \[
    \nabla_a(\sigma, \mu_b, \rho) = \bigl(\nabla_a\sigma - \mu_a,\;\; \nabla_a\mu_b + g_{ab}\rho - \mathrm{P}_{ab}\sigma,\;\; \nabla_a\rho + \mathrm{P}_a{}^b\mu_b\bigr),
    \]
    with $\mathrm{P}$ the Schouten tensor. (ii) The conformal class likewise carries the classical \emph{local twistor} bundle, fibrewise $\C^4$ with the scale splitting $Z = (\omega^B, \pi_{B'})$, and its transport
    \[
    \nabla^{\mathrm{LT}}_a(\omega^B, \pi_{B'}) \;=\; \bigl(\nabla_a \omega^B + i\,\varepsilon_A{}^B\,\pi_{A'},\;\; \nabla_a\pi_{B'} + i\,\mathrm{P}_{AA'BB'}\,\omega^B\bigr),
    \]
    in the index conventions of \cite[Vol.~2, Ch.~6]{PenroseRindler86}; under conformal rescaling $\omega$ is invariant and $\pi$ shifts, so the $\pi$-plane $\{\omega = 0\}$ is the canonical subbundle. \emph{Provenance:} (i) \cite{BEG1994, CurryGover2018}, in the conventions of \cite[Fact 4.1, eq.~(3)]{ButlerT6}; (ii) \cite{PenroseMacCallum73, Dighton74}; the statement that (ii) is the spin representation of (i) is standard in the tractor literature \cite{BEG1994, CurryGover2018}, and is \emph{proved} rather than imported below, since the proof is short in the present framework.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the local twistor bundle to the bundle of conformal spinors (fibre $\CS$, complex unit $I_6$) and local twistor transport to the conformal spinor connection; the transport formula is kept in Penrose-Rindler 2-spinor index form, as the import it is, with its factor $i$ read as $I_6$ and the $\pi$-plane read as the kernel of the point''s null vector.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - "the factors $i$ of the imported local twistor transport formula: the conformal spinors unit $I_6$, set by the earlier pass"
---

## formal
Let $[g]$ be the conformal class of the derived metric of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), on its invertible region. (i) $[g]$ carries a canonical connection on the rank-six tractor bundle, whose fibre is the vector space of $\Cl(2,4)$ and which on flat spacetime is the rotation-gauge field $D^{T}_{a} = a \cdot \nabla + \Omega_{T}(a)\times$ of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}; its expression in a scale $g$ is
\[
\nabla_a(\sigma, \mu_b, \rho) = \bigl(\nabla_a\sigma - \mu_a,\;\; \nabla_a\mu_b + g_{ab}\rho - \mathrm{P}_{ab}\sigma,\;\; \nabla_a\rho + \mathrm{P}_a{}^b\mu_b\bigr),
\]
with $\mathrm{P}$ the Schouten tensor. (ii) The conformal class likewise carries the classical bundle of conformal spinors (the \emph{local twistor} bundle), fibrewise the conformal spinor space $\CS = \Cl^+(2,4)P$, a $4$-dimensional module over the complex unit $I_6$, with the scale splitting $Z = (\omega^B, \pi_{B'})$ into the halves $\Som \oplus \Spi$, and its transport, the conformal spinor connection (local twistor transport),
\[
\nabla^{\mathrm{LT}}_a(\omega^B, \pi_{B'}) \;=\; \bigl(\nabla_a \omega^B + \varepsilon_A{}^B\,\pi_{A'}I_6,\;\; \nabla_a\pi_{B'} + \mathrm{P}_{AA'BB'}\,\omega^B I_6\bigr),
\]
in the index conventions of \cite[Vol.~2, Ch.~6]{PenroseRindler86}, where the complex unit of $\CS$, the source's imaginary unit, is right multiplication by the conformal pseudoscalar $I_6$; under conformal rescaling $\omega$ is invariant and $\pi$ shifts, so the $\pi$-plane $\{\omega = 0\}$ (the kernel in $\CS$ of the point's null vector) is the canonical subbundle. \emph{Provenance:} (i) \cite{BEG1994, CurryGover2018}, in the conventions of \cite[Fact 4.1, eq.~(3)]{ButlerT6}; (ii) \cite{PenroseMacCallum73, Dighton74}; the statement that (ii) is the spin representation of (i), that is, that the conformal spinor connection is the tractor connection acting on $\CS$, is standard in the tractor literature \cite{BEG1994, CurryGover2018}, and is \emph{proved} rather than imported below, since the proof is short in the present framework.

## technical
The conformal class of a gravitational field on flat spacetime carries two canonical connections. On the rank-six tractor bundle, whose fibre is the vector space of $\Cl(2,4)$ and on which the connection is the flat-space gauge field $\Omega_{T}$ built from $\Omega$, the frame and the Schouten map, the expression in a scale $g$ is $\nabla_a(\sigma, \mu_b, \rho) = (\nabla_a\sigma - \mu_a,\ \nabla_a\mu_b + g_{ab}\rho - \mathrm{P}_{ab}\sigma,\ \nabla_a\rho + \mathrm{P}_a{}^b\mu_b)$, with $\mathrm{P}$ the Schouten tensor. On the bundle of conformal spinors, fibrewise the $4$-dimensional spinor space $\CS$ of the even conformal algebra over the complex unit $I_6$ and split in a scale as $Z = (\omega^B, \pi_{B'})$, the conformal spinor connection is $\nabla^{\mathrm{LT}}_a(\omega^B, \pi_{B'}) = (\nabla_a\omega^B + \varepsilon_A{}^B\pi_{A'}I_6,\ \nabla_a\pi_{B'} + \mathrm{P}_{AA'BB'}\omega^B I_6)$ in Penrose-Rindler index conventions, with the unit $I_6$ acting on the right.

Under conformal rescaling $\omega$ is invariant and $\pi$ shifts, so the $\pi$-plane $\{\omega = 0\}$, the kernel of the point's null vector, is the canonical subbundle. Both connections are taken from the literature, the first in the series' own conventions; that the second is the first acting on conformal spinors (its spin representation) is proved in the series rather than imported.

## lay
Gravity on flat spacetime determines a conformal geometry, which carries two standard ways of carrying data from point to point. One acts on the six-component vectors of the series' conformal model, called tractors, and on flat spacetime it is itself a gauge field built from gravity; the other acts on four-component spinors of the conformal geometry. This entry records both formulas, taken from the literature, in the conventions the series uses.

## one-liner
The conformal class of a gravitational field on flat spacetime carries the tractor connection, a $\Cl(2,4)$ gauge field, and its spinor form, the conformal spinor connection on the rank-four bundle of conformal spinors, with explicit formulas imported in the series' conventions.
