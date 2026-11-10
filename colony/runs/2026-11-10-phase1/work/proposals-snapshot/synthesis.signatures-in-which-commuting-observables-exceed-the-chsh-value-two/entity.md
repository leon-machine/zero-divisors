---
id: synthesis.signatures-in-which-commuting-observables-exceed-the-chsh-value-two
kind: claim
version: 1
title: 'Signatures in which commuting observables exceed the CHSH value 2'
status: proved
region: synthesis
subject: clifford-structure
tags: [entanglement, clifford-classification, finite-models, classical-theorem]
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
  - synthesis.blade-square-signs-f2-quadratic-form@3
  - transport.classification-real-clifford-algebras@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_dagger_is_blade_inverse_and_the_chsh_square_identity
- kind: check
  ref: check.py::check_excluded_signatures_have_only_an_anticommuting_frame_of_observables
- kind: check
  ref: check.py::check_remaining_signatures_carry_blades_with_chsh_square_four_plus_four_k
- kind: check
  ref: check.py::check_excluded_list_is_matrix_size_at_most_two_in_the_classification
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.premise-minimal-non-commutativity
  - synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product
extraction:
  note: >-
    Adversarial test of the plan to state the CHSH bound for two subsystems of one Clifford algebra: is the
    value $2\sqrt{2}$ available in every algebra the foundation allows? It is not. The premise of minimal
    non-commutativity leaves the signature free, and the answer depends on it. Kill condition registered before
    computing: a commuting configuration with $[A_{1},A_{2}][B_{1},B_{2}] \ne 0$ in an excluded signature, or the
    self-adjoint blades of an excluded signature not forming an anticommuting frame (neither fired). Status of the
    content: classical mathematics. The identity of clause (i) is Landau's (L. J. Landau, Phys. Lett. A 120 (1987)
    54), the bound is Tsirelson's (B. S. Cirel'son, Lett. Math. Phys. 4 (1980) 93), both cited from memory; the
    list of clause (ii) is the list of matrix size at most two in the classification of the real Clifford
    algebras, and the absence of two commuting non-commutative factors in a two-by-two matrix algebra over
    $\R$, $\C$ or $\HH$ is standard (compare real and quaternionic quantum theory, where a quaternionic
    two-level system is not a pair of real two-level systems; from memory). What is added is the statement inside
    the series' algebra, with the dagger read off the group of signed directions, the complete list, and an
    elementary proof by blades that does not use the classification. Transport-absent: nothing here uses
    transport. The CHSH identity and the positivity bound are also the subject of a sibling result of the same
    run on the split signature $\Cl(2,2)$ (intended citation once both are stored); this result does not depend
    on it and proves the two lines it needs. Scope: coefficients in $\Q$ or any ordered field; a commuting
    imaginary unit (complex coefficients) is outside the scope and changes the list.
---

## formal
Let $\Cl(p,q)$, $n = p + q \ge 1$, be the Clifford algebra of Theorem \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra} with coefficients in $\Q$ (or any ordered field): generators $e_{1}, \dots, e_{n}$, the first $p$ of square $1$ and the rest of square $-1$, blades $e_{S}$ a basis. Let $x \mapsto x^{\dagger}$ be the linear extension of the inverse on blades, $e_{S}^{\dagger} = e_{S}^{-1}$ (the reverse, with a sign for each generator of square $-1$); it is an anti-automorphism and $\langle xx^{\dagger}\rangle_{0}$ is the sum of the squares of the coefficients of $x$. An \emph{observable} is an $x$ with $x^{\dagger} = x$ and $x^{2} = 1$; a \emph{state} is a linear functional $\varphi$ to the coefficients with $\varphi(1) = 1$ and $\varphi(xx^{\dagger}) \ge 0$ for all $x$. A \emph{CHSH configuration} is four observables $A_{1}, A_{2}, B_{1}, B_{2}$ with $A_{i}B_{j} = B_{j}A_{i}$ for all $i, j$; its CHSH element is $C = A_{1}B_{1} + A_{1}B_{2} + A_{2}B_{1} - A_{2}B_{2}$. No subsystem structure is assumed: the two parties are any two commuting pairs.
\begin{enumerate}
\item[(i)] \emph{(Identity; proved, classical.)} $C^{\dagger} = C$, $C^{2} = 4 - [A_{1},A_{2}][B_{1},B_{2}]$, and $\varphi(C)^{2} \le \varphi(C^{2})$ for every state.
\item[(ii)] \emph{(Excluded signatures; proved.)} Let $\mathcal{E}$ be the fourteen signatures with $n \le 3$ together with $(4,0)$, $(1,3)$, $(0,4)$, $(5,0)$, $(1,4)$. For $(p,q) \in \mathcal{E}$ every CHSH configuration has $[A_{1},A_{2}][B_{1},B_{2}] = 0$, so $C^{2} = 4$ and $|\varphi(C)| \le 2$ for every state. The reason: the self-adjoint elements are $s + v$ ($s$ a scalar, $v$ in the span $V$ of a set of at most five anticommuting blades of square $1$), or two such blocks cut out by a central self-adjoint pseudoscalar $J$ with $J^{2} = 1$ (signatures $(1,0)$, $(2,1)$, $(0,3)$, $(5,0)$, $(1,4)$); in each block the observables are $\pm 1$ and the unit vectors of $V$, and two unit vectors of $V$ commute only if they are equal or opposite. In $\Cl(4,0)$ the frame is $e_{1}, \dots, e_{4}$ and the pseudoscalar; in $\Cl(1,3)$ it is $e_{1}$, $e_{1}e_{2}$, $e_{1}e_{3}$, $e_{1}e_{4}$ and $e_{2}e_{3}e_{4}$; in $\Cl(3,0)$ it is $e_{1}, e_{2}, e_{3}$.
\item[(iii)] \emph{(All other signatures; proved.)} For $(p,q) \notin \mathcal{E}$ there is a CHSH configuration of blades with $A_{1}A_{2} = -A_{2}A_{1}$ and $B_{1}B_{2} = -B_{2}B_{1}$, so that $C^{2} = 4 + 4K$ with $K = -A_{1}A_{2}B_{1}B_{2}$ a non-central blade, $K^{\dagger} = K$, $K^{2} = 1$, $KC = CK$, and $C^{3} = 8C$. For $r$ in the coefficients, $\varphi_{r}(x) = \langle (1 + K)(1 + rC)x\rangle_{0}$ is a state exactly when $8r^{2} \le 1$, and then $\varphi_{r}(C) = 8r$ and $\varphi_{r}(C^{2}) = 8$. So over $\Q$ the values $8r$, $r \in \Q$, $8r^{2} \le 1$, occur, with supremum $2\sqrt{2}$ not attained, and over an ordered field containing $\sqrt{2}$ the value $2\sqrt{2}$ is attained at $r = \sqrt{2}/4$. In signature $(3,1)$: $A_{1} = e_{1}$, $A_{2} = e_{2}$, $B_{1} = e_{3}e_{4}$, $B_{2} = e_{1}e_{2}e_{4}$; in $(2,2)$: $A_{1} = e_{1}$, $A_{2} = e_{2}$, $B_{1} = e_{1}e_{2}e_{3}$, $B_{2} = e_{1}e_{2}e_{4}$.
\item[(iv)] \emph{(Reading; proved from Theorem \claimref{transport.classification-real-clifford-algebras}.)} $\mathcal{E}$ is exactly the set of signatures in which the real Clifford algebra is a matrix algebra of size at most $2$ over $\R$, $\C$ or $\HH$, or a sum of two such. In particular the algebra of space $\Cl(3,0)$ and the spacetime algebra in signature $(1,3)$ carry no CHSH configuration with value above $2$, while signature $(3,1)$ and the split signature $(2,2)$ do; with four directions these two are the only ones.
\end{enumerate}

## technical
The CHSH value $2\sqrt{2}$ is not available in every Clifford algebra that the foundation's premises allow: it depends on the signature, which the premise of minimal non-commutativity leaves free. Take as the two parties any two pairs of self-adjoint elements of square one that commute across the pairs, with the adjoint read off the group of signed directions (a blade goes to its inverse) and states the functionals that are non-negative on every $xx^{\dagger}$. In fourteen signatures (all those with at most three directions, and $(4,0)$, $(1,3)$, $(0,4)$, $(5,0)$, $(1,4)$) the self-adjoint elements of square one are, block by block, the unit vectors of one anticommuting frame, two of them commute only when they are parallel, and so one of the two commutators in the square of the CHSH element always vanishes: the value never exceeds $2$, for every state. In every other signature there are blades with CHSH square $4 + 4K$, $K$ a blade of square one, and rational states with values $8r$ for every rational $r$ with $8r^{2} \le 1$: the supremum $2\sqrt{2}$ is approached over the rationals and attained once $\sqrt{2}$ is a coefficient. The excluded signatures are those of matrix size at most two in the stored classification; they include $\Cl(3,0)$ and the spacetime algebra in signature $(1,3)$, and not signature $(3,1)$ or $(2,2)$. The mathematics is classical (the identity is Landau's, the bound Tsirelson's, the list a consequence of the classification); the statement in the series' algebra, the complete list and the elementary proof by blades are what is recorded. Real or rational coefficients only: a commuting imaginary unit changes the list.

## lay
The famous quantum limit on correlations between two distant parties, $2\sqrt{2}$ where everyday reasoning allows only $2$, needs room: each party must have two measurements that do not commute with each other but do commute with the other party's. This result asks in which of the algebras of directions that room exists, when the numbers used are ordinary real or rational numbers. The answer depends on how many directions square to plus one and how many to minus one. With three or fewer directions there is never room, and with four directions there is room in only two of the five cases. The algebra of three-dimensional space, and the spacetime algebra with one plus and three minus signs, have no room: there every such experiment stays at $2$. The mathematics is classical; what is recorded is the exact list and a short proof inside the algebra.

## one-liner
For commuting pairs of self-adjoint square-one elements of $\Cl(p,q)$ (rational or real coefficients, blade-inverse adjoint), every CHSH value is at most $2$ exactly in the fourteen signatures of matrix size at most two ($n \le 3$, $(4,0)$, $(1,3)$, $(0,4)$, $(5,0)$, $(1,4)$); in all others blades give $C^{2} = 4 + 4K$ and rational states with values $8r$, $8r^{2} \le 1$, of supremum $2\sqrt{2}$.
