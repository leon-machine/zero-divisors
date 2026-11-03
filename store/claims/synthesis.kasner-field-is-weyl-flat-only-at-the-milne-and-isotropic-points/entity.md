---
id: synthesis.kasner-field-is-weyl-flat-only-at-the-milne-and-isotropic-points
kind: claim
version: 1
title: 'On a four-dimensional diagonal Kasner field with $\sum p = 1$ the Weyl curvature is $t^{-2}$ times two conics in the exponents, which meet exactly at the three flat Milne points and the isotropic point $(\tfrac13, \tfrac13, \tfrac13)$; so at every other Kasner point the attachment supplies no state near the wall, and in cosmic time the Weyl-flat points are not tame walls'
status: proved
region: synthesis
subject: quantum-fields
tags: [kasner, conformal-spinors, no-go]
proposed_by:
  kind: ai
  session: 2026-11-01-deposit-state
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching@2
  - synthesis.attachment-transport-is-flat-only-where-weyl-vanishes@2
  - dark-energy.imported-walls-sphere-theorem@6
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_kasner_weyl_components_match_the_two_conics
- kind: check
  ref: check.py::check_the_two_conics_meet_exactly_at_four_points
- kind: check
  ref: check.py::check_weyl_flat_points_in_cosmic_and_conformal_time
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.pre-descent-contracting-kasner-stage-premise
  - synthesis.pre-descent-state-carried-into-descended-phase-premise
  - synthesis.attachment-transport-is-flat-only-where-weyl-vanishes
extraction:
  open_problem: op.deposit-state-is-hadamard
  note: >-
    Bears on the first and second steps of op.deposit-state-is-hadamard under the Kasner-exit premises (P1)
    and (P2): the attachment can supply a reference state (the conformal vacuum) only where the Weyl
    curvature vanishes, and a deposit set at the end of a Kasner approach sits on a field whose Weyl curvature
    is computed here for every point of the four-dimensional plane $\sum p = 1$ (no field equation imposed;
    under Einstein's equations every point of the plane has a stiff source, $P = \rho$). The Weyl map vanishes
    only at the three Milne points, which are flat, and at the isotropic point; everywhere else it grows as
    $t^{-2}$ toward the wall, so near the wall the attachment supplies no state and the state carried into the
    descended phase must come from the rule of (P2). In the smooth structure of cosmic time neither Weyl-flat
    case is a tame corank-one wall: at the isotropic point the conformal bracket degenerates at order two thirds,
    at the Milne points the metric (not the cometric) degenerates. In its conformal time the isotropic point's
    bracket is the radical-normal wall, as for every decelerating power law; the general power-law statement is synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state.
    The vanishing of the Weyl tensor of Bianchi I power-law fields at the isotropic and flat points is standard;
    it is re-derived here. Transport-absent.
  flags:
  - 'four-dimensional diagonal Kasner fields only; the stored setting also allows hidden directions (the five-dimensional end (0, 0, 0, 1) of (P2)), Bianchi I fields with rotating axes and the BKL sequence, none of which is covered'
  - 'the not-tame clause holds in the smooth structure of cosmic time; in conformal time the isotropic point is the radical-normal wall'
---

## formal
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric is the four-dimensional diagonal Kasner field $g_{p} = -dt^{2} + t^{2p_{1}}dx^{2} + t^{2p_{2}}dy^{2} + t^{2p_{3}}dz^{2}$, $t > 0$, with $p_{1} + p_{2} + p_{3} = 1$ (the Kasner plane of Theorem \claimref{synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching} with three exponents; no field equation imposed, and under Einstein's equations the source is stiff, $P = \rho$). Put $S = \sum p_{i}^{2}$, $E_{1} = p_{1}^{2} - 2p_{1}p_{2} - p_{1} - 2p_{2}^{2} + 2p_{2}$, $E_{2} = 2p_{1}^{2} + 2p_{1}p_{2} - 2p_{1} - p_{2}^{2} + p_{2}$, and let $e_{0}, e_{1}, e_{2}, e_{3}$ be the orthonormal frame of $g_{p}$.
\begin{enumerate}
\item[(i)] \emph{(The Weyl map; proved.)} The Weyl map on bivectors has the frame bivectors $e_{0}\wedge e_{i}$ and their duals $I_{4}\,e_{0}\wedge e_{i}$ as eigenvectors, with the same eigenvalue $\lambda_{i}$ on both, the mixed component $C_{0i}{}^{0i} = C_{jk}{}^{jk}$ ($\{i, j, k\} = \{1, 2, 3\}$): $\lambda_{i} = (p_{i}^{2} - p_{i} + \tfrac{1 - S}{3})\,t^{-2}$, so $\lambda_{1} = E_{1}/(3t^{2})$, $\lambda_{2} = -E_{2}/(3t^{2})$, $\lambda_{1} + \lambda_{2} + \lambda_{3} = 0$. So the Weyl curvature vanishes exactly where $E_{1} = E_{2} = 0$, and elsewhere it is nonzero at every $t > 0$ and grows as $t^{-2}$ toward the wall.
\item[(ii)] \emph{(The Weyl-flat points; proved.)} On the plane $E_{1} = E_{2} = 0$ holds exactly at the Milne points $(1, 0, 0)$, $(0, 1, 0)$, $(0, 0, 1)$, where $g_{p}$ is flat, and at the isotropic point $(\tfrac13, \tfrac13, \tfrac13)$, where $Rt^{2} = -\tfrac23$.
\item[(iii)] \emph{(No attached state at the wall; proved, a corollary.)} At every other point of the plane the Weyl curvature is nonzero on all of $t > 0$, so by Theorem \claimref{synthesis.attachment-transport-is-flat-only-where-weyl-vanishes} the tractor transport of the attachment supplies no state on any neighbourhood of the wall: on a four-dimensional Kasner approach as in Premise \claimref{synthesis.pre-descent-contracting-kasner-stage-premise} (P1), the state carried into the descended phase is not the attachment's, and must be supplied by the rule of Premise \claimref{synthesis.pre-descent-state-carried-into-descended-phase-premise} (P2).
\item[(iv)] \emph{(Not tame walls in cosmic time; proved.)} In the smooth structure of the cosmic coordinate $t$ neither Weyl-flat case is a tame corank-one wall (in the sense of the wall Fact \claimref{dark-energy.imported-walls-sphere-theorem}): at the isotropic point $g_{p} = t^{2/3}$ times a flat bracket whose cometric degenerates at order $\tfrac23$, and at a Milne point the metric itself degenerates at order two while the cometric has a pole. In its conformal time $\eta = \tfrac32 t^{2/3}$, and $t' = \eta^{2}/4$, the isotropic bracket is the radical-normal wall $-t'^{-1}dt'^{2} + \delta$, as for every decelerating power law (\claimref{synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state}), (iv)).
\end{enumerate}

## technical
If the descent ends a contracting four-dimensional Kasner approach, the state that reaches the descended phase is set on a field whose Weyl curvature this result computes exactly. Over the whole plane of Kasner exponents with sum one (under Einstein's equations, the stiff-source family) the Weyl curvature is the inverse square of the time times two quadratic forms in the exponents, and the two forms vanish together at only four points: the three flat Milne points and the isotropic point. Since the attachment's transport supplies a state only where the Weyl curvature vanishes, at every other Kasner point it supplies none near the wall, and the state must come from the matching rule of the second Kasner premise. In cosmic time the two Weyl-flat cases are not tame walls of the series' degenerate geometry, so in that coordinate the regular wall case and the conformally flat Kasner case do not meet; in conformal time the isotropic point is the regular wall. Transport-absent.

## lay
One proposal for the very early universe is a stage that shrinks unevenly in different directions before the descent. The series' way of building a quantum state from its geometry works only where a certain part of the curvature, the part that distorts shapes, is absent. For such uneven stages in four dimensions, this result computes that part and finds that it is absent only in four special cases; in all the others the series' construction gives no state near the descent, so another rule must supply it. Measured in the usual cosmic time, even the four special cases do not have the regular form the series' wall theory uses.

## one-liner
On a four-dimensional diagonal Kasner field with $\sum p = 1$ (no field equation imposed; under Einstein's equations a stiff source) the Weyl map has eigenvalues $\lambda_{i} = (p_{i}^{2} - p_{i} + \tfrac{1 - S}{3})t^{-2}$, which vanish together exactly at the three flat Milne points and the isotropic point $(\tfrac13, \tfrac13, \tfrac13)$; so under (P1) the attachment supplies no state near the wall at any other point and the state must come from (P2), and in cosmic time neither Weyl-flat case is a tame wall (in conformal time the isotropic point is the radical-normal wall).
