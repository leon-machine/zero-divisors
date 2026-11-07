---
id: synthesis.adiabatic-deposit-modulation-is-a-time-shift
kind: claim
version: 2
title: 'A deposit modulation is adiabatic only as a local time shift'
status: proved
region: synthesis
subject: dark-matter
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
  - synthesis.mirror-temperature-measures-deposit-under-r@1
  - dark-matter.stored-asymmetry-charge-not-number@8
  - synthesis.imported-planck-2018-lcdm-parameters@3
  - synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise@4
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb@5
  - synthesis.imported-superhorizon-zeta-conservation@3
  - synthesis.imported-large-scale-potential-and-sachs-wolfe-relations@2
  - synthesis.imported-planck-2018-isocurvature-and-isotropy-bounds@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_entropy_map_and_kernel
- kind: check
  ref: check.py::check_deposit_law_consistency
- kind: check
  ref: check.py::check_single_modulations
- kind: check
  ref: check.py::check_sachs_wolfe_share
- kind: check
  ref: check.py::check_mirror_radiation_share
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.cold-mirror-needs-non-equilibrium-descent
  - dark-matter.p1-single-frozen-point
extraction:
  open_problem: op.pre-descent-theory
  note: >-
    Cross-subject import from the dark-matter results (the charge reading of the stored asymmetry and
    the mirror's deposit law) into the two descent problems. With quasi-free deposits reduced to the
    vacuum plus shot noise, the remaining carrier of a primordial spectrum in the deposit is a classical
    modulation of its local data, the separate-universe form of zeta. This result asks which of the
    deposit's stored parameters may carry it: the reheating temperature, the deposited charge, or the
    deposit per unit charge that the mirror's temperature measures. Only a modulation that keeps the
    charge per unit entropy and the deposit per unit charge uniform is adiabatic, so the charge face of
    the deposit (the entries of op.pre-descent-theory) must be spatially uniform and cannot carry the
    spectrum; the spectrum face (op.descent-state-and-spectrum) is narrowed to a field of local delays of
    the one descent, which still meets the finite-range bound and is not supplied by anything stored.
    Here epsilon is the mirror proposition's deposit per unit charge, not the asymmetry of Q = epsilon N in the
    charge reading. The kernel statement is for the three local data listed; populations not fixed by the
    charge would add entropy directions. Complementary to a result synthesis.local-conversion-cannot-redden-a-gaussian-spectator, which bounds the index of a local
    conversion of a Gaussian modulating field: together, a delay field that is a local function of a Gaussian
    field read through the frozen point has index about 2.
    Transport-absent: standard separate-universe perturbation theory applied to the stored deposit law.
    Imported as Facts: the conservation of each decoupled species' curvature perturbation on super-Hubble
    scales (Wands, Malik, Lyth and Liddle 2000; synthesis.imported-superhorizon-zeta-conservation, version 3),
    the large-scale Sachs-Wolfe combination for mixed adiabatic and matter-isocurvature modes (Langlois and
    Riazuelo 2000; synthesis.imported-large-scale-potential-and-sachs-wolfe-relations), the Planck 2018
    isocurvature bound (results X: the non-adiabatic contribution to the observed temperature variance is
    below 1.3 percent for matter isocurvature and 1.7 percent for neutrino density isocurvature at 95 percent
    confidence; synthesis.imported-planck-2018-isocurvature-and-isotropy-bounds), and the baryon and cold dark
    matter densities, 0.02237 and 0.1200 in units of h^2 (synthesis.imported-planck-2018-lcdm-parameters,
    version 2), which enter only the large-scale estimate of clause (iv). The separate-universe reading is
    standard and cited from memory.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: the conservation of each decoupled species zeta, the Langlois-Riazuelo large-scale combination, the Planck 2018 isocurvature bound and the baryon and dark matter densities, cited from memory or checked in version 1, now cite imported Facts (uses edges to the zeta-conservation Fact at version 3, the large-scale relations Fact and the Planck isocurvature Fact added; the Planck parameters pin moved to version 2, which now holds the densities); claimrefs in the proof and the formal statement; pins to synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise and synthesis.finite-range-descent-deposit-cannot-seed-cmb moved to their versions 2 and 4, which add pointer notes to this result. No clause changed.'
---

## formal
Assume Premise (R) through Proposition \claimref{synthesis.mirror-temperature-measures-deposit-under-r}, whose deposit law gives the mirror an energy $\varepsilon T_{\mathrm{desc}}$ per unit of its charge ($\varepsilon$ is that proposition's deposit per unit charge, not the asymmetry $\epsilon$ of $Q = \epsilon N$), thermalised at once, with $\xi^{4} = \tfrac43 Y_{B}\varepsilon$ up to a floor below $1.5 \times 10^{-5}$ in $\xi$; and the charge reading of Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}, under which the deposited charge is fixed by the descent's data independently of the tower's temperature and the mirror carries the same baryon charge as this tower. Read a classical modulation of the deposit on scales outside the descent's Hubble length in the separate-universe sense: each patch is an unperturbed descended universe with local data on a slice of uniform time at the deposit, namely the visible bath's temperature $T_{d}$, the charge density $n_{Q}$ (the same in this tower and the mirror) and $\varepsilon$, and the towers do not exchange energy afterwards. Write $v = (\delta\ln T_{d}, \delta\ln n_{Q}, \delta\ln\varepsilon)$. Each decoupled population keeps its curvature perturbation outside the Hubble length: $\zeta_{\gamma} = \delta\ln T_{d}$ for the visible radiation, $\zeta_{Q} = \tfrac13\delta\ln n_{Q}$ for every population whose number is fixed by the deposited charge (baryons, the mirror's baryons), $\zeta_{m} = \tfrac14\delta\ln(\varepsilon T_{d}n_{Q})$ for the mirror's radiation; write $S_{Q} = 3(\zeta_{Q} - \zeta_{\gamma})$ and $S_{m} = 3(\zeta_{m} - \zeta_{\gamma})$.
\begin{enumerate}
\item[(i)] \emph{(The adiabatic direction, for the three local data listed; further deposited populations not fixed by the charge would add entropy directions.)} $S_{Q} = \delta\ln n_{Q} - 3\,\delta\ln T_{d} = \delta\ln Y_{B}$ and $S_{m} = \tfrac34(\delta\ln\varepsilon + S_{Q}) = \tfrac34\,\delta\ln\xi^{4}$. The map $v \mapsto (S_{Q}, S_{m})$ has rank $2$ and kernel spanned by $(1, 3, 0)$: a modulation is adiabatic exactly when the charge per unit entropy and the deposit per unit charge are uniform and only $T_{d}$ varies with $n_{Q} \propto T_{d}^{3}$, which is a local shift of the time of the descent; then $\zeta_{\gamma} = \zeta_{Q} = \zeta_{m} = \delta\ln T_{d}$.
\item[(ii)] \emph{(The three parameters one at a time.)} (a) $T_{d}$ at fixed $n_{Q}$: $S_{Q} = -3\zeta_{\gamma}$ and $S_{m} = -\tfrac94\zeta_{\gamma}$. (b) $\varepsilon$ alone: $\zeta_{\gamma} = \zeta_{Q} = 0$ and $S_{m} = \tfrac34\delta\ln\varepsilon$; the photons, the baryons and every charge carrier have no curvature perturbation of their own outside the Hubble length, and the mode is a pure isocurvature mode of the mirror's radiation (which perturbs the photons only gravitationally, after re-entry), which is below $0.0388$ of the radiation at the deposit under the dark-radiation cap $\xi < 0.448$ and below $1.7 \times 10^{-7}$ of it for a helium mirror. (c) $n_{Q}$ alone: $\zeta_{\gamma} = 0$ and $S_{Q} = \delta\ln n_{Q}$.
\item[(iii)] \emph{(Consequence for the two descent problems.)} If the measured primordial spectrum is carried by a classical modulation of the deposit, it is carried by the time-shift direction of (i): the deposit per unit charge $\varepsilon$ and the charge per unit entropy must be spatially uniform up to the isocurvature the record allows, so the charge face of the deposit cannot carry the spectrum, and the spectrum's carrier is a field of local delays of the one descent, whose two-point function is still subject to the finite-range bound of Theorem \claimref{synthesis.finite-range-descent-deposit-cannot-seed-cmb}.
\item[(iv)] \emph{(Large-scale estimate, argued.)} For (a), the matter carrying the deposited charge is at least the baryons and the mirror's baryons, a fraction $f_{Q} \ge 2\Omega_{b}/\Omega_{m} > 0.31$ of the matter; in the large-scale Sachs-Wolfe combination $\zeta + 2S_{\mathrm{eff}}$, $S_{\mathrm{eff}} = f_{Q}S_{Q}$, the non-adiabatic part is $6f_{Q}|\zeta| > 1.88|\zeta|$, and for either relative sign the non-adiabatic share of the large-scale temperature variance exceeds $0.27$ in magnitude, more than twenty times the bound of $0.013$ from Planck 2018 (Fact \claimref{synthesis.imported-planck-2018-isocurvature-and-isotropy-bounds}). For (b) and (c) the photons carry no curvature perturbation of their own, so neither can be the measured adiabatic spectrum.
\end{enumerate}

## technical
Quasi-free deposits add only shot noise to the vacuum (Theorem \claimref{synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise}), so if the descent's deposit carries the primordial spectrum it does so as a classical modulation of its local data, the separate-universe form of the curvature perturbation. The stored deposit has three local data: the reheating temperature, the deposited charge (the same for this tower and the mirror under the charge reading) and the energy per unit charge that, under Premise (R), alone sets the mirror's temperature. Treating each patch as its own descended universe, and each decoupled population's curvature perturbation as conserved outside the Hubble length, the entropy perturbations of the charge carriers and of the mirror's radiation against the photons are linear in the three modulations with a one-dimensional kernel: the charge must scale as the cube of the temperature and the energy per unit charge must not vary, which is a local shift of the time of the descent. A modulation of the energy per unit charge alone gives the photons and the charge carriers no curvature perturbation of their own: it is a pure isocurvature mode of the mirror's radiation, a few percent of the radiation at most; a modulation of the temperature at fixed charge gives the baryons and the mirror's baryons an isocurvature of minus three times the curvature perturbation, which on large scales would dominate the temperature anisotropy against Planck's bound of about one percent on non-adiabatic power. So the charge face of the deposit, the entries of the pre-descent theory, must be spatially uniform, and the spectrum face is narrowed to a field of local delays of the descent, which the finite-range bound still constrains and nothing stored supplies.

## lay
In this framework the universe's earliest state is laid down in one event, which also sets how much matter each family of worlds holds and how much energy the mirror world received. The ripples seen in the cosmic microwave background are of one particular kind, called adiabatic: everything, light and matter alike, was disturbed together, as if some regions simply started a little later than others. This result asks which of the event's settings could vary from place to place to make such ripples, under the framework's reading of matter as a stored charge. Only one kind of variation works: the event happening at slightly different times in different places, with the amount of matter per unit of light and the energy given to the mirror world the same everywhere. Varying the energy given to the mirror world gives ordinary light and matter no ripple of their own, only a mismatch between the mirror world's light and ours; varying the event's temperature while the matter stays fixed gives the wrong kind of ripple, which the measurements rule out. So the numbers the framework still has to supply about the event must be the same everywhere, and the ripples still need a source the framework does not have.

## one-liner
Under (R) and the charge reading, a separate-universe modulation $(\delta\ln T_{d}, \delta\ln n_{Q}, \delta\ln\varepsilon)$ of the descent's deposit has charge and mirror isocurvature $S_{Q} = \delta\ln n_{Q} - 3\delta\ln T_{d}$, $S_{m} = \tfrac34(\delta\ln\varepsilon + S_{Q})$, vanishing only along $(1, 3, 0)$, a local time shift; $\varepsilon$ alone (the deposit per unit charge, not the asymmetry $\epsilon$) gives the photons and charge carriers no curvature perturbation of their own, a pure mirror-radiation isocurvature mode, and $T_{d}$ at fixed charge gives $S_{Q} = -3\zeta$, so the deposit's charge face must be uniform and cannot carry the spectrum.
