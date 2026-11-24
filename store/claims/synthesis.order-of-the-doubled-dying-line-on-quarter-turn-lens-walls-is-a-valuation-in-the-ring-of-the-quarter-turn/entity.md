---
id: synthesis.order-of-the-doubled-dying-line-on-quarter-turn-lens-walls-is-a-valuation-in-the-ring-of-the-quarter-turn
kind: claim
version: 1
title: 'Order of the doubled dying line on quarter-turn lens walls: a valuation in Z[J]'
status: proved
region: synthesis
subject: walls
tags: [hyperbolic-plane, tameness, no-go, classical-theorem]
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
  why: "The ring of the quarter turn, Z[J] with J = e_1 e_2, is the integer even subalgebra of Cl(2,0), and the statements about it are computed with the Clifford product. The stored K-ring is a quotient of a polynomial ring over the integers, and the step from it to Z[J] is commutative algebra of polynomials (divisibility by a prime element); clause (iv) is stated in the ring Z[x]/(x^(N/2) + 1) of the 2^a-th turn, which is not a subring of a rational Clifford algebra of the plane for a > 2."
derivations:
- name: main
  uses:
  - synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure@1
  - std-algebra.complex-numbers@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_two_is_the_quarter_turn_times_the_square_of_j_minus_one
- kind: check
  ref: check.py::check_order_of_one_minus_chi_squared_in_the_stored_k_ring_is_two_to_the_ceiling_of_n_over_two
- kind: check
  ref: check.py::check_order_of_the_sign_line_for_the_half_turn_and_the_eighth_turn
- kind: check
  ref: check.py::check_ceiling_of_half_n_against_the_two_bounds_stored_before
lineage:
  motivated_by:
  - sheaf.wall-class
  - synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side
  - synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five
extraction:
  open_problem: op.wall-class-invariant
  note: >-
    The stored proof already maps the K-ring to the ring of the quarter turn modulo a power of $J - 1$ (there
    written $I$ and $\pi = I - 1$) and reads off a lower bound; dividing the relation by $\chi - 1$ first gives
    the exact order. The stored K-theory bound on the rungs of the quarter-turn lens walls rests on the order of $1 - \chi^{2}$ in
    the stored K-ring, which was proved to be at least $2^{\lfloor n/2 \rfloor}$ for every $n$ and computed to be
    $2^{\lfloor (n+1)/2 \rfloor}$ for $n \le 8$ (for $n \le 14$ in the cohomology theorem's own record). Clause
    (ii) proves the computed value for every $n$, so the bound $1 + \lfloor (n+1)/2 \rfloor$ holds for every $n$
    (stated in the lens-wall result from its version 3; clause (iii) here is a pointer to it); like the stored bound it stays conditional on the lambda-operations (L1) and, through the
    K-ring, on the imported Atiyah-Hirzebruch filtration. A test fixed before computing: whether for
    some $n$ the order computed directly in the quotient ring differs from the least power of $2$ divisible by
    $(J - 1)^{n}$ in $\Z[J]$. It does not for $n \le 40$, nor for the half turn and the eighth and sixteenth
    turns. A second test concerned a different route, which failed: the spectral asymmetries of the
    lens spaces twisted by characters, in the classical formula for the reduced asymmetry (Atiyah, Patodi and
    Singer; Donnelly; Gilkey's theorem that they detect the K-theory of lens spaces; all from memory, nothing
    imported), pair to integers with $2^{m}(\chi^{2} - 1)$ exactly from $m = \lceil n/2 \rceil$ on, for
    $n \le 8$ (an exact computation, not filed in the store); so they reproduce the order of clause (ii) by a third
    route and see nothing the complex K-ring does not. In particular they do not show that the doubled dying
    line is not stably trivial on $L^{5}(4)$, where the stored result needs the spin class $q_{1}$: a real
    refinement of the asymmetry needs a spin structure, and $L^{5}(4)$ has none (its stable tangent class
    $3\eta$ has $w_{2} \ne 0$ by the stored cohomology). That route is closed and $q_{1}$ stays the input there.
    Prior art on the definite side, read through a secondary source and not imported (Leon's decision is
    asked): S. Stolz, The level of real projective spaces, Comment. Math. Helv. 64 (1989) 661, as quoted in
    Example 2.2(ii) of M. Furuta, Y. Kametani, H. Matsue and N. Minami, Geom. Topol. Monogr. 10 (2007) 155
    (arXiv:0903.4462), where it is the level of $\mathbb{R}P^{2m-1}$ with the involution induced by $i$: the least $k$ with a map
    $S^{2m-1} \to S^{k-1}$ that changes sign under the quarter turn is $m + 1$ for $m \equiv 0, 2$, $m + 2$ for
    $m \equiv 1, 3, 4, 5, 7$ and $m + 3$ for $m \equiv 6$ modulo $8$. By the stored reduction this is the
    definite-side rung count of the $L^{2n+1}(4)$ walls with $m = n + 1$, and it agrees with the three stored
    values: $3$ on $L(4,1)$, $5$ on $L^{5}(4)$ (derived in the store) and $6$ on $L^{7}(4)$ (prior art there
    too). The K-theory bound of clause (iii) is about half of it. Clause (iv) for groups other than the
    quarter turn uses the K-ring of $L^{2n+1}(2^{a})$, classical (Atiyah; Kambe 1966; Mahammed 1971; from
    memory) and not stored: it is stated as algebra, with the consequence for rungs conditional on that ring.
    Ledger: transport-convenient for the bound (it prices a completion in rungs), transport-absent for the
    arithmetic.
---

## formal
Let $\Sig_{n} = L^{2n+1}(4)$, $\eta$, $\shL$ and $\chi$ be as in \claimref{synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure}: the generator of $\Z_{4}$ acts on every coordinate plane by the quarter turn, $\chi$ is the class of the flat line on which it acts by the quarter turn, $\xi = \chi^{2}$ is the complexification of the dying line $\shL$, and by clause (6) of that theorem (proved there given the imported Atiyah-Hirzebruch filtration) $K(\Sig_{n}) = \Z[\chi]/(\chi^{4} - 1, (\chi - 1)^{n+1})$. Let $J = e_{1}e_{2}$ be the unit bivector of $\Cl(2,0)$, the quarter turn of the plane ($J^{2} = -1$, \claimref{std-algebra.complex-numbers}(ii)), and $\Z[J] = \{a + bJ : a, b \in \Z\}$ the ring it generates; $\tilde{z}$ is the reverse.
\begin{enumerate}
\item[(i)] \emph{(The ring of the quarter turn; proved.)} $(J - 1)^{2} = -2J$, so $2 = J(J - 1)^{2}$; $(J - 1)(J - 1)^{\sim} = 2$, so $J - 1$ has no inverse in $\Z[J]$; and $(J - 1)^{n}$ divides $2^{m}$ in $\Z[J]$ exactly when $2m \ge n$.
\item[(ii)] \emph{(The order; proved.)} For every $n \ge 1$ the additive order of $1 - \chi^{2}$ in $\Z[\chi]/(\chi^{4} - 1, (\chi - 1)^{n+1})$ is
\[
2^{\lceil n/2 \rceil} = 2^{\lfloor (n+1)/2 \rfloor}.
\]
Precisely: $2^{m}(1 - \chi^{2}) = 0$ in that ring if and only if $2^{m}$ is divisible by $(J - 1)^{n}$ in $\Z[J]$, the ring obtained from $\Z[\chi]$ by setting $\chi = J$.
\item[(iii)] \emph{(Consequence for the rungs; drawn in the stored result, not here.)} By clause (1) of \claimref{synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height} a $k$-rung completion forces $2^{k-1}(1 - \xi) = 0$ in $K(\Sig)$, so (ii) gives $k(\Sig) \ge 1 + \lceil n/2 \rceil$ on every side of every tame wall with cross-section $L^{2n+1}(4)$ and $w_{1}(\shL) \ne 0$, for every $n \ge 1$. That statement, with its hypotheses (tameness; the lambda-operations, cited there from memory; the stored K-ring), is clause (2) of the cited result from its version 3, which cites (ii); it is recorded here as a pointer and no edge is drawn from this result to that one. Before, that clause had $1 + \lfloor n/2 \rfloor$ for all $n$ and $1 + \lfloor (n+1)/2 \rfloor$ for $n \le 8$; the new bound is larger than the first exactly when $n$ is odd.
\item[(iv)] \emph{(Other two-power turns; proved as algebra.)} Let $N = 2^{a}$, $a \ge 1$. In $\Z[\chi]/(\chi^{N} - 1, (\chi - 1)^{n+1})$ the additive order of $1 - \chi^{N/2}$ is $2^{\lceil 2n/N \rceil}$: $2^{n}$ for the half turn, $2^{\lceil n/2 \rceil}$ for the quarter turn, $2^{\lceil n/4 \rceil}$ for the eighth turn. The exponent is $n$ divided by $N/2$, rounded up, and $N/2$ is the power to which the element $\zeta - 1$ must be raised to give $2$ up to an invertible factor in the ring $\Z[x]/(x^{N/2} + 1)$ of the $N$-th turn $\zeta$. Remark, not part of this result: if $K(L^{2n+1}(N))$ is that quotient ring with $\chi^{N/2}$ the complexified dying line (classical, not stored for $N \ne 4$), clause (1) of the result named in (iii) would give $k(\Sig) \ge 1 + \lceil 2n/N \rceil$ on walls with cross-section $L^{2n+1}(N)$, so the bound from complex K-theory weakens as the turn gets finer.
\end{enumerate}

## technical
The stored K-theory obstruction says that a completion with $k$ rungs forces $2^{k-1}(1 - \xi) = 0$ in the K-theory of the wall, $\xi$ the complexified dying line. On the quarter-turn lens spaces $\xi = \chi^{2}$ in the stored ring $\Z[\chi]/(\chi^{4} - 1, (\chi - 1)^{n+1})$, and the order of $1 - \chi^{2}$ had been bounded below for all $n$ and computed for small $n$. This result computes it for every $n$: it is $2^{\lceil n/2 \rceil}$. The reason is arithmetic in the ring of the quarter turn itself. Since $\chi^{4} - 1 = (\chi^{2} - 1)(\chi^{2} + 1)$ and $\chi^{2} - 1$ is $\chi - 1$ times an element prime to $\chi - 1$, the multiple $2^{m}(1 - \chi^{2})$ vanishes in the quotient exactly when $2^{m}$ lies in the ideal generated by $\chi^{2} + 1$ and $(\chi - 1)^{n}$, that is when $2^{m}$ is divisible by $(J - 1)^{n}$ in $\Z[J]$, $J$ the quarter-turn bivector. There $2 = J(J - 1)^{2}$ and $J - 1$ is not invertible, so the condition is $2m \ge n$. The stored rung bound becomes $k \ge 1 + \lceil n/2 \rceil$ for every $n$, conditional as before on the lambda-operations and on the stored K-ring; that consequence is stated in the stored result, which cites this one. The same algebra for the $2^{a}$-th turn gives the order $2^{\lceil 2n/N \rceil}$, with the half turn recovering the order $2^{n}$ of the real projective spaces; for $N \ne 4$ the K-ring is classical and not stored, so the consequence for rungs is conditional on it. Three routes give the number for the quarter turn: the valuation in $\Z[J]$ (the proof), a direct computation in the quotient ring for $n \le 40$ (the check), and the classical formula for twisted spectral asymmetries for $n \le 8$ (not filed and not part of this result; computed for $n \le 8$, it indicates that those asymmetries see nothing more than the complex K-ring, so the spin class stays the input of the stored result on $L^{5}(4)$).

## lay
The series counts how many extra pairs of directions (rungs) are needed to complete the geometry across a wall. For a family of walls built from a quarter turn, an earlier result gave a lower bound on that count from a quantity that had been proved only partly and computed in small cases. This result computes the quantity in every dimension. The answer comes from the arithmetic of the quarter turn itself: in the whole-number system generated by a quarter turn $J$, the number $2$ is the quarter turn times the square of $J - 1$, and counting how many times $J - 1$ divides a power of two gives the bound.

## one-liner
In the stored K-ring $\Z[\chi]/(\chi^{4} - 1, (\chi - 1)^{n+1})$ of $L^{2n+1}(4)$ the order of $1 - \chi^{2}$ is $2^{\lceil n/2 \rceil}$ for every $n$, because $2^{m}(1 - \chi^{2}) = 0$ exactly when $(J - 1)^{n}$ divides $2^{m}$ in the ring $\Z[J]$ of the quarter turn, where $2 = J(J - 1)^{2}$; so the stored K-theory bound on the rungs of these walls becomes $k \ge 1 + \lceil n/2 \rceil$ on every side for every $n$ (drawn in the stored result, given the lambda-operations), and for the $2^{a}$-th turn the same algebra gives the order $2^{\lceil 2n/2^{a} \rceil}$.
