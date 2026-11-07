---
id: synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared
kind: claim
version: 3
title: 'On transport the frozen-point integrand is a quarter of the Weyl square'
status: proved
region: synthesis
subject: einstein
tags: [tractors, gauge-fields, curvature-and-field-equations, forcing-and-uniqueness, conformal-model]
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
  role: 'GA rewrite (Weyl square as a scalar of the Weyl map)'
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection@1
  - dark-energy.frozen-point-makes-stelle-west-vector@5
  - synthesis.imported-gtg-dictionary@1
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@2
  - synthesis.imported-miskovic-olea-identity@3
  - synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale@2
  - synthesis.promoted-norm-weyl-clock-flat-weight@6
  - synthesis.imported-chern-weil-and-chern-simons-forms@1
  - synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_tractor_field_strength_of_torsion_free_field_annihilates_x
- kind: check
  ref: check.py::check_eps_contraction_is_independent_of_the_second_vector_on_the_locus
- kind: check
  ref: check.py::check_frozen_point_integrand_is_a_quarter_weyl_square
- kind: check
  ref: check.py::check_invariant_forms_on_the_locus_are_chern_and_weyl
- kind: check
  ref: check.py::check_frame_leg_pairings_vanish_on_the_locus
- kind: check
  ref: check.py::check_weyl_square_integral_is_not_topological
- kind: check
  ref: check.py::check_chern_form_is_the_chern_simons_derivative
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part
  - synthesis.imported-miskovic-olea-identity
  - synthesis.promoted-norm-weyl-clock-flat-weight
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The Weyl square in (iii) and the one-liner is written (1/2)<W(a ^ b) W(d_b ^ d_a)>_0 for the Weyl map W, which equals (1/4) W_{abcd} W^{abcd} (the dictionary''s Kretschmann identity applied to W; checked exactly in scratch on a random pair-symmetric operator on the bivectors of Cl(1,3), 212 = 212), the components kept as a labelled reading; (v), on the closed Riemannian S^2 x S^2, and the proof''s bivector-valued two-forms and component Weyl basis stay, declared outside_ga (other).'
  open_problem: op.derive-gravitational-action
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 1 -> 2: the literature cited from memory now points to the imported Facts approved by Leon (Chern-Weil and Chern-Simons forms; Bach and Kaku-Townsend-van Nieuwenhuizen), both added to uses because the exactness of the Chern form and the reading that the field equations on transport are the Bach equations rest on them; the mentions of the results filed alongside are now claimrefs (text only, no uses edges). Statement unchanged.'
  note: >-
    Adversarial result on the open problem's first attack (does transport fix the form eps(I, V, F, F) among
    the invariant four-forms). Evaluated on the tractor gauge field of an arbitrary torsion-free field (the
    series' own transport, whose field strength has Lorentz block minus the Weyl part, a Cotton block along n0
    and no torsion block, so F.X = 0), the six-vector contraction eps(Y, X, F, F) is independent of Y beyond
    X.Y, so the frozen-point integrand eps(I, V, F, F) = eps(I, X, F, F) equals (X.I) eps_X(F, F) for every
    tractor I and every Lambda, and eps_X(F, F) is a quarter of the Weyl square (store orientation; exact:
    bilinear identity on a basis of the Weyl space). The frozen-point functional on transport is therefore
    3/(4 Lambda) times the Weyl (conformal gravity) action, which divided by 16 pi G is the stored instanton
    value (l^2/64 pi G) int |W|^2; on Einstein fields this agrees with the stored Miskovic-Olea identity and
    the Weyl-clock result, which hold on shell only. The identity itself is the Kaku-Townsend-van
    Nieuwenhuizen construction of conformal gravity as the epsilon-contracted square of the conformal-group
    curvature (1977, \claimref{synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form}(b)) written on the series' tractor gauge field; the series-specific
    content is the independence of the second vector on the locus, which makes the frozen point drop out.
    On the locus the stabiliser of X admits exactly two invariant symmetric bilinear forms, the Killing form
    (Chern form) and eps_X; eps_X is odd under the internal reflection with spacetime orientation fixed
    (parity-even in the usual combined sense, in which the Killing form, the Pontryagin density of the Weyl
    curvature there, is the odd one). The frame-leg pairings vanish on the locus, so no Einstein-Hilbert term
    exists there in this class. The Weyl square is not topological. Consequence: the Einstein equations of
    the stored functional come from varying it over connections preserving I, which is how import (b) of the
    open problem is worded (the field space, not the integrand); the no-inverse-frame hypothesis is what selects that field space
    (\claimref{synthesis.curvature-only-tractor-actions-are-macdowell-mansouri}). The statement that
    the tractor field alone gives only the Chern form is four-dimensional: in five dimensions the cubic
    Pfaffian has a non-topological Chern-Simons form
    (\claimref{synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons}).
    Transport-essential as a negative. Literature: Bach 1921 and Kaku, Townsend and van Nieuwenhuizen 1977 are
    \claimref{synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form}; Chern and Simons 1974 is
    \claimref{synthesis.imported-chern-weil-and-chern-simons-forms}.

outside_ga:
  kind: other
  why: 'The proof and its check work with the field strength as a bivector-valued two-form in frame components and with a basis of Weyl tensors built as component arrays (Kulkarni-Nomizu products), and clause (v) integrates the component Weyl square over the closed Riemannian S^2 x S^2, beyond one flat chart; the statement''s Weyl square is given as the scalar of the Weyl map.'
---

## formal
Work in $\Cl(2,4)$ with $\nO$, $\nInf$ as in Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection} ($\nO \cdot \nInf = 1$, both null) and canonical tractor $X = \nO$. Orientation and conventions are those of the stored check of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}: the unit pseudoscalar is $i_{6} = e_{0}e_{1}e_{2}e_{3}\,(\nInf \wedge \nO)$, and for vectors $a, b$ and bivectors $F, G$, $\epsilon(a, b, F, G)$ is the coefficient of $i_{6}$ in $a \wedge b \wedge F \wedge G$. A bivector-valued two-form is $F = \tfrac12 F_{ef}\,e^{e} \wedge e^{f}$, and $\epsilon(a, b, F, G)$ also denotes the four-form whose coefficient on $e^{0} \wedge e^{1} \wedge e^{2} \wedge e^{3}$ is the sum over ordered pairs of complementary coordinate planes (one quarter of the sum over the twenty-four orderings); in the opposite orientation every $\epsilon$ below changes sign. Let $(\hb, \Omega)$ be a torsion-free gravitational field on flat spacetime with Weyl part $\mathcal{W}$ of its curvature (Fact \claimref{synthesis.imported-gtg-dictionary}), $\Omega_{T}$ its tractor gauge field and $F$ the field strength of $\Omega_{T}$. Let $\Lambda \neq 0$, $I$ any tractor with $\ip{X}{I} \neq 0$ (the frozen point $\nInf + \tfrac{\Lambda}{6}\nO$ has $\ip{X}{I} = 1$) and $V = X - \tfrac{3}{\Lambda}I$, so that $I \wedge V = I \wedge X$ (Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(ii)).
\begin{enumerate}
\item[(i)] \emph{(The locus; proved.)} $F \cdot X = 0$: the field strength has Lorentz block $-\mathcal{W}$, an $\nO$ block (the Cotton term) and no $\nInf$ block, so its values lie in $\Lambda^{2}(X^{\perp})$. A torsion block (along $\nInf$) violates $F \cdot X = 0$.
\item[(ii)] \emph{(The frozen point drops out; proved.)} Fix $X$. For bivectors $F, G$ with $F \cdot X = G \cdot X = 0$, $\epsilon(Y, X, F, G)/\ip{X}{Y}$ does not depend on the vector $Y$ ($\ip{X}{Y} \neq 0$); call it $\epsilon_{X}(F, G)$. It is defined at fixed $X$, homogeneous of degree zero in $X$, and invariant under the stabiliser of $X$; it is not a polynomial in $(X, F)$ (for example $Y = I$ may be used). Off the locus it depends on $Y$. Hence on the tractor gauge field of every torsion-free field
\[
\epsilon(I, V, F, F) \;=\; \epsilon(I, X, F, F) \;=\; \ip{X}{I}\,\epsilon_{X}(F, F)
\]
for every such $I$ and every $\Lambda$.
\item[(iii)] \emph{(It is the Weyl square; proved.)} $\epsilon_{X}(F, F) = \tfrac12\langle\mathcal{W}(a \wedge b)\,\mathcal{W}(\partial_{b} \wedge \partial_{a})\rangle_{0}$ times the volume form, $\mathcal{W}$ the Weyl part of the curvature (in components $\tfrac14\,W_{abcd}W^{abcd}$ in an orthonormal frame of the derived metric); the Cotton block does not contribute. So for the frozen point ($Q(I) = \Lambda/3$, $\ip{X}{I} = 1$) the frozen-point functional evaluated on the series' transport is, in the stored normalisation up to the overall constant,
\[
\frac{1}{Q(I)}\int \epsilon(I, V, F, F) \;=\; \frac{3}{2\Lambda}\int \langle\mathcal{W}(a \wedge b)\,\mathcal{W}(\partial_{b} \wedge \partial_{a})\rangle_{0}\,\mathrm{vol} \;=\; \frac{3}{4\Lambda}\int W_{abcd}W^{abcd}\,\mathrm{vol},
\]
the Weyl (conformal gravity) action with coupling fixed by the prefactor, for every torsion-free field, Einstein or not.
\item[(iv)] \emph{(The quadratic densities on the locus; proved.)} The bilinear forms on $\Lambda^{2}(X^{\perp})$ invariant under the stabiliser of $X$ are: symmetric, a two-dimensional space spanned by the Killing form $K(F, G) = \langle FG\rangle_{0}$ and $\epsilon_{X}$; antisymmetric, none. Under the internal reflection in a spacetime vector, with the spacetime orientation fixed, $K$ is even and $\epsilon_{X}$ odd; under parity in the usual combined sense $\epsilon_{X}(F, F)$, the Weyl square, is even and $K(F \wedge F)$, on the locus the Pontryagin density of the Weyl curvature, is odd. In four dimensions $K(F \wedge F)$ is the Chern form, $d$ of the Chern-Simons form $\langle A \wedge dA\rangle_{0} + \tfrac13\langle A \wedge (A \times A)\rangle_{0}$ of any $\Cl(2,4)$ connection $A$. The pairings of $F$ with the frame legs $DX \wedge DX$ allowed by the same forms, $K(DX \wedge DX, F)$ and $\epsilon_{X}(DX \wedge DX, F)$, vanish on the locus.
\item[(v)] \emph{(Not topological; proved.)} On $S^{2} \times S^{2}$ with Riemannian product metric of constant curvatures $K_{1}$, $K_{2}$, $\int W_{abcd}W^{abcd}\,\mathrm{vol} = 16\pi^{2}\cdot\tfrac43(K_{1} + K_{2})^{2}/(K_{1}K_{2})$, which changes with $K_{2}/K_{1}$, while the Euler integral is $128\pi^{2}$ for every ratio. So the Euler-Lagrange derivative of the Weyl square is not identically zero, in either signature.
\end{enumerate}
\emph{Reading.} With the canonical tractor alone and the field strength on transport's locus, the densities quadratic in $F$ are $\alpha K + \beta\epsilon_{X}$, $K$ exact, and the stored frozen-point functional is the $\epsilon_{X}$ one: its field equations on transport are those of conformal gravity (the Bach equations, Fact \claimref{synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form}(a)), fourth order, solved by Einstein fields but not only by them. No density quadratic in $F$, with the frame legs $DX$ and the canonical tractor alone, has an Einstein-Hilbert term on transport's locus; the Einstein equations of Theorem \claimref{synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part} come from varying the functional over connections preserving $I$, not from the integrand. For a normal tractor connection, preserving $I$ is the Einstein condition (Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}(ii)); the hypothesis that admits only the $I$-preserving connections is the absence of an inverse frame, which excludes the Schouten slot of the normal connection (Theorem \claimref{synthesis.curvature-only-tractor-actions-are-macdowell-mansouri}). By (ii), restricted to a conformal class the integrand does not see the scale beyond $\ip{X}{I}$, which extends Theorem \claimref{synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale} to this integrand: the selection of the Einstein scale by the functional works through its field space. The statement that the tractor field alone gives only the Chern form is four-dimensional; in five dimensions the cubic Pfaffian of $\Cl(2,4)$ has a Chern-Simons form with field equations (Theorem \claimref{synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons}).

## technical
The open problem asks whether transport fixes the frozen-point MacDowell-Mansouri functional $Q(I)^{-1}\int\epsilon(I, V, F, F)$. This result evaluates that integrand on the series' own transport: the tractor gauge field of an arbitrary torsion-free field. Its field strength has Lorentz block minus the Weyl part, a Cotton block along $\nO$ and no torsion block, so it annihilates the canonical tractor $X = \nO$. On such bivectors the six-vector contraction $\epsilon(Y, X, F, G)$ depends on $Y$ only through $\ip{X}{Y}$, because $X \wedge F \wedge G$ lies in the one-dimensional top power of the five-dimensional space $X^{\perp}$; this defines $\epsilon_{X}$ at fixed $X$. Since $V$ differs from $X$ by a multiple of $I$, the frozen-point integrand is $\epsilon(I, X, F, F) = \ip{X}{I}\,\epsilon_{X}(F, F)$, and $\epsilon_{X}(F, F)$ is one quarter of the Weyl square in the store's orientation. So on transport the frozen-point functional is $\tfrac{3}{4\Lambda}$ times the conformal-gravity action, for every torsion-free field; the frozen point enters only through the prefactor. That the epsilon-contracted square of the conformal-group curvature is the Weyl action is the construction of conformal gravity by Kaku, Townsend and van Nieuwenhuizen (Fact \claimref{synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form}(b)), here on the series' tractor gauge field; the series-specific content is the independence of the second vector, which makes the frozen point drop out. On Einstein fields this is the on-shell identity of Mišković and Olea already in the store. On the same locus the stabiliser of $X$ admits exactly two invariant quadratic forms, the Killing form (the Chern form, exact in four dimensions) and $\epsilon_{X}$, which is odd under the internal reflection and even under parity in the usual sense; the frame-leg terms vanish there, so no Einstein-Hilbert term exists in this class. The Weyl square is not topological: its integral over a product of two spheres changes with the radius ratio while the Euler integral does not. Einstein's equations of the stored functional come from varying it over connections preserving $I$, which leave the normal tractor connections. All algebra is checked exactly in $\Cl(2,4)$.

## lay
The series writes its gravitational action as a squared curvature seen from a special fixed point, the frozen point. This result asks what that action becomes when it is fed the series' own notion of transport, the connection that carries the conformal geometry of spacetime. The answer is that the frozen point drops out except as an overall factor, and what remains is the action of a different theory, conformal gravity, which only measures tidal distortion and whose equations are of fourth order. With only the series' transport and its canonical marker, this is the one action of its kind that is not purely topological. Einstein's equations appear only when the action is varied over a larger family of connections that keep the frozen point fixed. So the frozen point's job in the action is to choose which fields are varied, not to shape the formula.

## one-liner
On the tractor gauge field of every torsion-free field ($F \cdot X = 0$), $\epsilon(Y, X, F, F)$ is independent of $Y$ beyond $\ip{X}{Y}$, so in the store's orientation the frozen-point integrand is $\epsilon(I, V, F, F) = \epsilon(I, X, F, F) = \ip{X}{I}\,\tfrac12\langle\mathcal{W}(a \wedge b)\,\mathcal{W}(\partial_{b} \wedge \partial_{a})\rangle_{0}$ (the Weyl square, $\tfrac14 W_{abcd}W^{abcd}$) for every $I$ and $\Lambda$: on transport the frozen-point functional is $\tfrac{3}{4\Lambda}$ times the conformal-gravity action; with the canonical tractor alone the only density quadratic in $F$ beyond the Chern form on that locus is this Weyl square (not topological), and none with frame legs has an Einstein-Hilbert term, so the Einstein equations come from varying over connections preserving $I$.
