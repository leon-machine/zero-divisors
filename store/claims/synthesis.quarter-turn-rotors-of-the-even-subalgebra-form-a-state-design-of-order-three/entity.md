---
id: synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three
kind: claim
version: 1
title: Quarter turns about blades of square -1 give a state design of order three when I^2 = -1
status: proved
region: synthesis
subject: entropy
tags: [rotors-and-stabilisers, pseudoscalar-and-centre, entanglement, finite-models, classical-theorem]
proposed_by:
  kind: ai
  session: 2026-11-09-bridges
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-09-bridges
review: draft
derivations:
- name: main
  uses:
  - synthesis.signed-directions-and-the-integer-clifford-algebra@2
  - synthesis.imported-haar-moments-of-random-pure-state@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_group_is_finite_and_transitive_on_classes_and_commuting_pairs
- kind: check
  ref: check.py::check_two_identities_of_a_state
- kind: check
  ref: check.py::check_moments_to_order_three_equal_the_invariant_ones
- kind: check
  ref: check.py::check_mean_purity_of_a_matrix_factor_is_the_imported_value
- kind: check
  ref: check.py::check_generators_are_rotors_only_for_bivector_blades
- kind: check
  ref: check.py::check_invariant_mixtures_and_the_parity_sector_corollary
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.signed-directions-and-the-integer-clifford-algebra
  - synthesis.imported-haar-moments-of-random-pure-state
extraction:
  open_problem: op.island-dictionary
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'The imported mean-purity Fact (former id synthesis.imported-haar-average-purity) is retired in favour of clause (v) of this result (decision 2 of 9 November 2026), which gives the value at dimensions that are powers of two only; for general m, n the classical value (Lubkin 1978) is the n = 2 case of the imported all-moment Fact, and the comparison of clause (v), the premise edge, the check and the cross-reference to the finite-averages result now point there. Version kept: the entity was accepted in the same pass.'
  note: >-
    Cross-subject link of 9 November 2026 (clifford-structure to entropy, no edge before): whether averages over the
    finite group attached to the group of signed directions reproduce the moments of the invariant measure that the
    entropy comparisons import. Result: yes to order three, by a finite sum, for every even subalgebra whose
    pseudoscalar squares to -1 (so that the complex unit is the pseudoscalar and every generator is a real element 1 + k of the algebra, a rotor for 2N <= 6).
    Which stored results need which moments: the Renyi-two comparison
    (synthesis.eviction-keeps-one-replica-saddle, clauses (iii) and (iv)) needs the second moment only, at
    dimensions that are powers of two, and clause (v) here gives that number as a finite average; the comparison at
    every Renyi index (synthesis.eviction-keeps-one-of-catalan-many-replica-saddles, clause (iii)) needs every
    moment and is reached here at indices two and three only; Page's mean entropy
    (singularity.imported-page-average-entropy-subsystem) needs all moments and is not reached. Nothing is claimed
    here at order four or beyond, and nothing about the even part of a subset of the generators (a set of modes
    under the parity superselection), which is not a matrix factor of the even subalgebra. Decision of 9 November 2026: the imported mean-purity Fact is retired in favour of this result (at powers of two; for general m, n the classical value of Lubkin 1978 stays prior art, stated as the n = 2 case of synthesis.imported-haar-moments-of-random-pure-state). Which
    dependants can cite it: synthesis.eviction-keeps-one-replica-saddle clause (iv) (the crossing, radiation
    dimension a power of two) and clause (iii) restricted to m, n powers of two; clause (iii) as stored, for all
    m and n, cannot, and neither can any comparison at Renyi index four or above or Page's mean entropy. Overlap:
    the agreement at orders two and three in
    synthesis.finite-normaliser-averages-leave-the-haar-moments-at-order-four-and-on-a-parity-sector is the
    blade-state case of clause (iii) here, and that result cites this one for it; the parity-sector
    corollary after (iii) is the same number as that result's. The statement applies as it stands to the slot
    module's ten generators (Cl(10,0), D = 16, the unit the volume element), where the bivector quarter turns
    alone have the two orbits 45 and 210 on classes and the design needs the grade-six generators as well.
    Prior art, cited from memory and not checked against the sources: the normaliser of the extraspecial group
    (the Clifford group of quantum information) is a unitary design of order three for qubits (Webb 2016; Zhu
    2017) and its orbit of stabiliser states a state design of order three (Kueng and Gross 2015). New here: the
    proof inside the even subalgebra, from sign flips, transvections and the idempotent identity alone, with no
    representation theory; every generator is a real element 1 + k of the algebra, a rotor for 2N <= 6; and the moments are derived for every invariant measure, so the imported formula is a cross-check. Transport-absent: finite group
    theory of the algebra.
outside_ga:
  kind: bridge
  why: 'Clauses (i) to (iii) and the factor purity of clause (v) are statements in the even subalgebra with the pseudoscalar as unit. Clause (iv) and the last sentence of (v) compare them with imported Facts that are stated for an abstract Hilbert space and the invariant measure on its unit sphere; the comparison needs the identification of the even subalgebra with the matrices over span{1, I} acting on that space, which is written in matrix language to match the imports.'
---

## formal
Let $\Cl(p,q)$ have $p + q = 2N \ge 4$ generators $e_{1}, \dots, e_{2N}$ with $N + q$ odd, so that the pseudoscalar $I = e_{1}\cdots e_{2N}$ has $I^{2} = -1$ ($\Cl(1,3)$, $\Cl(3,1)$, $\Cl(6,0)$, $\Cl(7,1)$ are examples); $I$ commutes with the even subalgebra $E$. Put $D = 2^{N-1}$. Call two even blades $e_{S}$, $e_{T}$ (notation of \claimref{synthesis.signed-directions-and-the-integer-clifford-algebra}) equivalent when $T = S$ or $T$ is the complement of $S$; since $Ie_{S} = \pm e_{S^{c}}$ and $(Ie_{S})^{2} = -e_{S}^{2}$, each class $c$ contains, up to sign, exactly one element $h_{c}$ of square $+1$, its \emph{unit}; $h_{0} = 1$. The classes form the $\mathbb{F}_{2}$-space $V$ of even subsets modulo the full set, of dimension $2N - 2$, with $D^{2}$ elements, and $b(c,d) \in \mathbb{F}_{2}$, equal to $1$ exactly when $h_{c}$ and $h_{d}$ anticommute, is the polar form of that theorem restricted to even subsets; it is alternating and nondegenerate on $V$. The $h_{c}$ and $Ih_{c}$ form a basis of $E$; $h_{c}h_{d} = \pm h_{c+d}$ when $b(c,d) = 0$ and $\pm Ih_{c+d}$ when $b(c,d) = 1$; for $b(c,d) = 0$, $c \ne d$, write $h_{c}h_{d} = \epsilon(c,d)h_{c+d}$. A \emph{state} is an idempotent $\rho = D^{-1}\bigl(1 + \sum_{c \ne 0}x_{c}h_{c}\bigr)$ of $E$ with rational or real coordinates $x_{c} = D\langle\rho h_{c}\rangle_{0}$. Let $\Gamma$ be the group of automorphisms of $E$ generated by the conjugations by the \emph{quarter-turn elements} $R_{c} = 1 + k_{c}$, $k_{c} = Ih_{c}$ a blade with $k_{c}^{2} = -1$, $c \ne 0$ (unnormalised; $R_{c}^{-1} = \tfrac12(1 - k_{c})$), and for a function $f$ of states let $\langle f\rangle_{\Gamma}(\rho)$ be the mean of $f(g\rho g^{-1})$ over $g \in \Gamma$.
\begin{enumerate}
\item[(i)] \emph{(The group; proved, the two orders computed.)} Conjugation by $R_{c}$ fixes $I$ and $h_{d}$ when $b(c,d) = 0$ and sends $h_{d}$ to $-Ih_{d}h_{c} = \pm h_{c+d}$ when $b(c,d) = 1$: on $V$ it is the transvection $d \mapsto d + b(c,d)c$. $\Gamma$ is finite, contains the conjugation by every $h_{c}$ (which is $R_{c}^{2}$ up to the central factor $2I$), carries states to states, and acts transitively on the nonzero classes and on the ordered pairs $(c,d)$ of distinct nonzero classes with $b(c,d) = 0$. For $N = 2$ it has order $24$ (in $\Cl(1,3)$ the $R_{c}$ are $1$ plus the spatial bivectors and $\Gamma$ is the rotation group of the cube acting on the relative vectors) and for $\Cl(6,0)$ order $11520$ (both computed; they equal $2^{2N-2}$, the sign flips, times the order of the symplectic group of $V$, given the classical theorem, not used here, that transvections generate it). $R_{c}$ is a rotor exactly when $k_{c}$ is a bivector: every generator for $2N \le 6$ ($\Cl(1,3)$, $\Cl(3,1)$, $\Cl(6,0)$). For $2N \ge 8$ the generators include blades of grade $4$ or $6$, which are not versors, and for grade $4$ ($\Cl(7,1)$: $35$ of $63$) $R_{c}\tilde R_{c} = 2k_{c}$ is not a scalar; the bivector rotors alone are not transitive on the classes ($\Cl(7,1)$: orbits $7$, $21$, $35$; $\Cl(10,0)$: $45$, $210$; computed) and are not a design. The statement is for signatures with $I^{2} = -1$, where the unit of the averages is the pseudoscalar.
\item[(ii)] \emph{(Two identities of a state; proved.)} $\sum_{c \ne 0}x_{c}^{2} = D - 1$, and for every $u \ne 0$, $\sum\epsilon(c,d)x_{c}x_{d} = (D - 2)x_{u}$, the sum over the $\tfrac12D^{2} - 2$ ordered pairs of nonzero classes with $c + d = u$ and $b(c,d) = 0$.
\item[(iii)] \emph{(Moments to order three; proved.)} For every state and all nonzero classes $c, d, e$:
\[
\langle x_{c}\rangle_{\Gamma} = 0, \qquad \langle x_{c}x_{d}\rangle_{\Gamma} = \frac{\delta_{cd}}{D + 1}, \qquad \langle x_{c}x_{d}x_{e}\rangle_{\Gamma} = \begin{cases}\dfrac{2\,\epsilon(c,d)}{(D + 1)(D + 2)} & e = c + d,\ c \ne d,\ b(c,d) = 0,\\[1ex] 0 & \text{otherwise.}\end{cases}
\]
The values do not depend on the state averaged. \emph{Corollary (a set of modes on a parity sector).} For a proper subset $A$ of $2a$ of the generators the even blades of $A$ are $\tfrac12 d_{A}^{2}$ distinct classes, $d_{A} = 2^{a}$, and the purity of a state on the even part of $A$ is $d_{A}^{-1}\sum x_{c}^{2}$ over them; by the second moment its mean is $d_{A}^{-1}\bigl(1 + (\tfrac12 d_{A}^{2} - 1)/(D + 1)\bigr) = (d_{A} + d_{B})/(d_{A}d_{B} + 2)$ with $d_{A}d_{B} = 2D$: $\tfrac23$ at four generators. It follows from (iii) and not from (v).
\item[(iv)] \emph{(Every invariant measure to order three; proved; the imported Fact is a cross-check.)} Since the $\Gamma$-mean of every monomial of degree at most three is the same number for every state, every probability measure on states that is invariant under $\Gamma$ has the moments of (iii): its moment is the integral of the $\Gamma$-mean. The unitarily invariant measure is one such measure, so for $D$ a power of two its moments to order three are derived here. Identify $E$ with the $D \times D$ matrices over $\mathrm{span}\{1, I\}$, the $h_{c}$ Hermitian of square one and trace $D\langle h_{c}\rangle_{0}$, a state with $\ket{\psi}\bra{\psi}$, $x_{c} = \bra{\psi}h_{c}\ket{\psi}$. The values of (iii) are those that Fact \claimref{synthesis.imported-haar-moments-of-random-pure-state} gives for $n \le 3$, $\sum_{\sigma}\operatorname{Tr}\bigl(P_{\sigma}\,h_{c}\otimes h_{d}\otimes h_{e}\bigr)/(D(D+1)(D+2))$ and its analogue with two factors. Since the monomials of degree at most three in the $x_{c}$ span the polynomials of degree at most three in $\ket{\psi}\bra{\psi}$, the $\Gamma$-orbit of every state is a design of order three: the mean of $(\ket{\psi}\bra{\psi})^{\otimes n}$ over the orbit is the invariant mean for $n = 1, 2, 3$. Each $\Gamma$-orbit is itself such a measure. No statement is made at order four.
\item[(v)] \emph{(Mean purity of a matrix factor; proved.)} Let $W \subset V$ be a subspace of dimension $2r$ on which $b$ is nondegenerate, $m = 2^{r}$ and $n = D/m$; the $h_{c}$, $c \in W$, span over $\mathrm{span}\{1, I\}$ a subalgebra isomorphic to the $m \times m$ matrices, and the purity of a state on it is $P_{W} = m^{-1}\sum_{c \in W}x_{c}^{2}$ (with $x_{0} = 1$). Then for every state
\[
\langle P_{W}\rangle_{\Gamma} = \frac1m\Bigl(1 + \frac{m^{2} - 1}{D + 1}\Bigr) = \frac{m + n}{mn + 1},
\]
the mean purity of the unitarily invariant measure on $\C^{m}\otimes\C^{n}$ by (iv), the value that Fact \claimref{synthesis.imported-haar-moments-of-random-pure-state} states at $n = 2$ (Lubkin's mean purity, there imported for all dimensions), here a finite sum, for dimensions $m$, $n$ that are powers of two and for no others: a comparison stated for all $m$, $n$ can rest on this clause only where its dimensions are powers of two. The even blades of a proper subset of the generators do not form such a $W$ (they are $\tfrac12 m^{2}$ classes, not $m^{2}$), and their purity is not covered by this clause.
\end{enumerate}

## technical
The even subalgebra of a Clifford algebra with an even number $2N$ of generators and a pseudoscalar of square $-1$ is a complex matrix algebra whose imaginary unit is the pseudoscalar. Its even blades, taken up to that unit, are the Pauli operators of $N - 1$ qubits, and each has a version $k$ of square $-1$, so $1 + k$ is a real invertible element, a quarter turn about the blade $k$; it is a rotor exactly when $k$ is a bivector, which is every case up to six generators and not beyond. The conjugations by these elements form a finite group (the Clifford group of quantum information, modulo phases). The result is that averaging any pure state over this group gives the first three moments of every measure invariant under the group, the unitarily invariant one among them, with a proof that uses three facts only: conjugation by a blade flips signs, the quarter-turn elements act on the classes of blades as the transvections of a nondegenerate alternating form and so mix them transitively, and a pure state is an idempotent. The second moment gives Lubkin's mean purity $(m + n)/(mn + 1)$ for a matrix factor as a finite sum, for dimensions that are powers of two. Orders four and above, and the parity-superselected purity of a set of modes, are outside the statement.

## lay
Several entropy comparisons in the store borrow, from the literature, the average behaviour of a quantum state chosen completely at random. A completely random choice means an average over a continuous infinity of states. This result shows that for the quantities of second and third order, which include the average purity those comparisons use, the same numbers come out of an average over a finite list of states: the ones reached from any starting state by quarter turns about the blades of the algebra (rotations in planes when there are at most six generators). For two qubits the list has at most 11520 entries. The finite average is carried out inside the algebra the series already uses, with its own unit in place of the imaginary number. It reproduces the borrowed numbers exactly up to third order and makes no claim beyond that.

## one-liner
In an even subalgebra with $2N$ generators and $I^{2} = -1$, the finite group generated by the quarter-turn elements $1 + Ih_{c}$ (rotors for $2N \le 6$ only) averages every state to $\langle x_{c}x_{d}\rangle = \delta_{cd}/(D+1)$ and $\langle x_{c}x_{d}x_{c+d}\rangle = 2\epsilon/((D+1)(D+2))$, $D = 2^{N-1}$, the moments to order three of every measure invariant under the group, the unitarily invariant one among them, so the mean purity of a matrix factor is Lubkin's $(m+n)/(mn+1)$ by a finite sum; order four is not claimed.
