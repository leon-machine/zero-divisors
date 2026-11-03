---
id: one-relation.imported-condensate-derived-content
kind: claim
version: 3
title: 'Imported: the condensate and the derived content'
status: proved
region: one-relation
subject: mass
tags: [frozen-point, symmetry-breaking]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
review: typed
about:
- obj.mass.grip-mass-composite
derivations:
- name: main
  uses:
  - families.alignment-computed-thirteenth-refutation-democracy-one@4
  - families.bracket-fixed-join@4
  - families.source-term-linear-tilt-mass-functional@4
  - mass.de-sitter-scale-frozen-point@6
  - mass.exact-join@7
  - mass.mass-weight-dictionary@4
  - standard-model.connection-forced@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_frozen_point_components_and_norm
- kind: check
  ref: check.py::check_klein_gordon_mass_is_minus_w_w_plus_3_lambda_over_3
locators:
  paper: T16
  number: Fact 2.6
  label: fact:condensate
  line: 525
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the frozen point''s flat-scale components and norm, and I.D(sigma^w phi) = -sigma^(w-1)(box_g + m^2)phi with m^2 = -w(w+3) Lambda/3 as an exact operator identity. Version 2 -> 3.'
  env: fact
  context_refs:
  - families.alignment-computed-thirteenth-refutation-democracy-one
  - families.bracket-fixed-join
  - families.source-term-linear-tilt-mass-functional
  - mass.de-sitter-scale-frozen-point
  - mass.exact-join
  - mass.mass-weight-dictionary
  - standard-model.connection-forced
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'All seven uses are the cited sources of this restating Fact and are kept; the condensation
      and minimal-coupling clauses stay at the observation level the sources declare. Levels pass: the
      one-liner now states the observation-level condensation reading, the indifference premise and the
      vacuum Einstein, Klein-Gordon level of the mass formula; the lay level adds the indifference premise,
      the background and the minimal-coupling reading.'
---

## formal
The condensate's bracket is fixed by the join, an identity that says nothing about a vacuum; that $\Lambda \neq 0$ tilts the potential so that condensation is not avoidable is a reading at observation level, under the assumption that the bracket and the vacuum area are independent variables; the alignment is democratic at structural level under the Gram-square reading, which rests on the indifference premise. Mass is the composite's grip on the frozen point (distinct from the frozen phase above: the series' name for the de Sitter scale tractor the cosmological constant fixes), quantified by the mass-weight dictionary at Klein-Gordon level: on a vacuum Einstein background with frozen point $I$, a density of conformal weight $w$ coupled by $I \cdot D\sigma = 0$ obeys, in the scale of $I$, $(\Box + m^{2})\sigma = 0$ with $m^{2} = -w(w+3)\Lambda/3$. The gauge content is derived with the connection forced by holonomy; the minimal coupling is that paper's observation-level reading of the forced connection. \emph{Provenance:} \cite[Prop.~4.1, Prop.~4.2(2), Prop.~4.3(3)]{ButlerT13}; \cite[Thm.~3.1, Lem.~5.1, Def.~5.4, Thm.~5.6]{ButlerT11}; \cite[Prop.~5.7 and the paragraph following it]{ButlerT12}.

## technical
Imported at the sources' declared levels. The condensate's bracket is fixed by the exact join, an identity that says nothing about a vacuum; that $\Lambda \neq 0$ tilts the potential so that condensation cannot be avoided is an observation-level reading, under the assumption that the bracket and the vacuum area are independent variables; and the alignment is democratic at structural level under the Gram-square reading, which rests on the indifference premise.

Mass is the composite's grip on the frozen point, quantified at Klein-Gordon level by the dictionary: on a vacuum Einstein background with frozen point $I$, a density of weight $w$ coupled by $I \cdot D\sigma = 0$ obeys $(\Box + m^{2})\sigma = 0$ with $m^{2} = -w(w+3)\Lambda/3$. The gauge content is derived with the connection forced by holonomy, and minimal coupling is an observation-level reading of that connection.

## lay
This collects earlier results on how mass arises, each at the strength it was established. The size of the mass-carrying bracket is fixed exactly, but whether a condensate actually forms is only a reading that rests on an assumption. The vacuum's alignment is democratic only under a reading that rests on the indifference premise. On an empty background obeying Einstein's equations, and at the level of the Klein-Gordon equation, mass is how a composite grips the cosmological scale, and the forces come from a connection the framework forces rather than chooses, though how matter couples to it is again a reading.

## one-liner
The condensate's bracket is fixed by the join, condensation is an observation-level reading under an independence assumption, the democratic alignment rests on the indifference premise, and on a vacuum Einstein background mass is the grip on the frozen point with $m^{2} = -w(w+3)\Lambda/3$ at Klein-Gordon level, the gauge content coming from the forced connection.
