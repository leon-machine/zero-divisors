---
id: synthesis.additive-weights-on-the-rational-projectors-of-two-or-more-modes-are-linear
kind: claim
version: 1
title: 'Additive weights on the rational projectors of two or more modes are linear'
status: proved
region: synthesis
subject: clifford-structure
tags: [finite-models, classical-theorem, measurement-and-records]
proposed_by:
  kind: ai
  session: 2026-11-24-three-routes
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-24-three-routes
review: draft
outside_ga:
  kind: other
  why: "The statement is about Cl(l,l), and the matrix units, the rotor norms and the reflection are computed with the Clifford product. The remaining steps are elementary linear algebra and arithmetic over the rationals: quadratic forms on a four-dimensional rational space, an induction on the number of nonzero coordinates, a pigeonhole count modulo a prime, and congruences modulo 8."
derivations:
- name: main
  uses:
  - synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear@1
  - synthesis.signed-directions-and-the-integer-clifford-algebra@2
  - tower.ladder-pairs-satisfy-car-vectors@4
  - std-algebra.quaternions@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_three_modes_are_the_rational_matrices_of_size_eight_and_even_elements_are_two_blocks
- kind: check
  ref: check.py::check_every_positive_rational_is_the_norm_of_a_rational_rotor
- kind: check
  ref: check.py::check_one_reflection_puts_a_vector_in_a_four_space_isometric_to_the_standard_one
- kind: check
  ref: check.py::check_quadratic_form_on_the_four_space_is_fixed_by_vectors_of_smaller_support
- kind: check
  ref: check.py::check_two_vectors_embed_only_if_their_determinant_is_a_sum_of_three_squares
- kind: check
  ref: check.py::check_linear_functionals_give_additive_weights_and_fifteen_values_recover_them
lineage:
  motivated_by:
  - synthesis.premise-positivity-of-values
  - synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them
  - one-relation.measure-indifference-borns-rule-located
extraction:
  open_problem: op.positivity-of-values
  note: >-
    Extends the stored theorem on two modes to every number of modes $\ell \ge 2$, and to the symmetric idempotents
    of $\Mat_{N}(\Q)$ for every $N \ge 4$. The whole of the extension rests on the two-mode theorem
    (synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear, used at its stored version
    and not reproved): what is added is a reduction, and it is short. Kill conditions registered before computing.
    First: for three modes a function on the projectors that adds on orthogonal ones and is not linear. None
    exists (clause (v)). Second: two rational vectors of $\Q^{8}$ that lie in no four-dimensional rational
    subspace similar to the standard one. This one fired: clause (iv) gives such a pair, so the first step
    named in the open problem (every two rational vectors lie in such a subspace, after which the parallelogram
    law would give a quadratic form at once) is false as stated. The proof given here does not need it: it uses
    one vector at a time, a reflection and an induction on the number of nonzero coordinates, and the only
    arithmetic input is that every positive rational is a sum of four rational squares, which is derived in
    clause (ii) in a few lines (the integer theorem of Lagrange is not needed). No fact on the representation of
    rationals by quadratic forms is imported, and the theorem of Hasse and Minkowski is not used. What is
    machine-verified and what is argued: the check verifies clause (i) completely for three modes (all $64$
    blades), the induction of clause (ii) for the integers up to $293$, the reflection of clause (iii) and the
    span statement behind the induction step of clause (v) on six sample vectors of $\Q^{5}$ to $\Q^{8}$, the
    congruences of clause (iv) exhaustively, and a sample functional for clause (vi); the general statements
    are the proof's. Clause (vii) bears on the open problem's item on parity: from three modes on, the
    projectors of the even subalgebra already carry the theorem for the even subalgebra, so the restriction to
    parity-even projectors loses linearity only on two modes; this also answers the sentence of
    synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them that leaves open
    whether three modes suffice for the even subalgebra (they do). Not established here, argued only: for $N \ge 8$ a
    pair $u, v$ lies in a four-dimensional rational subspace similar to the standard one exactly when its
    determinant is a sum of three rational squares (necessity is clause (iv); sufficiency would use the theorem
    of Hasse and Minkowski and is not claimed). Literature. Gleason's theorem (A. M. Gleason, J. Math. Mech. 6
    (1957) 885; from memory) is the statement for non-negative weights on a real or complex Hilbert space of
    dimension at least three, and the reduction to low dimension is standard there; over $\Q$ the reduction
    needs the subspace to be similar to the standard one, which is why it is done here by the reflection. The
    four-square theorem is Lagrange's (1770) and the multiplicativity of the norm is Euler's identity (both from
    memory). Prior art on the question itself, not read beyond abstracts: D. Kh. Mushtari, Lobachevskii J. Math.
    9 (2001) 47 poses the trace form of non-negative measures on the orthogonal rational projections of $\Q^{n}$
    as an open problem according to the summary recorded with the two-mode theorem; when this result was drafted
    only the abstract of the paper could be read (the full text could not be retrieved), so whether that
    paper contains a reduction from $\Q^{n}$ to $\Q^{4}$ is not known, and no claim of priority is made for the
    reduction. D. Mushtari, Int. J. Theor. Phys. 34 (1995) 1627 and Mat. Zametki 64 (1998) 584 treat orthoadditive
    functions on all rational idempotents of size at least three (abstracts and a colloquium abstract only), a
    larger domain from which the present statement does not follow. Ledger: transport-absent: the theorem is
    about the rational matrix algebra with the transpose; the series' content is where it places (P). Not done:
    other ordered fields (the reduction needs every sum of squares of the field to be a sum of four squares and
    the theorem in size four over that field, which is not stored); sizes $N = 3$ and blocks of size $2$.
---

## formal
Let $N \ge 4$. A \emph{projector} of $\Mat_{N}(\Q)$ is a symmetric idempotent; for nonzero $r \in \Q^{N}$ the \emph{atom} of $r$ is $\Pi_{r} = rr^{T}/(r \cdot r)$; a \emph{frame} is a set of $N$ pairwise orthogonal nonzero vectors, taken up to scale. Let $V$ be a vector space over $\Q$. An \emph{additive weight} with values in $V$ is a function $\mu$ from the projectors to $V$ with $\mu(E + E') = \mu(E) + \mu(E')$ whenever $EE' = 0$. No sign condition, normalisation or continuity is assumed. For a set $S$ of coordinates, $\Q^{S}$ is the coordinate subspace; the support of $r$ is the set of its nonzero coordinates. Let $\Cl_{\Q}(\ell,\ell)$ be the algebra of $\ell$ modes: generators $e_{j}$, $f_{j}$ with $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, the adjoint $\dagger$ the linear extension of the inverse on blades, $v_{j} = \tfrac12(e_{j} + f_{j})$, $w_{j} = \tfrac12(e_{j} - f_{j}) = v_{j}^{\dagger}$ (ladder pairs in the sense of Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}), $P_{0} = \prod_{j}w_{j}v_{j}$, and $s_{S} = v_{j_{1}}\cdots v_{j_{k}}P_{0}$ for $S = \{j_{1} < \dots < j_{k}\} \subseteq \{1, \dots, \ell\}$. Let $B_{1} = e_{3}e_{2}$, $B_{2} = e_{1}e_{3}$, $B_{3} = e_{2}e_{1}$ in $\Cl_{\Q}(3,0)$, $x_{r} = r_{0} + r_{1}B_{1} + r_{2}B_{2} + r_{3}B_{3}$ (\claimref{std-algebra.quaternions}) and $\tilde{x}$ the reverse, so that $x_{r}\tilde{x}_{r} = r \cdot r$.
\begin{enumerate}
\item[(i)] \emph{(Modes are matrices; proved.)} For every $\ell \ge 1$, $s_{S}^{\dagger}xs_{T} = m(x)_{ST}P_{0}$ defines an isomorphism $m$ of $\Cl_{\Q}(\ell,\ell)$ onto $\Mat_{2^{\ell}}(\Q)$ with $m(x^{\dagger}) = m(x)^{T}$. The even subalgebra is mapped onto the matrices that vanish between subsets of different parity: two blocks of size $2^{\ell - 1}$.
\item[(ii)] \emph{(Four squares over $\Q$; proved here; classical.)} Every positive rational is $x\tilde{x}$ for a rational $x$ in the even subalgebra of $\Cl_{\Q}(3,0)$, that is, a sum of four rational squares.
\item[(iii)] \emph{(One vector lies in a standard four-space; proved.)} For every nonzero $r \in \Q^{N}$ and every set $S$ of four coordinates there is $s \in \Q^{S}$ with $s \cdot s = r \cdot r$, and if $s \ne r$ the reflection $R$ in $m = r - s$, $R(x) = x - 2\frac{x \cdot m}{m \cdot m}m$ (in the algebra of $\Q^{N}$ with $Q(x) = x \cdot x$, $R(x) = -mxm^{-1}$), has $R(s) = r$. So $W = R(\Q^{S})$ is a four-dimensional rational subspace that contains $r$, lies in $\Q^{S} + \Q r$, and is isometric to the standard $\Q^{4}$.
\item[(iv)] \emph{(Two vectors need not; proved.)} If $u, v \in \Q^{N}$ lie in a four-dimensional rational subspace similar to the standard $\Q^{4}$ (a linear bijection $T$ onto $\Q^{4}$ with $Tx \cdot Ty = c\,x \cdot y$, $c > 0$), then $(u \cdot u)(v \cdot v) - (u \cdot v)^{2}$ is a sum of three rational squares. For $N \ge 5$ the vectors $u = (1,0,0,0,0,\dots)$ and $v = (0,1,1,1,2,0,\dots)$ have $(u \cdot u)(v \cdot v) - (u \cdot v)^{2} = 7$, which is not a sum of three rational squares, so they lie in no such subspace.
\item[(v)] \emph{(Additive weights are linear; proved, given the theorem for two modes.)} For every additive weight $\mu$ on the projectors of $\Mat_{N}(\Q)$ with values in $V$ there are unique $\rho_{ij} = \rho_{ji} \in V$ with
\[
\mu(\Pi_{r}) = \frac{1}{r \cdot r}\sum_{i,j}\rho_{ij}r_{i}r_{j} \quad \text{for all } r \ne 0, \qquad \mu(E) = \sum_{i,j}\rho_{ij}E_{ij} \quad \text{for every projector } E .
\]
In particular, for every $\ell \ge 2$, a function on the self-adjoint idempotents of $\Cl_{\Q}(\ell,\ell)$ that adds on orthogonal pairs is the restriction of a $\Q$-linear map $L(x) = \sum\rho_{ST}m(x)_{ST}$, and $L$ is the only linear extension with $L(x^{\dagger}) = L(x)$.
\item[(vi)] \emph{(With the sign condition: the states of (P); proved.)} Let $V = \Q$. A \emph{state} is a linear $\omega$ on $\Cl_{\Q}(\ell,\ell)$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$, $\omega(x^{\dagger}) = \omega(x)$ (the states of the premise of positivity of values, (P)). For $\ell \ge 2$, an additive weight with $\mu(\Pi) \ge 0$ on every atom and $\mu(1) = 1$ is the restriction of exactly one state, and every state restricts to such a weight.
\item[(vii)] \emph{(Even projectors suffice from three modes on; proved.)} Let $\ell \ge 3$. A function defined only on the self-adjoint idempotents of the even subalgebra of $\Cl_{\Q}(\ell,\ell)$ that adds on orthogonal pairs is the restriction of a $\Q$-linear map on the even subalgebra, unique among those with $L(x^{\dagger}) = L(x)$. For $\ell = 2$ this fails: the blocks have size two, where every function with $f(r) + f(r^{\perp})$ constant is an additive weight (an example is the stored two-valued weight on the even subalgebra of two modes, \claimref{synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them}).
\end{enumerate}
\emph{Reading.} The theorem for two modes (\claimref{synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear}) carries over to every number of modes: additivity on orthogonal rational projectors alone gives linearity, and of what the premise (P) asserts about projectors only the sign is not implied. The reduction is not the one first proposed (two vectors in one standard four-space), which (iv) rules out; one vector at a time is enough. As for two modes, nothing here derives (P): the sign is not implied, and that elements whose spectral projectors are not rational take the value of the linear extension is not a statement about weights on projectors. Clause (vii) changes one earlier remark: the theorem for two modes uses projectors that are odd under the total parity, and with even projectors alone it fails there; from three modes on the even projectors give linearity on the even subalgebra.

## technical
The stored theorem says that on the algebra of two modes over the rationals, which is the four by four rational matrices with the transpose as adjoint, a function on the symmetric idempotents that adds on orthogonal pairs is the restriction of a linear functional, with no sign or boundedness condition. This result extends it to the symmetric idempotents of the $N$ by $N$ rational matrices for every $N \ge 4$, hence to every number of modes, by a reduction that uses the two-mode theorem as given. Put $F(r) = (r \cdot r)\mu(\Pi_{r})$. On any four-dimensional rational subspace isometric to the standard one, the two-mode theorem makes $F$ a quadratic form. Subtract the quadratic form fixed by the values at the coordinate vectors and at the sums of two of them; the remainder $G$ vanishes on vectors with at most four nonzero coordinates. For a vector $r$ with more, write $r \cdot r$ as a sum of four rational squares, giving a vector $s$ in four of the coordinates of $r$ with the same square, and reflect $s$ to $r$: the image $W$ of the coordinate four-space contains $r$ and lies in the span of those four coordinates and $r$. On $W$, $G$ is a quadratic form, and it vanishes on the hyperplanes of $W$ where one coordinate is zero, by induction on the number of nonzero coordinates; at least four of these hyperplanes are distinct, and a quadratic form that vanishes on three distinct hyperplanes of a four-space is zero. So $G(r) = 0$. The only arithmetic input is the four-square theorem in its rational form, which follows from the multiplicativity of the rotor norm and a pigeonhole count by induction on primes, without the descent of the integer theorem. The shortcut proposed with the open problem, that any two rational vectors lie in one four-dimensional subspace similar to the standard one, is false: by the identity $(x\tilde{x})(y\tilde{y}) = \langle y\tilde{x}\rangle_{0}^{2} - \langle y\tilde{x}\rangle_{2}^{2}$ the determinant of two vectors of such a subspace is a sum of three rational squares, and the pair $(1,0,0,0,0)$, $(0,1,1,1,2)$ has determinant $7$. With non-negativity and normalisation the weights are exactly the restrictions of the states of (P). The even subalgebra of $\ell$ modes is two matrix blocks of size $2^{\ell-1}$, so from three modes on the theorem applies to each block and the projectors of the even subalgebra alone give linearity there; on two modes the blocks have size two and it fails. The result is transport-absent: it is a statement about rational matrices.

## lay
An earlier result of the series looked at the algebra of two modes with rational numbers only. It showed that if every yes-or-no question gets one number, the same whichever compatible questions it is asked with, and the numbers of mutually exclusive questions add up, then the numbers follow a formula of the same form as the usual quantum rule (without the guarantee that none is negative). This result shows the same for any number of modes. The idea is to reduce the big case to the small one. Any single question in the big algebra can be placed inside a copy of the two-mode situation, by a mirror reflection with rational entries; this uses the old fact that every positive fraction is a sum of four squares of fractions. Inside that copy the earlier result applies, and a short induction then ties all the copies together. A more direct plan, to place any two questions inside one copy at once, turns out to be impossible in general, for an arithmetic reason (the number 7 is not a sum of three squares). The result still does not show that the numbers are never negative; that remains an assumption.

## one-liner
For every $N \ge 4$, hence in $\Cl_{\Q}(\ell,\ell)$ for every $\ell \ge 2$, a function on the symmetric idempotents of $\Mat_{N}(\Q)$ that adds on orthogonal ones, with values in any rational vector space and no sign condition, is the restriction of a linear functional (given the stored theorem for two modes; the reduction uses one reflection per vector and four rational squares, since two rational vectors need not lie in one four-space similar to the standard one: determinant $7$ is an obstruction); with non-negativity and normalisation these are the restrictions of the states of (P); from three modes on the even projectors alone give linearity on the even subalgebra.
