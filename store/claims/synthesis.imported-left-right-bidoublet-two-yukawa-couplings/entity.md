---
id: synthesis.imported-left-right-bidoublet-two-yukawa-couplings
kind: claim
version: 1
title: 'Imported: in the left-right symmetric model the quark bidoublet $\Phi$ couples through two family matrices, $h$ on $\Phi$ and $\tilde{h}$ on $\tilde{\Phi} = \tau_{2}\Phi^{*}\tau_{2}$, giving $M_{U} = \kappa h + \kappa''e^{-\mathrm{i}\theta}\tilde{h}$ and $M_{D} = \kappa''e^{\mathrm{i}\theta}h + \kappa\tilde{h}$'
status: imported
region: synthesis
subject: standard-model
tags: [flavour-and-mixing, mass-generation, symmetry-breaking, classical-theorem]
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
- citation: 'G. Senjanovic and R. N. Mohapatra, Exact left-right symmetry and spontaneous violation of parity, Phys. Rev. D 12 (1975), 1502.'
  key: SenjanovicMohapatra1975
  doi: 10.1103/PhysRevD.12.1502
- citation: 'Y. Zhang, H. An, X. Ji and R. N. Mohapatra, General CP violation in minimal left-right symmetric model and constraints on the right-handed scale, arXiv:0712.4218, equations (7), (12) and (13).'
  key: ZhangAnJiMohapatra2008
  doi: 10.1016/j.nuclphysb.2008.05.019
extraction:
  note: >-
    Imported so that the coupling-to-conjugate result can pin the standard two-coupling structure of a
    complex bidoublet, which it cited from memory. Checked on 2026-11-01: the bibliographic data of
    Senjanovic and Mohapatra (title, Phys. Rev. D 12, 1502, 1975, DOI) against its INSPIRE record; the
    Lagrangian, the conjugate bidoublet and the mass matrices against Zhang, An, Ji and Mohapatra,
    arXiv:0712.4218: equation (12), L_Y = Qbar_L (h phi + htilde phitilde) Q_R + h.c. with family indices
    i, j = 1, 2, 3; the definition phitilde = -i tau_2 phi^* i tau_2 = tau_2 phi^* tau_2; equation (7),
    <phi> = diag(kappa, kappa' e^{i alpha}); equation (13), M_U = kappa h + kappa' e^{-i alpha} htilde and
    M_D = kappa' e^{i alpha} h + kappa htilde. The DOI of that paper is from its arXiv record; its journal
    volume and page are not stated here. That left-right parity makes h and htilde Hermitian (or symmetric,
    by the choice of parity) is cited from memory and is not part of the statement. The reading in the
    series' chart is an exact identification of formulas, checked by hand against the stored mass matrices.
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Created by the maintainer pass of 2026-11-01 (the standard left-right bidoublet coupling structure as a Fact, by Leon''s further imports).'
---

## formal
In the left-right symmetric model with gauge group $SU(2)_{L} \times SU(2)_{R} \times U(1)_{B - L}$ and a complex bidoublet $\Phi$ in $(2, 2, 0)$, the most general quark Yukawa coupling to the bidoublet is
\[
\mathcal{L}_{Y} = \bar{Q}_{L}\bigl(h\,\Phi + \tilde{h}\,\tilde{\Phi}\bigr)Q_{R} + \text{h.c.}, \qquad \tilde{\Phi} = \tau_{2}\Phi^{*}\tau_{2},
\]
with two independent $3 \times 3$ family matrices $h$ and $\tilde{h}$; $\tilde{\Phi}$ transforms under $SU(2)_{L} \times SU(2)_{R}$ as $\Phi$ does. With $\langle\Phi\rangle = \operatorname{diag}(\kappa, \kappa'e^{\mathrm{i}\theta})$, $\kappa$, $\kappa'$, $\theta$ real ($\theta$ is the phase the cited form calls $\alpha$), the quark mass matrices are
\[
M_{U} = \kappa h + \kappa'e^{-\mathrm{i}\theta}\tilde{h}, \qquad M_{D} = \kappa'e^{\mathrm{i}\theta}h + \kappa\tilde{h}.
\]
\emph{Provenance:} \cite{SenjanovicMohapatra1975}; the displayed form as in \cite{ZhangAnJiMohapatra2008}, equations (7), (12), (13).

\emph{Reading in the series' chart (identification of formulas, not part of the import).} With the rung-$4$ components of the rung field read as $\alpha \leftrightarrow \kappa$, $\beta \leftrightarrow \kappa'e^{\mathrm{i}\theta}$, $Y \leftrightarrow h$ and $\tilde{Y} \leftrightarrow \tilde{h}$, these are the mass matrices $M_{u} = \alpha Y + \bar{\beta}\tilde{Y}$, $M_{d} = \beta Y + \bar{\alpha}\tilde{Y}$ of the coupling $Yc + \tilde{Y}c^{*}$ of the rung field and its conjugate.

## technical
In the left-right symmetric extension of the Standard Model the Higgs field that gives the quarks their masses is a bidoublet, a doublet of both the left-handed and the right-handed weak isospin. It and its conjugate transform alike, so the quarks can couple to each with its own family matrix. The two vacuum values of the bidoublet then mix the two matrices, one combination giving the up-type masses and the other the down-type masses; with one matrix only, the up-type and down-type mass matrices would be proportional.

## lay
In left-right symmetric theories, which treat left-handed and right-handed particles alike at high energies, the Higgs field and its mirror image can each couple to the quarks with their own strengths. The up-type and down-type quark masses then come from different mixtures of the two couplings, which is how such theories let the top quark be much heavier than the bottom quark.

## one-liner
Left-right model: $\bar{Q}_{L}(h\Phi + \tilde{h}\tilde{\Phi})Q_{R}$ with two family matrices gives $M_{U} = \kappa h + \kappa'e^{-\mathrm{i}\theta}\tilde{h}$, $M_{D} = \kappa'e^{\mathrm{i}\theta}h + \kappa\tilde{h}$ (Senjanovic and Mohapatra 1975).
