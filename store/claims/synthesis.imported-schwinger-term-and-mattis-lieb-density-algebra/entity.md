---
id: synthesis.imported-schwinger-term-and-mattis-lieb-density-algebra
kind: claim
version: 1
title: 'Imported: the Schwinger term and the chiral density algebra (Mattis and Lieb)'
status: imported
region: synthesis
subject: quantum-fields
tags: [bosonisation, car-algebra, classical-theorem, hypercharge-and-anomalies]
proposed_by:
  kind: ai
  session: maintainer-2026-11-01
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'J. Schwinger, Field theory commutators, Phys. Rev. Lett. 3 (1959), 296--297.'
  key: Schwinger1959
  doi: 10.1103/PhysRevLett.3.296
- citation: 'S. Tomonaga, Remarks on Bloch''s method of sound waves applied to many-fermion problems, Prog. Theor. Phys. 5 (1950), 544--569.'
  key: Tomonaga1950
- citation: 'D. C. Mattis and E. H. Lieb, Exact solution of a many-fermion system and its associated boson field, J. Math. Phys. 6 (1965), 304--312.'
  key: MattisLieb1965
  doi: 10.1063/1.1704281
- citation: 'J. von Delft and H. Schoeller, Bosonization for beginners, refermionization for experts, Ann. Phys. (Leipzig) 7 (1998), 225, arXiv:cond-mat/9805275, equations (21) and (22).'
  key: vonDelftSchoeller1998
extraction:
  note: >-
    Imported so that the floor-regulator result can pin the central term and its origin instead of citing them from
    memory. Checked on 2026-11-01: the bibliographic data of Schwinger (Phys. Rev. Lett. 3, 296-297, 1959, DOI) and of
    Mattis and Lieb (J. Math. Phys. 6, 304-312, 1965, DOI) against their INSPIRE records; the content of (i) against von
    Delft and Schoeller, arXiv:cond-mat/9805275, equations (21) and (22): for a chiral band with the levels k <= 0
    filled, the bosons b_q built from the density's Fourier modes with weight 1/sqrt(n_q) obey [b_q, b_q'^dagger] =
    delta_qq', the constant coming from the difference of vacuum expectation values after normal ordering, a point the
    text credits to Mattis and Lieb. Cited from memory, not checked: Tomonaga's bibliographic data and content,
    Schwinger's content beyond the title (the field-theory commutator of the current with a nonzero vacuum
    expectation), and the statements of (ii) and (iii), which the citing result proves for its own truncation.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (Schwinger''s commutator term and the Mattis-Lieb / Tomonaga density algebra as a Fact, by Leon''s list of imports).'
---

## formal
\begin{enumerate}
\item[(i)] \emph{(The density algebra.)} For one chiral band of fermion modes $a_{k}$, $k \in \mathbb{Z}$, with the levels $k \le 0$ filled in the vacuum, the normal-ordered density modes $\rho(p) = \sum_{k}{:}a^{*}_{k+p}a_{k}{:}$ obey $[\rho(-p), \rho(p')] = p\,\delta_{pp'}$ for $p > 0$: up to normalisation, $b_{p} = \rho(-p)/\sqrt{p}$ and $b_{p}^{\dagger}$ are canonical boson modes \cite{Tomonaga1950, MattisLieb1965, vonDelftSchoeller1998}.
\item[(ii)] \emph{(Its origin.)} The central term $p$ is absent from the commutator of the unordered densities of any finite band (there $[\rho(-p), \rho(p)]$ is a difference of occupation numbers, of zero vacuum expectation in total); it arises from the infinitely filled sea through normal ordering \cite{MattisLieb1965, vonDelftSchoeller1998}.
\item[(iii)] \emph{(The Schwinger term.)} In a relativistic field theory with a positive-energy vacuum, the equal-time commutator of the charge density with the current density cannot vanish: it carries a term, the Schwinger term, proportional to the derivative of a delta function, whose one-dimensional chiral form is the central term of (i) \cite{Schwinger1959}.
\end{enumerate}

## technical
For fermions in one chiral band with the negative levels filled, the Fourier modes of the density do not commute: the commutator of a mode with its conjugate equals the momentum, a central term. It makes the density modes a set of boson modes, the basis of bosonisation (Tomonaga; Mattis and Lieb, who noticed the care the normal ordering needs). For any finite band the term is absent; it comes from the infinite sea. In relativistic field theory the same structure appears as Schwinger's term in the commutator of charge and current densities, which a positive-energy vacuum forces to be nonzero.

## lay
In a one-dimensional sea of fermions, ripples of density behave exactly like independent bosons, a standard result of the 1950s and 1960s. The reason is a small extra term in how density ripples combine, which comes from the infinitely deep sea of filled levels; Schwinger showed the same kind of term must appear in any relativistic theory with a stable vacuum. The series takes these results as given.

## one-liner
For a chiral band with the sea filled the normal-ordered density modes obey $[\rho(-p), \rho(p)] = p$ (Tomonaga; Mattis-Lieb), a central term from the infinite sea, absent for any finite band, the one-dimensional form of Schwinger's commutator term (1959).
