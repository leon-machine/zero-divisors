---
id: transport.odd-lorentzian-dimension-exactly-one-real
kind: claim
version: 5
title: 'Odd Lorentzian dimension: exactly one real form is split'
status: proved
region: transport
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
  source: authorship disclosure of T01, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 5
  source: maintainer pass 2026-11-07 (GA units)
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - transport.where-obstruction-lies-commuting-square@4
  - std-algebra.complexification@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:5.16
- kind: check
  ref: check.py::check_exactly_one_real_form_is_type_c
- kind: check
  ref: check.py::check_agrees_with_commuting_square_rule
- kind: check
  ref: check.py::check_common_complexification_is_split
locators:
  paper: T01
  number: Cor 5.16
  label: cor:lorentz
  line: 1341
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U3: the complexification Cl(p,q) (x) C of the odd-dimensional V is realised as Cl(V) + Cl(V) I_hatV inside the odd extension hatV of the even space V + R f, whose central pseudoscalar I_hatV squares to -1 and commutes with every vector (std-algebra.complexification-is-the-odd-extension, cited as a mention); i omega and e_i -> i e_i become I_hatV omega and e_k -> I_hatV e_k. No bare i remains, so the outside_ga declaration (other, for i only) is removed. Version kept, already bumped in this pass.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (other): the common complexification Cl(p,q) (x) C is the subject; its scalar i (in i omega and e_i -> i e_i) commutes with every vector, which no pseudoscalar does.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.complexification where the proof uses them. Version 3 -> 4.'
  env: corollary
  typing:
    by: ai-typing-pass
    note: Kept the single edge to the commuting-square theorem, which the proof applies; the complexification
      step is self-contained.
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: odd n <= 11, centre computed blade-wise, Cl(1,n-1) type C exactly at n = 5, 9 and Cl(n-1,1) at n = 3, 7, 11, agreement with the commuting-square rule, and the split common complexification. Version 2 -> 3.'
---

## formal
Let $n$ be odd and consider the two real forms of the Lorentzian algebra in dimension $n$, $\Cl(1,n{-}1)$ (time of square $+1$) and $\Cl(n{-}1,1)$ (time of square $-1$). Then $\Cl(1,n{-}1)$ is type C if and only if $n \equiv 1 \pmod 4$, $\Cl(n{-}1,1)$ is type C if and only if $n \equiv 3 \pmod 4$, and in each case the other real form has complex type. The two real forms have the same complexification, which is split for every odd $n$: over $\C$, realised as $\Cl(V) \oplus \Cl(V)I_{\hat V}$ with $V$ the $n$-dimensional space and $I_{\hat V}$ the central pseudoscalar of the odd extension $\hat V$ of $V \oplus \R f$ ($f$ one further vector), which squares to $-1$ and commutes with every vector (Theorem \claimref{std-algebra.complexification-is-the-odd-extension}), the element $\omega' = \omega$ or $I_{\hat V}\omega$, whichever has square $+1$, is central, and $\tfrac12(1 \pm \omega')$ are its central idempotents. Thus the obstruction is present in every odd Lorentzian dimension; the real form decides whether it is visible as a splitting or hidden as a central complex structure.

## technical
For odd $n$ compare the two Lorentzian real forms $\Cl(1,n-1)$, with $Q = +1$ on the time generator, and $\Cl(n-1,1)$, with $Q = -1$ on it. Using the commuting-square theorem on where the obstruction sits among one-dimensional extensions, $\Cl(1,n-1)$ is of type C if and only if $n \equiv 1 \pmod 4$, $\Cl(n-1,1)$ is of type C if and only if $n \equiv 3 \pmod 4$, and in each case the other real form has complex type.

Both forms have the same complexification, which is split for every odd $n$: over $\C$, with complex unit $I_{\hat V}$, the central pseudoscalar of an odd extension of $V \oplus \R f$, whichever of $\omega$ and $I_{\hat V}\omega$ squares to $+1$ is a central involution $\omega'$, and $\tfrac12(1 \pm \omega')$ are central idempotents. So the obstruction is present in every odd Lorentzian dimension, and the real form decides whether it appears as a splitting or as a central complex structure.

## lay
In an odd number of spacetime dimensions there are two ways to set up the algebra, depending on whether time is given a positive or a negative square. Exactly one of the two breaks into two pieces, and which one depends on the dimension modulo four; the other hides the same feature as a built-in square root of minus one. Over the complex numbers the two choices agree, and the result always splits.

## one-liner
In odd dimension $n$ exactly one of $\Cl(1,n-1)$ and $\Cl(n-1,1)$ is of type C, the first when $n \equiv 1$ and the second when $n \equiv 3 \pmod 4$, while their common complexification is always split.
