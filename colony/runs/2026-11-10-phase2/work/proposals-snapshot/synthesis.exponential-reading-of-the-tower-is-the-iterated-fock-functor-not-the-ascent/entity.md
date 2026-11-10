---
id: synthesis.exponential-reading-of-the-tower-is-the-iterated-fock-functor-not-the-ascent
kind: claim
version: 1
title: 'The exponential reading of the tower: the iterated Fock functor, not the ascent'
status: proved
region: synthesis
subject: tower
tags: [the-number-n, mode-counting, ladder-pairs, spinor-modules, finite-models]
proposed_by:
  kind: ai
  session: 2026-11-10-phase2
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase2
review: draft
derivations:
- name: main
  uses:
  - tower.fock-module-one-qubit-per-rung@6
  - tower.witt-index-quantum-capacity@5
  - tower.ladder-pairs-satisfy-car-vectors@4
  - tower.commuting-copies@5
  - tower.matrix-amplification-structural-properties@3
  - tower.answers-iteration-question@5
  - std-algebra.existence-uniqueness@1
  - standard-model.trichotomy-what-kind-number@11
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_three_pairs_have_eight_states_and_the_level_above_has_eight_pairs_and_256_states
- kind: check
  ref: check.py::check_one_ascent_from_three_pairs_gives_four_pairs_and_sixteen_states
- kind: check
  ref: check.py::check_non_vector_car_families_fill_the_level_and_the_dimension_bound
- kind: check
  ref: check.py::check_the_lift_of_the_ladder_to_the_level_above_is_lie_and_not_car
- kind: check
  ref: check.py::check_the_horizon_count_lies_between_the_third_and_fourth_levels
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.why-large
  - refuted.the-number-n-is-a-mystery-of-largeness
extraction:
  note: >-
    Decides the exponential reading of the tower that Observation standard-model.why-large (version 3, conjectured)
    states as unproved and on which refuted.the-number-n-is-a-mystery-of-largeness (version 2) rests. No open problem
    of the store is attached to the number N at present (op.t12-n-after-the-count is settled), so no open_problem
    field is set. The statement is on the split tower over the ground floor of the real numbers; the base count three
    of the reading is the pair count of a conformal spinor, a count on the complexified ambient space
    (standard-model.pair-count-dimension), and which base, real or complex, the reading intends is not decided here.
    Transport-essential only in clauses (ii) and (iii), which use the tower's one plane per rung; clauses (i) and
    (iv) are the classical second quantisation of a finite-dimensional space (prior art: the exterior-algebra
    functor and its derivation lift, textbook material cited from memory, for example Bratteli and Robinson,
    Operator Algebras and Quantum Statistical Mechanics 2, section 5.2), placed in the series' algebra. Not decided
    here: readings that use an invariant form of the module, one chirality half, or two-fermion states in place of
    all states; those would be separate statements.
---

## formal
Let $B_{k} = \Cl(k,k)$ be the algebra of $k$ ladder pairs $v_{i}, w_{i}$ (Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}) and $F_{k} = \Lambda^{\bullet}W_{k}$ its Fock module, of dimension $2^{k}$, with the basis of states $v_{S}$, $S \subseteq \{1, \dots, k\}$ (Theorem \claimref{tower.fock-module-one-qubit-per-rung}). Call a family $(a_{i}, b_{i})_{i \le m}$ of elements of a real algebra with unit a \emph{CAR family} if $a_{i}a_{j} + a_{j}a_{i} = 0$, $b_{i}b_{j} + b_{j}b_{i} = 0$ and $a_{i}b_{j} + b_{j}a_{i} = \delta_{ij}$. The exponential reading of Observation \claimref{standard-model.why-large} (each level's objects are the fermionic pairs of the level above, with counts $3$, $8$, $256$, $2^{256}$) has the following precise forms, on the split tower $B_{0} = \R \subset B_{1} \subset B_{2} \subset \cdots$.
\begin{enumerate}
\item[(i)] \emph{(As a functor on modules the counts hold.)} Let the level above $B_{k}$ be the Clifford algebra of $F_{k} \oplus F_{k}^{*}$ with the form $Q(x + \phi) = \phi(x)$. The states $V_{S} = v_{S}$ and the dual basis $W_{S}$ are a CAR family of $2^{k}$ vectors, so this algebra is $B_{2^{k}}$ and its Fock module is $\Lambda^{\bullet}F_{k}$, of dimension $2^{2^{k}}$. Iterating from $c_{0} = 3$ gives $c_{n+1} = 2^{c_{n}}$: $3$, $8$, $256$, $2^{256}$. On this reading $2^{256}$ is the number of ladder pairs of the third level above the base, equal to the number of states of the $256$ pairs of the second.
\item[(ii)] \emph{(As the ascent the counts fail at the first step.)} One step of the transport ascent adjoins one hyperbolic plane and raises the number of pairs of a CAR family of vectors by exactly one (Theorem \claimref{tower.witt-index-quantum-capacity}); $2^{k} = k + 1$ only for $k \in \{0, 1\}$. From three pairs one ascent gives $B_{4}$: four pairs and a module of dimension $16$, against the eight pairs and $256$ states of (i).
\item[(iii)] \emph{(Inside a level the counts fail for every kind of element.)} A CAR family of $m$ pairs in a real algebra $A$ with unit, of finite dimension, generates a copy of $\Mat_{2^{m}}(\R)$ containing the unit, so $4^{m} \le \dim A$. Hence $B_{j}$ holds no CAR family of more than $j$ pairs, of vectors or of any other elements, and a floor $\Cl(p + j, q + j)$ holds none of more than $j + (p+q)/2$ pairs. The $2^{k}$ states of a level are therefore the pairs of a CAR family in $B_{j}$ only for $j \ge 2^{k}$: the level above of (i) is the floor $2^{k}$, by any identification of a basis of $F_{k}$ with its ladder vectors, and the floors strictly between consecutive levels of the reading ($4$ floors between three pairs and eight, $247$ between eight and $256$) are floors of the proved tower that the reading passes over, one wall each (Theorem \claimref{tower.answers-iteration-question}(1)). The construction (i) names the floors $c_{n}$; no stored result on the tower selects them.
\item[(iv)] \emph{(The level above does not inherit the ladder.)} For an endomorphism $X$ of $F_{k}$ with matrix $X_{TS}$ in the states, put $L(X) = \sum_{T,S} X_{TS}V_{T}W_{S}$ in the level above. Then $[L(X), L(Y)] = L([X, Y])$, and $L(X)$ acts on $\Lambda^{\bullet}F_{k}$ as the derivation extending $X$. The lifted ladder is not a CAR family: $L(v_{1})L(w_{1}) + L(w_{1})L(v_{1})$ annihilates the vacuum of the level above, so it is not $1$, for every $k \ge 1$, and $L(v_{1})^{2} \neq 0$ for every $k \ge 2$. The tower's own inclusions $B_{j} \subset B_{j+1}$ keep every relation of the ladder.
\item[(v)] \emph{(Where the horizon count falls.)} With the stored bracket $2^{407} < C < 2^{408}$ for the horizon mode count $C \approx 4.8 \times 10^{122}$ (Theorem \claimref{standard-model.trichotomy-what-kind-number}), $c_{3} = 2^{256} < C < 2^{2^{256}} = c_{4}$, as for every number whose base-two logarithm lies between $256$ and $2^{256}$. On the proved tower a module of at least $C$ states first occurs at the floor $408$, and a CAR family of $C$ pairs at the floor $C$.
\end{enumerate}
So the reading is a true statement about iterating $k \mapsto \dim F_{k}$ and a false one about iterating the ascent: on the proved tower the number of pairs at the floor $j$ is $j$ and only the number of states, $2^{j}$, grows exponentially, so a large number of pairs is not a generic output of the tower.

## technical
The exponential reading of the tower says that the objects of each level are the fermionic pairs of the level above, with counts 3, 8, 256, $2^{256}$. Made precise on the split tower $\Cl(k,k)$, it is the second quantisation of the Fock module: take the $2^{k}$ states of $k$ ladder pairs as the creators of a new set of pairs. As arithmetic this holds exactly: three pairs have eight states, eight pairs have 256, and $2^{256}$ is the number of pairs of the next level. As a statement about the tower the series proves, it fails under each reading tested: one ascent from three pairs gives four pairs and sixteen states; inside the algebra of $j$ pairs no family of more than $j$ anticommuting pairs exists, whether of vectors or of general elements, by a dimension count; and the natural lift of a level's ladder operators to the level above preserves commutators but not the anticommutation relations.

The levels of the reading are therefore the floors 3, 8, 256, $2^{256}$ of the proved tower, with 4 and then 247 floors passed over, each one wall of the iteration theorem, and nothing stored selects those floors. Under the stored bracket for the horizon mode count, $2^{407} < C < 2^{408}$, the count lies between the third and fourth levels of the reading, as does any number with base-two logarithm between 256 and $2^{256}$; on the proved tower that many states need 408 floors and that many pairs need about $4.8 \times 10^{122}$ floors. The checks are exact: ranks of left ideals in $\Cl(3,3)$ and $\Cl(4,4)$, the anticommutation relations of eight state-indexed pairs in $\Cl(8,8)$ and its rank-one vacuum idempotent, non-vector families filling $\Cl(2,2)$ and $\Cl(3,3)$, and the lift for two and three pairs.

## lay
One unproved reading of the programme's tower says each level is built from the level below by an exponential step, giving the counts 3, 8, 256 and then a number with 77 digits, so that huge numbers come for free. This result makes that reading exact and tests it. If the step is "take every state of the level below as a new basic mode", the counts are right: it is a standard construction, but it is not the step the tower's theorems describe. Under the reading that the step is the tower's own, it fails at once: the proved step adds one mode at a time, so three modes become four, not eight, and no cleverer choice of modes inside a level can do better. The exponential levels are just floors number 3, 8 and 256 of the ordinary tower, and nothing in the theory picks them out. So, given the tower as proved, large mode counts are not automatic; only the number of states grows exponentially.

## one-liner
Read as second quantisation of the Fock module ($k$ pairs to $2^{k}$ pairs) the exponential reading gives $3, 8, 256, 2^{256}$ exactly; read as the tower's ascent it fails at the first step ($4$ pairs, not $8$), no level of $j$ pairs holds more than $j$ anticommuting pairs of any elements, the lifted ladder is not fermionic, and the reading's levels are the floors $3, 8, 256$ of the proved tower, selected by no stored result.
