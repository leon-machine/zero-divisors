---
id: synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them
kind: claim
version: 1
title: 'No two-valued weights on the rational atoms of two modes; the even subalgebra admits them'
status: proved
region: synthesis
subject: clifford-structure
tags: [entanglement, finite-models, classical-theorem, measurement-and-records]
proposed_by:
  kind: ai
  session: 2026-11-10-phase2
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase2
review: draft
derivations:
- name: main
  uses:
  - synthesis.signed-directions-and-the-integer-clifford-algebra@2
  - tower.ladder-pairs-satisfy-car-vectors@4
  - tower.commuting-copies@5
  - synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate@1
  - synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional@1
  - synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_eighteen_atoms_in_nine_contexts_admit_no_two_valued_weight
- kind: check
  ref: check.py::check_square_of_nine_blades_has_no_multiplicative_sign_assignment
- kind: check
  ref: check.py::check_even_subalgebra_of_two_modes_has_a_two_valued_weight
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.premise-positivity-of-values
  - one-relation.imported-envariance-born-rule
  - one-relation.measure-indifference-borns-rule-located
extraction:
  open_problem: op.positivity-of-values
  note: >-
    Placement in the series' algebra of the Kochen-Specker theorem, asked for by the question which statements
    of Gleason and Kochen-Specker type hold in the stored finite algebras over the rationals. Kill condition
    registered before computing: an assignment of $0$ and $1$ to the eighteen idempotents with exactly one $1$
    in each of the nine contexts, or the eighteen not lying in the algebra over $\Q$; neither occurred
    (exhaustive search over $2^{18}$ assignments). The eighteen vectors are those of Cabello, Estebaranz and
    Garcia-Alcaine, Bell-Kochen-Specker theorem: a proof with 18 vectors, Phys. Lett. A 212 (1996) 183,
    arXiv:quant-ph/9706009 (title and existence confirmed on the web by the referee; the table of vectors is
    from memory and verified here by enumeration), and the square of nine observables is that of Peres, Phys.
    Lett. A 151 (1990) 107, and Mermin, Phys. Rev. Lett. 65 (1990) 3373 (both from memory), with every property
    used recomputed here. Prior art over the rationals: D. A. Meyer, Finite precision measurement nullifies the
    Kochen-Specker theorem, Phys. Rev. Lett. 83 (1999) 3751, arXiv:quant-ph/9905080 (abstract checked on the
    web by the referee): the unit vectors with rational coordinates in dimension three can be coloured. Clause
    (i) does not conflict with it: its atoms are all rank-one projectors with rational coefficients, a larger
    set that contains rays whose unit vectors are not rational; Kent's extension of Meyer's result to all
    dimensions is from memory only. What is proved: over $\Q$,
    with no premise about values, the weights of the stored residual postulate that weights exist and add
    (one-relation.measure-indifference-borns-rule-located) cannot all be $0$ or $1$ on the atoms of two modes
    if they do not depend on the context; and on the even subalgebra of two modes such weights exist, so a
    statement of this type about parity-even elements needs more than two modes (whether three suffice is not
    shown). No statement of Gleason type
    (non-negative additive weights are linear) is proved here for size $4$ over $\Q$: a search for additive
    weights depending only on the residue of the integer vector modulo $2$, $3$ or $4$ found only the constant
    one (computed, in the run's scratch, not part of this result), and the question is left open. Size $2$ is clause (iii) of the stored result on weights on effects and the definition of an atom is that of
    the stored result on the Born weights under (P); both are cited (for a definition and a comparison; nothing
    here is under (P)).
    (P) is named in the Reading as plain text; nothing is assumed and no edge to it is wanted beyond lineage.
---

## formal
Let $\Cl_{\Q}(2,2)$ be the algebra of two modes: generators $e_{j}$, $f_{j}$, $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, $p_{j} = f_{j}e_{j}$, the adjoint $\dagger$ the linear extension of the inverse on blades (Theorem \claimref{synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate}), and $v_{j} = \tfrac12(e_{j} + f_{j})$, $w_{j} = \tfrac12(e_{j} - f_{j}) = v_{j}^{\dagger}$ the ladder pairs of Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}. An \emph{atom} is an atom in the sense of Theorem \claimref{synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional} (a nonzero projector whose corner has only the multiples of the projector self-adjoint); the atoms exhibited here are of the special form named in its Definitions, $\Pi x\Pi = 4\langle\Pi x\rangle_{0}\Pi$ for all $x$ (corner $\Q\Pi$, $\langle\Pi\rangle_{0} = \tfrac14$), and are atoms of the orbit of clause (ii) of that theorem; a \emph{context} is a set of four atoms with pairwise products $0$ and sum $1$. No premise about values is assumed.
\begin{enumerate}
\item[(i)] \emph{(No two-valued weight on the atoms; proved, the search complete.)} Let $P_{0} = w_{1}v_{1}w_{2}v_{2} = \tfrac14(1 - p_{1})(1 - p_{2})$, the projector annihilated by $w_{1}$, $w_{2}$ on the left (the fully occupied projector in the convention in which $v_{j}$ annihilates $\prod_{j}\tfrac12(1 + p_{j})$; not the vacuum projector of that convention), $s_{0} = P_{0}$, $s_{1} = v_{1}P_{0}$, $s_{2} = v_{2}P_{0}$, $s_{3} = v_{1}v_{2}P_{0}$. Then $s_{i}^{\dagger}s_{j} = \delta_{ij}P_{0}$ and $\sum_{i}s_{i}s_{i}^{\dagger} = 1$, and for every nonzero $r \in \Z^{4}$ the element $\Pi_{r} = y_{r}y_{r}^{\dagger}/(r \cdot r)$, $y_{r} = \sum_{i}r_{i}s_{i}$, is an atom with rational coefficients; $\Pi_{r}\Pi_{r'} = 0$ when $r \cdot r' = 0$, and four pairwise orthogonal vectors give a context. For the eighteen vectors with entries in $\{0, \pm 1\}$ listed in the proof, which form nine contexts with every vector in exactly two of them, there is no function $g$ from the eighteen atoms to $\{0, 1\}$ with $\sum_{\Pi \in c}g(\Pi) = 1$ for each of the nine contexts $c$. Hence there is no function from the atoms of $\Cl_{\Q}(2,2)$ to $\{0, 1\}$ that sums to $1$ on every context.
\item[(ii)] \emph{(No multiplicative signs on nine blades; proved.)} With $X_{1} = e_{1}$, $Z_{1} = p_{1}$, $X_{2} = e_{2}p_{1}$, $Z_{2} = p_{2}$ ($X_{2}$ the twisted generator of Theorem \claimref{tower.commuting-copies}), the nine elements
\[
\begin{array}{ccc} X_{1} & X_{2} & X_{1}X_{2} \\ Z_{2} & Z_{1} & Z_{1}Z_{2} \\ X_{1}Z_{2} & Z_{1}X_{2} & X_{1}X_{2}Z_{1}Z_{2} \end{array}
\]
are self-adjoint blades up to sign, of square $1$; the three of each row commute and the three of each column commute; the product of each column and of the first two rows is $1$ and the product of the third row is $-1$. So there is no assignment $\nu$ of $\pm 1$ to the nine with $\nu(a)\nu(b)\nu(c) = abc$ on every row and column.
\item[(iii)] \emph{(The even subalgebra of two modes admits a two-valued weight; proved.)} Let $\mathcal{A}^{+}$ be the even subalgebra of $\Cl_{k}(2,2)$, $k$ a subfield of $\R$. There is a function $g$ from the self-adjoint idempotents of $\mathcal{A}^{+}$ to $\{0, 1\}$ with $g(1) = 1$ and $g(E + E') = g(E) + g(E')$ whenever $EE' = 0$. The eighteen atoms of (i) are not all even.
\end{enumerate}
\emph{Reading.} (i) and (ii) are statements about the algebra over $\Q$ and need no linearity and no positivity: weights that exist, add within each context and do not depend on the context cannot all be $0$ or $1$ on two modes. The statement is about all atoms with rational coefficients, which include rays such as $(1,1,0,0)$ whose unit vector needs $\sqrt{2}$ (nine of the eighteen vectors have $r \cdot r = 2$): no square root is needed for the projectors, and one is needed for those unit vectors. For the smaller set of atoms of rational unit vectors two-valued weights are known to exist in dimension three (Meyer 1999), and the case of dimension four is not treated here. In size $2$ (one mode) no such obstruction exists: clause (iii) of Theorem \claimref{synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects} gives a non-negative weight on the projectors of one mode that is additive on every pair with sum $1$ and is not linear. (i) and (ii) do not show that such weights are linear in the element; that is the content of the premise of positivity of values, (P), which assumes it and is not assumed here. (iii) says that for parity-even elements of two modes no statement of this type holds: the even subalgebra is a sum of two corners in each of which every context has two members.

## technical
The stored account of the Born rule isolates a residual postulate, that weights exist and add. A classical question is how far that postulate goes without assuming, as (P) does, that values are linear across elements that do not commute. In the algebra of two modes over the rationals the answer has a negative and a positive part. Negative: eighteen self-adjoint primitive idempotents with rational coefficients, built from the ladder pairs, fall into nine sets of four orthogonal ones with sum $1$, each idempotent in two sets, and no assignment of $0$ or $1$ to them gives exactly one $1$ per set; nine blades arranged in a square, commuting along rows and columns, have row products $1, 1, -1$ and column products $1, 1, 1$, so no assignment of signs respects the products. Weights that add and do not depend on the context are therefore not two-valued on the atoms with rational coefficients; the projectors need no square root of $2$ and no continuum, though the unit vectors of nine of the eighteen rays do, and on rational unit vectors alone two-valued weights are known to exist in dimension three (Meyer 1999). Positive: on the parity-even elements of two modes a two-valued additive weight exists, because the even subalgebra splits into two corners in which an idempotent has only one orthogonal partner. So an argument of this type for parity-even elements needs at least three modes; whether three suffice is not shown here. Whether non-negative additive weights on the atoms of two modes over the rationals are forced to be linear is not decided here.

## lay
Can every yes-or-no question about a system have a definite answer fixed in advance, the same whichever other questions are asked together with it? For the series' algebra of two modes the answer is no, already when the questions are described with rational numbers and with no assumption about how averages behave: eighteen yes-or-no questions are arranged in nine groups of four, exactly one answer in each group must be yes, each question lies in two groups, and a count shows this is impossible (nine yes answers would have to be an even number). A second arrangement, nine quantities in a square, gives the same conclusion from signs. If only the quantities that are even under the parity of the modes are allowed, the obstruction disappears for two modes: definite answers can then be assigned. This is a known theorem of quantum theory placed in the series' algebra; it does not show that the series' rule for averages is forced.

## one-liner
In $\Cl_{\Q}(2,2)$, eighteen atoms with rational coefficients (rank-one projectors, not only those of rational unit vectors) built from the ladder pairs form nine contexts with each atom in two, so no function to $\{0,1\}$ sums to $1$ on every context, and nine blades in a square have row products $1, 1, -1$ and column products $1, 1, 1$; the even subalgebra of two modes admits a two-valued additive weight on its self-adjoint idempotents.
