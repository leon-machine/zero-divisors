---
id: synthesis.imported-chern-gauss-bonnet
kind: claim
version: 3
title: 'Imported: the Gauss-Bonnet-Chern theorem in two and four dimensions'
status: imported
region: synthesis
subject: einstein
tags: [curvature-and-field-equations, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-22
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
- citation: 'S.-S. Chern, A simple intrinsic proof of the Gauss-Bonnet formula for closed Riemannian manifolds, Ann. of Math. (2) 45 (1944), 747--752.'
  key: Chern1944
  doi: 10.2307/1969302
- citation: 'C. B. Allendoerfer and A. Weil, The Gauss-Bonnet theorem for Riemannian polyhedra, Trans. Amer. Math. Soc. 53 (1943), 101--129.'
  key: AllendoerferWeil1943
- citation: 'M. P. do Carmo, Differential Geometry of Curves and Surfaces, Prentice-Hall, Englewood Cliffs (1976).'
  key: doCarmo1976
  locator: 'Sec. 4-5'
extraction:
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 2 -> 3. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  note: >-
    Imported for the results that evaluate Euler-density integrals of horizon cross-sections and of
    closed Einstein instantons. Chern 1944 (title, journal, volume, pages) was checked against the
    Celebratio Mathematica bibliography of Chern; the other two references and the DOI are cited
    from memory, not checked against the source. The four-dimensional normalisation 32 pi^2 is the
    one the citing results confirm on the round four-sphere, the product of two-spheres and the
    complex projective plane.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Created by the maintainer pass so that the results citing the Chern-Gauss-Bonnet theorem from memory can pin it; partly verified (see note).'
  flags:
  - 'beyond one flat chart: Euler characteristic of the closed four-manifold'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated for Gauge Theory Gravity: (a) is read natively for a closed spacelike two-surface in the invertible region of a gravitational field on flat spacetime, such as a horizon cross-section, with its induced metric; (b) is stated with the Euler density written also in multivector form (DICTIONARY section 13) and flagged beyond one flat chart, since the Euler characteristic of a closed four-manifold is global. The abstract statements (a) and (b) are kept unchanged. Fix (referee GR1, 2026-10-23): in (a) the surface carries the Riemannian metric -h, h the negative-definite metric the (+,-,-,-) derived metric induces, so that int K dA = 2 pi chi keeps its sign.'
---

## formal
Let $\chi$ denote the Euler characteristic.
\begin{enumerate}
\item[(a)] (Two dimensions.) For a closed (compact, boundaryless) Riemannian surface $\Sigma$ with Gaussian curvature $K$ and scalar curvature ${}^{(2)}\!R = 2K$, $\int_{\Sigma}K\,dA = 2\pi\chi(\Sigma)$, so $\int_{\Sigma}{}^{(2)}\!R\,dA = 4\pi\chi(\Sigma)$. In particular this holds for a closed spacelike two-surface lying in the invertible region of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), such as a cross-section of a horizon locus, with the Riemannian metric $-h$, where $h$ is the (negative-definite) metric that the derived metric, of signature $(+,-,-,-)$, induces.
\item[(b)] (Four dimensions.) For a closed Riemannian four-manifold $M$,
\[
\int_{M}\bigl(R_{abcd}R^{abcd} - 4R_{ab}R^{ab} + R^{2}\bigr)\,dV \;=\; 32\pi^{2}\chi(M).
\]
The integrand is the Euler density of the curvature operator $\mathcal{R}$ on bivectors, $E = 2\langle\mathcal{R}(a \wedge b)\,\mathcal{R}(\partial_{b} \wedge \partial_{a})\rangle - 4\,\mathcal{R}(\partial_{a}) \cdot \mathcal{R}(a) + \mathcal{R}^{2}$, independent of the sign convention of $\mathcal{R}$.
\end{enumerate}
\emph{Provenance:} \cite{Chern1944, AllendoerferWeil1943}; the two-dimensional case is classical \cite[Sec.~4-5]{doCarmo1976}.

\emph{Beyond one flat chart.} The Euler characteristic of the closed four-manifold in (b) is global and is not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the Euler density above is in Gauge Theory Gravity on the invertible region, where its integral is a boundary term, and the Euler characteristic is read on the manifold assembled from the derived metric's charts.

## technical
The Gauss-Bonnet-Chern theorem expresses the Euler characteristic of a closed Riemannian manifold as the integral of a curvature density. For a closed surface the total Gaussian curvature is $2\pi\chi$, so the integral of the scalar curvature $2K$ is $4\pi\chi$; for a closed four-manifold the integral of the Euler density $R_{abcd}R^{abcd} - 4R_{ab}R^{ab} + R^{2}$, a quadratic expression in the curvature operator on bivectors, is $32\pi^{2}\chi$. In particular the integral does not change under any deformation of the metric. The two-dimensional case applies directly to a closed horizon cross-section of a gravitational field on flat spacetime. The four-dimensional Euler characteristic is global: no single gravitational field on flat spacetime carries it, so that part is read on several charts of flat spacetime (charts of Euclidean $\R^{4}$), each carrying its own gravitational field, glued on overlaps by displacement and rotation gauge transformations.

## lay
However a closed surface is bent or stretched, its total curvature stays the same, fixed by how many holes it has: a sphere always gives the same total, a doughnut always zero. Chern proved the analogue in higher dimensions, where a particular combination of curvatures integrates to a number fixed by the overall shape of the space. These are classical theorems of geometry taken from the literature.

## one-liner
On a closed surface $\int K\,dA = 2\pi\chi$; on a closed Riemannian four-manifold $\int(R_{abcd}R^{abcd} - 4R_{ab}R^{ab} + R^{2})\,dV = 32\pi^{2}\chi$.
