---
id: synthesis.norm-released-locally-on-isotropic-fields-tracks-dust-and-never-accelerates
kind: claim
version: 1
title: 'Under (Mat), bare functional, isotropic flat slices: the released norm tracks dust'
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
  - synthesis.frozen-phase-spectrum-not-red@4
  - synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands@1
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
  - synthesis.red-tilt-criterion-on-power-law-stages-and-the-index-ledger-of-the-stored-sources
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version kept at 1 (accepted in this pass): the note names, for comparison, the index ledger of the stored mode equations, whose de Sitter and dust rows take the constant fixed (lineage only); it also records that the w = -1 prediction (version 5), the field-space premise and Premise (N) now cite this result for the statement that the series has no fallback, which is labelled argued there.'
  note: >-
    Exposure of the w = -1 prediction: does any stored structure let the dark-energy density evolve? The promoted
    norm does not (stored: its multiplier is constant by its own equation). The one stored variant in which the
    norm is a field without its three-form is the local release, which the stored result shows excludes the
    Schwarzschild-de Sitter field in vacuum, on torsion-free fields of constant norm. What is added here: the
    computation in the store's Gauge Theory Gravity setting and its identification with the stored clock density;
    the result itself is known for the minimal varying-Lambda theory (prior art below). That the released norm's
    equation is the stored clock density set to zero is definitional: the stored theorem defines that density as
    the derivative of the Lagrangian in the norm at fixed frame and connection, and the release sets the same
    derivative to zero; clauses (iii) and the value of Lambda in (v) are corollaries of the stored display. What
    is beyond the store, and what the check tests where it can fail: the frame and norm equations keep their
    algebraic form with torsion solved and the norm varying (the rate of the norm enters only the connection
    equation), the connection equation itself, and the solved dynamics (expansion rate, torsion, deceleration).
    Dust forces the cosmological term to equal the matter density at all times, with H^2 half the Friedmann value
    for the matter density alone (a quarter of the value for matter plus the tracked term); one barotropic fluid
    with -1/3 < w < 1/3 decelerates with parameter (1 + 3w)/2; radiation admits no solution; vacuum leaves the norm
    a free function. Mixtures are not treated beyond a necessary condition. Kill condition written before
    computing: an accelerating solution, or an equation of state of the cosmological term near -1; neither occurs
    for one fluid. Scope:
    flat slices, reflection-invariant fields (no axial torsion), one barotropic fluid for the solutions, the bare
    functional (the stored coefficients c_3 = c_5 = 0), matter under the stored hypothesis (Mat), which here means
    matter on the derived metric of the frame with the norm varied at fixed frame and connection; with matter on
    the rescaled frame of the stored release the clauses on matter are not derived. Prior art (abstracts checked
    on the web, bodies not read): S. Alexander, M. Cortes, A. R. Liddle, J. Magueijo, R. Sims and L. Smolin, A
    zero-parameter extension of general relativity with varying cosmological constant, Phys. Rev. D 100 (2019)
    083506, arXiv:1905.10380, and The cosmology of minimal varying Lambda theories, Phys. Rev. D 100 (2019)
    083507, arXiv:1905.10382: Lambda made a field by a quasi-topological term added to the Einstein action, its
    variation carried by torsion; under homogeneity and isotropy Lambda proportional to the matter density with a
    constant depending on the equation of state; the constant infinite for pure radiation. That their term is
    the Euler term with coefficient proportional to 1/Lambda, which would make their action this functional with
    a varying norm, is from memory and not verified. Statements about what the store holds (two ways of making
    the norm a variable; no other stored structure with evolving dark energy) are argued from a text search, not
    audited over a cone; the search found one stored structure with a late-time equation of state different from
    -1, the unadopted branch of the unit-ball result with a static hidden direction (a dark-matter component with
    effective w = -1/4, no pressure derived), which is named in the Reading. The exact w = -1 no-go for the
    promoted norm as a source is held by the stored frozen-phase theorem, cited and not restated. Not treated:
    the polynomial family with derivative terms of the Stelle-West vector, for which the literature reports
    rolling quintessence (H. F. Westman and T. G. Zlosnik, Exploring Cartan gravity with dynamical symmetry
    breaking, Class. Quantum Grav. 31 (2014) 095004, arXiv:1302.1103; abstract checked on the web, the body from
    memory); the store evaluates that family only on torsion-free fields of constant norm. The spectrum side of the same exposure, whether a stage with a slowly varying constant
    could tilt the spectrum, is in the index ledger
    synthesis.red-tilt-criterion-on-power-law-stages-and-the-index-ledger-of-the-stored-sources
    (clauses (v), (vi); comparison only). No open-problem entry
    exists for the dark-energy exposure; the settled entry on the gravitational action is the nearest. The
    reduction to the isotropic family is by covariance of the Euler-Lagrange expressions under rotations and one
    reflection, proved in the proof text; the connection equation was also verified in form language by hand.
    Transport-absent: nothing here uses the transport structure; the frozen point enters only as the norm.
---

## formal
\emph{Setting.} Take the frozen-point MacDowell-Mansouri functional of Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west} and Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector} for a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with the norm $u = -Q(V) = 3/\Lambda > 0$ of the Stelle-West vector: density $k\,u\,\epsilon(F, F)$, $k$ a nonzero constant, where $F(b \wedge c) = R(b \wedge c) + u^{-1}\,\hb^{-1}(b) \wedge \hb^{-1}(c)$ is the Lorentz block on background bivectors (on physical bivectors $-(\mathcal{R}(B) - u^{-1}B)$ in the store's sign) and $\epsilon(F, F)$ is the sum over the $24$ orderings of the background frame, with the sign of the ordering, of the coefficient of $e_{0}e_{1}e_{2}e_{3}$ in $F(e_{\mu} \wedge e_{\nu})\,F(e_{\rho} \wedge e_{\sigma})$. \emph{Releasing the norm locally} means: $u$ is a positive field on spacetime, varied at fixed $(\hb, \Omega)$, with no three-form and no constraint. Matter obeys hypothesis (Mat) of Theorem \claimref{synthesis.promoted-norm-weyl-clock-flat-weight}(v): its action depends on the frame only through the derived metric and not on $u$ or on $\Omega$; so the frame equation is $\mathcal{G}(b) + 3u^{-1}\,b = -8\pi G\,T(b)$ with $u$ the local value, and the equations of $u$ and of $\Omega$ have no matter term. This fixes which frame matter sees as the norm varies: the derived metric of $\hb^{-1}$, with $u$ varied at fixed $(\hb, \Omega)$; every clause on matter below is for this choice. The functional is the bare one, the stored coefficients $c_{3} = c_{5} = 0$ of Theorem \claimref{synthesis.stelle-west-norm-is-no-local-output}. Write $\tilde\rho = 8\pi G\rho$, $\tilde p = 8\pi G p$ for a perfect fluid at rest in the frame below, $T(e_{0}) = \rho\,e_{0}$, $T(e_{i}) = -p\,e_{i}$.

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
the two frame equations, the equation of the norm, and the equation of $\Omega$. They are the full field equations on the family: every other component vanishes there by rotation and reflection covariance. The derivative $\dot u$ enters only the last: a varying norm is a source of torsion, and the three other equations are algebraic in $u$ and hold in the same form with torsion present. This, the connection equation and the solved dynamics of (iv) and (v) are what the clause adds to the stored results.
\item[(iii)] \emph{(Elimination; proved, a corollary of the stored display.)} The two frame equations give $\alpha\beta - u^{-2} = \tfrac{1}{18}\bigl[3u^{-1}(\tilde\rho - 3\tilde p) - \tilde\rho(\tilde\rho + 3\tilde p)\bigr]$, which is $\tfrac{1}{24}$ of the density $E - \tfrac83\Lambda^{2} = \tfrac43[\Lambda(\tilde\rho - 3\tilde p) - \tilde\rho(\tilde\rho + 3\tilde p)]$ of Theorem \claimref{synthesis.promoted-norm-weyl-clock-flat-weight}(v) at $\Lambda = 3u^{-1}$. So the equation of the released norm is
\[
\Lambda\,(\tilde\rho - 3\tilde p) = \tilde\rho\,(\tilde\rho + 3\tilde p),\qquad \Lambda = 3u^{-1},
\]
pointwise in time. The identification is definitional: the stored theorem's clause (iii) defines the clock density as the derivative of the Lagrangian in $u$ at fixed frame and connection, and the release sets that derivative to zero. The stored display was computed on torsion-free solutions of constant norm; by (ii) it holds unchanged with the norm varying and the torsion solved.
\item[(iv)] \emph{(Dust; proved.)} For $\tilde p = 0$ and $\tilde\rho = m s^{-3}$ with $m > 0$ constant, the solutions are exactly: $\Lambda = 3u^{-1} = \tilde\rho$ at every time; $\beta = \tfrac23\tilde\rho$, $\alpha = \tfrac16\tilde\rho$; $y = -2\dot s/n$ (so the torsion is $3\dot s\,e_{i}$, nonzero); and
\[
H^{2} = \tfrac16\tilde\rho = \tfrac{4\pi G}{3}\rho ,
\]
half the Friedmann value for the matter density alone (a quarter of the value $\tfrac13(\tilde\rho + \Lambda)$ for matter with the tracked term), with either sign of $H$. In proper time $s$ is proportional to the power $\tfrac23$ of the time from the singular point, the deceleration parameter is $\tfrac12$ at every time, and the cosmological term $\Lambda/8\pi G = \rho$ scales as $s^{-3}$: as a fluid it has equation of state $w = 0$, not $-1$. No solution with dust alone accelerates, and none has constant norm.
\item[(v)] \emph{(One barotropic fluid; proved; the value of $\Lambda$ a corollary of the stored display.)} For $\tilde p = w_{m}\tilde\rho$ with $\tilde\rho > 0$ the equation of (iii) gives $\Lambda = \tilde\rho\,(1 + 3w_{m})/(1 - 3w_{m})$ for $w_{m} \neq \tfrac13$, positive only for $-\tfrac13 < w_{m} < \tfrac13$, and has no solution for radiation, $w_{m} = \tfrac13$, where it reads $-2\tilde\rho^{2} = 0$. For $-\tfrac13 < w_{m} < \tfrac13$ and $\tilde\rho = m\,s^{-3(1 + w_{m})}$ the solutions are exactly $y = -2\dot s/\bigl(n(1 + 3w_{m})\bigr)$ with
\[
H^{2} = \frac{(1 + 3w_{m})^{2}}{6\,(1 - 3w_{m})}\,\tilde\rho ,
\]
and the deceleration parameter is $\tfrac12(1 + 3w_{m}) > 0$ at every time: no solution with one such fluid and $u > 0$ accelerates. Mixtures are not treated: the equation of (iii) with the total density and pressure is necessary, and no statement on their acceleration is made.
\item[(vi)] \emph{(Vacuum; proved.)} For $\tilde\rho = \tilde p = 0$ the equations give $\alpha = \beta = u^{-1}$, so $F = 0$, the equation of the norm holds identically, and for every positive function $u(t)$ the field with $y = \pm s\,u^{-1/2}$ and
\[
H = \pm u^{-1/2} + \frac{\dot u}{2 n u}
\]
is a solution. The norm is a free function and the expansion history is not determined; for constant $u$ this is the de Sitter field with every norm of Theorem \claimref{synthesis.stelle-west-norm-is-no-local-output}(iv)(a).
\item[(vii)] \emph{(The promoted norm, for comparison; recalled with one step added.)} Under the promotion of Fact \claimref{dark-energy.imported-henneaux-teitelboim-promotion}, the three-form's equation is $d\lambda = 0$ (Theorem \claimref{synthesis.promoted-norm-one-global-pair}(ii)); under (Mat) the three-form term contains neither the frame nor matter, so the frame equation is that of the Setting with $3u^{-1}$ a constant $\Lambda$, whose term is the stress-energy $(\Lambda/8\pi G)\,b$ of Proposition \claimref{dark-energy.vacuum-region-registration-condition}(i) with $p = -\rho$: $w = -1$ on every solution, the value of $\Lambda$ differing between solutions and not within one. The same holds if a function $g(\lambda)$ with $g' \neq 0$ is promoted, the equation being $g'(\lambda)\,d\lambda = 0$.
\end{enumerate}
\emph{Reading (argued).} A text search of the store, not an audit of a cone, finds two ways of making the norm a variable. The promotion keeps $w = -1$ exactly by (vii); that the promoted norm supplies no scale-dependent source is Theorem \claimref{synthesis.frozen-phase-spectrum-not-red}(iv), cited and not restated. The local release, the one in which the cosmological term can change in time, gives under (Mat), for the bare functional and on the isotropic family, no evolution of the kind the surveys test: with dust, or one barotropic fluid with $-\tfrac13 < w_{m} < \tfrac13$, the cosmological term is a fixed multiple of the matter density and the expansion decelerates; with radiation there is no solution; in vacuum nothing is predicted. Together with the exclusion of the Schwarzschild-de Sitter field (Theorem \claimref{synthesis.stelle-west-norm-is-no-local-output}(iv)), the local release is not a fallback for the prediction $w = -1$. The conclusions for matter hold for matter on the derived metric of $\hb^{-1}$ with $u$ varied at fixed $(\hb, \Omega)$; with matter on the frame $u^{-1/2}\hb^{-1}$ of the stored release the equation of the norm is the vanishing of the density $\epsilon(F, F)$ itself and the clauses on matter are not derived. The same search finds one stored structure with a late-time equation of state different from $-1$: the unadopted branch of Theorem \claimref{synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands}(ii) with a static hidden direction, a dark-matter component with effective $w = -\tfrac14$ read from a dilution exponent (no pressure derived there); it is not a variable norm and is not treated here. Actions with derivative terms of the Stelle-West vector are not treated. The result is known for the minimal varying-$\Lambda$ theory in the literature named in the extraction note; what is added is its form in the store's setting and its identification with the stored clock density. Transport-absent.

## technical
The prediction $w = -1$ would be refuted by a confirmed evolution of the dark-energy density, so it matters whether any stored structure allows one. Of the two ways the store holds of making the norm a variable (a search of the store, not a proof that there are no others), the promoted norm does not: its multiplier is constant by its own equation, and under hypothesis (Mat) the frame equation is Einstein's with that constant. The other releases the norm $u = 3/\Lambda$ of the bare functional as a local field with no three-form, a construction known in the literature as the minimal varying-$\Lambda$ theory. On homogeneous, isotropic, reflection-invariant gravitational fields with flat slices, $\hb^{-1}(e_{0}) = n e_{0}$, $\hb^{-1}(e_{i}) = s e_{i}$, $\Omega(e_{i}) = y\,e_{i}e_{0}$, the functional reduces to $24k\,n s^{3}u(\alpha - 1/u)(\beta - 1/u)$ with $\alpha = \dot y/(ns)$ and $\beta = y^{2}/s^{2}$ the two curvature eigenvalues, and under (Mat) the field equations are $3\beta = 3/u + \tilde\rho$, $2\alpha + \beta = 3/u - \tilde p$, $\alpha\beta = 1/u^{2}$ and $2s(\dot s - ny) = \dot u\,y^{2}$. The rate of change of the norm enters only the last, where it sources torsion. Eliminating gives $\Lambda(\tilde\rho - 3\tilde p) = \tilde\rho(\tilde\rho + 3\tilde p)$, the stored clock density of the promoted norm set to zero. Under (Mat), with matter on the derived metric of $\hb^{-1}$, dust forces $\Lambda = 8\pi G\rho$ at all times with $H^{2} = \tfrac{4\pi G}{3}\rho$ and deceleration parameter $\tfrac12$; one barotropic fluid with $-\tfrac13 < w_{m} < \tfrac13$ has deceleration parameter $\tfrac12(1 + 3w_{m}) > 0$; radiation has no solution; in vacuum $u(t)$ is free and $H = \pm u^{-1/2} + \dot u/(2nu)$. So under (Mat), on this family and for one such fluid, the release gives no accelerating solution, and no prediction without matter; mixtures are not treated.

## lay
The framework predicts that dark energy never changes. If measurements showed it changing, could the framework bend? Its equations contain one quantity, a fixed length, that sets the strength of dark energy. The collection holds two ways of letting that length vary (found by a search of the collection, not a proof that there are no others). In one, the length becomes a quantity the equations hold constant, and dark energy still never changes. In the other, the length is allowed to vary freely from place to place and moment to moment. This result works out what that second way does, for the simplest form of the action, to a smooth, uniform, spatially flat universe, assuming matter responds to gravity in the ordinary way. The outcome was already known in the research literature for an equivalent theory; here it is derived in the framework's own language. With ordinary matter alone present, the dark energy is forced to equal the density of matter at every moment, so the expansion always slows down and never speeds up, contrary to what is observed; the same slowing holds for any single simple fluid the equations admit, and mixtures of several kinds of matter were not worked out. With only radiation present, the equations have no solution. With nothing present, the equations allow any expansion history at all, so they predict nothing. Under that assumption about matter, and for flat uniform universes of this kind filled with one kind of matter, freeing the length in the simplest form of the action does not give the framework a way to accommodate changing dark energy.

## one-liner
Under hypothesis (Mat) with matter on the derived metric of $\hb^{-1}$, on homogeneous isotropic reflection-invariant fields with flat slices, the bare frozen-point functional ($c_{3} = c_{5} = 0$) with its norm $u = 3/\Lambda$ released locally has equations $3\beta = 3/u + \tilde\rho$, $2\alpha + \beta = 3/u - \tilde p$, $\alpha\beta = u^{-2}$, $2s(\dot s - ny) = \dot u\,y^{2}$: for one fluid, dust forces $\Lambda = 8\pi G\rho$ with $H^{2} = \tfrac{4\pi G}{3}\rho$ and deceleration $\tfrac12$ (one barotropic fluid: $\tfrac12(1 + 3w_{m}) > 0$), radiation has no solution, vacuum leaves $u(t)$ free, and the promoted norm keeps $w = -1$; the result is known in the literature for the minimal varying-$\Lambda$ theory.
