---
id: synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional
kind: claim
version: 2
title: 'Odd-parity gravity channels, l >= 2, are 2D at the static-frame horizon; even one way'
status: proved
region: synthesis
subject: thermality
tags: [boundary-modes, mode-counting, recovers-known-physics]
proposed_by:
  kind: ai
  session: 2026-11-09-three
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-09-three
- name: Claude Fable 5.2
  role: 'dated note at every level: the cited fact (C3) is proved by the even-parity result, what is still cited is (C1) and (C2), clause (3) is superseded on oscillating channels only, and clause (1) no longer depends on the degree bound; no clause reworded'
  version: 2
  source: 'maintainer pass of 2026-11-18 (run 2026-11-18-leads)'
amendments:
- version: 2
  kind: restatement
  defect: 'the statement gave the even-parity channel as conditional on the cited fact (C3) and clause (1) as resting on an argued degree bound; (C3) is now proved in the store and the closed forms of (1) are verified as identities in radius and angle, so the conditions named were no longer the ones the result needs'
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - pairing.imported-schwarzschild-connection-curvature@7
  - synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_odd_parity_linearised_ricci
- kind: check
  ref: check.py::check_regge_wheeler_reduction
- kind: check
  ref: check.py::check_superpotential_and_intertwiner
- kind: check
  ref: check.py::check_even_parity_zerilli_in_span
- kind: check
  ref: check.py::check_horizon_values
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - hawking.joint-j3-s-wave-reduction
  - hawking.helicity-lift-joints-itemised
extraction:
  maintainer_pass_2026_11_18_leads:
    by: maintainer-2026-11-18
    date: '2026-11-18'
    note: 'Version 1 -> 2. Dated note (18 November 2026) added to the formal level after the list of cited facts, with matching sentences in the technical level, the lay level and the one-liner: (C3) is clause (4) of synthesis.even-parity-gravity-channels-zerilli-equation-equivalent-to-the-vacuum-equations; what clause (5) here needs beyond (C3) is that result''s clause (5); (C1) and (C2) remain cited from memory; clause (3) here is superseded on oscillating channels only (the accepted result''s wording); clause (1) no longer depends on the degree bound (that result''s clause (2)). Clauses (1) to (5), the title, the proof and the check are unchanged. The citation is in the text only, not a uses edge: that result uses this one.'
  maintainer_pass:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'After acceptance (decisions of 9 November 2026): extraction note only. The id is kept (ids are stable; the title carries the scope); on this result joint J3 was restated (its version 3: the channel-reduction clause premise for even-parity spin 2 only); the companion result on the generation number is named by its stored id. Statement, premises and check unchanged.'
  open_problem: op.helicity-per-boundary-mode
  note: >-
    Attack on the spin-2 part of the channel-reduction clause of joint J3 (hawking.joint-j3-s-wave-reduction, version 2,
    where that clause is premise for spin 2 only), by linearising the gauge field of Gauge Theory Gravity about the
    stored static Schwarzschild field instead of importing the reduction. Method: the perturbed coframe
    hb^{-1}(e_mu) + eps k_mu with eps of square zero, the rotation-gauge field solved exactly from the linearised
    torsion-free condition, the first-order Ricci vector read from the linearised field strength, at jet points
    (lib/gtg.py). Prior art, cited from memory and not used as input: Regge and Wheeler (1957) for the odd-parity
    equation, Zerilli (1970) for the even-parity equation, Moncrief (1974) for the master function used in (3),
    Chandrasekhar (The Mathematical Theory of Black Holes, 1983, chapter 4) for the transformation between the two
    parities, Chandrasekhar (1984) on the algebraically special perturbations and Glampedakis, Johnson and Kennefick
    (Phys. Rev. D 96, 024036, 2017) for its reading as a Darboux transformation whose kernel is the algebraically
    special solutions (prior art for clause (4)), and Doran and Lasenby (Geometric Algebra for Physicists, sections
    13.4 to 13.6 for the gauge-theory setting, chapter 14 for its applications). The id of this entity names the
    field as a whole; the title carries the scope (odd parity derived, even parity one way, l >= 2, static frame),
    and the id is kept (ids are stable). The classical facts (C1) to (C3) stay hypotheses of the
    statement; deriving them is an open item. The
    equations and potentials reproduce the known ones; new for the store is that the reduction is computed from the
    stored field in the gauge-theory form, with the odd parity derived in both directions and the even parity reached
    in one direction (the vacuum equations imply the Zerilli equation; the converse reconstruction is cited). What
    this leaves of J3 as premise: the current-boson identification and the partial-wave lift for every massless
    field, and, for the channel clause at spin 2, only the classical inputs (C1) to (C3) of the formal level.
    On this result Leon decided on 9 November 2026 to keep the channel-reduction clause of J3 as premise for the
    even-parity channels of spin 2 only (its version 3, which cites this result for the odd parity). The two
    graviton channels per (omega, l, m), l >= 2, are the count used for eps = 1 in
    synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free.
    Status of the parts: (1) is proved given a degree bound that is argued (a grid of 144 exact cases: a basis of jets and of angular data,
    three polar angles, two values of L, identically in the radius); (2) is proved from (1); (3) is computed for the implication and cited for the converse;
    (4) and (5) are proved. Not covered: l = 0 and l = 1 (no radiative channel), the non-oscillating solutions at the
    special values of (4), other gauges and charts, uniformity in l. Transport-absent: the result recovers known
    physics in the series' gauge-theory language.
---

## formal
Let $(\hb, \Omega)$ be the Schwarzschild field in the static gauge of Fact \claimref{pairing.imported-schwarzschild-connection-curvature} on the exterior $r > 2M$, $f = 1 - 2M/r$, with physical frame $\gamma_{a}$ of signature $(+,-,-,-)$, $\hb^{-1}(e_{t}) = \sqrt f\,\gamma_{0}$, $\hb^{-1}(e_{r}) = \gamma_{1}/\sqrt f$, $\hb^{-1}(e_{\vartheta}) = r\gamma_{2}$, $\hb^{-1}(e_{\varphi}) = r\sin\vartheta\,\gamma_{3}$ (\claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), tortoise coordinate $r_{*}$ with $dr_{*}/dr = 1/f$, $\partial_{r_{*}} = f\partial_{r}$, and $\kappa = 1/(4M)$. A linearised gravitational field is a first-order change $\hb^{-1}(e_{\mu}) \mapsto \hb^{-1}(e_{\mu}) + \epsilon k_{\mu}$, $\epsilon^{2} = 0$, with $\Omega \mapsto \Omega + \epsilon\Omega_{1}$ fixed by the torsion-free condition; its Ricci vector is $\epsilon\,\mathcal{R}_{1}(\gamma_{b})$, and the linearised vacuum equations are $\mathcal{R}_{1}(\gamma_{b}) = 0$. Let $L$ be a separation constant ($L = \ell(\ell+1)$, $\ell \geq 2$, on the sphere), $\lambda := (L - 2)/2$, $P(\vartheta)$ a solution of $P'' + \cot\vartheta\,P' + LP = 0$ and $S := \sin\vartheta\,P'$.
\begin{enumerate}
\item \emph{(Odd parity; proved, given the degree bound (argued) and the homogeneity in $M$.)} For $k_{\varphi} = S(\vartheta)\bigl(f^{-1/2}h_{0}(t,r)\,\gamma_{0} - f^{1/2}h_{1}(t,r)\,\gamma_{1}\bigr)$ and $k_{t} = k_{r} = k_{\vartheta} = 0$ (the axisymmetric odd-parity field in the Regge-Wheeler gauge),
\[
\mathcal{R}_{1}(\gamma_{3}) = -\frac{S}{2r\sin\vartheta\,\sqrt f}\bigl(E_{t}\gamma_{0} + E_{r}\gamma_{1}\bigr) + \frac{S' - 2\cot\vartheta\,S}{2r^{2}\sin\vartheta}\,E_{\vartheta}\gamma_{2},
\]
the other $\mathcal{R}_{1}(\gamma_{a})$ are fixed by the symmetry $\gamma_{a} \cdot \mathcal{R}_{1}(\gamma_{b}) = \gamma_{b} \cdot \mathcal{R}_{1}(\gamma_{a})$, and
\[
E_{\vartheta} = \frac{\partial_{t}h_{0}}{f} - \partial_{r}(f h_{1}), \qquad
E_{r} = \partial_{t}^{2}h_{1} - \partial_{t}\partial_{r}h_{0} + \frac{2}{r}\partial_{t}h_{0} + \frac{(L-2) f}{r^{2}}h_{1},
\]
\[
E_{t} = f\Bigl(\partial_{r}^{2}h_{0} - \partial_{t}\partial_{r}h_{1} - \frac{2}{r}\partial_{t}h_{1}\Bigr) - \Bigl(\frac{L}{r^{2}} - \frac{4M}{r^{3}}\Bigr)h_{0}.
\]
The evidence: on a basis of the second-order jets of $h_{0}$ and of $h_{1}$ (six monomials each) and a basis of the data $(S, S')$ at the point, the equality holds as an identity of rational functions of $\sqrt f$, hence at every radius of the exterior, at three polar angles with distinct cotangents and for two values of $L$ at each ($144$ cases, every component compared, the vanishing ones included). Both sides are of degree at most one in $L$, and for fixed radius and each basis element $\sin\vartheta$ times each side is a polynomial of degree at most two in $\cot\vartheta$ (the degree bound, argued in the proof), so the grid decides the identity for every $L$, radius and polar angle; $M = 1$ is used, and the equations are homogeneous under $(t, r, M) \mapsto (ct, cr, cM)$.
\item \emph{(Regge-Wheeler channel; proved from (1).)} With $Q := f h_{1}/r$ and $V_{\mathrm{o}} := f\bigl(L/r^{2} - 6M/r^{3}\bigr)$,
\[
\partial_{t}^{2}Q - \partial_{r_{*}}^{2}Q + V_{\mathrm{o}}Q = \frac{f}{r}\Bigl(E_{r} + \partial_{r}(fE_{\vartheta}) - \frac{2f}{r}E_{\vartheta}\Bigr), \qquad
\partial_{t}E_{t} = -f\,\partial_{r}E_{r} - \frac{2f}{r}E_{r} - \frac{(L-2)f}{r^{2}}E_{\vartheta}
\]
identically in $h_{0}, h_{1}$. So the vacuum equations imply the two-dimensional equation $\partial_{t}^{2}Q - \partial_{r_{*}}^{2}Q + V_{\mathrm{o}}Q = 0$. Conversely, on a channel of frequency $\omega \neq 0$ (functions with $\partial_{t}^{2} = -\omega^{2}$), every solution $Q$ of that equation gives a solution of all three vacuum equations: $h_{1} = rQ/f$ and $h_{0}$ the solution of $\partial_{t}h_{0} = f\,\partial_{r}(rQ)$ in the channel. On such a channel the odd-parity vacuum equations in this gauge are equivalent to the two-dimensional equation.
\item \emph{(Even parity; computed at sample points in one direction only, the converse cited.)} For the even-parity field in the Regge-Wheeler gauge, $k_{t} = P\bigl(-\tfrac12\sqrt f\,H_{0}\gamma_{0} + \sqrt f\,H_{1}\gamma_{1}\bigr)$, $k_{r} = \tfrac12 f^{-1/2}H_{2}P\,\gamma_{1}$, $k_{\vartheta} = \tfrac12 rKP\,\gamma_{2}$, $k_{\varphi} = \tfrac12 r\sin\vartheta\,KP\,\gamma_{3}$ with $H_{0}, H_{1}, H_{2}, K$ functions of $(t,r)$, let
\[
\Psi := r\Bigl(K + \frac{fr}{\lambda r + 3M}\bigl(H_{2} - r\partial_{r}K\bigr)\Bigr), \qquad
V_{\mathrm{e}} := f\,\frac{2\lambda^{2}(\lambda+1)r^{3} + 6\lambda^{2}Mr^{2} + 18\lambda M^{2}r + 18M^{3}}{r^{3}(\lambda r + 3M)^{2}} .
\]
At the sample points (two points, $L = 6$ and $L = 7/2$) the linear functional $\partial_{t}^{2}\Psi - \partial_{r_{*}}^{2}\Psi + V_{\mathrm{e}}\Psi$ on third-order jets of $(H_{0}, H_{1}, H_{2}, K)$ lies in the span of the components of $\mathcal{R}_{1}(\gamma_{b})$ and their first $t$- and $r$-derivatives (rank $18$ with and without it; rank $19$ with $\lambda$ replaced by $\lambda + 1$ in $V_{\mathrm{e}}$): the vacuum equations imply the Zerilli equation. That every solution of the Zerilli equation arises from a vacuum solution is cited (C3), not derived.
\item \emph{(The two parities are intertwined; proved.)} With $c := \lambda(\lambda+1)/(3M)$ and the superpotential $W := 3Mf/\bigl(r(\lambda r + 3M)\bigr) + c$ (here $W$ and $\lambda$ are not the $W = \sqrt f/r$ and the sphere eigenvalue $\lambda$ of Theorem \claimref{synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional}),
\[
V_{\mathrm{o}} = W^{2} - \partial_{r_{*}}W - c^{2}, \qquad V_{\mathrm{e}} = W^{2} + \partial_{r_{*}}W - c^{2},
\]
so $(\partial_{r_{*}} + W)\bigl(\partial_{t}^{2} - \partial_{r_{*}}^{2} + V_{\mathrm{o}}\bigr) = \bigl(\partial_{t}^{2} - \partial_{r_{*}}^{2} + V_{\mathrm{e}}\bigr)(\partial_{r_{*}} + W)$ and $(\partial_{r_{*}} - W)(\partial_{r_{*}} + W) = -\bigl(-\partial_{r_{*}}^{2} + V_{\mathrm{o}} + c^{2}\bigr)$. On a channel with $\partial_{t}^{2} = -\omega^{2}$, $\omega$ real, $\partial_{r_{*}} + W$ maps solutions of the odd equation to solutions of the even equation, with inverse $-(\omega^{2} + c^{2})^{-1}(\partial_{r_{*}} - W)$; its kernel consists of solutions with $\partial_{t}^{2} = +c^{2}$, which are not oscillating channels. $W$ is bounded on the exterior and $W \to c$ at the horizon.
\item \emph{(At the horizon; proved.)} $V_{\mathrm{o}}/f$ and $V_{\mathrm{e}}/f$ are regular and positive at $r = 2M$, with values $(L - 3)/(4M^{2})$ and $(4\lambda^{2} + 4\lambda + 3)/\bigl(4M^{2}(2\lambda + 3)\bigr)$ for $L \geq 6$. Since $f = C(r)\,e^{2\kappa r_{*}}$ with $C$ regular and positive at the horizon (Theorem \claimref{synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional}, clause (4)), both potentials decay as $e^{2\kappa r_{*}}$ as $r_{*} \to -\infty$, the rate of the scalar and Maxwell channels, and each master function obeys the free two-dimensional equation there, with left- and right-moving solutions. For odd parity this is derived: given (C1), (C2) and (1), every odd-parity $(\omega, \ell, m)$ channel with $\ell \geq 2$ and real $\omega \neq 0$ is a two-dimensional mode at the horizon. For even parity it is conditional: the vacuum equations imply the Zerilli equation only at the sample points of (3), and that the Zerilli function carries the whole even-parity channel is the cited fact (C3); (4) then gives the even channel the same horizon behaviour as the odd one. With both, there are two channels (the two parities) for each $(\omega, \ell, m)$, and the channel-reduction clause of joint J3 (\claimref{hawking.joint-j3-s-wave-reduction}) holds for spin $2$, in the Regge-Wheeler gauge and for the master functions $Q$ and $\Psi$. Scope: (a) the statement is made in the static (Killing) frame, in the coordinates $(t, r_{*})$ in which the horizon is at $r_{*} = -\infty$; in coordinates regular across the horizon the same potential term does not vanish there, so ``free at the horizon'' is a statement about the Killing-time channel equation, as for the lower spins; (b) $\ell \geq 2$ only: for $\ell = 0$ ($\lambda = -1$) the denominator $\lambda r + 3M$ of $V_{\mathrm{e}}$ vanishes at $r = 3M$ and there is no odd field, and for $\ell = 1$ ($\lambda = 0$) the term of $E_{r}$ that carries $h_{1}$ algebraically vanishes and the perturbations are changes of mass, spin and gauge, so neither has a radiative channel; (c) the approach is channel by channel, not uniform in $\ell$, since $V/f$ grows with $L$; (d) the non-oscillating solutions of (4) are excluded. J3's current-boson identification and partial-wave lift are not derived.
\end{enumerate}
The classical facts assumed, cited from memory and not in the store: (C1) symmetric tensor fields on the sphere decompose into even- and odd-parity tensor harmonics, complete in $\ell$ and $m$, and by the rotational symmetry of the background the radial equations do not depend on $m$, so the axisymmetric representative suffices; (C2) for $\ell \geq 2$ every linearised field is carried by a first-order gauge change (a displacement, together with a local rotation of the frame) to the Regge-Wheeler gauge used in (1) and (3); (C3) every solution of the Zerilli equation in an oscillating channel is the function $\Psi$ of an even-parity vacuum solution. They enter the phrase ``every channel'' in (5); the identities (1) to (4) do not use them.

\emph{Note (18 November 2026).} The cited fact (C3) is now proved in the store. Clause (4) of Theorem \claimref{synthesis.even-parity-gravity-channels-zerilli-equation-equivalent-to-the-vacuum-equations} shows, identically and with no condition on the time dependence, that every solution of the Zerilli equation is the Zerilli-Moncrief function $\Psi$ of an even-parity vacuum solution, which is (C3); its clause (5) shows that on a channel with $\partial_{t}^{2} = -\omega^{2}$, $\omega^{2} \neq 0$, the vacuum equations imply the Zerilli equation identically and $\Psi$ determines the field. So the even-parity statement of (5) no longer rests on (C3): given (C1) and (C2), every even-parity $(\omega, \ell, m)$ channel with $\ell \geq 2$ and real $\omega \neq 0$ is a two-dimensional mode at the horizon in the static frame, as the odd-parity ones are (that theorem, (6)). What is still cited is (C1) and (C2), from memory and not in the store. Clause (3) above is superseded on oscillating channels only: without a condition on the time dependence the implication from the vacuum equations to the Zerilli equation is not proved identically and stays as stored, computed at the sample points. Clause (2) of that theorem gives the closed forms of (1) as identities in the radius and the polar angle together, so (1) no longer depends on the degree bound argued here. The clauses above are kept as first stated; the scope (a) to (d) is unchanged, and J3's current-boson identification and partial-wave lift are not derived.

## technical
Joint J3 treats each partial wave of a massless field near a Schwarzschild horizon as a two-dimensional mode. For spins zero, one half and one that clause has been derived in Gauge Theory Gravity; here the gravitational field itself is treated. The gauge field of the stored static Schwarzschild solution is changed to first order, the rotation-gauge field is solved from the torsion-free condition to the same order, and the first-order Ricci vector is read off, all in exact arithmetic at sample points with generic jets of the unknown functions. For the odd-parity field in the Regge-Wheeler gauge this gives three equations for two functions of time and radius. Two of them combine, by an identity that holds for all functions, into the Regge-Wheeler equation for the single function $Q = fh_{1}/r$: a wave equation in time and the tortoise coordinate with potential $f(\ell(\ell+1)/r^{2} - 6M/r^{3})$. The third equation has a time derivative that is a combination of the other two, so on a channel of nonzero frequency it follows from them, and conversely every solution of the Regge-Wheeler equation rebuilds a solution of all three: on such a channel the two-dimensional equation is equivalent to the linearised vacuum equations. For the even-parity field the corresponding statement is checked in one direction: the Zerilli equation for the Zerilli-Moncrief function is a linear combination of the vacuum equations and their first derivatives, with the rational Zerilli potential and no other. The two potentials are partners under one superpotential $W$, so the first-order operator $\partial_{r_{*}} + W$ carries odd-parity solutions to even-parity ones and back on every oscillating channel; it fails to be invertible only on non-oscillating solutions growing or decaying in time at the rate $\lambda(\lambda+1)/(3M)$. Both potentials are $f$ times a function that is regular and positive at the horizon, so they fall off as $e^{2\kappa r_{*}}$ and each channel becomes a free two-dimensional wave there, as for the scalar and Maxwell fields. There are two channels for each $(\omega, \ell, m)$ with $\ell \geq 2$, matching the two helicities of the graviton; the odd one is derived and the even one is conditional on the cited reconstruction. The statement is made in one gauge, for the master functions, and in the static frame, where the horizon lies at infinite tortoise coordinate. The first-order equations of (1) are verified on a basis of jets as identities in the radius on a grid of angles and separation constants that, by a degree bound, decides them everywhere; the implication of (3) is an exact computation at sample points only; the completeness of tensor harmonics, the reachability of the gauge and the even-parity reconstruction are cited from memory. J3's identification of these channels with the current boson of the s-wave theory, and its partial-wave lift, remain premise.

Since 18 November 2026 the even-parity channel is no longer conditional on the cited reconstruction: a later result (\claimref{synthesis.even-parity-gravity-channels-zerilli-equation-equivalent-to-the-vacuum-equations}) proves the reconstruction identically, and proves on every oscillating channel that the vacuum equations imply the Zerilli equation and that the master function determines the field. It also verifies the odd-parity closed forms as identities in the radius and the angle together, without the degree bound. The completeness of tensor harmonics and the reachability of the gauge remain cited from memory; off oscillating channels the implication from the vacuum equations to the Zerilli equation remains a computation at sample points.

## lay
Near a black hole's horizon, a field is often treated as a set of independent waves in one space dimension, one for each pattern on the sphere. Earlier this picture was derived, rather than assumed, for scalar fields, electrons and light. This result does the same for gravitational waves, the small ripples of the black hole's own field, in the geometric-algebra form of gravity the series uses. Each pattern with at least two lobes comes in two kinds, and each kind obeys a wave equation in one space dimension with a barrier that vanishes towards the horizon at the same rate as for light. So close to the horizon, as described in the time of static observers (in coordinates that cross the horizon smoothly the statement takes a different form), every such pattern is a free one-dimensional wave moving in or out, two for each pattern, which is the count expected for a particle of spin two. For one of the two kinds the equation is shown to be equivalent to the full equations of the ripple; for the other it is only shown to follow from them, at test points, and the reverse step is quoted from the literature, though a known exact relation carries solutions of one kind into the other. The equations themselves are the ones found by Regge, Wheeler and Zerilli; what is new here is that they are computed inside the series' own framework. Patterns with fewer than two lobes are not waves and are not covered, and the further step of identifying these waves with the boundary modes of the series stays an assumption. Since this was written a later result has shown the reverse step for the second kind exactly, for waves of a definite pitch, so the two kinds now stand on the same footing; two textbook facts about sorting ripples into patterns are still taken on trust.

## one-liner
In the static gauge of Gauge Theory Gravity on the Schwarzschild exterior, the odd-parity linearised gravitational field reduces on each oscillating channel with $\ell \geq 2$ to the Regge-Wheeler equation, equivalent to the vacuum equations there, with potential $f$ times a function regular and positive at the horizon, so the channel is two-dimensional at the horizon in the static frame (decay $e^{2\kappa r_{*}}$); the even-parity Zerilli equation is shown to follow from the vacuum equations at sample points and is intertwined with the odd one by $\partial_{r_{*}} + W$, its converse being cited, so the even channel is conditional here; a later result proves the converse and, on oscillating channels, the implication identically, so the even channel then holds given the cited harmonic and gauge facts (C1), (C2) alone.
