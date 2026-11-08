---
id: transport.centre
kind: claim
version: 4
title: The centre
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
  - primer.centre@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:2.6
- kind: check
  ref: check.py::check_centre_by_kernel
- kind: check
  ref: check.py::check_centre_blade_wise
locators:
  paper: T01
  number: Lem 2.6
  label: lem:center
  line: 537
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: centre by kernel computation for every (p,q) with n <= 6 and blade-wise for n <= 9. Version 2 -> 3. Sample inputs moved to module level; no change to what is tested. Version 3 -> 4.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'Re-reviewed: the single edge to the primer centre lemma it restates is kept; levels from the
      earlier pass kept.'
  repair:
    note: restatement of the T0 result primer.centre; derivation and proof text supplied by the store
subject: clifford-structure
tags: [pseudoscalar-and-centre]
equivalent_to:
- primer.centre@3
payload:
- kind: count
  clause: dimension of the centre
  python: all(len(centre_kernel(GA.sig(p, n - p))[1]) == (1 if n % 2 == 0 else 2) for n in range(1, 6)
    for p in range(n + 1))
  note: dim Z(Cl(p,q)) = 1 for n even, 2 for n odd, by the kernel of x -> [x, e_i], n <= 5
---

## formal
For $n \geq 1$, the centre of $\Cl(p,q)$ is $\R \cdot 1$ if $n$ is even, and $\R \cdot 1 \oplus \R \cdot \omega$ if $n$ is odd, where $\omega = e_1 e_2 \cdots e_n$ is the pseudoscalar.

## technical
Let $n = p + q \geq 1$ and let $\omega = e_1 e_2 \cdots e_n$ be the pseudoscalar of $\Cl(p,q)$. The centre $\Zc$ of the algebra depends only on the parity of $n$: for even $n$ it is just the scalars, $\Zc = \R \cdot 1$, while for odd $n$ it is two-dimensional, $\Zc = \R \cdot 1 \oplus \R \cdot \omega$.

The standard reason is that each basis blade either commutes or anticommutes with each generator $e_j$, and the only blades commuting with every generator are $1$ and, when $n$ is odd, $\omega$.

## lay
The centre of an algebra is the set of its elements that commute with everything else in it. For the Clifford algebra of a space with an even number of dimensions, only the ordinary numbers do this. With an odd number of dimensions there is one more such element, the product of all the basis directions, so the centre becomes two-dimensional.

## one-liner
For $n = p + q \geq 1$ the centre of $\Cl(p,q)$ is $\R \cdot 1$ when $n$ is even and $\R \cdot 1 \oplus \R \cdot \omega$ when $n$ is odd, with $\omega$ the pseudoscalar.
