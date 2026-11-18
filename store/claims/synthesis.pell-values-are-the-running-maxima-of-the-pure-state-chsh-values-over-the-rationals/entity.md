---
id: synthesis.pell-values-are-the-running-maxima-of-the-pure-state-chsh-values-over-the-rationals
kind: claim
version: 1
title: 'Pell values are the running maxima of pure-state CHSH values over the rationals'
status: proved
region: synthesis
subject: clifford-structure
tags: [entanglement, finite-models]
proposed_by:
  kind: ai
  session: 2026-11-18-leads
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-18-leads
review: draft
outside_ga:
  kind: other
  why: "The statement is elementary number theory about the set of values that the stored theorem computes in Cl(2,2); only the tie to the algebra (the state of value 2) uses the Clifford product."
derivations:
- name: main
  uses:
  - synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_deficit_of_a_pure_value_is_one_or_at_least_seven
- kind: check
  ref: check.py::check_pell_denominators_grow_by_less_than_the_square_root_of_thirty_four
- kind: check
  ref: check.py::check_running_maxima_of_pure_values_are_the_pell_values
- kind: check
  ref: check.py::check_first_pell_value_is_the_value_of_the_even_state
lineage:
  motivated_by:
  - synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records
extraction:
  open_problem: op.positivity-of-values
  note: >-
    Settles the last item of the open problem: whether the pure-state values of the sector that meet the
    denominator law with equality are the running maxima among pure-state values for every denominator. They
    are. The stored theorem had this computed for denominators up to $400$ and not proved; the proof is
    elementary (a parity argument, the fact that $2$ is not a square modulo $3$ or $5$, and the growth of the
    Pell denominators by a factor below $3 + 2\sqrt{2}$). Kill condition registered before computing: a pure
    value in lowest terms with $b \ge 3$ that no Pell value of smaller denominator exceeds, or $b = 3$ or
    $b = 5$ occurring in lowest terms, or failure of $Q_{n+1}^{2} < 34Q_{n}^{2}$; none occurred for
    denominators up to $1000$ ($317$ positive values, records at $1, 5, 29, 169, 985$). The statement is
    arithmetic about the set of values that clause (ii) of the stored theorem identifies; it inherits that
    theorem's setting (the one-mode Klein-twisted realisation, the split, and the premise of positivity of
    values under which states are spoken of) and adds no hypothesis. It could equally be folded into clause
    (v) of the stored theorem, replacing "computed, not proved beyond that range"; that is a maintainer's
    choice. Classical background: the best-approximation property of Pell solutions (from memory, not used).
---

## formal
Notation and setting of Theorem \claimref{synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records}: the algebra $\Cl_{\Q}(2,2)$, the settings of its clauses, the CHSH element $C$, and the pure states of the sector, whose values of $C$ form by its clause (ii) the set
\[
\mathcal{V} = \{X \in \Q : 8 - X^{2} \text{ is the square of a rational}\}.
\]
Let $(x_{n}, Q_{n})$ be the positive solutions of $x^{2} - 2Q^{2} = -1$, $(x_{0}, Q_{0}) = (1, 1)$, $(x_{n+1}, Q_{n+1}) = (3x_{n} + 4Q_{n},\ 2x_{n} + 3Q_{n})$, and $S_{n} = 2x_{n}/Q_{n}$ (clause (v) of that theorem). The \emph{denominator} of a rational is that of its expression in lowest terms. A value $X \in \mathcal{V}$ is a \emph{running maximum} if it is the largest element of $\mathcal{V}$ among those of denominator at most its own.
\begin{enumerate}
\item[(i)] \emph{(The deficit; proved.)} For $X = P/Q \in \mathcal{V}$ in lowest terms with $P, Q \ge 1$: $Q$ is odd, $P = 2a$, and $8Q^{2} - P^{2} = 4b^{2}$ with $a$, $b$ odd, $a^{2} + b^{2} = 2Q^{2}$; $b$ is divisible by neither $3$ nor $5$, so $b = 1$ or $b \ge 7$, and $8 - X^{2} = 4b^{2}/Q^{2}$. $b = 1$ holds exactly for $X = S_{n}$.
\item[(ii)] \emph{(Comparison; proved.)} $Q_{n+1}^{2} < 34Q_{n}^{2}$ for all $n$. If $X = P/Q \in \mathcal{V}$ is positive with $b \ge 7$ and $n$ is the largest index with $Q_{n} < Q$, then $S_{n} > X$.
\item[(iii)] \emph{(Running maxima; proved.)} For every $D \ge 1$ the largest element of $\mathcal{V}$ of denominator at most $D$ is $S_{n}$ with $n$ the largest index such that $Q_{n} \le D$, and it is attained only there. Hence the running maxima of the pure-state values are exactly $S_{0}, S_{1}, S_{2}, \dots = 2, \tfrac{14}{5}, \tfrac{82}{29}, \tfrac{478}{169}, \tfrac{2786}{985}, \dots$, for every denominator.
\end{enumerate}
\emph{Reading.} Among the pure states of the sector over $\Q$, the best value of the CHSH element available with denominators up to a given size is always a Pell value: the denominator law is met with equality along the whole staircase, not only in the computed range. This is a statement about pure states at the stored settings; among all state values the Pell values are not the running maxima (stored, clause (v)).

## technical
The stored theorem on the CHSH element over the rationals identifies the values of the pure states of a sector with the rationals $X$ for which $8 - X^{2}$ is a rational square, proves that every value $P/Q$ obeys $8 - (P/Q)^{2} \ge 4/Q^{2}$ with equality on a Pell sequence, and records as computed, up to denominator $400$, that these Pell values are the running maxima of the pure-state values as the denominator grows. This result proves it for all denominators. Writing $P = 2a$ and $8Q^{2} - P^{2} = 4b^{2}$, the numbers $a$, $b$, $Q$ are odd with $a^{2} + b^{2} = 2Q^{2}$, and a prime factor of $b$ must have $2$ as a square residue, so $b$ is $1$ or at least $7$. The case $b = 1$ is the Pell equation. For $b \ge 7$ the deficit is at least $196/Q^{2}$, while the Pell value with the largest denominator below $Q$ has deficit below $136/Q^{2}$, because consecutive Pell denominators grow by a factor whose square is below $34$. So every non-Pell value is beaten by a Pell value of smaller denominator.

## lay
With rational numbers only, the strongest quantum correlation in the standard two-party test cannot be reached exactly, only approached. The stored result found a staircase of best values, $2$, $14/5$, $82/29$, and so on, each the best possible for the size of its denominator, and had checked by computer up to denominator $400$ that for the simplest kind of state no other value ever takes the lead. This result proves that it never does, by a short argument about odd and even numbers and about how fast the staircase's denominators grow.

## one-liner
For the pure states of the sector of $\Cl_{\Q}(2,2)$ at the stored settings, a value $P/Q$ in lowest terms has $8 - (P/Q)^{2} = 4b^{2}/Q^{2}$ with $b = 1$ (the Pell values $S_{n}$) or $b \ge 7$, and since $Q_{n+1}^{2} < 34Q_{n}^{2}$ every value with $b \ge 7$ is below the Pell value of the largest smaller denominator; so the running maxima by denominator are exactly $2, \tfrac{14}{5}, \tfrac{82}{29}, \tfrac{478}{169}, \dots$ for every denominator.
