---
id: standard-model.imported-tractor-bundle-spinor-bundle-their
kind: claim
version: 6
title: 'Imported: the tractor bundle, its spinor bundle, and their connections'
status: proved
region: standard-model
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
  source: authorship disclosure of T12, deposited version
review: typed
derivations:
- name: main
  uses:
  - correspondence.imported-tractor-connection-local-twistor-transport@7
  - correspondence.local-twistor-transport-ascended-spinor-connection@9
  - interior.imported-tractor-connection@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_tractor_fibre_metric_and_structure_algebra
- kind: check
  ref: check.py::check_spinor_bundle_and_induced_spin_connection
- kind: check
  ref: check.py::check_change_of_scale_is_tractor_gauge_transformation
locators:
  paper: T12
  number: Fact 2.9
  label: fact:tractor
  line: 911
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: tractor fibre of rank 6 and signature (2,4) with structure algebra so(2,4), CS of rank 4 over I6 with the faithful spin lift B/2, and a change of scale as a tractor gauge transformation of the same shape. Version 4 -> 5. Sample inputs moved to module level; no change to what is tested. Version 5 -> 6.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the conformal four-manifold is the invertible region of a gravitational field on flat spacetime with the conformal class of its derived metric (an open subset of R^{1,3}, so spin and with trivial bundles), and the canonical connection is the tractor gauge field; content unchanged.'
  typing:
    by: ai-typing-pass
    note: 'All three uses are the restated sources (connection formula, local twistor bundle, spinor-connection
      identification); the pair-systems fact in context_refs only names the fibre elements, so it was
      not added; the E204 here comes from the spinor-connection proposition outside this list. Levels
      pass: the lay now carries the spin assumption.'
  env: fact
  context_refs:
  - correspondence.imported-tractor-connection-local-twistor-transport
  - correspondence.local-twistor-transport-ascended-spinor-connection
  - interior.imported-tractor-connection
  - standard-model.imported-pair-systems-two-chirality-halves
  flags:
  - 'fact restating several series results: derived from them'
  source_title: 'Imported: the tractor bundle, its spinor bundle, and their connections'
  source_formal: |-
    Over a conformal four-manifold the standard tractor bundle has rank six, carries a metric of signature $(2,4)$, and carries a canonical connection depending only on the conformal class, preserving that metric; its structure group is $SO(2,4)$. Where the conformal manifold is spin, which is assumed throughout (as the twistor paper assumes it), its spinor bundle is the local twistor bundle, of rank four, on whose fibres the ascended algebra $\Cl(2,4)$ acts with the twistors of Fact \claimref{standard-model.imported-pair-systems-two-chirality-halves} as fibre elements; local twistor transport is the spinor connection induced by the tractor connection, and its structure group is $\mathrm{Spin}(2,4)$, with Lie algebra $\mathfrak{so}(2,4)$. \emph{Provenance:} the connection formula, \cite[Fact~4.1]{ButlerT6}; the rank, the signature, the structure group and the spinor bundle, \cite[Fact~4.9, Prop.~4.10]{ButlerT9}.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted the local twistor bundle to the bundle of conformal spinors (fibre $\CS$, complex unit $I_6$), its twistors to conformal spinors and local twistor transport to the conformal spinor connection, in every level and the restated proof.'
---

## formal
Over the invertible region of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with the conformal class of its derived metric, the standard tractor bundle has rank six, fibre the vectors of $\Cl(2,4)$, carries a metric of signature $(2,4)$, and carries a canonical connection depending only on the conformal class, preserving that metric, which on flat spacetime is the rotation-gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}; its structure group is $SO(2,4)$. Where the conformal manifold is spin, which is assumed throughout (as the correspondence paper assumes it; the invertible region, an open subset of flat spacetime, is), its spinor bundle is the bundle of conformal spinors (the local twistor bundle), of rank four over the complex unit $I_6$, with fibre $\CS$, on whose fibres the ascended algebra $\Cl(2,4)$ acts with the conformal spinors (twistors) of Fact \claimref{standard-model.imported-pair-systems-two-chirality-halves} as fibre elements; the conformal spinor connection (local twistor transport) is the spinor connection induced by the tractor connection, and its structure group is $\mathrm{Spin}(2,4)$, with Lie algebra $\mathfrak{so}(2,4)$. \emph{Provenance:} the connection formula, \cite[Fact~4.1]{ButlerT6}; the rank, the signature, the structure group and the spinor bundle, \cite[Fact~4.9, Prop.~4.10]{ButlerT9}.

## technical
Over the invertible region of a gravitational field on flat spacetime, with the conformal class of its derived metric, the standard tractor bundle has rank six (fibre the vectors of $\Cl(2,4)$), a metric of signature $(2,4)$, and a canonical metric-preserving connection depending only on the conformal class, on flat spacetime the tractor gauge field, with structure group $SO(2,4)$. Where the manifold is spin, as assumed throughout, its spinor bundle is the rank-four bundle of conformal spinors, on whose fibres $\Cl(2,4)$ acts with conformal spinors as fibre elements.

The conformal spinor connection is the spinor connection induced by the tractor connection, with structure group $\mathrm{Spin}(2,4)$ and Lie algebra $\mathfrak{so}(2,4)$. The entry restates the series' tractor connection formula and its identification of the spinor bundle with the bundle of conformal spinors.

## lay
On spacetime considered up to rescaling there is a natural six-component structure with a way of carrying it from point to point, and, assuming spacetime is spin (as the series does throughout), an associated four-component structure whose elements are spinors of the conformal geometry. The second is carried around by the transport induced from the first. These facts, restated from earlier in the series, are the geometric setting for its particle content.

## one-liner
The rank-six tractor bundle with its $SO(2,4)$ connection has the rank-four bundle of conformal spinors as its spinor bundle, the conformal spinor connection being the induced spinor connection.
