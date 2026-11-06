---
id: synthesis.imported-sakharov-induced-gravity-coefficients
kind: claim
version: 1
title: 'Imported: one-loop coefficients of Sakharov''s induced gravity'
status: imported
region: synthesis
subject: einstein
tags: [curvature-and-field-equations, mode-counting, classical-theorem]
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
- citation: 'D. V. Vassilevich, Heat kernel expansion: user''s manual, Phys. Rep. 388 (2003), 279--360; arXiv:hep-th/0306138.'
  key: Vassilevich2003
  locator: 'Eq. (4.27)'
- citation: 'B. Broda and M. Szanecki, Induced gravity and gauge interactions revisited, Phys. Lett. B (2009); arXiv:0809.4203.'
  key: BrodaSzanecki2009
  locator: 'Eqs. (5), (8)'
  doi: 10.1016/j.physletb.2009.02.052
- citation: 'L. Boyle and N. Turok, Cancelling the vacuum energy and Weyl anomaly in the standard model with dimension-zero scalar fields, arXiv:2110.06258.'
  key: BoyleTurok2021
  locator: 'Eq. (17)'
- citation: 'W. Tichy and E. E. Flanagan, How unique is the expected stress-energy tensor of a massive scalar field?, Phys. Rev. D 58 (1998), 124007; arXiv:gr-qc/9807015.'
  key: TichyFlanagan1998
  locator: 'Sec. I.A, Eqs. (1.3)--(1.5)'
  doi: 10.1103/PhysRevD.58.124007
extraction:
  note: >-
    Imported so that the result on the attachment's modules and the Sakharov weights can pin the standard
    induced-gravity coefficients, the heat-kernel density they come from, the Boyle-Turok count and the
    Tichy-Flanagan statement instead of citing them in its text. Checked on 2026-11-01: Vassilevich against the
    arXiv text of hep-th/0306138, Eq. (4.27), a_2(f, D) = (4 pi)^(-n/2) (1/6) int tr_V f(6E + R) for
    D = -(g^{mu nu} nabla_mu nabla_nu + E), with R = 2 on the unit two-sphere; Broda and Szanecki against the
    arXiv text of 0809.4203 v4: Eq. (5), the induced term -(1/(192 pi^2 epsilon))(N_0 + N_{1/2} - 4N_1) R with a
    cut-off epsilon, and Eq. (8) at the Planckian cut-off, N_0 minimal scalars, N_{1/2} two-component fermion
    fields, N_1 gauge vectors, and the DOI against the arXiv record; Boyle and Turok against the arXiv text of
    2110.06258: Eq. (17), n_{1/2} = 4 n_1, n'_0 = 3 n_1, n_0 = 0, and with n_1 = 12 the requirement of
    n_{1/2} = 48 = 3 x 16 Weyl fermions, three generations with right-handed neutrinos, from cancelling the
    vacuum energy and both Weyl-anomaly coefficients with dimension-zero scalars; Tichy and Flanagan against
    the arXiv text of gr-qc/9807015 and the DOI record: Sec. I.A, Eqs. (1.3)-(1.5), for a massless field the
    ambiguity allowed by Wald's axioms is alpha H^(1)_ab + beta H^(2)_ab, the two conserved local curvature
    tensors of dimension mass^4 (no Einstein-tensor or metric term, which would need a dimensionful
    coefficient). Cited from memory, not checked: the journal volume and pages of Vassilevich and of Broda and
    Szanecki, and the journal version of Boyle and Turok. The factor (1 - 6 xi) for a scalar coupled to the
    curvature with strength xi is a consequence of clause (a) with E = -xi R, not a statement of the sources.
---

## formal
Work in Euclidean signature with scalar curvature $R$ positive on spheres (the sources' convention).
\begin{enumerate}
\item[(a)] (Vassilevich, the curvature-linear heat-kernel coefficient.) For a Laplace-type operator $D = -(g^{\mu\nu}\nabla_{\mu}\nabla_{\nu} + E)$ on a vector bundle $V$ over a closed $n$-dimensional Riemannian manifold, the heat trace $\mathrm{Tr}(f e^{-tD})$ has the coefficient linear in curvature $a_{2}(f, D) = (4\pi)^{-n/2}\tfrac16\int_{M}\mathrm{tr}_{V}\big(f(6E + R)\big)$: the local density is $\mathrm{tr}_{V}(E + R/6)$ (the store's proofs write it $a_{1}$, the coefficient of the first power of the heat-kernel time). For a scalar coupled to the curvature with strength $\xi$, $E = -\xi R$ and the density is $(1 - 6\xi)R/6$.
\item[(b)] (Broda and Szanecki, Sakharov's induced gravity.) At one loop with an ultraviolet cut-off $\epsilon$, the matter fields induce the Einstein-Hilbert term $-\tfrac{1}{192\pi^{2}\epsilon}(N_{0} + N_{1/2} - 4N_{1})R$, with $N_{0}$ the number of minimally coupled scalars, $N_{1/2}$ the number of two-component fermion fields and $N_{1}$ the number of gauge vectors; with (a), a scalar of coupling $\xi$ contributes $N_{0}(1 - 6\xi)$ in place of $N_{0}$.
\item[(c)] (Boyle and Turok.) Cancelling the vacuum energy and both coefficients of the Weyl anomaly of the Standard Model by conformally coupled dimension-zero scalars requires $n_{1/2} = 4n_{1}$ Weyl fermions (with $n'_{0} = 3n_{1}$, $n_{0} = 0$); with the twelve gauge vectors of the Standard Model, $n_{1/2} = 48 = 3 \times 16$, three generations including right-handed neutrinos.
\item[(d)] (Tichy and Flanagan.) For a massless field the renormalised stress tensor is fixed by Wald's axioms up to $\alpha H^{(1)}_{ab} + \beta H^{(2)}_{ab}$, the two conserved local curvature tensors of dimension $(\mathrm{mass})^{4}$; no Einstein-tensor term and no metric term is allowed, since either would need a dimensionful coefficient.
\end{enumerate}
\emph{Provenance:} \cite[Eq.~(4.27)]{Vassilevich2003}; \cite[Eqs.~(5), (8)]{BrodaSzanecki2009}; \cite[Eq.~(17)]{BoyleTurok2021}; \cite[Sec.~I.A]{TichyFlanagan1998}.

## technical
Sakharov proposed that Newton's constant is induced by the vacuum fluctuations of the matter and gauge fields. At one loop the induced coefficient of the scalar curvature in the effective action comes from the heat-kernel coefficient linear in curvature, whose density for an operator $-(\nabla^{2} + E)$ is the trace of $E + R/6$. Summing over species with a cut-off gives a coefficient proportional to $N_{0} + N_{1/2} - 4N_{1}$, counting minimally coupled scalars, two-component fermions and gauge vectors; a scalar coupled to curvature with strength $\xi$ counts with weight $1 - 6\xi$, zero for conformal coupling. Boyle and Turok, cancelling the vacuum energy and the Weyl anomaly by a different mechanism, arrive at the same count of four Weyl fermions per gauge vector, which the Standard Model with twelve gauge vectors meets at exactly three generations including right-handed neutrinos. In the locally covariant scheme of Wald's axioms, by contrast, the stress tensor of a massless field has no Einstein-tensor ambiguity at all, whatever the field content.

## lay
One idea for where the strength of gravity comes from is that it is induced by the quantum jitter of all the particle fields, like the stiffness of a material coming from its atoms. In the simplest version each kind of field contributes a fixed weight, and force-carrying fields count four times as strongly, with the opposite sign, as matter fields. With the known particles plus right-handed neutrinos, the matter fields number exactly four times the force carriers, a coincidence noticed in another context by Boyle and Turok. These are taken from the literature.

## one-liner
At one loop the induced Einstein-Hilbert coefficient is proportional to $N_{0} + N_{1/2} - 4N_{1}$ (Broda and Szanecki; $N_{0}(1 - 6\xi)$ for curvature-coupled scalars, from the heat-kernel density $\mathrm{tr}(E + R/6)$, Vassilevich); the Standard Model with right-handed neutrinos has $n_{1/2} = 4n_{1} = 48$ (Boyle and Turok); massless fields have no Einstein-tensor ambiguity in the locally covariant stress tensor (Tichy and Flanagan).
