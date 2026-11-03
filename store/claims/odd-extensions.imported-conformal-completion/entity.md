---
id: odd-extensions.imported-conformal-completion
kind: claim
version: 5
title: 'Imported: the conformal completion'
status: proved
region: odd-extensions
subject: completion
tags: [conformal-spinors, conformal-model]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
review: typed
derivations:
- name: main
  uses:
  - correspondence.imported-forced-completion-fibre-quadric@6
  - correspondence.spinor-identification@7
  - standard-model.imported-fock-representation-clifford-algebra-bogoliubov@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_shadow_completes_one_rung_up
- kind: check
  ref: check.py::check_conformal_spinor_space_is_c4_with_unit_i6
- kind: check
  ref: check.py::check_spin_group_acts_through_even_subalgebra
locators:
  paper: T14a
  number: Fact 1.4
  label: fact:conformal
  line: 419
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: about the core definitions it is stated in. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: shadow (t,s) completes to (t+1,s+1), CS = Cl^0(2,4) P is C^4 with complex unit I6, and Cl^0(2,4) acts faithfully on it. Version 3 -> 4.'
  env: fact
  context_refs:
  - correspondence.imported-forced-completion-fibre-quadric
  - correspondence.spinor-identification
  - standard-model.imported-fock-representation-clifford-algebra-bogoliubov
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: All three uses match the cited correspondence and lepton-paper results; the general (t,s) clause
      is carried by the cited forced-completion Fact rather than by root-paper minimality directly. E204
      is inherited from the spinor identification, outside this list.
  source_title: 'Imported: the conformal completion'
  source_formal: |-
    A shadow of signature $(t,s)$ has conformal completion with ambient of signature $(t+1, s+1)$, one rung up its own tower; for this world the ambient is $(2,4)$ and its conformal spin group acts on the twistor space $\C^{4}$ through $\Cl^{0}(2,4)$. \emph{Provenance:} \cite[Fact~2.1, Thm.~3.4]{ButlerT9}; \cite[Fact~2.11]{ButlerT12}.
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted twistor space $\C^4$ to the conformal spinor space $\CS \cong \C^4$ over $I_6$ in every level and the restated proof.'
about:
- obj.std-algebra.conformal-algebra
---

## formal
A shadow of signature $(t,s)$ has conformal completion with ambient of signature $(t+1, s+1)$, one rung up its own tower; for this world the ambient is $(2,4)$ and its conformal spin group acts on the conformal spinor space $\CS \cong \C^{4}$ (twistor space), whose complex unit is $I_6$, through $\Cl^{0}(2,4)$. \emph{Provenance:} \cite[Fact~2.1, Thm.~3.4]{ButlerT9}; \cite[Fact~2.11]{ButlerT12}.

## technical
A shadow of signature $(t,s)$ has a conformal completion whose ambient has signature $(t+1,s+1)$, one rung up its own tower. For this world the ambient signature is $(2,4)$, and its conformal spin group acts on the conformal spinor space $\CS \cong \C^4$, with complex unit $I_6$, through the even subalgebra $\Cl^0(2,4)$.

The statement restates earlier series results on the forced completion, the spinor identification and the Fock representation of a Clifford algebra.

## lay
A space-time of any signature can be enlarged by one extra direction of each kind, its conformal completion, which is the next step up its own ladder of algebras. For our four-dimensional world this gives a six-dimensional space with two time directions, whose spin symmetries act on a four-dimensional space of spinors whose complex unit is the algebra's own pseudoscalar.

## one-liner
A shadow of signature $(t,s)$ completes conformally to an ambient of signature $(t+1,s+1)$, which for this world is $(2,4)$, with its conformal spin group acting on the conformal spinor space $\CS \cong \C^4$ through $\Cl^0(2,4)$.
