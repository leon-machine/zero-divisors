---
id: synthesis.definite-side-rung-count-on-every-quarter-turn-lens-wall-is-the-level
kind: claim
version: 1
title: 'Definite-side rung count on every quarter-turn lens wall: the level, given Stolz'
status: proved
region: synthesis
subject: walls
tags: [classical-theorem, tameness]
proposed_by:
  kind: ai
  session: 2026-11-24-number-theory
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-24-number-theory
review: draft
outside_ga:
  kind: other
  why: "The result combines a stored reduction (the rung count on a definite side as the least number of components of a map that changes sign under the quarter turn, written in geometric algebra there) with an imported theorem of equivariant homotopy theory; what is added here is integer arithmetic on the imported formula."
derivations:
- name: main
  uses:
  - synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five@1
  - synthesis.imported-stolz-level-of-real-projective-spaces-under-the-quarter-turn@1
  - synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height@3
  - synthesis.wall-rung-count-is-height-of-dying-line-class@2
  - synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side@1
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_level_formula_reproduces_the_stored_counts_and_lies_between_the_stored_bounds
- kind: check
  ref: check.py::check_explicit_maps_are_optimal_exactly_in_four_dimensions_and_the_period_is_eight
lineage:
  motivated_by:
  - sheaf.wall-class
  - synthesis.lens-space-wall-rung-count-sees-the-integral-twist
extraction:
  open_problem: op.wall-class-invariant
  note: >-
    Draws the consequence of the imported theorem of Stolz for the open problem's question on definite sides:
    on the quarter-turn lens walls the rung count on a definite side is known in every dimension, given the
    import. The whole content is the import together with the stored reduction; nothing here is new
    mathematics, and the value rests on a theorem taken from secondary sources (see the imported Fact). The one
    value that goes beyond what the store held, $6$ on $L^{7}(4)$ ($m = 4$), lies in the residue $m \equiv 4$
    modulo $8$, where by the review the paper's general bounds differ; the check cannot tell $m + 2$ from
    $m + 1$ there, since the stored window is $5 \le k_{+} \le 6$, so that value should be read against the paper
    before anything is built on it. What the
    store holds independently: the values at $n = 1$ ($3$, a stored theorem) and $n = 2$ ($5$, a stored theorem
    given the imported Steenrod Fact) agree with the formula, and for every $n$ the formula lies between the
    stored lower bound from complex K-theory and the stored upper bound from explicit maps; the check verifies
    these agreements, which test the transcription of the import and do not prove it. The answer to "which
    integral datum decides the count when the side is definite" is, on this family, the residue of $n + 1$
    modulo $8$; no datum of the wall's cohomology ring is identified that carries that residue, and the general
    question of the open problem stays open. On indefinite sides nothing new is obtained beyond the upper bound.
    Ledger: transport-convenient (it prices a completion in rungs), given a transport-absent import.
---

## formal
Let $\Sig_{n} = L^{2n+1}(4)$, $J$, $\shL$ and $k_{+}(\Sig_{n})$ be as in \claimref{synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five}: $J$ is the quarter turn in every coordinate plane of $\R^{2n+2}$, $\shL$ the flat line on which it acts by $-1$, $e(\shL)$ the least $k$ with $\shL$ a subbundle of the trivial bundle of rank $k$, and $k_{+}(\Sig_{n})$ the rung count of a tame wall with cross-section $\Sig_{n}$, dying line $\shL$ and definite physical side, which equals $e(\shL)$ (there). Let (St) be the imported Fact \claimref{synthesis.imported-stolz-level-of-real-projective-spaces-under-the-quarter-turn}: for $m \ge 2$ the least number $s(m)$ of components of a continuous map of $S^{2m-1}$ that changes sign under the quarter turn is $m + 1$, $m + 2$ or $m + 3$ according as $m \equiv 0, 2$; $1, 3, 4, 5, 7$; or $6$ modulo $8$. Tameness (\claimref{sheaf.tameness}) is assumed, as in every result this one rests on. Given (St), for every $n \ge 1$:
\begin{enumerate}
\item[(i)] \emph{(The count.)} $e(\shL) = s(n + 1)$ on $\Sig_{n}$, so on a definite side
\[
k_{+}(L^{2n+1}(4)) = \begin{cases} n + 2 & n \equiv 1, 7 \pmod 8, \\ n + 4 & n \equiv 5 \pmod 8, \\ n + 3 & \text{otherwise}: \end{cases}
\]
$3, 5, 6, 7, 9, 9, 9, 11$ for $n = 1, \dots, 8$. The values at $n = 1$ and $n = 2$ are the stored ones, and the stored window $5 \le k_{+}(L^{7}(4)) \le 6$ closes at $6$ (the case $n + 1 \equiv 4 \pmod 8$ of (St), where the review of Stolz's paper notes that the paper's general bounds differ; see the imported Fact).
\item[(ii)] \emph{(Every side.)} On every side $k(\Sig) \le e(\shL) = s(n + 1)$ (clause (2) of \claimref{synthesis.wall-rung-count-is-height-of-dying-line-class}), and, given also the lambda-operations, $k(\Sig) \ge 1 + \lceil n/2 \rceil$ (clause (2) of \claimref{synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height}); with $k \ge 4$ for $n \ge 2$ (clause (3) of \claimref{synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side}, conditional at $n = 2$ on the spin class (L2) there) the windows on indefinite sides are $4 \le k \le 5$ on $L^{5}(4)$ and $4 \le k \le 6$ on $L^{7}(4)$, as stored. The lower bound from complex K-theory is about half the definite-side count.
\item[(iii)] \emph{(The explicit maps.)} The upper bound $\lceil 3(n+1)/2 \rceil$ of clause (2) of the first cited result, by sums of quadratic maps written in the algebra, equals $k_{+}$ exactly for $n = 1, 2, 3, 5$; for every other $n$ it is larger, by $1$ at $n = 4$ and by at least $2$ from $n = 6$ on.
\item[(iv)] \emph{(Period eight; a remark.)} The count depends on $n$ through $n$ and the residue of $n + 1$ modulo $8$. The stored classification of real Clifford algebras has the same period (\claimref{std-algebra.periodicity}); whether the two periods have one source is not examined here.
\end{enumerate}

## technical
The stored reduction says that on a definite side the number of rungs a quarter-turn lens wall needs is the least number of components of a map of the sphere that changes sign under the quarter turn. That number is the level of real projective space under the involution induced by the quarter turn, which Stolz computed in 1989; with his theorem imported, the definite-side rung count of $L^{2n+1}(4)$ is $n + 2$, $n + 3$ or $n + 4$ according to $n$ modulo $8$. This agrees with the two values the store proves by its own means ($3$ and $5$), settles the stored window on $L^{7}(4)$ at $6$, and shows that the explicit quadratic maps of the stored result are best possible only in four cases. On indefinite sides it gives an upper bound only. The count rests on an import read through secondary sources and assumes the tame-wall setting; the new value on $L^{7}(4)$ falls in the one residue where, by the review of Stolz's paper, the paper's general bounds differ.

## lay
The series counts how many extra pairs of directions are needed to complete the geometry across a wall. For one family of walls, built from a quarter turn, and for the case where the physical side has no time direction, an earlier result turned that count into a classical question about maps of spheres, and answered it in the two smallest cases. A theorem of 1989, taken here from accounts of it and not from the paper, answers the classical question in every dimension. Taking that theorem from the literature gives the count for the whole family: about half the dimension of the wall, plus a small correction that repeats every eight steps.

## one-liner
Assuming tameness and given the imported theorem of Stolz, the rung count on a definite side of the quarter-turn lens wall $L^{2n+1}(4)$ is the level $s(n+1)$: $n + 2$ for $n \equiv 1, 7$, $n + 4$ for $n \equiv 5$ and $n + 3$ otherwise modulo $8$ ($3, 5, 6, 7, 9, 9, 9, 11$ for $n = 1, \dots, 8$), agreeing with the stored $3$ and $5$ and closing the stored window on $L^{7}(4)$ at $6$ (the residue where the review of Stolz's paper notes that the paper's general bounds differ); on every side it is an upper bound, and the stored explicit maps are optimal exactly for $n = 1, 2, 3, 5$.
