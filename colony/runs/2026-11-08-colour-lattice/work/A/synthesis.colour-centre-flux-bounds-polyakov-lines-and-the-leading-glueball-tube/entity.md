---
id: synthesis.colour-centre-flux-bounds-polyakov-lines-and-the-leading-glueball-tube
kind: claim
version: 1
title: 'Colour rotor lattice: centre flux bounds, Polyakov and baryonic lines, the glueball tube'
status: proved
region: synthesis
subject: quantum-fields
tags: [gauge-fields, rotors-and-stabilisers, recovers-known-physics, finite-models]
proposed_by:
  kind: ai
  session: 2026-11-08-colour-lattice
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-08-colour-lattice
review: draft
derivations:
- name: main
  uses:
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent@3
  - synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_colour_block_pure_spinor_and_det_one
- kind: check
  ref: check.py::check_finite_colour_group_reproduces_haar_through_degree_three
- kind: check
  ref: check.py::check_character_from_scalar_and_pseudoscalar_parts
- kind: check
  ref: check.py::check_centre_rotor_in_q_sqrt3
- kind: check
  ref: check.py::check_character_moments_and_gluing
- kind: check
  ref: check.py::check_wilson_loops_leading_coefficients
- kind: check
  ref: check.py::check_polyakov_lines_and_the_baryonic_junction
- kind: check
  ref: check.py::check_glueball_tube_leading_coefficient
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.weak-factor-rotor-lattice-strong-coupling-area-law
extraction:
  open_problem: op.qft-non-abelian-gauge-fields
  note: >-
    Attack on the item "Colour: a colour rotor lattice (none is stored) and its continuum limit" of
    op.qft-non-abelian-gauge-fields. The su(3) factor is taken in the bivector realisation of
    synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent (the eight traceless bivectors
    of the e3..e8 block commuting with J), isomorphic to the colour summand of
    standard-model.gauge-algebra-minimal-massive-composite; Wilson's lattice formulation and beta = 2N/g^2 are the
    imported Fact synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement (i). The results are
    about the centre of colour and what it forces. (a) The group at rotor level: colour rotors are the rotors of the
    block fixing the pure-spinor idempotent E, one condition that gives both J-commutation and det = 1 (at vector
    level det = 1 is that the outermorphism fixes the J-complex volume trivector), and the triplet character is
    4(<R>_0 + <R>_6) - 1 (the rotor's spinor space is the triplet plus a singlet), so Wilson's weight is the scalar
    part of the plaquette rotor, exp((4 beta/3) <U_p>_0) up to a constant, as for the weak factor; the Haar average
    of the rotor is E. (b) The centre rotor z, exact in Q(sqrt 3), and the Z3 flux chain it forces on every surviving
    term of the expansion; with it, no term of order below A contributes to an R x T fundamental loop, so (beta/18)^A
    is its leading term; the centre bound does not apply to lines of zero triality, for example three coincident lines
    joined by the volume form give exactly 1 (the adjoint loop's perimeter behaviour is argued, not proved). (c) Polyakov lines: exact zeros of P and of PP at every beta by centre symmetry, the leading
    terms (1/9)(beta/18)^(N_t r) of a pair and (1/27)(beta/18)^(3 N_t) of three lines on a baryonic junction, which
    is carried by the cubic moment. (d) The connected plaquette correlator: no connected term below order 4t, leading
    term (1/18)(beta/18)^(4t) from the tube, leading decay rate 4 ln(18/beta) per time step. The single-link moments
    of degree at most three are needed as lemmas and are derived in the check (a group of 96 rational colour rotors
    with the same invariants as SU(3) in degrees one to three), not imported. The intended home of the shared
    degree-three lemma is the sibling proposal
    synthesis.a-finite-subgroup-of-colour-shares-its-strong-coupling-expansion-through-link-degree-three, to which
    clause (iii) can be repointed in a later version. Prior art, not premises, cited from
    memory: K. G. Wilson, Phys. Rev. D 10 (1974) 2445; M. Creutz, Quarks, Gluons and Lattices (Cambridge, 1983);
    J.-M. Drouffe and J.-B. Zuber, Phys. Rep. 102 (1983) 1 (strong-coupling and character expansions, u = beta/18 for
    SU(3)); G. Muenster, Nucl. Phys. B 190 (1981) 439 (strong-coupling glueball mass, -4 ln u at leading order);
    B. Svetitsky and L. G. Yaffe, Nucl. Phys. B 210 (1982) 423 (centre symmetry and the Polyakov loop);
    K. Osterwalder and E. Seiler, Ann. Phys. 110 (1978) 440 (convergent expansion, exponential clustering at strong
    coupling). The leading values agree with these standard results; new here are the geometric-algebra forms and the
    exact derivations and checks. What is not claimed: anything beyond a fixed finite order of the expansion on a
    finite lattice; uniformity in the separation (a gap at small beta in infinite volume) is expected to follow from
    the convergent expansion of Osterwalder and Seiler (cited from memory, not imported; their clustering statement is
    not in the imported Fact); nothing about the
    continuum limit, which needs beta -> infinity, the opposite regime, so nothing here bears on the Yang-Mills
    existence and mass-gap problem. Transport-absent: the series supplies the gauge algebra; J and the pseudoscalar of
    the block play the role of the imaginary unit, and nothing uses transport.
---

## formal
Represent the $\su(3)$ summand of $\su(2) \oplus \su(3) \oplus \uu(1)$ (Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite}) as in \claimref{synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent}: the eight bivectors of the block $e_3, \dots, e_8$ of $\Cl(9,0)$ that commute with $J = e_{34} + e_{56} + e_{78}$ and are orthogonal to it. Let $P_k = e_{34}, e_{56}, e_{78}$, $I = e_{345678}$, $E = \prod_k\tfrac12(1 + IP_k)$, $\Omega_R = e_{357} - e_{368} - e_{458} - e_{467}$, $\Omega_I = e_{457} + e_{367} + e_{358} - e_{468}$, $j(v) = v\cdot J$. A colour rotor is a rotor $R$ of the block (an even element with $R\widetilde{R} = 1$ and $Rv\widetilde{R}$ a vector for every vector $v$ of the block, equivalently a product of an even number of unit vectors) with $RE = E$; $f_R(v) = Rv\widetilde{R}$. On a hypercubic lattice give each oriented link a colour rotor ($\widetilde{U}$ reversed), let $U_p$ be the plaquette product, $w(U) = \tfrac13(4\langle U\rangle_0 - 1)$, and take the weight $\prod_p\exp(\beta w(U_p))$ with Haar measure.
\begin{enumerate}
\item[(i)] \emph{(The group at rotor level.)} $E^2 = E = \widetilde{E}$, $\langle E\rangle_0 = \tfrac14$, $JE = -3IE$, and a bivector $B$ of the block has $BE = 0$ exactly when $B \in \su(3)$. Every colour rotor commutes with $J$, $f_R$ fixes $\Omega_R$ and $\Omega_I$, and $R \mapsto f_R$ is an isomorphism of the colour rotors onto $SU(3)$; for a rotation $f$ commuting with $j$ whose $j$-complex determinant is $\cos\varphi + \sin\varphi\,j$, $f(\Omega_R) = \cos\varphi\,\Omega_R + \sin\varphi\,\Omega_I$. So $\det = 1$ is $RE = E$ on rotors and $f(\Omega_R) = \Omega_R$ on vectors.
\item[(ii)] \emph{(Character.)} The triplet character, written in $\mathrm{span}\{1, I\}$ with $I$ standing for $j$, is $\chi(R) = 4(\langle R\rangle_0 + \langle R\rangle_6) - 1$; so $w = \tfrac13\mathrm{Re}\Tr$, the weight is Wilson's with $\beta = 6/g^{2}$, and $1 - w(U) = \tfrac43(1 - \langle U\rangle_0)$.
\item[(iii)] \emph{(Lemma: the link moments used.)} $\int f_R(a)\,dR = 0$, $\int(x\cdot f_R(a))(y\cdot f_R(b))\,dR = \tfrac16\big((x\cdot y)(a\cdot b) + (x\cdot j(y))(a\cdot j(b))\big)$, $\int f_R(a)\wedge f_R(b)\wedge f_R(c)\,dR = \tfrac14\big(\langle(a\wedge b\wedge c)\widetilde{\Omega_R}\rangle_0\Omega_R + \langle(a\wedge b\wedge c)\widetilde{\Omega_I}\rangle_0\Omega_I\big)$ (the cubic moment is totally antisymmetric) and $\int R\,dR = E$; in characters $\int\chi = \int\chi^2 = \int\chi^2\bar\chi = 0$, $\int\chi\bar\chi = \int\chi^3 = 1$, $\int\chi(XR)\chi(\widetilde{R}Y)\,dR = \tfrac13\chi(XY)$, $\int\chi(XR)\chi(YR)\,dR = 0$.
\item[(iv)] \emph{(Centre and flux.)} The centre is $\{1, z, z^2\}$, $z = -\prod_k(\tfrac12 - \tfrac{\sqrt3}{2}P_k)$, acting on vectors as $\omega = -\tfrac12 + \tfrac{\sqrt3}{2}j$, with $w(z) = -\tfrac12$. A moment $\int\prod_{i \le a}\chi(X_iR)\prod_{k \le b}\chi(\widetilde{R}Y_k)\,dR$ vanishes unless $a \equiv b \pmod 3$, and every nonvanishing term of the expansion of the weight carries a $\Z_3$ two-chain of plaquette charges whose boundary is minus the observable's charge chain, and has order at least the size of its support.
\item[(v)] \emph{(Fundamental against $N$-ality zero.)} On any finite box with free boundary containing an $R \times T$ rectangle $C$ of area $A$, no term of order below $A$ contributes, and $\langle w(U_C)\rangle = (\beta/18)^{A} + O(\beta^{A+1})$, the rectangle's own plaquettes being the only term of order $A$. The centre bound does not apply to lines of zero triality: for example three coincident fundamental lines along any closed path, joined by the volume form, give $\tfrac14\langle f_{U_C}(\Omega_R)\widetilde{\Omega_R}\rangle_0 = 1$ identically.
\item[(vi)] \emph{(Polyakov lines.)} On a box with $N_t$ periodic time steps and free spatial boundary, with $P(x) = \tfrac13\chi(\prod_\tau U_0(x, \tau))$: $\langle P(x)\rangle = \langle P(x)P(y)\rangle = 0$ at every $\beta$; for $y = x + re_i$, $\langle P(x)\overline{P(y)}\rangle = \tfrac19(\beta/18)^{N_tr} + O(\beta^{N_tr+1})$; for the three neighbours $x + e_i$ of a site, $\langle P(x+e_1)P(x+e_2)P(x+e_3)\rangle = \tfrac1{27}(\beta/18)^{3N_t} + O(\beta^{3N_t+1})$, from three sheets on a junction at $x$ carried by $\int\chi^3 = 1$.
\item[(vii)] \emph{(Glueball tube.)} For a spatial plaquette $p$ and its translate $p_t$ by $t \ge 1$ time steps in a box with free boundary, the connected correlator of $w(U_p)$ and $w(U_{p_t})$ has no term of order below $4t$ and equals $\tfrac1{18}(\beta/18)^{4t} + O(\beta^{4t+1})$, from the tube of $4t$ plaquettes: the leading terms decay at the rate $4\ln(18/\beta)$ per time step.
\end{enumerate}
These are statements at a fixed finite order of the strong-coupling expansion on a finite lattice; uniformity in $t$ (a gap at small $\beta$) and the continuum limit, which needs $\beta \to \infty$, are not proved, so nothing here bears on the Yang-Mills existence and mass-gap problem.

## technical
The colour factor of the derived gauge algebra is realised by bivectors of the $e_3, \dots, e_8$ block commuting with $J$. Its group is the set of rotors fixing the pure-spinor idempotent $E = \prod_k\tfrac12(1 + IP_k)$ ($I$ the block's pseudoscalar); this one condition gives both commutation with $J$ and unit determinant, and on vectors unit determinant is that the rotation fixes the $J$-complex volume trivector. Because the rotor's spinor space is the colour triplet plus a singlet, the triplet character is $4(\langle R\rangle_0 + \langle R\rangle_6) - 1$, Wilson's action is the scalar part of the plaquette rotor as for the weak factor, and the average of the rotor is $E$. The centre is a rotor $z$ acting on vectors as a cube root of unity; changing one link by $z$ shows that every term of the strong-coupling expansion that survives carries a $\Z_3$ flux sheet ending on the observable. That bounds every term from below: a rectangular fundamental loop of area $A$ has no term below order $A$ and leading term $(\beta/18)^{A}$, while the centre bound does not apply to lines of zero triality; for example three coincident lines joined by the volume form give exactly one (the adjoint loop's perimeter behaviour is argued, not proved). With periodic time, a Polyakov line and a pair of like Polyakov lines vanish at every coupling; a line and an antiline at distance $r$ give $\tfrac19(\beta/18)^{N_tr}$ at leading order, and three lines meeting at a baryonic junction give $\tfrac1{27}(\beta/18)^{3N_t}$, through the cubic Haar moment that exists for $SU(3)$ and not for $U(3)$. The connected correlator of two plaquettes $t$ steps apart has leading term $\tfrac1{18}(\beta/18)^{4t}$ from the tube joining them, a leading decay rate $4\ln(18/\beta)$. All are finite-order strong-coupling statements on a finite lattice and do not reach the continuum limit.

## lay
The strong force's symmetry, which the series derives, can be put on a spacetime lattice in the form Wilson introduced, with each link carrying a rotation of a six-dimensional geometric algebra; here the rotations are singled out by fixing one special element of the algebra. The symmetry has a three-element centre, and that centre controls which configurations can contribute when the coupling is strong. Exactly at leading order: a quark and antiquark are bound with a cost growing with the area between them, three quarks can bind at a single junction as in a baryon, and the correlation between two plaquettes falls, at leading order, by a definite factor per time step (the strong-coupling estimate usually read as the lightest glueball's mass; that reading needs uniformity in the separation, not proved here). All of this holds only at strong coupling on a lattice of finite spacing. It says nothing about the continuum theory, and it makes no progress on the open problem of proving that quantum Yang-Mills theory exists and has a mass gap.

## one-liner
On Wilson's lattice with colour rotors of the $e_3..e_8$ block (rotors fixing the pure-spinor idempotent $E$, so $\det = 1$; character $4\langle R\rangle_{0+6} - 1$), the centre rotor forces a $\Z_3$ flux sheet on every surviving term, so a rectangular fundamental loop has leading term $(\beta/18)^{A}$ with nothing below, Polyakov lines vanish, a pair gives $\tfrac19(\beta/18)^{N_tr}$, a baryonic junction $\tfrac1{27}(\beta/18)^{3N_t}$, and the plaquette correlator $\tfrac1{18}(\beta/18)^{4t}$; finite-order lattice statements only, not touching the mass-gap problem.
