---
id: synthesis.de-sitter-field-fixes-the-observer-tube-point
kind: claim
version: 4
title: 'The de Sitter field fixes the observer''s tube point'
status: proved
region: synthesis
subject: one-relation
tags: [conformal-spinors, conformal-model, frozen-point, horizons, modular-theory, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, every imaginary unit resolved as a geometric-algebra pseudoscalar (unit principle)
  version: 3
  source: maintainer pass 2026-11-07 (resolve units)
- name: Claude Opus 5.5
  role: 'consistency pass, the normalisation of K against the cited theorem stated in the formal level'
  version: 4
  source: maintainer pass 2026-11-07 (consistency)
review: draft
derivations:
- name: main
  uses:
  - synthesis.wick-rotated-boost-selects-observer-tube-point@2
  - synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale@2
  - synthesis.de-sitter-horizon-translation-is-conformal-null-rotation@4
  - synthesis.de-sitter-static-boost-frozen-point@6
  - synthesis.imported-gtg-dictionary@1
  - one-relation.spacetime-manifold-vacuum-lines@6
  - dark-energy.frozen-point-makes-stelle-west-vector@5
  - synthesis.positive-structure-is-twistor-form-at-imaginary-time@5
  assumes:
  - synthesis.tube-point-clause-invariant-under-boost-commuting-symmetries@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_field_symmetries_commuting_with_the_boost
- kind: check
  ref: check.py::check_fixed_tube_point_is_the_frozen_point
- kind: check
  ref: check.py::check_boost_norm_is_maximal_and_equal_to_inverse_surface_gravity_at_the_frozen_point
- kind: check
  ref: check.py::check_frozen_point_orbit_is_the_free_fall_orbit
- kind: check
  ref: check.py::check_frozen_orbit_is_the_stored_static_observer
- kind: check
  ref: check.py::check_bifurcation_plane_is_a_round_sphere_with_equator_at_the_frozen_scale
- kind: check
  ref: check.py::check_no_fixed_tube_point_for_nonpositive_lambda
- kind: check
  ref: check.py::check_stelle_west_vector_at_the_tube_point
- kind: check
  ref: check.py::check_scale_of_the_null_pair_moves_rho_and_lambda_together
- kind: check
  ref: check.py::check_two_horizon_field_separates_the_candidates
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.wick-rotated-boost-selects-observer-tube-point
  - synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. The formal level says it uses the labels of synthesis.wick-rotated-boost-selects-observer-tube-point, whose K is (1/2) e_1 e_2, and then sets K = e_1 e_2; the proof already says ''twice the stored generator'', and clause (iii) needs the unit-rapidity one (Q(K . x) = rho^2 for K = e_1 e_2, rho^2/4 for (1/2) e_1 e_2, checked exactly with lib/GA.py); the formal level now says so; mathematics unchanged.'
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Unit principle U3: the tube points m = x_perp + i rho u, V(m) = i ell u, the tube points i rho e_1 and i e_1, the coefficient c = alpha + i beta and the closing remark on the unit of m = x + iy are written with I_7 = I_6 e, the central pseudoscalar of Cl(3,4) = Cl(2,4)_C, which commutes with every vector (std-algebra.complexification-is-the-odd-extension, cited as a mention); the remark keeps I_7 distinct from the conformal spinors'' I_6, which is +-I_7 on the two chirality halves. No bare i remains, so the outside_ga declaration (complex-analysis, for i only) is removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the i of the tube points and of the complexified Stelle-West vector belongs to the complexification of the vectors (forward tube), whose unit must commute with them; declared (version and levels unchanged).'
  open_problem: op.which-capacity
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Leon adopted the selection rule of the reading as a costed clause on 2026-10-31; it is registered as synthesis.tube-point-clause-invariant-under-boost-commuting-symmetries and this result now assumes it (assumes edge added; the reading and the technical level cite it). The pin of synthesis.de-sitter-horizon-translation-is-conformal-null-rotation is moved from @3 to @4 (its version 4 changes no content; the field definition hb = sigma is unchanged). Proof (viii) now cites synthesis.positive-structure-is-twistor-form-at-imaginary-time, a declared premise it used without naming. Statement unchanged. Version 1 -> 2.'
  note: >-
    Attack line 1 of the open problem (decide between rho^2 = 12/Lambda and rho = 1/kappa, or show that
    the bifurcation surface's round metric fixes rho), in the one gravitational field where the stored
    tube-point machinery applies verbatim: the de Sitter field in its pure-dilation gauge hb = sigma,
    whose symmetries are the bivectors commuting with the frozen point I_Lambda and which contains the
    chart boost K. Proved: the symmetries commuting with K are K plus a transverse so(3) (so(1,2) for
    Lambda < 0, the transverse Euclidean algebra for Lambda = 0); the compatible tube points it fixes are
    exactly the boost orbit with foot 0 and rho^2 = 12/Lambda (Re X(m) = (rho^2/2) I_Lambda there), which
    the store had argued only; the physical norm N = rho/sigma of the boost generator at the observer
    obeys 1 - H N = (1 - H rho/2)^2/sigma, so N <= 1/kappa with equality exactly on that orbit (a double
    root), and N = 4/(5H) at chart distance 1/H; the GTG acceleration of the boost orbit is
    ((1 - Lambda rho^2/12)/rho) w, zero exactly there; the rotor 1 + e2 W carries K to the stored static
    boost and the stored static observer onto that orbit; the bifurcation plane is round of curvature
    Lambda/3 with its equator at chart radius rho_Lambda; for Lambda <= 0 no tube point is fixed and N is
    monotone. So the candidates in the problem's statement are one tube point in the de Sitter field: the
    stored "factor 2 in chart length" remains in chart length and is the local scale sigma = 2 at that observer, and rho = 1/kappa read
    in chart length singles out no orbit. Argued only (reading): that the premise fixing rho is the field
    itself, through covariance of the state's tube point under the field's symmetries commuting with the
    boost (Allen's de Sitter-invariant Hadamard state of a massive scalar, imported in the store; the series' modes are CAR, outside its hypotheses); the Tolman reading (the selected
    observer is the coldest and the free-fall one); the Schwarzschild field is not covered (not a pure
    dilation; the analogue of the norm rule selects the asymptotic observer). Transport-convenient: the
    content is standard de Sitter static-patch geometry (Gibbons-Hawking); what is new to the store is
    its form on the compatible tube points of the twistor-form polarisation and the identification of the
    three candidates. Tolman's relation is cited from memory and used only in the reading.
---

## formal
Use the labels of Theorem \claimref{synthesis.wick-rotated-boost-selects-observer-tube-point}: $\Cl(2,4)$ with $e_{1}$ (square $+1$, time), $e_{2}, e_{3}, e_{4}$ (square $-1$), $e_{+}$ ($+1$), $e_{-}$ ($-1$), $\nO = \tfrac12(e_{+} + e_{-})$, $\ninf = e_{+} - e_{-}$, $X(x) = \nO + x - \tfrac12 Q(x)\ninf$; $K = e_{1}e_{2}$ (twice that theorem's generator, normalised to unit rapidity), the boost of the $(e_{1}, e_{2})$ plane with bifurcation plane $\operatorname{span}(e_{3}, e_{4})$; the compatible tube points $m = x_{\perp} + I_{7}\rho u$ (complex unit $I_{7} = I_{6}e$, the central pseudoscalar of $\Cl(2,4)_{\C} = \Cl(3,4)$, which commutes with every vector; Theorem \claimref{std-algebra.complexification-is-the-odd-extension}), $u = \cosh\eta\,e_{1} + \sinh\eta\,e_{2}$, $\rho > 0$, with observers $x(m) = x_{\perp} + \rho(\sinh\eta\,e_{1} + \cosh\eta\,e_{2})$. For real $\Lambda$ let $I_{\Lambda} = \ninf + \tfrac{\Lambda}{6}\nO$, $W = \ninf - \tfrac{\Lambda}{6}\nO$, $\sigma(x) = \ip{X(x)}{I_{\Lambda}} = 1 - \tfrac{\Lambda}{12}Q(x)$, and for $\Lambda > 0$ let $(\hb, \Omega)$, $\hb(a) = \sigma a$, $\Omega(a) = -(a \wedge \nabla\sigma)/\sigma$ on $\sigma > 0$, be the de Sitter gravitational field of Theorem \claimref{synthesis.de-sitter-horizon-translation-is-conformal-null-rotation}, $H = (\Lambda/3)^{1/2}$, $\kappa_{\Lambda} = H$ its surface gravity (Theorem \claimref{synthesis.de-sitter-static-boost-frozen-point}), $\ell = 1/H$ and $\rho_{\Lambda} = (12/\Lambda)^{1/2} = 2\ell$.
\begin{enumerate}
\item[(i)] \emph{(Symmetries commuting with the boost.)} The bivectors commuting with $I_{\Lambda}$ and $K$ are spanned by $K$, $e_{3}e_{4}$, $e_{3}W$, $e_{4}W$, with $Q(W) = -\Lambda/3$ and $[e_{3}W, e_{4}W] = -2Q(W)\,e_{3}e_{4}$: the three transverse ones span $\so(3)$ for $\Lambda > 0$, $\so(1,2)$ for $\Lambda < 0$, and for $\Lambda = 0$ ($W$ replaced by $\ninf$) the rotation and translations of the bifurcation plane.
\item[(ii)] \emph{(The fixed tube points.)} For $\Lambda > 0$ a compatible tube point is fixed by the three transverse symmetries if and only if $x_{\perp} = 0$ and $\rho = \rho_{\Lambda}$; then $\operatorname{Re}X(m) = \tfrac{\rho_{\Lambda}^{2}}{2}I_{\Lambda}$. These points form one orbit of the boost, the tube points of the observers on the hyperbola $Q(x) = -12/\Lambda$ of the right wedge.
\item[(iii)] \emph{(The boost generator's norm.)} At $x(m)$ with $x_{\perp} = 0$ the velocity $K \cdot x$ has $Q = \rho^{2}$ and physical norm $N(\rho) = \rho/\sigma(x(m)) = \rho/(1 + \tfrac{\Lambda}{12}\rho^{2})$. For $\Lambda > 0$, $1 - \kappa_{\Lambda}N(\rho) = (1 - H\rho/2)^{2}/\sigma$, so $N \le 1/\kappa_{\Lambda}$ with equality if and only if $\rho = \rho_{\Lambda}$, where $\sigma = 2$; at $\rho = 1/\kappa_{\Lambda}$, $N = \tfrac45\ell$.
\item[(iv)] \emph{(Free fall.)} The boost orbit through $x(m)$ ($x_{\perp} = 0$), with unit physical velocity $v$ and $x' = \hb(v)$, has $dv/d\tau + \Omega(x') \cdot v = \tfrac{1}{\rho}(1 - \tfrac{\Lambda}{12}\rho^{2})(\sinh\eta\,e_{1} + \cosh\eta\,e_{2})$, so it is a free-fall worldline (Fact \claimref{synthesis.imported-gtg-dictionary}(iii)) if and only if $\Lambda\rho^{2} = 12$. At $\Lambda = 3$ the rotor $1 + e_{2}W$, a symmetry of the field, carries $K$ to the static boost $e_{1} \wedge W$ of Theorem \claimref{synthesis.de-sitter-static-boost-frozen-point} and its observer at the origin onto this orbit.
\item[(v)] \emph{(The bifurcation surface.)} The physical metric $\sigma^{-2}(dy^{2} + dz^{2})$ induced on $\operatorname{span}(e_{3}, e_{4})$ has Gauss curvature $\Lambda/3$; for $\Lambda > 0$ it is the round sphere of radius $\ell$ (with its point at infinity), with rotation algebra the $\so(3)$ of (i), and the circle of chart radius $r$ has physical radius $N(r)$, so its equator lies at chart radius $\rho_{\Lambda}$.
\item[(vi)] \emph{(No field, or $\Lambda < 0$.)} For $\Lambda \le 0$ no compatible tube point is fixed by the transverse symmetries, $N$ is strictly increasing on $\sigma > 0$, and the acceleration of (iv) never vanishes.
\item[(vii)] \emph{(The Stelle-West vector.)} For $\Lambda \neq 0$ and every compatible $m$, $\sigma(m) = \ip{X(m)}{I_{\Lambda}} = 1 + \tfrac{\Lambda}{12}(|x_{\perp}|^{2} + \rho^{2})$ is real, and the complexified Stelle-West vector $V(m) = X(m)/\sigma(m) - \tfrac{3}{\Lambda}I_{\Lambda}$ of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector} has $\ip{V}{I_{\Lambda}} = 0$, $Q(V) = -3/\Lambda$, $\operatorname{Im}V = \operatorname{Im}X(m)/\sigma(m)$ orthogonal to $\operatorname{Re}V$, and $Q(\operatorname{Im}V) = (\rho/\sigma(m))^{2}$. For $\Lambda > 0$, $\operatorname{Re}V \in \operatorname{span}(e_{3}, e_{4}, W)$ has $Q(\operatorname{Re}V) \le 0$, so $\rho/\sigma(m) \le \ell$ at every compatible tube point, with equality if and only if $\operatorname{Re}V = 0$, if and only if $m$ is a fixed point of (ii); there $V(m) = I_{7}\ell u$. The conjugate point $\bar m$ is fixed by the same symmetries.
\item[(viii)] \emph{(The unit.)} The rescaling $\nO \mapsto s\nO$, $\ninf \mapsto \ninf/s$ of the null pair (the boost $1 + te_{+}e_{-}$ of the ascent plane) carries $I_{\Lambda}$ to $s^{-1}I_{s^{2}\Lambda}$ and the tube point $I_{7}\rho e_{1}$ to that of $I_{7}(\rho/s)e_{1}$, so $\rho^{2}\Lambda$ is unit-independent and fixed points go to fixed points; in the frame where $I_{\Lambda}$ is a multiple of $e_{+}$ ($\Lambda = 12$) the fixed tube point is $I_{7}e_{1}$, whose positive structure is the stored $h = h_{I_{7}e_{1}}$ (Theorem \claimref{synthesis.positive-structure-is-twistor-form-at-imaginary-time}).
\end{enumerate}
Consequently, in the de Sitter field the frozen-point candidate $\rho^{2} = 12/\Lambda$ (ii), the surface-gravity candidate read as unit physical norm of the boost generator normalised by $\kappa_{\Lambda}$ (iii), and the round metric of the bifurcation surface (v) select the same tube point, the free-fall observer's (iv), the one at which the Stelle-West vector is purely imaginary (vii); the factor $2$ between $\rho_{\Lambda}$ and $1/\kappa_{\Lambda}$ is the local scale $\sigma = 2$ there, and $\rho = 1/\kappa_{\Lambda}$ read as a chart length is selected by none of them. For $\Lambda \le 0$ none of them fixes the scale. The coincidence is one of a field with one horizon: for the Schwarzschild-de Sitter field with lapse $f(r) = 1 - 2M/r - \tfrac{\Lambda}{3}r^{2}$, one static region has two bifurcate horizons with different surface gravities ($\kappa_{b}/\kappa_{c} = \tfrac85$ at horizon radii $(1, 2)$, $\Lambda = \tfrac37$, $M = \tfrac37$), so the surface-gravity candidate depends on the horizon and the candidates separate there; this field is not a pure dilation and is not otherwise treated here.

## technical
The tube point that a boost-KMS state reads was known up to one scale, the distance $\rho$ of the observer from the bifurcation plane, with two candidates on record: the frozen point, $\rho^{2} = 12/\Lambda$, and the surface-gravity normalisation $\rho = 1/\kappa$, which disagreed by a factor $2$ in chart length. This result computes all of them in the de Sitter gravitational field, a pure dilation of the flat background in which the boost of a plane through the scale's centre is a symmetry. The field's symmetries that commute with the boost are the boost and a rotation algebra of the bifurcation plane; on the half space of compatible tube points they fix exactly the points over the centre at $\rho^{2} = 12/\Lambda$, where the real part of the tube point's null vector is $6/\Lambda$ times the frozen point and the complexified Stelle-West vector, normalised by the scale at the tube point, is purely imaginary. On the observer of that tube point the boost generator has its largest physical norm, exactly $1/\kappa$, and the observer is in free fall; the bifurcation plane is a round sphere whose equator is there. So, with $1/\kappa$ read as the physical norm of the boost generator, the two candidates are one point; in chart length the selected scale is $2/\kappa$, and the factor $2$ is the local scale factor $\sigma = 2$ of the field at that observer. Read as a chart length, $\rho = 1/\kappa$ picks no distinguished observer. The coincidence belongs to a field with one horizon: in the Schwarzschild-de Sitter field the two horizons of one static region have different surface gravities, and the candidates separate. With no gravitational field, or a negative $\Lambda$, nothing fixes a tube point and the scale stays free, as dilation symmetry requires. Which principle makes the state's tube point respect the field's symmetries is argued, not proved: the de Sitter-invariant Hadamard state of a massive scalar is unique (Allen's theorem), and a covariant rule must then return the fixed point; the series' boundary modes are fermionic (CAR), outside that theorem's hypotheses. That rule is adopted as a costed clause (\claimref{synthesis.tube-point-clause-invariant-under-boost-commuting-symmetries}), which carries that hypothesis gap and decides fields with one horizon only.

## lay
A state of the quantum vacuum, read near a horizon, has to pick a reference point off the real world, an imaginary-time partner of one particular observer. Earlier results showed that this choice is fixed except for one number, how far the observer stands from the horizon's edge, and two proposals for that number disagreed by a factor of two. In a universe with a positive cosmological constant both proposals, and a third one based on the horizon's own sphere, turn out to pick the same observer: the one who falls freely and sees the coldest horizon. The factor of two remains between distances measured on the flat background, and it is exactly the stretching of lengths by the gravitational field at that observer. With two horizons, as around a black hole in such a universe, the proposals part again. Without a cosmological constant nothing picks the distance. That a state's reference point is the one these symmetries pick is an adopted rule, assumed rather than derived.

## one-liner
In the de Sitter gravitational field $\hb = \sigma$ the field's symmetries commuting with a wedge's boost fix exactly the compatible tube points over the scale's centre at $\rho^{2} = 12/\Lambda$, where the boost generator's physical norm $\rho/\sigma$ is maximal and equal to $1/\kappa$, the observer is in free fall, the bifurcation sphere has its equator and the complexified Stelle-West vector $X(m)/\sigma(m) - \tfrac{3}{\Lambda}I_{\Lambda}$ is purely imaginary, $I_{7}\ell u$; so the frozen-point and surface-gravity candidates for the tube point's scale are one tube point when $\rho = 1/\kappa$ is read as the physical norm of the boost generator, while in chart length $\rho_{\Lambda} = 2/\kappa$, the factor $2$ being the local scale $\sigma = 2$; the coincidence holds for this one-horizon field (in Schwarzschild-de Sitter the candidates separate), and for $\Lambda \le 0$ no tube point is fixed; taking the fixed point as the state's tube point is the adopted costed clause, assumed rather than derived.
