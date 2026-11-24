---
id: synthesis.five-dimensional-plasma-exposure-is-one-inequality-in-coupling-mass-and-depth
kind: claim
version: 1
title: 'Five-dimensional relics: the plasma exposure is one inequality in coupling, mass and depth'
status: proved
region: synthesis
subject: dark-matter
tags: [halos-and-clusters, confronted-with-data]
proposed_by:
  kind: ai
  session: 2026-11-24-unit-ball-t14c
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'direction: whether the five-dimensional towers'' matter can collide at all'
- name: Claude Fable 5.2
  role: 'proposal, mathematics, check and drafting'
  source: run 2026-11-24-unit-ball-t14c
- name: Claude Opus 5.5
  role: 'blind referee: the single inequality, the exact stability of the lightest coloured species, the weights on the limits, the deposit'
  source: run 2026-11-24-unit-ball-t14c
review: draft
derivations:
- name: main
  uses:
  - dark-tower-matter.five-dimensional-content@5
  assumes:
  - dark-matter.e-equal-mass-per-unit-ball@1
  - dark-matter.r3-one-cell-per-unshared-direction@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_zero_mode_coupling_does_not_contain_the_mass
- kind: check
  ref: check.py::check_the_inequality_and_its_constant
- kind: check
  ref: check.py::check_readings_at_one_gev_and_at_the_rung_scale
- kind: check
  ref: check.py::check_a_tower_share_relaxes_the_limit
- kind: check
  ref: check.py::check_short_range_bound_and_binding
- kind: check
  ref: check.py::check_the_weaker_coefficient_is_the_square_of_the_charge_bound
lineage:
  motivated_by:
  - dark-tower-matter.five-dimensional-towers
  - dark-tower-matter.towers-built
  - dark-tower-matter.population
  - dark-matter.unit-ball-rule
  - synthesis.sheet-relic-bounds-under-e-fix-the-coupling-not-the-cells-mass
extraction:
  open_problem: op.odd-towers
  note: >-
    The companion of synthesis.sheet-relic-bounds-under-e-fix-the-coupling-not-the-cells-mass for the
    five-dimensional towers. The stored Computation dark-tower-matter.five-dimensional-towers(v) states the plasma
    exposure at the particle model (quanta of a GeV, depth d_b); the formulas are those of the source's supplement
    (T14c_supplement/D5C/verify_D5C.py, checks I3 and I4), with the charged mass and the depth left free. No edge is
    drawn to dark-tower-matter.five-dimensional-towers, which holds given R1 and R2; the zero mode and the form of
    the limits are stated as hypotheses local to this result, (Z) and (PL). The store holds no Fact for the imported
    plasma limits. Their coefficients are the supplement's. Read on 24 November 2026: arXiv:2411.15981 eq. (3) gives
    alpha_D < 4.2e-25 (L/100 kpc)^-2 (rho_D/0.01 GeV cm^-3)^-1 (m_D/TeV)^2 with alpha_D = e_D^2/(hbar c), which is
    the stronger coefficient with its mass scaling and a 1/rho scaling; arXiv:2411.11958 gives a bound on the charge,
    q < 2.8e-14 (m/GeV) in its first version (2.0e-14 in a later one), in units that appear to be Heaviside-Lorentz,
    so that alpha = q^2/(4 pi) and the supplement's 7.8e-22, which is q^2 at a TeV, would be too large by 4 pi. That
    reading of the second paper's units is an inference and was not confirmed; clause (vi) states both. The numbers
    of the annihilation branch (a charged residue of one percent needs g_5^2 m_c near 3e-3 at a GeV, rising about
    linearly with the mass and reaching the binding value near 5 TeV) are floating-point results of the supplement's
    freeze-out model and are not part of this result. Referee corrections applied (blind, one round): the condition
    stated as one inequality whose three factors are underived; the rung-scale coupling named as the supplement's
    assumption; the stability of the lightest coloured species stated as exact; the non-thermal deposit; the
    weights on the limits. Assumes edges to E and R3 are drawn for the maintainer to confirm.
---

## formal
\emph{Setting.} Assume Premise E (\claimref{dark-matter.e-equal-mass-per-unit-ball}) and Premise R3 (\claimref{dark-matter.r3-one-cell-per-unshared-direction}), and nothing about a tower's quanta. A five-dimensional tower ($r = 3, 5$) has the content of Proposition \claimref{dark-tower-matter.five-dimensional-content}; $m_{c}$ is the mass of a charged species that survives, $L = d$ the depth of the extra direction, E's common length, comoving and quoted at its present value, and $d_{b} \approx 0.98$ m. The gauge coupling $g_{5}^{2}$, a length, is written through the scale $E_{s} = 8\pi^{3}/g_{5}^{2}$, its strong-coupling scale for three colours. Two hypotheses are local to this result and are those of Computation \claimref{dark-tower-matter.five-dimensional-towers}(v): (Z) the gauge field keeps a four-dimensional zero mode, whose coupling is $\alpha_{4} = g_{5}^{2}/(4\pi L)$; (PL) the plasma-instability limits on a dark plasma in a cluster merger have the form $\alpha_{4} \le c\,(m_{c}/\mathrm{TeV})^{2}$ at the cluster's dark mass density, with $c = 4.2 \times 10^{-25}$ (Schoeffler, Shukla and Silva, arXiv:2411.15981) and $c = 7.8 \times 10^{-22}$ (as the source's supplement takes the bound of DeRocco and Giffin, arXiv:2411.11958). The particle model is the point $m_{c} = 1$ GeV, $d = d_{b}$.
\begin{enumerate}
\item[(i)] \emph{(The long-range coupling does not see the quanta.)} $\alpha_{4} = 2\pi^{2}/(E_{s}L)$: it is fixed by the coupling scale and the depth, and no mass appears. At $E_{s} = 10^{11}$ GeV and $d = d_{b}$ it is $3.97 \times 10^{-26}$.
\item[(ii)] \emph{(One inequality.)} Under (Z) and (PL) the tower is under the limit exactly when
\[
E_{s}\,m_{c}^{2}\,\frac{d}{d_{b}} \;\ge\; K(c) \;=\; \frac{2\pi^{2}\,\hbar c\,\mathrm{TeV}^{2}}{c\,d_{b}},
\]
with $K = 9.46 \times 10^{15}\ \mathrm{GeV}^{3}$ at $c = 4.2 \times 10^{-25}$ and $K = 5.09 \times 10^{12}\ \mathrm{GeV}^{3}$ at $c = 7.8 \times 10^{-22}$.
\item[(iii)] \emph{(Readings.)} At the particle model the inequality is a floor on the coupling scale alone, $E_{s} \ge 9.5 \times 10^{15}$ GeV or $5.1 \times 10^{12}$ GeV, and a deposit at $E_{s} = 10^{11}$ GeV is over the limits by factors of $9.5 \times 10^{4}$ and $51$: the exposure that Computation \claimref{dark-tower-matter.five-dimensional-towers}(v) states. At $E_{s} = 10^{11}$ GeV and $d = d_{b}$ it is a floor on the mass, $m_{c}$ above $308$ GeV or $7.1$ GeV, and along the threshold $m_{c}$ goes as $(E_{s}d)^{-1/2}$. So with charged quanta of a few hundred GeV or more, a deposit at that coupling is under both limits, with no annihilation and no neutral relic.
\item[(iv)] \emph{(Why the limits go as the square of the mass, and the tower's share.)} A plasma of mass density $\rho$ in quanta of mass $m_{c}$ has $\omega_{p}^{2} = 4\pi\alpha_{4}\rho/m_{c}^{2}$, and a limit on the growth of an instability over a crossing time is a limit on $\omega_{p}$, so at fixed mass density it bounds $\alpha_{4}/m_{c}^{2}$; E fixes the tower's mass density and leaves $m_{c}$ free, which is the case (PL) covers. The same form goes as $1/\rho$. One five-dimensional tower holds $8/(11\pi + 16) = 0.158$ of the dark matter, so read with the tower's own density each $K$ is smaller by that factor and each mass threshold by $2.51$; the values of (ii) and (iii) take the whole dark density.
\item[(v)] \emph{(Nothing else in the source's five-dimensional tests is worse for heavy quanta.)} With $\sigma_{5}$ of order $\beta^{2}/(\mu v)^{3}$, $\beta = m_{c}g_{5}^{2}C_{F}/(4\pi^{2})$, $\mu = m_{c}/2$, the short-range bound $\sigma_{\mathrm{eff}}/m = \sigma_{5}/(Lm_{c})$ goes as $1/m_{c}^{2}$ at fixed coupling. The $1/r^{2}$ potential binds only for $m_{c}g_{5}^{2}C_{F} \ge 4\pi^{2}$, that is $m_{c} \ge 3E_{s}/(8\pi) = 0.119\,E_{s}$, which is $1.19 \times 10^{10}$ GeV at $E_{s} = 10^{11}$ GeV. And the lightest coloured species is stable exactly, not only up to rung-scale operators: colour triality is conserved, a state of nonzero triality contains a coloured particle, and no such state is lighter than the lightest coloured species. So decays do not remove a tower's charged relic, and the inequality is a condition on the lightest coloured species and on any other charged species that survives.
\item[(vi)] \emph{(The weaker coefficient.)} $7.8 \times 10^{-22}$ is the square of the charge bound $2.8 \times 10^{-14}$ per GeV, at a TeV. If that bound is on a charge with $\alpha = q^{2}/(4\pi)$, the coefficient is $6.2 \times 10^{-23}$, $K$ is $6.4 \times 10^{13}\ \mathrm{GeV}^{3}$ and the mass threshold at $E_{s} = 10^{11}$ GeV, $d = d_{b}$ is $25$ GeV, not $7.1$ GeV. The stronger limit governs in either case.
\end{enumerate}
\emph{Limits.} The series fixes none of $E_{s}$, $m_{c}$ and $d$: the masses are bare (Observation \claimref{dark-tower-matter.r1-has-no-mechanism-odd-towers}), E gives its length no value, and a coupling at the rung scale $10^{11}$ GeV is an assumption of the source's supplement, not a result. So the inequality restates the choice that Observation \claimref{dark-tower-matter.towers-built} names, collisionless five-dimensional relics, in the form it takes on E and R3 alone; it does not remove it. Raising $m_{c}$ from $1$ GeV to $7$ GeV is the same step as raising $E_{s}$ by fifty. At a coupling this weak the species do not thermalise, so their number is the deposit's (Observation \claimref{dark-tower-matter.population}). The coefficients of (PL) are imported and are not checked in the store; they assume a plasma of unit charges. Whether such instabilities transfer bulk momentum in a merger is not established, so the inequality marks where the exposure itself is absent, not where an exclusion begins.

## technical
Assume E and R3 only, with the charged quanta's mass $m_{c}$ and the depth $d$ of a five-dimensional tower free. The zero mode's coupling, $\alpha_{4} = g_{5}^{2}/(4\pi L) = 2\pi^{2}/(E_{s}L)$, contains no mass, while a plasma-instability limit bounds the plasma frequency and so, at the fixed mass density E gives, goes as $m_{c}^{2}$. Under the source's two hypotheses (a zero mode; limits of the form $\alpha_{4} \le c\,(m_{c}/\mathrm{TeV})^{2}$) the exposure is the single inequality $E_{s}m_{c}^{2}(d/d_{b}) \ge K$, with $K = 9.46 \times 10^{15}\ \mathrm{GeV}^{3}$ for the stronger imported limit and $5.09 \times 10^{12}\ \mathrm{GeV}^{3}$ for the weaker as the supplement takes it. At a GeV and $d_{b}$ this is the source's floor on the coupling scale, by which a deposit at $10^{11}$ GeV fails by two to five orders; at $10^{11}$ GeV it is a floor on the mass of $308$ GeV or $7.1$ GeV.

The other five-dimensional tests do not get worse for heavy quanta: the short-range bound falls as $1/m_{c}^{2}$, binding needs $m_{c}$ above $0.119\,E_{s}$, and the lightest coloured species is exactly stable by colour triality. Read with one tower's share of the dark density, $0.158$, the mass thresholds fall by $2.51$. The weaker coefficient is the square of a charge bound; with $\alpha = q^{2}/(4\pi)$ it is $4\pi$ smaller and its threshold is $25$ GeV.

Limits: the series fixes none of the three factors, and the rung-scale coupling is the supplement's assumption, so the result restates the choice of collisionless five-dimensional relics and does not remove it; the quanta's number is a deposit; the limits' coefficients are imported; and the limits are an exposure, not an exclusion.

## lay
The five-dimensional hidden sectors hold charged particles, and charged matter can behave as a plasma when clusters of galaxies collide, which would show in the observations. A companion note found that these sectors would be exposed to that problem unless their force were extraordinarily weak. It assumed the particles weigh about what a proton does. This result redoes the test without that assumption. The strength of the long-range force does not depend on the particles' mass, while the plasma limits loosen quickly as the particles get heavier, because heavier particles are fewer for the same total mass. The whole test becomes one condition: the force scale, times the square of the particle mass, times the depth of the fifth direction must exceed a fixed number. With the force scale the note itself calls natural, particles a few hundred times heavier than a proton pass it. Nothing in the series fixes the force scale, the mass or the depth, so this does not show the sectors are safe; it shows that the condition is an ordinary one once the mass is free, not an extreme one.

## one-liner
Under Premises E and R3, assuming a gauge zero mode (Z) and plasma limits of the imported form (PL), with the charged mass $m_{c}$ and the depth $d$ free, the plasma exposure of a five-dimensional tower is the one inequality $E_{s}m_{c}^{2}(d/d_{b}) \ge 9.5 \times 10^{15}\ \mathrm{GeV}^{3}$ (stronger limit): the source's floor on the coupling scale at a GeV, and a floor of about $300$ GeV on the mass at $E_{s} = 10^{11}$ GeV.
