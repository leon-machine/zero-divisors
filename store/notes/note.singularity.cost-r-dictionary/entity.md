---
id: note.singularity.cost-r-dictionary
kind: note
version: 2
title: The cost of (R), and the dictionary
status: remark
subject: thermality
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
comments_on:
- singularity.why-calibration-cannot-be-internal
- singularity.euclidean-section-period
- singularity.exact-equilibrium-over-determines-boundary-modes
- singularity.two-kms-functionals-sign
locators:
  paper: T05
  number: Rem 7.26
  label: rem:priceR
  line: 1940
extraction:
  source_title: 'The cost of (R), and the dictionary'
  source_formal: |-
    (R) is not derived from the transport principle, and Proposition \claimref{singularity.why-calibration-cannot-be-internal} says why it cannot be, so the correct reading is that the chain has localised the last import of its state selection rather than removed it (Step 4e's (Q) is a further import, separately recorded, for the Planck sector alone). It is the same import every derivation of the Hawking temperature makes: Euclidean regularity at the bifurcation point \cite{GibbonsHawking1977, HartleHawking1976}, regularity on the future horizon \cite{Unruh1976}, nonsingularity of the quasi-free state \cite{KayWald1991}, the short-distance condition on the state near the horizon \cite{FredenhagenHaag1990}. What the chain contributes is smaller and exact: the period is computed from the section rather than chosen (Proposition \claimref{singularity.euclidean-section-period}); the premise is imposed on the marginals, mode by mode, because Theorem \claimref{singularity.exact-equilibrium-over-determines-boundary-modes} shows that its joint form destroys the correlations the chain needs; the sign of the statistics is located in the algebra (Proposition \claimref{singularity.two-kms-functionals-sign}); and the premise's irreducibility is a theorem (Theorem \claimref{singularity.rate-rigidity-temperature-not-algebra-intrinsic}). It does not supply the premise with a location inside the curvature: Proposition \claimref{singularity.euclidean-rotor-where-it-lies}(3) shows that the Euclidean rotation is not a member of the curvature-selected pair.

    The dictionary against the standard alternatives, now as points of an explicitly parametrised line rather than incommensurable constructions: $\beta_k = \infty$ at every mode is the Boulware analogue \cite{Boulware1975}, unoccupied boundary modes with a pure descended state, zero deficit by Theorem \claimref{singularity.deficit-theorem-cost-descent-exactly} and no flux, excluded by (R); $\beta_k = 2\pi/\kappa$ at every mode is the Hartle-Hawking and Unruh analogue, selected by (R), the product member of that class being the (G) state; $\beta_k$ finite but varying in $k$ is excluded by (R) at the offending modes, and has no geometric modular flow by Corollary \claimref{singularity.universality-temperature-under-g}; $\beta_k = 0$ is the tracial state, excluded with the other boundary case.

    One route to a better-placed premise is worth recording, because it is not the one the singular side offers. The Bisognano-Wichmann theorem does not assume the factor $2\pi$: it derives it, from the spectrum condition together with covariance and locality \cite{BW1976, Sewell1982}. The ascent of Step 3 lands in $\Cl(2,4)$, the conformal algebra, whose parabolic stabiliser of $\nInf$ contains exactly the translations such a spectrum condition needs, so the premise could be restated as positivity of the energy of the boundary modes with respect to a generator the ascent itself installed, rather than as smoothness of a Euclidean section. That would still be an import, positivity of energy being no Clifford fact, but it would be stated in the algebra the chain produces. Transcribing the theorem needs an action of the relevant subgroup on the boundary modes, a wedge and locality structure, and analyticity of the state, each of which is genuine work and any of which could fail; the item belongs with the twistor correspondence T9 \cite{ButlerT9} rather than here.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'One phrase converted: T9 is named as the correspondence paper on the conformal spinor space of $\Cl(2,4)$ rather than as the twistor correspondence.'
---

## formal
(R) is not derived from the transport principle, and Proposition \claimref{singularity.why-calibration-cannot-be-internal} says why it cannot be, so the correct reading is that the chain has localised the last import of its state selection rather than removed it (Step 4e's (Q) is a further import, separately recorded, for the Planck sector alone). It is the same import every derivation of the Hawking temperature makes: Euclidean regularity at the bifurcation point \cite{GibbonsHawking1977, HartleHawking1976}, regularity on the future horizon \cite{Unruh1976}, nonsingularity of the quasi-free state \cite{KayWald1991}, the short-distance condition on the state near the horizon \cite{FredenhagenHaag1990}. What the chain contributes is smaller and exact: the period is computed from the section rather than chosen (Proposition \claimref{singularity.euclidean-section-period}); the premise is imposed on the marginals, mode by mode, because Theorem \claimref{singularity.exact-equilibrium-over-determines-boundary-modes} shows that its joint form destroys the correlations the chain needs; the sign of the statistics is located in the algebra (Proposition \claimref{singularity.two-kms-functionals-sign}); and the premise's irreducibility is a theorem (Theorem \claimref{singularity.rate-rigidity-temperature-not-algebra-intrinsic}). It does not supply the premise with a location inside the curvature: Proposition \claimref{singularity.euclidean-rotor-where-it-lies}(3) shows that the Euclidean rotation is not a member of the curvature-selected pair.

The dictionary against the standard alternatives, now as points of an explicitly parametrised line rather than incommensurable constructions: $\beta_k = \infty$ at every mode is the Boulware analogue \cite{Boulware1975}, unoccupied boundary modes with a pure descended state, zero deficit by Theorem \claimref{singularity.deficit-theorem-cost-descent-exactly} and no flux, excluded by (R); $\beta_k = 2\pi/\kappa$ at every mode is the Hartle-Hawking and Unruh analogue, selected by (R), the product member of that class being the (G) state; $\beta_k$ finite but varying in $k$ is excluded by (R) at the offending modes, and has no geometric modular flow by Corollary \claimref{singularity.universality-temperature-under-g}; $\beta_k = 0$ is the tracial state, excluded with the other boundary case.

One route to a better-placed premise is worth recording, because it is not the one the singular side offers. The Bisognano-Wichmann theorem does not assume the factor $2\pi$: it derives it, from the spectrum condition together with covariance and locality \cite{BW1976, Sewell1982}. The ascent of Step 3 lands in $\Cl(2,4)$, the conformal algebra, whose parabolic stabiliser of $\nInf$ contains exactly the translations such a spectrum condition needs, so the premise could be restated as positivity of the energy of the boundary modes with respect to a generator the ascent itself installed, rather than as smoothness of a Euclidean section. That would still be an import, positivity of energy being no Clifford fact, but it would be stated in the algebra the chain produces. Transcribing the theorem needs an action of the relevant subgroup on the boundary modes, a wedge and locality structure, and analyticity of the state, each of which is genuine work and any of which could fail; the item belongs with the correspondence paper T9 \cite{ButlerT9}, on the conformal spinor space of $\Cl(2,4)$, rather than here.

## technical
pending

## lay
pending

## one-liner
pending
