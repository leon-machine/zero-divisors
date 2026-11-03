---
id: primer.sign
kind: claim
version: 2
title: The sign of $\omega^2$
status: proved
region: primer
programme: standard
subject: standard-algebra
tags: [pseudoscalar-and-centre]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T00, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_omega_square
- kind: check
  ref: check.py::check_exponent_parity_identity
locators:
  paper: T00
  number: Lem 9.5
  label: tk:omegasq
  line: 502
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: omega^2 against both closed forms for 1 <= n <= 10 and the exponent identity. Version 1 -> 2.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: Self-contained proof in the source; no edges.
payload:
- kind: identity
  clause: omega^2 closed forms
  python: 'all(omega_sq(p, n - p) == {(): F((-1) ** (n * (n - 1) // 2) * (-1) ** (n - p))} and (-1) **
    (n * (n - 1) // 2 + n - p) == (-1) ** ((2 * p - n) * (2 * p - n - 1) // 2) for n in range(1, 9) for
    p in range(n + 1))'
  note: omega^2 = (-1)^(n(n-1)/2) (-1)^q = (-1)^((p-q)(p-q-1)/2), every signature with n <= 8
- kind: classification
  clause: in particular
  python: all(((-1) ** ((p - q) * (p - q - 1) // 2) == 1) == ((p - q) % 4 in (0, 1)) for p in range(16)
    for q in range(16))
  note: omega^2 = +1 iff p - q = 0 or 1 mod 4 (the exponent depends on p - q mod 4 only)
---

## formal
$\displaystyle \omega^2 = (-1)^{\tfrac{n(n-1)}{2}} (-1)^q = (-1)^{\tfrac{(p-q)(p-q-1)}{2}}$. In particular $\omega^2 = +1$ if and only if $p - q \equiv 0$ or $1 \pmod 4$.

## technical
For the pseudoscalar $\omega = e_1 \cdots e_n$ of $\Cl(p,q)$, with $n = p + q$, reversing the $n$ factors costs $(-1)^{n(n-1)/2}$, and $\omega$ times its reverse collapses to the product of the $Q(e_i)$, which is $(-1)^{q}$. Hence $\omega^{2} = (-1)^{n(n-1)/2}(-1)^{q}$.

A parity count shows this depends only on $p - q$: $\omega^{2} = (-1)^{(p-q)(p-q-1)/2}$, so $\omega^{2} = +1$ exactly when $p - q \equiv 0$ or $1 \pmod 4$.

## lay
Multiplying all the basis directions of a Clifford algebra together gives a special element called the pseudoscalar. Its square is always plus one or minus one, and this result says which. The answer depends only on the number of positive directions minus the number of negative ones: plus one when that difference leaves remainder 0 or 1 on division by four, and minus one otherwise.

## one-liner
The pseudoscalar of $\Cl(p,q)$ satisfies $\omega^{2} = (-1)^{(p-q)(p-q-1)/2}$, so $\omega^{2} = +1$ exactly when $p - q \equiv 0$ or $1 \pmod 4$.
