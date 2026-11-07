---
id: correspondence.imported-forced-completion-fibre-quadric
kind: claim
version: 6
title: 'Imported: the forced completion and its fibre quadric'
status: proved
region: correspondence
subject: completion
tags: [obstruction-types, no-go, forcing-and-uniqueness, conformal-model]
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
review: typed
about:
- obj.transport.obstruction-types
- obj.std-algebra.spacetime-algebra
- obj.std-algebra.conformal-algebra
derivations:
- name: main
  uses:
  - transport.minimality@4
  - transport.no-go-level-elements@5
  - transport.totality@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_type_n_zero_divisor_has_no_element_level_resolution
- kind: check
  ref: check.py::check_minimal_completion_is_cl24
- kind: check
  ref: check.py::check_assignments_on_null_quadric_of_r24
locators:
  paper: T09
  number: Fact 2.1
  label: fact:completion
  line: 323
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: about the core definitions it is stated in. Version 5 -> 6.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the transvection obstruction for e0 + e1 in Cl(1,3) and Cl(2,4), the completion Cl(2,4) with hyperbolic-plane complement, and the assignments on the null quadric. Version 3 -> 4. Fix round: check_minimal_completion_is_cl24 now tests minimality (no null-lift completion of dimension 0 or 1) besides the signature and the hyperbolic complement. Version 4 -> 5.'
  env: fact
  context_refs:
  - transport.minimality
  - transport.no-go-level-elements
  - transport.totality
  outside_pilot_cites:
  - ButlerT1
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: "The three uses are exactly the root-paper no-go, totality and minimality results the Fact cites; the representation-independent sharpening it also cites has no separate store entry."
---

## formal
Division by a type-N zero divisor in $\Cl(1,3)$ admits no element-level resolution (the transvection no-go), and the minimal completion resolving it is $\Cl(1,3) \hookrightarrow \Cl(2,4)$, unique up to isomorphism; the resolving assignments lie on the quadric of null rays of $\R^{2,4}$, the completion's point space. \emph{Provenance:} \cite[Thms.~4.2, 4.10, 4.13]{ButlerT1}; representation-independent minimality \cite[\S4.6]{ButlerT1}.

## technical
Division by a type-N zero divisor in the spacetime algebra $\Cl(1,3)$ has no element-level resolution: this is the transvection no-go. The minimal completion that resolves it is $\Cl(1,3) \hookrightarrow \Cl(2,4)$, adjoining one hyperbolic plane, and it is unique up to isomorphism.

The resolving assignments lie on the quadric of null rays of $\R^{2,4}$, which is the point space of the completion. The statement restates earlier series results on the no-go, on totality of the transported reciprocal and on minimality.

## lay
In the algebra of spacetime some elements cannot be divided by, and nothing done inside the algebra fixes this. The smallest enlargement that does fix it adds two dimensions, one space-like and one time-like, and this enlargement is unique. The repaired divisions live on the set of light-like directions of the resulting six-dimensional space.

## one-liner
Division by a type-N zero divisor in $\Cl(1,3)$ has no element-level resolution, its unique minimal resolving completion is $\Cl(1,3) \hookrightarrow \Cl(2,4)$, and the resolving assignments lie on the null quadric of $\R^{2,4}$.
