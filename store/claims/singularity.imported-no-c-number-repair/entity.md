---
id: singularity.imported-no-c-number-repair
kind: claim
version: 5
title: 'Imported: no c-number repair'
status: proved
region: singularity
subject: zero-divisors
tags: [no-go, null-directions, rotors-and-stabilisers]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
about:
- obj.transport.equivariance
derivations:
- name: main
  uses:
  - sheaf.no-equivariant-value-wall@5
  - transport.cohomological-form-no-go@4
  - transport.no-go-level-elements@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_partners_form_affine_space_over_u
- kind: check
  ref: check.py::check_null_rotations_translate_partners
- kind: check
  ref: check.py::check_dimension_two_exception
- kind: check
  ref: check.py::check_wall_translation_action
locators:
  paper: T05
  number: Fact 5.4
  label: thm:nocnumber
  line: 1559
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: partners of a null v form an affine space over U translated by null rotations (also in the ascent), the dimension-two exception, and the wall translation action. Version 4 -> 5.'
  env: fact
  context_refs:
  - sheaf.no-equivariant-value-wall
  - singularity.imported-no-equivariant-value-wall
  - singularity.pseudo-inverse-identities-hyperbolic-atom
  - singularity.type-n-only-type-n
  - transport.cohomological-form-no-go
  - transport.no-go-level-elements
  - transport.totality
  flags:
  - 'fact restating several series results: derived from them'
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    - transport.totality
    note: Removed the mechanically added transport-algorithm edge (the import is a no-go, not a step of
      the algorithm) and totality, which the provenance lists but no clause relies on; the hyperbolic-atom
      lemma and the type-N-at-E proposition are comparison and scope, so not added.
---

## formal
No equivariant assignment of classical partner values to the dying directions exists, in the minimal ascent or in any enlargement. Mechanism: the stabiliser of the null direction $[v]$ contains the parabolic null rotations, the candidate partners form an affine space on which those rotations act by translation, and a translation of an affine space has no fixed point; cohomologically, the obstruction is the tautological class of the unipotent stabiliser, nonzero in every mixed-signature dimension above two. \emph{Provenance:} the element-level no-go is \cite[Thm.~4.2]{ButlerT1}; the totality of the transported division is \cite[Thm.~4.10]{ButlerT1}; the cohomological form, with the torsor made exact modulo the left ideal and the class identified as $\theta \in H^1(N_v; U) = \operatorname{Hom}(N_v, U)$, is \cite[Thm.~4.8]{ButlerT1}. The dimension-two exception, where the class vanishes, is exactly Lemma \claimref{singularity.pseudo-inverse-identities-hyperbolic-atom}'s self-completeness. \emph{Scope:} these theorems are proved where the ambient form is nondegenerate and the dying direction has a hyperbolic partner, which is the situation at every point of the invertible region, whose limits toward $E$ the no-go therefore governs; at $E$ itself the partner is exactly what is missing (Proposition \claimref{singularity.type-n-only-type-n}), so the import does not apply there verbatim. The boundary case is supplied by the no-value theorem at the wall, \cite[Thm.~10.4]{ButlerT4}, reproduced verbatim as Fact \claimref{singularity.imported-no-equivariant-value-wall}: no equivariant classical value exists at $E$ either, the completion's own transversal-independence carrying the equivariance. The claim that no classical value can repair the dying directions therefore holds on the approach by \cite[Thm.~4.2]{ButlerT1} and at the boundary by Fact \claimref{singularity.imported-no-equivariant-value-wall}.

## technical
Imported from the root and sheaf papers. No equivariant assignment of classical partner values to the dying directions exists, in the minimal ascent or in any enlargement. The mechanism: the stabiliser of the null direction $[v]$ contains the parabolic null rotations, the candidate partners form an affine space on which those rotations act by translation, and a translation of an affine space has no fixed point. Cohomologically, the obstruction is the tautological class $\theta \in H^1(N_v; U) = \mathrm{Hom}(N_v, U)$, nonzero in every mixed-signature dimension above two.

The element-level theorems need a nondegenerate ambient form and a hyperbolic partner for the dying direction. That holds at every point of the invertible region, so they govern the limits towards the singular locus $E$; at $E$ itself the partner is missing, and the no-value theorem at the wall supplies the boundary case. Together they bar a classical repair on the approach and at the boundary.

## lay
Near the black-hole singularity some directions lose their length altogether. This result, carried over from earlier papers in the series, says that no ordinary number can be assigned as a partner to such a direction in a way that respects the symmetries: the symmetries shift every candidate, so none is left in place. A separate theorem covers the singularity itself, where the usual argument does not apply directly.

## one-liner
No equivariant classical partner value for the dying directions exists, on the approach to the singular locus by the element-level and cohomological no-go and at the locus itself by the no-value theorem at the wall.
