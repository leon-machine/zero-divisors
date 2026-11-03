---
id: mass.grip-real
kind: claim
version: 7
title: The grip is real
status: proved
region: mass
subject: mass
tags: [frozen-point, conformal-spinors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
review: typed
about:
- obj.mass.grip-mass-composite
derivations:
- name: main
  uses:
  - correspondence.reality-conjugation-twistor-form-factor@6
  - mass.chart-form-spin-isomorphism@5
  - mass.imported-flat-model-twistor-chart-infinity@7
  - mass.imported-frozen-point-tractor-connection@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T11.py
  tags:
  - label:lem:real
- kind: check
  ref: check.py::check_real_pairs_generate_su22
- kind: check
  ref: check.py::check_moments_of_real_pairs_are_real
- kind: check
  ref: check.py::check_grip_on_frozen_point_is_real_vector_of_one_four_form
locators:
  paper: T11
  number: Lem 5.5
  label: lem:real
  line: 677
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: real pairs generate su(2,2) (with the commutator identity), real moments, and the grip on I_Lambda a real vector of the (1,4) space. Version 4 -> 5. Check strengthened: non-real control pinned as M_{A(iU ^ V)} = i M_{A(U ^ V)} with the real moments nonzero; control pair moved to module level. Version 5 -> 6. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 6 -> 7.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'x = (i/sqrt2) K epsilon and its consequences: the chart''s complex unit, set to I6 by the earlier GA pass (twistor unit, a 2 x 2 complex matrix chart)'
  env: lemma
  eqrefs: 3
  typing:
    by: ai-typing-pass
    added:
    - obj.mass.grip-mass-composite
    note: 'Kept the reality Fact of the twistor paper as a premise because the Hermitian form and its real form come from it, although the proof recomputes the anti-Hermiticity in the chart; the grip definition was added under about.'
  source_title: 'The grip is real'
  source_formal: |-
    Let $V_{\R}$ be the real span of $n_{\infty}$, $n_{0}$ and the real slice \eqref{eq:realslice} of the $x$-slot. For $U, V \in V_{\R}$ the generator $A(U\wedge V)$ lies in $\mathfrak{su}(2,2)$, the real form of $\Sigma$; hence $M_{U\wedge V}$ is real, and for $I \in V_{\R}$ the grip $P = M(I)$ lies in $V_{\R}$. For the frozen point $I_{\Lambda}$, $P$ is a real vector of $I_{\Lambda}^{\perp}$ and $m^{2} = \ip{P}{P}$ is a value of the $(1,4)$ form of Fact \claimref{mass.imported-frozen-point-tractor-connection}.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Sigma is named as the reversion form of CS (the twistor form) in the formal and technical levels, and a convention line in the proof reads the chart''s i as I6; the block computations are unchanged.'
---

## formal
Let $V_{\R}$ be the real span of $n_{\infty}$, $n_{0}$ and the real slice \eqref{eq:realslice} of the $x$-slot. For $U, V \in V_{\R}$ the generator $A(U\wedge V)$ lies in $\mathfrak{su}(2,2)$, the real form of $\Sigma$, the reversion form of $\CS$ (the twistor form); hence $M_{U\wedge V}$ is real, and for $I \in V_{\R}$ the grip $P = M(I)$ lies in $V_{\R}$. For the frozen point $I_{\Lambda}$, $P$ is a real vector of $I_{\Lambda}^{\perp}$ and $m^{2} = Q(P)$ is a value of the $(1,4)$ form of Fact \claimref{mass.imported-frozen-point-tractor-connection}.

## technical
Let $V_{\R}$ be the real span of $n_{\infty}$, $n_{0}$ and the real slice of the $x$-slot. For $U, V \in V_{\R}$ the generator $A(U\wedge V)$ lies in $\mathfrak{su}(2,2)$, the real form of the reversion form $\Sigma$, the Hermitian form of the conformal spinor space $\CS$, so the moment $M_{U\wedge V}$ is real, and for $I \in V_{\R}$ the grip $P = M(I)$ is a real ambient vector.

For the frozen point $I_{\Lambda}$, $P$ is a real vector of $I_{\Lambda}^{\perp}$, so $m^{2} = Q(P)$ is a value of the real form of signature $(1,4)$ that the frozen point induces on its orthogonal complement.

## lay
The mass of a composite is defined as the length of a vector, its grip on the cosmological scale. For that to be a physical mass the vector must be real, not complex. This lemma checks that it is: real points give real symmetry generators and real charges, so the grip is real and its length is measured by the de Sitter geometry.

## one-liner
Real bivectors give generators in $\mathfrak{su}(2,2)$, so the grip on a real $I$ is real and, for the frozen point, $m^{2}$ is a value of the $(1,4)$ form on $I_{\Lambda}^{\perp}$.
