---
id: synthesis.central-limit-of-tower-fluctuation-states-with-the-kernel-unit
kind: claim
version: 1
title: Central limit of tower fluctuation states for product block states, with the kernel unit
status: proved
region: synthesis
subject: quantum-fields
tags: [bosonisation, car-algebra, ladder-pairs, limits]
proposed_by:
  kind: ai
  session: 2026-11-07-boson-items
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-07-boson-items
review: draft
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - std-algebra.witt-basis-car@1
  - synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum@1
  - field-theory.no-canonical-commutation-relations-tower@3
  - field-theory.how-close-tower-comes-ccr@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_graded_locality_reduces_collective_brackets_to_single_blocks
- kind: check
  ref: check.py::check_commutators_have_no_scalar_part_and_anticommutators_can
- kind: check
  ref: check.py::check_fluctuation_cumulants_scale_exactly_and_the_second_carries_the_form
- kind: check
  ref: check.py::check_the_extended_state_is_positive_blades_unitary_and_uncertainty_holds
- kind: check
  ref: check.py::check_polarised_fluctuations_tend_to_the_fock_vacuum
- kind: proof
  derivation: main
extraction:
  open_problem: bos.qclt-states
  note: >-
    Attack on the target bos.qclt-states (convergence of the fluctuation states, not only of their commutator),
    with clause (i) bearing on bos.spin-statistics. The stored result
    synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum proves that the commutator of
    fluctuations tends to the form sigma_omega in mean square and states that the convergence of the states is not
    claimed; it also notes that a Weyl form with self-adjoint fields needs a central unit, which the block's even
    algebra lacks. Here the unit is the kernel bivector J = g1 g2 of the tower level Cl(m, m + 2) (the companion
    proposal synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower establishes that J is the
    only even unit commuting with every transport generator; the facts used here, J^2 = -1, J* = -J and J commuting
    with the transport generators, are re-derived in the proof and checked). New to the store: (ii) the convergence of the
    fluctuation states for product block states: exact factorisation of Weyl characteristic functions over blocks,
    exact scaling N^{1 - k/2} of the ordered cumulants, an explicit error bound of order N^{-1/2} that is attained,
    and the identification of the limit as the quasi-free state of the Weyl algebra with the stored form sigma_omega
    (values in J R) and the symmetric covariance, positive, with the uncertainty relation (the Cushen-Hudson theorem
    for identical product blocks, written with the unit J, with an elementary explicit bound; rates for the quantum
    central limit theorem are in the literature); (iii) on the hopping pair the polarised blocks' limit is the Fock
    vacuum, with the exact finite-N moments (the ladder coefficient is the one of
    synthesis.ladder-states-are-locally-product-with-non-gaussian-fluctuations (i), equivalently of
    field-theory.how-close-tower-comes-ccr); (i) the collective bracket of the kind matching the
    parity reduces exactly to single-block brackets, so even fluctuations tend to canonical commutation and odd ones to
    canonical anticommutation relations in mean square, and the trace over span{1, J} forbids a canonical commutator
    of transport elements at finite N but not a canonical anticommutator (graded locality itself, the statement that
    odd elements on disjoint supports anticommute and other pairs commute, is clause (ii) of
    synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes, cited here and re-proved in one line). The companion proposal
    synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes treats the spin side (the turn
    exp(theta J L_s), spin as a datum of the modes, graded locality as the statistics); clause (i) here adds the limit
    of the brackets and the finite-N asymmetry and does not restate that result. Prior art, not premises: the quantum
    central limit theorem is C. D. Cushen and R. L. Hudson, A quantum-mechanical central limit theorem, J. Appl.
    Probab. 8 (1971) 454-469, and D. Goderis, A. Verbeure and P. Vets, Non-commutative central limits, Probab. Th.
    Rel. Fields 82 (1989) 527-544 (as cited in the fluctuation-forms result, the second's volume and pages not
    independently verified); the central limit for odd (anticommuting) elements is R. L. Hudson, A quantum-mechanical central limit theorem for
    anti-commuting observables, J. Appl. Probab. (1973) (located by search; volume and pages not verified); the additivity of cumulants of independent commuting families is the classical moment-cumulant relation.
    The product hypothesis is used at the first step of (ii). Not claimed: convergence for non-product (mixing) states, or any
    construction of gauge bosons. Ledger: transport-absent (finite CAR algebra of tower blocks with the kernel unit).
---

## formal
Let a tower level be $\Cl(m, m + 2)$ with kernel generators $g_{1}, g_{2}$, $Q(g_{1}) = Q(g_{2}) = -1$, and $m$ transport planes with generators $e_{j}, f_{j}$, $Q(e_{j}) = 1$, $Q(f_{j}) = -1$. Let $v_{j} = \tfrac12(e_{j} + f_{j})$, $w_{j} = \tfrac12(e_{j} - f_{j})$, the Witt pairs of Theorem \claimref{std-algebra.witt-basis-car} read with $v_{j}$ as creators and $w_{j}$ as annihilators, $n_{j} = v_{j}w_{j}$; $J = g_{1}g_{2}$; and $x \mapsto x^{*}$ reversion composed with a sign for each generator of negative square, so $v_{j}^{*} = w_{j}$ and $J^{*} = -J$. Let $\mathcal{T}$ be the algebra generated by the transport generators and $\mathcal{T}_{J} = \mathcal{T} + J\mathcal{T}$; $J^{2} = -1$ and $J$ commutes with $\mathcal{T}$, so $\mathrm{span}\{1, J\}$ is a field and $\mathcal{T}_{J}$ an algebra over it. A block is a set of two planes; $\mathcal{A}_{e}$ is the even algebra of a block. Let $\omega$ be a real state of a block ($\omega(x^{*}) = \omega(x)$), with density $\rho$, extended to $\mathcal{A}_{e} + J\mathcal{A}_{e}$ by $\omega(x) = 4(\br{\rho x}_{0} - J\br{J\rho x}_{0})$; $\omega_{N}$ is the product state on $N$ blocks, $x_{k}$ the copy of $x$ on block $k$, and $F_{N}(x) = N^{-1/2}\sum_{k}(x_{k} - \omega(x))$ as in Theorem \claimref{synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum}(vii).
\begin{enumerate}
\item[(i)] \emph{(Brackets of collective modes.)} For $x, y$ of definite parity in the algebra generated by one block's generators and $J$, with $[x, y]_{\epsilon} = xy - \epsilon yx$ and $\epsilon = -1$ when $x$ and $y$ are both odd, $\epsilon = 1$ otherwise,
\[
\Bigl[\sum_{k}x_{k}, \sum_{l}y_{l}\Bigr]_{\epsilon} = \sum_{k}[x_{k}, y_{k}]_{\epsilon}
\]
exactly, by graded locality (synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes (ii): odd elements on disjoint sets of planes anticommute, other pairs commute), while for odd $x$, $y$ the commutator of the sums keeps cross terms. For an even product state ($\omega(x) = 0$ for odd $x$), $[F_{N}(x), F_{N}(y)]_{\epsilon} = N^{-1}\sum_{k}C_{k}$, $C = [x, y]_{\epsilon}$, has mean $\omega(C)$ and variance $(\omega(C^{*}C) - \omega(C^{*})\omega(C))/N$: even fluctuations obey canonical commutation relations and odd ones canonical anticommutation relations as $N \to \infty$, in mean square. The trace $\mathrm{tr}(x) = \br{x}_{0} - J\br{Jx}_{0}$ over $\mathrm{span}\{1, J\}$ is cyclic on $\mathcal{T}_{J}$ with $\mathrm{tr}(\alpha + \beta J) = \alpha + \beta J$, so no commutator of elements of $\mathcal{T}_{J}$ equals a nonzero element of $\mathrm{span}\{1, J\}$ (in the whole level $J = \tfrac12[g_{1}, g_{2}]$ is a commutator), while $\{w_{j}, v_{j}\} = 1$: the odd bracket can be canonical at finite $N$, the even one only in the limit.
\item[(ii)] \emph{(Central limit of the fluctuation states.)} The extension of $\omega$ is positive. For self-adjoint $x \in \mathcal{A}_{e} + J\mathcal{A}_{e}$ let $W_{N}(x) = \exp(JF_{N}(x))$, a unitary. For self-adjoint $x_{1}, \dots, x_{r}$ with $y_{j} = x_{j} - \omega(x_{j})$:
\begin{enumerate}
\item[(a)] $\omega_{N}(W_{N}(x_{1})\cdots W_{N}(x_{r})) = \bigl[\omega(e^{Jy_{1}/\sqrt N}\cdots e^{Jy_{r}/\sqrt N})\bigr]^{N}$;
\item[(b)] the ordered cumulants of the fluctuations (the moment-cumulant relation over set partitions, each part multiplied in its original order) satisfy $\kappa(F_{N}(x_{j_{1}}), \dots, F_{N}(x_{j_{k}})) = N^{1 - k/2}\kappa(y_{j_{1}}, \dots, y_{j_{k}})$ for $k \ge 2$, with first cumulants $0$;
\item[(c)] with $c = \tfrac12\omega\bigl((\sum_{j}y_{j})^{2}\bigr) + \tfrac12\sum_{j < l}\omega([y_{j}, y_{l}])$, $\|x\|_{1}$ the sum of the absolute values of the blade coefficients of $x$, $\nu = \sum_{j}\|y_{j}\|_{1}$, and $|a + bJ| = (a^{2} + b^{2})^{1/2}$,
\[
\bigl|\omega_{N}(W_{N}(x_{1})\cdots W_{N}(x_{r})) - e^{-c}\bigr| \le \frac{\nu^{3}}{6}e^{\nu/\sqrt N}N^{-1/2} + \frac{\nu^{4}}{8}e^{\nu^{2}/2N}N^{-1} ;
\]
\item[(d)] $e^{-c}$ is the value on $W(x_{1})\cdots W(x_{r})$ of the quasi-free state $\omega_{\infty}(W(x)) = e^{-s(x, x)/2}$ of the Weyl algebra $W(x)W(y) = e^{-\sigma_{\omega}(x, y)/2}W(x + y)$ with unit $J$, covariance $s(x, y) = \tfrac12\omega(\{y_{x}, y_{y}\})$, real, and symplectic form the stored fluctuation form $\sigma_{\omega}(x, y) = \omega([x, y])$, here with values in $J\R$; $\omega_{\infty}$ is positive and $|\sigma_{\omega}(x, y)|^{2} \le 4s(x, x)s(y, y)$. For the hopping fields $\phi = b + b^{*}$, $\pi = J(b^{*} - b)$ of $b = v_{1}w_{2}$ in the product state with occupations $p_{1}, p_{2}$, $s(\phi, \phi) = s(\pi, \pi) = p_{1} + p_{2} - 2p_{1}p_{2}$ and $\sigma_{\omega}(\phi, \pi) = 2J(p_{1} - p_{2})$, while for a real state $\sigma_{\omega}$ vanishes on pairs of self-adjoint elements of $\mathcal{A}_{e}$ (the stored result): the unit $J$ is what gives self-adjoint fields a nonzero form. The rate $N^{-1/2}$ is attained: $\kappa(n_{1}, n_{1}, n_{1}) = p_{1}(1 - p_{1})(1 - 2p_{1})$.
\end{enumerate}
\item[(iii)] \emph{(Polarised blocks: the Fock vacuum.)} In the polarised product state ($p_{1} = 1$, $p_{2} = 0$ on every block), with $B = N^{-1/2}\sum_{k}b_{k}$, $\omega_{N}(B^{k}B^{*k}) = k!\prod_{l < k}(1 - l/N)$ and $\omega_{N}(B^{*k}B^{k}) = 0$; the third cumulant of $F_{N}(\phi)$ is $0$ and the fourth is $-2/N$; the uncertainty bound of (ii)(d) is an equality, $s(\phi, \phi) = s(\pi, \pi) = 1$, $\sigma_{\omega}(\phi, \pi) = 2J$, and on the hopping pair $(\phi, \pi)$ the limit is the Fock vacuum of one boson mode.
\end{enumerate}
All clauses are proved. \emph{Reading.} For product states of tower blocks the fluctuation states themselves converge, with an explicit rate, to the quasi-free boson state whose symplectic form is the stored fluctuation form; the Weyl operators use the kernel unit $J$. Parity decides the bracket that survives the limit: even collective modes become bosons, odd ones fermions, and only the fermion bracket can be exact at finite size.

## technical
The stored result showed that the commutator of collective fluctuations of a tower converges, but not that their states do. With the kernel bivector $J$ of a tower level as the unit, the Weyl operators $\exp(JF_{N}(x))$ of self-adjoint fluctuation fields are unitary, and for a product state of the blocks their products factorise exactly: the characteristic function is the $N$-th power of a one-block expectation. The ordered cumulants of the fluctuations scale exactly as $N^{1 - k/2}$, so only the second survives, and an explicit bound of order $N^{-1/2}$, attained whenever a third cumulant is nonzero, carries the characteristic functions to those of the quasi-free (Gaussian) boson state. Its covariance is the symmetric part of $\omega(y_{x}y_{y})$ and its symplectic form is the stored $\sigma_{\omega} = \omega([x, y])$, with values in $J\R$; for the hopping fields $\phi$, $\pi$ it is $2J(p_{1} - p_{2})$, which vanishes for real fields alone. For polarised blocks the limit on the hopping pair is the Fock vacuum: normally ordered moments vanish and anti-normally ordered ones are $k!\prod_{l<k}(1 - l/N)$.

On the statistics side, elements of different blocks commute unless both are odd, when they anticommute (graded locality, as in the companion result on spin and statistics of ladder bosons); hence the bracket matching the parity of the fluctuation fields (commutator for even, anticommutator for odd) is exactly a sum of single-block brackets and obeys the law of large numbers: even fluctuations become bosons, odd ones fermions. A trace over $\mathrm{span}\{1, J\}$ shows that a commutator of transport elements is never a nonzero number over $\mathrm{span}\{1, J\}$ (in the whole level $J = \tfrac12[g_{1}, g_{2}]$ is one), while an anticommutator can be: fermion brackets can be exact at finite size, boson brackets only in the limit.

## lay
The tower is made of fermions, and bosons appear in it only as collective ripples averaged over many places. Earlier work showed that the ripples' basic commutation rule approaches that of a boson. This result shows that their whole statistical behaviour does too: when the places are independent, the probabilities of the averaged ripples approach the bell-shaped quantum state of a boson, at a known rate set by the square root of the number of places, and for a fully lopsided starting state they approach the boson's empty state. The phases in this statement use a spare plane of each tower level as their unit. Ripples built from pairs of fermion operations become bosons; ripples built from single fermion operations become fermions, and only the latter can be exact at finite size.

## one-liner
For product states of tower blocks the Weyl characteristic functions $\omega_{N}(\prod_{j}e^{JF_{N}(x_{j})})$, with $J$ the kernel bivector, are exact $N$-th powers, their cumulants scale as $N^{1 - k/2}$, and they tend at rate $N^{-1/2}$ to the quasi-free state with form $\omega([x, y])$; even collective brackets become canonical commutators, odd ones anticommutators, only the latter at finite $N$.
