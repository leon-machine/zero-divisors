---
id: transport.no-go-level-elements
kind: claim
version: 4
title: No-go at the level of elements
status: proved
region: transport
subject: zero-divisors
tags: [no-go, null-directions, refutation]
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
- obj.transport.equivariance
- obj.transport.extension-quadratic-spaces
derivations:
- name: main
  uses:
  - transport.splitting-along-hyperbolic-plane@3
  - primer.commutation-rule@2
  - std-algebra.witt-decomposition@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_pseudo_inverse_normal_form
- kind: check
  ref: check.py::check_null_rotations_fix_v_and_shear_w0
- kind: check
  ref: check.py::check_no_pseudo_inverse_fixed_by_null_rotations
locators:
  paper: T01
  number: Thm 4.2
  label: thm:nogo
  line: 686
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.witt-decomposition where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: in five mixed signatures and three ascents (degenerate included), v sigma v = v gamma^ and the pseudo-inverse normal form, the null rotations R = 1 + vu = u''u/Q(u) and their action, and inconsistency of v sigma v = v with R sigma R^-1 = sigma. Version 2 -> 3.'
  env: theorem
  eqrefs: 3
  typing:
    by: ai-typing-pass
    note: 'Edge kept: the unique-expansion lemma is the only store premise; the hyperbolic-pair identities
      come from a section with no store entity. Levels pass: conditions already kept.'
---

## formal
Let $(\mathbb{V}, Q)$ be nondegenerate of mixed signature $(p,q)$, $p, q \geq 1$, with $n = p + q \geq 3$, and let $\Ncone \subset \mathbb{V}$ be its null cone. Let $(\mathbb{V}', Q')$ be \emph{any} extension of $(\mathbb{V}, Q)$ in the sense of Definition \claimref{obj.transport.extension-quadratic-spaces}, possibly $\mathbb{V}$ itself. Then there is no map $\sigma : \Ncone \to \Cl(\mathbb{V}')$ satisfying $v\,\sigma(v)\,v = v$ for every null $v$ that is equivariant, in the sense of Definition \claimref{obj.transport.equivariance}, even under the identity component $\Spin^0(p,q)$; a fortiori none equivariant under $\Spin(p,q)$ or $\Pin(p,q)$. Equivariant division by zero is impossible at the level of elements, in the Clifford algebra of every ascent, however large.

## technical
Let $(\mathbb{V}, Q)$ be nondegenerate of mixed signature $(p,q)$, $p, q \geq 1$, with $n = p + q \geq 3$ and null cone $\Ncone$, and let $\mathbb{V}'$ be any extension of $\mathbb{V}$, possibly $\mathbb{V}$ itself. Then no map $\sigma : \Ncone \to \Cl(\mathbb{V}')$ with $v\,\sigma(v)\,v = v$ for every null $v$ is equivariant even under $\Spin^0(p,q)$, and a fortiori none is equivariant under $\Spin(p,q)$ or $\Pin(p,q)$.

The proof puts every pseudo-inverse in the normal form $w_0 + \alpha + v\beta + v w_0\delta$ relative to a hyperbolic pair $(v, w_0)$ and conjugates by a null rotation $R = 1 + vu$. This fixes $v$ but shifts the $\Cl(U')$-component by $-u$, so equivariance would force $u = 0$ for every $u \in U$ with $Q(u) \neq 0$, which is impossible.

## lay
A light-like direction has no inverse, but it has many partial inverses. This theorem shows that there is no way to choose one for every light-like direction that respects the symmetries of the geometry, in any space with both space and time directions and at least three dimensions. Enlarging the algebra by any number of new directions does not help.

## one-liner
In mixed signature with $n \geq 3$, no assignment of von Neumann pseudo-inverses to null vectors, valued in the Clifford algebra of any extension, is equivariant even under $\Spin^0(p,q)$.
