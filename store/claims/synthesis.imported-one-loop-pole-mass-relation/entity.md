---
id: synthesis.imported-one-loop-pole-mass-relation
kind: claim
version: 1
title: 'Imported: the one-loop QCD pole-mass relation'
status: imported
region: synthesis
subject: generations
tags: [running-and-unification, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: S. Navas et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110 (2024) 030001.
  key: PDG2024
  locator: 'Review 60, Quark masses (R. M. Barnett, L. P. Lellouch and A. V. Manohar), Eq. (60.25)'
  doi: 10.1103/PhysRevD.110.030001
- citation: 'R. Tarrach, The pole mass in perturbative QCD, Nucl. Phys. B 183 (1981), 384--396.'
  key: Tarrach1981
extraction:
  note: >-
    Imported for synthesis.mass-ordered-dressing-cannot-spoil-koide, which uses the sign of the
    pole correction (pole masses above the MS-bar masses, by more for the lighter heavy quarks,
    since alpha_s(m_Q) is larger at lower m_Q) and cites it from memory. Checked on 2026-10-26
    against the PDG 2024 quark-mass review: Eq. (60.25), M_Q = m_Q(m_Q)[1 + 4 alpha_s(m_Q)/(3 pi) +
    ...], and the review's remark that the two- and three-loop terms are comparable to the
    one-loop term, a sign that the series is asymptotic. Tarrach 1981 as the original one-loop
    computation is cited from memory, with its bibliographic data. The relation is perturbative
    and applies to heavy quarks (c, b, t); the light-quark pole masses are not defined
    perturbatively.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Created by the maintainer pass of 2026-10-26 (Leon accepted the Koide-dressing result and asked for this import); checked against the PDG review, the original paper cited from memory.'
---

## formal
For a heavy quark $Q$, the pole mass $M_{Q}$ and the $\overline{\mathrm{MS}}$ mass at its own scale are related by
\[
M_{Q} = m_{Q}(m_{Q})\Bigl[1 + \frac{4\alpha_{s}(m_{Q})}{3\pi} + O(\alpha_{s}^{2})\Bigr],
\]
so at one loop the pole mass exceeds the $\overline{\mathrm{MS}}$ mass by the positive fraction $4\alpha_{s}(m_{Q})/3\pi$, which is larger for the lighter of two heavy quarks because $\alpha_{s}$ decreases with the scale. The higher-order terms are of comparable size to the one-loop term at the charm and bottom scales; the series is asymptotic. \emph{Provenance:} \cite{PDG2024} (Review 60, Eq. (60.25)), \cite{Tarrach1981}.

## technical
A heavy quark's mass can be defined as the position of the pole of its propagator or as the running mass of the minimal-subtraction scheme taken at its own scale. At one loop in the strong coupling the pole mass is larger, by the fraction $4\alpha_{s}/3\pi$ with the coupling evaluated at the quark's mass. Since the coupling is stronger at lower scales, the correction is relatively larger for charm than for bottom, and for bottom than for top. The higher-order corrections are not small at the charm and bottom scales, so the relation is used at the order stated.

## lay
There is more than one way to define the mass of a heavy quark. This standard result relates two common definitions: the so-called pole mass is a little larger than the running mass, by an amount that grows with the strength of the strong force, which is stronger for the lighter heavy quarks.

## one-liner
$M_{Q} = m_{Q}(m_{Q})(1 + 4\alpha_{s}(m_{Q})/3\pi + O(\alpha_{s}^{2}))$: the pole mass exceeds the $\overline{\mathrm{MS}}$ mass, by a larger fraction for the lighter heavy quarks.
