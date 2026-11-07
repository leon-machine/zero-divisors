---
id: synthesis.kernel-turn-grades-collective-statistics-and-fluctuation-states-tend-to-quasi-free
kind: claim
version: 1
title: The kernel turn, graded statistics and the central limit of tower collective modes
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
  - synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom@1
  - field-theory.no-canonical-commutation-relations-tower@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_kernel_turn_is_a_unitary_group_acting_on_modes_as_the_kernel_rotor
- kind: check
  ref: check.py::check_weights_and_the_two_pi_sign_of_modes_pairs_and_collective_fields
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
  open_problem: bos.spin-statistics
  note: >-
    Answers two targets of the boson items, bos.spin-statistics (clauses (i) to (iii)) and bos.qclt-states
    (clauses (iv) and (v)); the extraction field names the first. Everything is derived in the Clifford algebra of a
    tower level; no imported Fact is a premise. The unit is the kernel bivector J = g1 g2 of the level Cl(m, m + 2)
    (the same day's item-4 result on the unit of Hermitian boson fields establishes that J is the only even unit
    commuting with every transport generator, and that the level pseudoscalar is +-J Gamma; the facts about J used
    here, J^2 = -1, J* = -J, J commutes with the transport generators and J Gamma = I, are re-derived in the check and
    the proof). At m = 1 the level is Cl(1,3) and J is the transverse bivector of
    synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom. What "spin" means here: the rotor
    R = e^{-theta J/2} turns the kernel plane through theta under the sandwich and acts on the modes by left
    multiplication, the action under which an element is a spinor; the modes, being vectors of the transport planes,
    are fixed by the sandwich, so under the rotor group of the level acting on vectors every element has integer
    weight. The clauses state which action they use; the identification of the kernel turn with a physical rotation is
    exact at m = 1 (the transverse plane of the radial atom), a reading for m > 1. Spin is the same datum for every
    mode here because one rotor acts on all of them; with spins assigned mode by mode the connection would be an
    extra condition. New here: (i) the kernel turn U_theta = exp(theta J Nhat/2) as a unitary group whose adjoint
    action is the kernel rotor on annihilators, U_{2 pi} = Gamma, and the Klein twist V = (1 + I)(1 + J)^{-1} built
    from the level pseudoscalar, with V^2 = Gamma (the form of the Klein-twist identity of
    synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics
    (iv), there with I4, here with J and the level's own pseudoscalar); (ii) the weights of modes, pairs, density
    modes and the Hermitian collective fields; (iii) graded locality reduces every collective bracket of the matching
    kind to single-block brackets, so integer-weight fluctuations obey commutation relations and half-integer ones
    anticommutation relations in the limit, while the trace over span{1, J} forbids a canonical commutator (never a
    canonical anticommutator) at finite N; (iv) the convergence of the fluctuation states (characteristic functions of
    Weyl operators with the unit J) to the quasi-free state with the stored form sigma_omega, with exact cumulant
    scaling N^{1 - k/2} and an explicit error bound; (v) the polarised blocks' Fock-vacuum limit. Prior art, not
    premises: the quantum central limit theorem is C. D. Cushen and R. L. Hudson, J. Appl. Probab. 8 (1971) 454-469,
    and D. Goderis, A. Verbeure and P. Vets, Probab. Th. Rel. Fields 82 (1989) 527-544 (cited as in the
    fluctuation-forms result; the volume and pages of the second not independently verified); the fermionic central
    limit for odd elements is in the same literature (C. D. Cushen and R. L. Hudson; W. von Waldenfels), cited from
    memory; the Klein transformation is standard (O. Klein 1938, cited from memory); additivity of cumulants of
    independent commuting families is the classical moment-cumulant relation. What is not claimed: the physical spin
    of the modes for m > 1, the spin-statistics theorem of relativistic fields (stored separately), convergence for
    states that are not product states (the product hypothesis is used in (iv) at the first step), or a construction
    of gauge bosons. Ledger: (i) to (v) are transport-absent (finite CAR algebra of a tower level with the kernel
    unit); the m = 1 reading is transport-convenient.
---

## formal
Let a tower level be $\Cl(m, m + 2)$ with kernel generators $g_{1}, g_{2}$, $Q(g_{1}) = Q(g_{2}) = -1$, and $m$ transport planes with generators $e_{j}, f_{j}$, $Q(e_{j}) = 1$, $Q(f_{j}) = -1$. Let $v_{j} = \tfrac12(e_{j} + f_{j})$, $w_{j} = \tfrac12(e_{j} - f_{j})$, the Witt pairs of Theorem \claimref{std-algebra.witt-basis-car} read with $v_{j}$ as creators and $w_{j}$ as annihilators, $n_{j} = v_{j}w_{j}$, $\hat N = \sum_{j}n_{j}$; $J = g_{1}g_{2}$; $\Gamma = \prod_{j}e_{j}f_{j}$; $I$ the product of all generators in the order $g_{1}, g_{2}, e_{1}, f_{1}, \dots$; and $x \mapsto x^{*}$ reversion composed with a sign for each generator of negative square, so $v_{j}^{*} = w_{j}$ and $J^{*} = -J$. Let $\mathcal{T}$ be the algebra generated by the transport generators and $\mathcal{T}_{J} = \mathcal{T} + J\mathcal{T}$; $J^{2} = -1$ and $J$ commutes with $\mathcal{T}$, so $\mathrm{span}\{1, J\}$ is a field and $\mathcal{T}_{J}$ is an algebra over it.
\begin{enumerate}
\item[(i)] \emph{(The kernel turn.)} For real $\theta$ let $U_{\theta} = \exp(\theta J\hat N/2) = \prod_{j}\bigl(1 + (e^{\theta J/2} - 1)n_{j}\bigr)$ and $R_{\theta} = e^{-\theta J/2}$. Then $U_{\theta}^{*}U_{\theta} = 1$, $U_{\theta}U_{\varphi} = U_{\theta + \varphi}$, and
\[
U_{\theta}w_{j}U_{\theta}^{*} = R_{\theta}w_{j}, \qquad U_{\theta}v_{j}U_{\theta}^{*} = R_{\theta}^{-1}v_{j}, \qquad R_{\theta}g_{1}\tilde R_{\theta} = \cos\theta\,g_{1} - \sin\theta\,g_{2}, \quad R_{\theta}g_{2}\tilde R_{\theta} = \sin\theta\,g_{1} + \cos\theta\,g_{2} :
\]
the adjoint action of $U_{\theta}$ multiplies each annihilator on the left by the rotor that turns the kernel plane through $\theta$, the action under which an element is a spinor of that plane. The turn through $2\pi$ is $U_{2\pi} = \Gamma$, the half turn satisfies $U_{\pi}^{2} = \Gamma$, and $J\Gamma = I$. The Klein twist $V = (1 + I)(1 + J)^{-1} = \tfrac12(1 + I)(1 - J)$ satisfies $VV^{*} = 1$ and $V^{2} = \Gamma$. At $m = 1$, with $e_{1}, f_{1}, g_{1}, g_{2}$ read as $e_{0}, e_{1}, e_{2}, e_{3}$ of $\Cl(1,3)$, $J$ is the transverse bivector of Theorem \claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom} and $\operatorname{Ad}(U_{\theta}) = \tau_{-\theta/2}$, its phase flow, so the kernel turn is the turn of the transverse plane about the radial direction.
\item[(ii)] \emph{(Weights and the $2\pi$ sign.)} Say $x \in \mathcal{T}_{J}$ has weight $s$ if $U_{\theta}xU_{\theta}^{*} = e^{-s\theta J}x$ for all $\theta$. Annihilators have weight $\tfrac12$, creators $-\tfrac12$, the normalised single-fermion sum $m^{-1/2}\sum_{j}w_{j}$ weight $\tfrac12$; hopping elements $v_{j}w_{k}$, the density modes $\rho_{q} = \sum_{k}v_{k}w_{k+q}$ and the Hermitian collective fields $\phi = S + S^{*}$, $\pi = J(S^{*} - S)$ of a hopping sum $S$ weight $0$; pairing elements $w_{j}w_{k}$ weight $1$. $U_{2\pi}xU_{2\pi}^{*}$ is $x$ for even $x$ and $-x$ for odd $x \in \mathcal{T}_{J}$, so an element of weight $s$ has $2\pi$ sign $(-1)^{2s}$.
\item[(iii)] \emph{(Graded locality and the brackets of collective modes.)} Let $x, y \in \mathcal{T}_{J}$ be built from $J$ and the generators of disjoint sets of planes. Then $xy = yx$ unless both are odd, and then $xy = -yx$. For copies $x_{k}, y_{k}$ of $x, y$ on $N$ disjoint blocks (sets of planes) and $[x, y]_{\epsilon} = xy - \epsilon yx$ with $\epsilon = -1$ when $x$ and $y$ are both odd and $\epsilon = 1$ otherwise,
\[
\Bigl[\sum_{k}x_{k}, \sum_{l}y_{l}\Bigr]_{\epsilon} = \sum_{k}[x_{k}, y_{k}]_{\epsilon}
\]
exactly, while for odd $x$, $y$ the commutator of the sums keeps cross terms. Hence, for an even product state $\omega_{N}$ of $N$ blocks with block state $\omega$ and $F_{N}(x) = N^{-1/2}\sum_{k}(x_{k} - \omega(x))$, $[F_{N}(x), F_{N}(y)]_{\epsilon} = N^{-1}\sum_{k}C_{k}$ with $C = [x, y]_{\epsilon}$, of mean $\omega(C)$ and variance $(\omega(C^{*}C) - \omega(C^{*})\omega(C))/N$: fluctuations of integer weight obey canonical commutation relations, and those of half-integer weight canonical anticommutation relations, as $N \to \infty$ in mean square. The trace $\mathrm{T}(x) = \br{x}_{0} - J\br{Jx}_{0}$ over $\mathrm{span}\{1, J\}$ is cyclic on $\mathcal{T}_{J}$ with $\mathrm{T}(1) = 1$, so no commutator of two elements of a level is a nonzero element of $\mathrm{span}\{1, J\}$, while $\{w_{j}, v_{j}\} = 1$: the half-integer bracket can be canonical at finite $N$, the integer one only in the limit.
\item[(iv)] \emph{(Central limit of the fluctuation states.)} Let $\mathcal{A}_{e}$ be the even algebra of a block of two planes, $\omega$ a real state of $\mathcal{A}_{e}$ ($\omega(x^{*}) = \omega(x)$) with density $\rho$, extended to $\mathcal{A}_{e} + J\mathcal{A}_{e}$ by $\omega(x) = 4(\br{\rho x}_{0} - J\br{J\rho x}_{0})$, which is positive, and $\omega_{N}$ the product state on $N$ blocks. For self-adjoint $x$ let $W_{N}(x) = \exp(JF_{N}(x))$, a unitary. For self-adjoint $x_{1}, \dots, x_{r}$ with $y_{j} = x_{j} - \omega(x_{j})$:
\begin{enumerate}
\item[(a)] $\omega_{N}(W_{N}(x_{1})\cdots W_{N}(x_{r})) = \bigl[\omega(e^{Jy_{1}/\sqrt N}\cdots e^{Jy_{r}/\sqrt N})\bigr]^{N}$;
\item[(b)] the ordered cumulants of the fluctuations (the moment-cumulant relation over set partitions, each part multiplied in its original order) satisfy $\kappa(F_{N}(x_{j_{1}}), \dots, F_{N}(x_{j_{k}})) = N^{1 - k/2}\kappa(y_{j_{1}}, \dots, y_{j_{k}})$ for $k \ge 2$, with first cumulants $0$;
\item[(c)] with $c = \tfrac12\omega\bigl((\sum_{j}y_{j})^{2}\bigr) + \tfrac12\sum_{j < l}\omega([y_{j}, y_{l}])$, $\|x\|_{1}$ the sum of the absolute values of the blade coefficients of $x$, and $r = \sum_{j}\|y_{j}\|_{1}$,
\[
\bigl|\omega_{N}(W_{N}(x_{1})\cdots W_{N}(x_{r})) - e^{-c}\bigr| \le \frac{r^{3}}{6}e^{r/\sqrt N}N^{-1/2} + \frac{r^{4}}{8}e^{r^{2}/2N}N^{-1},
\]
with $|a + bJ| = (a^{2} + b^{2})^{1/2}$;
\item[(d)] $e^{-c}$ is the value on $W(x_{1})\cdots W(x_{r})$ of the quasi-free state $\omega_{\infty}(W(x)) = e^{-s(x, x)/2}$ of the Weyl algebra $W(x)W(y) = e^{-\sigma_{\omega}(x, y)/2}W(x + y)$, with covariance $s(x, y) = \tfrac12\omega(\{y_{x}, y_{y}\})$, real, and symplectic form $\sigma_{\omega}(x, y) = \omega([x, y])$, the stored fluctuation form, here in $J\R$; $|\sigma_{\omega}(x, y)|^{2} \le 4s(x, x)s(y, y)$. For the hopping fields $\phi = b + b^{*}$, $\pi = J(b^{*} - b)$ of $b = v_{1}w_{2}$ in the product state with occupations $p_{1}, p_{2}$, $s(\phi, \phi) = s(\pi, \pi) = p_{1} + p_{2} - 2p_{1}p_{2}$ and $\sigma_{\omega}(\phi, \pi) = 2J(p_{1} - p_{2})$. The rate $N^{-1/2}$ is attained: $\kappa(n_{1}, n_{1}, n_{1}) = p_{1}(1 - p_{1})(1 - 2p_{1})$.
\end{enumerate}
\item[(v)] \emph{(Polarised blocks: the Fock vacuum.)} In the polarised product state ($p_{1} = 1$, $p_{2} = 0$ on every block) with $B = N^{-1/2}\sum_{k}b_{k}$, $\omega_{N}(B^{k}B^{*k}) = k!\prod_{l < k}(1 - l/N)$ and $\omega_{N}(B^{*k}B^{k}) = 0$, the third cumulant of $F_{N}(\phi)$ is $0$ and the fourth is $-2/N$; the uncertainty bound of (iv)(d) is an equality, and the limit is the Fock vacuum of one boson mode.
\end{enumerate}
All clauses are proved. \emph{Reading.} With the kernel rotor acting on modes as on spinors, half-integer weight goes with anticommutation and integer weight with commutation exactly on every finite tower (graded locality); what needs the limit is only the scalar value of the boson commutator, and the same limit carries the fluctuation states to the quasi-free boson state with the stored form, the unit of its Weyl operators being $J$.

## technical
Take a tower level, the transport planes together with the kernel plane whose bivector $J$ squares to $-1$ and commutes with every transport generator. The number operator $\hat N$ generates the kernel turn $U_{\theta} = \exp(\theta J\hat N/2)$, a unitary group whose adjoint action multiplies every annihilator on the left by the rotor $e^{-\theta J/2}$ that turns the kernel plane through $\theta$: the modes transform as spinors of that plane. At $\theta = 2\pi$ the turn is $\Gamma = \prod_{j}e_{j}f_{j}$, the fermion parity, so the $2\pi$ sign of a mode is $-1$ and that of every even element $+1$; $J\Gamma$ is the level pseudoscalar $I$, and the Klein twist $(1 + I)(1 + J)^{-1}$ squares to $\Gamma$. At $m = 1$ the level is the spacetime algebra, $J$ is the transverse bivector, and the kernel turn is the phase flow of the radial atom at half the angle. Modes have weight $\tfrac12$, hopping elements, density modes and the Hermitian fields $\phi$, $\pi$ weight $0$, pairings weight $1$.

Elements on disjoint planes commute unless both are odd, when they anticommute. So the collective bracket of the matching kind (commutator for integer weight, anticommutator for half-integer weight) is exactly a sum of single-block brackets, and by the law of large numbers the fluctuation brackets tend in mean square to the numbers $\omega([x, y])$ or $\omega(\{x, y\})$: bosons from integer weight, fermions from half-integer weight. A trace argument shows that a commutator in a level never equals a nonzero number of $\mathrm{span}\{1, J\}$, while an anticommutator can: fermion brackets can be exact at finite size, boson brackets only in the limit.

For product states the fluctuation states converge. Products of Weyl operators $\exp(JF_{N}(x))$ factorise exactly over the blocks, so the characteristic function is the $N$-th power of a one-block quantity; the ordered cumulants of the fluctuations scale exactly as $N^{1 - k/2}$; an explicit bound of order $N^{-1/2}$, attained when the third cumulant is nonzero, gives the limit, the quasi-free state with covariance the symmetric part of $\omega(y_{x}y_{y})$ and symplectic form the stored $\sigma_{\omega} = \omega([x, y])$, here with values in $J\R$. The kernel unit is what makes the form nonzero on self-adjoint fields; for the hopping fields it is $2J(p_{1} - p_{2})$. For polarised blocks the limit is the Fock vacuum: normally ordered moments vanish and the anti-normally ordered ones are $k!\prod_{l<k}(1 - l/N)$.

## lay
The tower is made of fermions, which come in two kinds of behaviour under a full turn: a fermion changes sign, a pair of fermions does not. This result gives that turn a definite meaning inside each level of the tower: a spare plane of the level, the one whose rotation also supplies the unit of phases, turns the fermion operations the way spinors turn, so a full turn flips their sign and leaves pairs alone. Operations that flip sign exclude each other when they sit in different places, and those that do not flip sign pass freely; averaged over many places they become fermions and bosons respectively. The averaged ripples of pairs also settle, in their full statistics and not only in their commutation, into the bell-shaped quantum state of a boson, with a known rate, and for a fully lopsided starting state into the boson's empty state.

## one-liner
In a tower level $\Cl(m, m + 2)$ the kernel turn $e^{\theta J\hat N/2}$ acts on modes as the kernel rotor on spinors and is the fermion parity at $2\pi$; graded locality makes integer-weight fluctuations bosons and half-integer ones fermions, and for product states the Weyl characteristic functions (unit $J$) tend to the quasi-free state with form $\omega([x, y])$, error $O(N^{-1/2})$, cumulants $N^{1 - k/2}$.
