---
id: correspondence.no-real-lorentzian-vacuum-half-flat
kind: claim
version: 7
title: No real Lorentzian vacuum is half-flat
status: proved
region: correspondence
subject: einstein
tags: [curvature-and-field-equations, no-go, classical-theorem]
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
  role: 'consistency pass, the complexifying scalar i of the bivectors written as the central pseudoscalar I5'
  version: 7
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - correspondence.imported-weyl-commutes-duality@2
  - correspondence.imported-weyls-theorem@2
  - correspondence.lorentzian-duality-complex-structure@5
  - interior.exact-scale-decoupling@4
  - interior.imported-kerr-curvature@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_weyl_space_and_duality
- kind: check
  ref: check.py::check_vanishing_half_forces_vanishing_weyl
- kind: check
  ref: check.py::check_signature_contrast
- kind: check
  ref: check.py::check_schwarzschild_and_kerr_are_not_half_flat
locators:
  paper: T09
  number: Prop 6.5
  label: prop:lorentz
  line: 807
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle (U3) the scalar that complexifies the bivectors, kept distinct from I, is the central pseudoscalar I5 of Cl(2,3), which commutes with every spacetime vector; complex conjugation is I5 -> -I5; no bare i remains.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Weyl maps of Cl(1,3) (exact kernel, dim 10) commute with I; restriction to either duality half is injective (rank 10); contrast signatures with I^2 = +1 (5-dim half-flat space); Schwarzschild (from its gauge fields) and Kerr Weyl maps have both halves nonzero. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5. Check strengthened: Kerr closed form at a = 0 asserted equal to the computed Schwarzschild operators (pins M/2); duality-half signs moved to module level. Version 5 -> 6.'
  typing:
    by: ai-typing-pass
    added:
    - interior.exact-scale-decoupling
    - interior.imported-kerr-curvature
    note: 'Added the Schwarzschild and Kerr curvature results the black-hole clause imports (nonzero curvature scale); the paper calls the half-flat statement classical, but the classical result itself is not in the store as an imported claim, so no standard-route was added.'
  env: proposition
  context_refs:
  - interior.exact-scale-decoupling
  - interior.imported-kerr-curvature
  source_title: 'No real Lorentzian vacuum is half-flat'
  source_formal: |-
    On an oriented Lorentzian $4$-manifold, if either duality half of the Weyl tensor vanishes, the Weyl tensor vanishes: a real Lorentzian half-flat metric is conformally flat. (This is classical, and is the reason the nonlinear graviton is stated for complex or Riemannian signature in \cite{Penrose76}; the proof is included because it is four lines.) In particular no real Lorentzian black hole is half-flat: the Schwarzschild and Kerr Weyl operators are nonzero (a nonzero curvature scale times a nonzero type-D bivector off the singular locus, imported from \cite[Prop.~3.3, Fact 6.3]{ButlerT6}).
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Only the lay level named twistors; it now names Penrose''s nonlinear graviton construction instead. The formal level and proof are unchanged: the complexification $\Lambda^2_\C$ there is of the Hodge star on 2-forms, not a twistor complexification, and replacing it by the $I_4$-complex structure on bivectors would merge $\Lambda^\pm$ and change the proof, so it is kept.'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - interior.exact-scale-decoupling
    - interior.imported-kerr-curvature
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Weyl tensor is the Weyl map of the field strength on physical bivectors of a gravitational field on flat spacetime, the duality halves are the eigenspaces of multiplication by I on the complexified bivectors (the scalar i kept separate from I, as the ga_conversion note requires), conformal flatness is that of the derived metric, and the black-hole clause names the Schwarzschild and Kerr fields; the manifold form is kept as the equivalent pointwise reading. Content unchanged; proof given a pointer to the dictionary Fact.'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), $\mathcal{W}$ the Weyl map of its field strength on physical bivectors, and $\Lambda^{\pm}$ the duality halves, the eigenspaces of multiplication by the pseudoscalar $I$ (the Hodge star) on the bivectors complexified by the central pseudoscalar $I_5$ of $\Cl(2,3)$, $\Lambda^{2}_{\C} = \Lambda^{2} \oplus \Lambda^{2}I_5$ ($I_5$ commutes with every spacetime vector and is kept distinct from $I$; complex conjugation is $I_5 \mapsto -I_5$). At every point of the invertible region, if either duality half of $\mathcal{W}$ vanishes, $\mathcal{W}$ vanishes: a real half-flat field has a conformally flat derived metric. The statement is pointwise; equivalently, on an oriented Lorentzian $4$-manifold, if either duality half of the Weyl tensor vanishes, the Weyl tensor vanishes: a real Lorentzian half-flat metric is conformally flat. (This is classical, and is the reason the nonlinear graviton is stated for complex or Riemannian signature in \cite{Penrose76}; the proof is included because it is four lines.) In particular no real Lorentzian black hole is half-flat: the Weyl maps of the Schwarzschild and Kerr fields are nonzero (a nonzero curvature scale times a nonzero type-D bivector off the singular locus, the locus where $\hb$ fails, imported from \cite[Prop.~3.3, Fact 6.3]{ButlerT6}).

## technical
For a gravitational field on flat spacetime, duality on bivectors is multiplication by the pseudoscalar $I$, the Hodge star of the derived metric, a complex structure on bivectors; on the bivectors complexified by the central pseudoscalar $I_5$ of $\Cl(2,3)$, distinct from $I$, its eigenspaces $\Lambda^\pm$ are interchanged by complex conjugation. The real Weyl map $\mathcal{W}$ of the field strength commutes with $I$, so it preserves $\Lambda^\pm$, and its restrictions $\mathcal{W}^\pm$ are complex conjugates of each other. Hence $\mathcal{W}^- = 0$ forces $\mathcal{W}^+ = 0$ and so $\mathcal{W} = 0$, and by Weyl's theorem the derived metric of a real half-flat field is conformally flat. In manifold language: on an oriented Lorentzian four-manifold a real half-flat metric is conformally flat.

In particular no real Lorentzian black hole is half-flat: the Weyl maps of the Schwarzschild and Kerr fields are a nonzero curvature scale times a nonzero type-D bivector off the singular locus. The result is classical, and is the reason the nonlinear graviton is stated for complex or Riemannian signature.

## lay
In four dimensions the part of the gravitational field strength that describes tidal forces splits into two mirror-image halves. For a real gravitational field with one time direction the two halves are complex conjugates, so if one vanishes so does the other, and the geometry the field describes is then flat up to a change of scale. Real black holes such as Schwarzschild and Kerr are therefore never half-flat, which is why Penrose's construction of such spaces from spinor geometry (the nonlinear graviton) is stated only in complex or Euclidean settings.

## one-liner
For a real gravitational field on flat spacetime (equivalently, on an oriented Lorentzian four-manifold) a vanishing duality half of the Weyl map forces the whole Weyl map to vanish, so no real Lorentzian black hole is half-flat.
