---
id: synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional
kind: claim
version: 1
title: 'Born weights under positivity (P): a state sharp on an atom is that atom''s functional'
status: proved
region: synthesis
subject: clifford-structure
tags: [measurement-and-records, finite-models, classical-theorem]
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
  - synthesis.signed-directions-and-the-integer-clifford-algebra@2
  - tower.ladder-pairs-satisfy-car-vectors@4
  - synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate@1
  assumes:
  - synthesis.premise-positivity-of-values@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_maximal_commuting_blade_sets_give_atoms_in_every_small_signature
- kind: check
  ref: check.py::check_orbit_atoms_hermitian_squares_and_overlap_weights
- kind: check
  ref: check.py::check_sharpness_on_an_atom_leaves_one_functional
- kind: check
  ref: check.py::check_reality_positivity_and_the_atom_condition_are_each_needed
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - one-relation.imported-envariance-born-rule
  - one-relation.measure-indifference-borns-rule-located
extraction:
  open_problem: op.positivity-of-values
  note: >-
    The fourth attack item of op.positivity-of-values: the Born weights from (P) and sharpness, for every
    idempotent on which sharpness can fix a state, generalising clause (viii) of the stored CHSH bound
    (one state, one idempotent). What is classical and what is placement. Classical: a state of an algebra
    with involution that takes the value 1 on a minimal projection is the vector state of that projection
    (the support-projection argument, a use of the Cauchy-Schwarz inequality; standard in the theory of
    operator algebras, cited from memory, no single source checked); the weights are then the trace formula,
    the Born rule in von Neumann's form; the idempotents built from commuting blades of square one are the
    primitive idempotents of Lounesto's Clifford Algebras and Spinors, chapter 17 (from memory), and the
    corner dimensions 1, 2, 4 found here are those of the classical table of real Clifford algebras, which
    is not used in any proof. Placement, which is all that is claimed: the statement over any ordered field
    and in particular over the rationals, with the blade inverse as adjoint and the scalar part as trace;
    the condition on the idempotent stated without the classification (the self-adjoint part of the corner
    is one-dimensional), which covers corners of complex and quaternion type; that every weight is a ratio
    of sums of squares of coefficients, so no square root and no completion is needed; and the equivalence
    of the positivity clause with non-negative weights on atoms. What it does to the stored Born account:
    it does not derive the Born rule from the stored measurement premises. It shows that under (P) the
    weights of a sharp state are fixed, with no use of the indifference premise, of an environment, of
    fine-graining or of continuity, so under (P) the imported envariance argument
    (one-relation.imported-envariance-born-rule) is not needed for the weights. The content of that
    argument's residual postulate (weights exist and add) has not gone away: it is inside (P), whose
    linearity across elements that do not commute is the non-contextuality assumption of theorems of
    Gleason's type (A. M. Gleason, J. Math. Mech. 6 (1957) 885, from memory). So this is a relocation of
    the assumption into (P), not a reduction of it. Whether the stored result
    one-relation.measure-indifference-borns-rule-located should cite this result in place of the import
    is a maintainer decision. Kill condition registered before computing: a functional satisfying (P),
    sharp on an idempotent whose corner has one-dimensional self-adjoint part, and different from the
    trace functional; or a signature with $p + q \le 6$ in which a maximal commuting set of blades of
    square one gives a corner with self-adjoint part of dimension above one (neither occurred). Classical
    mathematics; transport-absent.
---

## formal
Let $k$ be $\Q$ or any ordered field, and $\Cl_{k}(p,q)$ the Clifford algebra of Theorem \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra} with coefficients in $k$, with blades $e_{S}$, the blade inverse $x \mapsto x^{\dagger}$ and the scalar part $\langle\cdot\rangle_{0}$ as in Theorem \claimref{synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate}; by clause (iii) of that theorem $\langle x^{\dagger}x\rangle_{0}$ is the sum of the squares of the coefficients of $x$. Everything below is relative to the fixed split of the generators that defines $\dagger$. Premise (P), positivity of values (Premise \claimref{synthesis.premise-positivity-of-values}), is assumed, not derived: values are given by a \emph{state}, a $k$-linear $\omega$ with $\omega(1) = 1$ (normalisation), $\omega(xx^{\dagger}) \ge 0$ (positivity) and $\omega(x^{\dagger}) = \omega(x)$ (reality).

\emph{Definitions.} A \emph{projector} is an element $E$ with $E^{\dagger} = E = E^{2}$. The \emph{corner} of a projector $\Pi$ is $\Pi\Cl_{k}(p,q)\Pi$. An \emph{atom} is a nonzero projector $\Pi$ whose corner has no self-adjoint elements other than the multiples of $\Pi$. A functional $\omega$ is \emph{sharp} on a projector $\Pi$ if $\omega(\Pi) = 1$. For a nonzero projector $\Pi$ put $\omega_{\Pi}(x) = \langle\Pi x\rangle_{0}/\langle\Pi\rangle_{0}$; it is a state sharp on $\Pi$ (clause (iii) of the theorem above, with $\rho = \Pi = \Pi\Pi^{\dagger}$).
\begin{enumerate}
\item[(i)] \emph{(Atoms exist in every signature; proved, with a table computed for $p + q \le 5$ and for $(2,4)$, $(3,3)$.)} Let $b_{1}, \dots, b_{m}$ be commuting blades of square $1$, independent (no product of a nonempty subset is $\pm 1$) and maximal (every blade of square $1$ that commutes with all of them is, up to sign, a product of some of them); such a set exists in every signature, and $m = 0$ is allowed. For signs $\chi \in \{\pm 1\}^{m}$ put $\Pi_{\chi} = \prod_{i}\tfrac12(1 + \chi_{i}b_{i})$. Then every $\Pi_{\chi}$ is an atom with $\langle\Pi_{\chi}\rangle_{0} = 2^{-m}$, the $2^{m}$ atoms $\Pi_{\chi}$ are pairwise orthogonal and sum to $1$, and the corner of $\Pi_{\chi}$ is spanned by $\Pi_{\chi}$ and by elements $b\Pi_{\chi}$, $b$ a blade of square $-1$ commuting with every $b_{i}$, each of which is anti-self-adjoint with square $-\Pi_{\chi}$. In $\Cl_{k}(\ell,\ell)$ with the modes of Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors} ($Q(e_{j}) = 1$, $Q(f_{j}) = -1$, $v_{j} = \tfrac12(e_{j} + f_{j})$, $p_{j} = f_{j}e_{j}$) the parities $p_{1}, \dots, p_{\ell}$ are such a set, the atom $\Pi_{0} = \prod_{j}\tfrac12(1 + p_{j})$ satisfies $v_{j}\Pi_{0} = 0$ for all $j$ (the vacuum projector), and its corner is $k\Pi_{0}$. Computed: in every signature with $p + q \le 5$ and in $(2,4)$ and $(3,3)$ the corner of $\Pi_{\chi}$ has dimension $1$, $2$ or $4$ (for example $1$ in $(1,1)$, $(2,0)$, $(2,2)$, $(3,3)$; $2$ in $(3,0)$; $4$ in $(0,2)$, $(1,3)$, $(2,4)$), with $m = 1, 1, 2, 3, 1, 0, 1, 2$ in these eight.
\item[(ii)] \emph{(The orbit of an atom, and hermitian squares; proved.)} Let $\Pi$ be an atom and $y$ an element with $y\Pi \ne 0$. Then $\Pi y^{\dagger}y\Pi = n_{y}\Pi$ with $n_{y} = \langle\Pi y^{\dagger}y\rangle_{0}/\langle\Pi\rangle_{0} > 0$, and $\Pi_{y} = y\Pi y^{\dagger}/n_{y}$ is an atom with $\langle\Pi_{y}\rangle_{0} = \langle\Pi\rangle_{0}$. With the atoms $\Pi_{\chi}$ of (i), every $y$ satisfies $yy^{\dagger} = \sum_{\chi}n_{y,\chi}(\Pi_{\chi})_{y}$, the sum over the $\chi$ with $y\Pi_{\chi} \ne 0$ and $n_{y,\chi} > 0$ the number $n_{y}$ for $\Pi_{\chi}$: every element $yy^{\dagger}$ is a combination of atoms with positive coefficients. Consequently a $k$-linear functional that is non-negative on every atom is non-negative on every $yy^{\dagger}$: given linearity, the positivity clause of (P) is equivalent to non-negative values on all atoms.
\item[(iii)] \emph{(The weights, under (P); proved.)} Let $\omega$ be a state and $\Pi$ an atom. If $\omega$ is sharp on $\Pi$ then $\omega = \omega_{\Pi}$:
\[
\omega(x) = \frac{\langle\Pi x\rangle_{0}}{\langle\Pi\rangle_{0}} \quad\text{for all } x, \qquad\text{and for every projector } E:\quad \omega(E) = \frac{\langle\Pi E\rangle_{0}}{\langle\Pi\rangle_{0}} = \frac{\langle(E\Pi)^{\dagger}(E\Pi)\rangle_{0}}{\langle\Pi^{\dagger}\Pi\rangle_{0}} \in [0,1] .
\]
The weight of the outcome $E$ in the state sharp on $\Pi$ is the sum of the squares of the coefficients of $E\Pi$ divided by that of $\Pi$; for projectors $E_{1}, \dots, E_{r}$ with $E_{i}E_{j} = 0$ ($i \ne j$) and sum $1$ the weights sum to $1$. For two atoms $\Pi_{x}$, $\Pi_{y}$ of the orbit of $\Pi$, with overlap $z = \Pi x^{\dagger}y\Pi$,
\[
\omega_{\Pi_{x}}(\Pi_{y}) = \omega_{\Pi_{y}}(\Pi_{x}) = \frac{\langle zz^{\dagger}\rangle_{0}}{n_{x}\,n_{y}\,\langle\Pi\rangle_{0}} ,
\]
and when the corner of $\Pi$ is $k\Pi$, $z = c\Pi$ and the weight is $c^{2}/(n_{x}n_{y})$: the square of the overlap over the product of the squared norms. All weights lie in $k$: no square root is taken, because the atom $\Pi_{y}$ depends only on the ray of $y\Pi$ and $y$ is not normalised.
\item[(iv)] \emph{(Each hypothesis is needed; proved by examples, and the atom condition is necessary and sufficient.)} (a) Without the reality clause the conclusion of (iii) holds on self-adjoint elements only: on one mode, $\Cl_{k}(1,1)$ with $\Pi = \tfrac12(1 + p_{1})$, the functional $\mu(x) = \omega_{\Pi}(x) + \langle f_{1}x\rangle_{0}$ is linear, normalised, non-negative on every $xx^{\dagger}$ and sharp on $\Pi$, with $\mu(f_{1}) = -1 \ne 0 = \omega_{\Pi}(f_{1})$. (b) Without the positivity clause: $\nu(x) = \langle(1 + p_{1} + \tfrac13 e_{1})x\rangle_{0}$ is linear, normalised, real and sharp on $\Pi$, with $\nu(e_{1}) = \tfrac13 \ne 0 = \omega_{\Pi}(e_{1})$; it has the value $-\tfrac43$ on $yy^{\dagger}$ for $y = -3 + 3e_{1} - 2f_{1} + 2p_{1}$. (c) If a nonzero projector $\Pi'$ is not an atom, the states sharp on $\Pi'$ are not unique: for a self-adjoint $s$ in its corner with $\langle s\rangle_{0} = 0$, $s \ne 0$, there is $\varepsilon > 0$ in $k$ such that $x \mapsto \langle(\Pi' + ts)x\rangle_{0}/\langle\Pi'\rangle_{0}$ is a state sharp on $\Pi'$ for every $t \in k$ with $|t| \le \varepsilon$; in $\Cl_{k}(2,2)$, $\Pi' = \tfrac12(1 + p_{1})$ and $s = \Pi'p_{2}$ give the states with $\omega(p_{2}) = t$, $|t| \le 1$. So sharpness on a projector fixes the state exactly when the projector is an atom.
\end{enumerate}
\emph{Scope.} The theorem is conditional on (P). It says what a state sharp on an atom is; it does not say that physical states are sharp on atoms, which elements are outcomes of measurements, or why values should be linear on elements that do not commute. The last is assumed in (P), and it is the assumption that theorems of Gleason's type derive from weaker ones for projectors; so the result does not derive the Born rule from the stored measurement premises. Under (P) it makes the stored imported envariance argument (Fact \claimref{one-relation.imported-envariance-born-rule}) unnecessary for the weights of a sharp state: no indifference premise, environment, fine-graining or continuity step is used. The saturating state of clause (viii) of the theorem above is the case of one atom over $k \ni \sqrt{2}$.

## technical
Under Premise (P), positivity of values (values are given by a linear functional $\omega$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(x^{\dagger}) = \omega(x)$, the adjoint being the blade inverse for a fixed split of the generators; assumed, not derived), the weights of a sharp state are the Born weights, in every Clifford algebra $\Cl_{k}(p,q)$ over an ordered field $k$, the rationals included. The statement needs the right notion of a sharp state. A projector is a self-adjoint idempotent; an atom is a projector $\Pi$ whose corner $\Pi\Cl_{k}(p,q)\Pi$ has only the multiples of $\Pi$ as self-adjoint elements. Atoms exist in every signature: the product of the idempotents $\tfrac12(1 + b_{i})$ over a maximal set of commuting blades of square one is an atom, and for the mode algebra $\Cl_{k}(\ell,\ell)$ the blades can be taken to be the mode parities, which gives the vacuum projector. The corner of an atom can be larger than the multiples of the atom (it has dimension $2$ in $\Cl(3,0)$ and $4$ in $\Cl(1,3)$ and $\Cl(2,4)$), but the extra elements are anti-self-adjoint.

The theorem, under (P): a state with value $1$ on an atom $\Pi$ is $x \mapsto \langle\Pi x\rangle_{0}/\langle\Pi\rangle_{0}$, and nothing else. The weight it gives an outcome projector $E$ is the sum of the squares of the coefficients of $E\Pi$ divided by that of $\Pi$, a squared norm; between two atoms of one orbit it is the squared overlap divided by the two squared norms. All weights are in the field: no square root and no completion is needed. Each clause of (P) is needed (without reality the functional is fixed on self-adjoint elements only; without positivity a real normalised functional sharp on the atom gives other values), and a projector that is not an atom carries several sharp states. Given linearity, positivity itself is the same as non-negative values on all atoms, because every $yy^{\dagger}$ is a positive combination of atoms.

What this does and does not do, given (P): the weights follow with no indifference premise, no environment, no fine-graining and no continuity, so under (P) the imported envariance argument is not needed for them. But the assumption that argument isolates, that weights exist and add, is not removed; it sits inside (P), whose linearity on elements that do not commute is the non-contextuality assumption of Gleason-type theorems. The mathematics is classical (the support-projection argument and the trace form of the Born rule); the placement over the rationals with the blade inverse, and the atom condition stated without the classification of the algebras, are what is recorded.

## lay
Quantum theory says the chance of an outcome is a squared size, the Born rule. The series has an assumption, called (P), about averages: the rule giving averages adds up over sums, gives the trivial quantity the average 1, never gives a quantity times its mirror image a negative average, and gives a quantity and its mirror image the same average. This result shows that, assuming (P), the Born rule follows for every state that is as definite as a state can be. Such a state gives the answer yes with certainty to one of the finest yes-or-no questions the algebra contains (here called an atom), and under (P) there is exactly one such state for each atom; the chance it gives any other yes-or-no question is a ratio of two sums of squares, the squared size of the overlap. With whole-number or fractional ingredients the chances are fractions: no square roots and no limits are needed.

This is not a derivation of the Born rule from nothing. The assumption (P) already contains the idea that averages add up even for quantities that cannot be measured together, and that idea is what the well-known theorems in this area work hardest to justify. What the result does is show that, once (P) is assumed, the separate argument the series had borrowed for the Born rule is no longer needed for these chances. The mathematics is long known; what is new here is only its statement inside the series' algebra with fractions.

## one-liner
Under (P), in $\Cl_{k}(p,q)$ over any ordered field: a state sharp on an atom $\Pi$ (a self-adjoint idempotent whose corner has only the multiples of $\Pi$ self-adjoint; atoms exist in every signature) is $x \mapsto \langle\Pi x\rangle_{0}/\langle\Pi\rangle_{0}$, so the weight of a projector $E$ is the squared norm $\langle(E\Pi)^{\dagger}E\Pi\rangle_{0}/\langle\Pi\rangle_{0}$, in $k$ with no square root; each clause of (P) and the atom condition are needed.
