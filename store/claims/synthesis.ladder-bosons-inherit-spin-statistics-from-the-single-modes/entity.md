---
id: synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes
kind: claim
version: 1
title: "On the ladder the bosons' spin and statistics are fixed by the single modes' spins"
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
  - std-algebra.spin-double-cover@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_two_pi_rotation_is_the_product_of_half_integer_plane_volumes
- kind: check
  ref: check.py::check_spin_statistics_holds_exactly_when_every_mode_is_half_integer
- kind: check
  ref: check.py::check_bosons_obey_the_connection_exactly_for_uniform_assignments
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
    grading of the tower algebra and are exact at every N; the spin is a datum the tower does not supply. Spin and
    statistics agree on the whole algebra exactly when every single mode is a spinor; the bosons alone obey the
    connection exactly when the assignment is uniform (all spinor or all integer). New to the store: (i) the
    general diagonal mode rotation U(theta) = exp(theta J L), L = sum_j s_j n_j, with unit the kernel bivector J,
    whose turn by 2 pi is the product of the plane volume elements omega_j of the half-integer modes (this entity
    holds the formula; the phase circle of synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower
    (vi) is its case of alternating weights +-1/2); (ii) Ad U(2 pi) equals the parity Ad Gamma exactly when every s_j
    is half-integer, with graded locality on disjoint supports (this entity holds that statement); and Ad U(2 pi)
    fixes every even element exactly when the 2 s_j all have the same parity, the same fact as the commutant of the
    even part of Cl(N, N) being span{1, Gamma} (clause (i) of
    synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower, re-derived here directly on
    products of two modes); (iii) with all weights integer the bosons obey the connection while every single mode
    is a fermion of integer spin, and with a mixed assignment one spinor mode and one spin-0 mode per block give a
    hopping element of half-integer spin that commutes across blocks and whose normalised sum is the
    Holstein-Primakoff ladder of the stored result, a boson of half-integer spin in the limit; (iv) every rotor
    group of the level whose action on vectors has period 2 pi ends at +-1 (std-algebra.spin-double-cover), so
    rotations of the level's own vector space (the kernel rotors, the real rotation of two modes) give every
    element integer spin. Stored and cited, not refiled: the hopping ladder [B, B*] = 1 - 2k/N
    (synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum (ii)). For the attached
    free fields the half-integer assignment of the CAR modes is what locality with a positive norm supplies
    (synthesis.locality-of-the-attached-free-fields-fixes-their-statistics (iii), cited, not used): a continuum
    input about those fields, not a property of the ladder. Prior art, orientation only, cited from memory: that
    the second quantisation of the one-particle operator -1 is the parity, and that spin and statistics are
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
\item[(ii)] \emph{(Spin and statistics agree exactly when every mode is a spinor.)} $\operatorname{Ad}U_{s}(2\pi) = \operatorname{Ad}\Gamma$ on the algebra of the planes if and only if every $s_{j}$ is half-integer, and then $U_{s}(2\pi) = \Gamma$. In that case an element of definite spin has half-integer spin exactly when it is odd, two odd elements on disjoint sets of modes anticommute and every other pair on disjoint sets commutes; in particular every hopping element $v_{i}w_{j}$, pairing element $w_{i}w_{j}$, collective sum of them and density mode $\rho_{q} = \sum_{k}v_{k}w_{k+q}$ has integer spin and Bose statistics across blocks, exactly at every $N$, with no limit taken. \emph{(The bosons alone.)} $\operatorname{Ad}U_{s}(2\pi)$ fixes every even element (every product of two modes, hence every hopping, pairing, density and collective mode) if and only if the $2s_{j}$ all have the same parity: every $s_{j}$ half-integer, or every $s_{j}$ an integer.
\item[(iii)] \emph{(Uniform integer and mixed assignments.)} If some $s_{j}$ is an integer, $w_{j}$ has integer spin and anticommutes with every other mode: a fermion of integer spin. If every $s_{j}$ is an integer, $U_{s}(2\pi) = 1$: the bosons obey the connection (integer spin, Bose statistics) while every single mode breaks it. \emph{Counter-model for a mixed assignment: a boson of half-integer spin.} Take $N_{b}$ blocks, the lower mode of each with weight $\tfrac12$ and the upper with weight $0$, and $b_{i} = v_{\mathrm{lower},i}w_{\mathrm{upper},i}$. Each $b_{i}$ has half-integer spin; the $b_{i}$ and $b_{i}^{*}$ of distinct blocks commute; and $B = N_{b}^{-1/2}\sum_{i}b_{i}$ is the hopping ladder of Theorem \claimref{synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum}(ii): on $(B^{*})^{k}P_{\mathrm{pol}}$, $[B, B^{*}] = 1 - 2k/N_{b}$, $k = 0, \dots, N_{b}$, so $B$ tends on states of bounded $k$ to a canonical boson mode of half-integer spin.
\item[(iv)] \emph{(The level's own rotations give integer spin.)} If $R(\theta)$ is a one-parameter group of rotors of $L_{N}$ whose action $x \mapsto R(\theta)xR(\theta)^{\sim}$ on the vectors has period $2\pi$, then $R(2\pi) = \pm1$ (the kernel of the double cover, Theorem \claimref{std-algebra.spin-double-cover}), so $\operatorname{Ad}R(2\pi)$ is the identity on the whole level: every element has integer spin under rotations of the level's own vector space. Two instances: the kernel rotors $e^{\varphi J/2}$, with $e^{\pi J} = -1$, and $\operatorname{Ad}e^{\varphi J}$ fixes every element of the algebra of the planes, for every $\varphi$; The real rotation of two modes, $L = v_{0}w_{1} - v_{1}w_{0} = \tfrac12(e_{0}e_{1} - f_{0}f_{1})$, is a sum of two commuting bivectors of square $-1$; $[L, w_{0} \pm Jw_{1}] = \pm J(w_{0} \pm Jw_{1})$, so its weights are $\pm1$; $e^{\pi L} = \omega_{0}\omega_{1}$ negates both modes and $e^{2\pi L} = 1$. Half-integer weights need the unit $J$ at half angle, which is the datum $s$.
\end{enumerate}
Clauses (i) to (iv) are proved. \emph{Reading.} On the ladder, statistics is the grading of the algebra and holds exactly at every $N$; spin is the extra datum $s$. Spin and statistics agree on the whole algebra if and only if every mode is a spinor (ii). For the even elements, the bosons, every element has integer spin if and only if the $2s_{j}$ all have the same parity (all modes spinors, or all of integer weight); with a mixed assignment a hopping element between a spinor and an integer-weight mode is a commuting boson of half-integer spin (iii), and with all weights integer the bosons obey the connection while every single mode is a fermion of integer spin. So the collective modes cannot repair a mixed assignment, and they cannot detect a uniform integer one. The tower does not fix the datum: by (iv) the rotations of its own vector space give integer spin to everything, and half-integer weights need the kernel unit $J$ at half angle. For the attached free fields the spinor assignment of the CAR modes is supplied by locality with a positive norm (\claimref{synthesis.locality-of-the-attached-free-fields-fixes-their-statistics}), a continuum input.

## technical
On the tower, fermion modes anticommute and products of two modes on distinct blocks commute: this is the grading of the algebra and holds exactly for any number of modes. Spin is a separate datum: how a rotation acts on each mode. With the kernel bivector $J$ as the unit, a rotation diagonal in the mode basis with weights $s_{j}$ is implemented inside the level by $U(\theta) = e^{\theta J\sum s_{j}n_{j}} = \prod_{j}(1 - n_{j} + n_{j}e^{\theta Js_{j}})$, because each $n_{j}$ is an idempotent commuting with $J$ and the others. Since $n_{j} = \tfrac12(1 - \omega_{j})$ with $\omega_{j} = e_{j}f_{j}$, the turn by $2\pi$ is exactly the product of the plane volume elements of the modes of half-integer weight. It acts as the parity $\Gamma$ on all modes if and only if every weight is half-integer; then every odd element has half-integer spin and every even element, every boson built from pairs, has integer spin, at every size. On the bosons alone, the turn by $2\pi$ fixes every product of two modes exactly when the weights are all half-integer or all integer. If one mode has integer weight, that mode is a fermion of integer spin; if all weights are integer the bosons still obey the connection; if the assignment is mixed, pairing a spinor mode with a weight-zero mode in each block gives a hopping element of half-integer spin that commutes across blocks and whose normalised sum climbs the known Holstein-Primakoff ladder, a boson of half-integer spin in the limit. The level's own rotations give integer spin to everything: a rotor group whose action on vectors has period $2\pi$ ends at $\pm1$, the kernel of the double cover (instances: the kernel rotors, which fix every mode, and the real rotation of two modes, with weights $\pm1$). So the spinor assignment is an input, and the collective modes can neither repair a mixed assignment nor detect a uniform integer one. For the series' attached free fields it is supplied by locality with a positive norm, which is stored separately.

## lay
In the tower every particle is first a fermion, and bosons appear only as collective pairs. One would like the familiar rule that half-integer spin goes with fermions and whole-number spin with bosons to come out of this construction. The calculation shows exactly how much does. Whether two operators commute or anticommute is built into the algebra and holds exactly at every size. How an operator turns under a rotation is extra information: one has to say how each single mode turns. If every single mode turns like a spinor, picking up a minus sign after a full turn, then every pair, and so every collective boson, comes back to itself, and the rule holds exactly, without any limit. If some modes turn like spinors and others do not, the rule fails, and it fails for bosons too: a pair made of a spinor mode and a spinless mode builds a boson that picks up a minus sign after a full turn. If no mode turns like a spinor, the bosons still follow the rule but the single fermions break it. The tower itself does not decide which way the single modes turn; for the free fields the graph attaches, that input comes from the requirement that fields at separated points do not interfere, which the graph treats elsewhere.

## one-liner
On a tower level with unit $J$, the turn by $2\pi$ of a mode rotation of weights $s_{j}$ is $\prod_{s_{j} \notin \mathbb{Z}}e_{j}f_{j}$, equal to the parity exactly when every mode is a spinor; then all collective pair modes have integer spin and commute, at every $N$; if some but not all modes are spinors, a spinor mode paired with a spin-0 mode gives a commuting boson of half-integer spin; with all weights integer the pair modes keep integer spin and only the single modes break the connection.
