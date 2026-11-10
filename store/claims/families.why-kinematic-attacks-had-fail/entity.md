---
id: families.why-kinematic-attacks-had-fail
kind: claim
version: 4
title: Why the kinematic attacks had to fail
status: proved
region: families
subject: generations
tags:
- the-number-n
- no-go
- cosmological-constant
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 4
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  uses:
  - families.imported-dictionary-exact-join@7
  - standard-model.trichotomy-what-kind-number@12
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T13.py
  tags:
  - label:prop:covariance
- kind: check
  ref: check.py::check_imaginary_weight_is_mass_in_hubble_units
- kind: check
  ref: check.py::check_rescaling_weights
- kind: check
  ref: check.py::check_covariance_forces_linear
locators:
  paper: T13
  number: Prop 7.5
  label: prop:covariance
  line: 883
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The de Sitter weight -3/2 +- i nu, a physical number, is written -3/2 +- I_4 nu with numbers read in span{1, I_4}; no bare i remains.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Im w = m/H = N (m/M_P) as exponent monomials, the rescaling weights (N -1, m/M_P 0), and covariance forcing a linear relation, with N^(2/3) and Zel''dovich-Weinberg failing. Version 2 -> 3.'
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - the de Sitter weight -3/2 +- i nu (a complex number labelling a principal-series representation,
      not an operator unit)
  env: proposition
  context_refs:
  - families.absolute-scale-clean-negative-result
  typing:
    by: ai-typing-pass
    note: 'Kept both edges; the absolute-scale Observation is cited only for comparison and as the map
      of routes this closes, so it is not a premise; the result stands at the observation level of its
      rescaling-invariance premise. Levels pass: the lay level now marks the invariance premise as observation
      level and restores the formal''s "in this framework" for the coincidence.'
lineage:
  motivated_by:
  - families.absolute-scale-clean-negative-result
---

## formal
On the principal series $w = -\tfrac32 \pm I_4\nu$ with $\nu = m/H + O(H/m)$ (numbers are read in $\mathrm{span}\{1, I_4\}$) (Fact \claimref{families.imported-dictionary-exact-join}), so that $\mathrm{Im}\,w$ is the mass in Hubble units and, trivially,
\[
\mathrm{Im}\,w \;=\; \frac{m}{H} \;=\; N \cdot \frac{m}{M_{P}} .
\]
Under the rescaling of Fact \claimref{standard-model.trichotomy-what-kind-number}, $\Lambda \to \kappa^{2}\Lambda$ at fixed $M_{P}$, the two factors have different status: $N \to N/\kappa$, which is the proved clause of Fact \claimref{standard-model.trichotomy-what-kind-number}; and $m/M_{P}$ is invariant, $m$ fixed while $H \to \kappa H$, which is the observation-level reading of \cite[Prop.~7.6(1)]{ButlerT12} recorded in Fact \claimref{standard-model.trichotomy-what-kind-number} and is the premise of this proposition, so that the proposition stands at that level. Granting it, $\mathrm{Im}\,w \to \mathrm{Im}\,w/\kappa$, and consequently any relation $\mathrm{Im}\,w = f(N)$ that holds across the family of frozen points must satisfy $f(N/\kappa) = f(N)/\kappa$ for every $\kappa > 0$, which forces $f$ linear, $\mathrm{Im}\,w = cN$ with $c = m/M_{P}$ a rescaling invariant. A power law $\mathrm{Im}\,w \sim N^{a}$ with $a \neq 1$, the hadronic $N^{2/3}$ of Observation \claimref{families.absolute-scale-clean-negative-result} or any other clean exponent, is the relation $m/M_{P} \sim N^{a - 1}$ between two independent continuous moduli of the kinematic layer, which by Fact \claimref{standard-model.trichotomy-what-kind-number} fixes neither. So no kinematic attack can give an exponent other than one, and the exponent one says only that $m/M_{P}$ is a number. The Zel'dovich-Weinberg coincidence, $m_{h}^{3} \sim M_{P}^{2}H$, is $m_{h}/M_{P} \sim N^{-1/3}$ and can be, in this framework, only a coincidence of the present epoch or a dynamical relation among couplings, never a kinematic theorem. The map of failed routes in Observation \claimref{families.absolute-scale-clean-negative-result} is thereby closed by a proof rather than left open: the absolute scale dissolves into three separately assigned pieces, $N$ (the cosmological constant, behind the promotion decision and then the descent measure, the Standard-Model paper's successor (5)), the rung unit $v/M_{P} \approx 2 \times 10^{-17}$ (a second rescaling-invariant modulus, the Standard-Model paper's successor (1), so kinematically not a function of $N$), and the Yukawa pattern, $y_{e} \approx 3 \times 10^{-6}$ and the ratios (Section \ref{sec:weights}). Only the third has computable structure available; and the second-order breaking and the CKM angles, being ratios and angles, are invariant under the rescaling and independent of the first two, so they depend on the third alone.

## technical
On the principal series $w = -\tfrac32 \pm I_4\nu$ (numbers are read in $\mathrm{span}\{1, I_4\}$), the imaginary weight is the mass in Hubble units, $\mathrm{Im}\,w = m/H = N\,(m/M_{P})$ with $N = M_{P}/H$. Under the rescaling $\Lambda \to \kappa^{2}\Lambda$ at fixed $M_{P}$, $N \to N/\kappa$ (a proved clause), while $m/M_{P}$ is invariant (an observation-level premise, at whose level the result stands). Granting it, any relation $\mathrm{Im}\,w = f(N)$ valid across the frozen points must satisfy $f(N/\kappa) = f(N)/\kappa$ for every $\kappa > 0$, which forces $f(N) = cN$ with $c = m/M_{P}$.

So a power law $\mathrm{Im}\,w \sim N^{a}$ with $a \neq 1$, such as the hadronic $N^{2/3}$ or the Zel'dovich-Weinberg $m_{h}/M_{P} \sim N^{-1/3}$, relates two independent moduli and cannot be a kinematic theorem. The absolute scale splits into three separately assigned pieces: $N$, the rung unit $v/M_{P}$, and the Yukawa pattern; only the last has computable structure, and the rescaling-invariant breaking and CKM angles depend on it alone.

## lay
Particle masses are tiny next to the Planck mass yet enormous next to the expansion rate of the universe, which invites guesses that a mass is some power of one large cosmological number. Granting that masses stay fixed when the cosmological constant is rescaled, a premise held at observation level, this result shows that any such relation must be a plain proportionality, which says nothing new. So no purely kinematic argument could have found a different power, and the old coincidence linking the pion mass to cosmology can, in this framework, only be an accident of the present epoch or a dynamical effect.

## one-liner
Granting that $m/M_{P}$ is invariant when the cosmological constant is rescaled, covariance forces any kinematic relation between the imaginary weight and $N$ to be linear, so no kinematic attack can yield another exponent.
