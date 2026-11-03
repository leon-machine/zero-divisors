---
id: angle.imported-conformal-model-null-rotations
kind: claim
version: 5
title: 'Imported: the conformal model and the null rotations'
status: proved
region: angle
subject: conformal-spacetime
tags: [conformal-model, null-directions, rotors-and-stabilisers]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-angle, the series'' standard disclaimer'
review: typed
about:
- obj.transport.normalised-conformal-chart
- obj.std-algebra.conformal-algebra
- obj.std-algebra.rotor
derivations:
- name: main
  uses:
  - transport.group-null-rotations@4
  - transport.totality@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_conformal_model
- kind: check
  ref: check.py::check_null_rotations_isomorphic_to_u
locators:
  paper: T05-angle
  number: Fact 1.2
  label: fact:T1
  line: 120
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites obj.std-algebra.conformal-algebra, obj.std-algebra.rotor where the proof uses them. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the conformal model in six signatures (nO . nInf = -1, X(x) null, X(x) . X(y) = -Q(x - y)/2) and null rotations R_u = 1 + v u as rotors fixing v, additive and injective on U, in four settings. Version 3 -> 4. Wording fix (check writer''s finding, 2026-10-23): U defined as {v, w}^perp for a null partner w of v, as in transport.group-null-rotations; the check already uses this U.'
  env: fact
  context_refs:
  - transport.group-null-rotations
  - transport.totality
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: Fact restating earlier series results; both existing edges are the cited sources and were kept.
---

## formal
The completion $\Cl(p{+}1,q{+}1)$ of $\Cl(p,q)$ carries the null pair $\nO = \tfrac12(e_{-} - e_{+})$, $\nInf = e_{-} + e_{+}$ with $\nO \cdot \nInf = -1$, and represents the point $x$ by the null vector $X(x) = \nO + x + \tfrac12 Q(x)\nInf$, with $X(x)\cdot X(y) = -\tfrac12 Q(x - y)$. For a null vector $v$ and $u$ orthogonal to it, $R_{u} = 1 + vu$ is a rotor fixing $v$; and for a null partner $w$ of $v$ ($v \cdot w \neq 0$) and $U = \{v, w\}^{\perp}$, the nondegenerate complement of the hyperbolic plane they span, $u \mapsto R_{u}$ (for $u \in U$) is an isomorphism of $(U, +)$ onto the group of null rotations of $v$. \emph{Provenance:} \cite[Sec.~4.3, Lem.~4.6, Thm.~4.10]{ButlerT1}.

## technical
The completion $\Cl(p{+}1,q{+}1)$ of $\Cl(p,q)$ adjoins a null pair $\nO = \tfrac12(e_{-} - e_{+})$, $\nInf = e_{-} + e_{+}$ with $\nO\cdot\nInf = -1$. A point $x$ is represented by the null vector $X(x) = \nO + x + \tfrac12 Q(x)\nInf$, and the inner product of two representatives encodes their squared separation: $X(x)\cdot X(y) = -\tfrac12 Q(x-y)$.

For a null vector $v$ and $u$ orthogonal to it, $R_u = 1 + vu$ is a rotor fixing $v$; and for a null partner $w$ of $v$ ($v \cdot w \neq 0$) and $U = \{v, w\}^{\perp}$, $u \mapsto R_u$ (for $u \in U$) is an isomorphism of the additive group $(U,+)$ onto the group of null rotations of $v$. Both facts are carried over from earlier in the series.

## lay
Adding two extra directions to the algebra of space lets every point be written as a null vector, one whose square is zero, and the squared distance between two points can then be read off from a simple product of their vectors. In the same setting, each null direction has a family of rotations that leave it fixed, and these rotations combine exactly like ordinary addition of vectors. Both facts are carried over from earlier work in the series.

## one-liner
The conformal completion represents points as null vectors whose products give squared separations, and the null rotations fixing a null vector form a group isomorphic to an additive vector group.
