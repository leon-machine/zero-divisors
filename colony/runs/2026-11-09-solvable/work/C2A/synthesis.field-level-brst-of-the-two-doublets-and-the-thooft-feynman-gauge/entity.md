---
id: synthesis.field-level-brst-of-the-two-doublets-and-the-thooft-feynman-gauge
kind: claim
version: 1
title: "'t Hooft gauge fixing of the two scalar doublets: exactness, mixing and common masses"
status: proved
region: synthesis
subject: quantum-fields
tags: [gauge-fields, recovers-known-physics]
proposed_by:
  kind: ai
  session: 2026-11-09-solvable
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-09-solvable
review: draft
derivations:
- name: main
  uses:
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent@3
  - synthesis.imported-brst-kugo-ojima-strocchi-and-gribov@1
  - synthesis.quartet-homotopy-makes-gluon-and-massive-vector-physical-states-positive-at-every-number-of-quanta@4
  - synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_doublets_as_ga_quaternions_carry_the_gauge_algebra
- kind: check
  ref: check.py::check_scalar_brst_is_nilpotent_for_every_vacuum
- kind: check
  ref: check.py::check_covariant_derivative_kinetic_term_and_invariants
- kind: check
  ref: check.py::check_thooft_fermion_is_exact_and_cancels_the_mixing
- kind: check
  ref: check.py::check_thooft_feynman_masses_for_the_neutral_aligned_vacuum
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent
extraction:
  open_problem: op.qft-non-abelian-gauge-fields
  note: >-
    Attack on the item "Higgs-sector BRST: the field-level differential with the Goldstone and doublet terms (s phi)"
    of op.qft-non-abelian-gauge-fields, the part on the differential and the gauge fixing; the breaking pattern is
    taken as input here. Stored and used: the jet algebra, the bivector realisation of su(2) + su(3) + u(1) and the
    nilpotent differential on the gauge fields, with the Yang-Mills density and the covariant gauge fixing
    (synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent, which left out the Goldstone
    and doublet terms); the two hypercharge-1/2 doublets of the scalar sector
    (synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum) and the neutral aligned vacuum with its
    Goldstone rank 3 and the Feynman-'t Hooft one-particle charge
    (synthesis.quartet-homotopy-makes-gluon-and-massive-vector-physical-states-positive-at-every-number-of-quanta (iii),
    (v)). The doublets are even elements of Cl(3,0) on e_0, e_1, e_2 (GA quaternions): the weak bivectors act on the
    left, hypercharge by y e_12 on the right, so no imaginary unit enters. New: the extension s h = -g rho(c)(v + h)
    and its nilpotency on all fields for every constant vacuum and every hypercharge normalisation; the covariance of
    D phi and the invariance of the kinetic term and of the quadratic invariants; the 't Hooft gauge-fixing fermion,
    its exactness and the cancellation of the vector-Goldstone mixing up to a total derivative for every vacuum and
    every xi; the equality of vector, Goldstone and ghost masses at xi = 1, read off the Lagrangian for the neutral
    aligned vacuum. Prior art, not premises, cited from memory: G. 't Hooft, Nucl. Phys. B 35 (1971) 167 and K.
    Fujikawa, B. W. Lee and A. I. Sanda, Phys. Rev. D 6 (1972) 2923 (the R_xi gauges); C. Becchi, A. Rouet and R.
    Stora, Ann. Phys. 98 (1976) 287, and I. V. Tyutin (1975) (the BRST transformation with scalars); T. Kugo and I.
    Ojima, Prog. Theor. Phys. Suppl. 66 (1979) 1. The standard construction is Fact
    synthesis.imported-brst-kugo-ojima-strocchi-and-gribov (i). The nilpotency of the extended differential is used
    here as a lemma (clause (ii)); the main content is the gauge fixing, (iv) and (v). Not treated here: whether the
    quadratic part of the gauge-fixed action is a symmetry of the free differential away from a stationary vacuum of
    the potential, the Goldstone rank as a function of the vacuum, and the selection of the breaking pattern by the
    potential. The masses depend on the normalisation of y and of kappa on the u(1), which the stored
    differential leaves open, so no ratio of masses is claimed. What is not claimed: the potential, the derivation of
    the breaking pattern, the interacting BRST charge on the Krein space, renormalisation, anomalies and the Gribov
    problem. Transport-absent.
---

## formal
In the jet algebra of Theorem \claimref{synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent}, with the gauge algebra $\su(2) \oplus \su(3) \oplus \uu(1)$ of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite} realised there by bivectors ($T_{1}, T_{2}, T_{3} = \tfrac12e_{12}, \tfrac12e_{20}, \tfrac12e_{01}$ in $\Cl(3,0)$ on $e_{0}, e_{1}, e_{2}$, colour on $e_{3}, \dots, e_{8}$, $T_{12} = \tfrac12J$), the structure constants $f_{ab}{}^{c}$ and the invariant form $\kappa_{ab} = -\langle T_{a}T_{b}\rangle_{0}$, add the two doublets of the scalar sector: each is an even element $\phi = \phi^{0} + \phi^{1}e_{12} + \phi^{2}e_{02} + \phi^{3}e_{01}$ of $\Cl(3,0)$, with $\rho(T_{a})\phi = T_{a}\phi$ ($a = 1, 2, 3$), colour acting by $0$, and $\rho(T_{12})\phi = y\,\phi e_{12}$ for a rational $y \ne 0$ (the normalisation of hypercharge); $\langle\phi, \psi\rangle = \langle\widetilde{\phi}\psi\rangle_{0}$. Write $\phi = v + h$ with $v$ constant (the vacuum) and $h = (h^{1}, \dots, h^{8})$ even jet symbols, $\rho(c) = c^{a}\rho(T_{a})$, $D_\mu\phi = \partial_\mu h + g\rho(A^{a}_{\mu}T_{a})\phi$, $W_{a} = \rho(T_{a})v$ and $\Gamma_{ab} = \langle W_{a}, W_{b}\rangle$. Extend the stored differential by
\[
sh = -g\,\rho(c)(v + h), \qquad s(h_{J}) = \partial_{J}(sh).
\]
\begin{enumerate}
\item[(i)] \emph{(The doublets; proved.)} $\rho$ is a representation of the twelve generators by maps antisymmetric for $\langle\cdot,\cdot\rangle$, for every $y$; with hypercharge acting on the left it is not.
\item[(ii)] \emph{(Lemma: nilpotency; proved.)} $s^{2} = 0$ on the whole jet algebra, for every constant $v$, every $y$ and every $g$; with $sh = +g\rho(c)(v + h)$ it fails.
\item[(iii)] \emph{(Invariance; proved.)} $s(D_\mu\phi) = -g\rho(c)D_\mu\phi$; $s$ annihilates $\tfrac12\langle D_\mu\phi, D^{\mu}\phi\rangle$ and every polynomial in $|\phi_{1}|^{2}$, $|\phi_{2}|^{2}$, $\langle\phi_{1}, \phi_{2}\rangle$, $\langle\phi_{1}, \phi_{2}e_{12}\rangle$, so with the stored Yang-Mills density, $\mathcal{L} = \kappa_{ab}\langle F^{a}F^{b}\rangle_{0} + \tfrac12\langle D_\mu\phi, D^{\mu}\phi\rangle - V$ is $s$-invariant for every such $V$.
\item[(iv)] \emph{(The 't Hooft gauge; proved.)} For $\Psi_{\xi} = \kappa_{ab}\bar c^{a}\big(\nabla\cdot A^{b} + \tfrac{\xi}{2}B^{b}\big) - \xi g\,\bar c^{a}\langle W_{a}, h\rangle$, with $F^{a} = \nabla\cdot A^{a} - \xi g\,\kappa^{ab}\langle W_{b}, h\rangle$,
\[
s\Psi_{\xi} = \kappa_{ab}B^{a}F^{b} + \tfrac{\xi}{2}\kappa_{ab}B^{a}B^{b} - \kappa_{ab}\bar c^{a}\,\nabla\cdot(Dc)^{b} - \xi g^{2}\,\bar c^{a}\langle W_{a}, \rho(c)(v + h)\rangle, \qquad s(s\Psi_{\xi}) = 0,
\]
and after eliminating $B$ ($B^{a} = -F^{a}/\xi$, giving $-\tfrac{1}{2\xi}\kappa_{ab}F^{a}F^{b}$) the terms of $\tfrac12\langle D_\mu\phi, D^{\mu}\phi\rangle - \tfrac{1}{2\xi}\kappa_{ab}F^{a}F^{b}$ bilinear in $A$ and $h$ are exactly $g\,\partial_\mu\big(A^{a\mu}\langle W_{a}, h\rangle\big)$, a total derivative, for every $v$ and $\xi$; with the opposite sign of the 't Hooft term they are not a total derivative.
\item[(v)] \emph{(Masses; proved, computed.)} The squared masses of the vectors, the ghosts and the Goldstone modes are the eigenvalues of $g^{2}\kappa^{-1}\Gamma$, $\xi g^{2}\kappa^{-1}\Gamma$ and $\xi g^{2}W\kappa^{-1}W^{\mathsf T}$ (on the eight scalars); the nonzero ones agree with multiplicity, so at $\xi = 1$ every massive vector, its Goldstone mode and its ghosts share one mass. For the neutral aligned vacuum $v = (v_{1}, 0, 0, 0), (v_{2}, 0, 0, 0)$ (Goldstone rank $3$, as stored), the nonzero eigenvalues of $\kappa^{-1}\Gamma$ equal to $v_{1}^{2} + v_{2}^{2}$ (twice) and $(v_{1}^{2} + v_{2}^{2})(1 + \tfrac43y^{2})$; computed at $v_{1} = 1$, $v_{2} = 2$, $y = \tfrac12$: $\det(t - \kappa^{-1}\Gamma) = t^{9}(t - 5)^{2}(t - \tfrac{20}{3})$ and $\det(t - W\kappa^{-1}W^{\mathsf T}) = t^{5}(t - 5)^{2}(t - \tfrac{20}{3})$.
\item[(vi)] \emph{(Computed.)} (i) for $y = \tfrac12, \tfrac13$; (ii) on the $40$ generators $h^{i}_{J}$ with $|J| \le 1$ and the $72$ underived gauge, ghost and antighost generators, as polynomials in $g$ and eight formal vacuum components; (iii) on all $32$ components of $D\phi$, the kinetic term and the four invariants, with two non-invariant bilinears as controls; (iv) term by term, $256$ mixing monomials at $\xi = 1, 3$; (v) from the computed Lagrangian.
\end{enumerate}
\emph{Reading.} With the differential extended to the scalar sector (nilpotent for every vacuum, the lemma (ii)), the 't Hooft-Feynman gauge with the series' two doublets is an exact gauge fixing in which the vector-Goldstone mixing cancels and the vectors, Goldstone modes and ghosts share their masses, the gauge in which the stored quartet result treats the massive vectors. The vacuum, and hence the breaking pattern, is an input here.

## technical
The stored field-level BRST differential of the derived gauge fields left out the scalars. Here the series' two hypercharge-$\tfrac12$ doublets are written as even elements of $\Cl(3,0)$, with the weak bivectors acting on the left and hypercharge by a multiple of $e_{12}$ on the right, so the gauge algebra acts by real antisymmetric maps and no imaginary unit appears. The differential $sh = -g\rho(c)(v + h)$ around any constant vacuum $v$ squares to zero on all fields, the covariant derivative transforms covariantly, and the kinetic term and the four quadratic invariants of two doublets are BRST-invariant. The 't Hooft gauge-fixing fermion, which adds $-\xi g\,\bar c^{a}\langle\rho(T_{a})v, h\rangle$ to the covariant one, is exact, and its gauge-fixing function cancels the mixing between vectors and Goldstone modes up to a total derivative for every vacuum. In the Feynman-'t Hooft gauge the massive vectors, their Goldstone modes and their ghosts have one common mass matrix; for the neutral aligned vacuum the Goldstone map has rank three, as stored.

## lay
In the series' version of the Standard Model, the forces have a mathematical bookkeeping device, BRST symmetry, that makes their quantum theory consistent; it had been written down for the force fields alone. Here it is extended to the two Higgs-like scalar fields of the series, written in geometric algebra as four-component quantities on which the weak force acts from one side and hypercharge from the other. The extended symmetry is consistent whatever value the scalars settle at, and in the standard gauge choice due to 't Hooft the unwanted mixing between the force fields and the would-be Goldstone particles cancels, while the massive force carriers, their Goldstone partners and the bookkeeping ghost fields all share the same masses. Which way the symmetry breaks is not decided here; it is put in by hand.

## one-liner
With the two doublets as even elements of $\Cl(3,0)$ (weak bivectors on the left, hypercharge $y\,e_{12}$ on the right), $sh = -g\rho(c)(v + h)$ extends the stored differential nilpotently for every vacuum; the 't Hooft fermion $\kappa\bar c(\nabla\cdot A + \tfrac{\xi}{2}B) - \xi g\bar c^{a}\langle\rho(T_{a})v, h\rangle$ is exact, cancels the vector-Goldstone mixing up to a total derivative, and at $\xi = 1$ gives vectors, Goldstones and ghosts one mass matrix (rank $3$ for the neutral aligned vacuum).
