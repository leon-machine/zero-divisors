---
id: synthesis.imported-two-loop-yukawa-gauge-terms
kind: claim
version: 1
title: 'Imported: the Yukawa contribution to the two-loop running of a gauge coupling'
status: imported
region: synthesis
subject: standard-model
tags: [running-and-unification, classical-theorem]
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
- citation: 'M. E. Machacek and M. T. Vaughn, Two-loop renormalization group equations in a general quantum field theory (I). Wave function renormalization, Nucl. Phys. B 222 (1983), 83--103.'
  key: MachacekVaughn1983
- citation: 'M. E. Machacek and M. T. Vaughn, Two-loop renormalization group equations in a general quantum field theory (II). Yukawa couplings, Nucl. Phys. B 236 (1984), 221--232.'
  key: MachacekVaughn1984
- citation: 'M. Luo, H. Wang and Y. Xiao, Two-loop renormalization group equations in general gauge field theories, Phys. Rev. D 67 (2003), 065019.'
  key: LuoWangXiao2003
  locator: 'Eq. (30)'
  doi: 10.1103/PhysRevD.67.065019
extraction:
  note: >-
    Imported for op.two-loops-two-thresholds (partial supersymmetric content with gaugino Yukawas
    below a heavy threshold); no result cites it yet. Clause (a) was checked against Eq. (30) of
    Luo, Wang and Xiao (arXiv:hep-ph/0211440v3), including the definitions of kappa and Y_4(F) and
    their attribution to Machacek and Vaughn [Nucl. Phys. B 222 (1983) 83; B 236 (1984) 221; B 249
    (1985) 70]. The title and pages of Machacek-Vaughn II and the product-group form in clause (b)
    are cited from memory, not checked against the source. The gauge part of the product-group two-
    loop matrix is the existing Fact standard-model.imported-two-loop-gauge-coefficients.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Created by the maintainer pass for op.two-loops-two-thresholds; clause (a) verified against Luo-Wang-Xiao Eq. (30), clause (b) cited from memory.'
---

## formal
\begin{enumerate}
\item[(a)] For a renormalisable gauge theory with simple gauge group $G$ of dimension $d(G)$ and coupling $g$, fermions in a representation $F$ and real scalars in a representation $S$, with Yukawa matrices $Y^{a}$ (one for each real scalar $\phi_{a}$), and with the group invariants $C_{2}$, $S_{2}$ in the notation of the third reference,
\begin{align*}
\beta(g) \;=\; {}& -\frac{g^{3}}{(4\pi)^{2}}\Bigl\{\tfrac{11}{3}C_{2}(G) - \tfrac43\kappa S_{2}(F) - \tfrac16 S_{2}(S) + \frac{2\kappa}{(4\pi)^{2}}Y_{4}(F)\Bigr\} \\
& - \frac{g^{5}}{(4\pi)^{4}}\Bigl\{\tfrac{34}{3}C_{2}(G)^{2} - \kappa\bigl[4C_{2}(F) + \tfrac{20}{3}C_{2}(G)\bigr]S_{2}(F) - \bigl[2C_{2}(S) + \tfrac13 C_{2}(G)\bigr]S_{2}(S)\Bigr\},
\end{align*}
with $Y_{4}(F) = \frac{1}{d(G)}\Tr\bigl[C_{2}(F)\,Y^{a}Y^{a\dagger}\bigr]$ and $\kappa = \tfrac12$ for two-component and $1$ for four-component fermions. The Yukawa couplings enter the gauge running first at two loops, through the term $-2\kappa\,g^{3}Y_{4}(F)/(4\pi)^{4}$.
\item[(b)] For a product of simple factors and $\mathrm{U}(1)$s, the Yukawa term of the coupling $g_{i}$ is the same expression with $C_{2}(F)$ replaced by the quadratic Casimir of the factor $i$ and $d(G)$ by $d(G_{i})$ (with the chosen $\mathrm{U}(1)$ normalisation).
\end{enumerate}
\emph{Provenance:} \cite{MachacekVaughn1983, MachacekVaughn1984}; \cite[Eq.~(30)]{LuoWangXiao2003}.

## technical
In a general gauge theory the Yukawa couplings first affect the running of a gauge coupling at two loops. For a simple gauge group the two-loop beta function contains, besides the purely gauge, fermion and scalar terms, the term $-2\kappa\,g^{3}Y_{4}(F)/(4\pi)^{4}$ with $Y_{4}(F) = \Tr[C_{2}(F)Y^{a}Y^{a\dagger}]/d(G)$, where $\kappa = \tfrac12$ for Weyl fermions; for a product group the same term appears for each factor with that factor's Casimir. These are the general results of Machacek and Vaughn, as restated by Luo, Wang and Xiao.

## lay
The strengths of the forces change with the energy at which they are measured, and the rate of change can be computed order by order. At the second order the couplings of matter particles to the Higgs-like fields begin to contribute. This standard result gives that contribution for any gauge theory. It is taken from the literature.

## one-liner
In a general gauge theory the Yukawa couplings enter the two-loop gauge beta function through $-2\kappa\,g^{3}Y_{4}(F)/(4\pi)^{4}$, $Y_{4}(F) = \Tr[C_{2}(F)Y^{a}Y^{a\dagger}]/d(G)$, $\kappa = \tfrac12$ for Weyl fermions (Machacek-Vaughn; Luo-Wang-Xiao).
