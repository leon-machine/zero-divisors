---
id: dark-energy.wall-counterterm
kind: claim
version: 6
title: The wall counterterm
status: proved
region: dark-energy
subject: walls
tags: [kasner, curvature-and-field-equations]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
- name: Claude Opus 5.5
  role: consistency pass, Chern-Simons three-form renamed CS, freeing Q for the square of a vector
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GA rewrite (declared outside_ga)'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: GA rewrite (Chern-Simons form and topological density from Omega and the pseudoscalar pairing)
  version: 6
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - dark-energy.cosmological-constant-does-not-change-residue@6
  - dark-energy.frozen-point-datum-kasner-wall@7
  - dark-energy.frozen-point-makes-stelle-west-vector@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T10.py
  tags:
  - label:prop:counterterm
- kind: check
  ref: check.py::check_transgression_identity
- kind: check
  ref: check.py::check_slice_value_and_divergence_cancelled
- kind: check
  ref: check.py::check_quadratic_term_vanishes_and_gauge_dependence
locators:
  paper: T10
  number: Prop 4.11
  label: prop:counterterm
  line: 935
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Forms to GA on every level and in the proof: the Chern-Simons three-form is defined from the rotation-gauge field itself, CS(a ^ b ^ c) = sum_cyc <Omega(a), b . grad Omega(c) - c . grad Omega(b)>_eps + 2 <Omega(a), Omega(b) x Omega(c)>_eps with the invariant pairing <X, Y>_eps = 4 <X I_4^{-1} Y> of bivectors, the topological density is 2 <R, R>_eps antisymmetrised over four background vectors with R the field strength of the Definition, d is grad ^, and the slice value is CS(e_1 ^ e_2 ^ e_3) = 8 p1 p2 p3 tau^-2, computed in GA from Omega(e_i) = -adot_i B_i; the component forms (CS(omega) with epsilon_{abcd}, eps R ^ R, the Einstein-Cartan and cosmological densities) stay as labelled readings. Sign (reader R09): the component reading takes omega^{ab} as the components of the GTG rotation-gauge field, Omega = (1/2) omega^{ab} gamma_a ^ gamma_b, which is the sign of the Definition (DICTIONARY C10: the Cartan forms omega^{i0} = (p_i/tau) e^i assemble to -(p_i/tau) B_i, the stored Kasner Omega); with the right-action values -Omega the cubic term, odd in the connection, would flip and the slice value would be -8 p1 p2 p3, so the stated coefficient belongs to this identification, which is now explicit. Checked exactly with lib/GA.py in the maintainer scratch against the check module at s = 3/2: on both Kasner connections and on the generic so(1,3) connection of the check, the GA CS equals the check component Q(omega) in all four components and the GA topological density equals the check eps R ^ R. Statement and coefficients unchanged. An earlier pass of this run had declared outside_ga (other) with the Cartan-or-definition sign of omega^{ab} left for Leon; the rewrite settles that sign (above) and the declaration is withdrawn.'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: "The Chern-Simons three-form was written Q(omega), the store symbol for the square of a vector; it is now CS(omega) in every level and the proof, a pure notation change with formulas and coefficients unchanged."
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: dQ = eps R^R on Kasner and a generic connection, the slice value 8 p1 p2 p3 tau^-2 and the cancelled divergence, the vanishing quadratic term, and gauge dependence of Q. Version 3 -> 4.'
  env: proposition
  context_refs:
  - dark-energy.frozen-point-makes-stelle-west-vector
  - dark-energy.imported-weighted-limit-schwarzschild-singularity-matching
  typing:
    by: ai-typing-pass
    added:
    - dark-energy.frozen-point-makes-stelle-west-vector
    note: 'Added the action theorem because the counterterm renormalises its action and its topological
      term; the exceptional frame of the weighted-limit fact only fixes the frame relative to which the
      counterterm is defined and was left as context; clause (i) is the classical transgression formula,
      but no imported claim for it is in the store and the result as a whole has no standard route. Levels
      pass: the lay level now states the $\Lambda \neq 0$ hypothesis and that the counterterm is defined
      relative to a frame; the one-liner''s condition is reworded as an assumption.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-energy.frozen-point-makes-stelle-west-vector
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the Lorentz connection is the rotation-gauge field Omega written as connection one-forms in an orthonormal physical frame, R^{ab} its field strength in that frame, the local Lorentz rotation a rotation-gauge transformation; the identity is local on the chart. Formulas, coefficients and the counterterm unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact.'
---

## formal
Assume $\Lambda \neq 0$, so that the curvature-squared form (quadratic in the field strength) exists. Let $\Omega$ be the rotation-gauge field of the gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), $R(a\wedge b) = a\cdot\nabla\Omega(b) - b\cdot\nabla\Omega(a) + \Omega(a)\times\Omega(b)$ its field strength on background vectors (clause (c) of the Definition), $I_4$ the pseudoscalar of the physical frame, and $\langle X, Y\rangle_{\epsilon} := 4\langle X\,I_4^{-1}\,Y\rangle$ the invariant pairing of bivectors. Scalar forms on the background are read on background multivectors, with exterior derivative $\nabla\wedge$. Let $\mathrm{CS}(\Omega)$ be the Chern-Simons three-form of $\Omega$ for this pairing,
\[
\mathrm{CS}(a\wedge b\wedge c) \;=\; \sum_{\mathrm{cyc}(a,b,c)}\bigl\langle\Omega(a),\ b\cdot\nabla\Omega(c) - c\cdot\nabla\Omega(b)\bigr\rangle_{\epsilon} \;+\; 2\,\bigl\langle\Omega(a),\ \Omega(b)\times\Omega(c)\bigr\rangle_{\epsilon},
\]
and $\mathcal{E}_{R}(a\wedge b\wedge c\wedge d) = 2\bigl(\langle R(a\wedge b), R(c\wedge d)\rangle_{\epsilon} - \langle R(a\wedge c), R(b\wedge d)\rangle_{\epsilon} + \langle R(a\wedge d), R(b\wedge c)\rangle_{\epsilon}\bigr)$ the topological density (in components, a labelled reading: with $\Omega = \tfrac12\omega^{ab}\gamma_a\wedge\gamma_b$, the connection one-forms $\omega^{ab}$ in the sign of the Definition, and $R^{ab} = d\omega^{ab} + \omega^{a}{}_{e}\wedge\omega^{eb}$, these are $\mathrm{CS}(\omega) = \epsilon_{abcd}\bigl(\omega^{ab}\wedge d\omega^{cd} + \tfrac23\,\omega^{ab}\wedge\omega^{c}{}_{e}\wedge\omega^{ed}\bigr)$ and $\epsilon_{abcd}R^{ab}\wedge R^{cd}$). Then:
\begin{enumerate}
\item[(i)] $\nabla\wedge\mathrm{CS} = \mathcal{E}_{R}$ identically (in components $d\,\mathrm{CS} = \epsilon_{abcd}R^{ab}\wedge R^{cd}$): the topological term of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(2) is exact, with $\mathrm{CS}$ as primitive.
\item[(ii)] On a Kasner approach, $\Omega(\hb(e_i)) = -(p_i/\tau)B_i$ at leading order, the restriction of $\mathrm{CS}$ to the slice $\Sigma_\varepsilon = \{\tau = \varepsilon\}$ is
\[
\mathrm{CS}(e_1\wedge e_2\wedge e_3)\big|_{\tau = \varepsilon} \;=\; 8\,p_1p_2p_3\;\varepsilon^{-2}
\]
on the background trivector of the labels $x^1, x^2, x^3$ (in components $\mathrm{CS}|_{\Sigma_\varepsilon} = 8\,p_1p_2p_3\,\varepsilon^{-2}\,d^3x$),
so that the divergent part of the curvature-squared action on $\{\tau > \varepsilon\}$ is $-\tfrac{3}{\Lambda}\int_{\Sigma_\varepsilon}\mathrm{CS} = -\tfrac{24}{\Lambda}\,p_1p_2p_3\,\varepsilon^{-2}\,\mathrm{Vol}_3$, exactly the integral of Proposition \claimref{dark-energy.frozen-point-datum-kasner-wall}(iii).
\item[(iii)] The functional $S_{\mathrm{ren}} := S + \tfrac{3}{\Lambda}\int_{\Sigma_\varepsilon}\mathrm{CS}(\Omega)$, the action with the Chern-Simons form of the connection restricted to the wall added on the wall, has the same interior field equations as $S$ (a boundary term changes the boundary conditions of the variational problem, not the Euler-Lagrange equations), is finite as $\varepsilon \to 0$ on the Kasner approach, and its limit is the Einstein-Cartan and cosmological contributions together with the value of $\mathrm{CS}$ on the far boundary. The counterterm is local, but it is not intrinsic to the wall: on the Kasner approach the whole surviving value comes from the cubic term in the boost block $\Omega(\hb(e_i)) = -(p_i/\tau)B_i$, the extrinsic curvature of the slice, the derivative term vanishing because every nonzero value of $\Omega$ is a boost bivector $B_i$ and $\langle B_i, B_j\rangle_{\epsilon} = 0$ (in components, every nonzero $\omega^{ab}$ carries the index $0$ and $\epsilon_{abcd}$ needs four distinct indices). And $\mathrm{CS}$ is a Chern-Simons form, not gauge invariant: under a rotation-gauge transformation (a local Lorentz rotation of the frame) on the slice it shifts by an exact form and a Wess-Zumino term, so the counterterm is defined relative to a frame, here the exceptional frame of Fact \claimref{dark-energy.imported-weighted-limit-schwarzschild-singularity-matching}. The residual ambiguity of the renormalisation is that frame choice together with the $O(\Lambda)$ constant by which the finite part shifts under the corrections of Proposition \claimref{dark-energy.cosmological-constant-does-not-change-residue}.
\end{enumerate}
On the Kasner approach the counterterm's coefficient $8p_1p_2p_3$ is the third elementary symmetric function of the residue, the one Kasner invariant beyond the two relations.

## technical
Assume $\Lambda \neq 0$ and let $\mathrm{CS}(\Omega)$ be the Chern-Simons three-form of the rotation-gauge field $\Omega$ of Gauge Theory Gravity for the invariant pairing $\langle X, Y\rangle_{\epsilon} = 4\langle X I_4^{-1} Y\rangle$ of bivectors (in components, for $\epsilon_{abcd}$ and the Lorentz connection forms in an orthonormal physical frame). Then $\nabla\wedge\mathrm{CS}$ is the topological density, $2\langle R, R\rangle_{\epsilon}$ antisymmetrised over its four arguments, $R$ the field strength (in components $d\,\mathrm{CS} = \epsilon_{abcd}R^{ab}\wedge R^{cd}$), so the topological term of the frozen-point action is exact. On a Kasner approach the restriction of $\mathrm{CS}$ to the slice $\Sigma_\varepsilon = \{\tau = \varepsilon\}$ is $8\,p_1p_2p_3\,\varepsilon^{-2}$ on the coordinate trivector (in components $8\,p_1p_2p_3\,\varepsilon^{-2}\,d^3x$), so the divergent part of the curvature-squared action is $-\tfrac{24}{\Lambda}\,p_1p_2p_3\,\varepsilon^{-2}\,\mathrm{Vol}_3$, the integral found for the frozen-point datum at a Kasner wall.

Adding $\tfrac{3}{\Lambda}\int_{\Sigma_\varepsilon}\mathrm{CS}$ on the wall leaves the interior field equations unchanged, being a boundary term, and makes the action finite as $\varepsilon \to 0$ on the Kasner approach, with limit the Einstein-Cartan and cosmological contributions plus the far-boundary value of $\mathrm{CS}$. The counterterm is local but not intrinsic to the wall: its value comes entirely from the cubic term in the boost block, the extrinsic curvature of the slice. Since $\mathrm{CS}$ is not gauge invariant, the counterterm is defined relative to a frame, here the exceptional frame, and the residual ambiguity is that frame choice together with an $O(\Lambda)$ constant from the cosmological corrections.

## lay
Assume the cosmological constant is nonzero, so that the curvature-squared form of the frozen-point action exists. In that action one term grows without bound as a Kasner-type singularity is approached. This result shows that the troublesome term is a total derivative, so its divergence sits entirely on the boundary, and it can be cancelled by adding a matching term on the wall. Doing so leaves the field equations away from the wall unchanged. The cancellation is defined relative to a choice of frame and leaves a finite ambiguity of the size of the cosmological corrections.

## one-liner
Assuming $\Lambda \neq 0$, the divergent curvature-squared value on a Kasner approach is the wall restriction of the Chern-Simons form, $8\,p_1p_2p_3\,\varepsilon^{-2}\,d^3x$, and subtracting it on the wall makes the action finite without changing the interior field equations.
