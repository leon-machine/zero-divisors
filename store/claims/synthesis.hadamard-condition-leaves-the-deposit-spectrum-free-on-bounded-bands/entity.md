---
id: synthesis.hadamard-condition-leaves-the-deposit-spectrum-free-on-bounded-bands
kind: claim
version: 3
title: 'The Hadamard condition leaves the deposit spectrum free on bounded bands'
status: proved
region: synthesis
subject: dark-energy
tags: [frozen-point, no-go, pairing-and-bogoliubov, undetermined-input, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-01-deposit-state
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - synthesis.imported-microlocal-hadamard-condition@2
  - synthesis.imported-de-sitter-invariant-hadamard-state-unique@2
  - synthesis.frozen-point-geometry-reads-descent-as-vacuum@1
  - standard-model.imported-frozen-point-dictionary@7
  - synthesis.imported-ford-parker-infrared-divergence@1
  - synthesis.imported-conformal-covariance-of-massless-fields-and-local-conformal-flatness@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_conformal_mode_equation_and_complex_unit
- kind: check
  ref: check.py::check_every_positive_ratio_is_reached_on_a_band
- kind: check
  ref: check.py::check_price_of_a_ratio
- kind: check
  ref: check.py::check_conformal_energy_has_no_cross_term
- kind: check
  ref: check.py::check_band_difference_kernel_is_regular
- kind: check
  ref: check.py::check_power_laws_fail_the_energy_moment
- kind: check
  ref: check.py::check_red_law_has_no_infrared_end
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.frozen-point-geometry-reads-descent-as-vacuum
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb
  - synthesis.local-conversion-cannot-redden-a-gaussian-spectator
  - synthesis.imported-propagation-of-hadamard-form
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By Leon''s ruling R4 (one unit per entity; the entity already read its complex numbers as a + b I_4): the Wronskian normalisation chi chi-bar'' - chi'' chi-bar = I_4, the conformal modes e^{-I_4 k eta}/sqrt(2k), the Bogoliubov phases e^{+-2 I_4 k eta_d} and the Bunch-Davies control e^{-I_4 z}(1 - I_4/z) are written with I_4 (formal and proof), exact since span{1, I_4} is the complex numbers; no bare i remains, so the declaration is removed.'
  open_problem: op.descent-state-and-spectrum
  note: >-
    Bears on op.deposit-state-is-hadamard (the primordial spectrum as the infrared data of a Hadamard
    deposit) and on the open part of op.descent-state-and-spectrum on bosonic fields with occupations
    far above one. Answer: if the series' states are Hadamard, nothing about the spectrum on any bounded band of
    scales follows. Relative to the frozen point's invariant state (the conformal vacuum for the conformal
    weight), any bounded Bogoliubov or occupation data supported in a bounded shell give a Hadamard state, and
    every positive ratio to the vacuum's spectrum on a band is reached by a pure state, so the amplitude and the
    index on the observed band, the measured ones included, are data the Hadamard condition does not touch. What
    it does fix is the ultraviolet: the energy moments of the occupations are finite, so no power law of the
    ratio holds up to arbitrarily large k, the store's law n_k ~ k^(n_s - 3) included, and a homogeneous,
    dilatation-invariant Hadamard state is the vacuum. The existence of the state fixes the infrared side: a red
    law cannot continue to k -> 0. So a red band needs two ends, k_IR and k_UV, which the Hadamard condition
    requires (k_UV) or leaves to the existence of the state (k_IR) and fixes in neither case. Consequences for
    the stored no-gos (argued, not part of the formal statement): the frozen-point reading
    (synthesis.frozen-point-geometry-reads-descent-as-vacuum) and the Gaussian conversion result
    (synthesis.local-conversion-cannot-redden-a-gaussian-spectator) hold for the invariant state, a subclass of
    the Hadamard states, and are not strengthened by the Hadamard condition; the finite-range bound
    (synthesis.finite-range-descent-deposit-cannot-seed-cmb) is state-independent and unchanged, and the band
    states here are not of finite range (the Fourier transform of shell-supported data has no compact support);
    the Kasner results compute the exited spectrum of the vacuum on the approach, and under the premise carrying
    the pre-descent state into the descended phase a Hadamard state there is again free on bands. The
    renormalised (point-split) stress tensor of these states differs from the vacuum's by the finite energy
    density of the band, and the observed spectrum is the two-point function at separated points, which the
    Hadamard subtraction does not change; the proposal of Parker and collaborators (Agullo, Navarro-Salas, Olmo
    and Parker 2009) to subtract adiabatically at the scale of the observed modes, and its critique by Durrer,
    Marozzi and Rinaldi (2009), are cited from memory and not used. Literature: Ford and Parker (1977) on infrared
    divergences in Robertson-Walker universes, with the criterion of Higuchi and Rendell (arXiv 1711.03964,
    divergence for mode exponents nu >= (n - 1)/2), imported as synthesis.imported-ford-parker-infrared-divergence; Junker and Schrohe
    (2002) and Lueders and Roberts (1990) on adiabatic states and the Hadamard condition, cited from memory and
    not used: the proof uses only the smooth-difference characterisation of the imported microlocal Fact.
    Standard parts: the Hadamard property of finite-band Bogoliubov data (i), the rapid decay of the
    occupations of a Hadamard state (iii), the infrared divergence of red and scale-invariant laws (iv, Ford and
    Parker) and the uniqueness of the dilatation-invariant Hadamard state (the analogue of the alpha-vacua not
    being Hadamard) are standard; the reading for the descent's deposit is what is new. The "only if" half of
    (iii) for the massless Dirac field over the conformal vacuum, with the converse, is the result (synthesis.deposit-over-the-conformal-vacuum-is-hadamard-exactly-when-every-occupation-moment-is-finite),
    which is primary for that criterion; (iii) here is its scalar counterpart by an independent route (the
    cross-term-free energy weight 2k n_k). Transport-absent: the content is standard free field theory; the
    series supplies the setting (the frozen point's field under (F), the conformal weight of the dictionary,
    i = I4).
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, at Leon''s decisions of 2026-11-01 (deposit-state imports): uses edges to the imported Facts on the infrared divergence (Ford and Parker) and on conformal covariance replace the citations in the proof''s scope paragraph and the flag; the pins move to the microlocal Fact version 2 and the de Sitter-invariant state Fact version 2 (added statements and notes, not used here). Statement, proof steps and checks otherwise unchanged; clause (iii) off the frozen point still assumes the conformal vacuum Hadamard.'
  flags:
  - 'clauses (i), (ii) and (iv) hold relative to any homogeneous Hadamard reference state of a scalar field on a spatially flat Robertson-Walker field; clause (iii) is stated for the conformally coupled massless field with its conformal vacuum as reference, proved on the frozen point''s field (where it is the weight -1 field of the dictionary) and, on other spatially flat Robertson-Walker fields, given that the conformal vacuum is Hadamard there (the conformal covariance is the imported Fact synthesis.imported-conformal-covariance-of-massless-fields-and-local-conformal-flatness; the Hadamard property of the conformal vacuum there is assumed)'
  - 'the infrared clause is about the field algebra of the deposited field on the slice; it is evaded by restricting to fields smeared with test functions of zero mean, itself a choice the series would have to make'
---

## formal
Let $\phi$ be a real scalar field on a spatially flat Robertson-Walker field in conformal time, $\chi = a\phi$, and let $\omega_{\mathrm{ref}}$ be a homogeneous isotropic quasi-free Hadamard state with mode functions $\chi_{k}(\eta)$ (smooth in $\eta$, continuous in $k > 0$, Wronskian $\chi_{k}\bar\chi_{k}' - \chi_{k}'\bar\chi_{k} = I_{4}$) and slice spectrum $\Delta_{\mathrm{ref}}^{2}(k) = k^{3}|\chi_{k}(\eta_{d})|^{2}/(2\pi^{2}a^{2})$ on a slice $\eta = \eta_{d}$. A homogeneous isotropic quasi-free state $\omega$ is given relative to $\omega_{\mathrm{ref}}$ by measurable data $n_{k} \ge 0$, $c_{k}$ with $|c_{k}|^{2} \le n_{k}(n_{k} + 1)$ ($n_{k} = |\beta_{k}|^{2}$, $c_{k} = \alpha_{k}\bar\beta_{k}$ for a pure state with modes $u_{k} = \alpha_{k}\chi_{k} + \beta_{k}\bar\chi_{k}$, $|\alpha_{k}|^{2} - |\beta_{k}|^{2} = 1$); its slice spectrum is $\Delta_{\omega}^{2} = \rho_{k}\Delta_{\mathrm{ref}}^{2}$ with $\rho_{k} = 1 + 2n_{k} + 2\,\mathrm{Re}(c_{k}\theta_{k})$, $\theta_{k} = \chi_{k}(\eta_{d})^{2}/|\chi_{k}(\eta_{d})|^{2}$. Complex numbers are read as $a + bI_{4}$.
\begin{enumerate}
\item[(i)] \emph{(Bands are free.)} If $n_{k}$ and $c_{k}$ are bounded and vanish outside a bounded shell $k_{1} \le k \le k_{2}$, $k_{1} > 0$, then $\omega$ is Hadamard: its two-point function differs from that of $\omega_{\mathrm{ref}}$ by a smooth bisolution. For every continuous $\rho: [k_{1}, k_{2}] \to (0, \infty)$ the pure state with $|\beta_{k}| = \sinh(|\ln\rho_{k}|/2)$, $\beta_{k}\bar\theta_{k}$ in phase with $\alpha_{k}$ for $\rho_{k} \ge 1$ and opposite in phase for $\rho_{k} < 1$, and $\beta_{k} = 0$ off the band, is such a state and has slice spectrum $\rho_{k}\Delta_{\mathrm{ref}}^{2}$ on the band and $\Delta_{\mathrm{ref}}^{2}$ off it. So the amplitude and the index of the spectrum on any bounded band are not constrained by the Hadamard condition.
\item[(ii)] \emph{(The price of a ratio.)} Every $\omega$ has $4n_{k}\rho_{k} \ge (\rho_{k} - 1)^{2}$, that is $n_{k} \ge (\sqrt{\rho_{k}} - 1/\sqrt{\rho_{k}})^{2}/4$, with equality for the pure states of (i).
\item[(iii)] \emph{(The ultraviolet end, conformally coupled field.)} Let $\phi$ be conformally coupled and massless, so $\chi'' + k^{2}\chi = 0$, and let $\omega_{\mathrm{ref}}$ be its conformal vacuum, $\chi_{k} = e^{-I_{4}k\eta}/\sqrt{2k}$, assumed Hadamard (on the frozen point's field, $a = -1/(H\eta)$, this is the field of weight $w = -1$ of the dictionary of Fact \claimref{standard-model.imported-frozen-point-dictionary}, $m^{2} = 2H^{2}$, and its conformal vacuum is the stabiliser-invariant Hadamard state of Fact \claimref{synthesis.imported-de-sitter-invariant-hadamard-state-unique} used in Theorem \claimref{synthesis.frozen-point-geometry-reads-descent-as-vacuum}, slice spectrum $k^{2}/(4\pi^{2}a^{2})$). If $\omega$ is Hadamard then $\int k^{3 + 2j}n_{k}\,dk < \infty$ for every integer $j \ge 0$. Hence no law $\rho_{k} = Ck^{q}$ with $(C, q) \neq (1, 0)$ holds for all $k$ above any $K$ in a Hadamard state: no power-law ratio on a band unbounded toward short scales; in particular a slice correlator homogeneous of degree $-2\Delta$ with $\Delta \neq 1$ is not the slice two-point function of a Hadamard state, and the occupation law $n_{k} \propto k^{n_{s} - 3}$ cannot hold up to arbitrarily large $k$. A homogeneous isotropic quasi-free Hadamard state invariant under the dilatation $(\eta, \vec x) \mapsto (\lambda\eta, \lambda\vec x)$ of the frozen point's field is $\omega_{\mathrm{ref}}$.
\item[(iv)] \emph{(The infrared end, for slice fields of nonzero mean.)} The slice fields $\phi(g)$ have finite variance in $\omega$ for every test function $g$, those of nonzero mean included, only if $\int_{0}^{k_{1}}\Delta_{\omega}^{2}(k)\,dk/k < \infty$. A law $\Delta_{\omega}^{2} \propto k^{n - 1}$ with $n \le 1$ (red or scale invariant) on an interval $(0, k_{1})$ fails this; blue laws ($n > 1$) on $(0, k_{1})$ meet it, and so may be Hadamard there. The Hadamard condition does not involve this integral.
\end{enumerate}
Consequently, if the deposited state is Hadamard, a red spectrum is allowed on any bounded band, on no band unbounded toward short scales and, for slice fields of nonzero mean, on no band reaching $k = 0$: it must end below some $k_{\mathrm{IR}} > 0$ and above some $k_{\mathrm{UV}} < \infty$, and neither end, nor the amplitude and index between them, is fixed by the Hadamard condition.

## technical
The question is what the Hadamard condition would say about the primordial spectrum if the descent's deposit satisfied it. The answer is: nothing on any bounded band of scales. Measured against any homogeneous Hadamard reference state (on the frozen point's field, its invariant state; on a collar of the descent, an admissible vacuum there), a deposit is described by occupations $n_{k}$ and pair terms $c_{k}$; if these vanish outside a bounded shell, the deposit differs from the reference by a smooth kernel and is Hadamard. Every positive ratio to the reference spectrum on a band is reached by a squeezed pure state, at the price $n_{k} \ge (\sqrt{\rho} - 1/\sqrt{\rho})^{2}/4$. So the amplitude and the tilt on the observed band are free data.

The condition bites only toward short scales. For the conformally coupled field the energy difference has the positive Fourier weight $2kn_{k}$ exactly, with no cross term, so a Hadamard state has finite moments $\int k^{3 + 2j}n_{k}\,dk$: no power-law ratio continues to arbitrarily short scales, and a dilatation-invariant homogeneous Hadamard state is the vacuum, of index $2$. At long scales the state has to exist on slice fields of nonzero mean: their variance needs $\int_{0}\Delta^{2}\,dk/k < \infty$, which a red or scale-invariant law continued to $k \to 0$ violates, while a blue law there is allowed. A red band therefore needs an ultraviolet and an infrared end. The ingredients (finite-band Bogoliubov data, rapid decay of occupations, the infrared divergence of Ford and Parker, the uniqueness of the invariant state) are standard; the reading for the deposit is the content. The result is transport-absent.

## lay
The series needs the quantum state left by the descent to be of a regular kind, called Hadamard, so that energies and horizon physics make sense. One might hope that this regularity would also fix the pattern of primordial ripples seen in the sky. This result shows it does not. The Hadamard condition only controls the shortest distances; over any finite range of scales, including the whole range astronomers measure, the state can have any strength and any tilt of ripples. What the condition and the existence of the state do require is that a pattern tilted like the observed one must stop somewhere at very short scales and somewhere at very long ones, and nothing in the condition says where.

## one-liner
Relative to any homogeneous Hadamard reference state a homogeneous deposit can have any spectrum on any bounded band of scales; for the conformally coupled field a power-law ratio holds on no band unbounded toward short scales, and, for slice fields of nonzero mean, a red law on no band reaching k = 0, so a red band needs two ends that the Hadamard condition does not fix.
