---
id: synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form
kind: claim
version: 1
title: 'Imported: conformal gravity, its Bach equations and conformal gauge form'
status: imported
region: synthesis
subject: einstein
tags: [conformal-model, curvature-and-field-equations, gauge-fields, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-31
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
imported_from:
- citation: 'R. Bach, Zur Weylschen Relativitaetstheorie und der Weylschen Erweiterung des Kruemmungstensorbegriffs, Math. Z. 9 (1921), 110--135.'
  key: Bach1921
- citation: 'M. Kaku, P. K. Townsend and P. van Nieuwenhuizen, Gauge theory of the conformal and superconformal group, Phys. Lett. B 69 (1977), 304--308.'
  key: KakuTownsendVanNieuwenhuizen1977
extraction:
  note: >-
    Imported for the identification of the frozen-point integrand on transport with conformal gravity
    and for the order bound in the inversion of the Clausius route. Checked on 2026-10-31: Bach's title,
    journal, volume and first page against the encyclopedia article on the Bach tensor (which also
    states that it is trace-free and conformally invariant in four dimensions) and the bibliography of
    arXiv:1310.0526, whose text states that variation of the Weyl action gives the Bach equation;
    the title, journal, volume, pages and year of Kaku, Townsend and van Nieuwenhuizen against the
    bibliography of arXiv:2602.09664, whose introduction describes the paper as recognising conformal
    gravity as the gauge theory of the conformal group, with a Yang-Mills-like action. Cited from memory,
    not checked against the source: the last page of Bach 1921, the explicit form of the Bach tensor, the
    Bach-flatness of Einstein and conformally Einstein fields, and the form of the conventional
    constraints and of the epsilon-contracted action in (b).
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created at Leon''s decision of 2026-10-31 approving the import of Bach (Bach-flatness of Einstein fields in four dimensions) and Kaku-Townsend-van Nieuwenhuizen, merged into one Fact on conformal gravity; partly verified (see note).'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on four-dimensional flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with derived metric $g$ and Weyl map $\mathcal{W}$ of its field strength (index reading $W_{abcd}$, round-sphere-positive convention).
\begin{enumerate}
\item[(a)] (Bach.) The functional $\int W_{abcd}W^{abcd}\,\mathrm{vol}$ is invariant under constant and local rescalings of the metric in four dimensions, and its Euler-Lagrange expression under variation of $g$ is a constant multiple of the Bach tensor, in index reading $B_{ab} = \nabla^{c}\nabla^{d}W_{acbd} + \tfrac12 R^{cd}W_{acbd}$, symmetric, trace-free and of fourth order in $g$. $B$ vanishes on every Einstein field ($\Ric$ a multiple of $g$, any $\Lambda$), and, since it is conformally covariant, on every field conformal to an Einstein field; the converse fails.
\item[(b)] (Kaku, Townsend and van Nieuwenhuizen.) Four-dimensional conformal gravity is the gauge theory of the conformal group (in the series, the bivectors of $\Cl(2,4)$): for a conformal gauge field with the conventional constraints (zero torsion, and the special-conformal part solved algebraically in terms of the curvature, the Schouten tensor), the functional formed as the $\epsilon$-contracted square of the Lorentz block of the conformal field strength is, up to a constant factor and a topological term, the Weyl-squared functional of (a).
\end{enumerate}
\emph{Provenance:} \cite{Bach1921} for (a); \cite{KakuTownsendVanNieuwenhuizen1977} for (b).

## technical
Conformal (Weyl) gravity takes as action the integral of the square of the Weyl tensor, the part of the curvature that is unchanged by local rescalings of lengths. Bach found its field equations: they involve four derivatives of the metric, and every solution of Einstein's equations in four dimensions solves them, whatever the cosmological constant, as does every metric conformal to one; they have further solutions. Kaku, Townsend and van Nieuwenhuizen obtained the same action as a gauge theory of the conformal group: with the torsion set to zero and the special-conformal gauge field expressed through the curvature, the alternating square of the conformal field strength is the Weyl square. In the series the conformal group acts on $\Cl(2,4)$ and its gauge field is the tractor gauge field. Taken from the literature.

## lay
Einstein's theory is not the only possible law of gravity. One alternative, Weyl gravity, cares only about the shape of spacetime and not its size; Bach worked out its equations, which are more complicated than Einstein's but are satisfied by every solution of Einstein's. Later physicists showed that it is exactly what one gets by treating the symmetries of shape-preserving maps as a force field. These are results taken from the literature.

## one-liner
The four-dimensional Weyl-squared functional has the fourth-order Bach equations, solved by every Einstein field and every field conformal to one (Bach 1921), and it is the conformal-group gauge theory with the conventional constraints (Kaku, Townsend and van Nieuwenhuizen 1977).
