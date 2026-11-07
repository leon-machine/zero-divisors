---
id: synthesis.boundary-mode-first-law-of-entanglement
kind: claim
version: 7
title: The first law of entanglement and entanglement equilibrium on the boundary-mode algebra
status: proved
region: synthesis
subject: entropy
tags: [entanglement, boundary-modes, modular-theory, curvature-and-field-equations]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle (U1 to U6)
  version: 7
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 7
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - hawking.i-state@4
  - state-selection.partner-purification-are-canonical@4
  - synthesis.boundary-mode-thermal-entropy@2
  - angle.imported-theorems-deliver-their-hypotheses@3
  - synthesis.imported-jacobson-entanglement-equilibrium-2016@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_mode_algebra
- kind: check
  ref: check.py::check_first_law
- kind: check
  ref: check.py::check_equilibrium
- kind: check
  ref: check.py::check_small_ball_balance
- kind: proof
  derivation: main
about:
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics
- obj.synthesis.gtg-flat-spacetime-gauge-fields
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: Clause (iv) works in metric components with the sign conversion stated, as its imported premise does (reader R08: consistent, the import''s language); the GTG field equation is stated beside it.'
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle (U2) the window''s Fock space and its GNS spaces have their numbers read in span{1, J}, J = e_2 e_3 the complex unit of the radial atom (synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom, cited in the formal level); the entity wrote no bare i (the detector''s hits were the eigenbasis index of the purification, renamed k); the outside_ga declaration, whose reason was the complex Hilbert-space structure, is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the C^2 factors of the window''s Fock space carry the Hilbert-space structure of density matrices and purifications, which the store does not state with the unit I_4 here; declared (version and levels unchanged); the |i> are basis labels.'
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 5 -> 6. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  maintainer_pass_gtg_l0:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'd-dimensional reading of clause (iv) completed by the lead: the flat background of dimension d is the d-dimensional clause of the definition (version 2), whose store-sign field equation G(a) + Lambda a = -8 pi G T(a) is the conversion stated at the end of the clause; content unchanged.'
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'W503: the technical and lay levels now state as conditions (if) the inputs (a), (b), (c) of clause (iv). Sign convention: clause (iv), stated in signature (-,+,+,+) with sphere-positive curvature, now also gives its tensor equation in the store convention, Ric + 8 pi G T = (Lambda + 4 pi G tau) g as in synthesis.einstein-condition-is-infinity-vacuum-incidence clause (7), with the conversion in the proof (g = -g0, Ric = -Ric0, R and T_ab unchanged). Version 2 -> 3.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Maintainer pass: Jacobson 2016, cited from memory, is now the imported Fact synthesis.imported-jacobson-entanglement-equilibrium-2016; (J16), its tensor step, is imported rather than a stated hypothesis, added to uses and cited in the statement, proof and check. Inputs (a), (b), (c) remain the conditions of clause (iv). Version 1 -> 2.'
  open_problem: ein.entanglement-equilibrium
  note: >-
    Tests Jacobson's 2016 entanglement-equilibrium derivation against the boundary-mode algebra.
    On every window of that algebra the selected state obeys the first law of entanglement and
    uniquely maximises entropy at fixed modular energy, and these entropies are entanglement
    entropies with the canonical partner. These are standard facts of any faithful Gibbs state of
    a finite system, here on the series' windows. Jacobson's argument needs them for the state of
    the quantum fields in a small geodesic ball at an arbitrary point, which is a different system:
    the windows sit on the stretched singularity or at Killing horizons. So the field equations
    follow from the small-ball balance (recomputed here in every dimension) only under three inputs
    that the algebra does not supply: an area density eta of the ultraviolet entanglement (which
    would set G = 1/(4 eta) and is the calibration residue again), a geometric modular flow for
    small causal diamonds (held in the store only for conformal fields in flat space), and the
    small ball's state obeying the first law and maximal entanglement. Transport-absent in its
    proofs. Fix round 2026-10-22-toe: restated as the referee's weaker statement; the third
    missing input (c) and the hypothesis (J16) for the tensor step made explicit; curvature
    convention declared.
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity (light; clauses (i)-(iii) have no gravity content): in (iv) the small geodesic ball read at x0 in a gauge with hb(x0) = 1, Omega(x0) = 0 on a flat background of dimension d; flat-space conformal fields named as vanishing gravitational field; the store-convention equation given its GTG form R(a) + 8 pi G T(a) = (Lambda + 4 pi G tr T) a in four dimensions. The d-dimensional tensor balance kept in the clause''s declared signature and convention. Clauses (i)-(iv) unchanged.'
outside_ga:
  kind: other
  why: 'Clause (iv) works in metric components with the sign conversion stated, as its imported premise does (reader R08: consistent, the import''s language); the GTG field equation is stated beside it.'
---

## formal
Let $F$ be a window of the boundary-mode algebra with its boost dynamics (Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics}), $H_{F} = \sum_{j \in F}\omega_{j}N_{j}$, and $\omega_{I}$ the state of Theorem \claimref{hawking.i-state}, whose restriction to $F$ is the Gibbs state $\rho_{I} = e^{-\beta H_{F}}/Z_{F}$ with $n_{j} = (e^{\beta\omega_{j}} + 1)^{-1}$. Put $K_{F} := -\ln\rho_{I} = \beta H_{F} + \ln Z_{F}$, the modular Hamiltonian of $\omega_{I}$ on $F$. Numbers on the window's Fock space and its GNS spaces are read in $\mathrm{span}\{1, J\}$, $J = e_{2}e_{3}$ the complex unit of the radial atom from which the boundary modes descend (\claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}). Then:
\begin{enumerate}
\item[(i)] (First law of entanglement.) For every differentiable family $\rho_{t}$ of density matrices on $F$ with $\rho_{0} = \rho_{I}$, $\frac{d}{dt}S(\rho_{t})\big|_{0} = \frac{d}{dt}\Tr(\rho_{t}K_{F})\big|_{0} = \beta\,\frac{d}{dt}\Tr(\rho_{t}H_{F})\big|_{0}$.
\item[(ii)] (Equilibrium.) For every state $\rho$ on $F$, $S(\rho) - \beta\Tr(\rho H_{F}) = \ln Z_{F} - S(\rho\,\|\,\rho_{I}) \le \ln Z_{F}$, with equality if and only if $\rho = \rho_{I}$: among the states of $F$ with a given modular energy $\Tr(\rho K_{F})$, $\omega_{I}$ is the unique one of maximal entropy, and at second order the first law fails by exactly the relative entropy. Per mode, $s(q) - \beta\omega_{j}q$ is strictly concave in the occupation $q$ and stationary only at $q = n_{j}$.
\item[(iii)] (Entanglement reading.) In the GNS representation of $\omega_{I}$ the window's commutant is the partner copy and the cyclic vector is the product of the modes' thermofield doubles (Theorem \claimref{state-selection.partner-purification-are-canonical}), so $S(\rho_{I})$, and $S(\rho)$ for every faithful $\rho$ in its own GNS representation, is an entanglement entropy with the canonical partner, with $s \le \ln 2$ per mode (Theorem \claimref{synthesis.boundary-mode-thermal-entropy}). Clauses (i)-(iii) are standard facts of any faithful Gibbs state of a finite system, stated here on the series' windows.
\item[(iv)] (The small-ball balance, conditional.) In spacetime dimension $d$, with signature $(-,+,\ldots,+)$ and the curvature convention in which the round sphere has positive scalar curvature (so $R_{s} = 2G_{00} \ge 0$ on a time-symmetric slice with nonnegative energy density; the store's own curvature convention differs by a sign, and the conversion is stated at the end of this clause), grant (a) that the ultraviolet entanglement across the boundary of a small geodesic ball is $\eta$ per unit area (in Gauge Theory Gravity, Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}, read on the flat background $\R^{1,d-1}$ of its $d$-dimensional clause, whose field equation in the store's sign is $\mathcal{G}(a) + \Lambda a = -8\pi G\,T(a)$: the ball about a point $x_0$ of the background in a gauge with $\hb(x_0) = 1$, $\Omega(x_0) = 0$, with the frame transported along straight background rays, at leading order in its size against the curvature scale of $\mathcal{R}(x_0)$); (b) that the matter modular Hamiltonian of the ball's causal diamond is the conformal Killing one, $K = 2\pi\int_{B}\tfrac{\ell^{2} - r^{2}}{2\ell}\,T_{00}$, which the store holds for conformal fields in flat space with vanishing gravitational field (the Hislop-Longo clause of Fact \claimref{angle.imported-theorems-deliver-their-hypotheses}); and (c) that the state of the fields in the ball obeys the first law $\delta S_{\mathrm{matter}} = \delta\langle K\rangle$ and is maximally entangled at fixed energy, the analogues of (i) and (ii) for that system. Then at fixed volume $\delta A = -\Omega_{d-2}\ell^{d}G_{00}/(d^{2} - 1)$ and $\delta\langle K\rangle = 2\pi\Omega_{d-2}\ell^{d}\,\delta\langle T_{00}\rangle/(d^{2} - 1)$, and stationarity of the total entropy, $\eta\,\delta A + \delta S_{\mathrm{matter}} = 0$, is $G_{00} = (2\pi/\eta)\,\delta\langle T_{00}\rangle$ in every dimension. By (J16), Jacobson's passage from the $00$ component in every frame at every point to the tensor equation (part of Fact \claimref{synthesis.imported-jacobson-entanglement-equilibrium-2016}), this is $G_{ab} + \Lambda g_{ab} = 8\pi G\,T_{ab}$ with $G = 1/(4\eta)$ and $\Lambda$ undetermined. In the store's convention (signature $(+,-,-,-)$, $\Ric = \Lambda g$ for de Sitter space), with $g = -g^{\circ}$ for the metric $g^{\circ}$ of this clause, the store's $\Ric$ is minus the sphere-positive Ricci tensor, the scalar curvature $R$ is unchanged and $T_{ab}$ is unchanged as a covariant tensor, so the same equation reads $\Ric - \tfrac12 R\,g + \Lambda g = -8\pi G\,T$, equivalently, in four dimensions, $\Ric + 8\pi G\,T = (\Lambda + 4\pi G\,g^{ab}T_{ab})\,g$, which in Gauge Theory Gravity is $\mathcal{R}(a) + 8\pi G\,T(a) = (\Lambda + 4\pi G\,\partial_b \cdot T(b))\,a$ for a gravitational field on flat spacetime, the form of clause (7) of Theorem \claimref{synthesis.einstein-condition-is-infinity-vacuum-incidence}; its $00$ balance reads $\Ric_{00} - \tfrac12 R\,g_{00} = -(2\pi/\eta)\,\delta\langle T_{00}\rangle$. The boundary-mode algebra supplies none of (a), (b), (c).
\end{enumerate}

## technical
On every finite window of the boundary-mode algebra the selected thermal state obeys the first law of entanglement (the entropy changes at first order by the inverse temperature times the energy change) and is the unique state of maximal entropy at its modular energy, the shortfall of any other state being its relative entropy; because the state is purified by its canonical partner, these entropies are entanglement entropies. These are standard facts of any faithful Gibbs state, here on the series' windows.

Jacobson's 2016 argument needs the same two properties for a different system: the quantum fields in a small geodesic ball around an arbitrary point. If they are granted there, together with an area density $\eta$ for the ultraviolet entanglement and a geometric modular flow for small causal diamonds, the small-ball balance (recomputed here exactly in every dimension, the factor $1/(d^{2} - 1)$ cancelling) gives $G_{00} = (2\pi/\eta)T_{00}$, and Jacobson's tensor step (an imported Fact) then gives Einstein's equations with $G = 1/(4\eta)$, which in the store's sign convention read $\Ric + 8\pi G\,T = (\Lambda + 4\pi G\,g^{ab}T_{ab})\,g$, in Gauge Theory Gravity the field equations $\mathcal{R}(a) + 8\pi G\,T(a) = (\Lambda + 4\pi G\,\partial_b \cdot T(b))\,a$ of a gravitational field on flat spacetime. The boundary-mode algebra supplies none of these three inputs: $\eta$ is the calibration residue in another guise, the store has a geometric diamond flow only for conformal fields in flat space with vanishing gravitational field, and the windows are not small balls at arbitrary points.

## lay
One recent derivation of Einstein's equations treats empty space as maximally entangled and asks what geometry keeps it so when matter is added. The framework's boundary modes, in the thermal state it selects, have the two quantum properties that derivation uses: their entanglement changes in step with their energy, and no other state with the same energy is more entangled. But the derivation would give Einstein's equations only if it also had the same properties for every small region of space, an amount of entanglement per area, and a rule for time in small regions, none of which the framework yet supplies.

## one-liner
On every window of the boundary-mode algebra the selected state obeys the first law of entanglement and uniquely maximises entropy at fixed modular energy (standard Gibbs-state facts); Jacobson's small-ball balance would give $G_{00} = (2\pi/\eta)T_{00}$ only under an area density, a geometric diamond flow and the same properties for small balls, none of which the algebra supplies.
