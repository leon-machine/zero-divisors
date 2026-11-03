---
id: synthesis.imported-b-meson-mixing-inputs-vacuum-insertion-lattice-and-tree-level-quark-mixing
kind: claim
version: 1
title: 'Imported: the inputs of a neutral-meson mixing bound; the $\Delta F = 2$ operators and their vacuum-insertion matrix elements (Gabbiani et al. 1996), the lattice decay constants (FLAG 2024) and bag parameters (HPQCD 2019), the measured $B_{s}$ and $B_{d}$ mass differences (PDG 2025), and the quark-mixing determinations that do not use $B$ mixing (tree-level $|V_{cb}|$, $|V_{ub}|$, $\gamma$ and the other direct moduli, PDG 2025), with three-family unitarity'
status: imported
region: synthesis
subject: standard-model
tags: [flavour-and-mixing, confronted-with-data, classical-theorem]
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
- citation: 'F. Gabbiani, E. Gabrielli, A. Masiero and L. Silvestrini, A complete analysis of FCNC and CP constraints in general SUSY extensions of the standard model, Nucl. Phys. B 477 (1996), 321--352; arXiv:hep-ph/9604387.'
  key: Gabbiani1996
  locator: 'Eq. (3) (operators Q1 to Q5) and Eq. (8) (vacuum-insertion matrix elements)'
  doi: 10.1016/0550-3213(96)00390-2
- citation: 'Flavour Lattice Averaging Group (FLAG), Y. Aoki et al., FLAG Review 2024; arXiv:2411.04268.'
  key: FLAG2024
  locator: 'Table 1 (f_K+-, Nf = 2+1+1), Table 2 (f_B, f_Bs, Nf = 2+1+1)'
- citation: 'R. J. Dowdall, C. T. H. Davies, R. R. Horgan, G. P. Lepage, C. J. Monahan, J. Shigemitsu and M. Wingate (HPQCD), Neutral B-meson mixing from full lattice QCD at the physical point, Phys. Rev. D 100 (2019), 094508; arXiv:1907.01025.'
  key: HPQCD2019
  locator: 'Table VI (bag parameters B1 to B5 for B_s and B_d, MS-bar at mu = m_b)'
- citation: 'S. Navas et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110 (2024), 030001, and its 2025 update: the review of the CKM quark-mixing matrix (rpp2025-rev-ckm-matrix) and the B mixing averages of the Heavy Flavour Averaging Group for the 2025 edition.'
  key: PDG2025
  doi: 10.1103/PhysRevD.110.030001
extraction:
  note: >-
    Imported, by Leon's list of routine imports, so that the B-meson mixing result can pin its hadronic and
    mixing inputs instead of carrying them as citations. Checked on 2 November 2026: Gabbiani et al., the arXiv
    text of hep-ph/9604387, Eq. (3) (Q1 to Q5 with their colour structures; the tilde operators by L <-> R) and
    Eq. (8) (vacuum-insertion matrix elements with all B parameters set to one; the extracted text of Eq. (8) is
    partly garbled, and the forms stated here, Q2 = -(5/24) R and Q4 = (1/24 + R/4), both times m_M f_M^2, agree
    with the legible fragments); the journal data are from memory. FLAG 2024: the arXiv record (title, authors,
    DOI 10.1103/nfzp-p5dn) and the summary tables, f_B = 190.0(1.3) MeV, f_Bs = 230.3(1.3) MeV, f_K+- =
    155.7(3) MeV for Nf = 2+1+1. HPQCD 2019: the ar5iv text of arXiv:1907.01025, Table VI, B_s: B2 = 0.817(43),
    B4 = 1.033(47); B_d: B2 = 0.769(44), B4 = 1.077(55); MS-bar at mu = m_b; journal data from memory. PDG 2025:
    the HFLAV page of averages for the 2025 edition, Delta m_d = 0.5069 +- 0.0019 ps^-1, Delta m_s = 17.765 +-
    0.006 ps^-1; the 2025 CKM review, |V_cb| = (41.1 +- 1.2) x 10^-3 (inclusive and exclusive semileptonic
    average, error scaled by 3.0), |V_ub| = (3.82 +- 0.20) x 10^-3, gamma = (65.7 +- 3.0) degrees, |V_us| =
    0.22431 +- 0.00085, |V_cd| = 0.221 +- 0.004, |V_cs| = 0.975 +- 0.006, |V_tb| = 1.010 +- 0.027, the direct
    |V_ts| = (41.5 +- 0.9) x 10^-3 and |V_td| = (8.6 +- 0.2) x 10^-3 from B mixing with lattice inputs, and the
    global-fit values. The unitarity relations of (v) are the standard Wolfenstein ones, cited from memory.
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Created by the maintainer pass of 2 November 2026, by Leon''s list of routine imports (Gabbiani et al. 1996 vacuum insertion, FLAG 2024 decay constants, HPQCD 2019 bag parameters, PDG 2025 mixing data and tree-level-plus-unitarity quark mixing), as one Fact for the B-meson mixing result.'
---

## formal
\begin{enumerate}
\item[(i)] \emph{(Operators and vacuum insertion.)} For a neutral meson $M = (q\bar{q}')$, with colour indices $\alpha$, $\beta$, the $\Delta F = 2$ operators include $Q_{2} = \bar{q}^{\alpha}_{R}q'^{\alpha}_{L}\,\bar{q}^{\beta}_{R}q'^{\beta}_{L}$ and $Q_{4} = \bar{q}^{\alpha}_{R}q'^{\alpha}_{L}\,\bar{q}^{\beta}_{L}q'^{\beta}_{R}$, with $\tilde{Q}_{2}$ obtained by $L \leftrightarrow R$; in the vacuum-insertion approximation, with the bag parameters restored and relativistic normalisation, $\langle\bar{M}|Q_{2}|M\rangle = -\tfrac{5}{24}R\,m_{M}f_{M}^{2}B_{2}$ and $\langle\bar{M}|Q_{4}|M\rangle = (\tfrac{1}{24} + \tfrac14R)\,m_{M}f_{M}^{2}B_{4}$, $R = (m_{M}/(m_{q} + m_{q'}))^{2}$ \cite[Eqs.~(3), (8)]{Gabbiani1996}.
\item[(ii)] \emph{(Decay constants, $N_{f} = 2 + 1 + 1$.)} $f_{B} = 190.0(1.3)$ MeV, $f_{B_{s}} = 230.3(1.3)$ MeV, $f_{K^{\pm}} = 155.7(3)$ MeV \cite{FLAG2024}.
\item[(iii)] \emph{(Bag parameters, $\overline{\mathrm{MS}}$ at $\mu = m_{b}$.)} For $B_{s}$, $B_{2} = 0.817(43)$, $B_{4} = 1.033(47)$; for $B_{d}$, $B_{2} = 0.769(44)$, $B_{4} = 1.077(55)$ \cite[Table VI]{HPQCD2019}.
\item[(iv)] \emph{(Mass differences.)} $\Delta m_{s} = 17.765 \pm 0.006$ ps$^{-1}$ and $\Delta m_{d} = 0.5069 \pm 0.0019$ ps$^{-1}$ \cite{PDG2025}.
\item[(v)] \emph{(Quark mixing without $B$ mixing.)} From tree-level processes: $|V_{cb}| = (41.1 \pm 1.2) \times 10^{-3}$ (semileptonic $b \to c$, inclusive and exclusive average), $|V_{ub}| = (3.82 \pm 0.20) \times 10^{-3}$, $\gamma = (65.7 \pm 3.0)^{\circ}$, the tree-level kaon-decay determination of $|V_{us}|$, $0.22431 \pm 0.00085$ (not the global-fit value of the stored quantity, since the global fit uses $B$ mixing), $|V_{cd}| = 0.221 \pm 0.004$, $|V_{cs}| = 0.975 \pm 0.006$, $|V_{tb}| = 1.010 \pm 0.027$ \cite{PDG2025}. The direct values $|V_{ts}| = (41.5 \pm 0.9) \times 10^{-3}$ and $|V_{td}| = (8.6 \pm 0.2) \times 10^{-3}$ are extracted from $\Delta m_{s}$ and $\Delta m_{d}$ with lattice inputs, so they are valid only when mixing has no other tree-level contribution. Three-family unitarity fixes $|V_{ts}|$ and $|V_{td}|$ from the tree-level moduli and $\gamma$: $|V_{ts}| = |V_{cb}|(1 + O(\lambda^{2}))$ and $|V_{td}| = \lambda|V_{cb}|(1 - 2R_{u}\cos\gamma + R_{u}^{2})^{1/2}(1 + O(\lambda^{2}))$, $\lambda = |V_{us}|$, $R_{u} = |V_{ub}|/(\lambda|V_{cb}|)(1 + O(\lambda^{2}))$.
\end{enumerate}

## technical
These are the inputs any tree-level bound on neutral-meson mixing from a new scalar needs. The scalar's exchange produces the left-right operators $Q_{2}$ and $Q_{4}$; their matrix elements between a meson and its antiparticle are the vacuum-insertion forms of Gabbiani and collaborators corrected by lattice bag parameters, with the decay constants from the FLAG averages and the bag parameters from HPQCD. The measured mass differences are the Particle Data Group averages. Quark mixing must not be taken from the $B$-mixing extractions when a new tree-level contribution is under test; the tree-level determinations of $|V_{cb}|$, $|V_{ub}|$ and the angle $\gamma$, with unitarity of the three-family matrix, fix $|V_{ts}|$ and $|V_{td}|$ independently.

## lay
Mesons made of a bottom quark and a lighter antiquark turn into their own antiparticles and back at rates measured to a fraction of a percent. To test whether a new particle would speed this up, one needs how strongly the quarks are bound in the meson, taken from large lattice computations, the measured rates, and how the quark types mix, taken from decays that the new particle would not affect. The series takes all of these from the standard compilations.

## one-liner
Vacuum insertion $\langle Q_{2}\rangle = -\tfrac{5}{24}Rm f^{2}B_{2}$, $\langle Q_{4}\rangle = (\tfrac{1}{24} + \tfrac{R}{4})mf^{2}B_{4}$ (Gabbiani et al.); $f_{B} = 190.0(1.3)$, $f_{B_{s}} = 230.3(1.3)$, $f_{K} = 155.7(3)$ MeV (FLAG 2024); $B_{4} = 1.033(47)$, $1.077(55)$ and $B_{2} = 0.817(43)$, $0.769(44)$ for $B_{s}$, $B_{d}$ (HPQCD 2019); $\Delta m_{s} = 17.765(6)$, $\Delta m_{d} = 0.5069(19)$ ps$^{-1}$; tree-level $|V_{cb}| = 41.1(1.2) \times 10^{-3}$, $|V_{ub}|$, $\gamma$ with unitarity (PDG 2025).
