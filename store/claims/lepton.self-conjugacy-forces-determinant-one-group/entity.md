---
id: lepton.self-conjugacy-forces-determinant-one-group
kind: claim
version: 4
title: Self-conjugacy forces the determinant-one group
status: proved
region: lepton
subject: standard-model
tags: [gauge-fields, forcing-and-uniqueness, representation-theory]
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
  - lepton.content-constituent-space@4
  - lepton.imported-automorphism-group-section-hypercharge-generator@3
  - lepton.imported-duality-pair-system@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12_lepton.py
  tags:
  - label:prop:selfconj
- kind: check
  ref: check.py::check_not_self_dual_under_full_group
- kind: check
  ref: check.py::check_self_dual_iff_determinant_one
- kind: check
  ref: check.py::check_dimension_twelve
- kind: check
  ref: check.py::check_twisted_action_is_self_conjugate
locators:
  paper: T12-lepton
  number: Prop 3.1
  label: prop:selfconj
  line: 268
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: non-self-duality under U(2) x U(3) from torus weights, the biconditional over 301 central-character lattices, dimension 12, and self-conjugacy of the twisted action. Version 3 -> 4.'
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: VALUES M8
    open_problem: op.small-findings
    note: 'Scope stated: the theorem holds for the untwisted action, the one in which the first display holds. Twisting every component by t = (det A det B)^(-1/2) gives (Con_k t)^* = Con_{3-k} (det A det B)^(-1) t^(-1) = Con_{3-k} t, so the twisted spectrum is self-dual under the whole group and the conclusion fails there; T12 shows the generation''s state space carries that twisted action (lepton.what-self-conjugacy-says-about-thirteenth). The proof is unchanged.'
  source_formal: 'As a representation of $U(2) \times U(3)$, $\Con$ is not self-dual: $\Con_{k}^{*} \cong \Con_{3-k} \otimes (\det A \cdot \det B)^{-1}$, and no $\Con_{j}$ is isomorphic to $\Con_{k}^{*}$, since the $K$-weights $1 - j$ and $-(1 - k)$ never agree for $j, k \in \{0, 1, 2, 3\}$ with matching content. As a representation of a subgroup $G \subseteq U(2) \times U(3)$ containing $SU(2) \times SU(3)$, $\Con$ is self-dual if and only if $\det A \cdot \det B = 1$ on $G$, that is $G \subseteq S(U(2) \times U(3))$. In particular the largest subgroup of $U(2) \times U(3)$ under which the constituent spectrum is closed under conjugation is exactly the automorphism group of the hierarchy, $S(U(2) \times U(3))$, twelve-dimensional.'
  typing:
    by: ai-typing-pass
    added:
    - lepton.imported-automorphism-group-section-hypercharge-generator
    note: 'Added the automorphism-group Fact, which defines the kernel K whose weights the proof compares
      and identifies S(U(2) x U(3)) as the hierarchy''s automorphism group in the last clause; the proof
      does not cite it by name, so this addition is a judgement. Levels pass: the lay level now keeps
      the scope condition that the subgroup contains $SU(2) \times SU(3)$.'
  env: proposition
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - lepton.imported-automorphism-group-section-hypercharge-generator
---

## formal
As a representation of $U(2) \times U(3)$, $\Con$ is not self-dual: $\Con_{k}^{*} \cong \Con_{3-k} \otimes (\det A \cdot \det B)^{-1}$, and no $\Con_{j}$ is isomorphic to $\Con_{k}^{*}$, since the $K$-weights $1 - j$ and $-(1 - k)$ never agree for $j, k \in \{0, 1, 2, 3\}$ with matching content. As a representation of a subgroup $G \subseteq U(2) \times U(3)$ containing $SU(2) \times SU(3)$, $\Con$ is self-dual if and only if $\det A \cdot \det B = 1$ on $G$, that is $G \subseteq S(U(2) \times U(3))$. In particular the largest subgroup of $U(2) \times U(3)$ under which the constituent spectrum is closed under conjugation is exactly the automorphism group of the hierarchy, $S(U(2) \times U(3))$, twelve-dimensional. All of this is for the untwisted action, the one in which the first display holds: if every component is twisted by $t = (\det A \cdot \det B)^{-1/2}$, then $(\Con_{k} \otimes t)^{*} \cong \Con_{3-k} \otimes t$, the twisted spectrum is closed under conjugation for the whole group (on the double cover on which $t$ is a character), and the conclusion does not hold there (Observation \claimref{lepton.what-self-conjugacy-says-about-thirteenth}).

## technical
As a representation of $U(2) \times U(3)$ the constituent space $\Con$ is not self-dual: $\Con_{k}^{*} \cong \Con_{3-k} \otimes (\det A \cdot \det B)^{-1}$, and the $K$-weights, $1 - j$ on $\Con_{j}$ and $k - 1$ on $\Con_{k}^{*}$, never agree where the $SU(2) \times SU(3)$ contents match.

For a subgroup $G \subseteq U(2) \times U(3)$ containing $SU(2) \times SU(3)$, $\Con$ is self-dual if and only if $\det A \cdot \det B = 1$ on $G$, that is $G \subseteq S(U(2) \times U(3))$. So the largest subgroup under which the constituent spectrum is closed under conjugation is exactly the twelve-dimensional automorphism group of the hierarchy. This is a statement about the untwisted action: in the action twisted by $(\det A \cdot \det B)^{-1/2}$, which the Standard-Model paper shows the generation's state space carries, the dual of every component is a component and self-conjugacy no longer removes the thirteenth generator.

## lay
A symmetry group that makes physical sense should send every particle's antiparticle back into the list of particles. Among groups that contain the weak and strong symmetry groups, for the constituent space this works only when a determinant condition holds, which cuts the naive thirteen-dimensional group down to twelve dimensions. That twelve-dimensional group is exactly the symmetry group of the two-level structure. This holds for the plain way the groups act; in the slightly twisted action the series now uses, the argument no longer removes the thirteenth direction.

## one-liner
For a subgroup of $U(2) \times U(3)$ containing $SU(2) \times SU(3)$, the constituent spectrum in its untwisted action is closed under conjugation exactly when the subgroup lies in $S(U(2) \times U(3))$ (in the action twisted by $(\det A \cdot \det B)^{-1/2}$, defined on the double cover, it is closed for the whole group).
