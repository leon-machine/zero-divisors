---
id: families.rigidity-pairing-sector-one-event
kind: claim
version: 4
title: 'Rigidity: the pairing sector is one event'
status: proved
region: families
subject: generations
tags: [pairing-and-bogoliubov, flavour-and-mixing]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 4
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - families.imported-squeezed-vacuum-bosonic-pairing@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T13.py
  tags:
  - label:prop:rigidity
- kind: check
  ref: check.py::check_cross_product_factor_and_gram_spectrum
- kind: check
  ref: check.py::check_takagi_fourfold
- kind: check
  ref: check.py::check_channel_vectors
- kind: check
  ref: check.py::check_coherent_vector_and_universal_point
locators:
  paper: T13
  number: Prop 6.1
  label: prop:rigidity
  line: 785
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit in the channel vectors -i(1,1,1)/sqrt3, -i f_+/sqrt3, in zeta^2 - zeta = -i sqrt3 and in the channel phase e^{i chi} became I_4, with numbers and family-vector components read in span{1, I_4}; no bare i remains.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the cross-product factor and G G^dag spectrum, fourfold Takagi values, the channel vectors, and the coherent vector at the universal point in Q(zeta). Version 1 -> 2. Check strengthened: matrix equality ceq now also compares shapes, so the 6 x 6 annihilation and 2 x 2 unitarity are pinned in size; dimensions read from the matrices and Takagi sample vectors moved to module level. Version 2 -> 3.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - 'zeta, -i sqrt3, -i(1,1,1)/sqrt3 and the channel phases e^{i chi}: complex numbers and vectors of the family space C^3, a multiplicity space'
  env: proposition
  eqrefs: 3
  typing:
    by: ai-typing-pass
    note: "The squeezed-vacuum edge is the premise for applying functions in the Takagi basis and was kept; its E204 is cleared by removing the ordering-dictionary edge from that fact."
---

## formal
Every pairing the descent can write in the antisymmetric sector, any complex combination of the channels at any strengths, has family factor $G = [a]_{\times}$, the cross-product matrix of some complex $3$-vector $a$ (numbers and the components of family vectors are read in $\mathrm{span}\{1, I_4\}$), and
\begin{equation}
G G^{\dagger} \;=\; |a|^{2}\,\mathbb{1} \;-\; \bar{a}\,a^{\mathsf{T}}, \qquad \mathrm{spec} = \{\,|a|^{2},\ |a|^{2},\ 0\,\},
\end{equation}
doubly degenerate identically in $a$. Consequently the Takagi spectrum of the full pairing is fourfold degenerate at every $(\lambda, \chi)$, $\{\sigma, \sigma, \sigma, \sigma, 0, 0\}$ with $\sigma = \tau|a|$; the freezing is exactly one Bogoliubov event with one depth $r = \sigma$, which for the two channels is $r = \tau\sqrt{1 + \lambda^{2}}$ ($\lambda$ is a relabelling of $\tau$ plus a rotation of the coherent ray); the equal-gain identity of the two channels holds to all orders; and the coherent face vector is
\[
v_{k} \;=\; \langle \hat\Omega_{k}\rangle \;=\; 2\,\sinh r\cosh r\;n_{k}, \qquad n = a/|a|,
\]
which at the universal point reads $v_{k} = -I_4\sqrt{\tfrac{2}{3}}\,\sinh r\cosh r\,\bigl(1 + e^{I_4\chi}\zeta^{k}\bigr)$ and in general $v_{k} \propto 1 + \lambda e^{I_4\chi}\zeta^{k}$.

## technical
Every pairing the descent can write in the antisymmetric sector has family factor $G = [a]_{\times}$, the cross-product matrix of a complex $3$-vector $a$ (components read in $\mathrm{span}\{1, I_4\}$), and $GG^{\dagger} = |a|^{2}\,I - \bar{a}\,a^{\mathsf{T}}$ has spectrum $\{|a|^{2}, |a|^{2}, 0\}$ for every $a$. Tensoring with the spinor $\varepsilon$, the Takagi spectrum of the full pairing is $\{\sigma, \sigma, \sigma, \sigma, 0, 0\}$ with $\sigma = \tau|a|$, at every $(\lambda, \chi)$.

The freezing is therefore one Bogoliubov event with a single depth $r = \sigma$, which for the two channels is $r = \tau\sqrt{1 + \lambda^{2}}$; the two channels have equal gain to all orders; and the coherent face vector is $v_{k} = 2\sinh r\cosh r\,n_{k}$ with $n = a/|a|$, which in general is proportional to $1 + \lambda e^{I_4\chi}\zeta^{k}$.

## lay
This result looks at every way the vacuum can pair up particles within one sector and shows that, however the ingredients are mixed, the outcome is always the same kind of single event, governed by one depth parameter. Of the three underlying numbers, two always come out equal and the third zero, whatever the mix. This rigidity means the different pairing channels cannot be played off against each other, and it fixes the direction the vacuum picks out in family space.

## one-liner
Every antisymmetric pairing has family factor $[a]_{\times}$ with $GG^{\dagger}$ spectrum $\{|a|^{2}, |a|^{2}, 0\}$, so the freezing is a single fourfold-degenerate Bogoliubov event of depth $r = \tau|a|$.
