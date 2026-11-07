---
id: synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale
kind: claim
version: 3
title: 'Positive structure and natural actions leave the almost-Einstein scale free'
status: proved
region: synthesis
subject: einstein
tags: [tractors, curvature-and-field-equations, no-go, conformal-model]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle (U1 to U6)
  version: 2
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG proof of (ii) (dilation field, torsion-solved Omega, Kulkarni-Nomizu field strength, store-sign scalar) and of (iii) (tractor derivative in Cl(2,4)); decision A3 applied (store-sign scalar and Euler-Lagrange equation in (ii))'
  version: 3
  source: maintainer pass 2026-11-07 (GTG proofs)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.infinity-vacuum-incidence-is-a-property-of-the-scale@3
  - correspondence.imported-vacuum-equations-scale-tractor@6
  - synthesis.positive-conformal-energy-gives-positive-null-translations@7
  - synthesis.positive-structure-is-twistor-form-at-imaginary-time@4
  - synthesis.imported-gtg-dictionary@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_positive_structure_symmetry_fixes_no_scale
- kind: check
  ref: check.py::check_yamabe_stationary_scale_is_not_almost_einstein
- kind: check
  ref: check.py::check_tractor_dirichlet_stationary_points_are_not_parallel
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_gtg_dilation_field_scalar_and_tractor_dirichlet
lineage:
  motivated_by:
  - synthesis.einstein-condition-is-infinity-vacuum-incidence
  - synthesis.vacuum-field-stress-tensor-is-einstein-tensor-or-trace
  - mass.imported-frozen-point-tractor-connection
  - synthesis.rung-unit-second-free-number
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Decision A3 (Leon, 7 November 2026, DECISIONS.md category A; items-for-gtg.md): formal (ii) and proof (ii) restated in the store sign, sqrt|g| calR = 6 phi box phi, restricted action int(-6 eta(d phi, d phi) - 2 Lambda phi^4), Euler-Lagrange equation box phi = (2/3) Lambda phi^3 (the trace calR = 4 Lambda), and the index convention''s scalar named as -calR; the old text had -6 phi box phi and -(2/3) Lambda phi^3, contradicting synthesis.twistor-flat-fields-give-nordstrom-not-einstein (i). Evidence: the GTG scalar 6 box phi/phi^3 of the dilation field and box phi = (2/3) Lambda phi^3 for the de Sitter scale phi = 1/(1 - Lambda Q/12), both computed exactly in check_gtg_dilation_field_scalar_and_tractor_dirichlet (and in the reconciler''s and R03''s scripts). Kind: restatement; the Lambda = 0 counter-models and every conclusion are unaffected.'
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'GTG proof made the main proof for (ii) and (iii): the scale phi^2 eta is the derived metric of the dilation field hb^{-1}(a) = phi a; Omega(a) = a ^ grad ln phi solves the torsion equation; the field strength is the Kulkarni-Nomizu form R(a ^ b) = -(a ^ K(b) + K(a) ^ b), K(a) = a . grad w - (w . a) w + Q(w) a/2, w = grad ln phi; Ricci map (2K(b) + tr K b)/phi^2 and store-sign scalar 6 box phi/phi^3; (iii) computes D_a D sigma = H0(a) - (1/4)(a . grad box sigma) n0 with Omega_T(a) = -ninf ^ a and contracts it with the Cl(2,4) product; the Christoffel computation is kept as a labelled reading (index-convention scalar -calR). New check check_gtg_dilation_field_scalar_and_tractor_dirichlet (exact jets: three scales at two points, the de Sitter scale at Lambda = 3, three tractor scales); the Christoffel check now asserts the store-sign identity sqrt|g| calR = 6 phi box phi; runcheck 4/4, check4 clean on a proposals copy. outside_ga removed: no stand-in remains (tractor slots are coordinates of a Cl(2,4) vector). Status, links unchanged.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: The proof computes the Ricci tensor and the tractor slots of conformally rescaled metrics from Christoffel symbols in components; the GTG statement is in the formal level and the component computation is the evidence.'
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By the unit principle (U3) the complex unit of Cl(2,4)_C, of its module and of the tube points is the central pseudoscalar I_7 = I_6 e of Cl(3,4) (std-algebra.complexification-is-the-odd-extension), as in the cited Theorem synthesis.positive-structure-is-twistor-form-at-imaginary-time: J = I_7 e_1 e_+ in that theorem''s labels, the tube point I_7 rho e_0 and X(m) = n_0 + rho^2/2 n_inf + I_7 rho e_0 in the formal level and the proof; the outside_ga declaration is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: J = i e_1 e_+ is the involution of the module of the complexified Cl(2,4), and the tube point m = i rho e_0 with X(m) = n_0 + (rho^2/2) n_inf + i rho e_0 is a point of complexified spacetime; both i stand next to vectors, which no pseudoscalar commutes with, so i stays and is declared (version and levels unchanged).'
  open_problem: op.scale-selection-principle
  note: >-
    Tests both lines of attack of the open problem and finds each blocked, with exact counter-models. (a) The
    sesquilinear structure: its symmetry inside Spin(2,4) is the centraliser of the bivector of its positive
    plane, u(1) + so(4), which fixes no nonzero vector of R^{2,4}; its orbits on scale tractors are products of a
    circle and a 3-sphere, so an invariant principle can fix at most the two norms Q_+ and Q_- of a tractor's
    projections (hence Lambda, proportional to Q = Q_+ + Q_-), never the tractor; the u(1) of the conformal energy
    fixes exactly the Lambda < 0 tractors, and no null tractor (Lambda = 0) lies in either fixed space. (b) A
    variational principle in the scale at fixed conformal class: the Einstein-Hilbert action restricted to the
    class gives one Euler-Lagrange equation, the trace R = 4 Lambda (the Yamabe equation), and phi = 1 + x1 x2
    is a stationary non-almost-Einstein scale; the tractor Dirichlet functional gives box^2 sigma = 0, with
    1 + x1 x2 stationary and (t + x1)^2 of zero action density, both non-parallel. Cross-subject inputs: the
    Yamabe problem (the conformal factor carries only the trace of the field equations) and the Cauchy-Kovalevskaya
    count (one scalar equation against nine trace-free conditions), cited from memory. Consequence (argued beyond the two functionals): a
    principle that selects the scale must constrain the trace-free part, which no local functional of the scale at fixed
    class with a somewhere noncharacteristic Euler-Lagrange equation supplies; it has to be a dynamical principle for the whole gauge field hb (on the series' route, the
    Clausius relation with (C_loc)), or a Lagrange-multiplier rewording of the parallel-tractor condition, which
    the open problem excludes. Transport-absent.
---

## formal
Work in $\Cl(2,4)$ with the generators of Proposition \claimref{synthesis.positive-conformal-energy-gives-positive-null-translations}: $e_{0}$, $\nu$ (square $+1$), $e_{1}, e_{2}, e_{3}$, $e_{-}$ (square $-1$), $\nInf = \nu + e_{-}$, $\nO = \tfrac12(\nu - e_{-})$, $X(x) = \nO + x - \tfrac12 Q(x)\nInf$, $Z = e_{0}\nu$. A constant vector $I$ is a parallel tractor of the flat class, with scale $\sigma = \ip{X(x)}{I}$ and derived metric $\sigma^{-2}\eta$ of the pure dilation field $\hb = \sigma$; in the normalisation of the stored de Sitter tractor $\nInf + \tfrac{\Lambda}{6}\nO$, $Q(I) = \Lambda/3$. The almost-Einstein scales of the flat class are those whose scale tractor is parallel (Theorem \claimref{synthesis.infinity-vacuum-incidence-is-a-property-of-the-scale}(3), Fact \claimref{correspondence.imported-vacuum-equations-scale-tractor}); in the flat splitting this is the vanishing of the trace-free Hessian $H^{\circ}$ of $\sigma$, $H(a) = a\cdot\nabla\,\nabla\sigma$, $H^{\circ}(a) = H(a) - \tfrac14(\partial_{b}\cdot H(b))\,a$, whose solutions are $\sigma = c + b\cdot x - \tfrac{k}{2}Q(x)$.
\begin{enumerate}
\item[(i)] \emph{(The positive structure fixes no scale tractor.)} The symmetry of the positive Hermitian structure inside $\mathrm{Spin}(2,4)$ is the centraliser of the bivector of its positive plane: for the stored structure (Theorem \claimref{synthesis.positive-structure-is-twistor-form-at-imaginary-time}, $J = I_{7}e_{1}e_{+}$ in its labels, $I_7$ the central pseudoscalar of $\Cl(2,4)_{\C} = \Cl(3,4)$, the complex unit of the module and of complexified points, \claimref{std-algebra.complexification-is-the-odd-extension}) this is the centraliser of $Z$, with Lie algebra $\mathfrak{u}(1)\oplus\so(4)$ spanned by $Z$ and the six bivectors of $\mathrm{span}(e_{1}, e_{2}, e_{3}, e_{-})$; for any other positive structure it is a conjugate. The vectors commuting with $Z$ are exactly $\mathrm{span}(e_{1}, e_{2}, e_{3}, e_{-})$, negative definite, so the conformal energy's $\mathfrak{u}(1)$ fixes exactly the tractors with $\Lambda < 0$; the vectors fixed by $\so(4)$ are exactly $\mathrm{span}(e_{0}, \nu)$, positive definite (de Sitter tractors, $\Lambda > 0$), on which $1 + tZ$ acts by the Cayley rotation; the whole centraliser fixes no nonzero vector. A null tractor ($\Lambda = 0$, for example $\nInf$, the Minkowski scale) lies in neither space. Every orbit of the centraliser on nonzero tractors is a product of a circle and a $3$-sphere, one factor possibly a point, with invariants $Q_{+}(I) \ge 0$ and $Q_{-}(I) \le 0$, the norms of the projections, $Q(I) = Q_{+} + Q_{-}$. So a principle invariant under the positive structure can fix at most $(Q_{+}, Q_{-})$, hence $\Lambda$, and never a scale tractor. A boost is a datum outside the structure: for the boost of the plane $(e_{0}, e_{1})$ the vectors fixed by it and by the $\so(4)$ are exactly the ray of $\nu$, and for the tube point $I_{7}\rho e_{0}$ (foot at the origin), whose positive plane is $\mathrm{span}(\mathrm{Re}\,X, \mathrm{Im}\,X) = \mathrm{span}(\nO + \tfrac{\rho^{2}}{2}\nInf, e_{0})$, the boost-fixed vector of that plane is $\tfrac{\rho^{2}}{2}$ times the de Sitter tractor at $\Lambda = 12/\rho^{2}$: structure and boost together select a de Sitter scale with $\Lambda$ fixed by the tube unit, never a $\Lambda \le 0$ one. This is the converse direction of synthesis.wick-rotated-boost-selects-observer-tube-point (filed alongside), where the boost and an observer select the tube point. The two agree that the frozen point $I_{\Lambda}$ commutes with the boost; here its tube point at the origin has $\rho^{2} = 12/\Lambda$, that is $\rho = 2\ell$ in the de Sitter normalisation $\sigma = 1 - \Lambda Q/12$ with $\ell = (3/\Lambda)^{1/2}$, while the argued normalisation $\rho = 1/\kappa = \ell$ of the result filed alongside differs by a factor $2$; both statements treat only tube points with foot $x_{\perp} = 0$; tabulated: $I = \nu$ gives $\sigma = \tfrac12(1 - Q(x))$ (de Sitter, $\Lambda = 12$ in this normalisation up to the factor $\tfrac12$), $I = e_{0}$ gives $\sigma = t$, $I = e_{-}$ gives $\sigma = \tfrac12(1 + Q(x))$ (anti de Sitter).
\item[(ii)] \emph{(The Einstein-Hilbert action restricted to the class.)} For the scale $g = \varphi^{2}\eta$ ($\varphi = 1/\sigma$), the store-sign scalar curvature gives $\sqrt{|g|}\,\mathcal{R} = 6\varphi\,\Box\varphi$, so $\int\sqrt{|g|}(\mathcal{R} - 2\Lambda)$ restricted to the class is $\int(-6\,\eta(\partial\varphi, \partial\varphi) - 2\Lambda\varphi^{4})$ up to boundary terms, with the single Euler-Lagrange equation $\Box\varphi = \tfrac23\Lambda\varphi^{3}$, the trace $\mathcal{R} = 4\Lambda$ of the field equations (the Yamabe equation). It has stationary scales that are not almost-Einstein: $\varphi = 1 + x_{1}x_{2}$ and $\varphi = 1 + \tfrac{t}{3} + x_{1}^{2}x_{3} - x_{2}^{2}x_{3}$ at $\Lambda = 0$ have $\Box\varphi = 0$, hence $\mathcal{R} = 0$ everywhere, and a nonzero trace-free Ricci tensor at every sample point.
\item[(iii)] \emph{(The tractor Dirichlet functional.)} In the flat splitting the derivative of the tractor $D\sigma = (\sigma, \nabla\sigma, -\tfrac14\Box\sigma)$ has middle slot $H^{\circ}$ and vanishing top slot, so its tractor Dirichlet density is $H^{\circ}\!:\!H^{\circ} = \partial_{a}\cdot\partial_{b}\,(H^{\circ}(a)\cdot H^{\circ}(b))$. The functional $\int H^{\circ}\!:\!H^{\circ}$ has the single Euler-Lagrange equation $\tfrac32\Box^{2}\sigma = 0$. It is stationary at $\sigma = 1 + x_{1}x_{2}$, with $H^{\circ} \ne 0$ everywhere; and $\sigma = (t + x_{1})^{2}$ has $H^{\circ}(a) = 2(a\cdot l)\,l$, $l = e_{0} + e_{1}$ null, so $H^{\circ} \ne 0$ while $H^{\circ}\!:\!H^{\circ} = 0$: in Lorentzian signature even a vanishing action does not force a parallel tractor.
\item[(iv)] \emph{(Count, argued.)} Any local functional of the scale at fixed conformal class has one Euler-Lagrange equation, while parallelism of the scale tractor is nine independent trace-free conditions at second order, with a solution space of dimension at most six (parallel sections of a rank-six bundle). A single equation that is noncharacteristic on some hypersurface has an infinite-dimensional solution space (Cauchy-Kovalevskaya, cited from memory), so no such principle has exactly the almost-Einstein scales as its stationary points. Not treated: functionals whose Euler-Lagrange equation is characteristic everywhere, and principles that are not variational. A variational principle that does select them is either one with Lagrange multipliers for $\nabla I'$, a rewording of the parallel-tractor condition, or a principle that varies the conformal class too, that is, a dynamical principle for the whole gauge field $\hb$.
\end{enumerate}
In the vacuum the frozen point is the almost-Einstein scale; with matter, Theorem \claimref{synthesis.infinity-vacuum-incidence-is-a-property-of-the-scale}(4) already shows that the scale tractor's derivative is the trace-free stress tensor, a law only for an independently given $T$. The results above add that the series' positive structure does not supply the trace-free part, that the two natural variational principles in the scale do not, and (argued) that no local functional of the scale with a somewhere noncharacteristic Euler-Lagrange equation does.

## technical
The open problem asks for a principle of the series that selects the scale within the conformal class, so that the infinity vacua's incidence, and with matter the field equations, follow rather than being restated. It proposed two lines: the sesquilinear (non-conformally invariant) structure, where the rung unit is seen, and a variational principle for the scale tractor. The first is blocked by an exact symmetry argument, and the two natural forms of the second by exact counter-models; the general variational case is only argued.

The positive structure is invariant under the centraliser of the conformal energy $Z$: a circle times the rotations of the four negative directions. That group fixes no tractor. Its circle fixes exactly the tractors of negative cosmological constant, the wrong sign, and no null (flat) tractor is fixed by either factor. So the structure can at most fix two numbers of a tractor, the norms of its two projections, and with them $\Lambda$; it cannot fix the scale tractor itself, which also carries a position and a direction.

A variational principle in the scale alone, with the conformal class held fixed, has one Euler-Lagrange equation. The Einstein-Hilbert action restricted to a conformal class gives the trace of the field equations and nothing else, the Yamabe equation; its stationary scales include harmonic conformal factors such as $1 + x_{1}x_{2}$, whose metric has zero scalar curvature and nonzero trace-free Ricci tensor. The tractor Dirichlet functional gives the biharmonic equation, again with $1 + x_{1}x_{2}$ stationary; and in Lorentzian signature the scale $(t + x_{1})^{2}$, whose trace-free Hessian is a null square, has zero action density without being parallel. The trace-free part of the field equations, nine conditions, is what a selecting principle must supply. These two functionals do not supply it, and a count (argued, by Cauchy-Kovalevskaya) says that no local functional of one scalar with a somewhere noncharacteristic Euler-Lagrange equation does; everywhere-characteristic equations and nonvariational principles are not treated. What remains is a principle that varies the whole gauge field $\hb$, on the series' route the Clausius relation with the local-horizon premise, or a Lagrange-multiplier restatement, which the problem excludes. The computations are exact in $\Cl(2,4)$ (commutant ranks, the Cayley rotation, tabulated scales) and in rational arithmetic (Ricci from the Christoffel symbols of $\varphi^{2}\eta$ at rational points, polynomial Euler-Lagrange operators).

## lay
In the series, the step from quantum data to Einstein's equations stops at one choice: of all the ways to put a ruler on spacetime that agree about light rays, which one is the physical one. This result tests two natural ways of making that choice from inside the series and shows that neither works in the forms tested. The series' notion of positive probability has a symmetry, and that symmetry moves every possible ruler, so it cannot pick one out; at most it could pick the size of the cosmological constant. And the natural actions built from the ruler alone give only one equation, while Einstein's equations need ten; simple examples satisfy the one equation and are not solutions of Einstein's. A counting argument suggests the same for any such action, though it is not proved for every kind. The missing nine must come from something that moves the light cones as well, which is gravity's own dynamics.

## one-liner
The positive Hermitian structure's symmetry (the centraliser $\mathfrak{u}(1)\oplus\so(4)$ of $Z = e_{0}\nu$) fixes no scale tractor: its $\mathfrak{u}(1)$ fixes exactly the $\Lambda < 0$ ones and no null one, and it can fix at most the two projection norms (so $\Lambda$), not the scale. The restricted Einstein-Hilbert action has the single Euler-Lagrange equation of Yamabe, with $\varphi = 1 + x_{1}x_{2}$ stationary and not almost-Einstein, and the tractor Dirichlet functional gives $\Box^{2}\sigma = 0$, with $1 + x_{1}x_{2}$ stationary and $(t + x_{1})^{2}$ of zero action, neither parallel; argued: any local functional of the scale with a somewhere noncharacteristic Euler-Lagrange equation has an infinite-dimensional stationary set. With a boost added, structure and boost fix the ray of the de Sitter tractor at $\Lambda = 12/\rho^{2}$ for the tube point $I_{7}\rho e_{0}$ ($I_7$ the complex unit of $\Cl(2,4)_{\C}$; $\rho = 2\ell$; foot at the origin only).
