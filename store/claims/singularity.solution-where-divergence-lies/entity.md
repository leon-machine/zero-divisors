---
id: singularity.solution-where-divergence-lies
kind: claim
version: 4
title: The solution, and where the divergence lies
status: proved
region: singularity
subject: singularity
tags: [schwarzschild, curvature-and-field-equations]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, notation of the displayed curvature named (background field strength, LDG sign) against the store curvature operator'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - singularity.connection-bivector-computed@4
  - singularity.imported-equivalence-einstein-equations@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:2.4
- kind: check
  ref: check.py::check_radial_curvature_from_gauge_field
- kind: check
  ref: check.py::check_vacuum_curvature_spectrum
- kind: check
  ref: check.py::check_gauge_field_unimodular
locators:
  paper: T05
  number: Prop 2.4
  label: prop:solution
  line: 1379
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the radial curvature 2M/r^3 from Omega alone, the full vacuum spectrum and Ricci contraction from the PG gauge fields, and det hb = 1 with the (t,r) block determinant -1. Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  env: proposition
  context_refs:
  - singularity.curvature-gauge-field-exact-shape-decoupling
  - singularity.degeneration-exactly
  eqrefs: 4
  typing:
    by: ai-typing-pass
    note: "Did not add the shape theorem or the degeneration proposition from the context references: the first is a forward reference and the second a comparison."
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. Notation clarification, values unchanged: clause (1) writes the script letter, the store''s macro for the curvature operator calR(B) = -R(hb(B)), for the background field strength R(a wedge b) in LDG sign, as the setting note does (dictionary C5); a sentence at the formal and technical levels now says so and gives both eigenvalues, -2M/r^3 (LDG) and +2M/r^3 (store), on sigma_r = e_r e_t = -(d_t wedge d_r). the computation recorded: in lib/GA.py (Cl(1,3)), sigma_r = e_r e_t = -(e_t wedge e_r) with sigma_r^2 = 1, hb(e_t) wedge hb(e_r) = e_t wedge e_r for hb(a) = a - beta (a.e_t) e_r, and with the background field strength R(e_t wedge e_r) = (2M/r^3) sigma_r (the displayed value, commutator term zero) the LDG-sign eigenvalue on that plane is -2M/r^3 and the store sign gives calR(sigma_r) = -R(hb(sigma_r)) = +(2M/r^3) sigma_r, checked at M = 1, r = 2; the orientation sigma_r = e_r e_t is the one docs/gtg-dictionary.md C6 and C10 record for singularity.connection-bivector-computed.'
---

## formal
The pair $(\hb, \Omega)$ of \eqref{eq:hbar} and Proposition \claimref{singularity.connection-bivector-computed} solves the vacuum field equations \eqref{eq:gtgfield} at every $r > 0$, and the divergence of the classical description resides in $\Omega$ and in the curvature, not in $\hb$:
\begin{enumerate}
\item (The radial curvature, from the gauge field alone.) On the radial plane both connection values are multiples of the single bivector $\sigma_r$, so the commutator term of the field strength \eqref{eq:gtgdyn} vanishes identically and nothing depends on $t$; hence, in two lines,
\[
\mathcal{R}(\partial_t \wedge \partial_r)
\;=\; \partial_t\,\Omega(\partial_r) - \partial_r\,\Omega(\partial_t) + \Omega(\partial_t)\times\Omega(\partial_r)
\;=\; -\,\partial_r\Bigl(\frac{M}{r^2}\Bigr)\sigma_r
\;=\; \frac{2M}{r^3}\,\sigma_r :
\]
the radial plane is an eigenplane of the curvature with eigenvalue of magnitude $2M/r^3$, derived without leaving the gauge formalism. In this display, as in the paper, the script letter is the background field strength $R(a\wedge b) = a\cdot\nabla\Omega(b) - b\cdot\nabla\Omega(a) + \Omega(a)\times\Omega(b)$ in Lasenby, Doran and Gull's sign (Fact \claimref{synthesis.imported-gtg-dictionary}); with $\sigma_r = \er\et = -\partial_t\wedge\partial_r$, the orientation of Proposition \claimref{singularity.connection-bivector-computed}, its eigenvalue on the radial plane is $-2M/r^3$, and the store's curvature operator $-R(\hb(B))$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}; the radial plane is $\hb$-invariant) has eigenvalue $+2M/r^3$ there, as in Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling}.
\item (Vacuum.) The full curvature operator is diagonal on the six frame planes with eigenvalues of magnitudes $(2M/r^3, M/r^3, M/r^3, M/r^3, M/r^3, 2M/r^3)$ and vanishing Ricci contraction: the mixed and angular planes are computed in Appendix \ref{app:curvature} in the static chart, where the computation is shortest, and the two pictures agree on the invertible region by Fact \claimref{singularity.imported-equivalence-einstein-equations}. The shape this spectrum assembles into is Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling}'s task.
\item (Unimodularity.) $\det \hb = 1$ exactly, at every radius, horizon included: $P$ is rank-one nilpotent, so $1 - \beta P$ is unipotent as a matrix. Likewise the $(t,r)$ block of the metric \eqref{eq:metricdef} has determinant $-1$ at every radius. Nothing determinant-like degenerates at any $r > 0$: at finite radius the classical field is a volume-preserving shear, and the entire divergence of the approach is carried by the connection (Proposition \claimref{singularity.connection-bivector-computed}(3)) and by the curvature, both of which diverge, and by the metric components themselves, which diverge without a rescaled limit unless one is taken exactly as in Proposition \claimref{singularity.degeneration-exactly}.
\end{enumerate}

## technical
The pair $(\hb, \Omega)$ solves the vacuum field equations at every $r > 0$. On the radial plane both connection values are multiples of $\sigma_r$, so the commutator term of the field strength vanishes and $\mathcal{R}(\partial_t \wedge \partial_r) = -\partial_r(M/r^2)\,\sigma_r = (2M/r^3)\,\sigma_r$: an eigenplane with eigenvalue of magnitude $2M/r^3$, obtained within the gauge formalism (the display is the background field strength in Lasenby, Doran and Gull's sign: with $\sigma_r = \er\et = -\partial_t\wedge\partial_r$ its radial eigenvalue is $-2M/r^3$, the store's curvature operator $-R(\hb(B))$ having $+2M/r^3$). The full curvature operator is diagonal on the six frame planes with eigenvalue magnitudes $(2M/r^3, M/r^3, M/r^3, M/r^3, M/r^3, 2M/r^3)$ and vanishing Ricci contraction, the remaining planes being computed in the static chart and carried over by the imported equivalence with the Einstein equations on the invertible region.

Meanwhile $\det \hb = 1$ at every radius, horizon included, because $1 - \beta P$ is unipotent for the rank-one nilpotent $P$, and the $(t,r)$ block of the metric has determinant $-1$. So at finite radius the classical field is a volume-preserving shear, and the divergence of the description is carried by the connection, the curvature and the metric components, not by $\hb$.

## lay
The gravitational field of a non-rotating black hole is written here in a gauge-theory language with two ingredients: a field describing how lengths are stretched, and a connection describing how directions turn. The first ingredient stays well behaved at every distance from the centre and never squeezes or expands volume. All of the blow-up as the centre is approached lives in the connection, in the curvature built from it, and in the ordinary metric components.

## one-liner
The gauge-theory Schwarzschild solution satisfies the vacuum equations at every $r > 0$ with $\det \hb = 1$ throughout, so its divergence lies in the connection and the curvature, not in $\hb$.
