---
id: standard-model.imported-fock-model-twistor-space
kind: claim
version: 5
title: "Imported: the Fock model of the conformal spinor space"
status: proved
region: standard-model
subject: conformal-spacetime
tags: [conformal-spinors, spinor-modules]
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
  - correspondence.fock-model-complexified-ascended-algebra@8
  - correspondence.reality-conjugation-twistor-form-factor@7
  - correspondence.spinor-identification@7
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_complexified_algebra_is_m8_on_fock_space
- kind: check
  ref: check.py::check_klein_identification_and_chart
- kind: check
  ref: check.py::check_reality_structure_and_twistor_form
- kind: check
  ref: check.py::check_invariant_pairing_is_the_top_degree_pairing
locators:
  paper: T12
  number: Fact 9.2
  label: fact:twistor
  line: 1535
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Cl(V_C) = M_8(C) on the Fock space, the Klein identification and chart, the reality structure kappa with the (2,2) twistor form, and the top-degree pairing as the unique invariant symmetric pairing. Version 3 -> 4. Sample inputs moved to module level; no change to what is tested. Version 4 -> 5.'
  env: fact
  context_refs:
  - correspondence.fock-model-complexified-ascended-algebra
  - correspondence.reality-conjugation-twistor-form-factor
  - correspondence.spinor-identification
  - standard-model.invariant-pairing-five-modes
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Fact restating series results; the three uses are the cited sources and are kept, and the five-mode
      pairing lemma was not added because it extends the statement rather than supporting the three-mode
      case stated here. Levels pass: conditions already kept.'
  source_title: "Imported: the Fock model of twistor space"
  source_formal: |-
    Let $V = \R^{2,4}$ be the ambient space of the conformal completion, $V_{\C} = W \oplus \overline{W}$ with $W$ a maximal isotropic subspace, $\dim W = 3$. The complexified algebra $\Cl(V_{\C}) \cong \mathrm{M}_{8}(\C)$ acts irreducibly on $\Lambda^{\bullet}W$, whose chirality halves are $\T = \Lambda^{\mathrm{even}}W$ and $\T' = \Lambda^{\mathrm{odd}}W$, twistor space and its dual; there is a canonical isomorphism $V_{\C} \cong \Lambda^{2}\T$ of $\mathrm{Spin}$-modules under which the quadratic form is $P \mapsto \varepsilon(P \wedge P)$ for a volume functional $\varepsilon$ on $\Lambda^{4}\T$, and a vector is null exactly when its bivector is decomposable. In the chart $\T = \Som \oplus \Spi$, $Z = (\omega^{A}, \pi_{A'})$, the bivector of $\Som$ is the point at infinity $n_{\infty}$. Dual twistors are conjugate twistors: the reality structure pairs $\T$ with $\T'$ and induces on $\T$ the Hermitian twistor form of signature $(2,2)$ preserved by $\mathrm{Spin}(2,4) \cong SU(2,2)$. The $\mathrm{Spin}$-invariant bilinear pairing of the module with itself is the top-degree pairing, pairing $\T$ with $\T'$ (degrees summing to three), twisted by the reversal sign on one argument. \emph{Provenance:} \cite[Thms.~3.1, 3.4, Prop.~4.5]{ButlerT9}; proved there for three modes; the five-mode case is proved in Lemma \claimref{standard-model.invariant-pairing-five-modes} below.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor space and its dual to the conformal spinor space and its opposite chirality (\\CS, \\CSm), and the twistor form to the invariant Hermitian form, in all levels and the restating proof; the complexified Fock model and Penrose's index notation $(\\omega^A, \\pi_{A'})$ are kept as in the source."
---

## formal
Let $V = \R^{2,4}$ be the ambient space of the conformal completion, $V_{\C} = W \oplus \overline{W}$ with $W$ a maximal isotropic subspace, $\dim W = 3$. The complexified algebra $\Cl(V_{\C}) \cong \mathrm{M}_{8}(\C)$ acts irreducibly on $\Lambda^{\bullet}W$, whose chirality halves are $\CS = \Lambda^{\mathrm{even}}W$ and $\CSm = \Lambda^{\mathrm{odd}}W$, the conformal spinor space and its opposite chirality (twistor space and its dual); there is a canonical isomorphism $V_{\C} \cong \Lambda^{2}\CS$ of $\mathrm{Spin}$-modules under which the quadratic form is $P \mapsto \varepsilon(P \wedge P)$ for a volume functional $\varepsilon$ on $\Lambda^{4}\CS$, and a vector is null exactly when its bivector is decomposable. In the chart $\CS = \Som \oplus \Spi$, $Z = (\omega^{A}, \pi_{A'})$, the bivector of $\Som$ is the point at infinity $n_{\infty}$. The opposite chirality is the conjugate of the conformal spinor space: the reality structure pairs $\CS$ with $\CSm$ and induces on $\CS$ the invariant Hermitian form (the twistor form) of signature $(2,2)$ preserved by $\mathrm{Spin}(2,4) \cong SU(2,2)$. The $\mathrm{Spin}$-invariant bilinear pairing of the module with itself is the top-degree pairing, pairing $\CS$ with $\CSm$ (degrees summing to three), twisted by the reversal sign on one argument. \emph{Provenance:} \cite[Thms.~3.1, 3.4, Prop.~4.5]{ButlerT9}; proved there for three modes; the five-mode case is proved in Lemma \claimref{standard-model.invariant-pairing-five-modes} below.

## technical
For $V = \R^{2,4}$ with $V_\C = W \oplus \overline W$ and $\dim W = 3$, the algebra $\Cl(V_\C) \cong \mathrm{M}_8(\C)$ acts irreducibly on $\Lambda^\bullet W$, whose halves $\CS = \Lambda^{\mathrm{even}}W$ and $\CSm = \Lambda^{\mathrm{odd}}W$ are the conformal spinor space and its opposite chirality. There is a canonical $\mathrm{Spin}$-isomorphism $V_\C \cong \Lambda^2\CS$ with quadratic form $P \mapsto \varepsilon(P \wedge P)$, null vectors being decomposable, and in the chart $\CS = \Som \oplus \Spi$ the bivector of $\Som$ is $n_\infty$.

The reality structure pairs $\CS$ with $\CSm$ and induces on $\CS$ the invariant Hermitian form of signature $(2,2)$ preserved by $\mathrm{Spin}(2,4) \cong SU(2,2)$, and the invariant bilinear pairing of the module is the top-degree pairing of $\CS$ with $\CSm$, twisted by reversal on one argument.

## lay
This restates how the four-dimensional spinor space of the conformal algebra arises inside the completed algebra of the series. The algebra acts on an eight-dimensional space built from three fermionic modes, which splits into two halves of opposite chirality. Vectors of the six-dimensional ambient space correspond to pairs of spinors from one half, and complex conjugation turns one half into the other, giving the Hermitian form whose symmetry group is the conformal group.

## one-liner
Imported: the conformal spinor space and its opposite are the chirality halves of the Fock module $\Lambda^\bullet W$, with $V_\C \cong \Lambda^2\CS$, the signature-$(2,2)$ Hermitian form from the reality structure, and the top-degree invariant pairing.
