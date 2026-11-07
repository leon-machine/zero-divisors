---
id: synthesis.restricted-dirac-hadamard-parametrix-on-a-null-hypersurface-is-the-null-vacuum-plus-a-bounded-kernel
kind: claim
version: 2
title: 'Dirac parametrix on a null hypersurface: the null vacuum plus a bounded kernel'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, horizons, car-algebra, null-directions, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-02-hs-bound
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
- obj.hawking.continuum-mode-space
derivations:
- name: main
  uses:
  - synthesis.imported-gtg-dictionary@1
  - synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport@3
  - synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard@2
  - synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces@4
  - synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_projector_keeps_only_the_screen_null_components
- kind: check
  ref: check.py::check_log_coefficient_formula_on_generic_jets
- kind: check
  ref: check.py::check_log_coefficient_vanishes_by_the_van_vleck_identity
- kind: check
  ref: check.py::check_first_principles_plane_wave_kernel
- kind: check
  ref: check.py::check_flat_field_shearing_hypersurface
- kind: check
  ref: check.py::check_model_transport_rotor_and_connection
- kind: check
  ref: check.py::check_mass_and_log_terms_are_below_the_log_order
- kind: check
  ref: check.py::check_regularised_model_integrals
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.hadamard-scaling-limit-premise
  - synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces
  - synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes
  - synthesis.c-loc-local-horizon-premise
outside_ga:
  kind: complex-analysis
  why: 'i stays only in the regulator sigma_epsilon = sigma + i epsilon(t(x) - t(x'')) - epsilon^2/2, a shift of the spacetime separation along a time function, and in the epsilon-expressions it generates (the complex shift of the transverse Gaussian integral, C_epsilon, A_epsilon, s_0 + i g epsilon), and in the imported i0 prescription: no pseudoscalar commutes with the spacetime vectors; the Dirac numerator carries the right unit R_{I_4} and the restricted outputs, W_0 included, carry I_4'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By Leon''s ruling R2 (7 November 2026) the Hadamard chain carries the field theory''s unit I_4: the Dirac numerator is (R_{I_4}D_x + m_0) with R_{I_4} the right unit, and the outputs of the regularised restriction are written with I_4 (W_0 = (I_4/2 pi)(u - u'' + I_4 0)^{-1}, log(-I_4 s), log(-I_4(u - u'')), the I_4 0 term, the smooth kernel (I_4/2 pi) d_u log phi_t and the nonlinear-time limit), numbers read in span{1, I_4}. Stays: the regulator sigma_epsilon = sigma + i epsilon(t - t'') - epsilon^2/2 and every epsilon-expression it generates (the complex Gaussian shift, C_epsilon, A_epsilon, s_0 + i g epsilon), and the imported i0 prescription; declared complex-analysis. The exponents epsilon^{i}, i >= 1 of Step 5 are indices.'
  open_problem: op.qft-on-gtg-fields
  note: >-
    Proves the remainder bound that the premise (HS), synthesis.hadamard-scaling-limit-premise version 3,
    poses on the restricted Dirac parametrix, and the cancellation of the log epsilon terms that the result
    synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces
    left argued. Method: expand the projected kernel Lambda D(U/sigma) e0 Lambda in the label difference eta
    in a rotation gauge where the parallel null frame of the hypersurface has constant images (Lambda
    constant, Omega(k) = 0 on H). The numerator vanishes to second order in eta (Lambda k = 0 and Lambda p e0
    Lambda = (p.k) Lambda), so nothing is more singular than |eta|^-2; the coefficient of log epsilon (and of
    log(-is)) is the mean of the degree -2 part over the ellipse of the transverse Hessian M, and it equals
    2 pi (a a')^(1/2) (d_u + theta/2)(Delta^(1/2)/sqrt(det M)) Lambda: the derivative along the generator gives
    d_u, the projected transverse spin connection gives theta/2 (only the f^n components of a bivector survive
    the projection, and the trace of the self-adjoint expansion-shear map is the expansion), and the
    first-order spinor transport enters only through a transverse divergence of a degree -1 function, which
    has no logarithm. By the stored identity Delta^(1/2)/sqrt(det M) = (a a')^(-1/2) the bracket is zero: the
    term -pi theta (log epsilon + log(-is)) delta^2 is cancelled by the connection term, on every field and
    every geodesic null hypersurface, for every mass (the mass term and V log sigma are less singular). The
    only (u - u' + i0)^-1 term is the i0 term of the null vacuum. Exact model integrals (a shift of the
    transverse integration plane absorbs the part of the time function linear in eta) give a bound on the
    rest uniform in epsilon, so the epsilon -> 0 limit exists as a distribution and differs from W0 (x) id_K
    by a bounded kernel: generator scaling degree at most 0, which is the premise's clause with any varpi in
    (0, 1). Checked exactly on generic jets (arbitrary transport, connection components and frame data), on
    the plane-wave field from first principles (closed-form Synge function, exact spin transport rotor,
    connection checked against its coordinate reading (Christoffel symbols); tidal and deviation maps not commuting; central and off-central
    generators) and on the flat field with an expanding and shearing null hypersurface; mutations (no
    connection, non-self-adjoint B, frozen projector, doubled d log Delta, no transport) break the checks.
    What it does not give: the restriction is the epsilon-regularised one in which (HS) is posed; the
    agreement with the restriction defined through the characteristic-data embedding of the generator field,
    which carries the conclusion from the parametrix to states, is not part of it. The regularised restriction
    depends on the time function through a smooth kernel (on the flat null plane with a time function
    nonlinear along the generators the limit is (i/2 pi) t_u/(t(u) - t(u') + i0)), so it and the bounded
    remainder are defined for a chosen time function and only modulo smooth kernels, which the clause of
    (HS) does not see. Closest prior art: Kay and Wald (Phys. Rep. 207 (1991) 49) gave the restriction to the
    horizon of the Killing-invariant Hadamard state of the scalar field on a spacetime with a bifurcate
    Killing horizon, -(1/pi) int F1 F2 (U1 - U2 - i0)^-2, the whole restricted two-point function, through
    characteristic data (read through C. Dappiaggi, V. Moretti and N. Pinamonti, arXiv:0907.1034, Sec. 3.2,
    Eq. (27), and K. Sanders, arXiv:1310.5537, Sec. 1; not checked against the original); there expansion,
    shear and the tidal map vanish and the cancellation is empty. Transport-absent: free field theory on a Gauge
    Theory Gravity field; Gauge Theory Gravity is convenient (one global spinor trivialisation, the projector
    algebra in the spacetime algebra, the plane-wave field in Kerr-Schild form with an exact transport rotor).
  flags:
  - 'the restriction is the epsilon -> 0 limit of the transverse-smeared, i0-regularised parametrix, the one in which (HS) version 3 is posed; its agreement with the restriction through the characteristic-data embedding (cited from memory in the stored result) is not shown here'
  - 'hypothesis (S), that points of distinct generators are spacelike separated, is proved for small enough pieces of the hypersurface (transverse Hessian positive near the diagonal) and holds on local Rindler horizons (achronal null boundaries; standard causal theory, cited from memory); larger pieces need it as stated'
  - 'the epsilon-regularised restriction depends on the time function through a smooth kernel; it and the remainder are defined for a chosen time function, modulo smooth kernels'
  - 'the generic field is covered by the proof and by exact checks on arbitrary jets; a finite-separation computation on a generic polynomial field (no closed-form Synge function) was not made'
---

## formal
Units $\hbar = c = 1$. Let $(\hb, \Omega)$ be a gravitational field on four-dimensional flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric $g$ is smooth and globally hyperbolic on a region $U$ of its invertible region, $N \subset U$ geodesically convex, and $\mathcal{H} \subset N$ a piece of a null hypersurface generated by affinely parametrised null geodesics $u \mapsto X(u, y)$, with the notation of Theorem \claimref{synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces} ($J$, $a = |\det J|$, $B = J'J^{-1}$, $\theta = \mathrm{tr}\,B$, the transverse Hessian $M(u, u')$ of $-\sigma$, $\Delta$, the canonical projector $\Lambda = \tfrac12 nk$ of the parallel null frame, the canonical generator field $\sqrt{2a}\,\Lambda\psi$, $K = L^{2}(\R^{2}, d^{2}y)\otimes V_{\Lambda}$), such that (S) points of distinct generators of $\mathcal{H}$ are spacelike separated (true on every small enough piece, and on every local Rindler horizon of Premise \claimref{synthesis.c-loc-local-horizon-premise}, the null boundary of the past of a small two-surface element being achronal). For $m_{0} \ge 0$ let $G_{\mathrm{par}} = (R_{I_{4}}D_{x} + m_{0})H_{+}e_{0}$, $H = U/\sigma + V\log\sigma$, $U = \Delta^{1/2}R$, be the Dirac Hadamard parametrix (Fact \claimref{synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport}), regularised by $\sigma_{\epsilon} = \sigma + i\epsilon(t(x) - t(x')) - \tfrac12\epsilon^{2}$ for a time function $t$ (the field theory's unit is $I_{4}$, written $R_{I_{4}} : x \mapsto xI_{4}$ where it acts on the right on the non-even values of the bispinor kernel, and numbers, the values of the regularised kernels included, are read in $\mathrm{span}\{1, I_{4}\}$ and act on the right; $i$ is written only in the regulator itself, a shift of the spacetime separation along a time function), and let $W^{\mathrm{par}}_{\mathcal{H}}$ be its restriction to the generators in the canonical normalisation, smeared with transverse profiles $F, G \in C^{1}_{c}(\R^{2})\otimes V_{\Lambda}$, as the $\epsilon \to 0$ limit of the transverse-smeared kernel (the restriction in which Premise \claimref{synthesis.hadamard-scaling-limit-premise} is posed). With $W_{0}(u, u') = \tfrac{I_{4}}{2\pi}(u - u' + I_{4}0)^{-1}$:
\begin{enumerate}
\item[(i)] \emph{(The logarithms cancel; proved.)} In a rotation gauge in which the parallel null frame has constant images on $\mathcal{H}$, the projected kernel $\Lambda D(U/\sigma)e_{0}\Lambda$ at $x = X(u, y' + \eta)$, $x' = X(u', y')$ has numerator $N = \Lambda[(DU)\sigma - (\nabla\sigma)U]e_{0}\Lambda = O(|\eta|^{2})$, so no part of degree below $-2$ in $\eta$; the coefficient of $\log\epsilon$, which is also that of $\log(-I_{4}(u - u'))$, is
\[
2\pi\,\bigl(a(u)a(u')\bigr)^{1/2}\Bigl(\partial_{u} + \tfrac12\theta(u)\Bigr)\frac{\Delta^{1/2}}{\sqrt{\det M}}\;\Lambda\,\delta^{2}(y - y'),
\]
the derivative along the generator giving $\partial_{u}$, the projected transverse spin connection giving $\tfrac12\theta$, and the first-order spinor transport contributing nothing (it enters through a transverse divergence). Since $\Delta^{1/2}/\sqrt{\det M} = (a(u)a(u'))^{-1/2}$ and $\theta = a'/a$, the coefficient is zero for all $u, u'$: the term $-\pi\theta(u)(\log\epsilon + \log(-I_{4}s))\,\delta^{2}(y - y')$ is cancelled by the connection term. The mass term and $V\log\sigma$ have degree at least $-1$ and give no logarithm.
\item[(ii)] \emph{(The restricted parametrix; proved.)} The limit exists in $\mathcal{D}'$ and $W^{\mathrm{par}}_{\mathcal{H}} = W_{0}\otimes\id_{K} + r$, where in each $K$-component $r_{F,G}(u, u')$ is a bounded function, $\sup|r_{F,G}| \le C$ with $C$ depending only on a compact set containing the supports, a compact $u$-interval, $m_{0}$ and $C^{1}$ bounds on $F$, $G$. The coefficient of $(u - u' + I_{4}0)^{-1}\delta^{2}(y - y')$ is exactly that of $W_{0}\Lambda$ (Theorem \claimref{synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces}(ii)), and no other term contributes at that order. The regularised restriction depends on the time function $t$ through the smooth kernel $\tfrac{I_{4}}{2\pi}\partial_{u}\log\varphi_{t}(u, u')\,\Lambda\,\delta^{2}(y - y')$, where $t(X(u, y)) - t(X(u', y)) = (u - u')\varphi_{t}(u, u', y)$, $\varphi_{t} > 0$ (on the flat null plane with $t$ nonlinear along the generators the limit is $\tfrac{I_{4}}{2\pi}\,\partial_{u}t/(t(u) - t(u') + I_{4}0)$): $r$ is defined for the chosen $t$, and $W^{\mathrm{par}}_{\mathcal{H}}$ is determined only modulo smooth kernels, which the clause of (HS) does not see.
\item[(iii)] \emph{(The bound posed by (HS); proved.)} $R^{\mathrm{par}} = W^{\mathrm{par}}_{\mathcal{H}} - W_{0}\otimes\id_{K}$ has generator scaling degree at most $0$ at every $(u_{0}, u_{0})$: for every $\varpi > 0$, $\lambda^{\varpi}R^{\mathrm{par}}(u_{0} + \lambda x, u_{0} + \lambda x') \to 0$ in $\mathcal{D}'$, uniformly for profiles with support in a fixed compact set and bounded in $C^{1}$. So the clause of Premise \claimref{synthesis.hadamard-scaling-limit-premise} (version 3) holds, with any $\varpi \in (0, 1)$, for every $m_{0} \ge 0$, at every point of every local Rindler horizon (Premise \claimref{synthesis.c-loc-local-horizon-premise}), whatever the field strength there.
\end{enumerate}
Nothing here uses the field equations, vanishing expansion or shear, or the value of the field strength. The components in the parallel frame do not depend on the rotation gauge. Not part of this result: the agreement of the regularised restriction with the restriction defined through the characteristic-data embedding of the generator field, which the passage from the parametrix to Hadamard states in that premise uses; by the time-function dependence above, that agreement can hold only modulo smooth kernels.

## technical
The premise (HS) was reduced, in the store, to one statement about the field: the Hadamard parametrix of the Dirac field, a fixed singular kernel built from the geometry, restricted to the light rays (generators) of a horizon through a point, should differ from the null vacuum by something less singular under scaling along the rays. The coefficient of the leading singularity was known to be the null vacuum's; what was open was whether the remaining terms are less singular, and whether certain logarithmically divergent terms, one of them proportional to the expansion of the rays, cancel. This result settles both for every gravitational field, on every piece of a null hypersurface generated by affine null geodesics whose distinct rays are spacelike separated (every small enough piece, every local Rindler horizon), for every mass, with the restriction defined by the standard regularisation of the singular kernel and transverse smearing. Expanding the projected kernel in the transverse separation of the rays, nothing is more singular than the inverse square of that separation; the logarithmic divergence is the angular mean of that part, and it splits into a derivative along the ray, a spin-connection term carrying the expansion only, and a transport term that is a total transverse derivative and contributes nothing. By the stored identity relating the Van Vleck determinant to the transverse Hessian and the area density, the first two cancel exactly, so there is no logarithm at all. The rest is bounded: the restricted parametrix is the null vacuum plus a bounded kernel, which scales away faster than any positive power. The premise's bound therefore holds, with room to spare. The regularised restriction depends on the chosen time function only through a smooth kernel, which the bound does not see. What remains for the passage from the parametrix to states is the identification of the regularised restriction used here with the restriction defined through the characteristic data of the field on the hypersurface.

## lay
The series needs every reasonable quantum state of the electron field to look like empty space along the light rays of the small horizons used to derive the equations of gravity, when looked at closely enough. The question had been reduced to a statement about gravity's geometry alone: a fixed mathematical object, which carries the short-distance behaviour shared by all reasonable states, should look like that of empty space along those light rays, up to corrections that fade at short distances. The strongest part had been checked before; two weaker pieces, which separately would grow without limit, were expected but not shown to cancel. This result shows that they do cancel exactly, on small enough pieces of the light sheets of every gravitational field (including the small horizons the series uses) and for every mass of the field, and that everything left over stays bounded. So the assumed statement is now proved, for the precise way the object is restricted to the light rays. One step remains before it applies to the states themselves: showing that this way of restricting agrees with the more fundamental one.

## one-liner
On every piece of a geodesic null hypersurface of a gravitational field whose distinct generators are spacelike separated (every small enough piece, every local Rindler horizon), for every mass, the Dirac Hadamard parametrix restricted to the generators in the canonical normalisation, as the $\epsilon$-regularised transverse-smeared limit, is $W_{0}\otimes\id_{K}$ plus a bounded kernel (defined for a chosen time function, modulo smooth kernels): the $\log\epsilon$ terms cancel identically (the expansion term against the projected transverse spin connection, the first-order transport entering only through a divergence), so the remainder has generator scaling degree at most $0$ and the bound posed by (HS) holds; the agreement of this regularised restriction with the characteristic-data restriction, needed for states, is not part of it.
