---
id: rule2.imported-classification-centre-type-c
kind: claim
version: 3
title: 'Imported: classification, the centre, and type C'
status: proved
region: rule2
subject: clifford-structure
tags: [obstruction-types, pseudoscalar-and-centre, idempotents, grading-and-parity]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T17-rule2, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - rule2.imported-classification-centre-type-c-external@1
  - transport.centre@4
  - transport.classification-real-clifford-algebras@3
  - transport.existence-classification-type-c@4
  - transport.sign@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_even_simple_with_centre_r
- kind: check
  ref: check.py::check_odd_centre_and_square
- kind: check
  ref: check.py::check_central_idempotents
- kind: check
  ref: check.py::check_grade_involution_outer_and_ideals_simple
locators:
  paper: T17-rule2
  number: Fact 1.1
  label: fact:typeC
  line: 101
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: simplicity and centre for n even, centre R[omega] for n odd, central idempotents iff p - q = 1 mod 4, outer grade involution, simple ideals, n <= 8. Version 2 -> 3.'
  env: fact
  context_refs:
  - transport.centre
  - transport.classification-real-clifford-algebras
  - transport.existence-classification-type-c
  - transport.sign
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: All five edges are the restated series results and the external table; re-pinned transport.centre,
      transport.classification-real-clifford-algebras and transport.sign to their current version 2.
---

## formal
$\Cl(p,q)$ is simple for $n$ even, with centre $\R$. For $n$ odd the volume element is central, $\omega^2 = (-1)^{n(n-1)/2}(-1)^q$, and the centre is $\R[\omega]$: isomorphic to $\R \oplus \R$ when $\omega^2 = +1$ and to $\C$ when $\omega^2 = -1$. $\Cl(p,q)$ contains a nontrivial central idempotent if and only if $p - q \equiv 1 \pmod 4$, and then the nontrivial central idempotents are exactly $\varepsilon_\pm = \tfrac12(1 \pm \omega)$, exchanged by the grade involution, which is outer on the split algebra: no inner automorphism exchanges the two ideals $\varepsilon_\pm \Cl(p,q)$, each of which is simple. \emph{Provenance:} \cite[Thm.~2.5, Lemmas 2.6 and 2.7, Thm.~3.6]{ButlerT1}; the table itself is classical \cite{ABS1964, Lounesto2001}.

## technical
For even $n$, $\Cl(p,q)$ is simple with centre $\R$. For odd $n$, the volume element $\omega$ is central with $\omega^{2} = (-1)^{n(n-1)/2}(-1)^{q}$, and the centre $\R[\omega]$ is $\R \oplus \R$ when $\omega^{2} = +1$ and $\C$ when $\omega^{2} = -1$.

A nontrivial central idempotent exists if and only if $p - q \equiv 1 \pmod 4$, and then the nontrivial central idempotents are exactly $\varepsilon_\pm = \tfrac12(1 \pm \omega)$. They are exchanged by the grade involution, which is outer on the split algebra: no inner automorphism exchanges the two simple ideals $\varepsilon_\pm \Cl(p,q)$. These facts restate results proved earlier in the series; the table itself is classical.

## lay
This collects basic facts about the structure of real Clifford algebras. In even dimensions the algebra is a single indivisible block. In odd dimensions it may split into two identical blocks, which happens exactly when the number of positive directions minus the number of negative ones leaves remainder one on division by four. The two blocks can then be swapped by reversing the sign of every direction, but never by an internal change of viewpoint.

## one-liner
$\Cl(p,q)$ has a nontrivial central idempotent exactly when $p - q \equiv 1 \pmod 4$, namely $\tfrac12(1 \pm \omega)$, and its two simple ideals are exchanged only by the outer grade involution.
