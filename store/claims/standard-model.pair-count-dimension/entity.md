---
id: standard-model.pair-count-dimension
kind: claim
version: 4
title: The pair count in dimension $n$
status: proved
region: standard-model
subject: standard-model
tags: [witt-index, mode-counting]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
- name: Claude Opus 5.5
  role: notation pass, every imaginary unit resolved as a geometric-algebra pseudoscalar (unit principle)
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
review: typed
derivations:
- name: main
  uses:
  - standard-model.imported-pair-systems-two-chirality-halves@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_maximal_isotropic_dimension_is_half
- kind: check
  ref: check.py::check_no_larger_isotropic_subspace
- kind: check
  ref: check.py::check_dimension_four_has_three_pairs
locators:
  paper: T12
  number: Lem 2.12
  label: lem:paircount
  line: 923
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U3: V_C is realised as V + I_W V with I_W = I_V e the central pseudoscalar of the odd extension of the ambient space (I_7 = I_6 e at n = 4; std-algebra.complexification-is-the-odd-extension, cited as a mention), and the split of the squares (y_1 + iy_2)(y_1 - iy_2) is written with I_W, the unit of that field of scalars. No bare i remains, so the outside_ga declaration (other, for i only) is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Group F (found by the language check''s bare-unit detector): nothing replaced; the i stays and is declared outside_ga (other): the dimension count works on the complexified conformal vector space (C^{n+2}, split by (y_1 + iy_2)(y_1 - iy_2)); that complexification must commute with the vectors, which no pseudoscalar does.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: maximal isotropic subspaces of C^(n+2) with a form of signature (2,n) have dimension (n+2)/2 for n = 2..10, three pairs in dimension four. Version 2 -> 3.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted ''a twistor'' and ''a twistor''s pair system'' to the conformal spinor and its pair system at every level and in the proof. The complexification V_C and the complex split-form argument are kept: the Witt decomposition needs a complex unit commuting with vectors, which I6 is not.'
  source_title: |-
    The pair count in dimension $n$
  source_formal: |-
    Let the ambient space of the completion in spacetime dimension $n$ have signature $(2, n)$, so that $V_{\C}$ has dimension $n + 2$ and carries a nondegenerate symmetric bilinear form. If $n$ is even, a maximal totally isotropic subspace of $V_{\C}$ has dimension $(n+2)/2$, so a twistor's pair system has $(n+2)/2$ pairs; in dimension four it has three.
  env: lemma
  typing:
    by: ai-typing-pass
    note: "Edge to the imported pair-system Fact kept as the source of the Fock-vacuum description; pure linear algebra with no completion dependence, so no standard-route derivation."
payload:
- kind: count
  clause: in dimension four it has three
  python: len(null_basis(4)[0]) == 3 and perp_dim(form(4), null_basis(4)[0]) == 3 and all(bil(form(4),
    u, v) == QI(0) for u in null_basis(4)[0] for v in null_basis(4)[0])
  note: three null vectors spanning a totally isotropic U with U^perp of dimension 3, so U is maximal
- kind: count
  clause: (n+2)/2 for n even
  python: all(perp_dim(form(n), null_basis(n)[0]) == len(null_basis(n)[0]) == (n + 2) // 2 for n in EVEN_N)
---

## formal
Let the ambient space of the completion in spacetime dimension $n$ have signature $(2, n)$, so that $V_{\C}$ has dimension $n + 2$ and carries a nondegenerate symmetric bilinear form. If $n$ is even, a maximal totally isotropic subspace of $V_{\C}$ has dimension $(n+2)/2$, so the pair system of a conformal spinor (a twistor's pair system) has $(n+2)/2$ pairs; in dimension four it has three.

## technical
In spacetime dimension $n$ the ambient space of the completion has signature $(2,n)$, so its complexification $V_{\C}$ has dimension $n+2$ and carries a nondegenerate symmetric form. For $n$ even every such form over $\C$ is equivalent to the split form, whose maximal totally isotropic subspaces have dimension $(n+2)/2$; none is larger, since an isotropic $U$ satisfies $U \subseteq U^{\perp}$ and so $2\dim U \le n+2$.

A conformal spinor is the Fock vacuum of the pair system built on a maximal isotropic subspace, one ladder pair per dimension, so its pair system has $(n+2)/2$ pairs: three in dimension four.

## lay
A basic spinor state of the conformal algebra can be described as the empty state of a small set of paired switches, one pair for each independent direction of a special kind in the ambient space. This lemma counts those directions. In an even spacetime dimension n there are (n+2)/2 of them, which in our four-dimensional spacetime gives three pairs.

## one-liner
For even spacetime dimension $n$ a maximal isotropic subspace of $V_{\C}$ has dimension $(n+2)/2$, so the pair system of a conformal spinor has $(n+2)/2$ pairs, three in dimension four.
