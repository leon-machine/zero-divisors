---
id: synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field
kind: claim
version: 4
title: 'Hadamard Dirac states scale to the flat massless vacuum at every point'
status: proved
region: synthesis
subject: thermality
tags: [thermal-premises, horizons, car-algebra, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-02-hs-scaling
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 4
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: unit pass, every imaginary unit resolved to the geometric-algebra unit it stands for
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'H. Sahlmann and R. Verch, Microlocal spectrum condition and Hadamard form for vector-valued quantum fields in curved spacetime, Rev. Math. Phys. 13 (2001), 1203--1246; arXiv:math-ph/0008029.'
  key: SahlmannVerch2001
  locator: 'Prop. 5.6; Def. 5.3'
  doi: 10.1142/S0129055X01001010
- citation: 'K. Sanders, The locally covariant Dirac field, Rev. Math. Phys. 22 (2010); arXiv:0911.1304.'
  key: Sanders2010
  doi: 10.1142/S0129055X10003990
derivations:
- name: main
  uses:
  - synthesis.imported-gtg-dictionary@1
  - synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field@2
  - field-theory.second-quantisation@5
  - synthesis.imported-microlocal-hadamard-condition@2
  - synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard@2
  - synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport@3
  - synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem@1
  - synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_test_fields_are_in_the_store_gauge_and_weyl_curved
- kind: check
  ref: check.py::check_synge_function_scales_to_half_the_flat_square
- kind: check
  ref: check.py::check_van_vleck_determinant_and_transport_rotor_tend_to_one
- kind: check
  ref: check.py::check_scaled_dirac_parametrix_tends_to_the_flat_massless_kernel
- kind: check
  ref: check.py::check_flat_massless_kernel_and_normalisation
- kind: check
  ref: check.py::check_scaling_powers_of_the_hadamard_terms
- kind: check
  ref: check.py::check_store_dilation_is_normal_dilation_up_to_a_map_tending_to_the_identity
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.hadamard-scaling-limit-premise
  - synthesis.weyl-flat-fields-need-no-scaling-limit-premise-and-robertson-walker-generators-see-the-schwarzian
  - synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes
extraction:
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Folded into version 4 of this pass. The infinitesimal shift of the spacetime separation is written in scalar form with the field unit (U3 scalar form, citing std-algebra.complexification-is-the-odd-extension(iii); U1, the Hadamard chain): the boundary values sigma_{+-} with the -+ I_4 0 of a time function, the regulators sigma_l + I_4 epsilon h_l and Q(z)/2 + I_4 0 h, the flat boundary value Q(y - y) - I_4 0 <y - y, e_0> (from Q(y - y - i0 e_0): the square of the shifted vector is Q(xi) - 2 i 0 xi_0, so the scalar form is exact) and D_+(xi) = -1/(4 pi^2 (Q(xi) - I_4 0 xi_0)) of the imported Fact. A vector-form shift with I_5 is not used, since the kernels already carry I_4 and the two units must not meet in one distribution (I_4 I_5 = -e, not -1). No i remains; declaration removed. Mathematics, links and checks unchanged.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'By Leon''s ruling R2 (7 November 2026) the Dirac Hadamard chain carries the field theory''s unit I_4: on the bispinor kernels, whose values are not even, it is the right unit R_{I_4} : x -> xI_4 (the numerator (R_{I_4}D_x + m_0), the squared operator, p = +-R_{I_4} nabla on the plane waves e^{-+I_4 p.z}), and on the even limit kernels it is written I_4 ((I_4/2 pi^2)(y - y'')e_0/Q^2 = I_4 nabla D_+ e_0); numbers are read in span{1, I_4}. Stays: the i0 of a time function, the regulators sigma_l + i epsilon h_l and Q(z) + i0 h, and the flat boundary value Q(y - y'' - i0 e_0) (a shift of the spacetime separation), and D_+ as the imported Fact states it; declared complex-analysis.'
  open_problem: op.qft-on-gtg-fields
  note: >-
    Clause (a) of the adopted premise (HS), synthesis.hadamard-scaling-limit-premise, re-derived in the spacetime
    algebra on the store's gravitational fields. Standard: this is Prop. 5.6 of H. Sahlmann and R. Verch,
    Rev. Math. Phys. 13 (2001) 1203, arXiv math-ph/0008029 (statements of Prop. 5.6, Lemma 5.7, Def. 5.1 and
    Def. 5.3 checked against the arXiv text; the text conversion stops at the opening of their Sec. 5.4, so
    their Thm. 5.8 and the proof of Prop. 5.6 in Appendix A.5 could not be read and are not followed). The
    published result already covers every Dirac mass m >= 0 (their Def. 5.3), every globally hyperbolic
    spacetime and dimension four as a special case; none of that is new here, nor is the independence of the
    limit from Omega(x0) (gauge covariance). What is new: (1) the spacetime-algebra form on the store's fields
    (hb, Omega): the identity D_x sigma = hb^{-1}(gamma'(1)), the transport rotor R, the GA Taylor data;
    (2) the store's dilation x0 + l (x - x0) on the flat background in a gauge with hb(x0) = 1, related to the
    normal-coordinate dilation by a map Phi_l -> id (computed); (3) Dirac rather than Majorana spinors (their
    CAR case is posed for Majorana spinors in dimensions 3, 4, 9, 10 mod 8), by an argued transcription through
    gauge invariance, with the field theory's unit outside the Clifford product on massive lines; the role of
    their Theta (the matrix of the Dirac conjugation composed with charge conjugation, as the Majorana pairing
    needs) is taken in the gauge-invariant Dirac form by the constant Dirac adjoint, the e0 of the stored
    kernels, since the background trivialises the spinors; (4) the limit is identified with the stored
    normalisation i grad D_+ e0 of the flat-plane restriction result; (5) exact Taylor data on a Weyl-curved
    plane wave and a generic polynomial field. The equivalence "microlocal condition <=> Hadamard form" used in
    the proof is the stored Fact (a), their Thm. 5.8, which according to the paper's introduction repairs a
    gap in Radzikowski's argument that also affects the Dirac equivalence proofs of Koehler, Kratzert and
    Hollands (Thm. 5.8 itself not checked against the text); K. Sanders, Rev. Math. Phys. 22 (2010),
    arXiv 0911.1304, also addresses gaps in the Dirac equivalence (both recorded in the Fact at its version
    2, with Prop. 5.6 imported there as clause (d)). Imported as the Fact
    synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport
    (cited from memory in version 1): the Hadamard parametrix of a normally hyperbolic operator on a bundle
    with connection, with leading coefficient Delta^(1/2) times the parallel transport (Friedlander 1975;
    Bar, Ginoux and Pfaffle 2007, Ch. 2), applied to the squared Dirac operator, whose connection is the spin
    connection (Lichnerowicz); independence of the Hadamard form from the time function in its i0
    prescription (Kay and Wald 1991; Sahlmann and Verch 2001, Sec. 5.1). Cited from memory: continuity of
    pullbacks under diffeomorphisms converging in C-infinity (a change of variables). Gauge invariance is used to transcribe the Hadamard-form
    Fact, whose source is posed for Majorana spinors, to the store's pair of two-point functions (argued);
    quasi-freeness to pass from the two-point functions to the state. Transport-absent (standard quantum field
    theory on a Gauge Theory Gravity field; R is the Levi-Civita spin transport, not the series' transport);
    Gauge Theory Gravity is convenient: one global spinor trivialisation and a flat dilation. Its use: (HS)
    reduces to clause (b), the commutation of the scaling limit with the restriction to the generators of a
    local Rindler horizon, which this result does not give;
    synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces
    treats clause (b) (the leading null singularity on a null hypersurface), using the same two imported
    analytic inputs; the two cite each other (formal (v) and Step 9 here). The premise (HS) has since been
    restated (version 3): clause (a), the subject of this result, is retired from it, and clause (b) is now
    a premise about the restricted parametrix on horizon generators; "clause (a)" and "clause (b)" here name
    the clauses of its version 2.
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, at Leon''s decisions of 2 November 2026: uses edges to the imported Fact on the Dirac Hadamard parametrix (new) and to the Dirac Hadamard-form Fact at its version 2 (Prop. 5.6 of Sahlmann and Verch imported as its clause (d)) replace the citations from memory in formal (i), (iii) and proof Steps 1, 7 and 8; cross-citation of the clause (b) result added in formal (v) and Step 9; a sentence records that (HS) has been restated, clause (a) retired. Statement, proof steps and checks otherwise unchanged.'
  flags:
  - 'standard: Sahlmann and Verch 2001, Prop. 5.6 (any mass, normal-coordinate dilation, Majorana spinors); new here are the spacetime-algebra form, the store dilation and the Dirac transcription'
  - 'conditional on the imported Fact on the Dirac Hadamard parametrix (U = Delta^(1/2) R, time-function independence), whose four-dimensional leading coefficient is there partly cited from memory'
  - 'gauge: hb(x0) = 1 fixes the flat vacuum in the background coordinates; for other hb(x0) the limit is the vacuum in the local inertial coordinates hb^{-1}(x0)(x - x0)'
  - 'gauge-invariant quasi-free states, as in (HS): gauge invariance transcribes the Majorana-posed Hadamard-form Fact to the store''s pair of two-point functions (argued); quasi-freeness gives the state limit'
  - 'not the generator clause (b): restriction to a null surface is not a pullback, and the generator scaling is one-dimensional with fixed transverse profiles'
  maintainer_pass_hs_bound:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 2 -> 3, at Leon''s decisions of 2 November 2026 (Hadamard scaling bound): (HS), synthesis.hadamard-scaling-limit-premise, is now a theorem (version 4); a sentence in formal (v) and the technical level records that the premise, restated as the remainder bound, is now a theorem assembling this result with the generator results. What this entity asserts is unchanged.'
---

## formal
Units $\hbar = c = 1$. Let $(\hb, \Omega)$ be a gravitational field on four-dimensional flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric $g$ is smooth and globally hyperbolic on a region $U$ of its invertible region, $x_{0} \in U$, in a gauge with $\hb(x_{0}) = 1$ ($\Omega(x_{0})$ arbitrary), and let $\psi$ be the free Dirac field of mass $m_{0} \ge 0$ on it (Fact \claimref{synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field}; Proposition \claimref{field-theory.second-quantisation}), with covariant derivative $D_{a}\psi = a\cdot\nabla\psi + \tfrac12\Omega(a)\psi$ and Dirac operator $D = g^{\mu}D_{e_{\mu}}$, $g^{\mu} = \hb^{T}(e^{\mu})$. The field theory's unit is $I_{4}$ (numbers are read in $\mathrm{span}\{1, I_{4}\}$); on these kernels, whose values are not even, it stands outside the Clifford product as the right unit $R_{I_{4}} : x \mapsto xI_{4}$, which commutes with every left factor, and numbers act on the right in the same way. Let $\omega$ be a gauge-invariant quasi-free state that is Hadamard (Fact \claimref{synthesis.imported-microlocal-hadamard-condition}(b)), equivalently whose two-point functions have the Hadamard form (Fact \claimref{synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard}(a)).
\begin{enumerate}
\item[(i)] \emph{(Hadamard form in the spacetime algebra; standard, Fact \claimref{synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport}, written in the spacetime algebra.)} On a geodesically convex neighbourhood $N$ of $x_{0}$, $\omega(\psi(x)\psi^{\dagger}(x')) = (R_{I_{4}}D_{x} + m_{0})H_{+}(x, x')e_{0} + S_{+}(x, x')$ and $\omega(\psi^{\dagger}(x')\psi(x)) = -(R_{I_{4}}D_{x} + m_{0})H_{-}(x, x')e_{0} + S_{-}(x, x')$, with $S_{\pm}$ of class $C^{1}$ and
\[
H_{\pm} = -\frac{1}{8\pi^{2}}\Bigl(\frac{U}{\sigma_{\pm}} + V\log\sigma_{\pm}\Bigr),\qquad U(x, x') = \Delta^{1/2}(x, x')\,R(x, x'),
\]
where $\sigma$ is the Synge function of $g$ ($\sigma = \tfrac12 Q(x - x')$ on the flat field), $\sigma_{\pm}$ its boundary values with the $\mp I_{4}0$ of a time function (an infinitesimal shift of the separation, written in scalar form: the square of a shifted vector is a number, Theorem \claimref{std-algebra.complexification-is-the-odd-extension}(iii)), $\Delta$ the Van Vleck determinant, $R(x, x')$ the spinor transport rotor along the geodesic $\gamma$ from $x'$ ($t = 0$) to $x$ ($t = 1$), $\dot R = -\tfrac12\Omega(\dot\gamma)R$, $R(x', x') = 1$, and $V$ smooth (on the flat field $V(x, x) = -\tfrac12 m_{0}^{2}$). In this form $D_{x}\sigma = \hb^{-1}(\dot\gamma(1))$, the physical tangent of $\gamma$ at $x$ (proved).
\item[(ii)] \emph{(Taylor data in the store's dilation; computed.)} With $x = x_{0} + l y$, $x' = x_{0} + l y'$, $d = y - y'$, $\bar y = \tfrac12(y + y')$: $\sigma = l^{2}\sigma_{l}(y, y')$ with $\sigma_{l}$ jointly smooth down to $l = 0$ and $\sigma_{l} = \tfrac12 Q(d) + l\,d\cdot\bigl[(\bar y\cdot\nabla)\hb^{-1}\bigr](d)\big|_{x_{0}} + O(l^{2})$ (index reading $\tfrac{l}{2}(\partial_{\rho}g_{\mu\nu})(x_{0})\bar y^{\rho}d^{\mu}d^{\nu}$); $\Delta = 1 + \tfrac{l^{2}}{6}\Ric^{\circ}(d, d) + O(l^{3})$ with $\Ric^{\circ}(d, d) = -d\cdot\mathcal{R}(d)$ at $x_{0}$ (the store's Ricci map; at $x_{0}$ physical and background vectors agree); $R = 1 - \tfrac{l}{2}\Omega(d)(x_{0}) + O(l^{2})$, which is $1 - \tfrac{l^{2}}{2}(\bar y\cdot\nabla)\Omega(d)(x_{0}) + O(l^{3})$ when $\Omega(x_{0}) = 0$. The scaled Dirac operator is $lD = g^{\mu}(x_{0} + ly)(\partial_{y^{\mu}} + \tfrac{l}{2}\Omega(e_{\mu})(x_{0} + ly)) \to \nabla_{y}$, with mass term $lm_{0}$.
\item[(iii)] \emph{(The scaling limit; standard, \cite[Prop.~5.6]{SahlmannVerch2001}, posed there for Majorana spinors with a normal-coordinate dilation and Dirac mass $m \ge 0$; imported as Fact \claimref{synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard}(d); re-derived here, proved given the leading coefficient and the independence of the Hadamard form from the time function, Fact \claimref{synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport}.)} For every $m_{0} \ge 0$, at every point, whatever the Weyl and Ricci curvature, as $l \to 0^{+}$, in $\mathcal{D}'$ on a neighbourhood of $(0, 0)$,
\[
l^{3}\,\omega\bigl(\psi(x_{0} + ly)\psi^{\dagger}(x_{0} + ly')\bigr) \to \frac{I_{4}}{2\pi^{2}}\,\frac{(y - y')\,e_{0}}{\bigl(Q(y - y') - I_{4}0\,\ip{y - y'}{e_{0}}\bigr)^{2}} = I_{4}\nabla D_{+}(y - y')\,e_{0},
\]
and the other ordering tends to $-I_{4}\nabla D_{-}(y - y')e_{0}$ (even values, on which $I_{4}$ on the left and on the right agree), $D_{-} = \overline{D_{+}}$: the two-point functions of the vacuum of the massless Dirac field on the flat field in the stored normalisation (Fact \claimref{synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem}; the kernels of Theorem \claimref{synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes}(ii) at $m_{0} = 0$). Rates, in every gauge with $\hb(x_{0}) = 1$: the leading term converges at rate $l$ (the first derivatives of $\hb^{-1}$ at $x_{0}$); the mass term is $O(l)$; the connection and $D_{x}U$ terms are each $O(l)$ when $\Omega(x_{0}) \ne 0$, but their $O(l)$ parts cancel, so their sum is $O(l^{2})$ (each is $O(l^{2})$ when $\Omega(x_{0}) = 0$); the logarithmic term is $O(l^{2})$ (its $\log l$ part $O(l^{3}\log l)$); the $C^{1}$ remainder is $O(l^{3})$. Only $\hb(x_{0}) = 1$ is needed; $\Omega(x_{0}) = 0$ is not. Since $\omega$ is gauge-invariant and quasi-free, all its $n$-point functions converge: the scaling limit of $\omega$ at $x_{0}$ is the flat massless vacuum. This is clause (a) of Premise \claimref{synthesis.hadamard-scaling-limit-premise}, (HS), in its version 2, for every gravitational field in its scope; that clause is now retired from the premise, which is restated as a statement about the Hadamard parametrix restricted to horizon generators.
\item[(iv)] \emph{(Normal-coordinate dilation; computed.)} If $N(x)$ are the normal coordinates at $x_{0}$, $\Phi_{l}(y) = l^{-1}N(x_{0} + ly) = y + \tfrac{l}{2}\Gamma(x_{0})(y, y) + O(l^{2})$, where, when $\Omega(x_{0}) = 0$, $\Gamma(x_{0})(a, b) = (a\cdot\nabla\hb^{-1})(b)|_{x_{0}}$; $\Phi_{l}$ tends to the identity with all derivatives, and $\sigma(x_{0}, x) = \tfrac12 Q(N(x))$. So the limit (iii) is the normal-coordinate scaling limit of Sahlmann and Verch, and the role of their $\Theta$ (the matrix of the Dirac conjugation composed with charge conjugation) is taken by the constant Dirac adjoint, the $e_{0}$ above.
\item[(v)] \emph{(What it does not give.)} Not clause (b) of (HS): the restriction of the limit to the flat null plane through $x_{0}$ is the null vacuum by Theorem \claimref{synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes}(ii), but that the restriction to the generators of a local Rindler horizon commutes with the scaling is not shown: the restriction is not a pullback (the wave-front set of the kernel meets the conormal of the null surface along the generators), and (b) scales the generator parameter alone with fixed transverse profiles, while (iii) scales all four directions. Clause (b) is treated by Theorem \claimref{synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces}: the field strength cancels from the coefficient of the leading null singularity of the restricted kernel, restricted kernels of Hadamard states differ by smooth kernels, and what remains is a remainder bound on the restricted parametrix, argued; the premise, restated as that bound, gives clause (b) with this result and that one. (Added later: the bound is proved, and (HS) is now Theorem \claimref{synthesis.hadamard-scaling-limit-premise} (version 4), which assembles this result with the generator results; clause (b) holds for every mass at every point.) Not the ground-state clause of (N$_{+}$), not which state, and nothing beyond the free Dirac field.
\end{enumerate}

## technical
The adopted premise (HS) has two clauses: (a) a gauge-invariant quasi-free Hadamard state of the Dirac field looks, under scaling to a point of a gravitational field, like the flat field's massless vacuum; (b) the same holds on the null generators of every local Rindler horizon through the point, so that scaling and restriction to the horizon commute. This result proves (a) on every globally hyperbolic gravitational field, given two standard analytic inputs imported from the literature (the Hadamard parametrix of the squared Dirac operator and the independence of the Hadamard form from the time function). The premise has since been restated, with (a) retired and (b) posed on the Hadamard parametrix restricted to the null generators, and then proved: (HS) is now a theorem, assembling this result with results on the null generators. In the store, before, only the Weyl-flat massless case was a theorem. The statement is standard: it is Prop. 5.6 of Sahlmann and Verch (2001), who treat Majorana spinors of any mass with a normal-coordinate dilation; what is new is its form in the spacetime algebra on the store's fields, with the store's dilation and Dirac spinors.

The two-point function of a Hadamard state is, near the point, the Dirac operator applied to the Hadamard parametrix of the squared Dirac operator, $-(1/8\pi^{2})(U/\sigma + V\log\sigma)$, plus a smooth term, where $\sigma$ is the Synge function and $U$ is the square root of the Van Vleck determinant times the spinor transport rotor along the geodesic. In the store's gauge, with the gauge field equal to one at the point, scale both arguments by $l$ and the field by $l^{3/2}$. Then $\sigma$ is $l^{2}$ times $\tfrac12 Q(y - y')$ plus $O(l^{3})$, $U$ tends to one, and the Dirac operator of the Synge function is the physical tangent of the geodesic, so the leading term tends to the flat massless kernel $(I_{4}/2\pi^{2})(y - y')e_{0}/Q^{2}$. The mass term vanishes like $l$, the connection and rotor-derivative terms together like $l^{2}$ (whatever the connection at the point), the logarithmic term like $l^{2}$ and the smooth remainder like $l^{3}$. Convergence as distributions follows because the scaled Synge function is the flat square composed with a family of maps converging to the identity. Exact Taylor coefficients on a Weyl-curved plane wave and a generic field check each step. Clause (b), the commutation with the restriction to the generators, is not given: the restriction is not a pullback of distributions, and (b) scales only along the generators.

## lay
The series assumed that any state of the free electron field of the standard regular kind (gauge-invariant, quasi-free and Hadamard), looked at closely enough at a point where gravity is present, resembles the empty state of flat space. This result proves that assumption for the bulk of space-time, for massive and massless particles and for every gravitational field with a well-posed causal structure (globally hyperbolic), by redoing in the series' algebra a known theorem of Sahlmann and Verch from the mathematical physics literature: close up, the curvature, the mass and the gravitational connection all fade out of the state's correlations at definite rates. It relies on two standard analytic facts quoted from the literature rather than proved in the series. What it does not prove is the companion statement the series also needs: that the same is true when the state is looked at only along the light rays of a small horizon. That part stays an assumption.

## one-liner
Given the Hadamard parametrix of the squared Dirac operator (cited), at every point of every globally hyperbolic gravitational field a gauge-invariant quasi-free Hadamard state of the Dirac field of any mass scales, in a gauge with hb(x0) = 1, to the flat massless vacuum on both orderings (Synge function l^2 Q/2 + O(l^3), U = Delta^(1/2) R -> 1, D_x sigma the physical tangent; mass O(l), connection and D_x U together O(l^2), log O(l^2), remainder O(l^3)), so clause (a) of (HS) holds: standard (Sahlmann and Verch 2001, Prop. 5.6), re-derived in the spacetime algebra for Dirac spinors; clause (b), restriction to horizon generators, is not given.
