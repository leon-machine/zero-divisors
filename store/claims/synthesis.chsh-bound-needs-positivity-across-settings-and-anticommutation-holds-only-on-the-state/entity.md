---
id: synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state
kind: claim
version: 1
title: 'The CHSH bound needs positivity across settings; a box functional reaches 4'
status: proved
region: synthesis
subject: clifford-structure
tags: [entanglement, finite-models, classical-theorem]
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
  - tower.commuting-copies@5
  - synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate@1
  assumes:
  - synthesis.premise-positivity-of-values@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_box_functional_has_value_four_and_fails_positivity_only_across_settings
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.premise-superposition-over-the-integers
  - one-relation.imported-envariance-born-rule
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: >-
      Hypothesis (P) is now the stored premise synthesis.premise-positivity-of-values (Leon's decision of 10 November 2026): an assumes edge to it is added, the formal level and the proof cite it with the label (P) kept, and the note names the stored results it refers to by id. No statement changed; version kept at 1.
  note: >-
    Adversarial test of whether the CHSH bound on values follows from the algebra or needs a premise about
    values. A counter-model settles it: on the integer Clifford algebra, extended $\Q$-linearly, there is a
    normalised linear functional with $\lambda(x^{\dagger}) = \lambda(x)$ that assigns a non-negative,
    no-signalling probability table to every pair of settings and has CHSH value $4$. It is the Popescu-Rohrlich
    box (S. Popescu and D. Rohrlich, Found. Phys. 24 (1994) 379; existence checked on the web) written as a functional
    on the algebra. The stored CHSH result has the functional, its value $4$ and its negative value at $t = 1$
    (clause (v)); what is recorded here is where the functional is non-negative (inside each setting pair), where
    it is negative (inertia $(12, 4, 0)$, with examples), and a pair of positivity conditions that suffices for
    the bound. What is proved: the algebra and linearity do not imply the bound. That no stored premise supplies
    positivity is argued, not audited over the whole store. The stored definition of a state (an element
    $\rho = \sum x_{r}x_{r}^{\dagger}$ of unit trace) already has positivity built in, so the gap is between functionals and stored states. Decision of 10 November 2026: (P) is adopted as a premise, with reality, and is the stored entity synthesis.premise-positivity-of-values; this result assumes it for its statements about states (the counter-model, a functional that is not a state, needs no premise about values), and the label (P) is kept in the text. The statement that anticommutation of a
    party's observables holds only on the state, with its three-mode example, was first drafted here and is now
    clause (ix) of the stored CHSH result; it is not part of this result (the id keeps its original wording, as
    ids are not renamed). That maximal CHSH value fixes the observables only on the support of the state is the
    content of self-testing (Summers and Werner 1987; Popescu and Rohrlich 1992; both from memory). Kill
    condition registered before computing: the identity forcing the bound for all normalised functionals (did
    not fire). Only the twist is used of the stored commuting-copies theorem. Classical mathematics;
    transport-absent.
---

## formal
Let $k$ be $\Q$ or an ordered field, and $\Cl_{k}(2,2)$ the algebra of two modes: generators $e_{j}$, $f_{j}$ with $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, $p_{j} = f_{j}e_{j}$, the integer algebra $\Cl_{\Z}(2,2)$ of Theorem \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra} inside it. As in Theorem \claimref{synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate}, $\dagger$ is the linear extension of the inverse on blades, observables are self-adjoint elements of square $1$, and $C = A_{1}(B_{1} + B_{2}) + A_{2}(B_{1} - B_{2})$ for a configuration. The adjoint is defined by the chosen generators. In definite signature it does not depend on the orthonormal frame; in indefinite signature it depends on the split into generators of square $1$ and of square $-1$, so observables, states and (P) are relative to that split, and each statement holds for every fixed split.

\emph{Hypothesis (P), positivity of values:} values are given by a \emph{state}, a $k$-linear $\omega : \Cl_{k}(2,2) \to k$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(x^{\dagger}) = \omega(x)$ for all $x$; (P) is Premise \claimref{synthesis.premise-positivity-of-values}, assumed, not derived.

(P) extends the stored definition of a state as an element $\rho = \sum_{r}x_{r}x_{r}^{\dagger}$ of unit trace from elements to functionals. Throughout, the configuration is the blade configuration $A_{1} = p_{1}$, $A_{2} = e_{1}$, $B_{1} = p_{2}$, $B_{2} = e_{2}p_{1}$ (mode $1$ against the copy of mode $2$ twisted as in Theorem \claimref{tower.commuting-copies}; integer blades, commuting across the pairs, anticommuting within), with $C^{2} = 4 + 4K$, $K = -A_{1}A_{2}B_{1}B_{2}$, by clause (iv) of Theorem \claimref{synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate}. Let $\lambda(x) = \langle(1 + C)x\rangle_{0}$, the functional of clause (v) of that theorem: integer-valued on $\Cl_{\Z}(2,2)$, extended $\Q$-linearly, with $\lambda(1) = 1$, $\lambda(x^{\dagger}) = \lambda(x)$, $\lambda(C) = 4$. The element $1 + C$ is self-adjoint of unit scalar part and is not a stored state: it is not a sum of elements $xx^{\dagger}$, by (ii).
\begin{enumerate}
\item[(i)] \emph{(The box: a probability table at every setting pair; proved.)} $\lambda(A_{i}) = \lambda(B_{j}) = 0$, $\lambda(A_{1}B_{1}) = \lambda(A_{1}B_{2}) = \lambda(A_{2}B_{1}) = 1$, $\lambda(A_{2}B_{2}) = -1$. For each setting pair $(i,j)$ and outcomes $a, b = \pm 1$ the values $\lambda\bigl(\tfrac12(1 + aA_{i})\,\tfrac12(1 + bB_{j})\bigr) = \tfrac14(1 + ab\,\lambda(A_{i}B_{j}))$ on the four idempotents (elements of the algebra over $\Q$, not of the integer algebra) are $0$ or $\tfrac12$, they sum to $1$, and each party's marginal is $\tfrac12$ whatever the other party's setting. Moreover $\lambda(xx^{\dagger}) \ge 0$ for every $x$ in the algebra generated by one setting pair $A_{i}, B_{j}$: inside one setting pair $\lambda$ is a probability measure.
\item[(ii)] \emph{(Where the box is negative; proved.)} The symmetric form $(x, y) \mapsto \lambda(xy^{\dagger})$ on the $16$-dimensional algebra has inertia $(12, 4, 0)$: it is negative definite on a subspace of dimension $4$ and no larger. $\lambda((C - t)(C - t)^{\dagger}) = t^{2} - 8t + 4$, negative exactly for $4 - 2\sqrt{3} < t < 4 + 2\sqrt{3}$ (so for $t = 1, \dots, 7$; value $-12$ at $t = 4$). Negative values occur also on elements using only two setting pairs with a shared setting: $h = A_{1}(B_{1} + B_{2})$ has $\lambda((h - 2)^{2}) = -2$. All such elements combine different setting pairs; by (i) none lies in the algebra of one setting pair.
\item[(iii)] \emph{(A sufficient pair of positivity conditions, for this blade configuration; proved.)} Let $\varphi$ be $k$-linear with $\varphi(1) = 1$. If $\varphi((C - \varphi(C))^{2}) \ge 0$ and $\varphi((1 - K)^{2}) \ge 0$, then $\varphi(C)^{2} \le \varphi(C^{2}) = 4 + 4\varphi(K) \le 8$. Both elements combine different setting pairs. $\lambda$ satisfies the second condition ($\lambda((1 - K)^{2}) = 2$) and fails the first. The two conditions are sufficient; nothing here shows they are necessary, and other sufficient sets exist. Consequence: the stored identity for $C^{2}$, which $\lambda$ satisfies as an identity of elements, together with linearity, normalisation, reality and a probability table at every setting pair, does not imply the bound; the bound follows under (P), and (P) is not implied by the algebra.
\end{enumerate}

## technical
The identity $C^{2} = 4 - [A_{1},A_{2}][B_{1},B_{2}]$ holds already in the integer Clifford algebra, but it bounds no value by itself; the bound is a statement under Hypothesis (P), positivity of values (values are given by a state, a linear $\omega$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$, $\omega(x^{\dagger}) = \omega(x)$; assumed, not derived). On $\Cl_{\Z}(2,2)$, extended $\Q$-linearly, the stored functional $\lambda(x) = \langle(1 + C)x\rangle_{0}$ is normalised, real on self-adjoint elements, assigns to every pair of settings a non-negative no-signalling probability table, and has CHSH value $4$: the Popescu-Rohrlich box as a functional on the algebra. It is non-negative on $xx^{\dagger}$ for every $x$ in the algebra of one setting pair. It is negative on $(C - t)^{2}$ for $4 - 2\sqrt{3} < t < 4 + 2\sqrt{3}$ (about $0.54 < t < 7.46$) and on other elements that combine different setting pairs, for example $(A_{1}(B_{1} + B_{2}) - 2)^{2}$ with value $-2$, never inside one setting pair; the form $\lambda(xy^{\dagger})$ has inertia $(12, 4, 0)$. For this blade configuration the bound $\varphi(C)^{2} \le 8$ follows from positivity on $(C - \varphi(C))^{2}$ and $(1 - K)^{2}$; these two conditions are sufficient and are not claimed necessary. So the bound on values rests on (P), which the algebra does not supply. The stored definition of a state as an element $\sum x_{r}x_{r}^{\dagger}$ has positivity built in, and $1 + C$ is not such an element; the gap is between functionals and stored states. The adjoint, and with it (P), is relative to the split into generators of square $1$ and $-1$. Classical mathematics throughout.

## lay
The quantum limit $2\sqrt{2}$ on correlations between two parties is often derived from an algebraic identity. This result shows that the identity is not enough. Inside the same whole-number algebra there is a rule for assigning average values that gives sensible, non-negative probabilities for every experiment the two parties can actually perform, lets neither party signal to the other, and still reaches $4$, the largest value arithmetic allows. What rules it out is an extra requirement, Hypothesis (P): that averages of squares be non-negative even for combinations of measurements that can never be performed together. That requirement is an assumption about how values are assigned (assumed, not derived), not a consequence of the algebra. The rule that reaches $4$ breaks it only on such combinations, never within a single experiment.

## one-liner
On $\Cl_{\Z}(2,2)$, extended $\Q$-linearly, the functional $\langle(1 + C)x\rangle_{0}$ gives a non-negative no-signalling probability table at every setting pair and CHSH value $4$; it is negative on $(C - t)^{2}$ for $0.54 < t < 7.46$ and on other elements that combine different setting pairs, never inside one setting pair; the bound $\varphi(C)^{2} \le 8$ follows from positivity on $(C - \varphi(C))^{2}$ and $(1 - K)^{2}$, so it holds under (P), which the algebra does not imply.
