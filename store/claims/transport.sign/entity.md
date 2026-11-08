---
id: transport.sign
kind: claim
version: 3
title: The sign of $\omega^2$
status: proved
region: transport
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
derivations:
- name: main
  uses:
  - primer.sign@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:2.7
- kind: check
  ref: check.py::check_omega_square_closed_forms
- kind: check
  ref: check.py::check_reversal_sign_count
- kind: check
  ref: check.py::check_depends_only_on_p_minus_q
locators:
  paper: T01
  number: Lem 2.7
  label: lem:omegasq
  line: 541
extraction:
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'Re-reviewed: the single edge to the primer sign lemma it restates is kept; levels from the
      earlier pass kept.'
  repair:
    note: restatement of the T0 result primer.sign; derivation and proof text supplied by the store
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: omega^2 for every (p,q) with n <= 10 against both closed forms, the reversal sign count in GA, and dependence on p - q alone with residues {0, 1}. Version 2 -> 3.'
subject: clifford-structure
tags: [pseudoscalar-and-centre]
equivalent_to:
- primer.sign@3
---

## formal
$\displaystyle \omega^2 = (-1)^{\tfrac{n(n-1)}{2}} (-1)^q = (-1)^{\tfrac{(p-q)(p-q-1)}{2}}$. In particular $\omega^2 = +1$ if and only if $p - q \equiv 0$ or $1 \pmod 4$.

## technical
For the pseudoscalar $\omega = e_1 \cdots e_n$ of $\Cl(p,q)$, with $n = p + q$, the square is fixed by a count of signs: reversing the order of the $n$ generators costs $(-1)^{n(n-1)/2}$, and $\omega$ times its reverse is the product of the $Q(e_i)$, which is $(-1)^q$. Hence $\omega^2 = (-1)^{n(n-1)/2}(-1)^q$.

This depends only on $p - q$, namely $\omega^2 = (-1)^{(p-q)(p-q-1)/2}$, and in particular $\omega^2 = +1$ exactly when $p - q \equiv 0$ or $1 \pmod 4$.

## lay
Multiplying all the basis directions of a Clifford algebra together gives a special element called the pseudoscalar. Its square is always plus one or minus one, and this result says which. The answer depends only on the number of positive directions minus the number of negative ones: the square is plus one when that difference leaves remainder 0 or 1 on division by four, and minus one otherwise.

## one-liner
The pseudoscalar of $\Cl(p,q)$ satisfies $\omega^2 = (-1)^{(p-q)(p-q-1)/2}$, so $\omega^2 = +1$ exactly when $p - q \equiv 0$ or $1 \pmod 4$.
