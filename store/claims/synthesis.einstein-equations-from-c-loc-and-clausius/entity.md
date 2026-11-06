---
id: synthesis.einstein-equations-from-c-loc-and-clausius
kind: claim
version: 7
title: 'Under (C$_{\mathrm{loc}}$) and the Clausius relation, Jacobson''s argument gives Einstein''s equations with $\Lambda$ an integration constant and $G_{\mathrm{cl}} = 1/(4\eta)$; every further hypothesis named'
status: proved
region: synthesis
subject: einstein
tags: [curvature-and-field-equations, horizons, thermal-premises, null-directions, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-22-cloc
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
  - synthesis.imported-jacobson-clausius-1995@2
  - synthesis.einstein-condition-is-infinity-vacuum-incidence@3
  - synthesis.imported-raychaudhuri-null-congruence@2
  assumes:
  - synthesis.c-loc-local-horizon-premise@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_focusing_leading_order
- kind: check
  ref: check.py::check_equilibrium_hypotheses
- kind: check
  ref: check.py::check_unruh_to_killing_temperature
- kind: check
  ref: check.py::check_null_null_to_store_einstein
- kind: check
  ref: check.py::check_universality_at_bianchi
- kind: check
  ref: check.py::check_integrated_entropy_reading
- kind: check
  ref: check.py::check_dimension_enters_only_at_trace
- kind: check
  ref: check.py::check_newton_constant
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.clausius-route-newton-constant-is-residue
  - synthesis.black-hole-data-do-not-fix-field-equations
  - synthesis.boundary-mode-first-law-of-entanglement
extraction:
  maintainer_pass_2026_11_01:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 6 -> 7, at Leon''s decision of 2026-11-01 naming the whole-stress clause: a marked note records that the route assumes, through (H1) for every physical null k, that the whole stress map is the source (T(k,k) in every null direction fixes T up to a multiple of the metric), the clause any field-theory route to Einstein''s equations needs and which consistency alone does not supply (synthesis.twistor-flat-fields-give-nordstrom-not-einstein). Hypotheses, conclusions and checks unchanged; no edge added.'
  maintainer_pass_2026_10_31:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 5 -> 6, at Leon''s decision of 2026-10-31: a marked note records that the coupled system of item (4) and the matter equations is variational exactly when the heat tensor of (H1) is the Hilbert stress of the matter functional (heat tensor = Hilbert stress), citing the inversion of the Clausius route; the route does not impose that identification. Pin to the local-horizon premise moved to its version 5 (an added note). Hypotheses, conclusions and checks unchanged.'
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 4 -> 5. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 2 adds a note on the entropy reading: version 3 of the local-horizon premise reads (Loc) on the integrated reading S = int eta dA (Leon''s decision 6), where version 1 of this result took the differences reading. The content does not depend on the change: with (Loc) giving one universal constant eta, the integrated reading gives delta S = eta delta A, which is (H1) as stated, so items (1) to (5) hold unchanged, and item (6) already treats both readings; the proof''s closing sentence of step (6), "the store takes the differences reading", refers to version 2 of the premise. Proof and checks unchanged; pin to the premise moved to version 3. Version 1 -> 2. Check strengthened: lam0^3 defect coefficient kappa((t1 + e2 t0)/3 - e r1/6) and the shear''s lam0^4 shift -kappa e s2/12 pinned by hand; the integrated reading pins the differences defect through lam0^3 and counts its e1 = 0 control; samples moved to module level. Version 3 -> 4.'
  open_problem: op.derive-c-loc
  note: >-
    The conditional derivation asked for by the open problem, written out on store objects. The entropy
    clauses (Loc) and (R$_{\mathrm{loc}}$) of the local-horizon premise supply Jacobson's hypotheses (b)
    and (a); the modular-flow clause of version 1 is not used on this route. What Jacobson's argument assumes beyond
    the premise is stated as hypotheses (H1) to (H4): the Clausius relation with heat the boost energy of
    matter, no entropy other than the horizon's, and the differences reading delta S = eta delta A; the
    local geometry of the patch (the approximate boost field, a thin pencil about the generator through the
    point, balance at leading order in the patch size; vanishing expansion and shear at the point are the
    premise's own construction of the horizon, and the twist of null hypersurface generators vanishes); a
    C^1 conserved stress tensor on a C^3 metric; and dimension four, which enters only through the trace
    coefficient of the Bianchi step. Proved here, with exact checks: the focusing step at leading order (the
    gradients and the error of the approximate Killing field enter one order later, the shear two orders
    later), the cancellation of the boost-field normalisation, the conversion of the temperature a/2pi in
    proper time to kappa/2pi in Killing time, the coefficient 2 pi/eta = 8 pi G_cl, the sign convention of
    the store, and where the universality of eta is used: at the Bianchi step on the differences reading,
    and already at the focusing step (as a first-order Clausius defect) on the integrated reading
    S = int eta dA. The vacuum-incidence item is a proved identity that relabels the null Ricci component
    through the store's own-ray class; it adds no physical content. Imported: Jacobson's theorem (Fact),
    whose hypothesis (c) carries the Raychaudhuri focusing; the explicit Raychaudhuri and shear equations
    are cited from memory (Wald 1984, Sec. 9.2), the shear equation being the only step outside the Fact;
    a Fact for both is proposed to the maintainer. Used from the store: clause (7) of the Einstein-condition
    theorem for the polarisation lemma and the Bianchi step. The value of Lambda is not addressed. What
    selects Einstein's equations over their Ricci-polynomial extensions here is that the entropy density does
    not depend on curvature. The reading G_cl = G as the area-law condition is a remark that assumes one mode
    set placed at both the cutoff and the horizon; the Clausius-route theorem it cites is not a premise, so
    the result holds given (C_loc) alone. Transport-absent: Jacobson's argument in the store's variables.
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: U is a connected open part of the invertible region of a gravitational field on four-dimensional flat spacetime whose derived metric is C^3, null directions are physically null, the stress-energy is the symmetric map T(a) with T_ab chi^a k^b = chi.T(k), the null-null equation is also written -k.R(k) = (2 pi/eta) k.T(k), and Einstein''s equations are also written as the field equations R(a) + 8 pi G_cl T(a) = (Lambda + 4 pi G_cl tau) a of the store-sign curvature operator. Hypotheses (H1) to (H4), the conclusions and their strength unchanged; proof given a pointer to the dictionary Fact.'
---

## formal
Units $\hbar = c = 1$, signature $(1,3)$. Write $\Ric^{\circ}$ for the Ricci tensor of the convention in which the round sphere has positive Ricci curvature (the one in the Raychaudhuri equation); the store's $\Ric$ is $-\Ric^{\circ}$ (Theorem \claimref{synthesis.einstein-condition-is-infinity-vacuum-incidence}(7)). Let $(\hb, \Omega)$ be a gravitational field on four-dimensional flat spacetime whose derived metric $g$ is $C^{3}$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), let $U$ be a connected open part of its invertible region, and assume Premise \claimref{synthesis.c-loc-local-horizon-premise}, clauses (Loc) and (R$_{\mathrm{loc}}$): every local Rindler horizon $\mathcal{H}_{p,k}$ through $p \in U$ generated by a future physically null $k$ (the null boundary of the past of a small spacelike two-surface element through $p$, with vanishing expansion and shear at $p$) changes its entropy as $\delta S = \eta\,\delta A$ with $\eta$ one universal constant, and its selected state is at temperature $a/2\pi$ in the proper time of the boost observers of acceleration $a$. The Raychaudhuri equation for the generators enters through hypothesis (c) of Fact \claimref{synthesis.imported-jacobson-clausius-1995}; its explicit form and the shear equation are Fact \claimref{synthesis.imported-raychaudhuri-null-congruence}. Assume further the hypotheses of Jacobson's argument that the premise does not supply:
\begin{enumerate}
\item[(H1)] \emph{(Clausius.)} For every $p \in U$, every future null $k$ at $p$ and every small patch of $\mathcal{H}_{p,k}$ (generators with affine parameter $\lambda$, $\lambda = 0$ at $p$, $\lambda \in [\lambda_{0}, 0]$), the boost energy of matter crossing it, $\delta Q = \int T_{ab}\chi^{a}k^{b}\,d\lambda\,d\mathcal{A} = \int \chi \cdot T(k)\,d\lambda\,d\mathcal{A}$ with $\chi$ the approximate boost Killing field of surface gravity $\kappa$, equals $T_{\chi}\,\delta S$, with $T_{\chi}$ the temperature in the time of $\chi$ and $\delta S$ the change of the horizon's entropy alone, read as differences: $\delta S = \eta\,\delta A$, with $\eta$ the density at $p$.
\item[(H2)] \emph{(Patch.)} $\chi = -\kappa\lambda k$ on $\mathcal{H}_{p,k}$ up to $O(\lambda^{2})$; the balance (H1) is taken per unit cross-section area in the limit of a thin pencil about the generator through $p$ (the cross-section shrunk to zero before $\lambda_{0}$), and is required at leading order in $\lambda_{0}$. (The generators of a null hypersurface have zero twist.)
\item[(H3)] \emph{(Matter.)} $T$ is a given real symmetric linear map $a \mapsto T(a)$ on physical vectors, $C^{1}$ on $U$ (components $T_{ab}$; classical, or a renormalised expectation value), covariantly conserved, $\nabla^{a}T_{ab} = 0$ with $\nabla$ the covariant derivative $D$.
\item[(H4)] \emph{(Dimension.)} Spacetime is four-dimensional (the flat background is that of $\Cl(1,3)$).
\end{enumerate}
Then, with $G_{\mathrm{cl}} := 1/(4\eta)$:
\begin{enumerate}
\item \emph{(Temperature.)} Clause (ii) gives $T_{\chi} = \kappa/2\pi$: on the orbit of $\chi$ at proper distance $\rho$ from the edge, $a = 1/\rho$ and $|\chi| = \kappa\rho$, and $T_{\chi} = (a/2\pi)\,|\chi|$. Nothing below depends on $\kappa$.
\item \emph{(Focusing at leading order.)} $\theta(\lambda) = -\lambda\,\Ric^{\circ}(k,k)|_{p} + O(\lambda^{2})$, and per unit cross-section area at $p$
\[
\delta Q - T_{\chi}\,\eta\,\delta A \;=\; \frac{\kappa}{2}\Big(T(k,k) - \frac{\eta}{2\pi}\Ric^{\circ}(k,k)\Big)\Big|_{p}\,\lambda_{0}^{2} + O(\lambda_{0}^{3}),
\]
where the gradients of $\Ric^{\circ}(k,k)$ and $T(k,k)$ along the generator and the $O(\lambda^{2})$ error of $\chi$ enter at $O(\lambda_{0}^{3})$, and the shear and $\theta^{2}$ at $O(\lambda_{0}^{4})$. A shear $s_{0} = |\sigma|^{2}(p) \neq 0$ would replace $\Ric^{\circ}(k,k)$ by $\Ric^{\circ}(k,k) + s_{0}$, and an expansion $\theta_{0} \neq 0$ at $p$ gives a defect $\kappa\eta\theta_{0}\lambda_{0}/2\pi$ at first order, so (H1) forces $\theta_{0} = 0$. Hence (H1) gives $\Ric^{\circ}(k,k) = (2\pi/\eta)\,T(k,k)$, that is $-k \cdot \mathcal{R}(k) = (2\pi/\eta)\,k \cdot T(k)$, for every physical null $k$ at every $p \in U$.
\item \emph{(Restatement in the store's language.)} The leading defect equals $\kappa\,\tfrac{\eta}{2\pi}\big(4\pi G_{\mathrm{cl}}\,T(k,k) - \omega_{k}(I_{g},k)\big)\lambda_{0}^{2}$, with $\omega_{k}(I_{g},k) = -\Sch(k,k) = \tfrac12\Ric^{\circ}(k,k)$ the own-ray class of the infinity vacua through $k$ (Theorem \claimref{synthesis.einstein-condition-is-infinity-vacuum-incidence}(2)). This identity is a relabelling of $\Ric^{\circ}(k,k)$ and adds no content: the Clausius balance in the direction $k$ is the own-ray incidence condition of that theorem's clause (7).
\item \emph{(Einstein's equations.)} On $U$,
\[
\Ric + 8\pi G_{\mathrm{cl}}\,T = (\Lambda + 4\pi G_{\mathrm{cl}}\,\tau)\,g, \qquad \tau = g^{ab}T_{ab},
\]
with $\Lambda$ a constant, that is, for the gravitational field, $\mathcal{R}(a) + 8\pi G_{\mathrm{cl}}\,T(a) = (\Lambda + 4\pi G_{\mathrm{cl}}\,\tau)\,a$, or $\mathcal{G}(a) + \Lambda a = -8\pi G_{\mathrm{cl}}\,T(a)$, with the store's curvature operator; equivalently $\Ric^{\circ} - \tfrac12 R^{\circ}g - \Lambda g = 8\pi G_{\mathrm{cl}}\,T$ in signature $(1,3)$, which is $G_{ab} + \Lambda g_{ab} = 8\pi G_{\mathrm{cl}}T_{ab}$ in signature $(3,1)$. $\Lambda$ is an integration constant: (C$_{\mathrm{loc}}$) and (H1) to (H4) leave its value free.
\item \emph{(Newton's constant.)} $8\pi G_{\mathrm{cl}} = 2\pi/\eta$, so $G_{\mathrm{cl}} = 1/(4\eta)$, and in the mode-count reading of version 1 of the premise, $\eta = 4\pi\nu\langle s\rangle/G$, $G_{\mathrm{cl}} = G/(16\pi\nu\langle s\rangle)$, $G$ the constant that defines the Planck cell.
\item \emph{(Where the universality of $\eta$ is used.)} On the differences reading of (H1), if $\eta$ were a function on $U$, steps (1) to (3) would still give $\Ric + \gamma T = h\,g$ with $\gamma = 2\pi/\eta$, and the contracted Bianchi identity with $\nabla^{a}T_{ab} = 0$ would give $d(h - \tfrac12\gamma\tau) = -T(\nabla\gamma, \cdot)$: the cosmological term is constant only where $T(\nabla\eta, \cdot) = 0$, so universality is used at the Bianchi step. On the integrated reading $S = \int\eta\,dA$ instead, a varying $\eta$ already gives a first-order defect $(\kappa/2\pi)(k\cdot\nabla\eta)\lambda_{0}$ at step (2), and (H1) forces $\nabla\eta = 0$ there.
\end{enumerate}
\emph{Note (entropy reading).} Version 3 of Premise \claimref{synthesis.c-loc-local-horizon-premise} reads (Loc) on the integrated reading $S = \int\eta\,dA$, where this result was first stated with the differences reading. The conclusions do not depend on the change: with $\eta$ one universal constant the integrated reading gives $\delta S = \eta\,\delta A$, which is the entropy change (H1) uses, so items (1) to (5) hold as stated; item (6) treats both readings, and on the integrated reading the universality is used already at the focusing step. The remark in the proof that the store takes the differences reading refers to version 2 of the premise.

\emph{Note (heat tensor and Hilbert stress).} The source $T$ of item (4) is the heat tensor of (H1), the boost-energy flux of matter, whatever functional the matter has. If the matter equations are the Euler-Lagrange equations of a local functional $S_{m}$, the coupled system (item (4) with those equations) is the Euler-Lagrange system of one local functional exactly when $T$ is the Hilbert stress of $S_{m}$, up to a term independent of the matter (Theorem \claimref{synthesis.inverse-problem-for-the-clausius-route}(v)). The route does not impose this identification; it is the condition under which the route's equations have a variational form with matter.

\emph{Note (the whole-stress clause; added 1 November).} Item (2) uses (H1) for every physical null $k$ at every point, so the route takes the null-null component $T(k,k)$ of the whole stress map as the source in every null direction; since a symmetric map vanishing on every null vector is a multiple of the metric, these components fix $T$ up to such a multiple, and the Bianchi step of item (4) fixes the multiple up to the constant $\Lambda$. This is the clause that the whole stress map is the source, a clause of any field-theory route to Einstein's equations: consistency conditions alone do not supply it, since on twistor-flat fields Nordstr\"om's equations, sourced by the trace alone, satisfy the Bianchi identities, the conservation of the stress and the Newtonian limit (\claimref{synthesis.twistor-flat-fields-give-nordstrom-not-einstein}). The Clausius route assumes the clause through (H1); it does not derive it.

## technical
This writes out, inside the store, the conditional derivation of Einstein's equations from the local-horizon premise (C$_{\mathrm{loc}}$) and Jacobson's 1995 Clausius argument, and names every hypothesis the argument needs beyond the premise. The premise supplies two of Jacobson's inputs: an entropy density $\eta$ per unit area, one universal constant (clause (Loc)), and the temperature $a/2\pi$ of the boost observers (clause (R$_{\mathrm{loc}}$)), which in the time of a boost Killing field of surface gravity $\kappa$ is $\kappa/2\pi$. The modular-flow clause of version 1 is not used. The further hypotheses are: the Clausius relation, with heat the boost energy of matter crossing the horizon, no entropy other than the horizon's, and entropy changes read as $\eta\,\delta A$; the patch (the approximate boost field, balance per unit area in a thin pencil about one generator, at leading order in the patch length); a given $C^{1}$ conserved stress tensor on a gravitational field whose derived metric is $C^{3}$; and four dimensions. Vanishing expansion and shear at the point are the premise's own construction of the horizon. The Raychaudhuri focusing comes with Jacobson's Fact; the explicit Raychaudhuri and shear equations are imported as a Fact. Under these, the proof integrates the Raychaudhuri equation along a generator in exact power series: the area change and the heat both start at second order in the patch length, with coefficients $\Ric^{\circ}(k,k)/2$ and $\kappa T(k,k)/2$, while the gradients and the error of the Killing field enter one order later and the shear two orders later, so the Clausius relation at leading order is the pointwise null-null equation $\Ric^{\circ}(k,k) = (2\pi/\eta)T(k,k)$; the normalisation $\kappa$ cancels. A shear or an expansion at the point would spoil this. In the store's language, as a restatement, the Clausius defect is the gap between the matter's null energy and the own-ray class of the infinity vacua; this is a relabelling, not new content. The store's theorem on the Einstein condition (polarisation, valid in any dimension, then the contracted Bianchi identity, where four dimensions fix the coefficient $4\pi G\tau$) turns the null-null equation into Einstein's equations, the field equations $\mathcal{G}(a) + \Lambda a = -8\pi G_{\mathrm{cl}}\,T(a)$ of the gravitational field on flat spacetime, with $\Lambda$ an integration constant and $G_{\mathrm{cl}} = 1/(4\eta)$, that is $G/(16\pi\nu\langle s\rangle)$ in the mode-count reading. The universality of $\eta$ is used at the Bianchi step on the differences reading (a varying $\eta$ would make the cosmological term vary wherever matter flows along its gradient), and already at the focusing step on the integrated reading $S = \int\eta\,dA$. What selects Einstein's equations over their Ricci-polynomial extensions is the assumption that the density does not depend on curvature. $G_{\mathrm{cl}} = G$ holds at the area-law condition only if the horizon modes and the cutoff modes are one set. With matter, the field equations and the matter's own equations come from one action exactly when the heat tensor is the matter's Hilbert stress (the stress obtained by varying the matter action with respect to the metric); the route itself does not impose this. The derivation is Jacobson's, transport-absent; it is conditional on the premise and on the Clausius relation, and it says nothing about the value of $\Lambda$.

## lay
In 1995 Ted Jacobson showed that Einstein's equations of gravity follow if every small patch of horizon, as seen by an accelerating observer, has a temperature set by the acceleration and an entropy proportional to its area, and if heat crossing the patch raises its entropy by heat divided by temperature. The series assumes, as a premise, that its own horizon quantum modes give that temperature and that entropy on all such small horizons. This result writes the argument out step by step under that premise and checks each algebraic step exactly. It also lists everything else the argument needs: that the heat is the energy carried by matter and nothing else changes the entropy, that the horizon patch is momentarily neither expanding nor shearing, that matter is described by an ordinary conserved energy tensor, that the gravitational field is smooth enough, and that space-time has four dimensions. Given all that, Einstein's equations follow, with the strength of gravity fixed by the entropy per area and the cosmological constant left free. What singles out Einstein's equations, rather than more complicated versions of them, is that the entropy per area is the same everywhere and does not depend on the strength of the gravitational field there. The derivation is conditional: it shows what the premise would deliver, not that the premise holds.

## one-liner
Under the local-horizon premise (C$_{\mathrm{loc}}$) and Jacobson's further hypotheses, stated here (Clausius for the matter's boost energy with $\delta S = \eta\,\delta A$, a thin patch with vanishing expansion and shear at the point, a conserved $C^{1}$ $T_{ab}$ on a gravitational field with $C^{3}$ derived metric, four dimensions), $\Ric + 8\pi G_{\mathrm{cl}}\,T = (\Lambda + 4\pi G_{\mathrm{cl}}\,\tau)g$, that is $\mathcal{R}(a) + 8\pi G_{\mathrm{cl}}\,T(a) = (\Lambda + 4\pi G_{\mathrm{cl}}\,\tau)\,a$, holds with $\Lambda$ an integration constant and $G_{\mathrm{cl}} = 1/(4\eta)$, the focusing, normalisation, sign and coefficient steps checked exactly.
