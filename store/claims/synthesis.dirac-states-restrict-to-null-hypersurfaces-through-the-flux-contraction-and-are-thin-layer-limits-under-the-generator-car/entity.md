---
id: synthesis.dirac-states-restrict-to-null-hypersurfaces-through-the-flux-contraction-and-are-thin-layer-limits-under-the-generator-car
kind: claim
version: 3
title: 'Dirac states restrict to null hypersurfaces through the flux contraction'
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
review: draft
outside_ga:
  kind: complex-analysis
  why: 'i stays only in the i epsilon regulator of the bulk parametrix, sigma + i epsilon s with s from a time function, and the i0 it produces (a shift of the spacetime separation along the time direction, which no pseudoscalar commuting with the vectors can replace), and in the Kay-Wald form (U_1 - U_2 - i epsilon)^{-2} quoted from the literature; the null-side kernels carry I_4'
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
- obj.hawking.continuum-mode-space
imported_from:
- citation: 'D. Häfner and J.-P. Nicolas, The characteristic Cauchy problem for Dirac fields on curved backgrounds, J. Hyperbolic Differ. Equ. 8 (2011), 437--483; arXiv:0903.0515.'
  key: HafnerNicolas2011
  locator: 'Abstract; Sec. 4.1 (Def. 4.2, Eq. (14), Thm. 1); Sec. 4.4 (Thm. 2); Sec. 4.5 (hypotheses and Prop. 4.13 seen, Thm. 3 not read)'
- citation: 'B. S. Kay and R. M. Wald, Theorems on the uniqueness and thermal properties of stationary, nonsingular, quasifree states on spacetimes with a bifurcate Killing horizon, Phys. Rep. 207 (1991), 49--136.'
  key: KayWald1991
- citation: 'C. Dappiaggi, V. Moretti and N. Pinamonti, Rigorous construction and Hadamard property of the Unruh state in Schwarzschild spacetime, arXiv:0907.1034.'
  key: DappiaggiMorettiPinamonti2009
  locator: 'Sec. 3.2; Sec. 2.4, Thm. 2.1'
- citation: 'K. Sanders, On the construction of Hartle-Hawking-Israel states across a static bifurcate Killing horizon, arXiv:1310.5537.'
  key: Sanders2013
  locator: 'Sec. 1'
- citation: 'C. Gérard and M. Wrochna, Construction of Hadamard states by characteristic Cauchy problem, Anal. PDE 9 (2016), 111--149; arXiv:1409.6691.'
  key: GerardWrochna2016
  doi: 10.2140/apde.2016.9.111
derivations:
- name: main
  uses:
  - synthesis.imported-gtg-dictionary@1
  - synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field@2
  - synthesis.imported-microlocal-hadamard-condition@2
  - synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard@2
  - synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport@2
  - synthesis.imported-haefner-nicolas-dirac-characteristic-problem-on-light-cones-near-the-vertex@1
  - synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces@3
  - synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes@3
  - synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_dirac_current_is_future_causal_and_its_null_flux_is_canonical
- kind: check
  ref: check.py::check_generator_scaling_is_conjugation_by_a_unitary_dilation
- kind: check
  ref: check.py::check_thin_layers_on_the_flat_null_plane_converge_to_the_generator_car
- kind: check
  ref: check.py::check_regulator_direction_drops_out_of_the_null_singularity_coefficient
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.hadamard-scaling-limit-premise
  - synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces
  - synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes
  - synthesis.c-loc-local-horizon-premise
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By Leon''s ruling R2 (7 November 2026) the null-side kernels of the Hadamard chain carry the field theory''s unit I_4: (u - u'' + I_4 0)^{-1}, numbers read in span{1, I_4}. Stays: the i epsilon regulator of a time function and its i0 (a shift of the spacetime separation), and the Kay-Wald form (U_1 - U_2 - i epsilon)^{-2} quoted from the literature; declared complex-analysis.'
  open_problem: op.qft-on-gtg-fields
  note: >-
    Bears on the passage from the premise (HS), synthesis.hadamard-scaling-limit-premise (version 3), to
    states. (HS) poses its bound on the restricted Dirac parametrix computed as the epsilon -> 0 limit of the
    transverse-smeared, i0-regularised kernel, while the restricted state of a Hadamard state is defined
    through the characteristic-data embedding psi_H(F) = psi(Phi_F), cited from memory in the stored result
    synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces.
    Answer, in three parts. First, unconditionally: the Dirac current is future causal, so the flux of a solution
    through a piece of a null hypersurface is at most its norm (the standard energy inequality, re-derived in the
    store's normalisation); the trace iota_H* is a contraction, its adjoint defines psi_H(F) = psi(iota_H F), every
    state restricts to positive contractions with W+ + W- = iota_H* iota_H <= 1 exactly, and the generator scaling is
    a unitary dilation, so restricted kernels always have generator scaling degree at most one. Thin-layer solutions
    converge weakly to the embedded ones, and iterated limits of the bounded, locally smooth difference of two
    Hadamard two-point forms give the pullback of that difference: restricted kernels of Hadamard states differ by
    smooth pullbacks, and W^par_H := W_{H,omega} - D_{0,0} is the same for every Hadamard state. This makes (iii) of
    the stored null-singularity result unconditional. Second, if the generator CAR holds on the leaves of a null
    foliation ((Iso): the characteristic Cauchy problem with norm equal to data norm), thin-layer solutions converge
    in norm, the restricted state is the joint thin-layer limit of the bulk two-point function, and W^par_H is the
    thin-layer limit of the parametrix, a regularisation-free definition. (Iso) is proved for light cones by Haefner
    and Nicolas (2011) and holds on flat null planes; for local Rindler horizons it is cited from memory. Third,
    argued: the agreement of this W^par_H with the regularised one of (HS). The projector identity
    Lambda p e0 Lambda (k.e0) = (p.k) Lambda is exact for every regulator direction p (the stored flat-plane identity
    at k.e0 = 1), but the thin-layer displacement is real and the sign of its i0 depends on sgn(v - v'), so the
    coefficient matching across the two readings is argued, as is the cancellation of the log(epsilon) terms given
    (Iso). See synthesis.restricted-dirac-hadamard-parametrix-on-a-null-hypersurface-is-the-null-vacuum-plus-a-bounded-kernel
    (the remainder bound on the regularised restriction); the combined chain is (i) + (iii-a) + that bound + (v), with (v)
    the remaining argued step.
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, at Leon''s decisions of 2 November 2026 (Hadamard scaling bound): a marked note records that the hypothesis (Iso) of (iii-b) is discharged on geodesic null hypersurfaces by (ii) of the generator-CAR result (synthesis.dirac-causal-propagator-between-nearby-null-leaves-tends-to-the-generator-car-on-every-geodesic-null-hypersurface), cited in text only (no uses edge: that result uses this one), and that (v) is settled to a bounded kernel there; uses edges to the new Fact on the Dirac characteristic problem on light cones (Haefner and Nicolas) and to the Dimock Fact at version 2 (the reproducing formula, now clause (b)) replace citations from memory; the parametrix Fact repinned at version 2, and the null-singularity, flat null-plane and microlocal-generator results at their current versions (notes and wording only). What the result asserts is unchanged.'
  flags:
  - 'the identification of the Dimock anticommutator pairing with the conserved Cauchy inner product of the solutions is clause (b) of the Dimock Fact (version 2)'
  - '(Iso), the generator CAR on the leaves, is proved for light cones in Haefner and Nicolas (2011), Theorems 1 and 2, on the part of the cone in D_T inside a geodesically convex neighbourhood of the vertex (now the Fact synthesis.imported-haefner-nicolas-dirac-characteristic-problem-on-light-cones-near-the-vertex); on every small piece of a geodesic null hypersurface, local Rindler horizons included, it is (ii) of the generator-CAR result synthesis.dirac-causal-propagator-between-nearby-null-leaves-tends-to-the-generator-car-on-every-geodesic-null-hypersurface (marked note; text citation, no uses edge); (iii-b) keeps it as its stated hypothesis'
  - 'Kay and Wald (1991) is read through the account of Dappiaggi, Moretti and Pinamonti (arXiv:0907.1034, Sec. 3.2) and Sanders (arXiv:1310.5537, Sec. 1), not against the original'
  - '(v) is argued: only the projector identity and W+ + W- = iota_H* iota_H are exact; the coefficient matching across a complex time-function regulator and a real layer displacement (whose i0 sign depends on sgn(v - v'')), and the cancellation of the log(epsilon) terms given (Iso), are argued'
---

## formal
Units $\hbar = c = 1$. Let $(\hb, \Omega)$ be a gravitational field on four-dimensional flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric $g$ is smooth and globally hyperbolic on a region $U$ of its invertible region (Fact \claimref{synthesis.imported-gtg-dictionary}), and $\psi$ the free Dirac field of mass $m_{0} \ge 0$ on it (Fact \claimref{synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field}): $\mathcal{K}$ is the completion of the solutions with compactly supported Cauchy data in the norm $\|\Phi\|^{2}$, the flux of the Dirac current $J_{\Phi} = \Phi e_{0}\tilde\Phi$ through a Cauchy surface, and $\psi(\Phi)$ the field of a solution, $\{\psi(\Phi), \psi(\Phi')^{*}\} = (\Phi, \Phi')$ (the anticommutator pairing of the Fact, which is this inner product by its clause (b), Dimock's reproducing formula). Let $\mathcal{H} \subset U$ be a null hypersurface generated by affinely parametrised null geodesics $u \mapsto X(u, y)$, considered on a geodesically and causally convex neighbourhood $N$ in which it is achronal, with the canonical projector $\Lambda$, area density $a$ and canonical generator field $\sqrt{2a}\,\Lambda\psi$ of Theorem \claimref{synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces}, labels as multiplicity space $K = L^{2}(\R^{2}, d^{2}y)\otimes V_{\Lambda}$; let $\mathcal{H}_{c} \subset \mathcal{H}\cap N$ be compact and $L^{2}(\mathcal{H}_{c}) = L^{2}(du\,d^{2}y)\otimes V_{\Lambda}$ over it. For (iii) assume, as in that theorem, that gauge-invariant quasi-free Hadamard states of the Dirac field exist on $U$.
\begin{enumerate}
\item[(i)] \emph{(The flux contraction; proved.)} For every smooth solution $\Phi$ with compactly supported Cauchy data, $\int_{\mathcal{H}_{c}} 2a\,|\Lambda\Phi|^{2}\,du\,d^{2}y \le \|\Phi\|^{2}$ (the standard energy inequality for a conserved causal current, as in Fact \claimref{synthesis.imported-haefner-nicolas-dirac-characteristic-problem-on-light-cones-near-the-vertex}(a) (\cite{HafnerNicolas2011}, Eq.~(14)) and Hörmander's energy method, re-derived in the store's normalisation). So the trace $\iota_{\mathcal{H}}^{*}\Phi = \sqrt{2a}\,\Lambda\Phi|_{\mathcal{H}_{c}}$ extends to a contraction $\iota_{\mathcal{H}}^{*}: \mathcal{K} \to L^{2}(\mathcal{H}_{c})$, and with its adjoint $\iota_{\mathcal{H}}$ the generator field smeared with $F$ is $\psi_{\mathcal{H}}(F) = \psi(\iota_{\mathcal{H}}F)$: the characteristic-data embedding exists, with $\Phi_{F} = \iota_{\mathcal{H}}F$, $\|\psi_{\mathcal{H}}(F)\| \le \|F\|$ and $\{\psi_{\mathcal{H}}(F), \psi_{\mathcal{H}}(G)^{*}\} = \langle F, \iota_{\mathcal{H}}^{*}\iota_{\mathcal{H}}G\rangle$, $0 \le \iota_{\mathcal{H}}^{*}\iota_{\mathcal{H}} \le 1$. For every state $\omega$ of the field (Hadamard or not) the two restricted two-point functions are bounded positive operators $W^{\pm}_{\mathcal{H},\omega}$ on $L^{2}(\mathcal{H}_{c})$, and exactly $W^{+}_{\mathcal{H},\omega} + W^{-}_{\mathcal{H},\omega} = \iota_{\mathcal{H}}^{*}\iota_{\mathcal{H}} \le 1$. No characteristic Cauchy problem is used.
\item[(ii)] \emph{(Generator scaling degree at most one; proved.)} For every state, every interior $u_{0}$ and transverse profiles $f, g$, the scaled kernels $\lambda W^{\pm}_{\mathcal{H},\omega}(u_{0} + \lambda x, u_{0} + \lambda x')$ in the $(f, g)$ component are the unscaled ones conjugated by a unitary dilation, of norm at most $\|f\|\,\|g\|$ for all $\lambda$: $\lambda^{\varpi}W^{\pm}_{\mathcal{H},\omega}(u_{0} + \lambda\cdot, u_{0} + \lambda\cdot) \to 0$ for $\varpi > 1$, and the scaling limit points exist and are positive contractions. So $R^{\mathrm{par}}$ of Premise \claimref{synthesis.hadamard-scaling-limit-premise}, for a restricted parametrix that agrees with the restricted state up to a smooth pullback, always has generator scaling degree at most one; the premise asks for below one.
\item[(iii-a)] \emph{(Hadamard states differ by smooth pullbacks; proved, unconditional.)} Let $\{\mathcal{H}_{v}\}_{|v| < v_{1}}$ be a smooth family of null hypersurfaces of the same kind foliating a neighbourhood of $\mathcal{H}_{c}$ in $N$, $\mathcal{H}_{0} = \mathcal{H}$, with contractions $\iota_{v}$ as in (i), and $f_{n} = \int\rho_{n}(v)\,\delta_{\mathcal{H}_{v}}\otimes F_{v}\,dv$ thin-layer test spinors ($\rho_{n} \ge 0$ smooth, $\int\rho_{n} = 1$, supports shrinking to $\{0\}$, $F_{v}$ smooth in $v$, $F_{0} = F$). Then the bulk solutions $Sf_{n}$ converge weakly to $\iota_{\mathcal{H}}F$, with no further hypothesis. For two gauge-invariant quasi-free Hadamard states the difference of their two-point forms is bounded on $\mathcal{K}$ and a smooth kernel $D$ near $\mathcal{H}_{c}$ (Facts \claimref{synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard}(a), \claimref{synthesis.imported-microlocal-hadamard-condition}(b)), and its iterated thin-layer limits give $W^{\pm}_{\mathcal{H},\omega_{1}} - W^{\pm}_{\mathcal{H},\omega_{2}} = D_{0,0}$, the compressed, canonically normalised pullback of $D$, smooth. So $W^{\mathrm{par}}_{\mathcal{H}} := W_{\mathcal{H},\omega} - D^{\omega}_{0,0}$, with $D^{\omega}$ the smooth part of $\omega$'s kernel beyond the Dirac parametrix $G_{\mathrm{par}}$ (Fact \claimref{synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport}), is well defined and the same for every such state. This makes (iii) of Theorem \claimref{synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces} unconditional: the embedding it cites from memory is (i), and its smooth-difference statement is this clause.
\item[(iii-b)] \emph{(Thin layers, if the generator CAR holds; proved given (Iso).)} Assume \emph{(Iso)}: each $\iota_{v}$ is isometric on data supported in a fixed compact set (the generator CAR on $\mathcal{H}_{v}$). Then $Sf_{n} \to \iota_{\mathcal{H}}F$ in norm, so for every state $\omega$ the restricted two-point functions are the joint thin-layer limits of the bulk ones, $W^{\pm}_{\mathcal{H},\omega}(F, G) = \lim_{n}W^{\pm}_{\omega}(f_{n}, g_{n})$; the restricted parametrix of (iii-a) is $W^{\mathrm{par}}_{\mathcal{H}}(F, G) = \lim_{n}G_{\mathrm{par}}(f_{n}, g_{n})$, a regularisation-free definition independent of the foliation and the layers; and $W^{+}_{\mathcal{H},\omega} + W^{-}_{\mathcal{H},\omega} = 1$, so the sum of the two orderings of $R^{\mathrm{par}}$ is a smooth pullback.
\item[(iv)] \emph{(Where (Iso) holds.)} On the future light cone of a point $p_{0}$, on its part in $D_{T} = J^{+}(p_{0})\cap\{0 \le t \le T\}$ inside a geodesically convex, globally hyperbolic neighbourhood of $p_{0}$, and on foliations by such cones, (Iso) holds: the trace onto the transverse components on the cone is an $L^{2}$ isometry with dense range (Fact \claimref{synthesis.imported-haefner-nicolas-dirac-characteristic-problem-on-light-cones-near-the-vertex}(b), (c); \cite{HafnerNicolas2011}, Theorems 1 and 2). On flat null planes, for every mass, it is the generator CAR of Theorem \claimref{synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes}(i), and the thin-layer limit of the compressed anticommutator reproduces it for every positive approximate identity. On other null hypersurfaces, local Rindler horizons included, (Iso) is the characteristic Cauchy problem for Dirac data on a general null hypersurface (cited from memory; a route is to embed $\mathcal{H}_{c}$ in an achronal Lipschitz weakly spacelike Cauchy hypersurface and use \cite{HafnerNicolas2011}, Sec.~4.5, after localisation to a spatially compact field, not read); there (iii-b) is conditional on it.
\item[(v)] \emph{(The regularised restriction; argued.)} (HS) poses its bound on the restricted parametrix computed with the $i\epsilon$ regulator of a time function. Exact: for the Hermitian projector of any null $k$, $\Lambda p\,e_{0}\Lambda\,(k\cdot e_{0}) = (p\cdot k)\Lambda$ for every vector $p$ (at $k\cdot e_{0} = 1$ the identity of Theorem \claimref{synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes}(ii)), so for a complex time-function regulator the coefficient of $(u - u' + I_{4}0)^{-1}\delta^{2}(y - y')$ (the kernel's unit is the field theory's $I_{4}$, and numbers, the values of the regularised kernels included, are read in $\mathrm{span}\{1, I_{4}\}$; the regulator $i\epsilon$ shifts the time function, a shift of the spacetime separation, and keeps $i$) does not depend on the regulator direction; and $W^{+}_{\mathcal{H},\omega} + W^{-}_{\mathcal{H},\omega} = \iota_{\mathcal{H}}^{*}\iota_{\mathcal{H}}$. Argued: the thin-layer displacement is real and the sign of its $i0$ depends on $\mathrm{sgn}(v - v')$, so that the layer limit has the same coefficient is not shown; given (Iso) and this scheme comparison, the $\log\epsilon$ terms cancel, the regularised and the regularisation-free $W^{\mathrm{par}}_{\mathcal{H}}$ differ at most by bounded local terms $c(u, u')\delta^{2}(y - y')$, of generator scaling degree at most $0$, and (HS) has the same truth value with either.
\end{enumerate}
If (HS) were posed on the $W^{\mathrm{par}}_{\mathcal{H}}$ of (iii-a), its ingredient (B), the agreement of the restriction it uses with the restriction defined by the embedding, would be void. As (HS) is posed, on the regularised restriction, (B) is the scheme comparison of (v), argued; (Iso) is needed for the thin-layer reading of (iii-b) and for the generator CAR used downstream. Kay and Wald's restriction of Killing-invariant Hadamard states to bifurcate Killing horizons \cite{KayWald1991}, the closest prior art, is for the scalar field, uses the Killing invariance and the global horizon, and rests on the characteristic problem (as read through \cite{DappiaggiMorettiPinamonti2009}, \cite{Sanders2013}); Gérard and Wrochna \cite{GerardWrochna2016} construct bulk Hadamard states from boundary states on a light cone, the converse direction, for the scalar field.

\emph{Note (the hypothesis (Iso) discharged; added 2 November).} On every small piece of a geodesic null hypersurface, with a local null foliation of such pieces (local Rindler horizons through a point included), (Iso) is now a theorem: the generator anticommutation relations hold on every leaf, by (ii) of Theorem \claimref{synthesis.dirac-causal-propagator-between-nearby-null-leaves-tends-to-the-generator-car-on-every-geodesic-null-hypersurface}, which derives them from the causal propagator and the flux contraction (i) above. So there (iii-b) holds without hypothesis: the restriction of every state is the thin-layer limit of its bulk two-point functions. (Iso) stays the stated hypothesis of (iii-b) here, and that theorem is cited in this note only, not as a premise, since it uses (i) of this result. The comparison of (v) is also settled at the level of scaling degree: by (iii)(b) of that theorem with Theorem \claimref{synthesis.restricted-dirac-hadamard-parametrix-on-a-null-hypersurface-is-the-null-vacuum-plus-a-bounded-kernel}, the $\epsilon$-regularised restriction and the restriction through the flux trace differ by a bounded kernel, which contains a smooth term depending on the time function, so they do not agree identically; (v) as stated stays argued.

## technical
The premise (HS) asks about the Hadamard parametrix of the Dirac field restricted to the light rays of a local horizon, and the restriction is computed there by smearing over the transverse directions with an i0 regulator. The states of the field, on the other hand, are restricted through an embedding of the light-ray field into the field algebra, which the stored result on the leading null singularity cited from memory. This result supplies that embedding and relates the two restrictions.

The Dirac current of a solution is future causal, so the amount of it that flows through a piece of a null hypersurface can never exceed the solution's norm (the standard energy inequality, re-derived in the store's normalisation). The trace on the hypersurface is therefore a contraction, its adjoint defines the light-ray field inside the field algebra, and every state, Hadamard or not, restricts to a pair of positive operators whose sum is exactly the trace contraction's square, bounded by one (proved, with no characteristic Cauchy problem). Because scaling along the light rays is a unitary dilation, every restricted kernel has scaling degree at most one; (HS) needs strictly below one (proved). Thin layers of bulk test functions converge weakly to the light-ray field, and that is enough to show that restricted kernels of two Hadamard states differ by the pullback of the smooth difference of their bulk kernels. So the restricted parametrix, the restricted state minus that smooth pullback, is the same for every Hadamard state, and the state independence of the stored null-singularity result no longer rests on a cited embedding (proved).

If, in addition, the light-ray field obeys the canonical anticommutation relations on the nearby null hypersurfaces of a foliation (equivalently, the characteristic Cauchy problem conserves the norm), the convergence is in norm. The restricted state is then the limit of the bulk two-point function on thin layers, for every state, and the restricted parametrix then has a regularisation-free definition as the thin-layer limit of the parametrix (proved given that condition). The condition is a theorem for light cones near their vertex (Häfner and Nicolas, 2011) and holds on flat null planes; for local Rindler horizons it was the general characteristic problem, cited. (Note added later: a later result in the store derives the condition on every small piece of a null hypersurface generated by geodesics, local Rindler horizons included, from the causal propagator and the flux contraction proved here; this result keeps it as a stated condition, and the later result is cited in a note only, since it builds on this one.) The agreement of this definition with the regularised one used in (HS) is argued: the projector identity behind the coefficient of the null singularity is exact for every regulator direction, but a thin layer is a real displacement whose i0 sign depends on the order of the two layers, so the coefficient matching, and the cancellation of the logarithms given the anticommutation relations, are not shown. The result is transport-absent.

## lay
The series assumes that, seen closely along the light rays of a small horizon, quantum states of the electron field look like empty space. Testing this needs a precise way to look at a state "on the light rays only", and the earlier work borrowed one from memory. This result builds it from a basic fact: the flow of electron charge-current is never faster than light, so what flows through a sheet of light rays can never exceed the total. That alone makes every state restrict to the light rays, caps how singular the restriction can be, and shows that any two reasonable states differ there only by a smooth amount. If the light-ray field also obeys the usual rules for fermions, which mathematicians have proved for light cones but which are only believed for general light sheets, then the restriction is simply the limit of ordinary measurements made in thinner and thinner slabs, and the earlier borrowed step is no longer needed. Whether this matches the way the horizon assumption itself is computed is argued, not proved.

## one-liner
The future-causal Dirac current makes the trace on a null hypersurface a contraction, so every state of the Dirac field restricts to its generators with no characteristic Cauchy problem, as positive operators with $W^{+} + W^{-} = \iota_{\mathcal{H}}^{*}\iota_{\mathcal{H}} \le 1$ and generator scaling degree at most one, and restricted kernels of Hadamard states differ by smooth pullbacks (proved). If the generator CAR holds on nearby null hypersurfaces (a theorem for light cones near the vertex and, by a later result cited in a note, on every small piece of a geodesic null hypersurface, local Rindler horizons included), the restriction is the thin-layer limit of the bulk two-point function, and the restricted Hadamard parametrix then has a regularisation-free definition (proved given that condition), whose agreement with the regularised one used in (HS) is argued.
