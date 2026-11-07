---
id: rule2.odd-lorentzian-dimension-exactly-one-real
kind: claim
version: 6
title: 'Odd Lorentzian dimension: exactly one real form is split'
status: proved
region: rule2
subject: clifford-structure
tags: [obstruction-types, clifford-classification, pseudoscalar-and-centre]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 6
  source: maintainer pass 2026-11-07 (GA units)
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - rule2.where-obstruction-sits-commuting-square@5
  - std-algebra.complexification@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T17_rule2.py
  tags:
  - label:cor:lorentz
- kind: check
  ref: check.py::check_real_forms_alternate
- kind: check
  ref: check.py::check_same_complexification_split
locators:
  paper: T17-rule2
  number: Cor 2.4
  label: cor:lorentz
  line: 177
outside_ga:
  kind: other
  why: 'the common complexification Cl(p,q) (x) C is the subject; its scalar i (in i omega and e_i -> i e_i) commutes with every vector, which no pseudoscalar does'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (other): the common complexification Cl(p,q) (x) C is the subject; its scalar i (in i omega and e_i -> i e_i) commutes with every vector, which no pseudoscalar does.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.complexification where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: centre and omega^2 of Cl(1,n-1) and Cl(n-1,1) for odd n <= 11 (type C alternation agreeing with the commuting-square theorem) and the common split complexification. Version 3 -> 4.'
  env: corollary
  typing:
    by: ai-typing-pass
    note: 'Kept the single edge to the commuting-square theorem, which the proof applies; the complexification
      step is self-contained. Linked equivalent_to transport.odd-lorentzian-dimension-exactly-one-real:
      the companion note restates it.'
equivalent_to:
- transport.odd-lorentzian-dimension-exactly-one-real@5
---

## formal
Let $n$ be odd and consider the two real forms of the Lorentzian algebra in dimension $n$, $\Cl(1,n{-}1)$ (time of square $+1$) and $\Cl(n{-}1,1)$ (time of square $-1$). Then $\Cl(1,n{-}1)$ is type C if and only if $n \equiv 1 \pmod 4$, $\Cl(n{-}1,1)$ is type C if and only if $n \equiv 3 \pmod 4$, and in each case the other real form has complex type. The two real forms have the same complexification, which is split for every odd $n$: over $\C$ the element $\omega' = \omega$ or $i\omega$, whichever has square $+1$, is central, and $\tfrac12(1 \pm \omega')$ are its central idempotents. Thus the obstruction is present in every odd Lorentzian dimension; the real form decides whether it is visible as a splitting or hidden as a central complex structure.

## technical
For odd $n$ compare the two Lorentzian real forms $\Cl(1,n-1)$, with $Q = +1$ on the time generator, and $\Cl(n-1,1)$, with $Q = -1$ on it. Using the commuting-square theorem on where the obstruction sits among one-dimensional extensions, $\Cl(1,n-1)$ is of type C if and only if $n \equiv 1 \pmod 4$, $\Cl(n-1,1)$ is of type C if and only if $n \equiv 3 \pmod 4$, and in each case the other real form has complex type.

Both forms have the same complexification, which is split for every odd $n$: over $\C$, whichever of $\omega$ and $i\omega$ squares to $+1$ is a central involution $\omega'$, and $\tfrac12(1 \pm \omega')$ are central idempotents. So the obstruction is present in every odd Lorentzian dimension, and the real form decides whether it appears as a splitting or as a central complex structure.

## lay
In an odd number of spacetime dimensions there are two ways to set up the algebra, depending on whether time is given a positive or a negative square. Exactly one of the two breaks into two pieces, and which one depends on the dimension modulo four; the other hides the same feature as a built-in square root of minus one. Over the complex numbers the two choices agree, and the result always splits.

## one-liner
In odd dimension $n$ exactly one of $\Cl(1,n-1)$ and $\Cl(n-1,1)$ is of type C, the first when $n \equiv 1$ and the second when $n \equiv 3 \pmod 4$, while their common complexification is always split.
