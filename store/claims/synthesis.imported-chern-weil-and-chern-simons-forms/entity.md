---
id: synthesis.imported-chern-weil-and-chern-simons-forms
kind: claim
version: 1
title: 'Imported: invariant polynomials of a field strength are closed and locally exact, the exterior derivative of a Chern-Simons (transgression) form, so they have no field equations; the Chern-Simons form changes under gauge transformations by an exact form (Chern-Weil; Chern and Simons)'
status: imported
region: synthesis
subject: einstein
tags: [gauge-fields, curvature-and-field-equations, classical-theorem]
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
- citation: 'S.-S. Chern and J. Simons, Characteristic forms and geometric invariants, Ann. of Math. (2) 99 (1974), 48--69.'
  key: ChernSimons1974
  doi: 10.2307/1971013
- citation: 'S. Kobayashi and K. Nomizu, Foundations of Differential Geometry, Vol. II, Interscience, New York (1969).'
  key: KobayashiNomizu1969
  locator: 'Ch. XII'
extraction:
  note: >-
    Imported for the results that call a density topological because it is a Chern-Weil form, and
    for the results that use the transgression and gauge variation of Chern-Simons forms (the
    curvature-only classification of tractor actions, the Weyl-square identity on transport, the
    five-dimensional Chern-Simons reduction, and the edge term of the Euler entropy). Checked on
    2026-10-31: the bibliographic data of Chern and Simons 1974 (title, journal, series, volume,
    issue, pages, DOI) against the encyclopedia article on Chern-Simons forms, which also states that
    the integral of the Chern-Simons form is gauge invariant modulo an integer; the statement that a
    closed Pontryagin-type form is the exterior derivative of a locally defined Chern-Simons form, and
    the three-dimensional gauge variation by an exact form, against Zanelli's lecture notes,
    arXiv:hep-th/0502193 (his Eqs. (73), (74) and (80)). The general transgression formula of (b), the
    variation formula of (a) and the locator in Kobayashi and Nomizu are cited from memory, not checked
    against the source.
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created at Leon''s decision of 2026-10-31 approving the import of Chern and Simons 1974 for the gravitational-action results; partly verified (see note).'
  flags:
  - 'beyond one flat chart: the integral winding of a gauge transformation over a closed manifold'
---

## formal
Let $A$ be a connection (a gauge field, a one-form) on an $n$-dimensional region with values in a Lie algebra $\mathfrak{g}$ of bivectors, with field strength $F = dA + A \times A$ in the convention of the citing result ($\times$ the commutator product of the values, wedged as forms), and let $P$ be a symmetric $k$-linear form on $\mathfrak{g}$ invariant under $\mathfrak{g}$ (an invariant polynomial). Write $P(F^{k})$ for the $2k$-form $P(F \wedge \cdots \wedge F)$.
\begin{enumerate}
\item[(a)] (Chern-Weil.) $d\,P(F^{k}) = k\,P(DF \wedge F^{k-1}) = 0$ by the Bianchi identity $DF = 0$; for a variation $\delta A$, $\delta P(F^{k}) = k\,d\,P(\delta A \wedge F^{k-1})$, so with $2k = n$ the integral of $P(F^{k})$ has identically vanishing Euler-Lagrange derivative (it is a topological density, with no field equations).
\item[(b)] (Transgression.) For two connections $A_{0}$, $A_{1}$ with values in $\mathfrak{g}$, put $A_{t} = A_{0} + t(A_{1} - A_{0})$ with field strength $F_{t}$; then $P(F_{1}^{k}) - P(F_{0}^{k}) = d\,\bigl(k\int_{0}^{1}P((A_{1} - A_{0}) \wedge F_{t}^{k-1})\,dt\bigr)$. With $A_{0} = 0$ this is $P(F^{k}) = d\,\mathrm{CS}_{P}(A)$, the Chern-Simons form $\mathrm{CS}_{P}(A) = k\int_{0}^{1}P(A \wedge F_{t}^{k-1})\,dt$, $F_{t} = t\,dA + t^{2}A \times A$; so $P(F^{k})$ is locally exact.
\item[(c)] (Variation and gauge change.) $\delta\,\mathrm{CS}_{P}(A) = k\,P(\delta A \wedge F^{k-1})$ up to an exact form, so the field equations of $\int\mathrm{CS}_{P}$ in odd dimension $2k - 1$ are $P(J \wedge F^{k-1}) = 0$ for every $J$ in $\mathfrak{g}$. Under a gauge transformation $\mathrm{CS}_{P}$ changes by an exact form plus a closed form whose integral over a closed manifold is a topological (winding) number; under an infinitesimal one, $\delta_{\lambda}A = D\lambda$, it changes by an exact form.
\end{enumerate}
\emph{Beyond one flat chart.} The winding in (c) is the degree of a gauge transformation over a closed manifold, read on several charts of flat spacetime glued by gauge transformations; (a), (b) and the infinitesimal clause of (c) are local.

\emph{Provenance:} \cite{ChernSimons1974}; Chern-Weil theory as in \cite[Ch.~XII]{KobayashiNomizu1969}.

## technical
For any gauge field, the invariant polynomials of its field strength (traces of powers, Pfaffians, the Killing form) are closed forms by the Bianchi identity, and their variation is a total derivative, so integrated over a region of matching dimension they give no field equations: they are topological. Chern and Simons showed that each such form is locally the exterior derivative of a form built from the gauge field itself, the Chern-Simons form, obtained by integrating along the straight line of connections from zero (transgression); its variation gives the field equations of Chern-Simons theory in odd dimensions, and under a gauge transformation it changes by a total derivative plus a winding term whose integral is topological. Taken from the literature; the field strength's sign and normalisation follow the citing result.

## lay
Some combinations of a force field's strength never change when the field is deformed a little: their total over a region depends only on the field at the edge, or on the shape of space. Chern and Simons showed how to write each of them as the change of another quantity built from the field, which in odd dimensions becomes an action of its own. These are classical theorems taken from the literature.

## one-liner
For a gauge field with field strength $F$ and an invariant polynomial $P$, $P(F^{k})$ is closed with no field equations and locally $d\,\mathrm{CS}_{P}(A)$, $\mathrm{CS}_{P}(A) = k\int_{0}^{1}P(A \wedge F_{t}^{k-1})\,dt$, whose variation is $kP(\delta A \wedge F^{k-1})$ up to exact forms (Chern-Weil; Chern and Simons 1974).
