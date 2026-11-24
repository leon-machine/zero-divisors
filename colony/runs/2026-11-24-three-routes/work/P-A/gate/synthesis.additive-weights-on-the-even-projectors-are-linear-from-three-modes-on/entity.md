---
id: synthesis.additive-weights-on-the-even-projectors-are-linear-from-three-modes-on
kind: claim
version: 1
title: 'Additive weights on parity-even rational projectors are linear from three modes on'
status: proved
region: synthesis
subject: clifford-structure
tags: [finite-models, grading-and-parity, measurement-and-records]
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
  why: "The even subalgebra is identified as the commutant of the pseudoscalar with the Clifford product, and the block projectors are (1 +- Gamma)/2. The remaining steps are linear algebra of rational matrices in two blocks, and the parity of integers for the counterexample on two modes."
derivations:
- name: main
  uses:
  - synthesis.additive-weights-on-the-rational-projectors-are-linear-in-every-size-from-four@1
  - synthesis.signed-directions-and-the-integer-clifford-algebra@2
  - tower.ladder-pairs-satisfy-car-vectors@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_even_subalgebra_of_three_modes_is_the_commutant_of_the_pseudoscalar_and_two_blocks_of_size_four
- kind: check
  ref: check.py::check_block_atoms_of_three_modes_are_even_projectors_and_a_linear_weight_is_recovered_block_by_block
- kind: check
  ref: check.py::check_two_modes_have_blocks_of_size_two_and_a_parity_weight_on_a_block_is_additive_and_not_linear
lineage:
  motivated_by:
  - synthesis.premise-positivity-of-values
  - synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them
  - synthesis.records-keep-even-states-even-only-for-parity-homogeneous-observables
extraction:
  open_problem: op.positivity-of-values
  note: >-
    A corollary of the stored theorem for every size from four
    (synthesis.additive-weights-on-the-rational-projectors-are-linear-in-every-size-from-four), which carries
    all the content; what is added is the identification of the even subalgebra of $\ell$ modes with two matrix
    blocks of size $2^{\ell-1}$ through the pseudoscalar, and the remark that the theorem then applies block by
    block as soon as the blocks have size four. What it settles. First, the sentence of
    synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them that an argument
    of that type for parity-even elements needs at least three modes, "whether three suffice is not shown
    here": three suffice, in the stronger form that every additive weight on the even projectors is linear, so
    in particular none is two-valued. Second, the item of the open problem on which projectors can label a
    record says that the choice of all rational projectors is tied to the item on parity, because the theorem
    for two modes uses projectors that are odd under the total parity: that tie holds on two modes only. From
    three modes on, the projectors of the even subalgebra alone give linearity on the even subalgebra. What it
    does not settle: whether elements odd under the total parity are observables; whether records are labelled
    by even projectors, by all projectors, or by a smaller family; the sign, which additivity does not imply
    (the check has a linear weight with the value $-1$ on an even projector); the values of odd elements, on
    which a weight defined on even projectors says nothing; and nothing here derives (P). Like the theorem it
    rests on, it holds over the rational scalars and given the stored theorem for size four. Kill condition
    fixed before computing: an even self-adjoint idempotent of three modes that is not a sum of one projector
    in each block, or blocks of size other than four; neither occurred. What is machine-verified: for three
    modes, the pseudoscalar's action on the eight elements $s_{I}$, its commutation with all $64$ blades, the
    block form of the matrices of all blades with ranks $64$ and $32$, and the block identities
    $\tfrac12(1 \pm \Gamma)$; a sample linear weight evaluated in the algebra on block atoms and recovered from
    twenty values; for two modes, the parity weight on a block. The passage from additive to linear is the
    stored theorem's and is not recomputed. The parity weight is the one the stored theorem's note gives for
    one mode, placed on a block of two modes. Ledger: transport-absent (a statement about rational matrices in
    two blocks). Not done: the family of sector projectors of Witt flags adapted to the split, which is a
    proper subfamily of the even projectors and for which the question is open.
---

## formal
Let $\Cl_{\Q}(\ell,\ell)$ be the algebra of $\ell$ modes with generators $e_{j}$, $f_{j}$, $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, the adjoint $\dagger$ the linear extension of the inverse on blades, and $v_{j}$, $w_{j}$, $P_{0}$, $s_{I}$ and the isomorphism $m$ onto $\Mat_{2^{\ell}}(\Q)$, $m(x^{\dagger}) = m(x)^{T}$, as in clause (i) of \claimref{synthesis.additive-weights-on-the-rational-projectors-are-linear-in-every-size-from-four}. Let $\Gamma = e_{1}f_{1}e_{2}f_{2}\cdots e_{\ell}f_{\ell}$ be the pseudoscalar. An \emph{even projector} is a self-adjoint idempotent of the even subalgebra. Let $V$ be a vector space over $\Q$. An \emph{additive weight on the even projectors} is a function $\mu$ from the even projectors to $V$ with $\mu(E + E') = \mu(E) + \mu(E')$ whenever $EE' = 0$; it is not assumed to be defined on any projector that is not even, and no sign condition, normalisation or continuity is assumed.
\begin{enumerate}
\item[(i)] \emph{(The even subalgebra is two blocks; proved for every $\ell \ge 1$, computed for $\ell = 3$.)} $\Gamma^{2} = 1$, $\Gamma^{\dagger} = \Gamma$, $\Gamma$ commutes with even elements and anticommutes with odd ones, and $\Gamma s_{I} = (-1)^{|I|}s_{I}$. So the even subalgebra is the commutant of $\Gamma$, and $m$ maps it onto the matrices with $M_{IJ} = 0$ whenever $|I| + |J|$ is odd: two blocks of size $2^{\ell-1}$, with block identities $m(\tfrac12(1 \pm \Gamma))$. The even projectors are the $E_{+} + E_{-}$ with $E_{\pm}$ a projector below $\tfrac12(1 \pm \Gamma)$, that is, pairs of symmetric idempotents of $\Mat_{2^{\ell-1}}(\Q)$.
\item[(ii)] \emph{(Linearity from three modes on; proved, given the stored theorem for every size from four.)} Let $\ell \ge 3$. Every additive weight $\mu$ on the even projectors with values in $V$ is the restriction of a $\Q$-linear map $L$ from the even subalgebra to $V$, and $L$ is the only one with $L(x^{\dagger}) = L(x)$. In matrix form $\mu(E) = \sum_{|I| + |J|\ \mathrm{even}}\rho_{IJ}\,m(E)_{IJ}$ with unique $\rho_{IJ} = \rho_{JI} \in V$.
\item[(iii)] \emph{(With the sign condition; proved.)} Let $\ell \ge 3$ and $V = \Q$. If moreover $\mu(E) \ge 0$ for every even projector and $\mu(1) = 1$, then $L(xx^{\dagger}) \ge 0$ for every even $x$, and $\omega(x) = L(\tfrac12(x + \Gamma x\Gamma))$ is a state of the premise \claimref{synthesis.premise-positivity-of-values} on the whole algebra (linear, $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$, $\omega(x^{\dagger}) = \omega(x)$) that restricts to $\mu$ and vanishes on odd elements; it is the only state with these two properties.
\item[(iv)] \emph{(One and two modes; proved.)} For $\ell = 1$ the blocks have size one, the even projectors are $0$, $\tfrac12(1 \pm \Gamma)$, $1$, and (ii) holds trivially. For $\ell = 2$ the blocks have size two and (ii) fails: on the rays of one block, written as primitive integer vectors $(a, b)$, the function that is $1$ if $a$ is odd and $b$ even, $0$ if $a$ is even and $b$ odd, and $\tfrac12$ if both are odd, extended by $0$ on the other block, is a non-negative additive weight on the even projectors that is not the restriction of a linear map (its value at $(1, 2)$ is $1$, where the only candidate form gives $\tfrac15$).
\end{enumerate}
\emph{Reading.} This is a corollary of the stored theorem. It answers the question left open by \claimref{synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them} (whether three modes suffice for parity-even elements: they do), and it bears on the item of the open problem on parity: from three modes on, the passage from additive weights to a linear functional does not need projectors that are odd under the total parity. It does not decide whether odd elements are observables, it does not give the sign, and it says nothing about the values of odd elements.

## technical
The stored theorem says that on the rational matrices of every size from four a function on the symmetric idempotents that adds on orthogonal ones is the restriction of a linear functional, and that the algebra of $\ell$ modes is the rational matrix algebra of size $2^{\ell}$ with the transpose as adjoint. On two modes the stored results also show that the projectors of the even subalgebra alone do not carry such a theorem, and left open whether three modes suffice. They do, for a structural reason. The pseudoscalar $\Gamma$ of $\Cl_{\Q}(\ell,\ell)$ squares to one, is self-adjoint, and acts on the elements $s_{I}$ by the sign $(-1)^{|I|}$; the even subalgebra is its commutant, hence two matrix blocks of size $2^{\ell-1}$ with block identities $\tfrac12(1 \pm \Gamma)$. An even projector is a sum of one projector in each block, the two are orthogonal, and so an additive weight on the even projectors is a sum of two additive weights, one on the projectors of each block. For $\ell \ge 3$ the blocks have size at least four and the stored theorem applies to each. For $\ell = 2$ the blocks have size two, where each ray has a single orthogonal ray and additivity is one equation per pair, and a parity weight is a counterexample; for $\ell = 1$ the statement is trivial. With non-negativity and normalisation the weight is the restriction of exactly one state of (P) that vanishes on odd elements. The result is a corollary: all of its content beyond the block decomposition is the stored theorem, and through it the stored theorem for size four. It removes one remark from the account of the premise (P): that reading every rational projector as a possible label of a record needs projectors odd under the total parity is true on two modes only. It does not decide which elements are observables, does not give the sign, and is transport-absent.

## lay
Earlier results of the series showed that, with rational numbers, numbers attached to yes-or-no questions that add up for mutually exclusive questions must follow a formula of the same form as the usual quantum rule, once there are at least two modes. On two modes this needed questions of both parities; with the parity-even questions alone it failed, and it was not known whether more modes would help. This result shows that three modes are enough: the parity-even questions split into two separate families, each of which is by itself a copy of the situation the earlier theorem covers, as soon as each family has size four. On two modes the families have size two, which is too small, and an explicit counterexample is given. The result is a short consequence of the earlier theorem and shares its limits: it does not show that the numbers are never negative.

## one-liner
A corollary of the stored theorem for every size from four: in $\Cl_{\Q}(\ell,\ell)$ the even subalgebra is the commutant of the pseudoscalar $\Gamma$, two matrix blocks of size $2^{\ell-1}$ with identities $\tfrac12(1 \pm \Gamma)$, so for $\ell \ge 3$ a function defined only on the self-adjoint idempotents of the even subalgebra that adds on orthogonal ones is the restriction of a linear map on the even subalgebra (with non-negativity and normalisation, of one state of (P) vanishing on odd elements), while for $\ell = 2$ (blocks of size two) a parity weight is additive and not linear; the sign and the status of odd elements are not decided.
