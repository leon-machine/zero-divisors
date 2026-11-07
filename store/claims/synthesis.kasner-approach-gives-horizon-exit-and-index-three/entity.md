---
id: synthesis.kasner-approach-gives-horizon-exit-and-index-three
kind: claim
version: 3
title: 'A Kasner approach gives horizon exit with index three and no red tilt'
status: proved
region: synthesis
subject: dark-energy
tags: [kasner, no-go, confronted-with-data, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
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
  - interior.kasner-form-interior@5
  - sheaf.kasner-data-interior@2
  - synthesis.bkl-bounce-invariant-holonomy-and-bound@2
  - synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands@1
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb@4
  - synthesis.imported-planck-2018-lcdm-parameters@3
  - synthesis.kasner-wall-matter-maxwell-bounces-stiff-moves-residue@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_exponent_sets_have_unit_sum
- kind: check
  ref: check.py::check_bessel_order_zero
- kind: check
  ref: check.py::check_pump_linear_in_conformal_time
- kind: check
  ref: check.py::check_normalisation_k_independent
- kind: check
  ref: check.py::check_index_between_two_and_three
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.dating-descent
  - synthesis.frozen-point-geometry-reads-descent-as-vacuum
  - dark-energy.frozen-point-datum-kasner-wall
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By Leon''s ruling R4 (scalar mode functions and Hankel Wronskians are written with the field theory''s unit, one reading with synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching and the other scalar-mode entities): the modes e^{I_4 k x^i}, the canonical normalisation tau(phi phi-dot* - phi* phi-dot) = I_4 and the Hankel Wronskians -2 I_4 W[J_0, Y_0] = -4 I_4/(pi s) are written with I_4 (proof), numbers read in span{1, I_4}, exact since that span is the complex numbers; no bare i remains, so the declaration is removed.'
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'uses edge added to synthesis.kasner-wall-matter-maxwell-bounces-stiff-moves-residue (pinned @2, its version after this pass), now stored: its classification of matter walls (stiff matter on the disk, an aligned Maxwell field subleading or reflecting by the BKL law, a fluid with w < 1 subleading) is what keeps sum p = 1 at the matter points the hypothesis admits; proof (i) cites it. Version 1 -> 2.'
  open_problem: op.descent-state-and-spectrum
  note: >-
    Cross-subject import from the interior results (the Kasner form near a wall, the BKL epochs) into the
    descent problem. The stored obstruction to the measured spectrum is horizon exit: no observed mode
    leaves the Hubble length after the descent, and the frozen phase carries them inside its horizon. Of
    the geometries in the store, the approach to a Kasner wall is the one in which modes do leave the
    Hubble length (contraction toward the wall); this result shows that for a massless minimally coupled
    spectator scalar it gives index between 2 and 3 within an epoch, not a red tilt, for every exponent
    set, because only sum p = 1 enters. It closes a metric pre-descent stage of interior type as a source
    of the spectrum for such scalars only: fields with a dilaton or modulus coupling (the hidden
    direction's Kaluza-Klein vector and moduli among them) have a different pump and are not covered
    (in pre-big-bang models such a coupling gives flat or red axion spectra, Copeland, Easther and Wands
    1997, cited from memory), nor is the conversion of a spectator spectrum into the curvature
    perturbation. The series' dating takes pre-descent physics to be pre-metric, so this is a closed
    alternative, not a reversal. Transport-absent: standard mode analysis; the isotropic stiff case is the
    blue spectrum of pre-big-bang models (Brustein, Gasperini, Giovannini and Veneziano 1995, cited from
    memory). Cited from memory in the proof: the Bessel Wronskian, the small-argument form of Y_0, and
    Watson's monotonicity of J_nu^2 + Y_nu^2 and of x(J_nu^2 + Y_nu^2) for nu below 1/2 (Nicholson's
    integral). Matter walls: the classification of matter walls,
    \claimref{synthesis.kasner-wall-matter-maxwell-bounces-stiff-moves-residue}, keeps sum p = 1 at every reachable
    epoch, which is all this result uses; the check includes two interior points of the disk.
---

## formal
Let a gravitational field on flat spacetime have, near a wall at $\tau = 0$, the synchronous diagonal derived metric $d\tau^{2} - \sum_{j}\tau^{2p_{j}}(dx^{j})^{2}$, the sum over the three observed directions and any hidden ones, with $\sum_{j}p_{j} = 1$: the vacuum Kasner points ($\sum_{j}p_{j}^{2} = 1$, the Schwarzschild interior's $(-\tfrac13, \tfrac23, \tfrac23)$ of Lemma \claimref{interior.kasner-form-interior} among them), each single epoch of a BKL approach (Theorem \claimref{synthesis.bkl-bounce-invariant-holonomy-and-bound}), the points inside the circle that a massless scalar or stiff matter reaches ($\sum_{j}p_{j}^{2} < 1$), and Kasner points with a hidden direction (the five-dimensional towers' direction of Proposition \claimref{synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands}, read at its zero mode). Let $\phi$ be a massless minimally coupled scalar (on a vacuum point, any curvature coupling $\xi R\phi^{2}$, since the scalar contraction of the field strength vanishes there), a spectator with no dilaton or modulus coupling, and let $k$ be a comoving momentum along a principal axis $i$ with $p_{i} < 1$ (every axis except at the flat Milne points). Write $q = 1 - p_{i}$ and $s = k\tau^{q}/q$.
\begin{enumerate}
\item[(i)] \emph{(Exit.)} $\sqrt{|g|} = \tau$, the mode equation is $\ddot\phi + \dot\phi/\tau + k^{2}\tau^{-2p_{i}}\phi = 0$, and the ratio of the gradient term to the friction scale $\tau^{-2}$ is $q^{2}s^{2}$, which tends to $0$ at the wall: every mode leaves the Hubble length as the wall is approached.
\item[(ii)] \emph{(Order zero.)} In $s$ the equation is Bessel's equation of order $0$, $\phi_{ss} + \phi_{s}/s + \phi = 0$, for every exponent set with $\sum_{j}p_{j} = 1$; equivalently the pump field $z^{2} = \sqrt{|g|}/a_{i} = \tau^{q} = q\,\eta_{i}$ is linear in the axis' conformal time. The sum of the squares of the exponents never enters, so within any one epoch neither the exponent values nor the hidden directions change the order; for $\sum_{j}p_{j} \ne 1$ the friction coefficient changes and the order is not $0$.
\item[(iii)] \emph{(Spectrum within an epoch.)} For a mode in its adiabatic vacuum while inside, within the epoch in which it exits, $\phi_{k} = N H^{(1)}_{0}(s)$ with $|N|^{2} = \pi/(4q)$ independent of $k$, so $\Delta^{2}(k) \propto k^{3}\bigl(J_{0}(s)^{2} + Y_{0}(s)^{2}\bigr)$ and the local index is $n - 1 = 3 + s\,\tfrac{d}{ds}\ln(J_{0}^{2} + Y_{0}^{2})$. It lies in $[2, 3]$ for every $s$, tends to $2$ inside and to $3$ outside, and exceeds $2.57$ for every mode at least a hundred times outside ($s \le 10^{-2}$); for $s \to 0$, $\Delta^{2} \propto k^{3}\bigl((\ln\tfrac{s}{2} + \gamma)^{2} + \tfrac{\pi^{2}}{4}\bigr)$. Across a BKL bounce, for modes already outside, the index is argued to persist.
\item[(iv)] \emph{(Confrontation.)} Against the measured $n_{s} - 1 = -0.0351 \pm 0.0042$ (Fact \claimref{synthesis.imported-planck-2018-lcdm-parameters}) the index is blue by more than $2$, where a red tilt is measured. The exited spectrum has the leading power $k^{3}$ of the bound of Theorem \claimref{synthesis.finite-range-descent-deposit-cannot-seed-cmb}, with a squared logarithm as enhancement, so as $k \to 0$ it exceeds that bound for every finite range: it is log-correlated, not a deposit of finite range.
\end{enumerate}
So for a massless minimally coupled spectator scalar, the one stage of the store's geometry in which modes leave the Hubble length gives a blue spectrum, index between $2$ and $3$, within each Kasner epoch. A metric stage of interior type before the descent, contracting toward a wall, does not supply the measured tilt through such a field; the time-reversed stage, expanding away from a wall, has no exit. Not covered: fields with dilaton or modulus couplings (including the hidden direction's Kaluza-Klein fields), the conversion to the curvature perturbation, momenta off the principal axes, and non-minimal couplings off the vacuum points.

## technical
The obstruction recorded for the primordial spectrum is horizon exit: after the descent no observed mode leaves the Hubble length, and the frozen phase has every observed mode inside its horizon. The series does have one geometry in which modes leave the Hubble length: the approach to a Kasner wall, the generic form of the field near a singularity, which the store studies at length for black-hole interiors. Near such a wall every scale factor is a power of proper time, and because the exponents always sum to one the volume grows exactly like proper time. That single fact makes the equation of a massless minimally coupled scalar along any principal axis Bessel's equation of order zero, whatever the exponents and whether there are hidden directions, within any one epoch of a BKL approach (each epoch again has exponents summing to one). Order zero means the exited spectrum goes as $k^{3}$ times a squared logarithm: the local index is between $2$ (modes still inside) and $3$ (modes well outside), above $2.57$ once a mode is a hundred times outside. That is blue, not the measured red tilt; it shares the leading power of a finite-range deposit, but the logarithm makes it log-correlated, not of finite range. So a contracting interior-type stage before the descent supplies exit but no tilt through such a scalar, and an expanding stage leaving a wall supplies neither. The closure is for minimally coupled spectator scalars: fields coupled to a dilaton or to the size of a hidden direction have a different pump and can be flat or red, and the curvature perturbation is not treated. Modes that exit in one epoch and cross later bounces outside the Hubble length are argued to keep the index.

## lay
In standard cosmology, the ripples in the early universe come from quantum fluctuations stretched beyond the horizon by a rapid early expansion. This framework has no such stage, and earlier results showed that nothing after the universe's origin stretches the observed ripples out. The framework does contain one kind of geometry that stretches fluctuations beyond the horizon: the violent, direction-dependent squeezing near a singularity, as inside a black hole. This result checks whether that could stand in for the missing stage, for the simplest kind of field, one that feels only the geometry. It cannot: whatever the details of the squeezing, the fluctuations such a field is left with are strongly tilted toward small scales, the opposite of the slight tilt toward large scales that is measured. Fields coupled to other quantities, such as the size of a hidden direction, are not covered.

## one-liner
On a Kasner approach ($\sum p_{j} = 1$, hidden directions and points inside the circle included), within one epoch, a massless minimally coupled scalar's mode along a principal axis obeys Bessel's equation of order $0$ in $s = k\tau^{1-p}/(1-p)$, so modes leave the Hubble length but the exited spectrum is $k^{3}$ times a squared logarithm, index in $[2, 3]$ and above $2.57$ once a hundred times outside: no red tilt; it has the same leading power $k^{3}$ as a finite-range deposit, enhanced by a squared logarithm, so it is not of finite range.
