---
id: synthesis.imported-powers-stormer-takesaki-disjointness
kind: claim
version: 2
title: 'Imported: quasi-equivalence of quasi-free CAR states and the Powers-Stormer inequality (Powers-Stormer), and disjointness of KMS states at different temperatures (Takesaki)'
status: imported
region: synthesis
subject: thermality
tags: [car-algebra, modular-theory, superselection, classical-theorem]
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
imported_from:
- citation: 'R. T. Powers and E. Stormer, Free states of the canonical anticommutation relations, Commun. Math. Phys. 16 (1970), 1--33.'
  key: PowersStormer1970
- citation: 'M. Takesaki, Disjointness of the KMS-states of different temperatures, Commun. Math. Phys. 17 (1970), 33--41.'
  key: Takesaki1970
  doi: 10.1007/BF01649582
extraction:
  note: >-
    Imported for the result that compares the tower charge and the mirror's temperature as
    superselection labels. Takesaki 1970 (title, journal, volume, pages, DOI, and the abstract
    'Disjointness of (KMS)-states of different temperatures is proved') was checked against the
    publisher's listing, and the type III hypothesis against a recent secondary statement
    (arXiv:2402.14794, Sec. 4.1). For Powers-Stormer the title, journal and volume were checked
    against the Project Euclid listing; the pages and the statement of clause (a) are cited from
    memory, not checked against the source.
  maintainer_pass_2026_11_01:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: >-
      Version 1 -> 2, at Leon's decision of 2026-11-01 approving the Powers-Stormer inequality as a routine
      import into this Fact: clause (c) added, so that the result on the microlocal condition on a horizon
      generator cites it as a Fact rather than from memory; clauses (a) and (b) unchanged. Checked: the pages
      1-33 of Powers and Stormer 1970 against the bibliography of arXiv:1204.6665; the natural-cone form
      against arXiv:2102.07479, equation (11), which states it and names it "the Powers-Stormer inequality
      between the trace norm and the Hilbert-Schmidt norm". Cited from memory, not checked against the source:
      that the inequality is Lemma 4.1 of Powers and Stormer, and its operator form for bounded positive
      operators with possibly infinite norms (for positive trace-class operators it is the natural-cone form
      read on the bounded operators of a Hilbert space, where the representing vector of a positive
      trace-class operator is its square root).
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Created by the maintainer pass so that the sector-label result can pin the Powers-Stormer criterion it cited from memory and Takesaki''s theorem it cited in words; partly verified (see note).'
---

## formal
\begin{enumerate}
\item[(a)] (Powers-Stormer.) For operators $0 \le A, B \le 1$ on a Hilbert space $\mathcal{K}$, the gauge-invariant quasi-free states $\omega_{A}$, $\omega_{B}$ of the CAR algebra over $\mathcal{K}$ are factor states, and they are quasi-equivalent if and only if $A^{1/2} - B^{1/2}$ and $(1 - A)^{1/2} - (1 - B)^{1/2}$ are Hilbert-Schmidt; being factor states, they are disjoint whenever they are not quasi-equivalent.
\item[(b)] (Takesaki.) Let $\alpha$ be a one-parameter group of $*$-automorphisms of a C*-algebra and let $\omega$, $\omega'$ be $(\alpha, \beta)$- and $(\alpha, \beta')$-KMS states with $\beta \neq \beta'$. If the von Neumann algebra generated in the GNS representation of one of them is of type III, then $\omega$ and $\omega'$ are disjoint.
\item[(c)] (The Powers-Stormer inequality.) For bounded positive operators $A$, $B$ on a Hilbert space, $\|A^{1/2} - B^{1/2}\|_{2}^{2} \le \|A - B\|_{1}$, with $\|\cdot\|_{2}$ the Hilbert-Schmidt norm and $\|\cdot\|_{1}$ the trace norm, either side possibly infinite; in particular, if $A - B$ is trace class then $A^{1/2} - B^{1/2}$ is Hilbert-Schmidt. In the form for a von Neumann algebra in standard form, for normal positive functionals $\varphi$, $\psi$ with representing vectors $\xi_{\varphi}$, $\xi_{\psi}$ in the natural cone, $\|\xi_{\varphi} - \xi_{\psi}\|^{2} \le \|\varphi - \psi\| \le \|\xi_{\varphi} - \xi_{\psi}\|\,\|\xi_{\varphi} + \xi_{\psi}\|$.
\end{enumerate}
\emph{Provenance:} \cite{PowersStormer1970, Takesaki1970}.

## technical
Two results on when thermal states of an infinite system belong to different sectors. Powers and Størmer showed that the gauge-invariant quasi-free states of the fermion (CAR) algebra are factor states, and that two of them, with one-particle density operators $A$ and $B$, are quasi-equivalent exactly when $A^{1/2} - B^{1/2}$ and $(1 - A)^{1/2} - (1 - B)^{1/2}$ are Hilbert-Schmidt; otherwise they are disjoint. Takesaki showed that KMS states of the same dynamics at different temperatures are disjoint when the von Neumann algebra induced by one of them is of type III. The Powers-Størmer inequality bounds the Hilbert-Schmidt distance of the square roots of two positive operators by the trace distance of the operators, so that states close in norm have close square roots; for one-particle operators between $0$ and $1$ whose difference is trace class it gives the Hilbert-Schmidt condition on the square roots in (a).

## lay
For a system with infinitely many parts, two states can be so different that no measurement on finitely many parts relates them: they live in separate sectors. These two classical theorems say when that happens for fermions in thermal-like states, through a condition on how much their occupations differ in total (with an inequality that turns a small total difference into a small difference of square roots), and that equilibrium states at different temperatures are separated in this way in the typical infinite case. They are taken from the literature.

## one-liner
Gauge-invariant quasi-free CAR states $\omega_{A}$, $\omega_{B}$ are factor states, quasi-equivalent iff $A^{1/2} - B^{1/2}$ and $(1 - A)^{1/2} - (1 - B)^{1/2}$ are Hilbert-Schmidt and otherwise disjoint, and $\|A^{1/2} - B^{1/2}\|_{2}^{2} \le \|A - B\|_{1}$ for bounded positive $A$, $B$ (Powers-Størmer); KMS states at different temperatures are disjoint when one induces a type III algebra (Takesaki).
