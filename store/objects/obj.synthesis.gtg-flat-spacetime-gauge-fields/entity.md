---
id: obj.synthesis.gtg-flat-spacetime-gauge-fields
kind: object
version: 3
title: 'Gauge Theory Gravity: the gravitational field on flat spacetime'
status: defined
region: synthesis
subject: einstein
tags: [gauge-fields, curvature-and-field-equations, dictionaries]
proposed_by:
  kind: ai
  session: maintainer-2026-10-23-gtg
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: A. Lasenby, C. Doran and S. Gull, Gravity, gauge theories and geometric algebra, Phil. Trans.
    R. Soc. Lond. A 356 (1998), 487--582.
  key: LDG1998
  locator: \S\S 3--4, eqs.~(3.9), (3.18), (3.26), (3.31), (3.33), (3.35)--(3.36), (3.72)--(3.74), (4.1)--(4.4), (4.9), (4.11)--(4.13), (4.21), (4.36)--(4.40)
- citation: C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003).
  key: DoranLasenby2003
  locator: \S\S~13.4--13.6
- citation: A. N. Lasenby, Geometric algebra, gravity and gravitational waves, Adv. Appl. Clifford Algebras (2019).
  key: Lasenby2019
  doi: 10.1007/s00006-019-0991-y
  locator: \S\S~4--5 (arXiv:1912.05960)
extraction:
  maintainer_pass_2026_11_01:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 2 -> 3, at Leon''s decision of 2026-11-01: a marked note records that the definition already makes the Einstein-Cartan spin choice (Omega an independent gauge field, vanishing torsion a field equation for spinless matter, spin sourcing torsion otherwise), citing the result that on the frozen-point field space the independence of Omega decides exactly the torsion equation. Checked on 2026-11-01 against the arXiv text of Lasenby, Doran and Gull (gr-qc/0405033, read through a text-extraction tool): Section 4 takes h and Omega as the independent dynamical variables; Section 4.2 derives the Omega-equation, gives the torsion sourced by the Dirac spin trivector (eq. 4.37) and identifies D ^ h(a) with the torsion of the Einstein-Cartan-Sciama-Kibble theory; Section 4.3 sets the spin to zero for the paper''s applications (eq. 4.40); the introduction names spin-torsion theories Einstein-Cartan-Kibble-Sciama theories. The paper does not use the words Palatini or first-order. The definition itself is unchanged.'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'd-dimensional clause added by Leons decision of 2026-10-23 to extend GTG to d dimensions: same fields on Cl(p,q), d-dimensional Schouten and Weyl coefficients, store-sign de Sitter_d; the construction of Lasenby, Doran and Gull uses nothing four-dimensional except the pseudoscalar duality and the Dirac sector; exact identities in d = 3, 5, 6 and signature (2,3) checked (run folder verify/d_dimensional_identities.py).'
  note: >-
    The definition the store's gravity-facing results are stated against: the background is flat
    spacetime with its fixed product, gravity is the pair of gauge fields (hb, Omega), curvature is
    the field strength, and the metric is a derived reading. Conventions follow Lasenby, Doran and
    Gull 1998, with one notational difference fixed here: the series' hb is the map that paper writes
    with an underbar (its g_mu = h^{-1}(e_mu), eqs. 3.35-3.36), and the paper's overbar h is the
    series' adjoint hb^T. Confirmed on the stored Schwarzschild field: the series' hb(a) = a - beta
    (a.e_t) e_r is the adjoint of the Newtonian-gauge field a - beta (a.e_r) e_t of Lasenby 2019,
    Sec. 5, and hb^{-1}.hb^{-1} returns the Painleve-Gullstrand line element. Equation numbers of
    Lasenby, Doran and Gull 1998 were checked against the arXiv text (gr-qc/0405033) on 2026-10-23;
    Lasenby 2019 Secs. 4-5 were checked against arXiv:1912.05960; the Doran-Lasenby section titles
    against the publisher's table of contents. The torsion equation and the rotation law of hb are written
    in the series' convention (the paper's overbar laws transposed); the setting note of T05 is
    brought to the same convention in its version 2. The curvature operator is
    defined with the store's existing curvature convention (stated in
    synthesis.einstein-condition-is-infinity-vacuum-incidence, clause 7: de Sitter has Ric = Lambda g
    in signature (+,-,-,-)), which the T05 and T06 curvature spectra follow; it is the negative of
    the covariant field strength of Lasenby, Doran and Gull. Checked on the stored Schwarzschild
    connection: their sign gives the radial eigenvalue -2M/r^3, the store's +2M/r^3.
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Created so that results restated in Gauge Theory Gravity can point at one definition of the flat background, the gauge fields, the field strength and the derived metric.'
---

## formal
Let $V$ be the vector space of $\Cl(1,3)$, with its fixed product $a \cdot b$, $Q(a) = a^{2}$, signature $(+,-,-,-)$: \emph{flat spacetime}. Points are labelled by the position vector $x$; $\{e_\mu\}$ is a background frame with reciprocal $\{e^\mu\}$, and $\nabla = e^\mu \partial_\mu$ is the flat vector derivative. A \emph{gravitational field} on an open region of flat spacetime is a pair $(\hb, \Omega)$ of gauge fields:
\begin{enumerate}
\item[(i)] the \emph{position-gauge field} $\hb$, a position-dependent linear map of $V$, extended to multivectors as an outermorphism, with adjoint $\hb^{T}$ defined by $a \cdot \hb^{T}(b) = \hb(a) \cdot b$;
\item[(ii)] the \emph{rotation-gauge field} $\Omega$, a position-dependent linear map from vectors to bivectors.
\end{enumerate}
Its \emph{invertible region} is $U = \{x : \det \hb(x) \neq 0\}$. On $U$:
\begin{enumerate}
\item[(a)] \emph{Physical vectors.} The physical vector over a background vector $a$ is $\hb^{-1}(a)$; the frame and coframe are $g_\mu = \hb^{-1}(e_\mu)$ and $g^\mu = \hb^{T}(e^\mu)$, with $g_\mu \cdot g^\nu = \delta_\mu^\nu$. Physical vectors are compared with the flat product.
\item[(b)] \emph{Covariant derivative.} $D_a M = a \cdot \nabla M + \Omega(a) \times M$ on multivector fields, with $A \times B = \tfrac12(AB - BA)$, and $D_a \psi = a \cdot \nabla \psi + \tfrac12 \Omega(a)\psi$ on spinor fields. Along a physical vector $A$ the derivative is $A \cdot D = D_{\hb(A)}$, and the covariant vector derivative is $D = \hb^{T}(\partial_a) D_a$.
\item[(c)] \emph{Field strength.} $R(a \wedge b) = a \cdot \nabla\,\Omega(b) - b \cdot \nabla\,\Omega(a) + \Omega(a) \times \Omega(b)$, so that $[D_a, D_b]M = R(a \wedge b) \times M$. The \emph{curvature operator} is the linear map on physical bivectors $\mathcal{R}(B) = -R(\hb(B))$, the negative of the covariant field strength $R(\hb(B))$ of \cite{LDG1998}, so that the store's curvature convention holds (below); its contractions are $\mathcal{R}(b) = \partial_a \cdot \mathcal{R}(a \wedge b)$, $\mathcal{R} = \partial_a \cdot \mathcal{R}(a)$, and $\mathcal{G}(a) = \mathcal{R}(a) - \tfrac12 a\,\mathcal{R}$, the derivatives $\partial_a$ taken with respect to the physical argument.
\item[(d)] \emph{Derived metric.} $g(a, b) = \hb^{-1}(a) \cdot \hb^{-1}(b)$ for background vectors $a, b$, so $g_{\mu\nu} = g_\mu \cdot g_\nu$ and the line element is $ds^{2} = Q(\hb^{-1}(dx))$. It is a reading of $\hb$, not a structure of the background.
\item[(e)] \emph{Gauge freedoms.} For a rotor field $U$: $\hb(a) \mapsto \hb(\tilde U a U)$, equivalently $\hb^{T}(a) \mapsto U\,\hb^{T}(a)\,\tilde U$, so that physical vectors rotate, $\hb^{-1}(a) \mapsto U\,\hb^{-1}(a)\,\tilde U$; $\Omega(a) \mapsto U\,\Omega(a)\,\tilde U - 2\,(a \cdot \nabla U)\,\tilde U$, under which $\mathcal{R}(B) \mapsto U\,\mathcal{R}(\tilde U B U)\,\tilde U$. For a displacement $x \mapsto f(x)$ with differential $\underline{f}(a) = a \cdot \nabla f$: $\hb(a; x) \mapsto \underline{f}^{-1}\bigl(\hb(a; f(x))\bigr)$ and $\Omega(a; x) \mapsto \Omega(\underline{f}(a); f(x))$. The derived metric changes by the corresponding pullback and every scalar built from $\mathcal{R}$ is invariant.
\item[(f)] \emph{Field equations.} With matter stress-energy $T(a)$, a symmetric linear map on physical vectors, and cosmological constant $\Lambda$: $\mathcal{G}(a) + \Lambda a = -8\pi T(a)$, equivalently $\mathcal{R}(a) + 8\pi T(a) = (\Lambda + 4\pi\,\partial_a \cdot T(a))\,a$, and, for spinless matter, $D \wedge \hb^{T}(a) = \hb^{T}(\nabla \wedge a)$ (vanishing torsion, which fixes $\Omega$ from $\hb$).
\end{enumerate}
\emph{(d dimensions.)} The same definition on the vectors of $\Cl(p,q)$, $d = p + q \geq 3$, with the fixed product of flat $\R^{p,q}$ (the Lorentzian case $(1, d-1)$ in the sign $(+,-,\ldots,-)$), defines a gravitational field in $d$ dimensions: (a) to (f) are unchanged, the rotors being those of $\mathrm{Spin}(p,q)$, the field equation reading $\mathcal{G}(a) + \Lambda a = -8\pi G_{d}\,T(a)$, the torsion equation fixing $\Omega$ from $\hb$ as in four dimensions, and the Schouten map and Weyl curvature being $\Sch(a) = \bigl(\mathcal{R}(a) - \tfrac{a\,\mathcal{R}}{2(d-1)}\bigr)/(d-2)$ and $\mathcal{W}(a \wedge b) = \mathcal{R}(a \wedge b) - \Sch(a) \wedge b - a \wedge \Sch(b)$; de Sitter space has $\mathcal{R}(B) = \tfrac{2\Lambda}{(d-1)(d-2)}B$. The readings of Fact \claimref{synthesis.imported-gtg-dictionary} that do not use the pseudoscalar (clauses (i) to (iv) and (vi), and (v) with these coefficients) are the frame formalism and hold in every dimension; the duality $\mathcal{W}(IB) = I\mathcal{W}(B)$ is four-dimensional.

The sign of $\mathcal{R}$ is the store's curvature convention, in which de Sitter space of cosmological constant $\Lambda$ has $\mathcal{R}(B) = \tfrac{\Lambda}{3}B$ and $\mathcal{R}(a) = \Lambda a$, the Ricci map is minus that of the convention in which the round sphere has positive Ricci curvature (for a physical null vector $k$ the latter is $-k \cdot \mathcal{R}(k)$), and (f) is Einstein's equation; this is the one sign flip against the literature cited: Lasenby, Doran and Gull and \cite[Ch.~14]{DoranLasenby2003} write the curvature as $R(\hb(B))$ and the field equation as $\mathcal{G}(a) - \Lambda a = 8\pi T(a)$, and a result that uses their sign says so. \emph{Note (the spin choice).} Clause (f) makes the Einstein-Cartan choice for the spin part of the matter coupling: $\Omega$ is a gauge field independent of $\hb$ (clause (ii)), and vanishing torsion is a field equation that holds for spinless matter, not an identity of the definition. Lasenby, Doran and Gull take $\hb$ and $\Omega$ as independent dynamical variables; their $\Omega$-equation with minimally coupled Dirac matter gives a torsion sourced by the spin trivector, which they identify with the torsion of the Einstein-Cartan-Sciama-Kibble theory \cite[Section 4.2, eq.~(4.37)]{LDG1998}, and with vanishing spin it is the torsion equation of (f) \cite[eq.~(4.40)]{LDG1998}. On the field space of $\Cl(2,4)$ connections preserving the frozen point this independence decides exactly the torsion equation, not the frozen point (Theorem \claimref{synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation}(i)); the coupling with spin is Fact \claimref{synthesis.imported-einstein-cartan-matter-coupling}. The note records a reading of the definition; the definition is unchanged.

\emph{Provenance:} Lasenby, Doran and Gull \cite{LDG1998} (Sections 3 and 4), in the series' notation, in which $\hb$ is their underbarred map and their overbarred map is $\hb^{T}$; \cite[Sections 13.4--13.6]{DoranLasenby2003}; \cite[Sections 4--5]{Lasenby2019}.

## technical
Gauge Theory Gravity describes gravity on flat spacetime, the vectors of $\Cl(1,3)$ with their fixed product and signature $(+,-,-,-)$. A gravitational field is a pair of gauge fields: the position-gauge field $\hb$, a position-dependent linear map on vectors, and the rotation-gauge field $\Omega(a)$, a bivector for each direction $a$. Where $\hb$ is invertible, the physical vector over a background vector $a$ is $\hb^{-1}(a)$, and the frame vectors are $g_\mu = \hb^{-1}(e_\mu)$.

The covariant derivative is $D_a M = a \cdot \nabla M + \Omega(a) \times M$. Its commutator gives the field strength $R(a \wedge b) = a \cdot \nabla\,\Omega(b) - b \cdot \nabla\,\Omega(a) + \Omega(a) \times \Omega(b)$, and the curvature operator $\mathcal{R}(B) = -R(\hb(B))$ plays the part of the Riemann tensor, with the sign of the store's curvature convention (de Sitter space has $\mathcal{R}(B) = \tfrac{\Lambda}{3}B$), opposite to the gauge-theory literature's. Contracting once and twice gives the Ricci map $\mathcal{R}(b)$ and the scalar $\mathcal{R}$, and the field equations are $\mathcal{G}(a) + \Lambda a = -8\pi T(a)$ together with vanishing torsion for spinless matter. Since $\Omega$ is independent and the torsion equation is a field equation, spinning matter sources torsion: the definition makes the Einstein-Cartan choice for the spin coupling. The metric $g(a,b) = \hb^{-1}(a) \cdot \hb^{-1}(b)$ is a derived reading of $\hb$. The theory is invariant under local rotations, which rotate $\hb$ and shift $\Omega$ by a pure-gauge term, and under displacements of the background, which act by pullback. The series' $\hb$ is the map written with an underbar in Lasenby, Doran and Gull's 1998 paper, which fixes its conventions.

## lay
In this formulation of gravity there is no curved spacetime. Spacetime is flat and fixed, and gravity is carried by two fields defined on it: one tells how directions and distances measured by physical clocks and rulers relate to the fixed background, and the other tells how local frames turn from point to point. What would be called the curvature of spacetime is the strength of the second field, just as a magnetic field is the strength of the electromagnetic potential. The usual geometric description, with its metric, can always be read off from these fields wherever the first one can be inverted.

## one-liner
A gravitational field is a pair of gauge fields $(\hb, \Omega)$ on flat spacetime; $D_a = a \cdot \nabla + \Omega(a)\times$, the curvature is the field strength, $\mathcal{R}(B) = -R(\hb(B))$ in the store's sign, and the metric $g(a,b) = \hb^{-1}(a) \cdot \hb^{-1}(b)$ is derived.
