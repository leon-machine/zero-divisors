---
id: synthesis.local-conversion-cannot-redden-a-gaussian-spectator
kind: claim
version: 2
title: 'A local conversion cannot redden a Gaussian spectator'
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
  - synthesis.frozen-point-geometry-reads-descent-as-vacuum@1
  - synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise@3
  - synthesis.imported-planck-2018-lcdm-parameters@3
  - synthesis.imported-mehler-formula-hermite-rank-and-power-law-spectra@1
  - synthesis.imported-curvaton-and-modulated-reheating-coefficients@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_mehler_orthogonality
- kind: check
  ref: check.py::check_conversion_covariance_positive
- kind: check
  ref: check.py::check_local_degree_mean_order
- kind: check
  ref: check.py::check_index_never_below_field
- kind: check
  ref: check.py::check_series_fields_give_blue
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.kasner-approach-gives-horizon-exit-and-index-three
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb
  - standard-model.dating-descent
extraction:
  open_problem: op.descent-state-and-spectrum
  note: >-
    Outside mechanisms read in the series' terms. The curvaton (Lyth and Wands; Moroi and Takahashi;
    Enqvist and Sloth) and modulated reheating (Dvali, Gruzinov and Zaldarriaga; Kofman) make the
    curvature perturbation a local function of a light field: zeta = (2/3) delta sigma/sigma - (1/3)(delta
    sigma/sigma)^2 + (2/9)(delta sigma/sigma)^3 + ... for a curvaton that dominates at decay, zeta = -(1/6)
    delta Gamma/Gamma at first order for a modulated decay rate (coefficients from Choi and Seto,
    Modulated reheating by curvaton, arXiv:1204.1419, eqs. 16 and 46, imported as the Fact
    synthesis.imported-curvaton-and-modulated-reheating-coefficients). In the series the same structure is
    the classical modulation of the descent's deposit (T_desc(x) set by a field), the escape left open by
    synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise. In inflation these mechanisms inherit the field's
    tilt (n_s - 1 = 2 eta_sigma - 2 epsilon for a dominant curvaton, cited from memory); the general lemma
    here is the classical Hermite-rank result for functions of Gaussian fields (Taqqu 1975; Dobrushin and
    Major 1979, imported with Mehler's formula and the Fourier asymptotics of a power law as the Fact
    synthesis.imported-mehler-formula-hermite-rank-and-power-law-spectra; see Bai and Taqqu, arXiv:1610.00684, on the Hermite rank and its
    instability under a level shift, which is why c_1 is generically nonzero), and the series enters only
    through (iii). It gives the inheritance for every local conversion of a Gaussian field without inflation, and so
    shows that the conversion step cannot be the source of a red tilt: the field itself must already carry
    a red spectrum. It covers the conversion step left open by
    synthesis.kasner-approach-gives-horizon-exit-and-index-three, for spectators with a power-law correlation;
    by (ii) it also applies to the Kasner spectra of the hidden-scale-coupled scalars synthesis.kasner-hidden-scale-coupled-scalars-stay-blue (field index at least 1 there), so the conversion
    step cannot rescue them. Filed alongside, synthesis.adiabatic-deposit-modulation-is-a-time-shift says
    which direction of the deposit's data a modulation must lie along; this result bounds its index, so a
    time-shift field that is a local function of a Gaussian field read through the frozen point has index
    about 2.
    Transport-absent: Gaussian probability (Mehler's formula, a classical identity checked exactly here) and
    the Fourier transform of a power law (the weight Gamma(2 - beta) sin(pi(2 - beta)/2)), both in the
    imported Fact above.
    Not covered: non-Gaussian fields, non-local (gradient) conversions, fields with a red or scale-invariant
    spectrum (m <= 0), and logarithmic corrections at m = 3.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: Mehlers formula, the Hermite-rank result and the Fourier asymptotics of a power-law correlation (one imported Fact) and the curvaton and modulated-reheating coefficients (a second imported Fact), cited from memory or checked in version 1, now cite the Facts (uses edges added, claimrefs in the proof); the Planck parameters pin moved to version 2 (densities added there, not used here); the pin to synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise moved to its version 2 (a pointer note to this result added there). No clause changed.'
---

## formal
Let $\sigma$ be a statistically homogeneous and isotropic Gaussian field on a spatial slice: a classical Gaussian random field, or the field of a quasi-free state smeared over a fixed length and evaluated at spacelike separation, where its two-point function is real and Wick's theorem holds. Write $x = (\sigma - \bar\sigma)/s$ with $s^{2}$ its variance and $\rho(r)$ the normalised correlation of $x$ at separation $r$. Let $\zeta = f(\sigma)$ be a local conversion with finite variance, $f = \sum_{n} c_{n}\mathrm{He}_{n}(x)$ in the probabilists' Hermite polynomials, and let $n_{0} \ge 1$ (the Hermite rank) be the least $n \ge 1$ with $c_{n} \neq 0$.
\begin{enumerate}
\item[(i)] \emph{(Mehler.)} $\mathrm{Cov}(\zeta(\mathbf{x}), \zeta(\mathbf{y})) = g(\rho(r))$ with $g(\rho) = \sum_{n \ge 1} c_{n}^{2}\, n!\, \rho^{n}$, every coefficient non-negative.
\item[(ii)] \emph{(Local degree.)} Wherever $0 < \rho(r) \le 1$, $\dfrac{d\ln g(\rho(r))}{d\ln r} = \bar n(\rho)\,\dfrac{d\ln\rho}{d\ln r}$ with $\bar n(\rho) = \rho g'(\rho)/g(\rho)$, a weighted mean of the orders $n$ with weights $c_{n}^{2}n!\rho^{n} \ge 0$, so $\bar n \ge n_{0}$; if $c_{1} \neq 0$ then $\bar n = 1 + O(\rho)$. On any range of separations where $\rho$ falls, the converted correlation falls at least $n_{0}$ times as fast, and with a linear term at the field's own rate up to a relative correction of order $\rho$.
\item[(iii)] \emph{(Index.)} If moreover $\rho(r) = A r^{-m}(1 + o(1))$ as $r \to \infty$ with $A > 0$ and $0 < m < 3$ (dimensionless spectrum of $\sigma$ behaving as $k^{m}$ on large scales), then as $k \to 0$ the dimensionless spectrum of $\zeta$ behaves as $k^{n_{0}m}$ if $n_{0}m < 3$, and as $k^{3}$ or a higher power if $n_{0}m > 3$. Its large-scale index is at least $m$, and equals $m$ whenever $c_{1} \neq 0$.
\item[(iv)] \emph{(The series' fields.)} Under hypothesis (F), Theorem \claimref{synthesis.frozen-point-geometry-reads-descent-as-vacuum} gives every stabiliser-invariant Hadamard state of a field of the series on the descent slice the vacuum's index $2$ up to corrections of order $(k|x_{d}|)^{-2}$ on observed scales: exactly $2$ for the conformal weight, $2(k|x_{d}|)^{2}/(1 + (k|x_{d}|)^{2})$ for the massless field, and between $2 - 2/((k|x_{d}|)^{2} - 2)$ and $3$ for every unitary-series field at leading adiabatic order, where $k|x_{d}| > 2.7$ at the largest observed scales and about $960$ at the pivot. Since $\rho$ is small and positive at observed separations, a curvaton, a modulated descent or any other local conversion with $c_{1} \neq 0$ keeps that index, and one with $c_{1} = 0$ raises it. Against the measured $n_{s} - 1 = -0.0351 \pm 0.0042$ (Fact \claimref{synthesis.imported-planck-2018-lcdm-parameters}) the converted index is blue by more than $1.6$ at the largest observed scales and by more than $1.99$ at the pivot, more than $380$ and $480$ standard deviations away.
\end{enumerate}
So a classical modulation of the descent's deposit by a Gaussian field, the escape left open by Theorem \claimref{synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise}, supplies the measured tilt only if the modulating field already has a red spectrum, which no field read through the frozen point's invariant state has.

## technical
Outside inflation, the standard way to turn a light field's fluctuations into the curvature perturbation is a local conversion: a curvaton that comes to dominate and decays, or a decay rate (here, the descent's deposit) that depends on the field's local value. The curvature perturbation is then a function of the field at each point. For a Gaussian field the classical Hermite-rank argument applies. Expanding the function in Hermite polynomials, Mehler's formula writes the correlation of the converted quantity as a positive series in the field's normalised correlation: the first power from the linear part, the square from the quadratic part, and so on. Differentiating, the converted correlation's logarithmic slope is the field's slope times a weighted mean of the orders, which is at least the lowest order present and is one up to a correction of the size of the correlation when a linear part is present. So a conversion never makes a correlation fall more slowly than the field's, and for a power-law field the large-scale index is the field's own, $m$, or $\min(n_{0}m, 3)$ without a linear part. The conversion step cannot produce a red tilt from a blue field. Applied to the series under hypothesis (F): the frozen point's invariant state gives every field on the descent slice the vacuum's index $2$ up to corrections of order $(k|x_{d}|)^{-2}$, so every curvaton-type or modulated-descent reading of such a field gives the same index or a bluer one, where $-0.035$ is measured. A red spectrum would have to be present in the modulating field before conversion; fields with modulus couplings on a Kasner approach and non-Gaussian fields are not covered here.

## lay
Without a period of rapid early expansion, one alternative way to seed the ripples in the early universe uses a second field whose values vary from place to place and which then sets how much energy each region receives. This result shows that this conversion step cannot by itself produce the slight tilt toward large scales that is measured: whatever the conversion, if the second field's ripples are tilted toward small scales, the converted ripples are tilted at least as much. If the framework's fields are read at the universe's origin through the frozen point's symmetric state, as its preferred reading of the late cosmological constant implies, every one of them has ripples strongly tilted toward small scales, so the conversion route fails unless some field first acquires the right tilt on its own.

## one-liner
For a Gaussian field, Mehler's formula makes the correlation of any local conversion $\zeta = f(\sigma)$ a positive series $\sum c_{n}^{2}n!\rho^{n}$, so its logarithmic slope is the field's times a mean order at least the Hermite rank, and the large-scale index is the field's $m$ (or $\min(n_{0}m, 3)$ without a linear term), never lower; under hypothesis (F) the series' fields on the descent slice have index $2$ up to $O((k|x_{d}|)^{-2})$, so curvaton and modulated-descent readings stay blue by more than $1.6$, over $380$ standard deviations from the measured $-0.0351$.
