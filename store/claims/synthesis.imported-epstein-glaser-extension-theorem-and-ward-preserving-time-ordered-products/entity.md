---
id: synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products
kind: claim
version: 2
title: 'Imported: Epstein-Glaser extension and Ward-preserving time-ordered products'
status: imported
region: synthesis
subject: quantum-fields
tags: [gauge-fields, scattering-amplitudes, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-02
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Fable 5.2
  role: 'new clause (vi): the scaling-degree rules (SD1) to (SD4)'
  version: 2
  source: maintainer pass of 2026-11-10
review: draft
imported_from:
- citation: 'H. Epstein and V. Glaser, The role of locality in perturbation theory, Ann. Inst. H. Poincare A 19 (1973), no. 3, 211--295.'
  key: EpsteinGlaser1973
- citation: 'R. Brunetti and K. Fredenhagen, Microlocal analysis and interacting quantum field theories: renormalization on physical backgrounds, Commun. Math. Phys. 208 (2000), 623--661; arXiv:math-ph/9903028.'
  key: BrunettiFredenhagen2000
  locator: 'Sec. 5.2, Thm. 5.2 (scaling degree below the dimension: unique extension of the same degree) and Thm. 5.3 (finite scaling degree at least the dimension: extensions of the same degree exist; the ambiguity, terms P(d)delta supported at the point, in the proof and the discussion around it)'
  doi: 10.1007/s002200050004
- citation: 'G. Scharf, Finite Quantum Electrodynamics: The Causal Approach, 2nd ed., Springer, Berlin (1995).'
  key: Scharf1995
  locator: 'ch. 3 (the method of Epstein and Glaser, splitting of causal distributions, application to QED); sec. 4.6 (gauge invariance and Ward identities); sec. 5.3 (axial anomalies)'
  doi: 10.1007/978-3-642-57750-5
- citation: 'D. R. Grigore, Gauge invariance of the quantum electrodynamics in the causal approach to renormalization theory, arXiv:hep-th/9911214.'
  key: Grigore1999
  locator: 'introduction: a reformulated proof of gauge invariance of QED to all orders in the Epstein-Glaser approach, noting that an earlier proof relies on reduction formulae for one-particle reducible graphs'
- citation: 'M. Duetsch and K. Fredenhagen, A local (perturbative) construction of observables in gauge theories: the example of QED, Commun. Math. Phys. 203 (1999), 71--105; arXiv:hep-th/9807078.'
  key: DutschFredenhagen1999
  doi: 10.1007/s002200050606
- citation: 'S. Hollands, Renormalized quantum Yang-Mills fields in curved spacetime, Rev. Math. Phys. 20 (2008), 1033--1172; arXiv:0705.3340.'
  key: Hollands2008
  doi: 10.1142/S0129055X08003420
- citation: 'O. Steinmann, Perturbation Expansions in Axiomatic Field Theory, Lecture Notes in Physics 11, Springer, Berlin (1971).'
  key: Steinmann1971
  locator: 'the scaling degree of a distribution at a point; cited from memory, not read'
extraction:
  note: >-
    Imported so that the results which renormalise without a regulator, by extension of distributions across
    coincident points, and the results which use causal perturbation theory for interacting fields can pin these
    sources instead of citing them from memory. Checked on 2026-11-02: Epstein and Glaser, bibliographic data
    (title, journal, volume 19 no. 3, pages 211-295, 1973) against the Numdam record; Brunetti and Fredenhagen, the
    arXiv abstract (a purely local version of the Stueckelberg-Bogoliubov-Epstein-Glaser method, extension of
    distributions) and the statements and numbering of Thms. 5.2 and 5.3 against the arXiv text; that text states the
    ambiguity of Thm. 5.3 through the values on chosen test functions, the form as a sum of derivatives of delta up to
    order sd - n appearing in the proof and its discussion; Scharf, title, edition, year and publisher against the
    Springer record and the chapter and section titles (3.1 to 3.13, 4.6 Gauge invariance and Ward identities, 5.3
    Axial anomalies) against a library table of contents (the edition of that record not confirmed); Grigore, the
    arXiv abstract and introduction, which credits the earlier all-orders treatment of gauge invariance in QED and
    says its proof relies on reduction formulae for one-particle reducible graphs whose rigorous proof seems absent,
    and gives a reformulated proof; Duetsch and Fredenhagen, the arXiv abstract (interacting fields as formal power
    series in the local algebras without the adiabatic limit, the BRST transformation as a graded derivation
    implemented by a local Kugo-Ojima operator, stability of the Hilbert space structure, all assumptions verified in
    QED) and DOI; Hollands, the arXiv abstract (renormalised perturbative Yang-Mills on any globally hyperbolic
    background, Ward identities at the renormalised level keeping the interacting BRST current conserved and the
    BRST charge nilpotent, observables as the BRST cohomology) and DOI. Not checked against the sources: the
    journal page ranges of Brunetti-Fredenhagen, Duetsch-Fredenhagen and Hollands (from memory), the content of
    Epstein and Glaser beyond the title, the theorem-level statements of Scharf sec. 4.6, and the section numbers of
    Duetsch-Fredenhagen and Hollands cited by the causal spin-statistics result.
    Clause (vi), added in version 2 (10 November 2026, by decision 1 of 9 November 2026): the four rules (SD1) to
    (SD4) that the one-loop kernel result on a gravitational field
    (synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four)
    listed as the inputs of its degree count. NOT checked against the sources: the four rules, their attribution
    (Steinmann for the scaling degree; Brunetti and Fredenhagen 2000 for its calculus and for products of Feynman
    parametrices on a gravitational field; the Hadamard parametrix literature for (SD4)) and Steinmann's
    bibliographic data are cited from memory. (SD1) to (SD3) are rules about the scaling degree; (SD4) is a
    regularity statement about the Hadamard form that lets (SD2) be applied to a remainder, kept here with them
    because they are used together. Clause (vi) does not import the first Hadamard transport equation, the
    protraction identity of the curvature operator or local covariance with scaling; the last is the separate Fact
    synthesis.imported-local-covariance-with-scaling-of-time-ordered-products.
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Created by the maintainer pass of 2026-11-02 (the Epstein-Glaser, Brunetti-Fredenhagen, Scharf, Hollands 2008 and Duetsch-Fredenhagen 1999 extension Fact, by Leon''s list of routine imports), shared by the regulator-free vacuum polarisation and the causal spin-statistics result.'
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 1 -> 2, by decision 1 of 9 November 2026: new clause (vi), the scaling-degree rules (SD1) to (SD4), cited from memory, so that the degree count of the one-loop kernel on a gravitational field can cite them as a Fact. Clauses (i) to (v) assert what they asserted.'
---

## formal
Signature $(+,-,-,-)$, units $\hbar = c = 1$; free fields on flat spacetime, Wick polynomials of them, and a local interaction density $\mathcal{L}$ smeared with a test function $g$.
\begin{enumerate}
\item[(i)] \emph{(Causal perturbation theory.)} The time-ordered products $T_{n}$ of Wick polynomials are constructed by induction on $n$ from causal factorisation ($T_{n}$ factorises into lower products when the points are causally ordered); at each order $T_{n}$ is fixed by the lower orders away from the total diagonal, and the only freedom is its extension across the diagonal, which can be chosen Poincar\'e covariant; the S-matrix and the interacting fields (Bogoliubov's formula) are formal power series in $g$ built from the $T_{n}$, with no ultraviolet regulator \cite{EpsteinGlaser1973}.
\item[(ii)] \emph{(Extension by scaling degree.)} Let $t_{0}$ be a distribution on $\R^{n}\setminus\{0\}$ of scaling degree $\mathrm{sd}$ at the origin. If $\mathrm{sd} < n$ there is a unique extension $t$ to $\R^{n}$ with the same scaling degree. If $n \le \mathrm{sd} < \infty$, extensions with the same scaling degree exist, and two of them differ by $\sum_{|a| \le \omega}c_{a}\partial^{a}\delta$, $\omega = \mathrm{sd} - n$ \cite{BrunettiFredenhagen2000}. The same holds locally on any globally hyperbolic gravitational field, the scaling degree being read in local coordinates.
\item[(iii)] \emph{(Ward-preserving time-ordered products in electrodynamics.)} In quantum electrodynamics with the covariant (Gupta-Bleuler) photon the extensions of (i) can be normalised at every order so that perturbative gauge invariance holds; it implies the Ward identities, in particular the Ward-Takahashi identity of the vertex and the self-energy and the transversality of the vacuum polarisation \cite{Scharf1995, Grigore1999}.
\item[(iv)] \emph{(Local construction and BRST structure in electrodynamics.)} The interacting fields of (i) generate local algebras without the adiabatic limit; for electrodynamics the BRST transformation is a graded derivation of the interacting field algebra, implemented by a local Kugo-Ojima operator, and the positive Hilbert space structure of the physical states of the free theory is stable under the perturbation \cite{DutschFredenhagen1999}.
\item[(v)] \emph{(Yang-Mills.)} Perturbative Yang-Mills theory with ghosts and antifields is renormalisable on every globally hyperbolic gravitational field, flat spacetime included, with Ward identities at the renormalised level that keep the interacting BRST current conserved and the interacting BRST charge nilpotent; the physical observables are the BRST cohomology \cite{Hollands2008}.
\item[(vi)] \emph{(Scaling-degree rules; cited from memory, not checked.)} On a geodesically convex neighbourhood of a gravitational field as in (ii), with $\sigma$ the Synge function and $\sigma_{F}$ its boundary value with the Feynman prescription:
\begin{enumerate}
\item[(SD1)] the Feynman boundary value $\sigma_{F}^{-k}(\log\sigma_{F})^{j}$ has scaling degree $2k$ at the diagonal, in the relative normal coordinate for a fixed point;
\item[(SD2)] multiplication by a smooth function vanishing to order $j$ on the diagonal lowers the scaling degree by at least $j$;
\item[(SD3)] the scaling degree is subadditive under the products that occur: for two kernels with the same Feynman prescription, whose product is defined off the diagonal, the degree of the product is at most the sum of the degrees;
\item[(SD4)] the Hadamard form holds at higher order: after $N$ terms of the Hadamard series the remainder is of class $C^{N}$, so that (SD2) applies to the remainder.
\end{enumerate}
\cite{Steinmann1971} for the scaling degree; \cite{BrunettiFredenhagen2000} for its calculus and for products of Feynman parametrices; (SD4) is the Hadamard parametrix construction at higher order.
\end{enumerate}

## technical
Causal perturbation theory, due to Epstein and Glaser, builds the time-ordered products of an interacting quantum field theory order by order from causality alone. At each order the product is already determined away from the points where all arguments coincide; the ultraviolet problem is only how to extend a distribution across that set, and no regulator is introduced. Brunetti and Fredenhagen put the extension step in a local form ordered by the scaling degree: a distribution of scaling degree below the dimension has one extension of the same degree, and at or above the dimension extensions exist and differ by finitely many derivatives of the delta function, the local counterterms. For electrodynamics Scharf showed in this framework that the free normalisation can be chosen so that gauge invariance, and with it the Ward identities, hold at every order (a later proof by Grigore repairs a step that rests on reduction formulae). Duetsch and Fredenhagen constructed the local algebras of interacting fields and implemented the BRST symmetry of electrodynamics by a local Kugo-Ojima operator, with the positivity of the physical states preserved. Hollands extended the construction to Yang-Mills theory on any globally hyperbolic gravitational field, with Ward identities that keep the interacting BRST charge nilpotent. Clause (vi) records the rules by which the scaling degree of a one-loop kernel on a gravitational field is counted: an inverse power of the Synge function with the Feynman prescription has twice that power as its degree, a smooth factor vanishing on the diagonal lowers the degree by its order of vanishing, degrees add at most under the products that occur, and the Hadamard series can be cut after any number of terms with a remainder as differentiable as the number of terms kept. These four are cited from memory.

## lay
The infinities of quantum field theory can be avoided without any artificial cut-off. Epstein and Glaser showed that the calculation can be built up step by step from the requirement that cause precedes effect; the only freedom left at each step is how to treat the points where particles meet, and that freedom is a short list of constants. Later work showed that this freedom can be used to keep the conservation of electric charge exact at every step, constructed the local quantities of the theory directly, and extended the construction to the force fields of the strong and weak interactions, on flat spacetime and in gravitational fields. The series takes these results from the literature.

## one-liner
Causal perturbation theory (Epstein-Glaser): time-ordered products fixed off the diagonal, extension by scaling degree unique below the dimension and ambiguous by derivatives of delta up to order sd minus the dimension above it (Brunetti-Fredenhagen Thms. 5.2, 5.3); Ward-preserving normalisation in electrodynamics (Scharf; Grigore); local interacting fields and BRST for QED (Duetsch-Fredenhagen 1999); renormalised Yang-Mills with a nilpotent interacting BRST charge (Hollands 2008); scaling-degree rules (SD1) to (SD4) for Feynman parametrices on a gravitational field (cited from memory).
