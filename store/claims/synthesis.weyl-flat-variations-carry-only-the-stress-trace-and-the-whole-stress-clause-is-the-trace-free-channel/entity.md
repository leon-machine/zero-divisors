---
id: synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel
kind: claim
version: 1
title: 'Weyl-flat variations carry only the stress trace'
status: proved
region: synthesis
subject: einstein
tags: [curvature-and-field-equations, gauge-fields, forcing-and-uniqueness, no-go]
proposed_by:
  kind: ai
  session: 2026-11-02-qft-full
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
derivations:
- name: main
  uses:
  - synthesis.twistor-flat-fields-give-nordstrom-not-einstein@2
  - synthesis.imported-maxwell-stress-spacetime-algebra@2
  - synthesis.imported-nordstrom-scalar-theory-einstein-fokker-form@1
  - synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians@1
  - synthesis.imported-gtg-dictionary@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_linear_curvature_kernels
- kind: check
  ref: check.py::check_stabiliser_commutant_on_gauge_quotient
- kind: check
  ref: check.py::check_null_momentum_has_further_classes
- kind: check
  ref: check.py::check_conserved_source_pairing_channels
- kind: check
  ref: check.py::check_null_flux_is_the_trace_free_channel
- kind: check
  ref: check.py::check_minimal_coupling_responses
- kind: check
  ref: check.py::check_point_source_coupling_is_universal
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.twistor-flat-fields-give-nordstrom-not-einstein
  - synthesis.einstein-equations-from-c-loc-and-clausius
  - synthesis.inverse-problem-for-the-clausius-route
  - synthesis.vacuum-field-stress-tensor-is-einstein-tensor-or-trace
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: synthesis.imported-gtg-dictionary repinned 1 -> 2 after reviewing its correction of the component reading in clause (iv) to R(g_mu ^ g_nu) = -R(e_mu ^ e_nu), agreeing with the store''s sign R(B) = -R(hb(B)) the clause already stated, with GA wording in (ii) and (iv); the translation rules are unchanged; the use here holds as cited.'
  open_problem: op.einstein-from-the-field-theory
  note: >-
    Constructive attack on the open problem's second attack (derive the whole-stress clause from the field
    theory). Three routes were tried. (1) The gauge principle of Gauge Theory Gravity: the position-gauge field
    gauges displacements, and minimally coupled matter responds to it with its whole stress, canonical for a scalar and Belinfante-improved for the Maxwell field (clause
    (v), standard: Kibble 1961, Hehl, Lasenby, Doran and Gull 1998, cited from memory). But displacement gauge
    invariance does not decide which fields are varied: the Weyl-flat class is closed under every displacement
    (the gauge directions lie in the kernel of the linearised Weyl map, clause (i)), and varying within it gives
    Nordstrom's trace coupling (clause (iii)), the Einstein-Fokker form being generally covariant. So the
    clause is not a consequence of gauge invariance; it is the statement that the field is varied in the five
    directions that leave the Weyl-flat class. (2) The Deser self-coupling bootstrap keeps the channel it
    starts from: a symmetric-tensor seed gives Einstein's equations (Deser 1970), a scalar seed coupled to the
    trace gives a Nordstrom-type theory (Freund and Nambu 1968, Phys. Rev. 174, 1741); both cited from memory,
    the second located by search; it moves the question to the field content and is not filed. (3) Weinberg's
    soft-graviton universality (1964 to 1965, cited from memory), read classically as the linear algebra of
    clause (vi): displacement gauge invariance of a coupling through the field forces one coupling for all
    point sources (the equivalence principle), in every class; it does not select the channel, but in the
    trace channel massless sources have zero coupling, the stored absence of light deflection in Nordstrom's
    theory. Circularity: the past cone contains no postulate and no result that assumes the clause; the only
    entity there that names Einstein's equations is the dictionary Fact interior.imported-equivalence-einstein-equations
    (through the tractor gauge field result), and clause (f) of the definition of the gravitational field
    (the field equation) is not used. Cross-readings, not dependencies: the Clausius route
    synthesis.einstein-equations-from-c-loc-and-clausius takes its heat from the null fluxes T(k, k), which by
    clause (iv) are exactly the trace-free channel, and it returns Lambda as an integration constant, the
    zero-momentum remainder of clause (iv); the inverse-problem result synthesis.inverse-problem-for-the-clausius-route
    states that the coupled system is variational exactly when the heat tensor is the Hilbert stress, and
    clause (v) supplies the minimally coupled response that would be that stress; the vacuum-field result
    synthesis.vacuum-field-stress-tensor-is-einstein-tensor-or-trace shows a source read off the vacua is a
    relabelling or pure trace, so the trace-free channel needs a datum of the matter, here its response off
    the Weyl-flat class. For the quantum Dirac field the imported renormalised stress
    (synthesis.imported-renormalised-stress-tensor-of-hadamard-dirac-states) adds to the trace channel a
    state-independent anomaly, so for massless fields every state-dependent part of the stress lies in the
    trace-free channel (argued, not used). Transport-convenient for the placement of the attachment's domain
    as the trace channel (the domain is fixed by twistor transport in the stored result); transport-absent
    otherwise: the spin-zero and spin-two split of linearised gravity, Nordstrom's theory in the
    Einstein-Fokker form, the unimodular mechanism and Weinberg's universality are standard, re-derived here
    in the spacetime algebra. New: the attachment's domain identified as the trace channel of the variational
    problem, the decoupling of conformal matter there, the null-flux form of the Clausius route identified as
    the trace-free channel, and the reduction of the clause to variations off the attachment's domain.
---

## formal
Let $V$ be the vectors of $\Cl(1,3)$, signature $(+,-,-,-)$, with frame $\{e_{a}\}$ and reciprocal frame $\{e^{a}\}$, and consider gravitational fields $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}; only its clauses (i) to (e) are used, not the field equation (f)) at first order about $\hb = \id$, $\Omega = 0$: the derived metric is $g(a, b) = a \cdot b + h(a) \cdot b$ with $h$ a symmetric linear map of $V$. Fix a nonzero $p \in V$ and the field $h(x) = \tfrac12 (p \cdot x)^{2} h_{0}$, $h_{0} \in \mathrm{Sym}$ (the symmetric maps, dimension $10$); its first-order curvature is the constant map $\mathcal{R}_{p}[h_{0}](B) = -\tfrac12\,p \wedge h_{0}(B \cdot p)$ (up to the overall sign of the curvature convention, on which nothing below depends), with Ricci map, scalar $\mathcal{R}_{p}$, Schouten map and Weyl map $\mathcal{W}_{p}[h_{0}]$ formed as in Fact \claimref{synthesis.imported-gtg-dictionary}. A displacement $x \mapsto x + \tfrac12 (p \cdot x)^{2}\xi$ changes $h_{0}$ by $a \mapsto (a \cdot p)\xi + (a \cdot \xi)p$; these form the gauge space $G_{p}$. Write $L = \R\,\id$ (the conformal direction, $\hb^{-1}(a) = \phi\,a$ at first order). A \emph{conserved source at $p$} is $T_{0} \in \mathrm{Sym}$ with $T_{0}(p) = 0$; pair $h_{0}$ with $T_{0}$ by $\ip{h_{0}}{T_{0}} = \sum_{a} e^{a} \cdot h_{0}(T_{0}(e_{a}))$.
\begin{enumerate}
\item[(i)] \emph{(Kernels; proved.)} $\ker \mathcal{R}_{p} = G_{p}$ (dimension $4$) and $\ker \mathcal{W}_{p} = G_{p} \oplus L$ (dimension $5$), for every nonzero $p$, null or not. The kernel of the scalar $h_{0} \mapsto \mathcal{R}_{p}[h_{0}]$ has dimension $9$ and contains $G_{p}$; the scalar of $\id$ is $3\,Q(p)$, so for $Q(p) \neq 0$ this kernel is $G_{p} \oplus C_{p}$ with $C_{p} \cap L = 0$.
\item[(ii)] \emph{(Exactly four covariant classes; proved for $Q(p) \neq 0$.)} The stabiliser of $p$ in the Lorentz group preserves $G_{p}$, and its commutant on the six-dimensional quotient $\mathrm{Sym}/G_{p}$ has dimension $2$. Hence $\mathrm{Sym}/G_{p}$ is the sum of two inequivalent irreducible pieces, the images of $L$ (dimension $1$) and of $C_{p}$ (dimension $5$), and the subspaces of $\mathrm{Sym}$ that contain $G_{p}$ (closed under displacements) and are invariant under the stabiliser are exactly $G_{p}$, $G_{p} \oplus L$, $G_{p} \oplus C_{p}$ and $\mathrm{Sym}$. The second is the tangent space of the Weyl-flat fields; by Theorem \claimref{synthesis.twistor-flat-fields-give-nordstrom-not-einstein}(i) these are the twistor-flat fields, the domain on which the twistor attachment is carried by transport. At null $p$ the stabiliser is not reductive and the count fails (computed at $p = e_{0} + e_{1}$): with $N_{p}$ the two transverse trace-free (helicity-two) directions, $G_{p} \oplus N_{p}$ and $G_{p} \oplus L \oplus N_{p}$ are further invariant classes, and the scalar-flat kernel contains $L$, so there are at least six. Clauses (iii) and (iv) do not use (ii).
\item[(iii)] \emph{(What each class sees of a conserved source; proved.)} The conserved sources at $p$ form a space of dimension $6$; the pairing vanishes on $G_{p}$ and is nondegenerate between $\mathrm{Sym}/G_{p}$ and the conserved sources. A conserved source annihilates $G_{p} \oplus L$ if and only if its trace $\tau = \tr T_{0}$ vanishes, and (for $Q(p) \neq 0$) annihilates $G_{p} \oplus C_{p}$ if and only if $T_{0}(a) = \lambda\,(Q(p)\,a - (a \cdot p)\,p)$. So a field equation obtained by varying the field only within the Weyl-flat class, $\ip{\delta h_{0}}{E_{0} + \kappa T_{0}} = 0$ for $\delta h_{0} \in G_{p} \oplus L$, is one condition on the trace of the source and leaves its five trace-free components free (Nordstr\"om's coupling, Fact \claimref{synthesis.imported-nordstrom-scalar-theory-einstein-fokker-form}); varying within $\mathrm{Sym}$ gives all six.
\item[(iv)] \emph{(The null flux is the trace-free channel; proved.)} A symmetric map $T$ is determined by its null fluxes $k \cdot T(k)$, $Q(k) = 0$, up to adding $c\,\id$. A conserved source at $p \neq 0$ that is a multiple of $\id$ is zero. Hence if $X = E_{0} + \kappa T_{0}$ is conserved at $p \neq 0$ and its trace-free part vanishes, then $X = 0$: the trace-free channel together with conservation fixes the whole conserved source at every nonzero momentum, leaving only a constant multiple of $\id$ (a cosmological term) at $p = 0$.
\item[(v)] \emph{(Response of minimally coupled matter; proved, standard.)} If a matter Lagrangian density depends on the gravitational field only through $\hb$ applied to its derivatives (as an outermorphism on a field strength) and the factor $(\det \hb)^{-1}$, its derivative along $\hb = \id + t\,\delta$ at $t = 0$ is $\sum_{a} \delta(e_{a}) \cdot T(e^{a})$ with $T$ its $\hb$-response stress map. For a scalar field this is the canonical stress of displacements. For Maxwell matter, with density $\tfrac12\br{\hb(F)^{2}}/\det\hb$ for a field strength bivector $F = \nabla \wedge A$ held fixed, it is the symmetric gauge-invariant stress $T(a) = -\tfrac12 FaF$, the Belinfante-improved canonical stress (Fact \claimref{synthesis.imported-maxwell-stress-spacetime-algebra}) and its response to $\delta = \id$ vanishes; for a scalar field it is $(a \cdot \nabla\phi)\nabla\phi - a\,\mathcal{L}$, of trace $-Q(\nabla\phi) + 2m^{2}\phi^{2}$. More generally a density that depends on $\hb$ algebraically and is unchanged under $\hb \mapsto c\,\hb$ for constant $c$ has zero response along $\id$ at each point, so such matter (the Maxwell field) does not couple at first order to variations within the Weyl-flat class; for the massless Dirac field the same holds classically, on shell, since its stress has trace proportional to the mass (standard, cited from memory, not checked here); at the quantum level the trace anomaly contains a scheme-dependent $\Box\mathcal{R}$ term, first order in $h$ and nonzero on $L$ (the scalar of $\id$ is $3\,Q(p)$), so this decoupling is classical.
\item[(vi)] \emph{(One coupling; computed, standard.)} For point sources coupled through the field with strengths $\kappa_{n}\,p_{n} \cdot h_{0}(p_{n})$, invariance under $h_{0} \mapsto h_{0} + q \otimes \xi + \xi \otimes q$ requires $\sum_{n} s_{n}\kappa_{n}\,p_{n} = 0$ ($s_{n} = \pm 1$ for incoming and outgoing), which on the momentum-conserving configuration of five momenta spanning $V$ computed here (one linear relation among them) forces all $\kappa_{n}$ equal; with more momenta the condition must be imposed on every conserved configuration, as in Weinberg's argument; a source with $Q(p_{n}) = 0$ has zero coupling to $L$.
\item[(vii)] \emph{(Reading; argued.)} Displacement gauge invariance does not give the whole-stress clause: the Weyl-flat class is closed under displacements and gives the trace coupling. Under an action principle in which matter is minimally coupled and the field is varied in the five directions $C_{p}$ that leave the Weyl-flat class, the source is the whole response of (v), and by (iv) its trace-free part already fixes it up to the cosmological term; with Fact \claimref{synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians}(a) the second-order field equations are then Einstein's. The clause is therefore equivalent, at first order and under that action principle, to the matter theory being defined and varied off the attachment's domain; the Maxwell field (and, classically, the massless Dirac field) confined to that domain does not gravitate at first order. For matter with spin, $\Omega$ is varied independently (the Einstein-Cartan choice of the definition): the $\hb$-response is then the canonical stress, whose antisymmetric part enters the antisymmetric part of the $\hb$ equation, while the $\Omega$ equation ties the torsion to the spin density; after the torsion is eliminated the symmetric source is the Belinfante stress plus a spin-spin contact term of order $\kappa$, second order in the coupling, so at first order the channels of (iii) and (iv) apply to the Belinfante stress (standard, cited from memory). The quantum stress must stay conserved for (iv) to apply: for chiral matter this needs the mixed gravitational anomaly to cancel (argued).
\end{enumerate}

## technical
The open problem asks for the clause that the whole stress map, not its trace, is the gravitational source, to be derived from the field theory. This result works at first order about flat spacetime in Gauge Theory Gravity and asks which variations of the position-gauge field $\hb$ see which parts of the stress. At a momentum $p$ the symmetric perturbations $h_{0}$ (ten) split into the displacement gauge directions $G_{p}$ (four), the conformal line $L$ (one) and five further directions. Exact computations at the Lorentz-orbit representatives of every nonzero momentum show that the first-order curvature vanishes exactly on $G_{p}$ and the first-order Weyl curvature exactly on $G_{p} \oplus L$; the commutant of the stabiliser of $p$ on the six non-gauge directions is two-dimensional, so at every non-null momentum there are exactly four classes of fields closed under displacements and covariant under that stabiliser: gauge only, Weyl-flat (Nordstr\"om), scalar-flat, and all fields. At null momentum, the momentum of radiation, the stabiliser is not reductive and there are further classes, among them gauge plus the two helicity-two directions; the pairing statements below hold there too. The Weyl-flat class is the domain of the twistor attachment (stored). Pairing with a conserved source, the Weyl-flat class sees only its trace and leaves its five trace-free components free; all fields see all six. The null fluxes $k \cdot T(k)$ that the Clausius route uses determine $T$ up to a multiple of the identity, so they are exactly the trace-free channel, and a conserved source with no trace-free part is zero at nonzero momentum (the unimodular mechanism), which is why that route returns $\Lambda$ as an integration constant. The response of minimally coupled matter to $\hb$ is its $\hb$-response stress: for the Maxwell field the symmetric gauge-invariant (Belinfante) stress $-\tfrac12 FaF$, with zero response to the conformal direction, and for a scalar the canonical stress, with nonzero trace. For Dirac matter, under the Einstein-Cartan choice, the first-order symmetric source is the Belinfante stress and the spin contact term is second order; its decoupling from the conformal direction when massless is classical, the trace anomaly being first order there. Point sources coupled through the field must share one coupling, and massless ones do not couple to the conformal line. The reading: gauge invariance does not give the clause, since the Weyl-flat class is closed under displacements and yields Nordstr\"om's coupling; under an action principle with minimal coupling the clause is equivalent to varying the field off the attachment's domain, where the Maxwell field (and, classically, the massless Dirac field) would otherwise not gravitate at first order. Standard pieces (the spin-zero and spin-two split, Einstein-Fokker, unimodular gravity, Weinberg's universality) are re-derived in the spacetime algebra; new is their placement against the attachment's domain and the Clausius route.

## lay
Einstein's theory says that everything about matter's energy, momentum and pressure is a source of the gravitational field. An older rival, Nordstr\"om's, used only one number made from them, their trace, and is ruled out because it does not deflect light. The series wants to derive Einstein's rule from its own field theory. This result shows what that requires. If gravity's field is only allowed to change in the ways that keep the derived metric a rescaling of the flat one, which are exactly the fields where the series' twistors can be attached, then it responds only to the trace, as in Nordstr\"om's theory, and light and other massless fields do not affect it at all, even though this restricted theory respects every change of coordinates. The full rule needs the field to be able to change in five further ways that leave those fields. (For waves moving at the speed of light the bookkeeping has a few more cases, but the conclusion is the same.) The light-ray form of Einstein's equations used elsewhere in the series sees exactly the part that the trace misses, and energy conservation then fills in the rest, up to a cosmological constant. So the missing step is not a symmetry; it is that the matter theory must work, and be varied, beyond the fields where the twistors attach.

## one-liner
At first order there are exactly four displacement-closed covariant classes of gravitational fields at each non-null momentum (more at null momentum); varying only within the Weyl-flat class, the twistor attachment's domain, couples gravity to the stress trace alone (Nordstr\"om) and decouples the Maxwell field, so gauge invariance does not give the whole-stress clause; the clause is the trace-free channel, exactly what the Clausius route's null fluxes see, and under an action principle it amounts to varying the field off the attachment's domain.
