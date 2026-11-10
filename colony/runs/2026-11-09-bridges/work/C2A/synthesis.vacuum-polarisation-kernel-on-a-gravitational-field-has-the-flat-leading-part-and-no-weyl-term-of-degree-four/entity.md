---
id: synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four
kind: claim
version: 1
title: 'Vacuum polarisation on a curved field: flat leading kernel, no Weyl term to degree four'
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
  ref: check.py::check_degrees_of_the_terms_of_the_kernel
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.hadamard-scaling-limit-premise
extraction:
  open_problem: op.qft-loops-and-renormalisation
  note: >-
    Works the curved-field clause of extension of distributions (attack item 3 of op.qft-loops-and-renormalisation;
    clause (v) of the stored vacuum-polarisation result, which is argued there). The generator-level bounds of the
    Hadamard scaling theorem are not what is needed: the bulk Hadamard form and its Taylor data are stored, and the
    kernel is computed from them. What is proved in the algebra: the transport rotors cancel exactly from the
    leading kernel, which is the Van Vleck determinant times the flat trace in the world-function vector; the
    covariant derivative of the transport rotor contracts to the Ricci vector, so a field strength of Weyl type
    does not enter the kernel down to degree four. What is proved given standard facts: the scaling degrees (given
    (SD), three rules for scaling degrees cited from memory) and the consequences for the extension (given the
    imported extension theorem, whose clause (ii) includes the local statement on a gravitational field). What is
    not done: the transversality of an extension on the curved field, the value of the Ricci and mass terms of
    degree four, the reduction of the freedom to one constant by covariance (argued, Hollands and Wald from
    memory), and any other one-loop kernel. Prior art, cited from memory: the construction of time-ordered products
    on curved spacetime by scaling degree (Brunetti and Fredenhagen 2000; Hollands and Wald 2001, 2002), in which
    the flat power counting is a theorem; covariant expansions of the spinor parallel propagator (Christensen 1978),
    where the coincidence limit of its second derivative is half the commutator of derivatives; and the finiteness
    of the curvature couplings of the photon at one loop (Drummond and Hathrell 1980). What is specific here is the
    form in the series' algebra and the exact cancellation of the rotors. Transport-absent.
---

## formal
Units $\hbar = c = 1$. Let $(\hb, \Omega)$ be a gravitational field as in Theorem \claimref{synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field}, with vanishing torsion, so that its field strength $\mathcal{R}$ obeys the protraction identity $\partial_{a}\wedge\mathcal{R}(a\wedge b) = 0$ and the connection of the Dirac operator is the spin connection of the derived metric (Fact \claimref{synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport}(b)). On a geodesically convex neighbourhood let $\sigma$ be the Synge function, $\Delta$ the Van Vleck determinant, $R = R(x, x')$ the transport rotor from $x'$ to $x$ ($R(x', x) = \rev{R}$), $U = \Delta^{1/2}R$, $s = D_{x}\sigma$ the physical tangent at $x$ of the geodesic from $x'$, so $Q(s) = 2\sigma$, and $s' = D_{x'}\sigma = -\rev{R}sR$. Let $G(x, x') = (D_{x} + m)\,(U/\sigma + V\log\sigma)$ be the Dirac Hadamard parametrix of the cited theorem, clause (i), without its normalising constant, its unit and its boundary prescription (the unit stands outside the product and does not change the grade parity of the terms), and for a vector $a$ at $x$ and a vector $b$ at $x'$ let
\[
\Pi(a, b; x, x') = \langle a\,G(x, x')\,b\,G(x', x)\rangle_{0}, \qquad \hat b = R\,b\,\rev{R},
\]
the trace form whose value on the flat field at $m = 0$ is, up to a constant factor and the Wick rotation used there, the kernel of clause (ii) of Theorem \claimref{synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants} (that the connected two-point function of the current of a quasi-free Hadamard state is this trace form in its two-point functions, plus terms with the state's smooth part, is the standard Wick expansion and is not re-derived here). Degrees are scaling degrees at the diagonal in $x$ for fixed $x'$, in normal coordinates.
\begin{enumerate}
\item[(i)] \emph{(The rotors cancel from the leading kernel; proved.)} The leading part $-\Delta^{1/2}sR/\sigma^{2}$ of $G(x, x')$ and $-\Delta^{1/2}s'\rev{R}/\sigma^{2}$ of $G(x', x)$ give
\[
\Pi_{6}(a, b; x, x') = -\,\Delta(x, x')\,\frac{2\,(a\cdot s)(\hat b\cdot s) - (a\cdot\hat b)\,Q(s)}{\sigma^{4}},
\]
for every field strength: the flat trace $\langle a\,s\,\hat b\,s\rangle_{0}$ of the stored result in the vector $s$, with the vector at $x'$ transported to $x$, times the Van Vleck determinant. No rotor remains. The cross terms of the leading part with the mass term $mU/\sigma$ are scalar parts of odd elements and vanish identically, and the mass-mass term is $m^{2}\Delta\,(a\cdot\hat b)/\sigma^{2}$.
\item[(ii)] \emph{(The derivative of the transport rotor is Ricci; proved from the stored Taylor data.)} To first order in the separation $\xi$, $a\cdot D_{x}R = -\tfrac14\mathcal{R}(a\wedge\xi)R$, so $D_{x}R = -\tfrac14\gamma^{\mu}\mathcal{R}(e_{\mu}\wedge\xi)R = -\tfrac14\mathcal{R}(\xi)R$ with $\mathcal{R}(\xi) = \partial_{a}\cdot\mathcal{R}(a\wedge\xi)$ the Ricci vector: the trivector part vanishes by the protraction identity, and a field strength of Weyl type contributes nothing. With $\Delta^{1/2} = 1 - \tfrac{1}{12}\xi\cdot\mathcal{R}(\xi)$ of the cited theorem, clause (ii), $D_{x}U = -\tfrac{5}{12}\mathcal{R}(\xi)R + O(\xi^{2})$ (the coefficient is in the conventions of the cited theorem and rests on its Taylor data). On a vacuum field ($\mathcal{R}(\xi) = 0$ for all $\xi$), $D_{x}U = O(\xi^{2})$ whatever the Weyl field strength.
\item[(iii)] \emph{(Degrees; proved given (SD).)} $\Pi = \Pi_{6} + \Pi_{4} + \Pi_{\le 3}$, where $\Pi_{6}$ has degree $6$, there is no term of degree $5$, $\Pi_{4}$ has degree at most $4$ and is a sum of terms whose coefficients are $m^{2}$, the Ricci vector map and the coincidence value of $V$ (a scalar, by the Lichnerowicz form of the squared operator in the cited Fact; on the flat field $-\tfrac12 m^{2}$), and $\Pi_{\le 3}$ has degree at most $3$. Here $\Pi_{6} = \Pi^{0} + (\Delta - 1)\Pi^{0}$ with $\Pi^{0}$ the flat trace in $s$, and the second term has degree $4$ with a Ricci coefficient. The Weyl field strength enters $\Pi_{6}$ not at all and $\Pi_{4}$ not at all; it first enters in $\Pi_{\le 3}$. On a vacuum field with $m = 0$, $\Pi = \Pi^{0} + \Pi_{\le 3}$ up to the term with the coincidence value of $V$, which vanishes there if that value is the standard combination of $m^{2}$ and the scalar curvature (cited from memory; stored for the flat field only).
\item[(iv)] \emph{(The extension; proved given (SD) and the imported extension theorem.)} By Fact \claimref{synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products}(ii), at every point of a gravitational field of this scope, with Weyl field strength of any size: the degree of divergence of the kernel is $\omega = 6 - 4 = 2$, the flat value; $\Pi^{0}$ is the flat kernel in the normal coordinates of $x'$ and the transported frame, so the stored flat extension transplanted by these coordinates extends it with the stored logarithmic coefficient; $\Pi_{4}$ has $\omega = 0$ and $\Pi_{\le 3}$ extends uniquely. So two extensions of the same degree differ pointwise by the $15$ derivatives of $\delta$ of order at most $2$ per pair of indices, as on the flat field, and the terms that carry the Weyl field strength have no freedom of their own. This is the first half of clause (v) of the cited vacuum-polarisation theorem (flat degrees of divergence and flat leading scale coefficient), for the vacuum polarisation at one loop.
\end{enumerate}
(SD), standard facts on the scaling degree, cited from memory and not in the store (Steinmann; Brunetti and Fredenhagen 2000): the boundary values $\sigma_{\pm}^{-k}$ have degree $2k$ at the diagonal and $\log\sigma_{\pm}$ degree $0$; multiplication by a smooth function vanishing to order $j$ on the diagonal lowers the degree by at least $j$; the two factors of $\Pi$ are boundary values from the same side, so their product is the boundary value of the product. Not part of this result: that an extension can be chosen transverse on the curved field (the Ward identity there), the values of the terms of $\Pi_{4}$, and the reduction of the pointwise freedom to the single constant $Z_{3}$ by local covariance and dimension (argued: the only invariant symmetric forms on bivectors are the scalar and pseudoscalar parts of the product, and a coefficient built from the Weyl field strength has dimension two; Hollands and Wald, from memory), which is the second half of clause (v) and stays argued.

## technical
The stored bulk Hadamard form writes the Dirac two-point function as a first-order operator applied to $U/\sigma + V\log\sigma$ with $U$ the Van Vleck root times the spinor transport rotor. In the vacuum-polarisation trace the leading term at $x$ carries the rotor $R$ and the leading term at $x'$ carries $\rev{R}$, and the tangent of the geodesic at $x'$ is the transported tangent at $x$ with the sign reversed; so the rotors cancel in pairs and the trace is the flat one in the vector $D\sigma$, with one vector index transported. The field strength can then only enter through the Van Vleck determinant, the derivative of $U$ and the logarithmic coefficient. The derivative of the transport rotor at first order is a quarter of the field strength on the plane of the direction and the separation; contracted with the frame vectors it gives the Ricci vector and a trivector that vanishes by the protraction identity. The Van Vleck determinant is Ricci at second order and the coincidence value of the logarithmic coefficient is a scalar. Hence the kernel has the flat degree six, no degree five, a degree-four part with mass and Ricci coefficients only, and the Weyl field strength is confined to terms of degree at most three, which extend uniquely. The check verifies the rotor cancellation with exact rotors in the spacetime algebra, the derivative formula in the gauge $\Omega(a)(z) = \tfrac12\mathcal{R}(z\wedge a)$, and the contraction on field strengths of type D, sums of rotated copies and Ricci type. The generator-level bounds of the Hadamard scaling theorem are not used.

## lay
When a photon travels it can briefly turn into an electron and positron pair, and the mathematics of this effect, called vacuum polarisation, has an infinite part that must be fixed by a rule. In flat space the collection already contains a rule that needs no artificial cut-off: the troublesome expression is extended across the point where it is undefined, and the extension is unique up to a small, known set of constants. The collection had only argued that the same works where space is curved. This result does the computation for the leading approximation used in curved space. It shows that the most singular part of the expression is exactly the flat one, written along the straight path between the two points, with all the rotation picked up along the path cancelling out. It also shows that the tidal part of the curvature, the part present in empty space around a star or black hole, does not appear in any term singular enough to need a choice. So in empty curved space the counting of free constants is the same as in flat space, point by point. Several steps rest on standard facts about such singular expressions that are quoted and not derived here, and the result does not show that the charge conservation rule can be kept in curved space; that remains argued.

## one-liner
On a torsion-free gravitational field the one-loop vacuum-polarisation trace of the Dirac Hadamard parametrix leads with $-\Delta\,[2(a\cdot s)(\hat b\cdot s) - (a\cdot\hat b)Q(s)]/\sigma^{4}$, $s = D\sigma$, the transport rotors cancelling exactly; $D_{x}R = -\tfrac14\mathcal{R}(\xi)R$ is Ricci at first order, so the kernel has the flat degree $6$, no degree $5$, mass and Ricci terms at degree $4$ and the Weyl field strength only at degree at most $3$; given standard scaling-degree rules and the imported extension theorem, the degree of divergence and the pointwise freedom are the flat ones.
