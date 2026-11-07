---
id: synthesis.majorana-scale-is-126-doublet-vev
kind: claim
version: 3
title: 'The Majorana scale is set by the 126 doublet admixture'
status: proved
region: synthesis
subject: neutrinos
tags: [seesaw-and-majorana, flavour-and-mixing]
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
  role: 'GA rewrite (Dirac mass matrices named as such)'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - standard-model.imported-clebsch-structure-seesaw@1
  - standard-model.imported-spinor-bilinears@1
  assumes:
  - standard-model.premise-ew-equal-weight@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_majorana_matrix_is_126_difference
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.premise-ew-equal-weight
  - standard-model.what-angle-asks-neutrino-sector
  - standard-model.neutrino-dirac-matrix-charged-fermions
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3. The phrase "the Dirac matrices", which here means the Dirac mass matrices of the charged fermions and neutrinos (family matrices, which the conventions allow), is written "the Dirac mass matrices", so that it is not read as the Dirac gamma matrices; wording only, the mathematics unchanged.'
  open_problem: op.majorana-scale
  note: 'Adversarial answer to the problem''s second success clause. On the one-vev Pati-Salam route the triplet vev is not free (the weak angle fixes it), so the question is what fixes the Majorana coupling; under (EW) and the imported Clebsch structure it is the 126 component w_u of the light up-type doublet, the same number that sizes every 126 entry against the 10s, so op.majorana-scale and op.pair-sector-current share one unknown. Clause (i) extends the store''s no-120 identity (standard-model.neutrino-dirac-matrix-charged-fermions) to the case with a 120 by taking symmetric parts. Does not use Hypothesis (U), which contradicts (EW). Numerics (bounds on w_u and M_3) are in the proof, with the normalisation of w_u against the canonically normalised doublet flagged as cited from memory. Transport-absent.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Version 2 adds the assumes edge to standard-model.premise-ew-equal-weight: clause (ii) imposes (EW) along the heavy direction, which the title and proof already named as an inline hypothesis, so holds_given now tracks it; the check touches the premise where (ii) imposes it. Clause (i) does not use (EW). Statement unchanged.'
---

## formal
Under Fact \claimref{standard-model.imported-clebsch-structure-seesaw}, with the $10$ and $126$ couplings symmetric and the $120$ coupling antisymmetric in the family indices (Fact \claimref{standard-model.imported-spinor-bilinears}), and writing $\mathrm{Sym}\,X = \tfrac12(X + X^{\mathsf{T}})$:
\begin{enumerate}
\item[(i)] for any number of $10$s and with or without the $120$, $\mathrm{Sym}(M_{u} - M_{\nu}) = 4w_{u}f$ and $\mathrm{Sym}(M_{d} - M_{e}) = 4w_{d}f$, while the antisymmetric parts are $(c_{u} - c_{\nu})h$ and $(c_{d} - c_{e})h$; hence, when $w_{u}w_{d} \neq 0$,
\[
M_{R} \;=\; v_{R}f \;=\; \frac{v_{R}}{4w_{u}}\,\mathrm{Sym}(M_{u} - M_{\nu}) \;=\; \frac{v_{R}}{4w_{d}}\,\mathrm{Sym}(M_{d} - M_{e});
\]
\item[(ii)] if, in some family basis, $(M_{u})_{33} = m_{t}$ and $(M_{\nu})_{33} = 0$ (the content of Premise (EW), \claimref{standard-model.premise-ew-equal-weight}, in its basis), then $(M_{R})_{33} = v_{R}f_{33} = \dfrac{m_{t}\,v_{R}}{4w_{u}}$, so the Majorana coupling along the heavy family direction is $f_{33} = m_{t}/(4w_{u})$.
\end{enumerate}
So, under that premise and given $v_{R}$ (as on the chain, where the weak angle fixes it) and $m_{t}$, the entry of the Majorana matrix along the heavy direction of the up sector is determined by $w_{u}$, the $126$ component of the light up-type doublet, which the series does not derive; $w_{u}$ also sets the size of every $126$ entry of the Dirac mass matrices relative to the $10$s. This re-parametrises the open Majorana scale as the open $126$ admixture: the two are one unknown, and a derivation of either gives the other. The $33$ entry is not an eigenvalue of $M_{R}$; a lower bound on it bounds the largest singular value of $M_{R}$ from below, an upper bound on it does not bound that value.

## technical
Take the imported Pati-Salam Clebsch structure with any number of $10$s, one $126$ and one $120$. Because the $10$ and $126$ family couplings are symmetric and the $120$ coupling antisymmetric, the $10$s cancel in the differences $M_{u} - M_{\nu}$ and $M_{d} - M_{e}$, the $120$ survives only in their antisymmetric parts, and the symmetric parts are $4w_{u}f$ and $4w_{d}f$. The Majorana matrix $M_{R} = v_{R}f$ is therefore the symmetric part of either Dirac difference, rescaled by $v_{R}/4w$. This extends the store's no-$120$ identity to the case with the $120$.

Under Premise (EW), which sets the neutrino's Dirac entry to zero along the heavy family direction where the top sits, the $33$ entry gives $4w_{u}f_{33} = m_{t}$ (the premise's own content), so $(M_{R})_{33} = m_{t}v_{R}/4w_{u}$. On the Pati-Salam chain the weak angle fixes $v_{R}$, so the vev along the Majorana element is not a free input there; the open number is instead $w_{u}$, the $126$ admixture of the light up-type doublet, which also sizes every $126$ entry relative to the $10$s and which the series does not derive. The result is a re-parametrisation of the open problem, not a determination of the scale.

## lay
In the version of the framework where quarks and leptons are unified at an intermediate energy, the heavy right-handed neutrinos get their mass from the same field that breaks that unification, and the measured strength of the weak force already fixes how large that field is. What was missing was the strength of its coupling to the neutrinos. This result shows that, under a premise the series already uses about the top quark and the neutrino, that coupling is traded for one other number, which the series does not yet derive: how much of the ordinary Higgs field lives in the larger multiplet that couples to the heavy neutrinos. The same number decides how strongly that multiplet shapes the masses of the charged particles, so two open questions turn out to be one; neither is answered.

## one-liner
Under the imported Clebsch structure, $M_{R} = (v_{R}/4w_{u})\,\mathrm{Sym}(M_{u} - M_{\nu}) = (v_{R}/4w_{d})\,\mathrm{Sym}(M_{d} - M_{e})$ even with a $120$, and under (EW) $(M_{R})_{33} = m_{t}v_{R}/4w_{u}$: the Majorana scale along the heavy direction is determined by the $126$ doublet admixture $w_{u}$, which is not derived.
