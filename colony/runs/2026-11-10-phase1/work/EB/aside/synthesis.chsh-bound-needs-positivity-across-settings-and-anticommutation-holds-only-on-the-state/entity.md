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
  - synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_box_functional_has_value_four_and_fails_positivity_only_across_settings
- kind: check
  ref: check.py::check_square_eight_on_a_state_with_nonzero_anticommutator
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.premise-superposition-over-the-integers
  - one-relation.imported-envariance-born-rule
extraction:
  note: >-
    Adversarial test of two points of the plan for a CHSH statement rooted in the foundation's premises. First:
    does the bound on values follow from the algebra, or does it need a premise about values? A counter-model
    settles it: on the integer Clifford algebra there is a normalised, integer-valued linear functional that
    assigns non-negative, no-signalling probabilities to every pair of settings and has CHSH value $4$. It is the
    Popescu-Rohrlich box (S. Popescu and D. Rohrlich, Found. Phys. 24 (1994) 379, from memory) written as a
    functional on the algebra. So the operator identity for $C^{2}$, which holds in the integer algebra, bounds
    nothing by itself, and the premise needed is positivity of the value functional on elements that add
    products across settings that are not measured together; clause (ii) says on which two elements. This is
    a statement about one algebra and one functional; that no stored premise supplies such positivity is argued
    (the foundation postulates (F1) to (F4) define an algebra and its coefficients and mention no value
    functional; the stored Born account is the imported envariance Fact, which presupposes that probabilities
    exist and add), not audited over the whole store, and adopting a positivity premise is a decision for the
    maintainer. Second: is anticommutation of a party's two observables forced when $C^{2}$ has value $8$? For
    directions of a plane it is (a sibling result of the same run proves this with a rational certificate;
    intended citation once both are stored); clause (iii) shows that for general observables it holds only on
    the state. That maximal CHSH value fixes the observables only on the support of the state is the content of
    self-testing (Summers and Werner 1987; Popescu and Rohrlich 1992; from memory). Kill conditions registered
    before computing: the identity forcing the bound for all normalised functionals, or no pair of observables
    with nonzero anticommutator and $C^{2}$ of value $8$ (neither fired). Classical mathematics; transport-absent.
---

## formal
Let $\Cl_{\Z}(\ell,\ell)$ be the integer Clifford algebra of Theorem \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra} on the modes of Theorem \claimref{synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product}: generators $e_{k}$, $f_{k}$ with $Q(e_{k}) = 1$, $Q(f_{k}) = -1$, $p_{k} = f_{k}e_{k}$, and $\dagger$ the linear extension of the inverse on blades. Observables are self-adjoint elements of square $1$; for observables with $A_{i}B_{j} = B_{j}A_{i}$ put $C = A_{1}B_{1} + A_{1}B_{2} + A_{2}B_{1} - A_{2}B_{2}$, so that $C^{2} = 4 - [A_{1},A_{2}][B_{1},B_{2}]$ (classical). For $\ell = 2$ take the integer blades $A_{1} = p_{1}$, $A_{2} = e_{1}$, $B_{1} = p_{2}$, $B_{2} = e_{2}p_{1}$ of the twisted split: they commute across the pairs and anticommute within, and $C^{2} = 4 + 4K$, $K = -A_{1}A_{2}B_{1}B_{2}$, $K^{\dagger} = K$, $K^{2} = 1$.
\begin{enumerate}
\item[(i)] \emph{(The box functional; proved.)} $\lambda(x) = \langle(1 + C)x\rangle_{0}$ is linear and integer-valued on $\Cl_{\Z}(2,2)$, with $\lambda(1) = 1$ and $\lambda(x^{\dagger}) = \lambda(x)$. It has $\lambda(A_{i}) = \lambda(B_{j}) = 0$, $\lambda(A_{1}B_{1}) = \lambda(A_{1}B_{2}) = \lambda(A_{2}B_{1}) = 1$, $\lambda(A_{2}B_{2}) = -1$, hence $\lambda(C) = 4$. For each pair of settings and outcomes $a, b = \pm 1$ the number $\lambda\bigl(\tfrac12(1 + aA_{i})\,\tfrac12(1 + bB_{j})\bigr) = \tfrac14(1 + ab\,\lambda(A_{i}B_{j}))$ is $0$ or $\tfrac12$, the four sum to $1$, and each party's marginal is $\tfrac12$ whatever the other party's setting. So everything a CHSH experiment samples is a non-negative probability with no signalling. But $\lambda((C - t)(C - t)^{\dagger}) = t^{2} - 8t + 4$, which is negative for $t = 1, \dots, 7$ (it is $-12$ at $t = 4$): $\lambda$ is not non-negative on all $xx^{\dagger}$.
\item[(ii)] \emph{(What positivity is used; proved.)} Let $\varphi$ be linear with $\varphi(1) = 1$, on the algebra over any ordered field. If $\varphi((C - t)^{2}) \ge 0$ for every scalar $t$ and $\varphi((1 - K)^{2}) \ge 0$, then $\varphi(C)^{2} \le \varphi(C^{2}) = 4 + 4\varphi(K) \le 8$. Both elements add products of observables of different setting pairs; $\lambda$ satisfies the second condition ($\lambda((1 - K)^{2}) = 2$) and fails the first. So the CHSH identity bounds values only together with the premise that the value functional is non-negative on $xx^{\dagger}$ for such $x$, and the algebra of the foundation does not imply it: $\lambda$ is a counter-model.
\item[(iii)] \emph{(Anticommutation only on the state; proved.)} For $\ell = 3$ let $P_{\pm} = \tfrac12(1 \pm p_{3})$, $A_{1} = p_{1}$, $A_{2}' = e_{1}P_{+} + p_{1}P_{-}$, $B_{1} = p_{2}$, $B_{2} = e_{2}p_{1}$. These are observables commuting across the pairs, $A_{1}A_{2}' + A_{2}'A_{1} = 1 - p_{3} \ne 0$, and $C^{2} = 4 + 4KP_{+}$. For $8r^{2} \le 1$ the functional $\varphi_{r}(x) = \langle(1 + K)(1 + p_{3})(1 + rC)x\rangle_{0}$ is a state (non-negative on every $xx^{\dagger}$) with $\varphi_{r}(C^{2}) = 8$, $\varphi_{r}(C) = 8r$ and $\varphi_{r}((A_{1}A_{2}' + A_{2}'A_{1})^{2}) = 0$. So value $8$ of $C^{2}$ does not force $A_{1}A_{2} + A_{2}A_{1} = 0$ as an identity of elements; it holds only where the state is supported.
\end{enumerate}

## technical
Two limits on what a CHSH statement in the foundation's algebra can claim. First, the identity $C^{2} = 4 - [A_{1},A_{2}][B_{1},B_{2}]$ holds already in the integer Clifford algebra, but it bounds no correlation by itself. On $\Cl_{\Z}(2,2)$ the functional $\lambda(x) = \langle(1 + C)x\rangle_{0}$ is normalised, integer-valued, assigns to every pair of settings a non-negative no-signalling probability table, and has CHSH value $4$: it is the Popescu-Rohrlich box as a functional on the algebra. It fails non-negativity only on elements such as $(C - 4)^{2}$, which add products across setting pairs that are never measured together. The bound $\varphi(C)^{2} \le 8$ uses non-negativity on exactly the elements $(C - t)^{2}$ and $(1 - K)^{2}$. So the bound on values rests on a premise about the value functional, positivity on every $xx^{\dagger}$, which the algebra does not supply; naming and adopting it is a maintainer decision. Second, value $8$ for $C^{2}$ forces a party's two observables to anticommute only on the state: a three-mode example has anticommutator $1 - p_{3} \ne 0$ and rational states with $C^{2}$ of value $8$ and CHSH values $8r$ for every $8r^{2} \le 1$. For directions of a plane the anticommutator is a scalar and the stronger statement holds. Classical mathematics throughout.

## lay
The quantum limit $2\sqrt{2}$ on correlations between two parties is often derived from an algebraic identity. This result shows that the identity is not enough. Inside the same whole-number algebra there is a rule for assigning average values that gives sensible, non-negative probabilities for every experiment the two parties can actually perform, lets neither party signal to the other, and still reaches $4$, the largest value arithmetic allows. What rules it out is an extra requirement: that averages of squares be non-negative even for combinations of measurements that can never be performed together. That requirement is an assumption about how values are assigned, not a consequence of the algebra. The result also shows by example that reaching the quantum limit does not force a party's two measurements to be exactly "perpendicular", only to behave so on the state being measured.

## one-liner
On $\Cl_{\Z}(2,2)$ the functional $\langle(1 + C)x\rangle_{0}$ gives non-negative no-signalling probabilities at every setting pair and CHSH value $4$, failing only $\lambda((C - t)^{2}) \ge 0$; so the bound $\varphi(C)^{2} \le 8$ needs positivity on $(C - t)^{2}$ and $(1 - K)^{2}$, a premise the algebra does not supply; and value $8$ of $C^{2}$ forces anticommutation only on the state (three-mode example).
