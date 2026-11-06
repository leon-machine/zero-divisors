---
id: synthesis.collapse-in-vacuum-regular-at-future-horizon-selects-hawking-temperature
kind: claim
version: 1
title: 'Null-shell collapse: horizon regularity selects the Hawking temperature'
status: proved
region: synthesis
subject: thermality
tags: [horizons, thermal-premises, hawking-temperature, car-algebra, forcing-and-uniqueness]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.hawking.continuum-mode-space
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - singularity.connection-bivector-computed@4
  - synthesis.imported-gtg-dictionary@1
  - hawking.i-state-continuum@5
  - hawking.imported-ideal-fermi-gas-uniqueness@2
  - angle.imported-theorems-deliver-their-hypotheses@1
  assumes:
  - hawking.joint-j3-s-wave-reduction@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_ingoing_radius_is_affine_in_pg_gauge
- kind: check
  ref: check.py::check_killing_translation_dilates_the_crossing
- kind: check
  ref: check.py::check_vacuum_kernel_pulls_back_to_the_thermal_kernel
- kind: check
  ref: check.py::check_short_distance_condition_and_scaling_limit
- kind: check
  ref: check.py::check_vaidya_shell_flux_tends_to_hawking_value
- kind: check
  ref: check.py::check_regularity_across_future_horizon_selects_t_h
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.n-plus-null-ground-state
  - synthesis.positive-null-energy-gives-r-premises
  - singularity.r-regularity-fixed-locus
  - synthesis.positive-conformal-energy-gives-positive-null-translations
extraction:
  open_problem: op.collapsing-hole-state
  note: >-
    Companion to synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet, filed alongside, which states the short-distance condition on the ingoing
    sheet and derives the late-time I-state from it. This entity supplies the two things that statement leaves
    to be justified: (a) a hole formed by collapse is in the class, because its physical state, the vacuum before
    the collapse, is a ground state for the affine advanced time and the ray tracing through a null shell is an
    analytic map with nonzero derivative at the horizon ray; the flux is computed exactly at all times; (b) among
    states KMS for the Killing translations at late times, finite null energy across the future horizon holds
    only at kappa/2pi (the Candelas / Christensen-Fulling criterion). Cross-subject technique: the Schwarzian
    transformation law of a chiral field's null energy (1+1 conformal field theory, moving-mirror models), cited
    from memory (Davies and Fulling 1976-77; Fredenhagen and Haag 1990 for the four-dimensional short-distance
    form). Scope: per-light-ray chiral modes, the s-wave reduction of the postulate J3 (hawking.joint-j3-s-wave-reduction)
    in geometric optics; greybody factors and backscatter are not treated. The dichotomy formula
    F_U = (theta^2 - 1)/(48 pi U^2) is the formula <T_uu> = (c^-2 - 1)/(48 pi u^2) of synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit (filed alongside)
    with theta = 1/c, on a different null line; the late flux kappa^2/(48 pi) is the Robinson-Wilczek anomaly
    flux (cited from memory). Transport-absent: standard physics restated on the series' continuum carrier and
    in the Painleve-Gullstrand gauge of Gauge Theory Gravity.
  flags:
  - 'beyond one flat chart: the collapse field is the vanishing field for v < v0 and the Painleve-Gullstrand field for v > v0, glued across the null shell with the radial label continuous; past and future null infinity are read on the conformal compactification'
---

## formal
Work on flat spacetime with gravity the gauge fields $(\hb, \Omega)$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). The collapse field is the null-shell (Vaidya) field: vanishing field strength for advanced time $v < v_{0}$, and for $v > v_{0}$ the Schwarzschild field of mass $M$ in the Painlev\'e-Gullstrand gauge $\hb = 1 - \beta P$, $\beta^{2} = 2M/r$, with the rotation-gauge field of Proposition \claimref{singularity.connection-bivector-computed}, $\Omega(e_{t}) = -\beta\beta'\sigma_{r}$, $\Omega(e_{r}) = -\beta'\sigma_{r}$; $\kappa = 1/4M$, $m := 2M$, $T_{H} = \kappa/2\pi$. On each radial light ray the modes are the continuum mode space of Definition \claimref{obj.hawking.continuum-mode-space}: a complex chiral CAR field of weight $\tfrac12$ in a parameter $\lambda$ of the ray, with null vacuum kernel $\omega(\psi^{*}(\lambda_{2})\psi(\lambda_{1})) = \tfrac{i}{2\pi}(\lambda_{1} - \lambda_{2} + i0)^{-1}$; a reparametrisation $\lambda = f(\mu)$ acts by $\psi_{\mu}(\mu) = f'(\mu)^{1/2}\psi_{\lambda}(f(\mu))$. Say a state of the outgoing modes on an ingoing ray is in the short-distance class at a point $\lambda = 0$ if its kernel is $\tfrac{i}{2\pi}[(\lambda_{1} - \lambda_{2} + i0)^{-1} + R(\lambda_{1}, \lambda_{2})]$ with $R$ continuous near $(0,0)$. Write $\{f, x\} = f'''/f' - \tfrac32(f''/f')^{2}$ for the Schwarzian; the null energy flux of the state is $-\tfrac{1}{24\pi}$ times the Schwarzian of the map from its vacuum's parameter to the observer's (normal ordered at the observer's vacuum).
Two facts of the Painlev\'e-Gullstrand field are used and recomputed here from the stored rotation-gauge field (they are clauses (i) and (ii) of the result filed alongside, synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet, which states the short-distance condition and derives the late-time I-state from it): on the ingoing radial null worldlines the physical tangent $k = (\gamma_{0} - \gamma_{1})/(1 + \beta)$ is parallel, so $r$ is affine there; and on such a worldline $U := -\rho\,e^{\rho/2M}$, $\rho = r - 2M$, satisfies $dU/du = -\kappa U$ for the outgoing worldlines' Killing label $u$, with $dU/dr = -1$ at the crossing.
\begin{enumerate}
\item[(i)] \emph{(The collapse state is in the class.)} The ray that entered from past null infinity at advanced time $v < v_{H} := v_{0} - 4M$ and leaves the centre outgoing in the flat region leaves the shell at radius $s = (v_{0} - v)/2 > m$; its retarded Killing time is $u = v_{0} - 2s - 2m\ln(s/m - 1)$ and its Kruskal label is an analytic function of $v$ with nonzero derivative at $v_{H}$, of the form $C\,e^{z}z$, $z = s/m - 1$. If the ingoing modes at past null infinity are in the null vacuum for the affine translations of $v$ (the vacuum of the region before the shell), then on every ingoing ray crossing the future horizon the outgoing modes are in the short-distance class at the crossing in the affine parameter $r$, with remainder $R(\lambda_{1}, \lambda_{2}) = \tfrac{1}{12}\{f, \lambda\}(\lambda_{1} - \lambda_{2}) + O(|\lambda|^{2})$ vanishing at the crossing ($\{z e^{z}, z\}_{z=0} = -3$, $\{U, v\}_{v_{H}} = -3/(4m^{2})$, finite).
\item[(ii)] \emph{(The flux, exactly, and its limit.)} At future null infinity the outgoing flux per complex chiral field per ray is $-\tfrac{1}{24\pi}\{v, u\}$ with
\[
\{v, u\} = -\frac{m(4s - 3m)}{8s^{4}}\qquad\text{exactly}, \qquad \lim_{u\to\infty}\{v, u\} = -\frac{1}{8m^{2}} = -\frac{\kappa^{2}}{2},
\]
approached as $O(s - m) = O(e^{-\kappa u})$, so the late flux is $\kappa^{2}/48\pi = \tfrac{\pi}{12}T_{H}^{2}$, that of a complex chiral fermion at $T_{H}$. The late-time two-point function in $u$ is the pull-back of the null vacuum by $U = -e^{-\kappa u}/\kappa$, which is exactly $\tfrac{i}{2\pi}\tfrac{\kappa}{2}\sinh(\tfrac{\kappa}{2}(u_{1} - u_{2}) + i0)^{-1}$, the continuum I-state at $\beta = 2\pi/\kappa$ (Theorem \claimref{hawking.i-state-continuum}), unique by Fact \claimref{hawking.imported-ideal-fermi-gas-uniqueness}; the remainder contributes $O(e^{-2\kappa t})$ to the kernel at shift $t$ (for this state; the result filed alongside shows the limit for every state of the class).
\item[(iii)] \emph{(Regularity selects $T_{H}$.)} Let a state of the outgoing modes have late-time flux $\tfrac{\pi}{12}(\theta T_{H})^{2}$, $\theta \ge 0$. Its flux in the frame of the $U$-vacuum is $F_{U} = (\theta^{2} - 1)/(48\pi U^{2})$ at leading order as $U \to 0^{-}$, bounded across the future horizon if and only if $\theta = 1$. The Boulware state (the $u$-vacuum, $\theta = 0$) has $\{u, U\} = 1/(2U^{2})$ and diverges there. So, among states that are KMS for the Killing translations at late times, finite null energy across the future horizon holds only at temperature $\kappa/2\pi$. Only the flux is used: bounded $F_{U}$ is a necessary condition, and it is neither the short-distance class nor sufficient for it. (Filed alongside, synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet, shows that the Boulware-type state is outside the class and that no exact null-translation ground state can be posed on the collapse geometry's half-line rays.)
\end{enumerate}
Hypotheses: the in-region state (a ground state for the affine advanced time, the Minkowski vacuum of the region before the shell); the per-light-ray chiral reduction, which is the s-wave reduction of the postulate J3 (\claimref{hawking.joint-j3-s-wave-reduction}) in its geometric-optics form, with no greybody factors; and the transformation law of the null energy of a chiral field (the coefficient of the linear remainder, cited from memory).

\emph{Beyond one flat chart.} The glued field across the shell and the null infinities, read on the conformal compactification, are not carried by one gravitational field on one chart; the preliminaries and statement (iii) hold in the Painlev\'e-Gullstrand chart, which covers both sides of the future horizon.

## technical
The result filed alongside (synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet) states the condition for a collapsing hole as the short-distance ground-state condition on the ingoing light rays at the future horizon, and derives the Hawking state from it, since the Killing translation dilates the Kruskal parameter about the crossing. Two questions remain: does a hole formed by collapse satisfy the condition, and is the condition forced? This result answers both for the null-shell collapse, exactly, under the per-light-ray chiral reduction (the s-wave reduction of the postulate J3). The physical state is the vacuum of the region before the collapse, a ground state for the affine advanced time $v$ of the incoming light rays. Through the shell, the ray-tracing map from $v$ to the Kruskal label $U$ is analytic with nonzero derivative at the last ray that escapes, so the state on the future horizon's ingoing rays is the ground-state kernel plus a remainder that vanishes at the crossing. The flux at infinity is the Schwarzian $\{v, u\} = -m(4s - 3m)/8s^{4}$, exact at all times, tending to the value of a thermal chiral fermion at $\kappa/2\pi$. Conversely, a state KMS at late times at any other temperature has a flux in the horizon-regular frame that diverges as $U^{-2}$ at the future horizon; the Boulware state is the case $\theta = 0$. So the condition is realised by collapse, and among late-time KMS states only the Hawking temperature has finite null energy at the future horizon. The result filed alongside states the condition, proves that the late-time limit of every state in the class is the I-state, and excludes the Boulware-type state and an exact ground state; this result does not repeat those clauses.

The computations are exact: the parallel transport of the ingoing tangent with the stored Painlev\'e-Gullstrand rotation gauge field; the dilation identity $dU/du = -\kappa U$, whose exponential factor cancels; the pull-back identities of the weight-$\tfrac12$ kernel (M\"obius invariance; thermal kernel in $x = e^{\kappa u/2}$); the remainder series of the map $z e^{z}$ to sixth order; the Schwarzian along the shell exit radius from exact Taylor coefficients of $u'(s) = -2s/(s - m)$; and the regularity dichotomy. The Fermi integral behind $\tfrac{\pi}{12}T^{2}$ and the four-dimensional statement (Fredenhagen and Haag) are cited from memory.

## lay
A real black hole forms when matter collapses; it was never an eternal hole in equilibrium. The series' premise that fixes the Hawking temperature covered only the eternal hole. A result filed alongside says what the condition should be for a collapsing hole: near the horizon, at very short distances, the quantum field looks like empty space. This result checks that a collapse really produces such a state, in the simplest exact model, a thin shell of light falling inward. The field starts in empty space before the collapse; its light rays pass through the centre and out past the forming horizon, and the stretching they suffer is computed exactly. The outgoing energy flow tends to that of a thermal glow at exactly the Hawking temperature. It also shows that no other temperature is possible: any other late-time thermal state would make the field's energy blow up at the horizon. The calculation treats each light ray separately, as the series' standard reduction does.

## one-liner
For a null-shell collapse the vacuum before the collapse is in the short-distance ground-state class on the future horizon's ingoing light rays (the ray-tracing map is analytic with nonzero derivative at the last escaping ray), and its outgoing flux is exactly $-\tfrac{1}{24\pi}\{v,u\}$ with $\{v, u\} = -m(4s - 3m)/8s^{4}$ at every retarded time, tending to the chiral flux at $\kappa/2\pi$; among states KMS for the Killing translations at late times only $T = \kappa/2\pi$ has finite null energy across the future horizon. Per-light-ray chiral modes (the s-wave reduction of the postulate J3). Filed alongside synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet, which states the condition and derives the late-time I-state from it.
