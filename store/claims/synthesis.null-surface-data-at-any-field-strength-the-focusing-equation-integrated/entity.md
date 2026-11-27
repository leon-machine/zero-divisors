---
id: synthesis.null-surface-data-at-any-field-strength-the-focusing-equation-integrated
kind: claim
version: 1
title: 'Null-surface data at any field strength: the focusing equation integrated'
status: proved
region: synthesis
subject: einstein
tags: [curvature-and-field-equations, gauge-fields, null-directions]
proposed_by:
  kind: ai
  session: 2026-11-27-null-surface-three
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction (the question, the extension from first order to a field of any strength on one null surface, the instruction to work from the stored results and to state everything in geometric algebra)
- name: Claude Fable 5.2
  role: proposal, proof and drafting
  source: session 2026-11-27-null-surface-three
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators@1
  - synthesis.field-equation-linear-in-the-curvature-with-a-conserved-source-is-einsteins@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_plane_wave_is_an_exact_field_with_the_stored_first_order_curvature
- kind: check
  ref: check.py::check_null_gradient_of_the_wave_and_its_parallel_screen
- kind: check
  ref: check.py::check_area_density_and_the_linear_focusing_equation_on_strong_waves
- kind: check
  ref: check.py::check_orders_one_to_four_in_the_amplitude_on_a_null_plane
- kind: check
  ref: check.py::check_integrated_forms_in_the_parameter_s_and_in_the_area_parameter
- kind: check
  ref: check.py::check_exact_power_law_waves_and_the_area_as_a_clock
- kind: check
  ref: check.py::check_focusing_bound_and_exact_caustics
lineage:
  motivated_by:
  - synthesis.imported-raychaudhuri-null-congruence
  - synthesis.plane-wave-weak-null-crossing-null-shell-ambiguity
  - synthesis.premise-canonical-pair-on-the-two-null-directions
extraction:
  open_problem: op.gravitational-field-at-null-momentum
  note: >-
    Filed against op.gravitational-field-at-null-momentum, whose statement lists "anything beyond first order"
    as open and against which the first-order result on null-plane data is filed. What this result supplies is
    the classical half of that item on one null hypersurface: what the component of the field equation along
    the generators leaves free at any field strength (the shape history of the cross-section, equivalently the
    shear in a parameter built from the solution) and what it slaves to it (the area density, integrated
    explicitly once the shape is given in such a parameter), and an exact family of fields of any strength that
    realises every such shape history along a generator. The other components of the field equation on the
    hypersurface are not examined, so the result does not say that the shape history is the whole of the free
    data there. It does NOT
    settle anything quantum: no bracket, no states and no extension of Premise (TT) beyond first order are
    given, and the requirement of that problem (no signal outside the light cone) is not touched. It also bears
    on op.einstein-from-the-field-theory, but only as a consequence of the field equation: the hypotheses (E)
    and (P) are the K-K component of the equation obtained in
    synthesis.field-equation-linear-in-the-curvature-with-a-conserved-source-is-einsteins, and nothing here
    derives that equation. The store has no open problem on a clock or on time for the gravitational field;
    the nearest entries are the settled result on which boost flow is time
    (synthesis.phase-flow-is-time-rotor-flow-kms-continuation) and op.null-positivity-curved-horizons, which
    concerns the affine parameter of horizon generators as a state condition; clause (viii) is a classical
    relation between two parameters of one generator and says nothing on either. Kill conditions registered
    before computing and their outcome: (K1) the linear equation of clause (ii) fails on the exact plane wave
    at second order in the amplitude: did not fire (it holds at orders one to four and on waves that are not
    weak); (K2) an integrated form of clause (iii) fails at some order or on some exact strong-field example: did
    not fire; (K3) the plane wave is not an exact vacuum field in the stored conventions: did not fire; (K4)
    the null function of the wave is not null or not affinely parametrised: did not fire. Weaker than a reader
    might hope: the full characteristic initial value theorem is not proved and not claimed (clause (v) is a
    statement about one equation on one generator; clause (vi) realises a datum that is the same on every
    generator, because plane waves are homogeneous across their fronts); the bound of clause (iv) and the
    caustic of clause (vii) are the classical ones; in vacuum the odd orders of the area density in the
    amplitude vanish identically (a quarter turn about the generator reverses the sign of a trace-free
    profile), so the test at third order is vacuous for the vacuum wave and is made on a wave with matter.
    No imported Fact is a premise. The stored imported focusing equation
    (synthesis.imported-raychaudhuri-null-congruence) is not used: the focusing equation is taken from
    clause (iii) of the first-order result, where it is proved for gradients. Near-duplicates searched for and
    not found: no stored focusing bound, caustic statement or area-density equation; the stored plane-wave
    result (synthesis.plane-wave-weak-null-crossing-null-shell-ambiguity) holds the conformally flat plane
    waves in the Rosen gauge, whose Rosen factor a is the map E of clause (vi) for the pure-trace profile
    w = (a''/a) id (a wave with matter, not a gravitational wave), and it does not treat the shear. A link to the result on the second-order stress of the first-order field
    filed with this one (synthesis.second-order-stress-of-the-first-order-gravitational-field), not pinned here: on the plane wave of clause (vi) in the
    Kerr-Schild gauge the Einstein map is exactly linear in the profile (clause (vi)(a)), so its quadratic part
    vanishes identically there, although the wave focuses every null plane it crosses at second order; the
    change from that gauge to the transverse trace-free form of the first-order result is, by that companion
    computation, a displacement growing quadratically across the plane together with a change of rotation
    gauge. The Reading is worded to agree with this: the null energy of the wave is read from the focusing of
    the hypersurfaces, not from a local second-order term of the Einstein map.
    Decisions for the maintainer: (1) whether the result stays under op.gravitational-field-at-null-momentum
    or moves to op.einstein-from-the-field-theory, and whether either problem takes an attack item for the
    step this result does not take (a bracket on the shape history at any strength; the paper cited below
    proposes one); (2) whether the Limits paragraph of the first-order result, which says that beyond first
    order nothing is treated, is to cite this result for the classical part; (3) whether the stored Clausius
    derivation, whose hypothesis is vanishing shear and expansion at the point, takes a note citing clause
    (ii) for what the shear does to the area at second order; (4) whether clause (vi), the plane wave as an
    exact gravitational field in the Kerr-Schild gauge with its closed-form rotation-gauge field and a
    curvature equal to the stored first-order curvature with no correction, is to be split off as a result
    of its own, and whether lib/gtg.py takes a constructor for it (a change to the toolkit, not made here);
    (5) whether the store wants an open problem for the question clause (viii) does not answer, how a
    parameter built from the field along a generator relates to the flows the series calls time.
    Prior art, not premises. Read for this entity on 27 November 2026 through text extraction only:
    V. Chandrasekaran, arXiv:2611.34924 (its Section 3.2; the formulas quoted from it in the formal level
    are as extracted by a tool; a second, independent extraction made for review gave the same equations
    (3.25d), (3.25f) and (3.26a) to (3.26d); the typeset PDF was not read directly); the abstract page of L. Ciambelli,
    L. Freidel and R. G. Leigh, arXiv:2309.03932 (the dressing time); the abstract of A. N. Lasenby,
    arXiv:1912.05960 (plane gravitational waves in Gauge Theory Gravity, in a gauge whose reading is the
    Brinkmann line element; the field of clause (vi) was obtained here by direct computation and was not
    compared with that paper formula by formula). Bibliographic details verified on 27 November 2026 against
    publisher or index pages, the papers themselves not read: R. K. Sachs, J. Math. Phys. 3 (1962);
    R. Penrose, Rev. Mod. Phys. 37 (1965); A. D. Rendall, Proc. R. Soc. Lond. A 427 (1990). Cited from memory
    and not read: A. K. Raychaudhuri (1955) and R. K. Sachs (1961) for the focusing equation and the optical
    scalars; H. W. Brinkmann (1925) and H. Bondi, F. A. E. Pirani and I. Robinson (1959) for plane waves;
    R. P. Kerr and A. Schild (1965) for the form of the field; the textbook form of the focusing bound
    (S. W. Hawking and G. F. R. Ellis, 1973). The linear form of clause (ii) in the affine parameter and the
    area parameter of clause (iii) are in the paper that prompted this result; the linear form in the
    parameter with exponent one is, in an affine frame and up to a constant factor, the dressing time of
    Ciambelli, Freidel and Leigh; whether the parameter s
    of clause (iii) has a name in the literature was not established. No novelty is claimed for any clause;
    what is new to the store is the statement at any field strength in the series' variables, derived from
    the stored definition and the stored first-order result, the exact family in Gauge Theory Gravity with
    its checks, and the candid list of what one null hypersurface does not give. The paper's author is
    cited, not listed under credit, which names those who worked on this entry. Ledger: transport-absent.
---

## formal
Units $\hbar = c = 1$, $\Cl(1,3)$ with frame $e_{0}, e_{1}, e_{2}, e_{3}$, $Q(e_{0}) = 1$, $Q(e_{i}) = -1$, and a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) obeying the torsion equation of its clause (f), which fixes $\Omega$ from $\hb$. Only its clauses (i) to (e) and that torsion equation are used; the field equation of clause (f) is not assumed, and enters only through the two hypotheses (E) and (P) named below, each used only where it is named. The notation and the starting point are those of Theorem \claimref{synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators}(iii), proved there for every field obeying the torsion equation, weak or not, and not re-proved here: $A \cdot D = D_{\hb(A)}$ is the derivative along a physical vector; $\mathcal{R}$ is the curvature operator in the store's sign, with Ricci map $\mathcal{R}(b) = \partial_{a} \cdot \mathcal{R}(a \wedge b)$ and Einstein map $\mathcal{G}$; $\phi$ is a scalar field whose covariant gradient $K = \hb^{T}(\nabla\phi)$ is null, $Q(K) = 0$; $\mathsf{B}(A) = A \cdot D\,K$; the generators are the curves $dx/d\lambda = k$, $k = \hb(K)$, which rule each hypersurface of constant $\phi$ and have $\lambda$ as affine parameter; $\mathsf{B}$ induces on the screen (the physical vectors orthogonal to $K$, modulo $K$) a symmetric map with trace the expansion $\theta$ and trace-free part the shear $\sigma$, $\ip{\sigma}{\sigma} = \tr\sigma^{2} \geq 0$, and
\[
\frac{d\theta}{d\lambda} = -\tfrac12\,\theta^{2} - \ip{\sigma}{\sigma} + K \cdot \mathcal{R}(K) .
\]
A prime is $d/d\lambda$ along a generator. \emph{Hypotheses.} (E): $K \cdot \mathcal{R}(K) = 0$ along the generator. (P): $K \cdot \mathcal{R}(K) \leq 0$ along the generator. Since $Q(K) = 0$, $K \cdot \mathcal{G}(K) = K \cdot \mathcal{R}(K)$; so under the field equation $\mathcal{G}(a) + \Lambda a = -8\pi G\,T(a)$ (clause (f) of the Definition; Theorem \claimref{synthesis.field-equation-linear-in-the-curvature-with-a-conserved-source-is-einsteins}(vii) under its conditions) $K \cdot \mathcal{R}(K) = -8\pi G\,K \cdot T(K)$ whatever $\Lambda$ is: (E) is the one component of the field equation along the generator when no matter crosses the hypersurface, and (P) is the null energy condition $K \cdot T(K) \geq 0$, in the store's sign.
\begin{enumerate}
\item[(i)] \emph{(The area density $\rho^{2}$ and its root $\rho$; proved.)} Along a generator let $x_{1}, x_{2}$ be background vectors tangent to its hypersurface, $x_{i} \cdot \nabla\phi = 0$, and carried by the generators, $(k \cdot \nabla)x_{i} = (x_{i} \cdot \nabla)k$ (the separations of neighbouring generators at equal $\lambda$), with $x_{1} \wedge x_{2} \wedge k \neq 0$. Put $X_{i} = \hb^{-1}(x_{i})$ and
\[
\rho^{4} = -\bigl(\hb^{-1}(x_{1} \wedge x_{2})\bigr)^{2} = Q(X_{1})\,Q(X_{2}) - (X_{1} \cdot X_{2})^{2} > 0 .
\]
Then $X_{i} \cdot K = 0$, $K \cdot D\,X_{i} = \mathsf{B}(X_{i})$, and
\[
\frac{d\rho}{d\lambda} = \tfrac12\,\theta\,\rho :
\]
$\rho^{2}$, the \emph{area density}, is the area, measured with the physical vectors, of the cross-section element spanned by the two separations, the expansion is its logarithmic rate, $\theta = 2\rho'/\rho$, and $\rho$ is called the \emph{root area density}. Another pair multiplies $\rho$ by a constant along the generator, so ratios of $\rho$ along a generator belong to the field and the hypersurface (a generator lies on many null hypersurfaces, and $\rho$ depends on $\phi$). Minus the product is a positive symmetric form on the screen; let $G$ be its matrix in the basis $X_{1}, X_{2}$ of the screen (the Gram map of the two separations), with entries $-X_{i} \cdot X_{j}$ and $\det G = \rho^{4}$. Then $\bar q = G/\rho^{2}$, of determinant one, is the \emph{shape} of the cross-section, and $\bar q' = 2\,\bar q\,\sigma$ with $\sigma$ here the matrix, in the same basis, of the shear, a linear map of the screen, so that $\ip{\sigma}{\sigma} = \tfrac14\tr\bigl((\bar q^{-1}\bar q')^{2}\bigr)$: the shear is the rate of change of the shape.
\item[(ii)] \emph{(Focusing is linear in $\rho$; proved from clause (iii) of the cited theorem.)}
\[
\rho'' = -\tfrac12\bigl(\ip{\sigma}{\sigma} - K \cdot \mathcal{R}(K)\bigr)\,\rho, \qquad \text{and under (E)} \quad \rho'' = -\tfrac12\,\ip{\sigma}{\sigma}\,\rho .
\]
More generally, for a real $\alpha \neq -1$ and the parameter $\tau$ with $d\tau = \rho^{\alpha}\,d\lambda$, $d^{2}\rho^{1 + \alpha}/d\tau^{2} = -\tfrac{1 + \alpha}{2}\bigl(\ip{\sigma}{\sigma}_{\tau} - \rho^{-2\alpha}K \cdot \mathcal{R}(K)\bigr)\rho^{1 + \alpha}$, where $\ip{\sigma}{\sigma}_{\tau} = \rho^{-2\alpha}\ip{\sigma}{\sigma} = \tfrac14\tr\bigl((\bar q^{-1}d\bar q/d\tau)^{2}\bigr)$ is the square of the shear taken with $\tau$: the equation is linear in $\rho$ in the affine parameter ($\alpha = 0$) and linear in the area density $\rho^{2}$ in the parameter with $\alpha = 1$.
\item[(iii)] \emph{(Integration; proved.)} ($\alpha$) The excluded exponent. Let $ds = d\lambda/\rho$ and $e = d\ln\rho^{2}/ds = 2\rho'$. Then $de/ds = -\ip{\sigma}{\sigma}_{s} + \rho^{2}\,K \cdot \mathcal{R}(K)$ with $\ip{\sigma}{\sigma}_{s} = \rho^{2}\ip{\sigma}{\sigma} = \tfrac14\tr\bigl((\bar q^{-1}d\bar q/ds)^{2}\bigr)$, and under (E)
\[
e(s) = e_{0} - \int_{s_{0}}^{s}\ip{\sigma}{\sigma}_{s}\,dt, \qquad \rho^{2}(s) = \rho_{0}^{2}\exp\Bigl(e_{0}(s - s_{0}) - \int_{s_{0}}^{s}(s - t)\,\ip{\sigma}{\sigma}_{s}(t)\,dt\Bigr), \qquad \lambda(s) = \lambda_{0} + \int_{s_{0}}^{s}\rho\,dt ,
\]
on every stretch with $\rho > 0$, with no condition of monotonicity: the area density is an explicit exponential of the shear accumulated in the parameter $s$ and of the two constants $\rho_{0}$, $e_{0}$. The datum enters as a function of $s$ (or, in ($\beta$), of $\rho$), parameters built from the solution; given the shape as a function of $\lambda$, the formulas determine $\rho$ only implicitly, and $\lambda$ is recovered by the stated quadrature. ($\beta$) The area parameter. On a stretch where $p = \rho' \neq 0$, with $\rho$ as the parameter and $\ip{\sigma}{\sigma}_{\rho} = \ip{\sigma}{\sigma}/p^{2} = \tfrac14\tr\bigl((\bar q^{-1}d\bar q/d\rho)^{2}\bigr)$: $d(p^{2})/d\rho = -\rho\,\ip{\sigma}{\sigma}_{\rho}\,p^{2} + \rho\,K \cdot \mathcal{R}(K)$, and under (E)
\[
p(\rho) = p_{0}\,e^{-\Xi(\rho)}, \qquad \Xi(\rho) = \tfrac12\int_{\rho_{0}}^{\rho}r\,\ip{\sigma}{\sigma}_{r}\,dr, \qquad \lambda(\rho) = \lambda_{0} + \frac{1}{p_{0}}\int_{\rho_{0}}^{\rho}e^{\Xi(r)}\,dr .
\]
Form ($\beta$) under (E) is the formula of \cite{Chandrasekaran2026} (its equations (3.26), as extracted, in the paper's component notation, quoted: $\partial_{u}\varrho = p\,e^{-\Xi}$ with $\Xi = \tfrac18\int s\,(\partial_{s}\bar q)^{AB}\partial_{s}\bar q_{AB}\,ds$ in the ratio $v = \varrho/\varrho_{S}$); no difference from it was found. A second, independent extraction of the PDF made for review gave the same equations (3.25d), (3.25f), (3.26a) to (3.26d), with $\varrho$ the square root of the area density and $u$ affine; the typeset PDF was not read directly. What is added: the condition $p \neq 0$ under which it holds, form ($\alpha$), which does not need that condition, and the term for matter.
\item[(iv)] \emph{(The focusing bound; proved, given (P).)} Under (P), $\rho$ is a concave function of $\lambda$. If $\theta(\lambda_{0}) = \theta_{0} < 0$, then $\rho(\lambda) \leq \rho_{0}\bigl(1 - \tfrac12|\theta_{0}|(\lambda - \lambda_{0})\bigr)$ for $\lambda \geq \lambda_{0}$ as long as the generator stays where the field and $\phi$ are smooth with $\rho > 0$; so that cannot last beyond $\lambda_{0} + 2/|\theta_{0}|$: within that affine distance the stretch on which the field and $\phi$ are smooth and $\rho > 0$ ends: the generator leaves the region where they are defined or smooth, or $\rho \to 0$, a caustic. (That the stretch ends with $\rho \to 0$ whenever the field stays smooth is not proved here in general; it is proved for the plane waves in (vii).) Equality at $\lambda$ holds exactly when $\sigma = 0$ and $K \cdot \mathcal{R}(K) = 0$ on the stretch. Also $\rho'$ is non-increasing, so $\theta$ changes sign at most once along a generator, from positive to negative, and where $\rho$ is constant on an interval, $\sigma = 0$ and $K \cdot \mathcal{R}(K) = 0$ there.
\item[(v)] \emph{(The datum on one generator; proved.)} Under (E), on a stretch with $\rho > 0$, form ($\alpha$) of (iii) is a bijection between the triples $(\bar q(s), \rho_{0}, e_{0})$, $\bar q$ any smooth field of positive symmetric matrices of determinant one on an interval of $s$, $\rho_{0} > 0$ and $e_{0}$ real, and the pairs $(\rho(\lambda), \bar q(\lambda))$ that satisfy the equation of (ii), up to the origins of the two parameters. So the component of the field equation along the generators puts no condition on the shape history taken with $s$ (nor, on a stretch where $\rho$ is monotonic, on the shape history taken with $\rho$), and once the shape history is given it leaves two constants on each generator and nothing else: the shear is free and the expansion is slaved to it. Not claimed: that such data, given on every generator of a hypersurface and varying from one generator to the next, extend to a field without matter near it. That is the characteristic initial value theorem (Sachs \cite{Sachs1962}; Rendall \cite{Rendall1990}), which needs a second null hypersurface and the remaining components of the field equation, and is not proved here.
\item[(vi)] \emph{(Exact fields of any strength realising any shear history along a generator; proved.)} Let $n = e_{0} + e_{3}$, $\ell = \tfrac12(e_{0} - e_{3})$ ($Q(n) = Q(\ell) = 0$, $n \cdot \ell = 1$), write $x = (\ell \cdot x)\,n + (n \cdot x)\,\ell + y$ with $y$ in the span of $e_{1}, e_{2}$, and let $\mathsf{w}_{\lambda}$, $\lambda = \ell \cdot x$, be a smooth family of symmetric maps of that span, of any size, extended by $\mathsf{w}(n) = \mathsf{w}(\ell) = 0$. Put $W(x) = -y \cdot \mathsf{w}_{\lambda}(y)$.
\begin{enumerate}
\item[(a)] \emph{(The plane wave.)} $\hb(a) = a + \tfrac12 W\,(a \cdot \ell)\,\ell$ with $\Omega(a) = (a \cdot \ell)\;\ell \wedge \mathsf{w}_{\lambda}(y)$ is a gravitational field obeying the torsion equation, invertible everywhere ($\hb^{-1}(a) = a - \tfrac12 W\,(a \cdot \ell)\,\ell$, $\det\hb = 1$), with
\[
\mathcal{R}(B) = -\ell \wedge \mathsf{w}_{\lambda}(B \cdot \ell), \qquad \mathcal{R}(a) = (\tr\mathsf{w}_{\lambda})\,(a \cdot \ell)\,\ell ,
\]
exactly. The curvature operator is the first-order curvature of the cited theorem, $-\tfrac12\,p \wedge h(B \cdot p)$, at the null momentum $p = \ell$ and $h = 2\mathsf{w}$, with no correction at any order in $\mathsf{w}$; the Ricci map vanishes exactly when $\tr\mathsf{w} = 0$, and then the field satisfies (E) for every null gradient and the field equation without matter, for $\Lambda = 0$. (The derived metric reads $a \cdot b - W (a \cdot \ell)(b \cdot \ell)$.)
\item[(b)] \emph{(Its null hypersurfaces.)} Let $\mathsf{S}_{\lambda}$ be symmetric maps of the span of $e_{1}, e_{2}$ with $\mathsf{S}' = \mathsf{w} - \mathsf{S}^{2}$ on an interval. Then $\phi = n \cdot x + \tfrac12\,y \cdot \mathsf{S}_{\lambda}(y)$ has the null gradient $K = n + \mathsf{S}(y) + \tfrac12\bigl(y \cdot \mathsf{S}'(y) + W\bigr)\ell$, with $\ell \cdot \hb(K) = 1$: $\lambda = \ell \cdot x$ is the affine parameter. The vectors $m(e) = e - (K \cdot e)\,\ell$, $e$ in the span of $e_{1}, e_{2}$, are orthogonal to $K$, satisfy $m(e) \cdot m(e') = e \cdot e'$ and $K \cdot D\,m(e) = 0$, and $\mathsf{B}(m(e)) = m(\mathsf{S}(e))$: in the frame $m(e_{1}), m(e_{2})$ of the screen, orthonormal and parallel along each generator, the map of the screen is $\mathsf{S}$. So $\theta = \tr\mathsf{S}$, $\sigma$ is the trace-free part of $\mathsf{S}$, $K \cdot \mathcal{R}(K) = \tr\mathsf{w}$, $(K \wedge m(e')) \cdot \mathcal{R}(K \wedge m(e)) = -e' \cdot \mathsf{w}(e)$, and $\mathsf{S}' = \mathsf{w} - \mathsf{S}^{2}$ is the Riccati equation of clause (iii)(b) of the cited theorem. With $E' = \mathsf{S}E$, $E(\lambda_{0}) = \id$, the separations of the generators are $x_{i} = m(E(e_{i}))$, $G = E^{T}E$ and $\rho^{2} = |\det E|$. With $\mathsf{S}(\lambda_{0}) = 0$ the hypersurface touches the null plane $n \cdot x = \text{const}$ of the cited theorem along $\lambda = \lambda_{0}$ with the same expansion and shear, both zero, and it is that plane wherever $\mathsf{w}$ vanishes before $\lambda_{0}$: a null plane crossed by the wave.
\item[(c)] \emph{(Realisation.)} For every smooth family $\hat\sigma_{\lambda}$ of trace-free symmetric maps of the span of $e_{1}, e_{2}$, of any size, and every $\theta_{0}$, let $\theta$ solve $\theta' = -\tfrac12\theta^{2} - \tr\hat\sigma^{2}$, $\theta(\lambda_{0}) = \theta_{0}$, on its interval of existence, and put $\mathsf{w} = \hat\sigma' + \theta\,\hat\sigma$. Then $\tr\mathsf{w} = 0$, $\mathsf{S} = \tfrac12\theta + \hat\sigma$ satisfies $\mathsf{S}' = \mathsf{w} - \mathsf{S}^{2}$, and the hypersurface of (b) in the wave of (a), an exact field without matter, has in its parallel frame the shear $\hat\sigma_{\lambda}$ and the expansion $\theta$. Moreover every pair $(\rho(\lambda), \bar q(\lambda))$, smooth with $\rho > 0$, that satisfies the equation of (ii) under (E) is the root area density and the shape of such a hypersurface in such a wave.
\end{enumerate}
At first order in $\mathsf{w}$, with $\mathsf{S}(\lambda_{0}) = 0$: $\sigma = \int\mathsf{w}\,d\lambda$ and $\theta = 0$, the statement of the cited theorem, clause (iv) (the area does not respond); at second order $\theta = -\int\ip{\sigma}{\sigma}\,d\lambda$, where that statement gives no information. Limit of the family: the profile $\mathsf{w}_{\lambda}$, and with it the shear history, is the same on every generator of the hypersurface, a plane wave being unchanged by the displacements along its fronts; a shear history that varies from generator to generator is not realised here.
\item[(vii)] \emph{(A null plane crossed by a wave focuses; proved.)} In (vi) let $\mathsf{w}_{\lambda}$ be smooth on an interval $[\lambda_{0}, \lambda_{2}]$ with $\tr\mathsf{w} = 0$, let $\mathsf{S}(\lambda_{0}) = 0$, and suppose $\mathsf{w}$ does not vanish identically on $[\lambda_{0}, \lambda_{1}]$, $\lambda_{1} < \lambda_{2}$. Then either $\det E$ vanishes at some $\lambda_{c} \leq \lambda_{1}$, or $\theta(\lambda_{1}) \leq -\int_{\lambda_{0}}^{\lambda_{1}}\ip{\sigma}{\sigma}\,d\lambda < 0$ and, if $\lambda_{1} + 2/|\theta(\lambda_{1})| \leq \lambda_{2}$, $\det E$ vanishes at some $\lambda_{c} \leq \lambda_{1} + 2/|\theta(\lambda_{1})|$: the generators meet, at a place where the field itself is smooth, invertible and without matter. The same holds for a wave with matter obeying (P), $\tr\mathsf{w} \leq 0$, with $\ip{\sigma}{\sigma} - \tr\mathsf{w}$ in place of $\ip{\sigma}{\sigma}$.
\item[(viii)] \emph{(A clock from the field; the relations proved, the reading argued.)} Along a generator of a given null hypersurface the field fixes $\lambda$ up to $\lambda \mapsto a\lambda + b$ and $\rho$ up to $\rho \mapsto c\rho$ ($a, c > 0$), with no reference to the labels of the background. The ratio $v = \rho/\rho_{0}$ and the product $t = p_{0}(\lambda - \lambda_{0})/\rho_{0}$ are unchanged by both. Under (E), on a stretch with $p \neq 0$,
\[
t(v) = \int_{1}^{v}e^{\Xi(r)}\,dr, \qquad \Xi(v) = \tfrac12\int_{1}^{v}r\,\ip{\sigma}{\sigma}_{r}\,dr ,
\]
a functional of the shape history $\bar q(v)$ alone: the area ratio labels the cuts of the generator, and the shape read against it fixes the affine parameter elapsed between two cuts. For $v \geq 1$, $\Xi \geq 0$ and $t \geq v - 1$; for $v \leq 1$, $\Xi \leq 0$ and $|t| \leq 1 - v$: on a stretch where the area grows, shear lengthens the affine parameter needed to reach a given larger area, and on one where it falls, shear shortens the affine parameter needed to reach a given smaller area. Under (P) a generator has at most one stretch on which $\rho$ grows followed by at most one on which it falls, and $v$ is monotonic, hence a clock, on each. It is not a clock where $p = 0$: at the turning point, and on any interval on which $\rho$ is constant, where by (iv) no shear and no matter cross the hypersurface (for example a null plane where the field vanishes, or a stationary horizon); and it ends at a caustic. The parameter $s$ of (iii) is monotonic wherever $\rho > 0$, and under (P) $e$ is non-increasing in it, strictly decreasing where $\ip{\sigma}{\sigma}$ or $K \cdot \mathcal{R}(K)$ is not zero.
\end{enumerate}
\emph{Source of the idea.} That the free data of the gravitational field on a null hypersurface are the shape of its cross-sections, with the shear as its rate, that the area density is then fixed by the focusing equation, which becomes linear and integrates explicitly once the area is used as the parameter, and that the result is a clock carried by the field, is Section 3.2 of \cite{Chandrasekaran2026}, which does this on the null cones of a bounded region and goes on to a phase space, an operator for the clock and a space of states; none of that is done here. This result was prompted by that paper, takes the question from it, and reaches its integrated formula as form ($\beta$) of clause (iii); the derivations are made here from the stored definition and the stored first-order theorem, and the paper was read through text extraction only. The ideas are classical: the focusing equation is Raychaudhuri's \cite{Raychaudhuri1955} and the optical scalars Sachs's \cite{Sachs1961}; that the shear, or the conformal class of the cross-sections, is the free datum on a null hypersurface is Sachs's \cite{Sachs1962}, made a theorem by Rendall \cite{Rendall1990}; that a plane wave focuses the null hypersurfaces that cross it is Penrose's \cite{Penrose1965}; the parameter with $\alpha = 1$ in (ii), in which the area density obeys a linear equation, is, in an affine frame and up to a constant factor, the dressing time of \cite{CiambelliFreidelLeigh2024}; Gauge Theory Gravity is that of \cite{DoranLasenby2003}, and plane gravitational waves in it are treated in \cite{Lasenby2019}.

\emph{Reading (argued).} \emph{Beyond first order.} The first-order theorem says, in its limits, that beyond first order the trace is no longer free of the shear, and treats none of it. On one null hypersurface, and classically, this result does, for one equation: the component of the field equation along the generators leaves the shape history free, the area is slaved to it by that equation, which is linear in $\rho$ and integrates explicitly once the shape is given as a function of $s$ or of $\rho$, and nothing in that equation restricts the shape history. The other components of the field equation on the hypersurface are not examined here. By clause (vi) of that theorem $\ip{\sigma}{\sigma}/8\pi G$ is, at the leading order, the density of null energy of the two components of the first-order field; with the field equation, clause (ii) then reads $\rho'' = -4\pi G\,(\varepsilon + K \cdot T(K))\,\rho$ with $\varepsilon = \ip{\sigma}{\sigma}/8\pi G$: the root area density answers to the null energy of the wave as to that of matter. The equation is exact; calling $\varepsilon$ an energy density is the first-order identification and is not extended here, and it is not a statement about a local second-order term of the Einstein map: in the gauge of clause (vi) the Einstein map of the plane wave is exactly linear in the profile, so its quadratic part vanishes identically, while the hypersurfaces that cross the wave focus at second order. \emph{The plane wave.} The exact wave shows the two levels side by side: its curvature is the stored first-order curvature with no correction, linear in the profile, while the null hypersurfaces that cross it respond through the Riccati equation, which is not linear, and focus. A hypersurface of a field that vanishes can have shear as well (the case $a = -2$ of the check, a null hypersurface of the flat field whose generators meet on a line): the shear is a datum of the hypersurface in the field, and the part of it that belongs to the wave is $\mathsf{w} = \hat\sigma' + \theta\hat\sigma$, the curvature component of the shear equation. \emph{The clock.} Clause (viii) is a classical relation between two parameters that the field defines along one generator. It gives no flow on fields or states, no generator of such a flow and no modular structure, and it says nothing on which flow of the series is time (Theorem \claimref{synthesis.phase-flow-is-time-rotor-flow-kms-continuation} settles that for the boost flows of the boundary-mode algebra, a different question). It does say where a clock of this kind cannot exist: on a generator across which nothing passes. \emph{Limits.} One null hypersurface; a gradient, so no twist; classical throughout, with no bracket and no states, so Premise \claimref{synthesis.premise-canonical-pair-on-the-two-null-directions} is neither extended nor tested; no existence theorem for the field off the hypersurface; the realising family is homogeneous across the generators; $\Lambda$ does not enter clauses (i) to (v) and is zero in the vacuum reading of (vi).

## technical
The stored first-order result identifies the canonical data of the weak gravitational field on a null plane with the shear of the plane's generators, and proves, for a field of any strength, the focusing equation of a null congruence that is a gradient. This result builds on that one clause and asks what remains true on one null hypersurface when the field is not weak. It was prompted by \cite{Chandrasekaran2026}, which solves the focusing equation on null cones in terms of the shear and reads the solution as a clock.

The area density is defined from the gauge field: for two separations of neighbouring generators, the physical bivector over their outer product has a square, and minus that square is the square of the area density $\rho^{2}$; its root $\rho$ has logarithmic rate half the expansion. Substituting in the focusing equation removes the quadratic term: $\rho$ obeys a linear second-order equation whose coefficient is the square of the shear minus the Ricci term. The Ricci term is the one component of the field equation along the generator; without matter crossing the hypersurface it vanishes, and with matter of positive null energy it has the sign that focuses. These two cases are named hypotheses.

The equation integrates explicitly once the shape is given as a function of $s$ or of the area, parameters built from the solution; given the shape as a function of the affine parameter it remains a linear differential equation. In the parameter $s$ with $ds = d\lambda/\rho$ the logarithm of the area density has second derivative equal to minus the square of the shear, so the area density is an explicit exponential of a double integral of the shear and of two constants. With the area itself as the parameter, on a stretch where it is monotonic, the rate of the area is an exponential of an integral of the shear, which is the formula of the paper; no difference from that formula was found. A one-parameter family of such parameters makes the equation linear in a power of $\rho$; one member is, in an affine frame and up to a constant factor, the dressing time of \cite{CiambelliFreidelLeigh2024}.

Concavity of $\rho$ gives the classical bound: under the null energy condition, (P), a generator whose expansion is negative reaches a caustic, or leaves the region where the field and the hypersurface are smooth, within affine distance two over the magnitude of the expansion.

On one generator the shape history in the parameter $s$ is unrestricted by the equation, and two constants remain. That is the sense in which the shear is free and the expansion slaved. The characteristic initial value theorem, which would say that such data on a whole hypersurface determine a field, is not proved and not claimed.

An exact family realises every shear history along a generator at any strength: the plane wave in the Kerr-Schild gauge, whose rotation-gauge field has a closed form and whose curvature operator is exactly the stored first-order curvature of twice its profile at a null momentum. Its null hypersurfaces are given by a matrix Riccati equation, which is the Riccati equation of the first-order result in a parallel frame of the screen; any trace-free shear history is obtained by choosing the profile, the same on every generator, a plane wave being homogeneous across its fronts. A null plane crossed by such a wave, if the wave is smooth for long enough after it has begun to shear the plane, focuses to a caustic at a place where the field is smooth.

The area ratio, where it is monotonic, labels the cuts of a generator, and the shape history read against it determines the affine parameter elapsed. It fails as a clock where the area is stationary and ends at a caustic. This is a classical relation along one generator and makes no statement on the flows the series calls time.

Checked exactly with jets of the gauge fields on plane waves that are not weak (the shape and its rate computed from the gauge field), at orders one to four in the amplitude by interpolation, on exact power-law waves, and on exact caustics, one of them of a null plane crossed by a wave without matter.

Ledger: transport-absent. This is classical general relativity on a null hypersurface (Raychaudhuri, Sachs, Penrose), stated in the series' variables with exact checks.

## lay
Picture a thin bundle of light rays travelling side by side, and a small patch drawn across the bundle. Gravity can do two things to the patch as the rays travel: change its area, and change its shape without changing its area, squeezing a circle into an ellipse. The second effect is called shear, and it is what a passing gravitational wave does.

An earlier result in this collection showed that, for weak gravity, the shear on a surface swept out by light rays is exactly the freely choosable part of the gravitational field there. This result asks what happens when gravity is not weak.

The answer has three parts. First, one of Einstein's equations, the one along each ray, leaves the shape of the patch free and fixes how the area changes once the shape history is known. Second, that equation can be integrated explicitly. Written for the square root of the area it becomes a simple linear equation, and with the right way of marking position along the ray the area is given by a formula, an exponential of the accumulated shear. Third, shear always pulls rays together: once a bundle starts to converge it must come to a focus within a definite distance, provided any matter it meets has positive energy and the field around the rays extends that far.

There is an exactly solvable example, a plane gravitational wave of any strength. Light rays that were parallel before the wave arrived are bent by it and meet at a focus afterwards, and every possible history of squeezing along a ray can be produced by choosing the wave (the same history then holds on every ray of the surface).

Because the area changes in a way fixed by the shear, the area can serve as a clock along the ray: knowing the shape at each area tells you how far along the ray you are. The clock fails at the moment the area stops growing and starts to shrink, and wherever nothing crosses the surface; it ends at a focus.

The focusing equation, the role of shear and the focusing by plane waves are classical (Raychaudhuri, Sachs, Penrose, 1950s and 1960s); the integrated forms are recent. Here they are written in the collection's own language and checked exactly. The work was prompted by a 2026 paper by V. Chandrasekaran. It shows that one of Einstein's equations, along each ray, leaves the shape free and fixes the area from it; it does not show that the shape is all the data on the surface, or that such data determine gravity everywhere. It is not a quantum theory.

## one-liner
On a null hypersurface of a gravitational field of any strength, with $\rho^{4} = -(\hb^{-1}(x_{1} \wedge x_{2}))^{2}$ for two separations of the generators, $\theta = 2\rho'/\rho$ and the focusing equation of the first-order result becomes $\rho'' = -\tfrac12(\ip{\sigma}{\sigma} - K \cdot \mathcal{R}(K))\rho$; without matter crossing it integrates as $\rho^{2} = \rho_{0}^{2}\exp(e_{0}(s - s_{0}) - \int(s - t)\ip{\sigma}{\sigma}_{s}\,dt)$ in the parameter $ds = d\lambda/\rho$ and as $\rho' = p_{0}e^{-\Xi}$, $\Xi = \tfrac12\int r\ip{\sigma}{\sigma}_{r}\,dr$, with the area as parameter (agreeing, as far as a text extraction shows, with the paper that prompted it), so the component of the field equation along the generators leaves the shape history free and slaves the area to it with two constants per generator, a generator with $\theta < 0$ reaches a caustic within $2/|\theta|$ under the null energy condition, or leaves the region where the field and the hypersurface are smooth, and the area ratio is a clock where it is monotonic; the plane wave $\hb(a) = a + \tfrac12 W(a \cdot \ell)\ell$, whose curvature is exactly the stored first-order curvature, realises every shear history along a generator (the same on every generator) at any amplitude and focuses every null plane it crosses; the characteristic initial value theorem is not claimed.
