---
id: synthesis.norm-released-locally-on-isotropic-fields-tracks-dust-and-never-accelerates
kind: claim
version: 1
title: 'The norm released locally on isotropic fields tracks dust and never accelerates'
status: proved
region: synthesis
subject: dark-energy
tags: [cosmological-constant, frozen-point, curvature-and-field-equations, no-go]
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
  - dark-energy.imported-macdowell-mansouri-theorem-stelle-west@4
  - dark-energy.frozen-point-makes-stelle-west-vector@7
  - synthesis.promoted-norm-weyl-clock-flat-weight@7
  - synthesis.stelle-west-norm-is-no-local-output@2
  - synthesis.promoted-norm-one-global-pair@5
  - dark-energy.imported-henneaux-teitelboim-promotion@6
  - dark-energy.vacuum-region-registration-condition@8
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_field_strength_torsion_and_einstein_map_of_the_isotropic_field
- kind: check
  ref: check.py::check_frozen_point_density_on_the_isotropic_field_is_the_reduced_lagrangian
- kind: check
  ref: check.py::check_euler_lagrange_expressions_of_the_reduced_lagrangian
- kind: check
  ref: check.py::check_elimination_gives_the_stored_clock_density
- kind: check
  ref: check.py::check_dust_solution_tracks_the_density_and_decelerates
- kind: check
  ref: check.py::check_radiation_has_no_solution_and_barotropic_value
- kind: check
  ref: check.py::check_vacuum_leaves_the_norm_a_free_function
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.stelle-west-norm-is-no-local-output
  - synthesis.promoted-norm-weyl-clock-flat-weight
  - pred.dark-energy-w-minus-one
extraction:
  note: >-
    Exposure of the w = -1 prediction: does any stored structure let the dark-energy density evolve? The promoted
    norm does not (stored: its multiplier is constant by its own equation). The one stored variant in which the
    norm is a field without its three-form is the local release, which the stored result shows excludes the
    Schwarzschild-de Sitter field in vacuum, on torsion-free fields of constant norm. What is new here: the
    released norm on homogeneous isotropic fields with matter, with the norm time dependent and the torsion solved
    rather than set to zero. The three algebraic equations do not see the derivative of the norm, which enters
    only the connection equation as a source of torsion; so the stored clock density, computed there on solutions
    of constant norm, is exactly the released norm's equation. Dust forces the cosmological term to equal the
    matter density at all times, with matter-like deceleration at half the Friedmann rate squared; radiation
    admits no solution; vacuum leaves the norm a free function. Kill condition written before computing: an
    accelerating solution, or an equation of state of the cosmological term near -1; neither occurs. Scope:
    flat slices, reflection-invariant fields (no axial torsion), one barotropic fluid for the solutions, the bare
    functional (the stored coefficients c_3 = c_5 = 0), matter under the stored hypothesis (Mat). Not treated:
    the polynomial family with derivative terms of the Stelle-West vector, for which the literature reports
    rolling quintessence (H. F. Westman and T. G. Zlosnik, Exploring Cartan gravity with dynamical symmetry
    breaking, Class. Quantum Grav. 31 (2014) 095004, arXiv:1302.1103; abstract checked on the web, the body from
    memory); the store evaluates that family only on torsion-free fields of constant norm. No open-problem entry
    exists for the dark-energy exposure; the settled entry on the gravitational action is the nearest. The
    reduction to the isotropic family is by covariance of the Euler-Lagrange expressions under rotations and one
    reflection, proved in the proof text; the connection equation was also verified in form language by hand.
    Transport-absent: nothing here uses the transport structure; the frozen point enters only as the norm.
---

## formal
\emph{Setting.} Take the frozen-point MacDowell-Mansouri functional of Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west} and Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector} for a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with the norm $u = -Q(V) = 3/\Lambda > 0$ of the Stelle-West vector: density $k\,u\,\epsilon(F, F)$, $k$ a nonzero constant, where $F(b \wedge c) = R(b \wedge c) + u^{-1}\,\hb^{-1}(b) \wedge \hb^{-1}(c)$ is the Lorentz block on background bivectors (on physical bivectors $-(\mathcal{R}(B) - u^{-1}B)$ in the store's sign) and $\epsilon(F, F)$ is the sum over the $24$ orderings of the background frame, with the sign of the ordering, of the coefficient of $e_{0}e_{1}e_{2}e_{3}$ in $F(e_{\mu} \wedge e_{\nu})\,F(e_{\rho} \wedge e_{\sigma})$. \emph{Releasing the norm locally} means: $u$ is a positive field on spacetime, varied at fixed $(\hb, \Omega)$, with no three-form and no constraint. Matter obeys hypothesis (Mat) of Theorem \claimref{synthesis.promoted-norm-weyl-clock-flat-weight}(v): its action depends on the frame only through the derived metric and not on $u$ or on $\Omega$; so the frame equation is $\mathcal{G}(b) + 3u^{-1}\,b = -8\pi G\,T(b)$ with $u$ the local value, and the equations of $u$ and of $\Omega$ have no matter term. Write $\tilde\rho = 8\pi G\rho$, $\tilde p = 8\pi G p$ for a perfect fluid at rest in the frame below, $T(e_{0}) = \rho\,e_{0}$, $T(e_{i}) = -p\,e_{i}$.

\emph{The isotropic family.} With $t = e_{0} \cdot x$ and functions $n, s > 0$, $y$ and $u > 0$ of $t$ alone,
\[
\hb^{-1}(e_{0}) = n\,e_{0},\qquad \hb^{-1}(e_{i}) = s\,e_{i},\qquad \Omega(e_{0}) = 0,\qquad \Omega(e_{i}) = y\,e_{i}e_{0}\quad(i = 1, 2, 3),
\]
the homogeneous, isotropic, reflection-invariant gravitational fields with flat slices, torsion allowed ($n$ the lapse, $s$ the scale factor; the derived metric is $n^{2}dt^{2} - s^{2}dx^{2}$). A dot is $d/dt$, and $H = \dot s/(n s)$ is the expansion rate.
\begin{enumerate}
\item[(i)] \emph{(Kinematics; proved.)} The torsion is $D_{e_{0}}\hb^{-1}(e_{i}) - D_{e_{i}}\hb^{-1}(e_{0}) = (\dot s - n y)\,e_{i}$ and vanishes on spatial pairs, so the field is torsion-free exactly when $y = \dot s/n$. The curvature operator is diagonal, $\mathcal{R}(e_{0}e_{i}) = \alpha\,e_{0}e_{i}$ and $\mathcal{R}(e_{i}e_{j}) = \beta\,e_{i}e_{j}$ with
\[
\alpha = \frac{\dot y}{n s},\qquad \beta = \frac{y^{2}}{s^{2}},
\]
and $\mathcal{G}(e_{0}) = -3\beta\,e_{0}$, $\mathcal{G}(e_{i}) = -(2\alpha + \beta)\,e_{i}$.
\item[(ii)] \emph{(The four equations; proved.)} On the family, $u\,\epsilon(F, F) = 24\,L$ with
\[
L = n s^{3} u\,(\alpha - u^{-1})(\beta - u^{-1}) = u\,\dot y\,y^{2} - s^{2}\dot y - n s\,y^{2} + n s^{3}u^{-1},
\]
and the stationary points of the released functional with matter under (Mat) within the family are the solutions of
\[
3\beta = 3u^{-1} + \tilde\rho,\qquad 2\alpha + \beta = 3u^{-1} - \tilde p,\qquad \alpha\beta = u^{-2},\qquad 2s(\dot s - n y) = \dot u\,y^{2},
\]
the two frame equations, the equation of the norm, and the equation of $\Omega$. They are the full field equations on the family: every other component vanishes there by rotation and reflection covariance. The derivative $\dot u$ enters only the last: a varying norm is a source of torsion, and the three other equations are algebraic in $u$.
\item[(iii)] \emph{(Elimination; proved.)} The two frame equations give $\alpha\beta - u^{-2} = \tfrac{1}{18}\bigl[3u^{-1}(\tilde\rho - 3\tilde p) - \tilde\rho(\tilde\rho + 3\tilde p)\bigr]$, which is $\tfrac{1}{24}$ of the density $E - \tfrac83\Lambda^{2} = \tfrac43[\Lambda(\tilde\rho - 3\tilde p) - \tilde\rho(\tilde\rho + 3\tilde p)]$ of Theorem \claimref{synthesis.promoted-norm-weyl-clock-flat-weight}(v) at $\Lambda = 3u^{-1}$. So the equation of the released norm is
\[
\Lambda\,(\tilde\rho - 3\tilde p) = \tilde\rho\,(\tilde\rho + 3\tilde p),\qquad \Lambda = 3u^{-1},
\]
pointwise in time: the density that advances the promoted norm's clock, computed there on torsion-free solutions of constant norm, is set to zero here with the norm varying and the torsion solved.
\item[(iv)] \emph{(Dust; proved.)} For $\tilde p = 0$ and $\tilde\rho = m s^{-3}$ with $m > 0$ constant, the solutions are exactly: $\Lambda = 3u^{-1} = \tilde\rho$ at every time; $\beta = \tfrac23\tilde\rho$, $\alpha = \tfrac16\tilde\rho$; $y = -2\dot s/n$ (so the torsion is $3\dot s\,e_{i}$, nonzero); and
\[
H^{2} = \tfrac16\tilde\rho = \tfrac{4\pi G}{3}\rho ,
\]
half the Friedmann value, with either sign of $H$. In proper time $s$ is proportional to the power $\tfrac23$ of the time from the singular point, the deceleration parameter is $\tfrac12$ at every time, and the cosmological term $\Lambda/8\pi G = \rho$ scales as $s^{-3}$: as a fluid it has equation of state $w = 0$, not $-1$. No solution with dust accelerates, and none has constant norm.
\item[(v)] \emph{(Other fluids; proved.)} For $\tilde p = w_{m}\tilde\rho$ with $\tilde\rho > 0$ the equation of (iii) gives $\Lambda = \tilde\rho\,(1 + 3w_{m})/(1 - 3w_{m})$ for $w_{m} \neq \tfrac13$, positive only for $-\tfrac13 < w_{m} < \tfrac13$, and has no solution for radiation, $w_{m} = \tfrac13$, where it reads $-2\tilde\rho^{2} = 0$. For a mixture the same equation with the total density and pressure is necessary.
\item[(vi)] \emph{(Vacuum; proved.)} For $\tilde\rho = \tilde p = 0$ the equations give $\alpha = \beta = u^{-1}$, so $F = 0$, the equation of the norm holds identically, and for every positive function $u(t)$ the field with $y = \pm s\,u^{-1/2}$ and
\[
H = \pm u^{-1/2} + \frac{\dot u}{2 n u}
\]
is a solution. The norm is a free function and the expansion history is not determined; for constant $u$ this is the de Sitter field with every norm of Theorem \claimref{synthesis.stelle-west-norm-is-no-local-output}(iv)(a).
\item[(vii)] \emph{(The promoted norm, for comparison; recalled with one step added.)} Under the promotion of Fact \claimref{dark-energy.imported-henneaux-teitelboim-promotion}, the three-form's equation is $d\lambda = 0$ (Theorem \claimref{synthesis.promoted-norm-one-global-pair}(ii)); under (Mat) the three-form term contains neither the frame nor matter, so the frame equation is that of the Setting with $3u^{-1}$ a constant $\Lambda$, whose term is the stress-energy $(\Lambda/8\pi G)\,b$ of Proposition \claimref{dark-energy.vacuum-region-registration-condition}(i) with $p = -\rho$: $w = -1$ on every solution, the value of $\Lambda$ differing between solutions and not within one. The same holds if a function $g(\lambda)$ with $g' \neq 0$ is promoted, the equation being $g'(\lambda)\,d\lambda = 0$.
\end{enumerate}
\emph{Reading (argued).} Of the two stored ways of making the norm a variable, the promotion keeps $w = -1$ exactly by (vii), and the local release, the one in which the dark-energy density can change in time, gives under (Mat) and on the isotropic family no evolution of the kind the surveys test: with dust the cosmological term follows the matter density and the expansion never accelerates, with radiation there is no solution, and in vacuum nothing is predicted. Together with the exclusion of the Schwarzschild-de Sitter field (Theorem \claimref{synthesis.stelle-west-norm-is-no-local-output}(iv)), the local release is not a fallback for the prediction $w = -1$. This is a statement about the bare functional: actions with derivative terms of the Stelle-West vector are not treated here. Transport-absent.

## technical
The prediction $w = -1$ would be refuted by a confirmed evolution of the dark-energy density, so it matters whether any stored structure allows one. The promoted norm does not: its multiplier is constant by its own equation, and under hypothesis (Mat) the frame equation is Einstein's with that constant. The other stored variant releases the norm $u = 3/\Lambda$ as a local field with no three-form. On homogeneous, isotropic, reflection-invariant gravitational fields with flat slices, $\hb^{-1}(e_{0}) = n e_{0}$, $\hb^{-1}(e_{i}) = s e_{i}$, $\Omega(e_{i}) = y\,e_{i}e_{0}$, the functional reduces to $24k\,n s^{3}u(\alpha - 1/u)(\beta - 1/u)$ with $\alpha = \dot y/(ns)$ and $\beta = y^{2}/s^{2}$ the two curvature eigenvalues, and under (Mat) the field equations are $3\beta = 3/u + \tilde\rho$, $2\alpha + \beta = 3/u - \tilde p$, $\alpha\beta = 1/u^{2}$ and $2s(\dot s - ny) = \dot u\,y^{2}$. The rate of change of the norm enters only the last, where it sources torsion. Eliminating gives $\Lambda(\tilde\rho - 3\tilde p) = \tilde\rho(\tilde\rho + 3\tilde p)$, the stored clock density of the promoted norm set to zero. Under (Mat), dust forces $\Lambda = 8\pi G\rho$ at all times with $H^{2} = \tfrac{4\pi G}{3}\rho$ and deceleration parameter $\tfrac12$; radiation has no solution; in vacuum $u(t)$ is free and $H = \pm u^{-1/2} + \dot u/(2nu)$. So under (Mat), on this family, the release gives no accelerating solution with matter and no prediction without it.

## lay
The framework predicts that dark energy never changes. If measurements showed it changing, could the framework bend? Its equations contain one quantity, a fixed length, that sets the strength of dark energy. In one stored variant that length becomes a quantity the equations hold constant, and dark energy still never changes. In the other variant the length is allowed to vary freely from place to place and moment to moment. This result works out what that second variant does to a smooth, uniform universe, assuming matter responds to gravity in the ordinary way. With ordinary matter present, the dark energy is forced to equal the density of matter at every moment, so the expansion always slows down and never speeds up, contrary to what is observed. With only radiation present, the equations have no solution. With nothing present, the equations allow any expansion history at all, so they predict nothing. Under that assumption about matter, and for uniform universes of this kind, freeing the length does not give the framework a way to accommodate changing dark energy.

## one-liner
Under hypothesis (Mat), on homogeneous isotropic reflection-invariant fields with flat slices, the frozen-point functional with its norm $u = 3/\Lambda$ released locally has equations $3\beta = 3/u + \tilde\rho$, $2\alpha + \beta = 3/u - \tilde p$, $\alpha\beta = u^{-2}$, $2s(\dot s - ny) = \dot u\,y^{2}$: dust forces $\Lambda = 8\pi G\rho$ with $H^{2} = \tfrac{4\pi G}{3}\rho$ and deceleration $\tfrac12$, radiation has no solution, vacuum leaves $u(t)$ free, and the promoted norm keeps $w = -1$.
