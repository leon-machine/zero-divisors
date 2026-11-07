---
id: synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons
kind: claim
version: 3
title: 'MacDowell-Mansouri as the reduction of five-dimensional Chern-Simons'
status: proved
region: synthesis
subject: einstein
tags: [tractors, gauge-fields, curvature-and-field-equations, forcing-and-uniqueness]
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
- name: Claude Opus 5.5
  role: GA rewrite (outside_ga declared for the base forms; Weyl sign in (iii))
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG reading of the base forms as multivector fields of a flat five-dimensional background; declaration narrowed'
  version: 3
  source: maintainer pass 2026-11-07 (consistency, GTG proofs)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - dark-energy.frozen-point-makes-stelle-west-vector@5
  - dark-energy.imported-macdowell-mansouri-theorem-stelle-west@3
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection@1
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@2
  - rule2.rule-2-kaluza-klein-algebra@6
  - synthesis.imported-five-dimensional-chern-simons-gravity@1
  - synthesis.imported-chern-weil-and-chern-simons-forms@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_chern_simons_five_form_reduces_to_the_frozen_point_functional
- kind: check
  ref: check.py::check_reduced_lovelock_terms_are_a_perfect_square_only_on_the_chern_simons_family
- kind: check
  ref: check.py::check_five_dimensional_equations_on_the_ansatz_add_the_radion_equation
- kind: check
  ref: check.py::check_signature_of_the_five_dimensional_parent
- kind: check
  ref: check.py::check_gtg_reduction_with_base_forms_as_background_multivectors
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part
  - rule2.imported-five-dimensional-chern-simons-shift
  - rule2.rule-2-kaluza-klein-algebra
extraction:
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Proof given a geometric-algebra language paragraph: the Cl(2,4) values were already multivectors; the forms on the five-dimensional base are now read as multivector fields of a flat five-dimensional background (the d-dimensional clause of the GTG definition), dx^mu, dy the background vectors, the exterior product of base parts their outer product, d = grad ^, exact forms grad ^-derivatives; the orientation paragraph says so. The computation (multiplicities 1, 3, 5, the reduction, the equations) is unchanged and already algebraic. Original proof kept as orig-proof-main.tex. New exact check check_gtg_reduction_with_base_forms_as_background_multivectors (the reduction (i) recomputed with the outer product of Cl(1,4) for the base parts at three (Lambda, lambda, seed) cases; same five-form, equal to (3 lambda/Q(V)) eps(I, V, F, F) ^ dy). outside_ga kept and narrowed: the transgression and variation formulas of five-dimensional Chern-Simons forms are used as the imported Facts state them (theorems about differential forms, not proved here in GA), read through the multivector dictionary; no other stand-in remains. A GA proof of those formulas would restate the imported Chern-Weil theory, not this result.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Not rewritten; outside_ga declared (kind other). The Clifford parts are already geometric algebra; the differential forms that remain are the base forms of a Chern-Simons five-form on a five-dimensional base, whose transgression and variation formulas are imported theorems about differential forms (synthesis.imported-five-dimensional-chern-simons-gravity, synthesis.imported-chern-weil-and-chern-simons-forms). Weyl sign (reader R03): formal (iii) said that F is the Weyl curvature and displayed W(B) = m(B + 3 sigma B sigma), m = -M/(2r^3), which is minus the store-sign Weyl map; it now says F = -calW (the tractor theorem, clause (iv)) and F(B) = W(B) = m(B + 3 sigma B sigma), calW(sigma) = +2M/r^3 sigma; the value 48 m^2 is unchanged. Version 2 -> 3 for that formal change.'
  open_problem: op.derive-gravitational-action
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 1 -> 2: five-dimensional Chern-Simons gravity (Chamseddine) and the reduction of Lovelock densities along a line, cited from memory, now point to the imported Fact approved by Leon, and the transgression and variation formulas to the Chern-Weil and Chern-Simons Fact, both added to uses since the reduction rests on them; the mentions of the Weyl-square and Stelle-West results filed alongside are claimrefs (text only), and the remark that the Weyl-square identity is stated in the opposite orientation is corrected (that result now uses the store orientation, with the same sign as here). Statement unchanged.'
  note: >-
    Bears on import (b) of the open problem (the MacDowell-Mansouri form) and leaves (a) and (c) imported.
    The five-dimensional Chern-Simons gravity of the anti-de Sitter group (Chamseddine 1989 and 1990,
    \claimref{synthesis.imported-five-dimensional-chern-simons-gravity}) is a functional of the Cl(2,4) connection alone, with no reduction datum: the
    Chern-Simons transgression of the cubic Pfaffian invariant. Reduced along the frozen point it is
    exactly the frozen-point MacDowell-Mansouri density, and among reduced Lovelock densities the perfect
    square is exactly the Chern-Simons family, so the Gauss-Bonnet, Einstein-Cartan and volume ratio is the
    five-dimensional gauge invariance seen in four dimensions. The local action is relocated to five
    dimensions, not derived. Negative parts: the reduction is not a consistent truncation unless the scale
    of the reduced direction is held fixed (its equation is the MacDowell-Mansouri density itself, nonzero
    at Schwarzschild-de Sitter); the de Sitter case needs a parent of signature (2,3) inside Cl(2,4), or
    the other Rule 2 repair Cl(1,5); and the Chern-Simons level does not fix Newton's constant (argued: the
    four-dimensional coefficient is the level times the length of the reduced direction in units of the
    de Sitter radius, a free ratio, so the relation re-expresses N and predicts nothing). The reduction of Lovelock densities along a line is standard (\claimref{synthesis.imported-five-dimensional-chern-simons-gravity}, note); the new content is the frozen point as the reduced direction and the Stelle-West vector as the parent's vector. Transport-convenient: the series supplies the algebra, the frozen point
    as the reduced direction and the Stelle-West slot; the five-dimensional base and action are imported.
    The Euler term comes with the square, so the reduction does not help with its exclusion from horizon
    entropy.
outside_ga:
  kind: other
  why: 'The transgression formula CS5(A) - CS5(omega) = 3 int_0^1 P(E; F_t, F_t) dt and the variation formula delta CS5 = 3 P(delta A; F, F), modulo exact forms, are used as Facts synthesis.imported-five-dimensional-chern-simons-gravity and synthesis.imported-chern-weil-and-chern-simons-forms state them, as theorems about differential forms; the proof reads them with the base forms as multivector fields of a flat five-dimensional background (d = grad ^, exterior product = outer product) and is otherwise in geometric algebra, so the imported formulas'' own language is the only stand-in left.'
---

## formal
Work in $\Cl(2,4)$ with $\nO$, $\nInf$ as in Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, $\Lambda \neq 0$, frozen point $I = \nInf + \tfrac{\Lambda}{6}\nO$ ($Q(I) = \Lambda/3$), canonical tractor $X = \nO$ and Stelle-West vector $V = X - \tfrac{3}{\Lambda}I$ ($Q(V) = -3/\Lambda$, $\ip{I}{V} = 0$), as in Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}; $W = \{I, V\}^{\perp}$, of signature $(1,3)$. Orientation as in the stored check of that theorem: generators $e_{0}$ ($+1$), $e_{1}, e_{2}, e_{3}$ ($-1$), $e_{4}$ ($+1$), $e_{5}$ ($-1$), $\nO = \tfrac12(e_{4} + e_{5})$, $\nInf = e_{4} - e_{5}$, $I_{6} = e_{0}e_{1}e_{2}e_{3}e_{4}e_{5}$; two-forms are combined by the exterior product of their form parts (a sum over ordered planes), so that $\epsilon(I, V, e\wedge e, e\wedge e) = 6$ times the volume form. Let $P(B_{1}, B_{2}, B_{3}) = \langle B_{1}B_{2}B_{3}\rangle_{6}\,I_{6}^{-1}$ be the Pfaffian (cubic invariant) of the bivectors, so that $\epsilon(I, V, F, G) = P(I\wedge V, F, G)$. On a five-dimensional base with coordinates $(x, y)$, let $\theta$ be a vector-valued one-form with values in $V^{\perp}$ (the frame), $E = \theta\wedge V/Q(V)$ (the translational part of the connection, in the normalisation $A = \Omega - \hb^{-1}\wedge V/\ell^{2}$ of Fact \claimref{dark-energy.imported-macdowell-mansouri-theorem-stelle-west}), $K = E\times E$, and $R$ the curvature of the Lorentz part. The five-dimensional Chern-Simons form of $P$, written through its transgression from the Lorentz connection (Facts \claimref{synthesis.imported-five-dimensional-chern-simons-gravity} and \claimref{synthesis.imported-chern-weil-and-chern-simons-forms}(b)), is, modulo exact forms,
\[
L_{5} = 3\int_{0}^{1} P\big(E;\, (R + t^{2}K)\wedge(R + t^{2}K)\big)\,dt = P\big(E;\, 3\,R\wedge R + 2\,R\wedge K + \tfrac35\,K\wedge K\big).
\]
\begin{enumerate}
\item[(i)] \emph{(Reduction; proved.)} On the ansatz $\theta = \theta_{4} + \lambda\,dy\,I$, with $\theta_{4}$ a frame of $W$ on the four-dimensional directions and $R$ valued in $\Lambda^{2}W$, $K_{4} = E_{4}\times E_{4} = \tfrac{\Lambda}{3}\,\theta_{4}\wedge\theta_{4}$ and
\[
L_{5} = \frac{3\lambda}{Q(V)}\,\epsilon(I, V, F, F)\wedge dy, \qquad F = R + \tfrac{\Lambda}{3}\,\theta_{4}\wedge\theta_{4},
\]
the frozen-point MacDowell-Mansouri density of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(iii). The torsion never enters $L_{5}$.
\item[(ii)] \emph{(The ratio is the Chern-Simons locus; proved.)} The three five-dimensional Lovelock densities $P(E; R\wedge R)$, $P(E; R\wedge K)$, $P(E; K\wedge K)$ reduce to $Q(V)^{-1}\lambda$ times $1$, $3$, $5$ times $\epsilon(I, V, R, R)$, $\epsilon(I, V, R, K_{4})$, $\epsilon(I, V, K_{4}, K_{4})$. Hence $a\,P(E; RR) + b\,P(E; RK) + c\,P(E; KK)$ with $a \neq 0$ reduces to a multiple of a square $\epsilon(I, V, R + sK_{4}, R + sK_{4})$ if and only if $9b^{2} = 20ac$, and then $s = 3b/(2a)$; the solutions with $s = 1$ are exactly the multiples of the Chern-Simons coefficients $(3, 2, \tfrac35)$.
\item[(iii)] \emph{(Five-dimensional equations; proved.)} The Chern-Simons equations $P(J; F_{5}, F_{5}) = 0$, $J$ a bivector, evaluated on the torsion-free ansatz: for $J$ in $\Lambda^{2}(V^{\perp})$ they vanish identically; for $J = u\wedge V$, $u \in W$, they are the frame equation of the four-dimensional functional (wedged with $dy$), which vanishes on every Einstein field with the matching $\Lambda$ (Theorem \claimref{synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part}); for $J = I\wedge V$ they are the additional four-form equation
\[
\epsilon(I, V, F, F) = \frac{Q(V)}{3}\,\frac{\partial L_{5}}{\partial\lambda} = 0,
\]
the equation of the scale $\lambda$ of the reduced direction. On an Einstein field with the matching $\Lambda$, $F$ is minus the Weyl map in the store's sign, $F = -\mathcal{W}$ (the Lorentz block of the tractor field strength, Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}(iv)); at a point of Schwarzschild-de Sitter, $F(B) = W(B) = m(B + 3\sigma B\sigma)$ with $\sigma = e_{1}e_{0}$ and $m = -M/(2r^{3})$ (so $\mathcal{W}(\sigma) = +\tfrac{2M}{r^{3}}\sigma$), its value is $48m^{2} = \tfrac14 C_{abcd}C^{abcd} = 12M^{2}/r^{6} \neq 0$ for either sign of $\Lambda$ (in this orientation; the general identity $\epsilon(I, V, F, F) = \tfrac14 C_{abcd}C^{abcd}$ times the volume form on the tractor field strength of a torsion-free field is Theorem \claimref{synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared}(iii), in the same orientation), while for a type N Weyl field (plane waves) it is $0$. So the frozen-point functional is the consistent reduction of the five-dimensional one only with $\lambda$ held fixed; with $\lambda$ varied the black holes are not solutions. The same scalar equation is the equation of a released Stelle-West norm in Theorem \claimref{synthesis.stelle-west-norm-is-no-local-output}(iv): in both the Lagrangian is of degree one in the scale.
\item[(iv)] \emph{(Signature of the parent; proved.)} The five-dimensional frame space $V^{\perp} = W \oplus \langle I\rangle$ has signature $(2,3)$ for $\Lambda > 0$ ($I$ timelike) and $(1,4)$ for $\Lambda < 0$. So within $\Cl(2,4)$ the de Sitter functional is the reduction of a parent on a $(2,3)$ base along a timelike direction, and the anti-de Sitter functional that of the ordinary anti-de Sitter Chern-Simons gravity along a spacelike one. A Lorentzian parent with a spacelike reduced direction for $\Lambda > 0$ is the Chern-Simons gravity of $SO(1,5)$, in $\Cl(1,5)$, the second repair of Theorem \claimref{rule2.rule-2-kaluza-klein-algebra}(iv).
\item[(v)] \emph{(Coupling; argued.)} With the Chern-Simons coefficient $k$ (a level, quantised for a compact form of the group; the quantisation for $SU(2,2)$ is not standard) the four-dimensional coefficient is $k$ times the integral of $\lambda\,dy$ times a fixed number, so $N^{2} = 3/(G\Lambda)$ is $k$ times the length of the reduced direction in units of the de Sitter radius, times a fixed number: the level does not fix Newton's constant, and the relation is a re-expression of $N$, not a prediction.
\end{enumerate}

## technical
The open problem asks whether the frozen-point MacDowell-Mansouri functional $Q(I)^{-1}\int\epsilon(I, V, F, F)$ can be obtained from the series' objects. This result tests one outside route: five-dimensional Chern-Simons gravity, whose action is a functional of the $\Cl(2,4)$ connection alone (the Chern-Simons form of the cubic Pfaffian invariant, Chamseddine's, an imported Fact), so in five dimensions no reduction datum is needed.

Written through its transgression from the Lorentz connection, the five-dimensional form is $P(E; 3RR + 2RK + \tfrac35 KK)$, with $E$ the frame part and $K = \tfrac{\Lambda}{3}\theta\wedge\theta$. Taking the frozen point as the fifth frame direction, $\theta = \theta_{4} + \lambda\,dy\,I$, it reduces exactly to $(3\lambda/Q(V))\,\epsilon(I, V, F, F)\wedge dy$: the three Lovelock terms come with multiplicities $1$, $3$, $5$, and the Chern-Simons coefficients are exactly the ones that make the result a perfect square. Any other five-dimensional Lovelock combination misses the MacDowell-Mansouri ratio. The multiplicities and the reduction of five-dimensional Chern-Simons gravity to a four-dimensional curvature-squared form are the standard reduction of Lovelock densities along a line (literature, recorded with the imported Fact); what is new here is that the reduced direction is the frozen point and the parent's vector is the Stelle-West vector $V = X - (3/\Lambda)I$, so the reduction lands exactly on the series' frozen-point functional.

Three limits. The five-dimensional equations on the ansatz contain, besides the four-dimensional frame equation, the equation of the scale $\lambda$, which is the MacDowell-Mansouri density itself, the same scalar equation as for a released Stelle-West norm (Theorem \claimref{synthesis.stelle-west-norm-is-no-local-output}); its value on a torsion-free field is a quarter of the Weyl square (Theorem \claimref{synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared}), so it is nonzero at every point of Schwarzschild-de Sitter ($12M^{2}/r^{6}$ in the stored orientation), and the reduction is consistent only with that scale held fixed. For $\Lambda > 0$ the frozen point is timelike and the parent base has signature $(2,3)$; a Lorentzian parent needs $\Cl(1,5)$. The level does not fix the coupling (argued); the relation between level, length and $N$ is a re-expression, not a prediction. So the action is relocated, not derived; the form is explained by a gauge symmetry one dimension up; the matter coupling is untouched; and the Euler term comes with the square.

## lay
The series borrows a formula for the action of gravity. This result tries a borrowed route from outside: in five dimensions there is a gravitational action built from the series' six-dimensional connection alone, needing no special direction. Squashing the fifth dimension along the series' frozen point gives back exactly the borrowed four-dimensional formula, and the five-dimensional symmetry explains its particular mix of terms. But the squashing only works if the size of the fifth dimension is held fixed; if it is allowed to vary, black holes stop being solutions. For a positive cosmological constant the parent space would need two time directions, and the route does not fix the strength of gravity.

## one-liner
The five-dimensional Chern-Simons form of the $\Cl(2,4)$ Pfaffian, $P(E; 3RR + 2RK + \tfrac35 KK)$, reduced along the frozen point ($\theta = \theta_{4} + \lambda\,dy\,I$) is exactly $(3\lambda/Q(V))\,\epsilon(I, V, F, F)\wedge dy$, and the $1:2:1$ ratio is exactly the Chern-Simons locus ($9b^{2} = 20ac$) among reduced Lovelock densities; but the reduced scale's equation is $\epsilon(I, V, F, F) = 0$, equal to $12M^{2}/r^{6}$ at Schwarzschild-de Sitter, so the reduction holds only with that scale fixed, the de Sitter parent has signature $(2,3)$ in $\Cl(2,4)$ (Lorentzian only in $\Cl(1,5)$), and the level does not fix Newton's constant (argued; a re-expression of $N$). The action is relocated, not derived; transport-convenient.
