---
id: synthesis.joint-clifford-clause-is-a-klein-convention-on-the-composite-space
kind: claim
version: 1
title: 'The joint Clifford clause (f) is a Klein convention on the composite space'
status: proved
region: synthesis
subject: standard-model
tags: [hypotheses-s-r-c, car-algebra, ladder-pairs, grading-and-parity]
proposed_by:
  kind: ai
  session: 2026-11-07-ga-units
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-07-ga-units
review: draft
derivations:
- name: main
  uses:
  - synthesis.even-slots-need-a-spectator-generator@3
  - synthesis.blade-square-signs-f2-quadratic-form@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_both_slot_conventions_obey_the_car_and_differ_by_the_pair_parity
- kind: check
  ref: check.py::check_split_preserving_bivectors_and_grading_are_convention_free
- kind: check
  ref: check.py::check_the_klein_twist_is_unique_up_to_sign
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.slot-module-hypothesis
  - synthesis.even-slots-need-a-spectator-generator
extraction:
  open_problem: op.hypothesis-s
  note: >-
    Answers whether clause (f) of the slot-module hypothesis (slots and pairs one Clifford system) adds content
    on the composite space V = F (x) Lambda W: it does not. On V the natural slot operators commute with the
    pair operators; their Klein twists a (-1)^k anticommute with them, obey the same CAR, covariance and
    generation, and are unique up to a unit (sign, for an involution); the split-preserving (Pati-Salam)
    bivectors and the grading are the same operators in both conventions. Realised in the floor Cl(5,5) of
    synthesis.even-slots-need-a-spectator-generator, where the pair parity is the single blade
    e2 f2 e3 f3 e4 f4 (1 - 2 v w = e f), so uniqueness is a count with the commutation form of
    synthesis.blade-square-signs-f2-quadratic-form. The Majorana generator of square -1 is a real vector f_k,
    so no imaginary unit is needed; numbers are read in span{1, I4}. Pre-registered kill condition: a result in
    the future cone of (f) whose statement changes beyond an overall sign under a -> a (-1)^k, that is, one
    using the slot operators as given tower elements. Not run over the whole future cone; the clause keeps
    content exactly in that embedded reading, which this result does not address. The Klein transformation
    itself is standard (O. Klein 1938; H. Araki 1961; cited from memory), reproved here. Transport-absent.
  flags:
  - 'the kill condition was not run over the future cone of the slot-module hypothesis: results that use the slot operators as given tower elements could still give clause (f) content; on V itself it has none'
---

## formal
Read numbers in $\mathrm{span}\{1, I_{4}\}$. Let $V = F \otimes \Lambda^{\bullet}W$ be the composite space of Premise \claimref{standard-model.slot-module-hypothesis}(a) with fermionic slot module $F = \Lambda^{\bullet}D$, $D$ the slot doublet; let $a_{i} = a(u_{i}) \otimes 1$ ($i = 1, 2$) be the slot annihilators, $b_{p} = 1 \otimes b(t_{p})$ ($p = 1, 2, 3$) the pair annihilators, $(-1)^{k}$ the pair parity, $(-1)^{N} = (-1)^{n + k}$ the grading, and $\tilde a_{i} = a_{i}(-1)^{k}$ the Klein-twisted slot operators.
\begin{enumerate}
\item[(i)] \emph{(Same slot data; proved.)} The $\tilde a_{i}$ satisfy the same canonical anticommutation relations as the $a_{i}$, transform in the same way under $U(2) \times U(3)$, and on $F_{n} \otimes \Lambda^{k}W$ have $\tilde a_{i}^{\dagger} = (-1)^{k}a_{i}^{\dagger}$, so clause (G) holds for one set exactly when it holds for the other.
\item[(ii)] \emph{(Opposite relation to the pairs; proved.)} The $a_{i}$ commute with every $b_{p}$, $b_{p}^{\dagger}$; the $\tilde a_{i}$ anticommute with them. So $\tilde a_{1}, \tilde a_{2}, b_{1}, b_{2}, b_{3}$ satisfy the canonical anticommutation relations of one system of five modes, and their real Majorana combinations, five of square $+1$ and five of square $-1$, generate $\Cl(5,5)$ on $V$, whose span over $\mathrm{span}\{1, I_{4}\}$ is the $\Cl(10)$ of clause (f).
\item[(iii)] \emph{(Convention-free operators; proved.)} The $21$ split-preserving bivectors (the $6$ slot-slot and $15$ pair-pair Majorana bivectors, the Pati-Salam algebra of clause (CPT)) and the grading $(-1)^{N}$, which anticommutes with $a_{i}$, $\tilde a_{i}$ and $b_{p}$ alike, are the same operators in both conventions.
\item[(iv)] \emph{(Uniqueness; proved.)} If an operator $K$ on $V$ commutes with every $a_{i}$, $a_{i}^{\dagger}$ and the $a_{i}K$ anticommute with every pair operator and satisfy the canonical anticommutation relations, then $K = c(-1)^{k}$ with $c$ a unit of $\mathrm{span}\{1, I_{4}\}$ (a phase from the centre of the slot $U(2)$), and $c = \pm 1$ if $K$ is an involution.
\item[(v)] \emph{(Consequence; proved on $V$.)} Clause (f) holds on $V$ for every $F \cong \Lambda^{\bullet}D$, canonically up to that unit: it is a convention on $V$ (the $24$ cross bivectors depend on the convention, but the residual sign acts on them by $\mathrm{Ad}$ of the slot parity, an element of $\mathrm{Spin}(10)$, so the $\mathrm{Spin}(10)$ of clause (f) is canonical), and the qualifier of clause (CPT) ``when the slot module is fermionic, so that clause (f) applies'' adds no condition beyond $F \cong \Lambda^{\bullet}D$. The clause keeps content only relative to slot operators given in advance, for instance as tower elements (the setting of \claimref{synthesis.even-slots-need-a-spectator-generator}(iii)), which is not addressed.
\end{enumerate}
The twist is the replacement $s_{i} \mapsto s_{i}\Gamma_{W}$ of \claimref{synthesis.even-slots-need-a-spectator-generator}(iii), the commuting-copies device of \claimref{tower.commuting-copies} read backwards. In the floor $\Cl(5,5)$ of \claimref{synthesis.even-slots-need-a-spectator-generator}, with the modes as null pairs of vectors, the twisted operators are the vectors themselves, the untwisted ones are the vectors times the pair parity $\Gamma_{W} = e_{2}f_{2}e_{3}f_{3}e_{4}f_{4}$, a single blade, and (iv) is a count of blades with the commutation form of \claimref{synthesis.blade-square-signs-f2-quadratic-form}(ii). Transport-absent.

## technical
Clause (f) of the slot-module hypothesis asks that the slot and pair operators of a composite form one system of five fermionic modes, each slot operator anticommuting with each pair operator. On the tensor-product space $V = F \otimes \Lambda^{\bullet}W$ the natural slot operators commute with the pair operators instead. Multiplying them by the pair parity $(-1)^{k}$, the Klein transformation, turns commuting into anticommuting while keeping their anticommutation relations, their $U(2) \times U(3)$ behaviour and their images, so generation is unaffected. Everything the hypothesis asks of the chirality is the same in both conventions: the slot-slot and pair-pair bivectors (the Pati-Salam algebra) and the grading by the total mode number. The twist is unique: a factor commuting with the slot operators and making them anticommute with the pairs is a unit times $(-1)^{k}$, because it then commutes with all operators on $V$. In geometric algebra the five modes are null pairs of vectors in $\Cl(5,5)$, the twisted slot operators are those vectors, and the pair parity is the single blade $e_{2}f_{2}e_{3}f_{3}e_{4}f_{4}$; uniqueness is then a count with the two-element-field commutation form of blades. So on $V$ clause (f) is a convention, not a premise; it would carry content only for slot operators fixed in advance, for instance as tower elements, which this result does not treat. Transport-absent.

## lay
The series builds each quark or lepton from two kinds of ingredients, slots and pairs, and one of its assumptions says that the two kinds behave as a single family of fermions, swapping sign whenever one of each is exchanged. This result shows that, on the particle's own space of states, this costs nothing: if slot and pair operators are first written so that they ignore each other, a standard trick (multiplying each slot operator by a sign that counts the pairs) makes them behave as one family, changes nothing else that the theory uses, and is the only way to do it up to an overall sign. The assumption only matters if the slot operators are fixed in advance by something else, such as the deeper tower of the theory.

## one-liner
On the composite space $V = \Lambda^{\bullet}D \otimes \Lambda^{\bullet}W$ the Klein-twisted slot operators $a(-1)^{k}$ keep the slot CAR, covariance and generation, anticommute with the pair operators where the untwisted ones commute, leave the $21$ Pati-Salam bivectors and the grading unchanged, and are unique up to a unit, so clause (f) is a convention on $V$, with content only for slot operators fixed in advance.
