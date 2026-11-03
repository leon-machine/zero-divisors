---
id: lepton.imported-duality-pair-system
kind: claim
version: 3
title: 'Imported: duality in the pair system'
status: proved
region: lepton
subject: standard-model
tags: [representation-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-lepton, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - lepton.imported-duality-pair-system-external@1
  - standard-model.imported-cauchy-decomposition-exterior-power@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_characters_match
- kind: check
  ref: check.py::check_equivariant_pairings
locators:
  paper: T12-lepton
  number: Fact 1.6
  label: fact:duality
  line: 200
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the dualities by characters and by the det-equivariant wedge pairings with compound matrices. Version 2 -> 3.'
  typing:
    by: ai-typing-pass
    note: Kept the series Cauchy-decomposition import and the external textbook entry, the two provenances
      the Fact cites.
  env: fact
  context_refs:
  - standard-model.imported-cauchy-decomposition-exterior-power
  flags:
  - 'fact restating several series results: derived from them'
---

## formal
As $U(3)$-modules, $(\Lambda^{k}W)^{*} \cong \Lambda^{3-k}W \otimes \det{}^{-1}$; as a $U(2)$-module, $(\C^{2})^{*} \cong \C^{2} \otimes \det{}^{-1}$. \emph{Provenance:} \cite[Fact~2.6]{ButlerT12}; \cite[\S 6.1, \S 15.3]{FultonHarris1991}.

## technical
Two dualities of representation theory are used. As $U(3)$-modules, the dual of an exterior power of $W = \C^{3}$ is the complementary power twisted by the inverse determinant, $(\Lambda^{k}W)^{*} \cong \Lambda^{3-k}W \otimes \det^{-1}$; as a $U(2)$-module, $(\C^{2})^{*} \cong \C^{2} \otimes \det^{-1}$.

Both are standard, taken from the series' Cauchy-decomposition import and the textbook treatment of exterior powers.

## lay
Taking the dual of a representation, which turns it inside out, gives back a familiar representation for these small symmetry groups, up to a determinant factor. In three complex dimensions the dual of the $k$-fold wedge products is the $(3-k)$-fold products; in two dimensions the dual is the space itself. These standard facts let particles be matched with antiparticles.

## one-liner
As $U(3)$-modules $(\Lambda^{k}W)^{*} \cong \Lambda^{3-k}W \otimes \det^{-1}$, and as a $U(2)$-module $(\C^{2})^{*} \cong \C^{2} \otimes \det^{-1}$.
