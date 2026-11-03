---
id: neutrino.imported-indifference-faces-democratic-alignment-rank
kind: claim
version: 6
title: 'Imported: indifference, the faces, the democratic alignment, and the rank-one texture'
status: proved
region: neutrino
subject: generations
tags: [flavour-and-mixing, indifference]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T15, deposited version
review: typed
derivations:
- name: main
  uses:
  - families.alignment-computed-thirteenth-refutation-democracy-one@4
  - families.faces-ordered-what-identification-requires-first@3
  - families.imported-indifference-instrument@2
  assumes:
  - families.hyp-face-identification@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_democratic_line_and_invariant_forms
- kind: check
  ref: check.py::check_rank_one_spectrum
- kind: check
  ref: check.py::check_s3_protects_light_pair
- kind: proof
  derivation: main
locators:
  paper: T15
  number: Fact 2.3
  label: fact:democracy
  line: 562
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: S_3-fixed line and invariant forms span{1, J}; J of rank one with spectrum (3,0,0); S_3 keeps the light pair degenerate and an S_2 perturbation splits it. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6.'
  env: fact
  context_refs:
  - families.alignment-computed-thirteenth-refutation-democracy-one
  - families.faces-ordered-what-identification-requires-first
  - families.imported-indifference-instrument
  - families.three-generations-faces-maximal-composite
  outside_pilot_cites:
  - ButlerT12
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Kept the four restated families results as uses; the effective status is capped by the conjectural
      face identification, which the Fact itself declares, and the Standard-Model remark carrying the
      three-twistor bound has no separate store entry. Hypothesis pass: assumes families.hyp-face-identification
      added because it relies on the face identification, now a postulate, in place of a uses edge to
      the conjecture. Levels pass: lay now flags indifference as a premise, and the one-liner adds at
      leading order.'
    added:
    - families.hyp-face-identification
    removed:
    - families.three-generations-faces-maximal-composite
  source_title: 'Imported: indifference, the faces, the democratic alignment, and the rank-one texture'
  source_formal: |-
    The indifference instrument forbids uncaused structure (distinctions nothing in the framework determines); it is a structural premise of the series, not a theorem, and is flagged as such wherever it is used. The identification of the three generations with the three two-twistor faces of the maximal composite is the families paper's Conjecture 3.1, at conjectural level, and the maximality it invokes is the Standard-Model paper's three-twistor bound, imported there and here at the observation level that remark declares; the mass bracket is face-valued, one bracket per face, so a vacuum is a direction in the three-dimensional face space, and its alignment is what breaks $S_{3}$ (structural level). Under the instrument the condensate's source lies on the democratic line spanned by $u = (1,1,1)/\sqrt{3}$, and, under the Gram-square reading of the leading mass form, the leading Yukawa form is $Y_{0} \propto \J = u'u'^{\mathsf{T}}$ with $u' = (1,1,1)$ and $\J$ the $3 \times 3$ all-ones matrix, of spectrum $(3, 0, 0)$: one heavy family and two light at leading order, lifted by the second-order breaking $S_{3} \to S_{2} \to 1$ that converts the CKM shape into CKM numbers. \emph{Provenance:} \cite[Fact~2.5, Conj.~3.1, Prop.~4.3, Prop.~4.4(1)]{ButlerT13}, each at the level stated there; \cite[Rem.~3.3]{ButlerT12} for the three-twistor bound, at observation level.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'The faces and the bound are now named by conformal spinors (two-spinor faces, three-spinor bound) in the statement and its restated proof; nothing else was in twistor form.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - families.hyp-face-identification
---

## formal
The indifference instrument forbids uncaused structure (distinctions nothing in the framework determines); it is a structural premise of the series, not a theorem, and is flagged as such wherever it is used. The identification of the three generations with the three two-spinor faces (pairs of conformal spinors) of the maximal composite is the families paper's Conjecture 3.1, at conjectural level, and the maximality it invokes is the Standard-Model paper's three-spinor bound, imported there and here at the observation level that remark declares; the mass bracket is face-valued, one bracket per face, so a vacuum is a direction in the three-dimensional face space, and its alignment is what breaks $S_{3}$ (structural level). Under the instrument the condensate's source lies on the democratic line spanned by $u = (1,1,1)/\sqrt{3}$, and, under the Gram-square reading of the leading mass form, the leading Yukawa form is $Y_{0} \propto \J = u'u'^{\mathsf{T}}$ with $u' = (1,1,1)$ and $\J$ the $3 \times 3$ all-ones matrix, of spectrum $(3, 0, 0)$: one heavy family and two light at leading order, lifted by the second-order breaking $S_{3} \to S_{2} \to 1$ that converts the CKM shape into CKM numbers. \emph{Provenance:} \cite[Fact~2.5, Conj.~3.1, Prop.~4.3, Prop.~4.4(1)]{ButlerT13}, each at the level stated there; \cite[Rem.~3.3]{ButlerT12} for the three-spinor bound, at observation level.

## technical
This Fact gathers four results of the families programme, each at its stated level. The indifference instrument, a structural premise rather than a theorem, forbids distinctions that nothing in the framework determines. The three generations are identified with the three two-spinor faces of the maximal composite (a conjecture), the maximality resting on a three-spinor bound held at observation level; the mass bracket is face-valued, so a vacuum is a direction in the three-dimensional face space and its alignment is what breaks $S_{3}$.

Under the instrument the condensate's source lies on the democratic line spanned by $u = (1,1,1)/\sqrt{3}$, and under the Gram-square reading of the leading mass form, $Y_{0} \propto \J = u'u'^{\mathsf{T}}$ with $u' = (1,1,1)$, of spectrum $(3,0,0)$: one heavy family and two light at leading order, lifted by the second-order breaking $S_{3} \to S_{2} \to 1$.

## lay
The framework adopts a rule, as a premise rather than a theorem, that it may not build in distinctions that nothing explains. Applied to three families pictured as three equivalent pairs inside a three-part object, the rule says the vacuum must at first treat all three alike. If the leading masses come from squaring that evenly weighted direction, one family is heavy and two are massless at first order, with smaller effects later separating the light ones. Each step holds only at the level the earlier work stated, and the family picture itself is still a conjecture.

## one-liner
Under the indifference premise, the conjectural face picture of the families and the Gram-square reading, the leading Yukawa form is democratic, proportional to the all-ones matrix, giving one heavy and two light families at leading order.
