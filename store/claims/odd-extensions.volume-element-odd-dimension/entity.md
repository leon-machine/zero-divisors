---
id: odd-extensions.volume-element-odd-dimension
kind: claim
version: 4
title: The volume element in odd dimension
status: proved
region: odd-extensions
subject: clifford-structure
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
  source: authorship disclosure of T14a, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, duplicate link at Leon''s decisions'
  version: 4
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  uses:
  - std-algebra.orthogonal-anticommute@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_odd_volume_element_central_with_square
- kind: check
  ref: check.py::check_n5_square_is_minus_one_to_q
- kind: check
  ref: check.py::check_even_control_not_central
locators:
  paper: T14a
  number: Lem 2.2
  label: lem:omega
  line: 433
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. Decision item E7 (routine; no retirement): specialises primer.sign@2 added. With specialises primer.centre@2: this lemma restates primer.centre and primer.sign for odd n, the primer entities being the general statements and homes.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.orthogonal-anticommute where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: omega central with omega^2 = (-1)^(n(n-1)/2+q) for all odd n <= 11, the n = 5 values, and the even-n control. Version 1 -> 2.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: Self-contained lemma with its own proof; it restates content of the primer's centre and sign
      lemmas, but the source proves it directly, so no edges added.
payload:
- kind: identity
  clause: n = 5
  python: 'all(GA.mul(omega_of(5), omega_of(5), GA.sig(p, 5 - p)) == {(): F((-1) ** (5 - p))} and all(GA.commutes(GA.gen(i),
    omega_of(5), GA.sig(p, 5 - p)) for i in range(5)) for p in range(6))'
  note: for n = 5, omega is central and omega^2 = (-1)^q, all six signatures
specialises:
- primer.centre@3
- primer.sign@3
---

## formal
For $n$ odd, $\omega$ is central in $\Cl(p,q)$ and $\omega^{2} = (-1)^{n(n-1)/2 + q}$. For $n = 5$ this is $\omega^{2} = (-1)^{q}$.

## technical
For odd $n = p + q$ the volume element $\omega = e_1 \cdots e_n$ commutes with every generator, since moving $e_i$ through it passes the $n - 1$ other factors, an even number; so $\omega$ is central. Its square is
$\omega^{2} = (-1)^{n(n-1)/2 + q}$: reversing the order of the $n$ factors costs $(-1)^{n(n-1)/2}$, and the $q$ generators with $Q(e_i) = -1$ contribute $(-1)^{q}$. In dimension five this reads $\omega^{2} = (-1)^{q}$.

## lay
Multiply all the basis directions of an odd-dimensional Clifford algebra together and the result commutes with everything in the algebra. Its square is either plus one or minus one, and this lemma gives a simple formula for which. In five dimensions it is plus one exactly when the number of negative directions is even.

## one-liner
In odd dimension $n$ the volume element of $\Cl(p,q)$ is central with $\omega^{2} = (-1)^{n(n-1)/2 + q}$, which is $(-1)^{q}$ for $n = 5$.
