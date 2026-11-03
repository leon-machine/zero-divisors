---
id: synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians
kind: claim
version: 1
title: 'Imported: in four dimensions the natural second-order field equations of a metric are the Einstein map plus a constant (Lovelock), and the natural Lagrangians with no field equations are the Euler and Pontryagin densities up to divergences (Anderson and Duchamp; Anderson)'
status: imported
region: synthesis
subject: einstein
tags: [curvature-and-field-equations, forcing-and-uniqueness, classical-theorem]
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
- citation: 'D. Lovelock, The Einstein tensor and its generalizations, J. Math. Phys. 12 (1971), 498--501.'
  key: Lovelock1971
  doi: 10.1063/1.1665613
- citation: 'D. Lovelock, The four-dimensionality of space and the Einstein tensor, J. Math. Phys. 13 (1972), 874--876.'
  key: Lovelock1972
  doi: 10.1063/1.1666069
- citation: 'I. M. Anderson and T. Duchamp, On the existence of global variational principles, Amer. J. Math. 102 (1980), 781--868.'
  key: AndersonDuchamp1980
  doi: 10.2307/2374195
- citation: 'I. M. Anderson, Natural variational principles on Riemannian structures, Ann. of Math. (2) 120 (1984), 329--370.'
  key: Anderson1984
  doi: 10.2307/2006945
extraction:
  note: >-
    Imported so that the inversion of the Clausius route can pin the two literature theorems its
    clauses (ii) and (iv) rest on instead of citing them from memory. Checked on 2026-10-31: the
    bibliographic data of Lovelock 1971 and 1972 (titles, journal, volumes, pages, DOIs) and the
    statement of (a) as Lovelock's theorem in four dimensions (a symmetric divergence-free tensor
    built from the metric and its first two derivatives is a combination of the Einstein tensor and
    the metric, and the same holds for a second-order Euler-Lagrange expression of a scalar density)
    against the encyclopedia summary of Lovelock's theorem citing both papers; the bibliographic data of
    Anderson and Duchamp 1980 (journal, volume, issue, pages, DOI) and of Anderson 1984 against the Utah
    State University repository records, whose abstracts state the subject (the inverse problem of the
    calculus of variations, and the existence of invariant Lagrangians for invariant locally variational
    operators). The content of (b), the classification of natural variationally trivial Lagrangians of a
    four-dimensional metric, and its division between the two papers are cited from memory, not checked
    against the source. Necessity of the Helmholtz condition (symmetry of the second variation) is
    elementary and is proved where it is used; its sufficiency on star-shaped domains (Volterra-Vainberg)
    is not part of this Fact.
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Created at Leon''s decision of 2026-10-31 approving the import of Lovelock and Anderson-Duchamp for the gravitational-action results; partly verified (see note).'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on four-dimensional flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with derived metric $g$, and call an expression \emph{natural} if it is built from $g$ and its derivatives up to a fixed order covariantly, so that it transforms as a tensor under displacement and rotation gauge transformations (in a curved-spacetime reading: a concomitant of the metric, equivariant under diffeomorphisms).
\begin{enumerate}
\item[(a)] (Lovelock.) A natural symmetric map $E(a)$ built from $g$ and its derivatives up to second order that is divergence-free for every field is $E(a) = c_{1}\,\mathcal{G}(a) + c_{2}\,a$ with constants $c_{1}$, $c_{2}$, $\mathcal{G}$ the Einstein map in the store's sign. In particular, if a natural Lagrangian density of $g$ has an Euler-Lagrange expression of second order, that expression is of this form; its vacuum solutions with $c_{1} \neq 0$ have the one value $\Lambda = c_{2}/c_{1}$ of the cosmological term. In $n$ dimensions the divergence-free second-order expressions are the Lovelock family, which for $n = 4$ reduces to these two terms.
\item[(b)] (Variationally trivial natural Lagrangians.) A natural Lagrangian density of a four-dimensional metric whose Euler-Lagrange expression vanishes identically is, locally, $c_{E}E_{4} + c_{P}P_{4}$ plus the divergence of a natural current, with $E_{4}$ the Euler density ($R_{abcd}R^{abcd} - 4R_{ab}R^{ab} + R^{2}$ in index reading) and $P_{4}$ the Pontryagin density ($\tfrac12\epsilon^{cdef}R_{abcd}R^{ab}{}_{ef}$ in index reading), with constants $c_{E}$, $c_{P}$. Hence two natural Lagrangians of $g$ with the same Euler-Lagrange expressions differ by such a combination.
\end{enumerate}
\emph{Provenance:} \cite{Lovelock1971, Lovelock1972} for (a); \cite{AndersonDuchamp1980, Anderson1984} for (b) and for the inverse problem of the calculus of variations for natural operators.

## technical
Lovelock's theorem is the classical uniqueness result for Einstein's equations: in four dimensions, any field equation for the metric that is built covariantly from the metric and its first two derivatives and is automatically divergence-free (as the field equations of a covariant action are, by Noether's second theorem) is a combination of the Einstein tensor and the metric. Field equations of an action of second order are therefore Einstein's, with one value of the cosmological constant. Anderson and Duchamp developed the inverse problem of the calculus of variations (when a given differential equation is the Euler-Lagrange equation of some action), and Anderson treated actions invariant under the symmetries of the metric. The part used here is that the covariant actions of a four-dimensional metric with no field equations at all are the Euler (Gauss-Bonnet) and Pontryagin densities plus total divergences, so two covariant actions with the same field equations differ only by those. Taken from the literature; in Gauge Theory Gravity the metric is the derived metric of the gravitational field on flat spacetime.

## lay
Einstein's equations are not just one choice among many. Lovelock proved that in a four-dimensional world, if the equations for gravity involve the geometry and its rates of change no more than twice over, and automatically respect energy conservation, they must be Einstein's equations with some cosmological constant. Anderson and Duchamp studied the reverse question, when a set of equations comes from an action principle, and the part used here says that two such principles giving the same equations can differ only by terms that measure the overall shape of space. These are theorems taken from the literature.

## one-liner
In four dimensions a natural divergence-free second-order symmetric expression in the metric is $c_{1}\mathcal{G} + c_{2}g$ (Lovelock 1971, 1972), and a natural Lagrangian with identically vanishing Euler-Lagrange expression is $c_{E}E_{4} + c_{P}P_{4}$ plus a divergence (Anderson and Duchamp 1980; Anderson 1984).
