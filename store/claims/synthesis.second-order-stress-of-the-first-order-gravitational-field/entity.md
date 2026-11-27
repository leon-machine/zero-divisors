---
id: synthesis.second-order-stress-of-the-first-order-gravitational-field
kind: claim
version: 1
title: 'The second-order stress of the first-order gravitational field'
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
  role: direction (the question, the clauses to establish and their order, the kill conditions, the instruction to work from the stored results and to state everything in geometric algebra)
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
  - synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_first_order_part_is_the_stored_einstein_map_and_is_blind_to_the_rotation_gauge
- kind: check
  ref: check.py::check_quadratic_part_is_symmetric_and_its_divergence_off_solutions
- kind: check
  ref: check.py::check_quadratic_part_is_conserved_on_a_first_order_solution
- kind: check
  ref: check.py::check_quadratic_part_is_conserved_on_a_second_solution_with_other_data
- kind: check
  ref: check.py::check_displacement_changes_the_quadratic_part_by_the_first_order_map_of_a_quadratic_field
- kind: check
  ref: check.py::check_rotation_gauge_and_parametrisation_change_the_quadratic_part_the_same_way
- kind: check
  ref: check.py::check_first_order_einstein_map_is_the_divergence_of_a_bivector
- kind: check
  ref: check.py::check_null_null_component_in_the_light_cone_gauge_is_the_square_of_the_shear
- kind: check
  ref: check.py::check_null_null_identity_holds_in_the_light_cone_gauge_off_solutions
- kind: check
  ref: check.py::check_plane_wave_in_the_kerr_schild_gauge_has_no_quadratic_part
- kind: check
  ref: check.py::check_one_plane_wave_has_the_quadratic_part_along_its_momentum
- kind: check
  ref: check.py::check_dust_falling_in_its_own_field_is_balanced_by_the_quadratic_part
lineage:
  motivated_by:
  - synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators
  - synthesis.field-equation-linear-in-the-curvature-with-a-conserved-source-is-einsteins
  - synthesis.vacuum-field-stress-tensor-is-einstein-tensor-or-trace
extraction:
  open_problem: op.einstein-from-the-field-theory
  note: >-
    Filed against op.einstein-from-the-field-theory, as the second order of the two results stored on 26
    November 2026: the first-order result on a null plane
    (synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators), whose
    Reading says, as an argued remark, that the two free components gravitate through their null energy as
    matter does, and the derivation of the field equation under two named conditions
    (synthesis.field-equation-linear-in-the-curvature-with-a-conserved-source-is-einsteins). Route: every
    clause is the second order of a stored statement. Clause (ii) is the symmetry of the Ricci map (clause (ii)
    of the second result), clause (iii) the contracted identity (its clause (iii)), clause (iv) the gauge
    freedoms of clause (e) of the stored definition, clause (vi) the focusing equation (clause (iii) of the
    first result) in the gauge of its clause (iv). The quadratic part of the Einstein map is never written out
    in closed form; the checks compute it exactly from the gauge fields, with the expansion parameter carried
    as a truncated polynomial in the coefficients of the jets of lib/gtg.py, on fields that are neither
    symmetric nor plane waves. The field equation of clause (f) of the stored definition is not used: clauses
    (i) to (vii) are identities of the Einstein map, and clause (viii) takes the first-order field equation as
    its hypothesis (M1) and the matter's conservation law as (M2). Kill conditions registered before computing,
    none of which fired: (K1) the flat divergence of the quadratic part fails to vanish on an exact first-order
    solution; (K2) its change under a first-order gauge change is not the first-order Einstein map of a
    quadratic field; (K3) its null-null component in the gauge of the first result is not the square of the
    shear up to terms that integrate away along a generator. What was weaker than a naive reading: the
    quadratic part is not invariant under first-order displacements or rotation gauge changes, even on
    solutions, and it depends on the second-order parametrisation of the field; its null-null component equals
    the stored null energy density at each point only in one parametrisation (the exponential one) and one
    gauge, and in two of the six sample cases of the check it is negative at the point. What the result does
    NOT settle: it does not derive the whole-stress clause, which is condition (C) of the second result, to
    any order (clause (viii) assumes the matter's conservation law in the field, which is that condition for
    the matter, and concludes what the field's own contribution must then be, at second order only); it does
    not show that the quadratic part is the only admissible self-source (only its flat divergence is forced);
    it does not go beyond second order; it does not show that the fluxes of clause (v) are independent of the
    plane, nor that they are positive apart from the null energy of clause (vi); it does not carry out the
    average over several wavelengths of the literature; matter with spin is not covered. The instance in the Reading (one plane wave whose quadratic part
    is the one of clause (vii) in the transverse trace-free gauge and zero at every point in the Kerr-Schild
    gauge) uses the field of clause (vi) of the result on null-surface data at any field strength filed
    alongside this one (synthesis.null-surface-data-at-any-field-strength-the-focusing-equation-integrated),
    from which the observation came; that result is not a premise, and the facts used (the torsion equation,
    the curvature linear in the profile, the relating displacement) are proved in the last paragraph of the
    proof here and checked exactly. It shows, for the integrals along the generators, that the fall-off condition of clause (v) cannot be dropped. Near entries, none a
    duplicate: synthesis.vacuum-field-stress-tensor-is-einstein-tensor-or-trace concerns tensors affine in the
    curvature at a point, not the quadratic part; no stored result treats a gravitational stress, a
    pseudotensor, a superpotential or the self-coupling. Decisions for the maintainer: (1) whether the Reading
    of the first result (the paragraph on the shear) is to cite clause (vi) here in place of its argued remark;
    (2) whether the open problem takes clause (viii) under its work in store, with attack items for the same
    argument at every order and for deriving (M2) from the stored response of matter; (3) whether (M1) and
    (M2) stay hypotheses local to this result (they are kept local, and no assumes edge is declared); (4)
    which second-order parametrisation is the store's reference: the statement is written for
    hb = id + eps H1 + eps^2 H2, and the exponential one is the one in which clauses (vi) and (vii) hold at
    each point; (5) whether the truncated-polynomial ring and the explicit torsion solve of check.py are to
    move into lib/gtg.py (a toolkit change, the maintainer's alone). Prior art, not premises. Looked up for
    this entity on 27 November 2026 (title, journal, year and the abstract confirmed on the publisher's or the
    arXiv page; the texts not read; the last page of the first and the journal pages of the second are from
    memory): R. A. Isaacson, 1968, for the effective stress of gravitational waves at second order, which its
    abstract calls gauge invariant and averaged (reference Isaacson1968, appended); clause (vii) in the
    exponential parametrisation is its form for one wave without the average, and in the parametrisation in
    which t is defined the two differ by a second derivative in the phase, which the average removes; S. Deser, 1970, for the
    self-coupling argument carried to all orders (reference Deser1970, appended). Cited from memory and not read: S. N. Gupta, 1954, and R. P. Feynman's lectures on gravitation
    (given 1962 to 1963), for the argument that a field coupled to the stress of matter must couple to its
    own; A. Einstein's and L. D. Landau and E. M. Lifshitz's pseudotensors, and the freedom of a superpotential
    (P. Freud, 1939), for the absence of a local density of gravitational energy; the superpotential form of
    the first-order Einstein map is the standard one of the first-order theory. No novelty is claimed for any
    clause; what is new to the store is the statement in the series' variables, for a field with an arbitrary
    rotation gauge, the explicit quadratic fields of clause (iv), the comparison with the stored null energy,
    and the exact checks. Credit: the result was prompted by V. Chandrasekaran, "An algebraic quantization of
    gravity from the null cone", arXiv:2611.34924 (reference Chandrasekaran2026; its abstract page was read on
    27 November 2026 through a summarising fetch, the body not), which quantises the gravitational field from
    data on intersecting null cones, as was the first result; its use of the shear as the datum is as described
    in the first result, whose author read its text, and the question asked here is one it prompted; none of
    the paper's formulas is used. The paper's author is cited, not listed under credit, which names those who worked on
    this entry. Ledger: transport-absent.
---

## formal
Units $\hbar = c = 1$, $\Cl(1,3)$ with frame $e_{0}, e_{1}, e_{2}, e_{3}$, $Q(e_{0}) = 1$, $Q(e_{i}) = -1$, and a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), whose clauses are cited by their letters. Only its clauses (i) to (e) and the torsion equation of its clause (f), which fixes $\Omega$ from $\hb$, are used; the field equation of clause (f) is not assumed anywhere, and enters only clause (viii) below, as the named hypothesis (M1). Notation of Theorems \claimref{synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators} and \claimref{synthesis.field-equation-linear-in-the-curvature-with-a-conserved-source-is-einsteins}: the Einstein map $\mathcal{G}$ on physical vectors in the store's sign and the divergence $\operatorname{div}$ of a field of maps of physical vectors; for a field $h$ of symmetric maps, $\ip{h_{1}}{h_{2}} = \sum_{a} h_{1}(e_{a}) \cdot h_{2}(e^{a})$, $\tau = \tr h$, $d = \dot h(\dot\nabla)$, and the first-order Einstein map
\[
\mathcal{E}[h](a) = \tfrac12\bigl(\nabla^{2}h(a) + (a \cdot \nabla)\nabla\tau - (a \cdot \nabla)d - \nabla(a \cdot d)\bigr) - \tfrac12\,a\,\bigl(\nabla^{2}\tau - \nabla \cdot d\bigr),
\]
the Einstein map of the stored first-order curvature $\mathcal{R}[h](B) = -\tfrac12\,\nabla \wedge h(B \cdot \nabla)$ (Theorem \claimref{synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel}); $n = e_{0} + e_{3}$, $\bar n = e_{0} - e_{3}$, the null plane $N$: $n \cdot x = \text{const}$ with generators along $n$, parameter $\lambda$ ($\partial_{n} = n \cdot \nabla$), transverse position $y$ and measure $d\lambda\,d^{2}y$; $\nabla_{\perp} = e^{1}\partial_{1} + e^{2}\partial_{2}$; the maps $\epsilon_{+}$, $\epsilon_{\times}$, and for $h(n) = 0$ the part $h^{TT}$, the shear $\sigma = \tfrac12\,\partial_{n}h^{TT}$ and the expansion $\theta = \tfrac12\,\partial_{n}\tau$ of the generators of $N$. Derivatives marked with a dot act on the dotted factor only. For a linear map $H$ of the vectors, $H^{T}$ is its adjoint, $a \cdot H^{T}(b) = H(a) \cdot b$; for a vector field $\xi$, $\underline{\xi}(a) = a \cdot \nabla\,\xi$; for a bivector field $B$, $\beta_{B}(a) = a \cdot B$, an antisymmetric map.

\emph{Setting.} Let $H_{1}, H_{2}$ be smooth fields of linear maps of the vectors, not assumed symmetric, and $\hb_{\varepsilon} = \id + \varepsilon H_{1} + \varepsilon^{2}H_{2}$, a gravitational field for small $\varepsilon$ on any bounded region, with $\Omega_{\varepsilon}$ fixed by the torsion equation. Physical vectors are vectors of the algebra, so the Einstein map of $\hb_{\varepsilon}$ is a field of linear maps of the vectors, and
\[
\mathcal{G}_{\varepsilon} = \varepsilon\,\mathcal{G}^{(1)}[H_{1}] + \varepsilon^{2}\bigl(\mathcal{G}^{(1)}[H_{2}] + \mathcal{G}^{(2)}[H_{1}]\bigr) + O(\varepsilon^{3}),
\]
with $\mathcal{G}^{(1)}$ linear and $\mathcal{G}^{(2)}[H_{1}]$, \emph{the quadratic part}, a quadratic differential expression in $H_{1}$ with two derivatives in each term (the coefficient of $\varepsilon^{2}$ at $H_{2} = 0$). Put
\[
t = \frac{1}{8\pi G}\,\mathcal{G}^{(2)}[H_{1}] .
\]
If the field equation is taken in the store's form $\mathcal{G}(a) = -8\pi G\,T(a)$ with $T = \varepsilon T_{1} + \varepsilon^{2}T_{2}$, its coefficient of $\varepsilon^{2}$ is $\mathcal{G}^{(1)}[H_{2}] = -8\pi G\,(T_{2} + t)$: $t$ stands where a stress stands, with this sign. That remark motivates the definition and is not used in clauses (i) to (vii). A \emph{first-order solution} is an $H_{1}$ with $\mathcal{G}^{(1)}[H_{1}] = 0$. For a constant vector $c$, the \emph{flat divergence} of a field $M$ of linear maps at $c$ is $\nabla \cdot (M(c))$.
\begin{enumerate}
\item[(i)] \emph{(First order; proved.)} Write $H_{1}(a) = S(a) + a \cdot A$ with $S = \tfrac12(H_{1} + H_{1}^{T})$ and $A = \tfrac12\,\partial_{a} \wedge H_{1}(a)$. Then $\Omega_{\varepsilon}(a) = \varepsilon\,\Omega_{1}(a) + O(\varepsilon^{2})$ with $\Omega_{1}(a) = \dot\nabla \wedge \dot S(a) - (a \cdot \nabla)A$, and
\[
\mathcal{G}^{(1)}[H_{1}] = \mathcal{E}[h], \qquad h = -(H_{1} + H_{1}^{T}) ,
\]
the first-order part of the derived metric being $a \cdot b + \varepsilon\,h(a) \cdot b$: the first-order part does not see $A$. It is a symmetric map, its flat divergence vanishes identically, and $\mathcal{G}^{(1)}[\underline{\xi}] = 0 = \mathcal{G}^{(1)}[\beta_{B}]$ for every $\xi$ and $B$.
\item[(ii)] \emph{(Symmetry; proved.)} $\mathcal{G}^{(2)}[H_{1}]$ is a symmetric map, $a \cdot \mathcal{G}^{(2)}[H_{1}](b) = b \cdot \mathcal{G}^{(2)}[H_{1}](a)$, for every $H_{1}$: symmetric or not, a first-order solution or not. It has no antisymmetric part in any rotation gauge.
\item[(iii)] \emph{(Conservation; proved.)} For every $H_{1}$ and every constant vector $c$, with $v = \mathcal{G}^{(1)}[H_{1}](c)$ and $w = \partial_{a} \cdot \Omega_{1}(a)$,
\[
\nabla \cdot \bigl(\mathcal{G}^{(2)}[H_{1}](c)\bigr) = -\,\dot\nabla \cdot H_{1}(\dot v) \;-\; v \cdot w \;-\; c \cdot \bigl(\Omega_{1}(\partial_{a}) \cdot \mathcal{G}^{(1)}[H_{1}](a)\bigr) .
\]
Each term on the right contains $\mathcal{G}^{(1)}[H_{1}]$ or its first derivative as a factor. So on a first-order solution the flat divergence of $t$ vanishes, $\nabla \cdot (t(c)) = 0$ for every $c$, and off solutions it is the displayed combination.
\item[(iv)] \emph{(Gauge behaviour; proved.)} Under the displacement $x \mapsto x + \varepsilon\,\xi(x)$, $H_{1} \mapsto H_{1} - \underline{\xi}$ and
\[
\mathcal{G}^{(2)}[H_{1} - \underline{\xi}] = \mathcal{G}^{(2)}[H_{1}] + (\xi \cdot \nabla)\,\mathcal{G}^{(1)}[H_{1}] - \mathcal{G}^{(1)}\bigl[(\xi \cdot \nabla)H_{1} - \underline{\xi}\,H_{1} + \underline{\xi}\,\underline{\xi}\bigr] .
\]
Under the rotation gauge change with rotor $e^{\varepsilon B/2}$, $H_{1} \mapsto H_{1} + \beta_{B}$ and
\[
\mathcal{G}^{(2)}[H_{1} + \beta_{B}] = \mathcal{G}^{(2)}[H_{1}] - \mathcal{G}^{(1)}\bigl[H_{1}\beta_{B} + \tfrac12\,\beta_{B}\beta_{B}\bigr] + \mathcal{G}^{(1)}[H_{1}]\,\beta_{B} - \beta_{B}\,\mathcal{G}^{(1)}[H_{1}] .
\]
Under a change of the second-order parametrisation, $\hb_{\varepsilon} = \id + \varepsilon H_{1} + \varepsilon^{2}(H_{2} + q)$ with $q$ a quadratic expression in $H_{1}$, the quadratic part becomes $\mathcal{G}^{(2)}[H_{1}] + \mathcal{G}^{(1)}[q]$; write $\mathcal{G}^{(2)}_{r} = \mathcal{G}^{(2)}[H_{1}] + r\,\mathcal{G}^{(1)}[H_{1}H_{1}]$ for a number $r$, which is the quadratic part for $\hb^{-1} = \id - \varepsilon H_{1} - \varepsilon^{2}H_{2}$ at $r = 1$ and for $\hb = \exp(\varepsilon H_{1} + \varepsilon^{2}H_{2})$ at $r = \tfrac12$. (Products of maps are compositions.) Hence on a first-order solution each of the three changes $t$ by
\[
\frac{1}{8\pi G}\,\mathcal{G}^{(1)}[X], \qquad X_{\xi} = -(\xi \cdot \nabla)H_{1} + \underline{\xi}\,H_{1} - \underline{\xi}\,\underline{\xi}, \quad X_{B} = -H_{1}\beta_{B} - \tfrac12\,\beta_{B}\beta_{B}, \quad X_{q} = q ,
\]
the first-order Einstein map of an explicit quadratic field. These changes do not vanish: $t$ is not invariant under first-order gauge changes, even on solutions. At every point of every first-order solution some displacement changes it: replacing $\xi$ by $s\,\xi$ with a number $s$ changes $t$ by $s$ times a term linear in $\xi$ minus $s^{2}\,\mathcal{G}^{(1)}[\underline{\xi}\,\underline{\xi}]/8\pi G$, and $\mathcal{G}^{(1)}[\underline{\xi}\,\underline{\xi}]$ is nonzero at a given point for a suitable polynomial $\xi$ (computed; on the flat field itself, $H_{1} = -\underline{\xi}$ is a first-order solution with $\mathcal{G}^{(2)}[-\underline{\xi}] = \mathcal{G}^{(1)}[-\underline{\xi}\,\underline{\xi}] \neq 0$). On a solution that is neither symmetric nor a plane wave the change is nonzero in all sixteen components, for $\xi$ and for $B$ (computed).
\item[(v)] \emph{(The change is a superpotential; fluxes; proved.)} For a field $x$ of symmetric maps and a constant vector $a$ put $W_{a}[x] = \tfrac12\bigl(\dot\nabla \wedge \dot x(a) - a \wedge d_{x} + a \wedge \nabla\tau_{x}\bigr)$, a bivector field. Then
\[
\mathcal{E}[x](a) = \nabla \cdot W_{a}[x], \qquad n \cdot \mathcal{E}[x](n) = \partial_{n}\Bigl(\tfrac12\,\partial_{n}\bigl(\tau_{x} - \bar n \cdot x(n)\bigr) - \nabla_{\perp} \cdot x(n)\Bigr) + \tfrac12\,\nabla_{\perp}^{2}\bigl(n \cdot x(n)\bigr) ,
\]
identically. So each change of (iv) is the divergence of a bivector, $\tfrac{1}{8\pi G}\nabla \cdot W_{a}[-(X + X^{T})]$, with identically vanishing flat divergence, and since $n \cdot W_{a}$ is orthogonal to $n$ its flux through $N$ is the integral over $N$ of a divergence within $N$. Consequently, for a first-order solution and a constant vector $c$, the flux $P_{c} = \int_{N} n \cdot t(c)\,d\lambda\,d^{2}y$ of the conserved vector field $t(c)$, when it converges, is unchanged by a displacement, a rotation gauge change or a change of parametrisation whose field $X$ vanishes near $N$ outside a compact part of $N$. For $c = n$ less is needed: with $x = -(X + X^{T})$, $P_{n}$ is unchanged whenever the integral over $y$ of $\tfrac12\,\partial_{n}(\tau_{x} - \bar n \cdot x(n)) - \nabla_{\perp} \cdot x(n)$ tends to zero at both ends of the generators and the transverse boundary integrals of $x(n)$ and of $\nabla_{\perp}(n \cdot x(n))$ vanish. Some such condition is needed (the Reading gives an instance, a plane wave, in which it fails and the integrals of $n \cdot t(n)$ along the generators differ).
\item[(vi)] \emph{(The null energy; proved from the focusing equation.)} Let (LC): $H_{1}$ is symmetric and $H_{1}(n) = 0$, the gauge $h(n) = 0$ of the cited theorem's clause (ii), with $h = -2H_{1}$; $H_{1}$ need not be a solution. Then, identically,
\[
n \cdot \mathcal{G}^{(2)}_{r}(n) = \ip{\sigma}{\sigma} + \tfrac12\,\theta^{2} + \bigl(\tfrac18 - \tfrac{r}{4}\bigr)\,\partial_{n}^{2}\ip{h}{h}, \qquad\text{so}\qquad 8\pi G\;n \cdot t(n) = \ip{\sigma}{\sigma} + \tfrac12\,\theta^{2} + \tfrac18\,\partial_{n}^{2}\ip{h}{h} .
\]
On a first-order solution $\theta$ is constant along each generator. The null-null component of $t$ therefore agrees with the stored density $\ip{\sigma}{\sigma}/8\pi G$ of null energy at each point only in the exponential parametrisation ($r = \tfrac12$) and where $\theta = 0$; in the others it differs by a second derivative along the generator, with no transverse divergence in this gauge, and it is not of one sign (computed: negative at the sample point in two of six cases). Let (F): on each generator $h$ is bounded and $\partial_{n}h$ tends to zero at both ends. Under (LC) and (F), on a first-order solution, $\theta = 0$ and, when the integrals converge, for every $r$ and every generator
\[
\int n \cdot \tfrac{1}{8\pi G}\,\mathcal{G}^{(2)}_{r}(n)\;d\lambda = \frac{1}{8\pi G}\int \ip{\sigma}{\sigma}\,d\lambda \;\geq\; 0, \qquad P_{n} = \frac{1}{8\pi G}\int_{N}\ip{\sigma}{\sigma}\,d\lambda\,d^{2}y ,
\]
the expression $P$ of the cited theorem's clause (vi). The equality of the integrals is unconditional; calling the right side the null energy carries the hypotheses (L), (D), (V) and (N) of that clause. On a first-order solution, out of the gauge (LC) the null-null component of $t$ differs from the one in the gauge by $\tfrac{1}{8\pi G}\,n \cdot \mathcal{E}[x](n)$ with $x = -(X + X^{T})$, with $X$ the field of (iv) of the rotation and displacement that bring $H_{1}$ to (LC), composed, which by (v) is a derivative along the generator plus a transverse divergence.
\item[(vii)] \emph{(One plane wave; proved by an exact finite computation.)} For $h = f_{+}(k \cdot x)\,\epsilon_{+} + f_{\times}(k \cdot x)\,\epsilon_{\times}$ with $k = \bar n$ and any two profiles, $H_{1} = -\tfrac12 h$ is a first-order solution satisfying (LC), and with primes for derivatives in the phase $k \cdot x$,
\[
\mathcal{G}^{(2)}_{r}(a) = \tfrac14\Bigl(\ip{h'}{h'} + \bigl(\tfrac12 - r\bigr)\ip{h}{h}''\Bigr)\,(a \cdot k)\,k :
\]
in the exponential parametrisation the stress of one wave is $\tfrac{1}{32\pi G}\ip{h'}{h'}\,(a \cdot k)\,k$ at every point, of null energy density $\tfrac{1}{8\pi G}\ip{\sigma}{\sigma}$ on $N$; in the others it differs by a second derivative in the phase.
\item[(viii)] \emph{(The field's own stress as a source at second order; proved, given (M1) and (M2).)} Let matter have a stress map $T_{\varepsilon} = \varepsilon\,T_{1} + \varepsilon^{2}T_{2} + O(\varepsilon^{3})$, a field of symmetric linear maps of the physical vectors. Assume (M1): the first-order field equation $\mathcal{G}^{(1)}[H_{1}] = -8\pi G\,T_{1}$ (clause (vi) of the first cited theorem; clause (vii) of the second at first order, $\Lambda = 0$). Assume (M2): the matter obeys its conservation law in the field, $\operatorname{div}T_{\varepsilon} = O(\varepsilon^{3})$ with the divergence of the field $(\hb_{\varepsilon}, \Omega_{\varepsilon})$ (the conservation of condition (C) of the second cited theorem, asked of the matter through second order). Then, by (M2) alone, $\nabla \cdot (T_{1}(c)) = 0$ and
\[
\nabla \cdot (T_{2}(c)) = -F(c), \qquad F(c) = \dot\nabla \cdot H_{1}\bigl(\dot T_{1}(c)\bigr) + T_{1}(c) \cdot w + c \cdot \bigl(\Omega_{1}(\partial_{a}) \cdot T_{1}(a)\bigr) ,
\]
so the matter's stress alone is not conserved in the flat sense where $F \neq 0$; and with (M1)
\[
\nabla \cdot \bigl((T_{2} + t)(c)\bigr) = 0 \qquad\text{for every constant vector } c .
\]
Conversely (M1) and the last equation give (M2) at second order. Since the flat divergence of $\mathcal{G}^{(1)}[H_{2}]$ vanishes identically, an equation $\mathcal{G}^{(1)}[H_{2}] = -8\pi G\,(T_{2} + \chi)$ for the second-order field, with $\chi$ quadratic in $H_{1}$, has a solution only if $\nabla \cdot ((T_{2} + \chi)(c)) = 0$. Under (M1) and (M2) the choice $\chi = t$ meets this condition, as does $t + \tfrac{1}{8\pi G}\mathcal{G}^{(1)}[q]$ for any $q$, and $\chi = \mu\,t$ with a constant $\mu$ meets it only if $(\mu - 1)\,F = 0$. So wherever $F \neq 0$, a second-order equation of this form needs a source quadratic in $H_{1}$ whose flat divergence is that of $t$; $t$ meets this condition, and among the multiples of $t$ only $t$ itself, with the constant $8\pi G$ of the matter coupling, does. The condition fixes the flat divergence of that source and nothing more. This is a statement at second order under (M1) and (M2). It is not a derivation of condition (C) of the second cited theorem, at this order or any other.
\end{enumerate}
\emph{Source of the idea.} This result was prompted, as the first cited theorem was, by \cite{Chandrasekaran2026}, which quantises the gravitational field from data on intersecting null cones (its use of the shear as the datum is as described in the first cited theorem, whose author read its text); the question asked here, which it prompted, is in what sense the energy of that datum is itself a source of the field. None of the paper's formulas is used, and only its abstract page was read. The content is classical: the effective stress of gravitational waves at second order is due to \cite{Isaacson1968}, clause (vii) in the exponential parametrisation being its form for one wave without the average; in the parametrisation in which $t$ is defined the two differ by a second derivative in the phase, which the average removes; the argument that a field coupled to the stress of matter must couple to its own stress with the same constant is due to S. N. Gupta (1954) and R. P. Feynman (lectures on gravitation, 1962 to 1963), both cited from memory, and was carried to all orders in \cite{Deser1970}; that the energy of the gravitational field has no density at a point, its candidates differing by superpotentials, is reflected in the pseudotensors of A. Einstein and of L. D. Landau and E. M. Lifshitz (cited from memory). What is done here is the second order only, in the series' variables, with the rotation gauge left free.

\emph{Reading (argued).} \emph{Gravitational waves gravitate.} The Reading of the first cited theorem observes that in the focusing equation the square of the shear stands beside the matter's null energy with the same coefficient. Clauses (vi) and (viii) say what that amounts to as a field equation. In the gauge (LC) and the exponential parametrisation, if the field equation $\mathcal{G} = -8\pi G\,T$ (clause (f) of the Definition; the second cited theorem under its conditions (Q) and (C)) holds through second order, the null-null component of the second-order equation is $\tfrac12\,\partial_{n}^{2}\tau_{2} = -8\pi G\,n \cdot T_{2}(n) - \ip{\sigma}{\sigma} - \tfrac12\theta^{2}$, with $\tau_{2}$ the trace of $h_{2} = -2H_{2}$ and $H_{2}$ in the same gauge: the null energy density of the two components is a source of the second-order field exactly as the matter's is. That holds at each point in one gauge and one parametrisation. In general it holds for the integral along a generator, and for the flux through the plane. \emph{No density at a point.} By (iv) the quadratic part is defined only up to the first-order Einstein map of a quadratic field, and three independent choices move it within that class: the displacement gauge, the rotation gauge, and the parametrisation of the field at second order. Nothing in the stored definition prefers one of them. What is defined is the class of $t$ modulo such terms, its vanishing flat divergence on solutions, and the fluxes of (v). \emph{The whole-stress clause.} Condition (C) of the second cited theorem says that the source of the Einstein map is the whole stress of the matter, conserved. Read on the flat background at second order, with the quadratic part moved to the side of the source, the same equation says that the second-order field has the source $T_{2} + t$: the matter's stress and the field's own, with one constant. Clause (viii) shows that a source with the flat divergence of $t$ is forced, at this order, once the first-order field couples to the matter's stress (M1) and the matter responds to the field by its conservation law (M2). (M2) is condition (C) for the matter, so nothing of that condition is derived here; what is shown is that the condition cannot hold for matter alone on a flat background beyond first order, the field's own stress entering with the same constant. Whether the same argument at every order reproduces the full equation is the subject of \cite{Deser1970} and is not carried out in the store. \emph{An instance: one wave with and without a quadratic part (proved in the last paragraph of the proof, and computed).} Let $\ell = \tfrac12\bar n$, $\lambda = \ell \cdot x$, and let $F_{\lambda}$ be symmetric trace-free maps of the span of $e_{1}, e_{2}$, with $F(n) = F(\ell) = 0$ and $\mathsf{w} = \tfrac12 F''$, primes for derivatives in $\lambda$. The wave $h = F$ of clause (vii), $H_{1} = -\tfrac12 F$, has the quadratic part of (vii), which is not zero. The field $H_{1}^{KS}(a) = \tfrac12 W (a \cdot \ell)\,\ell$ with $W = -y \cdot \mathsf{w}_{\lambda}(y)$, the Kerr-Schild form of the same wave, has the same first-order curvature, and the Einstein map of $\id + \varepsilon H_{1}^{KS}$ is $\varepsilon\,(\tr\mathsf{w})(a \cdot \ell)\,\ell$ exactly: it is a first-order solution and its quadratic part vanishes at every point, in every parametrisation $r$, the square of $H_{1}^{KS}$ being zero. The two fields are related as in (iv): $H_{1}^{KS} = H_{1} - \underline{\xi} + \beta_{B}$ with $\xi = -\tfrac12 F(y) + \tfrac14(y \cdot F'(y))\,\ell$ and $\beta_{B}$ the antisymmetric part of $\underline{\xi}$, and the difference of the quadratic parts is $\mathcal{G}^{(1)}[X]$ with $X$ composed of $X_{\xi}$ and $X_{B}$. So one and the same first-order wave has the stress of (vii) in one gauge and no stress at all, at any point, in another. This is the sharpest instance of (iv), and it does not contradict (v): $\xi$ grows quadratically across the plane, so neither condition of (v) is met, and the integrals of $n \cdot t(n)$ along the generators do differ: under (F) for $F$ they are $\tfrac{1}{8\pi G}\int\ip{\sigma}{\sigma}\,d\lambda$ on each generator in the first gauge and zero in the second ($P_{n}$ itself diverges for a plane wave, whose integrand does not depend on $y$). The instance shows that the fall-off condition of (v) cannot be dropped: the fluxes are defined on a class of gauges related by changes that fall off, such as (LC) with (F), not on all gauges. In the Kerr-Schild gauge $H_{1}(n) \neq 0$, so the planes $n \cdot x = \text{const}$ are not in the gauge (LC); the convergence of the null planes that the wave crosses, which the gauge (LC) assigns at second order to this stress, is there carried by the field with no quadratic part (argued). \emph{Limits.} Second order only. Only the flat divergence of the self-source is fixed. The fluxes $P_{c}$ are not shown to be independent of the plane, and only $P_{n}$ is evaluated. The formula of (vii) is stated for the wave along $\bar n$; a constant rotor carries any null momentum with its transverse frame to that one, and the construction is covariant under it, which is argued and not checked. No average over wavelengths is taken. Matter without spin, as in the second cited theorem.

## technical
The store holds the first-order gravitational field as a field of symmetric maps on flat spacetime, with its Einstein map, and since 26 November 2026 two results about it: on a null plane its free data are the shear of the plane's generators, with null energy the integral of the square of the shear over $8\pi G$; and a field equation linear in the curvature with a conserved source is Einstein's. The first of them remarks, as an argued reading, that the square of the shear stands in the focusing equation where the matter's null energy stands. This result takes the next order and makes the remark a set of proved statements, including the respects in which it fails.

Write the displacement gauge field as the identity plus a first-order and a second-order map, with the rotation gauge field fixed by the torsion equation, and expand the Einstein map. Its second-order part is the first-order Einstein map of the second-order field plus a quadratic expression in the first-order field. On a first-order solution without matter that quadratic part, over $8\pi G$, stands in the second-order equation where a stress stands.

Four properties are proved by expanding stored identities to second order, without writing the quadratic part out. It is a symmetric map for every first-order field, whatever the rotation gauge, because the Ricci map of every field obeying the torsion equation is symmetric. Its flat divergence is a combination of the first-order Einstein map and its first derivatives, so it is conserved on first-order solutions; this is the contracted identity at second order. Under a first-order displacement, a first-order rotation gauge change, or a change of how the field is parametrised at second order, it changes, on solutions, by the first-order Einstein map of an explicit quadratic field. And the first-order Einstein map of any field is the divergence of a bivector, so those changes are superpotential terms: identically conserved, and with flux through a null plane equal to a boundary term.

So the quadratic part is not invariant: at every point of every first-order solution some displacement changes it, and no choice of gauge or parametrisation is singled out by the stored definition. What is invariant is the flux through a complete null plane for changes of compact support. In the light-cone gauge of the first result the null-null component is computed from the stored focusing equation: it is the square of the shear, plus half the square of the expansion, plus a second derivative along the generator whose coefficient depends on the parametrisation and vanishes for the exponential one. On solutions the expansion is constant along a generator, so for data that settle at both ends the integral along each generator is the integral of the square of the shear, and the flux is the stored null energy. For a single plane wave the whole quadratic part lies along the wave's momentum and, in the exponential parametrisation, is the familiar effective stress at each point, with no averaging.

Finally, if the first-order field couples to the matter's stress with the stored constant and the matter obeys its conservation law in the field, then the matter's second-order stress is not conserved in the flat sense (the difference is the force), and its sum with the quadratic part over $8\pi G$ is. The second-order equation can only be solved for a conserved source, so it needs a quadratic self-source with the flat divergence of the field's own stress; among multiples of that stress only the one with the same constant qualifies. This is a second-order statement under those two hypotheses, and the second of them is the conservation half of the whole-stress clause for matter; the clause itself is not derived.

The checks compute the quadratic part exactly from the gauge fields, with the expansion parameter carried as a truncated polynomial, on polynomial fields that are neither symmetric nor plane waves, on first-order solutions built from three or four null waves with a displacement and a rotation gauge, and on dust falling in its own first-order field.

Ledger: transport-absent. This is second-order perturbation theory of general relativity about flat spacetime, stated in the series' variables with exact checks.

## lay
Gravitational waves carry energy, and in Einstein's theory all energy is a source of gravity. So gravitational waves should themselves produce gravity. This result makes that precise at the first order at which it can happen, and shows what is and is not true about it.

The series treats weak gravity as a field on flat spacetime. To first approximation the field obeys a linear equation, like light. At the next approximation the equation has an extra term built from the square of the first-order field. That term sits in the equation exactly where the energy and momentum of matter sit. It is the natural candidate for the energy and momentum of the gravitational field itself.

Three things are proved about it. First, it is conserved: on any solution, what flows into a region flows out. Second, it is not a definite quantity at a point. Relabelling the points of spacetime, turning the local frames, or changing the bookkeeping at second order all change it. They change it only by terms of a special kind, which have no net flow through a complete wall of light when the relabelling or turning is confined to a bounded region. So one cannot say how much gravitational energy there is at a point, only how much crosses a whole surface. This is an old insight, and here it comes out with every term written down.

Third, on a wall of light, the surface used in the earlier result, the total energy crossing along each light ray is, for waves that die away at both ends of the ray, exactly the quantity found there: the square of the shear, the rate at which the wave distorts a bundle of rays. In one particular bookkeeping the match even holds point by point.

Last, a consistency argument. If weak gravity pulls on matter, the matter's momentum is not conserved by itself: a falling stone gains momentum. The books balance only when the field's own energy and momentum are added, with exactly the same strength of coupling as for matter. So gravity must be a source of gravity, and the field's own energy and momentum, entering with exactly the same constant, balance the books (this fixes how the source flows, not every detail of it). The check does this for dust falling in its own gravity. The argument assumes that matter responds to gravity in the usual way, and it reaches only this one order; it does not by itself produce Einstein's full equation.

The work was prompted by a 2026 paper by V. Chandrasekaran on gravity described on surfaces of light. The ideas are classical: R. Isaacson (1968) for the energy of the waves, and S. Gupta, R. Feynman and S. Deser for the consistency argument.

## one-liner
For $\hb = \id + \varepsilon H_{1} + \varepsilon^{2}H_{2}$ with $\Omega$ from the torsion equation, the quadratic part $\mathcal{G}^{(2)}[H_{1}]$ of the Einstein map is a symmetric map for every $H_{1}$ in every rotation gauge; its flat divergence is a combination of $\mathcal{G}^{(1)}[H_{1}]$ and its first derivatives, so $t = \mathcal{G}^{(2)}[H_{1}]/8\pi G$ is conserved on first-order solutions; under a first-order displacement, rotation gauge change or reparametrisation it changes on solutions by $\mathcal{G}^{(1)}[X]/8\pi G$ with $X$ an explicit quadratic field ($X_{\xi} = -(\xi \cdot \nabla)H_{1} + \underline{\xi}H_{1} - \underline{\xi}\,\underline{\xi}$), the divergence of a bivector, so $t$ is not invariant (at every point of every solution some displacement changes it) while its flux through a complete null plane is, for changes of compact support; in the gauge $h(n) = 0$, $8\pi G\,n \cdot t(n) = \ip{\sigma}{\sigma} + \tfrac12\theta^{2} + \tfrac18\partial_{n}^{2}\ip{h}{h}$, equal to the stored null energy density only after integration along a generator (at each point only in the exponential parametrisation); and if the first-order field couples to matter's stress and the matter obeys its conservation law in the field, then $T_{2} + t$, not $T_{2}$, has vanishing flat divergence, so at second order the field needs a self-source with the flat divergence of $t$, and among multiples of $t$ only $t$, with the same constant $8\pi G$, qualifies.
