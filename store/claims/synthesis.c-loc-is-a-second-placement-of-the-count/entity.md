---
id: synthesis.c-loc-is-a-second-placement-of-the-count
kind: claim
version: 3
title: '(C$_{\mathrm{loc}}$) is a second placement of the count'
status: proved
region: synthesis
subject: einstein
tags: [counting-rules, horizons, kerr, mode-counting, no-go, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-22-cloc
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'consistency pass, the clause cited named as clause (i) of version 1 of the local-horizon premise'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - singularity.stretched-singularity-count@9
  - scrambling.epoch-modular-period-two-unknowns-become@6
  - scrambling.area-law-test@5
  - synthesis.clausius-route-newton-constant-is-residue@4
  - synthesis.imported-jacobson-clausius-1995@3
  - synthesis.kerr-ring-count-misses-area-law@7
  - synthesis.imported-kerr-surface-gravity-entropy@2
  - synthesis.quarter-from-temperature@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_cutoff_meets_no_horizon
- kind: check
  ref: check.py::check_killing_patch_is_local_rindler
- kind: check
  ref: check.py::check_double_count_doubles_newton_constant
- kind: check
  ref: check.py::check_two_placements_on_kerr
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.kerr-ring-count-misses-area-law
  - synthesis.clausius-route-newton-constant-is-residue
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: '(H) is the mode-count clause (i) of version 1 of the local-horizon premise; the current version (6) has the clauses (Loc) and (R_loc) and lists the count under Not part of this premise; the clause references now say so.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 1 -> 2.'
  open_problem: op.derive-c-loc
  note: >-
    Consistency test of the local-horizon premise against the store's placement of the count (C1, C2)
    and against the Kerr tension. Outcome: the premise is consistent with the store only with a stated
    relation between the modes it places on a hole's horizon and the modes the cutoff premises place
    inside the hole. Independent placements give Newton's constant 2G through Jacobson's theorem at the
    area-law calibration, under the reading that the hole's thermodynamic entropy is the total entropy of
    all its boundary modes; identified placements inherit the existing conflict between the literal Kerr
    count and the Kerr entropy; a correlated joint state is the residual case, not excluded by these data.
    The Kerr shortfall is a statement about the cutoff tube, present in every reading, and counts against
    the cutoff placement on spinning holes rather than against the premise.
    The independence of clause (i) from the other premises is argued in the technical level as a survey,
    not proved. Transport-absent: the computation uses the counting premises and classical horizon
    geometry, not the completion. Literature cited from memory in the proof: vanishing expansion and shear
    of Killing-horizon generators (a standard consequence of Killing's equation, also derived in the proof).
---

## formal
Units $G = \hbar = c = 1$, with $G$ the constant that defines the Planck cell. Let (H) be clause (i) of version 1 of Premise \claimref{synthesis.c-loc-local-horizon-premise} (its mode-count reading, which the current version records under ``Not part of this premise''), taken here as a hypothesis and not assumed: every local Rindler horizon carries boundary modes with entropy $\eta = 4\pi\nu\langle s\rangle$ per unit area, with the constants of the Killing case. The registered value is the area-law condition $16\pi\nu\langle s\rangle = 1$ of Theorem \claimref{synthesis.clausius-route-newton-constant-is-residue}(iii), at which $\eta = \tfrac14$. Let (S$_{\mathrm{tot}}$) be the reading that the hole's thermodynamic entropy $\SBH = A/4$ (Theorem \claimref{synthesis.quarter-from-temperature}) is the total entropy of all its boundary modes.
\begin{enumerate}
\item[(i)] \emph{(The stored placement meets no horizon.)} The curvature-cutoff locus $r_{c} = (2M)^{1/3}$ of Premise \claimref{singularity.c1-curvature-cutoff} lies strictly inside the Schwarzschild horizon if and only if $M > \tfrac12$, and on the horizon the curvature scale $2M/r^{3}$ equals $1/(4M^{2})$. For Kerr with $a \ge 2(2M)^{2/3}$ the locus lies in $|r| < r_{-}$ (Theorem \claimref{synthesis.kerr-ring-count-misses-area-law}(1)), so it meets neither horizon. Premises (C1) and (C2) place modes only on the cutoff locus of a hole, so the count of Proposition \claimref{singularity.stretched-singularity-count} places none on the horizon of a hole of mass above $\tfrac12$ and none on any local Rindler horizon, and the count that (H) asserts on such a horizon is not an instance of it.
\item[(ii)] \emph{(It applies at the horizons of holes.)} The generators of a Killing horizon have vanishing expansion and shear at every point, so near any point $p$ of a Killing horizon with generator $\ell$ the horizon is the local Rindler horizon $\mathcal{H}_{p,\ell}$ at leading order. At the registered value (H) then gives a horizon cross-section of area $A$ the entropy $\eta A = A/4$: $\SBH$ for Schwarzschild, and $A_{+}/4$ for Kerr at every spin, the Bekenstein-Hawking entropy of Fact \claimref{synthesis.imported-kerr-surface-gravity-entropy}.
\item[(iii)] \emph{(Independent placements.)} Assume (H) and (S$_{\mathrm{tot}}$), and suppose the modes (H) places on a Schwarzschild horizon are distinct from those that (C1) and (C2) place on the cutoff locus, and the state is a product across the two sets, so their entropies add. The epoch count of Theorem \claimref{scrambling.epoch-modular-period-two-unknowns-become} carries $4\pi\nu\langle s\rangle A$, the horizon carries $\eta A = 4\pi\nu\langle s\rangle A$, and the area law $N = \SBH$ of Theorem \claimref{scrambling.area-law-test} read for all of the hole's boundary modes requires $32\pi\nu\langle s\rangle = 1$; then $\eta = \tfrac18$ and Jacobson's theorem (Fact \claimref{synthesis.imported-jacobson-clausius-1995}) returns $G_{\mathrm{cl}} = 1/(4\eta) = 2G$, against $G_{\mathrm{cl}} = G$. Keeping the registered value instead, the hole's boundary modes carry $A/2 = 2\SBH$, against (S$_{\mathrm{tot}}$). With $k$ independent sets of one density, $k$ counting all of them, the cutoff set included, $G_{\mathrm{cl}} = kG$.
\item[(iv)] \emph{(Identified placements.)} Assume (H), and suppose instead the modes on the horizon are the modes on the cutoff locus, one set described at two loci. On Kerr with $a \ge 2(2M)^{2/3}$ that set then has entropy $A_{+}/4$ by (ii) and, in the 1-nat convention, the literal count $N$ of Theorem \claimref{synthesis.kerr-ring-count-misses-area-law}(4). These differ: at $(M, a) = (500, 300)$, $N \le \tfrac{11}{28}\cdot A_{+}/4$, and at $(M, a) = (500, 480)$, $N > A_{+}/4$. This is the conflict between the literal Kerr count and Fact \claimref{synthesis.imported-kerr-surface-gravity-entropy} that holds already without (H); the identified reading inherits it, and under (S$_{\mathrm{tot}}$) the independent reading meets it too, since $A_{+}/4 + N \ne A_{+}/4$.
\end{enumerate}
So (H), and with it (C$_{\mathrm{loc}}$), is consistent with the registration of $\nu$ and with Jacobson's coupling only if the store states how its horizon modes relate to the cutoff modes at a hole: independence fails by (iii) under (S$_{\mathrm{tot}}$); identification leaves the literal reading of (C1), (C2) and (IC) on Kerr in that regime in conflict with the Kerr entropy, as it already is; the residual case, a correlated joint state whose total entropy is $\SBH$, is not excluded by these data. The literal Kerr count is a count on the cutoff tube, not on any local horizon, and its conflict with $A_{+}/4$ is present in every reading: it counts against the cutoff placement on spinning holes, not against (C$_{\mathrm{loc}}$), and on its own it does not meet refutation condition (a) of (C$_{\mathrm{loc}}$).

## technical
The series counts a black hole's boundary modes where the curvature reaches the Planck scale, deep inside the hole, and the ratio of that count to the horizon area is the constant $4\pi\nu$ along the Schwarzschild family. The local-horizon premise (C$_{\mathrm{loc}}$) asks for the same constant as an entropy density on every local Rindler horizon. This result tests that request against the store. The cutoff locus lies strictly inside the horizon of every hole heavier than half a Planck mass (for Kerr above the spin threshold it lies inside the inner horizon), and the cutoff premises place modes only on that locus, so they put none on any horizon of a hole and none on any local horizon: clause (i) is a new placement of modes, borrowing only the algebraic form of the boundary-mode algebra.

Patches of a Killing horizon have generators with zero expansion and shear, so they are local Rindler horizons and the premise applies there: at the registered value it gives the horizon the entropy $A/4$, and $A_{+}/4$ for Kerr at every spin. A hole then has modes at two loci. If they are independent and the hole's thermodynamic entropy is the total over all its boundary modes, the hole carries the area law twice: recalibrating to one area law halves the density and Jacobson's theorem doubles Newton's constant. If they are one set, the Kerr hole's set has two entropies, $A_{+}/4$ from the horizon density and the literal tube count, which is below $\tfrac{11}{28}$ of $A_{+}/4$ at $(M, a) = (500, 300)$ and above it at $(500, 480)$; that is the conflict between the literal Kerr count and the Kerr entropy which the store already has without the premise. The residual case, a correlated joint state of the two sets with total entropy the Bekenstein-Hawking value, is not excluded. Since the Kerr conflict appears in every reading, it counts against the cutoff placement on spinning holes, not against a universal horizon density, which gives the Kerr entropy exactly.

Remark (a survey of the store's premises, not a theorem). No premise of the store quantifies over local Rindler horizons, small causal diamonds or all points of spacetime in a way that places modes there: the counting premises concern the cutoff locus, the regularity premises the KMS data of Killing flows, (L$_E$) the internal dynamics of given windows, and the de Sitter boundary modes leave their number free. This suggests, without proving it, that clause (i) of version 1 of (C$_{\mathrm{loc}}$) is independent of the other premises; no model is constructed.

## lay
The series places a black hole's hidden quantum modes deep inside the hole, where the curvature reaches the Planck scale, and their number matches the hole's known entropy. A newer assumption, needed to derive Einstein's equations, puts modes with the same entropy per unit area on every small horizon, including the horizon of a black hole itself. This result shows that the two placements never touch: the deep locus lies inside the horizon of every hole heavier than half a Planck mass. So a black hole would have modes in two places. If the two sets are independent and the hole's entropy is the total over both, the entropy is counted twice, and fixing that would make the derived strength of gravity twice the true value. If they are the same set, then for fast-spinning holes the deep count disagrees with the known entropy, as it already does without the new assumption. That disagreement appears whichever way the two sets are related, so it counts against placing the modes deep inside spinning holes, not against the new assumption. The assumption still needs a rule saying how the two sets are related.

## one-liner
Clause (i) of version 1 of (C$_{\mathrm{loc}}$) places modes on horizons, where the cutoff premises put none (the locus lies inside every horizon for $M > \tfrac12$): independent placements make Jacobson's $G_{\mathrm{cl}} = 2G$ at the area-law calibration if the hole's entropy is the total over all its boundary modes, identified placements inherit the literal Kerr count's conflict with $A_{+}/4$ ($\le \tfrac{11}{28}A_{+}/4$ at $(500, 300)$), and that conflict, present in every reading, counts against the cutoff placement on spinning holes, not against (C$_{\mathrm{loc}}$).
