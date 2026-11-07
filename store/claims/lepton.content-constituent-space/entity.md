---
id: lepton.content-constituent-space
kind: claim
version: 4
title: The content of the constituent space
status: proved
region: lepton
subject: standard-model
tags: [representation-theory, hypercharge-and-anomalies, recovers-known-physics]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-lepton, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - lepton.imported-automorphism-group-section-hypercharge-generator@4
  - lepton.imported-duality-pair-system@3
  assumes:
  - lepton.hyp-c-constituent@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12_lepton.py
  tags:
  - label:prop:content
- kind: check
  ref: check.py::check_constituent_content_and_weights
- kind: check
  ref: check.py::check_odd_and_even_halves
- kind: check
  ref: check.py::check_duality_on_the_section
- kind: check
  ref: check.py::check_lattice_condition
locators:
  paper: T12-lepton
  number: Prop 2.1
  label: prop:content
  line: 220
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: weights, SU(2) and SU(3) content of each C_k from the unit action, the odd and even halves, duality on the section, and the lattice condition. Version 3 -> 4.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted C^2 (x) T, C^2 (x) T'' and the bare twistor to the conformal spinor space S = Lambda^even W, its partner S'' = Lambda^odd W and the bare conformal spinor, at the formal and lay levels. The proof had no twistor language.'
  source_title: |-
    The content of the constituent space
  source_formal: |-
    Assume Hypothesis (C), and let $S(U(2) \times U(3))$ act through its canonical section. Then:
    \begin{enumerate}
    \item $\Con_{k}$ transforms as $(2, \Lambda^{k}\C^{3})$ with abelian weight $q = 3 - 2k$, so
    \[
    \Con_{0} = (2,1)_{1/2}, \qquad \Con_{1} = (2,3)_{1/6}, \qquad \Con_{2} = (2,\bar{3})_{-1/6}, \qquad \Con_{3} = (2,1)_{-1/2}.
    \]
    \item The odd half is one generation's doublets, in the same chirality half:
    \[
    \C^{2} \otimes \T' \;=\; \Con_{1} \oplus \Con_{3} \;=\; (2,3)_{1/6} \oplus (2,1)_{-1/2} \;=\; Q \oplus L.
    \]
    The lepton doublet is a slot holding the full pair system; the quark doublet is a slot holding one excited pair; and they lie in the same chirality half because one and three are both odd, whichever sign $\epsilon$ takes.
    \item The even half is the dual of the odd half, constituent by constituent: $\Con_{k}^{*} \cong \Con_{3-k}$, so $\C^{2} \otimes \T = \Con_{0} \oplus \Con_{2} = L^{*} \oplus Q^{*}$, the antiparticles, in the opposite chirality half. A slot holding a bare twistor, the Fock vacuum $u$ itself, is the antilepton.
    \item The lattice condition $2t + 3\delta + q \equiv 0 \pmod 6$ of \cite[Thm.~4.2(ii)]{ButlerT12} holds on every $\Con_{k}$.
    \end{enumerate}
  typing:
    by: ai-typing-pass
    note: 'Kept both Facts the proof cites; the lattice condition in item (4) is checked by direct arithmetic,
      so the global-form theorem in context_refs was not added as a premise; Hypothesis (C) has no postulate
      entity in the store. Hypothesis pass: assumes lepton.hyp-c-constituent added because its statement
      assumes Hypothesis (C). Levels pass: the lay now names Hypothesis (C).'
    added:
    - lepton.hyp-c-constituent
  env: proposition
  context_refs:
  - standard-model.global-form-quotient-determined
---

## formal
Assume Hypothesis (C), and let $S(U(2) \times U(3))$ act through its canonical section. Then:
\begin{enumerate}
\item $\Con_{k}$ transforms as $(2, \Lambda^{k}\C^{3})$ with abelian weight $q = 3 - 2k$, so
\[
\Con_{0} = (2,1)_{1/2}, \qquad \Con_{1} = (2,3)_{1/6}, \qquad \Con_{2} = (2,\bar{3})_{-1/6}, \qquad \Con_{3} = (2,1)_{-1/2}.
\]
\item The odd half is one generation's doublets, in the same chirality half, writing $\CS = \Lambda^{\mathrm{even}}W$ for the conformal spinor space and $\CSm{} = \Lambda^{\mathrm{odd}}W$ for its partner (twistor and dual twistor space):
\[
\C^{2} \otimes \CSm{} \;=\; \Con_{1} \oplus \Con_{3} \;=\; (2,3)_{1/6} \oplus (2,1)_{-1/2} \;=\; Q \oplus L.
\]
The lepton doublet is a slot holding the full pair system; the quark doublet is a slot holding one excited pair; and they lie in the same chirality half because one and three are both odd, whichever sign $\epsilon$ takes.
\item The even half is the dual of the odd half, constituent by constituent: $\Con_{k}^{*} \cong \Con_{3-k}$, so $\C^{2} \otimes \CS = \Con_{0} \oplus \Con_{2} = L^{*} \oplus Q^{*}$, the antiparticles, in the opposite chirality half. A slot holding a bare conformal spinor, the Fock vacuum $u$ itself, is the antilepton.
\item The lattice condition $2t + 3\delta + q \equiv 0 \pmod 6$ of \cite[Thm.~4.2(ii)]{ButlerT12} holds on every $\Con_{k}$.
\end{enumerate}

## technical
Under Hypothesis (C), with $S(U(2) \times U(3))$ acting through its canonical section, the constituent $\Con_{k} = \C^{2} \otimes \Lambda^{k}W$ transforms as $(2, \Lambda^{k}\C^{3})$ with abelian weight $q = 3 - 2k$, so $\Con_{0}, \Con_{1}, \Con_{2}, \Con_{3}$ are $(2,1)_{1/2}$, $(2,3)_{1/6}$, $(2,\bar{3})_{-1/6}$, $(2,1)_{-1/2}$.

The odd half $\Con_{1} \oplus \Con_{3} = Q \oplus L$ is one generation's doublets, in the same chirality half whatever the sign $\epsilon$. The even half is its dual, $\Con_{k}^{*} \cong \Con_{3-k}$, the antiparticles, in the opposite half; a slot holding the bare Fock vacuum is the antilepton. Every $\Con_{k}$ satisfies the lattice condition $2t + 3\delta + q \equiv 0 \pmod 6$. The proof reads the weights off the section's action and uses the duality of exterior powers with $\det A \cdot \det B = 1$ on the section.

## lay
Under a stated hypothesis about how a basic spinor state sitting in a slot transforms (Hypothesis (C)), this result lists the charges of the four kinds of constituent. Two of them are exactly the quark doublet and the lepton doublet of one Standard Model generation, and they share a handedness; the other two are their antiparticles. A slot holding an unexcited spinor state is the antilepton, and all four have charges on the series' charge lattice.

## one-liner
Under Hypothesis (C), the constituent space is the quark and lepton doublets in one chirality half and their antiparticles in the other, all on the $\mathbb{Z}_{6}$ charge lattice.
