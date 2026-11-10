---
id: synthesis.scalar-sector-at-the-isotropic-scalar-kasner-point-obeys-the-spectator-equation
kind: claim
version: 1
title: 'Scalar sector at the isotropic scalar Kasner point: the order-zero spectator equation'
status: proved
region: synthesis
subject: dark-energy
tags: [kasner, no-go, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-10-phase3
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase3
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall@2
  - synthesis.kasner-approach-gives-horizon-exit-and-index-three@4
  - synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_background_point
- kind: check
  ref: check.py::check_three_operators_force_lapse_and_shift
- kind: check
  ref: check.py::check_flat_gauge_solution_is_the_spectator_equation
- kind: check
  ref: check.py::check_order_zero_and_curvature_perturbation
- kind: check
  ref: check.py::check_clifford_frame_and_residue
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.kasner-approach-gives-horizon-exit-and-index-three
  - synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling
extraction:
  open_problem: op.descent-state-and-spectrum
  note: >-
    Closes, at the one isotropic point of the scalar Kasner disk, two items the stored Kasner results list as not
    covered: the scalar sector of the gravitational field's own perturbations (the diagonal modes, which couple to
    the scalar) and the conversion of a spectator's spectrum into the curvature perturbation. At that point no
    conversion is needed: the background scalar's own perturbation is the curvature perturbation up to the factor
    one third, and it obeys the stored spectator equation exactly, so the stored index (between 2 and 3) is the
    index of a gauge-invariant quantity and not a property of a spectator or of a choice of time slicing. It is a
    test of a stored negative result, and it leaves that result standing. Prior art, standard and not new: the
    gauge-invariant curvature variable and its pump field (Bardeen 1980; Mukhanov 1985; Sasaki 1986, cited from
    memory); on a power-law field with constant equation of state the pump field is proportional to the scale
    factor, so the curvature perturbation and a massless spectator share one equation, and the stiff case is the
    self-dual point of Wands' duality (the imported Fact synthesis.imported-wands-duality-of-perturbation-spectra,
    not used in the proof); the five-dimensional vacuum point (0, 0, 0, 1), which reduces to this point, is the
    compactified Milne field of Khoury, Ovrut, Seiberg, Steinhardt and Turok (2001) and of Tolley and Turok
    (2002, arXiv hep-th/0204091, read on the web: the reduced field has a massless scalar proportional to the
    logarithm of the time, and free fields cross with no particle production under their matching rule). What is
    added here is the exact linearised computation in the store's setting and the forced form of the lapse and
    shift. The intended base citation for the index table over all stored sources is the sibling result on the
    red-tilt criterion on power-law stages, filed in the same session and not cited here because it is not yet
    stored. Not covered: anisotropic points of the disk, where the scalar sector couples to the diagonal shear
    modes; the vacuum normalisation of the mode (the quadratic action of the curvature variable is textbook and
    is not rederived; the index does not depend on a momentum-independent normalisation); the tensor-to-scalar
    ratio, which with the textbook normalisations of the two quadratic actions is 16 times the slow-roll
    parameter 3, that is 48, a remark and not part of the statement.
---

## formal
Let the gravitational field on flat spacetime be the isotropic point of the scalar Kasner disk of Theorem \claimref{synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall}: $\hb^{-1}(e_{0}) = e_{0}$, $\hb^{-1}(e_{i}) = \tau^{1/3}e_{i}$, derived metric $d\tau^{2} - \tau^{2/3}\sum_{i}(dx^{i})^{2}$, with a massless scalar $\phi_{0} = q\log\tau$, $8\pi G q^{2} = \tfrac23$ (the common reduction of the five-dimensional vacuum points $(\tfrac12, \tfrac12, \tfrac12, -\tfrac12)$ and $(0, 0, 0, 1)$). Consider a first-order scalar perturbation of momentum $k \neq 0$ along $e_{1}$ in the gauge in which the spatial part of the derived metric is unperturbed:
\[
\hb^{-1}(e_{0}) = (1 + f\cos kx^{1})\,e_{0}, \qquad \hb^{-1}(e_{1}) = \tau^{1/3}e_{1} + b\,\sin kx^{1}\,e_{0}, \qquad \hb^{-1}(e_{2,3}) = \tau^{1/3}e_{2,3},
\]
\[
\phi = q\,(\log\tau + u\cos kx^{1}),
\]
with $f$, $b$, $u$ functions of $\tau$ (first-order derived metric: $2f\cos kx^{1}$ on $(0,0)$, $b\sin kx^{1}$ on $(0,1)$).
\begin{enumerate}
\item[(i)] \emph{(Lapse and shift are forced.)} The linearised Einstein-scalar equations (in the component reading of the derived metric, as in Theorem \claimref{synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling}(i)) hold if and only if
\[
f = u, \qquad b = \tau^{2/3}\,\dot u/k, \qquad \ddot u + \frac{\dot u}{\tau} + k^{2}\tau^{-2/3}u = 0 .
\]
The first is the time-space component, the second a transverse diagonal component, the third the time-time component; the remaining components are then satisfied identically.
\item[(ii)] \emph{(Order zero.)} The equation for $u$ is the mode equation of the massless minimally coupled spectator of Theorem \claimref{synthesis.kasner-approach-gives-horizon-exit-and-index-three}(i) at $p_{i} = \tfrac13$: Bessel's equation of order $0$ in $s = \tfrac32 k\tau^{2/3}$.
\item[(iii)] \emph{(The curvature perturbation.)} Write the first-order spatial derived metric of a general gauge as $-\tau^{2/3}(1 - 2\psi)\delta_{ij}$ plus second derivatives of a function, and $\delta\phi$ for the scalar's perturbation. The combination $\zeta = \psi + (H/\dot\phi_{0})\,\delta\phi$, $H = 1/(3\tau)$, is unchanged by a first-order change of time $\tau \mapsto \tau + \xi^{0}$ ($\psi \mapsto \psi + H\xi^{0}$, $\delta\phi \mapsto \delta\phi - \dot\phi_{0}\xi^{0}$) and by first-order spatial displacements. In the gauge above $\psi = 0$ and
\[
\zeta = \tfrac13\,u\cos kx^{1} = \tfrac13\,f\cos kx^{1},
\]
so the curvature perturbation is a constant multiple of the scalar's perturbation and of the lapse perturbation; its pump field satisfies $z^{2}/a^{2} = (\dot\phi_{0}/H)^{2} = 9q^{2}$, constant ($6$ in units $8\pi G = 1$), with $a = \tau^{1/3}$.
\item[(iv)] \emph{(Index.)} If the mode $u_{k}$ is in the adiabatic vacuum of Theorem \claimref{synthesis.kasner-approach-gives-horizon-exit-and-index-three}(iii) while inside, with a normalisation independent of $k$, then the spectrum of $\zeta$ is $\Delta^{2}_{\zeta}(k) \propto k^{3}\bigl(J_{0}(s)^{2} + Y_{0}(s)^{2}\bigr)$, with local index in $[2, 3]$ tending to $3$ outside: the same as the spectator's and as that of the cross modes of the gravitational field at this point.
\end{enumerate}
So at the isotropic scalar point the stored blue index is the index of the gauge-invariant curvature perturbation itself: it is not an artefact of reading a spectator or of the time slicing, no conversion step intervenes, and no number is free in it. Not covered: anisotropic points of the disk, and the normalisation of the vacuum mode beyond its independence of $k$.

## technical
The stored Kasner results give a blue spectrum, index between two and three, for a spectator scalar and for the gravitational field's cross modes, and list the scalar sector and the conversion to the curvature perturbation as not covered. At the isotropic point of the scalar Kasner disk the scalar sector can be solved exactly. In the gauge with unperturbed spatial metric the unknowns are the lapse perturbation, one shift component and the scalar's perturbation in units of its rate. The time-space equation forces the lapse perturbation to equal the scalar's; a transverse diagonal equation forces the shift to be the time derivative of the same function times $\tau^{2/3}/k$; the time-time equation is then exactly the stored spectator equation, friction $1/\tau$ and gradient term $k^{2}\tau^{-2/3}$, and the last equation follows. The reason the background drops out is that the combination $a^{3}\dot\phi_{0}^{2}/H$ is constant at this point, so the coupling of the scalar's perturbation to the metric perturbation adds no term. The gauge-invariant curvature perturbation is one third of the scalar's perturbation, and its pump field is a constant multiple of the scale factor. Given the stored adiabatic vacuum with a momentum-independent normalisation, the curvature perturbation therefore has the stored spectrum, $k^{3}$ times a squared logarithm outside, and under these hypotheses the index is that of a gauge-invariant quantity. The check computes the linearised Ricci tensor exactly with a formal engine, pins the three linear operators, and verifies the solution and three controls; the frame and the completed residue are checked in the Clifford algebra.

## lay
Earlier results in this collection showed that a passive test field riding on a universe collapsing toward a wall acquires ripples of the wrong colour: far stronger on small scales, where the sky shows ripples slightly stronger on large scales. A fair objection is that a test field is not the quantity the sky records, which is the ripple in the geometry itself, and that the answer might depend on how time is sliced. This result removes the objection in the one case the collection singles out, the collapse that is the same in all directions and is driven by a single field. There the field's own ripple is the geometric ripple, up to a factor of three, and it obeys exactly the equation of the test field. Assuming the same starting state as before, the wrong colour is therefore a property of the geometry's own ripple, with no adjustable number.

## one-liner
At the isotropic scalar Kasner point, in the gauge with unperturbed spatial metric, the field equations force $f = u$ and $b = \tau^{2/3}\dot u/k$ and reduce to $\ddot u + \dot u/\tau + k^{2}\tau^{-2/3}u = 0$, order zero, with $\zeta = u/3$; so, given the stored adiabatic vacuum, the gauge-invariant curvature perturbation has the stored blue index.
