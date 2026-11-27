---
id: synthesis.corner-area-variation-of-a-null-plane-pair-is-the-charge-of-the-relative-boost
kind: claim
version: 1
title: "First-order corner charge of the relative boost of a null-plane pair"
status: proved
region: synthesis
subject: einstein
tags: [quantum-gravity, gauge-fields, curvature-and-field-equations, null-directions, horizons]
proposed_by:
  kind: ai
  session: 2026-11-27-null-surface-three
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction (the question, the instruction to derive the corner charge inside the graph from the stored symplectic current in place of the imported Noether-charge entropy, and to state everything in geometric algebra)
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
  - synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints@2
  - synthesis.modular-period-on-values-is-the-dual-plane-turn@5
  - synthesis.imported-null-plane-modular-hamiltonian-first-law@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_pairing_with_a_displacement_is_the_field_equation_plus_a_divergence
- kind: check
  ref: check.py::check_bivectors_bilinear_in_the_field_and_the_flow_with_one_derivative_are_six
- kind: check
  ref: check.py::check_corner_value_of_the_potential_is_the_transverse_trace
- kind: check
  ref: check.py::check_area_density_of_the_corner_from_the_position_gauge_field
- kind: check
  ref: check.py::check_flux_of_a_vacuum_field_against_the_corner_boost_is_a_pure_corner_term
- kind: check
  ref: check.py::check_corner_term_for_a_vacuum_field_found_by_elimination_and_off_the_solutions
- kind: check
  ref: check.py::check_boost_weighted_flux_through_the_half_plane_and_the_corner_by_two_routes
- kind: check
  ref: check.py::check_flux_of_the_boost_variation_is_the_quadratic_boost_generator
- kind: check
  ref: check.py::check_dual_of_the_boost_plane_is_the_corner_plane_and_the_periods
- kind: check
  ref: check.py::check_modular_hamiltonian_of_a_source_about_a_cut_against_the_area_combination
lineage:
  motivated_by:
  - synthesis.imported-wald-noether-charge-entropy
  - synthesis.c-loc-local-horizon-premise
  - synthesis.clausius-on-the-action-shell-ties-entropy-density-to-period
  - synthesis.einstein-equations-from-c-loc-and-clausius
extraction:
  open_problem: op.derive-loc-and-r-loc
  note: >-
    Filed against op.derive-loc-and-r-loc, on the maintainer's instruction of 27 November 2026 to derive, inside
    the graph and from the stored symplectic current, the statement that the store otherwise takes from the
    imported Noether-charge entropy (synthesis.imported-wald-noether-charge-entropy): that the charge of the
    boost at the edge of a horizon is the area over 8 pi G. That imported Fact is not a premise here and is not
    used. What is derived is its first order about the flat field, on the corner of a pair of null planes, with
    the constant of the stored first-order functional (clause (vi) of the first-order null-plane result, which
    takes it from the stored Newtonian coupling, its hypothesis (N)). Kill conditions registered before computing,
    and their outcome. (K1) "the boost generator obtained from the stored current is not a pure corner term":
    fires in its literal form and not in the form that is true. The stored current is bilinear in two first-order
    fields; the variation of the whole field under a flow is the displacement of the flat field, of order zero,
    plus the variation of the first-order field, of order one. For the exact boost the first part vanishes and
    the second gives a generator that is quadratic and a bulk term (clause (vi)(a)); for a flow that is the boost
    near the corner only, the first part gives, on solutions, a pure corner term (clause (iv)). The two are tied
    by the focusing equation (clause (vi)). (K2) "the corner term is not proportional to the first-order area
    variation": does not fire; the corner value is minus the trace over the corner plane, in every gauge. (K3)
    "the coefficient is not 1/(8 pi G)": does not fire; the magnitude is forced, and the sign is fixed by the
    orientation and by which plane is boosted against which, as clause (iv) states. What this supplies toward
    (Loc): the generator of the boost at the edge is local on the corner, with density the first-order change of
    the area density over 8 pi G, independent of the gauge up to a divergence along the corner under
    displacements along it (clause (ii)); the boost energy of matter at first order and the quadratic boost
    generator of the field at second order (not positive definite: the trace enters with the opposite sign)
    stand in the area balance of the half-plane with one coefficient, in an integrated form with its boundary
    terms, the first order by two routes that agree; and, given the imported null-plane modular Hamiltonian and a stated
    semiclassical hypothesis, the first-order entropy difference of the state on the half-plane is the area combination of the first law
    over 4 G, the
    value that synthesis.clausius-on-the-action-shell-ties-entropy-density-to-period obtains at leading order on
    its joint set. What it does not supply: the area itself (a first-order result gives its first variation, and
    a generator is fixed only up to a constant); anything on a background of nonvanishing field strength, so
    nothing on the curvature clause; anything on the Euler term (a charge obtained from the symplectic current
    does not see a term that is a divergence in the functional); the period 2 pi, which is taken from the
    imported Fact; a state or an entropy for the field's own two components; and (Loc) as a statement that
    the entropy of every cut is a multiple of its area, which stays a premise. Clause (vii)(b) pins the
    imported Fact synthesis.imported-null-plane-modular-hamiltonian-first-law and names it as imported; clauses
    (i) to (vi) pin no imported Fact. The past cone contains imported Facts that state the field equation
    (synthesis.imported-einstein-cartan-matter-coupling, hawking.imported-exterior-exactly-general-relativity
    with the two imported equivalence Facts, and synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians),
    through the pinned two-free-directions result, the first-order theorem and the dual-plane theorem. The
    clauses used here (the kernel of the stored Einstein map at null momentum, which is algebraic from the
    stored first-order curvature and is recomputed in the check; the current, flux, focusing equation and
    constant of the first-order theorem; the rotor identities of clauses (i) and (ii) of the dual-plane theorem,
    recomputed in the check) do not rest on them. synthesis.imported-wald-noether-charge-entropy is not in the
    past cone. No assumes edge is declared. Overlap inside this run, for the maintainer:
    clause (vi)(b), the focusing equation in area form in the gauge s(n) = 0, is a short consequence of clauses
    (iii) and (iv) of the first-order result and is the special case (generators along n, area density the
    square of its rho, same signs) of the general form proved by the result on null-surface data at any field
    strength filed with this one (synthesis.null-surface-data-at-any-field-strength-the-focusing-equation-integrated,
    not pinned here: clause (vi)(b) is proved in this entity on its own); clause (vi) uses only the null-null component
    of the second-order equation, through the focusing equation, and not the result on the second-order stress filed with
    this one (synthesis.second-order-stress-of-the-first-order-gravitational-field). Decisions for the maintainer: (1) whether the stored results that cite clause (b) of the imported
    Noether-charge Fact for the Einstein functional at first order are to cite clause (iv) here; (2) whether
    op.derive-loc-and-r-loc takes an attack item for the corner charge on a background of nonvanishing field
    strength (it needs the symplectic current at second order, which is not stored), as the form of the curvature
    clause that this route could reach; (3) whether hypothesis (S) of clause (vii)(b), the semiclassical source,
    is to be registered or kept local (it is kept local); (4) whether the argued paragraph on the weight is kept
    as a Reading or removed; (5) the sign convention of clause (iv): the store may prefer to name the relative
    boost so that its generator is plus the area variation over 8 pi G, as is done here; (6) whether clause
    (vi)(b) is to be re-pinned to the any-strength result. Prior art, not premises. Read for
    this entity only through its abstract and partial text extraction on 27 November 2026: V. Chandrasekaran,
    arXiv:2611.34924 (reference Chandrasekaran2026), which prompted the result. Cited from memory and not read
    for this entity: the Noether-charge form of horizon entropy and the first law (R. M. Wald, 1993; V. Iyer and
    R. M. Wald, 1994); the area of the horizon as the variable conjugate to the opening angle of the boost (S.
    Carlip and C. Teitelboim, 1995; title, journal and first page confirmed from the bibliography of the
    prompting paper as extracted, the last page, the arXiv number and the DOI from memory); corner charges of
    subregions (W. Donnelly and L. Freidel, 2016; same remark); the potential of a Killing field for the
    first-order field (L. F. Abbott and S. Deser, 1982; pages and DOI from memory); the first law for a process
    crossing a horizon (R. M. Wald, 1994; S. Gao and R. M. Wald, 2001); the thermal reading of the boost (J. J.
    Bisognano and E. H. Wichmann, 1975 and 1976; W. G. Unruh, 1976); the equation of state (T. Jacobson, 1995).
    No novelty is claimed for any clause: this is the linearised form of the standard covariant phase space
    result; what is new to the store is the derivation from the stored current in the series' variables, with the
    constant and the signs fixed and exact checks. Ledger: transport-absent.
---

## formal
Units $\hbar = c = 1$, $\Cl(1,3)$ with frame $e_{0}, e_{1}, e_{2}, e_{3}$, $Q(e_{0}) = 1$, $Q(e_{j}) = -1$, $I_{4} = e_{0}e_{1}e_{2}e_{3}$, and a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). The first-order setting is that of Theorem \claimref{synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators}, called the first-order theorem below, whose notation is kept: a first-order field $h$ of symmetric maps (the derived metric is $a \cdot b + h(a) \cdot b$, and $\hb^{-1} = \id + \tfrac12 h$ to this order), the pairing $\ip{h_{1}}{h_{2}}$, $\tau = \tr h$, $d = \dot h(\dot\nabla)$, the first-order Einstein map $\mathcal{E}[h]$, the symplectic current $\omega(h_{1}, h_{2})$ of its clause (i), with $\nabla \cdot \omega(h_{1}, h_{2}) = \ip{\mathcal{E}[h_{1}]}{h_{2}} - \ip{h_{1}}{\mathcal{E}[h_{2}]}$, the null vectors $n = e_{0} + e_{3}$, $\bar n = e_{0} - e_{3}$, the null plane $N = \{n \cdot x = 0\}$ with $x = \lambda n + y$, $\partial_{n} = n \cdot \nabla = \partial/\partial\lambda$, the gauge $h(n) = 0$, and in that gauge $\theta = \tfrac12\partial_{n}\tau$, $\sigma = \tfrac12\partial_{n}h^{TT}$. Dots mark the factor a derivative acts on. Of the Definition only its clauses (i) to (e) and the torsion equation of its clause (f) are used; the field equation of clause (f) is not assumed, except that clause (vi)(c) takes its null-null component as the named hypothesis (F); clauses (v), (vi)(c) at first order and (vii)(b) use the first-order field equation of clause (vi) of the first-order theorem, under that theorem's hypotheses (L), (D), (V), (N).

\emph{The pair and its corner.} Let $\bar N = \{\bar n \cdot x = 0\}$, with $x = \bar\lambda\,\bar n + y$ on it. The two null planes meet in the \emph{corner} $C = \{n \cdot x = \bar n \cdot x = 0\}$, the plane of $e_{1}, e_{2}$; $N_{+} = \{\lambda \geq 0\}$ and $\bar N_{+} = \{\bar\lambda \geq 0\}$ are the halves to the future of $C$. Let $B = e_{0}e_{3} = \tfrac12\,\bar n \wedge n$, the unit bivector of the plane of $n$ and $\bar n$, $B^{2} = 1$. The boost rotor $R_{\chi} = e^{-\chi B/2}$ gives $R_{\chi}nR_{\chi}^{\sim} = e^{\chi}n$, $R_{\chi}\bar nR_{\chi}^{\sim} = e^{-\chi}\bar n$ and fixes $C$ pointwise; the velocity of $x \mapsto R_{\chi}xR_{\chi}^{\sim}$ is $\xi_{B}(x) = x \cdot B$, with $a \cdot \nabla\xi_{B} = a \cdot B$, $\xi_{B} = \lambda n$ on $N$, $\xi_{B} = -\bar\lambda\,\bar n$ on $\bar N$ and $\xi_{B} = 0$ on $C$. For a symmetric map put $\tr_{\perp}h = \tau - n \cdot h(\bar n) = e^{1} \cdot h(e_{1}) + e^{2} \cdot h(e_{2})$, the trace over the corner plane.

\emph{Variations.} For a vector field $\xi$ let $\Delta_{\xi}(a) = a \cdot \nabla\xi + \nabla(\xi \cdot a)$, the derivatives on $\xi$: under the displacement $x \mapsto x - \epsilon\,\xi(x)$ of clause (e) of the Definition the first-order field of the flat field changes by $-\epsilon\,\Delta_{\xi}$ to first order in $\epsilon$ (its symbol is the displacement $a \mapsto (a \cdot p)\xi + (a \cdot \xi)p$ of the first-order theorem), and the first-order field $h$ by $-\epsilon\,(\Delta_{\xi} + \text{terms of first order in } h)$. The covariant action of the boost on a field, the transport of the argument together with the rotor on the frame (clause (e): the displacement by $x \mapsto R_{\chi}^{\sim}xR_{\chi}$ followed by the rotation gauge of rotor $R_{\chi}$), is $h(a; x) \mapsto R_{\chi}\,h(R_{\chi}^{\sim}aR_{\chi};\,R_{\chi}^{\sim}xR_{\chi})\,R_{\chi}^{\sim}$; it leaves the flat field unchanged, $\Delta_{\xi_{B}} = 0$, and its derivative at $\chi = 0$ is $-L_{B}h$, with
\[
L_{B}h(a) = (\xi_{B} \cdot \nabla)h(a) + B \cdot h(a) - h(B \cdot a) .
\]
The rate of change of the field along a flow is meant in the sense in which the null translation $\lambda \mapsto \lambda + t$ has the rate $\partial_{n}h$ in the first-order theorem (the derivative of the field along the flow; carrying the field forward has the opposite rate): for the flow of a vector field $\xi$ it is $\Delta_{\xi}$ at order zero in $h$, and for the exact boost it is $L_{B}h$, of order one.

\emph{Fluxes and generators.} For a window $W = \{0 \leq \lambda \leq \Lambda,\ y \in U\}$ of $N_{+}$ put $\Phi_{W}(h, k) = \int_{W} n \cdot \omega(h, k)\,d\lambda\,d^{2}y$, and likewise $\bar\Phi_{\bar W}$ on $\bar N_{+}$ with $\bar n$ and $d\bar\lambda\,d^{2}y$. The generator $H_{X}$ of a flow of the first-order field with rate $X$ is defined, with the orientation and the constant of clause (vi) of the first-order theorem, by $\delta H_{X} = \tfrac{1}{16\pi G}\,\Phi_{W}(\delta h, X)$; for the null translation, $X = \partial_{n}h$, this is $dP$ of that clause on the two components, up to terms on the cuts. For the pair, the generator of a flow is defined as the sum of the generators of its two halves; that is, the flux of the current through $N_{+}$ together with $\bar N_{+}$ is taken as the symplectic form of the pair (the light-front setting of the first-order theorem, not proved here).
\begin{enumerate}
\item[(i)] \emph{(The potential; proved.)} For every first-order field $h$ and every vector field $\xi$ put
\[
\Psi_{\xi}[h] = \xi \wedge (d - \nabla\tau) - \dot\nabla \wedge \dot h(\xi) + \dot\nabla \wedge h(\dot\xi) - \tfrac12\,\tau\,\nabla \wedge \xi ,
\]
a field of bivectors. Then, identically,
\[
\omega(h, \Delta_{\xi}) = 2\,\mathcal{E}[h](\xi) + \nabla \cdot \Psi_{\xi}[h] .
\]
The bivectors that are linear in a symmetric map and in two vectors and commute with the rotors form a space of dimension six (an exact count): the three built with the product and their duals, $I_{4}$ times them, and the three are the ones carried along by a reflection of the frame. So the six bivectors $\xi \wedge d$, $\xi \wedge \nabla\tau$, $\dot\nabla \wedge \dot h(\xi)$, $\dot\nabla \wedge h(\dot\xi)$, $\tau\,\nabla \wedge \xi$, $h(\partial_{a}) \wedge (a \cdot \nabla)\xi$ span the bivectors bilinear in $h$ and $\xi$ with one derivative that commute with the rotors and are even under reflection, and among their combinations $\Psi_{\xi}[h]$ is the only one for which the identity holds. So the pairing of a solution of $\mathcal{E}[h] = 0$ with a displacement is the divergence of a bivector: its flux through any hypersurface is a term on the boundary.
\item[(ii)] \emph{(The corner value; proved.)} Let $\xi$ vanish on $C$ with $a \cdot \nabla\xi = w\,a \cdot B$ there for every $a$, $w$ a function on $C$ (for instance $\xi = w\,\xi_{B}$ with $w$ any function on spacetime; $w = 1$ is the boost). Then on $C$, for every $h$, in every gauge and pointwise,
\[
B \cdot \Psi_{\xi}[h] = -\,w\,\tr_{\perp}h ,
\]
with $B \cdot \Psi$ the scalar part of the product. The displacement $\Delta_{\xi}$ itself vanishes on $C$, so the value is the same for $\omega + \nabla \cdot Y$ with $Y(h_{1}, h_{2})$ any bilinear bivector without derivatives. Under a displacement of the field, $\tr_{\perp}\Delta_{\zeta} = 2\,\nabla_{\perp} \cdot \zeta_{\perp}$, the divergence along $C$ of the part of $\zeta$ along $C$: the corner value does not change under displacements whose part along $C$ vanishes on $C$ (those that fix $C$ pointwise, and those that move it off itself along $n$ and $\bar n$), and changes by a divergence on $C$ otherwise.
\item[(iii)] \emph{(The area of the corner; proved.)} The physical bivector over the corner plane is $\hb^{-1}(e_{1}) \wedge \hb^{-1}(e_{2})$ (clause (a) of the Definition and the outermorphism of $\hb^{-1}$), and its size
\[
\mathsf{a} = \bigl(-\bigl(\hb^{-1}(e_{1}) \wedge \hb^{-1}(e_{2})\bigr)^{2}\bigr)^{1/2} = \bigl(g(e_{1}, e_{1})\,g(e_{2}, e_{2}) - g(e_{1}, e_{2})^{2}\bigr)^{1/2}
\]
is the physical area of the corner per unit area of the background, unchanged by the rotation gauge. To first order $\mathsf{a} = 1 + \mathsf{a}_{1}$ with $\mathsf{a}_{1} = \tfrac12\,\tr_{\perp}h$. So the corner value of (ii) is $-2\,w\,\mathsf{a}_{1}$.
\item[(iv)] \emph{(The charge of the boost at the corner; proved.)} Let $h$ satisfy $\mathcal{E}[h] = 0$, in any gauge, and let $\xi$ be as in (ii) near $C$. On $N$, for every bivector field, $n \cdot (\nabla \cdot \Psi) = \partial_{\lambda}(-B \cdot \Psi) + \nabla_{\perp} \cdot (\Psi \cdot n)_{\perp}$, so
\[
\Phi_{W}(h, \Delta_{\xi}) = \int_{U}(-B \cdot \Psi_{\xi}[h])\Big|_{\lambda = \Lambda}d^{2}y \;-\; 2\int_{U} w\,\mathsf{a}_{1}\,d^{2}y \;+\; (\text{flux of } (\Psi_{\xi}[h] \cdot n)_{\perp} \text{ through the sides of } W) ,
\]
with no term in the interior; off the solutions the right side gains $2\int_{W} n \cdot \mathcal{E}[h](\xi)$. If $\xi$ vanishes with its first derivatives on the far cut and on the sides,
\[
\frac{1}{16\pi G}\,\Phi_{W}(h, \Delta_{\xi}) = -\frac{1}{8\pi G}\int_{C \cap U} w\,\mathsf{a}_{1}\,d^{2}y .
\]
On $\bar N$, $\bar n \cdot (\nabla \cdot \Psi) = \partial_{\bar\lambda}(+B \cdot \Psi) + \nabla_{\perp} \cdot (\Psi \cdot \bar n)_{\perp}$, and the corner term of $\tfrac{1}{16\pi G}\bar\Phi_{\bar W}(h, \Delta_{\xi})$ is $+\tfrac{1}{8\pi G}\int w\,\mathsf{a}_{1}$. Hence, for the pair $N_{+} \cup \bar N_{+}$ and a flow that near $C$ is $w_{N}\,\xi_{B}$ on $N_{+}$ and $w_{\bar N}\,\xi_{B}$ on $\bar N_{+}$, and trivial far from $C$, the part of the generator linear in $h$ is
\[
H = \frac{1}{8\pi G}\int_{C}(w_{\bar N} - w_{N})\,\mathsf{a}_{1}\,d^{2}y .
\]
This is the generator of a flow that is the relative boost near $C$ and the identity away from it. For the exact boost of both halves the linear part vanishes identically ($\Delta_{\xi_{B}} = 0$), and the corner term enters only through the balance of (v), against the far cut and the matter flux. A flow differentiable across the corner has no corner term, only the relative rate enters (a flow with $w_{\bar N} \neq w_{N}$ on $C$ is not the displacement by one vector field: it acts on the data of the two halves separately), and for the \emph{relative boost} of the pair at unit rate ($w_{\bar N} - w_{N} = 1$: the flow $x \mapsto R_{\chi}xR_{\chi}^{\sim}$ near $C$ on $\bar N_{+}$ and the identity on $N_{+}$, under which $\bar n \mapsto e^{-\chi}\bar n$ at fixed $n$ and $n \cdot \bar n$ decreases as $e^{-\chi}$), cut off away from $C$, the part of the generator linear in $h$ is the first-order area of the corner over $8\pi G$, $\delta A/8\pi G$ with $\delta A = \int_{C}\mathsf{a}_{1}\,d^{2}y$; for the opposite sense it is $-\delta A/8\pi G$, and for a rate depending on the point of $C$ the density $\mathsf{a}_{1}/8\pi G$ enters with that rate as weight. The magnitude $1/8\pi G$ is twice the constant $1/16\pi G$ of the stored current, which the first-order theorem fixes under its (L), (D), (V), (N); given that constant it is not adjustable; the sign is fixed by the orientation of the first-order theorem and by which half is carried against which.
\item[(v)] \emph{(The exact boost and the first law; proved, the form with a source given (L), (D), (V), (N) of the first-order theorem.)} Since $\Delta_{\xi_{B}} = 0$, clause (i) gives $\nabla \cdot \Psi_{\xi_{B}}[h] = -2\,\mathcal{E}[h](\xi_{B})$ for every $h$: on $N$,
\[
\partial_{\lambda}\bigl(-B \cdot \Psi_{\xi_{B}}[h]\bigr) + \nabla_{\perp} \cdot (\Psi_{\xi_{B}}[h] \cdot n)_{\perp} = -2\,\lambda\,n \cdot \mathcal{E}[h](n) .
\]
In the gauge $h(n) = 0$, on $N$: $-B \cdot \Psi_{\xi_{B}}[h] = \tau - \lambda\,\partial_{n}\tau$, the second term on the left vanishes, and the law is $\lambda$ times the first-order focusing equation $\partial_{n}\theta = n \cdot \mathcal{E}[h](n)$ of clauses (ii) and (iv) of the first-order theorem, integrated once: the route through the symplectic current and the route through the focusing equation agree identically. With the first-order field equation with a source, $\mathcal{E}[h] + 8\pi G\,T = 0$ (clause (vi) of the first-order theorem, under its hypotheses (L), (D), (V), (N)), and $\mathsf{a}_{1} = \tfrac12\tau$ in the gauge, on each generator
\[
\int_{0}^{\Lambda}\lambda\;n \cdot T(n)\,d\lambda = \frac{1}{8\pi G}\Bigl(\bigl(\mathsf{a}_{1} - \lambda\,\partial_{\lambda}\mathsf{a}_{1}\bigr)\Big|_{\lambda = \Lambda} - \mathsf{a}_{1}\Big|_{\lambda = 0}\Bigr) :
\]
the boost energy that crosses $N_{+}$ is the area of the far cut, continued back to the corner along its tangent, less the area of the corner, over $8\pi G$. In any gauge the same holds after integration over $U$, with $-\tfrac12 B \cdot \Psi_{\xi_{B}}[h]$ in place of $\mathsf{a}_{1} - \lambda\,\partial_{\lambda}\mathsf{a}_{1}$ and the flux through the sides. The same holds about any cut $\lambda = \lambda_{0}$ of $N$ in place of the corner, with $\lambda - \lambda_{0}$ in place of $\lambda$ and the integral from $\lambda_{0}$ (the flat field is unchanged by the translations along $n$).
\item[(vi)] \emph{(Second order: the quadratic boost generator; (a) and (b) proved, (c) proved given (F).)}
\begin{enumerate}
\item[(a)] If $h(n) = 0$ then $L_{B}h(n) = 0$, and on $N$
\[
n \cdot \omega(h, L_{B}h) = 4\lambda\bigl(\ip{\sigma}{\sigma} - \tfrac12\theta^{2}\bigr) - \tfrac12\,\partial_{\lambda}\Bigl(\lambda\bigl(\ip{h}{\partial_{n}h} - \tau\,\partial_{n}\tau\bigr)\Bigr) .
\]
So the generator of the exact boost on a window of $N_{+}$, which is quadratic, $H^{(2)} = \tfrac{1}{32\pi G}\Phi_{W}(h, L_{B}h)$ (its variation is $\tfrac{1}{16\pi G}\Phi_{W}(\delta h, L_{B}h)$ up to a term on the far cut), is $\tfrac{1}{8\pi G}\int_{W}\lambda\,(\ip{\sigma}{\sigma} - \tfrac12\theta^{2})$ less a term on the far cut, with no term on the corner: the null energy density $\ip{\sigma}{\sigma}/8\pi G$ of the first-order theorem with the boost weight, the trace entering with the opposite sign. It is the boost-weighted null energy of the two components plus a trace term of the opposite sign; it is not positive definite unless $\theta = 0$ (on vacuum first-order fields in the gauge $\theta$ is constant along each generator). It is a term in the interior, not a corner term. The flow $L_{B}$ carries solutions to solutions and displacements to displacements.
\item[(b)] Let $\hb^{-1} = \id + s$ with $s$ a field of symmetric maps and $s(n) = 0$, of any size, and $\Omega$ fixed by the torsion equation, so that the generators of $N$ run along $n$ with expansion $\theta$ and shear $\sigma$ (clauses (iii) and (iv) of the first-order theorem). Then $\theta = \partial_{\lambda}\ln\mathsf{a}$ and
\[
\partial_{\lambda}^{2}\mathsf{a} = \mathsf{a}\,\bigl(\tfrac12\theta^{2} - \ip{\sigma}{\sigma} + n \cdot \mathcal{R}(n)\bigr) .
\]
\item[(c)] Assume (F): on $N$ the field obeys $n \cdot \mathcal{R}(n) = -8\pi G\;n \cdot T(n)$, the equation of Theorem \claimref{synthesis.field-equation-linear-in-the-curvature-with-a-conserved-source-is-einsteins}(vii) contracted twice with $n$ (the term in $\Lambda$ drops, $Q(n) = 0$), taken here as a hypothesis. Then, exactly, on each generator
\[
\bigl(\mathsf{a} - \lambda\,\partial_{\lambda}\mathsf{a}\bigr)\Big|_{\lambda = \Lambda} - \mathsf{a}\Big|_{\lambda = 0} = \int_{0}^{\Lambda}\lambda\,\mathsf{a}\,\bigl(\ip{\sigma}{\sigma} - \tfrac12\theta^{2} + 8\pi G\;n \cdot T(n)\bigr)\,d\lambda .
\]
For a family $\hb^{-1} = \id + \epsilon s_{1} + \epsilon^{2}s_{2} + \dots$ in this gauge with $T = \epsilon T_{1} + \epsilon^{2}T_{2} + \dots$, the order $\epsilon$ is the first law of (v), and at order $\epsilon^{2}$
\[
\frac{1}{8\pi G}\Bigl(\bigl(\mathsf{a}_{2} - \lambda\,\partial_{\lambda}\mathsf{a}_{2}\bigr)\Big|_{\Lambda} - \mathsf{a}_{2}\Big|_{0}\Bigr) = \int_{0}^{\Lambda}\lambda\,\Bigl(\frac{\ip{\sigma}{\sigma} - \tfrac12\theta^{2}}{8\pi G} + n \cdot T_{2}(n) + \mathsf{a}_{1}\,n \cdot T_{1}(n)\Bigr)d\lambda ,
\]
with $\sigma$, $\theta$ those of the first-order field $h = 2s_{1}$ (the coefficients of $\epsilon$ in the shear and the expansion). So without matter the quadratic generator of (a) equals, on solutions, the second-order area of the far cut continued back to the corner, less that of the corner, over $8\pi G$, up to its own term on the far cut: at second order the quadratic generator of (a) stands in the area balance with the coefficient $8\pi G$ of matter, and the relation between the generator and the area of the corner is that of (v). Clause (c) has no check of its own; it is the combination of (a) and (b).
\end{enumerate}
\item[(vii)] \emph{(The period; (a) proved, (b) proved given the imported Fact and (S).)}
\begin{enumerate}
\item[(a)] $I_{4}B = e_{1}e_{2} = B^{*}$: the dual of the boost plane is the corner plane itself, $(B^{*})^{2} = -1$, and $B^{*}$ commutes with $B$. By Theorem \claimref{synthesis.modular-period-on-values-is-the-dual-plane-turn}(i), on even values the boost rotor continued to the rapidity $\chi + I_{4}\varphi$ is $e^{-\chi B/2}e^{-\varphi B^{*}/2}$, the second factor being the real rotor of the corner plane; no unit other than $I_{4}$ enters. That rotor fixes $n$ and $\bar n$ and turns the corner in itself by $\varphi$; acting on a first-order field by $h \mapsto e^{-\varphi B^{*}/2}h(e^{\varphi B^{*}/2}a\,e^{-\varphi B^{*}/2})e^{\varphi B^{*}/2}$ it leaves $\tr_{\perp}h$ and the block of $n, \bar n$ unchanged, turns the two transverse trace-free components by $2\varphi$ (clause (viii) of the first-order theorem) and the components that mix the corner with $n, \bar n$ by $\varphi$. At $\varphi = \pi$ it is $-B^{*}$: the identity on the first and $-1$ on the last. At $\varphi = 2\pi$ it is $-1$: the identity on every vector and every map, and $-1$ on spinor values. On points the continued boost is not a rotor of $\Cl(1,3)$ (clause (ii) of that theorem).
\item[(b)] Assume, with the imported Fact \claimref{synthesis.imported-null-plane-modular-hamiltonian-first-law} (imported: Wall, after Bisognano and Wichmann, and Casini, Teste and Torroba), that matter is a free quantum field whose vacuum $\omega_{0}$ restricted to the algebra of $N_{+}$ has the modular Hamiltonian $2\pi\int\!\!\int_{0}^{\infty}\lambda\;n \cdot T(n)\,d\lambda\,d^{2}y$ (its clause (i), with $u = \lambda$ and $T_{uu} = n \cdot T(n)$), and assume (S), semiclassical coupling at first order: the first-order field solves the equation of (v) (hence under (L), (D), (V), (N)) with source the expected stress $\rho(T) - \omega_{0}(T)$, supported in $0 < \lambda < \Lambda$, $y \in U$, for a state $\rho$ with $S(\rho\,\|\,\omega_{0})$ finite and finite $\Delta\langle K\rangle$, $K$ the boost energy $\int\!\!\int_{0}^{\infty}\lambda\;n \cdot T(n)$. (S) is not a consequence of any stored result. Then by clause (iii) of that Fact and (v), in the gauge $h(n) = 0$,
\[
\Delta S = \frac{1}{4G}\int_{U}\Bigl(\bigl(\mathsf{a}_{1} - \lambda\,\partial_{\lambda}\mathsf{a}_{1}\bigr)\Big|_{\Lambda} - \mathsf{a}_{1}\Big|_{0}\Bigr)d^{2}y \;-\; S(\rho\,\|\,\omega_{0}) ,
\]
so the entropy difference $\Delta S$ of $\rho$ on the algebra of $N_{+}$ (clause (iii) of the Fact) is the area combination of (v) over $4G$ at first order in $\rho - \omega_{0}$, and at most that always: the period $2\pi$ times the corner coefficient $1/8\pi G$ is $1/4G$. The same holds about any cut of $N_{+}$, by the last sentence of (v) and the Fact's statement for every cut.
\end{enumerate}
\end{enumerate}
\emph{Source of the idea.} That the area of the corner where two null hypersurfaces meet, over $8\pi G$, is the variable conjugate to the relative boost of the two, and that the full period of the continued boost then weights a corner of area $A$ by $e^{-A/4G\hbar}$, is taken from \cite{Chandrasekaran2026}, which builds the phase space of the full theory on intersecting null cones; this result was prompted by that paper and takes the question from it. The idea is classical: the entropy of a horizon is $2\pi$ times the Noether charge of the boost that fixes its edge \cite{Wald1993, IyerWald1994}; the area of the edge and the Euclidean opening angle at the horizon are conjugate \cite{CarlipTeitelboim1995}; the corner of a subregion carries charges of this kind \cite{DonnellyFreidel2016}; the potential of clause (i) plays, for a field that preserves the flat product, the role of the Abbott-Deser potential of the conserved charges of the first-order field \cite{AbbottDeser1982} (not compared term by term here); and the thermal reading of the boost is that of \cite{BisognanoWichmann1976} and \cite{Unruh1976}. What is done here is the first order about the flat field on a pair of null planes, and the second order through the focusing equation, in the series' variables and from the stored current; the paper was read through its abstract and partial text extraction only, and none of its formulas is used.

\emph{Reading (argued).} \emph{Which generator is a corner term.} The stored current pairs two first-order fields. Paired with the displacement of a flow that is the boost near the corner, it gives the first-order area of the corner, (iv). Paired with the variation of the field under the exact boost, it gives the quadratic boost generator of (vi)(a), a term in the interior. The two are one statement at successive orders: for the exact boost the part of the generator linear in $h$ vanishes identically, because $\Delta_{\xi_{B}} = 0$; what the identity of (i) then gives is a balance: what crosses the half-plane (the boost energy of matter at first order and, given (F), the quadratic boost generator of the field at second order) equals the difference of the area terms at its two ends over $8\pi G$, (v) and (vi)(c). \emph{The weight.} Suppose (not proved here, and not a premise of the store) that in a quantisation of the half-plane the state is of the kind of (vii)(b) for the whole generator of the boost, the corner term included. Its density operator then carries the factor $e^{-2\pi H/\hbar}$ with $H$ the generator of the future-directed boost on $N_{+}$, whose corner term by (iv) is $-\delta A/8\pi G$, so the factor is $e^{+\delta A/4G\hbar}$; for the relative boost in the sense of (iv) it is $e^{-\delta A/4G\hbar}$ (the weight in the paper is of this second form, with the area in place of its first variation, as far as its text was read). The magnitude of the exponent is fixed by (iv) and the period, the sign by the sense; half a period, which carries one half of a generator to the other, gives the square root, with $1/8G\hbar$ in the exponent. The units of the formal clauses are $\hbar = 1$; $\hbar$ is restored in this paragraph and in the paragraph on the source of the idea. This is a first-order statement about $\delta A$: the area itself is not reached, and a generator is defined up to a constant. For the two components of the field no state is selected here or in the first-order theorem, so no entropy is assigned to them, and the quadratic generator of (vi)(a) is not positive definite. \emph{The entropy clause.} For Premise \claimref{synthesis.c-loc-local-horizon-premise}: (iv) shows that at first order about the flat field the charge of the boost at the edge is local on the edge, with density the change of the area density over $8\pi G$, independent of the gauge up to a divergence along the corner under displacements along it (clause (ii)); the curvature is itself of first order there, so a dependence of the density on the curvature would be of second order and is not seen; a term that is a divergence in the functional, the Euler term among them, does not change the symplectic current and so is not seen either. With (vii)(b) the coefficient of the area combination in the entropy difference of the state on the half-plane is $1/4G$, the value Theorem \claimref{synthesis.clausius-on-the-action-shell-ties-entropy-density-to-period}(i) finds at leading order on its joint set; here it is obtained on a finite window with its boundary terms. That the entropy of every cut is a multiple of its area is not derived. \emph{Limits.} First order about the flat field, and second order only through the null-null component of the field equation; flat null planes; the gauge $h(n) = 0$ for (v) in its form on each generator, for (vi) and for (vii)(b); the light-front setting of the first-order theorem for calling the flux a generator. The corner is a plane of the background, of infinite area: the statements are on windows and with weights.

## technical
The store takes from the literature that the entropy of a horizon is the Noether charge of the boost that fixes its edge, which for Einstein's theory is a quarter of the area. This result derives the classical statement behind it, to first order, from the store's own symplectic current of the first-order gravitational field, with no import. It was prompted by \cite{Chandrasekaran2026}, where the area of the corner of two null cones is the variable conjugate to their relative boost.

Two null planes of flat spacetime meet in a spacelike plane, the corner. The boosts of the plane of the two null directions fix the corner pointwise and stretch one null direction while shrinking the other. The stored current pairs two first-order fields. The rate of change of the whole field under a flow has two parts: the displacement of the flat field, which does not involve the first-order field, and the variation of the first-order field. The exact boost, with its rotor, is a symmetry of the flat field, so its first part is zero.

The first result is an identity: the current paired with the displacement of any vector field equals twice the first-order Einstein map applied to the field, plus the divergence of an explicit bivector. So on solutions the pairing with a displacement is a boundary term. For a vector field that is the boost near the corner, the bivector's value on the corner is minus the trace of the first-order field over the corner plane, in every gauge. The physical area of the corner, defined from the position-gauge field as the size of the physical bivector over the corner plane, changes at first order by half that trace. So the corner term is the first-order change of the corner's area over $8\pi G$, the factor being twice the stored $1/16\pi G$. Its sign is opposite on the two half-planes, so a flow that is smooth across the corner has no corner term and only the relative boost of the two planes has one. This is the part linear in the field of the generator of a flow that is the relative boost near the corner and the identity away from it, the generator of the pair being defined as the sum over its two halves; for the exact boost of both halves the linear part vanishes identically.

For the exact boost the same identity is a conservation law. Integrated over the half-plane to the future of the corner it says that the boost energy of matter crossing it equals the area of the far cut, continued back along its tangent, less the area of the corner, over $8\pi G$. In the light-cone gauge this is the first-order focusing equation of the stored null-plane result multiplied by the distance from the corner and integrated once; the two derivations agree identically.

The pairing with the variation of the field under the exact boost is a different object: the quadratic boost generator, an integral over the half-plane of the stored null energy density of the two transverse trace-free components with the boost weight, together with a trace term of the opposite sign, which is the square of the expansion in the focusing equation; it is not positive definite unless the expansion vanishes. Written for the area density, the focusing equation has exactly this combination as its source, so the quadratic generator equals the second-order area combination of (v) (the far cut continued back, less the corner) over $8\pi G$, given the null-null field equation at second order, with the coefficient of matter.

Continued to an angle, the boost rotor becomes on values the rotor of the dual plane, by a stored result; the dual plane is the corner plane itself. A full turn is the identity on vectors and maps. With the imported statement that the vacuum of a free field on a half null plane is thermal for the boost at period $2\pi$, and the assumption that the first-order field is sourced by the expected stress, the entropy difference of the state on the half-plane, vacuum subtracted, is the area combination of the first law over $4G$ at first order, and at most that.

Assumed and not proved: the first-order field equation with its constant, under the conditions of the stored null-plane result; for the second order, the null-null component of the field equation; for the entropy statement, the imported Fact and the semiclassical source. The weight of a corner of given area in a quantum state is argued, not proved. The area itself is not reached, only its first variation and its second-order combination; nothing is said for a background of nonvanishing field strength.

Ledger: transport-absent. This is the linearised form of the covariant phase space account of horizon charges, in the series' variables, with exact checks.

## lay
Picture two walls of light crossing each other in empty space. Where they cross there is an ordinary flat surface, the corner. One can slide one wall against the other without moving the corner: this is a boost, the change of view between two observers in relative motion, done on one wall and not the other.

In mechanics every such motion has a quantity that generates it, as momentum generates shifts and angular momentum generates turns. The question here is what generates the sliding of the two walls. The literature gives the answer for gravity at full strength: it is the area of the corner, divided by eight pi times Newton's constant. The series had taken a closely related statement on trust. Here it is worked out from the series' own description of weak gravity.

The outcome has three parts. First, when weak gravity slightly changes the area of the corner, that change of area, divided by eight pi times Newton's constant, is exactly the quantity that generates a sliding done near the corner and fading out away from it. The number is not adjustable: it is twice a constant fixed earlier by Newton's law of attraction. Second, when matter crosses one of the walls, the energy it carries, counted with a weight that grows with distance from the corner, equals the area at the far end, as it would be if continued back along the light rays to the corner, less the area at the corner, in the same units. Third, given the field equation at second order, gravitational waves crossing the wall count with the same coefficient as matter, one order further on, together with a term from the expansion of the light rays that enters with the opposite sign.

Why it matters: the entropy of a black hole is a quarter of the area of its horizon, and the reason usually given is that the horizon's area plays precisely this role for the boost at its edge, which is tied to temperature. Combining the result with the known thermal behaviour of the vacuum gives back the quarter, for small changes of area.

What it does not do: it gives changes of area, not the area itself; it holds for weak gravity around empty flat space; and the step from the quantity that generates the sliding to a count of quantum states is argued, not proved. The work was prompted by a 2026 paper by V. Chandrasekaran; the idea goes back to work of the 1990s by Wald, Iyer, Carlip and Teitelboim.

## one-liner
For first-order fields on flat spacetime the stored symplectic current obeys $\omega(h, \Delta_{\xi}) = 2\mathcal{E}[h](\xi) + \nabla \cdot \Psi_{\xi}[h]$ with an explicit bivector $\Psi$ whose value on the corner of the null planes $n \cdot x = 0$, $\bar n \cdot x = 0$, for a flow that is the boost $x \cdot B$ there, is $-\tr_{\perp}h$, minus twice the first-order change of the corner's area density defined from $\hb$; so on solutions the part linear in $h$ of the generator of a flow that is the relative boost of the two half-planes near the corner, and trivial away from it, is $\delta A/8\pi G$ (sign by the sense, magnitude forced by the stored $1/16\pi G$), for the exact boost the same identity is the first law $\int\lambda\,n \cdot T(n) = (\text{area of the far cut continued back} - \text{area of the corner})/8\pi G$, equal by a second route to the integrated focusing equation, the quadratic boost generator $\tfrac{1}{8\pi G}\int\lambda(\ip{\sigma}{\sigma} - \tfrac12\theta^{2})$ is, given the null-null field equation at second order, the second-order part of the same area combination over $8\pi G$, and with the imported thermal period $2\pi$ the vacuum-subtracted entropy of the state on $N_{+}$ is (area of the far cut continued back less area of the corner)$/4G$ at first order, and at most that: the first-order content of the imported Noether-charge entropy, derived from the stored current.
