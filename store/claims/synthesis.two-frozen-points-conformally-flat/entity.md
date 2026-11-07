---
id: synthesis.two-frozen-points-conformally-flat
kind: claim
version: 4
title: 'Two frozen points of one norm on conformally flat fields'
status: proved
region: synthesis
subject: dark-matter
tags: [premises-p1-p5, frozen-point, tractors, no-go]
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
  role: 'GA rewrite (declared outside_ga)'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG proof: tractors as Cl(2,4) vectors, the flat-scale connection as the gauge field -ninf ^ a, stabilisers as bivectors'
  version: 4
  source: maintainer pass 2026-11-07 (consistency, GTG proofs)
- name: Claude Opus 5.5
  role: 'GTG review (referee F1): Einstein scale computed directly instead of from the converse of the Fact'
  version: 4
  source: maintainer pass 2026-11-07 (consistency, GTG review)
review: draft
derivations:
- name: main
  uses:
  - dark-energy.imported-frozen-point-geometry@6
  - dark-energy.point-infinity-has-no-physical-fluctuation@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_parallel_frozen_points_and_norms
- kind: check
  ref: check.py::check_two_frozen_points_give_two_metrics
- kind: check
  ref: check.py::check_pair_has_one_gauge_invariant
- kind: check
  ref: check.py::check_gtg_parallel_tractors_flat_strength_and_einstein_scale
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - dark-matter.p1-single-frozen-point
extraction:
  maintainer_pass_gtg_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Referee F1 fix 10.1 applied: proof (i) read ''a parallel tractor of norm Lambda/3 is the scale tractor of an Einstein scale'' from Fact dark-energy.imported-frozen-point-geometry, which states the converse direction only. The step is now computed: for hb^{-1}(a) = a/sigma the torsion equation gives Omega(a) = (grad sigma ^ a)/sigma, R(a ^ b) = -(2 r sigma + Q(grad sigma)) sigma^-2 a ^ b = -Q(I) sigma^-2 a ^ b, calR(B) = -R(sigma^2 B) = Q(I) B, Lambda = 3 Q(I). Fixer verified exactly with the gtg engine (torsion solved, not assumed) at (s, r) = (1, 1), (-2, 3/4), (3/2, -5/2), (1, 1/2) with generic m and points: torsion-free, Omega(e_mu) equal to the formula, R(e_mu ^ e_nu) = -Q(I) sigma^-2 e_mu ^ e_nu, calR = Q(I) id and Ricci map 3 Q(I) id. The existing check already computes this field; no check change.'
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Proof rewritten in Gauge Theory Gravity: tractors as Cl(2,4) vectors sigma ninf + mu + rho n0; the flat-scale tractor connection of the frozen-point Fact as the gauge field Omega_T(a) = -ninf ^ a (hb = 1, Omega = 0, Schouten map 0), giving the parallel tractors I(x) = sigma(x) ninf + (m - r x) + r n0 and the norm 2rs + Q(m) in one line; the field strength (ninf ^ a) x (ninf ^ b) = 0; the Einstein scale read as the dilation field hb^{-1}(a) = a/sigma; the pairing constant because Omega_T is bivector-valued; the stabilisers as the bivectors of I-perp and of the complement of the plane. Component reading kept, shortened, at the end; the original proof kept as orig-proof-main.tex. New exact check check_gtg_parallel_tractors_flat_strength_and_einstein_scale (parallelism as exact jets at three points for four tractors, constant norm, flat strength, the dilation field''s store-sign curvature calR(B) = Q(I) B with Omega solved from the torsion condition at twelve points, which the coverage judge had listed as untested, and the stabiliser dimensions 15, 10, 6 by rank on the bivectors of Cl(2,4)). outside_ga withdrawn: no stand-in remains.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: The proof solves the tractor parallelism equations in flat components (eta_ab, partial_a partial_b sigma); on flat spacetime the connection is the Cl(2,4) gauge field Omega_T of synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection, and the component solution is the evidence (reader R05).'
  maintainer_pass:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 2 -> 3.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  open_problem: pr.p1-single-frozen-point
  note: >-
    The independence model asked for by pr.p1-single-frozen-point, on the region where it can
    exist: where the Weyl tensor has no kernel vector the parallel tractors are multiples of one
    (filed alongside, synthesis.frozen-point-unique-where-weyl-has-no-kernel; the two results agree
    that on conformally flat regions the parallel tractors form a six-dimensional space), so the
    model lives on conformally flat regions, which include the
    de Sitter vacuum of the dark-energy paper. The orientation clause of P1 (one Witt flag) is
    not addressed. Transport-convenient: tractor geometry, no Clifford input.
---

## formal
Let $U$ be a connected region of conformal Minkowski space with the flat scale $\eta$ of signature $(1,3)$, so that the tractor connection of Fact \claimref{dark-energy.imported-frozen-point-geometry} is flat, with tractor form $\eta^{-1}(\mu,\mu) + 2\sigma\rho$ of signature $(2,4)$.
\begin{enumerate}
\item[(i)] \emph{(Frozen points.)} For constants $s, r \in \R$ and $m \in \R^{1,3}$, the tractor $I_{(s,m,r)} = (\sigma, d\sigma, r)$ with $\sigma = s + \eta(m, x) - \tfrac{r}{2}Q(x)$ is parallel, with constant norm $Q(I) = 2rs + Q(m)$; on the region $\sigma \neq 0$ its scale $\sigma^{-2}\eta$ is Einstein with $\Lambda = 3Q(I)$.
\item[(ii)] \emph{(Two frozen points, one $\Lambda$.)} Two such tractors $I_A, I_B$ of equal norm $\Lambda/3 \neq 0$ that are not proportional give, where $\sigma_A\sigma_B \neq 0$, two Einstein metrics $\sigma_A^{-2}\eta$ and $\sigma_B^{-2}\eta$ with the same $\Lambda$ in one conformal class that are not homothetic ($\sigma_A/\sigma_B$ is not constant). Example: $I_A = (1, 0, 1)$, $I_B = (1, (1,0,0,0), \tfrac12)$, $\Lambda = 6$, $\ip{I_A}{I_B} = \tfrac32$.
\item[(iii)] \emph{(Not a gauge copy.)} The ambient group $SO(2,4)$ has dimension $15$; the stabiliser of one non-null frozen point has dimension $10$, and that of an equal-norm pair spanning a nondegenerate plane has dimension $6$. Pairs of points of fixed norm form a ten-dimensional space with nine-dimensional orbits, so the pair has exactly one invariant, $\ip{I_A}{I_B}$, which no gauge transformation changes. Proposition \claimref{dark-energy.point-infinity-has-no-physical-fluctuation}, which makes every fluctuation of one pair $(I, V)$ a gauge transformation, does not reach it.
\item[(iv)] \emph{(Stationarity.)} The tractor curvature $F$ vanishes on $U$, so a sum over towers $\sum_r Q(I_r)^{-1}\int \epsilon(I_r, V_r, F, F)$ of functionals in the three-argument form, with one shared connection, is stationary at this configuration under variations of the connection and of every $(I_r, V_r)$, whatever the frozen points are.
\end{enumerate}
Consequently, on a region where the Weyl part of the field strength vanishes, and in particular on the de Sitter vacuum, the frozen-point geometry, the three-argument functional and the no-fluctuation proposition allow the towers to couple to different frozen points of one norm. The metric clause of Premise \claimref{dark-matter.p1-single-frozen-point} is there an independent choice: it fixes the invariant by requiring $I_B = \pm I_A$.

## technical
P1 says that every tower couples to one frozen point and so to one metric. This result tests whether that follows from the frozen-point geometry and the action. On a region where the Weyl part of the field strength vanishes (conformally flat derived metric), which includes the de Sitter vacuum, the tractor connection is flat and every constant tractor is parallel. Any two parallel tractors of the same norm give two Einstein metrics with the same cosmological constant in one conformal class, not related by a constant rescaling. The ambient group cannot carry one into the other while keeping the pair: the pair has one gauge invariant, their inner product. The configuration is stationary for a sum of the functional over towers, since every term of its first variation carries a factor of the vanishing curvature. So on the vacuum, the premises other than P1 allow towers with different frozen points of one norm, and the metric clause of P1 is an independent choice there. Where the Weyl tensor has no kernel vector, parallel tractors are multiples of one, and the question does not arise.

## lay
One of the series' assumptions is that every hidden sector feels the same gravity, because the origin of the universe fixed one special reference point for everything. This result asks whether the rest of the theory forces that. In empty space with a cosmological constant it does not. There, two different reference points of the same strength can coexist, and each gives a perfectly good geometry with the same cosmological constant but a different notion of distance. No change of description turns one into the other. So in empty space the assumption is a real choice. Where there is matter and curvature of the right kind, the choice is forced.

## one-liner
On a region where the Weyl part of the field strength vanishes (the de Sitter vacuum included) two non-proportional parallel tractors of one norm give two non-homothetic Einstein metrics with one $\Lambda$ and a gauge-invariant pairing, so the metric clause of P1 is an independent choice there.
