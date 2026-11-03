---
id: rungs.imported-ladder-automorphism-group-no-lepton
kind: claim
version: 4
title: 'Imported: the ladder, the automorphism group, and the no-lepton clause'
status: proved
region: rungs
subject: standard-model
tags: [gauge-fields, representation-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-rungs, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - standard-model.global-form-quotient-determined@3
  - standard-model.internal-symmetry-ladder@3
  - standard-model.quarks-leptons-two-level-fermion-content@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_mixings_preserving_momentum_and_helicity_are_unitary
- kind: check
  ref: check.py::check_automorphism_algebras_and_cosets
- kind: check
  ref: check.py::check_tensor_ledger_has_no_lepton_doublet
locators:
  paper: T12-rungs
  number: Fact 1.5
  label: fact:ladder
  line: 217
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: unitary mixings preserving momentum and helicity at sample configurations (non-unitary ones failing), automorphism algebras of dimension 12 and 17 with the determinant section, and no (2,1) in the tensor ledger. Version 3 -> 4.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the n-twistor system and C^n (x) T to n conformal spinors and C^n (x) S at every level and in the provenance proof. The unitary groups and hierarchy C^2 (x) C^3 are kept as they are.'
  source_title: |-
    Imported: the ladder, the automorphism group, and the no-lepton clause
  source_formal: |-
    The mixings of an $n$-twistor system preserving momentum and helicity for every configuration are exactly $U(n)$, acting on the $n$-tuple $(Z^{1}, \ldots, Z^{n}) \in \C^{n} \otimes \T$ as $U \otimes 1$; the automorphism group of the hierarchy $\C^{2} \otimes \C^{3}$ is $(U(2) \times U(3))/K \cong S(U(2) \times U(3))$, and that of $\C^{3} \otimes \C^{3}$ has Lie algebra $\su(3) \oplus \su(3) \oplus \uu(1)$, dimension seventeen; the tensor ledger $\Lambda^{\bullet}(\C^{2} \otimes \C^{3})$ contains no $(2,1)$. \emph{Provenance:} \cite[Prop.~3.1, Thms.~4.1, 4.2, Prop.~5.3(2)]{ButlerT12}.
  env: fact
  context_refs:
  - standard-model.gauge-algebra-minimal-massive-composite
  - standard-model.global-form-quotient-determined
  - standard-model.internal-symmetry-ladder
  - standard-model.quarks-leptons-two-level-fermion-content
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Kept all four edges, which match the provenance list one for one; the fact restates them. Levels
      pass: no conditions to keep; the lay level now says the three-by-three algebra is seventeen-dimensional
      instead of ''too many symmetries'', which went beyond the formal.'
---

## formal
The mixings of a system of $n$ conformal spinors (an $n$-twistor system) preserving momentum and helicity for every configuration are exactly $U(n)$, acting on the $n$-tuple $(Z^{1}, \ldots, Z^{n}) \in \C^{n} \otimes \CS$, $\CS$ the conformal spinor space, as $U \otimes 1$; the automorphism group of the hierarchy $\C^{2} \otimes \C^{3}$ is $(U(2) \times U(3))/K \cong S(U(2) \times U(3))$, and that of $\C^{3} \otimes \C^{3}$ has Lie algebra $\su(3) \oplus \su(3) \oplus \uu(1)$, dimension seventeen; the tensor ledger $\Lambda^{\bullet}(\C^{2} \otimes \C^{3})$ contains no $(2,1)$. \emph{Provenance:} \cite[Prop.~3.1, Thms.~4.1, 4.2, Prop.~5.3(2)]{ButlerT12}.

## technical
Three results imported from the Standard Model paper. The mixings of $n$ conformal spinors that preserve momentum and helicity for every configuration are exactly $U(n)$, acting on the tuple $(Z^{1}, \ldots, Z^{n}) \in \C^{n} \otimes \CS$ as $U \otimes 1$. The automorphism group of the hierarchy $\C^{2} \otimes \C^{3}$ is $(U(2) \times U(3))/K \cong S(U(2) \times U(3))$, while that of $\C^{3} \otimes \C^{3}$ has Lie algebra $\su(3) \oplus \su(3) \oplus \uu(1)$, of dimension seventeen.

Finally, the tensor ledger $\Lambda^{\bullet}(\C^{2} \otimes \C^{3})$ contains no $(2,1)$: the exterior algebra of the hierarchy alone has no state with the $SU(2) \times SU(3)$ content of a lepton doublet.

## lay
This entry collects three earlier results that the rung note builds on. Rotations that mix a set of basic spinor states of the conformal algebra without changing their total momentum or helicity form the unitary group. The symmetry group of the two-by-three structure is the Standard Model's group, while the three-by-three structure has a larger symmetry algebra, of dimension seventeen. And the simplest state space built on the two-by-three structure has no room for a lepton doublet.

## one-liner
Imported: the mixings of $n$ conformal spinors preserving momentum and helicity are $U(n)$, the hierarchy $\C^{2} \otimes \C^{3}$ has automorphism group $S(U(2) \times U(3))$ while $\C^{3} \otimes \C^{3}$ has a seventeen-dimensional algebra, and the tensor ledger contains no $(2,1)$.
