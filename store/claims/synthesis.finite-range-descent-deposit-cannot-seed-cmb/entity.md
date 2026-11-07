---
id: synthesis.finite-range-descent-deposit-cannot-seed-cmb
kind: claim
version: 4
title: 'A finite-range descent deposit cannot seed the measured amplitude'
status: proved
region: synthesis
subject: dark-energy
tags: [no-go, confronted-with-data, frozen-point, cosmological-constant, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-23-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - synthesis.frozen-phase-spectrum-not-red@2
  - synthesis.quadratic-flows-cannot-thermalise-descent@1
  - synthesis.de-sitter-temperature-frozen-point-norm@5
  - synthesis.imported-planck-2018-lcdm-parameters@3
  - synthesis.imported-bbn-reheating-temperature-floor@1
  - synthesis.imported-superhorizon-zeta-conservation@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_amplitude_bound_constants
- kind: check
  ref: check.py::check_descent_hubble_ratio_and_pivot
- kind: check
  ref: check.py::check_correlation_range_needed
- kind: check
  ref: check.py::check_no_horizon_exit_after_descent
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.dating-descent
  - synthesis.sudden-descent-feature-not-tilt
  - dark-matter.p1-single-frozen-point
extraction:
  open_problem: op.descent-state-and-spectrum
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 2: the record inputs that version 1 cited from memory now rest on three imported Facts added to uses and reached in the check through premise() (synthesis.imported-planck-2018-lcdm-parameters, synthesis.imported-bbn-reheating-temperature-floor, synthesis.imported-superhorizon-zeta-conservation); Omega_r is corrected from 9.1e-5 to 9.2e-5, the value the Planck temperature and three relativistic neutrino species give at h = 0.674, with the two exact pins of the no-exit check recomputed; no conclusion changes.'
  maintainer_pass_2:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Version 2 -> 3. Added to (iii), the technical level and the one-liner that the required range is one comoving length for every T_d, a0 H0 R_req = (3 pi A_s/2)^(1/3)/(k_*/a0 H0), about 9.5e-6 of the present Hubble radius (about 42 kpc comoving), so the 460 and 6.8e17 Hubble lengths of the descent are that one length in a unit that grows with T_d; the computation is in synthesis.frozen-point-geometry-reads-descent-as-vacuum (ii), cited in the text. No statement or number of this claim changes.'
  note: 'Answer to "is a near-scale-invariant primordial spectrum possible at all from the descent": it is, but only as a deposit correlated far beyond the descended phase''s Hubble length, which the series must then supply as pre-metric initial data. The dating reads the descent, not an inflationary epoch, as the source of the earliest correlations; in a descended phase that decelerates until the Lambda era, no mode at or below the pivot scale leaves the Hubble length after the descent, so the pivot mode''s primordial (passive) amplitude is the deposit''s own spatial correlation at the descent, at a separation larger than the descent''s Hubble length by the computed factor. Any deposit whose correlations stop at a finite range (pure pairs across a horizon, a thermal or KMS state that clusters at the thermal length) then has an amplitude suppressed as the cube of k R, and the measured one needs R of hundreds (lowest reheating allowed by nucleosynthesis) to about 10^18 (reheating near the store''s heavy-neutrino scales) Hubble lengths, with a one-point variance below one. Clause (iv) records that the stored frozen-phase no-gos, if the frozen phase is the de Sitter stage of the observed Lambda, concern modes that leave its horizon only in the far future, so the binding constraint on the measured spectrum is this one. The id is stronger than the result: a deposit correlated beyond the stated ranges can seed the spectrum; the content is that it must be so correlated. Transport-absent: standard causality (white-noise) and horizon arithmetic with record inputs; the series supplies the setting (no inflation, descent at the origin, deposit not relaxation).'
  maintainer_pass_five_fronts:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 4: a marked pointer note after the formal statement sends the classically modulated deposit to synthesis.adiabatic-deposit-modulation-is-a-time-shift (adiabatic only as a field of delays, still under the bound) and synthesis.local-conversion-cannot-redden-a-gaussian-spectator (the classical-modulation escape closed for Gaussian modulators), as claimrefs, not edges, since both results use this one. The pins to the Planck parameters and superhorizon-zeta Facts moved to their versions 2 and 3 (additions there are not used here). No clause changed.'
---

## formal
Let the descent deposit, on the comoving slice of the descent, a scalar perturbation $\zeta$ whose two-point function is homogeneous and isotropic, $C(r) = \langle\zeta(\vec x)\zeta(\vec x + \vec r)\rangle$, with one-point variance $\sigma^{2} = C(0)$, power spectrum $P(k) = \int C(r)e^{-i\vec k\cdot\vec r}\,d^{3}r$ and dimensionless spectrum $\Delta^{2}(k) = k^{3}P(k)/2\pi^{2}$.
\begin{enumerate}
\item[(i)] \emph{(Finite range.)} If $C(r) = 0$ for $r > R$ (comoving), then for every $k$, $\Delta^{2}(k) \le \tfrac{2}{3\pi}\,\sigma^{2}(kR)^{3}$. If instead $|C(r)| \le \sigma^{2}e^{-r/\xi}$, then $\Delta^{2}(k) \le \tfrac{4}{\pi}\,\sigma^{2}(k\xi)^{3}$.
\item[(ii)] \emph{(No exit after the descent.)} Let the descended phase, from the descent to today, be a flat FLRW universe with $\dot a^{2}/H_{0}^{2} = \Omega_{r}a^{-2} + \Omega_{m}a^{-1} + \Omega_{\Lambda}a^{2}$ ($a_{0} = 1$, $\Omega_{m} = 0.315$, $\Omega_{r} = 9.2 \times 10^{-5}$, $\Omega_{\Lambda} = 1 - \Omega_{m} - \Omega_{r}$, the record values of Fact \claimref{synthesis.imported-planck-2018-lcdm-parameters}). Then $\dot a$ decreases on $(0, \tfrac12]$ and $\dot a \le H_{0}$ on $[\tfrac12, 1]$, so a mode with $k > a_{0}H_{0}$ that is outside the Hubble length at the descent enters once and never leaves it again before today. The pivot $k_{*} = 0.05\ \mathrm{Mpc}^{-1}$ has $k_{*}/a_{0}H_{0} \in (222, 223)$.
\item[(iii)] \emph{(The range needed.)} With the descent at reheating temperature $T_{d}$, at least $1$ MeV by the nucleosynthesis floor (Fact \claimref{synthesis.imported-bbn-reheating-temperature-floor}), and radiation domination from it (entropy conserved), $\rho(T_{d}) := a_{d}H_{d}/a_{0}H_{0}$ exceeds $4.9 \times 10^{7}$ at $T_{d} = 1$ MeV and $7.2 \times 10^{22}$ at $T_{d} = 10^{12}$ GeV, so the pivot lies outside the descent's Hubble length by more than $2.2 \times 10^{5}$ and $3.2 \times 10^{20}$ respectively. If the pivot's primordial amplitude, $\Delta^{2}(k_{*}) = A_{s} \ge 2.0 \times 10^{-9}$ (Fact \claimref{synthesis.imported-planck-2018-lcdm-parameters}: $(2.100 \pm 0.030) \times 10^{-9}$), is the deposit's, carried unchanged outside the Hubble length as an adiabatic $\zeta$ (Fact \claimref{synthesis.imported-superhorizon-zeta-conservation}), and $\sigma^{2} \le 1$, then (i) requires $R > 460/(a_{d}H_{d})$ at $T_{d} = 1$ MeV and $R > 6.8 \times 10^{17}/(a_{d}H_{d})$ at $T_{d} = 10^{12}$ GeV (and a clustering length $\xi > 250/(a_{d}H_{d})$ at $1$ MeV); the required range grows linearly with $T_{d}$ in units of the descent's Hubble length. In comoving units it is one length for every $T_{d}$: (i) gives $k_{*}R > (3\pi A_{s}/2)^{1/3}$, so $a_{0}H_{0}R > (3\pi A_{s}/2)^{1/3}\,a_{0}H_{0}/k_{*}$, about $9.5 \times 10^{-6}$ of the present Hubble radius (about $42$ kpc comoving; in $(9.4, 9.8) \times 10^{-6}$ over the recorded band of $A_{s}$, Proposition \claimref{synthesis.frozen-point-geometry-reads-descent-as-vacuum}(ii)), and the $T_{d}$ dependence above is that of the unit $1/(a_{d}H_{d})$.
\item[(iv)] \emph{(Scope of the frozen-phase results.)} If the frozen phase is the de Sitter stage of the observed $\Lambda$, $H_{\Lambda} = \sqrt{\Lambda/3} = H_{0}\sqrt{\Omega_{\Lambda}}$, the temperature of whose horizon is Theorem \claimref{synthesis.de-sitter-temperature-frozen-point-norm}'s $T_{\Lambda}$, then the pivot mode leaves that phase's Hubble length only at $a > 268\,a_{0}$, in the future: the late-time boundary on which Proposition \claimref{synthesis.frozen-phase-spectrum-not-red} reads the index is not where the measured spectrum was set.
\end{enumerate}
Consequently, in the series' history as the dating reads it (descent at the origin, no inflationary stage), a primordial spectrum of the measured amplitude at the pivot from the descent's deposit, passive and with $\sigma^{2} \le 1$, needs correlations over hundreds to about $10^{18}$ Hubble lengths of the descent, set before or outside the descended metric; a deposit of finite range at the Hubble or thermal length gives $\Delta^{2} \propto (kR)^{3}$ there, index $n_{s} - 1 = 3$ in the limit, and an amplitude far below $A_{s}$.

\emph{Note (pointer).} Two later results bear on a deposit that is not passive but classically modulated by a field: such a modulation is adiabatic only along a local time shift of the one descent, so the carrier is a field of delays, itself still subject to the bound of (i) (Proposition \claimref{synthesis.adiabatic-deposit-modulation-is-a-time-shift}); and a local conversion of a Gaussian modulating field into the curvature perturbation cannot lower the field's index, so under hypothesis (F) a Gaussian modulator read through the frozen point's invariant state gives index $2$ up to corrections of order $(k|x_{d}|)^{-2}$ (Proposition \claimref{synthesis.local-conversion-cannot-redden-a-gaussian-spectator}). The classical-modulation escape is therefore closed for Gaussian modulators; a red or non-Gaussian modulator is not covered.

## technical
The bound is the causality (white-noise) argument in its simplest form: the power spectrum of a field with correlations of finite range is bounded by the integral of the absolute correlation, at most the variance times the range volume, so the dimensionless spectrum falls as the cube of $kR$ on scales larger than the range, whatever the tilt inside it. The horizon arithmetic is standard: in a descended phase that decelerates until the dark-energy era, comoving Hubble lengths only grow, so a mode at the pivot was outside the descent's Hubble length by the factor $\rho(T_{d})/222$ and, once inside, never leaves. Exact rational bounds with record inputs give the factors in (iii).

So a descent can seed the measured spectrum only through a deposit whose correlations reach hundreds of Hubble lengths of the descent at the lowest reheating temperature nucleosynthesis allows (at least $1.8$ MeV, Fact \claimref{synthesis.imported-bbn-reheating-temperature-floor}, used here in the weaker form $1$ MeV) and about $10^{18}$ at the heavy-neutrino scales the store uses for $T_{\mathrm{desc}}$. These are one comoving length, about $9.5 \times 10^{-6}$ of the present Hubble radius, at every reheating temperature: what grows with the temperature is the descent's Hubble length used as the unit. Such correlations are not produced by anything inside the descended metric; they are initial data of the pre-metric sector. The pure-pair deposit of the quadratic-flows result, and any deposit that is locally the I-state and clusters at the thermal length, fall under (i). The stored frozen-phase no-gos, read at $H = H_{\Lambda}$, concern modes that leave the horizon only in the far future. Active causal sources after the descent are not covered; their incoherent acoustic peaks are excluded by the measured spectrum as a dominant source (cited from memory, not used).

## lay
In this theory the universe begins with a descent event rather than with inflation. The temperature ripples in the cosmic background were, at the moment of the descent, spread over distances far larger than anything that could have been in causal contact then. A deposit whose correlations stop at a finite distance gives ripples on much larger scales that are weaker by the cube of the ratio, so to produce the observed ripples the descent's initial state must already be correlated over hundreds to a billion billion of its own horizon lengths. Either the pre-spacetime phase supplies such long-range order, or a source acting after the descent does (which the observed acoustic peaks disfavour), or the theory cannot produce the observed spectrum.

## one-liner
A finite-range deposit has $\Delta^{2}(k) \le \tfrac{2}{3\pi}\langle\zeta^{2}\rangle(kR)^{3}$; with no horizon exit after the descent the pivot lay outside the descent's Hubble length by more than $2 \times 10^{5}$ to $3 \times 10^{20}$, so the measured amplitude (passive, with $\langle\zeta^{2}\rangle \le 1$) needs a deposit correlated over more than $460$ (at $1$ MeV) to $6.8 \times 10^{17}$ (at $10^{12}$ GeV) Hubble lengths of the descent, one comoving length (about $9.5 \times 10^{-6}$ of the present Hubble radius) at every reheating temperature, initial data of the pre-metric sector.
