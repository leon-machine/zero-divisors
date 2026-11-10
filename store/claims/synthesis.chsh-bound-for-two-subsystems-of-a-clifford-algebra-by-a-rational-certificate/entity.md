---
id: synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate
kind: claim
version: 1
title: 'CHSH bound under positivity (P): certificate, blade lemma and $\Cl(2,2)$ realisation'
status: proved
region: synthesis
subject: clifford-structure
tags: [entanglement, measurement-and-records, classical-theorem, superselection]
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
  - synthesis.division-gives-the-rationals@2
  - tower.commuting-copies@5
  - singularity.descent-parity-average@5
  assumes:
  - synthesis.premise-positivity-of-values@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_square_of_the_chsh_element_and_the_rational_certificate
- kind: check
  ref: check.py::check_scalar_part_is_positive_and_every_sample_state_obeys_the_bound
- kind: check
  ref: check.py::check_blade_configurations_give_square_four_plus_four_k_and_states_of_value_eight_r
- kind: check
  ref: check.py::check_functional_violating_positivity_reaches_four
- kind: check
  ref: check.py::check_square_one_element_that_is_not_self_adjoint_exceeds_four
- kind: check
  ref: check.py::check_klein_twisted_directions_commute_and_the_square_is_four_plus_four_wedges_k
- kind: check
  ref: check.py::check_saturating_state_is_a_pure_state_over_the_field_with_root_two
- kind: check
  ref: check.py::check_square_eight_on_a_state_with_nonzero_anticommutator
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.premise-minimal-non-commutativity
  - synthesis.premise-superposition-over-the-integers
  - synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: >-
      Hypothesis (P) is now the stored premise synthesis.premise-positivity-of-values (Leon's decision of 10 November 2026): an assumes edge to it is added, the formal level and the proof cite it with the label (P) kept, and the note names the related stored results by id. No statement changed; version kept at 1.
  note: >-
    The graph had no Bell, CHSH or Tsirelson result. This one states the CHSH bound inside the algebra that the
    foundation postulates produce and says what it uses; it is the base statement that the other stored entanglement results cite. Kill conditions registered before computing: the identity for the square or the
    certificate failing on an exact instance; a state and self-adjoint commuting settings with squared value above
    8; the bound needing a positivity premise beyond the foundation and definitions (the first two did not fire;
    the third did, in this sense: the bound needs Hypothesis (P)). Hypothesis (P) is the stored premise synthesis.premise-positivity-of-values (adopted 10 November 2026, with reality, relative to the split of the generators that defines the modes); this result assumes it, and the label (P) is kept in the text. What is used besides (P): the integer
    algebra of the signed directions and its blades (the stored result on the group of signed directions, resting
    on the postulates of the bit, minimal non-commutativity and superposition); rational coefficients, for the
    factor one half and for directions that are not blades (the stored division result); the twist of the stored
    commuting-copies theorem, for the realisation of clauses (vii) to (ix) only, with the lines needed proved in
    place; the stored parity average, only to name the average in clause (vii). The adjoint is the inverse on the
    group of signed directions extended linearly and the scalar part is the coefficient of the identity, so the
    positivity of the scalar part of $x^{\dagger}x$ is a theorem, and the order used on the rationals is the one
    in which sums of squares are non-negative. No step of the proof uses real coefficients; the saturating state
    of clause (viii) needs a square root of two and nothing else. Two settings are recorded side by side and
    neither is called the physical one: the one-mode Klein-twisted realisation of clauses (vii), (viii), whose
    directions are odd under the total parity, and parity-even observables with two modes for each party
    (synthesis.chsh-with-parity-even-observables-needs-two-modes-per-party-and-no-klein-twist, not used here), to which clauses (i) to (iv) apply unchanged. Related stored results, not used here: with rational or real coefficients a configuration of two commuting
    pairs inside one copy of the algebra with squared value above 4 exists in every signature except fourteen,
    among them the algebra of space and the signature $(1,3)$ (synthesis.signatures-in-which-commuting-observables-exceed-the-chsh-value-two; this concerns two commuting pairs inside one copy
    and says nothing against Bell violation for two systems each described by its own copy); the functional of clause (v) as the Popescu-Rohrlich box with its probabilities (synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state); the attainment question over the rationals (synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records); the three-party trade-off (synthesis.three-party-trade-off-of-chsh-values-and-the-local-value-two). Clause (iv) and clause (ix) were first drafted in those results and are stated here once. Status of the content: classical mathematics. The identity for the square is Landau's
    (L. J. Landau, Phys. Lett. A 120 (1987) 54, cited from memory) and the bound is Tsirelson's (B. S. Cirel'son,
    Lett. Math. Phys. 4 (1980) 93, existence checked on the web). Checked on the web: the algebraic form of the
    bound for ordered star-rings is formalised in the Lean library mathlib (Algebra.Star.CHSH), by a
    sum-of-squares decomposition that uses the square root of two and its inverse; the certificate of clause (ii)
    bounds $C^{2}$ in place of $C$ and has rational coefficients, was not found in the sources read, is an
    elementary rearrangement and is not claimed as new. That value 8 of the square forces the anticommutators to
    vanish only on the state is the rigidity of Summers and Werner (1987, from memory). C. Held, arXiv:2007.05301,
    derives the value $2\sqrt{2}$ in the geometric algebra of space for vector-valued hidden variables, a
    different statement. Geometric-algebra treatments of two-particle states use the multiparticle spacetime
    algebra, one copy of the spacetime algebra for each particle with commuting even parts (Doran, Lasenby and
    co-workers; Havel and Doran, arXiv:quant-ph/0106063; from memory); here the two parties are two modes of one
    Clifford algebra and commute through the stored twist. What is added to the classical theorem: its statement
    and proof over the rationals inside the foundation's algebra with the premises listed, the role of the twist,
    the forced anticommutation for directions against its failure for general observables, the dependence on the
    chosen split of the generators with an exact example, and the saturating state as an element of the algebra
    with its uniqueness. Transport-absent: nothing here uses transport.
---

## formal
Let $k$ be $\Q$ or any ordered field, and $\Cl_{k}(p,q)$ the Clifford algebra of Theorem \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra} with coefficients in $k$ (Theorem \claimref{synthesis.division-gives-the-rationals}), with blades $e_{S}$, the images of the group $G$ of signed directions. Let $x \mapsto x^{\dagger}$ be the linear extension of the inverse of $G$, $e_{S}^{\dagger} = e_{S}^{-1}$. The adjoint is defined by the chosen generators. In definite signature it does not depend on the orthonormal frame; in indefinite signature it depends on the split into generators of square $1$ and of square $-1$, so observables, states and (P) are relative to that split, and each statement holds for every fixed split. An \emph{observable} is an $x$ with $x^{\dagger} = x$ and $x^{2} = 1$.

\emph{Hypothesis (P), positivity of values:} values are given by a \emph{state}, a $k$-linear $\omega : \Cl_{k}(p,q) \to k$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(x^{\dagger}) = \omega(x)$ for all $x$; (P) is Premise \claimref{synthesis.premise-positivity-of-values}, assumed, not derived.

The functionals $\omega_{\rho}(x) = \langle\rho x\rangle_{0}/\langle\rho\rangle_{0}$, $\rho = \sum_{r}y_{r}y_{r}^{\dagger} \ne 0$, are states; (P) extends the stored definition of a state as an element $\rho = \sum_{r}x_{r}x_{r}^{\dagger}$ of unit trace from elements to functionals. Let $A_{1}, A_{2}, B_{1}, B_{2}$ be observables with $A_{i}B_{j} = B_{j}A_{i}$ for all $i, j$ (a \emph{configuration}; any signature, and no subsystem structure is assumed in (i) to (v)), and
\[
C = A_{1}(B_{1} + B_{2}) + A_{2}(B_{1} - B_{2}), \qquad X = [A_{1},A_{2}], \quad Y = [B_{1},B_{2}], \quad S_{A} = A_{1}A_{2} + A_{2}A_{1}, \quad S_{B} = B_{1}B_{2} + B_{2}B_{1} .
\]
\begin{enumerate}
\item[(i)] \emph{(The identity; proved, classical.)} $C^{\dagger} = C$ and $C^{2} = 4 - XY$.
\item[(ii)] \emph{(The certificate; proved.)} With $Z = X - Y$,
\[
8 - C^{2} = \tfrac12\bigl(Z^{\dagger}Z + S_{A}^{2} + S_{B}^{2}\bigr), \qquad X^{\dagger}X = 4 - S_{A}^{2}, \quad Y^{\dagger}Y = 4 - S_{B}^{2},
\]
identities with rational coefficients in which $S_{A}$, $S_{B}$ are self-adjoint.
\item[(iii)] \emph{(The bound, under (P); proved; the check samples the two inequalities and not the strictness.)} $\langle x^{\dagger}x\rangle_{0}$ is the sum of the squares of the coefficients of $x$, so $\omega_{\rho}$ is a state. For every state
\[
\omega(C)^{2} \le \omega(C^{2}) = 8 - \tfrac12\omega(Z^{\dagger}Z) - \tfrac12\omega(S_{A}^{2}) - \tfrac12\omega(S_{B}^{2}) \le 8, \qquad \bigl(\omega(C^{2}) - 4\bigr)^{2} \le \omega(4 - S_{A}^{2})\,\omega(4 - S_{B}^{2}) .
\]
If $2$ is not a square in $k$ (as for $k = \Q$) then $\omega(C)^{2} < 8$. If $\omega(C)^{2} = 8$ then $\omega(S_{A}^{2}) = \omega(S_{B}^{2}) = \omega(Z^{\dagger}Z) = 0$. If $A_{1}A_{2} = A_{2}A_{1}$ or $B_{1}B_{2} = B_{2}B_{1}$ then $C^{2} = 4$ and $\omega(C)^{2} \le 4$. The bound $8$ is an upper bound in every signature; whether it is approached depends on whether configurations with $XY \ne 0$ exist, which depends on the signature. This clause uses of (P) only $\omega(xx^{\dagger}) \ge 0$ and $\omega(1) = 1$.
\item[(iv)] \emph{(Blade lemma; proved.)} Let the four observables be blades up to sign with $A_{1}A_{2} = -A_{2}A_{1}$ and $B_{1}B_{2} = -B_{2}B_{1}$ (any signature in which such a configuration exists). Then with $K = -A_{1}A_{2}B_{1}B_{2}$,
\[
C^{2} = 4 + 4K, \qquad K^{\dagger} = K, \quad K^{2} = 1, \quad KC = CK = C, \qquad C^{3} = 8C, \qquad \langle C\rangle_{0} = \langle K\rangle_{0} = 0 ,
\]
and $K$ is a blade up to sign and not a scalar. For $r \in k$ the functional $\omega_{r}(x) = \langle(1 + K)(1 + rC)x\rangle_{0}$ satisfies (P) exactly when $8r^{2} \le 1$, and then $\omega_{r}(C) = 8r$, $\omega_{r}(C^{2}) = 8$. So over $\Q$ every rational $v$ with $v^{2} < 8$ is a value $\omega_{r}(C)$, the supremum of the values is $2\sqrt{2}$ and is not attained, and over an ordered field containing $\sqrt{2}$ the value $2\sqrt{2}$ is attained at $r = \sqrt{2}/4$.
\item[(v)] \emph{(Without positivity the value $4$ occurs; proved.)} In the situation of (iv), $\lambda(x) = \langle(1 + C)x\rangle_{0}$ is linear with $\lambda(1) = 1$ and $\lambda(x^{\dagger}) = \lambda(x)$, and $\lambda(C) = 4$; $\lambda((C - t)(C - t)^{\dagger}) = t^{2} - 8t + 4$, which is negative at $t = 1$. So $\lambda$ satisfies every part of (P) except $\lambda(xx^{\dagger}) \ge 0$, and the bound of (iii) fails for it.
\item[(vi)] \emph{(Self-adjointness for one fixed frame is needed; proved by an example.)} In $\Cl_{\Q}(2,2)$ with the notation of (vii), $A = \tfrac{17}{8}e_{1} + \tfrac{15}{8}f_{1}$ has $A^{2} = 1$ and $A^{\dagger} \ne A$, it commutes with the observable $p_{2}$, and for $A_{1} = A_{2} = A$, $B_{1} = B_{2} = p_{2}$ the state $\omega_{\rho}$, $\rho = \tfrac14(1 + e_{1})(1 + p_{2})$, has $\omega_{\rho}(C) = \tfrac{17}{4} > 4$, while $C^{2} = 4$. So square one and commutation alone give no bound on values, not even the bound $4$. $A$ is a unit vector of square $1$, the first generator of the boosted frame $A$, $\tfrac{15}{8}e_{1} + \tfrac{17}{8}f_{1}$ (anticommuting, of squares $1$ and $-1$); it is an observable for the adjoint of that frame, for which $\omega_{\rho}$ is not a state (its value on $(1 - A)^{2}$, which is $(1 - A)(1 - A)^{\dagger'}$ for that adjoint, is $-\tfrac94$). So the clause shows that the bound is relative to one split into positive and negative generators, not that such elements are unphysical.
\item[(vii)] \emph{(Realisation: one mode against the Klein-twisted other mode of $\Cl(2,2)$, with parity-odd directions, under (P); proved.)} Let $\Cl_{k}(2,2)$ have generators $e_{1}, f_{1}, e_{2}, f_{2}$ with $Q(e_{j}) = 1$, $Q(f_{j}) = -1$ and mode parities $p_{j} = f_{j}e_{j}$. The adjoint fixes $e_{j}$ and negates $f_{j}$; the self-adjoint elements of the sub-Clifford algebra of mode $j$ are spanned by $1, e_{j}, p_{j}$, and its observables are $\pm 1$ and the \emph{directions} $xe_{j} + zp_{j}$, $x^{2} + z^{2} = 1$. The directions of mode $1$ and of mode $2$ do not commute ($e_{1}e_{2} = -e_{2}e_{1}$, and $e_{1}e_{2}$ is not self-adjoint), so the two sub-Clifford algebras are not two parties. The parties are mode $1$ and the copy of mode $2$ twisted by $p_{1}$ as in Theorem \claimref{tower.commuting-copies} (generators $e_{2}p_{1}$, $f_{2}p_{1}$, which keep their squares, anticommute, and commute with mode $1$): party $A$ has the directions $a = xe_{1} + zp_{1}$ and party $B$ the directions $b = x\,e_{2}p_{1} + z\,p_{2}$. These commute, and for directions $a_{1}, a_{2}$ of $A$ and $b_{1}, b_{2}$ of $B$, with $a_{1} \cdot a_{2} = x_{1}x_{2} + z_{1}z_{2}$ and $a_{1} \wedge a_{2} = x_{1}z_{2} - z_{1}x_{2}$ (so $(a_{1} \cdot a_{2})^{2} + (a_{1} \wedge a_{2})^{2} = 1$),
\[
S_{A} = 2\,a_{1} \cdot a_{2}, \qquad C^{2} = 4 + 4\,(a_{1} \wedge a_{2})(b_{1} \wedge b_{2})\,K, \qquad K = e_{1}f_{2}, \quad K^{\dagger} = K, \quad K^{2} = 1, \quad KC = CK .
\]
Hence $\omega(C)^{2} \le 4 + 4\,|a_{1} \wedge a_{2}|\,|b_{1} \wedge b_{2}|$ for every state, and the value $8$ of $\omega(C^{2})$ requires $a_{1} \cdot a_{2} = b_{1} \cdot b_{2} = 0$: each party's two directions anticommute. For directions this is forced as an identity of elements; for general observables it is not (clause (ix)). \emph{Parity.} The directions $e_{1}$ and $e_{2}p_{1}$ anticommute with the total parity $\Gamma = p_{1}p_{2}$, so the parity average $x \mapsto \tfrac12(x + \Gamma x\Gamma)$ (Theorem \claimref{singularity.descent-parity-average}, in its total-parity form) sends $xe_{1} + zp_{1}$ to $zp_{1}$ and $x\,e_{2}p_{1} + z\,p_{2}$ to $z\,p_{2}$: the averaged directions commute, and the CHSH combination of the averaged directions is $\bigl(z_{1}(z'_{1} + z'_{2}) + z_{2}(z'_{1} - z'_{2})\bigr)p_{1}p_{2}$ with coefficient of absolute value at most $2$ ($z_{i}$, $z'_{j}$ the $p$-components of $a_{i}$, $b_{j}$). This realisation is therefore the setting in which parity-odd elements are observables; in the other setting, parity-even observables only, it gives nothing above $2$, each party needs two modes, no twist is needed, and clauses (i) to (iv) apply unchanged. Neither setting is singled out here.
\item[(viii)] \emph{(The saturating state of the realisation (vii); proved.)} At $A_{1} = e_{1}$, $A_{2} = p_{1}$, $B_{1} = e_{2}p_{1}$, $B_{2} = p_{2}$, a configuration of blades as in (iv): $C = e_{2}f_{1} + e_{1}p_{2} + e_{2} - p_{1}p_{2}$ and $K = e_{1}f_{2}$. If $k$ contains $\sqrt{2}$,
\[
P = \tfrac14(1 + K) + \tfrac{\sqrt{2}}{8}\,C
\]
satisfies $P^{\dagger} = P = P^{2}$, $CP = 2\sqrt{2}\,P$, $\langle P\rangle_{0} = \tfrac14$ and $PxP = 4\langle Px\rangle_{0}P$ for every $x$; $\omega_{P}(x) = 4\langle Px\rangle_{0}$ is the functional $\omega_{r}$ of (iv) at $r = \sqrt{2}/4$, a state with $\omega_{P}(C) = 2\sqrt{2}$, and at these settings it is the only state with that value: any functional with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(C) = 2\sqrt{2}$ agrees with $\omega_{P}$ on all self-adjoint elements, and the reality clause of (P) then gives equality on all elements. Its projection onto the blades of mode $1$ is $\tfrac14$. At these blade directions $P$ does not commute with the total parity $p_{1}p_{2}$ (this depends on the directions: with party $B$'s pair turned by an eighth of a turn, which puts $\sqrt{2}$ in the directions, the saturating state can be even), and its projection onto the blades of mode $2$ is $\tfrac14 + \tfrac{\sqrt{2}}{8}e_{2}$. Only $\sqrt{2}$ is adjoined.
\item[(ix)] \emph{(For general observables anticommutation holds only on the state; proved.)} In $\Cl_{k}(3,3)$ with a third mode $e_{3}, f_{3}$, $p_{3} = f_{3}e_{3}$, let $P_{\pm} = \tfrac12(1 \pm p_{3})$ and
\[
A_{1} = p_{1}, \qquad A_{2} = e_{1}P_{+} + p_{1}P_{-}, \qquad B_{1} = p_{2}, \qquad B_{2} = e_{2}p_{1} .
\]
These are observables commuting across the pairs, $S_{A} = 1 - p_{3} \ne 0$, and $C^{2} = 4 + 4K'P_{+}$ with $K' = -p_{1}e_{1}\,p_{2}\,e_{2}p_{1}$, a self-adjoint blade of square $1$. For $8r^{2} \le 1$ the functional $\omega'_{r}(x) = \langle(1 + K')(1 + p_{3})(1 + rC)x\rangle_{0}$ satisfies (P), with $\omega'_{r}(C^{2}) = 8$, $\omega'_{r}(C) = 8r$ and $\omega'_{r}(S_{A}^{2}) = 0$. So the value $8$ of $\omega(C^{2})$ does not force $S_{A} = 0$ as an identity of elements, only $\omega(S_{A}^{2}) = 0$ as in (iii).
\end{enumerate}

## technical
The Clauser-Horne-Shimony-Holt combination of four two-valued quantities, two for each of two parties, is bounded by $2\sqrt{2}$ in quantum theory (Tsirelson's bound), by $2$ for quantities that commute, and by $4$ on general grounds. This result places the first of these inside the Clifford algebra that the foundation postulates of the series produce, with rational coefficients. The quantities are self-adjoint elements of square one, where the adjoint is the inverse on the group of signed directions extended linearly, and a party's quantities commute with the other party's. The square of the combination is $4$ minus the product of the two commutators (Landau's identity), and $8$ minus that square is one half of a sum of three squares with rational coefficients. Everything about values rests on Hypothesis (P), positivity of values: values are given by a state, a linear functional $\omega$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(x^{\dagger}) = \omega(x)$ for all $x$; (P) is assumed, not derived. Under (P) the combination has a squared value of at most $8$, and over the rationals strictly less. Positivity of the scalar part is a theorem of the blade basis, so states exist, and no step uses real coefficients; but (P) itself does not follow from the algebra: the functional $\langle(1 + C)\,\cdot\,\rangle_{0}$ is linear, normalised and real, has the value $4$ on the combination, and fails only the positivity clause. The adjoint, and with it observables, states and (P), is relative to the chosen split of the generators into those of square $1$ and those of square $-1$: a unit vector of a boosted frame has square one, is not self-adjoint for the original split, and gives the combination the value $17/4$ on a state of the original split. The bound holds in every signature; whether it is approached depends on the signature.

When the four quantities are blades that anticommute within each pair, the squared combination is $4 + 4K$ with $K$ a self-adjoint blade of square one, its cube is $8$ times itself, and the functionals $\langle(1 + K)(1 + rC)\,\cdot\,\rangle_{0}$ are states exactly for $8r^{2} \le 1$, with values $8r$: over the rationals every rational value of square below $8$ occurs and $2\sqrt{2}$ does not. Two settings are recorded side by side. In the first, parity-odd elements count as observables: for two modes of the split-signature algebra $\Cl(2,2)$ the parties are one mode and the Klein-twisted copy of the other, since the untwisted sub-Clifford algebras anticommute on odd elements; each party's quantities are the unit directions of a plane, the squared combination is $4 + 4(a_{1} \wedge a_{2})(b_{1} \wedge b_{2})K$, and the value $8$ needs both parties' directions to anticommute. At anticommuting blade directions the state reaching $2\sqrt{2}$ is a single element of the algebra with coefficients in the rationals extended by $\sqrt{2}$, a primitive idempotent, the only such state at these settings, and not invariant under the total parity. In the second setting only parity-even elements are observables; the parity average removes the odd directions of the one-mode realisation, which then gives at most $2$, and each party needs two modes, to which the identity, the certificate, the bound and the blade lemma apply unchanged. For observables that are not directions the anticommutation at the bound holds only on the state: a three-mode example has anticommutator $1 - p_{3}$ and states with squared-combination value $8$.

## lay
Two experimenters each choose between two yes-or-no measurements on their half of a shared system, and a particular combination of the four possible correlations is formed. If the world were made of pre-existing answers the combination could not exceed 2; quantum theory allows up to about 2.83 (2 times the square root of 2) and no more. That limit is a known theorem from 1980. What is done here is to place it inside the algebra of directions that the series builds from its simplest assumptions (a yes-no bit, the least possible dependence on order, and whole-number addition), using only fractions. The limit comes out as a single algebraic identity: 8 minus the square of the combination is a sum of squares. The limit rests on one assumption that is not part of the algebra and is assumed, not derived, called (P), positivity of values: averages of measurements are given by a rule that is linear, gives the trivial measurement the value 1, never gives a quantity times its mirror image (its adjoint) a negative average, and gives a quantity and its mirror image the same average. Without the positivity part the combination can reach 4, and an example is given. The example in which the quantum limit is reached uses the algebra of two paired directions of opposite kind for each experimenter, and measurements that change the count of particles between even and odd; if such measurements are not allowed, each experimenter needs a larger system, and both cases are recorded without choosing between them. The result also shows that for simple directions the limit is reached only when each experimenter's two measurements are as incompatible as possible; that which quantities count as measurements depends on a chosen division of the directions into two kinds, and a quantity that is a legitimate measurement for another division breaks the limit for this one; and it writes down the shared state that reaches the limit, the only one at these settings, which needs the square root of 2 and nothing more.

## one-liner
Under Hypothesis (P) (values are given by a state, a linear $\omega$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$, $\omega(x^{\dagger}) = \omega(x)$; assumed, not derived), commuting pairs of self-adjoint square-one elements of a rational Clifford algebra satisfy $C^{2} = 4 - XY$, $8 - C^{2} = \tfrac12(Z^{\dagger}Z + S_{A}^{2} + S_{B}^{2})$ and $\omega(C)^{2} \le 8$ (strictly over $\Q$); blades anticommuting within the pairs give $C^{2} = 4 + 4K$ and states of value $8r$, $8r^{2} \le 1$; without positivity the value $4$ occurs; in the one-mode Klein-twisted realisation in $\Cl(2,2)$, with parity-odd directions, $C^{2} = 4 + 4(a_{1} \wedge a_{2})(b_{1} \wedge b_{2})e_{1}f_{2}$ and the saturating state at blade settings is $\tfrac14(1 + e_{1}f_{2}) + \tfrac{\sqrt{2}}{8}C$.
