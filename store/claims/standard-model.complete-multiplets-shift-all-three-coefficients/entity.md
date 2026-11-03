---
id: standard-model.complete-multiplets-shift-all-three-coefficients
kind: claim
version: 3
title: Complete multiplets shift all three coefficients equally
status: proved
region: standard-model
subject: standard-model
tags: [running-and-unification, representation-theory]
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
  - standard-model.imported-coefficient-sum-indices@1
  - standard-model.imported-invariant-forms-simple-lie-algebra@1
  - standard-model.imported-one-loop-running-trace-ratio@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_invariant_form_is_unique
- kind: check
  ref: check.py::check_indices_equal_on_complete_multiplets
- kind: check
  ref: check.py::check_shifts_are_multiples_of_one_one_one
locators:
  paper: T12
  number: Lem 8.8
  label: lem:complete
  line: 1332
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the unique Weyl-invariant form on the Cartan of su(5), T_1 = T_2 = T_3 on nine SU(5) and Spin(10) representations, and the shifts c(1,1,1). Version 2 -> 3.'
  env: lemma
  context_refs:
  - standard-model.imported-one-loop-running-trace-ratio
  typing:
    by: ai-typing-pass
    added:
    - standard-model.imported-one-loop-running-trace-ratio
    note: Added the one-loop running fact, whose normalisation is a hypothesis of the lemma; the result
      is standard in unification but the paper does not say so here and no imported claim states it, so
      no standard-route derivation.
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.imported-one-loop-running-trace-ratio
---

## formal
Let $G_{U}$ be a simple group containing $S(U(2) \times U(3))$ in the normalisation of Fact \claimref{standard-model.imported-one-loop-running-trace-ratio}(b) (for definiteness $SU(5) \supset S(U(2) \times U(3))$, or $\mathrm{Spin}(10) \supset SU(5)$), and let $\rho$ be a representation of $G_{U}$ restricted to $S(U(2) \times U(3))$. Then $T_{1}(\rho) = T_{2}(\rho) = T_{3}(\rho)$, and content forming a representation of $G_{U}$ with a common threshold contributes a shift $\Dl = c\,(1, 1, 1)$ with $c = \tfrac23 T(\rho)$ for Weyl fermions and $\tfrac13 T(\rho)$ for complex scalars.

## technical
Let $G_{U}$ be a simple group containing $S(U(2) \times U(3))$ in the unification normalisation of one-loop running, such as $SU(5)$ or $\mathrm{Spin}(10)$, and $\rho$ a representation of $G_{U}$ restricted to $S(U(2) \times U(3))$. Then the three indices agree, $T_{1}(\rho) = T_{2}(\rho) = T_{3}(\rho)$: the three normalised generators have equal norm $\tfrac12$ on the fundamental $5$, and every invariant trace form on the simple algebra is a multiple of the Killing form.

Consequently content forming a representation of $G_{U}$ with a common threshold shifts the one-loop coefficients by $\Dl = c\,(1,1,1)$, with $c = \tfrac23 T(\rho)$ for Weyl fermions and $c = \tfrac13 T(\rho)$ for complex scalars.

## lay
The three forces of the Standard Model change strength with energy at rates set by the particles present. If new particles come as a complete family of a larger unifying symmetry, all entering at the same energy, they change the three rates by exactly the same amount. The size of that common change is fixed by a single number belonging to the family.

## one-liner
Complete multiplets of a simple unifying group containing $S(U(2) \times U(3))$ have equal indices on the three factors, so with a common threshold they shift all three one-loop coefficients by the same amount.
