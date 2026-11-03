---
id: synthesis.imported-general-quartic-running-and-two-doublet-renormalisation-group-equations
kind: claim
version: 1
title: 'Imported: the running of scalar quartic couplings in a general gauge theory at one loop and of its pure-quartic part at two loops (Machacek and Vaughn 1985; Luo, Wang and Xiao 2003), and the one-loop renormalisation-group equations of the two-Higgs-doublet model with a discrete symmetry and type-II Yukawa couplings (Haber and Hempfling 1993; Branco et al. 2012)'
status: imported
region: synthesis
subject: standard-model
tags: [running-and-unification, symmetry-breaking, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-02
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'M. E. Machacek and M. T. Vaughn, Two-loop renormalization group equations in a general quantum field theory (III). Scalar quartic couplings, Nucl. Phys. B 249 (1985), 70--92.'
  key: MachacekVaughn1985
  doi: 10.1016/0550-3213(85)90040-9
- citation: 'M. Luo, H. Wang and Y. Xiao, Two-loop renormalization group equations in general gauge field theories, Phys. Rev. D 67 (2003), 065019; arXiv:hep-ph/0211440.'
  key: LuoWangXiao2003
  doi: 10.1103/PhysRevD.67.065019
- citation: 'I. Schienbein, F. Staub, T. Steudtner and K. Svirina, Revisiting RGEs for general gauge theories, Nucl. Phys. B 939 (2019), 1--48; arXiv:1809.06797.'
  key: Schienbein2019
  locator: 'Eqs. (5.9), (5.13), (5.14)'
- citation: 'H. E. Haber and R. Hempfling, The renormalization-group improved Higgs sector of the minimal supersymmetric model, Phys. Rev. D 48 (1993), 4280--4309.'
  key: HaberHempfling1993
  doi: 10.1103/PhysRevD.48.4280
- citation: 'P. M. Ferreira and D. R. T. Jones, Bounds on scalar masses in two Higgs doublet models, JHEP 08 (2009), 069; arXiv:0903.2856.'
  key: FerreiraJones2009
  locator: 'Eqs. (1), (37), (44), Appendix A'
- citation: 'G. C. Branco, P. M. Ferreira, L. Lavoura, M. N. Rebelo, M. Sher and J. P. Silva, Theory and phenomenology of two-Higgs-doublet models, Phys. Rept. 516 (2012), 1--102; arXiv:1106.0034.'
  key: Branco2012
  locator: 'Eq. (2) (the potential); Appendix E (renormalisation-group equations)'
  doi: 10.1016/j.physrep.2012.02.002
extraction:
  note: >-
    Imported, by Leon's list of routine imports, so that the result on the running of the rung field's
    quartics can pin the general formulas and the standard two-doublet equations it reproduces. Checked on 2
    November 2026: Luo, Wang and Xiao, the arXiv record (title, authors, DOI) and the normalisation of the
    quartic term, -(1/4!) lambda_abcd phi_a phi_b phi_c phi_d in the Lagrangian; the structure of the one-loop
    quartic beta function, Lambda^2 - 8 kappa H + 2 kappa Lambda^Y - 3 g^2 Lambda^S + 3 g^4 A, and of the
    two-loop pure-quartic terms, (1/12) sum_perm Lambda^2_af lambda_fbcd - Lambda-bar^3_abcd, with
    Lambda^2_ab(S) = (1/6) sum lambda_acde lambda_bcde, against Schienbein et al., arXiv:1809.06797, Eqs. (5.9),
    (5.13), (5.14); the normalisations of Lambda^2_abcd and Lambda-bar^3_abcd stated in (i) are from memory. The
    two-doublet equations of (ii): the potential normalisation of Branco et al., Eq. (2); the scalar and gauge
    terms and the top-Yukawa terms for one doublet against Ferreira and Jones, arXiv:0903.2856, Eqs. (1), (37),
    (44), which derive them and state agreement with Haber and Hempfling (up to a typo in beta_lambda2 and an
    overall factor two in the definition of beta). The type-II terms in y_t and y_b on both doublets, including the
    mixed terms -12 y_t^2 y_b^2 in beta_lambda3 and +12 y_t^2 y_b^2 in beta_lambda4, are cited from memory.
    Machacek and Vaughn's journal data and the journal data of Schienbein et al. and of Ferreira and Jones are
    from memory; Branco et al.'s Appendix E was not legible in the extracted text.
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Created by the maintainer pass of 2 November 2026, by Leon''s list of routine imports (Machacek-Vaughn and the two-doublet renormalisation-group equations), for the result on the running of the rung field''s quartics.'
---

## formal
\begin{enumerate}
\item[(i)] \emph{(General quartic running.)} For real scalars $\phi_{a}$ with potential $V = \tfrac{1}{4!}\lambda_{abcd}\phi_{a}\phi_{b}\phi_{c}\phi_{d}$, in a gauge theory with gauge coupling $g$ and Yukawa couplings to fermions, in a mass-independent scheme, $16\pi^{2}\beta_{abcd}^{(1)} = \Lambda^{2}_{abcd} - 8\kappa H_{abcd} + 2\kappa\Lambda^{Y}_{abcd} - 3g^{2}\Lambda^{S}_{abcd} + 3g^{4}A_{abcd}$ with $\Lambda^{2}_{abcd} = \tfrac18\sum_{\mathrm{perm}}\lambda_{abef}\lambda_{efcd}$, and the two-loop terms built from the quartics alone are $(16\pi^{2})^{2}\beta_{abcd}^{(2)} \supset \tfrac{1}{12}\sum_{\mathrm{perm}}\Lambda^{2}_{af}\lambda_{fbcd} - \bar{\Lambda}^{3}_{abcd}$, with $\Lambda^{2}_{ab} = \tfrac16\lambda_{acde}\lambda_{bcde}$ and $\bar{\Lambda}^{3}_{abcd} = \tfrac14\sum_{\mathrm{perm}}\lambda_{abef}\lambda_{cegh}\lambda_{dfgh}$ \cite{MachacekVaughn1985, LuoWangXiao2003, Schienbein2019}.
\item[(ii)] \emph{(Two doublets.)} For two doublets $\Phi_{1}$, $\Phi_{2}$ of hypercharge $\tfrac12$ with $V \supset \tfrac12\lambda_{1}(\Phi_{1}^{\dagger}\Phi_{1})^{2} + \tfrac12\lambda_{2}(\Phi_{2}^{\dagger}\Phi_{2})^{2} + \lambda_{3}(\Phi_{1}^{\dagger}\Phi_{1})(\Phi_{2}^{\dagger}\Phi_{2}) + \lambda_{4}(\Phi_{1}^{\dagger}\Phi_{2})(\Phi_{2}^{\dagger}\Phi_{1}) + [\tfrac12\lambda_{5}(\Phi_{1}^{\dagger}\Phi_{2})^{2} + \mathrm{h.c.}]$ (a discrete symmetry forbidding the other quartics), $\Phi_{2}$ coupled to the top with $y_{t}$ and $\Phi_{1}$ to the bottom with $y_{b}$ (type II), gauge couplings $g$, $g'$ (non-unified normalisation) and $w = 3(3g^{2} + g'^{2})$, at one loop
\begin{align*}
16\pi^{2}\beta_{\lambda_{1}} &= 12\lambda_{1}^{2} + 4\lambda_{3}^{2} + 4\lambda_{3}\lambda_{4} + 2\lambda_{4}^{2} + 2|\lambda_{5}|^{2} + \tfrac34(3g^{4} + g'^{4} + 2g^{2}g'^{2}) - w\lambda_{1} + 12\lambda_{1}y_{b}^{2} - 12y_{b}^{4},\\
16\pi^{2}\beta_{\lambda_{3}} &= (\lambda_{1} + \lambda_{2})(6\lambda_{3} + 2\lambda_{4}) + 4\lambda_{3}^{2} + 2\lambda_{4}^{2} + 2|\lambda_{5}|^{2} + \tfrac34(3g^{4} + g'^{4} - 2g^{2}g'^{2}) - w\lambda_{3} + 6\lambda_{3}(y_{t}^{2} + y_{b}^{2}) - 12y_{t}^{2}y_{b}^{2},\\
16\pi^{2}\beta_{\lambda_{4}} &= 2(\lambda_{1} + \lambda_{2})\lambda_{4} + 8\lambda_{3}\lambda_{4} + 4\lambda_{4}^{2} + 8|\lambda_{5}|^{2} + 3g^{2}g'^{2} - w\lambda_{4} + 6\lambda_{4}(y_{t}^{2} + y_{b}^{2}) + 12y_{t}^{2}y_{b}^{2},\\
16\pi^{2}\beta_{\lambda_{5}} &= \lambda_{5}\bigl(2(\lambda_{1} + \lambda_{2}) + 8\lambda_{3} + 12\lambda_{4} - w + 6(y_{t}^{2} + y_{b}^{2})\bigr),
\end{align*}
and $\beta_{\lambda_{2}}$ is $\beta_{\lambda_{1}}$ with $\lambda_{1} \to \lambda_{2}$, $y_{b} \to y_{t}$ \cite{HaberHempfling1993, FerreiraJones2009, Branco2012}.
\end{enumerate}

## technical
The running of quartic scalar couplings in any renormalisable gauge theory is known in closed form: at one loop it is a sum of a quadratic term in the quartics, an anomalous-dimension term from gauge and Yukawa couplings, a Yukawa box and a gauge box; at two loops the terms with quartics alone are a cubic term and a product of the one-loop scalar anomalous dimension with the quartic. Specialised to two Higgs doublets with a discrete symmetry and the type-II assignment of the top and bottom couplings, these give the standard one-loop equations for the five quartics, in which the gauge couplings and the top and bottom couplings enter as stated.

## lay
How strongly the Higgs-type fields push on one another changes with the energy at which they are probed, by an amount that can be calculated once and for all for any theory of this kind. The general formulas, and their standard form for a theory with two Higgs fields, are taken from the literature; the series uses them to follow its own Higgs field's couplings up in energy.

## one-liner
General quartic running: $16\pi^{2}\beta^{(1)} = \Lambda^{2} - 8\kappa H + 2\kappa\Lambda^{Y} - 3g^{2}\Lambda^{S} + 3g^{4}A$, two-loop pure-quartic part $\tfrac{1}{12}\sum\Lambda^{2}\lambda - \bar{\Lambda}^{3}$ (Machacek-Vaughn; Luo-Wang-Xiao); the type-II two-doublet one-loop equations, $16\pi^{2}\beta_{\lambda_{1}} = 12\lambda_{1}^{2} + 4\lambda_{3}^{2} + 4\lambda_{3}\lambda_{4} + 2\lambda_{4}^{2} + 2|\lambda_{5}|^{2} + \ldots$ (Haber-Hempfling; Branco et al.).
