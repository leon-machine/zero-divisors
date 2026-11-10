---
id: synthesis.three-party-trade-off-of-chsh-values-and-the-local-value-two
kind: claim
version: 1
title: 'Three-party trade-off of CHSH values under positivity, and the values 2 and 4'
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
  - synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product@1
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
    Companion to the CHSH bound of the same run (sibling result, intended citation once stored): does the same
    anticommutation give a monogamy statement for three parties, and where do the values 2, $2\sqrt{2}$ and 4
    sit? Kill condition registered before computing: an exact three-party state with the two squared CHSH values
    summing to more than 8 for self-adjoint commuting settings, or commuting directions on one side with squared
    value above 4 (neither fired). Status: classical mathematics. The quadratic trade-off is the monogamy
    relation of Toner and Verstraete (arXiv:quant-ph/0611001; cited from memory, the page could not be opened in
    this run). The method, bounding the sum of squared values of anticommuting observables, is the correlation
    complementarity of Kurzynski, Paterek, Ramanathan, Laskowski and Kaszlikowski (arXiv:1010.2012, checked on
    the web), who derive Bell monogamy relations from it for qubits. The arrangement here uses only that the sum
    and the difference of two elements of square one anticommute, so it needs no qubit structure, no dimension
    and no square root, and holds for every functional satisfying the positivity hypothesis; it is not claimed
    as new. The whole statement rests on that hypothesis, which is not derived from the foundation postulates
    (a sibling result exhibits a normalised functional violating it with CHSH value 4). The realisation in
    clause (iv) uses directions that are odd under the total parity and two nested Klein twists, both instances
    of clause (ii) of the stored mode-split theorem (the second with the first two modes as the untwisted set);
    with parity-even observables only, each party needs two modes and no twist, and clauses (i) to (iii) apply
    unchanged. Whether the whole arc of the trade-off between the points found is reached by rational states is
    not examined. Remark for the stored account of the horizon: by clause (v), a window mode whose pair state
    with its partner has squared value close to $4(2 - r^{2})$ leaves any third party a squared value of at most
    about $4r^{2} < 4$, below the local value; this is the quantitative form, for CHSH values, of the monogamy
    that the stored note note.singularity.monogamy-firewalls-small-corrections-theorem discusses, and it is a
    remark, not a statement about that note's theorem. Transport-absent.
---

## formal
Let $k$ be $\Q$ or any ordered field and $\Cl_{k}(p,q)$ the Clifford algebra of Theorem \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra} with coefficients in $k$ (Theorem \claimref{synthesis.division-gives-the-rationals}), $\dagger$ the linear extension of the inverse on blades. An \emph{observable} is an $x$ with $x^{\dagger} = x$, $x^{2} = 1$. \emph{Hypothesis (P), positivity of values:} values are given by a \emph{state}, a $k$-linear $\omega$ with $\omega(1) = 1$ and $\omega(xx^{\dagger}) \ge 0$ for all $x$; (P) is assumed, not derived, and every inequality below is a statement about functionals satisfying it. Let $A_{1}, A_{2}$; $B_{1}, B_{2}$; $D_{1}, D_{2}$ be observables such that elements of different pairs commute, and
\[
C_{AB} = A_{1}(B_{1} + B_{2}) + A_{2}(B_{1} - B_{2}), \qquad C_{AD} = A_{1}(D_{1} + D_{2}) + A_{2}(D_{1} - D_{2}), \qquad A_{\pm} = A_{1} \pm A_{2} .
\]
\begin{enumerate}
\item[(i)] \emph{(The diagonals anticommute; proved.)} $A_{+}A_{-} + A_{-}A_{+} = 0$, $A_{+}^{2} + A_{-}^{2} = 4$, and $C_{AB} = A_{+}B_{1} + A_{-}B_{2}$, $C_{AD} = A_{+}D_{1} + A_{-}D_{2}$. The self-adjoint elements $A_{+}B_{1}$ and $A_{-}D_{2}$ anticommute, as do $A_{-}B_{2}$ and $A_{+}D_{1}$, and $(\lambda A_{+}B_{1} + \mu A_{-}D_{2})^{2} = \lambda^{2}A_{+}^{2} + \mu^{2}A_{-}^{2}$ for scalars $\lambda, \mu$.
\item[(ii)] \emph{(Trade-off, under (P); proved.)} For every state
\[
\omega(C_{AB})^{2} + \omega(C_{AD})^{2} \le 8 .
\]
So the two CHSH values that share party $A$ cannot both exceed $2$ in absolute value, and $\omega(C_{AB})^{2} = 8$ forces $\omega(C_{AD}) = 0$ for every third party. Taken alone, the same argument gives $\omega(C_{AB})^{2} \le 8$.
\item[(iii)] \emph{(The values $2$ and $4$, under (P); proved.)} If $A_{1}A_{2} = A_{2}A_{1}$ then $C_{AB}^{2} = 4$ and $\omega(C_{AB})^{2} \le 4$ for every state. If all four of $A_{1}, A_{2}, B_{1}, B_{2}$ lie in a commutative subalgebra spanned by orthogonal self-adjoint idempotents $q_{1}, \dots, q_{m}$ with sum $1$, then $C_{AB} = \sum_{i}\gamma_{i}q_{i}$ with every $\gamma_{i} \in \{2, -2\}$, and $\omega(C_{AB})$ is an average of these with the weights $\omega(q_{i}) \ge 0$. For arbitrary observables $\omega(A_{i}B_{j})^{2} \le 1$, so $|\omega(C_{AB})| \le 4$, and by (ii) the value $4$ is not reached by any state: $2$ is the bound for commuting directions, $8$ the bound for the square in general, and $4$ is reached only by functionals that violate (P) or by elements that are not self-adjoint.
\item[(iv)] \emph{(Three modes of $\Cl_{\Q}(3,3)$; proved, the sample values computed.)} With generators $e_{j}, f_{j}$ ($Q(e_{j}) = 1$, $Q(f_{j}) = -1$) and $p_{j} = f_{j}e_{j}$, the three pairs $\{e_{1}, p_{1}\}$, $\{e_{2}p_{1}, p_{2}\}$, $\{e_{3}p_{1}p_{2}, p_{3}\}$ consist of anticommuting observables and commute across pairs: the second and third are Klein twists of modes $2$ and $3$ by $p_{1}$ and by $p_{1}p_{2}$ (clause (ii) of Theorem \claimref{synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product}, applied with untwisted sets $\{1\}$ and $\{1,2\}$), and with the single factor $p_{1}$ in place of $p_{1}p_{2}$ the third pair would not commute with the second. The elements $e_{1}$, $e_{2}p_{1}$, $e_{3}p_{1}p_{2}$ are odd under the total parity. For the state $\rho \propto (1 + e_{1}\,e_{2}p_{1})(1 + e_{1}\,e_{3}p_{1}p_{2})(1 + p_{1}p_{2}p_{3})$ and the settings $A = (e_{1}, p_{1})$, $B_{1} = B_{2} = e_{2}p_{1}$, $D_{1} = D_{2} = e_{3}p_{1}p_{2}$ the two values are $(2, 2)$: the bound of (ii) is attained over $\Q$. For the pair state of parties $A$, $B$ with value $\tfrac{14}{5}$ at the blade settings, times any state of mode $3$, every CHSH value of $A$ with $D$ at rational directions has square at most $8 - (\tfrac{14}{5})^{2} = \tfrac{4}{25}$.
\item[(v)] \emph{(What a pair state leaves a third party; proved, with a computed instance.)} If $\omega(C_{AB}) = S$ then $\omega(C_{AD})^{2} \le 8 - S^{2}$ for every third pair. For the pair state of clause (v) of the mode-split Theorem with weights $c, s$ ($c^{2} + s^{2} = 1$, $r = c^{2} - s^{2}$) on modes $1, 2$, the correlations of the directions are $\omega(e_{1}\,e_{2}p_{1}) = 2cs$, $\omega(p_{1}p_{2}) = 1$, $\omega(e_{1}p_{2}) = \omega(p_{1}\,e_{2}p_{1}) = 0$, and the settings $(p_{1}, e_{1}; zp_{2} + x\,e_{2}p_{1}, zp_{2} - x\,e_{2}p_{1})$, $x^{2} + z^{2} = 1$, have value $S = 2(z + 2cs\,x)$, with $S^{2} \le 4(1 + 4c^{2}s^{2}) = 4(2 - r^{2})$. At $(c, s) = (\tfrac35, \tfrac45)$, $(x, z) = (\tfrac{20}{29}, \tfrac{21}{29})$: $S = \tfrac{402}{145}$, so a third party is left $\omega(C_{AD})^{2} \le \tfrac{6596}{21025}$, against $4r^{2} = \tfrac{196}{625}$ in the limit of the best directions.
\end{enumerate}

## technical
When one party shares correlations with two others, the two Clauser-Horne-Shimony-Holt values are not independent: the sum of their squares is at most $8$, the Toner-Verstraete relation. Here it is proved in the rational Clifford algebra of the foundation, for commuting self-adjoint elements of square one, under the hypothesis that values are given by a linear normalised functional that is non-negative on squares $xx^{\dagger}$; that hypothesis is assumed and not derived. The proof uses one fact about the shared party: the sum and the difference of its two quantities anticommute, like the diagonals of a rhombus, and their squares add to $4$. Each CHSH element is a sum of two products with these diagonals, the products pair up across the two CHSH elements into anticommuting pairs, and for anticommuting self-adjoint elements the squared values add up to at most the value of the sum of the squares. No dimension, no square root and no completion of the coefficients enters. The same computation gives the bound $8$ for a single pair, the bound $4$ for the square when one party's quantities commute (the local value $2$, with values exactly $\pm 2$ on the points of a commutative subalgebra), and shows that the trivial bound $4$ is never reached under the hypothesis.

A realisation with three modes of the split-signature algebra needs two nested Klein twists, both covered by the stored twist, and uses directions that are odd under the total parity; with parity-even observables each party needs two modes and no twist, and the general statement applies unchanged. The bound is attained over the rationals at the point $(2, 2)$. A pair of modes in the stored pair state with weights $c$, $s$ has squared value up to $4(2 - r^{2})$, $r = c^{2} - s^{2}$, and so leaves a third party a squared value of at most about $4r^{2}$, below the local value.

## lay
If one experimenter shares strong quantum correlations with a second, there is less left to share with a third. For the standard measure of such correlations the rule is exact: the squares of the two values add up to at most 8, so if one pair reaches the quantum maximum the other pair shows no correlation of this kind at all, and two pairs can never both beat the limit of 2 that holds for a world of pre-existing answers. This is a known theorem. Here it is proved inside the algebra of directions that the series builds from its simplest assumptions, using only fractions, from one geometric fact: the sum and the difference of two unit directions are perpendicular. The proof assumes, as the companion result does, that averages never give a square a negative value; that assumption is not derived. The result also places the three familiar numbers: 2 for measurements that do not interfere with each other, 2 times the square root of 2 as the quantum maximum, and 4 as a value that no allowed assignment of averages reaches.

## one-liner
Under the hypothesis that values are a linear normalised functional non-negative on $xx^{\dagger}$, for three mutually commuting pairs of self-adjoint square-one elements of a rational Clifford algebra the sum and difference of the shared pair anticommute and $\omega(C_{AB})^{2} + \omega(C_{AD})^{2} \le 8$ (attained at $(2,2)$ over $\Q$ on three modes of $\Cl(3,3)$ with nested Klein twists and parity-odd directions); commuting directions give $C^{2} = 4$, and the value $4$ is never reached.
