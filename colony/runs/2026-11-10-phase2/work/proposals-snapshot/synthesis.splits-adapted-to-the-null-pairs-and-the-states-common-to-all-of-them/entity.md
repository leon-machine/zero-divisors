---
id: synthesis.splits-adapted-to-the-null-pairs-and-the-states-common-to-all-of-them
kind: claim
version: 1
title: 'Splits adapted to the null pairs, and the states of (P) common to all of them'
status: proved
region: synthesis
subject: clifford-structure
tags: [measurement-and-records, finite-models, grading-and-parity]
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
about:
- obj.std-algebra.clifford-algebra
derivations:
- name: main
  uses:
  - tower.ladder-pairs-satisfy-car-vectors@4
  - synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate@1
  - synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product@1
  assumes:
  - synthesis.premise-positivity-of-values@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_adapted_frames_and_the_stored_boosted_frame
- kind: check
  ref: check.py::check_number_parity_and_sector_projectors_are_self_adjoint_for_every_adapted_split
- kind: check
  ref: check.py::check_functionals_real_for_all_adapted_splits_are_functions_of_the_number
- kind: check
  ref: check.py::check_pair_state_depends_on_the_split_and_common_states_stay_at_two
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - dark-matter.premise-flag-as-datum
  - synthesis.positive-structure-is-twistor-form-at-imaginary-time
extraction:
  open_problem: op.positivity-of-values
  note: >-
    The second attack item of op.positivity-of-values: whether the datum that defines the modes fixes the
    split behind the adjoint of (P), and what (P) becomes under a change of split. Answer for the mode
    algebras: the null pairs (two complementary isotropic subspaces) fix the split only up to a positive
    definite form on one of them; the boosted frame of clause (vi) of the stored CHSH bound is the case of
    one mode. The states that do not depend on this missing datum are the mixtures over the sectors of the
    number element, a family of $\ell$ parameters; every other state, the stored entangled pair states
    included, needs the split. Classical background, from memory: the adapted splits are the positive
    complex structures of the theory of quasi-free states and Bogoliubov transformations restricted to
    those preserving the polarisation; that the invariants of the general linear group on the exterior
    algebra are functions of the degree is standard; neither is used in the proof, which is by scalings
    and one finite computation. What is not shown. The flag of dark-matter.premise-flag-as-datum lives
    in the complexification of the algebra of signature (2,4) and its premise concerns one sign; that it
    cannot supply a continuous datum is an observation, and the relation of the splits of that algebra to
    the stored positive structures at points of the forward tube
    (synthesis.positive-structure-is-twistor-form-at-imaginary-time, whose positive Hermitian structures
    with every generator unitary are the adjoints of splits) is argued, not proved here: it suggests that
    the datum supplying the split in the series is the observer's tube point, not the flag. Kill condition
    registered before computing: the stabiliser of the null pairs fixes the split (it does not). The
    family of common states was not predicted before computing. Transport-convenient: the statement is
    about the series' modes; the mathematics is classical.
---

## formal
Let $k$ be $\Q$ or an ordered field and $\Cl_{k}(\ell,\ell)$ the algebra of $\ell$ modes of Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}: generators $e_{j}$, $f_{j}$ with $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, null pairs $v_{j} = \tfrac12(e_{j} + f_{j})$, $w_{j} = \tfrac12(e_{j} - f_{j})$, with $v_{i}w_{j} + w_{j}v_{i} = \delta_{ij}$; let $V$ be the span of the generators, $W$ the span of the $v_{j}$ and $W'$ the span of the $w_{j}$ (isotropic, $V = W \oplus W'$). A \emph{split} is a decomposition $V = V_{+} \oplus V_{-}$ into orthogonal subspaces on which $Q$ is positive and negative definite; its \emph{adjoint} is the anti-automorphism $\dagger_{s}$ of the algebra that is $+1$ on $V_{+}$ and $-1$ on $V_{-}$. The stored split, $V_{+}$ spanned by the $e_{j}$ and $V_{-}$ by the $f_{j}$, has the blade inverse $\dagger$ as adjoint. A split is \emph{adapted} (to the null pairs) if its adjoint maps $W$ onto $W'$. Premise (P), positivity of values (Premise \claimref{synthesis.premise-positivity-of-values}; assumed, not derived), is stated relative to a split: a state for the split $s$ is a $k$-linear $\omega$ with $\omega(1) = 1$, $\omega(xx^{\dagger_{s}}) \ge 0$ and $\omega(x^{\dagger_{s}}) = \omega(x)$.
\begin{enumerate}
\item[(i)] \emph{(The null pairs fix the split up to a positive form; proved.)} The adapted splits correspond one to one to the positive definite symmetric bilinear forms $g$ on $W$, by $g(v,v') = vv'^{\dagger_{s}} + v'^{\dagger_{s}}v$; the stored split has $g(v_{i},v_{j}) = \delta_{ij}$. For $A \in \mathrm{GL}_{\ell}(k)$ the vectors $v'_{j} = \sum_{i}A_{ij}v_{i}$, $w'_{j} = \sum_{i}(A^{-1})_{ji}w_{i}$ are null pairs spanning the same $W$, $W'$, and $e'_{j} = v'_{j} + w'_{j}$, $f'_{j} = v'_{j} - w'_{j}$ is an orthonormal frame of an adapted split. For $\ell = 1$ the adapted splits are the frames $e' = tv_{1} + t^{-1}w_{1}$, $f' = tv_{1} - t^{-1}w_{1}$, $t \ne 0$, with the same two null lines and the same parity $f'e' = f_{1}e_{1}$; $t = 4$ is the boosted frame $\tfrac{17}{8}e_{1} + \tfrac{15}{8}f_{1}$, $\tfrac{15}{8}e_{1} + \tfrac{17}{8}f_{1}$ of clause (vi) of Theorem \claimref{synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate}. So the null pairs that define the modes do not determine the adjoint of (P); what is missing is a positive definite form on $W$, $\ell(\ell+1)/2$ numbers.
\item[(ii)] \emph{(What the null pairs do fix; proved.)} The number element $N = \sum_{j}w_{j}v_{j}$ is the same for every pair of dual bases of $W$ and $W'$, and $N^{\dagger_{s}} = N$ for every adapted split. Hence the sector projectors $Q_{n} = \prod_{m \ne n}(N - m)/(n - m)$, $0 \le n \le \ell$ (idempotent, with sum $1$ and $\langle Q_{n}\rangle_{0} = \binom{\ell}{n}2^{-\ell}$), the vacuum projector $Q_{0}$ and the total parity are self-adjoint for every adapted split.
\item[(iii)] \emph{(The functionals real for every adapted split; proved, with the case $\ell = 2$ by a complete finite computation.)} A $k$-linear functional $\omega$ satisfies $\omega(x^{\dagger_{s}}) = \omega(x)$ for all $x$ and all adapted splits $s$ if and only if $\omega(x) = \langle h(N)x\rangle_{0}$ for a polynomial $h$ of degree at most $\ell$: a space of dimension $\ell + 1$. Such a functional is a state for one adapted split if and only if it is a state for all of them, if and only if $\omega = \sum_{n}q_{n}\,\langle Q_{n}x\rangle_{0}/\langle Q_{n}\rangle_{0}$ with $q_{n} \ge 0$ and $\sum_{n}q_{n} = 1$. These are the states of (P) that do not depend on the choice of adapted split; they include the vacuum state, the state of $Q_{\ell}$ and the products $\prod_{j}\tfrac12(1 + rp_{j})$ with one common $r$, $|r| \le 1$, $p_{j} = f_{j}e_{j}$. If only the splits adapted to each mode separately are admitted ($g$ diagonal in the $v_{j}$), the functionals real for all of them are the $\langle h(w_{1}v_{1}, \dots, w_{\ell}v_{\ell})x\rangle_{0}$, a space of dimension $2^{\ell}$, which contains every product $\prod_{j}\tfrac12(1 + r_{j}p_{j})$.
\item[(iv)] \emph{(States that need the split; proved.)} Every other state of the stored split fails to be a state for some adapted split. In particular the pair state $\rho_{12}$ of clause (v) of Theorem \claimref{synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product} with $cs \ne 0$ is not real for the split with $v'_{1} = 2v_{1}$ (at $c = \tfrac35$, $s = \tfrac45$ its values on $w_{1}w_{2}$ and on the adjoint of $w_{1}w_{2}$ for that split are $\tfrac{12}{25}$ and $\tfrac{48}{25}$). For $\ell = 2$ and the directions $a_{i} = x_{i}e_{1} + z_{i}p_{1}$, $b_{j} = x'_{j}e_{2}p_{1} + z'_{j}p_{2}$ of clause (vii) of the CHSH theorem, a state of the family (iii) gives the CHSH element the value $Z\,\omega(p_{1}p_{2})$, $Z = z_{1}(z'_{1} + z'_{2}) + z_{2}(z'_{1} - z'_{2})$, of absolute value at most $2$: in that setting a value above $2$ requires a state that depends on the split.
\end{enumerate}
\emph{Scope.} A state for one split assigns numbers in $[0,1]$ to the projectors of that split only; for an idempotent that is self-adjoint for another adapted split its value can lie outside $[0,1]$, as in the stored example with the value $\tfrac{17}{4}$. The statements are about the algebras $\Cl_{k}(\ell,\ell)$ and the splits adapted to their null pairs. Splits that are not adapted exist for $\ell \ge 2$ and are not treated. Nothing here says which split, if any, the series' other premises select.

## technical
Premise (P), positivity of values, is stated relative to a split of the generators into those of square $+1$ and those of square $-1$, because the adjoint is defined by the split; (P) is assumed, not derived. For the mode algebras $\Cl_{k}(\ell,\ell)$ this result says how much of the split the modes themselves fix. The modes are given by null pairs $v_{j}$, $w_{j}$, that is, by two complementary isotropic subspaces $W$ and $W'$. The splits whose adjoint exchanges $W$ and $W'$ correspond exactly to the positive definite forms on $W$: for one mode a single positive number, the scale $t$ in $e' = tv + w/t$, and the stored boosted frame with the value $17/4$ of the CHSH combination is $t = 4$. So the null pairs do not determine the adjoint. They do determine the number element $N$, its sector projectors, the vacuum projector and the total parity, which are self-adjoint for every adapted split.

Under (P) for a given split, the states that are states for every adapted split are exactly the mixtures of the normalised sector projectors of $N$: a family with $\ell$ free weights, containing the vacuum and the product states with one common occupation for all modes. If the scale of each mode is free but the modes are kept apart, the common states are the number-diagonal ones, which include all thermal products. Every state with coherence between sectors, such as the stored pair states, is tied to one split; and with one mode per party the split-independent states give the CHSH combination at most $2$. The correspondence, the invariance of $N$ and the classification are proved; the classification uses scalings of single modes and a complete finite computation for two modes.

## lay
The series' assumption (P) about averages uses a mirror operation on the algebra, and that operation depends on dividing the basic directions into two kinds. Given that assumption and the series' description of its modes by pairs of light-like directions, this result asks how much of the division those pairs fix. The answer is: not all of it. For one mode a single positive number, a scale, is left free; for several modes a whole table of such numbers. A known example in the series where the limit on correlations seems to be broken is just a change of this scale.

Assuming (P), the result then finds which states make sense whatever the scale is: only those that are a mixture of "this many modes are occupied" with nothing more specific, such as the empty state or a thermal state with the same occupation for every mode. States in which two modes are entangled depend on the scale, and under the same assumption the states that do not depend on it never exceed the classical limit 2 in the simplest two-party arrangement. So some further datum of the theory has to supply the scale; the result does not say which.

## one-liner
In $\Cl_{k}(\ell,\ell)$ the null pairs fix the split behind the adjoint of (P) only up to a positive definite form on their isotropic span (for one mode a scale $t$; $t = 4$ is the stored boosted frame); given (P), the states common to all adapted splits are exactly the mixtures of the sector projectors of the number element, and with one mode per party they give the CHSH element at most $2$.
