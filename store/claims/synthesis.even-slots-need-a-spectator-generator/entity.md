---
id: synthesis.even-slots-need-a-spectator-generator
kind: claim
version: 2
title: Two-level slots in the composite's own five-rung floor are odd, giving Hypothesis (S) with the tower grading as chirality; even slots need a spectator generator
status: proved
region: synthesis
subject: standard-model
tags: [hypotheses-s-r-c, spinor-modules]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - tower.ladder-pairs-satisfy-car-vectors@4
  - field-theory.no-canonical-commutation-relations-tower@3
  - standard-model.imported-pair-systems-two-chirality-halves@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_even_slots_need_spectator
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.hyp-s-slot-statistics
  - rungs.r-s-are-one-hypothesis-two
  - field-theory.no-canonical-commutation-relations-tower
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'The slot-module hypothesis was restated on 2026-10-23 (version 2: clauses (c), (d), (e) replaced by the generation clause (G) and chirality as a CPT halving); the clauses this result bears on are those of version 1, and its mathematics stands. Version 1 -> 2.'
  open_problem: op.hypothesis-s
  note: 'Decides where the parity of a slot comes from. A slot operator of even tower parity (a Klein-twisted fermion c K, a boson made of fermions that the statistics no-go allows) needs an odd factor K from outside the algebra of the composite own five rungs; inside that floor the slots are odd and every clause of (S) follows, with the tower grading as chirality and without anomaly input. Every floor of the tower contains the base generators, so a spectator is always available: the no-spectator condition is a premise, weaker than the rung reading (R) (it allows slot operators that are not rung vectors, such as the grade-seven Klein twists), not a theorem. Complements the anomaly route to the same decision (filed alongside, synthesis.slot-parity-decides-hypothesis-s), which fixes the parity by hypercharge anomaly cancellation once a spectator is allowed and whose clause (i) is the same covariance lemma as (i) here; with an even slot the state space and group action of (S) survive and only the identification of its chirality with the tower grading fails. Transport-absent apart from the tower floor itself. Two-levelness (single-mode CAR per slot) is a hypothesis, not derived: parafermionic slots are excluded by assumption. Not addressed: slots that are not two-level; the three-constituent count.'
---

## formal
Let $F = \Cl(5,5)$ be a floor spanned by five rungs of the tower, with null pairs $(v_{k}, w_{k})$ satisfying the canonical anticommutation relations as vectors (Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}); let rungs $1, 2, 3$ carry the composite's pair modes, as in Fact \claimref{standard-model.imported-pair-systems-two-chirality-halves}, with pair algebra $P$ and pair parity $\Gamma_{W} = \prod_{k \le 3}(1 - 2v_{k}w_{k})$. Let $s_{1}, s_{2} \in F_{\C}$ be slot operators that are (a) homogeneous of tower parity $\pi$, (b) two-level, $s_{i}^{2} = 0$, $s_{i}s_{i}^{*} + s_{i}^{*}s_{i} = 1$, (c) carried into two-level operators by every $A \in U(2)$ acting on their span, and (d) such that each slot operator commutes with every pair operator, or each anticommutes with every one. Then:
\begin{enumerate}
\item[(i)] $s_{1}, s_{2}$ satisfy the canonical anticommutation relations among themselves; commuting two-level slots violate (c);
\item[(ii)] the commutant $P'$ of $P$ in $F$ is spanned by $16$ blades, of which $8$ are even and span a subalgebra; $s_{i}$ or $s_{i}\Gamma_{W}$ lies in $P'$ and has parity $\pi$; two canonical anticommutation modes generate a $16$-dimensional algebra; hence $\pi = 1$: inside $F$ every such pair of slots is odd;
\item[(iii)] with $\pi = 1$, after replacing $s_{i}$ by $s_{i}\Gamma_{W}$ if they commute with the pairs (which changes each state $s_{J}^{*}b_{K}^{*}\lvert 0\rangle$ only by $(-1)^{jk}$), the five modes satisfy the canonical anticommutation relations, the states built on their joint vacuum span $32$ dimensions, $U(2) \times U(3)$ acts as $\Lambda^{\bullet}(A \oplus B)$, and the tower grading, conjugation by the pseudoscalar of $F$ (the only blade anticommuting with all ten generators), takes the value $(-1)^{j + k}$ on the component with $j$ slots and $k$ pairs occupied relative to the vacuum: every clause of Hypothesis (S), with the tower grading as chirality;
\item[(iv)] in $\Cl(6,5)$, the floor with one further generator $g$, $g^{2} = 1$, the even operators $s_{k} = v_{k}g$ ($k = 4, 5$) satisfy (b), (c) and (d).
\end{enumerate}
So the tower parity of two-level, $U(2)$-covariant slots is fixed by whether the slot operators may use a generator outside the composite's own five rungs: without such a spectator they are odd and Hypothesis (S) follows with the tower grading as chirality; with one, even slots exist, and for them the tower grading is $(-1)^{k}$ on the component $(j, k)$, not the chirality (S) declares. The statistics no-go of Proposition \claimref{field-theory.no-canonical-commutation-relations-tower} excludes neither.

## technical
Take the composite's three pair modes on three rungs of a floor and ask which slot operators the same floor can supply. Two-level slots carrying a linear $U(2)$ action must anticommute with each other. If they also commute, or anticommute, with all pair operators, then each slot, possibly multiplied by the pair parity $\Gamma_{W}$ (which is even), lies in the commutant of the pair algebra. When the floor is spanned by the composite's own five rungs, that commutant is a sixteen-dimensional algebra whose even part has dimension eight, too small to hold two fermionic modes, which generate sixteen dimensions. So inside the composite's own floor the slots are odd, and then the thirty-two states, the $U(2) \times U(3)$ action and the chirality, read as the tower grading, are those of Hypothesis (S); the commuting or anticommuting choice is a Klein transformation that changes states only by signs.

With a single extra generator $g$ outside the five rungs, the products $v_{k}g$ are even slot operators meeting the same conditions. Every floor of the tower contains such generators, so the condition that the slots use none of them is an assumption about where slots live, weaker than identifying slots with rungs, not a theorem of the tower. The statistics no-go is silent on both cases: it excludes only a canonical bosonic slot.

## lay
The framework assumes, as Hypothesis (S), that the two places a composite particle's basic spinor states occupy behave as fermion modes. This result asks what the tower of algebras forces. If those slot operators are built only from the composite's own five modes, the algebra leaves no room for anything else: the slots must be fermion modes, and every part of (S) follows, including which states count as left-handed. If the slots may borrow one more ingredient from the rest of the tower, which always has such ingredients available, then boson-like slots made of two fermions also fit. So, for two-level slots, (S) with the tower grading as chirality follows from the condition that slots use nothing beyond the composite's own modes; with one borrowed ingredient the slots may be boson-like, and then the tower grading is no longer the chirality (S) declares.

## one-liner
Under two-level (single-mode) slots that are $U(2)$-covariant and commute or anticommute with the pairs, the composite's own five-rung floor admits only odd slots, giving every clause of (S) with the tower grading as chirality; even slots need one spectator generator outside those rungs, which every floor supplies, so the no-spectator condition is a premise.
