---
id: synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling
kind: claim
version: 3
title: 'Kasner coupled modes reach the measured tilt only by a fitted coupling'
status: proved
region: synthesis
subject: dark-energy
tags: [kasner, no-go, confronted-with-data, needs-continuum]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - synthesis.kasner-approach-gives-horizon-exit-and-index-three@2
  - synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall@1
  - interior.kasner-form-interior@5
  - synthesis.bkl-bounce-invariant-holonomy-and-bound@2
  - synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands@1
  - synthesis.kasner-wall-matter-maxwell-bounces-stiff-moves-residue@2
  - synthesis.imported-einstein-cartan-matter-coupling@1
  - synthesis.imported-planck-2018-lcdm-parameters@3
  - synthesis.imported-bessel-reduction-and-small-argument-hankel-forms@1
  - synthesis.imported-kaluza-klein-ansatz@1
  - synthesis.imported-planck-2018-isocurvature-and-isotropy-bounds@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_points_and_reduction
- kind: check
  ref: check.py::check_offdiagonal_mode_equation
- kind: check
  ref: check.py::check_bessel_order
- kind: check
  ref: check.py::check_index_table
- kind: check
  ref: check.py::check_clifford_weights
- kind: check
  ref: check.py::check_isotropic_segment
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.kasner-approach-gives-horizon-exit-and-index-three
  - standard-model.dating-descent
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By Leon''s ruling R4 (scalar mode functions and Hankel Wronskians are written with the field theory''s unit, one reading with synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching and the other scalar-mode entities): the Hankel Wronskian W[H^(1), H^(2)](s) = -4 I_4/(pi s) are written with I_4 (proof), numbers read in span{1, I_4}, exact since that span is the complex numbers; no bare i remains, so the declaration is removed.'
  open_problem: op.descent-state-and-spectrum
  note: >-
    Closes the part the stored Kasner result left out for two families: the gravitational field's off-diagonal
    (cross) polarisation, which with one index along the five-dimensional towers' hidden direction is the
    Kaluza-Klein vector, and a curvature coupling xi R phi^2 at the points of the disk. Scalars weighted by a
    power of the hidden scale are treated in the result synthesis.kasner-hidden-scale-coupled-scalars-stay-blue (index at least 1 for the stored weights); the order
    formula here agrees with it and is not restated for them. The comparison list was fixed before any value was
    compared: the couplings the store fixes, at the points with equal observed exponents. The stiff segment
    between the two vacuum ends was added after a first comparison at the ends; along it the Kaluza-Klein
    vector's transverse potential has an index passing through the measured value near p = 0.456, but its field
    strength, which carries the energy spectrum, is blue there (index about 1.96) and on the whole segment, so
    the Kaluza-Klein vector reaches no observable red tilt; a vector sources an isotropic curvature perturbation
    only quadratically, and a local conversion does not lower a Gaussian field's index (synthesis.local-conversion-cannot-redden-a-gaussian-spectator). The one match left, a curvature coupling xi
    in [1.5225, 1.5481], is one free number fitted to one target, with its conversion not treated. Imported as
    Facts: the Kaluza-Klein ansatz (synthesis.imported-kaluza-klein-ansatz), the small-argument form of the
    Hankel functions (synthesis.imported-bessel-reduction-and-small-argument-hankel-forms) and the statistical
    isotropy of the measured spectrum (synthesis.imported-planck-2018-isocurvature-and-isotropy-bounds). Cited
    from memory, a flagged citation (no five-dimensional stiff source is adopted): the five-dimensional
    analogue of the stiff-matter wall. Transport-absent: standard mode analysis; the reading of the off-diagonal order as
    a difference of residue weights in Cl(1,4) is transport-convenient. The series' dating takes pre-descent
    physics as pre-metric, so a metric Kasner stage before the descent remains a closed alternative, not a
    reversal.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2: the Kaluza-Klein ansatz, the small-argument Hankel forms and the statistical isotropy of the record, cited from memory in version 1, now cite the imported Facts (uses edges added, claimrefs in the proof); the Planck parameters pin moved to version 2 (baryon and dark matter densities added there, not used here); the five-dimensional stiff wall stays a flagged citation. No clause changed.'
---

## formal
Let a gravitational field on flat spacetime have, near a wall at $T = 0$, the synchronous diagonal derived metric $dT^{2} - \sum_{a}T^{2P_{a}}(dx^{a})^{2}$ over the three observed directions and any hidden ones, with $\sum_{a}P_{a} = 1$: the vacuum points ($\sum_{a}P_{a}^{2} = 1$; in four dimensions the BKL circle $p(u)$ of Theorem \claimref{synthesis.bkl-bounce-invariant-holonomy-and-bound}, the Schwarzschild interior of Lemma \claimref{interior.kasner-form-interior} among them; in five dimensions the sphere $K_{5}$, the fifth direction being the hidden direction of Proposition \claimref{synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands}, scale $b = T^{P_{h}}$), and the points with $\sum_{a}P_{a}^{2} < 1$ that a massless scalar or stiff matter reaches (Theorems \claimref{synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall} and \claimref{synthesis.kasner-wall-matter-maxwell-bounces-stiff-moves-residue} in four dimensions; in five dimensions their analogue, stiff matter giving $\sum P = 1$, $\sum P^{2} < 1$, which no stored field supplies), with rate $c^{2} = 1 - \sum_{a}P_{a}^{2}$. Take comoving momentum $k$ along a principal axis $j$ with $P_{j} < 1$, $s = kT^{1 - P_{j}}/(1 - P_{j})$.
\begin{enumerate}
\item[(i)] \emph{(Off-diagonal modes.)} For $h_{ab} = T^{2P_{b}}A(T)\cos(kx^{j})$, $a, b, j$ distinct, the linearised field equation (in the component reading of the derived metric) is the single equation $\ddot A + (1 + 2P_{b} - 2P_{a})\dot A/T + k^{2}T^{-2P_{j}}A = 0$, every other first-order component vanishing, at vacuum and at scalar or stiff points alike. With $a, b$ observed this is the cross polarisation of a gravitational wave; with $b$ the hidden direction, $A$ is the Kaluza-Klein vector's component $a$.
\item[(ii)] \emph{(Order.)} A mode obeying $\ddot\chi + (1 + w)\dot\chi/T + (k^{2}T^{-2P_{j}} - \xi c^{2}T^{-2})\chi = 0$ ($\xi$ normalised so that $\tfrac16$ is the conformal coupling) is $s^{-w/(2(1 - P_{j}))}$ times a Bessel function of order
\[
\nu_{j} = \frac{\sqrt{w^{2} + 4\xi c^{2}}}{2(1 - P_{j})} .
\]
The off-diagonal mode has $w = 2(P_{b} - P_{a})$, so $\nu = |P_{a} - P_{b}|/(1 - P_{j})$. At the isotropic disk point $(\tfrac13, \tfrac13, \tfrac13)$, $c^{2} = \tfrac23$, a curvature-coupled scalar has $\nu^{2} = \tfrac32\xi$, and $\xi = \tfrac16$ gives the conformal $\nu = \tfrac12$.
\item[(iii)] \emph{(Index.)} For a mode in its adiabatic vacuum before exit, $|\chi_{k}|^{2} = \tfrac{\pi}{4(1 - P_{j})}T^{-w}|H^{(1)}_{\nu}(s)|^{2}$, so the exited spectrum has $n - 1 = 3 - 2\nu$ for $\nu > 0$ (the stored logarithm for $\nu = 0$). This is the index of $A$ itself: for the cross modes the strain, the usual tensor spectrum; for the Kaluza-Klein vector the transverse potential, invariant under its gauge transformations at linear order since a gauge parameter's gradient has no component transverse to $k$. For a vector the physical field is the field strength: its magnetic part $\partial_{j}A_{a}$ has index $5 - 2\nu$, two more, and the vector's energy spectrum carries that index.
\item[(iv)] \emph{(Anisotropic points.)} For $\nu \ne 0$ the order depends on the axis through $P_{j}$ and, for the off-diagonal modes, through the pair $(a, b)$. On the BKL circle the cross modes have orders $|1 - u|/(1 + u)$, $(2 + u)/u$, $1 + 2u$ ($u \ge 1$) on the three axes: the index along the axis of largest exponent is $1 - 4u \le -3$, red, and the three indices spread by more than $4u \ge 4$.
\item[(v)] \emph{(Equal observed exponents.)} A statistically isotropic spectrum needs equal indices along the observed axes. The points $(p, p, p, 1 - 3p)$ with $\sum P^{2} \le 1$ form the segment $0 \le p \le \tfrac12$, with vacuum ends $(0, 0, 0, 1)$ and $(\tfrac12, \tfrac12, \tfrac12, -\tfrac12)$ (both reducing to $(\tfrac13, \tfrac13, \tfrac13)$, $c^{2} = \tfrac23$, in four dimensions). Along it: the cross modes of observed pairs have $\nu = 0$; the Kaluza-Klein vector has $\nu = |1 - 4p|/(1 - p) \in [0, 2]$, so its transverse potential has index $(5 - 11p)/(1 - p)$ for $p \ge \tfrac14$, running from $3$ at $p = \tfrac14$ to $-1$ at $p = \tfrac12$, while its field strength has index $5 - 2\nu \in [1, 5]$, blue at every point of the segment. Only the vacuum ends are reached by the store's own fields; the interior points need five-dimensional stiff matter.
\item[(vi)] \emph{(Confrontation.)} Against $n_{s} - 1 = -0.0351 \pm 0.0042$ (Fact \claimref{synthesis.imported-planck-2018-lcdm-parameters}), within three standard deviations: no coupling the store fixes (cross modes, a conformal or minimally coupled scalar, the minimal coupling being that of Fact \claimref{synthesis.imported-einstein-cartan-matter-coupling}, the Kaluza-Klein vector at either vacuum end, index $1$ or $-1$, the latter more than $229$ standard deviations off) at a point the store singles out. The Kaluza-Klein vector's transverse potential passes through the window for $p \in (0.4556, 0.4570)$, but its field strength there has index between $1.95$ and $1.98$: a property of the potential, not a route to the measured tilt. A curvature-coupled scalar at the isotropic point meets the window only for $\xi \in [1.5225, 1.5481]$ ($n - 1 = 3 - \sqrt{6\xi}$; $\xi = \tfrac32$ gives exact scale invariance): one free number fitted to one target, which nothing in the store fixes, with its conversion into the curvature perturbation not treated.
\end{enumerate}
So the gravitational field's own off-diagonal modes and curvature-coupled scalars can exit a Kasner approach with a red spectrum, but only with indices that differ between axes by at least $4$; with equal observed exponents the Kaluza-Klein vector's field strength is blue, and only a chosen curvature coupling matches the measured tilt. Not covered: the conversion into the curvature perturbation (a vector sources no isotropic curvature perturbation at linear order without a background value of its own, which would break isotropy), momenta off the principal axes, the diagonal (plus) polarisations, which couple to the scalar sector, and the persistence of an index across BKL bounces. In $\Cl(1,4)$ the unit-boost residue $B_{5} = \sum_{a}P_{a}e_{0}e_{a}$ has $\tfrac12(e_{a}B_{5} - B_{5}e_{a}) = P_{a}e_{0}$, so the numerator $|P_{a} - P_{b}|$ in (i) is the difference of the residue weights of $e_{a}$ and $e_{b}$.

## technical
The stored result on Kasner approaches closed one candidate source of the primordial spectrum, a massless minimally coupled spectator scalar, and left out fields coupled to the geometry beyond the volume element. This result treats the gravitational field's own off-diagonal modes and the curvature coupling with one formula. Any such mode obeys a Bessel-type equation whose friction term carries an extra power of time, and whose order is that power, combined with any curvature coupling, divided by twice one minus the exponent of the momentum's axis. For the gravitational field's own off-diagonal modes the extra power is twice the difference of the two exponents, computed exactly from the linearised field equations; with one index along the hidden direction this mode is the Kaluza-Klein vector. Nonzero orders give spectra $k^{3 - 2\nu}$, and some are red; but the order depends on the axis, so red spectra at generic points differ from axis to axis by at least four in the index, against a statistically isotropic record. Equal observed exponents leave a segment between two vacuum points, filled by stiff matter. There the gravitational wave modes keep the stored index. The Kaluza-Klein vector's transverse potential has an index running from $3$ to $-1$, passing the measured value near $p = 0.456$, but its field strength, the physical field and the carrier of its energy spectrum, has index at least $1$ everywhere on the segment, so the vector supplies no observable red tilt. A curvature-coupled scalar matches the measured tilt only for a coupling near $1.53$, which nothing fixes. The comparison list was fixed before values were compared, except the stiff segment, whose interior points need five-dimensional stiff matter that no stored field supplies. The conversion of these spectra into the curvature perturbation is not treated.

## lay
In standard cosmology the slight tilt of the early universe's ripples, a little more power on large scales, comes from a stage of rapid expansion. This framework has no such stage, but near a singularity, where space is squeezed differently along different directions, fluctuations are stretched beyond the horizon. An earlier result showed that the simplest fields come out with the wrong tilt there. This result looks at fields that feel the geometry more strongly: ripples of gravity itself, a field that comes from a hidden extra direction, and fields coupled to curvature. Ripples of gravity can come out tilted the right way only along some directions, whereas the observed ripples look the same in every direction; ripples of gravity itself and the field from a hidden direction come out tilted the wrong way in every direction-independent case; a field coupled to curvature can match the measured tilt only if its coupling is set to just the right value, which nothing in the framework does.

## one-liner
On a Kasner approach ($\sum P = 1$) the gravitational field's off-diagonal modes obey Bessel's equation of order $|P_{a} - P_{b}|/(1 - P_{j})$ and a curvature-coupled scalar order $\sqrt{\xi}|c|/(1 - P_{j})$, so red strain spectra exit, but with indices spreading by at least $4$ between axes on the vacuum circle; with equal observed exponents the Kaluza-Klein vector's transverse potential has index $(5 - 11p)/(1 - p)$ in $[-1, 3]$ (gauge-invariant at linear order) but its field strength has index $5 - 2\nu \in [1, 5]$, blue, and a curvature-coupled scalar matches the measured tilt only for $\xi \in [1.5225, 1.5481]$, a coupling fitted to it that nothing in the series fixes.
