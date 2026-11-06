---
id: synthesis.euler-entropy-of-a-horizon-patch-is-an-edge-term
kind: claim
version: 2
title: 'The Euler entropy of a horizon patch is an edge term'
status: proved
region: synthesis
subject: einstein
tags: [horizons, curvature-and-field-equations, thermal-premises, no-go, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-31-gravity-action
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
  - synthesis.euler-term-horizon-entropy-shift@4
  - synthesis.imported-wald-noether-charge-entropy@3
  - synthesis.series-wald-entropy-changes-without-flux-on-local-horizons@2
  - synthesis.euler-entropy-first-order-rate-on-local-patches@2
  - synthesis.sds-clausius-fixes-area-constant@4
  - synthesis.einstein-equations-from-c-loc-and-clausius@7
  - dark-energy.wall-counterterm@4
  - synthesis.imported-gtg-dictionary@1
  - synthesis.imported-gauss-bonnet-with-corners-poincare-hopf-and-edge-term@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_euler_density_is_the_cut_transgression
- kind: check
  ref: check.py::check_edge_term_makes_patch_euler_entropy_topological
- kind: check
  ref: check.py::check_clutching_winding_is_the_euler_number
- kind: check
  ref: check.py::check_edge_term_gauge_and_winding
- kind: check
  ref: check.py::check_counterterm_restores_area_density_on_sds_generators
- kind: check
  ref: check.py::check_closed_cut_residual_is_the_stored_shift
- kind: check
  ref: check.py::check_disk_patch_entropy_sign_and_non_additivity
- kind: check
  ref: check.py::check_wall_counterterm_anomaly_is_the_edge_transgression
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.series-wald-entropy-changes-without-flux-on-local-horizons
  - dark-energy.wall-counterterm
  - synthesis.c-loc-local-horizon-premise
extraction:
  open_problem: op.derive-gravitational-action
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 1 -> 2: Gauss-Bonnet with edge and corners, Poincare-Hopf with the clutching number and the two-dimensional Gibbons-Hawking term, cited from memory, now point to the imported Fact approved by Leon, added to uses since (ii) and (iii) rest on it; the gauge variation of a Chern-Simons form points to the Chern-Weil and Chern-Simons Fact (text only, the identity is checked exactly here); the BF result, cited as filed alongside in a remark, is a claimref (text only); pin moved to version 6 of the Einstein-from-Clausius result (an added note). Statement unchanged.'
  note: >-
    Decides the Euler-term question of the problem on the model of the wall counterterm. The Euler part of the
    Jacobson-Myers density on any cut is exact on the cut (the two-dimensional transgression), so its value on a
    patch is an edge quantity: the holonomy angle of the cut's own rotation-gauge field around the edge, measured
    against a frame smooth on the patch. The edge term of the two-dimensional Euler functional (the geodesic
    curvature of the edge plus corner turns, its Gibbons-Hawking term), a choice within the edge ambiguity of the
    Noether charge on open patches (argued, not derived), turns the Euler part of every patch into the constant 2 pi alpha chi(P); then the
    entropy changes along every local horizon carry no Euler contribution and the Clausius relation holds where
    the bare Jacobson-Myers reading fails (radial Schwarzschild-de Sitter generators). What remains is a
    topological constant per patch, the open-patch form of the stored closed-cut shift; no additive edge term
    built from the field and the cut removes it, and a frame-relative (Chern-Simons) edge term, the wall
    counterterm one dimension down (a reading supported by an exact identity), moves it into frame singularities or clutching windings. So the two routes
    agree on entropy changes and differ on entropy values only by that constant, which the stored normalisation
    (Z), nonnegativity, or the integrated reading of (Loc) removes; the exclusion of the Euler term is not
    derived from transport. For Lambda > 0 the constant makes the edge-corrected entropy negative on every disk
    patch of area below 6 pi/Lambda, half the de Sitter horizon area, so it is usable as an entropy only after
    the normalisation; this matches the adopted reading that horizon entropy is (Loc), not the action's Wald
    entropy, with the Euler exclusion recorded as the normalisation (Z). Remark (argued): in the BF variables
    of \claimref{synthesis.frozen-point-action-is-bf-transport-broken-by-the-blade-i-wedge-x}, the
    Jacobson-Myers density on an admissible edge is, up to a constant, the binormal component of the on-shell B,
    so the Wald entropy is the flux of B through the cut; the soldering part of the Cartan curvature gives the
    quarter and the Lorentz-curvature part the Euler part, so (Loc) keeps the flux of the soldering part only.
    Transport-absent (the series supplies alpha): Gauss-Bonnet, Poincare-Hopf and the clutching construction
    are classical. Literature:
    Gauss-Bonnet with boundary and corners, Poincare-Hopf, the clutching description of the Euler number
    and the two-dimensional Gibbons-Hawking term are \claimref{synthesis.imported-gauss-bonnet-with-corners-poincare-hopf-and-edge-term};
    the gauge variation of a Chern-Simons form is \claimref{synthesis.imported-chern-weil-and-chern-simons-forms}.
---

## formal
Units $\hbar = c = G = 1$; $\Lambda \neq 0$ and $\alpha = -3/(4\Lambda)$, the Euler coefficient of the series' Lagrangian $(R - 2\Lambda + \alpha E_{4})/16\pi$ (Theorem \claimref{synthesis.euler-term-horizon-entropy-shift}(i)). Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), $\Sigma$ a spacelike two-surface element (a cut of a local horizon) with its Riemannian induced metric, Gauss curvature $K$ (${}^{(2)}\!R = 2K$) and area element $dA$, and for a compact patch $P \subset \Sigma$ with piecewise smooth edge let $S[P] = \tfrac14\int_{P}(1 + 2\alpha\,{}^{(2)}\!R)\,dA = A(P)/4 + S_{E}[P]$, $S_{E}[P] = \alpha\int_{P}K\,dA$, be the Jacobson-Myers functional of Fact \claimref{synthesis.imported-wald-noether-charge-entropy}(c) evaluated on the patch, as in (W$_{\mathrm{loc}}$) of Theorem \claimref{synthesis.series-wald-entropy-changes-without-flux-on-local-horizons}.
\begin{enumerate}
\item[(i)] \emph{(Transgression on the cut.)} For every orthonormal frame $(e_{2}, e_{3})$ tangent to $\Sigma$ on an open set $U$, with $\omega_{\Sigma}$ the rotation-gauge field of the cut in that frame (the $e_{2}\wedge e_{3}$ component of its connection one-form, $de^{2} = -\omega_{\Sigma}\wedge e^{3}$, $de^{3} = \omega_{\Sigma}\wedge e^{2}$), $d\omega_{\Sigma} = K\,e^{2}\wedge e^{3}$. Hence on every patch $P \subset U$ on which the frame is smooth, $S_{E}[P] = \alpha\oint_{\partial P}\omega_{\Sigma}$, $\alpha$ times the holonomy angle of the cut's own rotation-gauge field (its Levi-Civita connection) around the edge, measured against the frame smooth on $P$; under a rotation of the frame by $\theta$, $\omega_{\Sigma} \mapsto \omega_{\Sigma} - d\theta$, so the edge integral is unchanged for $\theta$ smooth on $P$ and shifts by $-2\pi w$ for winding $w$ along the edge, $S_{E}$ by $-2\pi\alpha w$. (Reading.) In a frame adapted to the cut this edge term is the wall counterterm one dimension down, a reading supported by the following exact identities: the Chern-Simons form $Q(\omega)$ of Proposition \claimref{dark-energy.wall-counterterm} has gauge variation $\delta_{\lambda}Q = d\bigl(\epsilon_{abcd}\lambda^{ab}d\omega^{cd}\bigr)$ (for $\delta\omega = D\lambda$), whose two-form $\epsilon_{abcd}\lambda^{ab}d\omega^{cd}$ is $4\,d\omega^{23}$ for $\lambda$ the binormal $e_{0}\wedge e_{1}$ of the cut, and on the cut $R^{23} - d\omega^{23} = -(b_{2}\wedge a_{3} + a_{2}\wedge b_{3})$ with $a_{A} = \omega^{A0} - \omega^{A1}$ and $b_{A} = \tfrac12(\omega^{A0} + \omega^{A1})$ the extrinsic forms along the null normals $k = e_{0} + e_{1}$ and $l$, which vanishes on admissible cuts ($a = 0$, the local Rindler cuts of Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius}).
\item[(ii)] \emph{(The edge term.)} By Gauss-Bonnet with edge and corners (Fact \claimref{synthesis.imported-gauss-bonnet-with-corners-poincare-hopf-and-edge-term}(a)), for every patch $P$, with $k_{g}$ the geodesic curvature of its edge in $\Sigma$ (the rate at which the edge tangent turns against the cut's own parallel transport along the edge) and $\varepsilon_{j}$ the turning angles at its corners,
\[
S_{E}[P] + \alpha\Bigl(\oint_{\partial P}k_{g}\,ds + \sum_{j}\varepsilon_{j}\Bigr) \;=\; 2\pi\alpha\,\chi(P) \;=\; -\frac{3\pi\,\chi(P)}{2\Lambda} .
\]
So with the edge term $E[\partial P] = \alpha(\oint k_{g}\,ds + \sum_{j}\varepsilon_{j})$ added (the two-dimensional Gibbons-Hawking term of the Euler functional, Fact \claimref{synthesis.imported-gauss-bonnet-with-corners-poincare-hopf-and-edge-term}(c); on open patches the Noether charge is fixed only up to edge terms, and choosing this one is argued, not derived), the Euler part of the entropy of every patch is a constant fixed by its topology, $-3\pi/(2\Lambda)$ for a disk. Along the generators of any local horizon, patches keep their topology, so the entropy $S'[P] = S[P] + E[\partial P] = A(P)/4 + 2\pi\alpha\chi(P)$ changes as $\delta A/4$: on the radial generators of every Schwarzschild-de Sitter hole, where the bare density $-3M/(2\Lambda r^{3})$ varies with no area change and no flux, $\delta S' = 0 = \delta Q$, and on every admissible element the first-order defect of Theorem \claimref{synthesis.euler-entropy-first-order-rate-on-local-patches}(ii) is absent; the Clausius relation (H1) holds for $S'$ on every open patch on which it holds for $A/4$.
\item[(iii)] \emph{(What no edge term removes.)} No edge term that is additive under gluing (equal and opposite on the two orientations of a shared edge) and determined by the field and the cut alone makes $S_{E}$ vanish on every patch: cutting a closed cut along a circle into two disks, the edge terms cancel while $\alpha\int_{\Sigma}K\,dA = 2\pi\alpha\chi(\Sigma) \neq 0$ for a sphere. The geodesic-curvature term of (ii) leaves $2\pi\alpha\chi(P)$ on each patch (its corner turns are not additive); the frame-relative term of (i) is additive but needs a frame smooth on each patch, and on a sphere the frames smooth on two complementary caps differ along the common edge by a rotation of winding $2 = \chi$ (the clutching number, Fact \claimref{synthesis.imported-gauss-bonnet-with-corners-poincare-hopf-and-edge-term}(b)), which carries the same $2\pi\alpha\chi$. On closed cuts every choice leaves $2\pi\alpha\chi = -3\pi\chi/(2\Lambda)$, the shift of Theorem \claimref{synthesis.euler-term-horizon-entropy-shift}(ii), equal to $-\chi/2$ times the de Sitter entropy $3\pi/\Lambda$; it is removed by the normalisation (Z) or by nonnegativity (Theorem \claimref{synthesis.sds-clausius-fixes-area-constant}(v)), not by an edge term. On open patches the constant is not negligible: for $\Lambda > 0$, $S'[P] = A(P)/4 - 3\pi/(2\Lambda)$ on every disk patch, negative whenever $A(P) < 6\pi/\Lambda$, half the de Sitter horizon area $12\pi/\Lambda$; $S'$ is non-additive and is usable as an entropy only after the normalisation.
\item[(iv)] \emph{(The two routes.)} Read with the edge term of (ii), the Wald (Jacobson-Myers) entropy of the series' action and the entropy of the Clausius route agree on every entropy change of an open patch and differ on values by the topological constant $2\pi\alpha\chi(P)$ alone. The open-patch disagreement of Theorem \claimref{synthesis.series-wald-entropy-changes-without-flux-on-local-horizons} is therefore the bare functional's missing edge term, and the remaining disagreement is one constant on open patches and closed cuts alike. Since $A(P)/4 + 2\pi\alpha\chi(P)$ is not the integral of a density, the integrated reading of (Loc) excludes the constant, and so excludes the Euler term from horizon entropy; on the differences reading it is invisible. Transport fixes neither: the exclusion of the Euler term stays a decision (the normalisation (Z), with horizon entropy read as (Loc) rather than the action's Wald entropy), not a consequence of the series' objects; nothing in (i) to (iii) uses the series' objects beyond the value of $\alpha$.
\end{enumerate}

## technical
Take the series' Lagrangian $(R - 2\Lambda + \alpha E_{4})/16\pi$, $\alpha = -3/(4\Lambda)$, and read the entropy of a patch $P$ of a cut as the Jacobson-Myers functional, $A(P)/4$ plus the Euler part $S_{E}[P] = \alpha\int_{P}K\,dA$. On a cut, $K\,dA$ is exact: $K\,e^{2}\wedge e^{3} = d\omega_{\Sigma}$ with $\omega_{\Sigma}$ the cut's rotation-gauge field in any tangent frame. So $S_{E}[P]$ is an edge quantity, $\alpha$ times the holonomy angle of the cut's own rotation-gauge field around the edge, measured against a frame smooth on $P$, unchanged by smooth frame rotations and shifted by $-2\pi\alpha w$ for a frame winding $w$ times along the edge. As a reading, in an adapted frame this is the Chern-Simons wall counterterm one dimension down: the gauge variation of $Q(\omega)$ under the cut's binormal is $4\,d\omega^{23}$, and on admissible cuts $R^{23} = d\omega^{23}$ there.

By Gauss-Bonnet, $S_{E}[P] + \alpha(\oint k_{g}\,ds + \sum\varepsilon_{j}) = 2\pi\alpha\chi(P)$. With this geodesic-curvature edge term added (the two-dimensional Gibbons-Hawking term, a choice within the edge ambiguity of the Noether charge on open patches, argued not derived), the Euler part of every patch is the constant $-3\pi\chi(P)/(2\Lambda)$, so entropy changes along a local horizon are $\delta A/4$: on radial Schwarzschild-de Sitter generators the change is zero, matching the zero heat flux, where the bare density changes as $-3M/(2\Lambda r^{3})$. No additive edge term built from the field and the cut removes the constant (on a sphere cut into two disks the edge terms cancel and $4\pi\alpha$ is left); a frame-relative edge term moves it into the clutching winding $\chi$ of the cap frames. On closed cuts every choice leaves the stored shift $-3\pi\chi/(2\Lambda)$, which the normalisation (Z) or nonnegativity removes; on open patches, for $\Lambda > 0$, it makes the edge-corrected entropy negative on every disk patch of area below $6\pi/\Lambda$. So, with that edge term, the action and Clausius routes agree on entropy changes and differ by one topological constant; the integrated reading of (Loc) excludes it, transport does not. Transport-absent: the series supplies only $\alpha$.

## lay
The series' gravitational action contains an extra term (the Euler term) which leaves Einstein's equations unchanged but, in the standard recipe, adds a curvature-dependent piece to the entropy of a horizon. A stored result showed that this piece changes along small patches of a horizon with no heat flowing, which clashes with the heat-balance route to Einstein's equations. This result shows that the troublesome piece of a patch is really a property of the patch's edge: it equals a fixed multiple of the angle by which a direction carried around the edge within the patch's own surface turns. Adding the standard edge correction (how sharply the edge bends), which is a natural choice rather than one forced by the action, turns the piece into a fixed number set only by the patch's shape type, the same for every disk-shaped patch. Then the entropy changes exactly as the heat-balance route requires. What is left is a constant that no edge correction can remove; it is the same constant already known for closed horizons, and it is removed by the existing normalisation, not by anything in the series' objects. Without that normalisation the constant would even make the entropy of small patches negative.

## one-liner
The Euler part of the series' Jacobson-Myers entropy of a horizon patch is exact on the cut, $\alpha\oint_{\partial P}\omega_{\Sigma}$ (the holonomy angle of the cut's own rotation-gauge field around the edge; read as the wall counterterm one dimension down); with the edge's geodesic-curvature term (the two-dimensional Gibbons-Hawking term, a choice within the edge ambiguity of the Noether charge, argued not derived) it becomes $2\pi\alpha\chi(P) = -3\pi\chi(P)/2\Lambda$, so with that edge term the action and Clausius routes agree on every entropy change of an open patch (zero change on radial Schwarzschild-de Sitter generators) and differ only by that topological constant, which no additive edge term built from the field and the cut removes and which for $\Lambda > 0$ makes the entropy negative on every disk patch of area below $6\pi/\Lambda$ and which the stored normalisation (Z) or the integrated reading of (Loc) excludes. Transport-absent (the series supplies $\alpha$).
