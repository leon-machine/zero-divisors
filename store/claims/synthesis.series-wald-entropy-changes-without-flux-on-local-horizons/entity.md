---
id: synthesis.series-wald-entropy-changes-without-flux-on-local-horizons
kind: claim
version: 3
title: 'Wald entropy changes without flux on local horizons, against (Loc)'
status: proved
region: synthesis
subject: einstein
tags: [horizons, curvature-and-field-equations, no-go, thermal-premises, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-23-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG proof: field strength of the SdS gauge field in the PG chart, sectional curvature as <calR(B) B^-1>, surface gravity as (xi.D)xi; G6 applied; exact checks'
  version: 3
  source: maintainer pass 2026-11-07 (GTG proofs)
- name: Claude Opus 5.5
  role: 'GTG review fixes (referee F2): the cross-section sentence of proof (i) corrected, the sectional-curvature convention stated, outside_ga made exact; check tightened'
  version: 3
  source: maintainer pass 2026-11-07 (GTG review fixes)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.euler-term-horizon-entropy-shift@5
  - synthesis.imported-wald-noether-charge-entropy@3
  - dark-energy.imported-macdowell-mansouri-theorem-stelle-west@4
  - synthesis.imported-raychaudhuri-null-congruence@2
  - synthesis.einstein-equations-from-c-loc-and-clausius@8
  - synthesis.sds-clausius-fixes-area-constant@5
  - synthesis.imported-gtg-dictionary@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_sds_radial_generator_data
- kind: check
  ref: check.py::check_density_is_cartan_curvature
- kind: check
  ref: check.py::check_entropy_change_without_flux
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_gtg_sds_field_strength_on_radial_generators
- kind: check
  ref: check.py::check_gtg_horizon_cross_section_surface_gravity_and_value
lineage:
  motivated_by:
  - synthesis.euler-term-horizon-entropy-shift
  - synthesis.c-loc-local-horizon-premise
extraction:
  maintainer_pass_gtg_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Referee F2 findings applied. (1) Proof (i) said that on the cross-section {t = t_0, r = r_b} of the horizon locus both null second fundamental forms vanish (Killing horizon); the sentence came with item G6 and is false off the bifurcation surface. Computed exactly with the SdS PG field at three rational horizons (r_b, Lambda) = (1, 3/4), (2, 3/16), (1/2, 3/2): chi^(xi)(e_A, e_B) = e_B . ((e_A . D) xi) = 0 for A, B in {2, 3}, while the expansion of n = e_0 - e_1 is -4/r_b. The step needs only chi^(xi) = 0 (formula (i) with k = xi), so the sentence now says that, with the other normal''s expansion and the bifurcation surface named; the value A/4 - 3 pi/Lambda is unchanged. check_gtg_horizon_cross_section_surface_gravity_and_value now asserts chi^(xi) = 0 and theta_n = -4/r_b (mutants: xi -> e_0 - beta e_1, n -> xi, and a forced failure of the chi assertion all fail). The formal level is not affected: its (i) assumes only that the second fundamental form along one null normal vanishes, and its cross-section clause names xi. (2) The proofs "positive on round spheres in either convention" replaced by the exact statement: K = <calR(B) B^{-1}> is the sectional curvature for the planes positive-definite induced metric because the vectors of a spacelike plane of Cl(1,3) square to -1 (B^2 = -1); on a plane whose vectors square to +1 the stores sign gives -K (checked on S^2 in Cl(2,0) and Cl(0,2): calR(J) = -J and +J). (3) outside_ga widened to the formal levels component displays (F_abcd, R(k, A, k, B), R(k, A, B, C), k_pm in static coordinates, signature (-,+,+,+)), whose GA forms are in the proof. (4) uses: synthesis.imported-gtg-dictionary@2 added (C11 and clauses (i), (ii), (iv) are cited for the translation steps); synthesis.c-loc-local-horizon-premise is a postulate and not added (listed for Leon; the result refutes (W_loc) against it and does not rest on it). Repinned euler-term-horizon-entropy-shift 4 -> 5 (GA notation for the Euler form; the cited (i), (ii) values hold), einstein-equations-from-c-loc-and-clausius 7 -> 8 (a clause label), sds-clausius-fixes-area-constant 4 -> 5 (formal unchanged). Version kept at 3.'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Item G6 (DECISIONS.md, Leon 7 November): proof (i) evaluates on a cross-section {t = t_0, r = r_b} of the horizon locus in the Painleve-Gullstrand chart in place of the bifurcation sphere (the item''s parenthetical, both null second fundamental forms vanish on the Killing horizon, was false and is corrected by maintainer_pass_gtg_review: only the one along xi vanishes), as the formal level and the dictionary''s bifurcation rule have it. Wording in the proof; the value A/4 - 3 pi/Lambda is unchanged (checked at three rational horizons by check_gtg_horizon_cross_section_surface_gravity_and_value).'
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Proof rewritten in GTG (store signature; the quantities used, K = <calR(B) B^{-1}> of a spacelike plane, K - Lambda/3 and the vanishing of (k ^ B) . calR(k ^ A), are the same in the statement''s signature): SdS in the PG chart, calR(B) = (M/2r^3)(B + 3 sigma B sigma) + (Lambda/3) B, K = 2M/r^3 + Lambda/3 on e_2 ^ e_3, calR(k ^ A) = (Lambda/3 - M/r^3) k ^ A for k radial null and A transverse, so R(k, A, k, B) = R(k, A, B, C) = 0; k_+ = (e_0 + e_1)/(1 - beta), k_- = (e_0 - e_1)/(1 + beta); the transverse frame is D-parallel along both (Omega(hb(e_1)) = -beta'' e_1 e_0 commutes with e_2, e_3). Item G6 applied (maintainer_pass_decisions): proof (i) on a cross-section {t = t_0, r = r_b} of the horizon locus in the PG chart, with xi = hb^{-1}(e_t) null and (xi.D)xi = kappa_b xi there. The Christoffel computation is kept as a labelled reading. Checked exactly: check_gtg_sds_field_strength_on_radial_generators (three points of the static region: Ricci map Lambda a, the transverse eigenvalue, the two vanishing contractions for both signs, sectional curvature unchanged at three tilts, transverse frame parallel, the density -3M/(2 Lambda r^3); de Sitter K = Lambda/3 on two planes) and check_gtg_horizon_cross_section_surface_gravity_and_value (three rational horizons: beta = 1, xi null, (xi.D)xi = (f''(r_b)/2) xi, and 4 r_b^2 s = r_b^2 - 3/Lambda in units of pi). Version kept at 3 (already above the lock in this run). outside_ga narrowed to the component Gauss and Sachs equations.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: The Wald-entropy computation works in the components of the Riemann tensor of the derived metric (F_abcd, h^{ac} h^{bd} R_{abcd}, binormals) in the source''s signature (-,+,+,+), as the Wald formula is stated; the components are the computation.'
  open_problem: op.horizon-entropy-functional
  note: >-
    Settles the open-patch question left by the Euler-term result: whether the topological shift of the
    Wald entropy of the series' MacDowell-Mansouri action affects a Clausius relation on small open
    patches. It does, at first order, already in vacuum. On a local edge the Jacobson-Myers density is the
    Cartan curvature of the edge plane (zero on de Sitter); along the radial generators of a
    Schwarzschild-de Sitter hole the expansion and shear vanish identically for every admissible cut while
    this density changes, with opposite signs inward and outward. Hence the Wald reading, extended to local
    horizons, meets refutation condition (a) of the local-horizon premise and fails the Clausius relation
    and the second law; with the premise adopted, the Euler term is excluded from horizon entropy (it stays
    in the action). The change is the value at p of a divergence on the cut and cancels over any closed cut, so
    what fails is the Clausius relation on open patches in the thin-pencil limit, with entropy a functional of
    the cut. The general first-order rate on any local patch is filed alongside,
    synthesis.euler-entropy-first-order-rate-on-local-patches; on radial Schwarzschild-de Sitter generators it
    reduces to the gradient term, whose value, and the exact all-orders change, are computed here.
    Transport-absent: classical geometry of the series' action. Literature cited from
    memory in the proof: the Gauss equation for a codimension-two surface, the Jacobson-Kang-Myers
    ambiguity of the Wald entropy off stationary horizons, and the Eling-Guedens-Jacobson entropy-production
    reading of the Clausius relation.
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the Lagrangian is that of a gravitational field on flat spacetime, the Cartan curvature is the Lorentz block of the MacDowell-Mansouri field strength (R(B) - (Lambda/3) B in the store''s sign), de Sitter space is the de Sitter field, and Schwarzschild-de Sitter is the field in the Painleve-Gullstrand gauge beta^2 = 1 - f. Following Leon''s decision on bifurcation surfaces (DICTIONARY), the integral over the bifurcation sphere in (i) is restated on a cross-section of the horizon locus r = r_b in the Painleve-Gullstrand chart (same area, same surface gravity, same value A/4 - 3 pi/Lambda), with the note that the bifurcation surface itself is beyond one chart. Signature (-,+,+,+) kept as declared. Clauses (i) to (iii) and their strength unchanged; proof given a pointer to the dictionary Fact. Fix (referee GR1, 2026-10-23): the Killing field renamed xi (K is the sectional curvature) with kappa_b = f''(r_b)/2 defined; F is minus the Lorentz block of the MacDowell-Mansouri field strength, matching the Fact''s -(R(B) - B/l^2).'
outside_ga:
  kind: other
  why: 'The Gauss equation of the cut and the Sachs equation are used in their component form (h^{ac} h^{bd} R_abcd, chi_AB, theta), as the standard Gauss equation and the imported Raychaudhuri Fact state them, and the formal level states the Cartan curvature F_abcd, the contractions R(k, A, k, B) and R(k, A, B, C) and the generators k_pm = f^{-1} d_t pm d_r in components in the source''s signature (-,+,+,+); their GA forms (K - Lambda/3 = <(calR(B) - Lambda/3 B) B^{-1}>, (k ^ B) . calR(k ^ A), (B ^ C) . calR(k ^ A), k_pm = (e_0 pm e_1)/(1 mp beta)) and the curvature computation itself are in the proof, in GTG.'
---

## formal
Units $\hbar = c = G = 1$, signature $(-,+,+,+)$, Riemann tensor positive on spheres, read from the field strength of a gravitational field $(\hb, \Omega)$ on flat spacetime with derived metric $g$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). Let $\Lambda > 0$, $\alpha = -3/(4\Lambda)$, and let the gravitational Lagrangian of the field be the series' $(R - 2\Lambda + \alpha E_{4})/16\pi$ (Theorem \claimref{synthesis.euler-term-horizon-entropy-shift}(i), from Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west}). Let (W$_{\mathrm{loc}}$) be the hypothesis (W) of that theorem extended to the local Rindler horizons of Premise \claimref{synthesis.c-loc-local-horizon-premise}: the entropy of a cut $\Sigma$ of a local horizon is the Jacobson-Myers functional $S[\Sigma] = \tfrac14\int_{\Sigma}(1 + 2\alpha\,R_{\Sigma})\,dA$ of Fact \claimref{synthesis.imported-wald-noether-charge-entropy}(c), $R_{\Sigma}$ the scalar curvature of $\Sigma$.
\begin{enumerate}
\item[(i)] \emph{(The density on a local edge.)} At a point of $\Sigma$ where the second fundamental form along one null normal $k$ vanishes, $R_{\Sigma} = 2K$ with $K$ the sectional curvature of the tangent plane, and the density is
\[
s \;=\; \tfrac14\bigl(1 - 3K/\Lambda\bigr) \;=\; -\frac{3}{4\Lambda}\,F(e_{2}, e_{3}, e_{2}, e_{3}),
\]
with $F_{abcd} = R_{abcd} - \tfrac{\Lambda}{3}(g_{ac}g_{bd} - g_{ad}g_{bc})$ the Cartan curvature of the MacDowell-Mansouri square (minus the Lorentz block of its field strength, $-\mathcal{F}(B) = \mathcal{R}(B) - \tfrac{\Lambda}{3}B$ in the store's sign, the Lorentz block of Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west} being $-(\mathcal{R}(B) - B/l^{2})$, evaluated on the edge plane) and $e_{2}, e_{3}$ an orthonormal basis of the plane. For the de Sitter field every plane has $K = \Lambda/3$, so $s = 0$ on every local edge. Integrated over a cross-section $\{t = t_{0},\ r = r_{b}\}$ of the horizon locus of a Schwarzschild-de Sitter hole in the Painlev\'e-Gullstrand chart ($\hb = 1 - \beta P$, $\beta^{2} = 1 - f(r)$ with $f$ as in (ii)), of area $A = 4\pi r_{b}^{2}$, on which the Killing field $\xi = \hb^{-1}(e_{t})$ is null and normal to the horizon with $(\xi \cdot D)\xi = \kappa_{b}\xi$, $\kappa_{b} = f'(r_{b})/2$ its surface gravity, $s$ gives $A/4 - 3\pi/\Lambda$, the value of Theorem \claimref{synthesis.euler-term-horizon-entropy-shift}(ii).
\item[(ii)] \emph{(Radial generators of Schwarzschild-de Sitter.)} Let $f(r) = 1 - 2M/r - \Lambda r^{2}/3$ with $M > 0$, the metric function of the Schwarzschild-de Sitter field, $p$ a point of the static region $f > 0$ at radius $r_{0}$, and $k_{\pm} = f^{-1}\partial_{t} \pm \partial_{r}$ (in the static coordinates of the derived metric), the affinely parametrised radial future null directions at $p$. For either sign and for every cut through $p$ orthogonal to $k_{\pm}$ with vanishing expansion and shear at $p$ (any tilt of its tangent plane along $k$, any normalisation of $k$ along it): $R(k, A, k, B) = 0$ and $R(k, A, B, C) = 0$ along the generator $\gamma$ through $p$ for transverse $A, B, C$; hence the expansion and shear vanish along all of $\gamma$, the area per unit cross-section is constant along it, and no matter crosses ($\delta Q = 0$). Along $\gamma$, $r(\lambda) = r_{0} \pm \lambda$ and the density of (i) is
\[
s(\lambda) \;=\; -\frac{3M}{2\Lambda\,r(\lambda)^{3}} .
\]
So per unit cross-section area, in the thin-pencil limit of Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius}(H2), the patch $\lambda \in [\lambda_{0}, 0]$ changes its (W$_{\mathrm{loc}}$) entropy by
\[
\Delta S \;=\; -\frac{3M}{2\Lambda}\Bigl(\frac{1}{r_{0}^{3}} - \frac{1}{(r_{0} \pm \lambda_{0})^{3}}\Bigr) \;=\; \pm\frac{9M}{2\Lambda r_{0}^{4}}\,|\lambda_{0}| + O(\lambda_{0}^{2}),
\]
positive for the outgoing and negative for the ingoing horizon, while $\delta A = 0$ and $\delta Q = 0$.
\item[(iii)] \emph{(Consequences.)} Under (W$_{\mathrm{loc}}$): the entropy change of the radial local horizons of every Schwarzschild-de Sitter hole is not $\eta\,\delta A$ for any $\eta$, which is refutation condition (a) of Premise \claimref{synthesis.c-loc-local-horizon-premise}; the Clausius relation (H1) of Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius} fails at first order in $\lambda_{0}$ in vacuum, the defect being that theorem's integrated-reading term $(k\cdot\nabla s)\lambda_{0}$ with $k\cdot\nabla s = \pm 9M/(2\Lambda r_{0}^{4})$; and since the entropy falls along the ingoing horizon with no flux, no reading $dS = \delta Q/T + d_{i}S$ with $d_{i}S \ge 0$ restores it. The same holds for every entropy functional that differs from the Jacobson-Myers one by terms vanishing where the $k$-extrinsic curvature vanishes, or by functions of the Ricci tensor. The area term alone, $A/4$, is constant along these generators and consistent with (H1). The change is the value at $p$ of a divergence on the cut: it cancels over any closed cut (Theorem \claimref{synthesis.euler-term-horizon-entropy-shift}(ii)), so the failure is of the Clausius relation on open patches, as (H1) and (H2) require it, with the entropy of a patch the integral of the density over the patch (a functional of the cut) taken per unit cross-section area in the thin-pencil limit.
\end{enumerate}
Hence, with entropy a functional of the cut and (H1) imposed on open patches, (C$_{\mathrm{loc}}$) and (W$_{\mathrm{loc}}$) cannot both hold, nor can (H1) and (W$_{\mathrm{loc}}$). The general first-order rate of the Euler entropy on any local patch is filed alongside, synthesis.euler-entropy-first-order-rate-on-local-patches; on radial Schwarzschild-de Sitter generators it reduces to the curvature-gradient term evaluated in (ii). With (C$_{\mathrm{loc}}$) adopted, horizon entropy on local horizons is not the Wald functional of the series' action: the Euler term must be left out of the entropy functional, while it stays in the action, where it is topological. Together with Theorem \claimref{synthesis.sds-clausius-fixes-area-constant}(v), which excludes its constant shift on closed horizons, this gives the de Sitter entropy $3\pi/\Lambda = \pi N^{2}$ and the Einstein-Hilbert nucleation exponent $-1$, not $0$ and $-4$. The bifurcation surface itself, where the boost flow has its fixed points, lies beyond one flat chart (it is the meeting of the four regions of the maximal extension); the chart contains the future horizon, on whose cross-sections the area, the surface gravity and the boost flow are those stated.

## technical
The series' gravitational action, the MacDowell-Mansouri square, contains the Euler density with coefficient $-3/(4\Lambda)$. If horizon entropy were its Wald (Jacobson-Myers) functional, the stored result shows the extra term is a constant on closed horizons, invisible to every Clausius relation between closed cuts; it left open whether it matters on the small open patches of a local Rindler horizon, which is where the local-horizon premise (C$_{\mathrm{loc}}$) and Jacobson's argument live. It does. On a local edge the Jacobson-Myers density equals $-3/(4\Lambda)$ times the Cartan curvature of the edge plane, so it depends on the curvature (the field strength) at the point and vanishes identically for the de Sitter field.

The cleanest test is the store's own vacuum solution, Schwarzschild-de Sitter. Along a radial null generator, ingoing or outgoing, the curvature components that focus or shear the generators vanish identically, so for every admissible cut the area stays constant and, in vacuum, no energy crosses. Yet the density changes, as $-3M/(2\Lambda r^{3})$: the Wald entropy grows along outgoing and falls along ingoing local horizons with nothing crossing them. That violates the curvature-independence clause (Loc) of the premise (the change is not proportional to the area change, which is zero), violates the Clausius relation at first order, and cannot be absorbed into an entropy production because it has both signs. The change is the value at the point of a divergence on the cut, so it cancels over any closed cut, as the stored result requires; what fails is the Clausius relation on each open patch, which is how Jacobson's argument and the store's hypotheses impose it, with the entropy of a patch the integral of its density (a functional of the cut). The general first-order rate on any patch is filed alongside, synthesis.euler-entropy-first-order-rate-on-local-patches; this result supplies the exact radial value and the all-orders, two-signed change. The result does not depend on the choice of cut, on the normalisation of the generators, or on the usual ambiguity of the Wald entropy away from stationary horizons, since the terms that ambiguity adds vanish where the expansion and shear vanish.

So the Euler term must be excluded from the horizon entropy functional (not from the action): with (C$_{\mathrm{loc}}$) adopted, the entropy of local horizons is the area term. With the stored result on closed horizons, the de Sitter entropy is $\pi N^{2}$, not zero, and black-hole nucleation keeps its Einstein-Hilbert exponent. Whether the entropy is, in addition, exactly the boundary-mode count is not decided here.

## lay
The series writes gravity's action as the square of a curvature built from its frozen point. That action contains an extra term which does not change Einstein's equations but, in the standard Wald recipe, does change the entropy assigned to horizons. Earlier work showed the change is a fixed constant for closed horizons such as a black hole's, so it cannot be seen in the usual heat-balance arguments. This result looks at the small pieces of horizon that Jacobson's derivation of Einstein's equations uses. Around a black hole in a universe with a cosmological constant, a light front moving straight inward or outward keeps its area and has nothing crossing it, yet the Wald entropy of the extra term changes: it goes up on the way out and down on the way in. A horizon whose entropy changes with no heat crossing it, and that can even lose entropy, breaks the heat balance and the assumption that entropy grows with area at the same rate everywhere. So if the local-horizon assumption is kept, the extra term has to be left out of the entropy, while it can stay in the action.

## one-liner
Under the Wald (Jacobson-Myers) functional of the series' action the density on a local edge is $-3/(4\Lambda)$ times the Cartan curvature of the edge plane, and along radial generators of every Schwarzschild-de Sitter hole, where area and flux are constant, it changes as $-3M/(2\Lambda r^{3})$, up outward and down inward; so, with entropy a functional of the cut, the Euler term violates (Loc) and the Clausius relation on open patches (the change is a divergence on the cut and cancels on closed cuts) and, with (C$_{\mathrm{loc}}$) adopted, must be left out of horizon entropy.
