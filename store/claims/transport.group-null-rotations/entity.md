---
id: transport.group-null-rotations
kind: claim
version: 5
title: The group of null rotations
status: proved
region: transport
subject: zero-divisors
tags: [null-directions, rotors-and-stabilisers]
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
  role: 'consistency pass, Spin^0 membership for null u completed in the proof'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - transport.no-go-level-elements@4
  - std-algebra.blade-basis@1
  - std-algebra.orthogonal-anticommute@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:4.6
- kind: check
  ref: check.py::check_group_law_and_injectivity
- kind: check
  ref: check.py::check_null_rotations_are_rotors_fixing_v
- kind: check
  ref: check.py::check_levi_equivariance
locators:
  paper: T01
  number: Lem 4.6
  label: lem:Nv
  line: 792
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. Proof gap: Step 2 of the no-go, cited for membership in Spin^0, covers u with Q(u) != 0 only; the null u of U are now covered by the group law (u a sum of two non-null vectors of the nondegenerate U). Statement unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.blade-basis, std-algebra.orthogonal-anticommute where the proof uses them. Version 3 -> 4.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'Edge kept: membership in the identity component and the fixing of v are taken from the proof
      of the element-level no-go.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: in 9 signatures, the group law, injectivity, rotor membership on a path from 1, fixing of v, and Levi equivariance g R_u g^-1 = R_{gug^-1}. Version 1 -> 2. Wording fix (Leon 2026-10-23): the formal statement now opens by defining v (null, with hyperbolic partner w) and U = {v, w}^perp. Check strengthened: path asserted to start at 1; shear pinned exactly as R_u w R_u^-1 - w = -u - Q(u) v; path samples moved to module level. Version 2 -> 3.'
---

## formal
Let $v$ be a null vector with hyperbolic partner $w$ and $U = \{v, w\}^{\perp}$ the nondegenerate complement of the plane they span. For $u \in U$ set $R_u = 1 + vu$. Then $R_u R_{u'} = R_{u + u'}$, so
\[
N_v \;=\; \{\, R_u : u \in U \,\}
\]
is an abelian subgroup of $\Spin^0(p,q)$, and $u \mapsto R_u$ is an isomorphism of groups $(U, +) \cong N_v$. Each $R_u$ fixes $v$. Moreover the assignment is equivariant for the Levi factor: every rotor $g$ in the even subalgebra of $\Cl(U)$ fixes $v$ and satisfies $g\, R_u\, g^{-1} = R_{g u g^{-1}}$, the conjugation on the right being the vector action of $\Spin(U)$ on $U$.

## technical
Let $v$ be a null vector with hyperbolic partner and $U$ the nondegenerate complement of the hyperbolic plane. For $u \in U$ put $R_u = 1 + vu$. Then $R_u R_{u'} = R_{u + u'}$, so $N_v = \{R_u : u \in U\}$ is an abelian subgroup of $\Spin^0(p,q)$ and $u \mapsto R_u$ is a group isomorphism $(U, +) \cong N_v$; each $R_u$ fixes $v$.

The isomorphism is equivariant for the Levi factor: every rotor $g$ in the even subalgebra of $\Cl(U)$ fixes $v$ and satisfies $g R_u g^{-1} = R_{g u g^{-1}}$, where $u \mapsto g u g^{-1}$ is the vector action of $\Spin(U)$ on $U$.

## lay
Among the symmetries of a space with both space and time directions, some leave a chosen light-like direction exactly in place while shearing other directions along it. These null rotations combine just as vectors add in the directions perpendicular to the light ray and its partner. Ordinary rotations of those perpendicular directions act on the null rotations in the expected way.

## one-liner
The null rotations $R_u = 1 + vu$ with $u \in U$ form an abelian subgroup of $\Spin^0(p,q)$ that fixes $v$ and is isomorphic to $(U, +)$, equivariantly for the rotors of $U$.
