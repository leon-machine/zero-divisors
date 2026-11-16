---
id: synthesis.spectral-asymmetry-on-real-projective-five-space-from-monogenic-polynomials
kind: claim
version: 1
title: 'The spectral asymmetry on real projective five-space from monogenic polynomials'
status: proved
region: synthesis
subject: standard-model
tags: [hypercharge-and-anomalies, spinor-modules, pseudoscalar-and-centre, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-16-anomaly
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-16-anomaly
review: draft
outside_ga:
  kind: complex-analysis
  why: 'Clauses (i) to (iv) are stated and proved in the geometric algebra of the six-space, with the volume element J as the only unit. Clause (v) evaluates a spectral asymmetry: the value at zero of the analytic continuation of a Dirichlet series, obtained by a Mellin transform, and its Abel sum; that step is complex analysis in the variable s and has no geometric-algebra form. The completeness step of clause (iii), that the polynomial eigenfunctions give the whole spectrum of the operator on square-integrable fields, is Hilbert-space structure (density and essential self-adjointness) and is likewise outside geometric algebra.'
derivations:
- name: main
  uses:
  - synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element@1
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_volume_element_spinor_ideal_and_the_pair_with_omega
- kind: check
  ref: check.py::check_monogenic_dimensions
- kind: check
  ref: check.py::check_bivector_operator_eigenvalues_and_the_antipodal_lift
- kind: check
  ref: check.py::check_spectrum_on_polynomials_of_each_parity
- kind: check
  ref: check.py::check_clifford_map_and_connection_on_the_sphere
- kind: check
  ref: check.py::check_alternating_series_and_the_count_for_fifteen_and_sixteen
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element
  - synthesis.wall-rung-count-is-height-of-dying-line-class
extraction:
  open_problem: op.order-four-anomaly-and-sixteen
  note: >-
    Third attack item of op.order-four-anomaly-and-sixteen: the fixed-point count on real projective five-space,
    which the problem records as argued and not computed in the store, derived here from the spectrum. Proved
    with exact checks: the Fischer decomposition and the dimensions of the monogenic spaces, the eigenvalues of
    the bivector operator, the compatibility of the connection, the lift of the antipodal map and its pairing
    with the pseudoscalar of the ten, the generating function and its two evaluations. Classical analysis used,
    named as background (CA) in the formal statement and not derived in the store: density of polynomials in the
    continuous functions on the sphere and essential self-adjointness of the Dirac operator on a closed manifold
    (the eigenfunctions give the whole spectrum); the value at zero of a Mellin transform (the equality of the
    continued series with the Abel sum). Standard and transport-absent: the Fischer decomposition and the spherical monogenics are
    those of Clifford analysis (Brackx, Delanghe and Sommen 1982; Delanghe, Sommen and Soucek 1992; from memory),
    and the Dirac spectrum of the round spheres and the eta invariants of spherical space forms are classical
    (the spectrum: Trautman; Baer; the eta invariants: Gilkey), cited from memory and not used as premises, and the result agrees with the value 1/16
    modulo integers that the formula of Hsieh (Discrete gauge anomalies revisited, arXiv:1808.02881, equation
    (2.47) at m = 2, charge 1) gives, checked at source, and with the value 1/16 stated for real projective
    five-space by Garcia-Etxebarria and Montero (arXiv:1808.00009, section 4.3, checked at source), whose
    eta of equation (2.14) includes the factor one half and so is the xi of this result. Not claimed, and not a premise: that the
    phase built from half the asymmetry is an obstruction to a consistent theory of the components on a wall
    (the anomaly statement of the literature, which by the decision of 9 November 2026 is not imported); that a
    wall with this cross-section occurs in the series; anything on a reading with the Majorana term, where the
    pseudoscalar is broken to the grading. The count separates fifteen from sixteen only if that statement is
    added.
---

## formal
Let the six-space be $\R^{6}$ with $Q(e_{a}) = -1$ for an orthonormal frame $e_{1}, \dots, e_{6}$, so that $Q(x) = -|x|^{2}$ with $|x|^{2} = \sum_{a}x_{a}^{2}$, and let $\Cl(0,6)$ be its geometric algebra, with volume element $J = e_{1}e_{2}\cdots e_{6}$. Let $S$ be a minimal left ideal of $\Cl(0,6)$, the real spinor space, of real dimension $8$; $J^{2} = -1$, $J$ commutes with the even subalgebra and anticommutes with vectors, so left multiplication by $J$ makes $S$ a module of dimension $4$ over $\mathrm{span}\{1, J\}$. Write $\partial = \sum_{a}e_{a}\partial_{a}$ for the vector derivative (in this frame; the reciprocal frame changes its sign, not its kernel), $E = \sum_{a}x_{a}\partial_{a}$ for the Euler operator and
\[
x \wedge \partial = \sum_{a < b}e_{a}e_{b}\,(x_{a}\partial_{b} - x_{b}\partial_{a}),
\]
the bivector part of $x\partial$, so that $x\partial = -E + x \wedge \partial$. Let $\mathcal{P}_{k}$ be the $S$-valued polynomials on the six-space homogeneous of degree $k$, and $M_{k} = \{P \in \mathcal{P}_{k} : \partial P = 0\}$ the monogenic ones. The unit sphere is $\Sph^{5} = \{Q(x) = -1\}$, with unit normal $n = x$, and real projective five-space $\mathbb{RP}^{5}$ is its quotient by the antipodal map.

\emph{Background (CA), classical analysis, used and not derived here.} (CA1) The polynomials are dense in the continuous functions on the sphere (Stone and Weierstrass), hence in the square-integrable ones. (CA2) The Dirac operator of a closed Riemannian manifold with a spin structure is essentially self-adjoint on smooth fields, so that a complete system of smooth eigenfields carries its whole spectrum, with multiplicities. (CA3) The Mellin lemma: for $f$ smooth on $[0, \infty)$ with exponential decay, $\Gamma(s)^{-1}\int_{0}^{\infty}t^{s-1}f(t)\,dt$ continues to an entire function of $s$ with value $(-1)^{j}f^{(j)}(0)$ at $s = -j$. Clauses (i), (ii) and (iv) and the algebraic identities of (iii) and (v) do not use (CA); the statements of (iii) that the listed values are the whole spectrum, and of (v) that the continued asymmetry function at $0$ equals the Abel sum, are proved given (CA).
\begin{enumerate}
\item[(i)] \emph{(Fischer decomposition.)} $\partial : \mathcal{P}_{k} \to \mathcal{P}_{k-1}$ is onto, $\mathcal{P}_{k} = M_{k} \oplus x\,\mathcal{P}_{k-1}$, and
\[
\dim_{\R}M_{k} = 8\Bigl[\binom{k+5}{5} - \binom{k+4}{5}\Bigr] = 8\binom{k+4}{4} .
\]
For $P \in M_{k}$, $\partial(xP) = -(6 + 2k)P$. Since $x^{2} = -1$ on the sphere, the restrictions to $\Sph^{5}$ of all $S$-valued polynomials are spanned by the restrictions of the $M_{k}$ and the $xM_{k}$.
\item[(ii)] \emph{(The bivector operator.)} $x \wedge \partial = k$ on $M_{k}$ and $x \wedge \partial = -(k + 5)$ on $xM_{k}$.
\item[(iii)] \emph{(The Dirac operator of the sphere.)} On $S$-valued fields on $\Sph^{5}$ let a tangent vector $X$ act by the bivector $Xn$, and let $\nabla_{X} = \partial_{X} + \tfrac12 Xn$. Then $(Xn)(Yn) + (Yn)(Xn) = XY + YX$, the Clifford relation of the tangent space; $\nabla_{X}(Yn\,\psi) = (D_{X}Y)n\,\psi + Yn\,\nabla_{X}\psi$ with $D$ the Levi-Civita derivative of the round sphere; and for a tangent frame $e_{a}$
\[
D_{\Sph} = \sum_{a = 1}^{5}e_{a}n\,\nabla_{e_{a}} = -\,x \wedge \partial - \tfrac52 .
\]
By (ii), $D_{\Sph} = -(k + \tfrac52)$ on $M_{k}|_{\Sph^{5}}$ and $+(k + \tfrac52)$ on $xM_{k}|_{\Sph^{5}}$, each of dimension $4\binom{k+4}{4}$ over $\mathrm{span}\{1, J\}$, $k = 0, 1, 2, \dots$; given (CA1) and (CA2) these exhaust the spectrum, and $0$ is not in it.
\item[(iv)] \emph{(The antipodal map and the pseudoscalar of the ten.)} $(A\psi)(x) = J\psi(-x)$ covers the antipodal map, preserves the Clifford map $X \mapsto Xn$, commutes with $D_{\Sph}$, and $A^{2} = -1$: on $M_{k}$ it is $(-1)^{k}J$ and on $xM_{k}$ it is $(-1)^{k+1}J$, with $J(xP) = -x(JP)$. The rotors covering the rotation $x \mapsto -x$ of the six-space are $\pm J$ only, of square $-1$, so the deck group does not lift to the rotor group and $\mathbb{RP}^{5}$ has no spin structure. Let $\omega$ be the pseudoscalar of the ten Majorana generators of Hypothesis (S) (\claimref{standard-model.hyp-s-slot-statistics}), which satisfies $\omega^{2} = -1$ and acts on the sixteen components $V_{+}$ of a generation as $-I$, $I$ the unit of the module (\claimref{synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element}(2)). Then $J \otimes \omega$ is an involution of $S \otimes V_{+}$, equal to $+1$ on the half $W_{+}$ on which $J \otimes 1 = 1 \otimes I$ (the tensor product over the unit, with $J$ matched with $+I$: a matching of the two units on this module, not an identification of them) and to $-1$ on the other half $W_{-}$, the opposite matching, on which every sign of $\xi$ below is reversed. Hence $A \otimes \omega$ is an involution of the $W_{+}$-valued fields on $\Sph^{5}$, acting by $\Psi(x) \mapsto \Psi(-x)$: the fields on $\mathbb{RP}^{5}$ that the pair $(A, \omega)$ defines are the even $W_{+}$-valued fields on the sphere, and for $\omega^{-1}$ in place of $\omega$, or $W_{-}$ in place of $W_{+}$, the odd ones. Per component of $V_{+}$ these are the $S$-valued fields of one parity: for even fields $D_{\Sph}$ has the eigenvalues $-(k + \tfrac52)$, $k$ even, and $+(k + \tfrac52)$, $k$ odd.
\item[(v)] \emph{(The spectral asymmetry.)} For one component of $V_{+}$ and even fields, the asymmetry function is
\[
\eta(s) = \sum_{\lambda}\operatorname{sgn}(\lambda)\,|\lambda|^{-s} = -\sum_{k \ge 0}(-1)^{k}\,4\binom{k+4}{4}\,(k + \tfrac52)^{-s}, \qquad 4\binom{k+4}{4} = \tfrac16\bigl(u^{2} - \tfrac94\bigr)\bigl(u^{2} - \tfrac14\bigr), \ u = k + \tfrac52 .
\]
The series $\sum_{k}(-1)^{k}4\binom{k+4}{4}t^{k} = 4/(1 + t)^{5}$ has Abel sum $\tfrac18$ at $t = 1$; given (CA3) the continuation of $\eta$ to $s = 0$ is finite and equals minus that Abel sum, and the same value follows from $\sum_{k}(-1)^{k}(k + a)^{j} = \tfrac12E_{j}(a)$ with the Euler polynomials, $\tfrac1{12}\bigl(E_{4}(\tfrac52) - \tfrac52E_{2}(\tfrac52) + \tfrac9{16}\bigr) = \tfrac18$, independently of the shift $a$ in which the multiplicity is expanded. So
\[
\eta(0) = \mp\tfrac18, \qquad \xi = \tfrac12\eta(0) = \mp\tfrac1{16}
\]
per component, the upper sign for even and the lower for odd fields. For $n$ components on which $\omega$ acts by the same unit, $\xi = \mp\tfrac{n}{16}$: an integer exactly when $16$ divides $n$; $\mp1$ for the sixteen of one generation and $\mp\tfrac{15}{16}$ for fifteen components. With $n_{-}$ components on which an order-four element acts as $-I$ and $n_{+}$ on which it acts as $+I$, $\xi = \mp\tfrac{1}{16}(n_{-} - n_{+})$, the signed counts of clause (4) of the cited result divided by $16$.
\end{enumerate}
\emph{What is and is not shown.} Clauses (i), (ii), (iv), the operator identity and eigenvalues of (iii) and the two evaluations of (v) are proved, with exact checks. That the eigenvalues of (iii) are the whole spectrum, and that the continued asymmetry function of (v) at $0$ is the Abel sum, are proved given the background (CA), which is classical and is not derived or stored here. Here $\xi$ is per component of the sixteen $V_{+}$, each component carrying one copy of the spinor module $S$ of the five-sphere; reading it as the contribution of one four-dimensional Weyl field is the inflow statement of the literature and is not imported. The value agrees with the classical fixed-point weight $\tfrac12 \cdot 2^{-3}$ of the one nontrivial deck element recorded as argued in the open problem. Not shown, not imported and not used: that $\exp(2\pi I\,\xi)$ is the phase by which a theory of these components fails to be defined on such a quotient, so that a nonintegral $\xi$ excludes the content. That statement is the anomaly statement of the literature. With it, the count would say: on a reading without the Majorana term, sixteen components per generation are allowed and fifteen are not, for any number of generations not divisible by $16$. Without it, the count is a spectral invariant of the pair $(A, \omega)$ and constrains nothing. The lens space of the quarter turn is not the relevant quotient for the same reason that $J$ enters here: the rotor lifting the quarter turn in three planes has fourth power $-1$, so with it $\omega$ would have to be replaced by an element of order eight.

## technical
Under Hypothesis (S), which supplies the pseudoscalar $\omega$ of the ten, and given the classical analysis named as background in the formal statement: spinor fields on the five-sphere are restrictions of spinor-valued polynomials on the six-space, and the monogenic ones, annihilated by the vector derivative, organise them: every polynomial of degree $k$ is a monogenic one plus $x$ times a polynomial of lower degree. The Dirac operator of the round sphere, built from the flat derivative with the Clifford map $X \mapsto Xn$, is $-x \wedge \partial - \tfrac52$, and the bivector operator $x \wedge \partial$ is $k$ on monogenic polynomials of degree $k$ and $-(k+5)$ on $x$ times them. That gives the spectrum $\pm(k + \tfrac52)$ with multiplicity $4\binom{k+4}{4}$, with no matrices and no imaginary unit: the unit is the volume element $J$ of the six-space.

The antipodal map is a rotation of the six-space, and its lift to spinors is $J$, of square $-1$, so projective five-space has no spinors. The pseudoscalar $\omega$ of the ten Majorana generators also squares to $-1$ on the sixteen, and the pair $J\omega$ is an involution; on the half of the spinors where $J$ is matched with the module's unit it acts trivially, so the fields on projective five-space are simply the even (or the odd) fields on the sphere. The parity of a monogenic polynomial is that of its degree, and of $x$ times it the opposite, so the positive and negative eigenvalues alternate with $k$, and the spectral asymmetry is the alternating sum of the multiplicities. Its generating function is $4/(1+t)^{5}$, with value $\tfrac18$ at $t = 1$; half of it is $\tfrac1{16}$ per component.

So the number $\tfrac1{16}$ per component of the sixteen (one copy of the five-dimensional spinor module each) is rederived here in geometric algebra, and sixteen components give an integer while fifteen do not. The mathematics is classical: the Fischer decomposition and the spherical monogenics are those of Clifford analysis, and the value agrees with the literature's. What is new for the store is the derivation in its language, not the result. Whether a nonintegral value is forbidden is a separate statement, from the literature on global anomalies, which the store does not hold.

## lay
The open problem asked for a count that had only been argued: on a five-dimensional space made by identifying opposite points of a sphere, each matter component contributes one sixteenth to a certain spectral quantity. Here the count is rederived step by step in the series' own language; the mathematics behind it is classical. The vibration modes of a matter field on the sphere are read off from polynomials on the surrounding six-dimensional space; identifying opposite points keeps the modes of one parity; positive and negative frequencies then alternate, and their imbalance sums to one eighth, half of which is one sixteenth. Sixteen components therefore give a whole number and fifteen do not. Whether nature requires a whole number is a further statement from the literature that the store has chosen not to adopt, so by itself the count does not yet forbid fifteen. The count is made assuming the series' hypothesis on the matter components, Hypothesis (S), and given three classical facts of analysis that are named and not rederived.

## one-liner
On the unit sphere of the six-space $D_{\Sph} = -x \wedge \partial - \tfrac52$ is $\mp(k + \tfrac52)$ on $M_{k}$ and $xM_{k}$ (dimension $4\binom{k+4}{4}$ over $\mathrm{span}\{1, J\}$); the antipodal lift $J$ and the pseudoscalar $\omega$ of the ten pair to an involution whose fields on $\mathbb{RP}^{5}$ are the fields of one parity, so, given classical analysis named as background (density, essential self-adjointness, the Mellin lemma), $\eta(0) = \mp\tfrac18$ (Abel sum of $4/(1+t)^{5}$) and $\xi = \mp\tfrac1{16}$ per component of the sixteen: an integer for sixteen components, $\tfrac{15}{16}$ for fifteen; that a nonintegral $\xi$ excludes the content is the literature's anomaly statement, not imported.
