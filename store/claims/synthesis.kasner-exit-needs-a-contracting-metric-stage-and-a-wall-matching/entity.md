---
id: synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching
kind: claim
version: 4
title: 'Kasner exit needs a contracting stage and a wall matching'
status: proved
region: synthesis
subject: dark-energy
tags: [kasner, no-go, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-01-xi-ledger
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
- name: Claude Opus 5.5
  role: GA rewrite (wall curvature as the store-sign curvature operator)
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - synthesis.kasner-approach-gives-horizon-exit-and-index-three@4
  - synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling@3
  - synthesis.imported-bessel-reduction-and-small-argument-hankel-forms@2
  - dark-energy.frozen-point-datum-kasner-wall@8
  - synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_exit_direction
- kind: check
  ref: check.py::check_liouville_and_adiabaticity
- kind: check
  ref: check.py::check_wall_curvature
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.dating-descent
  - dark-energy.gravity-pre-metric-forces-degenerate-exactly
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Forms to GA in (iii), formal and proof: the curvature at the wall is the store-sign curvature operator on the physical frame planes, calR(e_0 ^ e_i) = p_i(p_i - 1) tau^-2 e_0 ^ e_i and calR(e_i ^ e_j) = p_i p_j tau^-2 e_i ^ e_j, computed in the proof from Omega(hb(e_i)) = -(p_i/tau) B_i through the field strength, and the Kretschmann scalar is 2 <calR(a ^ b) calR(d_b ^ d_a)>, four times the sum of the squared eigenvalues; the Cartan forms and curvature two-forms stay as a labelled component reading. The same eigenvalues were checked exactly with lib/GA.py for dark-energy.frozen-point-datum-kasner-wall (in any number of directions the computation is the same plane by plane); the Kretschmann formula and its values are unchanged.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The positive-frequency mode u = e^{-is}/sqrt 2 in the proof of (ii) is written e^{-I_4 s}/sqrt 2, with the field theory''s unit I_4 and numbers read in span{1, I_4}; no bare i remains.'
  open_problem: op.descent-state-and-spectrum
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2: a marked note at the end of the formal level cites the two premises registered by Leon''s decision of 2026-11-01, synthesis.pre-descent-contracting-kasner-stage-premise (P1) and synthesis.pre-descent-state-carried-into-descended-phase-premise (P2), by claimref only; by the same decision this result has no uses or assumes edge to them, and (i)-(iii) and the reading are unchanged.'
  note: >-
    Addresses the part of the problem that asks whether a Kasner stage exists before the descent. The stored Kasner
    results compute spectra within an epoch of an approach to a wall; this result fixes the direction of time those
    spectra need for every Bessel order (curvature-coupled and hidden-scale-coupled modes included), shows that the
    expanding branch fixes no state at its wall, and computes where the stored Kasner data are curvature singularities.
    Clause (i) extends to every Bessel order the closing remark of
    synthesis.kasner-approach-gives-horizon-exit-and-index-three, that the expanding stage has no exit. The conclusion
    about existence is a reading, labelled argued, under the hypothesis that the descended phase expands monotonically
    from the descent: the stage is excluded only under the dating's reading of pre-descent physics as pre-metric, a
    conjecture, and admitted with two hypotheses, (P1) and (P2), stated in the reading. The dating, the finite-range
    deposit result and the pre-metric result are cited in the reading as context, not as premises of (i)-(iii).
    Filed alongside: the result on the series' curvature couplings at the isotropic Kasner point
    (synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point), which carries the coupling
    inventory. Cited from memory, flagged: the compactified Milne geometry of the ekpyrotic and cyclic models and the
    open status of its matching (Khoury, Ovrut, Steinhardt and Turok 2001; Tolley, Turok and Steinhardt 2004).
    Transport-absent: standard mode analysis and curvature invariants.
---

## formal
Let a gravitational field on flat spacetime have, near a wall at $\tau = 0$, the synchronous diagonal derived metric $d\tau^{2} - \sum_{j}\tau^{2p_{j}}(dx^{j})^{2}$ over the three observed directions and any hidden ones, with $\sum_{j}p_{j} = 1$ (the setting of Theorem \claimref{synthesis.kasner-approach-gives-horizon-exit-and-index-three}). Take a comoving momentum $k$ along a principal axis $i$ with $p_{i} < 1$, $q = 1 - p_{i}$, $s = k\tau^{q}/q$, and a mode whose equation reduces, as in Theorem \claimref{synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling}(ii), to $s^{-w/(2q)}Z(s)$ with $Z'' + Z'/s + (1 - \nu^{2}/s^{2})Z = 0$, for any order $\nu \ge 0$ (the minimally coupled scalar, $\nu = 0$; curvature-coupled scalars; the gravitational field's off-diagonal modes; scalars weighted by the hidden scale).
\begin{enumerate}
\item[(i)] \emph{(Exit only toward the wall.)} The expansion rate is $(\sum_{j}p_{j})/\tau = 1/\tau$ and the ratio of the mode's wavelength along the axis to the Hubble length is $1/(qs) = 1/(k\tau^{q})$, strictly decreasing in $\tau$. So a mode leaves the Hubble length only on the branch on which $\tau$ decreases toward the wall, and on the branch expanding away from a wall every mode starts outside and enters; this holds for every order $\nu$, since the order does not enter. This extends to every order the closing remark of Theorem \claimref{synthesis.kasner-approach-gives-horizon-exit-and-index-three}, made there for order $0$.
\item[(ii)] \emph{(No adiabatic state at the wall on the expanding branch.)} In the Liouville form in $s$: with $Z = s^{-1/2}u$ the equation is $u'' + \omega^{2}u = 0$, $\omega^{2} = 1 + a/s^{2}$, $a = \tfrac14 - \nu^{2}$. For $0 \le \nu < \tfrac12$ the adiabatic parameter obeys $(\omega'/\omega^{2})^{2} = a^{2}/(s^{2} + a)^{3}$, equal to $1/a \ge 4$ at the wall and decreasing in $s$, at least $1$ for $s^{2} \le a^{2/3} - a$; for $\nu > \tfrac12$, $\omega^{2} < 0$ for $s^{2} < \nu^{2} - \tfrac14$, so the mode does not oscillate there; only $\nu = \tfrac12$ gives $\omega^{2} = 1$ exactly. So on an expanding branch the state of every mode with $\nu \ne \tfrac12$ is not fixed by an adiabatic condition in $s$ at the wall: it is initial data there (in $\ln s$ the frequency squared is $s^{2} - \nu^{2}$, with the same conclusion). Modes with $\nu = \tfrac12$ have the exact positive-frequency solution, index $2$.
\item[(iii)] \emph{(The walls.)} The field strength is diagonal on the physical frame planes, $\mathcal{R}(e_{0}\wedge e_{i}) = p_{i}(p_{i} - 1)\tau^{-2}\,e_{0}\wedge e_{i}$ and $\mathcal{R}(e_{i}\wedge e_{j}) = p_{i}p_{j}\tau^{-2}\,e_{i}\wedge e_{j}$ in the store's sign (as in Theorem \claimref{dark-energy.frozen-point-datum-kasner-wall}(i), whose computation uses no field equation; in components, the curvature two-forms $p_{i}(p_{i} - 1)/\tau^{2}$ on $e^{0}\wedge e^{i}$ and $-p_{i}p_{j}/\tau^{2}$ on $e^{i}\wedge e^{j}$), so the Kretschmann scalar $K = 2\langle\mathcal{R}(a\wedge b)\,\mathcal{R}(\partial_{b}\wedge\partial_{a})\rangle$ is
\[
K\tau^{4} = 4\sum_{i}p_{i}^{2}(p_{i} - 1)^{2} + 4\sum_{i<j}p_{i}^{2}p_{j}^{2},
\]
which equals $-16p_{1}p_{2}p_{3}$ on the four-dimensional vacuum circle. With $\sum_{j}p_{j} = 1$ it vanishes exactly at the flat Milne points, one exponent $1$ and the others $0$. Every other Kasner wall is a curvature singularity: the Schwarzschild interior, every BKL epoch, the isotropic disk point $(\tfrac13, \tfrac13, \tfrac13)$ and the five-dimensional vacuum end $(\tfrac12, \tfrac12, \tfrac12, -\tfrac12)$. At the other five-dimensional vacuum end $(0, 0, 0, 1)$ the five-dimensional metric is flat and the hidden scale $b = \tau$ collapses at the wall, while its Einstein-frame reduction is the isotropic disk point (Theorem \claimref{synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall}), a curvature singularity in four dimensions.
\end{enumerate}
\emph{Reading (argued).} Assume the dating's placement of the descent at the origin and the hypothesis that the descended phase expands monotonically from the descent (no recollapse and bounce after it; the record supports expansion back to nucleosynthesis). Then the descended phase can contain a Kasner stage only on an expanding branch, where by (i) no mode exits and by (ii) the state at the wall is the descent's deposited state, the open datum of Theorem \claimref{synthesis.finite-range-descent-deposit-cannot-seed-cmb}: such a stage supplies no spectrum of its own. A Kasner source of the measured spectrum therefore needs two hypotheses the store does not hold: (P1) a metric stage before the descent, contracting toward a wall; (P2) a rule carrying the exited state from that contracting stage into the descended phase, across the wall if the approach reaches it, or across whatever ends the approach before it. By (iii) the wall is a curvature singularity at every stored Kasner point except the five-dimensional Milne end, and there, by the argument of Theorem \claimref{dark-energy.frozen-point-datum-kasner-wall}(i) (a diverging curvature scalar), the frozen-point datum extends regularly in no chart; if the descent ends the approach at finite $\tau$, after the modes have left, the rule is a matching across the descent itself; either way a turn from contraction to expansion under Einstein's equations needs a singularity or a violation of the null energy condition, so (P2) is needed in every case. The dating reads pre-descent physics as pre-metric (\claimref{standard-model.dating-descent}, reading (iii), a conjecture), which denies (P1); no proved result denies it, since gravity's polynomial action is defined across the singular locus (\claimref{dark-energy.gravity-pre-metric-forces-degenerate-exactly}(2)). So a pre-descent Kasner stage is excluded by the dating's reading and admitted only with (P1) and (P2) as hypotheses, whose tension with that reading is not resolved here. Granting (P1) and (P2) does not supply the tilt: at tree level every curvature coupling the series fixes leaves the exited spectrum blue at the Kasner points the store fixes (\claimref{synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point}), so the tilt-matching coupling stays a free parameter. At the five-dimensional Milne end the wall is the collapse of the hidden circle in flat five-dimensional spacetime, the compactified Milne geometry of the ekpyrotic and cyclic models, whose matching is not settled there either (cited from memory).

\emph{Note (premises, 2026-11-01).} The two hypotheses of the reading are now registered as premises of the series: (P1) as Premise \claimref{synthesis.pre-descent-contracting-kasner-stage-premise} and (P2), in the general form stated above, as Premise \claimref{synthesis.pre-descent-state-carried-into-descended-phase-premise}, each with its tension with the dating's pre-metric reading recorded and not resolved. This result states them as hypotheses of its argued reading and does not rest on them: (i)-(iii) hold without them, and the sentence above that the store does not hold them describes the store before their registration.

## technical
The stored Kasner results compute the spectrum of fields leaving the Hubble length as a wall is approached. Leaving needs the approach, as the stored result remarked for the simplest field, and the same holds for every field: the wavelength along an axis shrinks more slowly than the Hubble length only while the volume contracts toward the wall, for every field whose mode equation reduces to Bessel's, whatever its order. Run the other way, away from a wall, every mode starts outside and comes in. In the Liouville form in $s$ the mode is an oscillator of frequency squared $1 + (\tfrac14 - \nu^{2})/s^{2}$; at the wall the adiabatic parameter is at least $2$ for orders below $\tfrac12$, the mode does not oscillate for orders above it, and only the order $\tfrac12$ is exactly adiabatic. So an expanding stage fixes no state at its wall: the state there is initial data, which for the descended phase is the descent's deposit. The curvature at a Kasner wall is computed from the exponents alone; with exponents summing to one the Kretschmann scalar vanishes only at the flat Milne points, so every other wall the store holds, the isotropic point and one of the two five-dimensional ends included, is a curvature singularity. Read with the descent at the origin and the descended phase expanding from it (argued), a Kasner source of the spectrum therefore needs a metric contracting stage before the descent, which the dating's reading denies, and a rule carrying its state into the descended phase, across a singular wall if the approach reaches it, which no stored result supplies. Even with both granted, the curvature couplings the series fixes leave the spectrum blue at tree level.

## lay
In this framework the universe begins with an event called the descent, and the earliest ripples must be explained without a stage of rapid expansion. Earlier results looked at a squeezing stage near a singularity, where ripples are stretched beyond the horizon. This result shows that the stretching only happens while space is collapsing toward the singularity, never while it expands away from it. Since the framework places the descent at the beginning, such a collapsing stage would have to come before the descent, which the framework's account of the descent treats as a stage without any geometry. Even if such a stage existed, the ripples would have to be carried into the expanding universe, through a true singularity or through whatever ends the collapse, and nothing in the framework says how; and even then the fields the framework fixes would give the wrong tilt.

## one-liner
For every Bessel order the wavelength-to-Hubble ratio along an axis of a Kasner approach is $1/(k\tau^{1-p})$, so modes exit only toward the wall; on the expanding branch the squared adiabatic parameter in the Liouville form in $s$ at the wall is $1/(\tfrac14 - \nu^{2}) \ge 4$ for $\nu < \tfrac12$ and modes with $\nu > \tfrac12$ do not oscillate there, so the state at the wall is initial data; $K\tau^{4} = 4\sum p_{i}^{2}(p_{i} - 1)^{2} + 4\sum_{i<j}p_{i}^{2}p_{j}^{2}$ vanishes only at the flat Milne points; so, by an argued reading (the descent at the origin, the descended phase expanding from it), a Kasner source needs a metric contracting stage before the descent and a matching into the descended phase (across a singular wall if the approach reaches it), neither of which the store holds.
