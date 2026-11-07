---
id: synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes
kind: claim
version: 1
title: 'On the ladder the bosons inherit spin and statistics from the single modes'
status: proved
region: synthesis
subject: quantum-fields
tags: [bosonisation, car-algebra, ladder-pairs, grading-and-parity]
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
  - tower.ladder-pairs-satisfy-car-vectors@4
  - tower.volume-elements-planes@5
  - std-algebra.bivector-exponential@4
  - synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_two_pi_rotation_is_the_product_of_half_integer_plane_volumes
- kind: check
  ref: check.py::check_spin_statistics_holds_exactly_when_every_mode_is_half_integer
- kind: check
  ref: check.py::check_half_integer_spin_boson_from_a_spinor_and_a_scalar_mode
- kind: check
  ref: check.py::check_rotations_of_the_level_itself_give_integer_spin
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum
  - synthesis.locality-of-the-attached-free-fields-fixes-their-statistics
extraction:
  open_problem: bos.spin-statistics
  note: >-
    Attack on the run target bos.spin-statistics (whether, on the ladder, half-integer spin goes with
    anticommutation and integer spin with commutation of the collective modes). Answer: the statistics are the
    grading of the tower algebra and are exact at every N; the spin is a datum the tower does not supply, and
    spin and statistics agree for the collective modes exactly when they agree for the single modes. New here:
    (i) the turn by 2 pi of any diagonal mode rotation U(theta) = exp(theta J L), L = sum_j s_j n_j, is the product
    of the plane volume elements omega_j of the half-integer modes, computed exactly in the level Cl(N, N+2) with
    the kernel bivector J as the unit; (ii) Ad U(2 pi) equals the parity Ad Gamma exactly when every s_j is
    half-integer, and then every even element (hopping, pairing and density modes, at every N) has integer spin;
    (iii) the counter-model: one spinor mode and one spin-0 mode per block give a hopping element of
    half-integer spin that commutes across blocks and whose normalised sum is the Holstein-Primakoff ladder of
    the stored result, a boson of half-integer spin in the limit, while the spin-0 mode is an anticommuting mode
    of integer spin; (iv) the rotations the level supplies by itself (the kernel rotors, and the real rotation
    of two modes) give every element integer spin. Stored and cited, not refiled: the hopping ladder
    [B, B*] = 1 - 2k/N (synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum (ii));
    the kernel bivector J commuting with every plane generator is re-derived here in one line. The half-integer
    assignment of every CAR mode is what locality with a positive norm supplies for the attached free fields
    (synthesis.locality-of-the-attached-free-fields-fixes-their-statistics (iii), cited, not used): it is a
    continuum input, not a property of the ladder. Prior art, orientation only, cited from memory: that the
    second quantisation of the one-particle operator -1 is the parity, and that spin and statistics are
    independent without locality (non-relativistic models of spin-0 fermions), are standard; the spin-statistics
    theorem itself is in the stored Facts on Pauli, Guido and Longo, and Kuckert. No imported Fact is a premise
    and no imaginary unit is used: the unit is J throughout. Ledger: transport-absent (finite Clifford algebra of
    a tower level).
---

## formal
Let $L_{N} = \Cl(N, N{+}2)$ be a tower level, written as the anisotropic kernel $\mathrm{span}\{g_{1}, g_{2}\}$ ($Q = -1, -1$) orthogonal to $N$ hyperbolic planes $(e_{j}, f_{j})$, $Q(e_{j}) = 1$, $Q(f_{j}) = -1$, with $v_{j} = \tfrac12(e_{j} + f_{j}) = a_{j}^{*}$, $w_{j} = \tfrac12(e_{j} - f_{j}) = a_{j}$ (the canonical anticommutation relations, Theorem \claimref{tower.ladder-pairs-satisfy-car-vectors}), $n_{j} = v_{j}w_{j}$, $\omega_{j} = e_{j}f_{j}$, $\Gamma = \prod_{j}\omega_{j}$, $J = g_{1}g_{2}$, and $*$ the adjoint (reversion composed with the sign flip of the generators of square $-1$). A \emph{spin assignment} is $s = (s_{1}, \dots, s_{N})$ with $s_{j} \in \tfrac12\mathbb{Z}$, the weights of a rotation of the one-particle space that is diagonal in the mode basis; it defines $L_{s} = \sum_{j}s_{j}n_{j}$ and
\[
U_{s}(\theta) = e^{\theta JL_{s}} = \prod_{j}\bigl(1 - n_{j} + n_{j}e^{\theta Js_{j}}\bigr), \qquad e^{\varphi J} = \cos\varphi + J\sin\varphi .
\]
An element $x$ has \emph{integer} (\emph{half-integer}) \emph{spin} if $U_{s}(2\pi)\,x\,U_{s}(2\pi)^{*} = x$ ($= -x$). Two elements obey Bose (Fermi) statistics if they commute (anticommute).
\begin{enumerate}
\item[(i)] \emph{(The turn by $2\pi$.)} $J^{2} = -1$, $J^{*} = -J$, and $J$ commutes with every plane generator. $U_{s}(\theta)$ is unitary, commutes with $J$, satisfies $U_{s}(\theta)U_{s}(\theta') = U_{s}(\theta + \theta')$, and $U_{s}(\theta)w_{j}U_{s}(\theta)^{*} = e^{-\theta Js_{j}}w_{j}$, $U_{s}(\theta)v_{j}U_{s}(\theta)^{*} = e^{\theta Js_{j}}v_{j}$. Since $n_{j} = \tfrac12(1 - \omega_{j})$,
\[
U_{s}(2\pi) = \prod_{j:\ s_{j} \in \mathbb{Z} + \frac12}\omega_{j} ,
\]
the product of the volume elements of the planes of half-integer weight.
\item[(ii)] \emph{(Spin and statistics agree exactly when every mode is a spinor.)} $\operatorname{Ad}U_{s}(2\pi) = \operatorname{Ad}\Gamma$ on the algebra of the planes if and only if every $s_{j}$ is half-integer, and then $U_{s}(2\pi) = \Gamma$. In that case an element of definite spin has half-integer spin exactly when it is odd, two odd elements on disjoint sets of modes anticommute and every other pair on disjoint sets commutes; in particular every hopping element $v_{i}w_{j}$, pairing element $w_{i}w_{j}$, collective sum of them and density mode $\rho_{q} = \sum_{k}v_{k}w_{k+q}$ has integer spin and Bose statistics across blocks, exactly at every $N$, with no limit taken.
\item[(iii)] \emph{(Counter-model: a boson of half-integer spin.)} Let some $s_{j}$ be an integer. Then $w_{j}$ has integer spin and anticommutes with every other mode. Take $N_{b}$ blocks, the lower mode of each with weight $\tfrac12$ and the upper with weight $0$, and $b_{i} = v_{\mathrm{lower},i}w_{\mathrm{upper},i}$. Each $b_{i}$ has half-integer spin; the $b_{i}$ and $b_{i}^{*}$ of distinct blocks commute; and $B = N_{b}^{-1/2}\sum_{i}b_{i}$ is the hopping ladder of Theorem \claimref{synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum}(ii): on $(B^{*})^{k}P_{\mathrm{pol}}$, $[B, B^{*}] = 1 - 2k/N_{b}$, $k = 0, \dots, N_{b}$, so $B$ tends on states of bounded $k$ to a canonical boson mode of half-integer spin.
\item[(iv)] \emph{(The level's own rotations give integer spin.)} $\operatorname{Ad}e^{\varphi J}$ fixes every element of the algebra of the planes, for every $\varphi$. The real rotation of two modes, $L = v_{0}w_{1} - v_{1}w_{0} = \tfrac12(e_{0}e_{1} - f_{0}f_{1})$, is a sum of two commuting bivectors of square $-1$; $[L, w_{0} \pm Jw_{1}] = \pm J(w_{0} \pm Jw_{1})$, so its weights are $\pm1$; $e^{\pi L} = \omega_{0}\omega_{1}$ negates both modes and $e^{2\pi L} = 1$.
\end{enumerate}
Clauses (i) to (iv) are proved. \emph{Reading.} On the ladder, statistics is the grading of the algebra and holds exactly at every $N$; spin is the extra datum $s$. Spin and statistics agree for the collective modes if and only if they agree for the single modes, so the collective limit neither produces nor repairs the connection: half-integer spin with anticommutation and integer spin with commutation for the bosons is equivalent to every tower mode being a spinor. The tower does not fix that datum: by (iv) the rotations it supplies by itself give integer spin to everything, and half-integer weights need the kernel unit $J$ at half angle. For the attached free fields the spinor assignment of the CAR modes is supplied by locality with a positive norm (\claimref{synthesis.locality-of-the-attached-free-fields-fixes-their-statistics}), a continuum input.

## technical
On the tower, fermion modes anticommute and products of two modes on distinct blocks commute: this is the grading of the algebra and holds exactly for any number of modes. Spin is a separate datum: how a rotation acts on each mode. With the kernel bivector $J$ as the unit, a rotation diagonal in the mode basis with weights $s_{j}$ is implemented inside the level by $U(\theta) = e^{\theta J\sum s_{j}n_{j}} = \prod_{j}(1 - n_{j} + n_{j}e^{\theta Js_{j}})$, because each $n_{j}$ is an idempotent commuting with $J$ and the others. Since $n_{j} = \tfrac12(1 - \omega_{j})$ with $\omega_{j} = e_{j}f_{j}$, the turn by $2\pi$ is exactly the product of the plane volume elements of the modes of half-integer weight. It acts as the parity $\Gamma$ on all modes if and only if every weight is half-integer; then every odd element has half-integer spin and every even element, every boson built from pairs, has integer spin, at every size. If one mode has integer weight, that mode is a fermion of integer spin; and pairing a spinor mode with a weight-zero mode in each block gives a hopping element of half-integer spin that commutes across blocks and whose normalised sum climbs the known Holstein-Primakoff ladder, a boson of half-integer spin in the limit. The level's own rotations (the kernel rotors, which fix every mode, and the real rotation of two modes, whose weights are $\pm1$ and whose turn by $2\pi$ is $+1$) give integer spin to everything, so the spinor assignment is an input. For the series' attached free fields it is supplied by locality with a positive norm, which is stored separately.

## lay
In the tower every particle is first a fermion, and bosons appear only as collective pairs. One would like the familiar rule that half-integer spin goes with fermions and whole-number spin with bosons to come out of this construction. The calculation shows exactly how much does. Whether two operators commute or anticommute is built into the algebra and holds exactly at every size. How an operator turns under a rotation is extra information: one has to say how each single mode turns. If every single mode turns like a spinor, picking up a minus sign after a full turn, then every pair, and so every collective boson, comes back to itself, and the rule holds exactly, without any limit. If some mode does not, the rule fails, and it fails for bosons too: a pair made of a spinor mode and a spinless mode builds a boson that picks up a minus sign after a full turn. The tower itself does not decide which way the single modes turn; that input comes from the requirement that fields at separated points do not interfere, which the graph treats elsewhere.

## one-liner
On a tower level with unit $J$, the turn by $2\pi$ of a mode rotation of weights $s_{j}$ is $\prod_{s_{j} \notin \mathbb{Z}}e_{j}f_{j}$, equal to the parity exactly when every mode is a spinor; then all collective pair modes have integer spin and commute, at every $N$; otherwise a spinor mode paired with a spin-0 mode gives a commuting boson of half-integer spin.
