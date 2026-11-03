---
id: hawking.imported-kms-passes-inductive-limits
kind: claim
version: 1
title: 'Imported: KMS passes to inductive limits'
status: imported
region: hawking
subject: descent
tags: [classical-theorem, modular-theory, limits]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
review: typed
imported_from:
- citation: O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd
    ed., Springer, Berlin (1997).
  key: BratteliRobinson1997
  locator: Prop.~5.3.25
locators:
  paper: T07
  number: Fact 3.4
  label: fact:limitkms
  line: 477
extraction:
  env: fact
  typing:
    by: ai-typing-pass
    note: 'Imported fact with no derivation; nothing to edge. Levels pass: conditions already kept.'
---

## formal
Let a C*-algebra be the closure of an increasing union of subalgebras, each globally invariant under a one-parameter dynamics, and let a state be KMS at $\beta$ on each subalgebra for the restricted dynamics. Then the state is KMS at $\beta$ on the whole algebra: the analytic-element requirement is checked on the dense union and passes to the closure. \emph{Provenance:} \cite[Prop.~5.3.25]{BratteliRobinson1997}.

## technical
Suppose a C*-algebra is the closure of an increasing union of subalgebras, each globally invariant under a one-parameter dynamics, and a state is KMS at inverse temperature $\beta$ on each subalgebra for the restricted dynamics. Then the state is KMS at $\beta$ on the whole algebra: the analytic-element requirement is checked on the dense union and passes to the closure. This is a standard result of operator-algebraic statistical mechanics, imported from the literature.

## lay
Thermal equilibrium, in its precise algebraic form, can be checked piece by piece. If a large system is the limit of an increasing chain of smaller subsystems, each preserved by the time evolution, and a state is in equilibrium on every one of them, then it is in equilibrium on the whole system. This is a known result taken from the literature.

## one-liner
A state that is KMS at $\beta$ on each subalgebra of an increasing chain of dynamics-invariant subalgebras is KMS at $\beta$ on the closure of their union.
