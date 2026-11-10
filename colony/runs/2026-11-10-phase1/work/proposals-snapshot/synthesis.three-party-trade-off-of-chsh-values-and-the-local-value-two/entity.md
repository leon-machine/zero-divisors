---
id: synthesis.three-party-trade-off-of-chsh-values-and-the-local-value-two
kind: claim
version: 1
title: 'Three-party trade-off of CHSH values under positivity (P), and the values 2 and 4'
status: proved
region: synthesis
subject: clifford-structure
tags: [entanglement, measurement-and-records, classical-theorem, superselection]
proposed_by:
  kind: ai
  session: 2026-11-10-phase1
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase1
review: draft
derivations:
- name: main
  uses:
  - synthesis.signed-directions-and-the-integer-clifford-algebra@2
  - synthesis.division-gives-the-rationals@2
  - synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate@1
  - tower.commuting-copies@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_sum_and_difference_of_two_observables_anticommute
- kind: check
  ref: check.py::check_two_chsh_values_sharing_a_party_have_squares_summing_to_at_most_eight
- kind: check
  ref: check.py::check_commuting_directions_give_square_four_and_values_two
- kind: check
  ref: check.py::check_pair_state_value_and_what_it_leaves_a_third_party
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product
  - singularity.eviction-window-thermal-product-radiation-entropy
extraction:
  note: >-
    Companion to the stored CHSH bound: does the same anticommutation give a monogamy statement for three
    parties, and where do the values 2, $2\sqrt{2}$ and 4 sit? Kill condition registered before computing: an
    exact three-party state with the two squared CHSH values summing to more than 8 for self-adjoint commuting
    settings, or commuting directions on one side with squared value above 4 (neither fired). Everything is
    under Hypothesis (P) of the stored bound, which has been adopted as a postulate and is to become an assumes
    edge. Status: classical mathematics. The quadratic trade-off is the monogamy relation of Toner and
    Verstraete (arXiv:quant-ph/0611001, Theorem 1, checked on the web in this run: for a state of arbitrary
    dimension, with the shared party's measurements the same in both expressions, and tight for all pairs of
    values on the circle). Here only the points $(2, 2)$ over the rationals and, by the stored bound,
    $(\pm 2\sqrt{2}, 0)$ with a square root of two are exhibited; whether the whole arc is reached by rational
    states is not examined. The method, bounding the sum of squared values of anticommuting observables, is the
    correlation complementarity of Kurzynski, Paterek, Ramanathan, Laskowski and Kaszlikowski (arXiv:1010.2012,
    checked on the web), who derive Bell monogamy relations from it for qubits. The arrangement here uses only
    that the sum and the difference of two elements of square one anticommute, so it needs no qubit structure, no
    dimension and no square root; it is not claimed as new. No step of the proof uses real coefficients. Two
    settings are recorded side by side and neither is called the physical one: clauses (i) to (iii) are
    signature-free and apply to parity-even observables with two modes for each party, which need no twist;
    clauses (iv) and (v) are in the one-mode Klein-twisted realisation, whose directions are odd under the total
    parity, with two nested twists, both instances of the stored commuting-copies twist (the second with the
    first two modes as the planes). The pair state of clause (v) is written out and verified there, so no edge
    to the stored mode-split theorem is used; it is the element that theorem's clause (v) reads as an eviction
    pair. Remark (horizon), not a result: if (a) the eviction pairs of the stored account are read as these pair
    states (the stored pair-state reading), (b) the shared window mode uses the same two directions $p_{1}$,
    $e_{1}$ in both tests, and (c) the parity-odd elements $e_{1}$, $e_{2}p_{1}$ count as observables, then by
    clause (v) a window mode whose pair with its partner has squared value close to $4(2 - r^{2})$ leaves any
    third party a squared value of at most about $4r^{2} < 4$, the quantitative form for CHSH values of the
    monogamy discussed in the stored note note.singularity.monogamy-firewalls-small-corrections-theorem. Under
    parity superselection, with only parity-even observables, one window mode has no CHSH value above 2 at all
    and the remark is empty. Transport-absent.
---

## formal
Notation, hypotheses and clause numbers of Theorem \claimref{synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate} (the base) are used: $k$ is $\Q$ or any ordered field, $\Cl_{k}(p,q)$ the Clifford algebra of Theorem \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra} with coefficients in $k$ (Theorem \claimref{synthesis.division-gives-the-rationals}), $\dagger$ the linear extension of the inverse on blades, an \emph{observable} an $x$ with $x^{\dagger} = x$, $x^{2} = 1$, and \emph{Hypothesis (P), positivity of values:} values are given by a \emph{state}, a $k$-linear $\omega : \Cl_{k}(p,q) \to k$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(x^{\dagger}) = \omega(x)$ for all $x$; (P) is assumed, not derived. The adjoint is defined by the chosen generators. In definite signature it does not depend on the orthonormal frame; in indefinite signature it depends on the split into generators of square $1$ and of square $-1$, so observables, states and (P) are relative to that split, and each statement holds for every fixed split. Let $A_{1}, A_{2}$; $B_{1}, B_{2}$; $D_{1}, D_{2}$ be observables such that elements of different pairs commute, and
\[
C_{AB} = A_{1}(B_{1} + B_{2}) + A_{2}(B_{1} - B_{2}), \qquad C_{AD} = A_{1}(D_{1} + D_{2}) + A_{2}(D_{1} - D_{2}), \qquad A_{\pm} = A_{1} \pm A_{2} .
\]
The shared party uses \emph{the same} two observables $A_{1}, A_{2}$ in both CHSH elements; every statement below about two CHSH values is under this condition.
\begin{enumerate}
\item[(i)] \emph{(The diagonals anticommute; proved.)} $A_{+}A_{-} + A_{-}A_{+} = 0$, $A_{+}^{2} + A_{-}^{2} = 4$, and $C_{AB} = A_{+}B_{1} + A_{-}B_{2}$, $C_{AD} = A_{+}D_{1} + A_{-}D_{2}$. The self-adjoint elements $A_{+}B_{1}$ and $A_{-}D_{2}$ anticommute, as do $A_{-}B_{2}$ and $A_{+}D_{1}$, and $(\lambda A_{+}B_{1} + \mu A_{-}D_{2})^{2} = \lambda^{2}A_{+}^{2} + \mu^{2}A_{-}^{2}$ for scalars $\lambda, \mu$.
\item[(ii)] \emph{(Trade-off, under (P), same $A_{1}, A_{2}$ in both; proved.)} For every state
\[
\omega(C_{AB})^{2} + \omega(C_{AD})^{2} \le 8 .
\]
So the two CHSH values that share party $A$ with the same two observables cannot both exceed $2$ in absolute value, and $\omega(C_{AB})^{2} = 8$ forces $\omega(C_{AD}) = 0$ for every third pair tested with the same $A_{1}, A_{2}$. This clause uses of (P) only $\omega(xx^{\dagger}) \ge 0$ and $\omega(1) = 1$.
\item[(iii)] \emph{(The values $2$ and $4$, under (P); proved.)} If $A_{1}A_{2} = A_{2}A_{1}$ then $C_{AB}^{2} = 4$ and $\omega(C_{AB})^{2} \le 4$ (base, clause (iii)). If all four of $A_{1}, A_{2}, B_{1}, B_{2}$ lie in a commutative subalgebra spanned by orthogonal self-adjoint idempotents $q_{1}, \dots, q_{m}$ with sum $1$, then $C_{AB} = \sum_{i}\gamma_{i}q_{i}$ with every $\gamma_{i} \in \{2, -2\}$, and $\omega(C_{AB})$ is an average of these with the weights $\omega(q_{i}) \ge 0$. For arbitrary commuting observables $\omega(A_{i}B_{j})^{2} \le 1$, so $|\omega(C_{AB})| \le 4$. Under (P) and for observables the value $4$ is not reached (base, clause (iii)); it is reached when positivity is dropped (base, clause (v)) and exceeded when self-adjointness is dropped (base, clause (vi)).
\item[(iv)] \emph{(Three modes of $\Cl_{\Q}(3,3)$ with nested Klein twists and parity-odd directions; proved, the sample values computed.)} With generators $e_{j}, f_{j}$ ($Q(e_{j}) = 1$, $Q(f_{j}) = -1$) and $p_{j} = f_{j}e_{j}$, the three pairs $\{e_{1}, p_{1}\}$, $\{e_{2}p_{1}, p_{2}\}$, $\{e_{3}p_{1}p_{2}, p_{3}\}$ consist of anticommuting observables and commute across pairs: the second and third are twists of modes $2$ and $3$ by $p_{1}$ and by $p_{1}p_{2}$, as in Theorem \claimref{tower.commuting-copies} with one and with two planes, and with the single factor $p_{1}$ in place of $p_{1}p_{2}$ the third pair would not commute with the second. The elements $e_{1}$, $e_{2}p_{1}$, $e_{3}p_{1}p_{2}$ are odd under the total parity. For the state $\omega_{\rho}$, $\rho \propto (1 + e_{1}\,e_{2}p_{1})(1 + e_{1}\,e_{3}p_{1}p_{2})(1 + p_{1}p_{2}p_{3})$, and the settings $A = (e_{1}, p_{1})$, $B_{1} = B_{2} = e_{2}p_{1}$, $D_{1} = D_{2} = e_{3}p_{1}p_{2}$ the two values are $(2, 2)$: the bound of (ii) is attained over $\Q$. With $I_{B} = e_{2}p_{1}p_{2}$, $I_{D} = e_{3}p_{1}p_{2}p_{3}$ and $y = (1 + \tfrac15I_{B})(1 - \tfrac14I_{D})$, the state of $y\rho y^{\dagger}$ has, at the same settings, the values $(\tfrac{24}{13}, \tfrac{30}{17})$, both nonzero, with sum of squares $\tfrac{318564}{48841} < 8$ (computed). The pure state of modes $1, 2$
\[
\rho_{AB} = \tfrac45\,y'\rho_{0}y'^{\dagger}, \qquad \rho_{0} = \tfrac14(1 + e_{1}\,e_{2}p_{1})(1 - p_{1}p_{2}), \qquad y' = 1 - \tfrac12e_{2}p_{1}p_{2},
\]
has value $\tfrac{14}{5}$ at the blade settings $(e_{1}, p_{1}; e_{2}p_{1}, p_{2})$ (it is not the pair state of clause (v), whose value at the blade settings is at most $2$); so for every state $\omega$ with $\omega(C_{AB}) = \tfrac{14}{5}$, for instance that of $\rho_{AB}\cdot\tfrac12(1 + p_{3})$, every CHSH value of the same $A_{1}, A_{2}$ with a third pair has square at most $8 - (\tfrac{14}{5})^{2} = \tfrac{4}{25}$; for the instance named the values with party $D$ at rational directions are all $0$.
\item[(v)] \emph{(What a pair state leaves a third party, same $A_{1}, A_{2}$ in both; proved, with a computed instance.)} If $\omega(C_{AB}) = S$ then $\omega(C_{AD})^{2} \le 8 - S^{2}$ for every third pair tested with the same $A_{1}, A_{2}$. For \emph{amplitudes} $c, s$ with $c^{2} + s^{2} = 1$ and $r = c^{2} - s^{2}$, the pair state of modes $1, 2$ with amplitude $c$ on $\ket{00}$ and $s$ on $\ket{11}$ is
\[
\rho_{c,s} = \tfrac14(1 + p_{1}p_{2})(1 + rp_{1}) + cs\,(w_{1}w_{2} + v_{2}v_{1}), \qquad v_{j} = \tfrac12(e_{j} + f_{j}), \quad w_{j} = \tfrac12(e_{j} - f_{j}),
\]
a self-adjoint idempotent with $\langle\rho_{c,s}\rangle_{0} = \tfrac14$ (the element that the stored account reads as an eviction pair). Its correlations in the directions of the two parties are $\omega(e_{1}\,e_{2}p_{1}) = 2cs$, $\omega(p_{1}p_{2}) = 1$, $\omega(e_{1}p_{2}) = \omega(p_{1}\,e_{2}p_{1}) = 0$, and the settings $(p_{1}, e_{1}; zp_{2} + x\,e_{2}p_{1}, zp_{2} - x\,e_{2}p_{1})$, $x^{2} + z^{2} = 1$, have value $S = 2(z + 2cs\,x)$, with $S^{2} \le 4(1 + 4c^{2}s^{2}) = 4(2 - r^{2})$. At amplitudes $(c, s) = (\tfrac35, \tfrac45)$ and direction $(x, z) = (\tfrac{20}{29}, \tfrac{21}{29})$: $S = \tfrac{402}{145}$, so a third pair tested with the same $(p_{1}, e_{1})$ is left $\omega(C_{AD})^{2} \le \tfrac{6596}{21025}$, against $4r^{2} = \tfrac{196}{625}$ in the limit of the best directions.
\end{enumerate}

## technical
When one party shares correlations with two others, the two Clauser-Horne-Shimony-Holt values are not independent: with the shared party's two quantities the same in both, the sum of their squares is at most $8$, the Toner-Verstraete relation. Here it is proved in the rational Clifford algebra of the foundation, for commuting self-adjoint elements of square one, under Hypothesis (P) of the stored CHSH bound, positivity of values: values are given by a state, a linear functional $\omega$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(x^{\dagger}) = \omega(x)$ for all $x$; (P) is assumed, not derived. The proof uses one fact about the shared party: the sum and the difference of its two quantities anticommute, like the diagonals of a rhombus, and their squares add to $4$. Each CHSH element is a sum of two products with these diagonals, the products pair up across the two CHSH elements into anticommuting pairs, and for anticommuting self-adjoint elements the squared values add up to at most the value of the sum of the squares. No dimension and no square root enters, and no step uses real coefficients. For quantities in a commutative subalgebra the combination takes the values $\pm 2$ on its points; the bound $4$ for the square when one party's quantities commute, the fact that $4$ is not reached under the hypothesis, that it is reached without positivity and exceeded without self-adjointness, are the stored bound's.

Two settings are recorded side by side. The general statement applies to parity-even observables with two modes for each party, which need no twist. The realisation given here is the other one: three modes of the split-signature algebra with two nested Klein twists and directions that are odd under the total parity. There the bound is attained over the rationals at the point $(2, 2)$, and a state entangled across all three parties with values $(24/13, 30/17)$ is given. A pair of modes in the pair state with amplitudes $c$, $s$ has squared value up to $4(2 - r^{2})$, $r = c^{2} - s^{2}$, and so leaves a third party tested with the same two quantities of the shared mode a squared value of at most about $4r^{2}$, below the local value (remark, resting on the stored pair-state reading of the eviction pairs and on parity-odd elements counting as observables; under parity superselection it is empty).

## lay
If one experimenter shares strong quantum correlations with a second, there is less left to share with a third. For the standard measure of such correlations the rule is exact, provided the shared experimenter uses the same two measurements in both comparisons: the squares of the two values add up to at most 8, so if one pair reaches the quantum maximum the other pair, tested with those same two measurements, shows no correlation of this kind at all, and two pairs can never both beat the limit of 2 that holds for a world of pre-existing answers. This is a known theorem. Here it is proved inside the algebra of directions that the series builds from its simplest assumptions, using only fractions, from one geometric fact: the sum and the difference of two unit directions are perpendicular. The proof assumes the rule called (P), positivity of values: averages are given by a rule that is linear, gives the trivial measurement the value 1, never gives a quantity times its mirror image a negative average, and gives a quantity and its mirror image the same average; this is assumed, not derived. The result also places the three familiar numbers: 2 for measurements that do not interfere with each other, 2 times the square root of 2 as the quantum maximum, and 4 as a value that no allowed assignment of averages reaches.

## one-liner
Under (P), for three mutually commuting pairs of self-adjoint square-one elements of a rational Clifford algebra, with the shared pair the same in both CHSH elements, the sum and difference of the shared pair anticommute and $\omega(C_{AB})^{2} + \omega(C_{AD})^{2} \le 8$ (attained at $(2,2)$ over $\Q$ on three modes of $\Cl(3,3)$ with nested Klein twists and parity-odd directions); in a commutative subalgebra $C = \pm 2$ on each point, and the value $4$ is never reached.
