---
id: std-algebra.complex-clifford-algebra
kind: claim
version: 3
title: The complex Clifford algebra, its classification modulo 2, its Fock model and its pairing
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- clifford-classification
- spinor-modules
- car-algebra
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle (U1 to U6)
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
about:
- obj.std-algebra.clifford-algebra
- obj.std-algebra.minimal-left-ideal
- obj.std-algebra.witt-index
derivations:
- name: main
  uses:
  - std-algebra.existence-uniqueness@1
  - std-algebra.blade-basis@1
  - std-algebra.polarisation@1
  - std-algebra.witt-basis-car@1
  - std-algebra.fock-representation@1
  - std-algebra.chevalley-pairing@1
  - std-algebra.involution-properties@1
  - std-algebra.even-subalgebra-isomorphism@1
  - std-algebra.complexification@2
  - primer.centre@2
  - primer.sign@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_orthogonal_basis_and_witt_basis
- kind: check
  ref: check.py::check_fock_model_is_the_whole_matrix_algebra
- kind: check
  ref: check.py::check_vacuum_idempotent_and_minimal_left_ideal
- kind: check
  ref: check.py::check_odd_dimension_splits
- kind: check
  ref: check.py::check_complex_chevalley_pairing
- kind: check
  ref: check.py::check_ascended_witt_basis
- kind: check
  ref: check.py::check_blade_basis_for_a_degenerate_complex_form
locators:
  sources:
  - key: Chevalley1954
    locator: Ch. II and III (Clifford algebras over a field; spinors, pure spinors)
  - key: LawsonMichelsohn1989
    locator: Ch. I, Sections 4 and 5 (complex Clifford algebras and their representations)
  - key: Lounesto2001
    locator: Ch. 18 (scalar products of spinors)
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle the abstract complex field of a complex quadratic space is read as span{1, I_4} (U1), its unit acting as a ground-field scalar: w_j, omega_C, e_j -> I_4 e_j e_n and the proof''s computations are written with I_4; the concrete complexification Cl(2,4) (x) C of (v) is Cl(3,4) with the central unit I_7 (U3, std-algebra.complexification-is-the-odd-extension), so w_3 = b_3 + I_7 b_4; the entity says once which unit acts where and that the isomorphism with Cl_6(C) relates them without identifying them; the outside_ga declaration is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (other): the result is about Clifford algebras of complex quadratic spaces, whose scalar i (in w_j = (e_{2j-1} + i e_{2j})/2, omega_C, e_j -> i e_j e_n) commutes with every vector, which no pseudoscalar does.'
  open_problem: op.complex-clifford
---

## formal
A \emph{complex quadratic space} is a complex vector space $V$ of dimension $n$ with a quadratic form $Q : V \to \C$ whose polar form $B$ is $\C$-bilinear. Its Clifford algebra $\Cl(V, Q)$ is defined by the universal property of \claimref{obj.std-algebra.clifford-algebra} with ``real'' replaced by ``complex'' throughout (complex unital algebras, $\C$-linear maps). The complex field is read, as the store reads the scalars of an abstract complex space, as $\mathrm{span}\{1, I_4\}$ (conventions, the unit principle, U1): $V$ is a vector space over that field, and its unit $I_4$ acts on $V$ and on $\Cl(V, Q)$ as a scalar, central by construction, not as a product of vectors of $V$. Where the complex space is the complexification of a real one of even dimension, the scalar is realised inside a real Clifford algebra as the central pseudoscalar of the odd extension (\claimref{std-algebra.complexification-is-the-odd-extension}); in (v), $\Cl(2,4) \otimes \C = \Cl(3,4)$ with scalars $\mathrm{span}\{1, I_7\}$, the isomorphism with $\Cl_6(\C)$ carrying the abstract scalar $I_4$ to $I_7$ (the two are related by that isomorphism and not identified).
\begin{enumerate}
\item[(i)] $\Cl(V, Q)$ exists and is unique up to unique isomorphism; for any basis of $V$ the $2^{n}$ increasing products form a $\C$-basis, degenerate forms included; the grade involution, reversion and the $\Z_2$-grading are as in the real case. For a real quadratic space $(V_\R, Q_\R)$, $\Cl(V_\R, Q_\R) \otimes_\R \C \cong \Cl(V_\R \otimes \C, Q_\C)$.
\item[(ii)] If $Q$ is nondegenerate, $V$ has a basis with $Q(e_i) = 1$ and $B(e_i, e_j) = 0$ for $i \ne j$. So $(V, Q) \cong (\C^{n}, \sum_i z_i^{2})$ and $\Cl(V, Q) \cong \Cl_n(\C)$ depends only on $n$.
\item[(iii)] Let $Q$ be nondegenerate and $n = 2k$. Every totally null subspace has dimension at most $k$. For every totally null $W$ of dimension $k$ (for instance $w_j = \tfrac12(e_{2j-1} + I_4\, e_{2j})$) there is a totally null $W'$ with bases $w_j \in W$, $v_j \in W'$ such that $B(v_i, w_j) = \tfrac12 \delta_{ij}$, and $V = W \oplus W'$. Letting $w \in W$ act on $\Lambda W$ by $w \wedge{}$ and $v \in W'$ by the contraction $\iota_{2B(v, \cdot)}$ gives an isomorphism $\Cl(V, Q) \cong \End_\C(\Lambda W) \cong \Mat_{2^{k}}(\C)$; $f = v_1 w_1 \cdots v_k w_k$ is a primitive idempotent and $\Cl(V, Q) f \cong \Lambda W$ is a minimal left ideal with basis $w_I f$. Vectors act oddly, and $\Cl^{+}(V, Q) \cong \End(\Lambda^{\mathrm{even}} W) \oplus \End(\Lambda^{\mathrm{odd}} W)$: the two half-spinor modules, each of dimension $2^{k-1}$.
\item[(iv)] Let $Q$ be nondegenerate and $n = 2k + 1$. Then $\omega_\C = I_4^{\,n(n-1)/2} e_1 \cdots e_n$ is central with $\omega_\C^{2} = 1$, $P_\pm = \tfrac12(1 \pm \omega_\C)$ split $\Cl = \Cl P_+ \oplus \Cl P_-$ as algebras, $a \mapsto a P_\pm$ maps $\Cl^{+}$ isomorphically onto $\Cl P_\pm$, and $e_j \mapsto I_4\, e_j e_n$ ($j < n$) gives $\Cl_{2k}(\C) \cong \Cl^{+}$. These are the types stated in part (i) of \claimref{std-algebra.complexification}, now with $\Cl$ over $\C$ defined directly. Hence
\begin{equation}
\Cl_{2k}(\C) \cong \Mat_{2^{k}}(\C), \qquad \Cl_{2k+1}(\C) \cong \Mat_{2^{k}}(\C) \oplus \Mat_{2^{k}}(\C), \qquad \Cl_{n+2}(\C) \cong \Mat_2(\Cl_n(\C)).
\end{equation}
\item[(v)] In the Fock model of (iii), with $\tau$ the reversal of $\Lambda W$ and $\operatorname{top}$ the coefficient of $w_1 \wedge \dots \wedge w_k$, the $\C$-bilinear form $\beta(x, y) = \operatorname{top}(\tau x \wedge y)$ is nondegenerate, pairs $\Lambda^{m} W$ only with $\Lambda^{k-m} W$, satisfies $\beta(y, x) = (-1)^{k(k-1)/2} \beta(x, y)$ and $\beta(a x, y) = \beta(x, \tilde a y)$ for every $a \in \Cl(V, Q)$. So every complex bivector $A$ is skew, $\beta(Ax, y) + \beta(x, Ay) = 0$, and every $R$ with $\tilde R R = 1$ preserves $\beta$. For $k = 3$ ($\Cl_6(\C) \cong \Cl(2,4) \otimes \C$) the pairing is antisymmetric and pairs $\Lambda^{\mathrm{even}} W$ perfectly with $\Lambda^{\mathrm{odd}} W$.
\end{enumerate}

## technical
The Clifford algebra of a complex quadratic space is built and behaves exactly as the real one, because the real constructions never used anything about the real numbers beyond their being a field in which 2 is invertible. Over the complex numbers every nondegenerate form has an orthonormal basis, so only the dimension matters. In even dimension the space splits into two complementary totally null halves, and wedge and contraction on the exterior algebra of one half make the whole algebra a full complex matrix algebra, the Fock model, whose vacuum idempotent generates the spinor space inside the algebra. In odd dimension a normalised volume element splits the algebra into two copies. The reversal-and-top-degree pairing on the Fock space is complex bilinear, makes every vector self-adjoint, and in six dimensions pairs the two chiralities antisymmetrically.

## lay
Allowing complex coefficients erases the difference between space-like and time-like directions, so the algebra depends only on the number of dimensions: a single complex matrix algebra in even dimension and a pair of them in odd dimension. In even dimension the matrix algebra is the algebra of creation and annihilation operators of fermion modes, and the states carry a pairing that every rotation respects.

## one-liner
$\Cl(V_\C)$ has a blade basis and only depends on $n$: $\Cl_{2k}(\C) \cong \End(\Lambda W) \cong \Mat_{2^{k}}(\C)$ on any maximal totally null $W$, $\Cl_{2k+1}(\C) \cong \Mat_{2^{k}}(\C)^{\oplus 2}$; $\operatorname{top}(\tau x \wedge y)$ is a $\C$-bilinear invariant pairing, antisymmetric for $k = 3$.
