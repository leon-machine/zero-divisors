---
id: transport.existence-classification-type-c
kind: claim
version: 4
title: Existence and classification of type C
status: proved
region: transport
subject: zero-divisors
tags: [obstruction-types, idempotents, pseudoscalar-and-centre, grading-and-parity]
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
review: typed
about:
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - transport.centre@4
  - transport.classification-real-clifford-algebras@3
  - transport.sign@3
  - std-algebra.involution-properties@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:3.6
- kind: check
  ref: check.py::check_type_c_iff_p_minus_q_one_mod_four
- kind: check
  ref: check.py::check_eps_pm_identities_and_exchange
- kind: check
  ref: check.py::check_splitting_into_two_ideals
locators:
  paper: T01
  number: Thm 3.6
  label: thm:typeC
  line: 608
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.involution-properties where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: on all 35 (p,q) with n <= 7 the centre is computed blade-wise and its idempotents solved: a nontrivial central idempotent exists iff p - q = 1 mod 4; eps_+- identities, exchange by the grade involution, fixed by conjugation; the two ideals of dimension 2^(n-1) with one-dimensional centres. Version 2 -> 3.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: "kept all three edges; the centre and sign lemmas drive the existence proof and the classification supplies the simplicity of the two ideals asserted in the statement"
---

## formal
$\Cl(p,q)$ ($n \geq 1$) contains a nontrivial central idempotent if and only if
\[
p - q \equiv 1 \pmod 4 ,
\]
and in that case the nontrivial central idempotents are exactly the two elements
\[
\varepsilon_\pm = \tfrac12\,(1 \pm \omega),
\]
which are exchanged by the grade involution $\hat{\cdot}$ (an \emph{outer} automorphism of the split algebra; no inner automorphism exchanges them, centrality being conjugation-invariant), and satisfy $\varepsilon_+ \varepsilon_- = 0$ and $\varepsilon_+ + \varepsilon_- = 1$, and effect the splitting $\Cl(p,q) = \varepsilon_+ A \,\oplus\, \varepsilon_- A$ into the two simple ideals of Theorem \claimref{transport.classification-real-clifford-algebras}.

## technical
A type C obstruction is a nontrivial central idempotent, so it must lie in the centre, which is $\R$ for even $n$ and $\R[\omega]$ for odd $n$. When $\omega^2 = -1$ that centre is a copy of $\C$, whose only idempotents are $0$ and $1$; when $\omega^2 = +1$ it is $\R \oplus \R$, with exactly two nontrivial idempotents $\varepsilon_\pm = \tfrac12(1 \pm \omega)$. Combining the parity of $n$ with the sign of $\omega^2$ shows that $\Cl(p,q)$, $n \geq 1$, has a nontrivial central idempotent if and only if $p - q \equiv 1 \pmod 4$.

In that case $\varepsilon_+ \varepsilon_- = 0$ and $\varepsilon_+ + \varepsilon_- = 1$, and $\Cl(p,q) = \varepsilon_+ A \oplus \varepsilon_- A$ is the splitting into two simple ideals. The grade involution sends $\omega \mapsto -\omega$ and so exchanges $\varepsilon_+$ and $\varepsilon_-$; it is an outer automorphism, because an inner automorphism fixes every central element and therefore cannot exchange them.

## lay
Some Clifford algebras secretly come in two independent halves, and the elements that pick out each half are called central idempotents. This result pins down exactly when that happens: precisely when the number of positive directions minus the number of negative ones leaves remainder 1 on division by four. In that case there are exactly two such elements, built from the product of all the basis directions. Reversing every direction swaps the two halves, but no conjugation by an element of the algebra itself can do so, since these elements commute with everything.

## one-liner
$\Cl(p,q)$, $n \geq 1$, has a nontrivial central idempotent exactly when $p - q \equiv 1 \pmod 4$, and then the only ones are $\varepsilon_\pm = \tfrac12(1 \pm \omega)$, which split the algebra into two simple ideals and are exchanged by the grade involution but by no inner automorphism.
