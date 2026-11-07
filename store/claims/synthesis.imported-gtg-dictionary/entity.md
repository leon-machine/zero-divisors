---
id: synthesis.imported-gtg-dictionary
kind: claim
version: 2
title: 'Imported: the dictionary between Gauge Theory Gravity and curved-spacetime language'
status: imported
region: synthesis
subject: einstein
tags: [gauge-fields, curvature-and-field-equations, dictionaries, classical-theorem]
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
- name: Claude Opus 5.5
  role: 'GA rewrite (component forms marked as readings)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: A. Lasenby, C. Doran and S. Gull, Gravity, gauge theories and geometric algebra, Phil. Trans.
    R. Soc. Lond. A 356 (1998), 487--582.
  key: LDG1998
  locator: \S\S 3.5, 4.3--4.4, 5.1--5.2, App.~C
- citation: C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003).
  key: DoranLasenby2003
  locator: \S\S~13.5--13.6, 14.1
- citation: A. N. Lasenby, Geometric algebra, gravity and gravitational waves, Adv. Appl. Clifford Algebras (2019).
  key: Lasenby2019
  doi: 10.1007/s00006-019-0991-y
  locator: \S\S~4--5, eq.~(8.5) (arXiv:1912.05960)
- citation: R. M. Wald, General Relativity, University of Chicago Press (1984).
  key: Wald1984
  locator: \S~12.5
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The Levi-Civita and curvature clauses state the GTG objects first (D_{e_mu} A, the curvature operator R(B), the Ricci and Einstein maps) with the components nabla_mu A^nu, Gamma^rho_{mu nu}, R_{mu nu}^{rho sigma}, R_{mu nu} as labelled readings; the previous formal level is kept as source_formal; declared outside_ga (bridge), since the Fact is the translation table between the two languages; the content is unchanged; status imported. Reader fix (R03): clause (iv) gives the frame-plane reading R(g_mu ^ g_nu) = -R(e_mu ^ e_nu) in the store''s sign instead of the tautology R(hb(g_mu ^ g_nu)) = R(e_mu ^ e_nu), naming the sources'' opposite sign.'
  source_formal: |-
    Let $(\hb, \Omega)$ be a gravitational field on flat spacetime with invertible region $U$ and derived metric $g$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with frame $g_\mu = \hb^{-1}(e_\mu)$ and coframe $g^\mu = \hb^{T}(e^\mu)$. On $U$, with $\Omega$ the torsion-free field of $\hb$:
    \begin{enumerate}
    \item[(i)] \emph{Vectors.} The tangent vectors of $(U, g)$ at $x$ are the physical vectors $\hb^{-1}(a)$, and $g(a,b) = \hb^{-1}(a) \cdot \hb^{-1}(b)$. A background vector $a$ is null, timelike or spacelike for $g$ exactly when $Q(\hb^{-1}(a))$ is zero, positive or negative; the light cone of $g$ at $x$ is the image under $\hb$ of the null cone of the flat product. The components of a physical vector field $A$ are $A^\mu = g^\mu \cdot A$, and an orthonormal frame of $g$ is any orthonormal set $\{\gamma_a\}$ of $\Cl(1,3)$, with tetrad components $\gamma^a \cdot g_\mu$.
    \item[(ii)] \emph{Levi-Civita derivative and parallel transport.} For a physical vector field $A$, $\nabla_\mu A^\nu = g^\nu \cdot D_{e_\mu} A$, and the Christoffel symbols are $\Gamma^\rho{}_{\mu\nu} = g^\rho \cdot D_{e_\mu} g_\nu$. Parallel transport along a curve $x(\lambda)$ is $D_{x'} M = 0$; it is solved by $M(\lambda) = U M(0) \tilde U$ with $dU/d\lambda = -\tfrac12\Omega(x')U$, $U(0) = 1$, a rotor, so it preserves the flat product of physical vectors.
    \item[(iii)] \emph{Geodesics.} A curve $x(\tau)$ is an affinely parametrised timelike (null) geodesic of $g$ exactly when $v = \hb^{-1}(x')$ satisfies $D_{x'}v = 0$, that is $dv/d\tau = -\Omega(x') \cdot v$, with $Q(v) = 1$ ($Q(v) = 0$).
    \item[(iv)] \emph{Curvature.} The Riemann tensor of $g$ is the covariant field strength: $R(\hb(g_\mu \wedge g_\nu)) = R(e_\mu \wedge e_\nu)$, contracted with the reciprocal planes, gives $R_{\mu\nu}{}^{\rho\sigma}$ (Fact \claimref{singularity.imported-equivalence-einstein-equations}), so the curvature operator on bivectors is $B \mapsto \mathcal{R}(B)$. The Ricci tensor is $R_{\mu\nu} = g_\mu \cdot \mathcal{R}(g_\nu)$ with $\mathcal{R}(b) = \partial_a \cdot \mathcal{R}(a \wedge b)$, the scalar curvature is $\mathcal{R} = \partial_a \cdot \mathcal{R}(a)$, and the Einstein tensor is $\mathcal{G}(a) = \mathcal{R}(a) - \tfrac12 a\,\mathcal{R}$; the GTG field equations are Einstein's equations for $g$ (Facts \claimref{singularity.imported-equivalence-einstein-equations} and \claimref{interior.imported-equivalence-einstein-equations}). In the store's sign of the definition, $\mathcal{R}(B) = -R(\hb(B))$, the Ricci curvature of the round-sphere-positive convention on a physical null vector $k$ is $-k \cdot \mathcal{R}(k)$, and de Sitter space has $\mathcal{R}(B) = \tfrac{\Lambda}{3}B$; the cited sources use $R(\hb(B))$.
    \item[(v)] \emph{Weyl and Schouten.} The Schouten tensor is $\Sch(a) = \tfrac12\bigl(\mathcal{R}(a) - \tfrac16 a\,\mathcal{R}\bigr)$, and the Weyl tensor is the trace-free part of the curvature,
    \[
    \mathcal{W}(a \wedge b) \;=\; \mathcal{R}(a \wedge b) - \Sch(a) \wedge b - a \wedge \Sch(b) \;=\; \mathcal{R}(a \wedge b) - \tfrac12\bigl(\mathcal{R}(a) \wedge b + a \wedge \mathcal{R}(b)\bigr) + \tfrac16\,\mathcal{R}\; a \wedge b ,
    \]
    with $\partial_a \cdot \mathcal{W}(a \wedge b) = 0$ and $\mathcal{W}(IB) = I\,\mathcal{W}(B)$, $I$ the pseudoscalar.
    \item[(vi)] \emph{Killing vectors and surface gravity.} A vector field $\xi = \xi^\mu \partial_\mu$ is a Killing field of $g$ exactly when the physical vector field $K = \xi^\mu g_\mu = \hb^{-1}(\xi^\mu e_\mu)$ makes $A \mapsto A \cdot D K$ antisymmetric for the flat product, $B \cdot (A \cdot D K) + A \cdot (B \cdot D K) = 0$; then $A \cdot D K = A \cdot F_K$ with the bivector $F_K = \tfrac12 D \wedge K$. On a Killing horizon, a locus where $Q(K) = 0$ and $K$ is normal, the surface gravity $\kappa$ is defined by $(K \cdot D)K = \kappa K$.
    \end{enumerate}
    \emph{Provenance:} Lasenby, Doran and Gull \cite{LDG1998} (Sections 3.5, 4.3, 4.4, 5.1, 5.2 and Appendix C, the translation of tensor calculus), in the series' notation; \cite[Sections 13.5, 13.6, 14.1]{DoranLasenby2003}; the Weyl formula as in \cite[eq.~(8.5)]{Lasenby2019}; the surface gravity as defined in \cite[Section 12.5]{Wald1984}.
  note: >-
    Imported so that results stated in metric language can be read, and restated, in Gauge Theory
    Gravity on flat spacetime without re-deriving the translation each time. The equivalence of the
    field equations and the Riemann clause are not repeated here: they are
    singularity.imported-equivalence-einstein-equations (with the curvature clause) and
    interior.imported-equivalence-einstein-equations, cited in (iv). What was checked, on
    2026-10-23: against the arXiv text of Lasenby, Doran and Gull 1998 (gr-qc/0405033), the frame
    and metric (eqs. 3.35-3.36), omega(a) = Omega(h(a)) and the covariant directional derivative
    (3.72)-(3.74), the commutator and field strength (4.1)-(4.4), the covariant Riemann (4.9), the
    contractions (4.11)-(4.13), and the section titles 3.5, 4.3, 4.4, 5.1, 5.2 and Appendix C (The
    translation of tensor calculus), whose contents lay beyond the text available and were not
    read; against arXiv:1912.05960 (Lasenby 2019), the Weyl formula (8.5), the vacuum equations and
    the Newtonian-gauge field of Sec. 5; against the publisher's table of contents, the
    Doran-Lasenby section titles. Clause (iii) is the standard reading of geodesics through the
    covariant derivative (1998 Sec. 4.4 by title). Clause (vi) is the coordinate-free Killing
    equation and Wald's definition of surface gravity (Sec. 12.5, cited from memory) read through
    clause (ii). The Schouten form in (v) and the equality of its two Weyl expressions, the
    surface gravity of the stored Painleve-Gullstrand connection, and the de Sitter sign of (iv)
    were checked in exact arithmetic with GA.py. The 2019 journal volume and article number were
    not checked. The 1998 paper writes the series' hb with an underbar (see the definition).
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Created as the translation table the gravity-facing results cite when restated in Gauge Theory Gravity.'
outside_ga:
  kind: bridge
  why: 'The Fact is the translation table between tensor calculus on the derived metric and Gauge Theory Gravity on flat spacetime: it states each GTG object and, as its labelled reading, the component form it translates (frame and tetrad components, Christoffel symbols, Riemann and Ricci components, the coordinate form of a Killing field).'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime with invertible region $U$ and derived metric $g$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), with frame $g_\mu = \hb^{-1}(e_\mu)$ and coframe $g^\mu = \hb^{T}(e^\mu)$. On $U$, with $\Omega$ the torsion-free field of $\hb$:
\begin{enumerate}
\item[(i)] \emph{Vectors.} The tangent vectors of $(U, g)$ at $x$ are the physical vectors $\hb^{-1}(a)$, and $g(a,b) = \hb^{-1}(a) \cdot \hb^{-1}(b)$. A background vector $a$ is null, timelike or spacelike for $g$ exactly when $Q(\hb^{-1}(a))$ is zero, positive or negative; the light cone of $g$ at $x$ is the image under $\hb$ of the null cone of the flat product. The components of a physical vector field $A$ are $A^\mu = g^\mu \cdot A$, and an orthonormal frame of $g$ is any orthonormal set $\{\gamma_a\}$ of $\Cl(1,3)$, with tetrad components $\gamma^a \cdot g_\mu$.
\item[(ii)] \emph{Levi-Civita derivative and parallel transport.} The Levi-Civita derivative of a physical vector field $A$ along $e_\mu$ is $D_{e_\mu} A$ (in components: $\nabla_\mu A^\nu = g^\nu \cdot D_{e_\mu} A$, and the Christoffel symbols are $\Gamma^\rho{}_{\mu\nu} = g^\rho \cdot D_{e_\mu} g_\nu$). Parallel transport along a curve $x(\lambda)$ is $D_{x'} M = 0$; it is solved by $M(\lambda) = U M(0) \tilde U$ with $dU/d\lambda = -\tfrac12\Omega(x')U$, $U(0) = 1$, a rotor, so it preserves the flat product of physical vectors.
\item[(iii)] \emph{Geodesics.} A curve $x(\tau)$ is an affinely parametrised timelike (null) geodesic of $g$ exactly when $v = \hb^{-1}(x')$ satisfies $D_{x'}v = 0$, that is $dv/d\tau = -\Omega(x') \cdot v$, with $Q(v) = 1$ ($Q(v) = 0$).
\item[(iv)] \emph{Curvature.} The curvature of $g$ is the covariant field strength: the curvature operator on physical bivectors is $B \mapsto \mathcal{R}(B)$ (in components: on the frame planes $\mathcal{R}(g_\mu \wedge g_\nu) = -R(e_\mu \wedge e_\nu)$, since $\hb(g_\mu \wedge g_\nu) = e_\mu \wedge e_\nu$, and contracted with the reciprocal planes it gives the Riemann tensor $R_{\mu\nu}{}^{\rho\sigma}$ of $g$ in the store's sign, the cited sources' $R(\hb(B))$ giving it in theirs; Fact \claimref{singularity.imported-equivalence-einstein-equations}). The Ricci map is $\mathcal{R}(b) = \partial_a \cdot \mathcal{R}(a \wedge b)$ (in components $R_{\mu\nu} = g_\mu \cdot \mathcal{R}(g_\nu)$), the scalar curvature is $\mathcal{R} = \partial_a \cdot \mathcal{R}(a)$, and the Einstein map is $\mathcal{G}(a) = \mathcal{R}(a) - \tfrac12 a\,\mathcal{R}$; the GTG field equations are Einstein's equations for $g$ (Facts \claimref{singularity.imported-equivalence-einstein-equations} and \claimref{interior.imported-equivalence-einstein-equations}). In the store's sign of the definition, $\mathcal{R}(B) = -R(\hb(B))$, the Ricci curvature of the round-sphere-positive convention on a physical null vector $k$ is $-k \cdot \mathcal{R}(k)$, and de Sitter space has $\mathcal{R}(B) = \tfrac{\Lambda}{3}B$; the cited sources use $R(\hb(B))$.
\item[(v)] \emph{Weyl and Schouten.} The Schouten tensor is $\Sch(a) = \tfrac12\bigl(\mathcal{R}(a) - \tfrac16 a\,\mathcal{R}\bigr)$, and the Weyl tensor is the trace-free part of the curvature,
\[
\mathcal{W}(a \wedge b) \;=\; \mathcal{R}(a \wedge b) - \Sch(a) \wedge b - a \wedge \Sch(b) \;=\; \mathcal{R}(a \wedge b) - \tfrac12\bigl(\mathcal{R}(a) \wedge b + a \wedge \mathcal{R}(b)\bigr) + \tfrac16\,\mathcal{R}\; a \wedge b ,
\]
with $\partial_a \cdot \mathcal{W}(a \wedge b) = 0$ and $\mathcal{W}(IB) = I\,\mathcal{W}(B)$, $I$ the pseudoscalar.
\item[(vi)] \emph{Killing vectors and surface gravity.} A vector field $\xi = \xi^\mu \partial_\mu$ is a Killing field of $g$ exactly when the physical vector field $K = \xi^\mu g_\mu = \hb^{-1}(\xi^\mu e_\mu)$ makes $A \mapsto A \cdot D K$ antisymmetric for the flat product, $B \cdot (A \cdot D K) + A \cdot (B \cdot D K) = 0$; then $A \cdot D K = A \cdot F_K$ with the bivector $F_K = \tfrac12 D \wedge K$. On a Killing horizon, a locus where $Q(K) = 0$ and $K$ is normal, the surface gravity $\kappa$ is defined by $(K \cdot D)K = \kappa K$.
\end{enumerate}
\emph{Provenance:} Lasenby, Doran and Gull \cite{LDG1998} (Sections 3.5, 4.3, 4.4, 5.1, 5.2 and Appendix C, the translation of tensor calculus), in the series' notation; \cite[Sections 13.5, 13.6, 14.1]{DoranLasenby2003}; the Weyl formula as in \cite[eq.~(8.5)]{Lasenby2019}; the surface gravity as defined in \cite[Section 12.5]{Wald1984}.

## technical
On the region where the position-gauge field $\hb$ is invertible, every notion of the curved-spacetime description has a counterpart in Gauge Theory Gravity on flat spacetime. Tangent vectors are the physical vectors $\hb^{-1}(a)$, and a background direction is null for the derived metric exactly when $Q(\hb^{-1}(a)) = 0$. The Levi-Civita derivative is the covariant derivative $D_a = a \cdot \nabla + \Omega(a)\times$ read in the frame $g_\mu = \hb^{-1}(e_\mu)$, parallel transport is a rotor, and a geodesic is a worldline whose velocity $\hb^{-1}(x')$ is $D$-parallel.

The Riemann tensor is the covariant field strength $\mathcal{R}(B)$; the Ricci tensor, scalar curvature and Einstein tensor are its contractions, and the field equations of the two descriptions agree (the imported equivalence Facts). The Schouten tensor is $\tfrac12(\mathcal{R}(a) - a\mathcal{R}/6)$ and the Weyl tensor is the trace-free part $\mathcal{W}$ of $\mathcal{R}$, linear over the pseudoscalar. A Killing field is a physical vector field whose covariant derivative is antisymmetric, and the surface gravity of a Killing horizon is defined by $(K \cdot D)K = \kappa K$. The table is imported from the gauge-theory-gravity literature, in the series' notation.

## lay
General relativity is usually written in the language of curved spacetime: metrics, geodesics, curvature tensors. Gauge Theory Gravity writes the same physics on a flat background, with gravity carried by two fields. This imported dictionary says how each geometric notion reads in the gauge-field language: which directions light can travel in, what it means to carry a direction along a path without turning it, what a free-fall path is, and which combinations of the field strength are the familiar curvature tensors. With it, any statement made in one language can be restated in the other.

## one-liner
On the invertible region, tangent vectors are $\hb^{-1}(a)$, the Levi-Civita derivative is $D_a$, geodesics have $D$-parallel velocity, and the Riemann, Ricci, Schouten and Weyl tensors and Killing fields are read from the field strength $\mathcal{R}(B)$ and $D$.
