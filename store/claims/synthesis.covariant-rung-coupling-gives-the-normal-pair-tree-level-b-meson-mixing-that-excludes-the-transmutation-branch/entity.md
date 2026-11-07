---
id: synthesis.covariant-rung-coupling-gives-the-normal-pair-tree-level-b-meson-mixing-that-excludes-the-transmutation-branch
kind: claim
version: 4
title: 'B-meson mixing excludes the transmutation branch under covariant coupling'
status: proved
region: synthesis
subject: standard-model
tags: [flavour-and-mixing, symmetry-breaking, confronted-with-data, no-go]
proposed_by:
  kind: ai
  session: 2026-11-02-qft-full
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: 'consistency pass, bare i in a unit aside removed'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: draft
imported_from:
- citation: 'F. Gabbiani, E. Gabrielli, A. Masiero and L. Silvestrini, A complete analysis of FCNC and CP constraints in general SUSY extensions of the standard model, Nucl. Phys. B 477 (1996), 321--352; arXiv:hep-ph/9604387.'
  key: Gabbiani1996
  locator: 'Eq. (3) (operators Q1 to Q5) and Eq. (8) (vacuum-insertion matrix elements)'
  doi: 10.1016/0550-3213(96)00390-2
- citation: 'S. Navas et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110 (2024), 030001, and its 2025 update (pdg.lbl.gov): the B mixing mass differences and the quark mixing review.'
  key: PDG2025
  doi: 10.1103/PhysRevD.110.030001
- citation: 'Flavour Lattice Averaging Group (FLAG), FLAG Review 2024; arXiv:2411.04268.'
  key: FLAG2024
- citation: 'R. J. Dowdall, C. T. H. Davies, R. R. Horgan, G. P. Lepage, C. J. Monahan, J. Shigemitsu and M. Wingate (HPQCD), Neutral B-meson mixing from full lattice QCD at the physical point, Phys. Rev. D 100 (2019), 094508; arXiv:1907.01025.'
  key: HPQCD2019
  locator: 'Table VI (bag parameters B2, B4 for B_s and B_d)'
- citation: 'S. Bertolini, A. Maiezza and F. Nesti, Present and future K and B meson mixing constraints on TeV scale left-right symmetry, Phys. Rev. D 89 (2014), 095028; arXiv:1403.7112.'
  key: BertoliniMaiezzaNesti2014
  doi: 10.1103/PhysRevD.89.095028
quantities:
- quantity.fermi-scale@1
derivations:
- name: main
  uses:
  - synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix@3
  - synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum@4
  - synthesis.imported-takagi-factorisation@1
  - synthesis.imported-left-right-bidoublet-two-yukawa-couplings@3
  - synthesis.imported-b-meson-mixing-inputs-vacuum-insertion-lattice-and-tree-level-quark-mixing@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_normal_pair_couples_down_quarks_through_the_up_mass_matrix
- kind: check
  ref: check.py::check_integrating_out_the_normal_pair
- kind: check
  ref: check.py::check_flavour_changing_entries_are_bounded_below
- kind: check
  ref: check.py::check_tree_level_mixing_exceeds_the_measured_mass_differences
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum
  - synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The formal level''s aside ''(i = I_4 on rung values ...)'' wrote a bare i to name the unit; it now says the unit is the field theory''s I_4 there. The letter A names both the pseudoscalar component of phi and the coupling matrix V^dag M_u V^*; that clash is listed for Leon, not changed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The bare i that the formal level and the proof had kept as the number convention of the imported four-quark operators is written as I_4: in the bidoublet form e^{-+ I_4 theta}, in phi = (H + I_4 A)/sqrt 2 of step 3 (the same field as in step 1) and in the source K_A = I_4 (J^dagger - J)/sqrt 2, the bilinears J being number-valued; the sentences that set i apart as that convention now say the unit is I_4 there too; nothing stays.'
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s decisions of 2 November 2026: a uses edge to the new imported Fact synthesis.imported-b-meson-mixing-inputs-vacuum-insertion-lattice-and-tree-level-quark-mixing@1 (Gabbiani et al. vacuum insertion, FLAG 2024 decay constants, HPQCD 2019 bag parameters, PDG 2025 mass differences and tree-level quark mixing with unitarity), cited by claimref in the formal level and the proof and touched by the checks of the CKM bounds and of the mixing excess; the quartic-running result is cited by claimref in the proof and by id in the note, with no edge. Pin of synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum moved to @3 (dated note recording the transmutation branch as excluded on this result among others; spectrum unchanged). Statement unchanged; by Leon''s decision the branch with a level is now the working branch.'
  open_problem: op.qft-bosons-and-the-rung-field
  note: >-
    Answers the attack line on collider and precision limits for the neutral normal pair and the charged pair
    below 456 GeV, by the limit that turns out to decide it: neutral-meson mixing. The stored coupling reading
    (Leon's decision of 1 November: the su(2)_R-covariant completion Y c + Ytilde c*) is the left-right
    bidoublet structure with kappa' = 0 at the vacuum alpha = 0 (Fact
    synthesis.imported-left-right-bidoublet-two-yukawa-couplings): the doublet without a vacuum value couples
    down quarks through Ytilde = -M_u/v and up quarks through Y = -M_d/v. For complex symmetric Y, Ytilde (the
    rung 10 of the stored statement), Takagi forms give in the down mass basis the matrix A = V^dag Mhat_u V^*,
    symmetric, with |A_jk| = |sum_i V_ij V_ik m_i|; the relative phases are physical (Takagi leaves only signs)
    and free, so the bounds take the worst phase. Standard: the tree-level flavour-changing neutral Higgs problem
    of a bidoublet with one vacuum value (minimal left-right model; Ecker and Grimus 1985, from memory); Bertolini,
    Maiezza and Nesti (2014, ar5iv text read 2 November 2026) find the flavour-changing Higgs "always above 20
    TeV" from B mixing in the minimal model, consistent with the weaker bound here (which drops the QCD
    enhancement). New: the series' coupling reading has this structure, and the stored scalon sum puts the
    flavour-changing doublet below 542 GeV. Inputs, imported and taken as conservative rational ranges in the
    check: |V_ts| in [0.0376, 0.0425] and |V_td| in [0.0078, 0.0092] from the tree-level determinations (|V_cb|
    from semileptonic b -> c decays, |V_ub|, the angle gamma) and three-family unitarity, not from the PDG
    direct values, which are extracted from Delta M_s and Delta M_d and so assume no new tree-level
    contribution; the other moduli widened from PDG 2025; running masses at 100 to 600 GeV, m_t in [140, 172]
    GeV, m_c in [0.50, 0.70] GeV (from memory); Delta M_s = 17.765(6) ps^-1, Delta M_d = 0.5069(19) ps^-1 (PDG
    2025 via HFLAV), Delta M_K = 3.484e-15 GeV; f_Bs >= 0.228, f_Bd >= 0.187, f_K >= 0.1554 GeV (FLAG 2024:
    230.3(1.3), 190.0(1.3), 155.7(3) MeV); bag parameters B4 >= 0.85 and B2 <= 0.95 for B mesons (HPQCD 2019,
    Table VI: B4 = 1.033(47), 1.077(55); B2 = 0.817(43), 0.769(44)), B4 >= 0.70 for the kaon (from memory);
    (m_b + m_s), (m_b + m_d) <= 4.30 GeV, (m_s + m_d)(2 GeV) <= 0.100 GeV; vacuum-insertion forms of Gabbiani
    et al. (Eq. (8), checked against the arXiv text on 2 November 2026); the QCD running factor of the operators
    from the scalar mass down is set to one, which can only weaken the bound (the leading-order anomalous
    dimension of the scalar LR operator is minus twice that of a mass, as stated by Bertolini, Maiezza and
    Nesti). v = quantity.fermi-scale plus 1 GeV. Free numbers: none; the exclusion uses the stored upper bound
    542 GeV on both normal masses. With central inputs the excess is about 94 (B_s) and 100 (B_d) before QCD
    running (computed). See also synthesis.rung-field-quartics-run-to-strong-coupling-within-a-few-tev-on-the-transmutation-branch,
    which finds the same branch strongly coupled at a few TeV with the same coupling reading. Also checked (not
    part of the claim; dated 2 November 2026): the Particle Data Group 2026 average mu_gamma_gamma = 1.10 +-
    0.06 (pdglive), so the stored bound mu_gamma_gamma < 0.900 is now 3.3 standard deviations low,
    independently of this result. Transport-absent in the flavour physics; the coupling reading and the field
    are the series'.
  flags:
  - 'the hadronic inputs (decay constants, bag parameters, quark masses, CKM ranges, mass differences) are imported with conservative ranges; decay constants, B-meson bag parameters, mass differences and the vacuum-insertion forms checked against their sources, the running quark masses and the kaon bag parameter from memory'
  - 'the QCD running factor of the four-quark operators is set to one, which only weakens the bound'
  - 'the result needs Y and Ytilde complex symmetric; for general family matrices a tuned right-handed mixing can make A triangular and remove the LR operator in every pair, at the price of an O(m_t) flavour-changing entry that then requires |m_H^2 - m_A^2|/m^2 of order 1e-5 (argued), so the exclusion is then not established'
  - 'clause (iv), the level branch, is a conservative lower bound (degenerate pair, no running) plus an argued statement on the charged pair that uses the perturbativity convention |k10 +- r| <= pi'
  - 'one-loop contributions (charged-pair boxes) are not computed; they are loop suppressed against a tree-level excess of more than 50'
---

## formal
Take the linear rung field of \claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum} at a vacuum with $\alpha = 0$, $\beta = (-v, 0)$ (eight real components with kinetic coefficient one, so $|\beta| = v$), coupled to quarks as in \claimref{synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix}, $M_{d} = \beta Y + \bar{\alpha}\tilde{Y}$, $M_{u} = \alpha Y + \bar{\beta}\tilde{Y}$ on rung-$4$ components, with $Y$, $\tilde{Y}$ complex symmetric (the rung $10$). Let $M_{q} = U_{q}\hat{M}_{q}U_{q}^{\mathsf T}$ be Takagi forms (Fact \claimref{synthesis.imported-takagi-factorisation}) and $V = U_{u}^{\dagger}U_{d}$, whose moduli are those of the quark mixing matrix. The normal pair is the direction $\alpha_{4} = \sqrt2\,\phi$, $\phi = (H + I_{4}A)/\sqrt2$ (the unit is the field theory's $I_{4}$ on rung values and on the number-valued quark bilinears of the four-quark algebra below), with masses $m_{H}$, $m_{A}$.
\begin{enumerate}
\item[(i)] \emph{(Couplings; proved.)} In the down mass basis the normal pair enters as $-\kappa\bar{\phi}\,\bar{d}_{L}Ad_{R} + \mathrm{h.c.}$ with $\kappa = \sqrt2/v$ and $A = V^{\dagger}\hat{M}_{u}V^{*}$, symmetric, $|A_{jk}| = |\sum_{i}V_{ij}V_{ik}m_{u_{i}}|$; in the up mass basis it enters through $V\hat{M}_{d}V^{\mathsf T}$. This is the flavour structure of a left-right bidoublet with one vacuum value (Fact \claimref{synthesis.imported-left-right-bidoublet-two-yukawa-couplings}).
\item[(ii)] \emph{(Lower bounds; proved, given the imported ranges.)} For every choice of the relative phases, $|A_{sb}| \ge m_{t}|V_{ts}||V_{tb}| - m_{c}|V_{cs}||V_{cb}| - m_{u}|V_{us}||V_{ub}| > 5.18$ GeV, $|A_{db}| > 1.07$ GeV and $|A_{sd}| \ge m_{c}|V_{cs}||V_{cd}| - m_{t}|V_{ts}||V_{td}| - m_{u}|V_{us}||V_{ud}| > 0.035$ GeV, with running masses at any scale from $100$ to $600$ GeV and $|V_{ts}|$, $|V_{td}|$ from tree-level determinations and three-family unitarity.
\item[(iii)] \emph{(Tree-level mixing; proved form, computed bound.)} Integrating out $H$ and $A$ gives $\kappa^{2}\bigl(\tfrac{a + b}{2}A_{jk}\bar{A}_{kj}\,Q_{4} + \tfrac{a - b}{4}(A_{jk}^{2}Q_{2} + \bar{A}_{kj}^{2}\tilde{Q}_{2})\bigr)$ in the effective Lagrangian, $a = m_{H}^{-2}$, $b = m_{A}^{-2}$, $Q_{2}$, $Q_{4}$ the operators of \cite{Gabbiani1996}. With the vacuum-insertion matrix elements of \cite[Eq.~(8)]{Gabbiani1996} (Fact \claimref{synthesis.imported-b-meson-mixing-inputs-vacuum-insertion-lattice-and-tree-level-quark-mixing}(i)), $E_{4} = (\tfrac14R + \tfrac{1}{24})m_{M}f_{M}^{2}B_{4}$, $E_{2} = \tfrac{5}{24}Rm_{M}f_{M}^{2}B_{2}$, $R = (m_{M}/(m_{q} + m_{q'}))^{2}$, the contribution to $|M_{12}|$ is at least $\kappa^{2}|A_{jk}|^{2}F(a, b)$ with $F = \tfrac{a + b}{2}E_{4} - \tfrac{|a - b|}{2}E_{2}$. For $a \ge b$, $F = \tfrac{a}{2}(E_{4} - E_{2}) + \tfrac{b}{2}(E_{4} + E_{2})$, increasing in $a$ and $b$ when $E_{4} > E_{2}$, which holds for the $B$ mesons; so with both masses at most $542$ GeV the minimum is at $m_{H} = m_{A} = 542$ GeV, where the contribution exceeds $\tfrac12\Delta M$ by a factor of more than $52$ in $B_{s}$ and more than $50$ in $B_{d}$, for every splitting. For the kaon $E_{4} < E_{2}$ and the excess exceeds $4$ when $m_{H} = m_{A}$ (computed with the imported inputs of Fact \claimref{synthesis.imported-b-meson-mixing-inputs-vacuum-insertion-lattice-and-tree-level-quark-mixing}, the QCD running factor set to one).
\item[(iv)] \emph{(Consequences.)} Under the Gildener-Weinberg formula and decoupling of the Majorana and Pati-Salam sectors, \claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum}(4) puts $m_{H}, m_{A} < 542$ GeV, so by (iii) the scale-free (transmutation) branch of the rung field is excluded under the covariant coupling with symmetric family matrices: tree-level $B_{s}$ and $B_{d}$ mixing would exceed the measured values more than fifty times in magnitude, whatever the phases and the splitting (computed). On the branch with a level the normal masses $m_{H,A}^{2} = 2W' + 4N(k_{10} \pm r)$ are free, and allowing the new contribution up to $2.3$ times the measured $|M_{12}|$ requires, for equal masses, $m_{H} = m_{A}$ at least about $2.5$ TeV with these conservative inputs and no QCD running (computed); with $|k_{10} \pm r| \le \pi$ (perturbative quartics, $|\lambda_{4} \pm \lambda_{5}| \le 4\pi$) this needs $2W'$ of order $(2.4\ \mathrm{TeV})^{2}$ or more, so the charged pair, $m_{\pm}^{2} = M_{W}^{2} + 2W'$, is heavy too (argued).
\end{enumerate}

## technical
The series records the Higgs as the elementary linear rung field, two doublets, coupled to quarks through the field and its conjugate in the form that is covariant under the right-handed rotations: one family matrix on the field, one on its conjugate. At the vacuum only one doublet has a value, and the other doublet, which contains the neutral normal pair and the charged pair, then couples down quarks with the up-quark mass matrix and up quarks with the down-quark mass matrix. In the quark mass basis these couplings are not diagonal: the bottom-strange entry is the top mass times the mixing element $V_{ts}$, about $6$ GeV, and the bottom-down entry about $1.3$ GeV, with no freedom of phases that can remove them. This is the standard flavour-changing neutral Higgs bound of a bidoublet with one vacuum value; new is that the stored scalon sum makes the doublet light.

Exchanging the normal pair at tree level mixes $B_{s}$ with its antiparticle, and $B_{d}$ likewise. With conservative hadronic inputs, quark mixing taken from tree-level measurements and unitarity (the usual values of $|V_{ts}|$, $|V_{td}|$ come from the mixing itself), and both masses below the $542$ GeV that the stored scalon sum allows, the mixing exceeds the measured values more than fifty times for every split of the two masses; equal masses are the least constraining case. So the transmutation branch, on which the weak scale arises from quantum corrections, is excluded under the series' coupling reading with symmetric family matrices; with a level the second doublet can survive only at a few TeV or above.

## lay
The series' Higgs field contains a second set of particles. On the branch where all masses come from quantum effects, and under the approximations used there, these particles must weigh less than about 540 GeV. With the symmetric reading of how the series couples the Higgs field to quarks, the second set changes one kind of quark into another as it passes. Strange and bottom quarks bound into mesons would then turn into their antiparticles more than fifty times faster than is measured. So that branch is ruled out, unless the coupling to quarks is read differently.

## one-liner
Under the covariant rung coupling with symmetric family matrices the normal pair couples down quarks through $\sqrt2V^{\dagger}\hat{M}_{u}V^{*}/v$ ($|A_{sb}| > 5.18$, $|A_{db}| > 1.07$ GeV for every phase), and at tree level with both masses at most $542$ GeV it gives $B_{s}$, $B_{d}$ mixing more than $50$ times the measured values for every mass split, with imported hadronic inputs and tree-level-plus-unitarity quark mixing; so under Gildener-Weinberg and decoupling the transmutation branch is excluded (the standard flavour-changing neutral Higgs bound, applied to the doublet the scalon sum makes light), and with a level the second doublet is at least about $2.5$ TeV.
