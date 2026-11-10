---
id: synthesis.exponential-reading-of-the-tower-is-the-iterated-fock-functor-not-the-ascent
kind: claim
version: 1
title: 'The exponential reading of the tower: the iterated Fock functor, not a step of the ascent'
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
  - one-relation.two-capacities-three-consequences@6
  - field-theory.second-quantisation@6
  - synthesis.de-sitter-mode-count@3
  - synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping@1
  - std-algebra.existence-uniqueness@1
  - standard-model.trichotomy-what-kind-number@12
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_three_pairs_have_eight_states_and_the_level_above_has_eight_pairs_and_256_states
- kind: check
  ref: check.py::check_one_ascent_from_three_pairs_gives_four_pairs_and_sixteen_states
- kind: check
  ref: check.py::check_non_vector_car_families_fill_the_level_and_a_non_split_floor_exceeds_its_witt_index
- kind: check
  ref: check.py::check_the_lift_of_the_ladder_to_the_level_above_is_lie_and_not_car
- kind: check
  ref: check.py::check_the_quoted_horizon_bracket_lies_between_the_third_and_fourth_levels
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.why-large
  - refuted.the-number-n-is-a-mystery-of-largeness
  - synthesis.invariant-forms-on-the-fock-module-and-the-pair-counts-of-a-next-level
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version kept at 1. The intended citation of the invariant-forms result left in the note is now a named comparison (claimref in clause (iv) and the closing paragraph, lineage entry); it is not a uses edge, since nothing of it is used in a proof step and that result cites this one.'
  note: >-
    Decides the exponential reading of the tower that Observation standard-model.why-large (version 3, conjectured)
    states as unproved and on which refuted.the-number-n-is-a-mystery-of-largeness (version 2) rests. No open problem
    of the store is attached to the number N at present (op.t12-n-after-the-count is settled), so no open_problem
    field is set. The statement is on the split tower over the ground floor of the real numbers, base three real pairs; the
    stored base three is the complex capacity of the space of signature (2,4), whose real capacity is two
    (one-relation.two-capacities-three-consequences), and clause (ii) is stated for both. Clause (iii) settles, for
    the split floors, the question the stored remark note.tower.what-capacity-theorem-forbids leaves outside the
    capacity theorem (mode systems that are not vectors). The sentence that nothing stored selects the floors or a
    rule is argued: a reading of the stored tower results (Fock module, capacity theorem, commuting copies,
    rigidity, limit and iteration theorems), not an audit of the tower region. The bracket for the horizon count is
    quoted: it is stated in the proof of standard-model.trichotomy-what-kind-number and asserted by its check
    (floor of the base-two logarithm 407 for counts between 4.75 and 4.85 times 10^122), the statement levels of
    that entity saying only "about 407", and it stands in the technical level of
    refuted.the-number-n-is-a-mystery-of-largeness from version 3 on (at version 2 in its strength-pass note
    only); it is not recomputed here. The
    closing remark that a large number of pairs is not generic repeats, as a reading, a sentence of that
    entity's technical level (returned to open, status conjectured, on 10 November 2026).
    Transport-essential only in clauses (ii) and (iii), which use the tower's one plane per rung; clauses (i) and
    (iv) are the classical second quantisation of a finite-dimensional space (prior art: the exterior-algebra
    functor and its derivation lift, textbook material cited from memory, for example Bratteli and Robinson,
    Operator Algebras and Quantum Statistical Mechanics 2, section 5.2), placed in the series' algebra. Not decided
    here: readings that use an invariant form of the module, one chirality half, or two-fermion states in place of
    all states. The first of these is treated in synthesis.invariant-forms-on-the-fock-module-and-the-pair-counts-of-a-next-level
    (under the module's invariant symmetric form the eight states of three pairs are the vectors of four pairs, a
    Witt index that equals the pair count of the tower's next floor as a number only, and the counts run 3, 4, 8,
    128, 2^127). It is named for comparison in clause (iv) and the closing paragraph and is recorded in lineage,
    not as a premise: nothing of it is used in a proof step here, and that result cites this one as the base
    statement of the reading in the form (i).
---

## formal
Let $B_{k} = \Cl(k,k)$ be the algebra of $k$ ladder pairs $v_{i}, w_{i}$ (Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}) and $F_{k} = \Lambda^{\bullet}W_{k}$ its Fock module, of dimension $2^{k}$, with the basis of states $v_{S}$, $S \subseteq \{1, \dots, k\}$ (Theorem \claimref{tower.fock-module-one-qubit-per-rung}). Call a family $(a_{i}, b_{i})_{i \le m}$ of elements of a real associative algebra with unit a \emph{CAR family} if $a_{i}a_{j} + a_{j}a_{i} = 0$, $b_{i}b_{j} + b_{j}b_{i} = 0$ and $a_{i}b_{j} + b_{j}a_{i} = \delta_{ij}$. The exponential reading of Observation \claimref{standard-model.why-large} (each level's objects are the fermionic pairs of the level above, with counts $3$, $8$, $256$, $2^{256}$) has the following precise forms, on the split tower $B_{0} = \R \subset B_{1} \subset B_{2} \subset \cdots$, with the base level taken as $B_{3} = \Cl(3,3)$, three real pairs. The base three of the stored reading is the complex capacity of the space of signature $(2,4)$, whose real capacity is two (Theorem \claimref{one-relation.two-capacities-three-consequences}); clauses (i), (iii) and (iv) use only dimensions and hold for the complexified floors with complex dimensions, and from a base of two real pairs the recursion of (i) would read $2, 4, 16, 65536$.
\begin{enumerate}
\item[(i)] \emph{(Under the rule "states become creators" the counts hold.)} Let the level above $B_{k}$ be the Clifford algebra of $F_{k} \oplus F_{k}^{*}$ with the form $Q(x + \phi) = \phi(x)$: the states become creators and as many annihilators are adjoined. The states $V_{S} = v_{S}$ and the dual basis $W_{S}$ are a CAR family of $2^{k}$ vectors, so this algebra is $B_{2^{k}}$ and its Fock module is $\Lambda^{\bullet}F_{k}$, of dimension $2^{2^{k}}$. Iterating from $c_{0} = 3$ gives $c_{n+1} = 2^{c_{n}}$: $3$, $8$, $256$, $2^{256}$. Under this rule $2^{256}$ is the number of ladder pairs of the third level above the base, equal to the number of states of the $256$ pairs of the second.
\item[(ii)] \emph{(The step of (i) is not a step of the ascent.)} One step of the transport ascent adjoins one hyperbolic plane and raises the number of pairs of a CAR family of vectors by exactly one (Theorem \claimref{tower.witt-index-quantum-capacity}); $2^{k} = k + 1$ only for $k \in \{0, 1\}$. From three pairs one ascent gives $B_{4}$: four pairs and a module of dimension $16$, against the eight pairs and $256$ states of (i). The same holds for the stored complex base: the complex capacity also rises by one per ascent, so three complex pairs become four (Theorem \claimref{one-relation.two-capacities-three-consequences}). The level above of (i) is reached from $B_{k}$ by $2^{k} - k$ ascents.
\item[(iii)] \emph{(Inside a level the counts fail for every kind of element.)} A CAR family of $m$ pairs in a real associative algebra $A$ with unit, of finite dimension, generates a copy of $\Mat_{2^{m}}(\R)$ containing the unit, so $4^{m} \le \dim A$. Hence $B_{j}$ holds no CAR family of more than $j$ pairs, of vectors or of any other elements, and a floor $\Cl(p + j, q + j)$ holds none of more than $j + (p+q)/2$ pairs; this last is a bound, equal to the stored complex capacity, not a count, and on a floor that is not split families of elements that are not vectors can exceed the Witt index (in $\Cl(2,0)$, of Witt index zero, $a = \tfrac12(e_{1} + e_{1}e_{2})$, $b = \tfrac12(e_{1} - e_{1}e_{2})$ is a CAR pair). The $2^{k}$ states of a level are therefore the pairs of a CAR family in $B_{j}$ only for $j \ge 2^{k}$: the level above of (i) is the floor $2^{k}$, by any identification of a basis of $F_{k}$ with its ladder vectors, and the floors strictly between consecutive levels of the reading ($4$ floors between three pairs and eight, $247$ between eight and $256$) are floors of the same tower that the reading passes over. The construction (i) names the floors $c_{n}$; no stored result on the tower selects them (argued, from a reading of the stored tower results and not from an audit of the tower region).
\item[(iv)] \emph{(The level above does not inherit the ladder through the second-quantised lift.)} For an endomorphism $X$ of $F_{k}$ with matrix $X_{TS}$ in the states, put $L(X) = \sum_{T,S} X_{TS}V_{T}W_{S}$ in the level above (the lift that Theorem \claimref{field-theory.second-quantisation} names for the field algebra). Then $[L(X), L(Y)] = L([X, Y])$, and $L(X)$ acts on $\Lambda^{\bullet}F_{k}$ as the derivation extending $X$. The lifted ladder is not a CAR family: $L(v_{1})L(w_{1}) + L(w_{1})L(v_{1})$ annihilates the vacuum of the level above, so it is not $1$, for every $k \ge 1$, and $L(v_{1})^{2} \neq 0$ for every $k \ge 2$. The tower's own inclusions $B_{j} \subset B_{j+1}$ keep every relation of the ladder. This clause concerns the lift $L$ only: whether $F_{k}$ carries other structure that makes its states vectors of a next level, such as an invariant bilinear form, is a separate question, not treated here, and such a rule gives other counts than (i) (Theorem \claimref{synthesis.invariant-forms-on-the-fock-module-and-the-pair-counts-of-a-next-level}(v)).
\item[(v)] \emph{(Where the horizon count falls, as a comparison of sizes only.)} The horizon count is $|J| = \pi N^{2}/\ln 2 \approx 4.8 \times 10^{122}$ (Theorem \claimref{synthesis.de-sitter-mode-count}); the store quotes $2^{407} < |J| < 2^{408}$ (the check of Theorem \claimref{standard-model.trichotomy-what-kind-number} and the technical level of the stored entry on largeness; quoted, not recomputed here). Given that bracket, $c_{3} = 2^{256} < |J| < 2^{2^{256}} = c_{4}$, as for every number whose base-two logarithm lies between $256$ and $2^{256}$; and a module of at least $|J|$ states first occurs at the floor $408$. The comparison is of sizes only: the stored count is of registered units averaging two arrays, not of ladder pairs or rungs, and no single ladder pair qualifies as a unit (Theorem \claimref{synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping}); the trichotomy's "one qubit per rung" is a statement of units.
\end{enumerate}
So the reading, under the rule of (i), is a true statement about iterating $k \mapsto \dim F_{k}$ and a false one about a step of the ascent: its levels are the floors $3$, $8$, $256$ of the one tower, reached by $2^{k} - k$ ascents each. The rule of (i) is one of at least two counting rules with a claim to the stored wording (a rule through an invariant form of the module gives other counts, Theorem \claimref{synthesis.invariant-forms-on-the-fock-module-and-the-pair-counts-of-a-next-level}(v)), and nothing stored selects one of them (argued, on the same reading of the stored tower results). As a reading, not a theorem: on the proved tower the number of pairs at the floor $j$ is $j$ and only the number of states, $2^{j}$, grows exponentially, so a large number of pairs is not singled out by the tower; the stored entry on largeness says the same in its technical level.

## technical
The exponential reading of the tower says that the objects of each level are the fermionic pairs of the level above, with counts 3, 8, 256, $2^{256}$. Made precise on the split tower $\Cl(k,k)$ under the rule that the $2^{k}$ states of $k$ ladder pairs become the creators of a new set of pairs, with as many annihilators adjoined, it is the second quantisation of the Fock module, and as arithmetic it holds exactly: three pairs have eight states, eight pairs have 256, and $2^{256}$ is the number of pairs of the next level. That step is not a step of the tower's ascent: one ascent from three pairs gives four pairs and sixteen states (for three real pairs and for the stored complex count on signature $(2,4)$ alike). Inside the algebra of $j$ pairs no family of more than $j$ anticommuting pairs exists, whether of vectors or of general elements, by a dimension count valid for any real associative algebra; on floors that are not split this is only a bound. And the second-quantised lift of a level's ladder operators to the level above preserves commutators but not the anticommutation relations (other structure on the module, such as an invariant form, is not treated and gives other counts).

The levels of the reading are therefore the floors 3, 8, 256, $2^{256}$ of the proved tower, with 4 and then 247 floors passed over. That nothing stored selects those floors, or this rule over another, is argued from a reading of the stored tower results, not from an audit. Given the stored bracket for the horizon count, $2^{407} < |J| < 2^{408}$, the count lies between the third and fourth levels of the reading, as does any number with base-two logarithm between 256 and $2^{256}$; this compares sizes only, since the stored count is of registered units and not of ladder pairs. The checks are exact: ranks of left ideals in $\Cl(3,3)$ and $\Cl(4,4)$, the anticommutation relations of eight state-indexed pairs in $\Cl(8,8)$ and its rank-one vacuum idempotent, non-vector families filling $\Cl(2,2)$ and $\Cl(3,3)$, a non-vector pair in $\Cl(2,0)$, and the lift for two and three pairs.

## lay
One unproved reading of the programme's tower says each level is built from the level below by an exponential step, giving the counts 3, 8, 256 and then a number with 77 digits, so that huge numbers come for free. This result makes that reading exact and tests it. Under the rule "take every state of the level below as a new basic mode", the counts are right: it is a standard construction, but it is not a step of the kind the tower's theorems describe. The proved step adds one mode at a time, so three modes become four, not eight, and no cleverer choice of modes inside a level can do better. The exponential levels are floors number 3, 8 and 256 of the ordinary tower. On our reading of the stored results, which is an argument and not a complete audit, nothing in the theory picks those floors out, and this rule is only one of at least two that fit the original wording. The test is done for three real modes; the three of the original reading is a count over complex numbers on a space whose real count is two, and for it too one step gives four. So, given the tower as proved, only the number of states grows exponentially; the number of modes grows one at a time.

## one-liner
Under the rule that states become creators ($k$ pairs to $2^{k}$ pairs; here on three real pairs, $\Cl(3,3)$, the stored base three being a complex count on signature $(2,4)$ of real Witt index two) the exponential reading gives $3, 8, 256, 2^{256}$ exactly; that step is not a step of the tower's ascent ($4$ pairs, not $8$), no level of $j$ pairs holds more than $j$ anticommuting pairs of any elements, the lifted ladder is not fermionic, and the reading's levels are the floors $3, 8, 256$ of the proved tower, selected by no stored result (argued, from a reading of the tower results, not an audit).
