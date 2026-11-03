---
id: synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport
kind: claim
version: 2
title: 'Imported: the Hadamard parametrix of a normally hyperbolic operator on a vector bundle has leading coefficient the square root of the Van Vleck determinant times the parallel transport of the operator''s connection (Friedlander 1975; Bar, Ginoux and Pfaffle 2007, Ch. 2); for the squared Dirac operator that connection is the spin connection (Lichnerowicz), so U = Delta^(1/2) R; the Hadamard form does not depend on the time function of its i0 prescription (Kay and Wald 1991; Sahlmann and Verch 2001, Sec. 5.1); and in four dimensions the retarded and advanced fundamental solutions on a causal domain are (1/4 pi) theta(+-(t - t'')) [U delta(sigma) + V theta(sigma)] with V smooth (Friedlander 1975; Bar, Ginoux and Pfaffle 2007, Ch. 2)'
status: imported
region: synthesis
subject: quantum-fields
tags: [car-algebra, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-02
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'F. G. Friedlander, The Wave Equation on a Curved Space-Time, Cambridge University Press, Cambridge, 1975.'
  key: Friedlander1975
  locator: 'the fundamental solutions of normally hyperbolic operators and their Hadamard form; cited from memory, not read'
- citation: 'C. Bar, N. Ginoux and F. Pfaffle, Wave Equations on Lorentzian Manifolds and Quantization, ESI Lectures in Mathematics and Physics, European Mathematical Society, 2007; arXiv:0806.1036.'
  key: BarGinouxPfaffle2007
  locator: 'Ch. 2 (Def. 2.2.1, Prop. 2.3.1; the formal and local fundamental solutions as sums of Hadamard coefficients times Riesz distributions); Sec. 1.3 (the function mu_x)'
  doi: 10.4171/037
- citation: 'E. Poisson, The motion of point particles in curved spacetime, Living Rev. Relativity 7 (2004), 6; arXiv:gr-qc/0306052.'
  key: Poisson2004
  locator: 'Sec. 4.3.2, Eqs. (266), (268), (269), (273) (scalar Green functions); Sec. 4.4.2 (electromagnetic Green functions, U = parallel propagator times Delta^(1/2))'
- citation: 'H. Sahlmann and R. Verch, Microlocal spectrum condition and Hadamard form for vector-valued quantum fields in curved spacetime, Rev. Math. Phys. 13 (2001), 1203--1246; arXiv:math-ph/0008029.'
  key: SahlmannVerch2001
  locator: 'Sec. 3.5; Sec. 5.1'
  doi: 10.1142/S0129055X01001010
- citation: 'B. S. Kay and R. M. Wald, Theorems on the uniqueness and thermal properties of stationary, nonsingular, quasifree states on spacetimes with a bifurcate Killing horizon, Phys. Rep. 207 (1991), 49--136.'
  key: KayWald1991
- citation: 'M. J. Radzikowski, Micro-local approach to the Hadamard condition in quantum field theory on curved space-time, Commun. Math. Phys. 179 (1996), 529--553.'
  key: Radzikowski1996
  doi: 10.1007/BF02100096
- citation: 'L. Ronge, Formulas for Hadamard coefficients in terms of Green''s operators, arXiv:2604.25763 (2026).'
  key: Ronge2026
  locator: 'Def./Prop. 2.9, 2.10; Sec. 2.1'
- citation: 'A. G. M. Lewis, Hadamard renormalization of a 2-dimensional Dirac field, Phys. Rev. D 101 (2020), 125019; arXiv:1910.05663.'
  key: Lewis2020
  locator: 'Eqs. (14), (26), (52)'
  doi: 10.1103/PhysRevD.101.125019
extraction:
  note: >-
    Imported so that the two results on the scaling of Hadamard Dirac states
    (synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field
    and synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces)
    cite as a Fact the two analytic inputs they had cited from memory: the leading Hadamard coefficient of
    the squared Dirac operator and the independence of the Hadamard form from the time function of its i0
    prescription. The time-function clause is put here, not on the microlocal Fact
    synthesis.imported-microlocal-hadamard-condition, so that the results pinning that Fact are not
    disturbed. Checked on 2 November 2026. Sahlmann and Verch against the arXiv text of math-ph/0008029:
    Sec. 3.5 (the Dirac operators are nabla-slash plus or minus i m, m >= 0 a constant or a bundle map, and
    "P = D D is a wave operator" on the Dirac bundle, wave operators being those with metric principal part,
    Sec. 3.1, which also defines the connection nabla(P) determined by P through 2 nabla(P)_{grad phi} f =
    P(phi f) - phi P(f) - (box phi) f); Sec. 5.1 (the Hadamard coefficients are the sections uniquely
    determined by the Hadamard recursion relations of P, given in their Appendix A.1, which the text
    conversion does not reach; a time function has future-directed timelike unit gradient; the regularised
    distribution uses s - 2 i epsilon (t(x) - t(y)) + epsilon^2, s the signed squared geodesic distance,
    positive for spacelike separation; and "the definition of Hadamard form is independent of the choice of
    the time-function", the argument following Kay and Wald). That the connection of P is the spin connection
    is not stated in the part of their text read; it is the Lichnerowicz formula, cited from memory. Ronge,
    arXiv:2604.25763, Sec. 2.1 and Def./Prop. 2.9, 2.10, against its arXiv text: a normally hyperbolic P
    decomposes uniquely as the d'Alembertian of a connection plus a zero-order term, and the Hadamard
    coefficients V^k_x are the unique sections with (rho_x - 2k) V^k_x = 2k P V^{k-1}_x, V^0_x(x) = 1, where
    rho_x V = nabla_{grad Gamma_x} V - (box Gamma_x / 2 - d) V with the connection of P, citing Bar, Ginoux
    and Pfaffle, Def. 2.2.1 and Prop. 2.3.1, and Friedlander for other descriptions. Bar, Ginoux and Pfaffle
    against the arXiv text of 0806.1036: only Sec. 1.3 is reachable in the text conversion (the density mu_x
    with dV = mu_x (exp_x^{-1})^* dz, mu_x = det(d exp_x) o exp_x^{-1}, and Lemma 1.3.17, Hess(mu_x) at x
    equal to -ric/3); their Ch. 2 was not read; the book's data (EMS, 2007, DOI 10.4171/037) against the
    publisher's page. The solution of the k = 0 transport equation as V^0_x = mu_x^{-1/2} times the parallel
    transport of the connection, and mu_x^{-1/2} = Delta^{1/2} (Van Vleck), is cited from memory (Bar, Ginoux
    and Pfaffle, Ch. 2; Friedlander 1975); for spinors it was checked against Lewis, arXiv:1910.05663, where
    the squared Dirac operator is the spin d'Alembertian plus R/4 (Eq. (14)) and the leading Hadamard
    coefficient is minus Delta^{1/2} times the spinor parallel propagator (Eq. (52), with Eq. (26)), in two
    dimensions, where it multiplies the logarithm; the four-dimensional statement is cited from memory.
    Friedlander's book and Kay and Wald's paper were not read; their bibliographic data are from memory
    (Kay and Wald's as recorded in the store's references). Radzikowski is cited for the scalar field, where
    the equivalence of the Hadamard form with the wave front set condition makes the time function
    irrelevant (from memory). Not part of this Fact: the higher Hadamard coefficients, the covariant
    expansion of Delta, the sign and coefficient of the curvature term in the Lichnerowicz formula in the
    store's conventions, and the normalising constant of the parametrix (fixed in the results by the flat
    field).
    Clause (d), added in version 2 (2 November 2026), checked against E. Poisson, Living Rev. Relativity 7 (2004) 6,
    Sec. 4.3.2 (read in its online edition): for the scalar wave equation (box - xi R) G = -4 pi delta_4, in
    signature (-,+,+,+) with sigma negative for timelike separation, the retarded and advanced Green functions are
    G_+- = U delta_+-(sigma) + V theta_+-(-sigma) with U and V smooth biscalars, [U] = 1 and U = Delta^(1/2),
    valid for x in the normal convex neighbourhood of x' (Eqs. (268), (269), (273)); Sec. 4.4.2: the same form for
    the electromagnetic Green functions with U the parallel propagator times Delta^(1/2) and V a smooth bitensor fixed
    by the wave equation and characteristic data. In the store's signature (+,-,-,-), sigma positive for timelike
    separation and P G = delta, this is G_+- = (1/4 pi) theta(+-(t - t')) [U delta(sigma) + V theta(sigma)] (the
    conversion is the store's; on the flat field (1/4 pi) theta(t) delta(sigma) = theta(t) delta(t - r)/(4 pi r)).
    The statement for a general normally hyperbolic operator on a vector bundle (the Dirac case among them), with
    U the leading coefficient of (a), is Friedlander's and Bar, Ginoux and Pfaffle's (the local fundamental
    solutions as the sum of Hadamard coefficients times Riesz distributions, Ch. 2, whose four-dimensional terms
    are delta(sigma) on the light cone and smooth functions on its interior), cited from memory: their Ch. 2 is
    beyond the arXiv text conversion and Friedlander's book was not read. Clause (c) concerns the bulk
    distributions; a restriction of the regularised distributions to a null hypersurface (an epsilon-regularised
    transverse limit) depends on the time function by a smooth kernel, and is not part of this Fact.
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Created at Leon''s decisions of 2 November 2026 (imports for the Hadamard scaling results), so that the two scaling results cite the leading Hadamard coefficient of the squared Dirac operator and the time-function independence as a Fact instead of citing them from memory; partly verified (see note).'
  maintainer_pass_hs_bound:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, at Leon''s decisions of 2 November 2026 (Hadamard scaling bound): new clause (d), the four-dimensional form of the retarded and advanced fundamental solutions on a causal domain (Friedlander; Bar, Ginoux and Pfaffle; checked for the scalar and vector cases against Poisson 2004, Secs. 4.3.2, 4.4.2), so that the generator-CAR result cites it as a Fact; a sentence records that (c) concerns the bulk distributions. Clauses (a) to (c) assert what they asserted.'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on four-dimensional flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric $g$ is smooth and globally hyperbolic on a region $U$ of its invertible region, $N \subset U$ geodesically convex, $\sigma$ the Synge function of $g$ on $N\times N$ ($\sigma = \tfrac12 Q(x - x')$ on the flat field) and $\Delta$ its Van Vleck determinant.
\begin{enumerate}
\item[(a)] \emph{(Bundle parametrix; Friedlander; B\"ar, Ginoux and Pf\"affle, Ch.~2.)} A normally hyperbolic operator $P$ on a vector bundle over $N$ (principal part that of the d'Alembertian of $g$) is, uniquely, the d'Alembertian of a connection $\nabla^{P}$ plus a zero-order term. Its Hadamard coefficients are the unique sections fixed by transport equations along the geodesics from $x'$ with the identity at coincidence, and the leading one is $\Delta^{1/2}(x, x')\,\Pi(x, x')$, $\Pi(x, x')$ the parallel transport of $\nabla^{P}$ along the geodesic from $x'$ to $x$. In four dimensions the Hadamard parametrix of $P$ is, up to its normalising constant, $U/\sigma + V\log\sigma + W$ with $U = \Delta^{1/2}\Pi$ and $V$, $W$ smooth.
\item[(b)] \emph{(The squared Dirac operator; Lichnerowicz.)} Let $\psi$ be the free Dirac field of mass $m \ge 0$ on $(\hb, \Omega)$, with covariant derivative $D_{a}\psi = a\cdot\nabla\psi + \tfrac12\Omega(a)\psi$ and Dirac operator $D = g^{\mu}D_{e_{\mu}}$, $g^{\mu} = \hb^{T}(e^{\mu})$; on massive lines the field theory's unit $i$ stands outside the Clifford product. The squared operator $(iD - m)(iD + m) = -(D^{2} + m^{2})$ is normally hyperbolic, and by the Lichnerowicz formula ($D^{2}$ is the d'Alembertian of the spin connection plus a multiple of the scalar curvature) its connection $\nabla^{P}$ is the spin connection. So $\Pi(x, x')$ is left multiplication by the rotor $R$ of the geodesic $\gamma$ from $x'$ ($t = 0$) to $x$ ($t = 1$), $\dot R = -\tfrac12\Omega(\dot\gamma)R$, $R = 1$ at $t = 0$ (parallel transport, Fact \claimref{synthesis.imported-gtg-dictionary}(ii)), and the leading Hadamard coefficient of the squared Dirac operator is $U = \Delta^{1/2}R$.
\item[(c)] \emph{(The $i0$ prescription; Kay and Wald; Sahlmann and Verch, Sec.~5.1.)} The distributions $1/\sigma$ and $\log\sigma$ of the Hadamard form are the $\epsilon \to 0^{+}$ limits of their regularisations by $\epsilon(t(x) - t(x'))$ and $\epsilon^{2}$, for a time function $t$ (a smooth function with future-directed timelike unit gradient), as in the source; the Hadamard form so defined, for the scalar field and for vector-valued fields such as the Dirac field, does not depend on the choice of time function. This concerns the bulk distributions on $N\times N$.
\item[(d)] \emph{(Fundamental solutions in four dimensions; Friedlander; B\"ar, Ginoux and Pf\"affle, Ch.~2; for scalar and vector fields Poisson, Secs.~4.3.2, 4.4.2.)} On a geodesically convex, causally convex domain $N$ (a causal domain), with $\sigma$ positive on timelike separation, a time function $t$, and $P$ normalised so that its principal part is $g^{\mu\nu}\partial_{\mu}\partial_{\nu}$ (on the flat field the d'Alembertian $\partial_{t}^{2} - \nabla^{2}$), the retarded and advanced fundamental solutions of $P$ ($PG_{\pm} = \delta$, $G_{\pm}(\cdot, x')$ supported in $J^{\pm}(x')$) are
\[
G_{\pm}(x, x') = \frac{1}{4\pi}\,\theta\bigl(\pm(t(x) - t(x'))\bigr)\bigl[U(x, x')\,\delta(\sigma) + V(x, x')\,\theta(\sigma)\bigr],
\]
with $U = \Delta^{1/2}\Pi$ the leading coefficient of (a) and $V$ smooth on $N\times N$; on the flat field $\tfrac{1}{4\pi}\theta(t)\delta(\sigma) = \theta(t)\delta(t - r)/(4\pi r)$. For the squared Dirac operator $D^{2} + m^{2}$ of (b), $U = \Delta^{1/2}R$.
\end{enumerate}
Not part of this Fact: the higher Hadamard coefficients, the covariant expansion of $\Delta$, the coefficient of the curvature term in the Lichnerowicz formula, the normalising constant of the parametrix, and restrictions of the regularised distributions of (c) to null hypersurfaces, which depend on the time function by smooth kernels. \emph{Provenance:} \cite{Friedlander1975}; \cite[Ch.~2]{BarGinouxPfaffle2007}; \cite[Secs.~3.5, 5.1]{SahlmannVerch2001}; \cite{KayWald1991}; \cite{Radzikowski1996}; for the transport equations \cite[Def./Prop.~2.10]{Ronge2026}; for the spinor coefficient in two dimensions \cite[Eq.~(52)]{Lewis2020}; for (d) in the scalar and vector cases \cite[Secs.~4.3.2, 4.4.2]{Poisson2004}.

## technical
The Hadamard condition says that at short distances the two-point function of a state looks like the vacuum's, and it is written with an explicit singular term built from the squared geodesic distance $\sigma$ between the two points. For a field with several components, the coefficient of the leading singular term is a matrix: the square root of the Van Vleck determinant, which measures how geodesics from a point spread, times the parallel transport of the field's connection along the geodesic joining the two points. For the Dirac field the relevant operator is the square of the Dirac operator, whose connection is the spin connection, so in Gauge Theory Gravity the transport is left multiplication by the rotor that solves $\dot R = -\tfrac12\Omega(\dot\gamma)R$ along the geodesic. The singular terms carry an infinitesimal imaginary shift fixed by a time function, and the resulting Hadamard form is the same for every time function. In four dimensions the retarded and advanced solutions of the squared operator have the same coefficient: a delta function on the light cone with that coefficient, plus a smooth tail inside the cone. These are standard results taken from the literature.

## lay
Physicists describe the regular states of a quantum field by the exact way its correlations blow up when two points come together. For the electron field, the strength of that blow-up is set by two pieces of geometry: how quickly straight paths from a point spread out, and how the electron's spin is carried along the path joining the two points. The rule also does not depend on which way of slicing space-time into moments is used to state it, and the same two pieces of geometry fix how a disturbance of the field spreads along the light cone. These are taken from the literature.

## one-liner
For a normally hyperbolic operator on a vector bundle the leading Hadamard coefficient is $\Delta^{1/2}$ times the parallel transport of the operator's connection (Friedlander 1975; Bar, Ginoux and Pfaffle 2007); for the squared Dirac operator that is the spin connection, so $U = \Delta^{1/2}R$ with $\dot R = -\tfrac12\Omega(\dot\gamma)R$; the Hadamard form does not depend on the time function of its $i0$ prescription (Kay and Wald 1991; Sahlmann and Verch 2001, Sec. 5.1); in four dimensions the retarded and advanced fundamental solutions on a causal domain are $\tfrac{1}{4\pi}\theta(\pm(t - t'))[U\delta(\sigma) + V\theta(\sigma)]$, $V$ smooth.
