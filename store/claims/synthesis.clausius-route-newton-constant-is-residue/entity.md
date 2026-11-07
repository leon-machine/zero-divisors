---
id: synthesis.clausius-route-newton-constant-is-residue
kind: claim
version: 4
title: 'Newton''s constant on the Clausius route is a consistency only'
status: proved
region: synthesis
subject: entropy
tags: [mode-counting, curvature-and-field-equations, counting-rules, hawking-temperature, needs-continuum]
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
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - scrambling.mode-count@2
  - scrambling.epoch-modular-period-two-unknowns-become@6
  - synthesis.residue-from-mode-entropy@4
  - synthesis.quarter-from-temperature@1
  - angle.imported-theorems-deliver-their-hypotheses@3
  - synthesis.imported-jacobson-clausius-1995@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_accrual_versus_epoch
- kind: check
  ref: check.py::check_newton_constant_ratio
- kind: proof
  derivation: main
extraction:
  correction:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'W503: the lay level and one-liner now state the conditions of clauses (ii) and (iii), the epoch count under (IC) and the if-clause that it hold on every local Rindler horizon. Version 2 -> 3.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Maintainer pass: Jacobson''s theorem (J), stated as a hypothesis cited from memory, is now the imported Fact synthesis.imported-jacobson-clausius-1995, added to uses and cited in the statement, proof and check; the one-liner says imported theorem instead of hypothesis. The conditional in (iii) (if (b) held on every local Rindler horizon) is unchanged. Version 1 -> 2.'
  open_problem: ein.clausius-route
  note: >-
    Maps Jacobson's 1995 derivation onto the store. Temperature: imported (Bisognano-Wichmann,
    Unruh) for flat-space fields; the series' own regularity premises supply it at Killing horizons
    only ((R) at Schwarzschild, (R_Lambda) at the de Sitter cosmological horizon). Entropy: of the
    two counts in the store only the epoch count is a Clausius entropy; under (IC) it is 4 pi nu
    modes per Planck area per period on the Schwarzschild family. Newton's constant: Jacobson's step
    would return G_cl = G/(16 pi nu <s>), and G_cl = G is the same condition as the area-law
    condition that defines the registered nu, so it is a consistency, not a determination of G.
    Jacobson's theorem (J) is the imported Fact synthesis.imported-jacobson-clausius-1995. Transport-absent. Fix round 2026-10-22-toe:
    restated as a consistency at every level (the referee's weaker statement); the survey of where
    the store places boundary modes moved to a remark and corrected to Killing horizons; check
    rebuilt from the surface gravity, with the registered nu derived twice and a negative control.
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: Jacobson''s local Rindler horizons read at x0 in a gauge with hb(x0) = 1, Omega(x0) = 0; his conclusion written G(a) + Lambda a = -(2 pi/eta) T(a) in the store''s sign (DICTIONARY C6), the tensor form kept as Jacobson''s reading; flat-space fields named as vanishing gravitational field. Clauses (i)-(iii) unchanged; proof given a pointer.'
---

## formal
Let (J) be Jacobson's theorem (Fact \claimref{synthesis.imported-jacobson-clausius-1995}): if at every point $x_0$ of a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) and for every physically null direction the local Rindler horizon (the flat null hyperplane piece through $x_0$ in a gauge with $\hb(x_0) = 1$, $\Omega(x_0) = 0$) (a) is at the temperature $a/2\pi$ of its boost flow, (b) has entropy $\eta$ per unit area with $\eta$ one universal constant, and (c) satisfies $\delta Q = T\,\delta S$ for the boost-energy flux of matter across it, then $\mathcal{G}(a) + \Lambda a = -(2\pi/\eta)\,T(a)$ in the store's sign (in Jacobson's tensor form, $G_{ab} + \Lambda g_{ab} = (2\pi/\eta)\,T_{ab}$ for the derived metric), with $\Lambda$ an undetermined constant. Units $\hbar = c = 1$, with $G$ the constant that defines the Planck cell.
\begin{enumerate}
\item[(i)] \emph{(Temperature.)} (a) holds for quantum fields in flat space with vanishing gravitational field by the Bisognano-Wichmann and Unruh clauses of Fact \claimref{angle.imported-theorems-deliver-their-hypotheses}; the series' own regularity premises supply the corresponding temperature only at Killing horizons: (R) at the horizon of a Schwarzschild hole (Theorem \claimref{synthesis.quarter-from-temperature}) and (R$_{\Lambda}$) at the de Sitter cosmological horizon.
\item[(ii)] \emph{(Which count is an entropy.)} The accrual count of Theorem \claimref{scrambling.mode-count}, $N = 8\pi\nu M\,\Delta t$, is not a Clausius entropy: along a stationary horizon no flux crosses and the area is constant, so (c) requires $dS/dt = 0$, while $dN/dt = 8\pi\nu M > 0$. The epoch count of Theorem \claimref{scrambling.epoch-modular-period-two-unknowns-become}, over one modular period $2\pi/\kappa = 8\pi M$ under (IC), is $64\pi^{2}\nu M^{2} = 4\pi\nu\,A$, a fixed multiple of the area along the Schwarzschild family, so with mean mode entropy $\langle s\rangle$ it would supply (b) on that family with $\eta = 4\pi\nu\langle s\rangle$.
\item[(iii)] \emph{(A consistency, not a determination of $G$.)} If (b) held on every local Rindler horizon with this $\eta$, (J) would return Einstein's equations with $G_{\mathrm{cl}} = 1/(4\eta) = G/(16\pi\nu\langle s\rangle)$. The condition $G_{\mathrm{cl}} = G$, that is $16\pi\nu\langle s\rangle = 1$, is the area-law condition $\nu\,\Delta t\,\langle s\rangle = M/2$ of the epoch count, which is how the registered value $\nu = 1/(16\pi\ln 2)$ at zero weight is defined (Theorem \claimref{scrambling.epoch-modular-period-two-unknowns-become}); under the black-hole calibration $\kappa_{c} = 1/(4\langle s\rangle)$ of Theorem \claimref{synthesis.residue-from-mode-entropy}, $\eta = \tfrac14$ identically. So the route is consistent with the registered value and carries no information on $G$ beyond the area-law condition.
\end{enumerate}

## technical
Jacobson derived Einstein's equations, in Gauge Theory Gravity the field equations $\mathcal{G}(a) + \Lambda a = -8\pi G\,T(a)$ of a gravitational field on flat spacetime, by demanding that heat crossing every small local horizon change its entropy by heat over temperature, with temperature from the Unruh effect and entropy proportional to area. Mapped onto the series: the temperature is imported for fields in flat space with vanishing gravitational field, and the series' own regularity premises supply it only at Killing horizons (the black hole's and the de Sitter cosmological horizon). Of the two mode counts in the store, the running count that grows linearly in Killing time is not an entropy in Clausius' sense, since it grows on a stationary horizon where no heat flows; the count per modular period is, and on the Schwarzschild family it is $4\pi\nu$ modes per Planck area.

If that count held on every local horizon, Jacobson's step would give Einstein's equations with Newton's constant $G/(16\pi\nu\langle s\rangle)$, in units of the $G$ that defines the counting cells. The two agree exactly when the area-law condition holds, and that condition is how the registered value $\nu = 1/(16\pi\ln 2)$ was obtained in the first place, so the agreement is a consistency and not a determination of $G$. Remark (a survey of the store, not a theorem): the store places boundary modes and counting rules only on Killing horizons, the Schwarzschild horizon and the de Sitter cosmological horizon; nothing places them on a local Rindler horizon through a regular point, and that is the step of Jacobson's derivation the series lacks. The cosmological constant comes out as an integration constant on this route.

## lay
One famous argument gets Einstein's equations from thermodynamics: every small patch of horizon must gain entropy in proportion to the heat that crosses it. The framework can supply the temperature in flat space and at black-hole and cosmological horizons, and it has a count of quantum modes that grows with area. If the count, taken over one period of the horizon's thermal cycle as the series assumes, held on every small horizon and were fed into the argument, it would reproduce the strength of gravity exactly when the count's open calibration number takes the value that was itself chosen to match black-hole entropy, so the agreement is a consistency check, not a prediction. What the framework does not yet have is a reason for modes to sit on every small horizon, not just on black holes and the cosmological horizon.

## one-liner
On Jacobson's Clausius route (the imported theorem (J)) the epoch count ($4\pi\nu$ modes per Planck area per period under (IC); the accrual count fails Clausius) would give, if it held on every local Rindler horizon, $G_{\mathrm{cl}} = G/(16\pi\nu\langle s\rangle)$, and $G_{\mathrm{cl}} = G$ is the area-law condition that already defines the registered $\nu$: a consistency, not a determination of $G$; the missing step is a count on non-Killing horizons.
