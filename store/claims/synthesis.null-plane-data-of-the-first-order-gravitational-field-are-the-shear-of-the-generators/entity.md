---
id: synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators
kind: claim
version: 1
title: 'Null-plane data of the first-order gravitational field: the shear of the generators'
status: proved
region: synthesis
subject: quantum-fields
tags: [quantum-gravity, gauge-fields, curvature-and-field-equations, null-directions]
proposed_by:
  kind: ai
  session: 2026-11-26-null-plane
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction (the question, the scope of first order, the instruction to work from the stored results, to derive what was imported and to state everything in geometric algebra)
- name: Claude Fable 5.2
  role: proposal, proof and drafting
  source: session 2026-11-26-null-plane
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel@1
  - synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints@2
  - field-theory.operator-newtonian-coupling@4
  - field-theory.fock-space-maxwell-modes@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_symplectic_current_of_the_first_order_einstein_operator
- kind: check
  ref: check.py::check_flux_through_the_null_plane_in_the_gauge
- kind: check
  ref: check.py::check_gauge_is_reachable_and_the_generator_equation_is_first_order_focusing
- kind: check
  ref: check.py::check_riccati_equation_of_the_generators_on_a_field_that_is_not_weak
- kind: check
  ref: check.py::check_curvature_form_of_the_null_datum_is_the_rate_of_shear
- kind: check
  ref: check.py::check_second_order_covariant_operators_and_the_einstein_map
- kind: check
  ref: check.py::check_constant_from_the_newtonian_coupling_and_the_stored_residue
- kind: check
  ref: check.py::check_modes_on_a_closed_generator
- kind: check
  ref: check.py::check_rotation_about_the_generator_turns_the_two_components_by_twice_the_angle
lineage:
  motivated_by:
  - synthesis.premise-canonical-pair-on-the-two-null-directions
  - synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators
  - synthesis.einstein-equations-from-c-loc-and-clausius
extraction:
  open_problem: op.gravitational-field-at-null-momentum
  flags:
  - 'beyond one flat chart: the generator closed to a period in clause (vii), the discretised light-cone setting'
  note: >-
    Filed against limit (f) of Premise (TT) (synthesis.premise-canonical-pair-on-the-two-null-directions): the
    normalisation of the free part of the first-order field, which that premise says is taken over from the photon
    and not computed in the store. Route: the null plane, as for the stored photon
    (synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators, clauses (i) and (ii)), with the
    stored first-order Einstein map in place of the Maxwell operator. No imported Fact is a premise of this
    result. Two were premises of its first draft and are derived here instead, on the maintainer's instruction
    of 26 November 2026. (1) The focusing and shear equations of a null congruence
    (synthesis.imported-raychaudhuri-null-congruence) are clause (iii), proved from clauses (b), (c) and the
    torsion equation of the stored definition of the gravitational field, for a congruence that is a gradient;
    the twist term of the imported Fact is not covered, a gradient having none. (2) The frame equation
    (synthesis.imported-einstein-cartan-matter-coupling, clause (a)) is not derived as such, and cannot be from
    the stored content: that is open problem op.einstein-from-the-field-theory. What is derived is its first
    order, in clauses (v) and (vi), from three conditions stated there as hypotheses (a local second-order
    covariant equation, vanishing on displacements, coming from a quadratic functional) and from a fourth, (N),
    that the static interaction is the stored Newtonian coupling, for the constant; that Proposition takes the
    coupling as its input, so (N) is an identification and not a derivation. The three conditions with the response of matter are the whole-stress
    clause at first order; they are assumed. Clause (v) is a first-order form of Lovelock's theorem (the store
    holds the theorem for the full theory as synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians)
    and is proved here by an exact finite computation. The constants agree with clause (f) of the stored
    definition, with the imported frame equation and with the stored interaction of
    synthesis.gravitational-pair-production-from-the-operator-source-at-first-order, clauses (i) and (ii), whose
    constant lambda that result leaves unevaluated: it is 16 pi G. Clause (iv) also settles the overall sign
    that synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel
    leaves open for the stored first-order curvature: it is the store's sign. No assumes edge to Premise (TT) is
    declared: no proved clause needs it, and whether the Reading's comparison should carry one is for the
    maintainer. Decisions for the maintainer: (1) whether limit (f) of Premise (TT) is to be reworded to cite
    clauses (vi) and (vii) here for the normalisation on a null plane; (2) whether the stored Clausius derivation
    and the other users of the imported focusing equation are to cite clause (iii) in its place, the import
    being kept for the twist term or retired; (3) whether the hypothesis of that derivation, vanishing shear at
    the point, takes a note citing clause (iv) and the Reading for what the excluded term is; (4) whether the
    one-coupling item of op.derive-loc-and-r-loc takes the Reading's paragraph on the Clausius route as an attack
    item (it is argued, not proved); (5) whether clause (v) is to be split off as a result of its own for
    op.einstein-from-the-field-theory, beside the result for fields of any strength stored with this one
    (synthesis.field-equation-linear-in-the-curvature-with-a-conserved-source-is-einsteins), which uses clauses (iv)
    and (vi) here. Prior art, not premises, all cited from memory and none read for this
    entity: the focusing equation (A. K. Raychaudhuri, 1955) and the optical scalars (R. K. Sachs, 1961);
    quantisation of the linearised gravitational field in the light-cone gauge, with the two transverse
    trace-free components as the independent variables (the light-front literature of the 1970s, following J. B.
    Kogut and D. E. Soper for electrodynamics); the shear of a null congruence as the free radiative datum on a
    null hypersurface (R. K. Sachs, 1962) and the symplectic form on the shear at null infinity (A. Ashtekar,
    1981); the uniqueness of the linearised Einstein operator among second-order operators invariant under
    linearised displacements (M. Fierz and W. Pauli, 1939; D. Lovelock, 1971, for the full theory); the reading
    of the shear term of the focusing equation as a flux of gravitational energy across a local horizon (G.
    Chirco and S. Liberati, 2010). No novelty is claimed for any clause; what is new to the store is the
    statement in the series' variables, the constant, the derivations in place of the two imports, and the exact
    checks. Credit: the result was prompted by V. Chandrasekaran, "An algebraic quantization of gravity from the null
    cone", arXiv:2611.34924 (reference Chandrasekaran2026; read on 26 November 2026 through text extraction only),
    which builds a phase space of the full theory on intersecting null cones with the shear as free data. The
    starting point (the field's canonical structure posed on a null surface, with the shear as its datum, tied to
    the expansion by the focusing equation) is taken from that paper and credited to it in the formal level; the
    idea that the shear is the free datum on a null surface is classical (Sachs, 1962); none of the paper's
    formulas is used, and apart from clause (iii) nothing here goes beyond first order or one null plane.
    The paper's author is cited, not listed under credit, which names those who worked on this entry. Ledger:
    transport-absent.
---

## formal
Units $\hbar = c = 1$, $\Cl(1,3)$ with frame $e_{0}, e_{1}, e_{2}, e_{3}$, $Q(e_{0}) = 1$, $Q(e_{i}) = -1$, and a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), whose clauses are cited by their letters: physical vectors $\hb^{-1}(a)$, the derivative $A \cdot D = D_{\hb(A)}$ along a physical vector, the curvature operator $\mathcal{R}$ in the store's sign with Ricci map $\mathcal{R}(b) = \partial_{a} \cdot \mathcal{R}(a \wedge b)$, the derived metric $g(a, b) = \hb^{-1}(a) \cdot \hb^{-1}(b)$ as a reading, and the torsion equation $D \wedge \hb^{T}(a) = \hb^{T}(\nabla \wedge a)$ of its clause (f), which fixes $\Omega$ from $\hb$. Only its clauses (i) to (e) and that torsion equation are used; the field equation of clause (f) is not assumed anywhere. Derivatives marked with a dot act on the dotted factor only. \emph{First order}, in the conventions of Theorem \claimref{synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints}: a field $h$ of symmetric linear maps of the vectors, the derived metric being $a \cdot b + h(a) \cdot b$ (Theorem \claimref{synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel}); $\ip{h_{1}}{h_{2}} = \sum_{a} h_{1}(e_{a}) \cdot h_{2}(e^{a})$, $\tau = \tr h$, and $d = \dot h(\dot\nabla)$ is the divergence of $h$. The first-order curvature is $\mathcal{R}[h](B) = -\tfrac12\,\nabla \wedge h(B \cdot \nabla)$, both derivatives acting on $h$; on $h(x) = \tfrac12 (p \cdot x)^{2} h_{0}$ it is the stored $\mathcal{R}_{p}[h_{0}]$. Write $\mathcal{E}[h]$ for its Einstein map, a second-order operator whose value on that field is the stored $\mathcal{G}_{p}[h_{0}]$. Let $n = e_{0} + e_{3}$ and $\bar n = e_{0} - e_{3}$ ($Q(n) = Q(\bar n) = 0$, $n \cdot \bar n = 2$), let $N$ be a null plane $n \cdot x = \text{const}$, whose generators run along $n$, with parameter $\lambda$ ($x = \lambda n + y$, $\partial_{n} = n \cdot \nabla = \partial/\partial\lambda$) and transverse position $y$ in the span of $e_{1}, e_{2}$. Let $\epsilon_{+}(a) = (a \cdot e_{1})e_{1} - (a \cdot e_{2})e_{2}$ and $\epsilon_{\times}(a) = (a \cdot e_{1})e_{2} + (a \cdot e_{2})e_{1}$ (the maps $n_{+}$, $n_{\times}$ of that theorem with $m_{1} = e_{1}$, $m_{2} = e_{2}$; $\ip{\epsilon_{+}}{\epsilon_{+}} = \ip{\epsilon_{\times}}{\epsilon_{\times}} = 2$, $\ip{\epsilon_{+}}{\epsilon_{\times}} = 0$), and for a field with $h(n) = 0$ write $h_{+} = \tfrac12\ip{h}{\epsilon_{+}}$, $h_{\times} = \tfrac12\ip{h}{\epsilon_{\times}}$ and $h^{TT} = h_{+}\epsilon_{+} + h_{\times}\epsilon_{\times}$, its transverse trace-free part.
\begin{enumerate}
\item[(i)] \emph{(The symplectic current; proved.)} For any two first-order fields put
\[
\omega(h_{1}, h_{2}) = \tfrac12\bigl(\dot\nabla\ip{\dot h_{1}}{h_{2}} - \dot\nabla\ip{h_{1}}{\dot h_{2}}\bigr) + \tfrac12\bigl(h_{2}(\nabla\tau_{1}) - h_{1}(\nabla\tau_{2})\bigr) + \tfrac12\bigl(\tau_{2}d_{1} - \tau_{1}d_{2}\bigr) + h_{1}(d_{2}) - h_{2}(d_{1}) - \tfrac12\bigl(\tau_{2}\nabla\tau_{1} - \tau_{1}\nabla\tau_{2}\bigr),
\]
a vector field. Then $\omega(h_{2}, h_{1}) = -\omega(h_{1}, h_{2})$ and $\nabla \cdot \omega(h_{1}, h_{2}) = \ip{\mathcal{E}[h_{1}]}{h_{2}} - \ip{h_{1}}{\mathcal{E}[h_{2}]}$ identically. So $\omega$ is conserved on pairs of solutions of the first-order equation without source, $\mathcal{E}[h] = 0$.
\item[(ii)] \emph{(Null data; proved, with the light-front rule the setting.)} At a momentum $p$ the displacements change $h(n)$ by $(n \cdot p)\xi + (n \cdot \xi)p$, a map of $\xi$ of rank four when $n \cdot p \neq 0$ and of rank one when $n \cdot p = 0$, $p \neq 0$: a field with no part constant along the generators is brought to the gauge $h(n) = 0$ by exactly one displacement. In that gauge, identically,
\[
n \cdot \omega(h_{1}, h_{2}) = \tfrac12\bigl(\ip{\partial_{n}h_{1}^{TT}}{h_{2}^{TT}} - \ip{h_{1}^{TT}}{\partial_{n}h_{2}^{TT}}\bigr) - \tfrac14\bigl(\tau_{2}\,\partial_{n}\tau_{1} - \tau_{1}\,\partial_{n}\tau_{2}\bigr), \qquad n \cdot \mathcal{E}[h](n) = \tfrac12\,\partial_{n}^{2}\tau .
\]
The flux of $\omega$ through $N$ contains the two transverse trace-free components and the trace, the trace with the opposite sign; it contains no component of $h$ along $n$ (the parts $a \mapsto (a \cdot n)w + (a \cdot w)n$, $w$ in the span of $n, e_{1}, e_{2}$) and no transverse derivative. On solutions the trace is affine along each generator, $\partial_{n}^{2}\tau = 0$, so its term is constant along each generator and vanishes on a generator closed to a period: the trace carries no datum, and its sign never enters. Taking, as in light-front quantisation, the flux of the symplectic current through $N$ (parts constant along the generators dropped) as the symplectic form of the free field, its canonical data on $N$ are $\partial_{n}h^{TT}$, two real fields on each generator; data on distinct generators are independent, and the pairing of the two components in the form is positive definite: no indefinite form enters.
\item[(iii)] \emph{(Focusing and shear of a null gradient; proved from the Definition, for every gravitational field obeying the torsion equation, weak or not.)} Let $\phi$ be a scalar field whose covariant gradient $K = \hb^{T}(\nabla\phi)$ is null, $Q(K) = 0$, and put $\mathsf{B}(A) = A \cdot D\,K$, a linear map of the physical vectors at each point. Then:
\begin{enumerate}
\item[(a)] $\mathsf{B}$ is symmetric, $A \cdot \mathsf{B}(C) = C \cdot \mathsf{B}(A)$; $K \cdot \mathsf{B}(A) = 0$ for every $A$; and $\mathsf{B}(K) = K \cdot D\,K = 0$: the integral curves of $K$ are affinely parametrised null geodesics, the generators of the hypersurfaces of constant $\phi$, with $d/d\lambda = K \cdot D$.
\item[(b)] \emph{(Riccati.)} For every physical vector field $A$, $K \cdot D\bigl(\mathsf{B}(A)\bigr) - \mathsf{B}(K \cdot D\,A) = -\mathsf{B}(\mathsf{B}(A)) - \mathcal{R}(K \wedge A) \cdot K$.
\item[(c)] $\mathsf{B}$ induces a symmetric map $\mathsf{S}$ of the screen, the two-dimensional space of physical vectors orthogonal to $K$ modulo $K$, with $\tr\mathsf{B} = \tr\mathsf{S}$ and $\tr\mathsf{B}^{2} = \tr\mathsf{S}^{2}$. With the expansion $\theta = \tr\mathsf{S}$ and the shear $\sigma = \mathsf{S} - \tfrac12\theta$, a symmetric trace-free map of the screen with $\ip{\sigma}{\sigma} = \tr\sigma^{2} \geq 0$,
\[
\frac{d\theta}{d\lambda} = -\tfrac12\,\theta^{2} - \ip{\sigma}{\sigma} + K \cdot \mathcal{R}(K), \qquad
K \cdot D\,\sigma = -\theta\,\sigma - \widehat{\mathcal{C}}, \qquad \mathcal{C}(a, b) = (K \wedge b) \cdot \mathcal{R}(K \wedge a) ,
\]
the hat denoting the trace-free part on the screen, and $\mathcal{C}$ may be formed with the Weyl map $\mathcal{W}$ in place of $\mathcal{R}$, the two forms differing on the screen by a multiple of the product. (In components $\ip{\sigma}{\sigma}$ is $\sigma_{ab}\sigma^{ab}$.) These are the focusing and shear equations in the store's sign, for a congruence with no twist.
\end{enumerate}
\item[(iv)] \emph{(The datum is the shear of the generators; proved.)} Let $\hb^{-1} = \id + s$ with $s$ a field of symmetric maps and $s(n) = 0$, of any size, and $\Omega$ fixed by the torsion equation. Then $\hb^{T}(n) = \hb(n) = \hb^{-1}(n) = n$, so (iii) holds with $\phi = n \cdot x$ and $K = n$: $N$ is ruled by null geodesics of the field along $n$, with $K \cdot D = \partial_{n}$ on scalars, and for background vectors $a, b$
\[
\tfrac12\,\partial_{n}\,g(a, b) = \hb^{-1}(a) \cdot \mathsf{B}\bigl(\hb^{-1}(b)\bigr) .
\]
At first order ($h = 2s$) this is the gauge of (ii), $\mathsf{B} = \tfrac12\,\partial_{n}h$, and the expansion and shear of the generators of $N$ are
\[
\theta = \tfrac12\,\partial_{n}\tau, \qquad \sigma = \tfrac12\,\partial_{n}h^{TT} :
\]
the canonical datum of (ii) is twice the shear. The equation of (ii) along the generators is $\partial_{n}\theta = n \cdot \mathcal{E}[h](n)$, the focusing equation of (iii) at first order. For transverse $u, a, b$, $n \cdot \mathcal{R}[h](n \wedge u) = \tfrac12\,\partial_{n}^{2}h(u)$ and $(n \wedge b) \cdot \mathcal{R}[h](n \wedge a) = -\tfrac12\,\partial_{n}^{2}h(a) \cdot b$, whose trace-free part is the first-order shear equation of (iii), $\partial_{n}\sigma = -\widehat{\mathcal{C}}$. The curvature is unchanged by displacements, so $\partial_{n}\sigma$, and with it $\sigma$ up to a part constant along the generator, does not depend on the gauge. The stored first-order curvature $\mathcal{R}_{p}[h_{0}]$ is the curvature operator of the field $\hb^{-1} = \id + \tfrac14(p \cdot x)^{2}h_{0}$, with $\Omega$ fixed by the torsion equation, at $x = 0$, exactly and in the store's sign.
\item[(v)] \emph{(The first-order operator; proved.)} The linear maps $h \mapsto E_{p}[h]$ of the symmetric maps, homogeneous of degree two in a vector $p$, that commute with the rotors, $E_{Rp\tilde R}[Rh(\tilde R\,\cdot\,R)\tilde R] = R\,E_{p}[h](\tilde R\,\cdot\,R)\,\tilde R$, form a space of dimension five, spanned by
\[
Q(p)\,h, \qquad Q(p)\,\tau\,\id, \qquad (p \cdot h(p))\,\id, \qquad \tau\,(a \mapsto (a \cdot p)\,p), \qquad a \mapsto (a \cdot p)\,h(p) + (a \cdot h(p))\,p .
\]
Those that vanish on every displacement $a \mapsto (a \cdot p)\xi + (a \cdot \xi)p$ form the two-dimensional space spanned by the Ricci map of $\mathcal{R}_{p}$ and $\id$ times its trace. Of these, the ones symmetric for the pairing, and equally the ones with conserved values, $E_{p}[h](p) = 0$, are the multiples of the Einstein map $\mathcal{G}_{p}$. So a linear differential equation for $h$ with constant coefficients that is (L) homogeneous of second order and covariant under the rotors, (D) unchanged by displacements of $h$, and (V) the stationarity condition of a quadratic functional, is $c\,\mathcal{E}[h] = \text{source}$, with one constant.
\item[(vi)] \emph{(The constant; proved, given (L), (D), (V) for the first-order field and (N).)} Hypothesis (N): the interaction that the first-order field gives two bodies at rest, $T_{i}(a) = m_{i}(a \cdot e_{0})e_{0}$, is the stored Newtonian coupling $-G m_{1}m_{2}/r$ of Proposition \claimref{field-theory.operator-newtonian-coupling}, which takes that coupling as its input and does not derive it; (N) is what gives $G$ its meaning here. With the response of matter to the field of Theorem \claimref{synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel}(v), which at first order is $-\tfrac12\ip{h}{T}$, the functional $c\int\ip{h}{\mathcal{E}[h]}$ gives two bodies at rest the interaction $m_{1}m_{2}/(8c\,|\mathbf{k}|^{2})$ at spatial momentum $\mathbf{k}$, and this is the transform $-4\pi G\,m_{1}m_{2}/|\mathbf{k}|^{2}$ of the coupling of (N) exactly for $c = -1/32\pi G$:
\[
S[h] = -\frac{1}{32\pi G}\int \ip{h}{\mathcal{E}[h]}, \qquad \mathcal{E}[h] + 8\pi G\,T = 0 .
\]
The field of a source at $Q(p) \neq 0$ is $h = 16\pi G\,(T - \tfrac12\,\id\,\tr T)/Q(p)$ up to a displacement, the interaction of two sources is $\tfrac12\ip{T_{1}}{h[T_{2}]} = 8\pi G\,B(T_{1}, T_{2})/Q(p)$, and on maps transverse and trace-free at their momentum, where $\mathcal{G}_{p} = \tfrac12 Q(p)$, the functional has density $\tfrac{1}{64\pi G}\ip{\partial h}{\partial h}$ up to a divergence, with $\ip{\partial h}{\partial h} = \sum_{a}\ip{(e_{a} \cdot \nabla)h}{(e^{a} \cdot \nabla)h}$, whose exchange between conserved sources at a null momentum has the residue $8\pi G\bigl(\tfrac12\ip{T_{1}}{\epsilon_{+}}\ip{T_{2}}{\epsilon_{+}} + \tfrac12\ip{T_{1}}{\epsilon_{\times}}\ip{T_{2}}{\epsilon_{\times}}\bigr)$ of Theorem \claimref{synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints}(iv). The field equation is clause (f) of the Definition at first order, with $G$ restored; it is obtained here from (L), (D), (V) and (N), and nothing in clause (f) is used to obtain it. The symplectic current of $S$ is $\omega/16\pi G$. Hence, with the orientation in which the future null translations have a positive generator, the symplectic form and that generator, the null energy, are
\[
\varpi(h, h') = \frac{1}{8\pi G}\sum_{i \in \{+, \times\}}\int_{N} h_{i}\,\partial_{n}h_{i}'\;d\lambda\,d^{2}y, \qquad P = \frac{1}{32\pi G}\int_{N}\ip{\partial_{n}h^{TT}}{\partial_{n}h^{TT}}\,d\lambda\,d^{2}y = \frac{1}{8\pi G}\int_{N}\ip{\sigma}{\sigma}\,d\lambda\,d^{2}y \;\geq\; 0 ,
\]
with $\varpi(\partial_{n}h, h') = dP(h')$: $8\pi G$ times the density of null energy of the two components on $N$ is $\ip{\sigma}{\sigma}$.
\item[(vii)] \emph{(Modes; proved, with the quantisation rule a hypothesis.)} In the discretised light-cone setting, a generator closed to period $2\pi$ with a transverse cell of area $s$, $h_{i} = \sum_{k \geq 1}(a_{ik}\cos k\lambda + b_{ik}\sin k\lambda)$ for $i \in \{+, \times\}$ (the part constant along the generator carries no shear). Then $\varpi = \tfrac{s}{8G}\sum_{i,k} k\,(a_{ik}b_{ik}' - b_{ik}a_{ik}')$, $P = \tfrac{s}{16G}\sum_{i,k} k^{2}(a_{ik}^{2} + b_{ik}^{2})$, and the bracket for which $P$ generates $\lambda \mapsto \lambda + t$ is $\{a_{ik}, b_{jl}\} = 8G\,\delta_{ij}\delta_{kl}/(sk)$. Under the quantisation hypothesis $[\,,\,] = I_{4}\{\,,\,\}$ (Dirac's rule, with the unit of Premise \claimref{synthesis.premise-canonical-pair-on-the-two-null-directions}, the scalars of the mode space being $\mathrm{span}\{1, I_{4}\}$), the modes $\alpha_{ik} = (s/16G)^{1/2}\,k\,(a_{ik} + I_{4}b_{ik})$ satisfy
\[
[\alpha_{ik}, \alpha_{jl}^{*}] = k\,\delta_{ij}\delta_{kl}, \qquad [\alpha_{ik}, \alpha_{jl}] = 0, \qquad [P, \alpha_{ik}] = -k\,\alpha_{ik},
\]
and the sign $+k$ is the same for either orientation of the unit: it is fixed by positive null energy. So $k^{-1/2}\alpha_{ik}$ and its adjoint are a canonical pair, with the representation $\partial/\partial z$, $z$ on polynomials of Proposition \claimref{field-theory.fock-space-maxwell-modes}(1), and in a state of $N$ quanta at level $k$, $a_{ik}^{2} + b_{ik}^{2}$ has the value $8G(2N + 1)/(sk)$: each quantum adds $16G/(sk)$, so in a cell of area $s$ the amplitude of one quantum is of the order of the Planck length over $\sqrt{sk}$. Beyond one flat chart: the closed generator identifies points along a null direction of the background, the periodic setting of discretised light-cone quantisation; it is used for the mode count only, and the statements of (i) to (vi) are on the open plane.
\item[(viii)] \emph{(The two helicities; proved.)} The rotation about the generator $u \mapsto Ru\tilde R$, $R = e^{e_{1}e_{2}\phi/2}$, fixes $n$ and $\bar n$ and acts on fields by $h \mapsto Rh(\tilde RaR)\tilde R$; it leaves $\tau$ unchanged and turns the two components by twice its angle, $h_{+} \pm U h_{\times} \mapsto (\cos 2\phi \pm U\sin 2\phi)(h_{+} \pm Uh_{\times})$ for any unit $U$ commuting with the components, $U^{2} = -1$. So $\beta_{\pm,k} = 2^{-1/2}(\alpha_{+k} \pm I_{4}\alpha_{\times k})$ satisfy $[\beta_{\pm,k}, \beta_{\pm,l}^{*}] = k\,\delta_{kl}$, $[\beta_{+,k}, \beta_{-,l}^{*}] = 0$, are multiplied by $e^{\pm 2I_{4}\phi}$ under the rotation and by $e^{-I_{4}kt}$ under the null translation by $t$: on each generator, two commuting chiral current algebras, the two helicities $\pm 2$ being the two relative orientations of the rotation and the null translation.
\end{enumerate}
\emph{Source of the idea.} That the free data of the gravitational field on a null surface are the shear of its generators, that the expansion is tied to the shear by the focusing equation, and that a null surface is therefore the place to pose the field's canonical structure, is the starting point of \cite{Chandrasekaran2026}, which does this for the full theory on intersecting null cones, with corner terms, a clock and a space of states that are not treated here. This result was prompted by that paper and takes its starting point from it; that the shear is the free datum of the field on a null surface is itself classical (R. K. Sachs, 1962, cited from memory). What is done here is its first order on one null plane, in the series' variables and by the route of the stored photon result, with the derivations and the constants of clauses (i) to (viii); the paper was read through text extraction only, and none of its formulas is used.

\emph{Reading (argued).} \emph{Premise (TT).} The premise posits, at first order, a canonical pair on the two transverse trace-free directions at each nonzero null momentum, on polynomials over $\mathrm{span}\{1, I_{4}\}$, and says in its limit (f) that the normalisation of the free part is not computed in the store. Clauses (ii), (vi) and (vii) compute it on a null plane: the flux of the symplectic current of the stored first-order map is a definite form on exactly those two components, its constant is fixed by matching the Newtonian coupling, hypothesis (N), and agrees with the stored residue at the cone, and on a closed generator it gives the pairs $k^{-1/2}\alpha_{ik}$ with the premise's representation. What is assumed and not proved is what the stored photon result assumes, that the flux through one null plane is the whole symplectic form (the data on a null plane are complete once the parts constant along the generators are dropped, the light-front setting) and Dirac's rule; together with the conditions (L), (D), (V) of (v) for the field equation and the matching (N) of (vi). Under a transverse Fourier transform over the generators, the two modes at level $k$ are the modes that the premise places at the null momenta $p$ with $n \cdot p = k$ and at their negatives; that identification is not carried out here. \emph{The shear.} By (iv) the canonical datum of the premise's mode on a null plane is, to the factor two, the shear of the plane's generators, and by (vi) its null energy is $\tfrac{1}{8\pi G}\int\ip{\sigma}{\sigma}$. In the focusing equation of (iii), with the field equation in the form $K \cdot \mathcal{R}(K) = -8\pi G\,K \cdot T(K)$ for null $K$ (clause (vi) at first order; for a field that is not weak it is clause (f) of the Definition, obtained from two named conditions in Theorem \claimref{synthesis.field-equation-linear-in-the-curvature-with-a-conserved-source-is-einsteins}), the generators obey $d\theta/d\lambda = -\tfrac12\theta^{2} - \ip{\sigma}{\sigma} - 8\pi G\,K \cdot T(K)$: the null energy density of the two components stands in it with the coefficient of the matter's, $-8\pi G\,(\tfrac{1}{8\pi G}\ip{\sigma}{\sigma} + K \cdot T(K))$. The equality of the two coefficients is proved here, and so is the focusing equation, which is exact; the first-order field supplies $\sigma$, so the comparison holds at the leading order, the second, in $h$. So, to that order, the two components gravitate through their null energy as matter does, with no further constant. \emph{The Clausius route.} Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius} takes local horizons with vanishing expansion and shear at the point, which removes this term there. In the series' variables the removed term is $8\pi G$ times the null energy of the pair of Premise (TT) crossing the patch; on a patch that it does cross, the area deficit of a cut counts that energy and the matter's with one coefficient. This is a statement about the focusing equation and the field equation; no entropy is assigned to the pair here, and whether the one-coupling clause of (Loc) holds for it is not shown. \emph{The field equation.} Clauses (v) and (vi) do not derive Einstein's equations; the theorem just cited, stored with this one, does so for a field of any strength under its conditions (Q) and (C), and takes its constant from clause (vi) here. They show that at first order nothing is left to choose once the field is the whole symmetric map up to displacements, its equation is local of second order and comes from a functional, and matter enters by its response: the operator is the Einstein map and the constant is Newton's. Those conditions are the whole-stress clause at first order in another form, and they are assumed. \emph{Limits.} Apart from (iii), first order and one null plane only. Beyond first order the trace is no longer free of the shear (the term $-\ip{\sigma}{\sigma}$ of (iii) sources it), the decoupling of (ii) is not available as stated, and null planes become null cones with caustics; none of that is treated. Clause (iii) covers gradients only, so it has no twist term. No state is selected: a ground state for $P$ would be annihilated by every $\alpha_{ik}$, the pair's form of the null ground state of Premise \claimref{synthesis.n-plus-null-ground-state}, which is not extended to the pair here. The dipole obstruction of the stored lattice model and the question of a dressing are untouched.

## technical
The series holds the first-order gravitational field as a field of symmetric maps on flat spacetime, with a stored first-order curvature and Einstein map, and since 24 November 2026 it posits a canonical pair on the two transverse trace-free directions at each null momentum (Premise (TT)), with a normalisation that was not computed. This result computes that structure on a null plane, in the way the stored photon result does for the Maxwell field, and it imports nothing: the two results it would otherwise have taken from the literature are derived in it. The result was prompted by \cite{Chandrasekaran2026}, which poses the canonical structure of the full theory on null cones with the shear of their generators as the datum, and it takes that starting point from the paper; that the shear is the free datum on a null surface is classical (Sachs, 1962). Here the question is taken to first order only.

The stored Einstein map is symmetric, so it has a conserved bilinear current on pairs of solutions; the current is written out and its divergence identity checked exactly. In the gauge in which the field annihilates the null direction of the plane, the flux of that current through the plane contains only the two transverse trace-free components and the trace. The trace enters with the opposite sign, but the one field equation along the generators says its second derivative vanishes, so it carries no data and its sign never matters. The canonical data on the plane are the derivatives of the two components along the generators, two real fields per generator, independent from one generator to the next.

The focusing and shear equations are proved from the definition of the gravitational field. For a null vector field that is the covariant gradient of a scalar, the map $\mathsf{B}(A) = A \cdot D\,K$ is symmetric and annihilates $K$, so the curves of $K$ are null geodesics; commuting two covariant derivatives, with the torsion equation, gives a Riccati equation for $\mathsf{B}$ with the curvature as its source; its trace is the focusing equation and its trace-free part the shear equation. This holds for every field obeying the torsion equation and is checked exactly on a field that is not weak, built with the gauge fields themselves.

In the gauge above the plane is ruled by null geodesics along its null direction for a field of any size, and half the derivative of the derived metric along them is $\mathsf{B}$. At first order the expansion is half the derivative of the trace and the shear half the derivative of the trace-free part: the canonical datum is twice the shear, the equation along the generators is the focusing equation, and the curvature component that the data determine is the rate of change of the shear. The stored first-order curvature is confirmed against the definition, sign included.

The first-order field equation is not imported either. Among linear maps of symmetric maps that are quadratic in the momentum and commute with the rotors there are exactly five independent ones (an exact finite computation); those that vanish on displacements are two, and the one that comes from a functional is the Einstein map. The constant then follows from matching the stored Newtonian coupling for two bodies at rest, which is a hypothesis and is what gives Newton's constant its meaning here: the functional is minus one over $32\pi G$ times the pairing of the field with its Einstein map. It reproduces the stored field of a source, the stored interaction and the stored residue at the cone. With it, $8\pi G$ times the null energy density of the two components equals the square of the shear, which is the term that stands beside the matter's null energy in the focusing equation.

On a closed generator the Fourier coefficients of each component are canonical pairs with bracket $8G/(sk)$ for a cell of area $s$; with Dirac's rule and the unit $I_{4}$ they give two commuting chiral current algebras per generator, and a rotation about the generator turns the two components by twice its angle, so the two algebras are the helicities plus and minus two.

Assumed and not proved: that the flux through one null plane is the whole symplectic form, and Dirac's rule, both assumed by the stored photon result too; and, for the field equation, that it is local of second order, covariant, unchanged by displacements and comes from a functional, and that its static limit is Newton's law. The field equation of the stored definition is not used. Apart from the focusing and shear equations, everything is first order on one null plane. No state is selected.

Ledger: transport-absent. This is the light-cone-gauge structure of the linearised gravitational field of standard physics, stated in the series' variables with exact checks.

## lay
A gravitational wave stretches space one way and squeezes it the other as it passes. The series treats weak gravity as a field on flat spacetime, and it has recently assumed that the two polarisations of such a wave are quantum variables, like light. That assumption came with a gap: it did not say how big one quantum is.

This result fills the gap by looking at the field on a wall of light: a flat surface swept out by parallel light rays. On such a surface the mathematics simplifies. Of the ten components of the weak gravitational field, eight drop out or are fixed by the equations, and exactly two remain free on each light ray.

Those two have a direct meaning. Neighbouring light rays on the surface form a little bundle with a round cross-section. A passing gravitational wave distorts that circle into an ellipse without changing its area. The rate of that distortion is called the shear, and the two free components are precisely the shear, in its two orientations.

The size of one quantum then follows with no new number. The law of weak gravity is pinned down by a few general requirements, and its strength by Newton's law of attraction. For a patch of the surface of a given area, the stretch produced by one quantum is roughly the Planck length divided by the size of the patch.

One more thing falls out. The energy carried by the wave across the surface is the square of the shear, divided by a known constant. That is exactly the term by which shear makes bundles of light rays converge, in the same way and with the same strength as the energy of ordinary matter does. The equation that says so is a classical one, and it is proved here from the series' own definition of gravity, not taken from a textbook. So the two wave components gravitate like everything else.

This work was prompted by a 2026 paper by V. Chandrasekaran, which reads gravity's free data off surfaces of light, as the shear of their rays, for gravity at full strength; the underlying idea goes back to R. Sachs in the 1960s. All of this holds only for weak fields on one flat surface of light, and it is the standard account written in the series' language.

## one-liner
At first order, in the gauge $h(n) = 0$, the flux through a null plane of the symplectic current of the stored Einstein map holds only the two transverse trace-free components (the trace, of opposite sign, is removed by the focusing equation $\partial_{n}^{2}\tau = 0$), and its canonical datum is twice the shear of the plane's generators, $\sigma = \tfrac12\partial_{n}h^{TT}$; the focusing and shear equations are proved from the definition of the gravitational field (a Riccati equation for $A \mapsto A \cdot D\,K$), the first-order operator is shown to be the Einstein map by an exact count (five covariant second-order maps, two vanishing on displacements, one from a functional) and its constant $-1/32\pi G$ comes from matching the stored Newtonian coupling, so the null energy is $\tfrac{1}{8\pi G}\int\ip{\sigma}{\sigma}$, the term that stands beside the matter's in the focusing equation, and on a closed generator with cell area $s$ the bracket is $\{a_{k}, b_{k}\} = 8G/(sk)$, giving with Dirac's rule and $I_{4}$ two chiral current algebras per generator of helicity $\pm 2$: the normalisation that Premise (TT) left uncomputed, on a null plane, with no imported Fact as a premise.
