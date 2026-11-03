---
id: synthesis.imported-heat-kernel-coefficients-and-background-field-gauge
kind: claim
version: 1
title: 'Imported: the heat-kernel (Seeley-DeWitt) coefficients of a Laplace-type operator, whose field-strength part on a flat background is $\tfrac{1}{12}\Omega_{\mu\nu}\Omega^{\mu\nu} + \tfrac12E^{2}$ ($a_{2}$ in DeWitt''s numbering, $a_{4}$ in Vassilevich''s), and the background-field gauge with Faddeev-Popov ghosts and the one-loop determinant weights (Abbott 1981)'
status: imported
region: synthesis
subject: quantum-fields
tags: [running-and-unification, gauge-fields, classical-theorem, recovers-known-physics]
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
- citation: 'D. V. Vassilevich, Heat kernel expansion: user''s manual, Phys. Rep. 388 (2003), 279--360, arXiv:hep-th/0306138.'
  key: Vassilevich2003
  doi: 10.1016/j.physrep.2003.09.002
- citation: 'B. S. DeWitt, Dynamical Theory of Groups and Fields, Gordon and Breach (1965).'
  key: DeWitt1965
- citation: 'L. F. Abbott, The background field method beyond one loop, Nucl. Phys. B 185 (1981), 189--203.'
  key: Abbott1981
  doi: 10.1016/0550-3213(81)90371-0
extraction:
  note: >-
    Imported so that the one-loop running coefficients can pin the heat-kernel coefficient, the background-field
    gauge and the determinant weights instead of citing them from memory. Checked on 2026-11-01 against
    Vassilevich, arXiv:hep-th/0306138 (v3): the expansion Tr(f exp(-tD)) ~ sum_k t^((k-n)/2) a_k(f, D),
    equation (2.21), so his a_4 is the coefficient of t^0 in four dimensions; a_0 and a_2 in the forms (4.13),
    (4.14) with alpha_0 = 1 and alpha_1 = 6 (the coefficient of E); a_4 in the general form (4.15) with prefactor
    1/360 and alpha_5 = 180, the coefficient of E^2 (stated after (4.17)). Not checked against the source (cited
    from memory): the coefficient 30 of Omega_ij Omega_ij in a_4 (the value of alpha_10) and the remaining
    curvature coefficients, the coefficient alpha_2 = 1 of R in a_2, DeWitt's own numbering and equations, the
    proper-time form of the logarithm in (ii) (an elementary consequence of (i)), and the one-loop operators
    and determinant weights of (iii). The bibliographic data of Vassilevich (Phys. Rep.
    388, 279-360, 2003, DOI) and of Abbott (title, Nucl. Phys. B 185, 189-203, 1981, DOI) checked against their
    INSPIRE records; the content of Abbott beyond the title is cited from memory.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (the heat-kernel coefficient and the background-field gauge as a Fact, by Leon''s list of imports).'
---

## formal
\begin{enumerate}
\item[(i)] \emph{(The heat-kernel expansion.)} Let $D = -(g^{\mu\nu}\nabla_{\mu}\nabla_{\nu} + E)$ be a Laplace-type operator on a vector bundle over an $n$-dimensional manifold without boundary, $\nabla$ a connection with curvature $\Omega_{\mu\nu}$ and $E$ an endomorphism. Then $\mathrm{Tr}(f e^{-tD}) \simeq \sum_{k \ge 0}t^{(k-n)/2}a_{k}(f, D)$ as $t \to 0$, with the odd $k$ absent, $a_{0} = (4\pi)^{-n/2}\int\mathrm{tr}\,f$, $a_{2} = (4\pi)^{-n/2}\tfrac16\int\mathrm{tr}\,f(6E + R)$ and
\[
a_{4} = \frac{(4\pi)^{-n/2}}{360}\int\mathrm{tr}\,f\bigl(60E_{;kk} + 60RE + 180E^{2} + 12R_{;kk} + 5R^{2} - 2\Ric^{2} + 2\,\mathrm{Riem}^{2} + 30\,\Omega_{ij}\Omega_{ij}\bigr)
\]
\cite{Vassilevich2003}. On a flat background with $f = 1$ the local part of $a_{4}$ is $(4\pi)^{-n/2}\int\mathrm{tr}\bigl(\tfrac12E^{2} + \tfrac{1}{12}\Omega_{\mu\nu}\Omega^{\mu\nu}\bigr)$ up to a total derivative. DeWitt's expansion runs in integer powers of $t$ and calls this coefficient $a_{2}$ \cite{DeWitt1965}.
\item[(ii)] \emph{(Logarithmic divergence.)} In four dimensions, with a proper-time cut-off at $t = 1/L$, the logarithmic part of $\ln\det D$ is $-\ln(L/\mu^{2})\,a_{4}(1, D)$ \cite{Vassilevich2003}; on a flat background this is $-\tfrac{1}{16\pi^{2}}\ln(L/\mu^{2})\int\mathrm{tr}\bigl(\tfrac12E^{2} + \tfrac{1}{12}\Omega^{2}\bigr)$.
\item[(iii)] \emph{(Background-field gauge.)} Splitting the gauge field into a background and a quantum part and fixing the gauge covariantly with respect to the background (the background Feynman gauge), with Faddeev-Popov ghosts, keeps background gauge invariance, so the one-loop effective action is a gauge-invariant functional of the background field strength and its coefficient of $\Omega^{2}$ gives the one-loop beta coefficient \cite{Abbott1981}. The one-loop operators are $-D^{2}$ for scalars and for the ghosts (a complex adjoint scalar of opposite statistics), the square of the Dirac operator for spinors, and $-D^{2}\delta^{\mu}{}_{\nu} + 2\Omega^{\mu}{}_{\nu}$ on the vector index for the quantum gauge field; the effective action is $\sum\sigma w\ln\det$ with $w = 1$ for complex bosons and for ghosts, $w = \tfrac12$ for real bosons and for the squared Dirac operator, and $\sigma = -1$ for fermions and ghosts, $+1$ otherwise.
\end{enumerate}

## technical
The heat kernel of a second-order operator of Laplace type has a small-time expansion whose coefficients are integrals of local invariants: the endomorphism part $E$, the curvature $\Omega$ of the connection and the curvature of the manifold. Vassilevich labels them by the power $t^{(k-n)/2}$, so the coefficient that carries $E^{2}$ and $\Omega^{2}$ is his $a_{4}$; DeWitt labels by integer powers and calls it $a_{2}$. On a flat background its field-strength part is $\tfrac12E^{2} + \tfrac1{12}\Omega^{2}$, and it multiplies the logarithm of the cut-off in the one-loop determinant. In the background-field gauge of Abbott the gauge fixing respects the gauge symmetry of the background, so the one-loop effective action is a gauge-invariant function of the background field strength, and the coefficient of its square gives the running of the coupling; each field contributes the determinant of its one-loop operator, weighted by its statistics and by whether it is real or complex, with the Faddeev-Popov ghosts entering as a complex scalar with fermionic sign.

## lay
How strongly the forces of nature act changes with the energy at which they are probed, and the rate of change at the first quantum level can be read from a standard expansion that describes how heat would spread on the space of field configurations. Combined with a standard way of fixing the redundancy of force fields that keeps their symmetry visible, the expansion gives each kind of particle's contribution to the running. These are textbook results that the series takes as given.

## one-liner
The heat-kernel expansion $\mathrm{Tr}\,e^{-tD} \simeq \sum t^{(k-n)/2}a_{k}$, with flat-background field-strength coefficient $\tfrac12E^{2} + \tfrac1{12}\Omega^{2}$ ($a_{4}$ in Vassilevich's labelling, $a_{2}$ in DeWitt's) multiplying the logarithm in $\ln\det$, and the background-field gauge with Faddeev-Popov ghosts and the one-loop determinant weights (Abbott 1981).
