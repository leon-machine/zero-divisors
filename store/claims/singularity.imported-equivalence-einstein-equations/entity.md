---
id: singularity.imported-equivalence-einstein-equations
kind: claim
version: 3
title: 'Imported: equivalence with the Einstein equations'
status: imported
region: singularity
subject: einstein
tags: [classical-theorem, curvature-and-field-equations]
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
  role: 'GA rewrite (curvature correspondence stated for the curvature operator)'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
review: typed
imported_from:
- citation: A. Lasenby, C. Doran and S. Gull, Gravity, gauge theories and geometric algebra, Phil. Trans.
    R. Soc. Lond. A 356 (1998), 487--582.
  key: LDG1998
  locator: \S 4 (\S 4.3, covariant forms of the field equations), App.~C
- citation: C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003).
  key: DoranLasenby2003
  locator: Ch.~13-14
locators:
  paper: T05
  number: Fact 2.1
  label: fact:gtgequiv
  line: 1322
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The curvature clause is stated for the GTG curvature operator B -> R(B) on physical bivectors, with the Riemann components R_{mu nu}^{rho sigma} (contraction with the reciprocal frame planes) as a labelled reading; the source''s form, the previous formal level, is in source_formal; the equivalence and the curvature correspondence are unchanged; status imported.'
  source_formal: |-
    On any region where $\hb$ is invertible, the GTG field equations \eqref{eq:gtgfield} for $(\hb, \Omega)$ are equivalent to the Einstein field equations for the metric \eqref{eq:metricdef}; in vacuum, to Ricci-flatness of $g$. Moreover the curvatures correspond, not only the equations: on the invertible region the GTG curvature bivector $\mathcal{R}(B)$, evaluated on the coordinate planes $g_\mu \wedge g_\nu$ of the frame $g_\mu = \hb^{-1}(e_\mu)$ and contracted with the reciprocal planes, reproduces the Riemann tensor $R_{\mu\nu}{}^{\rho\sigma}$ of $g$, so the curvature operator on bivectors, its spectrum, its eigenplanes and its scalar invariants are the same objects in the two pictures. \emph{Provenance:} Lasenby, Doran and Gull \cite[\S 4.3 and App.~C]{LDG1998}; textbook form, including the dictionary between $\mathcal{R}(B)$ and the Riemann tensor, \cite[Ch.~13-14]{DoranLasenby2003}. It is the second clause that licenses the assembly of Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling}'s spectrum from the two formalisms.
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Locator corrected from \S 7 (which is "Electromagnetism in a gravitational background") to \S 4, the field equations and their covariant forms (Sec. 4.3, Covariant forms of the field equations), and Appendix C, the translation of tensor calculus; section titles checked against arXiv:gr-qc/0405033 on 2026-10-23.'
  env: fact
  context_refs:
  - singularity.curvature-gauge-field-exact-shape-decoupling
  eqrefs: 2
  typing:
    by: ai-typing-pass
    note: 'imported fact with no derivation; its reference to the shape-decoupling theorem records what it licenses, not a premise'
---

## formal
On any region where $\hb$ is invertible, the GTG field equations \eqref{eq:gtgfield} for $(\hb, \Omega)$ are equivalent to the Einstein field equations for the metric \eqref{eq:metricdef}; in vacuum, to Ricci-flatness of $g$. Moreover the curvatures correspond, not only the equations: on the invertible region the GTG curvature operator $B \mapsto \mathcal{R}(B)$ on physical bivectors is the curvature of $g$ (in components: $\mathcal{R}(g_\mu \wedge g_\nu)$, on the coordinate planes of the frame $g_\mu = \hb^{-1}(e_\mu)$ and contracted with the reciprocal planes $g^\rho \wedge g^\sigma$, is the Riemann tensor $R_{\mu\nu}{}^{\rho\sigma}$ of $g$), so the curvature operator on bivectors, its spectrum, its eigenplanes and its scalar invariants are the same objects in the two pictures. \emph{Provenance:} Lasenby, Doran and Gull \cite[\S 4.3 and App.~C]{LDG1998}; textbook form, including the dictionary between $\mathcal{R}(B)$ and the Riemann tensor, \cite[Ch.~13-14]{DoranLasenby2003}. It is the second clause that licenses the assembly of Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling}'s spectrum from the two formalisms.

## technical
On any region where $\hb$ is invertible, the gauge-theory field equations for $(\hb, \Omega)$ are equivalent to the Einstein field equations for the induced metric, and in vacuum to Ricci-flatness of $g$. The correspondence extends to curvature: the gauge-theory curvature operator $\mathcal{R}(B)$ on physical bivectors is the curvature of $g$, its values on the frame planes $g_\mu \wedge g_\nu$, $g_\mu = \hb^{-1}(e_\mu)$, giving the Riemann components of $g$.

So the curvature operator on bivectors, its spectrum, eigenplanes and scalar invariants are the same objects in both pictures, which is what allows a curvature spectrum to be assembled from computations in the two formalisms. The result is imported from the literature on gauge-theory gravity.

## lay
Gravity can be described either as the curvature of spacetime, as in Einstein's theory, or as a gauge theory on flat spacetime written in geometric algebra. This imported result says that wherever the gauge field is invertible the two descriptions have equivalent field equations and the same curvature. Curvature calculations can therefore be done in either language and combined.

## one-liner
Where $\hb$ is invertible, gauge-theory gravity is equivalent to the Einstein equations and its curvature operator $\mathcal{R}(B)$ is the curvature of the derived metric.
