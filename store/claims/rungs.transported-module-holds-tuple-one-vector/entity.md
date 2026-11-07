---
id: rungs.transported-module-holds-tuple-one-vector
kind: claim
version: 5
title: The transported module holds the tuple as one vector, not as two conformal spinors
status: proved
region: rungs
subject: standard-model
tags:
- spinor-modules
- conformal-spinors
- no-go
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-rungs, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - rungs.ladder-group-rung-mixing-group-one@4
  - rungs.mass-bracket-frozen-points-grip-slot@3
  - rungs.rung-spinor-module-mixings@5
  - standard-model.under-s-composites-state-space-spinor@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12_rungs.py
  tags:
  - label:prop:config
- kind: check
  ref: check.py::check_two_spinor_configuration_is_the_one_rung_sector
- kind: check
  ref: check.py::check_two_particle_product_not_in_module
- kind: check
  ref: check.py::check_mass_bracket_is_quadratic
locators:
  paper: T12-rungs
  number: Prop 3.3
  label: prop:config
  line: 319
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the (1,0)+(1,2) sector is C^2 (x) CS with content (2,1)_1/2 + (2,3b)_-1/6, S^2(Lambda^2 W) (Casimir 20/3) is absent from the module, and the bracket is quadratic. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: Converted T, T (+) T, T (x) T and Lambda^2 T to the conformal spinor space S and its sums, products
      and exterior square at every level, title and proof included, and read (omega, pi) as the E = -1
      and E = +1 parts at the origin. The complex structures of C^2 and the Fock module are kept.
  source_title: The transported module holds the tuple as one vector, not as two twistors
  source_formal: 'The two-twistor configuration space of Fact \claimref{rungs.imported-mass-symplectic-area},
    as a vector space, is $\T \oplus \T = \C^{2} \otimes \T$, eight-dimensional, carrying the continuous
    data $(\omega^{i}, \pi^{i})$; it is the sector $(j, k) \in \{(1,0), (1,2)\}$ of the two-rung module,
    which under $U(2) \times U(3)$ is, by Fact \claimref{standard-model.under-s-composites-state-space-spinor},
    $(2,1)_{1/2} \oplus (2,\bar{3})_{-1/6}$, the antiparticle doublets $L^{*} \oplus Q^{*}$ in the orientation
    of T12''s listing or $L \oplus Q$ in the opposite one. The two-particle tensor product $\T \otimes
    \T$, by contrast, has no $U(3)$-equivariant embedding in the module: it contains $S^{2}(\Lambda^{2}W)$,
    the six-dimensional $SU(3)$-irreducible $\bar{6}$, while every sector of the module is a multiple
    of $\Lambda^{\bullet}W$, whose $SU(3)$ content is $1, 3, \bar{3}, 1$. And the mass bracket, the $\Lambda^{2}\C^{2}
    \otimes \Lambda^{2}\T$ component of $\Psi \odot \Psi$ (Lemma \claimref{rungs.mass-bracket-frozen-points-grip-slot}),
    is quadratic in $\Psi$ and lives in $S^{2}$ of the module, not in the module. So the module treats
    the composite as T12 does, as one tuple $\Psi$ with a slot index, and not as a product state of two
    twistors.'
  env: proposition
  context_refs:
  - rungs.imported-mass-symplectic-area
  typing:
    by: ai-typing-pass
    note: 'Did not add the mass-as-area fact from context_refs, which only names the configuration space
      and is not relied on by the proof; the Fulton-Harris irreducibility is an external citation with
      no store claim. Levels pass: conditions already kept.'
about:
- obj.standard-model.two-rung-module-sectors-slot-components
---

## formal
The configuration space of two conformal spinors (two twistors) of Fact \claimref{rungs.imported-mass-symplectic-area}, as a vector space, is $\CS \oplus \CS = \C^{2} \otimes \CS$, $\CS$ the conformal spinor space, eight-dimensional, carrying the continuous data $(\omega^{i}, \pi^{i})$, the parts of each spinor in the $E = -1$ and $E = +1$ eigenspaces at the origin; it is the sector $(j, k) \in \{(1,0), (1,2)\}$ of the two-rung module, which under $U(2) \times U(3)$ is, by Fact \claimref{standard-model.under-s-composites-state-space-spinor}, $(2,1)_{1/2} \oplus (2,\bar{3})_{-1/6}$, the antiparticle doublets $L^{*} \oplus Q^{*}$ in the orientation of T12's listing or $L \oplus Q$ in the opposite one. The two-particle tensor product $\CS \otimes \CS$, by contrast, has no $U(3)$-equivariant embedding in the module: it contains $S^{2}(\Lambda^{2}W)$, the six-dimensional $SU(3)$-irreducible $\bar{6}$, while every sector of the module is a multiple of $\Lambda^{\bullet}W$, whose $SU(3)$ content is $1, 3, \bar{3}, 1$. And the mass bracket, the $\Lambda^{2}\C^{2} \otimes \Lambda^{2}\CS$ component of $\Psi \odot \Psi$ (Lemma \claimref{rungs.mass-bracket-frozen-points-grip-slot}), is quadratic in $\Psi$ and lives in $S^{2}$ of the module, not in the module. So the module treats the composite as T12 does, as one tuple $\Psi$ with a slot index, and not as a product state of two conformal spinors.

## technical
The configuration space of two conformal spinors, as a vector space, is $\CS \oplus \CS = \C^{2} \otimes \CS$, eight-dimensional. In the two-rung module it is the sector $(j,k) \in \{(1,0), (1,2)\}$, which under $U(2) \times U(3)$ is $(2,1)_{1/2} \oplus (2,\bar{3})_{-1/6}$: the antiparticle doublets $L^{*} \oplus Q^{*}$ in one orientation, or $L \oplus Q$ in the other.

The two-particle product $\CS \otimes \CS$ has no $U(3)$-equivariant embedding in the module: it contains $S^{2}(\Lambda^{2}W)$, the irreducible $\bar{6}$ of $SU(3)$, whereas every sector of the module is a multiple of $\Lambda^{\bullet}W$, whose $SU(3)$ content is $1, 3, \bar{3}, 1$. The mass bracket, quadratic in $\Psi$, lives in $S^{2}$ of the module rather than in the module. So the module holds the composite as one tuple $\Psi$ with a slot index, not as a product of two conformal-spinor states.

## lay
A pair of basic spinor states of the conformal algebra could be described either as a single object with two slots or as two separate particles combined. The transported state space only accommodates the first description: it contains the two-slot object as one of its sectors, but has no room for a six-dimensional colour pattern that the two-particle description would bring. The mass, which depends quadratically on the pair, sits outside the state space itself.

## one-liner
The transported module contains the configuration $\C^{2} \otimes \CS$ of two conformal spinors as its $(1,0) \oplus (1,2)$ sector but admits no equivariant embedding of $\CS \otimes \CS$, so it holds the composite as one tuple, not as two spinors.
