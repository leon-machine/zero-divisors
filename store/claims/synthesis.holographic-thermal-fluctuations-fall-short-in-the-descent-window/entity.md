---
id: synthesis.holographic-thermal-fluctuations-fall-short-in-the-descent-window
kind: claim
version: 2
title: 'Holographic thermal fluctuations fall short of the measured spectrum'
status: proved
region: synthesis
subject: dark-energy
tags: [no-go, confronted-with-data, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-01-five-fronts
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
  - singularity.area-law-test@5
  - synthesis.untuned-fit-caps-lightest-heavy-neutrino@1
  - synthesis.frozen-point-geometry-reads-descent-as-vacuum@3
  - synthesis.imported-planck-2018-lcdm-parameters@3
  - synthesis.imported-string-gas-thermal-spectrum-and-conversion@1
  - synthesis.imported-large-scale-potential-and-sachs-wolfe-relations@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_index_from_capacity_and_temperature
- kind: check
  ref: check.py::check_amplitude_in_window
- kind: check
  ref: check.py::check_frozen_point_temperature
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb
  - standard-model.dating-descent
  - synthesis.mirror-temperature-measures-deposit-under-r
extraction:
  maintainer_pass_2026_11_16:
    by: maintainer-2026-11-16
    date: '2026-11-16'
    note: 'Note added at the technical level, version kept, no statement changed (Leon''s decisions of 16 November 2026: the descent slice is left free and no reading is adopted). The conversion this result takes from the string-gas Fact is the uniform-expansion reading (UE) of synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit, in the variant (UE_Phi) named in synthesis.quasi-free-deposit-has-white-energy-noise-unless-pure-and-stationary, so this result and clause (iv) of synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise (stated under (FR) at its version 5) read the same white noise through different slice data. Claimrefs, not edges. No number, status, premise or pin changed.'
  open_problem: op.descent-state-and-spectrum
  note: >-
    Outside mechanism read in the series' terms: Nayeri, Brandenberger and Vafa (2006) obtain a scale-invariant
    spectrum from the thermal fluctuations of a string gas whose heat capacity scales as the area, C_V = 2
    (R^2/l_s^3)/(T(1 - T/T_H)), with P_Phi(k) = 8 G^2 k^-4 <delta rho^2>, <delta rho^2> = T^2 C_V/R^6 at R = 1/k,
    and a red tilt from the temperature falling across exit, n_s - 1 = (1 - T/T_H)^-1 k d(T/T_H)/dk (formulas
    from Brandenberger, arXiv:1505.02381, eqs. 2 and 4 to 8, where the exit dynamics, and so dT/dk, is not
    modelled, imported as the Fact synthesis.imported-string-gas-thermal-spectrum-and-conversion; the 8 G^2
    k^-4 form is eqs. 2 and 6 combined at R = 1/k; Phi = (2/3) zeta in the radiation era is imported as the
    Fact synthesis.imported-large-scale-potential-and-sachs-wolfe-relations). The series has an area law for horizons (singularity.area-law-test) and a join at which
    the observed modes pass from inside the frozen phase's horizon to outside the descent's Hubble length, the
    same topology as the string-gas exit. This result asks what the mechanism gives with the series' numbers.
    Hypotheses: the conversion is the imported one (Einstein gravity at exit, a sudden transition); the heat
    capacity is lam times the area entropy A/4G of a sphere of radius R; the temperature at exit is either the
    frozen point's Gibbons-Hawking temperature (under (F)) or at most the descent window's ceiling 7.3e8 GeV
    (under Premise (R), on the untuned fit under Premise (EW), via
    synthesis.untuned-fit-caps-lightest-heavy-neutrino). The area law of singularity.area-law-test is a
    calibrated boundary-mode capacity of a black hole; a horizon with T proportional to 1/R has a negative
    heat capacity, so gamma = 2 for the heat capacity of a sub-horizon region is the mechanism's hypothesis. The string gas reaches large lam only
    through the Hagedorn factor 1/(1 - T/T_H), a limiting temperature the series does not have. The
    conversion formula is the imported Fact named above. Constants cited:
    M_Pl = 1.22089e19 GeV, hbar = 6.58212e-25 GeV s, 1 Mpc = 3.08568e19 km. Transport-absent: the mechanism is
    thermodynamic; the series enters through the area law and the stored window and frozen-point reading.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: the string-gas conversion formulas and Phi = (2/3) zeta in the radiation era, cited in version 1, now cite the imported Facts (uses edges added, claimrefs in the formal statement and the proof); the Planck parameters pin moved to version 2 (densities added there, not used here). No clause changed.'
---

## formal
Assume the conversion of thermal fluctuations at Hubble exit used in string-gas cosmology (Fact \claimref{synthesis.imported-string-gas-thermal-spectrum-and-conversion}): a mode of physical wavenumber $k$ that leaves the Hubble length from a thermal phase of temperature $T$ carries $P_{\Phi}(k) = 8G^{2}k^{-4}\langle\delta\rho^{2}\rangle_{R}$ with $\langle\delta\rho^{2}\rangle_{R} = T^{2}C(R)/R^{6}$ at $R = 1/k$, where $C(R)$ is the heat capacity of a region of size $R$, and $\Phi = \tfrac23\zeta$ in the radiation era after exit (Fact \claimref{synthesis.imported-large-scale-potential-and-sachs-wolfe-relations}).
\begin{enumerate}
\item[(i)] \emph{(Index.)} If $C \propto R^{\gamma}$ and the temperature at exit varies as $T \propto R^{\tau}$ across the exiting scales, then $P_{\Phi} \propto k^{2 - \gamma - 2\tau}$, so $n_{s} - 1 = 2 - \gamma - 2\tau$. The area law, $\gamma = 2$ (Proposition \claimref{singularity.area-law-test} for horizons), at fixed temperature gives $n_{s} = 1$ exactly, between $8.3$ and $8.4$ standard deviations from the measured $n_{s} - 1 = -0.0351 \pm 0.0042$ (Fact \claimref{synthesis.imported-planck-2018-lcdm-parameters}); an extensive capacity gives $-1$; the area law at a modular temperature $T \propto 1/R$ gives $+2$. The measured value needs $\gamma + 2\tau = 2.0351$: with the area law, a temperature at exit rising as $R^{0.01755}$, one exponent for one number.
\item[(ii)] \emph{(Amplitude.)} With $C = \lambda A/4G$, $A = 4\pi R^{2}$, $P_{\Phi} = 8\pi\lambda (T/M_{\mathrm{Pl}})^{2}$ for every $k$. If the temperature at exit is at most the ceiling $7.3 \times 10^{8}$ GeV of the descent's window (Proposition \claimref{synthesis.untuned-fit-caps-lightest-heavy-neutrino}, under Premise (R)), then $P_{\Phi} < 9.0 \times 10^{-20}\lambda$, short of $\tfrac49 A_{s} = 9.33 \times 10^{-10}$ by more than $10^{10}$ unless $\lambda > 10^{10}$; at $\lambda = 1$ the measured amplitude needs $7.4 \times 10^{13} < T < 7.5 \times 10^{13}$ GeV, above the ceiling by more than $10^{5}$.
\item[(iii)] \emph{(Frozen point.)} At the frozen point's Gibbons-Hawking temperature $T = H_{\Lambda}/2\pi$, $H_{\Lambda}^{2} = H_{0}^{2}\Omega_{\Lambda}$ (the frozen phase of Theorem \claimref{synthesis.frozen-point-geometry-reads-descent-as-vacuum} under hypothesis (F)), $P_{\Phi} = 2\lambda H_{0}^{2}\Omega_{\Lambda}/(\pi M_{\mathrm{Pl}}^{2})$ lies between $10^{-123}\lambda$ and $10^{-122}\lambda$, short by more than $10^{112}$.
\end{enumerate}
So with the series' area law and either of its temperatures, the thermal-holographic mechanism gives the measured amplitude only with a heat capacity about $10^{10}$ times the area entropy or more, and its index only with a fitted temperature exponent.

## technical
String-gas cosmology replaces inflation's quantum fluctuations with thermal ones: in a quasi-static hot phase, a region of size $R$ has energy fluctuations set by its heat capacity, and if that capacity grows like the area of the region rather than its volume, the curvature perturbation left when the region leaves the Hubble length is the same on every scale. The series has two ingredients that resemble this: an area law for horizon entropy (not a heat capacity of sub-horizon regions, which the mechanism assumes), and a join at which the observed modes go from inside the frozen phase's horizon to outside the descent's Hubble length, the same sudden exit the string gas uses. Taking the cited conversion at face value, simple power counting gives the index as $2 - \gamma - 2\tau$ for capacity $\propto R^{\gamma}$ and temperature $\propto R^{\tau}$: the area law at fixed temperature is exactly scale invariant, over eight standard deviations from the measured red tilt, and the tilt needs a temperature exponent of about $0.018$ that nothing fixes. The amplitude is $8\pi\lambda(T/M_{\mathrm{Pl}})^{2}$ for a capacity of $\lambda$ times the area entropy. At the descent window's ceiling under Premise (R), $7.3 \times 10^{8}$ GeV, it is below $9 \times 10^{-20}\lambda$, about ten orders short; the measured amplitude needs about $7.4 \times 10^{13}$ GeV at $\lambda = 1$. At the frozen point's horizon temperature it is about $10^{-122}$. The string gas reaches the needed amplitude through a capacity enhanced near its Hagedorn temperature; the series has no limiting temperature, so the route needs an input the series does not supply.

\emph{Note (the conversion and the descent slice; added 16 November).} The conversion taken from the string-gas Fact is the Poisson relation with the potential read as the growing solution's: in the terms of Proposition \claimref{synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit} it is the reading (UE), a descent slice of uniform expansion, up to the factor between $\Phi$ and $\tfrac23\zeta$ (the variant (UE$_{\Phi}$) of Theorem \claimref{synthesis.quasi-free-deposit-has-white-energy-noise-unless-pure-and-stationary}). It is a hypothesis of this result, as the statement says; the series leaves the slice's expansion datum free and adopts no reading. An extensive capacity is white energy noise: its index $-1$ here and the index $3$ of clause (iv) of Theorem \claimref{synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise}, which is stated there under the flat-slice reading (FR), are the same white noise read through different slice data. The amplitudes of (ii) and (iii) are amplitudes under this conversion.

## lay
One alternative to a rapid early expansion seeds the early universe's ripples with heat: in a hot early phase, regions of different sizes have random energy differences, and if the heat a region can hold grows only with its surface area, the ripples come out the same on every scale. This framework has an area law for horizon entropy, though not the heat capacity the mechanism needs, and a moment when the ripples are carried out of causal contact. But with the framework's own numbers, the ripples come out exactly equal on all scales, where a slight tilt is measured, and, if a region holds no more heat than its surface-area entropy allows and the temperature is one the framework allows, they are about ten billion times too weak or worse.

## one-liner
Under the string-gas conversion $P_{\Phi} = 8G^{2}k^{-4}T^{2}C/R^{6}$, a capacity $\propto R^{\gamma}$ at temperature $\propto R^{\tau}$ gives $n_{s} - 1 = 2 - \gamma - 2\tau$ (area law at fixed $T$: exactly $0$, $8.4$ standard deviations off), and $C = \lambda A/4G$ gives $P_{\Phi} = 8\pi\lambda(T/M_{\mathrm{Pl}})^{2}$: below $9 \times 10^{-20}\lambda$ at the descent window's ceiling and about $10^{-122}\lambda$ at the frozen point's horizon temperature, against $9.3 \times 10^{-10}$ needed.
