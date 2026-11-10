---
id: synthesis.signatures-in-which-commuting-observables-exceed-the-chsh-value-two
kind: claim
version: 1
title: 'Signatures in which two commuting pairs of one real Clifford algebra exceed CHSH value 2'
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
  - synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate@1
  assumes:
  - synthesis.premise-positivity-of-values@2
  proof: proof-main.tex
checked_by:
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
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: >-
      Hypothesis (P) is now the stored premise synthesis.premise-positivity-of-values (Leon's decision of 10 November 2026): an assumes edge to it is added, the formal level and the proof cite it with the label (P) kept, and the note names the stored results it refers to by id. No statement changed; version kept at 1.
  note: >-
    Adversarial test of the plan to state the CHSH bound for two subsystems of one Clifford algebra: is a value
    above $2$ available in every algebra the foundation allows? It is not. The premise of minimal
    non-commutativity leaves the signature free, and the answer depends on it. Kill condition registered before
    computing: a commuting configuration with $[A_{1},A_{2}][B_{1},B_{2}] \ne 0$ in an excluded signature, or the
    self-adjoint blades of an excluded signature not forming an anticommuting frame (neither fired). Hypothesis (P) is stated in the formal level under its label; it is the stored premise synthesis.premise-positivity-of-values, which this result assumes. The identity, the bound under (P) and the blade lemma with its
    functionals are cited from the stored CHSH result (its clauses (i), (iii), (iv)) and are not reproved here;
    this result keeps the list, the frame proof, the table of configurations and the classification reading.
    Status of the content: classical mathematics. The list of clause (i) is the list of matrix size at most two in
    the classification of the real Clifford algebras, and the absence of two commuting non-commutative factors in
    a two-by-two matrix algebra over $\R$, $\C$ or $\HH$ is standard (from memory; no source was found to check it
    against, and the proof here does not use it). What is added is the statement inside the series' algebra, the
    complete list, and an elementary proof by blades that does not use the classification. Transport-absent.
    Scope: one copy of the algebra, coefficients in $\Q$ or any ordered field; adjoining a unit that commutes with
    $\Cl(1,3)$ gives $\Cl(4,1)$, of matrix size $4$, which is outside the list.
---

## formal
Let $k$ be $\Q$ or any ordered field and $\Cl_{k}(p,q)$, $n = p + q \ge 1$, the Clifford algebra of Theorem \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra} with coefficients in $k$: generators $e_{1}, \dots, e_{n}$, the first $p$ of square $1$ and the rest of square $-1$ (the label $(p,q)$ follows the stored convention, $p$ generators of square $1$), blades $e_{S}$ a basis. As in Theorem \claimref{synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate}, $x \mapsto x^{\dagger}$ is the linear extension of the inverse on blades, an \emph{observable} is an $x$ with $x^{\dagger} = x$ and $x^{2} = 1$, a \emph{configuration} is four observables $A_{1}, A_{2}, B_{1}, B_{2}$ with $A_{i}B_{j} = B_{j}A_{i}$ for all $i, j$, and $C = A_{1}(B_{1} + B_{2}) + A_{2}(B_{1} - B_{2})$. No subsystem structure is assumed: the two parties are any two commuting pairs inside the one algebra. The adjoint is defined by the chosen generators. In definite signature it does not depend on the orthonormal frame; in indefinite signature it depends on the split into generators of square $1$ and of square $-1$, so observables, states and (P) are relative to that split, and each statement holds for every fixed split. The list below does not depend on the frame: a change of frame is an automorphism carrying the configurations for one adjoint to the configurations for the other.

\emph{Hypothesis (P), positivity of values:} values are given by a \emph{state}, a $k$-linear $\omega : \Cl_{k}(p,q) \to k$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(x^{\dagger}) = \omega(x)$ for all $x$; (P) is Premise \claimref{synthesis.premise-positivity-of-values}, assumed, not derived.

(P) extends the stored definition of a state as an element $\rho = \sum_{r}x_{r}x_{r}^{\dagger}$ of unit trace from elements to functionals.
\begin{enumerate}
\item[(i)] \emph{(Excluded signatures; proved; the value bound under (P).)} Let $\mathcal{E}$ be the following fourteen signatures: the nine with $1 \le n \le 3$, and $(4,0)$, $(1,3)$, $(0,4)$, $(5,0)$, $(1,4)$. For $(p,q) \in \mathcal{E}$ every configuration has $[A_{1},A_{2}][B_{1},B_{2}] = 0$, so $C^{2} = 4$ and, under (P), $\omega(C)^{2} \le 4$ for every state (clauses (i) and (iii) of Theorem \claimref{synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate}). The reason: the self-adjoint elements are $s + v$ ($s$ a scalar, $v$ in the span $V$ of a set of at most five anticommuting blades of square $1$), or two such blocks cut out by a central self-adjoint pseudoscalar $J$ with $J^{2} = 1$ (signatures $(1,0)$, $(2,1)$, $(0,3)$, $(5,0)$, $(1,4)$); in each block the observables are $\pm 1$ and the unit vectors of $V$, and two unit vectors of $V$ commute only if they are equal or opposite. In $\Cl(4,0)$ the frame is $e_{1}, \dots, e_{4}$ and the pseudoscalar; in $\Cl(1,3)$ it is $e_{1}$, $e_{1}e_{2}$, $e_{1}e_{3}$, $e_{1}e_{4}$ and $e_{2}e_{3}e_{4}$; in $\Cl(3,0)$ it is $e_{1}, e_{2}, e_{3}$.
\item[(ii)] \emph{(All other signatures; proved; values under (P).)} For $n \ge 1$ and $(p,q) \notin \mathcal{E}$ there is a configuration of blades with $A_{1}A_{2} = -A_{2}A_{1}$ and $B_{1}B_{2} = -B_{2}B_{1}$. By the blade lemma, clause (iv) of Theorem \claimref{synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate}, $C^{2} = 4 + 4K$ with $K = -A_{1}A_{2}B_{1}B_{2}$ a non-scalar blade of square $1$, and the functionals $\omega_{r}(x) = \langle(1 + K)(1 + rC)x\rangle_{0}$, $8r^{2} \le 1$, satisfy (P) with $\omega_{r}(C) = 8r$: over $\Q$ every rational $v$ with $v^{2} < 8$ is a value, with supremum $2\sqrt{2}$ not attained, and $2\sqrt{2}$ is attained over an ordered field containing $\sqrt{2}$. In signature $(3,1)$: $A_{1} = e_{1}$, $A_{2} = e_{2}$, $B_{1} = e_{3}e_{4}$, $B_{2} = e_{1}e_{2}e_{4}$; in $(2,2)$: $A_{1} = e_{1}$, $A_{2} = e_{2}$, $B_{1} = e_{1}e_{2}e_{3}$, $B_{2} = e_{1}e_{2}e_{4}$; the thirteen signatures with $4 \le n \le 6$ are tabulated in the check, and $n \ge 7$ follows by restriction to six generators.
\item[(iii)] \emph{(Reading; proved from Theorem \claimref{transport.classification-real-clifford-algebras}.)} $\mathcal{E}$ is exactly the set of signatures with $n \ge 1$ in which the real Clifford algebra is a matrix algebra of size at most $2$ over $\R$, $\C$ or $\HH$, or a sum of two such ($(0,0)$ is left out only by $n \ge 1$). In particular one copy of the algebra of space $\Cl(3,0)$, or of the spacetime algebra in signature $(1,3)$, carries no configuration with value above $2$, while signature $(3,1)$ and the split signature $(2,2)$ do; with four directions these two are the only ones. This concerns two commuting pairs inside ONE copy of the algebra with real or rational coefficients. It says nothing against Bell violations for two systems each described by the spacetime algebra: two such systems live in a larger algebra (two commuting copies, or more generators), which is outside $\mathcal{E}$. It also depends on the coefficients: adjoining a unit that commutes with $\Cl(1,3)$ gives $\Cl(4,1)$, of matrix size $4$, which is outside $\mathcal{E}$.
\end{enumerate}

## technical
Whether two commuting pairs of observables inside one Clifford algebra can have a CHSH value above $2$ depends on the signature, which the premise of minimal non-commutativity leaves free. Observables are self-adjoint elements of square one for the adjoint that sends a blade to its inverse; values are taken under Hypothesis (P), positivity of values (values are given by a state, a linear functional $\omega$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(x^{\dagger}) = \omega(x)$; (P) is assumed, not derived). In fourteen signatures (the nine with one to three directions, and $(4,0)$, $(1,3)$, $(0,4)$, $(5,0)$, $(1,4)$) the observables are, block by block, the unit vectors of one anticommuting frame, two of them commute only when parallel, so one of the two commutators in the stored identity for $C^{2}$ always vanishes: $C^{2} = 4$, and under (P) the value never exceeds $2$. In every other signature there is a blade configuration to which the stored blade lemma applies, giving under (P) every rational value of square below $8$. The excluded signatures are those of matrix size at most two in the stored classification. The adjoint depends, in indefinite signature, on the split into positive and negative generators; the list does not. The statement is about two commuting pairs inside ONE copy of the algebra with real or rational coefficients: it says nothing against Bell violations for two systems each described by the spacetime algebra, which live in a larger algebra outside the list, and adjoining a unit that commutes with $\Cl(1,3)$ gives $\Cl(4,1)$, of matrix size $4$, also outside the list. Classical mathematics; the complete list and the elementary proof by blades are what is recorded.

## lay
The quantum limit on correlations between two parties, $2\sqrt{2}$ where everyday reasoning allows only $2$, needs room: each party must have two measurements that do not commute with each other but do commute with the other party's. This result asks in which single algebras of directions that room exists, when the numbers used are ordinary real or rational numbers, and when average values are assumed to be non-negative on squares (Hypothesis (P), an assumption, not something derived). The answer depends on how many directions square to plus one and how many to minus one. With three or fewer directions there is never room, and with four directions there is room in only two of the five cases. For the spacetime algebra with one plus and three minus signs: inside a single copy of that algebra there are not two independent pairs of such measurements; this is a statement about the size of one algebra, not about experiments in spacetime. Two systems, each described by such an algebra, live in a larger algebra, where there is room. The mathematics is classical; what is recorded is the exact list and a short proof inside the algebra.

## one-liner
Under (P), for two commuting pairs of self-adjoint square-one elements inside one $\Cl(p,q)$ (rational or real coefficients, blade-inverse adjoint), every CHSH value is at most $2$ exactly in the fourteen signatures of matrix size at most two (the nine with $1 \le n \le 3$, and $(4,0)$, $(1,3)$, $(0,4)$, $(5,0)$, $(1,4)$); in all others a blade configuration gives $C^{2} = 4 + 4K$ and every rational value of square below $8$.
