---
id: synthesis.stored-fits-are-models-of-not-u
kind: claim
version: 2
title: 'The stored Pati-Salam fits are models of not-(U)'
status: proved
region: synthesis
subject: neutrinos
tags: [hypothesis-u, confronted-with-data, neutrino-premises]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 2
  source: maintainer pass 2026-11-07 (GA units)
review: draft
derivations:
- name: main
  uses:
  - standard-model.fits-record-level@6
  - standard-model.imported-clebsch-structure-seesaw@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_charged_heavy_values
- kind: check
  ref: check.py::check_leading_dirac_values
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - dark-matter.hyp-u-equal-rank-one-eigenvalues
  - standard-model.fits-record-level
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The complex fitted entries f_22 and f_23 of the 126 coupling are written with I_4 in the technical level and the remark of the proof (numbers read in span{1, I_4}); nothing stays. Wording, to clear W222: "Dirac matrices" (the Dirac mass matrices, not gamma matrices) now reads "Dirac mass matrices".'
  open_problem: pr.u-equal-rank-one
  note: The four coupling sets are those of the Standard-Model paper's script verify_T12.py (Part M, STORED_FITS, the rows of obs:anglefits), copied digit for digit into the check as decimal strings and read as exact rationals; the check brackets singular values by Sturm sequences. Premise (EW) is a property of the sets (imposed exactly as in that script), not an assumption of this claim. Complements, filed alongside, synthesis.hypothesis-u-readings-on-the-rung-coupling-line (one family structure) and synthesis.hypothesis-u-under-ew-is-a-charged-fermion-condition ((EW) with independent family matrices); this is the stored two-structure case.
---

## formal
Take the four coupling sets of Proposition \claimref{standard-model.fits-record-level}, in the order of its table, with the Dirac mass matrices of Fact \claimref{standard-model.imported-clebsch-structure-seesaw} at $M_{I}$ and Premise (EW) imposed exactly, $Y_{33} = 3w_{u}f_{33}$, so that $(M_{\nu})_{33} = 0$. Read as exact rationals:
\begin{enumerate}
\item[(i)] in every set $\sigma_{\max}(M_{u}) \in (92.44, 92.46)$ GeV and $\sigma_{\max}(M_{d}) \in (1.3649, 1.3652)$ GeV, the top and bottom masses at $M_{I}$ that the fits target;
\item[(ii)] the leading singular value of the neutrino Dirac matrix is $\sigma_{\max}(M_{\nu}) \in (0.0543, 0.0544)$, $(3.160, 3.161)$, $(5.004, 5.005)$ and $(3.122, 3.123)$ GeV;
\item[(iii)] so in every set it differs from $m_{t}(M_{I})$ by a factor above $18$ and from $m_{b}(M_{I})$ by a factor above $2.2$, and the sets differ among themselves by a factor above $90$.
\end{enumerate}
Each set is therefore a model of Hypothesis (S), the Clebsch structure, Premise (EW), the Pati-Salam triplet vev and the eighteen fitted observables in which Hypothesis (U) (Postulate \claimref{dark-matter.hyp-u-equal-rank-one-eigenvalues}) fails at $M_{I}$ in both readings: those premises and data do not imply it. At the ceiling (argued, not computed): running from $M_{I}$ multiplies $m_{D}/m_{b}$ by a factor shared by the four sets to the extent that the neutrino Dirac couplings, below $0.03$ in units of the top's, feed back negligibly; a shared factor cannot bring sets differing by a factor $90$ to one value, so at most one of them can meet the bottom reading at the ceiling, and the top reading would need a shared factor above $18$. The claim is independence from these premises, not that (U) is false, and the sets, having more couplings than observables, predict nothing.

## technical
Hypothesis (U) puts the neutrino's leading Dirac eigenvalue at the common rank-one value of all sectors at the ceiling, read either as the top's or as the bottom's. The Standard-Model paper's fits on its Pati-Salam route reproduce all eighteen fitted observables with the equal-weight premise held exactly, and they leave the neutrino Dirac matrix to the couplings. Evaluated exactly from the stored coupling sets, its leading singular value at the intermediate scale is about $0.054$, $3.16$, $5.00$ and $3.12$ GeV in the four sets, while the top and bottom there are $92.45$ and $1.365$ GeV.

No set is near either reading: all are at least eighteen times below the top and at least a factor $2.2$ away from the bottom, and they spread over a factor above ninety. So (U) is not a consequence of the premises the fits satisfy; it is an additional input. A common running factor to the ceiling cannot change that conclusion for more than one set. On the set without a $120$ the leading value is fixed mainly by the $126$'s second-family entry, $\hat{f}_{22} \approx 0.025 + 0.011I_{4}$ (numbers are read in $\mathrm{span}\{1, I_{4}\}$), rather than by the mixing ratio $\hat{f}_{23}$, so a rank-one model of $\hat{f}$ does not describe these sets.

## lay
An assumption of the series, Hypothesis (U), fixes the neutrino's ordinary mass at the highest energy scale to be the top quark's mass or the bottom quark's. The series' unified-theory fits reproduce all measured quark and lepton masses and mixings without using this assumption. This result reads off, exactly, what those fits give for the neutrino's ordinary mass: at the intermediate scale of the fits, between about 0.05 and 5 GeV depending on the fit, never close to the top quark's 92 GeV or to the bottom quark's 1.4 GeV there; whether the same holds at the highest scale is argued, not computed. So the assumption is not forced by the rest of the theory and the data; it is an extra choice that the series would have to justify separately.

## one-liner
Exactly from the four stored Pati-Salam coupling sets (with (EW) exact), the leading neutrino Dirac value at $M_{I}$ is $0.054$, $3.16$, $5.00$ or $3.12$ GeV, never within a factor $18$ of $m_{t}$ or $2.2$ of $m_{b}$: these premises and data do not imply Hypothesis (U).
