---
id: synthesis.stretched-horizon-count-on-kerr-gives-the-area-law-at-every-spin
kind: claim
version: 1
title: 'On Kerr a stretched-horizon count gives the area law at every spin, and tests nothing'
status: proved
region: synthesis
subject: entropy
tags: [kerr, mode-counting, boundary-modes]
proposed_by:
  kind: ai
  session: 2026-11-10-phase1
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase1
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - interior.imported-kerr-schild-form-kerr-gauge@2
  - synthesis.imported-kerr-surface-gravity-entropy@2
  - singularity.stretched-singularity-count@8
  - scrambling.epoch-modular-period-two-unknowns-become@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_volume_rate_of_constant_r_surfaces_is_flow_independent
- kind: check
  ref: check.py::check_rate_per_area_over_proper_distance_is_the_surface_gravity_at_every_latitude
- kind: check
  ref: check.py::check_three_schwarzschild_forms_split_on_kerr_and_the_area_form_is_the_smarr_rate
- kind: check
  ref: check.py::check_schwarzschild_rate_is_reached_on_three_slices
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.kerr-ring-count-misses-area-law
  - scrambling.mode-count
  - pred.boundary-mode-density
extraction:
  open_problem: op.kerr-ring
  note: >-
    Attack item 2 of op.kerr-ring (place the count on the horizon's modular data for the co-rotating Killing
    flow and see whether A_+/4 returns). Kill conditions registered before computing: the count per unit
    horizon area depends on latitude or on a/M at leading order, or needs a spin-dependent density or distance
    (did not fire); and, for the question whether the Schwarzschild formula fixes its own carry to Kerr, that
    its stored forms give different counts on Kerr (fired: they do, clause (v)). Verdict rule registered
    before computing: if the surface gravity cancels between rate and period by its definition alone, the
    comparison with A_+/4 is declared a tautology (it is, clause (iv)). What is classical: every identity
    here is Kerr geometry (the zeroth law, the Smarr relation, kappa_+ A_+ = kappa_- A_-), and a count on a
    surface at fixed proper distance from a horizon is the geometry of the brick-wall and stretched-horizon
    constructions ('t Hooft 1985; Susskind, Thorlacius and Uglum 1993; both cited from memory, nothing is
    imported from them). What is new for the store: the horizon placement of clause (Loc) of
    synthesis.c-loc-local-horizon-premise written as a three-volume count of the same form as the
    Schwarzschild count, the proof that it needs no spin-dependent input, the statement that the Kerr
    comparison is therefore no test of pred.boundary-mode-density, the exact factors by which the two other
    stored forms of the Schwarzschild rate miss on Kerr, and the form 8 pi nu (M - 2 Omega_H J) of the rate.
    The stored result synthesis.c-loc-is-a-second-placement-of-the-count (ii) already states that a constant
    density per unit area gives A_+/4 on Kerr at every spin; this result does not restate that, it supplies
    the three-volume count behind it. (SH) is a hypothesis of this result and is not adopted here; whether
    (C1) is restated by it away from Schwarzschild is a premise decision. Transport-absent: Kerr geometry and
    the counting premises only. The literal cutoff count at small spin, which the stored ring result leaves
    untreated, is intended to be cited from the sibling proposal of this session on that regime.
---

## formal
Units $G = c = \hbar = 1$. Take the Kerr gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) of mass $M$ and spin parameter $a$, $0 \le a < M$, in the Kerr-Schild gauge $\hb(b) = b + H\,(b\cdot k)\,k$, $Q(k) = 0$, of Fact \claimref{interior.imported-kerr-schild-form-kerr-gauge}, in the oblate coordinates $(t, r, u, \phi)$, $u = \cos\theta$, of the flat background, with derived metric $g(b,c) = \hb^{-1}(b)\cdot\hb^{-1}(c)$, written in components in the signature $(-,+,+,+)$ as $g = \eta + 2H\,k\otimes k$, $\eta = -dt^2 + \tfrac{\Sigma}{P}dr^2 + \tfrac{\Sigma}{1-u^2}du^2 + P(1-u^2)d\phi^2$, $k = -dt - \tfrac{\Sigma}{P}dr + a(1-u^2)d\phi$, $H = Mr/\Sigma$, $\Sigma = r^2 + a^2u^2$, $P = r^2 + a^2$. Put $s = \sqrt{M^2 - a^2}$, $r_\pm = M \pm s$, $\Delta = r^2 - 2Mr + a^2 = (r - r_+)(r - r_-)$, $P_\pm = r_\pm^2 + a^2 = 2Mr_\pm$, and, with Fact \claimref{synthesis.imported-kerr-surface-gravity-entropy}, $\kappa_\pm = (r_+ - r_-)/(2P_\pm)$, $A_\pm = 4\pi P_\pm$, $\Omega_H = a/P_+$, $J = aM$, $T_H = \kappa_+/2\pi$, $S = A_+/4$, and the co-rotating Killing flow $K = \hb^{-1}(\partial_t + \Omega_H\partial_\phi)$ with modular period $\beta_+ = 2\pi/\kappa_+$. Induced metrics are Gram matrices of physical tangent vectors $\hb^{-1}(\partial_\mu)$.

\emph{Hypothesis (SH), a hypothesis of this result, not a premise of the store.} The count rule of Proposition \claimref{singularity.stretched-singularity-count} ($\nu$ modes per Planck cell of the three-volume that a surface invariant under the Killing flows sweeps per unit Killing time) is read on the stretched horizon $\mathcal{S}_{\rho_0}$, the surface at proper distance $\rho_0$ from the horizon locus $r = r_+$ along the gradient lines of $r$, and the counted epoch is $\beta_+$, as Theorem \claimref{scrambling.epoch-modular-period-two-unknowns-become} has it for Schwarzschild.
\begin{enumerate}
\item[(i)] \emph{(Volume rate, any Killing flow.)} On a surface $r = \mathrm{const}$ the Gram determinant of $\hb^{-1}(\partial_t + \Omega\partial_\phi)$, $\hb^{-1}(\partial_u)$, $\hb^{-1}(\partial_\phi)$ is $-\Delta\Sigma$ for every constant $\Omega$. So the three-volume swept per unit Killing parameter is
\[
V'(r) \;=\; 2\pi\sqrt{|\Delta(r)|}\;I(r), \qquad I(r) = \int_{-1}^{1}\sqrt{r^2 + a^2u^2}\,du ,
\]
the same for the static flow $\partial_t$ and the co-rotating flow; the surface is spacelike for $r_- < r < r_+$ and timelike otherwise. At $a = 0$ this is $4\pi r^2\sqrt{|1 - 2M/r|}$. The choice of the co-rotating flow enters the count only through the epoch.
\item[(ii)] \emph{(Rate per unit area and distance.)} The gradient lines of $r$ run at fixed $u$, and the proper length along them from the locus $r = r_\pm$ is $\ell_\pm(r,u) = |\int_{r_\pm}^{r}\sqrt{\Sigma/|\Delta|}\,dr'|$. With $w = \sqrt{|\Delta|\Sigma}$ the rate per $du\,d\phi$ and $P_\pm\,du\,d\phi$ the area element of the locus's cross-section,
\[
\lim_{r\to r_\pm}\frac{w(r,u)}{P_\pm\,\ell_\pm(r,u)} \;=\; \kappa_\pm \qquad\text{for every } u \in [-1,1],
\]
from either side: the rate per unit cross-section area per unit proper distance is the surface gravity, the same at every latitude.
\item[(iii)] \emph{(The count.)} The volume rate of $\mathcal{S}_{\rho_0}$ satisfies $V'_{\rho_0}/(\kappa_+\rho_0A_+) \to 1$ as $\rho_0/M \to 0$ at fixed $a/M < 1$. Under (SH) the count over one modular period is therefore, at leading order in $\rho_0/M$,
\[
N \;=\; \nu\,\kappa_+\rho_0A_+\cdot\frac{2\pi}{\kappa_+} \;=\; 2\pi\nu\rho_0\,A_+ ,
\]
and with the Schwarzschild value $\nu\rho_0 = 1/(8\pi)$ (the density $\nu = 1/16\pi$ of Theorem \claimref{scrambling.epoch-modular-period-two-unknowns-become}, 1-nat convention, at $\rho_0 = 2$ Planck lengths) $N = A_+/4$ for every $a/M \in [0,1)$, with no input depending on the spin. Only the product $\nu\rho_0$ enters.
\item[(iv)] \emph{(Not a test.)} In (iii) the surface gravity cancels between the rate and the period, and it does so by (ii), which is the definition of the surface gravity of a Killing horizon ($\sqrt{|Q(K)|} = \kappa\ell$ at leading order) together with its constancy over the horizon. So under (SH) the count per modular period is $2\pi\nu\rho_0$ times the cross-section area on the Kerr horizon whatever $M$ and $a$ are: the comparison with $A_+/4$ cannot fail, and the Kerr entropy does not test the density $\nu$ once the count is placed on the horizon. (SH) is the three-volume form of a constant entropy density per unit area, $2\pi\nu\rho_0$.
\item[(v)] \emph{(The Schwarzschild formula does not fix its carry.)} On Schwarzschild the rate $8\pi\nu M$ of Proposition \claimref{singularity.stretched-singularity-count} equals $\nu\beta$ and $2\nu\kappa A$. Carried to Kerr with the epoch $\beta_+$ and $\nu = 1/16\pi$, these three forms give
\[
\frac{N}{A_+/4} \;=\; \frac{M}{s}\ \ (\text{rate } 8\pi\nu M), \qquad \frac{Mr_+}{2s^2}\ \ (\text{rate } \nu\beta_+), \qquad 1\ \ (\text{rate } 2\nu\kappa_+A_+),
\]
that is $1 + \tfrac12(a/M)^2$, $1 + \tfrac34(a/M)^2$ and $1$ to second order in $a/M$; the first two are unbounded as $a \to M$. The third is the rate of (iii) at $\rho_0 = 2$, and by the Smarr relation $M = 2T_HS + 2\Omega_HJ$ it is
\[
2\nu\kappa_+A_+ \;=\; 16\pi\nu\,T_HS \;=\; 8\pi\nu\,(M - 2\Omega_HJ) \;=\; 8\pi\nu\sqrt{M^2 - a^2} .
\]
\item[(vi)] \emph{(Other slices with the same rate.)} $\kappa_-A_- = \kappa_+A_+ = 4\pi s$, so by (ii) the surface at proper distance $\rho_0$ from the inner locus has the same leading rate as $\mathcal{S}_{\rho_0}$. A surface $r = \mathrm{const}$ gives $N = A_+/4$ at $\nu = 1/16\pi$ over $\beta_+$ exactly when $\sqrt{|\Delta(r)|}\,I(r) = 4s$. On Schwarzschild this reads $r^3|2M - r| = 4M^2$, which for $M^2 > 64/27$ has exactly three roots: one in $(r_c, r_c + 1/r_c)$, $r_c = (2M)^{1/3}$ the cutoff radius of Proposition \claimref{singularity.stretched-singularity-count} (for $r_c \ge 2$), and one on each side of the horizon, at $r = 2M \mp \tfrac{1}{2M}(1 + o(1))$, which is proper distance $2$ at leading order. So on Schwarzschild (SH) with $\rho_0 = 2$ and the cutoff placement give the same count at leading order in $1/M$.
\item[(vii)] \emph{(Extremal limit.)} As $a \to M$ the rate $8\pi\nu s$ of (v) tends to zero, the period $\beta_+ = 4\pi Mr_+/s$ diverges, and their product stays $4\pi\nu A_+ \to 32\pi^2\nu M^2$. At $a = M$ itself $\Delta = (r - M)^2$, the length $\ell_+$ of (ii) diverges logarithmically, so no surface lies at finite proper distance from the horizon locus along the gradient lines of $r$, and $\kappa_+ = 0$ gives no modular period: the count of (iii) exists at $a = M$ only as the limit.
\end{enumerate}

## technical
The Schwarzschild count is a three-volume count: $\nu$ modes per Planck cell of the volume a slice sweeps per unit Killing time, $8\pi M$ on the cutoff slice, over one modular period $8\pi M$. The stored literal reading of that rule on the Kerr field (at the Planck-curvature locus) misses the area law. This result asks what the same kind of count gives when it is placed on the horizon instead, as a hypothesis (SH): the surface at fixed proper distance $\rho_0$ from the horizon locus of the Kerr gauge field, counted over the modular period $2\pi/\kappa_+$ of the co-rotating Killing flow.

The three-volume that a surface $r = \mathrm{const}$ sweeps per unit Killing parameter is $2\pi\sqrt{|\Delta|}\int\sqrt{r^2 + a^2u^2}\,du$ exactly, and it is the same for the static and the co-rotating flow, so the flow matters only through the period. Near the horizon locus the rate per unit cross-section area is $\kappa_+$ times the proper distance, at every latitude. Hence the stretched horizon sweeps $\kappa_+\rho_0A_+$ per unit time and the count per period is $2\pi\nu\rho_0A_+$: with the Schwarzschild value $\nu\rho_0 = 1/8\pi$ it is $A_+/4$ at every spin below extremality, at leading order in $\rho_0/M$, with no spin-dependent input.

This is not a test of the density. The surface gravity cancels between rate and period because the rate is, by the definition of surface gravity and its constancy on the horizon, $\kappa_+$ times distance times area; the result holds for all $M$ and $a$ and could not have come out otherwise. What does discriminate is the form in which the Schwarzschild rate is carried: $8\pi\nu M$ and $\nu/T_H$, both stored forms, overshoot on Kerr by $M/s$ and $Mr_+/2s^2$, $s = \sqrt{M^2 - a^2}$ (by $\tfrac12(a/M)^2$ and $\tfrac34(a/M)^2$ at slow rotation), and only $2\nu\kappa A$ survives, which by the Smarr relation is $8\pi\nu(M - 2\Omega_HJ)$: under (SH) the accrual rate is proportional to $T_HS$, not to $1/T_H$. On Schwarzschild (SH) with $\rho_0 = 2$ and the cutoff placement agree at leading order (the rate $8\pi M$ is reached on three slices: near the cutoff radius and at proper distance two on either side of the horizon). The inner horizon locus has the same product $\kappa_-A_- = \kappa_+A_+$. In the extremal limit the rate tends to zero and the period to infinity with a finite product; at extremality the count exists only as that limit.

## lay
The series counts a non-rotating black hole's hidden modes on a surface deep inside the hole, and the count, taken over one cycle of the hole's natural clock, equals the known entropy. For spinning holes that inner surface gives the wrong answer. This result places the same kind of count just next to the horizon instead, at a fixed tiny distance from it, as an assumption to be examined and not as an adopted rule. With the packing density already fixed on non-rotating holes, the count then equals the entropy of a spinning hole at every spin short of the maximum, for large holes, with nothing adjusted. But this success is automatic: the clock's period and the rate at which the surface sweeps out volume both contain the hole's surface gravity, and it cancels exactly, for any horizon of this kind. So a spinning hole cannot test the packing density once the count sits at the horizon. What the spin does expose is that two other ways of writing the non-rotating count, which agree there, give different and wrong answers for a spinning hole.

## one-liner
If the count rule is placed on the Kerr stretched horizon at proper distance $\rho_0$ and counted over $2\pi/\kappa_+$ of the co-rotating flow, the count is $2\pi\nu\rho_0A_+$ at leading order in $\rho_0/M$, equal to $A_+/4$ at the Schwarzschild value $\nu\rho_0 = 1/8\pi$ for every $a < M$; $\kappa_+$ cancels by definition, so this is no test, while the rate forms $8\pi\nu M$ and $\nu/T_H$ miss by $M/s$ and $Mr_+/2s^2$.
