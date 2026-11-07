---
id: dark-matter.imported-frozen-point-de-sitter-radius
kind: claim
version: 6
title: 'Imported: the frozen point and the de Sitter radius'
status: proved
region: dark-matter
subject: dark-energy
tags:
- frozen-point
- cosmological-constant
- undetermined-input
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-energy.frozen-point-makes-stelle-west-vector@6
  - dark-energy.imported-frozen-point-geometry@7
  - dark-energy.under-action-written-norm-parameter-laws@4
  - interior.non-null-stabilisers-section-they-act@4
  - interior.scale-tractor-leaves-cone@8
  - interior.stabiliser-rotates-parabolic-reductive@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_parallel_scale_tractor_norm_and_complement
- kind: check
  ref: check.py::check_stabiliser_is_de_sitter_algebra
- kind: check
  ref: check.py::check_section_is_de_sitter_hyperboloid_radius_l
- kind: check
  ref: check.py::check_lambda_is_a_parameter_of_the_laws
locators:
  paper: T14
  number: Fact 7.18
  label: fact:dsradius
  line: 1035
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (second round): dark-energy.imported-frozen-point-geometry repinned 6 -> 7 after reviewing its restatement (the sentence naming the tractor gauge-field theorem moved to a text-only remark); the parts cited here (parallel frozen point, Q(I) = Lambda/3, the stabilisers, the scale-g display and the Schouten tensor) are unchanged, and the use here holds as cited.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: parallel scale tractor with Q(I) = Lambda/3, I^perp of signature (1,4), stabiliser so(1,4) = Lambda^2(I^perp), the section a hyperboloid Q(Y) = -l^2 with l^2 = 3/Lambda, and the fluctuation count showing Lambda a parameter. Version 5 -> 6.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Einstein region is that of a gravitational field on flat spacetime and the scale tractor the Cl(2,4) vector parallel for the tractor gauge field; the de Sitter hyperboloid is a conformal-model section.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  typing:
    by: ai-typing-pass
    note: 'Restatement of series results; kept all six premises, each matching a cited locator, and the
      E204 traces to the trichotomy fact outside this list. Levels pass: lay and one-liner now keep the
      Einstein region, and the one-liner keeps "under the action as written".'
  env: fact
  context_refs:
  - dark-energy.frozen-point-makes-stelle-west-vector
  - dark-energy.imported-frozen-point-geometry
  - dark-energy.under-action-written-norm-parameter-laws
  - interior.non-null-stabilisers-section-they-act
  - interior.scale-tractor-leaves-cone
  - interior.stabiliser-rotates-parabolic-reductive
  flags:
  - 'fact restating several series results: derived from them'
about:
- obj.dark-energy.four-ways-number-enters-theory-shape
---

## formal
On the Einstein region with $\Lambda > 0$ of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), the scale tractor $I$, parallel for the tractor gauge field of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, has squared norm $Q(I) = \tfrac{\Lambda}{3}$, its stabiliser is the de Sitter group $SO(1,4)$, its orthogonal complement $I^{\perp}$ in the vectors of $\Cl(2,4)$ carries the induced form of signature $(1,4)$, and the flat-model section is the de Sitter hyperboloid of radius $\ell$, $\ell^{2} = \tfrac{3}{\Lambda}$. Under the action as written, $\Lambda$ is a parameter of the laws, not initial data. \emph{Provenance:} \cite[Thm.~4.7, Prop.~4.10, Prop.~4.4]{ButlerT6}; \cite[Fact~2.1, Thm.~3.1, Prop.~5.8]{ButlerT10}.

## technical
On the Einstein region with $\Lambda > 0$ of a gravitational field on flat spacetime, the scale tractor $I$, parallel for the tractor gauge field, has $Q(I) = \Lambda/3$, its stabiliser is the de Sitter group $SO(1,4)$, and $I^\perp$ carries the induced form of signature $(1,4)$; the flat-model section is the de Sitter hyperboloid of radius $\ell$, $\ell^2 = 3/\Lambda$. Under the action as written, $\Lambda$ is a parameter of the laws, not initial data. The fact restates results proved earlier in the series.

## lay
This fact carries over earlier results about the frozen point on the region where Einstein's equations hold for the gravitational fields on flat spacetime, when the cosmological constant is positive. Its length is set by the cosmological constant, the symmetries that preserve it form the de Sitter group, and the matching model space is de Sitter space, with radius fixed by the same constant. Under the action as written, the cosmological constant is a setting of the laws, not an initial condition.

## one-liner
On the Einstein region with $\Lambda > 0$ of a gravitational field on flat spacetime the frozen point has $Q(I) = \Lambda/3$ and stabiliser $SO(1,4)$, the model section is the de Sitter hyperboloid of radius $\sqrt{3/\Lambda}$, and under the action as written $\Lambda$ is a parameter of the laws.
