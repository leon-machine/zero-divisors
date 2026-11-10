---
id: synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four
kind: claim
version: 1
title: 'One-loop parametrix trace on a torsion-free field: rotors cancel, first order is Ricci'
status: proved
region: synthesis
subject: quantum-fields
tags: [recovers-known-physics, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-09-bridges
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-09-bridges
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field@6
  - synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport@5
  - synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products@1
  - synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_transport_rotors_cancel_from_the_leading_kernel
- kind: check
  ref: check.py::check_contraction_of_the_field_strength_is_the_ricci_vector
- kind: check
  ref: check.py::check_first_order_derivative_of_the_transport_rotor
- kind: check
  ref: check.py::check_first_order_part_of_the_derivative_of_the_leading_coefficient
- kind: check
  ref: check.py::check_tidal_map_of_a_weyl_type_operator
- kind: check
  ref: check.py::check_degrees_of_the_terms_of_the_kernel
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.hadamard-scaling-limit-premise
extraction:
  open_problem: op.qft-loops-and-renormalisation
  note: >-
    Works towards the curved-field clause of extension of distributions (attack item 3 of
    op.qft-loops-and-renormalisation; clause (v) of the stored vacuum-polarisation result, which is argued there and
    stays argued: this result supports its first half and does not lift it). Scope: one loop, the trace form of the
    Dirac Hadamard parametrix, a torsion-free gravitational field, the normal coordinates of one point with the
    other index transported along the geodesic. Status by clause: (i) proved; (ii) proved given the stored
    (computed) Taylor data of the bulk scaling theorem and the protraction identity; (iii) and (iv) argued, because
    the inputs they need are not in the store. Inputs a maintainer Fact would have to supply for (iii) and (iv) to
    become "proved given", all cited from memory here. Scaling-degree rules (Steinmann; Brunetti and Fredenhagen
    2000): (SD1) the Feynman boundary value sigma_F^{-k} (log sigma_F)^j has scaling degree 2k at the diagonal, in
    the relative normal coordinate for a fixed point; (SD2) multiplication by a smooth function vanishing to order
    j on the diagonal lowers the degree by at least j; (SD3) the degree is subadditive under the products that
    occur (two kernels with the same Feynman prescription, whose product is defined off the diagonal); (SD4) the
    Hadamard form at higher order, a remainder of class C^N after N terms, so that (SD2) applies to the remainder,
    the stored theorem giving only C^1. The first Hadamard transport equation: the coincidence value of V is a
    fixed multiple of the squared Dirac operator applied to U at coincidence, which with clause (ii) and the
    Lichnerowicz form is a scalar. The protraction identity of the curvature operator of a torsion-free field
    (the first Bianchi identity; the word does not occur in the store). For the reduction of the freedom to one
    constant: local covariance with scaling (Hollands and Wald 2001, 2002), in the form "the extension is a local
    and covariant functional of the field and scales almost homogeneously under a constant rescaling of the
    displacement gauge field with the mass rescaled inversely", so that the coefficient of a derivative of delta
    of order j is a polynomial in the curvature operator, its derivatives and the mass of dimension 2 - j, and
    the Ward identity then leaves the single constant of the flat field. Second expansion used and not derived:
    the Van Vleck determinant on a vacuum field, Delta = 1 + (1/180) tr K^2 + O(xi^5) with K the tidal map
    (standard, from the Jacobi equation; cited). Not done: the transversality of an extension on the curved field,
    the values of the terms of degree four, the joint extension across the diagonal of the product of the field
    with itself, any other one-loop kernel, and the identification of the current two-point function of a state
    with the stripped trace form (unit and adjoint conventions). Version history of this draft: the sign of the
    rotor term was first taken with the field strength of the gauge field in place of the curvature operator,
    its negative in the store's convention, giving a wrong coefficient -5/12; corrected to +1/12, and the check
    now tests the gauge against the stored sign and on the de Sitter operator. Prior art, cited from memory: time-ordered products on curved
    spacetime by scaling degree (Brunetti and Fredenhagen 2000; Hollands and Wald), where the flat power counting
    is a theorem; covariant expansions of the spinor parallel propagator (Christensen 1978); finiteness of the
    curvature couplings of the photon at one loop (Drummond and Hathrell 1980). What is specific here is the form
    in the series' algebra and the exact cancellation of the rotors. In dimension d the same leading kernel has
    degree 2d - 2 and omega = d - 2 (not used here). Transport-absent.
---

## formal
Units $\hbar = c = 1$. Scope: one loop; the trace form of the Dirac Hadamard parametrix, not a state's current two-point function; a gravitational field $(\hb, \Omega)$ as in Theorem \claimref{synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field} with vanishing torsion; the normal coordinates of the point $x'$, with the vector index at $x$ compared by transport along the geodesic. In another smooth frame or chart the full curvature operator appears at degree four through the change of frame. Vanishing torsion is used in the form of the protraction identity $\partial_{a}\wedge\mathcal{R}(a\wedge b) = 0$ of the curvature operator $\mathcal{R}(B) = -R(\hb(B))$ of Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}, clause (c) ($R$ the covariant field strength of $\Omega$); the identity is the first Bianchi identity of a torsion-free field and is a hypothesis here, not a stored result. The connection of the Dirac operator is then the spin connection of the derived metric (Fact \claimref{synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport}(b)). On a geodesically convex neighbourhood let $\sigma$ be the Synge function, $\Delta$ the Van Vleck determinant, $R(x, x')$ the transport rotor from $x'$ to $x$ ($R(x', x) = \rev{R}$; the rotor is written $R(x, x')$ or $R$ after a vector, the field strength never without its bivector argument), $U = \Delta^{1/2}R$, $s = D_{x}\sigma$ the physical tangent at $x$ of the geodesic from $x'$, so $Q(s) = 2\sigma$, and $s' = D_{x'}\sigma = -\rev{R}sR$. Let $G(x, x') = (D_{x} + m)\,(U/\sigma + V\log\sigma)$ be the parametrix of the cited theorem, clause (i), stripped of its normalising constant, its unit and its boundary prescription, and for a vector $a$ at $x$ and a vector $b$ at $x'$ let
\[
\Pi(a, b; x, x') = \langle a\,G(x, x')\,b\,G(x', x)\rangle_{0}, \qquad \hat b = R\,b\,\rev{R}, \qquad \Pi^{0} = -\frac{2\,(a\cdot s)(\hat b\cdot s) - (a\cdot\hat b)\,Q(s)}{\sigma^{4}} .
\]
Off the diagonal, with the Feynman prescription $\sigma + I_{4}0$ in both factors, this is the form of the time-ordered kernel, which is the one with an extension problem; with the two factors as boundary values from the same side it is the Wightman product, which is a distribution across the diagonal and needs no extension. On the flat field at $m = 0$, $\Pi = \Pi^{0}$ is, up to a constant factor and the Wick rotation used there, the kernel of clause (ii) of Theorem \claimref{synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants}.
\begin{enumerate}
\item[(i)] \emph{(The rotors cancel from the leading kernel; proved.)} The leading parts $-\Delta^{1/2}sR/\sigma^{2}$ of $G(x, x')$ and $-\Delta^{1/2}s'\rev{R}/\sigma^{2}$ of $G(x', x)$ give exactly $\Delta(x, x')\,\Pi^{0}$, for every field strength: $\langle a\,(sR)\,b\,(s'\rev{R})\rangle_{0} = -\langle a\,s\,\hat b\,s\rangle_{0}$, the flat trace of the stored result in the vector $s$ with the vector at $x'$ transported to $x$. No rotor remains, and $\Pi^{0}$ carries no field strength. The cross terms of the leading part with the mass term $mU/\sigma$ are scalar parts of odd elements and vanish identically. The mass-mass trace is $\langle a\,R\,b\,\rev{R}\rangle_{0} = a\cdot\hat b$; the sign of the term $m^{2}\Delta\,(a\cdot\hat b)/\sigma^{2}$ relative to the leading one is not fixed by the stripped trace form (it depends on the unit that has been dropped).
\item[(ii)] \emph{(The derivative of the transport rotor is Ricci; proved given the Taylor data of the cited theorem, clause (ii), which are labelled computed there, and the protraction identity.)} To first order in the separation $\xi$, in the store's convention for $\mathcal{R}$,
\[
a\cdot D_{x}R = +\tfrac14\,\mathcal{R}(a\wedge\xi)\,R, \qquad D_{x}R = \tfrac14\,\gamma^{\mu}\mathcal{R}(e_{\mu}\wedge\xi)\,R = +\tfrac14\,\mathcal{R}(\xi)\,R,
\]
$\mathcal{R}(\xi) = \partial_{a}\cdot\mathcal{R}(a\wedge\xi)$ the Ricci vector: the trivector part vanishes by the protraction identity, and a curvature operator of Weyl type contributes nothing. With $\Delta^{1/2} = 1 - \tfrac{1}{12}\,\xi\cdot\mathcal{R}(\xi)$ of the cited theorem, whose gradient is $-\tfrac16\mathcal{R}(\xi)$,
\[
D_{x}U = +\tfrac{1}{12}\,\mathcal{R}(\xi)\,R + O(\xi^{2}) .
\]
On the de Sitter operator $\mathcal{R}(B) = \tfrac{\Lambda}{3}B$ this is $\tfrac{\Lambda}{12}\,\xi R$. On a vacuum field ($\mathcal{R}(\xi) = 0$ for all $\xi$), $D_{x}U = O(\xi^{2})$ whatever the Weyl part.
\item[(iii)] \emph{(Degrees; argued.)} Given the scaling-degree rules, the coincidence value of $V$ and the higher-order Hadamard form listed in the note, none of which is stored: in the normal coordinates of $x'$ and the transported frame, $\Pi$ has scaling degree $6$ with leading part $\Pi^{0}$; nothing at degree $5$; at degree $4$ terms whose coefficients are $m^{2}$, the Ricci vector map (through $D_{x}U$ and through $(\Delta - 1)\Pi^{0}$) and the coincidence value of $V$ (a scalar, by the first transport equation and (ii)); and the Weyl part of the curvature operator only from degree $3$ down: at degree $3$ through derivatives of the curvature operator, and at degree $2$ through the Van Vleck determinant, $\Delta = 1 + \tfrac{1}{180}\operatorname{tr}K_{\xi}^{2} + O(\xi^{5})$ on a vacuum field, $K_{\xi}(a) = \mathcal{R}(a\wedge\xi)\cdot\xi$ the tidal map (cited), which is quadratic in the Weyl part and not zero.
\item[(iv)] \emph{(The extension; argued, given (iii) and Fact \claimref{synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products}(ii).)} For each fixed $x'$ the time-ordered kernel, as a distribution in the relative normal coordinate off the origin, has degree of divergence $\omega = 6 - 4 = 2$, the flat value, whatever the Weyl part; the stored flat extension read in these coordinates extends $\Pi^{0}$ with the stored logarithmic coefficient; and two extensions of the same degree differ by the $15$ derivatives of $\delta$ of order at most $2$ per pair of indices. On the field these are $15$ coefficient functions of $x'$ per index pair, and nothing here constrains their dependence on $x'$: the joint extension across the diagonal of $M \times M$ is not treated. Even the Ward-preserving freedom on a fixed field is a function space, since $\partial_{\mu}(c(x)F^{\mu\nu})$ is conserved for every smooth $c$. The reduction to the single constant $Z_{3}$ needs local covariance with scaling (argued; Hollands and Wald, from memory). This supports the first half of clause (v) of the cited vacuum-polarisation theorem; it does not prove it.
\end{enumerate}

## technical
The stored bulk Hadamard form writes the Dirac two-point function as a first-order operator applied to $U/\sigma + V\log\sigma$, with $U$ the Van Vleck root times the spinor transport rotor. In the vacuum-polarisation trace the leading term at $x$ carries the rotor and the leading term at $x'$ its reverse, and the tangent of the geodesic at $x'$ is the transported tangent at $x$ with the sign reversed; so the rotors cancel in pairs and the trace is the flat one in the vector $D\sigma$, with one vector index transported, times the Van Vleck determinant. This part is exact algebra. The curvature can then enter only through the Van Vleck determinant, the derivative of $U$ and the logarithmic coefficient. In the gauge $\Omega(a)(x_{0} + z) = -\tfrac12\mathcal{R}(z\wedge a)$, whose field strength is $-\mathcal{R}$ as the store's sign convention requires, the derivative of the transport rotor at first order is $+\tfrac14$ of the curvature operator on the plane of the direction and the separation; contracted with the frame vectors it gives the Ricci vector and a trivector that vanishes by the protraction identity. With the gradient $-\tfrac16$ of the Van Vleck root the first-order part of $D_{x}U$ is $+\tfrac1{12}$ of the Ricci vector, checked against the de Sitter operator. The statements on scaling degrees and on the extension are argued: they need scaling-degree rules, the first Hadamard transport equation and a higher-order Hadamard form that the store does not hold, and they concern the time-ordered kernel for a fixed point $x'$ in its normal coordinates. In that reading the kernel has the flat degree six, no degree five, mass and Ricci coefficients at degree four, and the Weyl part from degree three down, at degree two through the Van Vleck determinant. The freedom of the extension at each point is the flat list of fifteen local terms per index pair, but with coefficients that are functions of the point; only local covariance with scaling would reduce them to the flat constant.

## lay
When a photon travels it can briefly turn into an electron and positron pair, and the mathematics of this effect, called vacuum polarisation, has an infinite part that must be fixed by a rule. In flat space the collection already contains a rule that needs no artificial cut-off. It had only argued that the same works where space is curved, and this result takes two exact steps towards that, without completing it. The setting is the standard leading approximation in curved space, for a gravitational field without the twisting of space that intrinsic spin would source. First, the most singular part of the expression is exactly the flat one written along the straight path between the two points, times one known smooth factor: all the rotation picked up along the path cancels. Second, the first correction to the next ingredient involves only the part of the curvature that is tied to matter, with a definite coefficient of one twelfth; the tidal part, which is all there is in empty space around a star or black hole, drops out at that order. From these it is argued, not proved, that the strength of the infinity is the same as in flat space and that the tidal curvature appears only in milder terms. The list of quantities left free by the rule is the same as in flat space at each point, but in curved space each of them may vary from point to point, and reducing them to the single constant of flat space needs a further principle that is quoted and not derived here. The result does not show that charge conservation can be kept in curved space.

## one-liner
One loop, trace form of the Dirac Hadamard parametrix on a torsion-free gravitational field, normal coordinates at $x'$ with the other index transported: the leading part is exactly $-\Delta\,[2(a\cdot s)(\hat b\cdot s) - (a\cdot\hat b)Q(s)]/\sigma^{4}$, $s = D\sigma$, the transport rotors cancelling (proved); $D_{x}R = +\tfrac14\mathcal{R}(\xi)R$ and $D_{x}U = +\tfrac1{12}\mathcal{R}(\xi)R$ at first order, Ricci only (proved given stored Taylor data and the protraction identity); argued: degree $6$, none at $5$, mass and Ricci terms at $4$, Weyl from $3$ down, and for the time-ordered kernel at each fixed $x'$ the flat $\omega = 2$ with $15$ local terms per index pair whose coefficients are functions of $x'$.
