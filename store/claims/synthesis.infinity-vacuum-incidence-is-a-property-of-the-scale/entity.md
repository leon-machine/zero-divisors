---
id: synthesis.infinity-vacuum-incidence-is-a-property-of-the-scale
kind: claim
version: 4
title: 'Infinity-vacuum incidence is a property of the scale'
status: proved
region: synthesis
subject: einstein
tags: [tractors, curvature-and-field-equations, spinor-modules, null-directions, no-go]
proposed_by:
  kind: ai
  session: 2026-10-23-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: GA rewrite (tractors as Cl(2,4) vectors and the Schouten map in place of index tensors)
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - synthesis.einstein-condition-is-infinity-vacuum-incidence@3
  - interior.imported-tractor-connection@2
  - correspondence.imported-vacuum-equations-scale-tractor@6
  - mass.imported-frozen-point-tractor-connection@6
  - one-relation.imported-pure-spinors-incidence-chart@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_ray_closure
- kind: check
  ref: check.py::check_conformal_blindness
- kind: check
  ref: check.py::check_frozen_point_decomposition
- kind: check
  ref: check.py::check_matter_sources_frozen_point
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.einstein-condition-is-infinity-vacuum-incidence
  - one-relation.spacetime-manifold-vacuum-lines
  - interior.covariant-form-vacuum-equations
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Tensors and forms to GA in the formal level and the proof: tractors are the Cl(2,4) vectors sigma ninf + mu + rho n0 with the tractor connection the gauge field Omega_T(a) = Omega(a) - ninf ^ hb^{-1}(a) + n0 ^ P(hb^{-1}(a)); X = n0, I_g = ninf, L = l (the physical null vector itself, in place of (0, l^flat, 0)); the Schouten tensor is the Schouten map (P(l, l) becomes l . P(l), the trace J = d_a . P(a)); the rescaled example is the dilation field hb^{-1}(b) = f^{1/2} b, whose Schouten map at the origin is P(v) = a (v . e^1) e^1; nabla I'' = -P(v) + (J/4) v + (v . hat-grad J)/4 n0 and, with matter, 4 pi G (T(v) - tau v/4 + (v . hat-grad tau)/12 n0); slot triples, Christoffel symbols and index tensors stay as labelled readings. Checked exactly with lib/GA.py in the maintainer scratch: Omega_T(a) x (sigma ninf + mu + rho n0) = -(A . mu) ninf + rho A - sigma P(A) + (P(A) . mu) n0 for random rational A, mu, P(A), sigma, rho, which is the slot formula of the imported tractor connection; the remaining steps are linear in it. Statement unchanged.'
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 2 -> 3. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: g is the derived metric of a gravitational field on flat spacetime, the tractor connection its Cl(2,4) gauge field, null geodesics worldlines of D-parallel null velocity; content unchanged. Checks untouched.'
  open_problem: ein.infinity-vacuum-incidence
  note: >-
    Answers the target's second alternative, and gives the known almost-Einstein result in the series' terms; it does not supply a reason that selects the scale. (2) is the
    counter-model: the data stated on the CAR side (the Fock module of the tractor fibre with its CAR,
    the tractor connection, the canonical tractor X and the point vacua) depend only on the conformal
    class, while the own-ray classes of the infinity vacua depend on the scale's second derivatives; the
    scales eta and (1 + a x1^2) eta agree at the origin in every such datum, in their infinity vacua there,
    and in the vacua themselves, and differ in the incidence. So no condition on those data alone can
    force it, and a CAR-side reason must be a principle selecting the scale. (3) restates the selection that
    works (the almost-Einstein characterisation, Bailey, Eastwood and Gover 1994, Gover; cited from memory): the infinity tractor is the null projection I' - (1/2) Q(I') X of I' = I_g + (J/4) X, the same
    formula as the point embedding, and the incidence is the vanishing of the middle slot of nabla I', that
    is (on a connected region) parallelism of I', the store's scale tractor of g (correspondence import), which is then the frozen point, with Lambda its integration constant.
    This is the almost-Einstein characterisation (the stored import), read through the vacua: the parallel
    part contributes no class and the X part contributes the point class, which vanishes on own rays. (1)
    upgrades the stored first-order classes to transport along a whole null geodesic (point vacua in every
    metric; infinity vacua exactly for Einstein metrics). (4) is the standard formula nabla_a I' = (0, -Sch_tf, (1/4) d J) with
    Einstein's equations substituted, nabla_a I' = 4 pi G (0, T_tf, (1/12) d tau): a rewriting of the field
    equations, which becomes a law only with a T given independently of the vacuum field (a source read
    linearly off the vacuum classes is a definition of T, by the proposal
    synthesis.vacuum-field-stress-tensor-is-einstein-tensor-or-trace, filed alongside). None of
    this supplies a quantum principle that selects the frozen-point scale; it locates the missing principle.
    The conformal-change behaviour of the Schouten tensor is recomputed from the metric at the origin, not
    imported. Transport-convenient. Related, not used: local twistor transport along null geodesics in
    curved space (Penrose; cited from memory).
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with derived metric $g$ of signature $(1,3)$. Tractors are the vectors $\sigma\nInf + \mu + \rho\nO$ of $\Cl(2,4)$, $\mu$ a physical vector and $\ip{\nO}{\nInf} = 1$ (in the splitting of $g$, the components $(\sigma, \mu_{b}, \rho)$), and the connection of Fact \claimref{interior.imported-tractor-connection} is, on flat spacetime, the $\Cl(2,4)$ gauge field $\Omega_{T}(a) = \Omega(a) - \nInf\wedge\hb^{-1}(a) + \nO\wedge\Sch(\hb^{-1}(a))$ of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, with $\Sch$ the Schouten map; write $\nabla_{v}$ for its covariant derivative $a\cdot\nabla + \Omega_{T}(a)\times$ along a physical vector $v = \hb^{-1}(a)$. $X = \nO$ and $I_{g} = \nInf$ (components $(0,0,1)$ and $(1,0,0)$), infinity vacua (Fock vacua $u$ with $c(I_{g})u = 0$) and point vacua ($c(X)u = 0$) are as in Theorem \claimref{synthesis.einstein-condition-is-infinity-vacuum-incidence}. For a physical null vector $\ell$ put $L = \ell$, a null tractor orthogonal to $X$ and $I_{g}$ (components $(0, \ell^{\flat}, 0)$), and put $I' := I_{g} + \tfrac{J}{4}X$, $J = \partial_a\cdot\Sch(a)$ the trace of the Schouten map, $\Sch^{\circ}(a) = \Sch(a) - \tfrac{J}{4}a$.
\begin{enumerate}
\item \emph{(Ray closure.)} Along an affinely parametrised null geodesic $\gamma$ with tangent $\ell$ (a worldline whose physical null velocity is $D$-parallel, Fact \claimref{synthesis.imported-gtg-dictionary}(iii)), $\nabla_{\ell}X = L$ and $\nabla_{\ell}L = (\ell\cdot\Sch(\ell))\,X$, so $\mathrm{span}(X, L)$ is parallel along $\gamma$ in every metric: a point vacuum $u$ at $\gamma(0)$ with real null direction $\ell$ ($c(X)u = c(L)u = 0$), carried along $\gamma$ by the tractor transport of the Fock module, is for every parameter value a point vacuum of $\gamma(t)$ with real null direction $\gamma'(t)$. If $g$ is Einstein, $\nabla_{\ell}I_{g} = -\tfrac{\Lambda}{6}L$ and $\nabla_{\ell}L = 0$, so infinity vacua carried along their own null geodesics remain infinity vacua with real direction $\gamma'(t)$ for every parameter value. Conversely, if every infinity vacuum at $x$ remains one to first order along its own ray, $g$ is Einstein at $x$.
\item \emph{(Blindness of the conformal CAR data.)} The Fock module of each tractor fibre with its CAR, the tractor connection, $X$ and the point vacua depend only on the conformal class $[g]$; the field of infinity vacua depends on the scale. Explicitly, compare the field $\hb = 1$ (derived metric $\eta$) with the dilation field $\hb^{-1}(b) = f^{1/2}\,b$, whose derived metric is $\hat g = f\,\eta$, with $f = 1 + a x_{1}^{2}$, $a \neq 0$. At the origin $\nabla f = 0$, so the two splittings agree there: the same $X$, the same $I_{g}$, the same infinity and point vacua. In the store's convention the Schouten map of $\hat g$ at the origin is $\Sch_{\hat g}(v) = a\,(v\cdot e^{1})\,e^{1}$ (in components $\Sch_{\hat g} = a\,dx^{1}\otimes dx^{1}$), with nonzero trace-free part, and for $\ell = e_{0} + e_{1}$ the infinity vacuum of $\mathrm{span}(I_{g}, L, m)$ is unexcited along $\ell$ as an infinity vacuum of $\eta$ and excited ($\omega_{\ell}(I_{\hat g}, \ell) = -a$) as one of $\hat g$. Hence no condition stated on the conformally invariant CAR data alone implies the own-ray incidence of the infinity vacua: it is a condition on the choice of scale. The pure dilation fields $\hb = \sigma$ that are Einstein (derived metrics $\sigma^{-2}\eta$; Hessian of $f$ at the origin proportional to $\eta$) pass it.
\item \emph{(Restatement: the almost-Einstein characterisation.)} $\ip{I'}{X} = 1$, $Q(I') = J/2$ and $I_{g} = I' - \tfrac12 Q(I')\,X$, the null projection with the slot coefficient $-\tfrac12$ of the point embedding of Fact \claimref{one-relation.imported-pure-spinors-incidence-chart}. For every null $\ell$, $\omega_{\ell}(I_{g}, \ell) = \ip{\nabla_{\ell}I'}{L}$, and the middle slot of $\nabla_{v}I'$ is $-\Sch^{\circ}(v)$. So every infinity vacuum at $x$ is unexcited along its own ray if and only if the middle slot of $\nabla I'$ vanishes at $x$, and on a connected region if and only if $I'$, the scale tractor of $g$ in the sense of Fact \claimref{correspondence.imported-vacuum-equations-scale-tractor}, is parallel; it is then the frozen point of Fact \claimref{mass.imported-frozen-point-tractor-connection}, with $\Lambda = 6\rho_{I'} = \tfrac32 J$ constant (Fact \claimref{correspondence.imported-vacuum-equations-scale-tractor}). This is the almost-Einstein characterisation of conformal geometry read through the vacua. In these terms the infinity vacua obey the point vacua's incidence when the infinity tractor differs from a parallel tractor by a multiple of $X$: the parallel part contributes no class and the $X$ part only the point class, which vanishes along own rays.
\item \emph{(Matter: the standard formula with Einstein's equations substituted.)} Always $\nabla_{v}I' = -\Sch^{\circ}(v) + \tfrac14\,(v\cdot\hat\nabla J)\,\nO$, with $\hat\nabla J = \hb^{T}(\nabla J)$ the physical gradient (in components $\nabla_{a}I' = (0, -\Sch^{\circ}_{ab}, \tfrac14\nabla_{a}J)$). If $\mathcal{R}(a) + 8\pi G\,T(a) = (\Lambda + 4\pi G\,\tau)\,a$ with $\tau = \partial_a\cdot T(a)$ (clause (7) of Theorem \claimref{synthesis.einstein-condition-is-infinity-vacuum-incidence}; in components $\Ric + 8\pi G\,T = (\Lambda + 4\pi G\,\tau)\,g$), then
\[
\nabla_{v}I' = 4\pi G\,\big(T^{\circ}(v) + \tfrac{1}{12}\,(v\cdot\hat\nabla\tau)\,\nO\big), \qquad \Lambda = 6\rho_{I'} - 2\pi G\,\tau,
\]
with $T^{\circ}(a) = T(a) - \tfrac{\tau}{4}a$ the trace-free part of $T$; conversely the middle-slot equation at every point is that clause's pointwise condition. The own-ray class of the infinity vacua is $\ip{\nabla_{\ell}I'}{L} = 4\pi G\,\ell\cdot T(\ell)$: with matter the scale tractor, which is the frozen point in vacuum, is not parallel, and its derivative is read along null rays by the infinity vacua. Read from left to right this is a rewriting of the field equations, a definition of $T^{\circ}$ by $-\Sch^{\circ}/4\pi G$; it is a law only for a $T$ given independently of the vacuum field.
\end{enumerate}

## technical
The stored theorem reads Einstein's condition as the infinity vacua, the Fock vacua annihilated by the pure-scale tractor, being unexcited along their own null rays, which point vacua are in every metric. The open question was why infinity should obey what every point obeys. Three results answer it as far as the store's objects allow. First, transport: along a null geodesic, the span of the canonical tractor and the ray's tractor is parallel in every metric, so a point vacuum carried along its own ray stays a point vacuum to all orders; the pure-scale tractor and the ray's tractor span a parallel plane exactly when the metric is Einstein, so then infinity vacua do the same. Second, blindness, an elementary observation (the Einstein condition is not conformally invariant): everything the store places on the CAR side (the Fock module with its anticommutation relations, the tractor connection, the canonical tractor and the point vacua) depends only on the conformal class, while the infinity vacua's classes depend on the second derivatives of the scale. The flat metric and its rescaling by $1 + a x_{1}^{2}$ agree at the origin in all of those data and in the infinity vacua themselves, yet one is Einstein there and the other is not. No condition on the conformal CAR data can force the incidence; a reason must select the scale. Third, the selection that works, which is the known almost-Einstein characterisation restated: the pure-scale tractor is the null projection, along the canonical tractor, of $I' = I_{g} + (J/4)X$, by the same formula that embeds points as null vectors, and the infinity vacua's own-ray classes are those of $I'$. They vanish exactly when $I'$ is parallel, that is when the scale is the scale of a frozen point, and then the cosmological constant is the frozen point's integration constant. With matter, the standard formula for the scale tractor's derivative with Einstein's equations substituted says that the scale tractor's covariant derivative is $4\pi G$ times the trace-free stress tensor, with the trace's gradient in the last slot; this rewrites the field equations and is a law only for a stress tensor given independently of the vacuum field. The parts (3) and (4) are the almost-Einstein characterisation of conformal geometry read through the vacua; (1) and (2) are new in the store, (2) being elementary. The missing piece is now precise: a principle, quantum or otherwise, that selects the frozen-point scale.

## lay
In the series, each point of spacetime carries a family of quantum vacuum states, and so does the "point at infinity" that a choice of length scale singles out. Einstein's equations are equivalent to the statement that the vacua at infinity are never disturbed when moved along their own light rays, which the vacua of ordinary points never are, in any spacetime. This result shows first that the property holds along whole light rays, not only at the start. It then shows that the question "why does infinity behave like a point?" cannot be answered from the quantum side alone: two spacetimes that look identical to every quantum structure the series attaches to points can differ in exactly this property, because it depends on the choice of length scale, which the quantum side does not see. What does answer it, by a known result of conformal geometry restated here, is a fixed object of the series, the frozen point: infinity behaves like a point exactly when it is a frozen, unchanging object plus a piece of an ordinary point. With matter present, the object that is the frozen point in empty space is no longer unchanging, and how it changes is the matter's energy and stress; this rewrites Einstein's equations rather than explaining them.

## one-liner
Point vacua stay point vacua along their own light rays in every metric and infinity vacua do exactly in Einstein metrics; the CAR data the store states depend only on the conformal class and cannot see the difference ($\eta$ and $(1 + a x_{1}^{2})\eta$ agree in all of them at the origin), so the incidence is a condition on the scale: by the almost-Einstein characterisation it holds exactly when the scale tractor $I' = I_{g} + \tfrac{J}{4}X$, of which $I_{g}$ is the null projection, is parallel (the frozen point), and with matter the scale tractor's derivative is $\nabla_{a}I' = 4\pi G\,(0, T^{\circ}_{ab}, \tfrac{1}{12}\nabla_{a}\tau)$, a rewriting of the field equations.
