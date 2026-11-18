---
id: synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear
kind: claim
version: 1
title: 'Additive weights on the rational projectors of two modes are linear; no sign condition'
status: proved
region: synthesis
subject: clifford-structure
tags: [finite-models, classical-theorem, measurement-and-records]
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
derivations:
- name: main
  uses:
  - synthesis.signed-directions-and-the-integer-clifford-algebra@2
  - tower.ladder-pairs-satisfy-car-vectors@4
  - std-algebra.quaternions@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_two_modes_are_the_rational_matrices_of_size_four_and_the_adjoint_is_the_transpose
- kind: check
  ref: check.py::check_frames_are_cosets_of_the_klein_groups_of_half_turns
- kind: check
  ref: check.py::check_octahedral_rays_span_a_copy_of_the_three_by_three_matrices
- kind: check
  ref: check.py::check_certificate_puts_the_rotor_two_plus_b1_in_the_octahedral_span
- kind: check
  ref: check.py::check_integer_rotors_of_norm_a_power_of_five_factor_into_six_rotors_and_a_unit
- kind: check
  ref: check.py::check_conjugate_of_a_power_by_a_half_turn_is_an_integer_rotor_of_norm_a_power_of_five
- kind: check
  ref: check.py::check_half_turn_relation_forces_the_central_factor_to_be_one
- kind: check
  ref: check.py::check_linear_functionals_give_the_weights_and_non_negative_weights_are_states
- kind: check
  ref: check.py::check_atoms_of_rational_unit_vectors_admit_an_additive_weight_that_is_not_linear
lineage:
  motivated_by:
  - synthesis.premise-positivity-of-values
  - synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them
  - synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects
  - one-relation.measure-indifference-borns-rule-located
extraction:
  open_problem: op.positivity-of-values
  note: >-
    Answers the item of the open problem that asks whether non-negative additive weights on the projectors with
    rational coefficients of two modes (size four over $\Q$) are restrictions of linear functionals, a statement
    of Gleason type. The answer is yes, and the sign condition is not needed: additivity on orthogonal projectors
    alone gives linearity. Kill conditions registered before computing: a non-constant weight depending only on
    the primitive integer vector modulo $8$ (none: the frame equations of $9000$ integer frames have full rank on
    the $1920$ classes); a gap that persists in a linear programme on growing boxes of rays (none: the admissible
    values close on the quadratic value, and from entries up to $4$ they are pinned by equalities); failure of
    any of the exact computations the proof relies on (none failed). What is machine-verified and what is argued:
    the proof is complete on paper except for four finite exact computations done in the check (the $24$
    octahedral rays and the rank $15$ of their relations; the identity of $34$ frames that puts the rotor
    $2 + B_{1}$ in their span; the division table modulo $5$; the conjugates of $2 + B_{1}$ by the octahedral
    rotors). The $34$ frames were found by a linear programme and the identity is verified in exact arithmetic;
    the check also runs the argument end to end on ten sample bivectors. No uses edge is drawn to the stored
    results on positivity of values: the adjoint, the elements $s_{i}$ and the atoms $\Pi_{r}$ are defined here as
    in synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them and
    synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate, so that nothing
    here is under a premise about values; the premise synthesis.premise-positivity-of-values and the functional
    of synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state are
    named in clause (iv) for a comparison, with their definitions restated. Literature. Gleason's theorem (A. M.
    Gleason, J. Math. Mech. 6 (1957) 885; from memory) is the statement for non-negative weights on a real or
    complex Hilbert space of dimension at least three; it is not used. Prior art on exactly this structure
    exists and was not read in full: D. Kh. Mushtari, Some remarks on measures on orthogonal rational projections
    and the rational sphere, Lobachevskii J. Math. 9 (2001) 47 (abstract read on the web: it examines measures on
    the logic of all projections with rational $n \times n$ matrices and on the sublogic of lines through
    rational unit vectors; the full text could not be opened in this pass, so whether it contains clause (iii)
    or clause (v) is not known); D. Kh. Mushtari, The Gleason theorem for the field of rational numbers and
    residue fields, Mat. Zametki 64 (1998) 584 (abstract read on the web: the representation $\mu(P) =
    \operatorname{tr}(T_{\mu}P)$ for charges on the logic of all projectors, not only the self-adjoint ones, of
    a finite-dimensional space over $\Q$). No claim of priority is made. The colouring behind clause (v) is that
    of C. D. Godsil and J. Zaks and of D. A. Meyer in dimension three (from memory), carried to dimension four
    here with its proof. Not done: more than two modes (the first step would be to show that any two rational
    vectors of $\Q^{2^{\ell}}$ lie in a four-dimensional rational subspace similar to the standard one, so that
    the present theorem applies to it); other ordered fields.
---

## formal
Let $\Cl_{\Q}(2,2)$ be the algebra of two modes: generators $e_{j}$, $f_{j}$, $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, the adjoint $\dagger$ the linear extension of the inverse on blades, $v_{j} = \tfrac12(e_{j} + f_{j})$, $w_{j} = \tfrac12(e_{j} - f_{j}) = v_{j}^{\dagger}$ the ladder pairs of Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}, $P_{0} = w_{1}v_{1}w_{2}v_{2}$, $s_{0} = P_{0}$, $s_{1} = v_{1}P_{0}$, $s_{2} = v_{2}P_{0}$, $s_{3} = v_{1}v_{2}P_{0}$, and for nonzero $r \in \Q^{4}$, $y_{r} = \sum_{i}r_{i}s_{i}$, $\Pi_{r} = y_{r}y_{r}^{\dagger}/(r \cdot r)$. A \emph{projector} is a self-adjoint idempotent; a \emph{frame} is a set of four pairwise orthogonal nonzero vectors of $\Q^{4}$, taken up to scale (rays). Let $V$ be a vector space over $\Q$. An \emph{additive weight} with values in $V$ is a function $\mu$ from the projectors to $V$ with $\mu(E + E') = \mu(E) + \mu(E')$ whenever $EE' = 0$. No sign condition, normalisation or continuity is assumed. Let $B_{1} = e_{3}e_{2}$, $B_{2} = e_{1}e_{3}$, $B_{3} = e_{2}e_{1}$ be the unit bivectors of $\Cl_{\Q}(3,0)$, which with $1$ span its even subalgebra (\claimref{std-algebra.quaternions}), $x_{r} = r_{0} + r_{1}B_{1} + r_{2}B_{2} + r_{3}B_{3}$, and $\tilde{x}$ the reverse.
\begin{enumerate}
\item[(i)] \emph{(Matrices; proved.)} $s_{i}^{\dagger}xs_{j} = m(x)_{ij}P_{0}$ defines an isomorphism $m$ of $\Cl_{\Q}(2,2)$ onto $\Mat_{4}(\Q)$ with $m(x^{\dagger}) = m(x)^{T}$ and $m(\Pi_{r}) = rr^{T}/(r \cdot r)$. The projectors are the orthogonal projections onto the rational subspaces, each is a sum of pairwise orthogonal $\Pi_{r}$, and those of rank one (the atoms) are exactly the $\Pi_{r}$. So an additive weight is the same thing as a function $f(r) = \mu(\Pi_{r})$ on the rays of $\Q^{4}$ whose sum over every frame is the same element $\mu(1)$ of $V$.
\item[(ii)] \emph{(Rotors; proved.)} $x_{r}\tilde{x}_{r} = r \cdot r$ and $\langle x_{r}\tilde{x}_{r'}\rangle_{0} = r \cdot r'$, so two rays are orthogonal exactly when $x_{r}x_{r'}^{-1}$ is a bivector. The frames are exactly the sets $\{x, ax, bx, abx\}$ with $a, b$ orthogonal nonzero rational bivectors and $x$ a nonzero element of the even subalgebra: cosets of the groups of half turns about three orthogonal rational directions.
\item[(iii)] \emph{(Additive weights are linear; proved, with four finite exact computations carried by the check.)} For every additive weight $\mu$ with values in $V$ there are unique $\rho_{ij} = \rho_{ji} \in V$ with
\[
\mu(\Pi_{r}) = \frac{1}{r \cdot r}\sum_{i,j}\rho_{ij}r_{i}r_{j} \quad \text{for all } r, \qquad \mu(E) = L(E), \quad L(x) = \sum_{i,j}\rho_{ij}\,m(x)_{ij},
\]
so $\mu$ is the restriction to the projectors of a $\Q$-linear map $L$ on $\Cl_{\Q}(2,2)$, and $L$ is the only linear extension with $L(x^{\dagger}) = L(x)$. Equivalently $\mu(\Pi_{r}) = \tfrac14\mu(1) + \Lambda(R(x_{r}))$ with $R(x)$ the rotation $n \mapsto xnx^{-1}$ of the bivectors and $\Lambda$ linear on $\Mat_{3}(\Q)$. In the proof the rotors enter through three facts: the $24$ rays with entries in $\{0, \pm 1\}$ and $r \cdot r \in \{1, 2, 4\}$ are a group $O$ (the octahedral group) whose classes span a copy of $\Mat_{3}(\Q)$ in the quotient of the group algebra by the frame relations; the value at the ray of $2 + B_{1}$ is a fixed rational combination of $\mu(1)$ and the values on $O$, by an identity of $34$ frames with entries up to $4$; every $x$ with integer components and $x\tilde{x}$ a power of $5$ is a product of the six rotors $2 \pm B_{k}$ and one of $\pm 1, \pm B_{k}$.
\item[(iv)] \emph{(With the sign condition: the states of (P); proved.)} Let $V = \Q$. A \emph{state} is a linear $\omega$ on $\Cl_{\Q}(2,2)$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(x^{\dagger}) = \omega(x)$ (the states of the premise of positivity of values, (P)). An additive weight with $\mu(\Pi_{r}) \ge 0$ for all $r$ and $\mu(1) = 1$ is the restriction of exactly one state, and every state restricts to such a weight. So on two modes over $\Q$ the linearity that (P) asserts follows from additivity on orthogonal projectors; what (P) adds to "weights on projectors exist, do not depend on the context and add" is the sign condition only. The functional $\lambda(x) = \langle(1 + C)x\rangle_{0}$ with $C = A_{1}(B'_{1} + B'_{2}) + A_{2}(B'_{1} - B'_{2})$, $A_{1} = e_{1}$, $A_{2} = f_{1}e_{1}$, $B'_{1} = e_{2}f_{1}e_{1}$, $B'_{2} = f_{2}e_{2}$ (the stored functional with $\lambda(C) = 4$) restricts to an additive weight with $\mu(1) = 1$, and $\lambda(\Pi_{(1,0,0,1)}) = -\tfrac14$.
\item[(v)] \emph{(The atoms of rational unit vectors alone do not suffice; proved.)} Call $\Pi_{r}$ a unit atom if $r \cdot r$ is the square of a rational. A primitive integer vector $r$ with $r \cdot r$ a square has either exactly one odd coordinate or four. For $\alpha_{0}, \dots, \alpha_{3} \in \Q$ with sum $1$ let $g(\Pi_{r}) = \alpha_{i}$ if the $i$-th coordinate of $r$ is the odd one and $g(\Pi_{r}) = \tfrac14$ if all are odd. Then $g$ sums to $1$ on every frame of unit atoms, it is non-negative if the $\alpha_{i}$ are, and it is of the form $\sum\rho_{ij}r_{i}r_{j}/(r \cdot r)$ on the unit atoms only if $\alpha_{i} = \tfrac14$ for all $i$.
\end{enumerate}
\emph{Reading.} (iii) decides the question left open by the stored result on two-valued weights on the atoms of two modes: over $\Q$, in size four, a weight on projectors that adds on orthogonal projectors is linear, and neither non-negativity nor boundedness is needed (over $\R$ the corresponding statement needs them). The atoms that carry the theorem are those of rational rays whose unit vectors are not rational: on the unit atoms alone (v) gives non-negative additive weights that are not linear, and with $\alpha = (1, 0, 0, 0)$ a weight with values in $\{0, \tfrac14, 1\}$. In size two no such theorem holds, and the even subalgebra of two modes admits a two-valued additive weight (both stored). (iv) locates what the premise (P) assumes on two modes: non-contextual weights on the rational projectors that add on orthogonal ones and are non-negative; the stored functional of value $4$ meets everything but the sign. Nothing here derives (P), and more than two modes are not treated.

## technical
The stored account of the Born rule isolates a residual postulate, that weights exist and add, and the premise of positivity of values (P) assumes in addition that values are linear across elements that do not commute. For the algebra of two modes over the rationals this result shows that the linearity is not an extra assumption: any function on the self-adjoint idempotents that adds on orthogonal pairs, with values in any rational vector space and with no sign or boundedness condition, is the restriction of a linear functional. The algebra is the four by four rational matrices with the transpose as adjoint, its projectors of rank one are the rays of $\Q^{4}$, and the rays are the nonzero elements of the even subalgebra of $\Cl_{\Q}(3,0)$ up to scale, a group of rational rotors. Two rays are orthogonal when their quotient is a half turn, and a frame is a coset of the four-element group of half turns about three orthogonal rational directions. So an additive weight of total weight zero is a linear map on the group algebra that kills the frame relations, and the theorem says that the quotient of the group algebra by those relations is the three by three matrices, through the rotation representation. The proof has a finite part and a general part. Finite: the $24$ rotors of the octahedral group already span a copy of the matrix algebra in the quotient; one further rotor, $2 + B_{1}$, a rotation of infinite order, lies in that span by an identity of $34$ frames with integer entries up to $4$, verified exactly; and integer rotors whose norm is a power of $5$ factor into the six rotors $2 \pm B_{k}$ by a table modulo $5$. General: for any rational half turn, a suitable power of $2 + B_{1}$ is conjugated by it to an integer rotor of norm a power of $5$, hence to a known element, so the class of the half turn commutes, up to its rotation matrix, with two rotations about different axes and is that matrix times a central factor; the frame relation of an orthogonal triple forces the factor to be $1$; and half turns generate the group. With non-negativity and normalisation the weights are exactly the states of (P). On the atoms of rational unit vectors alone the theorem fails, by a parity colouring. Prior work by Mushtari on measures on rational projections exists and was not read in full; no priority is claimed.

## lay
Quantum theory assigns probabilities to yes-or-no questions, and the usual rule makes them depend on the question in one particular smooth way. A famous theorem says that this rule is forced once the probabilities of mutually exclusive questions add up, provided they are never negative and the numbers used are the real numbers. This result looks at the series' algebra of two modes with rational numbers only, and finds something stronger there: if the numbers assigned to mutually exclusive questions simply add up, the usual rule follows, even if negative numbers were allowed. The proof turns each question into a rotation of space with rational entries, shows by a finite exact computation that a handful of rotations determine one more, and then spreads that to all of them. It does not show that the numbers are never negative; that remains an assumption. And it needs all questions that can be written with rational numbers: if only a smaller natural family is allowed, other rules exist.

## one-liner
In $\Cl_{\Q}(2,2)$, with projectors the symmetric idempotents of $\Mat_{4}(\Q)$ and rays read as rational rotors of $\Cl_{\Q}^{+}(3,0)$ (frames are cosets of half-turn groups), every function on projectors that adds on orthogonal ones, with values in any rational vector space and no sign condition, is the restriction of a linear functional, $\mu(\Pi_{r}) = \sum\rho_{ij}r_{i}r_{j}/(r \cdot r)$; with non-negativity these are exactly the states of (P); on the atoms of rational unit vectors alone a parity colouring gives additive weights that are not linear.
