---
id: synthesis.twistor-flat-fields-give-nordstrom-not-einstein
kind: claim
version: 2
title: 'Twistor-flat fields give Nordstrom, not Einstein'
status: proved
region: synthesis
subject: einstein
tags: [conformal-spinors, tractors, curvature-and-field-equations, no-go, forcing-and-uniqueness]
proposed_by:
  kind: ai
  session: 2026-11-01-qft
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
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection@1
  - correspondence.imported-tractor-connection-local-twistor-transport@8
  - correspondence.imported-weyls-theorem@2
  - synthesis.imported-gtg-dictionary@2
  - synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians@1
  - synthesis.imported-nordstrom-scalar-theory-einstein-fokker-form@1
  - field-theory.twistor-attachment@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_attachment_domain_is_tractor_flat
- kind: check
  ref: check.py::check_curl_identity_forces_uniform_rest_density
- kind: check
  ref: check.py::check_nordstrom_trace_equation_solvable_for_any_trace
- kind: check
  ref: check.py::check_einstein_vacuum_on_attachment_domain_is_constant_curvature
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - field-theory.twistor-attachment
  - synthesis.einstein-equations-from-c-loc-and-clausius
  - field-theory.operator-newtonian-coupling
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review: synthesis.imported-gtg-dictionary repinned 1 -> 2 after reviewing its correction of the component reading in clause (iv) to R(g_mu ^ g_nu) = -R(e_mu ^ e_nu), agreeing with the store''s sign R(B) = -R(hb(B)) the clause already stated, with GA wording in (ii) and (iv); the translation rules are unchanged; the use here holds as cited.'
  open_problem: op.einstein-from-the-field-theory
  note: >-
    Adversarial result on the open problem's second attack (consistency of the coupled system: Bianchi
    identities and the conservation of the stress as conditions) and on the domain question of
    op.qft-on-gtg-fields. The twistor attachment uses one conformal spinor space; local twistor transport
    carries it unchanged from point to point exactly where the tractor field strength vanishes, which is
    exactly where the Weyl curvature vanishes (clause (i), from the stored splitting of the tractor field
    strength into the Weyl, torsion and Cotton blocks). On that class Einstein's equations force the
    covariant curl of T - tau g/3 to vanish (the Cotton block), which for a conserved perfect fluid forces
    uniform density on each rest space: an isolated star, a static dust cloud of varying density and every
    nonflat vacuum field at Lambda = 0 (Schwarzschild, gravitational waves) lie outside the class. On the
    same class Nordstrom's pair (vanishing Weyl curvature, scalar curvature proportional to the trace) is
    one semilinear wave equation for one function, formally solvable for every trace, so the coupled
    system is consistent with no condition beyond the matter's own conservation, and its static weak field
    is the Newtonian one, the only part of gravity the stored operator Newtonian coupling uses. The trace
    of Einstein's equations on the class is a Nordstrom-type equation of the opposite sign (repulsive, one
    third of Newton's strength). Reading: consistency does not select Einstein's equations; what does,
    with Lovelock's theorem, is the hypothesis that a divergence-free natural map of the field is equated
    to the whole stress map, and a field theory attached only on twistor-flat fields cannot carry the
    sources that Einstein's equations have. Clause (i) overlaps the result on parallel conformal spinors
    synthesis.attachment-transport-is-flat-only-where-weyl-vanishes, which classifies the
    points with nonzero Weyl curvature by Petrov type; here only the flat case is used, as a lemma for
    (ii); that result classifies the rest by Petrov type and cites the converse proved in (i) here. The
    induced-gravity result synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations, is computed on a
    twistor-flat field, where Weyl-square terms vanish. Cross-reading with
    synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise: on shell D^T I =
    4 pi G (T - tau g/3), and on a twistor-flat field the tractor curl of D^T I is F_T x I = 0, the same
    curl condition. Transport-essential for clause (i) (the domain is fixed by tractor transport);
    transport-convenient for (ii) (the Cotton condition read as a block of the tractor field strength);
    transport-absent for (iii), which is Nordstrom's 1913 theory in the Einstein-Fokker form re-derived in
    the store's conventions (standard; the new content is its placement as the theory of the attachment's
    domain). Nordstrom's theory in the Einstein-Fokker form and its observational failures (no light
    deflection, perihelion shift of minus one sixth of Einstein's) are the imported Fact
    synthesis.imported-nordstrom-scalar-theory-einstein-fokker-form. Literature cited from memory:
    Cauchy-Kovalevskaya and local
    existence for semilinear wave equations, the conformal-change formula for the scalar curvature
    (checked exactly here), Stephani's classification of conformally flat perfect fluids (consistent with
    clause (ii)(a)).
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2, at Leon''s decisions of 2026-11-01 (Nordstrom''s theory imported as a Fact with its observational failures): a uses edge to synthesis.imported-nordstrom-scalar-theory-einstein-fokker-form@1 replaces the two citations from memory in the proof of (iii) and (iv); the clause that the whole stress map is the source is recorded on op.einstein-from-the-field-theory and in a marked note on synthesis.einstein-equations-from-c-loc-and-clausius. Statement, proof and checks otherwise unchanged.'
---

## formal
Let $(\hb, \Omega)$ be a torsion-free gravitational field on four-dimensional flat spacetime, signature $(+,-,-,-)$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with store curvature $\mathcal{R}$, Schouten map $\Sch$ and Weyl curvature $\mathcal{W}(A \wedge B) = \mathcal{R}(A \wedge B) - \Sch(A) \wedge B - A \wedge \Sch(B)$ (Fact \claimref{synthesis.imported-gtg-dictionary}), and let $F_{T}$ be the field strength of its tractor gauge field $\Omega_{T}(a) = \Omega(a) - \nInf \wedge \hb^{-1}(a) + \nO \wedge \Sch(\hb^{-1}(a))$ (Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}). Call the field \emph{twistor-flat} on an open region if $F_{T} = 0$ there; by Fact \claimref{correspondence.imported-tractor-connection-local-twistor-transport} this is the condition that local twistor transport, the tractor connection acting on the conformal spinor space $\CS$, is path independent on simply connected subregions, so that the one space $\CS$ of the twistor attachment (Proposition \claimref{field-theory.twistor-attachment}) is carried unchanged to every point.
\begin{enumerate}
\item[(i)] The field is twistor-flat on a region if and only if $\mathcal{W} = 0$ there, if and only if (Fact \claimref{correspondence.imported-weyls-theorem}) about each point there is a gauge with $\hb^{-1}(a) = \phi\,a$, $\phi > 0$; then the scalar curvature is $\mathcal{R} = 6\,\Box\phi/\phi^{3}$ with $\Box = \partial_{t}^{2} - \partial_{x}^{2} - \partial_{y}^{2} - \partial_{z}^{2}$.
\item[(ii)] On a twistor-flat field suppose Einstein's equations $\mathcal{G}(a) + \Lambda a = -8\pi G\,T(a)$ hold with a symmetric stress map $T$ of trace $\tau$. Then $S(a) = T(a) - \tfrac{\tau}{3}a$ has vanishing covariant curl, $(D_{A}S)(B) = (D_{B}S)(A)$ for all vectors $A$, $B$. Hence (a) if $T(a) = (\rho + p)(a \cdot u)u - p\,a$ is a conserved perfect fluid ($Q(u) = 1$), then $\nabla\rho = u\,(u \cdot \nabla\rho)$: the density is constant on each rest space of the fluid, for every pressure and every $\Lambda$; (b) if $T = 0$ then $\mathcal{R}(B) = \tfrac{\Lambda}{3}B$, constant curvature. So no static perfect-fluid body whose density varies in space, and no vacuum field of nonzero field strength at $\Lambda = 0$ (the Schwarzschild field, gravitational waves), is twistor-flat under Einstein's equations.
\item[(iii)] On the same class Nordstr\"om's pair, $\mathcal{W} = 0$ and $\mathcal{R} = -24\pi G\,\tau$, is the single equation $\Box\phi = -4\pi G\,\tau\,\phi^{3}$ for one function. For every trace $\tau$ and Cauchy data $\phi$, $\partial_{t}\phi$ on $t = t_{0}$ its Taylor coefficients are determined order by order with no condition on $\tau$, and the Bianchi identities of the gravitational side hold identically, so the coupled system with matter conserved by its own equations is consistent with no condition beyond that conservation. Its static weak field obeys $\nabla^{2}(\phi - 1) = 4\pi G\rho$, the Newtonian field; the trace of Einstein's equations on the class, $\mathcal{R} = 8\pi G\tau + 4\Lambda$, gives at $\Lambda = 0$ instead $\nabla^{2}(\phi - 1) = -\tfrac{4\pi}{3}G\rho$, repulsive at one third of Newton's strength.
\item[(iv)] Hence the consistency conditions of a coupled system of matter and a twistor-flat gravitational field (Bianchi identities, conservation of the stress, gauge covariance, second order, the Newtonian static limit) are met by Nordstr\"om's equations, which are not Einstein's; by Fact \claimref{synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians}(a), Einstein's equations with free $G$ and $\Lambda$ follow only once a divergence-free natural map of the field of second order is equated to the whole stress map, that is, under the clause that the whole stress map is the source, which these conditions do not supply. The classification of the points with $\mathcal{W} \neq 0$ by Petrov type, with the subspaces of $\CS$ that stay parallel there, is the result \claimref{synthesis.attachment-transport-is-flat-only-where-weyl-vanishes}.
\end{enumerate}

## technical
Work with a torsion-free gravitational field $(\hb, \Omega)$ on four-dimensional flat spacetime and its tractor gauge field $\Omega_{T}$, the $\Cl(2,4)$ connection whose action on conformal spinors is local twistor transport. Call the field twistor-flat where the field strength $F_{T}$ of $\Omega_{T}$ vanishes: there the one conformal spinor space $\CS$ used by the twistor attachment is carried unchanged from point to point.

(i) A field is twistor-flat exactly where its Weyl curvature vanishes, that is, locally $\hb^{-1}(a) = \phi\,a$, and then $\mathcal{R} = 6\,\Box\phi/\phi^{3}$.

(ii) If such a field satisfies Einstein's equations with stress $T$, the Cotton block of $F_{T}$ forces $T - \tfrac{\tau}{3}g$ to have vanishing covariant curl. For a conserved perfect fluid this means the density is constant on each rest space; in vacuum the field has constant curvature. Isolated perfect-fluid bodies, inhomogeneous static perfect fluids, the Schwarzschild field and gravitational waves are all outside the class.

(iii) Nordstr\"om's equations, $\mathcal{W} = 0$ and $\mathcal{R} = -24\pi G\tau$, reduce on the class to $\Box\phi = -4\pi G\tau\phi^{3}$, which can be solved order by order for every trace, so they impose nothing on the matter beyond its own conservation; their static weak field is Newton's. The trace of Einstein's equations on the class has the opposite sign and gives a repulsive field of one third of Newton's strength. Nordstr\"om's theory is excluded by observation (no light deflection, a perihelion shift of minus one sixth of Einstein's); it serves as a consistent counter-model.

(iv) So the consistency conditions of the coupled system on twistor-flat fields (Bianchi identities, conservation, second order, Newtonian limit) hold for Nordstr\"om's equations, which are not Einstein's; with Lovelock's theorem, Einstein's equations follow only under the clause that the whole stress map, not its trace, is the source.

## lay
The series attaches its quantum particles to spacetime through twistors, a space that is the same at every point only where the gravitational field has no tidal part of a particular kind (the Weyl curvature, the part that bends light around a star and travels as gravitational waves). Such fields are rescalings of flat spacetime. If Einstein's equations hold on them, the matter they contain must be spread evenly in its own rest frame: a star or a lumpy dust cloud cannot sit in such a field, and empty space can curve only uniformly, so the space outside a body is not of this kind. On the same fields an older theory of gravity, Nordstr\"om's, in which only the trace of the matter's stress-energy sources gravity, works for any matter at all, satisfies every consistency requirement, and reproduces Newton's law. It is ruled out by observation (it bends no light, and it gives the wrong advance of Mercury's perihelion, minus one sixth of Einstein's), so it is a counterexample to the logic, not a viable theory. So requiring the coupled system of matter and gravity to be consistent on the fields where the twistors attach does not single out Einstein's equations; something more is needed: the rule that the whole stress-energy, not only its trace, is the source, or an attachment of the particles that works where the Weyl curvature is nonzero.

## one-liner
Twistor transport is path independent exactly where the Weyl curvature vanishes; there Einstein's equations allow only perfect fluids of uniform rest density and constant-curvature vacuum, while Nordstr\"om's trace equation is solvable for any matter, so consistency on these fields does not give Einstein's equations without the clause that the whole stress map is the source.
