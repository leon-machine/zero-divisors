---
id: synthesis.a-division-no-rung-of-the-switch-tower-performs
kind: claim
version: 1
title: A division that no rung of the switch tower performs
status: proved
region: synthesis
subject: tower
tags: [idempotents, ladder-pairs, no-go, limits]
proposed_by:
  kind: ai
  session: 2026-11-13-continuum-from-tower
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: idea and direction
- name: Claude Fable 5.2
  role: 'proposal, mathematics and drafting'
  source: run 2026-11-13-continuum-from-tower
- name: Claude Opus 5.5
  role: independent review
  source: run 2026-11-13-continuum-from-tower
review: draft
founded_on:
- synthesis.premise-superposition-over-the-integers@2
lineage:
  motivated_by:
  - tower.commuting-copies
  - tower.fock-module-one-qubit-per-rung
derivations:
- name: main
  uses:
  - synthesis.size-of-an-element-of-the-switch-tower@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_first_on_tests_are_exclusive_with_sizes
- kind: check
  ref: check.py::check_finite_parts_are_solved_by_partial_sums
- kind: check
  ref: check.py::check_no_solution_in_a_lower_rung_by_linear_algebra
- kind: check
  ref: check.py::check_factorisation_used_in_the_proof
- kind: check
  ref: check.py::check_sizes_of_partial_solutions_and_the_gap_from_one_third
- kind: proof
  derivation: main
extraction:
  note: >-
    From the session of 13 November 2026 on Leon's proposal that division by zero, by instantiating
    the never-ending transport, is the route to the continuum. The statement is Section 4 of the
    working note "The Never-Ending Transport and the Continuum" (draft 0.5; not a paper of the series
    and not imported into the store). Pre-registered as Claims C3 and C4 of
    preregistration_continuum_from_tower.md (kill conditions K4, K5, not triggered) before any check
    ran; clause (ii) was sharpened to an if and only if after the first cold review, and the wording
    of (iii) (no "limit 1/3" is formed; the gap is an explicit fraction) follows the third. The
    referee found no error. The construction is elementary: the g_j are the standard infinite family
    of orthogonal idempotents of an infinite tensor product of 2 x 2 matrix algebras. What it records
    for the store: each rung repairs the divisions of the one below, and the tower as a whole poses a
    system of divisions that is finitely solvable and solved at no rung. Its solutions exist in the
    completion of
    synthesis.imported-rank-completion-of-the-doubled-matrix-algebra. Ledger: transport-convenient.
---

## formal
Let $T = \bigcup_{k}A_{k}$, $A_{k} = \Cl_{\Q}(k,k)$, with switches $(v_{i}, w_{i})$, tests $\mathrm{on}_{i} = v_{i}w_{i}$, $\mathrm{off}_{i} = w_{i}v_{i}$ and size $N$, as in Theorem \claimref{synthesis.size-of-an-element-of-the-switch-tower}. For $j \ge 1$ and $m \ge 0$ put
\[
g_{j} = \mathrm{off}_{1}\,\mathrm{off}_{2}\cdots\mathrm{off}_{j-1}\,\mathrm{on}_{j}, \qquad P_{m} = \mathrm{off}_{1}\,\mathrm{off}_{2}\cdots\mathrm{off}_{m}
\]
(``the first switch that is on is the $j$-th''; ``the first $m$ switches are off'').
\begin{enumerate}
\item[(o)] The $g_{j}$ are idempotents with $g_{i}g_{j} = 0$ for $i \ne j$, $P_{m}$ is an idempotent, $N(g_{j}) = 2^{-j}$, $N(P_{m}) = 2^{-m}$, and $g_{1} + \dots + g_{m} + P_{m} = 1$.
\end{enumerate}
Let $J$ be a set of positive integers, and consider the system for an unknown $x$:
\[
x\,g_{j} = g_{j} \quad (j \in J), \qquad x\,g_{j} = 0 \quad (j \notin J).
\]
\begin{enumerate}
\item[(i)] Every finite set of these equations has a common solution in $T$: $E_{n} = \sum_{j \in J,\ j \le n} g_{j}$ solves those with $j \le n$.
\item[(ii)] The whole system has a solution in $T$ if and only if $J$ is finite or its complement is finite.
\item[(iii)] For $J$ the even numbers, $N(E_{2n}) = \tfrac13(1 - 4^{-n})$ and $N(E_{2n+2} - E_{2n}) = 4^{-(n+1)}$, while every $x \in A_{m}$ has $|N(x) - \tfrac13| \ge \tfrac{1}{3 \cdot 2^{m}}$ and hence
\[
N(E_{2n} - x) \;\ge\; \frac{1}{3 \cdot 2^{m}} - \frac{1}{3 \cdot 4^{n}} .
\]
So the partial solutions come within $4^{-(n+1)}$ of one another and stay a fixed distance from each element of $T$.
\end{enumerate}

## technical
In the tower with one switch per rung, the tests ``the first switch that is on is the $j$-th'' are mutually exclusive, of sizes $\tfrac12, \tfrac14, \tfrac18, \dots$ Ask for an element $x$ that acts as the identity on the tests with $j$ in a given set $J$ and as zero on the others. Any finite part of this demand is met by a finite sum of tests. The whole demand is met inside the tower only when $J$ or its complement is finite: a solution living in rung $m$ would have to act on the test ``the first $m$ switches are off'' both as the identity and as zero. For $J$ the even numbers the partial solutions have sizes $\tfrac14, \tfrac5{16}, \tfrac{21}{64}, \dots$, all below $\tfrac13$ and differing from it by $\tfrac13 4^{-n}$, while sizes in the tower have denominators a power of two; so the partial solutions crowd together without approaching any element of the tower. This is the failure of division that only a completion of the tower repairs.

## lay
Each step of the tower repairs the divisions that failed one step below. But the whole endless tower poses a division of its own: one where every finite piece can be done, yet no single step of the tower does all of it. The partial answers get closer and closer to each other while staying away from everything the tower contains.

## one-liner
With $g_{j} = \mathrm{off}_{1}\cdots\mathrm{off}_{j-1}\mathrm{on}_{j}$ (exclusive tests of size $2^{-j}$), the system $xg_{j} = g_{j}$ ($j \in J$), $xg_{j} = 0$ ($j \notin J$) is solvable in every finite part, and solvable in $T = \bigcup_{k}\Cl_{\Q}(k,k)$ only for $J$ finite or cofinite; for $J$ even the partial solutions have sizes $\tfrac13(1 - 4^{-n})$, not approached by any size in $T$.
