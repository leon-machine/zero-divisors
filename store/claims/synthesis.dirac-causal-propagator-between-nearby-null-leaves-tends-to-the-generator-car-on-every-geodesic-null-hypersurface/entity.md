---
id: synthesis.dirac-causal-propagator-between-nearby-null-leaves-tends-to-the-generator-car-on-every-geodesic-null-hypersurface
kind: claim
version: 5
title: 'The Dirac propagator tends to the generator CAR on null hypersurfaces'
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
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: unit pass, every imaginary unit resolved to the geometric-algebra unit it stands for
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: 'notation: the region of the formal renamed O (calligraphic)'
  version: 5
  source: maintainer pass 2026-11-07 (decisions, second round)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
- obj.hawking.continuum-mode-space
imported_from:
- citation: 'F. G. Friedlander, The Wave Equation on a Curved Space-Time, Cambridge University Press, Cambridge, 1975.'
  key: Friedlander1975
  locator: 'the retarded and advanced fundamental solutions of a normally hyperbolic operator in a causal domain, in four dimensions U delta(sigma) plus a smooth V times theta(sigma); imported as clause (d) of the Fact synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport'
- citation: 'C. Bar, N. Ginoux and F. Pfaffle, Wave Equations on Lorentzian Manifolds and Quantization, ESI Lectures in Mathematics and Physics, European Mathematical Society, 2007; arXiv:0806.1036.'
  key: BarGinouxPfaffle2007
  locator: 'Ch. 2 (Riesz distributions, Hadamard series and the local fundamental solutions); imported as clause (d) of the Fact synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport'
  doi: 10.4171/037
- citation: 'J. Dimock, Dirac quantum fields on a manifold, Trans. Amer. Math. Soc. 269 (1982), 133--147.'
  key: Dimock1982
  locator: 'Prop. 2.4, Sec. III, Thm. 3.1 (the causal propagator as the kernel of the conserved Cauchy pairing; reproducing formula); imported as clause (b) of the Fact synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field'
  doi: 10.1090/S0002-9947-1982-0637032-8
- citation: 'L. Hormander, The Analysis of Linear Partial Differential Operators I, Springer, Berlin, 1983.'
  key: Hormander1983
  locator: 'Thm. 8.2.4 (pullback of distributions); cited from memory'
- citation: 'L. Hormander, The Analysis of Linear Partial Differential Operators III, Springer, Berlin, 1985.'
  key: Hormander1985
  locator: 'Appendix C (the Morse lemma with parameters); cited from memory, lemma number not checked'
derivations:
- name: main
  uses:
  - synthesis.imported-gtg-dictionary@2
  - synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field@3
  - synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport@5
  - synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard@3
  - synthesis.imported-microlocal-hadamard-condition@2
  - synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces@5
  - synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes@5
  - synthesis.dirac-states-restrict-to-null-hypersurfaces-through-the-flux-contraction-and-are-thin-layer-limits-under-the-generator-car@4
  - synthesis.restricted-dirac-hadamard-parametrix-on-a-null-hypersurface-is-the-null-vacuum-plus-a-bounded-kernel@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_projector_algebra_of_the_null_trace
- kind: check
  ref: check.py::check_step_coefficient_formula_on_generic_jets
- kind: check
  ref: check.py::check_step_coefficient_vanishes_on_the_plane_wave_field
- kind: check
  ref: check.py::check_step_coefficient_vanishes_on_a_flat_cubic_null_hypersurface
- kind: check
  ref: check.py::check_layer_displacement_and_coincidence_coefficient
- kind: check
  ref: check.py::check_layer_wightman_term_has_one_i0_for_both_leaf_sides
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.hadamard-scaling-limit-premise
  - synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces
  - synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes
  - synthesis.c-loc-local-horizon-premise
extraction:
  maintainer_pass_decisions_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Notation (Leon, second round, answer 8; DECISIONS H5, consistency-R01 item 5): the formal named the globally hyperbolic region U, and the proof uses U for the leading Hadamard coefficient Delta^{1/2} R. The region is now \mathcal{O}, unused in the entity (O alone is the order symbol); U stays the Hadamard coefficient, as in the Fact it imports. No content change.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: synthesis.imported-gtg-dictionary repinned 1 -> 2 after reviewing its correction of the component reading in clause (iv) to R(g_mu ^ g_nu) = -R(e_mu ^ e_nu), agreeing with the store''s sign R(B) = -R(hb(B)) the clause already stated, with GA wording in (ii) and (iv); the translation rules are unchanged; the use here holds as cited.'
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. The regulator sigma + I_4 epsilon(t(x) - t(x)) of the bulk kernels and the I_4 0 sgn v it carries through the Morse-coordinate computation of the layer kernel (the Sokhotski-type integrals (s - t -+ I_4 0)^{-1}, the logarithms log(s -+ I_4 0), the pole term) are written in scalar form with the field unit (U3 scalar form of an infinitesimal shift of the separation, citing std-algebra.complexification-is-the-odd-extension(iii); U1, the Hadamard chain), the unit the layer limit and the null vacuum already carry, numbers acting on the right as stated. No i remains; declaration removed. Mathematics, links and checks unchanged.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By Leon''s ruling R2 (7 November 2026) the Hadamard chain carries the field theory''s unit I_4: the null vacuum W_0 = (I_4/2 pi)(u - u'' + I_4 0)^{-1} and its i0 in the layer limit, the right unit of the conventions, the jump -2 pi I_4 delta(u - u''), the coefficient (I_4/2 pi)Lambda and the logarithm log(I_4 s) of the restriction, numbers read in span{1, I_4}. Stays: the regulator sigma + i epsilon(t(x) - t(x'')) and the i0 sgn v it carries through the Morse-coordinate computation and onto the light cone (a shift of the spacetime separation); declared complex-analysis.'
  open_problem: op.qft-on-gtg-fields
  note: >-
    Bears on the passage from the premise (HS), synthesis.hadamard-scaling-limit-premise (version 3), to states.
    The restriction of the Dirac field to the generators of a null hypersurface through the flux trace needs the
    generator anticommutation relations (the trace isometric), which were known for light cones and flat null
    planes and otherwise cited. Here they are derived on every geodesic null hypersurface by a local computation
    on the causal propagator, which is state independent and supported on the causal set. For a source on a
    nearby leaf H_v of a null foliation (v not zero) the propagator pulls back to H x H_v; the transverse
    integral of its delta(sigma) and delta'(sigma) terms is done exactly by the Morse lemma with parameters,
    and gives a delta(u - u') term fixed by coincidence data alone (exactly Lambda) plus a step term whose
    coefficient is a(u')(d_u + theta/2)(Delta^(1/2)/sqrt(det M)) Lambda, zero by the stored identity
    Delta^(1/2)/sqrt(det M) = (a a')^(-1/2) and the half-density law; the tail, curvature and mass terms vanish in
    the limit because Lambda k = 0. With the flux contraction of the conserved current (synthesis.dirac-states-restrict-to-null-hypersurfaces-through-the-flux-contraction-and-are-thin-layer-limits-under-the-generator-car, (i)), this
    makes the flux trace isometric. A second argument, from causality and the flux contraction, shows that the
    restricted anticommutator is a multiplication operator, so the step term had to vanish: given the jet
    computation of the step coefficient, it recovers the stored identity from its coincidence value. A third
    route, the jump relation of the retarded and advanced solutions across the leaf, gives the same limit (argued). The same Morse data give the one-sided thin-layer limit of the Hadamard
    parametrix: the i0 is the same from both sides of the leaf (the sign of the regulator and of v change
    together), the log coefficient is the same combination as the step coefficient (zero), and the result is
    the null vacuum plus a bounded kernel, independent of the time function. The premise (HS) is posed on the
    epsilon-regularised restriction; this result gives the generator anticommutation relations and the flux-trace
    (thin-layer) restriction, and reaches (HS) as posed only together with the bound on the epsilon-regularised
    restriction (synthesis.restricted-dirac-hadamard-parametrix-on-a-null-hypersurface-is-the-null-vacuum-plus-a-bounded-kernel). (HS) has since been retired to a theorem (synthesis.hadamard-scaling-limit-premise,
    version 4), which assembles this result with that bound and the flux-contraction result. Transport-absent.
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, at Leon''s decisions of 2 November 2026 (Hadamard scaling bound): uses edges added to the flux-contraction result (version 2) and the bound result (version 1), now both stored, and the plain mentions of them replaced by references; (ii) and (iii)(b) now rest on the stored flux contraction instead of stating it as a condition; the form of the fundamental solutions and the reproducing formula, cited from memory in version 1, are the imported parametrix Fact (d) and Dimock Fact (b) at version 2; (HS) is cited as the theorem it has become; the null-singularity result and the flat null-plane result repinned at their version 3 (notes and wording only). The derivation and checks are unchanged.'
  flags:
  - 'the retarded and advanced fundamental solutions of the squared Dirac operator in the form (1/4 pi) theta(+-(t - t'')) (U delta(sigma) + V theta(sigma)) with V smooth on a causal domain are clause (d) of the parametrix Fact (version 2), checked against the source for scalar and vector fields; the general bundle case there is cited from memory'
  - 'the reproducing formula of the causal propagator (the Dimock pairing as the conserved Cauchy inner product) is clause (b) of the Dimock Fact (version 2)'
  - '(ii) and the state part of (iii) use the flux contraction (i) and the thin-layer limits (iii-a) of synthesis.dirac-states-restrict-to-null-hypersurfaces-through-the-flux-contraction-and-are-thin-layer-limits-under-the-generator-car; (i) and (iii)(a) do not'
  - 'that the epsilon-regularised restriction of (HS) differs from the flux-trace restriction by a bounded kernel rests on the bound synthesis.restricted-dirac-hadamard-parametrix-on-a-null-hypersurface-is-the-null-vacuum-plus-a-bounded-kernel together with (iii)(a); that kernel contains a smooth term depending on the time function'
  - 'the jump-relation route in the proof is argued: it assumes conormal regularity of the retarded and advanced solutions up to the leaf, uniformly in v'
  - 'the existence of a local null foliation containing a given small piece of a geodesic null hypersurface (null hypersurfaces orthogonal to a family of parallel two-surfaces) is standard, cited from memory'
---

## formal
Units $\hbar = c = 1$. Let $(\hb, \Omega)$ be a gravitational field on four-dimensional flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric $g$ is smooth and globally hyperbolic on a region $\mathcal{O}$ of its invertible region (Fact \claimref{synthesis.imported-gtg-dictionary}), $N \subset \mathcal{O}$ geodesically and causally convex, and $\psi$ the free Dirac field of mass $m_{0} \ge 0$ on it (Fact \claimref{synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field}) with causal propagator $S$, normalised by the reproducing formula $\Phi(x) = \int_{\Sigma}S(x, x')\,n(x')\Phi(x')\,d\Sigma'$ on a Cauchy surface (Fact \claimref{synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field}(b), \cite{Dimock1982}). Let $\mathcal{H} \subset N$ be a piece of a null hypersurface generated by affinely parametrised null geodesics $u \mapsto X(u, y)$, with the notation of Theorem \claimref{synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces} ($k$, the parallel null frame, $\Lambda = \tfrac12 nk$, $J$, $a = |\det J|$, $\theta = \mathrm{tr}\,J'J^{-1}$, $M(u, u')$, $\Delta$), small enough that (S) points of distinct generators are spacelike separated. Let $\{\mathcal{H}_{v}\}_{|v| < v_{1}}$, $\mathcal{H}_{0} = \mathcal{H}$, be a smooth local foliation by null hypersurfaces of the same kind, $X_{v}(u, y)$ their affinely parametrised generators, smooth in $(u, v, y)$, with tangents $k_{v}$, area densities $a_{v}$, the foliation function increasing to the future along causal curves, and $\ell = \partial_{v}X_{v}$ ($k\cdot\ell > 0$). For a smooth compactly supported $\Psi$ of the labels with $\Lambda\Psi = \Psi$ and $v \neq 0$, let
\[
\Phi^{\Psi}_{v}(x) = \int S\bigl(x, X_{v}(u', y')\bigr)\,k_{v}\,\Psi(u', y')\,a_{v}\,du'\,d^{2}y'
\]
be the solution radiated by the null data $\Psi$ on $\mathcal{H}_{v}$ (labels and spin frames of the leaves identified with those of $\mathcal{H}$ along $\ell$).
\begin{enumerate}
\item[(i)] \emph{(The restricted causal propagator; proved, given the imported form of the retarded and advanced fundamental solutions, Fact \claimref{synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport}(d).)} For $v \neq 0$ the pullback of $S$ to $\mathcal{H}\times\mathcal{H}_{v}$ is defined and $\Lambda\Phi^{\Psi}_{v}$ is smooth on $\mathcal{H}$. As $v \to 0$ from either side, $\Lambda\Phi^{\Psi}_{v}(X(u, y)) \to \Psi(u, y)$ as distributions, for every $m_{0} \ge 0$: the restricted causal propagator tends to $\delta(u - u')\,\delta^{2}(y - y')\,\Lambda$. After the transverse integral (Morse lemma with parameters) it is $\theta(\sigma_{*})\,c_{v} + \delta(\sigma_{*})\,d_{v}$ plus terms that vanish in the limit, $\sigma_{*} = v\,\tilde b(u, u')$ the critical value of $\sigma$ in the label difference, $\tilde b = (u' - u)(k\cdot\ell) + O(v)$. The $\delta(u - u')$ coefficient is fixed by coincidence data ($\Delta = 1$, $R = 1$, transverse Hessian $\bar JJ$) and is exactly $\Lambda$; the step coefficient is
\[
c_{0}(u, u') = -\mathrm{sgn}(v)\,a(u')\Bigl(\partial_{u} + \tfrac12\theta(u)\Bigr)\frac{\Delta^{1/2}}{\sqrt{\det M}}(u, u')\;\Lambda ,
\]
the derivative along the generator, the projected transverse connection (expansion only) and the first-order transport (which drops out) as in the log coefficient of the restricted parametrix; it vanishes because $\Delta^{1/2}/\sqrt{\det M} = (a(u)a(u'))^{-1/2}$ and $\theta = a'/a$ (the half-density law). The tail $V\theta(\sigma)$, the curvature terms and the mass term vanish in the limit ($\Lambda k = 0$).
\item[(ii)] \emph{(The generator anticommutation relations; proved, with the flux contraction.)} The flux traces $T_{v}^{*}\Phi = \sqrt{2a_{v}}\,\Lambda\Phi|_{\mathcal{H}_{v}}$ (canonical normalisation) extend to contractions, the flux of the future-causal Dirac current through a null piece being at most the norm (the flux contraction, Theorem \claimref{synthesis.dirac-states-restrict-to-null-hypersurfaces-through-the-flux-contraction-and-are-thin-layer-limits-under-the-generator-car}(i)), and $T^{*}T = 1$ on $L^{2}(\mathcal{H}_{c})$ for every compact $\mathcal{H}_{c}$ in the piece: $\{\psi_{\mathcal{H}}(u, y), \psi_{\mathcal{H}}(u', y')^{*}\} = \delta(u - u')\,\delta^{2}(y - y')\,\Lambda$, on every geodesic null hypersurface (small pieces), local Rindler horizons through $x_{0}$ of Premise \claimref{synthesis.c-loc-local-horizon-premise} included, whatever the field strength, expansion or shear. Independently of the vanishing of the step coefficient, causality (finite propagation speed, the foliation function monotone along causal curves) together with the flux contraction makes $T^{*}T$ a multiplication operator $0 \le m \le 1$; with the coincidence coefficient $m = 1$, and the step coefficient is forced to vanish, which, given the jet formula of (i) for that coefficient, returns the identity $\Delta^{1/2}/\sqrt{\det M} = (a a')^{-1/2}$ from its coincidence value.
\item[(iii)] \emph{(The thin-layer restricted parametrix.)} (a) (Proved.) For the Dirac Hadamard parametrix $G^{+}_{\mathrm{par}}$ (Facts \claimref{synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport}, \claimref{synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard}(a)), normalised so that $G^{+}_{\mathrm{par}} + G^{-}_{\mathrm{par}} = S$ modulo smooth kernels, the same pullback between $\mathcal{H}$ and $\mathcal{H}_{v}$ in the canonical normalisation has, as $v \to 0$ from either side, the limit $W_{0}\otimes\id_{K} + r$, $W_{0} = \tfrac{I_{4}}{2\pi}(u - u' + I_{4}0)^{-1}$ (the field theory's unit $I_{4}$; numbers are read in $\mathrm{span}\{1, I_{4}\}$), where for each pair of transverse profiles $r(u, u')$ is a bounded function of $(u, u')$, bounded uniformly for profiles bounded in $C^{4}$ with support in a fixed compact set: the $I_{4}0$ is the same from both sides (with the regulator $\sigma + I_{4}\epsilon(t(x) - t(x'))$ of the ordering $\omega(\psi^{*}(x')\psi(x))$, its sign at the light cone is $-\mathrm{sgn}(v)$, and $\sigma_{*}$ carries the factor $v$), the coefficient of $\log|v|$ is the same combination of jets as the step coefficient of (i), hence zero, and the limit does not depend on the time function. (b) (Proved, with the flux contraction and the thin-layer limits of Theorem \claimref{synthesis.dirac-states-restrict-to-null-hypersurfaces-through-the-flux-contraction-and-are-thin-layer-limits-under-the-generator-car}(i), (iii-a).) For every gauge-invariant quasi-free Hadamard state $\omega$, the restricted two-point function through the flux trace is $W_{0}\otimes\id_{K} + r + D_{0,0}$, $D_{0,0}$ smooth; so the restriction through the flux trace has generator scaling degree below one after subtracting $W_{0}\otimes\id_{K}$, with any $\varpi \in (0, 1)$, at every point of every local Rindler horizon, which is clause (b) of Theorem \claimref{synthesis.hadamard-scaling-limit-premise} for the flux-trace restriction. Its statement on the $\epsilon$-regularised restriction is Theorem \claimref{synthesis.restricted-dirac-hadamard-parametrix-on-a-null-hypersurface-is-the-null-vacuum-plus-a-bounded-kernel}(iii); with that bound, the $\epsilon$-regularised restriction differs from the flux-trace restriction by a bounded kernel, which contains a smooth term depending on the time function, nonzero for time functions whose derivative along $k$ varies along the generators; the two do not agree identically.
\end{enumerate}
Nothing here uses the field equations or the value of the field strength.

## technical
The light-ray (generator) field of the Dirac field on a null hypersurface is defined through the flux of the conserved current, and the earlier results needed the canonical anticommutation relations of that field, which were a theorem only for light cones and flat null planes. This result derives them on every null hypersurface generated by geodesics, in particular on the local horizons used for the thermodynamic derivation of gravity, by a local computation. The tool is the causal propagator, which is the same for every state and vanishes between spacelike separated points. A source placed on a nearby null sheet of a foliation radiates a solution that is smooth on the original sheet, and its trace there can be computed exactly from the known form of the propagator near the light cone: a delta function on the light cone with the Van Vleck root and the spin transport as coefficient, plus a smooth tail inside the cone. Integrating over the transverse directions leaves two terms as the sheets approach each other: a delta function along the light rays, whose coefficient is fixed at coincidence and equals the canonical one, and a step function, whose coefficient is the derivative along the rays of the Van Vleck root divided by the transverse Hessian, corrected by half the expansion. By the stored identity relating these to the area density, that coefficient is zero: the light-ray field is a half-density. The tail and the mass drop out. A second argument, from causality and the flux contraction, shows the step had to vanish, and with the computed form of the step coefficient gives the stored identity back. The same computation, applied to the Hadamard parametrix, shows that its restriction defined by thin layers is the null vacuum plus a bounded kernel, with no logarithm and with the same sign of the regulator from both sides. With the flux contraction and the thin-layer limits of the flux-contraction result, the restriction through the flux trace of every gauge-invariant quasi-free Hadamard state is then the null vacuum plus a bounded and a smooth kernel, which is what (HS) is used for. (HS) on the epsilon-regularised restriction needs in addition the bound on that restriction (the bound result); with both, (HS) is now a theorem. The result is transport-absent.

## lay
Earlier work needed a basic rule for the electron field seen only along the light rays of a small horizon: the field there should obey the standard rules for fermions, exactly as in empty space. Mathematicians had proved this for light cones; for the general light sheets used in the series it was only believed. This result proves it for every such sheet by a short calculation with the one object every state shares, the propagator that carries signals at or below light speed. Two corrections that could have spoiled the rule turn out to cancel, because the area of the sheet and the focusing of light rays are tied together. Together with two companion results, it also shows that every reasonable state looks like empty space along these light rays at short distances.

## one-liner
On every geodesic null hypersurface the Dirac causal propagator, restricted between the hypersurface and a nearby leaf of a null foliation, tends to $\delta(u - u')\delta^{2}(y - y')\Lambda$: the delta coefficient comes from coincidence data, the step coefficient $a(u')(\partial_{u} + \theta/2)(\Delta^{1/2}/\sqrt{\det M})\Lambda$ vanishes by the half-density law, and tail and mass terms drop (proved). Since the flux trace is a contraction (the flux-contraction result), the generator anticommutation relations hold there, local Rindler horizons included, and the thin-layer restricted Hadamard parametrix is the null vacuum plus a bounded kernel, so, with the thin-layer limits of that result, the restriction through the flux trace of every gauge-invariant quasi-free Hadamard state is the null vacuum plus a bounded and a smooth kernel, which is what (HS) is used for; for (HS) on the epsilon-regularised restriction the bound on that restriction (the bound result) is used in addition.
