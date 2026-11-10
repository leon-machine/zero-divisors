---
id: synthesis.one-loop-self-energy-and-vertex-extend-with-the-ward-identity-holding-at-a-common-cut-off-length
kind: claim
version: 1
title: 'One-loop self-energy and vertex: cut-off extensions obeying the Ward identity'
status: proved
region: synthesis
subject: quantum-fields
tags: [recovers-known-physics, scattering-amplitudes, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-10-phase3
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase3
review: draft
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - field-theory.second-quantisation@6
  - field-theory.coupled-system-tree-level@4
  - synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products@2
  - synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_kernels_in_the_euclidean_algebra_and_their_gauge_dependence
- kind: check
  ref: check.py::check_identities_off_the_origin
- kind: check
  ref: check.py::check_cut_off_extensions_against_the_logarithmic_forms
- kind: check
  ref: check.py::check_product_of_the_extended_self_energy_with_a_coordinate
- kind: check
  ref: check.py::check_ward_matching_of_subtractions_and_scale_coefficients
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants
  - synthesis.one-loop-qed-in-the-spacetime-algebra
extraction:
  open_problem: op.qft-loops-and-renormalisation
  note: >-
    Answers, at one loop, the second attack line of the problem (existence of Ward-preserving extensions of the
    self-energy and vertex inside the store) and the self-energy and vertex half of the first. The stored
    regulator-free result already holds the scaling degrees, the degrees of divergence ($1$ and $0$) and the count
    of covariant differences ($\delta m$ and $Z_{2} = Z_{1}$ under the Ward-Takahashi identity and the
    reflection); it imports the existence of a Ward-preserving pair (Scharf). This result supplies one such pair
    explicitly and proves the identity for it, so at one loop, for these two kernels, the import is not needed;
    at higher orders, and for the four-photon and three-current kernels, it still is. Kill conditions registered
    before computing: a nonzero Ward defect at a common cut-off length (did not fire: the defect is zero by an
    identity of absolutely convergent integrals); a ratio of the differential-renormalisation scales different
    from the literature value (did not fire); log coefficients contradicting the stored $c_{V} = -c_{2}$ or the
    textbook $Z_{2}$ coefficient (did not fire); a hidden infrared regulator (none: the vertex falls off as the
    inverse sixth power of the position of the photon vertex, so its integral over that position converges).
    Everything here is standard physics. The Ward-Takahashi identity and its zero-transfer form are textbook; the
    coefficients $-\xi$ and $3 + \xi$ of the one-loop self-energy in a covariant gauge and the vanishing of the
    massless self-energy in the Landau gauge are textbook (from memory); the method is that of Epstein and Glaser
    and of differential renormalisation. Prior art for clause (v): Freedman, Johnson and Latorre (Nucl. Phys. B
    371 (1992) 353; from memory) and Haagensen and Latorre found that the Ward identity ties the two scales of the
    differentially renormalised self-energy and vertex by $\ln(M_{\Sigma}/M_{V}) = 1/4$; the value was checked on
    the web as quoted in eq. (36) of del Aguila, Culatti, Munoz Tapia and Perez-Victoria, arXiv:hep-th/9709067,
    who attribute it to Haagensen and Latorre for a general covariant gauge. The scale $M_{V}$ of clause (v) is
    defined on the zero-transfer vertex; that it is the same scale as theirs is not shown, only that the value
    agrees. What may be new is only the arrangement: the cut-off region of the vertex is taken to be a cylinder
    (the length of the photon line below the cut-off length, the photon vertex anywhere), which makes the
    identity exact with no computation of the vertex; it is not claimed as new. The geometric algebra adds
    nothing to the textbook content: the kernels are products of vectors of $\Cl(4,0)$ and no matrix or
    imaginary unit occurs on the Euclidean section, which is the whole of what the algebra contributes.
    Transport-absent. The self-energy and vertex kernels contain the photon propagator in a covariant gauge, so,
    as in the stored result, they are read under the Krein-form premise
    synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields, which is in the past cone through the
    stored result; no assumes edge is filed here (maintainer's decision). Not covered: the continuation to the
    Feynman distributions (the standard Wick rotation, as in the stored result); on-shell renormalisation
    conditions and the infrared divergence of the on-shell $Z_{2}$; the form factors (the stored one-loop result
    has $F_{2}(0)$ with regulator fields); any gravitational field.
  flags:
  - 'the Freedman, Johnson and Latorre reference and the textbook gauge coefficients are cited from memory; the value 1/4 was checked on the web in a later paper of the same school that quotes it'
  - 'the identification of the vertex scale of clause (v) with the scale of the differential-renormalisation literature is not shown'
  - 'the massive propagator is used through its standard properties (fundamental solution, exponential decay, local integrability, scaling degree 3), which are not checked; the checks are on the massless kernels and the order-m coefficient'
  - 'the Krein-form premise is in the cone through the stored regulator-free result; whether this result should carry its own assumes edge is the maintainer''s decision'
---

## formal
Units $\hbar = c = 1$; the Euclidean section of the flat field, as in Theorem \claimref{synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants} (the Feynman distributions follow by the standard Wick rotation), under the imported extension theorem (Fact \claimref{synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products}(ii)). Vectors are those of $\Cl(4,0)$ with orthonormal basis $\gamma_{1},\dots,\gamma_{4}$; $\nabla = \sum_{a}\gamma_{a}\partial_{a}$. For the Dirac field of Proposition \claimref{field-theory.second-quantisation} of mass $m \ge 0$ let $S$ be its Euclidean propagator, the vector-plus-scalar valued kernel with $(\nabla + m)S = \delta = S(\overleftarrow{\nabla} + m)$ that tends to zero at infinity; for $m = 0$, $S(w) = w/(2\pi^{2}Q(w)^{2})$. The photon propagator in the covariant gauge with parameter $\xi$ ($\xi = 1$ Feynman, $\xi = 0$ Landau) is the bilinear form $D_{w}(a,b) = \frac{1}{4\pi^{2}Q(w)}\big(\tfrac{1+\xi}{2}\,a\cdot b + (1-\xi)\frac{(a\cdot w)(b\cdot w)}{Q(w)}\big)$. With the vertex and coupling $e$ of Proposition \claimref{field-theory.coupled-system-tree-level}, the one-loop kernels are, with $x$, $y$ the ends of the electron line, $z$ the photon vertex, $u = x - z$, $v = z - y$, $w = u + v$ and $n$ the vector at the photon vertex,
\[
\Sigma(w) = e^{2}\sum_{a,b}\gamma_{a}S(w)\gamma_{b}\,D_{w}(\gamma_{a},\gamma_{b}), \qquad \Lambda(n;u,v) = e^{2}\sum_{a,b}\gamma_{a}S(u)\,n\,S(v)\gamma_{b}\,D_{u+v}(\gamma_{a},\gamma_{b}),
\]
defined for $w \neq 0$ and for $(u,v) \neq (0,0)$ (overall signs and units are conventions and are not fixed here). Write $\operatorname{div}\Lambda = \sum_{a}(\partial_{v_{a}} - \partial_{u_{a}})\Lambda(\gamma_{a};u,v)$, the divergence in $z$. For a length $\ell > 0$ define, on test functions $g$ on $\R^{4}$ and $f$ on $\R^{8}$,
\[
\langle\bar\Sigma^{\ell},g\rangle = \int\Sigma(w)\big(g(w) - \theta(\ell^{2} - Q(w))(g(0) + w\cdot\nabla g(0))\big)d^{4}w, \qquad \langle\bar\Lambda^{\ell}(n),f\rangle = \int\Lambda(n;u,v)\big(f(u,v) - \theta(\ell^{2} - Q(u+v))f(0,0)\big)d^{4}u\,d^{4}v,
\]
$\theta$ the unit step. The method and all values are standard; the statement records them in the series' algebra.
\begin{enumerate}
\item[(i)] \emph{(Kernels and degrees; computed.)} $\sum_{a,b}\gamma_{a}w\gamma_{b}D_{w}(\gamma_{a},\gamma_{b}) = -2\xi w/(4\pi^{2}Q(w))$ and $\sum_{a,b}\gamma_{a}\gamma_{b}D_{w}(\gamma_{a},\gamma_{b}) = (3+\xi)/(4\pi^{2}Q(w))$, so $\Sigma(w) = -\frac{\xi e^{2}}{4\pi^{4}}\frac{w}{Q(w)^{3}} + \frac{(3+\xi)e^{2}m}{16\pi^{4}}\frac{1}{Q(w)^{2}} + (\text{scaling degree at most } 3)$: scaling degree $5$ in $\R^{4}$, degree of divergence $1$, as stored. $\Lambda$ is locally integrable on $\R^{8}\setminus\{0\}$ (its factors have scaling degrees $3$, $3$, $2$ on the partial diagonals) and has scaling degree $8$ at the origin, degree of divergence $0$, as stored. For $m = 0$ in the Landau gauge $\Sigma$ vanishes identically off the origin.
\item[(ii)] \emph{(Off the coincident point; proved.)} On $\R^{8}\setminus\{0\}$, $\operatorname{div}\Lambda = \delta(v)\Sigma(u) - \delta(u)\Sigma(v)$. For $w \neq 0$ the integral of $\Lambda$ over the photon vertex converges absolutely and
\[
\int\Lambda\big(n;\tfrac{w}{2}+t,\tfrac{w}{2}-t\big)\,d^{4}t = (n\cdot w)\,\Sigma(w),
\]
which follows from $\int S(x-z)\,n\,S(z-y)\,d^{4}z = (n\cdot(x-y))\,S(x-y)$. Both hold for every $m \ge 0$ and for any photon kernel that depends on $w$ alone.
\item[(iii)] \emph{(The Ward identity on the extended kernels; proved.)} $\bar\Sigma^{\ell}$ and $\bar\Lambda^{\ell}$ are extensions of $\Sigma$ and $\Lambda$ with the same scaling degrees, covariant under rotations and reflections of $\Cl(4,0)$, and for every $\ell > 0$, every $\xi$ and every $m \ge 0$
\[
\operatorname{div}\bar\Lambda^{\ell} = \delta(v)\,\bar\Sigma^{\ell}(u) - \delta(u)\,\bar\Sigma^{\ell}(v) \qquad\text{on } \R^{8}.
\]
The identity is not imposed by a choice of constant: it holds because the vertex is subtracted on the cylinder $Q(u+v) < \ell^{2}$ and the self-energy on the ball $Q(w) < \ell^{2}$ of the same length.
\item[(iv)] \emph{(Different lengths, $m = 0$; computed.)} With $\mu = 1/\ell$, $\mu\,\partial_{\mu}\bar\Sigma^{\ell} = \frac{\xi e^{2}}{8\pi^{2}}\nabla\delta$ and $\mu\,\partial_{\mu}\bar\Lambda^{\ell}(n) = -\frac{\xi e^{2}}{8\pi^{2}}\,n\,\delta(u)\delta(v)$: the coefficient $\xi e^{2}/(16\pi^{2})$ of $\ln\mu^{2}$ in the self-energy is the textbook one, and the two derivatives are opposite, the stored relation $c_{V} = -c_{2}$. With the vertex cut at length $\ell_{V}$ and the self-energy at $\ell_{\Sigma}$ the identity of (iii) fails by the local term $\frac{\xi e^{2}}{8\pi^{2}}\ln(\ell_{V}/\ell_{\Sigma})\sum_{a}(\partial_{v_{a}} - \partial_{u_{a}})\gamma_{a}\delta(u)\delta(v)$, zero only for $\ell_{V} = \ell_{\Sigma}$ unless $\xi = 0$. For $m > 0$ the mass term of $\bar\Sigma^{\ell}$ has $\mu\,\partial_{\mu}$ equal to $\frac{(3+\xi)e^{2}m}{8\pi^{2}}\delta$ at leading order in $m\ell$.
\item[(v)] \emph{(In the logarithmic form of the stored result, $m = 0$; computed.)} With $s = Q(w)$: the cut-off extension of $1/s^{2}$ with the value subtracted on the ball of radius $\ell$ is $-\frac14\nabla^{2}(\ln(M^{2}s)/s)$ with $\ln(M^{2}\ell^{2}) = 1$; that of $w/s^{3}$ with the first-order Taylor polynomial subtracted is $\frac{1}{16}\nabla\nabla^{2}(\ln(M^{2}s)/s)$ with $\ln(M^{2}\ell^{2}) = \frac32$. So $\bar\Sigma^{\ell} = -\frac{\xi e^{2}}{64\pi^{4}}\nabla\nabla^{2}(\ln(M_{\Sigma}^{2}s)/s)$, and the zero-transfer vertex $\int\bar\Lambda^{\ell}(n)\,d^{4}t$ is $-\frac{\xi e^{2}}{4\pi^{4}}$ times the sum of the homogeneous distribution $\frac18\big((n\cdot\nabla)\nabla - \frac14 n\nabla^{2}\big)(1/s)$, which carries no scale, and $-\frac{1}{16}n\,\nabla^{2}(\ln(M_{V}^{2}s)/s)$; the identity of (iii) holds exactly when
\[
\ln\big(M_{\Sigma}^{2}/M_{V}^{2}\big) = \tfrac12 ,
\]
the value $\ln(M_{\Sigma}/M_{V}) = \frac14$ of differential renormalisation.
\item[(vi)] \emph{(The freedom; from the stored count.)} By clause (iii) of the stored theorem any two covariant pairs of extensions obeying the identity and the reflection differ by $\delta m$ and $Z_{2} = Z_{1}$ only. With (iii) here such a pair exists at one loop, so the Ward-preserving pairs of extensions of the one-loop self-energy and vertex are exactly $\bar\Sigma^{\ell} + c_{m}\delta + c_{2}\nabla\delta$, $\bar\Lambda^{\ell}(n) - c_{2}\,n\,\delta(u)\delta(v)$ with two real constants $c_{m}$, $c_{2}$ (a change of $\ell$ being a change of $c_{2}$ at $m = 0$). For these two kernels at one loop the existence imported in that theorem (Scharf) is proved here; at higher orders and for the four-photon and three-current kernels it remains imported. As there, the kernels contain the covariant photon propagator and are read under the Krein-form premise.
\end{enumerate}

## technical
The stored regulator-free result extends the one-loop vacuum polarisation explicitly and, for the electron self-energy and the vertex, counts how two Ward-preserving extensions can differ while importing that one exists. Here one is written down. On the Euclidean section the self-energy kernel is the product of the electron and photon propagators, $-\xi e^{2}w/(4\pi^{4}Q(w)^{3})$ plus a mass term with coefficient $3 + \xi$, with $\xi$ the gauge parameter; the vertex kernel is a product of two electron propagators and the photon propagator of the line joining the electron's ends. Away from the point where all three positions coincide, the divergence of the vertex in the position of the photon vertex is the difference of two self-energies (the Ward-Takahashi identity), and the integral of the vertex over that position is the self-energy times the separation of the ends (its zero-transfer form); both follow from the propagator being a fundamental solution, for any mass and any gauge parameter. Extend the self-energy by subtracting the test function's first-order Taylor polynomial inside a ball of radius $\ell$, and the vertex by subtracting the test function's value at the origin whenever the electron's ends are closer than $\ell$, wherever the photon vertex is. Then the Ward-Takahashi identity holds for the extended kernels exactly, as an identity of absolutely convergent integrals: nothing is adjusted. If the two lengths differ, it fails by a local term proportional to $\xi\ln(\ell_{V}/\ell_{\Sigma})$. Rewritten in the logarithmic form used by the stored result, the two cut-off extensions carry scales with $\ln(M^{2}\ell^{2}) = 3/2$ and $1$, so the identity ties the scales by $\ln(M_{\Sigma}^{2}/M_{V}^{2}) = 1/2$, the known relation of differential renormalisation. With the stored count this gives all Ward-preserving pairs at one loop: the pair above plus the two constants $\delta m$ and $Z_{2} = Z_{1}$. All of it is textbook physics under the imported extension theorem and, for the photon line, the Krein-form premise; no infrared regulator enters, and the on-shell conditions are not treated.

## lay
A charged particle's own field feeds back on it, and the calculation of this effect is singular where the points involved coincide. The series already treated one such quantity, the screening of charge, by a method that needs no artificial regulator, and for two others, the electron's self-interaction and its coupling to light, it relied on the literature for the statement that the method can be made to respect charge conservation. Under the same standard theorem on extending singular quantities, and assuming the series' premise on how the photon's states are measured, this result carries out those two cases at the lowest order: if both quantities are cut off at one common length, charge conservation holds exactly with nothing adjusted, and what remains free is two constants, the electron's mass and the normalisation of its field, as the series had counted. The numbers obtained are the known ones. This is a recovery of standard physics in the series' algebra, at the lowest order only; higher orders still rely on the literature.

## one-liner
Standard (Ward and Takahashi; Epstein and Glaser; differential renormalisation), now in the store: under the imported extension theorem and the Krein-form premise, on the Euclidean section, the one-loop electron self-energy (cut off on a ball) and vertex (cut off on the cylinder where the electron's ends are closer than the same length) obey the Ward-Takahashi identity exactly for every gauge parameter and mass, so a Ward-preserving pair exists at one loop without the imported existence statement, the remaining freedom being $\delta m$ and $Z_{2} = Z_{1}$; in logarithmic form the identity requires $\ln(M_{\Sigma}^{2}/M_{V}^{2}) = 1/2$; transport-absent.
