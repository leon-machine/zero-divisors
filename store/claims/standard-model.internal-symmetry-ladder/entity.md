---
id: standard-model.internal-symmetry-ladder
kind: claim
version: 4
title: The internal symmetry ladder
status: proved
region: standard-model
subject: standard-model
tags: [conformal-spinors, gauge-fields]
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
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 4
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12.py
  tags:
  - label:prop:ladder
- kind: check
  ref: check.py::check_momentum_preservation_forces_unitarity
- kind: check
  ref: check.py::check_unitaries_preserve_and_others_fail
- kind: check
  ref: check.py::check_un_is_sun_times_u1_mod_zn
locators:
  paper: T12
  number: Prop 3.1
  label: prop:ladder
  line: 941
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Group F: the polarisation vector e_j + i e_k of the proof is written e_j + e_k I_6: the numbers of v and U multiply twistor components, so by R3''s twistor clause they carry the conformal-spinor unit I_6 (right multiplication), numbers read in span{1, I_6}; no bare i remains.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: momentum preservation forcing unitarity (independence at n = 2, polarisation at n = 3), unitary and non-unitary samples, and U(n) = (SU(n) x U(1))/Z_n. Version 2 -> 3.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'v = e_j + i e_k in the polarisation step: a vector of the multiplicity space C^n'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the n-twistor system to n conformal spinors, read pi as the E = +1 part and the helicity form as the summed reversion form h, at every level and in the proof. Kept in two-spinor form: the momentum p_{AA''} = sum pi_A pibar_{A''} and the proof''s 2 x n complex matrix computation p = Pi Pi^dagger, which the dictionary does not cover; the computation is unchanged.'
  source_title: |-
    The internal symmetry ladder
  source_formal: |-
    For an $n$-twistor system $(Z^{1}, \ldots, Z^{n})$, the linear mixings $Z^{i} \mapsto U^{i}{}_{j} Z^{j}$ that preserve the total momentum $p_{AA'} = \sum_{i} \pi^{i}_{A}\bar\pi^{i}_{A'}$ and the total helicity form $\sum_{i} \bar{Z}^{i} \cdot Z^{i}$ for every configuration form exactly the unitary group $U(n)$. The ladder therefore reads: one twistor, massless, internal group $U(1)$; two twistors, the first massive step, internal group $U(2)$, with Lie algebra $\su(2) \oplus \uu(1)$; three twistors, internal group $U(3)$, with Lie algebra $\su(3) \oplus \uu(1)$. (The groups are $U(n)$ themselves, not products: the map $SU(n) \times U(1) \to U(n)$, $(a, \mu) \mapsto \mu a$, is onto, and its kernel is $\{(\mu^{-1}I_{n}, \mu) : \mu^{n} = 1\} \cong \mathbb{Z}_{n}$ by the determinant, so $U(n) = (SU(n) \times U(1))/\mathbb{Z}_{n}$; the distinction is treated in Section \ref{sec:algebra}.)
  env: proposition
  typing:
    by: ai-typing-pass
    note: "Self-contained computation; no edges needed, and the paper states no standard route."
---

## formal
For a system of $n$ conformal spinors (an $n$-twistor system) $(Z^{1}, \ldots, Z^{n})$, the linear mixings $Z^{i} \mapsto U^{i}{}_{j} Z^{j}$ that preserve the total momentum $p_{AA'} = \sum_{i} \pi^{i}_{A}\bar\pi^{i}_{A'}$, built from the parts $\pi^{i}$ in the $E = +1$ eigenspace, and the total helicity form $\sum_{i} \bar{Z}^{i} \cdot Z^{i}$, the reversion form $h$ summed over the spinors, for every configuration form exactly the unitary group $U(n)$. The ladder therefore reads: one conformal spinor, massless, internal group $U(1)$; two, the first massive step, internal group $U(2)$, with Lie algebra $\su(2) \oplus \uu(1)$; three, internal group $U(3)$, with Lie algebra $\su(3) \oplus \uu(1)$. (The groups are $U(n)$ themselves, not products: the map $SU(n) \times U(1) \to U(n)$, $(a, \mu) \mapsto \mu a$, is onto, and its kernel is $\{(\mu^{-1}I_{n}, \mu) : \mu^{n} = 1\} \cong \mathbb{Z}_{n}$ by the determinant, so $U(n) = (SU(n) \times U(1))/\mathbb{Z}_{n}$; the distinction is treated in Section \ref{sec:algebra}.)

## technical
For $n$ conformal spinors, put the spinor parts $\pi^{i}$ (the $E = +1$ parts) in the columns of a $2 \times n$ matrix $\Pi$, so that the total momentum is $p = \Pi\,\Pi^{\dagger}$. A linear mixing $U$ preserves $p$ for every configuration exactly when $U^{\dagger}U = 1$, as testing on rank-one configurations and polarisation show, and unitary mixings also preserve the total helicity form $\sum_{i}\bar{Z}^{i} \cdot Z^{i}$, the summed reversion form.

So the internal group is exactly $U(n)$: $U(1)$ for one massless conformal spinor, $U(2)$ with Lie algebra $\su(2) \oplus \uu(1)$ at the first massive step, and $U(3)$ with Lie algebra $\su(3) \oplus \uu(1)$ at three. Each is $U(n) = (SU(n) \times U(1))/\mathbb{Z}_{n}$, not a direct product.

## lay
In this description a massless particle is one basic spinor state of the conformal algebra and a massive one at least two. Mixing the spinor states of a system among themselves without changing its total momentum or total helicity is possible only through unitary transformations. So one spinor state has a circle of internal symmetry, two have the group $U(2)$, and three have $U(3)$. These are genuine unitary groups, not simple products of a special unitary group with a circle.

## one-liner
The mixings of a system of $n$ conformal spinors that preserve total momentum and total helicity form exactly $U(n)$, giving the ladder $U(1)$, $U(2)$, $U(3)$.
