---
id: synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate
kind: claim
version: 1
title: 'The CHSH bound for two subsystems of one Clifford algebra, by a rational certificate'
status: proved
region: synthesis
subject: clifford-structure
tags: [entanglement, measurement-and-records, classical-theorem, forcing-and-uniqueness]
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
  - synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_square_of_the_chsh_element_and_the_rational_certificate
- kind: check
  ref: check.py::check_scalar_part_is_positive_and_every_sample_state_obeys_the_bound
- kind: check
  ref: check.py::check_klein_twisted_directions_commute_and_the_square_is_four_plus_four_wedges_k
- kind: check
  ref: check.py::check_saturating_state_is_a_pure_state_over_the_field_with_root_two
- kind: check
  ref: check.py::check_square_one_element_that_is_not_self_adjoint_exceeds_four
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.premise-minimal-non-commutativity
  - synthesis.premise-superposition-over-the-integers
  - synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product
extraction:
  note: >-
    The graph had no Bell, CHSH or Tsirelson result. This one states the CHSH bound inside the algebra that the
    foundation postulates produce and says what it uses. Kill conditions registered before computing: the identity
    for the square or the certificate failing on an exact instance; a state and self-adjoint commuting settings
    with squared value above 8; the bound needing a positivity premise beyond the foundation and definitions
    (none fired; the audit of the third is the list that follows). What is used: the integer algebra of the
    signed directions and its blades (the stored result on the group of signed directions, resting on the
    postulates of the bit, minimal non-commutativity and superposition); rational coefficients, for the factor
    one half and for directions that are not blades (the stored division result); the Klein twist of the stored
    mode split, for clause (iv) only. The adjoint is the inverse on the group of signed directions extended
    linearly and the scalar part is the coefficient of the identity, so the positivity of the scalar part of
    $x^{\dagger}x$ is a theorem, and the order used on the rationals is the one in which sums of squares are
    non-negative. What is not derived and is a definition here: that a value assignment is a normalised linear
    functional that is non-negative on every $xx^{\dagger}$, and that the quantities compared with experiment are
    its values on products of commuting self-adjoint elements of square one. This is the one place where a
    premise about measurement enters, and whether it is adopted as a named premise, or derived from the stored
    record-chain account, is a decision for the maintainer. The completion postulate is not used; the saturating
    state of clause (v) needs a square root of two and nothing else. Status of the content: classical
    mathematics. The identity for the square is Landau's (L. J. Landau, Phys. Lett. A 120 (1987) 54) and the
    bound is Tsirelson's (B. S. Cirel'son, Lett. Math. Phys. 4 (1980) 93), both cited from memory. Checked on the
    web: the algebraic form of the bound for ordered star-rings is formalised in the Lean library mathlib
    (Algebra.Star.CHSH), by a sum-of-squares decomposition that uses the square root of two and its inverse; the
    certificate of clause (i) bounds $C^{2}$ in place of $C$ and has rational coefficients, was not found in the
    sources read, is an elementary rearrangement and is not claimed as new. C. Held, arXiv:2007.05301, derives the
    value $2\sqrt{2}$ in the geometric algebra of space for vector-valued hidden variables, a different
    statement. Geometric-algebra treatments of two-particle states use the multiparticle spacetime algebra, one
    copy of the spacetime algebra for each particle with commuting even parts (Doran, Lasenby and co-workers;
    Havel and Doran, arXiv:quant-ph/0106063; from memory); here the two parties are two modes of one Clifford
    algebra and commute through the stored twist. What is added to the classical theorem: its statement and
    proof over the rationals inside the foundation's algebra with the premises listed, the role of the twist,
    the forced anticommutation for directions, the necessity of self-adjointness with an exact counterexample,
    and the saturating state as an element of the algebra with its uniqueness. Sibling results of the same run
    (intended citations once stored): the list of signatures in which a value above 2 exists, with a family of
    rational states of the same configuration; the attainment question over the rationals; the three-party
    trade-off and the local bound. Transport-absent: nothing here uses transport.
---

## formal
Let $k$ be $\Q$ or any ordered field, and $\Cl_{k}(p,q)$ the Clifford algebra of Theorem \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra} with coefficients in $k$ (Theorem \claimref{synthesis.division-gives-the-rationals}), with blades $e_{S}$, the images of the group $G$ of signed directions. Let $x \mapsto x^{\dagger}$ be the linear extension of the inverse of $G$, $e_{S}^{\dagger} = e_{S}^{-1}$. An \emph{observable} is an $x$ with $x^{\dagger} = x$ and $x^{2} = 1$. A \emph{state} is a $k$-linear $\omega : \Cl_{k}(p,q) \to k$ with $\omega(1) = 1$ and $\omega(xx^{\dagger}) \ge 0$ for all $x$; examples are $\omega_{\rho}(x) = \langle\rho x\rangle_{0}/\langle\rho\rangle_{0}$ for $\rho = \sum_{r}y_{r}y_{r}^{\dagger} \ne 0$. Let $A_{1}, A_{2}, B_{1}, B_{2}$ be observables with $A_{i}B_{j} = B_{j}A_{i}$ for all $i, j$, and
\[
C = A_{1}(B_{1} + B_{2}) + A_{2}(B_{1} - B_{2}), \qquad X = [A_{1},A_{2}], \quad Y = [B_{1},B_{2}], \quad S_{A} = A_{1}A_{2} + A_{2}A_{1}, \quad S_{B} = B_{1}B_{2} + B_{2}B_{1} .
\]
\begin{enumerate}
\item[(i)] \emph{(Square and certificate; proved, the first identity classical.)} $C^{\dagger} = C$, $C^{2} = 4 - XY$, and with $Z = X - Y$
\[
8 - C^{2} = \tfrac12\bigl(Z^{\dagger}Z + S_{A}^{2} + S_{B}^{2}\bigr) ,
\]
an identity with rational coefficients in which $S_{A}$, $S_{B}$ are self-adjoint.
\item[(ii)] \emph{(The bound; proved.)} $\langle x^{\dagger}x\rangle_{0}$ is the sum of the squares of the coefficients of $x$, so $\omega_{\rho}$ is a state. For every state
\[
\omega(C)^{2} \le \omega(C^{2}) = 8 - \tfrac12\omega(Z^{\dagger}Z) - \tfrac12\omega(S_{A}^{2}) - \tfrac12\omega(S_{B}^{2}) \le 8, \qquad \bigl(\omega(C^{2}) - 4\bigr)^{2} \le \omega(4 - S_{A}^{2})\,\omega(4 - S_{B}^{2}) .
\]
If $2$ is not a square in $k$ (as for $k = \Q$) then $\omega(C)^{2} < 8$. If $\omega(C)^{2} = 8$ then $\omega(S_{A}^{2}) = \omega(S_{B}^{2}) = \omega(Z^{\dagger}Z) = 0$. If $A_{1}A_{2} = A_{2}A_{1}$ or $B_{1}B_{2} = B_{2}B_{1}$ then $C^{2} = 4$ and $\omega(C)^{2} \le 4$.
\item[(iii)] \emph{(Self-adjointness is needed; proved by an example.)} In $\Cl_{\Q}(2,2)$ with the notation of (iv), $A = \tfrac{17}{8}e_{1} + \tfrac{15}{8}f_{1}$ has $A^{2} = 1$ and $A^{\dagger} \ne A$, it commutes with the observable $p_{2}$, and for $A_{1} = A_{2} = A$, $B_{1} = B_{2} = p_{2}$ the state $\omega_{\rho}$, $\rho = \tfrac14(1 + e_{1})(1 + p_{2})$, has $\omega_{\rho}(C) = \tfrac{17}{4} > 4$, while $C^{2} = 4$. So square one and commutation alone give no bound on values, not even the bound $4$.
\item[(iv)] \emph{(Two subsystems and the twist; proved.)} Let $\Cl_{k}(2,2)$ have generators $e_{1}, f_{1}, e_{2}, f_{2}$ with $Q(e_{j}) = 1$, $Q(f_{j}) = -1$ and mode parities $p_{j} = f_{j}e_{j}$, as in Theorem \claimref{synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product}. The adjoint fixes $e_{j}$ and negates $f_{j}$; the self-adjoint elements of the sub-Clifford algebra of mode $j$ are spanned by $1, e_{j}, p_{j}$, and its observables are $\pm 1$ and the \emph{directions} $xe_{j} + zp_{j}$, $x^{2} + z^{2} = 1$. The directions of mode $1$ and of mode $2$ do not commute ($e_{1}e_{2} = -e_{2}e_{1}$, and $e_{1}e_{2}$ is not self-adjoint), so the two sub-Clifford algebras are not two parties. The parties are mode $1$ and the twisted copy of mode $2$ of clause (ii) of that Theorem: party $A$ has the directions $a = xe_{1} + zp_{1}$ and party $B$ the directions $b = x\,e_{2}p_{1} + z\,p_{2}$. These commute, and for directions $a_{1}, a_{2}$ of $A$ and $b_{1}, b_{2}$ of $B$, with $a_{1} \cdot a_{2} = x_{1}x_{2} + z_{1}z_{2}$ and $a_{1} \wedge a_{2} = x_{1}z_{2} - z_{1}x_{2}$ (so $(a_{1} \cdot a_{2})^{2} + (a_{1} \wedge a_{2})^{2} = 1$),
\[
S_{A} = 2\,a_{1} \cdot a_{2}, \qquad C^{2} = 4 + 4\,(a_{1} \wedge a_{2})(b_{1} \wedge b_{2})\,K, \qquad K = e_{1}f_{2}, \quad K^{\dagger} = K, \quad K^{2} = 1, \quad KC = CK .
\]
Hence $\omega(C)^{2} \le 4 + 4\,|a_{1} \wedge a_{2}|\,|b_{1} \wedge b_{2}|$ for every state, and the value $8$ of $\omega(C^{2})$ requires $a_{1} \cdot a_{2} = b_{1} \cdot b_{2} = 0$: each party's two directions anticommute. For directions this is forced, not one maximiser among several.
\item[(v)] \emph{(The saturating state; proved.)} At $A_{1} = e_{1}$, $A_{2} = p_{1}$, $B_{1} = e_{2}p_{1}$, $B_{2} = p_{2}$: $C = e_{2}f_{1} + e_{1}p_{2} + e_{2} - p_{1}p_{2}$, $C^{2} = 4(1 + K)$, $KC = C$, $C^{3} = 8C$. If $k$ contains $\sqrt{2}$,
\[
P = \tfrac14(1 + K) + \tfrac{\sqrt{2}}{8}\,C
\]
satisfies $P^{\dagger} = P = P^{2}$, $CP = 2\sqrt{2}\,P$, $\langle P\rangle_{0} = \tfrac14$ and $PxP = 4\langle Px\rangle_{0}P$ for every $x$; $\omega_{P}(x) = 4\langle Px\rangle_{0}$ is a state with $\omega_{P}(C) = 2\sqrt{2}$, and every state with that value at these settings agrees with $\omega_{P}$ on all self-adjoint elements (so it is $\omega_{P}$ if states are required to satisfy $\omega(x^{\dagger}) = \omega(x)$). Its projection onto the blades of mode $1$ is $\tfrac14$ (reduced state $\tfrac12$). $P$ does not commute with the total parity $p_{1}p_{2}$, and its projection onto the blades of mode $2$ is $\tfrac14 + \tfrac{\sqrt{2}}{8}e_{2}$, which by clause (iii) of that Theorem is not the reduction of the twisted split. Only $\sqrt{2}$ is adjoined: completeness of the coefficients is not used.
\end{enumerate}

## technical
The Clauser-Horne-Shimony-Holt combination of four two-valued quantities, two for each of two parties, is bounded by $2\sqrt{2}$ in quantum theory (Tsirelson's bound), by $2$ for quantities that commute, and by $4$ on general grounds. This result places the first of these inside the Clifford algebra that the foundation postulates of the series produce, with rational coefficients. The quantities are self-adjoint elements of square one, where the adjoint is the inverse on the group of signed directions extended linearly, and a party's quantities commute with the other party's. The square of the combination is $4$ minus the product of the two commutators (Landau's identity), and $8$ minus that square is one half of a sum of three squares with rational coefficients. A value assignment that is linear, normalised and non-negative on squares $xx^{\dagger}$ therefore gives the combination a squared value of at most $8$, and over the rationals strictly less. Nothing beyond the algebra and this definition of a value assignment is used: positivity of the scalar part is a theorem of the blade basis, and no completion of the coefficients enters. The definition itself, that measured correlations are values of such a functional, is not derived here; it is the single measurement premise of the statement. Self-adjointness cannot be dropped: an element of square one that mixes a direction of positive square with one of negative square has values above $1$, and an explicit rational example gives the combination the value $17/4$.

For two modes of the split-signature algebra the parties are one mode and the Klein-twisted copy of the other, since the untwisted sub-Clifford algebras anticommute on odd elements. Each party's quantities are then the unit directions of a plane, the squared combination is $4 + 4(a_{1} \wedge a_{2})(b_{1} \wedge b_{2})K$ with $K$ a self-adjoint blade of square one, and the value $8$ needs both parties' directions to anticommute. At anticommuting directions the state reaching $2\sqrt{2}$ is a single element of the algebra with coefficients in the rationals extended by $\sqrt{2}$, a primitive idempotent, and every state with that value has the same values on self-adjoint elements. It is not invariant under the total parity, so for these one-mode directions the stored caveat on the reduction of states that are not even applies to it.

## lay
Two experimenters each choose between two yes-or-no measurements on their half of a shared system, and a particular combination of the four possible correlations is formed. If the world were made of pre-existing answers the combination could not exceed 2; quantum theory allows up to about 2.83 (2 times the square root of 2) and no more. That limit is a known theorem from 1980. What is done here is to place it inside the algebra of directions that the series builds from its simplest assumptions (a yes-no bit, the least possible dependence on order, and whole-number addition), using only fractions. The limit comes out as a single algebraic identity: 8 minus the square of the combination is a sum of squares, so it can never be negative. The one thing that has to be assumed in addition is what it means to assign values to measurements, namely that averages are taken in a way that never gives a square a negative average. The result also shows that the limit is reached only when each experimenter's two measurements are as incompatible as possible, that it fails outright for quantities that are not of the allowed kind, and it writes down the one shared state that reaches the limit, which needs the square root of 2 and nothing more.

## one-liner
In the rational Clifford algebra of the foundation, commuting self-adjoint elements of square one give $8 - C^{2} = \tfrac12(Z^{\dagger}Z + S_{A}^{2} + S_{B}^{2})$, so every linear normalised functional non-negative on $xx^{\dagger}$ has $\omega(C)^{2} \le 8$ (strictly over $\Q$); for one mode and the Klein-twisted other mode of $\Cl(2,2)$, $C^{2} = 4 + 4(a_{1} \wedge a_{2})(b_{1} \wedge b_{2})e_{1}f_{2}$, the value $8$ forces anticommuting directions, and the saturating state, unique on self-adjoint elements, is $\tfrac14(1 + e_{1}f_{2}) + \tfrac{\sqrt{2}}{8}C$; without self-adjointness the value $\tfrac{17}{4}$ occurs.
