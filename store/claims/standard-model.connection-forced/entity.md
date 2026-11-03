---
id: standard-model.connection-forced
kind: claim
version: 4
title: The connection is forced
status: proved
region: standard-model
subject: standard-model
tags: [gauge-fields, forcing-and-uniqueness, tractors]
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
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - standard-model.imported-tractor-bundle-spinor-bundle-their@6
  - standard-model.segre-lemma-automorphisms-preserving-decomposable-tensors@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_spin_connection_form_is_so24
- kind: check
  ref: check.py::check_factorisation_preserving_unitary_algebra
locators:
  paper: T12
  number: Prop 5.7
  label: prop:connection
  line: 1150
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the tangent algebra of Spin(2,4) is the 15 bivectors, faithful and I6-linear on CS; the factorisation- and Hermitian-preserving algebra on C^2 (x) C^3 is su(2) + su(3) + u(1) of dimension 12. Version 3 -> 4.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: spacetime is the invertible region of a gravitational field on flat spacetime and the conformal spinor connection is the tractor gauge field acting on conformal spinors; the theorem unchanged.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the local twistor bundle and local twistor transport to the conformal spinor bundle and the conformal spinor connection (tractor connection on S), naming the twistor terms once, at every level. The proof had no twistor language.'
  source_title: |-
    The connection is forced
  source_formal: |-
    Let matter fields be sections of $\mathcal{S} \otimes \mathcal{H}$ over spacetime, with $\mathcal{S}$ the local twistor bundle of Fact \claimref{standard-model.imported-tractor-bundle-spinor-bundle-their} (the spinor bundle of the tractor bundle, whose fibres are the twistors) and $\mathcal{H}$ the hierarchy bundle, a complex vector bundle of rank six whose fibres carry the factorisation $\C^{2} \otimes \C^{3}$ and its Hermitian structure. Let $D$ be a connection on $\mathcal{S} \otimes \mathcal{H}$ that is induced from connections on the two factors, $D = \nabla \otimes 1 + 1 \otimes D_{\mathcal{H}}$, with $\nabla$ a $\mathrm{Spin}(2,4)$-connection on $\mathcal{S}$ (one whose transports lie in the spin group acting on the twistor fibre, as local twistor transport does) and $D_{\mathcal{H}}$ preserving the Hermitian structure and the factorisation of the fibre (its parallel transports map the set of decomposable tensors onto itself). Then $\nabla$ has connection form valued in $\mathfrak{so}(2,4)$ and $D_{\mathcal{H}} = d + \mathcal{A}$ in any factorisation-adapted local frame, with $\mathcal{A}$ a one-form valued in $\su(2) \oplus \su(3) \oplus \uu(1)$ acting through Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}'s action; conversely every such pair $(\nabla, \mathcal{A})$ gives a connection with these properties.
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'Kept all three edges, each a premise of the proof; the closed-subgroup theorem is an external citation.'
---

## formal
Let matter fields be sections of $\mathcal{S} \otimes \mathcal{H}$ over the invertible region of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with $\mathcal{S}$ the conformal spinor bundle (local twistor bundle) of Fact \claimref{standard-model.imported-tractor-bundle-spinor-bundle-their} (the spinor bundle of the tractor bundle, whose fibre is the conformal spinor space) and $\mathcal{H}$ the hierarchy bundle, a complex vector bundle of rank six whose fibres carry the factorisation $\C^{2} \otimes \C^{3}$ and its Hermitian structure. Let $D$ be a connection on $\mathcal{S} \otimes \mathcal{H}$ that is induced from connections on the two factors, $D = \nabla \otimes 1 + 1 \otimes D_{\mathcal{H}}$, with $\nabla$ a $\mathrm{Spin}(2,4)$-connection on $\mathcal{S}$ (one whose transports lie in the spin group acting on the conformal spinor fibre, as the conformal spinor connection, local twistor transport, does; on flat spacetime that connection is the tractor gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection} acting on $\CS$) and $D_{\mathcal{H}}$ preserving the Hermitian structure and the factorisation of the fibre (its parallel transports map the set of decomposable tensors onto itself). Then $\nabla$ has connection form valued in $\mathfrak{so}(2,4)$ and $D_{\mathcal{H}} = d + \mathcal{A}$ in any factorisation-adapted local frame, with $\mathcal{A}$ a one-form valued in $\su(2) \oplus \su(3) \oplus \uu(1)$ acting through Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}'s action; conversely every such pair $(\nabla, \mathcal{A})$ gives a connection with these properties.

## technical
Let matter fields be sections of $\mathcal{S} \otimes \mathcal{H}$ over the invertible region of a gravitational field on flat spacetime, with $\mathcal{S}$ the conformal spinor bundle and $\mathcal{H}$ a rank-six hierarchy bundle whose fibres carry the factorisation $\C^{2} \otimes \C^{3}$ and a Hermitian structure. Suppose the connection is induced from the factors, $D = \nabla \otimes 1 + 1 \otimes D_{\mathcal{H}}$, with $\nabla$ a $\mathrm{Spin}(2,4)$-connection and $D_{\mathcal{H}}$ preserving the Hermitian structure and the set of decomposable tensors.

Then $\nabla$ has connection form valued in $\so(2,4)$, and in any factorisation-adapted frame $D_{\mathcal{H}} = d + \mathcal{A}$ with $\mathcal{A}$ a one-form valued in $\su(2) \oplus \su(3) \oplus \uu(1)$, by the Segre lemma and the closed-subgroup theorem. Conversely every such pair $(\nabla, \mathcal{A})$ gives a connection with these properties.

## lay
Suppose matter fields carry both the spinor structure of the conformal algebra and the two-by-three internal structure, and that moving them from point to point must respect both. Then the only freedom left is a connection of a very particular kind, whose internal part takes values in exactly the Lie algebra of the Standard Model's forces. Under these assumptions the gauge fields are what the preserved structure allows, rather than an extra ingredient.

## one-liner
A connection on $\mathcal{S} \otimes \mathcal{H}$ induced from a $\mathrm{Spin}(2,4)$-connection and a connection preserving the hierarchy's factorisation and Hermitian structure is exactly an $\so(2,4)$ part plus an $\su(2) \oplus \su(3) \oplus \uu(1)$ gauge field.
