---
id: mass.five-broken-generators
kind: claim
version: 6
title: The five broken generators
status: proved
region: mass
subject: mass
tags: [rotors-and-stabilisers, frozen-point, symmetry-breaking, conformal-spinors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
review: typed
derivations:
- name: main
  uses:
  - mass.de-sitter-scale-frozen-point@6
  - mass.imported-flat-model-twistor-chart-infinity@7
  - mass.imported-frozen-point-tractor-connection@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T11.py
  tags:
  - label:lem:five
- kind: check
  ref: check.py::check_omega_nondegenerate_iff_non_null
- kind: check
  ref: check.py::check_stabiliser_ten_complement_five
- kind: check
  ref: check.py::check_real_form_de_sitter_and_anti_de_sitter
locators:
  paper: T11
  number: Lem 5.8
  label: lem:five
  line: 796
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: det Omega_I = (Q(I)/2)^2, the stabiliser of dimension 10 and the 5-dimensional complement spanned by A(e_a ^ I), and the (1,4) / (2,3) real forms. Version 4 -> 5. Sample inputs moved to module level; no change to what is tested. Version 5 -> 6.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: lemma
  context_refs:
  - dark-energy.point-infinity-has-no-physical-fluctuation
  typing:
    by: ai-typing-pass
    added:
    - mass.imported-flat-model-twistor-chart-infinity
    note: 'The proof relies on the pairing on bivectors and the isomorphism defining $A(U\wedge V)$, both from the flat-model Fact, so that Fact was added; the action paper''s Goldstone count (context_ref) is a comparison and was not added.'
  source_title: 'The five broken generators'
  source_formal: |-
    Let $\Omega_{I}(u,v) := \ip{I}{u\wedge v}$ be the $2$-form on $\T$ of an ambient vector $I$; it is nondegenerate iff $I$ is non-simple iff $\ip{I}{I} \neq 0$. For such $I$, the elements $A \in \mathfrak{sl}(\T)$ with $\Omega_{I}A$ symmetric form the stabiliser of $I$, of dimension $10$ (six conditions on $\mathfrak{gl}(\T)$, none of which is the trace); the elements with $\Omega_{I}A$ antisymmetric form a $6$-dimensional complement in $\mathfrak{gl}(\T)$, cut to $5$ by the trace; and the five generators $A(e_{a}\wedge I)$, $e_{a}$ a basis of $I^{\perp}$, are an independent basis of that $5$-dimensional complement. On the real form, for the frozen point with $\Lambda > 0$, the stabiliser is $\mathfrak{so}(1,4)$ and the five are the de Sitter translations, the $I$-half of the nine Goldstone modes of the action paper \cite[Prop.~5.4]{ButlerT10}.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Twistor space \T is now the conformal spinor space \CS in all levels and in the proof (sl(CS), gl(CS), Lambda^2 CS); nothing was kept in twistor form.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - mass.imported-flat-model-twistor-chart-infinity
---

## formal
Let $\Omega_{I}(u,v) := \ip{I}{u\wedge v}$ be the $2$-form on the conformal spinor space $\CS$ (twistor space) of an ambient vector $I$; it is nondegenerate iff $I$ is non-simple iff $Q(I) \neq 0$. For such $I$, the elements $A \in \mathfrak{sl}(\CS)$ with $\Omega_{I}A$ symmetric form the stabiliser of $I$, of dimension $10$ (six conditions on $\mathfrak{gl}(\CS)$, none of which is the trace); the elements with $\Omega_{I}A$ antisymmetric form a $6$-dimensional complement in $\mathfrak{gl}(\CS)$, cut to $5$ by the trace; and the five generators $A(e_{a}\wedge I)$, $e_{a}$ a basis of $I^{\perp}$, are an independent basis of that $5$-dimensional complement. On the real form, for the frozen point with $\Lambda > 0$, the stabiliser is $\mathfrak{so}(1,4)$ and the five are the de Sitter translations, the $I$-half of the nine Goldstone modes of the action paper \cite[Prop.~5.4]{ButlerT10}.

## technical
An ambient vector $I$ defines a $2$-form $\Omega_{I}(u,v) = \ip{I}{u\wedge v}$ on the conformal spinor space $\CS$, nondegenerate exactly when $Q(I) \neq 0$. For such $I$, the elements $A \in \mathfrak{sl}(\CS)$ with $\Omega_{I}A$ symmetric form the stabiliser of $I$, of dimension $10$; those with $\Omega_{I}A$ antisymmetric form a $6$-dimensional complement in $\mathfrak{gl}(\CS)$, cut to $5$ by the trace, and the five generators $A(e_{a}\wedge I)$, $e_{a}$ a basis of $I^{\perp}$, are an independent basis of it.

On the real form, for the frozen point with $\Lambda > 0$, the stabiliser is $\mathfrak{so}(1,4)$ and the five broken generators are the de Sitter translations, the $I$-half of the nine Goldstone modes of the action principle.

## lay
The cosmological scale picks out a direction that breaks the conformal symmetry of spacetime down to de Sitter symmetry. Of the fifteen conformal symmetries ten survive and five are broken. This result identifies the five broken ones exactly: they are the de Sitter translations, the symmetries whose charges make up a composite's momentum.

## one-liner
For non-null $I$ the stabiliser in $\mathfrak{sl}(\CS)$ is $10$-dimensional and the five generators $A(e_{a}\wedge I)$, $e_{a} \in I^{\perp}$, span its $5$-dimensional complement, the de Sitter translations for the frozen point.
