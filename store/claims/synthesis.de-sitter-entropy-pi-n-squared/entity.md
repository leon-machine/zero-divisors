---
id: synthesis.de-sitter-entropy-pi-n-squared
kind: claim
version: 6
title: The cosmological horizon's entropy is pi N^2
status: proved
region: synthesis
subject: entropy
tags: [the-number-n, horizons, cosmological-constant, frozen-point, needs-continuum]
proposed_by:
  kind: ai
  session: de-sitter-count-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 6
  source: maintainer pass 2026-11-07 (GA units)
review: reviewed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.imported-gibbons-hawking-entropy@3
  - standard-model.imported-frozen-point-dictionary@8
  - synthesis.de-sitter-static-boost-frozen-point@5
  - synthesis.cosmological-horizon-completed-pair@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_de_sitter_entropy
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.what
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Group F: the de Sitter weight w = -3/2 + i N_w of the proof is written -3/2 + I_4 N_w, a physical number read in span{1, I_4}, as elsewhere in the store; no bare i remains.'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'de Sitter chart sign corrected: beta = -rH (expanding chart, free fall dr/dt = Hr), so that the chart contains the future cosmological horizon the note sentence names; with beta = +rH it is the contracting chart and contains the past horizon. Checked exactly in verify/dictionary_identities.py.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'V4 side question: technical, lay and one-liner now say pi N^2 is the imported Einstein-Hilbert area law value; the MacDowell-Mansouri action as written gives zero (its Gauss-Bonnet term contributes -pi N^2). Formal unchanged; the subtraction decision stays open.'
  note: Clause (i) of the de Sitter count, held apart so that it carries no premise of the black hole's calibration chain; it is exact given the imported area law.
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity per Leon 2026-10-23 (DICTIONARY, Bifurcation surfaces): the horizon is met on a cross-section of the horizon locus r = 1/H in the static Painleve-Gullstrand chart of the de Sitter field, same areal radius and area, replacing the bifurcation sphere; note sentence added. Same value pi N^2; proof given a pointer.'
---

## formal
Let $\Lambda = 3H^{2} > 0$, in units $\hbar = c = 1$ with $G = M_{P}^{-2}$, and let $N := M_{P}/H$ be the number of Fact \claimref{standard-model.imported-frozen-point-dictionary}, which in the series' terms is $N^{2} = M_{P}^{2}/Q(I_{\Lambda})$. The entropy of the cosmological horizon of the de Sitter gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}; Fact \claimref{synthesis.imported-gibbons-hawking-entropy}) is exactly
\[
S_{\Lambda} \;=\; \pi N^{2} \;=\; \frac{\pi M_{P}^{2}}{Q(I_{\Lambda})} ,
\]
the horizon being met on a cross-section of the cosmological horizon locus $r = 1/H$ in the static Painlev\'e-Gullstrand chart of de Sitter space ($\hb = 1 - \beta P$, $\beta = -rH$, the expanding chart, whose free-fall observers have $dr/dt = Hr$ and which contains the static observer's future horizon), of area $4\pi/H^{2}$, on which the static Killing field is null and normal with surface gravity $H$ (Proposition \claimref{synthesis.de-sitter-static-boost-frozen-point}(iii)): areal radius $R_{h} = 1/H$, area $A_{\Lambda} = 4\pi N^{2}$ Planck areas. With $N$ read as the imaginary part of the Planck mass's weight, $N_{w} := \operatorname{Im} w(M_{P})$, exactly $S_{\Lambda} = \pi\bigl(N_{w}^{2} + \tfrac94\bigr)$.

The bifurcation surface itself, where the boost flow has its fixed points, lies beyond one flat chart (it is the meeting of the four regions of the maximal extension); the chart contains the future horizon, on whose cross-sections the area, the surface gravity and the boost flow are those stated.

## technical
The series' number $N$ is the Planck mass over the Hubble rate of the cosmological constant, $N = M_{P}/H$, about $1.0 \times 10^{61}$. Each cross-section of the cosmological horizon locus of the de Sitter field, in its static Painlev\'e-Gullstrand chart, is a sphere of radius $1/H$, so its area is $4\pi N^{2}$ Planck areas and its Gibbons-Hawking entropy, a quarter of that, is exactly $\pi N^{2}$, about $3.3 \times 10^{122}$; in the series' language, $\pi M_{P}^{2}$ divided by the frozen point's norm. This value is the imported Einstein-Hilbert area law's: the series' own MacDowell-Mansouri action as written would give zero, because its Gauss-Bonnet term contributes $-\pi N^{2}$. If the imaginary part of the Planck mass's weight is used for $N$ instead, the entropy is $\pi(N^{2} + 9/4)$. The bifurcation sphere itself lies beyond one flat chart; the chart's cross-sections carry the same area.

## lay
The series condenses the smallness of the cosmological constant into one large number, $N$, about $10^{61}$. The entropy of the cosmological horizon, the standard measure of how much information the observable universe's horizon can hold, comes out as exactly $\pi$ times $N$ squared, about $3 \times 10^{122}$. No counting assumption is needed for this: it follows from the standard area law of Einstein's theory, which the series imports. The series' own form of the gravitational action, as written, would give zero instead, because an extra topological term in it subtracts the same amount.

## one-liner
Under the imported Einstein-Hilbert area law, the cosmological horizon's entropy is exactly $\pi N^{2} = \pi M_{P}^{2}/Q(I)$ (and $\pi(N_{w}^{2} + 9/4)$ with $N_{w} = \operatorname{Im} w(M_{P})$).
