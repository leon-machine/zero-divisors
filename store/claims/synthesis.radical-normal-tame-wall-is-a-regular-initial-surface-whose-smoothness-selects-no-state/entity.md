---
id: synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state
kind: claim
version: 4
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
- name: Claude Opus 5.5
  role: 'GTG proof of the curvature statements of (i), (iii), (iv): diagonal gauge fields, torsion-solved Omega, store-sign field strength, Ricci and Einstein maps; coordinate engine kept as a confirming reading'
  version: 3
  source: maintainer pass 2026-11-07 (GTG proofs)
- name: Claude Fable 5.2
  role: 'dated note: the clauses are about prescribed fields; the radiation-type descent hypothesis is stated for a Cauchy collar only; reference to the trace-anomaly result with its hypotheses (A) and (E); no clause changed'
  version: 4
  source: 'maintainer pass of 2026-11-24 (run 2026-11-24-three-routes)'
amendments:
- version: 4
  kind: restatement
  defect: 'the statement did not say that clauses (i) and (iv), read of the series'' descended field, use the wall itself (a flat half-space with Cauchy slices down to the wall; the radiation origin as the initial slice of half of Minkowski space), which the radiation-type descent hypothesis as restated for the collar does not assert, and that with the whole expected stress as source the exact radiation field is not a solution given hypotheses (A) and (E) of the trace-anomaly result; clauses (i) to (iv), the proof and the checks are unchanged'
  evidence: 'synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall: check.py::check_no_power_law_origin_is_tame_unless_the_anomaly_vanishes'
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
- kind: check
  ref: check.py::check_gtg_wall_field_strengths
lineage:
  motivated_by:
  - standard-model.dating-descent
  - synthesis.imported-propagation-of-hadamard-form
  - dark-energy.gravity-pre-metric-forces-degenerate-exactly
  - synthesis.pre-descent-state-carried-into-descended-phase-premise
extraction:
  maintainer_pass_2026_11_24_three_routes:
    by: maintainer-2026-11-24
    date: '2026-11-24'
    note: 'Version 3 -> 4. By Leon''s decision of 24 November 2026 the radiation-type descent hypothesis is restated for the collar only. This theorem is about prescribed fields (the tame wall as geometry) and is not changed: a dated note is added to the formal level, and one sentence of the technical level is restated, saying that the clauses are about prescribed fields, that the hypothesis is about a Cauchy collar only, that a result using the wall itself must name what it assumes there, and that with the whole expected stress as source the exact radiation field is not a solution, citing the trace-anomaly result with its named hypotheses (A) and (E). The sentence of the note below ''the radiation-type reading is the one under which this step holds'' is to be read with the hypothesis in its collar form. No mathematics, link or check changed.'
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'GTG proof for the curvature content: every metric of the result is (up to the sign of C7) the derived metric of a diagonal gauge field hb^{-1}(e_t) = N e0, hb^{-1}(e_i) = A_i e_i; the torsion equation gives Omega(e_{x^i}) = -(dA_i/N) B_i, and the store-sign operator is diagonal with calR(B_i) = d_t(dA_i/N)/(N A_i), calR(e_i ^ e_j) = dA_i dA_j/(N^2 A_i A_j); from it (i) the radical-normal side is flat (Omega = 0), (iii) R = (b/2)(b + 2 - a) t^(a - 2), 3/2 t^-2 for (0, 1), (iv) the Einstein map gives p = 2/(3(1 + w)) and the radiation field has R = 0, Ricci square 3/4 t^-4; the sign agreement with the (-,+,+,+) index convention is derived. The Dirac and scalar analysis was already in GA and scalar calculus. The coordinate engine stays as a confirming reading. New check check_gtg_wall_field_strengths; runcheck 6/6, check4 clean on a proposals copy. outside_ga removed: the curvature values now come from the gauge field, and the line elements and cometric components are the definition''s readings (tameness is defined on the cometric). Statement, status, links unchanged.'
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
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) and $g$ its derived metric, with inverse $G$ (the cometric). Let $\Sigma = \{t = 0\}$ in coordinates $(t, x, y, z)$, with physical side $t > 0$, and for exponents $(a, b)$ let $G_{a,b} = \mathrm{diag}(-t^{a}, t^{b}, 1, 1)$, with $g_{a,b} = \mathrm{diag}(-t^{-a}, t^{-b}, 1, 1)$ on $t \neq 0$; these components, and the line elements below, are written in the signature $(-,+,+,+)$ (dictionary C7), while the spacetime algebra of (ii) has $\gamma_{0}^{2} = +1$; the scalar curvature $R$ quoted below has the same value in the store's sign in $(+,-,-,-)$, and the Ricci square does not depend on the sign. The degeneration at $\Sigma$ is tame (Definition \claimref{sheaf.tameness}) exactly for $(a, b) = (1, 0)$, with radical $dt$, the conormal of $\Sigma$, and $(a, b) = (0, 1)$, with radical $dx$, tangent; in both the metric has the simple pole of Fact \claimref{dark-energy.imported-walls-sphere-theorem}.
\begin{enumerate}
\item[(i)] \emph{(Radical the conormal: a regular initial surface; proved.)} For $(1, 0)$, with $\tau = 2\sqrt{t}$, $g_{1,0} = -d\tau^{2} + dx^{2} + dy^{2} + dz^{2}$: the physical side is the half $\tau > 0$ of Minkowski space, flat, at proper time $2\sqrt{t}$ from $\Sigma$, and its slices $\tau = \varepsilon > 0$ are Cauchy surfaces; the far side is Riemannian. So the propagation of the Hadamard form (Fact \claimref{synthesis.imported-propagation-of-hadamard-form}, scalar field) carries a two-point function of Hadamard form near one slice $\tau = \varepsilon$ to the whole physical side.
\item[(ii)] \emph{(Smoothness at the wall selects no bulk state; proved.)} $\partial_{\tau}^{2} = t\,\partial_{t}^{2} + \tfrac12\partial_{t}$, with indicial exponents $0$ and $\tfrac12$. A Klein-Gordon solution of any mass on the physical side is smooth in $t$ up to $\Sigma$ exactly when it is even in $\tau$, that is when $\partial_{\tau}\phi = 0$ on $\Sigma$; these solutions form a Lagrangian subspace for the symplectic form, so the fields they smear commute. In the constant frame of the chart $(\tau, x, y, z)$ (zero spin connection), a Dirac plane wave (Hestenes form, spatial wave vector $k$, mass $m$) obeys $\phi' = M\phi$ with $M^{2} = -(|k|^{2} + m^{2})$, so it is smooth in $t$ across $\Sigma$ only if it vanishes, unless $k = 0 = m$; the only Dirac solution with square-integrable data that is smooth in $t$ across $\Sigma$ in this frame is zero, for every mass. So no bulk field obeying the canonical commutation or anticommutation relations is smooth across $\Sigma$ in $t$, while in $\tau$ the surface imposes no condition: smoothness at the wall selects no bulk state. This does not concern the boundary modes the wall carries by the wall Fact, nor any selection by the Riemannian far side.
\item[(iii)] \emph{(Radical tangent: a singular wall; proved.)} For $(0, 1)$, $g_{0,1} = -dt^{2} + t^{-1}dx^{2} + dy^{2} + dz^{2}$ has scalar curvature $R = \tfrac32 t^{-2}$, unbounded at $\Sigma$, at finite proper time; the far side has signature $(2, 2)$. Its slices $t = \varepsilon > 0$ are Cauchy surfaces of the physical side, and $\Sigma$ is a singular past boundary.
\item[(iv)] \emph{(Power-law origins in cosmic time; proved.)} For a spatially flat expanding field $-dt^{2} + t^{2p}(dx^{2} + dy^{2} + dz^{2})$ of a perfect fluid with $P = w\rho$, $p = 2/(3(1 + w))$, in the cosmic coordinate $t$ the metric is $t^{2p}$ times a field whose cometric degenerates at $t = 0$ with radical $dt$, tamely exactly when $2p = 1$, that is $w = \tfrac13$; the radiation-dominated field is $t\,g_{1,0}$, with conformal time $\tau$, scalar curvature $0$ and Ricci square $\mathcal{R}(\partial_{a})\cdot\mathcal{R}(a) = \tfrac34 t^{-4}$ (in components $R_{ab}R^{ab}$). In its conformal time $\eta$ every such field with $p < 1$ has the bracket $-d\eta^{2} + dx^{2} + dy^{2} + dz^{2}$, which is $g_{1,0}$ in $t' = \eta^{2}/4$: tameness of the bracket is a property of the time coordinate. For the conformally covariant fields (the massless Dirac, Maxwell and Yang-Mills fields) the radiation origin is the initial slice of half of Minkowski space, where the Weyl curvature vanishes. Which bulk solutions are smooth in $t$ there depends on the conformal weight: for the massless scalar ($R = 0$, so minimal and conformal coupling agree), $\phi = t^{-1/2}\phi_{\mathrm{flat}}$, they are the solutions odd in $\tau$ (indicial exponents $0$ and $-\tfrac12$), the other half from (ii); for the massless Dirac field, $\psi = t^{-3/4}\psi_{\mathrm{flat}}$, the exponents $-\tfrac34 + \tfrac{n}{2}$ are never integers and no nonzero solution is smooth in $t$.
\end{enumerate}
\emph{Note (24 November 2026; the radiation-type descent hypothesis).} Clauses (i) to (iv) are statements about prescribed fields, the model walls $G_{a,b}$ and the power-law fields of (iv), and are unchanged. They do not say that the descended field of the series is the exact radiation field down to $\Sigma$. The radiation-type descent hypothesis, where a result takes it, is a hypothesis about a Cauchy collar of the descent and nothing more (restated for the collar only by Leon's decision of 24 November 2026): on the collar the scale factor is smooth, the field is Weyl-flat and the conformal vacuum is an admissible reference. It does not say that the field is the exact radiation field down to the wall, and a result that uses the wall itself (a mass term linear in conformal time through it, a continuation across it, the wall as the initial slice of half of Minkowski space) must name what it assumes there. Two sentences above are of that kind when they are read of the descended field: that the physical side is a flat half of Minkowski space with Cauchy slices down to $\Sigma$ (clause (i)), and that the radiation origin is the initial slice of half of Minkowski space for the conformally covariant fields (clause (iv)); each holds for the prescribed field of its clause. With the whole expected stress as the source the exact radiation field is not a solution of the field equation, given hypotheses (A) and (E) of Theorem \claimref{synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall}, which are named hypotheses of that result and not stored premises.

## technical
The deposit chain needs the descent's surface to be a surface on which a state can be set and then carried forward by the standard propagation of the Hadamard form. The series' walls are tame corank-one degenerations of the inverse metric. In the two aligned normal forms the outcome depends on whether the degenerate direction is the wall's normal. If it is, the physical side, measured in its own proper time, is a flat half of Minkowski space, so slices near the wall are Cauchy surfaces and propagation works from any thin collar; but the bulk fields that are smooth across the wall in the wall's own coordinate have zero momentum there (half of the scalar phase space, on which the fields commute) and, for the Dirac field in the flat frame, vanish, so smoothness at the wall cannot carry quantum data and selects no state. Whether the wall's boundary modes or a Euclidean reading of its Riemannian far side select one is not examined. If the degenerate direction is tangent, the wall is a curvature singularity. In cosmic time a radiation-dominated expanding universe is, up to a conformal factor, exactly the normal case, and it is the only power law with this property in that coordinate; in conformal time every decelerating power law is. Under the radiation-type descent hypothesis, which is about a Cauchy collar of the descent only (restated for the collar only by Leon's decision of 24 November 2026) and not about the field down to the wall, the chain's second step holds from the collar; what is missing is the state itself on the collar. The clauses here are about prescribed fields: with the whole expected stress as the source the exact radiation field is not a solution, given the two named hypotheses of the trace-anomaly result (\claimref{synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall}). Transport-absent.

## lay
For a quantum field to be in a reasonable state everywhere, it is enough to set it up reasonably on one complete slice of time and let the equations carry it forward. This result asks whether the moment of the descent, where the series' geometry degenerates in the mild way the series assumes, can be that slice. In the case where the degenerate direction points along time, the moment behaves like an ordinary starting slice, so the carrying forward works, but requiring the fields to be smooth there puts no usable condition on the state, so it does not choose one. In the other case the moment is a genuine singularity. In the usual cosmic time, the early radiation-filled universe turns out to be the first case in disguise.

## one-liner
Under the tameness hypothesis, at an aligned tame corank-one wall with the radical the conormal, the physical side is in its proper time $\tau = 2\sqrt{t}$ a flat half-spacetime with Cauchy slices, so the propagation of the Hadamard form holds from any collar, but bulk fields smooth across the wall in $t$ are a Lagrangian half of the scalar data and zero for the Dirac field in the flat frame, so smoothness at the wall selects no state; with the radical tangent the wall has $R = \tfrac32 t^{-2}$; in cosmic time only the radiation-dominated power law ($w = \tfrac13$) has a tame conformal bracket (factor $t$), while in conformal time every power law with $p < 1$ is the radical-normal wall.
