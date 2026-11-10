---
id: synthesis.imported-local-covariance-with-scaling-of-time-ordered-products
kind: claim
version: 2
title: 'Imported: local covariance with scaling of time-ordered products (Hollands-Wald)'
status: imported
region: synthesis
subject: quantum-fields
tags: [gauge-fields, classical-theorem, needs-continuum]
proposed_by:
  kind: ai
  session: maintainer-2026-11-10
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: maintainer pass of 2026-11-10
- name: Claude Fable 5.2
  role: 'sourcing corrected after a web check: scalar-field scope stated in the clauses, the regularity requirement worded as the source has it, the Dirac-field literature added at the level verified'
  version: 2
  source: maintainer pass of 2026-11-10
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'S. Hollands and R. M. Wald, Local Wick polynomials and time ordered products of quantum fields in curved spacetime, Commun. Math. Phys. 223 (2001), 289--326; arXiv:gr-qc/0103074.'
  key: HollandsWald2001
  locator: 'the requirements of locality and covariance, scaling, continuous and analytic dependence on the metric, and the uniqueness theorem for Wick polynomials and time-ordered products up to finitely many parameters; abstract and the first 100 000 characters of the arXiv text checked on the web on 10 November 2026 (restricted to a real scalar field; existence of the time-ordered products deferred); section and theorem numbers, journal volume and pages not verified'
  doi: 10.1007/s002200100540
- citation: 'S. Hollands and R. M. Wald, Existence of local covariant time ordered products of quantum fields in curved spacetime, Commun. Math. Phys. 231 (2002), 309--345; arXiv:gr-qc/0111108.'
  key: HollandsWald2002
  locator: 'existence of local and covariant time-ordered products for a free scalar field, with a scaling expansion about the total diagonal in polynomials of the curvature times Lorentz-invariant distributions; abstract checked on the web on 10 November 2026; journal volume and pages not verified'
  doi: 10.1007/s00220-002-0719-y
- citation: 'R. Brunetti and K. Fredenhagen, Microlocal analysis and interacting quantum field theories: renormalization on physical backgrounds, Commun. Math. Phys. 208 (2000), 623--661; arXiv:math-ph/9903028.'
  key: BrunettiFredenhagen2000
  locator: 'the microlocal setting: time-ordered products on a globally hyperbolic background by extension of distributions ordered by the scaling degree'
  doi: 10.1007/s002200050004
- citation: 'J. Zahn, The renormalized locally covariant Dirac field; arXiv:1210.4031.'
  key: Zahn2012
  locator: 'the locally covariant Dirac field charged under a gauge group in gauge and Yukawa background fields: renormalised Wick powers and time-ordered products, the current and the stress-energy tensor conserved, the remaining ambiguity characterised; abstract only, checked on the web on 10 November 2026; journal data not verified'
  doi: 10.1142/S0129055X13300124
- citation: 'J. Zahn, Locally covariant charged fields and background independence; arXiv:1311.7661.'
  key: Zahn2013
  locator: 'perturbative agreement (a perturbative form of independence of the gauge background) for the charged Dirac field; abstract only, checked on the web on 10 November 2026; journal data not verified'
  doi: 10.1142/S0129055X15500178
extraction:
  maintainer_pass_2026_11_10_sourcing:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 1 -> 2, sourcing. Checked on the web on 10 November 2026: the two papers of Hollands and Wald (arXiv abstract pages, and the first 100 000 characters of the text of the first) and the abstracts of two papers of J. Zahn on the Dirac field. Changes: the clauses now say that the sources treat a real scalar field, that the first paper proves uniqueness and defers the existence of the time-ordered products to the second, and that the regularity requirement is continuity under smooth variations of the metric together with analytic dependence under analytic ones (version 1 said smooth dependence); the two Zahn papers are added as the literature for the Dirac field at the level verified (abstracts), without a claim that they give the clauses in the form used here on a gravitational field. No existence statement is added: the Ward identity on a gravitational field and the existence of a transverse extension stay outside this Fact. Where the note below says nothing was checked against the sources, this note holds.'
  note: >-
    Imported, by decision of 9 November 2026 (decision 1), so that results on one-loop kernels on a gravitational
    field can pin the input that reduces the freedom of an extension from coefficient functions to constants,
    instead of citing it from memory. Clause (iii) is the form the curved-field one-loop kernel result names in
    its clause (iv). NOT checked against the sources: the statement, the bibliographic data (volumes, pages,
    arXiv numbers) and the attribution of each clause are cited from memory; only the data of Brunetti and
    Fredenhagen 2000 were checked, on 2 November 2026, for the Fact
    synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products, which holds the
    scaling-degree rules and the extension theorem this Fact is used with. Scope caveats. The sources prove the
    statement for the Wick polynomials and time-ordered products of a real scalar field; the same structure for
    the Dirac field and its current is the literature's later extension and is taken here as part of the import,
    the less well sourced part of it. The sources state the scaling for a constant rescaling of the metric with
    the parameters of the field rescaled by their dimensions, and their coefficients are polynomial in the squared
    mass of the scalar field; the form with the mass of the Dirac field rescaled inversely is the transcription
    used here. The sources also require a smooth, in a second form analytic, dependence on the field, which
    is what excludes coefficients that are not polynomial; it is included in clause (i). Not part of this Fact:
    the Ward identity on a gravitational field, the principle of perturbative agreement, the conservation of the
    stress tensor, and the values of any constant. Written in geometric algebra where the statement allows (the
    gravitational field as displacement and rotation gauge fields, the curvature operator); the analytic
    statements are in the sources' language.
  maintainer_pass:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Created by the maintainer pass of 10 November 2026, by decision 1 of 9 November 2026: local covariance with scaling of time-ordered products imported as a Fact, beside the scaling-degree rules added to the Epstein-Glaser Fact, so that the reduction of the extension freedom on a gravitational field to constants has a stored premise.'
outside_ga:
  kind: imported
  why: 'A theorem of quantum field theory on curved spacetime (existence and uniqueness of local and covariant time-ordered products with almost homogeneous scaling), taken from the literature; its analytic content (operator-valued distributions, wave front sets, extension across the diagonal) is stated in its source''s language.'
---

## formal
Units $\hbar = c = 1$. Let $(\hb, \Omega)$ be a gravitational field on four-dimensional flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric is smooth and globally hyperbolic, with curvature operator $\mathcal{R}$, and let the free fields on it be given with their Wick polynomials defined by subtraction of the Hadamard parametrix. For $\lambda > 0$ write $(\hb, \Omega)_{\lambda}$ for the field obtained by the constant rescaling of the displacement gauge field that multiplies the derived metric by $\lambda^{2}$, and $m \mapsto m/\lambda$ for the accompanying rescaling of the mass. The sources treat a real scalar field; the statement was written from memory and then compared with the sources at the level given under provenance:
\begin{enumerate}
\item[(i)] \emph{(Existence.)} Time-ordered products $T_{n}$ of Wick polynomials exist on every such field with the following properties. \emph{Locality and covariance:} $T_{n}$ on a region is a functional of the field on that region only, and an isometric embedding of one field into another that preserves the causal structure, the orientations and the spin structure carries the products of the first to those of the second. \emph{Scaling:} under $(\hb, \Omega) \mapsto (\hb, \Omega)_{\lambda}$, $m \mapsto m/\lambda$, each $T_{n}$ is multiplied by the power of $\lambda$ given by the engineering dimensions of its arguments, up to a polynomial in $\log\lambda$ whose coefficients are products of lower order with local terms (almost homogeneous scaling). \emph{Regularity:} the products obey the microlocal spectrum condition, vary continuously under smooth variations of the metric, and depend analytically on it along analytic families (the source requires both: continuity alone does not exclude local curvature terms that are not analytic). Together with causal factorisation, symmetry, unitarity and the commutation relations with the free field \cite{HollandsWald2001, HollandsWald2002}; the microlocal construction by extension of distributions is that of \cite{BrunettiFredenhagen2000}. The first source proves the existence of the local Wick polynomials and defers that of the time-ordered products to the second, which proves it for a free scalar field.
\item[(ii)] \emph{(Uniqueness.)} Two prescriptions with the properties of (i) differ, at each order, by terms supported on the total diagonal that are themselves local and covariant functionals of the field with almost homogeneous scaling: sums of covariant derivatives of the delta function whose coefficients are polynomials, with constant real coefficients, in the curvature operator, its covariant derivatives and the mass, each term of the engineering dimension fixed by the scaling. The freedom at each order is therefore a finite list of constants, the same on every field \cite{HollandsWald2001}.
\item[(iii)] \emph{(The form used in the store.)} For a kernel of degree of divergence $\omega$ (Fact \claimref{synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products}(ii)), the extension across the diagonal can be chosen as a local and covariant functional of the field that scales almost homogeneously under the constant rescaling of the displacement gauge field with the mass rescaled inversely; and in the difference of two such extensions the coefficient of a derivative of $\delta$ of order $j \leq \omega$ is a polynomial in the curvature operator, its covariant derivatives and the mass, of dimension $\omega - j$ (the curvature operator of dimension $2$, each covariant derivative and the mass of dimension $1$), with constant coefficients. For $\omega = 2$ the dimension is $2 - j$.
\end{enumerate}
The sources prove (i) and (ii) for a real scalar field (the first states the restriction, the second's abstract says a free scalar field). For the Dirac field charged under a gauge group, in gauge and Yukawa background fields, renormalised Wick powers and time-ordered products are constructed in \cite{Zahn2012}, with the current and the stress-energy tensor conserved and the remaining ambiguity characterised, and perturbative agreement for the charged Dirac field is shown in \cite{Zahn2013}; both were read at the level of the abstract only, and whether they give (i) to (iii) in the form used here, for the current of the Dirac field on a gravitational field, was not verified. That use is therefore taken with the import and is its less well sourced part. Not part of this Fact: the Ward identity on a gravitational field, the existence of a transverse extension there, and the value of any constant. \emph{Provenance:} \cite{HollandsWald2001} (abstract and the first part of the arXiv text checked on the web on 10 November 2026: the restriction to a real scalar field, uniqueness up to finitely many parameters, the continuity and analyticity requirements, scaling with the metric and the squared mass rescaled together, existence of the time-ordered products deferred); \cite{HollandsWald2002} (abstract checked); \cite{BrunettiFredenhagen2000} for the microlocal setting; \cite{Zahn2012}, \cite{Zahn2013} (abstracts checked). Section and theorem numbers are not given because they were not verified.

## technical
On flat spacetime the freedom in extending a one-loop kernel across coincident points is a short list of constants, because translation and Lorentz covariance force the coefficients of the delta-function terms to be constant invariant tensors. On a gravitational field there is no such symmetry, and the extension theorem alone leaves the coefficients free functions of the point. Hollands and Wald replaced the missing symmetry by two requirements. The construction must be local and covariant: it may use only the field in a neighbourhood of the points, and it must be the same construction on every field, so that the coefficients are built from the curvature operator and its derivatives at the point. And it must scale almost homogeneously when the displacement gauge field is rescaled by a constant with the mass rescaled inversely, so that each coefficient has a fixed dimension; analytic dependence on the field then makes it a polynomial (continuity alone would not). Curvature has dimension two and a mass dimension one, so a kernel of degree of divergence two allows a constant in front of the second derivatives of delta and, without derivatives, terms linear in the curvature operator and quadratic in the mass, each with a constant coefficient. They proved that time-ordered products with these properties exist and that any two differ in this way. The sources treat a scalar field; the store uses the statement for the current of the Dirac field, which is the less well sourced part of the import: the literature for the Dirac field (Zahn 2012, 2013, in gauge and Yukawa background fields) was read at the level of the abstracts only. The Ward identity on the field, which removes further constants, is not part of this Fact. The statement was written from memory and compared with the abstracts of the sources and the opening part of the first paper; theorem numbers were not verified.

## lay
Quantum field theory leaves a small amount of freedom at the points where particles meet: on flat spacetime, a few constants. In a gravitational field the same mathematics would allow those constants to vary from place to place in an arbitrary way. Hollands and Wald showed around 2001 that two natural demands remove this: the rule must be built only from the field near the point, in the same way everywhere, and it must behave correctly when all lengths are rescaled together. Then the freedom is again a few constants, multiplying expressions made from the curvature. The collection takes this from the literature. The original papers prove it for the simplest kind of field, not for the electron's; the statement was compared with the summaries of the papers and the opening part of the first, not with their proofs.

## one-liner
Time-ordered products on a globally hyperbolic gravitational field exist as local and covariant functionals of the field with almost homogeneous scaling, and two such prescriptions differ by derivatives of delta whose coefficients are constant-coefficient polynomials in the curvature operator, its derivatives and the mass of the dimension fixed by scaling, so the extension freedom is a finite list of constants (Hollands and Wald 2001, 2002, proved for a real scalar field; Brunetti and Fredenhagen 2000 for the microlocal setting; for the Dirac field Zahn 2012, 2013, abstracts only; compared with the sources at abstract level).
