---
id: synthesis.phase-flow-is-time-rotor-flow-kms-continuation
kind: claim
version: 2
title: The phase flow is the time evolution; the rotor flow is its KMS continuation
status: proved
region: synthesis
subject: thermality
tags: [modular-theory, rotors-and-stabilisers, car-algebra, boundary-modes]
proposed_by:
  kind: ai
  session: colony-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics
derivations:
- name: main
  uses:
  - tower.structure-tower-c-norms@7
  - scrambling.clock-inventory-boundary-modes@5
  - field-theory.boost-modes@3
  - singularity.kms-uniqueness-factor@4
  - singularity.euclidean-rotor-where-it-lies@4
  - rungs.imported-fock-representation-bogoliubov-group@4
  - scrambling.spreading-law-chaos-bound-saturated@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_star_adjoint_and_compact_part
- kind: check
  ref: check.py::check_atom_boost_rotor_not_star
- kind: check
  ref: check.py::check_rotor_flow_not_positive
- kind: check
  ref: check.py::check_rotor_at_beta_is_kms_swap
- kind: check
  ref: check.py::check_detuned_pairing_and_hop
- kind: check
  ref: check.py::check_conjugated_clocks_not_star
- kind: check
  ref: check.py::check_pairing_flow_exponentiated
- kind: proof
  derivation: main
outside_ga:
  kind: complex-analysis
  why: 'i is the unit of the complexified windows Cl(p,q)_C and of V_C (phase flow Ad(e^{itH}), the common phase e^{-i kappa t}, the continuation tau_{-i lambda}, the check over Q(i)); the frame *-structure is conjugate-linear in it and it must commute with the mode vectors, which no pseudoscalar of a general Cl(p,q) does'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: i is the unit of the complexification of a general Cl(p,q) and of V_C, on which the frame *-structure is conjugate-linear and which must commute with the vectors (the mode generators), so no pseudoscalar can stand for it; it stays in the phase flow Ad(e^{itH}), the phases, the KMS continuation tau_{-i lambda} and the check over Q(i) (declared complex-analysis).'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 1 -> 2.'
  open_problem: op.which-boost-flow-is-time
  tension_with:
  - id: scrambling.spreading-law-chaos-bound-saturated@1
    note: its growth step exponentiates the boost with a real parameter, which by (ii) is the rotor flow; on the CAR windows quadratic real-time evolution conserves the h-norm.
  flow_note: both; the claim is about the relation of the rotor flow to the phase flow.
  note: >-
    Decides op.which-boost-flow-is-time in the sense of its first success branch: the phase flow is
    the window's time evolution and the rotor flow its imaginary-time (KMS-strip) continuation.
    Clauses (i)-(v) are proved; the reading of the spreading law in the last paragraph is a
    consequence of (ii)-(iii) for quadratic generators and says nothing about non-quadratic
    dynamics. The mathematics is standard (compactness of the fermionic Bogoliubov group, Araki's
    quasi-free automorphisms; the KMS condition) and is transport-absent; what is new is its
    application to the series' two flows. The core verdict (the unitary real-time flow is the rotor
    at imaginary rapidity) is already in field-theory.boost-modes; new here are the generality of
    (i)-(ii) over every frame *-structure and every clock, the positivity counterexample (iv), the
    KMS-swap identity (v) and the consequence for the spreading law. Bookkeeping for the maintainer:
    op.which-boost-flow-is-time can be marked resolved on the naming, with a successor problem,
    real-time spreading on the CAR windows requires non-quadratic dynamics. This result reclassifies
    the growth step of scrambling.spreading-law-chaos-bound-saturated as a rotor-flow
    (imaginary-time) step; that claim is recorded under tension_with (a claim cannot be an about
    target, and a pinned contradicts between proved claims is not appropriate here).
---

## formal
Let $\Cl(p,q)$, $p + q \ge 2$, carry the frame $*$-structure of Theorem \claimref{tower.structure-tower-c-norms} ($x^{*} = x$ for a frame generator with $Q(x) = 1$, $x^{*} = -x$ for one with $Q(x) = -1$, extended as an antiautomorphism, conjugate-linear on the complexification), let $V$ be its vectors, $E(x,y) := \br{x\,y^{*}}_{0}$, positive definite on $V$ with the frame orthonormal, and $h$ the same expression on $V_{\C}$, a positive Hermitian form. Write $\operatorname{ad}_{B}x = Bx - xB$.
\begin{enumerate}
\item[(i)] For every bivector $B$, $\operatorname{ad}_{B}$ preserves $V$ and its $E$-adjoint is $\operatorname{ad}_{B^{*}}$. Every bivector splits uniquely as $B = B_{c} + B_{b}$ with $B_{c}^{*} = -B_{c}$ (spanned by $e_{i}e_{j}$ with $Q(e_{i}) = Q(e_{j})$) and $B_{b}^{*} = B_{b}$ (spanned by $e_{i}e_{j}$ with $Q(e_{i}) = -Q(e_{j})$, the boosts). The rotor flow $\operatorname{Ad}(e^{\lambda B})$ is a $*$-automorphism for all $\lambda$ if and only if $B_{b} = 0$, and then it acts on $V$ by $E$-orthogonal maps, with $\operatorname{ad}_{B}$ of purely imaginary spectrum.
\item[(ii)] No clock in the sense of Lemma \claimref{scrambling.clock-inventory-boundary-modes}(ii) (adjoint action semisimple with a nonzero real eigenvalue) generates a $*$-automorphic flow, for any frame $*$-structure. The atom boost $\sigma = v^{*}v - vv^{*}$ is $*$-symmetric, $\operatorname{ad}_{\sigma}$ has weights $-2, +2$ on $v, v^{*}$, and its rotor flow $v \mapsto e^{-\lambda}v$, $v^{*} \mapsto e^{\lambda}v^{*}$ is not a $*$-map.
\item[(iii)] Let $H = H^{*}$ be a quadratic element of a complexified window (for instance $K = \sigma/2$, $\sum_{j}\omega_{j}K_{j}$, or these plus any hop or pairing coupling). Then $\operatorname{ad}_{H}$ is $h$-Hermitian on $V_{\C}$, $\operatorname{Ad}(e^{itH})$ is a $*$-automorphism acting on $V_{\C}$ by $h$-unitary maps (the compact Bogoliubov group, Fact \claimref{rungs.imported-fock-representation-bogoliubov-group}), and $\operatorname{Ad}(e^{\lambda H})$ with $\lambda$ real and nonzero is not a $*$-map unless $H$ is a scalar. If $H = \kappa K_{\mathrm{tot}} + W$ with $K_{\mathrm{tot}} = \sum_{j}(N_{j} - \tfrac12)$ and $W$ gauge-invariant, the boost multiplies every evolved mode operator by the common phase $e^{-i\kappa t}$ and the moduli of its coefficients do not depend on $\kappa$. If $W = g(a_{1}^{*}a_{2}^{*} + a_{2}a_{1})$ on two modes, $\operatorname{ad}_{H}$ on $(a_{1}, a_{2}^{*})$ is $\left(\begin{smallmatrix}-\kappa & -g\\ -g & \kappa\end{smallmatrix}\right)$ with square $\Omega^{2} = \kappa^{2} + g^{2}$: the unitary flow is trigonometric at frequency $\Omega$ and moves at most $g^{2}/(\kappa^{2} + g^{2})$ of the weight of $a_{1}$ onto $a_{2}^{*}$, so in real time the boost detunes, while the real-parameter flow grows as $\cosh(\Omega\lambda)$.
\item[(iv)] The common-rapidity rotor flow $\alpha_{\lambda}(a_{j}) = e^{-\lambda}a_{j}$ does not map states to states: for every $\lambda \neq 0$ there are an even pure two-mode state $\omega = c\ket{00} + s\ket{11}$ (a thermofield pair, $c\cosh 2\lambda > 1$) and $X = a_{1}a_{2} - t$ with $\omega(\alpha_{\lambda}(X^{*}X)) = s^{2}(1 - c^{2}\cosh^{2}2\lambda) < 0$.
\item[(v)] The rotor flow is the phase flow $\tau_{t} = \operatorname{Ad}(e^{itK})$ at imaginary parameter, $\operatorname{Ad}(e^{\lambda K}) = \tau_{-i\lambda}$, and at rapidity $\beta$ it is the KMS swap of the Gibbs state $\omega_{\beta}$ of $K$: $\omega_{\beta}(A\,\operatorname{Ad}(e^{-\beta K})(B)) = \omega_{\beta}(BA)$ for all $A, B$.
\end{enumerate}
Hence, taking a physical time evolution to be a one-parameter group of $*$-automorphisms that preserves the state space, the time evolution of a window is the phase flow, the boost dynamics of Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics}, and the rotor flow is its continuation into the KMS strip; by (i), (ii), (iv) and (v) this holds for every bivector and every clock, not only for quadratic dynamics. On the CAR windows, the growth step of Assumption \claimref{scrambling.spreading-law-chaos-bound-saturated}, that a quadratic generator containing the boost scales the ladder operators by $e^{\pm\kappa t}$, holds for the rotor flow only: under any quadratic time evolution of the windows the $h$-norm of an evolved mode operator is conserved (the fermionic Bogoliubov group is compact) and the boost contributes a phase or a detuning, so for the quadratic dynamics that law assumes the rate $\kappa$ of $t_{*} = \kappa^{-1}\ln N$ is an imaginary-time rate, and the chaos-bound comparison of that rate with $2\pi T$ is the identity $\kappa = 2\pi/\beta$ of (R), not a statement about real-time spreading on the windows. This restriction is to the CAR windows: bosonic or geometric boosts, such as the real-time blueshift $p_{U} \mapsto e^{\kappa t}p_{U}$ of Kruskal momenta in shock-wave scrambling arguments, are unitary and grow exponentially in real time, and nothing here bears on them or on non-quadratic generators.

## technical
In the real Clifford algebra with the tower's frame $*$-structure, the bivectors split into a compact part ($*$-antisymmetric: rotations among generators of equal square) and a boost part ($*$-symmetric: mixed planes). The $E$-adjoint of $\operatorname{ad}_{B}$ on vectors is $\operatorname{ad}_{B^{*}}$, so a bivector flow preserves the $*$-structure exactly when it has no boost part, and such flows act on vectors orthogonally, with imaginary spectrum. A clock, whose adjoint action has a real nonzero eigenvalue, is therefore never a $*$-automorphism, and the atom's boost rotor, which scales $v$ and $v^{*}$ by $e^{\mp\lambda}$, is not one.

On the complexified windows every self-adjoint quadratic generator $H$ gives the unitary flow $\operatorname{Ad}(e^{itH})$, acting on the mode operators through the compact Bogoliubov group; the same generator at a real parameter is not a $*$-map. For a gauge-invariant coupling the boost only multiplies every mode operator by a common phase; for a pairing coupling it detunes, capping the transferred weight at $g^{2}/(\kappa^{2} + g^{2})$, while the real-parameter flow of the same generator grows as $\cosh$. The rotor flow at common rapidity sends a thermofield pair to a functional that is negative on a positive element, so it is not an evolution of states. It is the phase flow at imaginary time, and at rapidity $\beta$ it is the KMS swap of the Gibbs state.

So, taking a time evolution to be a group of $*$-automorphisms preserving the states, the phase flow is the window's time evolution and the rotor flow its KMS-strip continuation. On the CAR windows the spreading law's exponential growth $e^{\kappa t}$ is the rotor flow's: under any quadratic time evolution of the windows the norm of an evolved mode operator is conserved and the boost supplies a phase or a detuning, so for the quadratic dynamics the law assumes, the chaos-bound comparison reduces to $\kappa = 2\pi/\beta$, which is (R). Bosonic or geometric boosts, such as the real-time blueshift of Kruskal momenta, do grow exponentially in real time and are outside this statement.

## lay
The papers used one name for two motions built from the same ingredient: a stretching that makes some quantities grow exponentially, and a turning that rotates each quantum mode's phase like a clock hand. This result decides which one is the real passage of time. Only the turning respects the rules of quantum theory: the stretching would turn some legitimate quantum states into impossible ones with negative probabilities. The stretching is the turning run in imaginary time, the device behind black-hole temperature, and at one full thermal period it is exactly the swap that defines thermal equilibrium. The series' fast-scrambling argument for the boundary modes relied on the stretching's exponential growth. For the simple (quadratic) dynamics of those fermionic modes, that growth belongs to imaginary time, not to the actual evolution, and the claimed match with the quantum chaos bound reduces to the definition of the temperature. This is a statement about the series' fermionic boundary modes only: in standard treatments of black-hole scrambling, other ingredients (gravitational blueshift, interactions) do grow exponentially in real time.

## one-liner
Only the phase flow is a $*$-automorphism (every clock's rotor flow is not, and fails positivity on a thermofield pair), the rotor flow is its KMS-strip continuation, and, for the quadratic dynamics the stored law assumes, the spreading law's $e^{\kappa t}$ is an imaginary-time rate on the CAR windows.
