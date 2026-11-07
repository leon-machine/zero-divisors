---
id: rungs.two-twistor-bivector-null-invites-one
kind: claim
version: 4
title: 'Two conformal spinors invite one rung, whose $U(2)$ mixes chirality'
status: proved
region: rungs
subject: standard-model
tags: [null-directions, conformal-spinors, chirality, ladder-pairs]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-rungs, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - rungs.imported-spinor-identification-witt-data-line@4
  - rungs.imported-totality-minimality-completion@6
  - rungs.imported-tower-one-qubit-per-rung@4
  - rungs.mass-bracket-frozen-points-grip-slot@3
  - rungs.rung-spinor-module-mixings@7
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12_rungs.py
  tags:
  - label:prop:bivector
- kind: check
  ref: check.py::check_pairwise_bivectors_null
- kind: check
  ref: check.py::check_one_hyperbolic_plane_completion
- kind: check
  ref: check.py::check_one_rung_u2_mixes_chirality
- kind: check
  ref: check.py::check_two_rungs_give_chirality_preserving_u2
locators:
  paper: T12-rungs
  number: Prop 3.2
  label: prop:bivector
  line: 311
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: pairwise conformal-spinor bivectors null under the Klein form, the mass bracket, the one-plane completion to R^(3,5), the one-rung commutant M_2(C) with abelian chirality-preserving part, and the two-rung chirality-preserving u(2). Version 2 -> 3. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 3 -> 4.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Converted the twistors to conformal spinors and Lambda^2 T to Lambda^2 S (exterior square over the complex unit I6) at every level, title included, and glossed Sigma as the reversion form. Kept V_C, the complexified Cl(2,4) and the complex Fock module Sp: their complex unit must commute with vectors, which I6 does not, so the dictionary''s I6 does not apply to them.'
  source_title: |-
    The two-twistor bivector is null, invites one rung, and that rung's $U(2)$ mixes chirality
  source_formal: |-
    For twistors $Z^{1}, \ldots, Z^{n}$, every pairwise bivector $Z^{i} \wedge Z^{j} \in \Lambda^{2}\T \cong V_{\C}$ is a null vector of the complexified ambient space of $\Cl(2,4)$, decomposable by construction, and for $n = 2$, $m^{2} = 2|\varepsilon(n_{\infty} \wedge Z^{1}\wedge Z^{2})|^{2}$ by Lemma \claimref{rungs.mass-bracket-frozen-points-grip-slot}. The transport principle iterates on the real ambient space $\R^{2,4}$ (Fact \claimref{rungs.imported-tower-one-qubit-per-rung}), and Fact \claimref{rungs.imported-totality-minimality-completion} applied to it gives one further hyperbolic plane, unique, with a reciprocal total on the whole real cone, whatever $n$: the mechanism is a completion of one quadratic space and depends on no count of twistors. The one-rung module $\Lambda^{\bullet}(W \oplus \C v)$, of dimension sixteen, is $\C^{2} \otimes \Sp$ as a vector space, the constituent space of (C), and the transported algebra does supply a $U(2)$ on the $\C^{2}$ factor: the unitary group of the rung's own Clifford algebra $B_{1} \otimes \C \cong \mathrm{M}_{2}(\C)$, the commutant of the ground algebra. But that $U(2)$ contains the odd elements $v \pm w$ of the rung, which anticommute with the chirality operator; its chirality-preserving part is the abelian $\{1, vw\}$-span, a torus. So one rung gives (C)'s vector space with a $U(2)$ that mixes the chirality of the two constituent states, while (C), (S) and the ladder need a $U(2)$ acting within one chirality, which is the rung-mixing $U(2)$ on $\Lambda^{1}R_{2}$ of Theorem \claimref{rungs.rung-spinor-module-mixings}(2), available at two rungs.
  env: proposition
  typing:
    by: ai-typing-pass
    removed:
    - rungs.fact-null-momenta-invite-one-rung
    note: 'Removed the null-momenta corollary, cited only as the parallel case (the completion applies
      "exactly as to R^{1,3}"); the other five edges are premises of the proof. Levels pass: the lay now
      says the null direction is complex and that the one-chirality requirement is that of (C), (S) and
      the ladder, rather than stating it only as a fact about the weak force.'
---

## formal
For conformal spinors (twistors) $Z^{1}, \ldots, Z^{n} \in \CS$, where $\CS = \Lambda^{\mathrm{even}}W$ is the conformal spinor space with complex unit $I_6$ (not the Dirac module $\Sp = \Lambda^{\bullet}W$ below), every pairwise bivector $Z^{i} \wedge Z^{j} \in \Lambda^{2}\CS \cong V_{\C}$ is a null vector of the complexified ambient space of $\Cl(2,4)$, decomposable by construction, and for $n = 2$, $m^{2} = 2|\varepsilon(n_{\infty} \wedge Z^{1}\wedge Z^{2})|^{2}$ by Lemma \claimref{rungs.mass-bracket-frozen-points-grip-slot}. The transport principle iterates on the real ambient space $\R^{2,4}$ (Fact \claimref{rungs.imported-tower-one-qubit-per-rung}), and Fact \claimref{rungs.imported-totality-minimality-completion} applied to it gives one further hyperbolic plane, unique, with a reciprocal total on the whole real cone, whatever $n$: the mechanism is a completion of one quadratic space and depends on no count of conformal spinors. The one-rung module $\Lambda^{\bullet}(W \oplus \C v)$, of dimension sixteen, is $\C^{2} \otimes \Sp$ as a vector space, the constituent space of (C), and the transported algebra does supply a $U(2)$ on the $\C^{2}$ factor: the unitary group of the rung's own Clifford algebra $B_{1} \otimes \C \cong \mathrm{M}_{2}(\C)$, the commutant of the ground algebra. But that $U(2)$ contains the odd elements $v \pm w$ of the rung, which anticommute with the chirality operator; its chirality-preserving part is the abelian $\{1, vw\}$-span, a torus. So one rung gives (C)'s vector space with a $U(2)$ that mixes the chirality of the two constituent states, while (C), (S) and the ladder need a $U(2)$ acting within one chirality, which is the rung-mixing $U(2)$ on $\Lambda^{1}R_{2}$ of Theorem \claimref{rungs.rung-spinor-module-mixings}(2), available at two rungs.

## technical
Each pairwise bivector $Z^{i} \wedge Z^{j} \in \Lambda^{2}\CS \cong V_{\C}$ of conformal spinors, $\CS = \Lambda^{\mathrm{even}}W$, is decomposable, hence a null vector of the complexified ambient space of $\Cl(2,4)$, and for two spinors $m^{2} = 2|\varepsilon(n_{\infty} \wedge Z^{1} \wedge Z^{2})|^{2}$. Completing the real ambient space $\R^{2,4}$ adds one hyperbolic plane, unique, with a reciprocal total on the whole real cone, whatever the number of spinors.

The resulting one-rung module $\Lambda^{\bullet}(W \oplus \C v)$, of dimension sixteen, is $\C^{2} \otimes \Sp$, and the commutant of the ground algebra supplies a $U(2)$ on the $\C^{2}$ factor, the unitary group of $B_{1} \otimes \C \cong \mathrm{M}_{2}(\C)$. Its odd elements $v \pm w$ anticommute with chirality, so its chirality-preserving part is only the torus spanned by $1$ and $vw$. A $U(2)$ acting within one chirality, as the constituent hypothesis, (S) and the ladder require, is the rung-mixing $U(2)$ available at two rungs.

## lay
Any two basic spinor states of the conformal algebra define a null direction in the complexified larger space the programme works in, and completing that space adds exactly one new rung, whatever the number of such states. That single rung gives a state space of the right size for a two-state constituent, with a two-by-two unitary symmetry. But that symmetry mixes left- and right-handed states, whereas the constituent hypothesis, Hypothesis (S) and the ladder need one acting within a single handedness, as the weak force does; a symmetry of the right kind appears only with two rungs.

## one-liner
Pairwise bivectors of conformal spinors are null and the completion adds one rung whatever the number of spinors, but that rung's $U(2)$ mixes chirality, so a chirality-preserving $U(2)$ needs two rungs.
