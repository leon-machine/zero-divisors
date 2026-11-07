---
id: synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom
kind: claim
version: 1
title: 'The transverse bivector is the even complex unit of the radial atom'
status: proved
region: synthesis
subject: descent
tags: [pseudoscalar-and-centre, car-algebra, modular-theory, hyperbolic-plane]
proposed_by:
  kind: ai
  session: maintainer-2026-11-07
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: maintainer pass 2026-11-07
review: draft
derivations:
- name: main
  uses:
  - singularity.modular-structure-completed-pair@5
  - singularity.pseudo-inverse-identities-hyperbolic-atom@4
  - std-algebra.bivector-exponential@4
  - tower.structure-tower-c-norms@10
  - singularity.kms-uniqueness-factor@6
  - primer.centre@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_transverse_plane_is_a_central_unit_of_the_atom
- kind: check
  ref: check.py::check_frame_star_is_conjugate_linear_in_the_unit
- kind: check
  ref: check.py::check_left_i4_is_not_a_scalar_of_the_atom
- kind: check
  ref: check.py::check_phase_flow_with_unit_J
- kind: check
  ref: check.py::check_gibbs_state_is_kms_for_the_J_flow
- kind: proof
  derivation: main
extraction:
  note: >-
    The completed pair of the horizon is built in the spacetime radial plane, where the field
    theory's unit I_4 anticommutes with the mode operators, so the source's scalar i on that atom
    (its phase flow, its Euclidean continuation, its KMS state) had no pseudoscalar to stand for it.
    The pseudoscalar of the orthogonal plane does: it commutes with the whole atom and squares to -1,
    and the phase flow, the rotor flow as its continuation, the Gibbs state and the KMS relation are
    written with it here. Algebra in Cl(1,3) on top of the completed pair, its hyperbolic atom, the
    exponential, the frame *-structure and KMS uniqueness for a matrix factor; no thermal premise, no
    postulate. Transport-absent (no transport completion in its cone): it fixes the unit of the
    boundary-mode results without changing any of them. Clauses (iv) to (vi) restate stored results
    with their scalar unit written as J: singularity.euclidean-rotor-where-it-lies (1)-(2) (the
    continued boost and its action on the module), singularity.kms-uniqueness-factor and
    singularity.two-kms-functionals-sign (1) (the KMS state and its occupation), and the atom case of
    synthesis.phase-flow-is-time-rotor-flow-kms-continuation (v) (the rotor flow as the phase flow at
    imaginary parameter, the KMS swap); the signs agree throughout. The new content is (i) to (iii),
    JK = I_4/2, and that the unit lies in Cl(1,3). The source's phase flow is that of T05 Thm 7.16
    (singularity.rate-rigidity-temperature-not-algebra-intrinsic) and T07 Def 2.7
    (obj.hawking.boundary-mode-algebra-windows-boost-dynamics). Literature cited from memory, as orientation only: that the modular group of a
    faithful state of a matrix algebra with density rho is conjugation by the imaginary powers of rho (finite-dimensional
    Tomita-Takesaki theory; Takesaki, Theory of Operator Algebras II, 2003).
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Created at Leon''s instruction of 7 November 2026 to resolve every imaginary unit (colony/runs/2026-11-07-ga-units/RESOLVE.md, unit principle U2): the core result the sweep cites when it writes the completed-pair atom''s and the boundary modes'' unit as J = e_2 e_3. Signs fixed here: J sigma = +I_4, Ad(e^{JtK}) v = e^{-Jt} v and v* -> e^{+Jt} v*, the rotor flow is the phase flow at t = -J lambda, KMS at tau_{J beta} = Ad(e^{-beta K}), and the modular flow of the Gibbs state is tau_{-beta t}. It also records that JK = I_4/2, and that I_4 = +J on the image of v* v and -J on that of v v*, so the two units are never identified. Referee fixes of 7 November 2026, folded into version 1: (i) now states that the centraliser of the atom in Cl(1,3) is the quaternion algebra span{1, J, e_0 e_1 e_2, e_0 e_1 e_3}, that J is up to sign its only even unit of square -1 (fixed by the transverse rotations, sign fixed by J sigma = +I_4), and that odd units such as sigma e_2 are not identified with it; the title says the even complex unit (the id is kept); (iv) names the source''s phase flow; (v) separates the continued boost on the modes, e^{theta I_4/2}, from the dual-plane rotor e^{theta J/2} on values; (vi) says the only span{1, J}-linear KMS state and, for beta != 0, not at -beta; the ledger reads transport-absent; primer.centre is added to the premises; the check tests tau_z at a mixed z = t + J theta and computes the centraliser.'
---

## formal
Work in $\Cl(1,3)$, $e_{0}^{2} = 1$, $e_{k}^{2} = -1$ ($k = 1, 2, 3$), $I_{4} = e_{0}e_{1}e_{2}e_{3}$, with the completed pair of Theorem \claimref{singularity.modular-structure-completed-pair} realised in the hyperbolic atom of the radial plane (Lemma \claimref{singularity.pseudo-inverse-identities-hyperbolic-atom}): $v = \tfrac12(e_{0} + e_{1})$, $v^{*} = \tfrac12(e_{0} - e_{1})$, $\sigma = v^{*}v - vv^{*} = e_{0}e_{1}$, $K = \sigma/2$, $P_{+} = v^{*}v = \tfrac12(1 + \sigma)$, $P_{-} = vv^{*} = \tfrac12(1 - \sigma)$. Let $J = e_{2}e_{3}$, the unit bivector of the transverse plane, and let $x \mapsto x^{*} = e_{0}\rev{x}e_{0}$ be the frame $*$-structure of Theorem \claimref{tower.structure-tower-c-norms} ($e_{0}^{*} = e_{0}$, $e_{k}^{*} = -e_{k}$, an antiautomorphism).
\begin{enumerate}
\item[(i)] \emph{(The unit.)} $J^{2} = -1$; $J$ commutes with $e_{0}$ and $e_{1}$, hence with $v$, $v^{*}$, $\sigma$ and everything they generate; $J\sigma = \sigma J = +I_{4}$, so $J = I_{4}\sigma$; and $J^{*} = -J$. $J$ is a choice among the units that commute with the atom, fixed as follows: the centraliser of $e_{0}, e_{1}$ in $\Cl(1,3)$ is $\mathrm{span}\{1, J, e_{0}e_{1}e_{2}, e_{0}e_{1}e_{3}\}$, a quaternion algebra; $\pm J$ are its only elements of square $-1$ in the even subalgebra (equivalently, the only ones fixed by the rotations of the transverse plane), and the sign of $J$ is fixed by $J\sigma = +I_{4}$. Odd units such as $\sigma e_{2} = e_{0}e_{1}e_{2}$, which anticommutes with $J$, also square to $-1$, commute with the atom and are sent to their negatives by $*$; they are not identified with $J$.
\item[(ii)] \emph{(The atom over $J$.)} The real algebra $\Aa = \Cl(1,1) \oplus \Cl(1,1)J$ generated by $e_{0}$, $e_{1}$ and $J$ has real dimension $8$ and centre $\mathrm{span}\{1, J\}$, a field isomorphic to $\C$; over that field it is spanned by $1$, $v$, $v^{*}$, $v^{*}v$, so it is the CAR algebra of one mode, a full $2 \times 2$ matrix algebra over $\mathrm{span}\{1, J\}$. The frame $*$ maps $\Aa$ to itself, sends $v$ to $v^{*}$, fixes $\sigma$ and $K$, and is conjugate-linear over the field ($J^{*} = -J$).
\item[(iii)] \emph{(The left unit $I_{4}$ is not a scalar of the atom.)} $I_{4} = J\sigma$ lies in $\Aa$ but is not central: it anticommutes with $e_{0}$, $e_{1}$, $v$, $v^{*}$, and for vectors $a, b$ of the radial plane $(I_{4}a)(I_{4}b) = +ab$, whereas $(Ja)(Jb) = -ab$. On the spectral projectors $I_{4}P_{\pm} = \pm JP_{\pm}$: the two units agree on the image of $v^{*}v$ and are opposite on that of $vv^{*}$, and they are not identified.
\item[(iv)] \emph{(The phase flow.)} $JK = I_{4}/2$ and $(2JK)^{2} = -1$, so $e^{JtK} = \cos\tfrac{t}{2} + 2JK\sin\tfrac{t}{2}$, and for real $t$
\[
\tau_{t}(x) := e^{JtK}\,x\,e^{-JtK}, \qquad \tau_{t}(v) = e^{-Jt}v, \qquad \tau_{t}(v^{*}) = e^{+Jt}v^{*},
\]
infinitesimally $JKv - vJK = -Jv$ and $JKv^{*} - v^{*}JK = +Jv^{*}$. $(e^{JtK})^{*} = e^{-JtK}$, so $\tau$ is a one-parameter group of $*$-automorphisms of $\Aa$. The phase flow of the source on the atom (T05 Thm 7.16, T07 Def 2.7) and the flow of Theorem \claimref{singularity.kms-uniqueness-factor}, written there with a scalar unit, are $\tau_{t}$ with that unit written as $J$; the sign agrees, $v \mapsto e^{-Jt}v$. For $\sin t \neq 0$, $\tau_{t}(v) = v\cos t - Jv\sin t$ is not a vector ($Jv$ is a trivector): $\tau_{t}$ acts on values, and maps no nonzero vector to a vector.
\item[(v)] \emph{(The rotor flow is its continuation.)} For $z$ in the field $\mathrm{span}\{1, J\}$, $\tau_{z} := \operatorname{Ad}(e^{JzK})$ is an automorphism of $\Aa$ with $\tau_{z}(v) = e^{-Jz}v$ and $\tau_{z}(v^{*}) = e^{Jz}v^{*}$, and at $z = -J\lambda$, $\lambda$ real, $e^{JzK} = e^{\lambda K} = R_{\lambda}$, so $\tau_{-J\lambda}(v) = e^{-\lambda}v$ and $\tau_{-J\lambda}(v^{*}) = e^{\lambda}v^{*}$: the rotor flow of Theorem \claimref{singularity.modular-structure-completed-pair}(2) is the phase flow at the parameter $t = -J\lambda$, that is $\lambda = Jt$. The continued boost on the mode operators, $e^{J\theta K} = e^{\theta I_{4}/2}$, and the dual-plane rotor $e^{\theta J/2}$ that the continuation gives when its unit is read as $I_{4}$ acting on values are different objects acting on different things: the second is central in $\Aa$ and acts trivially on it, so the two readings do not contradict each other.
\item[(vi)] \emph{(KMS and the modular flow.)} Let $T(x) = 2\br{x}_{0} - 2J\br{Jx}_{0}$, the trace of $\Aa$ over $\mathrm{span}\{1, J\}$ ($T(1) = 2$, $T(Jx) = JT(x)$, $T(xy) = T(yx)$), and for real $\beta$ let $\omega_{\beta}(x) = T(e^{-\beta K}x)/T(e^{-\beta K})$. Then $\omega_{\beta}$ is a state ($\omega_{\beta}(x^{*}x) > 0$ for $x \neq 0$), $\omega_{\beta}(v^{*}v) = 1/(1 + e^{\beta})$, and it satisfies the KMS condition of $\tau$ at $\beta$ with the unit $J$,
\[
\omega_{\beta}\bigl(x\,\tau_{J\beta}(y)\bigr) = \omega_{\beta}(yx) \quad (x, y \in \Aa), \qquad \tau_{J\beta} = \operatorname{Ad}(e^{-\beta K}),
\]
and, for $\beta \neq 0$, not at $-\beta$; it is the only $\mathrm{span}\{1, J\}$-linear state of $\Aa$ that does (Theorem \claimref{singularity.kms-uniqueness-factor}, for the matrix factor $\Aa$ over the field $\mathrm{span}\{1, J\}$). With $\varrho = e^{-\beta K}/T(e^{-\beta K})$ and $\varrho^{Jt} := e^{Jt\ln\varrho}$, $\operatorname{Ad}(\varrho^{Jt}) = \tau_{-\beta t}$, so $\operatorname{Ad}(\varrho^{Jt})(v) = e^{J\beta t}v$: the flow that is the modular group of $\omega_{\beta}$ in a matrix factor is the phase flow at $-\beta t$, written with $J$.
\end{enumerate}

## technical
The completed pair $v = \tfrac12(e_{0} + e_{1})$, $v^{*} = \tfrac12(e_{0} - e_{1})$ lives in the spacetime radial plane, where the field theory's unit $I_{4}$ anticommutes with both mode operators and cannot serve as their complex scalar: $(I_{4}v)(I_{4}w) = +vw$, not $-vw$. The unit bivector of the orthogonal plane, $J = e_{2}e_{3}$, can: it squares to $-1$, commutes with $e_{0}$, $e_{1}$ and so with the whole atom, is sent to $-J$ by the frame adjoint, and with $1$ spans the centre of the atom's algebra $\Cl(1,1) \oplus \Cl(1,1)J$, which is the one-mode CAR algebra over that field. It is the even such unit: the elements commuting with the atom form a quaternion algebra, whose odd units, such as $\sigma e_{2}$, also square to $-1$ but are not identified with $J$, and $J$ is the one fixed by rotations of the transverse plane, with its sign set by $J\sigma = +I_{4}$. The two units are related by $J\sigma = I_{4}$ with $\sigma = e_{0}e_{1}$: $I_{4}$ equals $J$ on the occupied projector $v^{*}v$ and $-J$ on $vv^{*}$. Written with $J$, the phase flow is $\operatorname{Ad}(e^{JtK})$ with $K = \sigma/2$, and it multiplies $v$ by $e^{-Jt}$ and $v^{*}$ by $e^{+Jt}$; since $JK = I_{4}/2$ it is conjugation by $e^{I_{4}t/2}$, which is not a rotor and maps no nonzero vector to a vector. At the parameter $t = -J\lambda$ it is the real rotor flow $e^{\lambda K}$, $v \mapsto e^{-\lambda}v$. The Gibbs state of $K$, computed with the trace of the atom over $\mathrm{span}\{1, J\}$, gives occupation $1/(1 + e^{\beta})$, satisfies the KMS relation $\omega_{\beta}(x\,\tau_{J\beta}(y)) = \omega_{\beta}(yx)$ and is the only $\mathrm{span}\{1, J\}$-linear state that does, and its modular flow is $\tau_{-\beta t}$. So the store's complex phase flow, its continuation, its KMS states and its modular group on this atom are all written with $J$.

## lay
At a horizon, the graph pairs two fermion modes, one moving outwards and one inwards, and builds them from the two directions of the plane in which the horizon boosts: time and the radial direction. Quantum mechanics needs a square root of minus one that acts on these modes as an ordinary number, and the usual choice in this algebra, the spacetime volume element, does not behave as a number here, because it reverses sign when moved past either direction. The plane of the two remaining directions, the one tangent to the horizon's sphere, supplies one that does, the only one built from the even part of the algebra: it squares to minus one and commutes with everything built from time and the radial direction. This result proves that, and rewrites the modes' time evolution, its thermal state and the link between real and imaginary time with that element in place of the imaginary unit, fixing every sign.

## one-liner
For the completed pair $v = \tfrac12(e_{0} + e_{1})$, $v^{*} = \tfrac12(e_{0} - e_{1})$ with $\sigma = e_{0}e_{1}$, the transverse bivector $J = e_{2}e_{3}$ ($J^{2} = -1$, $J\sigma = +I_{4}$, $J^{*} = -J$) commutes with the atom and is its even complex unit: $\operatorname{Ad}(e^{Jt\sigma/2})$ sends $v \mapsto e^{-Jt}v$, $v^{*} \mapsto e^{+Jt}v^{*}$, is the rotor flow at $t = -J\lambda$, and its Gibbs state is KMS for $\tau_{J\beta} = \operatorname{Ad}(e^{-\beta\sigma/2})$, while $(I_{4}v)(I_{4}w) = +vw$.
