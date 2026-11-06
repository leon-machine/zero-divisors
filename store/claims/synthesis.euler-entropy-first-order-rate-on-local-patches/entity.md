---
id: synthesis.euler-entropy-first-order-rate-on-local-patches
kind: claim
version: 2
title: 'The Euler entropy''s first-order rate on local patches'
status: proved
region: synthesis
subject: einstein
tags: [horizons, entropy-premises, curvature-and-field-equations, no-go, thermal-premises, needs-continuum]
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
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.euler-term-horizon-entropy-shift@4
  - synthesis.imported-wald-noether-charge-entropy@3
  - synthesis.imported-raychaudhuri-null-congruence@2
  - synthesis.einstein-equations-from-c-loc-and-clausius@7
  - synthesis.imported-jacobson-clausius-1995@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_first_order_rate_formula
- kind: check
  ref: check.py::check_ppwave_cases
- kind: check
  ref: check.py::check_flat_element_vacuum
- kind: check
  ref: check.py::check_null_data_force_constant_curvature
- kind: check
  ref: check.py::check_first_order_defect
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.euler-term-horizon-entropy-shift
  - synthesis.c-loc-entropy-clause-curvature-independent-density
  - synthesis.c-loc-local-horizon-premise
extraction:
  open_problem: op.derive-loc-and-r-loc
  note: >-
    On clause (Loc) of the local-horizon premise and the open-patch question of
    op.horizon-entropy-functional. The series' Lagrangian is (R - 2 Lambda + alpha E_4)/16 pi G with
    alpha = -3/(4 Lambda); its Wald entropy on bifurcation surfaces is the Jacobson-Myers functional
    (1/4G) int (1 + 2 alpha R_Sigma) dA. What is proved: on an element through p whose null normal k has
    vanishing expansion and shear at p, the first derivative along the generators of sqrt(h) R_Sigma is
    theta_l Ric(k,k) - 2 sigma_l:C(.,k,.,k) + 4 omega.Z + (nabla_k R)(e_a,e_b,e^a,e^b), and that of the
    projected (Noether-charge) form h^ac h^bd R_abcd is 4 omega.Z + (nabla_k R)(e_a,e_b,e^a,e^b), with
    theta_l, sigma_l the l-expansion and shear of the element, omega its normal connection and
    Z_b = h^ac R(e_a,k,e_c,e_b). The Euler part of the entropy therefore changes at first order in the
    affine extent lambda_0, one order before the heat and the area change; the Clausius relation on every
    element forces the rate to vanish; theta_l, sigma_l and omega are free data of the element; so with
    alpha nonzero the Clausius relation holds at p only if Ric(k,k) = 0 and C(.,k,.,k) = 0 for every null k,
    that is trace-free Ricci and Weyl both zero at p. Even on flat elements both forms leave the gradient
    term, nonzero in vacuum (an exact vacuum pp-wave; on radial generators of Schwarzschild-de Sitter the
    value is the one computed in the result filed alongside, not recomputed here).
    Consequence: within the family of entropy functionals the series' action supplies (area plus Euler
    term, in either form), the Clausius relation forces the pure area density, which is the
    curvature-independence of (Loc); with the stored result that a density varying over spacetime is
    excluded at first order, this derives (Loc) from the Clausius relation for every density of the form
    eta(x) + beta times the cut's intrinsic or projected curvature. It does not derive (Loc) for arbitrary
    curvature-dependent densities, and it concerns entropies that are functionals of the cut: on the
    differences reading the premise adopts, a curvature-dependent eta is not excluded by (H1) (filed
    alongside, synthesis.loc-independent-of-clausius-and-killing-data). Filed alongside on the same question from the vacuum side,
    synthesis.series-wald-entropy-changes-without-flux-on-local-horizons (Schwarzschild-de Sitter radial
    generators); this result is the general rate formula and its consequence. Transport-absent: classical
    null geometry (Gauss, Raychaudhuri and shear equations); the series enters only through the Euler
    coefficient of its action. Literature cited from memory in the proof: the Gauss equation for a
    codimension-two spacelike surface, the first variation of the two-dimensional Einstein-Hilbert
    density, Schur's lemma, and Guedens-Jacobson-Sarkar 2012 (not used).
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: p is a point of the invertible region of a gravitational field on four-dimensional flat spacetime with C^3 derived metric, k and l are physical null vectors, g is the flat product of physical vectors, the second fundamental forms and normal connection are built from the covariant derivative D, the Riemann and Weyl tensors are read from the field strength and its Weyl map, constant curvature is R(B) = cB, and the plane wave is a vacuum field given by its derived metric. Signature (-,+,+,+) kept as declared; the rate formulas stay in components. Statements (i) to (iii), their readings and strength unchanged; proof given a pointer to the dictionary Fact.'
---

## formal
Signature $(-,+,+,+)$ in this statement and its proof, units $\hbar = c = 1$; the store's $(+,-,-,-)$ changes the signs of inner products and of $\Ric$ but not of $\Ric^{\circ}$, the Ricci tensor of the convention in which the round sphere has positive Ricci curvature. Let $(\hb, \Omega)$ be a gravitational field on four-dimensional flat spacetime whose derived metric $g$ is $C^{3}$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), $p$ a point of its invertible region, $k$ a future null physical vector at $p$ ($g$ on physical vectors is the flat product), and $\Sigma$ a small spacelike two-surface element through $p$ orthogonal to $k$, with null normals $k$, $l$ normalised by $g(k,l) = -1$ and extended along the generators of the null hypersurface $\mathcal{H}$ that $\Sigma$ emits in the direction $k$, affinely parametrised by $\lambda$ with $\Sigma$ at $\lambda = 0$; let $\Sigma_{\lambda}$ be the cuts at constant $\lambda$, $h$ their induced metric, $e_{a}$ a frame of $T\Sigma$ dragged along the generators, $B^{(k)}_{ab} = g(\nabla_{e_{a}}k, e_{b})$ and $B^{(l)}_{ab} = g(\nabla_{e_{a}}l, e_{b})$, with $\nabla_{e_{a}} = e_{a} \cdot D$ the covariant derivative, the two null second fundamental forms, $\theta_{k}, \theta_{l}$ their traces and $\sigma_{k}, \sigma_{l}$ their trace-free parts, $\omega_{a} = -g(l, \nabla_{e_{a}}k)$ the normal connection, $C$ the Weyl tensor, $\widehat{C}_{k}(e_{a}, e_{b}) = C(e_{a}, k, e_{b}, k)$, and $Z_{b} = h^{ac}R(e_{a}, k, e_{c}, e_{b})$, the Riemann and Weyl tensors being read from the field strength $\mathcal{R}$ and its Weyl map $\mathcal{W}$ in the convention of the proof (Riemann positive on spheres). Call $\Sigma$ \emph{admissible} if $B^{(k)} = 0$ at $p$ ($\theta_{k} = \sigma_{k} = 0$ there), the condition defining the local Rindler patches of Fact \claimref{synthesis.imported-jacobson-clausius-1995} and hypothesis (H1) of Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius}. Write ${}^{(2)}\!R$ for the scalar curvature of $h$ and $P = h^{ac}h^{bd}R_{abcd}$ for the projected curvature. Then, on an admissible element:
\begin{enumerate}
\item[(i)] \emph{(Rates.)} At $p$,
\[
\frac{d}{d\lambda}\Big(\sqrt{h}\,{}^{(2)}\!R\Big)\Big|_{0} = \theta_{l}\,\Ric^{\circ}(k,k) - 2\,\sigma_{l}^{ab}\widehat{C}_{k\,ab} + 4\,\omega^{b}Z_{b} + (\nabla_{k}R)(e_{a},e_{b},e^{a},e^{b}),
\qquad
\frac{d}{d\lambda}\Big(\sqrt{h}\,P\Big)\Big|_{0} = 4\,\omega^{b}Z_{b} + (\nabla_{k}R)(e_{a},e_{b},e^{a},e^{b}),
\]
per unit area, where the last term equals $2\,(\nabla_{e^{b}}R)(e_{a},k,e^{a},e_{b})$ by the second Bianchi identity; the difference of the two rates is the derivative of the extrinsic term of the Gauss equation. Data of the element beyond its second fundamental forms and normal connection at $p$ do not enter. Given $p$ and $k$, every symmetric $B^{(l)}(p)$ and every covector $\omega(p)$ is realised by some admissible element.
\item[(ii)] \emph{(The Clausius relation at first order.)} Take as the entropy of a patch the Jacobson-Myers functional $S = \frac{1}{4G}\int(1 + 2\alpha\,{}^{(2)}\!R)\,dA$ of the series' Lagrangian $(R - 2\Lambda + \alpha E_{4})/16\pi G$, $\alpha = -3/(4\Lambda)$ (Theorem \claimref{synthesis.euler-term-horizon-entropy-shift}, Fact \claimref{synthesis.imported-wald-noether-charge-entropy}(c)), or its projected form with $P$ in place of ${}^{(2)}\!R$, and take the Clausius relation (H1) of Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius} on every open admissible element, with $\delta S$ the change of this functional (entropy read as a functional of the cut), in the thin-pencil limit (H2). Per unit cross-section area the defect $\delta Q - T_{\chi}\,\delta S$ is $(\kappa/2\pi)(\alpha/2G)\,r\,\lambda_{0} + O(\lambda_{0}^{2})$, with $r$ the rate of (i), while the heat and the area change start at $\lambda_{0}^{2}$. So (H1) on every admissible element through $p$ requires $r = 0$ for all of them. For the Jacobson-Myers form this requires $\Ric^{\circ}(k,k) = 0$ and $\widehat{C}_{k} = 0$ for every null $k$ at $p$, that is the trace-free Ricci tensor and the Weyl tensor vanish at $p$ (then $Z = 0$ at $p$), and the gradient term to vanish; at every point of a connected region it holds if and only if the region has constant curvature, $\mathcal{R}(B) = cB$ with $c$ constant (Schur's lemma). For the projected form it requires $Z_{b} = 0$ and $(\nabla_{k}R)(e_{a},e_{b},e^{a},e^{b}) = 0$ for every null $k$ and every screen. On flat elements ($B^{(l)} = 0$, $\omega = 0$ at $p$) both forms reduce to the gradient term, which is nonzero in vacuum: for the vacuum plane-wave field whose derived metric is $-2\,du\,dv + (x^{3} - 3xy^{2})\,du^{2} + dx^{2} + dy^{2}$ it is $6$ at the origin for the null direction $\partial_{u} + \tfrac12\partial_{v} + \partial_{x}$; on radial generators of Schwarzschild-de Sitter the formula reduces to this term, whose value there is computed in the result filed alongside on the vacuum side.
\item[(iii)] \emph{(Consequences.)} With $\alpha \neq 0$, the Clausius relation on every admissible patch through every point of a region holds for the Jacobson-Myers form only if the region has constant curvature; if Einstein's equations hold there, $\Ric^{\circ}(k,k) = 8\pi G\,T(k,k)$, so no null energy crosses and no Weyl curvature is present. Hence on the Einstein route the entropy of open patches cannot contain the Euler term of the series' action, in either form, and the entropy functional within the family $\frac{1}{4G}\int(\eta' + \beta\,{}^{(2)}\!R)\,dA$ or with $P$ is forced to $\beta = 0$: the curvature-independent area density of clause (Loc) of Premise \claimref{synthesis.c-loc-local-horizon-premise}. Together with clause (iv) of Theorem \claimref{synthesis.c-loc-entropy-clause-curvature-independent-density} (a density varying over spacetime is excluded at first order), the Clausius relation derives (Loc) for every density of the form $\eta(x) + \beta\,{}^{(2)}\!R$ or $\eta(x) + \beta P$; it does not derive (Loc) for arbitrary curvature-dependent densities. All of (iii) concerns entropies that are functionals of the cut, the reading under which a Wald entropy is defined; on the differences reading $\delta S = \eta\,\delta A$ that the premise adopts, an $\eta$ depending on curvature scalars at the point produces no first-order term and is not excluded by (H1) (filed alongside, synthesis.loc-independent-of-clausius-and-killing-data).
\end{enumerate}

## technical
The series' action contains, besides the Einstein-Cartan term, an Euler (Gauss-Bonnet) term with coefficient $\alpha = -3/(4\Lambda)$. Its Wald entropy adds to the area term the integral of the intrinsic curvature of the horizon cut; on closed cuts that is a topological constant, invisible to every first law, and the store left open whether it matters on the small open patches of a local Clausius argument. It does, and at the leading order. Along the generators of a Jacobson patch (an element whose expansion and shear vanish at the point), in a gravitational field on flat spacetime whose field strength plays the part of curvature, the Euler density changes at first order in the affine extent, by an amount fixed by the Ricci curvature times the element's other expansion, the Weyl curvature times its other shear, a normal-connection term and a curvature gradient. The heat and the area change start one order later, so the Clausius relation forces this rate to vanish on every patch. Since the element's other expansion, shear and normal connection can be chosen freely, that happens only where the trace-free Ricci and Weyl tensors vanish: in regions of constant curvature, with no null energy if Einstein's equations hold. The projected form of the Wald entropy loses the first two terms but keeps the gradient term, which is already nonzero in vacuum (an exact plane wave; radial generators of Schwarzschild-de Sitter, treated in a result filed alongside). Both conclusions use two readings, stated here: the Clausius relation is imposed on every open patch (the Euler change is a divergence on the cut and cancels on closed cuts, so closed-cut relations do not see it), and the entropy is a functional of the cut. So the Euler term cannot be part of the entropy on the Einstein route, and within the family of entropies the series' action supplies, the Clausius relation selects the pure area density: the curvature-independence that clause (Loc) of the local-horizon premise assumes. This derives (Loc) from the Clausius relation within that family (and, with a stored result, for densities varying over spacetime); it does not exclude every conceivable curvature-dependent density, and on the differences reading $\delta S = \eta\,\delta A$, with $\eta$ evaluated at the point, a density depending on curvature scalars escapes it, so there (Loc) is not derived.

## lay
The series' description of gravity has an extra term in its action that does not change the equations of motion but would, by the standard formula for black-hole entropy, add a curvature term to the entropy of a horizon. For whole horizons that term is a constant and cancels from every comparison. This result looks at the small pieces of horizon used in Jacobson's thermodynamic derivation of Einstein's equations. On those pieces the extra entropy changes at once, as soon as the piece moves along its light rays, whereas the heat carried in by matter and the growth of the area only appear one step later. The balance between heat and entropy that the derivation needs therefore fails unless the gravitational field strength at that point is perfectly uniform, the same in every direction, with no matter flowing and no gravitational waves. So on the thermodynamic route to Einstein's equations, if the entropy of a piece of horizon is computed from the shape of that piece, it must be the area term alone, and within the kinds of entropy the series' action supplies this is exactly the assumption that the entropy per area does not depend on curvature. For whole, closed horizons the extra term cancels again, so the conclusion concerns the small open pieces only.

## one-liner
On a Jacobson patch the series' Euler (Jacobson-Myers) entropy changes at first order in the affine extent, at the rate $\theta_{l}\Ric^{\circ}(k,k) - 2\sigma_{l}\!:\!\widehat{C}_{k} + 4\omega\cdot Z + (\nabla_{k}R)(e,e,e,e)$ (projected form: $4\omega\cdot Z + (\nabla_{k}R)(e,e,e,e)$), one order before heat and area, so the Clausius relation imposed on every open patch (the Euler change is a divergence on the cut and cancels on closed cuts) admits the Euler term only where trace-free Ricci and Weyl curvature vanish, and, for entropies that are functionals of the cut, within the series' entropy family it forces the curvature-independent area density of (Loc); on the differences reading $\delta S = \eta\,\delta A$ (Loc) is not derived.
