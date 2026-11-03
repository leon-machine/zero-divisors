---
id: synthesis.supersymmetric-splits-two-loops
kind: claim
version: 2
title: The four supersymmetric splits at two loops
status: proved
region: synthesis
subject: standard-model
tags: [running-and-unification, confronted-with-data]
proposed_by:
  kind: ai
  session: colony-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.standard-model.one-threshold-spectrum-admissible
derivations:
- name: main
  uses:
  - standard-model.four-supersymmetric-splits@5
  - standard-model.supersymmetric-row-two-loops@6
  - standard-model.imported-two-loop-gauge-coefficients@1
  - standard-model.imported-coefficient-sum-indices@1
  - standard-model.table-exact@7
  - standard-model.two-threshold-criterion@4
  - standard-model.spectrum-run@6
  - standard-model.imported-proton-condition@1
  - standard-model.proton-condition-candidates@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_coefficients
- kind: check
  ref: check.py::check_decision
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - standard-model.four-supersymmetric-splits
  - standard-model.supersymmetric-row-two-loops
extraction:
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'W503: the lay level now states Hypothesis (S) and the record central values the run starts from.'
  open_problem: op.two-loops-two-thresholds
  note: Clause (ii) is the decision and rests only on the stored two-loop row. The numbers in (iii) to (v) use the generic matrix exactly as the Fact quotes it, which excludes gauge Yukawas. The gaugino-Higgs-higgsino Yukawas of splits (a) and (d) enter through the general two-loop Yukawa term Tr[C(F) Y Y^+]/d(G) of Machacek and Vaughn (Nucl. Phys. B222 (1983) 83), which the store does not hold as a Fact; derived from components they have coefficients (9/20, 11/4, 0)(gu^2 + gd^2) and (3/20, 1/4, 0)(gpu^2 + gpd^2) (matching the split-supersymmetry literature, Giudice and Romanino 2004, cited from memory), the normalisation calibrated exactly against the Fact's top coefficients and against the superfield matrix. With them included at tree matching (gu^2 + gd^2 = g2^2, gpu^2 + gpd^2 = (3/5) g1^2) the diagonal point is unchanged, (d)'s f' = 0 end moves from 3.5e9 to 3.4e9 GeV, its proton crossing does not move at the printed precision, and (a)'s heavy end moves from 9.7e7 to 5.4e7 GeV; no decision changes. An independent leading-log route (two-loop terms integrated along the one-loop path) gives the diagonal point at 2.2 TeV and the same far ends to within 20 percent in the heavy scale. Collider bounds are not used; with them, the light set of (a) contains the gluino below 2.3 TeV, which the LHC gluino searches put under pressure.
---

## formal
Under Hypothesis (S), run the four splits of Proposition \claimref{standard-model.four-supersymmetric-splits} at two loops with the top Yukawa, from the record's central values and with the top Yukawa as in Proposition \claimref{standard-model.supersymmetric-row-two-loops} ($y_{t}(M_{Z}) = 0.95$, matched by $1/\sin\beta$ at the heavy threshold, $\sin\beta = 1$): the Standard Model matrix below $M_{I}$, between $M_{I}$ and $M_{I}'$ the generic matrix of Fact \claimref{standard-model.imported-two-loop-gauge-coefficients} for the Standard Model content with the light set, as the Fact quotes it, that is without the gaugino-Higgs-higgsino Yukawa couplings of splits (a) and (d), above $M_{I}'$ the minimal supersymmetric matrix. Then:
\begin{enumerate}
\item[(i)] \emph{(Exact.)} The middle-regime one-loop coefficients are $(\tfrac92, -\tfrac76, -5)$, $(\tfrac92, -\tfrac52, -7)$, $(\tfrac{23}{5}, -\tfrac73, -7)$ and $(\tfrac92, -\tfrac76, -7)$ for (a) to (d), and the two-loop matrices are the generic formula's for the listed content. At $f = f'$ every split is the full supersymmetric content at one threshold, so the four lines of Theorem \claimref{standard-model.two-threshold-criterion} share the diagonal point; at one loop it is $f = f' = 1.0116$, outside the triangle, the $1.2$ percent miss in $f$ (a threshold near $62$ GeV, below $M_{Z}$) of Proposition \claimref{standard-model.table-exact}(c), and this is why the lines of (a), (b) and (c) miss the triangle.
\item[(ii)] \emph{(The decision.)} At two loops the diagonal point is admissible, $M_{I} = M_{I}' = 2.3$ TeV, $f = f' = 0.901$, $M_{U} = 1.1 \times 10^{16}$ GeV, $\alpha_{U}^{-1} = 25.7$ (Proposition \claimref{standard-model.supersymmetric-row-two-loops}), and it meets the proton condition. So each of the four splits is admissible at two loops, and none is excluded by unification: the one-loop exclusion of (a), (b) and (c) does not survive.
\item[(iii)] \emph{(Record, computed numerically; middle-regime matrices without the gaugino Yukawas.)} Each admissible set is a curve ending at the diagonal point. For (a), (b) and (c) the light set lies between $M_{Z}$ and $2.3$ TeV and the heavy set above, the far end at $f = 1$ having the heavy set at $1.0 \times 10^{8}$, $7.9 \times 10^{5}$ and $1.6 \times 10^{9}$ GeV and $M_{U} = 2.7 \times 10^{16}$, $2.8 \times 10^{15}$ and $4.8 \times 10^{14}$ GeV. For (d) the light set lies above $2.3$ TeV, the far end at $f' = 0$ having the light set at $3.5 \times 10^{9}$ GeV and $M_{U} = 1.2 \times 10^{14}$ GeV. Including the gaugino-Higgs-higgsino Yukawas at tree-level matching, through the general two-loop Yukawa term (not a Fact of the store), moves the far end of (a) to a heavy set at $5.4 \times 10^{7}$ GeV and that of (d) to $3.4 \times 10^{9}$ GeV, and leaves the diagonal point and every decision unchanged. The one-loop end $(f, f') = (1, 0.991)$, every partner near $M_{Z}$, is not admissible at two loops, and on the whole curve every partner of (d), the gluino included, lies above $2.3$ TeV.
\item[(iv)] \emph{(Record, computed numerically; proton condition of Fact \claimref{standard-model.imported-proton-condition}, same matrices as (iii).)} (a) meets it on its whole curve; (b) and (c) meet it from the diagonal point down to the light set at about $490$ GeV and $1.2$ TeV respectively, the heavy set then at $3.7 \times 10^{4}$ GeV; (d) meets it from the diagonal point up to the light set at $1.7 \times 10^{4}$ GeV, the heavy set at $7.8 \times 10^{4}$ GeV and $M_{U} = 5.7 \times 10^{15}$ GeV, against $6 \times 10^{3}$ GeV at one loop (Proposition \claimref{standard-model.proton-condition-candidates}(2)).
\item[(v)] \emph{(Sensitivity, computed numerically.)} Across $\alpha_{s} = 0.1180 \pm 0.0009$ the diagonal point moves between $1.7$ and $3.0$ TeV and stays inside the triangle, so (ii) holds across the record's range; (d)'s far end moves between about $3$ and $4 \times 10^{9}$ GeV.
\end{enumerate}

## technical
Under Hypothesis (S), at two loops and from the record's central values, the four ways of splitting the supersymmetric partners into a light and a heavy set all share one spectrum: both sets at the same scale. That spectrum is the supersymmetric row, which one loop places at $f = 1.0116$, a threshold of about $62$ GeV, below $M_{Z}$, and two loops place at $2.3$ TeV. One loop excluded three of the four splits only because their lines reach the diagonal outside the allowed triangle; at two loops the diagonal point is inside, so all four splits are admissible on curves ending there.

For the gaugino-higgsino split (a), the higgsino split (b) and the two-doublet split (c), the light set lies below $2.3$ TeV and the heavy set rises to $10^{8}$, $8 \times 10^{5}$ and $1.6 \times 10^{9}$ GeV at the far end. For split (d), the only one one loop admitted, the light set must lie above $2.3$ TeV, up to $3.5 \times 10^{9}$ GeV; its near-degenerate one-loop end is gone, so the gluino of (d) is above $2.3$ TeV automatically. The proton condition holds on all of (a), near the diagonal end of (b) and (c), and on (d) up to a light set at $1.7 \times 10^{4}$ GeV. The decision rests on the stored two-loop row; the curves are record-level integrations, with the generic matrix as the Fact quotes it, without the gaugino Yukawas; including them moves the far ends by a few percent in the logarithm, (a)'s heavy end by a factor of about two. Collider limits are not applied: in (a) the light set contains the gluino below $2.3$ TeV.

## lay
Supersymmetric partner particles could come in two groups at two different energies. A simpler calculation had found that only one of four natural groupings lets the three forces meet. Redoing it one level more precisely, under the series' slot-statistics hypothesis (S) and with the measured coupling values, all four groupings work for the meeting of the forces and the proton's lifetime (limits from particle colliders are not applied here), because each of them includes the case where both groups sit together at about 2.3 TeV, which the more precise calculation already allowed. What changes between groupings is how far the two groups can be pulled apart. In the grouping the simpler calculation favoured, every partner now has to be heavier than about 2.3 TeV, and the proton lives long enough only while the lighter group stays below about 17 TeV.

## one-liner
Under (S), at two loops all four supersymmetric splits are admissible on curves ending at the shared degenerate point $M_{I} = M_{I}' = 2.3$ TeV; one loop's exclusion of three of them was its miss of that point, which it places near $62$ GeV, below $M_{Z}$, and the favoured split (d) now needs every partner above $2.3$ TeV.
