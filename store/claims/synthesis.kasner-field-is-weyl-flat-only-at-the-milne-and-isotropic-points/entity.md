---
id: synthesis.kasner-field-is-weyl-flat-only-at-the-milne-and-isotropic-points
kind: claim
version: 2
title: 'Kasner fields are Weyl-flat only at the Milne and isotropic points'
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
- name: Claude Opus 5.5
  role: 'GA rewrite (Weyl eigenvalue stated for the Weyl map; proof route declared)'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG proof of (i): Omega from the torsion equation of the synchronous gauge field, store-sign field strength, Ricci and Weyl maps; coordinate route kept as a labelled reading'
  version: 2
  source: maintainer pass 2026-11-07 (GTG proofs)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching@3
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
- kind: check
  ref: check.py::check_gtg_kasner_field_strength_and_weyl_map
lineage:
  motivated_by:
  - synthesis.pre-descent-contracting-kasner-stage-premise
  - synthesis.pre-descent-state-carried-into-descended-phase-premise
  - synthesis.attachment-transport-is-flat-only-where-weyl-vanishes
extraction:
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'GTG proof made the main proof for (i): the synchronous gauge field hb^{-1}(e_t) = e0, hb^{-1}(e_i) = t^{p_i} e_i (derived metric -g_p, dictionary C7), Omega(e_{x^i}) = -p_i t^{p_i - 1} B_i from the torsion equation, the field strength and calR(B_i) = p_i(p_i - 1) t^-2 B_i, calR(e_i ^ e_j) = p_i p_j t^-2 e_i ^ e_j, the Ricci map (S - 1) t^-2 on e0 and 0 on e_j, scalar (S - 1) t^-2, and the Weyl map W(B_i) = W(I4 B_i)/I4 = lambda_i with the sign of the (-,+,+,+) mixed component derived from C11; (ii) and (iv) read flatness off the field strength (the isotropic bracket has Omega = 0); the Christoffel route is kept as a labelled reading. New check check_gtg_kasner_field_strength_and_weyl_map (seven rational points of the plane, torsion-solved Omega on exact jets, the bracket field); runcheck 4/4, check4 clean on a proposals copy. The proof cites the dictionary Fact for the Weyl formula, which is not in uses (a links question left for Leon). outside_ga removed: no stand-in remains. Statement, status, links unchanged.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The eigenvalue is stated for the Weyl map on bivectors with the mixed component C_{0i}^{0i} = C_{jk}^{jk} as a labelled reading; the proof and its check compute the Weyl components from the coordinate Riemann tensor of the diagonal metric (Christoffel route) and are kept, declared outside_ga (other): a GTG derivation through the rotation-gauge field would be a different proof, listed for Leon. Reader fix (R06), version kept: the formal declares the (-,+,+,+) signature of its line element and says that lambda_i are store-sign eigenvalues of the Weyl map (the mixed component C_{0i}^{0i} of the round-sphere-positive tensor in that signature agrees in sign with the store''s operator: +2M/r^3 on the Schwarzschild radial boost plane, Lambda/3 on de Sitter) and that R t^2 = -2/3 holds in the store''s sign.'
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
Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) whose derived metric is the four-dimensional diagonal Kasner field $g_{p} = -dt^{2} + t^{2p_{1}}dx^{2} + t^{2p_{2}}dy^{2} + t^{2p_{3}}dz^{2}$, $t > 0$, with $p_{1} + p_{2} + p_{3} = 1$ (the Kasner plane of Theorem \claimref{synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching} with three exponents; no field equation imposed, and under Einstein's equations the source is stiff, $P = \rho$). Put $S = \sum p_{i}^{2}$, $E_{1} = p_{1}^{2} - 2p_{1}p_{2} - p_{1} - 2p_{2}^{2} + 2p_{2}$, $E_{2} = 2p_{1}^{2} + 2p_{1}p_{2} - 2p_{1} - p_{2}^{2} + p_{2}$, and let $e_{0}, e_{1}, e_{2}, e_{3}$ be the orthonormal frame of $g_{p}$. The line element is written in the signature $(-,+,+,+)$ (dictionary C7); the eigenvalues $\lambda_{i}$ below are those of the Weyl part of the store's curvature operator $\mathcal{R}$ on the physical bivectors (in components the mixed $C_{0i}{}^{0i}$ of the round-sphere-positive tensor in that signature, which has the store's sign: both give $+2M/r^{3}$ on the radial boost plane of Schwarzschild and $\Lambda/3$ on de Sitter), and the scalar curvature $Rt^{2} = -\tfrac23$ has the same value in the store's sign in $(+,-,-,-)$.
\begin{enumerate}
\item[(i)] \emph{(The Weyl map; proved.)} The Weyl map on bivectors has the frame bivectors $e_{0}\wedge e_{i}$ and their duals $I_{4}\,e_{0}\wedge e_{i}$ as eigenvectors, with the same eigenvalue $\lambda_{i}$ on both ($\{i, j, k\} = \{1, 2, 3\}$; in components the mixed Weyl component $C_{0i}{}^{0i} = C_{jk}{}^{jk}$): $\lambda_{i} = (p_{i}^{2} - p_{i} + \tfrac{1 - S}{3})\,t^{-2}$, so $\lambda_{1} = E_{1}/(3t^{2})$, $\lambda_{2} = -E_{2}/(3t^{2})$, $\lambda_{1} + \lambda_{2} + \lambda_{3} = 0$. So the Weyl curvature vanishes exactly where $E_{1} = E_{2} = 0$, and elsewhere it is nonzero at every $t > 0$ and grows as $t^{-2}$ toward the wall.
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
