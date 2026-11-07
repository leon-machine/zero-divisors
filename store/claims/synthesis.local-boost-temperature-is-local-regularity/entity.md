---
id: synthesis.local-boost-temperature-is-local-regularity
kind: claim
version: 5
title: 'Local boost temperature is local regularity'
status: proved
region: synthesis
subject: einstein
tags: [thermal-premises, modular-theory, horizons, hawking-temperature, forcing-and-uniqueness]
proposed_by:
  kind: ai
  session: 2026-10-22-cloc
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle (U1 to U6)
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: 'consistency pass, version-1 clause numbers of the local-horizon premise named, and the signature sentence made exact'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: draft
about:
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - singularity.euclidean-section-period@6
  - angle.imported-theorems-deliver-their-hypotheses@3
  - singularity.kms-uniqueness-factor@6
  - hawking.gibbs-states-are-kms-conversely-finite@4
  - singularity.modular-theory-matrix-factor-proved-outright@6
  - hawking.kms-restricts-invariant-subalgebras@3
  - hawking.imported-kms-passes-inductive-limits@1
  - hawking.full-uniqueness-given-dynamics@3
  - singularity.rate-rigidity-temperature-not-algebra-intrinsic@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_local_boost_period
- kind: check
  ref: check.py::check_acceleration_temperature
- kind: check
  ref: check.py::check_diamond_flow_unit_boost
- kind: check
  ref: check.py::check_window_kms_iff_modular
- kind: proof
  derivation: main
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The clauses (ii) and (iii) cited are those of version 1 of the local-horizon premise (now (R_loc) and a dropped modular clause), now said; the sign sentence held for the round-sphere-positive tensor in (+,-,-,-), while in the store sign k = R_0101/3 is unchanged, now said (checked on de Sitter, v/r03_checks.py).'
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle two units act, named once in the proof and not identified: the boundary-mode algebra and its window flows use J = e_2 e_3 (U2; synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom, cited in the formal level): e^{-J w_j lambda}, Ad(e^{J lambda K}), the modular flow rho^{Js} = Ad(e^{-J beta K s}), tau_{J beta} and the KMS strip F(lambda + 2 pi J) of (R_loc); the Wick continuation lambda = -I_5 theta of the line element''s rapidity coordinate uses the central unit I_5 of Cl(2,3) (U3; std-algebra.complexification-is-the-odd-extension), as in the cited Proposition singularity.euclidean-section-period; the Definition''s mode-set letter J is written calligraphic where it would clash with the unit; the outside_ga declaration is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced, by Leon''s ruling R1 (7 November 2026): the boundary-mode flow e^{-iw_j lambda}, the window flows Ad(e^{i lambda K}), the modular flow rho^{is} and the KMS strip lambda + 2 pi i keep i, since the boundary modes descend from T05''s atom, whose mode operators anticommute with I_4; the Wick continuation lambda = -i theta of the induced metric also stays. Declared (version and levels unchanged).'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  open_problem: op.derive-c-loc
  note: >-
    On (C_loc), clauses (ii) and (iii). (1) Derived: the geometric half. At any point and null
    direction the boost-plane metric in Riemann normal coordinates to second order is rapidity
    independent with F'(0) = 1 for every curvature tensor, so the Euclidean section of the local boost
    is regular exactly at rapidity period 2 pi, and T = a/2 pi in the observers' proper time up to a
    relative correction -(3/2) k rho^2 + O(rho^3); a small diamond's conformal Killing field has unit
    surface gravity at its edge. (2) On every window, a state is KMS at beta for a quasi-free phase flow
    iff it is faithful with modular group the flow at -beta s, so clause (iii), read on the whole mode
    algebra, adds nothing to clause (ii). (3) Assumed, not derived: the thermal half. Clauses (ii) and
    (iii) together are the joint KMS condition (R_loc) for the local boost on whole windows: the
    local-boost form of the condition defining the I-state, which at a Schwarzschild horizon the store
    obtains from (R) for single-mode marginals together with the joint quasi-freeness of (Q). (R_loc)
    is a new premise, stronger than the local form of (R) alone. Rate rigidity shows that some
    reference to geometry is unavoidable. Fix round 2026-10-22-cloc: restated after review (the earlier
    identification of (R_loc) with (R) was overstated); remainder in T corrected to O(rho^3);
    signature stated; tautological KMS sub-check replaced by a test of Ad(G) against the imaginary-time
    flow on the generators. Transport-absent. Hislop-Longo and Takesaki are cited from memory and not
    used.
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity (DICTIONARY sections 9 and 14 item 5): the point is a point of the invertible region of a gravitational field on flat spacetime, Riemann normal coordinates are a normal gauge at p (hb(p) = 1, Omega(p) = 0, straight background lines through p geodesic), the metric expansion is that of the derived metric with the curvature read from the field strength, and the Euclidean section is regular at its tip, the fixed point p of the local boost in the boost plane (local, one chart). Signature (-,+,+,+) kept as declared. Statements (i) to (iii) and their strength unchanged; proof given a pointer to the dictionary Fact.'
---

## formal
Signature $(-,+,+,+)$ in this statement and its proof; in signature $(+,-,-,-)$ with the Riemann tensor still positive on spheres every component $R_{abcd}$ with all indices down changes sign, so $k$ below is $-R_{0101}/3$ there, while with the store's curvature sign (minus that tensor) it is $R_{0101}/3$ unchanged. The clause numbers (i), (ii) and (iii) of Premise \claimref{synthesis.c-loc-local-horizon-premise} used here are those of its version 1 (clause (i) the mode count and entropy, clause (ii) the temperature, clause (iii) the modular flow); the current version states the entropy as (Loc), the temperature as (R$_{\mathrm{loc}}$), and records the rest under ``Not part of this premise''. Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), $p$ a point of its invertible region, $\ell$ a future physically null direction at $p$, $n$ the other null direction of a boost plane through $p$ containing $\ell$, and $\mathcal{H}_{p,\ell}$ the local Rindler horizon of Premise \claimref{synthesis.c-loc-local-horizon-premise}; let $D$ be a causal diamond about $p$ of edge radius $L$. Leading order means leading order in the size of the patch against the scale of the field strength $\mathcal{R}$ at $p$.
\begin{enumerate}
\item[(i)] \emph{(The geometric half, derived.)} In a normal gauge at $p$ (Riemann normal coordinates: a displacement gauge in which the straight background lines through $p$ are the geodesics of the derived metric, with $\hb(p) = 1$ and $\Omega(p) = 0$), the derived metric is $g_{ab} = \eta_{ab} - \tfrac13 R_{acbd}x^{c}x^{d} + O(x^{3})$, with $x$ the background displacement from $p$ and $R_{acbd}$ the curvature at $p$, read from the field strength in the signature of this statement. On the boost plane through $p$, with $x = \rho(\sinh\lambda, \cosh\lambda, 0, 0)$, the metric induced by the terms up to second order is
\[
d\rho^{2} - F(\rho)^{2}\,d\lambda^{2}, \qquad F(\rho)^{2} = \rho^{2} + k\rho^{4}, \quad k = \tfrac13 R_{0101},
\]
with no cross term and no dependence on the rapidity $\lambda$, for every field strength at $p$; the third-order terms $-\tfrac16\nabla_{e}R_{acbd}x^{c}x^{d}x^{e}$ add $O(\rho^{5})$ to $F^{2}$, with rapidity dependence. Hence $F(0) = 0$ and $F'(0) = 1$, and by Proposition \claimref{singularity.euclidean-section-period} read with unit rate, the Euclidean section of the local boost is regular at its tip $\rho = 0$ (the bifurcation point $p$ of the local boost, its fixed point in the boost plane) exactly when the period of imaginary rapidity is $2\pi$. The static observer at $\rho$ has proper acceleration $a = F'/F$ and, at rapidity period $2\pi$, proper inverse temperature $2\pi F$, so $T = a/(2\pi F'(\rho))$; with $F'(\rho)^{2} = (1 + 2k\rho^{2})^{2}/(1 + k\rho^{2})$ from the second-order terms, $T = (a/2\pi)\bigl(1 - \tfrac32 k\rho^{2} + O(\rho^{3})\bigr)$, and $T = a/2\pi$ at leading order. Off the boost plane, at transverse distance $y$, the induced metric depends on $\lambda$ at order $|\mathrm{Riem}|\,y^{2}$, the size of the field strength times $y^{2}$, so these statements hold at leading order and not beyond. For a diamond of radius $L$ in the leading-order flat geometry of the normal gauge, $\zeta = \bigl((L^{2} - t^{2} - r^{2})\partial_{t} - 2t\,x^{i}\partial_{i}\bigr)/(2L)$ is conformal Killing, vanishes on the edge $\{t = 0, r = L\}$, is divergence-free there, and its derivative on the edge is the unit boost of the plane spanned by $\partial_{t}$ and the edge normal: surface gravity $1$, the normalisation of (i) for the wedge.
\item[(ii)] \emph{(Clause (iii), read on the whole mode algebra, is clause (ii).)} Let $\mathfrak{A}$ be the CAR algebra over a mode set $\mathcal{J}$ (the Definition's mode set, renamed here so as not to clash with the unit $J$) with windows $\mathfrak{A}_{F}$ (Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics}), its numbers read in $\mathrm{span}\{1, J\}$, $J = e_{2}e_{3}$ the complex unit of the radial atom from which the boundary modes descend (\claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}), and let $\tau_{\lambda}(a_{j}) = e^{-Jw_{j}\lambda}a_{j}$ be a quasi-free flow in rapidity with real weights $w_{j}$. For $\beta > 0$ a state $\omega$ is $(\tau, \beta)$-KMS if and only if, on every window, $\omega|_{\mathfrak{A}_{F}}$ is faithful and its modular group is $\sigma_{s} = \tau_{-\beta s}$; the faithful states with that modular group on a window are exactly one, the Gibbs state of $\sum_{j \in F} w_{j}N_{j}$ at $\beta$. With $\beta = 2\pi$ of rapidity, clause (iii) of Premise \claimref{synthesis.c-loc-local-horizon-premise}, read as a statement about the modular flow of the state on the patch's whole mode algebra, is therefore equivalent, on a patch carrying such modes, to KMS at rapidity period $2\pi$, which is clause (ii) at leading order, the conversion to $T = a/2\pi$ in proper time being (i) (exact only where $F' = 1$). The stronger geometric reading of clause (iii), a flow carrying the algebras of nested sub-patches properly into one another, cannot hold on a mode space where the boost acts by phases (Theorem \claimref{synthesis.c-loc-modular-clause-moves-no-nested-patch}) and is not treated here.
\item[(iii)] \emph{(The thermal half, assumed.)} Consequently, for a patch carrying a mode algebra on which the local boost (or the diamond flow) acts as such a quasi-free phase flow, an assumption and not a result, clauses (ii) and (iii) of Premise \claimref{synthesis.c-loc-local-horizon-premise} together are, at leading order, the single condition
\begin{enumerate}
\item[(R$_{\mathrm{loc}}$)] for all elements $a, b$ of every window, the correlator $F_{a,b}(\lambda) = \omega\bigl(a\,\tau_{\lambda}(b)\bigr)$ continues in imaginary rapidity and its two orderings meet after one period of the regular Euclidean section of the local boost: $F_{a,b}(\lambda + 2\pi J) = \omega\bigl(\tau_{\lambda}(b)\,a\bigr)$, the continuation taken in $\mathrm{span}\{1, J\}$.
\end{enumerate}
This is joint KMS on whole windows: the local-boost form of the joint KMS condition that defines the I-state (Theorem \claimref{hawking.i-state}), which the store obtains at a Schwarzschild horizon from Premise \claimref{singularity.r-regularity-fixed-locus} for the single-mode marginals together with the joint quasi-freeness of Premise \claimref{singularity.q-joint-quasi-freeness-s-wave}, and at the de Sitter horizon from Premise \claimref{synthesis.r-lambda-regularity-cosmological-horizon} for the marginals. (R$_{\mathrm{loc}}$) is a new premise, stronger than the local form of (R) alone. Under it the state is the quasi-free state with symbol $(1 + e^{2\pi w})^{-1}$, the unique KMS state whatever the weights $w_{j}$, so the condition fixes the state without fixing which modes the patch carries. No condition on the pair $(\mathfrak{A}, \tau)$ alone can replace it: by Theorem \claimref{singularity.rate-rigidity-temperature-not-algebra-intrinsic} the value of $\beta$ is fixed only by a stipulation or by data outside the pair.
\end{enumerate}

## technical
Premise (C$_{\mathrm{loc}}$) asks for three things on every small local horizon: an area density of entropy, the temperature $a/2\pi$ and a geometric modular flow. This result shows that the last two, with the modular flow read on the patch's whole mode algebra and the boost acting on the modes by phases, are one condition, and separates what in it is derived from what is assumed. Derived: the geometric half. In a normal gauge about any point of a gravitational field on flat spacetime ($\hb = 1$ and $\Omega = 0$ there, the Riemann normal coordinates of the derived metric; signature $(-,+,+,+)$), the second-order derived metric on a boost plane is $d\rho^{2} - (\rho^{2} + \tfrac13R_{0101}\rho^{4})\,d\lambda^{2}$, the same at every rapidity, so the Euclidean continuation is smooth at its tip, the bifurcation point of the local boost, exactly for rapidity period $2\pi$, whatever the field strength, and an observer of acceleration $a$ sees $T = a/2\pi$ up to a relative correction $-\tfrac32k\rho^{2}$ and terms of order $\rho^{3}$. The diamond's conformal Killing field has unit surface gravity at its edge, the same normalisation. On every finite window of a mode algebra, a state is thermal (KMS) at inverse temperature $\beta$ for the boost exactly when it is faithful and its modular flow is the boost run at $-\beta$ per unit modular parameter, so the modular-flow clause adds nothing to the temperature clause (a geometric action on nested sub-patches is a stronger reading, not treated here). Assumed: the thermal half, the condition (R$_{\mathrm{loc}}$) that the state of the patch's modes be jointly KMS for the local boost at rapidity period $2\pi$ on whole windows. At Killing horizons the series makes the corresponding assumption in two parts, (R) for each single mode and (Q) for the joint quasi-free state; (R$_{\mathrm{loc}}$) is the local form of both together, a new premise and stronger than the local form of (R). It fixes the state uniquely whatever modes the patch carries. Because the temperature is not intrinsic to the algebra and its flow, a condition referring to the geometry cannot be avoided. This is a reduction of two clauses to one premise, not a derivation of the temperature, and it uses no feature specific to the series.

## lay
The assumption that every small horizon is hot at the Unruh temperature and that its quantum state's internal clock runs along the horizon's own boost was stated as two separate requirements. This result shows that, read as statements about all the modes of the horizon together, they are one. The geometry part can be made local: near any point, however strong the gravitational field is, the smoothness condition that sets the temperature at a black hole gives the Unruh temperature, up to small corrections. For a quantum state on a finite set of modes, being thermal for a flow and having that flow as its internal clock are the same property. What is left is one assumption, that the modes of every small horizon are jointly thermal at that temperature. At black holes the series makes the corresponding assumption in two parts, one for each mode separately and one for how the modes combine; the local version needs both, so it is a new assumption, stronger than the black-hole smoothness rule alone. It is not derived here from anything weaker.

## one-liner
For any patch carrying modes on which the local boost acts by phases (assumed), clause (iii) of version 1 of (C$_{\mathrm{loc}}$), read on the patch's whole mode algebra, is equivalent to its clause (ii) (KMS at $\beta$ iff faithful with modular group the boost at $-\beta s$, on every window), and both together are (R$_{\mathrm{loc}}$), the joint KMS condition of the I-state for the local boost at rapidity period $2\pi$, a new premise stronger than the local form of (R); derived is only the geometric half, that this period is where the local boost's Euclidean section is regular for every field strength at leading order, giving $T = a/2\pi$ up to a relative correction $-\tfrac32k\rho^{2} + O(\rho^{3})$.
