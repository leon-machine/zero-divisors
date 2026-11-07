---
id: synthesis.second-doublet-of-one-family-coupling-gives-no-quark-mixing
kind: claim
version: 2
title: 'A second doublet of one family coupling gives no quark mixing'
status: proved
region: synthesis
subject: standard-model
tags: [no-go, symmetry-breaking]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'consistency pass, imaginary unit in the Jarlskog identity written as I_4'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - standard-model.one-vev-vector-relations-breaking-pattern@7
  - standard-model.bidoublet-complex@11
  - standard-model.imported-clebsch-structure-seesaw@1
  - synthesis.residual-s2-fixes-120-family-form@1
  - neutrino.breaking-relation@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_proportional_coupling_gives_no_mixing
- kind: check
  ref: check.py::check_s3_invariant_couplings_are_degenerate
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.bidoublet-complex
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The proof''s quotation of Jarlskog''s identity writes the unit as I_4 (det[H_u, H_d] = 2 I_4 J prod ...), matching the restated Fact synthesis.imported-jarlskog-commutator-identity (numbers in span{1, I_4}).'
  open_problem: op.rung-unit
  note: >-
    The problem's third line of attack (find the second coupling that splits up-type from down-type
    masses under the c* reading), answered by an obstruction from electroweak data. The stored
    bidoublet result says a second doublet coupling is needed and that a complex bidoublet supplies
    one. This result says what kind of coupling. A second doublet vev of the same family coupling (a
    tan-beta between the bidoublet's two doublets) is not enough: then M_u is a multiple of M_d, all
    three up/down ratios are equal and the CKM matrix is the identity. The record says otherwise:
    m_u/m_d about 0.44, m_c/m_s about 11 and m_t/m_b about 59 at M_Z, and |V_us| about 0.225 (values
    cited from memory: Particle Data Group, and the M_Z running-mass table of Xing, Zhang and Zhou 2008, Phys. Rev. D 77, 113016). So
    the second coupling must be a family matrix not proportional to the first (a second 10 with its
    own Yukawa, the 126 or the 120), with det[H_u, H_d] != 0 for three families. This is the standard
    single-10 relation of SO(10) model building (one Yukawa matrix, real or complex 10, gives M_u
    proportional to M_d and V = 1), applied to the c* reading; it qualifies standard-model.bidoublet-complex,
    whose complex bidoublet supplies the up/down scale ratio but not the family pattern. Filed
    alongside, synthesis.residual-s2-decouples-first-family-from-ckm-and-pmns proves the common-eigenvector
    lemma of clause (1) in general and the residual-S2 case (S2-respecting couplings share the
    eigenvector (1, -1, 0)); this result does not repeat it. Fully S3-invariant couplings are a special
    case of that one, and here they are recorded only for their degenerate spectrum (eigenvalues alpha,
    alpha, alpha + 3 beta), which the record excludes before mixing is considered. Literature cited from memory: the Jarlskog determinant identity
    (Jarlskog 1985), and the fact that one-loop running preserves [H_u, H_d] = 0. Transport-absent:
    this is linear algebra of mass matrices, on the series' couplings.
---

## formal
Let $M_{u}$, $M_{d}$ be the up-type and down-type Dirac mass matrices at $M_{I}$ in the form of Fact \claimref{standard-model.imported-clebsch-structure-seesaw}, $H_{q} = M_{q}M_{q}^{\dagger}$, and $V$ the CKM matrix, the overlap of the eigenbases of $H_{u}$ and $H_{d}$ (masses nondegenerate in each sector).
\begin{enumerate}
\item \emph{(Commuting squares.)} If $[H_{u}, H_{d}] = 0$, then $V$ is a permutation matrix up to phases and the Jarlskog invariant vanishes (a case of the common-eigenvector lemma of the result filed alongside, synthesis.residual-s2-decouples-first-family-from-ckm-and-pmns).
\item \emph{(One coupling.)} Suppose every coupling entering $M_{u}$ and $M_{d}$ is a multiple of one family matrix $Y$. This covers one rung coupling read through $c^{*}$ as in Corollary \claimref{standard-model.one-vev-vector-relations-breaking-pattern} with any number of doublet vevs, and a complex bidoublet with a single coupling (Proposition \claimref{standard-model.bidoublet-complex}). Then $M_{u} = rM_{d}$ for one complex number $r$, so $m_{u_{i}}/m_{d_{i}} = |r|$ for every family and $V = 1$.
\item \emph{($S_{3}$-invariant couplings.)} If every coupling is invariant under the family $S_{3}$ of Lemma \claimref{neutrino.breaking-relation}, then each coupling is $\alpha 1 + \beta\J$ and no $120$ is allowed (Proposition \claimref{synthesis.residual-s2-fixes-120-family-form}(i)), so every mass matrix and its square has eigenvalues $\alpha, \alpha, \alpha + 3\beta$: two degenerate families in every sector, which the record excludes, and the mixing is undetermined. (The general residual-$S_{2}$ case, of which this is a special case, is the result filed alongside, synthesis.residual-s2-decouples-first-family-from-ckm-and-pmns.)
\item \emph{(Against the record.)} The record has three different up/down ratios, $|V_{us}| \approx 0.225$ and $J \ne 0$ (cited from memory). So under the $c^{*}$ reading the up/down split needs a second coupling that is a family matrix independent of the first, and for three families $\det[H_{u}, H_{d}] \ne 0$; a second vev of the rung coupling does not supply it, and an $S_{3}$-symmetric completion is already excluded by its degenerate spectrum.
\end{enumerate}

## technical
Quark mixing measures how far apart the mass eigenbases of the up and down sectors are. A single rung coupling read through any number of doublet vevs makes $M_{u}$ a multiple of $M_{d}$. This includes the complex bidoublet with one Yukawa matrix, where the two doublets differ only by a ratio of vevs. The consequence is one up/down ratio for all three families and no mixing at all. Couplings invariant under the full family permutation group leave two families degenerate in every sector, which the record excludes before mixing is considered. The record has three very different up/down ratios and a nonzero Cabibbo angle. So the second coupling the up/down split needs must be a genuinely different family matrix, not a second vev of the same coupling. The residual-$S_{2}$ result filed alongside, synthesis.residual-s2-decouples-first-family-from-ckm-and-pmns, shows that such a matrix must also break the residual $S_{2}$ to produce the Cabibbo angle.

## lay
Quarks of the up kind and the down kind mix with each other, by angles that are measured. Mixing happens only when the two kinds' mass patterns do not line up. One natural way to make up-type quarks heavier than down-type ones is to use the same coupling twice with two different strengths. That scales every up-type mass by one common factor and lines the patterns up exactly. The result would be the same mass ratio in every family and no mixing, and neither fits the measurements. So the series needs a genuinely different second coupling.

## one-liner
A second doublet vev of the same family coupling gives $M_{u} = rM_{d}$, one up/down ratio for every family and $V = 1$, and $S_{3}$-invariant couplings leave two families degenerate; so the series' up/down split needs an independent second family matrix.
