---
id: synthesis.premise-positivity-of-values
kind: claim
version: 2
title: 'Premise (P): positivity of values'
status: postulate
region: synthesis
subject: clifford-structure
tags: [entanglement, measurement-and-records]
proposed_by:
  kind: ai
  session: maintainer-2026-11-10
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction and decision (adoption of the premise, with reality, relative to the mode split)
- name: Claude Fable 5.2
  role: drafting
  source: maintainer pass of 2026-11-10
- name: Claude Fable 5.2
  role: 'premise wording: what the counter-model shows restated (local weights already give the bound in the one-mode realisation); pointers to the results on weights on effects, on the split and on sharp states'
  version: 2
  source: maintainer pass of 2026-11-10
review: draft
about:
- obj.std-algebra.clifford-algebra
lineage:
  motivated_by:
  - synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate
  - synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state
  - synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product
  - synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values
  - synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects
  - synthesis.splits-adapted-to-the-null-pairs-and-the-states-common-to-all-of-them
  - synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional
extraction:
  maintainer_pass_2026_11_10_b:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: >-
      Version 1 -> 2 (second pass of 10 November 2026, after the run on positivity and the Born rule). The first
      sentence of the paragraph on costs said that positivity on elements combining quantities never measured
      together is "the part the counter-model shows cannot be dropped"; that was too strong, because in the
      one-mode realisation non-negative weights at all pairs of local directions already give the bound
      (synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values, clauses (ii) and (iii)). It is restated, and the phrase "negative only on elements that combine
      different pairs of settings" now says that the pairs meant are the four configured ones. Added: what (P)
      says in terms of weights on effects (synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects); that in the mode algebras the stored null pairs as vectors fix
      the split, and only the isotropic subspaces leave it open (synthesis.splits-adapted-to-the-null-pairs-and-the-states-common-to-all-of-them); what (P) gives for a state sharp on an
      atom (synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional). The reference to the imported envariance Fact, now retired, is replaced by the stored Born
      account, which rests on (P) from its version 4. The three clauses of the premise (normalisation,
      positivity, reality) and the split are unchanged, so results assuming version 1 assume the same premise.
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: >-
      New postulate, registered by Leon's decisions of 10 November 2026: Hypothesis (P) of the stored CHSH results is
      adopted as a named premise, with the reality clause, and is stated relative to the split of the generators
      that defines the modes. It is not a foundation postulate. The six entanglement results assume it.
  env: premise
  open_problem: op.positivity-of-values
  note: >-
    The wording of the premise is that of Hypothesis (P) in the formal level of the stored CHSH bound
    (synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate), where it was an
    in-statement hypothesis; that result and five others now assume this entity. The letter (P) is also the
    letter of the univalence premise of the singularity results (singularity.p-univalence), a different
    statement; in the store's texts "(P), positivity of values" is always this one. The premise is not one of
    the foundation postulates F1 to F4 and carries no founded_on edge: the foundation supplies the algebra, and
    this is a premise about the functionals that give values. What is recorded about it, with the place where
    each item is proved: stored states satisfy it (the CHSH bound, clause (iii)); it turns the identity for the
    square of the CHSH element into the bound (clause (iii)); without its positivity clause the value 4 occurs
    (clause (v), and the box functional of
    synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state); the
    adjoint it uses depends on the split in indefinite signature (clause (vi)). Not derived, and not shown
    independent of the store's other premises: the counter-model is a functional on one algebra, not a model of
    the whole store. Both questions, the choice of split and the status of parity-odd elements are the open
    problem op.positivity-of-values. Classical background: (P) is the definition of a state on an algebra with
    an involution (a positive normalised linear functional), here over an ordered field and with the involution
    fixed by the generators.
---

## formal
\emph{Premise (P), positivity of values.} Let $k$ be $\Q$ or any ordered field, and $\Cl_{k}(p,q)$ the Clifford algebra of Theorem \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra} with coefficients in $k$ (Theorem \claimref{synthesis.division-gives-the-rationals}), with blades $e_{S}$, the images of the group $G$ of signed directions. Let $x \mapsto x^{\dagger}$ be the linear extension of the inverse of $G$, $e_{S}^{\dagger} = e_{S}^{-1}$ (the blade inverse): the anti-automorphism that fixes each generator of square $1$ and negates each generator of square $-1$. The premise is: values are given by a \emph{state}, a $k$-linear $\omega : \Cl_{k}(p,q) \to k$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(x^{\dagger}) = \omega(x)$ for all $x$. The three clauses are called normalisation, positivity and reality. The value of an element $x$ is $\omega(x)$.

\emph{The split.} The adjoint is defined by the chosen generators, so (P) is stated relative to a split of the generators into those of square $+1$ and those of square $-1$. The split meant is the one that defines the modes: in $\Cl_{k}(\ell,\ell)$ the generators $e_{j}$, $f_{j}$ with $Q(e_{j}) = 1$, $Q(f_{j}) = -1$ of the null pairs $v_{j} = \tfrac12(e_{j} + f_{j})$, $w_{j} = \tfrac12(e_{j} - f_{j})$ (Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}); the adjoint fixes $e_{j}$, negates $f_{j}$ and exchanges $v_{j}$ with $w_{j}$. In definite signature the adjoint does not depend on the orthonormal frame (it is the reverse in signature $(p,0)$ and the Clifford conjugate in signature $(0,q)$). In indefinite signature another split gives another adjoint, and with it other self-adjoint elements and other states: by clause (vi) of Theorem \claimref{synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate}, in $\Cl_{\Q}(2,2)$ the unit vector $\tfrac{17}{8}e_{1} + \tfrac{15}{8}f_{1}$ of a boosted frame has square $1$ and is not self-adjoint for the split $e_{j}, f_{j}$, the functional of $\rho = \tfrac14(1 + e_{1})(1 + p_{2})$, $p_{2} = f_{2}e_{2}$, which satisfies (P) for that split, is not a state for the boosted one, and it gives a CHSH element built with that vector, an element of square $4$, the value $\tfrac{17}{4}$, where (P) bounds the value of an element of square $4$ that is self-adjoint for the split $e_{j}, f_{j}$ by $2$. So every statement made under (P) is relative to one fixed split and holds for each fixed split. In the mode algebras $\Cl_{k}(\ell,\ell)$ the split is fixed by the stored null pairs as vectors, $e_{j} = v_{j} + w_{j}$, $f_{j} = v_{j} - w_{j}$; the two isotropic subspaces they span fix it only up to a positive definite form on one of them, and the states of (P) that are states for every split adapted to those subspaces are the mixtures of the sector projectors of the number element (Theorem \claimref{synthesis.splits-adapted-to-the-null-pairs-and-the-states-common-to-all-of-them}). So the datum that supplies the split there is the choice of the pairs within their subspaces, which the relations the pairs satisfy do not force. For other indefinite signatures the premise does not say which stored datum supplies the split.

\emph{Status and cost.} A premise of the series about values, adopted by decision (10 November 2026): assumed, not derived. It is not one of the foundation postulates F1 to F4 and is not part of the foundation layer. The foundation gives the algebra, its blades and, once the generators are chosen, the adjoint; (P) is a further premise, about the functionals that give values, and the results that use it hold given it. It is not the univalence premise of the singularity results, which carries the same letter (Premise \claimref{singularity.p-univalence}).

What it does. It is what turns an identity of elements into a bound on values. For two commuting pairs of self-adjoint elements of square one, the identity for the square of the CHSH element $C$ and the certificate that writes $8 - C^{2}$ as one half of a sum of three squares (clauses (i) and (ii) of the theorem above) hold in the algebra with no premise about values; they need only the foundation postulates F1 to F3. With (P) they give Tsirelson's bound, $\omega(C)^{2} \le \omega(C^{2}) \le 8$ (clause (iii)), which uses the normalisation and positivity clauses only. Without the positivity clause the value $4$ occurs: at a configuration of blades the functional $\lambda(x) = \langle(1 + C)x\rangle_{0}$ is linear, normalised and real, has $\lambda(C) = 4$, and is negative on some $xx^{\dagger}$ (clause (v)); it gives a probability table with no signalling at each of its four configured pairs of settings and is negative only on elements that combine different pairs among those four (Theorem \claimref{synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state}); among such elements is the joint outcome idempotent of a single pair of local directions outside the four (Theorem \claimref{synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values}, clause (iii)). So (P) is not implied by the algebra together with linearity, normalisation and reality. The reality clause is used where a functional has to be fixed on all elements by its values on self-adjoint ones (the uniqueness statement of clause (viii)). The completion postulate F4 is not needed for the bound; the bound is attained only when $2$ is a square in $k$, that is, over the rationals, only after $\sqrt{2}$ is adjoined (clauses (iii), (iv) and (viii)).

What it extends. The stored definition of a state is an element $\rho = \sum_{r}x_{r}x_{r}^{\dagger}$ of unit trace (Theorem \claimref{synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product}). For such an element the functional $x \mapsto \langle\rho x\rangle_{0}/\langle\rho\rangle_{0}$ satisfies (P), because $\langle x^{\dagger}x\rangle_{0}$ is the sum of the squares of the coefficients of $x$ (clause (iii)). (P) extends that definition from elements to functionals: it says that every assignment of values is of the positive kind, which the definition of the elements $\rho$ does not say.

What it costs, and what it leaves open. Positivity is asked on every element $xx^{\dagger}$, including those that combine quantities which the two parties never measure together, and it is assumed. What the counter-model shows is narrower than version 1 of this premise said: in the one-mode realisation, local weights already give the bound, that is, non-negative weights at every pair of local directions give $\omega(C)^{2} \le 8$ with no positivity on any other element, and the box has a negative weight at such a pair outside its four (Theorem \claimref{synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values}, clauses (ii) and (iii)); positivity across settings is what the box violates, and it is not shown to be what the bound needs. What positivity on all elements adds to non-negative local weights is not visible in the values of products of local observables: a family of functionals with the same values on all of them satisfies (P) at one parameter only (clause (iv) of the same theorem). In terms of weights, (P) is equivalent to: the values of effects are non-negative, normalised and additive, additivity being asked also across effects that do not commute (Theorem \claimref{synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects}, clause (ii), for $k = \Q$ and Archimedean ordered $k$); that is the non-contextuality assumption, and it is inside the premise. Under (P) a state sharp on an atom is fixed and its weights are squared norms (Theorem \claimref{synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional}); that theorem does not derive (P) or sharpness. No derivation of (P) from the series' account of measurement is stored (the store's Born account, Proposition \claimref{one-relation.measure-indifference-borns-rule-located}, rests on (P) from its version 4 and does not derive it; the envariance argument of Zurek is prior art there), and (P) has not been shown independent of the store's other premises: the counter-model is a functional on one algebra, not a model of the whole store. The premise does not say which self-adjoint elements are observables. In particular it does not decide whether elements odd under the total parity are observables: both settings are recorded side by side (clause (vii) of the theorem above; Theorem \claimref{synthesis.chsh-with-parity-even-observables-needs-two-modes-per-party-and-no-klein-twist}). These questions are the open problem op.positivity-of-values.

## technical
The series' results on correlations between two or three parties speak of the values of elements of a Clifford algebra with rational coefficients (or coefficients in any ordered field). This premise says what a value is: values are given by a state, a linear functional $\omega$ on the algebra with $\omega(1) = 1$ (normalisation), $\omega(xx^{\dagger}) \ge 0$ for every $x$ (positivity) and $\omega(x^{\dagger}) = \omega(x)$ (reality), where the adjoint $\dagger$ is the inverse on blades extended linearly. It is assumed, not derived, and it is not one of the four foundation postulates: those give the algebra, and this is a separate premise about values, which the results using it hold given.

The adjoint is fixed by the choice of generators, so the premise is relative to a split of the generators into those of square $+1$ and those of square $-1$. The split meant is the one that defines the modes, the pairs $e_{j}$, $f_{j}$ of the null pairs. In definite signature the adjoint does not depend on the frame. In indefinite signature another split gives another adjoint, other self-adjoint elements and other states, and a bound that holds under (P) for one split can fail for elements that are self-adjoint for another: a stored example gives the CHSH combination the value $17/4$, above $2\sqrt{2}$ and above $4$. For the mode algebras the stored null pairs, as vectors, fix the split; the two isotropic subspaces alone do not, and what fixes the pairs within them is open.

Under the premise the identity for the square of the CHSH combination, which holds in the algebra without it and needs only the first three foundation postulates, becomes Tsirelson's bound: the squared value is at most $8$. Without the positivity clause the bound fails: a linear, normalised, real functional gives the combination the value $4$, with a legitimate probability table at each of its four pairs of settings, and is negative only on elements that combine different pairs among those four. That does not make positivity across settings the part the bound needs: with one mode per party, non-negative weights at every pair of local directions already give the bound, and the functional has a negative weight at a pair outside its four. In terms of weights the premise says that the values of effects are non-negative, normalised and additive, also across effects that do not commute. The premise extends the stored definition of a state, an element that is a sum of terms $xx^{\dagger}$ of unit trace, from elements to functionals. It does not say which self-adjoint elements are observables, and in particular not whether parity-odd elements are; a derivation of the premise from the series' structure, or a proof that it is independent of the other premises, is an open problem.

## lay
This is an assumption about what the average result of a measurement is. The series builds an algebra of directions from very simple starting points, and its results on correlations between distant experimenters need to say what number an average takes. The assumption, called (P), is that averages are given by a rule with three properties: the average of a sum is the sum of the averages; the trivial quantity 1 has average 1; and a quantity multiplied by its mirror image (its adjoint) never has a negative average, with a quantity and its mirror image having the same average. It is assumed, not proved, and it is not one of the four basic assumptions the algebra itself is built from.

It matters because the algebra alone does not limit correlations to the quantum limit. With this assumption the well-known limit of about 2.83 on a standard combination of correlations follows; if the "never negative" part is dropped, a rule exists that reaches 4, the largest value the combination could have, while still giving sensible probabilities for every single experiment.

Two things are left open. The mirror image depends on a division of the directions into two kinds, those squaring to plus one and those squaring to minus one; the assumption is stated for the division that defines the series' modes, and a different division gives a different mirror image and different allowed averages (for the series' modes the stored pairs of light-like directions fix the division; the two families of such directions alone would not). And the assumption does not say which quantities count as measurements. Whether it can be derived from the series' own account of measurement is an open problem.

## one-liner
Premise (P), assumed and not a foundation postulate: values are given by a state, a $k$-linear $\omega$ on $\Cl_{k}(p,q)$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(x^{\dagger}) = \omega(x)$, $\dagger$ the blade inverse, relative to the split of the generators into squares $+1$ and $-1$ that defines the modes; it turns $C^{2} = 4 - XY$ into Tsirelson's bound, and without positivity the value $4$ occurs.
