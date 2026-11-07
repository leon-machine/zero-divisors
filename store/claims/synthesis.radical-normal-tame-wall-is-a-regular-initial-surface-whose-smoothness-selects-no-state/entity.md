---
id: synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state
kind: claim
version: 3
title: 'A radical-normal tame wall is a regular initial surface that selects no state'
status: proved
region: synthesis
subject: quantum-fields
tags: [no-go, horizons, car-algebra]
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
  role: 'GA rewrite (Ricci square; coordinate curvature engine declared)'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - dark-energy.imported-walls-sphere-theorem@6
  - sheaf.metrics-residue-square-root-twist@5
  - synthesis.imported-propagation-of-hadamard-form@1
  - transport.pinching-kernel@3
  - synthesis.imported-bochner-theorem-moment-lemma-and-whitney-even-functions@2
  - synthesis.imported-conformal-covariance-of-massless-fields-and-local-conformal-flatness@1
  - synthesis.imported-hadamard-stress-tensor-diverges-at-the-reissner-nordstrom-de-sitter-cauchy-horizon@1
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_aligned_tame_walls_regular_iff_radical_normal
- kind: check
  ref: check.py::check_radiation_origin_is_conformally_a_radical_normal_wall
- kind: check
  ref: check.py::check_wall_smooth_scalar_solutions_are_a_lagrangian_half
- kind: check
  ref: check.py::check_wall_smooth_dirac_solutions_are_static_zero_modes
- kind: check
  ref: check.py::check_radiation_field_smoothness_in_t_depends_on_the_conformal_weight
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.dating-descent
  - synthesis.imported-propagation-of-hadamard-form
  - dark-energy.gravity-pre-metric-forces-degenerate-exactly
  - synthesis.pre-descent-state-carried-into-descended-phase-premise
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The Ricci square is written R(d_a).R(a) for the Ricci map of the GTG definition (sign-independent, equal to R_{ab} R^{ab}, kept as a labelled reading); the curvature values of the proof come from the check''s coordinate curvature engine (Christoffel route, its stated sign convention, metrics in (-,+,+,+)), described as such and declared outside_ga (other). Reader fix (R06), version kept: the signature (-,+,+,+) of the components and line elements is declared beside the (+,-,-,-) algebra of (ii), with the statement that R has the same value in the store''s sign and the Ricci square is sign-free (dictionary C6, C7).'
  open_problem: op.deposit-state-is-hadamard
  note: >-
    Bears on the second step of op.deposit-state-is-hadamard: whether the descent's surface is a Cauchy
    surface on which a deposited state can be set and then propagated. Read as a tame corank-one wall (the
    series' degenerate-cometric wall), the answer splits by the radical. With the radical the conormal the
    physical side is, in its proper time, a flat half of Minkowski space: the propagation of the Hadamard form
    holds from any collar. Smoothness in the wall's own coordinate selects no bulk state: the bulk solutions
    smooth there are a Lagrangian half of the scalar data (vanishing momentum on the wall) and, for the Dirac
    field in the flat frame, only zero. This concerns smoothness only: the wall's boundary modes of the stored
    wall Fact are not bulk fields, and the Riemannian far side could act as a Euclidean (no-boundary) selector,
    which is not examined here. With the radical tangent the wall is a curvature singularity and the state there
    is initial data to be matched. In cosmic time the radiation-dominated power-law field is, up to the factor t,
    the radical-normal wall, and it is the only power law whose conformal bracket is a tame wall in that
    coordinate; in its own conformal time every power law with p < 1 is the same wall, so tameness depends on the
    choice of time coordinate. Smoothness in t at the radiation origin depends on the conformal weight: for the
    massless scalar the smooth solutions are the other half, for the massless Dirac field there are none. With the
    descent's conditional expectation the identity on its range, the missing datum is located exactly: a Hadamard
    state on a collar of the wall. Which normal form the descent has is not fixed by the store; the
    radiation-type reading is the one under which this step holds. Transport-absent. Imported as Facts: conformal
    covariance of the massless Dirac, Maxwell and Yang-Mills fields in four dimensions (synthesis.imported-conformal-covariance-of-massless-fields-and-local-conformal-flatness); S. Hollands, R. Wald and J. Zahn (2020) on the stress tensor at the Cauchy horizon of
    Reissner-Nordstrom-de Sitter (synthesis.imported-hadamard-stress-tensor-diverges-at-the-reissner-nordstrom-de-sitter-cauchy-horizon); Whitney's theorem on
    even functions, H. Whitney, Duke Math. J. 10 (1943) 159 (synthesis.imported-bochner-theorem-moment-lemma-and-whitney-even-functions, clause (c)).
    The tameness of the models is Definition sheaf.tameness, taken as given (an assumes edge, as for the wall
    Fact). Literature cited from memory: G. Ellis, A. Sumeruk, D. Coule and C. Hellaby, Class. Quantum Grav. 9 (1992) 1535, and T. Dray, C. Manogue
    and R. Tucker, Gen. Rel. Grav. 23 (1991) 967 (signature change at a degenerate metric).
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, at Leon''s decisions of 2026-11-01: an assumes edge to sheaf.tameness@1, matching the stored wall Fact (the models are tame corank-one degenerations in the sense of that definition); uses edges to the imported Facts on Whitney''s theorem, conformal covariance and the Reissner-Nordstrom-de Sitter Cauchy horizon (Hollands, Wald and Zahn) replace the citations from memory in the proof and the note; the lay level and the one-liner name the tameness hypothesis. Statement, proof steps and checks otherwise unchanged.'
  flags:
  - 'aligned models only: the cometric is diagonal with the degeneration in one coordinate; tame walls whose radical is neither the conormal nor tangent are not classified here'
  - 'flat transverse block in the proved clauses; transverse metrics depending on t are treated in argued remarks only'
  - 'smoothness in t is coordinate- and weight-dependent: tameness of a power-law bracket holds in cosmic time only, and which solutions are smooth in t depends on the conformal weight and, for spinors, on the frame'
outside_ga:
  kind: other
  why: 'The scalar and Ricci curvatures and the Einstein components of the proof are those returned by the check''s coordinate curvature engine, which works from the Christoffel symbols of metrics written in the signature (-,+,+,+) and states its own sign convention; the proof describes that computation in components, and a derivation through the rotation-gauge field would be a different proof.'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) and $g$ its derived metric, with inverse $G$ (the cometric). Let $\Sigma = \{t = 0\}$ in coordinates $(t, x, y, z)$, with physical side $t > 0$, and for exponents $(a, b)$ let $G_{a,b} = \mathrm{diag}(-t^{a}, t^{b}, 1, 1)$, with $g_{a,b} = \mathrm{diag}(-t^{-a}, t^{-b}, 1, 1)$ on $t \neq 0$; these components, and the line elements below, are written in the signature $(-,+,+,+)$ (dictionary C7), while the spacetime algebra of (ii) has $\gamma_{0}^{2} = +1$; the scalar curvature $R$ quoted below has the same value in the store's sign in $(+,-,-,-)$, and the Ricci square does not depend on the sign. The degeneration at $\Sigma$ is tame (Definition \claimref{sheaf.tameness}) exactly for $(a, b) = (1, 0)$, with radical $dt$, the conormal of $\Sigma$, and $(a, b) = (0, 1)$, with radical $dx$, tangent; in both the metric has the simple pole of Fact \claimref{dark-energy.imported-walls-sphere-theorem}.
\begin{enumerate}
\item[(i)] \emph{(Radical the conormal: a regular initial surface; proved.)} For $(1, 0)$, with $\tau = 2\sqrt{t}$, $g_{1,0} = -d\tau^{2} + dx^{2} + dy^{2} + dz^{2}$: the physical side is the half $\tau > 0$ of Minkowski space, flat, at proper time $2\sqrt{t}$ from $\Sigma$, and its slices $\tau = \varepsilon > 0$ are Cauchy surfaces; the far side is Riemannian. So the propagation of the Hadamard form (Fact \claimref{synthesis.imported-propagation-of-hadamard-form}, scalar field) carries a two-point function of Hadamard form near one slice $\tau = \varepsilon$ to the whole physical side.
\item[(ii)] \emph{(Smoothness at the wall selects no bulk state; proved.)} $\partial_{\tau}^{2} = t\,\partial_{t}^{2} + \tfrac12\partial_{t}$, with indicial exponents $0$ and $\tfrac12$. A Klein-Gordon solution of any mass on the physical side is smooth in $t$ up to $\Sigma$ exactly when it is even in $\tau$, that is when $\partial_{\tau}\phi = 0$ on $\Sigma$; these solutions form a Lagrangian subspace for the symplectic form, so the fields they smear commute. In the constant frame of the chart $(\tau, x, y, z)$ (zero spin connection), a Dirac plane wave (Hestenes form, spatial wave vector $k$, mass $m$) obeys $\phi' = M\phi$ with $M^{2} = -(|k|^{2} + m^{2})$, so it is smooth in $t$ across $\Sigma$ only if it vanishes, unless $k = 0 = m$; the only Dirac solution with square-integrable data that is smooth in $t$ across $\Sigma$ in this frame is zero, for every mass. So no bulk field obeying the canonical commutation or anticommutation relations is smooth across $\Sigma$ in $t$, while in $\tau$ the surface imposes no condition: smoothness at the wall selects no bulk state. This does not concern the boundary modes the wall carries by the wall Fact, nor any selection by the Riemannian far side.
\item[(iii)] \emph{(Radical tangent: a singular wall; proved.)} For $(0, 1)$, $g_{0,1} = -dt^{2} + t^{-1}dx^{2} + dy^{2} + dz^{2}$ has scalar curvature $R = \tfrac32 t^{-2}$, unbounded at $\Sigma$, at finite proper time; the far side has signature $(2, 2)$. Its slices $t = \varepsilon > 0$ are Cauchy surfaces of the physical side, and $\Sigma$ is a singular past boundary.
\item[(iv)] \emph{(Power-law origins in cosmic time; proved.)} For a spatially flat expanding field $-dt^{2} + t^{2p}(dx^{2} + dy^{2} + dz^{2})$ of a perfect fluid with $P = w\rho$, $p = 2/(3(1 + w))$, in the cosmic coordinate $t$ the metric is $t^{2p}$ times a field whose cometric degenerates at $t = 0$ with radical $dt$, tamely exactly when $2p = 1$, that is $w = \tfrac13$; the radiation-dominated field is $t\,g_{1,0}$, with conformal time $\tau$, scalar curvature $0$ and Ricci square $\mathcal{R}(\partial_{a})\cdot\mathcal{R}(a) = \tfrac34 t^{-4}$ (in components $R_{ab}R^{ab}$). In its conformal time $\eta$ every such field with $p < 1$ has the bracket $-d\eta^{2} + dx^{2} + dy^{2} + dz^{2}$, which is $g_{1,0}$ in $t' = \eta^{2}/4$: tameness of the bracket is a property of the time coordinate. For the conformally covariant fields (the massless Dirac, Maxwell and Yang-Mills fields) the radiation origin is the initial slice of half of Minkowski space, where the Weyl curvature vanishes. Which bulk solutions are smooth in $t$ there depends on the conformal weight: for the massless scalar ($R = 0$, so minimal and conformal coupling agree), $\phi = t^{-1/2}\phi_{\mathrm{flat}}$, they are the solutions odd in $\tau$ (indicial exponents $0$ and $-\tfrac12$), the other half from (ii); for the massless Dirac field, $\psi = t^{-3/4}\psi_{\mathrm{flat}}$, the exponents $-\tfrac34 + \tfrac{n}{2}$ are never integers and no nonzero solution is smooth in $t$.
\end{enumerate}

## technical
The deposit chain needs the descent's surface to be a surface on which a state can be set and then carried forward by the standard propagation of the Hadamard form. The series' walls are tame corank-one degenerations of the inverse metric. In the two aligned normal forms the outcome depends on whether the degenerate direction is the wall's normal. If it is, the physical side, measured in its own proper time, is a flat half of Minkowski space, so slices near the wall are Cauchy surfaces and propagation works from any thin collar; but the bulk fields that are smooth across the wall in the wall's own coordinate have zero momentum there (half of the scalar phase space, on which the fields commute) and, for the Dirac field in the flat frame, vanish, so smoothness at the wall cannot carry quantum data and selects no state. Whether the wall's boundary modes or a Euclidean reading of its Riemannian far side select one is not examined. If the degenerate direction is tangent, the wall is a curvature singularity. In cosmic time a radiation-dominated expanding universe is, up to a conformal factor, exactly the normal case, and it is the only power law with this property in that coordinate; in conformal time every decelerating power law is. Under the radiation-type reading the chain's second step holds; what is missing is the state itself on the collar. Transport-absent.

## lay
For a quantum field to be in a reasonable state everywhere, it is enough to set it up reasonably on one complete slice of time and let the equations carry it forward. This result asks whether the moment of the descent, where the series' geometry degenerates in the mild way the series assumes, can be that slice. In the case where the degenerate direction points along time, the moment behaves like an ordinary starting slice, so the carrying forward works, but requiring the fields to be smooth there puts no usable condition on the state, so it does not choose one. In the other case the moment is a genuine singularity. In the usual cosmic time, the early radiation-filled universe turns out to be the first case in disguise.

## one-liner
Under the tameness hypothesis, at an aligned tame corank-one wall with the radical the conormal, the physical side is in its proper time $\tau = 2\sqrt{t}$ a flat half-spacetime with Cauchy slices, so the propagation of the Hadamard form holds from any collar, but bulk fields smooth across the wall in $t$ are a Lagrangian half of the scalar data and zero for the Dirac field in the flat frame, so smoothness at the wall selects no state; with the radical tangent the wall has $R = \tfrac32 t^{-2}$; in cosmic time only the radiation-dominated power law ($w = \tfrac13$) has a tame conformal bracket (factor $t$), while in conformal time every power law with $p < 1$ is the radical-normal wall.
