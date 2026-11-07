---
id: synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared
kind: claim
version: 4
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
- name: Claude Opus 5.5
  role: 'GTG reading of the proof: two-forms as linear maps on physical bivectors, the Weyl-square identity on Weyl maps, (v) pointwise from the product operator; declaration narrowed'
  version: 3
  source: maintainer pass 2026-11-07 (GTG proofs)
- name: Claude Opus 5.5
  role: 'GTG review fixes (referee F3): Weyl space described with the first Bianchi identity; frame-leg pairings of (iv) proved in GA with a new check; declaration narrowed; Beyond-one-flat-chart flag added (dictionary section 14); stale pins reviewed'
  version: 3
  source: maintainer pass 2026-11-07 (GTG review fixes)
- name: Claude Opus 5.5
  role: 'GA rewrite of the two-form and four-form definitions (linear maps of physical bivectors and their densities), the frame-leg two-form and the Weyl square of (v); the component forms kept as readings; new exact check'
  version: 4
  source: maintainer pass 2026-11-07 (decisions, second round)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection@1
  - dark-energy.frozen-point-makes-stelle-west-vector@6
  - synthesis.imported-gtg-dictionary@2
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@3
  - synthesis.imported-miskovic-olea-identity@3
  - synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale@3
  - synthesis.promoted-norm-weyl-clock-flat-weight@7
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
- kind: check
  ref: check.py::check_gtg_weyl_square_of_weyl_maps
- kind: check
  ref: check.py::check_gtg_frame_legs_and_weyl_space
- kind: check
  ref: check.py::check_gtg_four_form_density_of_bivector_maps
lineage:
  motivated_by:
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part
  - synthesis.imported-miskovic-olea-identity
  - synthesis.promoted-norm-weyl-clock-flat-weight
extraction:
  flags:
  - 'beyond one flat chart: the closed Riemannian S^2 x S^2 and the integrals over it'
  maintainer_pass_decisions_2:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Leon''s answers, second round, item 7 (version 3 -> 4): the formal''s remaining non-GA notation rewritten in GA, the mathematics unchanged. A bivector-valued two-form is now the linear map B -> F(B) of physical bivectors to bivectors of Cl(2,4), and the four-form beta(F ^ G) of a bilinear pairing is (1/2) beta(F(c ^ d), G(I4 (d_d ^ d_c))) vol, I4 = e0 e1 e2 e3 the spacetime pseudoscalar of the orientation of i6 (eps(a, b, F, G) for beta = eps(a, b, ., .), K(F ^ G) for beta = K); the old forms F = (1/2) F_ef e^e ^ e^f and the coefficient on e^0 ^ e^1 ^ e^2 ^ e^3 as the sum over ordered pairs of complementary planes are kept as the labelled reading. The frame legs DX ^ DX are named as the two-form a ^ b -> 2 ((a . D) X) ^ ((b . D) X), the values 2 e_e ^ e_f the proof already used. In (v) the Weyl square is written 2 <W(a ^ b) W(d_b ^ d_a)>_0, W_abcd W^abcd as reading (the identity of (iii), and the dictionary''s Kretschmann identity). Evidence: new check check_gtg_four_form_density_of_bivector_maps: for two generic rational maps F, G and five pairings (eps(Y, X, ., .) at three Y, eps(I, V, ., .) at the frozen point, K) the component coefficient (1/4) sum_p sgn(p) beta(F_{p0 p1}, G_{p2 p3}) equals the GA density in all fifteen cases; in the general frame f_a = H(e_a), det H = -50, the component coefficient on f^0 ^ ... ^ f^3 is det H times the density (the four-form is density times vol, so the reading holds in any coframe, coordinate ones included); (a . D) X = a from the tractor gauge field with a generic slot, and 2 (a . D X) ^ (b . D X) is the frame-leg two-form of the component check. The declaration is narrowed to what remains: the Chern-Simons form of (iv) and its exactness proof, the global integrals of (v) and its signature transfer.'
  maintainer_pass_gtg_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Blind referee F3: accept with fixes; all checked exactly (lib/GA.py, lib/gtg.py). (4a) The Weyl space was described as trace-free and I-linear: with symmetry these conditions cut out 11 dimensions (computed), B -> I4 B satisfying them and violating the first Bianchi identity; with d_a ^ W(a ^ b) = 0 added, 10 (computed). Proof (iii) now names the Bianchi identity. (4b) The frame-leg argument of (iv) is now in GA: with F = -calR on the Lorentz block (the Cotton block drops out), K(DX ^ DX, F) = -<I4 calR(a ^ b)(d_b ^ d_a)>, zero by the first Bianchi identity, and eps_X(DX ^ DX, F) = -<calR(a ^ b)(d_b ^ d_a)> = -calR, zero on the Weyl block by trace-freeness; new check check_gtg_frame_legs_and_weyl_space verifies both identities on a Kulkarni-Nomizu map with a Ricci part (K = 0, eps = 2 = -calR), on B -> I4 B (K = 12 = -<I4 ...>) and their sum, zero on the ten basis Weyl maps, and the Bianchi statements of (4a); runcheck 9/9; five mutants (signs of both identities, the Bianchi control, outer -> commutator in the Bianchi map, a pinned value) all fail. (4c) The declaration now names what is left: the statements two-forms and four-forms, the Chern-Simons form of (iv) and its frame-component exactness proof, (v)s global integrals and (v)s signature-transfer argument. (4d) Dictionary section 14 prescribes the flag sentence at the end of the formal level and in technical, and the extraction.flags entry, for every result with a global ingredient; (v) integrates over the closed S^2 x S^2, so the sentence and the flag were added (the house rule, not a change of the mathematics; the proof already carried the sentence). Also corrected (not a referee finding, a false sentence the proof does not need): proof (v) gave the product operator of S^2 x S^2 on Cl(4,0) as +K1, +K2; in the store sign it is -K1 e1 ^ e2, -K2 e3 ^ e4 (computed from the torsion-solved field of S^2(1) x S^2(1/4) with lib/gtg.py, now asserted in check_gtg_weyl_square_of_weyl_maps, with the dictionary''s Euclidean note of this run: the round S^4 has calR = -12); the densities are quadratic, so no value changes.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Stale pins reviewed (fix round, 2026-11-07): dark-energy.frozen-point-makes-stelle-west-vector 5 -> 6 and synthesis.promoted-norm-weyl-clock-flat-weight 6 -> 7 have byte-identical formal levels (N). R: synthesis.imported-gtg-dictionary 1 -> 2 (frame-plane reading of clause (iv) restated) is cited for the Weyl part and the Schouten map of (v), unchanged; synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part 2 -> 3 now names the store curvature sign in place of positive on spheres, and is cited only in the Reading for its Einstein equations from varying over I-preserving connections, which the change does not touch; synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale 2 -> 3 (A3, signs of (ii)) is cited only for the scale non-selection that (ii) of this result extends, untouched by A3. Uses hold; all five repinned.'
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Partial GTG proof: the proof''s algebra was already in Cl(2,4); now the two-forms are read as linear maps B -> F(B) on physical bivectors, the identity of (iii) is stated and checked as eps_X(F1, F2) = (1/2) <W1(a ^ b) W2(d_b ^ d_a)> on ten independent Weyl maps built by the library (Weyl parts of Kulkarni-Nomizu operators; trace-free and I-linear confirmed), all 55 pairs and with the Cotton block, and (v) computes the Weyl square (4/3)(K1 + K2)^2 and Euler density 8 K1 K2 pointwise from the product operator of Cl(4,0), with the Beyond-one-flat-chart sentence for the integrals; the component Weyl tensors stay as the confirming reading. Not achieved without a formal change: the statement itself is written in two-forms and four-forms, and (v) is a global integral, so the declaration is kept, narrowed. New check check_gtg_weyl_square_of_weyl_maps; runcheck 8/8, check4 clean on a proposals copy. Statement, status, links unchanged (the flag entry for (v) is not added; listed for Leon).'
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
  why: '(iv) states the Chern-Simons form <A ^ dA>_0 + (1/3)<A ^ (A x A)>_0 as a differential form and proves its exactness in frame components; clause (v) integrates over the closed Riemannian S^2 x S^2, beyond one flat chart, and transfers the conclusion to Lorentzian signature by the argument that the Euler-Lagrange derivative is a universal polynomial in the metric jets. The two-forms and four-forms of the statement are linear maps of physical bivectors and their densities, the proof''s algebra is in Cl(2,4), and the Weyl-square identity of (iii), the frame-leg pairings of (iv) and the pointwise densities of (v) are computed on curvature maps as linear functions of bivectors.'
---

## formal
Work in $\Cl(2,4)$ with $\nO$, $\nInf$ as in Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection} ($\nO \cdot \nInf = 1$, both null) and canonical tractor $X = \nO$. Orientation and conventions are those of the stored check of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}: the unit pseudoscalar is $i_{6} = e_{0}e_{1}e_{2}e_{3}\,(\nInf \wedge \nO)$, and for vectors $a, b$ and bivectors $F, G$, $\epsilon(a, b, F, G)$ is the coefficient of $i_{6}$ in $a \wedge b \wedge F \wedge G$. A bivector-valued two-form is a linear map $B \mapsto F(B)$ from physical bivectors to bivectors of $\Cl(2,4)$. For a bilinear pairing $\beta$ of bivectors, $\beta(F \wedge G)$ is the four-form $\tfrac12\,\beta\bigl(F(c \wedge d),\, G(I_{4}(\partial_{d} \wedge \partial_{c}))\bigr)\,\mathrm{vol}$, summed over physical vectors $c, d$, with $I_{4} = e_{0}e_{1}e_{2}e_{3}$ the spacetime pseudoscalar of the orientation of $i_{6}$ and $\mathrm{vol}$ its volume form; $\epsilon(a, b, F, G)$ also denotes this four-form for $\beta = \epsilon(a, b, \cdot, \cdot)$, and $K(F \wedge G)$, also written $K(F, G)$ for two-forms, for $\beta = K$ below. (Reading: $F = \tfrac12 F_{ef}\,e^{e} \wedge e^{f}$ with $F_{ef} = F(e_{e} \wedge e_{f})$, and the four-form's coefficient on $e^{0} \wedge e^{1} \wedge e^{2} \wedge e^{3}$ is the sum over ordered pairs of complementary coordinate planes, one quarter of the sum over the twenty-four orderings.) In the opposite orientation every $\epsilon$ below changes sign. Let $(\hb, \Omega)$ be a torsion-free gravitational field on flat spacetime with Weyl part $\mathcal{W}$ of its curvature (Fact \claimref{synthesis.imported-gtg-dictionary}), $\Omega_{T}$ its tractor gauge field and $F$ the field strength of $\Omega_{T}$. Let $\Lambda \neq 0$, $I$ any tractor with $\ip{X}{I} \neq 0$ (the frozen point $\nInf + \tfrac{\Lambda}{6}\nO$ has $\ip{X}{I} = 1$) and $V = X - \tfrac{3}{\Lambda}I$, so that $I \wedge V = I \wedge X$ (Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(ii)).
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
\item[(iv)] \emph{(The quadratic densities on the locus; proved.)} The bilinear forms on $\Lambda^{2}(X^{\perp})$ invariant under the stabiliser of $X$ are: symmetric, a two-dimensional space spanned by the Killing form $K(F, G) = \langle FG\rangle_{0}$ and $\epsilon_{X}$; antisymmetric, none. Under the internal reflection in a spacetime vector, with the spacetime orientation fixed, $K$ is even and $\epsilon_{X}$ odd; under parity in the usual combined sense $\epsilon_{X}(F, F)$, the Weyl square, is even and $K(F \wedge F)$, on the locus the Pontryagin density of the Weyl curvature, is odd. In four dimensions $K(F \wedge F)$ is the Chern form, $d$ of the Chern-Simons form $\langle A \wedge dA\rangle_{0} + \tfrac13\langle A \wedge (A \times A)\rangle_{0}$ of any $\Cl(2,4)$ connection $A$. The pairings of $F$ with the frame legs, the two-form $DX \wedge DX$ that takes $a \wedge b$ to $2\,((a \cdot D)X) \wedge ((b \cdot D)X)$, allowed by the same forms, $K(DX \wedge DX, F)$ and $\epsilon_{X}(DX \wedge DX, F)$, vanish on the locus.
\item[(v)] \emph{(Not topological; proved.)} On $S^{2} \times S^{2}$ with Riemannian product metric of constant curvatures $K_{1}$, $K_{2}$, $\int 2\langle\mathcal{W}(a \wedge b)\,\mathcal{W}(\partial_{b} \wedge \partial_{a})\rangle_{0}\,\mathrm{vol} = 16\pi^{2}\cdot\tfrac43(K_{1} + K_{2})^{2}/(K_{1}K_{2})$ (in components $\int W_{abcd}W^{abcd}\,\mathrm{vol}$), which changes with $K_{2}/K_{1}$, while the Euler integral is $128\pi^{2}$ for every ratio. So the Euler-Lagrange derivative of the Weyl square is not identically zero, in either signature.
\end{enumerate}
\emph{Reading.} With the canonical tractor alone and the field strength on transport's locus, the densities quadratic in $F$ are $\alpha K + \beta\epsilon_{X}$, $K$ exact, and the stored frozen-point functional is the $\epsilon_{X}$ one: its field equations on transport are those of conformal gravity (the Bach equations, Fact \claimref{synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form}(a)), fourth order, solved by Einstein fields but not only by them. No density quadratic in $F$, with the frame legs $DX$ and the canonical tractor alone, has an Einstein-Hilbert term on transport's locus; the Einstein equations of Theorem \claimref{synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part} come from varying the functional over connections preserving $I$, not from the integrand. For a normal tractor connection, preserving $I$ is the Einstein condition (Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}(ii)); the hypothesis that admits only the $I$-preserving connections is the absence of an inverse frame, which excludes the Schouten slot of the normal connection (Theorem \claimref{synthesis.curvature-only-tractor-actions-are-macdowell-mansouri}). By (ii), restricted to a conformal class the integrand does not see the scale beyond $\ip{X}{I}$, which extends Theorem \claimref{synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale} to this integrand: the selection of the Einstein scale by the functional works through its field space. The statement that the tractor field alone gives only the Chern form is four-dimensional; in five dimensions the cubic Pfaffian of $\Cl(2,4)$ has a Chern-Simons form with field equations (Theorem \claimref{synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons}). \emph{Beyond one flat chart.} The closed Riemannian $S^{2} \times S^{2}$ of (v) and the integrals over it are global and are not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the statements above that hold on the invertible region are in Gauge Theory Gravity, and that manifold and its integrals are read on the manifold assembled from the derived metric's charts.

## technical
The open problem asks whether transport fixes the frozen-point MacDowell-Mansouri functional $Q(I)^{-1}\int\epsilon(I, V, F, F)$. This result evaluates that integrand on the series' own transport: the tractor gauge field of an arbitrary torsion-free field. Its field strength has Lorentz block minus the Weyl part, a Cotton block along $\nO$ and no torsion block, so it annihilates the canonical tractor $X = \nO$. On such bivectors the six-vector contraction $\epsilon(Y, X, F, G)$ depends on $Y$ only through $\ip{X}{Y}$, because $X \wedge F \wedge G$ lies in the one-dimensional top power of the five-dimensional space $X^{\perp}$; this defines $\epsilon_{X}$ at fixed $X$. Since $V$ differs from $X$ by a multiple of $I$, the frozen-point integrand is $\epsilon(I, X, F, F) = \ip{X}{I}\,\epsilon_{X}(F, F)$, and $\epsilon_{X}(F, F)$ is one quarter of the Weyl square in the store's orientation. So on transport the frozen-point functional is $\tfrac{3}{4\Lambda}$ times the conformal-gravity action, for every torsion-free field; the frozen point enters only through the prefactor. That the epsilon-contracted square of the conformal-group curvature is the Weyl action is the construction of conformal gravity by Kaku, Townsend and van Nieuwenhuizen (Fact \claimref{synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form}(b)), here on the series' tractor gauge field; the series-specific content is the independence of the second vector, which makes the frozen point drop out. On Einstein fields this is the on-shell identity of Mišković and Olea already in the store. On the same locus the stabiliser of $X$ admits exactly two invariant quadratic forms, the Killing form (the Chern form, exact in four dimensions) and $\epsilon_{X}$, which is odd under the internal reflection and even under parity in the usual sense; the frame-leg terms vanish there, so no Einstein-Hilbert term exists in this class. The Weyl square is not topological: its integral over a product of two spheres changes with the radius ratio while the Euler integral does not. Einstein's equations of the stored functional come from varying it over connections preserving $I$, which leave the normal tractor connections. All algebra is checked exactly in $\Cl(2,4)$. Its closed product of two spheres and the integrals over it are global: no single gravitational field on flat spacetime carries them, so that part is read on the curved manifold.

## lay
The series writes its gravitational action as a squared curvature seen from a special fixed point, the frozen point. This result asks what that action becomes when it is fed the series' own notion of transport, the connection that carries the conformal geometry of spacetime. The answer is that the frozen point drops out except as an overall factor, and what remains is the action of a different theory, conformal gravity, which only measures tidal distortion and whose equations are of fourth order. With only the series' transport and its canonical marker, this is the one action of its kind that is not purely topological. Einstein's equations appear only when the action is varied over a larger family of connections that keep the frozen point fixed. So the frozen point's job in the action is to choose which fields are varied, not to shape the formula.

## one-liner
On the tractor gauge field of every torsion-free field ($F \cdot X = 0$), $\epsilon(Y, X, F, F)$ is independent of $Y$ beyond $\ip{X}{Y}$, so in the store's orientation the frozen-point integrand is $\epsilon(I, V, F, F) = \epsilon(I, X, F, F) = \ip{X}{I}\,\tfrac12\langle\mathcal{W}(a \wedge b)\,\mathcal{W}(\partial_{b} \wedge \partial_{a})\rangle_{0}$ (the Weyl square, $\tfrac14 W_{abcd}W^{abcd}$) for every $I$ and $\Lambda$: on transport the frozen-point functional is $\tfrac{3}{4\Lambda}$ times the conformal-gravity action; with the canonical tractor alone the only density quadratic in $F$ beyond the Chern form on that locus is this Weyl square (not topological), and none with frame legs has an Einstein-Hilbert term, so the Einstein equations come from varying over connections preserving $I$.
