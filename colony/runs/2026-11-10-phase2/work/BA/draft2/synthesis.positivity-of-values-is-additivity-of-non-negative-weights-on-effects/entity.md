---
id: synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects
kind: claim
version: 1
title: 'Positivity (P) as additive weights on effects; the parity average supplies none'
status: proved
region: synthesis
subject: clifford-structure
tags: [measurement-and-records, finite-models, classical-theorem, grading-and-parity]
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
  - singularity.descent-parity-average@5
  - synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product@1
  assumes:
  - synthesis.premise-positivity-of-values@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_self_adjoint_blades_and_the_order_unit
- kind: check
  ref: check.py::check_an_effect_relation_forces_the_born_weight_on_one_mode
- kind: check
  ref: check.py::check_parity_average_keeps_the_cone_and_adds_no_positivity
- kind: check
  ref: check.py::check_even_atom_sees_the_products_of_odd_directions
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - one-relation.measure-indifference-borns-rule-located
  - one-relation.imported-envariance-born-rule
  - singularity.p-univalence
extraction:
  open_problem: op.positivity-of-values
  note: >-
    The first and third attack items of op.positivity-of-values, constructive side: what (P) is equivalent
    to, and whether the descent supplies it. Clause (ii) is the theorem of P. Busch (Quantum states and
    generalized observables: a simple proof of Gleason's theorem, Phys. Rev. Lett. 91 (2003) 120403,
    arXiv:quant-ph/9909073; existence, title and abstract checked on the web, the argument from memory) and
    of Caves, Fuchs, Manne and Renes (Found. Phys. 34 (2004) 193, from memory), placed in the series'
    algebra with the blade inverse and stated over ordered fields; over the rationals the linear extension
    needs no positivity and no continuity, a remark that is probably known and is not claimed as new.
    Clause (iv) is the standard fact that a group average is a positive map. Clause (v) is an identity in
    the algebra of two modes; the stored CHSH bound, clause (viii), already records that a saturating state
    can be even. What this result records about the open problem. (1) (P) is not derived from the stored
    measurement premises; it is shown equivalent to a strong form of the residual postulate that the stored
    Born account isolates (one-relation.measure-indifference-borns-rule-located: that weights exist and
    add), namely non-negative normalised weights on all effects that add whenever the sum is an effect.
    That this is the right reading of the residual postulate is argued, not proved: the stored postulate
    is informal, and its weak reading (additivity for projectors of one commuting family) does not give
    (P) when atoms come in complementary pairs (Gleason's theorem excludes dimension two; the sibling
    result of this run on weights on projectors is the intended citation, and clause (iii) here is one
    instance used only to show an effect relation at work). (2) The parity average of the descent maps
    positive elements to positive elements and creates no positivity, so "the descent is a conditional
    expectation" gives (P) only for functionals already positive on even elements; under the univalence
    premise (singularity.p-univalence) (P) is a statement about the even subalgebra. A sibling result of this run treats the mode-wise and total parity averages on two modes with the box functional and is the intended citation for that instance; clause (iv) here is the general lemma. (3) Univalence and
    the parity average act on states and on single elements; they do not remove the correlations of
    parity-odd elements, so they do not decide between the two stored settings for observables. The
    independence statement that these clauses support is limited: positivity is independent of linearity,
    normalisation, reality, evenness and invariance under the parity average, on one algebra; independence
    from the whole stored premise set is not claimed. Kill conditions registered before computing: 1 fails
    to be an order unit for the cone of hermitian squares, or the extension is not well defined (neither
    occurred); an even state cannot exceed 2 at one mode per party with the Klein-twisted directions (it
    reaches 14/5). Classical mathematics; transport-absent.
---

## formal
Let $k$ be $\Q$ or an ordered field, and $\Cl_{k}(p,q)$, the blade inverse $\dagger$ and the scalar part $\langle\cdot\rangle_{0}$ as in Theorem \claimref{synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate}, for a fixed split of the generators. Premise (P), positivity of values (Premise \claimref{synthesis.premise-positivity-of-values}), is assumed, not derived, wherever states are spoken of: a \emph{state} is a $k$-linear $\omega$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(x^{\dagger}) = \omega(x)$.

\emph{Definitions.} The \emph{cone} $\mathcal{K}$ is the set of sums $\sum_{r}c_{r}x_{r}x_{r}^{\dagger}$ with $c_{r} \ge 0$ in $k$. An \emph{effect} is an element $E$ with $E \in \mathcal{K}$ and $1 - E \in \mathcal{K}$; projectors (elements $E = E^{\dagger} = E^{2}$) are effects. A \emph{weight} is a map $\mu$ from effects to $k$ with $\mu(E) \ge 0$, $\mu(1) = 1$, and $\mu(E + F) = \mu(E) + \mu(F)$ whenever $E$, $F$ and $E + F$ are effects.
\begin{enumerate}
\item[(i)] \emph{(The unit bounds every self-adjoint element; proved.)} The self-adjoint elements are the span of the blades of square $1$. For such a blade $b$, $1 \pm b = \tfrac12(1 \pm b)(1 \pm b)^{\dagger}$. Hence for self-adjoint $s = \sum_{b}c_{b}b$ and $n_{s} = \sum_{b}|c_{b}|$ both $n_{s} - s$ and $n_{s} + s$ lie in $\mathcal{K}$; every self-adjoint element is a difference of two elements of $\mathcal{K}$, and the effects span the self-adjoint elements.
\item[(ii)] \emph{(Weights on effects are the states of (P); proved for $k = \Q$ and for every Archimedean ordered $k$.)} The restriction of a state to the effects is a weight, and every weight is the restriction of exactly one state. For $k = \Q$ the non-negativity of $\mu$ is not used in showing that $\mu$ extends to a linear functional: every map on effects with values in $\Q$ that is additive in the sense above extends uniquely to a $\Q$-linear functional $\omega$ with $\omega(x^{\dagger}) = \omega(x)$, and it is non-negative on effects exactly when $\omega(xx^{\dagger}) \ge 0$ for all $x$. So (P) is equivalent to: values of effects are non-negative, normalised and additive.
\item[(iii)] \emph{(An effect relation at work; proved, one instance.)} On one mode, $\Cl_{k}(1,1)$ with $p_{1} = f_{1}e_{1}$, let $\Pi_{e} = \tfrac12(1 + e_{1})$, $\Pi_{p} = \tfrac12(1 + p_{1})$, $E_{a} = \tfrac12(1 + \tfrac35 e_{1} + \tfrac45 p_{1})$, three projectors. Then $\tfrac12E_{a} + \tfrac{1}{10} = \tfrac{3}{10}\Pi_{e} + \tfrac{4}{10}\Pi_{p}$, with every term and both sides effects. A weight with $\mu(\Pi_{p}) = 1$ and $\mu(\Pi_{e}) = \tfrac12$ therefore has $\mu(E_{a}) = \tfrac{9}{10}$, the value of the state $x \mapsto 2\langle\Pi_{p}x\rangle_{0}$. The function $\tfrac12(1 + xe_{1} + zp_{1}) \mapsto \tfrac12(1 + z^{3})$ on the projectors other than $0$ and $1$ is non-negative, takes those two values, and is additive on every pair of projectors with sum $1$, the only families of orthogonal projectors of one mode; it gives $E_{a}$ the value $\tfrac{189}{250}$ and so is not the restriction of a weight on effects.
\item[(iv)] \emph{(The parity average keeps the cone and adds no positivity; proved.)} Let $\Gamma$ be self-adjoint with $\Gamma^{2} = 1$ and $E_{\Gamma}(x) = \tfrac12(x + \Gamma x\Gamma)$, the average of Theorem \claimref{singularity.descent-parity-average} (there for one mode; for the total parity as in Theorem \claimref{synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product}). Then $E_{\Gamma}(x^{\dagger}) = E_{\Gamma}(x)^{\dagger}$, $E_{\Gamma}(yy^{\dagger}) = \tfrac12\bigl(yy^{\dagger} + (\Gamma y)(\Gamma y)^{\dagger}\bigr)$, and $E_{\Gamma}(\mathcal{K})$ is the set of elements of $\mathcal{K}$ fixed by $E_{\Gamma}$. So for a linear functional $\varphi$, $\varphi \circ E_{\Gamma}$ is non-negative on $\mathcal{K}$ exactly when $\varphi$ is non-negative on the fixed elements of $\mathcal{K}$: a functional invariant under the average satisfies the positivity clause only if it is already non-negative on the fixed positive elements, and the average does not make it so. Example: on $\Cl_{k}(2,2)$, $\varphi(x) = \langle(1 + 2p_{1})x\rangle_{0}$ is linear, normalised, real and invariant under the total parity average, with $\varphi(\tfrac12(1 - p_{1})) = -\tfrac12$. If $\Gamma$ is the total parity (the grading) and $p + q \ge 1$, the fixed elements of $\mathcal{K}$ are the sums $\sum_{r}c_{r}y_{r}y_{r}^{\dagger}$ with every $y_{r}$ even: for a functional that vanishes on odd elements, (P) on the algebra is equivalent to (P) for its restriction to the even subalgebra.
\item[(v)] \emph{(Even states see the products of odd directions; proved, under (P) for the inequality.)} In $\Cl_{k}(2,2)$ let $\Gamma = p_{1}p_{2}$ and take the directions of clause (vii) of the theorem cited first, $a_{i} = x_{i}e_{1} + z_{i}p_{1}$ and $b_{j} = x'_{j}e_{2}p_{1} + z'_{j}p_{2}$ ($x_{i}^{2} + z_{i}^{2} = x'^{2}_{j} + z'^{2}_{j} = 1$), with CHSH element $C = a_{1}(b_{1} + b_{2}) + a_{2}(b_{1} - b_{2})$. Put $X = x_{1}(x'_{1} + x'_{2}) + x_{2}(x'_{1} - x'_{2})$, $Z = z_{1}(z'_{1} + z'_{2}) + z_{2}(z'_{1} - z'_{2})$ and $u = e_{2}f_{1}$. Then
\[
E_{\Gamma}(C) = Xu + Z\Gamma, \qquad u^{\dagger} = u, \quad u^{2} = 1, \quad u\Gamma = \Gamma u ,
\]
while the CHSH element of the averaged directions $E_{\Gamma}(a_{i}) = z_{i}p_{1}$, $E_{\Gamma}(b_{j}) = z'_{j}p_{2}$ is $Z\Gamma$: the average is not multiplicative, $E_{\Gamma}(a_{i}b_{j}) \ne E_{\Gamma}(a_{i})E_{\Gamma}(b_{j})$ when $x_{i}x'_{j} \ne 0$. For every state $\omega$ with $\omega \circ E_{\Gamma} = \omega$ (an even state): $\omega(C) = X\omega(u) + Z\omega(\Gamma)$ and $|\omega(C)| \le |X| + |Z|$, with equality on the four even projectors $\tfrac14(1 \pm u)(1 \pm \Gamma)$ for suitable signs, and $(|X| + |Z|)^{2} \le 8$. At $a_{1} = e_{1}$, $a_{2} = p_{1}$, $b_{1} = \tfrac35 e_{2}p_{1} + \tfrac45 p_{2}$, $b_{2} = \tfrac45 e_{2}p_{1} - \tfrac35 p_{2}$: $X = Z = \tfrac75$, the even state of $\tfrac14(1 + u)(1 + \Gamma)$ has $\omega(C) = \tfrac{14}{5} > 2$, and the averaged directions give at most $\tfrac75$. So a restriction to even states (Premise \claimref{singularity.p-univalence}, which is not assumed here) together with the parity average does not reduce the setting with parity-odd directions to the setting with parity-even observables; only a restriction on which elements are observables would.
\end{enumerate}
\emph{Scope.} Clause (ii) does not derive (P); it says what (P) is equivalent to. The equivalent statement is strong: additivity is asked of all effects, including sums of effects that do not commute, which no single measurement realises. Clause (iv) is about one algebra and the positivity clause; it does not show that (P) is independent of the series' other premises.

## technical
Premise (P), positivity of values, is assumed in the series and not derived. This result says what it is equivalent to and what the descent does for it, in every Clifford algebra $\Cl_{k}(p,q)$ over the rationals or an Archimedean ordered field, with the blade inverse as adjoint. Call an element an effect if it and its complement to $1$ are combinations, with non-negative coefficients, of elements $xx^{\dagger}$; projectors are effects, and so are their multiples by numbers between $0$ and $1$. Then the states of (P) are exactly the assignments of non-negative numbers to effects that give $1$ the value $1$ and add whenever a sum of two effects is an effect. Over the rationals additivity alone already gives linearity, with no continuity argument; non-negativity then is the positivity clause. So, given this reading, (P) is the statement that weights exist on all effects, are non-negative and add; it is a strong form of the residual postulate that the stored Born account isolates, and it is strong because it asks additivity also of effects that do not commute. A relation among effects of one mode shows the mechanism: it forces the weight $\tfrac{9}{10}$ where a function that is additive only on complementary projectors can give $\tfrac{189}{250}$.

The parity average of the descent, $x \mapsto \tfrac12(x + \Gamma x\Gamma)$, commutes with the adjoint and maps positive elements to positive elements, so it preserves states; but it creates no positivity. A functional invariant under the average satisfies the positivity clause only if it is already non-negative on the positive even elements, and a normalised real invariant functional can give a projector the value $-\tfrac12$. For functionals that vanish on odd elements, (P) is a statement about the even subalgebra alone. Finally, under (P), the average is not multiplicative: for the stored one-mode directions of mixed parity against the Klein-twisted other mode, the average of the CHSH element is $Xu + Z\Gamma$ with $u = e_{2}f_{1}$ even, and an even state gives it values up to $|X| + |Z|$, for example $\tfrac{14}{5}$, where the CHSH element of the averaged directions gives at most $\tfrac75$. So restricting states to even ones and applying the average does not turn the setting with parity-odd directions into the setting with even observables; that would take a restriction on observables.

## lay
The series assumes a rule, called (P), for the averages of measurable quantities: averages add up, the trivial quantity has average 1, and a quantity times its mirror image never has a negative average. This result shows, under that reading of the terms, what the assumption amounts to. Think of every yes-or-no question, sharp or blurred, as having a chance. Then (P) holds exactly when those chances are never negative, the certain question has chance 1, and the chances add up whenever two questions combine into one. Over fractions nothing more is needed, not even an argument about limits. So (P) is the assumption that chances exist and add, in a strong form: the adding is required even for questions that cannot be asked in the same experiment.

Two further points, both given the series' stated definitions. The series has an averaging step, part of what it calls the descent, that erases quantities which change the count of particles from even to odd. Assuming nothing beyond its definition, that step keeps non-negative averages non-negative, but it cannot produce the property where it is absent, so (P) cannot be obtained from it. And although the step erases each such quantity on its own, it does not erase the product of two of them, which is of the even kind. Under (P), a state that respects the even-odd rule can still show correlations of 2.8 between two parties who use such quantities, above the limit of 2 that holds when they do not. So the even-odd rule for states does not settle whether such quantities count as measurements.

## one-liner
Under the stated definitions, in $\Cl_{k}(p,q)$ over $\Q$ or an Archimedean ordered field: the states of (P) are exactly the non-negative, normalised, additive weights on effects (over $\Q$ additivity alone gives linearity); the parity average maps positive elements to positive elements and creates no positivity; and for even states the CHSH element of mixed-parity directions has the value of $Xu + Z\Gamma$, up to $|X| + |Z|$ (for example $\tfrac{14}{5}$), not that of the averaged directions.
