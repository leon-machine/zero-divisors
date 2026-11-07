---
id: synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff
kind: claim
version: 3
title: 'The frozen point reduces the connection only when infinitely stiff'
status: proved
region: synthesis
subject: einstein
tags: [tractors, frozen-point, gauge-fields, symmetry-breaking, curvature-and-field-equations, forcing-and-uniqueness]
proposed_by:
  kind: ai
  session: 2026-11-01-field-space
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
  role: 'GTG proof: forms as multivector fields, the curvature contractions and densities as maps of the curvature operator'
  version: 3
  source: maintainer pass 2026-11-07 (consistency, GTG proofs)
- name: Claude Opus 5.5
  role: 'GTG review (referee F1): two conformal-product values in proof (i) corrected'
  version: 3
  source: maintainer pass 2026-11-07 (consistency, GTG review)
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection@1
  - dark-energy.frozen-point-makes-stelle-west-vector@6
  - synthesis.stelle-west-norm-is-no-local-output@2
  - synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared@3
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@3
  - synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form@1
  - dark-energy.imported-macdowell-mansouri-theorem-stelle-west@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_broken_components_of_the_frozen_point
- kind: check
  ref: check.py::check_stelle_west_family_slot_gradient_at_the_frozen_value
- kind: check
  ref: check.py::check_stiffness_is_the_slot_hessian_form
- kind: check
  ref: check.py::check_stiffness_interpolates_conformal_gravity_and_the_frozen_functional
- kind: check
  ref: check.py::check_frame_equation_is_the_frozen_slot_equation
- kind: check
  ref: check.py::check_gtg_readings_of_the_curvature_operator
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared
  - synthesis.curvature-only-tractor-actions-are-macdowell-mansouri
  - synthesis.stelle-west-norm-is-no-local-output
  - synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form
extraction:
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (fix round): synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part repinned 2 -> 3 after reviewing its convention line, corrected from ''Riemann positive on spheres'' to the store''s sign that its formulas already used (de Sitter Ric = Lambda g, F_abcd = 0); its frame equation 2(G(a) + Lambda a) is unchanged; this result cites that frame equation in (v), in the store sign, so the use holds as cited.'
  maintainer_pass_gtg_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Referee F1 fix 6.1 applied: proof (i) said (ninf ^ n0) . ninf = -n0 and (ninf ^ n0) . n0 = ninf (carried over from the component proof, orig-proof-main.tex, which has the same slip and is kept as history). With (u ^ w) . Y = u (w . Y) - w (u . Y) and n0 . ninf = 1 the values are ninf and -n0; the fixer verified this in Cl(2,4) with GA.py and recomputed Omega_T x I and Omega_T x X for a generic Lorentz bivector, slot, dilation and spacetime vector at rho = 3/7 and -2/5: the displayed DI(a) = rho a - S(a) + beta(a)(ninf - rho n0) and DX(a) = a - beta(a) n0 hold, and the values the proof stated would give beta (rho ninf - n0) and + beta ninf, which fail. So the error did not propagate: the displays, formal (i) and check_broken_components_of_the_frozen_point (which computes the products) were right; only the sentence is corrected. Pins: dark-energy.frozen-point-makes-stelle-west-vector 5 -> 6 (formal unchanged), synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared 2 -> 3 (GA rewrite of (iii), component value kept as reading), synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part 2 -> 3 (see maintainer_pass_pin_review).'
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Proof rewritten in Gauge Theory Gravity: forms as multivector fields (one- and two-forms as linear maps of physical vectors and bivectors, four-form densities as the alternating product on the physical frame); the curvature of Omega as the store-sign operator calR(A ^ B) without pair symmetry when Omega has torsion, its Ricci map d_a . calR(a ^ b) (equal to the index reading sum_a eta^aa R_adab also with torsion), Schouten, Einstein and Weyl maps, traces d_a . M(a), the slot derivative as the map D with dL = d_a . D(dS(a)), the Weyl square (1/2) <W(a ^ b) W(d_b ^ d_a)> and the Euler density from the dictionary; the index expressions of the formal level are their labelled readings. The arguments of (i)-(v) were already in Cl(2,4) and are unchanged. Original proof kept as orig-proof-main.tex. New exact check check_gtg_readings_of_the_curvature_operator (Ricci map and Schouten map against the index readings for a torsion-free and a torsionful curvature, scalar, Weyl square and Euler density in GA against the index values, Q2 by GA traces, L1 at the Schouten slot = Weyl square and at the frozen slot = E/4 - (Lambda/3)(calR - 2 Lambda), and the slot derivative 2(calG + Lambda id) as a map, at two values of rho). outside_ga withdrawn: no stand-in remains in the proof; the formal level''s index expressions are labelled readings.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: The action and its elimination are written in forms and frame components (W_abcd W^abcd, R_abcd R^abcd, eta^{aa} R_{adab}, two-forms F = (1/2) F_ab e^a ^ e^b); the Weyl square is the scalar (1/2)<W(a ^ b) W(d_b ^ d_a)> of the Weyl map, but the elimination is computed on the components.'
  open_problem: op.derive-gravitational-action
  maintainer_pass:
    by: maintainer-2026-11-01
    date: '2026-11-01'
    note: 'Version 1 -> 2: the mentions of the slot lattice (elimination step) and of the slot lemma are now claimrefs, text only, since both are not claimed or used here and the matter-regions result depends on this one; the Reading names the field-space premise synthesis.field-space-premise-parallel-frozen-point by claimref (text only). Statement unchanged.'
  note: >-
    Outside idea tested: the Stelle-West reading of symmetry breaking (Stelle and West 1980, cited from
    memory), applied to the first reduction step, Spin(2,4) to the stabiliser of the frozen point, rather than
    to the second (stabiliser of I to Lorentz, by V). Field space: the unreduced Cl(2,4) connection with frame,
    rotation gauge, special-conformal slot S and dilation beta independent; it contains both the normal tractor
    connection and the I-preserving connections and presupposes no field equation (trap check: the Einstein
    condition is an output in (ii) and (v) only). Results: the broken components of the connection relative to
    stab(I) are S - rho e and beta (DI); the stored Stelle-West family does not set them to zero off the
    Einstein locus (its slot equation at the frozen value is a multiple of G + Lambda_eff), except on one line
    of couplings where the frozen value is the Euler form of the rotation gauge (no field equations); the
    stiffness term eps(I, X, DI, DI, DX, DX), polynomial and inverse-frame free, equals the same quadratic form
    Q2 that is the slot Hessian of the frozen-point integrand, so adding mu times it interpolates exactly
    between conformal gravity (mu = 0) and the frozen-point functional (mu to infinity), with the frozen-point
    functional plus a Weyl-square term in between. In the Stelle-West mechanism the Higgs vector's derivative
    is the frame, nondegenerate; for I the reduction needs DI = 0, which no finite coupling of these terms
    imposes. So the I-preserving field space is the statement that the frozen point is infinitely stiff
    (its broken components absent): an equivalent reading of the field-space premise. A Lagrange multiplier
    for DI imposes DI = 0 at finite coupling and is the premise itself. The slot elimination at mu = 0 is the
    in-series Kaku-Townsend-van Nieuwenhuizen step (stored import), used here only as the mu = 0 end of the
    family; it is clause (ii) of the slot lattice, \claimref{synthesis.frozen-point-integrand-gives-einstein-only-with-the-symmetric-slot-frozen}, and the lemma that the connection preserves I iff S = rho e and beta = 0 is clause (i) of \claimref{synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise}; here (i) gives only
    the explicit broken components DI, DX that the stiffness term is built from (dilation written beta ninf ^ n0,
    as there), and (iii) only the identity of the stiffness form with the slot Hessian. The store already counts
    the twenty broken components per point and says they would spoil the identification
    (dark-energy.frozen-point-makes-stelle-west-vector (iii)); this result says what they give. Clause (v) adds: the slot equation evaluated at the frozen value is the stored frame
    equation, by the frame-slot symmetry of the Lorentz block. Transport-convenient: the chart, X and I are
    the series' objects; transport does not choose mu. Quadratic gravity as fourth order (Stelle 1977, cited
    from memory) is mentioned only in the reading.
---

## formal
Work in $\Cl(2,4)$ with the chart of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection} ($\nO \cdot \nInf = 1$, both null), unit pseudoscalar $i_{6} = e_{0}e_{1}e_{2}e_{3}e_{4}e_{5}$, $\epsilon(\dots)$ the coefficient of $i_{6}$ in the wedge, canonical tractor $X = \nO$, $\Lambda = 6\rho \neq 0$, frozen point $I = \nInf + \rho\nO$ ($Q(I) = 2\rho = \Lambda/3$) and Stelle-West vector $V = X - I/(2\rho)$ (Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}). The \emph{unreduced field} is
\[
\Omega_{T}(a) = \Omega(a) - \nInf \wedge \hb^{-1}(a) + \nO \wedge S(a) + \beta(a)\,\nInf \wedge \nO,
\]
with $\hb$ (invertible), $\Omega$, the special-conformal slot $S$ (a vector-valued one-form) and the dilation $\beta$ (a scalar one-form) independent; $D Y = \Omega_{T} \times Y$. It contains the normal tractor connection ($S = \Sch\,\hb^{-1}$, $\beta = 0$, $\Omega$ torsion-free) and the connections preserving $I$, and no field equation enters its definition. With $I$ and $X$ held as fixed data, the densities below are invariant only under their joint stabiliser, the Lorentz rotations; holding $I$ constant is the unitary gauge of the Higgs reading (a special-conformal rotor of the parabolic group that gauges the tractor field moves $I$). The four-form densities are $L_{1} = \epsilon(I, V, F, F)$, $L_{3} = \epsilon(I, V, DV, DV, F)$, $L_{5} = \epsilon(I, V, DV, DV, DV, DV)$ (the family of Theorem \claimref{synthesis.stelle-west-norm-is-no-local-output}) and the stiffness $St = \epsilon(I, X, DI, DI, DX, DX)$, all polynomial with no inverse frame. In frame components ($\hb = 1$ at a point) write $M$ for a linear map, $Q_{2}(M) = 2\bigl((\tr M)^{2} - \tr(M^{2})\bigr)$ times the volume form, $\mathcal{G}$ the Einstein map of the curvature $\mathcal{R}$ of $\Omega$, $\Sch_{*}$ its Schouten map built from the Ricci contraction (index reading $R_{bd} = \sum_{a}\eta^{aa}R_{adab}$; for torsion-free $\Omega$ the stored Schouten map), and $\mathcal{W} = \mathcal{R} - \mathrm{KN}(\Sch_{*})$ its Weyl part.
\begin{enumerate}
\item[(i)] \emph{(Broken components; proved.)} $DI(a) = \rho\,\hb^{-1}(a) - S(a) + \beta(a)(\nInf - \rho\nO)$ and $DX(a) = \hb^{-1}(a) - \beta(a)\nO$. Relative to the stabiliser of $I$ the broken components are therefore $S - \rho\,\hb^{-1}$ and $\beta$ (that $\Omega_{T}$ preserves $I$ exactly when both vanish is the slot lemma of Theorem \claimref{synthesis.parallel-frozen-point-on-matter-regions-is-the-field-space-premise}(i), and is not claimed here).
\item[(ii)] \emph{(The Stelle-West family does not freeze the slot; computed, general by equivariance.)} With $S$ varied, the slot derivative of $c_{1}L_{1} + c_{3}L_{3} + c_{5}L_{5}$ at the frozen value $S = \rho\,\hb^{-1}$ is, for torsion-free $\Omega$,
\[
\bigl(2c_{1} + c_{3}/\rho\bigr)\,\mathcal{G} + \bigl(2c_{1}\Lambda + 2c_{3}\Lambda/\rho + 12c_{5}/\rho\bigr)\id .
\]
So when $2c_{1} + c_{3}/\rho \neq 0$ the frozen slot solves its own equation only where $\mathcal{G} = -\Lambda_{\mathrm{eff}}\id$, an Einstein condition; for every curvature it does so only on the line $c_{3} = -2\rho c_{1}$, $c_{5} = \rho^{2}c_{1}$, where the density at the frozen slot is $c_{1}$ times the Euler form $\epsilon(I, X, \mathcal{R}, \mathcal{R})$ of $\Omega$ (also with torsion), which has no field equations, while the density still depends on $S$ away from it. More generally, adding to $c_{1}L_{1}$ ($c_{1} \neq 0$) any slot potential that does not involve the curvature leaves the frozen slot stationary only where $2c_{1}(\mathcal{G} + \Lambda\,\id)$ equals a fixed map, again an Einstein condition.
\item[(iii)] \emph{(Stiffness is the slot Hessian; proved.)} $St = Q_{2}(S - \rho\,\hb^{-1})$, independent of $\beta$ and $\Omega$, and the same nondegenerate form is the slot Hessian of the frozen-point integrand: $L_{1}(S) = L_{1}(\Sch_{*}) + Q_{2}(S - \Sch_{*})$ for every curvature, where $\Sch_{*}$, the unique stationary slot of $L_{1}$, is the Schouten map of the slot elimination (for torsion-free $\Omega$ the stored Schouten map, with $L_{1}(\Sch_{*}) = \tfrac14 W_{abcd}W^{abcd}$; the elimination itself is the conformal-gauge step of Fact \claimref{synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form}(b), and is not claimed here).
\item[(iv)] \emph{(Interpolation; proved.)} For $\mu \neq -1$ the slot equation of $L_{1} + \mu\,St$ has the unique solution $S_{\mu} = (\Sch_{*} + \mu\rho\,\id)/(1 + \mu)$ and the density there is $L_{1}(\Sch_{*}) + t\,Q_{2}(\rho\,\id - \Sch_{*})$ with $t = \mu/(1 + \mu)$; for torsion-free $\Omega$, in index reading,
\[
(1 - t)\,\tfrac14 W_{abcd}W^{abcd} + t\Bigl(\tfrac14\bigl(R_{abcd}R^{abcd} - 4R_{ab}R^{ab} + R^{2}\bigr) - \tfrac{\Lambda}{3}(R - 2\Lambda)\Bigr).
\]
At $\mu = 0$ this is the Weyl square (the normal tractor slot, conformal gravity); as $\mu \to \infty$ it is the frozen-point density with the slot frozen; for finite $\mu \neq 0$ it is $t$ times the frozen-point density plus $\tfrac{1-t}{4}W_{abcd}W^{abcd}$: the frozen-point functional with Newton's constant rescaled by $1/t$, plus a Weyl square whose coefficient relative to the Einstein-Hilbert term has magnitude $3/(4\mu\Lambda)$, so with $\Lambda$ as small as observed the Weyl-square scale $(\mu\Lambda)^{-1/2}$ stays unobservable only for enormous $\mu$. $Q_{2}$ is indefinite and $S$ enters without derivatives, so $St$ is a penalty on an auxiliary field, not a mass for propagating fields.
\item[(v)] \emph{(Einstein's equation is the frozen slot's equation; proved.)} The slot derivative of $L_{1}$ at $S = \rho\,\hb^{-1}$ is $2(\mathcal{G} + \Lambda\,\id)$. With $\Omega$ fixed and the slot tied to the frame ($S = \rho\,\hb^{-1}$), the frame derivative of $L_{1}$ is $2\rho$ times it, and divided by $Q(I) = 2\rho$ it is the frame equation $2(\mathcal{G}(a) + \Lambda a)$ of Theorem \claimref{synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part}.
\end{enumerate}
\emph{Reading.} In the Stelle-West mechanism the Higgs vector's covariant derivative is the frame, which must be nondegenerate. Read the same way for the first step, from $\so(2,4)$ to the stabiliser of $I$, the field space of the frozen-point functional asks for the opposite: the broken components $DI$ must vanish. No member of the stored constant-coupling family, and no curvature-independent slot potential, imposes that off the Einstein locus; the stiffness penalty imposes it only in the limit $\mu \to \infty$. A Lagrange multiplier three-form paired with $DI$ (polynomial, inverse-frame free) imposes $DI = 0$ at finite coupling, but adding it is the same premise written into the action. The connections preserving $I$ are therefore the infinitely stiff frozen point, an equivalent reading of the field-space premise (Premise \claimref{synthesis.field-space-premise-parallel-frozen-point}), not a derivation of it. With the slot free the same integrand gives conformal gravity.

## technical
Write the $\Cl(2,4)$ gauge field with all its parts independent: rotation gauge $\Omega$, frame $\hb^{-1}$, special-conformal slot $S$ and dilation $\beta$. This space holds both the normal tractor connection and the connections preserving the frozen point $I = \nInf + \rho\nO$, and assumes no field equation. The covariant derivative of $I$ is $DI = \rho\,\hb^{-1} - S$ plus a dilation part, so the parts that the frozen point "breaks" are $S - \rho\,\hb^{-1}$ and $\beta$. Holding $I$ constant is the unitary gauge; the densities are then invariant only under Lorentz rotations.

Three facts follow, all by exact computation. First, the stored Stelle-West family $c_{1}L_{1} + c_{3}L_{3} + c_{5}L_{5}$ does not hold the slot at its frozen value: there the slot equation reads $(2c_{1} + c_{3}/\rho)\mathcal{G}$ plus a multiple of the identity, which vanishes only on Einstein fields, and the same holds for any slot potential not involving the curvature. The one exception is a single line of couplings, and on it the frozen value of the density is the Euler form, with no field equations. Second, the stiffness term $\epsilon(I, X, DI, DI, DX, DX)$, a polynomial with no inverse frame, is exactly $Q_{2}(S - \rho\,\id)$, $Q_{2}(M) = 2((\tr M)^{2} - \tr M^{2})$, the same quadratic form as the slot Hessian of the frozen-point integrand, which is $\tfrac14 W\cdot W + Q_{2}(S - \Sch)$. Adding $\mu$ times the stiffness gives the slot $S_{\mu} = (\Sch + \mu\rho)/(1 + \mu)$ and the density $(1 - t)\tfrac14 W\cdot W + t\,(\text{frozen-point density})$, $t = \mu/(1 + \mu)$: Einstein gravity with rescaled Newton's constant plus a Weyl square of relative size $3/(4\mu\Lambda)$. Since $S$ has no derivatives and $Q_{2}$ is indefinite, this is a penalty on an auxiliary field, not a mass term. Third, at the frozen value the slot equation is $2(\mathcal{G} + \Lambda)$, and the frame equation of the reduced theory is the same expression: Einstein's equation is the equation the frozen slot would have obeyed.

So the Higgs reading does not supply the field space: it supplies conformal gravity at zero stiffness and the frozen-point functional only in the limit of infinite stiffness, where the broken components vanish. A multiplier imposing $DI = 0$ does it at finite coupling but is the premise itself. Infinite stiffness is thus an equivalent reading of the field-space premise. Transport-convenient.

## lay
Einstein's equations come out of the series' gravitational action only if one particular part of the gravitational field is held fixed rather than allowed to vary. A standard way physicists fix such parts is a Higgs mechanism, in which a field settles into a preferred value. This result tries that idea on the series' fixed point. It finds that the usual terms do not hold the part fixed, except in situations that already obey Einstein's equations. A natural extra penalty term can hold it, but only in the limit where its coefficient is infinite; a term that simply forces the part to stay fixed works too, but that is the assumption itself. With zero strength one gets a different theory, conformal gravity; with finite strength one gets Einstein's theory plus an extra higher-derivative piece. So holding the part fixed remains an assumption, now stated as infinite stiffness.

## one-liner
On unreduced $\Cl(2,4)$ connections ($\hb$, $\Omega$, slot $S$, dilation $\beta$ independent) the frozen point's broken components are $DI = \rho\,\hb^{-1} - S$ plus a dilation part; the stored Stelle-West family has slot equation $(2c_{1} + c_{3}/\rho)\mathcal{G} + (\dots)\id$ at the frozen value, so it freezes the slot only on Einstein fields or, on one line of couplings, at an Euler-only value; so does any curvature-independent slot potential; the polynomial stiffness penalty $\epsilon(I, X, DI, DI, DX, DX) = Q_{2}(S - \rho\,\id)$ is the slot Hessian form, and adding $\mu$ times it gives $(1 - t)\tfrac14 W\cdot W + t\,(\text{frozen-point density})$, $t = \mu/(1+\mu)$ (Weyl square of relative size $3/(4\mu\Lambda)$); a multiplier imposing $DI = 0$ is the premise itself: the connections preserving $I$ are the infinitely stiff limit, an equivalent reading of the field-space premise; transport-convenient.
