---
id: synthesis.imported-five-dimensional-chern-simons-gravity
kind: claim
version: 1
title: 'Imported: five-dimensional Chern-Simons gravity, the Chern-Simons five-form of the cubic invariant of the conformal algebra, which split by a vector is the Lovelock combination with ratios $1 : \tfrac23\ell^{-2} : \tfrac15\ell^{-4}$ (Chamseddine)'
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
- citation: 'A. H. Chamseddine, Topological gauge theory of gravity in five and all odd dimensions, Phys. Lett. B 233 (1989), 291--294.'
  key: Chamseddine1989
- citation: 'A. H. Chamseddine, Topological gravity and supergravity in various dimensions, Nucl. Phys. B 346 (1990), 213--234.'
  key: Chamseddine1990
- citation: 'J. Zanelli, Lecture notes on Chern-Simons (super-)gravities, arXiv:hep-th/0502193 (second edition, 2008).'
  key: Zanelli2005
extraction:
  note: >-
    Imported for the reduction of five-dimensional Chern-Simons gravity along the frozen point. Checked
    on 2026-10-31: the titles, journals, volumes, pages and years of Chamseddine 1989 and 1990, the
    five-dimensional Chern-Simons form Tr(F^2 A - (1/2) F A^3 + (1/10) A^5) and the expanded action
    (k/8) eps_ABCDE((1/l) R R E + (2/(3 l^3)) R E E E + (1/(5 l^5)) E E E E E), whose ratios are those
    of (b), against arXiv:2203.05020 (its Eqs. (2.8) and (2.18) and its references [14], [16]); the
    general odd-dimensional form as a sum of Lovelock terms against Zanelli's lecture notes,
    arXiv:hep-th/0502193 (his Eqs. (51) and (102)). Cited from memory, not checked against the source: the
    statement of the field equations in (a) and the note on the reduction of Lovelock densities along a line.
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created at Leon''s decision of 2026-10-31 approving the import of Chamseddine''s five-dimensional Chern-Simons gravity, with the standard reduction of Lovelock densities along a line recorded as a note; partly verified (see note).'
---

## formal
Let $A$ be a gauge field on a five-dimensional region with values in the bivectors of a six-dimensional Clifford algebra ($\Cl(2,4)$, the anti-de Sitter case in five dimensions, or $\Cl(1,5)$), with field strength $F$, and let $P(F_{1}, F_{2}, F_{3})$ be the cubic invariant, the pseudoscalar part of $F_{1} \wedge F_{2} \wedge F_{3}$ (index reading $\epsilon_{ABCDEF}F_{1}^{AB}F_{2}^{CD}F_{3}^{EF}$).
\begin{enumerate}
\item[(a)] (The action.) Five-dimensional Chern-Simons gravity is $\kappa_{5}\int\mathrm{CS}_{5}(A)$, with $\mathrm{CS}_{5}$ the Chern-Simons form of $P$, $d\,\mathrm{CS}_{5}(A) = P(F, F, F)$, and constant $\kappa_{5}$ (the level). It needs no metric and no reduction datum, and is gauge invariant up to boundary terms; its field equations are $P(J, F, F) = 0$ for every bivector $J$.
\item[(b)] (The Lovelock form.) Splitting $A = \omega + E$ by a fixed vector $V$ of nonzero square, with $\omega$ in the stabiliser of $V$ (its curvature $R$) and $E = \theta \wedge V/Q(V)$ carrying the frame $\theta$, the Chern-Simons form is, up to exact forms and torsion terms, a constant times the combination of the five-dimensional Lovelock densities $\epsilon(R, R, \theta) + \tfrac23\ell^{-2}\epsilon(R, \theta, \theta, \theta) + \tfrac15\ell^{-4}\epsilon(\theta, \theta, \theta, \theta, \theta)$, with $\ell^{2} = |Q(V)|$ the (anti-)de Sitter radius (index reading $\epsilon_{abcde}(R^{ab}R^{cd}e^{e} + \tfrac23\ell^{-2}R^{ab}e^{c}e^{d}e^{e} + \tfrac15\ell^{-4}e^{a}e^{b}e^{c}e^{d}e^{e})$): the Euler (Gauss-Bonnet), Einstein-Hilbert and volume terms with ratios fixed by gauge invariance.
\end{enumerate}
\emph{Note (reduction along a line; standard, from the literature).} On a product of a four-dimensional region with a line, with the frame along the line a multiple of $dy$, each five-dimensional Lovelock density reduces to $dy$ wedged with the four-dimensional density of the same type, with multiplicities fixed by the choice of the frame leg along $dy$; this is how a five-dimensional Chern-Simons form yields a four-dimensional curvature-squared density.

\emph{Provenance:} \cite{Chamseddine1989, Chamseddine1990}; the transgression form and the Lovelock expansion as in \cite{Zanelli2005}.

## technical
In five dimensions gravity can be written as a Chern-Simons theory of the conformal (anti-de Sitter) group: the action is the Chern-Simons form of the cubic invariant of its gauge field, needs no metric, and is gauge invariant up to boundary terms. Chamseddine showed that, once a vector splits the gauge field into a connection and a frame, the action becomes a definite combination of the Gauss-Bonnet, Einstein-Hilbert and cosmological terms, with relative weights $1$, $\tfrac23\ell^{-2}$ and $\tfrac15\ell^{-4}$ fixed by the larger gauge invariance, $\ell$ the radius. Reducing such densities along a line in the standard Kaluza-Klein way gives four-dimensional curvature-squared densities. Taken from the literature; in the series the gauge field takes values in the bivectors of $\Cl(2,4)$.

## lay
In a five-dimensional world, gravity can be built entirely from the symmetries of spacetime, with no lengths put in by hand; Chamseddine found that the rule then contains the usual ingredients of gravity in fixed proportions. Shrinking one direction to a line gives four-dimensional rules of a related form. This is taken from the literature.

## one-liner
Five-dimensional Chern-Simons gravity, $\kappa_{5}\int\mathrm{CS}_{5}(A)$ for the cubic invariant of the conformal algebra, is, split by a vector, the Lovelock combination $\epsilon(RRe + \tfrac23\ell^{-2}Reee + \tfrac15\ell^{-4}eeeee)$ with ratios fixed by gauge invariance (Chamseddine 1989, 1990).
