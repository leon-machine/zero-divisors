---
id: dark-energy.wall-counterterm
kind: claim
version: 4
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
Assume $\Lambda \neq 0$, so that the curvature-squared form (quadratic in the field strength) exists. Let $\omega^{ab}$ be the rotation-gauge field $\Omega$ of the gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), written as Lorentz-connection one-forms in an orthonormal physical frame, $R^{ab} = d\omega^{ab} + \omega^{a}{}_{e}\wedge\omega^{eb}$ its field strength in that frame, and let $Q(\omega) := \epsilon_{abcd}\bigl(\omega^{ab}\wedge d\omega^{cd} + \tfrac23\,\omega^{ab}\wedge\omega^{c}{}_{e}\wedge\omega^{ed}\bigr)$ be its Chern-Simons three-form for the invariant $\epsilon_{abcd}$. Then:
\begin{enumerate}
\item[(i)] $dQ = \epsilon_{abcd}R^{ab}\wedge R^{cd}$ identically: the topological term of Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(2) is exact, with $Q$ as primitive.
\item[(ii)] On a Kasner approach the restriction of $Q$ to the slice $\Sigma_\varepsilon = \{\tau = \varepsilon\}$ is
\[
Q\big|_{\Sigma_\varepsilon} \;=\; 8\,p_1p_2p_3\;\varepsilon^{-2}\, d^3x ,
\]
so that the divergent part of the curvature-squared action on $\{\tau > \varepsilon\}$ is $-\tfrac{3}{\Lambda}\int_{\Sigma_\varepsilon}Q = -\tfrac{24}{\Lambda}\,p_1p_2p_3\,\varepsilon^{-2}\,\mathrm{Vol}_3$, exactly the integral of Proposition \claimref{dark-energy.frozen-point-datum-kasner-wall}(iii).
\item[(iii)] The functional $S_{\mathrm{ren}} := S + \tfrac{3}{\Lambda}\int_{\Sigma_\varepsilon}Q(\omega)$, the action with the Chern-Simons form of the connection restricted to the wall added on the wall, has the same interior field equations as $S$ (a boundary term changes the boundary conditions of the variational problem, not the Euler-Lagrange equations), is finite as $\varepsilon \to 0$ on the Kasner approach, and its limit is the Einstein-Cartan and cosmological contributions together with the value of $Q$ on the far boundary. The counterterm is local, but it is not intrinsic to the wall: on the Kasner approach the whole surviving value comes from the cubic term in the boost block $\omega^{i0}$, the extrinsic curvature of the slice, the quadratic term vanishing because every nonzero $\omega^{ab}$ carries the index $0$ and $\epsilon_{abcd}$ needs four distinct indices. And $Q$ is a Chern-Simons form, not gauge invariant: under a rotation-gauge transformation (a local Lorentz rotation of the frame) on the slice it shifts by an exact form and a Wess-Zumino term, so the counterterm is defined relative to a frame, here the exceptional frame of Fact \claimref{dark-energy.imported-weighted-limit-schwarzschild-singularity-matching}. The residual ambiguity of the renormalisation is that frame choice together with the $O(\Lambda)$ constant by which the finite part shifts under the corrections of Proposition \claimref{dark-energy.cosmological-constant-does-not-change-residue}.
\end{enumerate}
On the Kasner approach the counterterm's coefficient $8p_1p_2p_3$ is the third elementary symmetric function of the residue, the one Kasner invariant beyond the two relations.

## technical
Assume $\Lambda \neq 0$ and let $Q(\omega)$ be the Chern-Simons three-form, for the invariant $\epsilon_{abcd}$, of the rotation-gauge field $\Omega$ of Gauge Theory Gravity written as a Lorentz connection in an orthonormal physical frame. Then $dQ = \epsilon_{abcd}R^{ab}\wedge R^{cd}$ identically, with $R^{ab}$ the field strength, so the topological term of the frozen-point action is exact. On a Kasner approach the restriction of $Q$ to the slice $\Sigma_\varepsilon = \{\tau = \varepsilon\}$ is $8\,p_1p_2p_3\,\varepsilon^{-2}\,d^3x$, so the divergent part of the curvature-squared action is $-\tfrac{24}{\Lambda}\,p_1p_2p_3\,\varepsilon^{-2}\,\mathrm{Vol}_3$, the integral found for the frozen-point datum at a Kasner wall.

Adding $\tfrac{3}{\Lambda}\int_{\Sigma_\varepsilon}Q$ on the wall leaves the interior field equations unchanged, being a boundary term, and makes the action finite as $\varepsilon \to 0$ on the Kasner approach, with limit the Einstein-Cartan and cosmological contributions plus the far-boundary value of $Q$. The counterterm is local but not intrinsic to the wall: its value comes entirely from the cubic term in the boost block, the extrinsic curvature of the slice. Since $Q$ is not gauge invariant, the counterterm is defined relative to a frame, here the exceptional frame, and the residual ambiguity is that frame choice together with an $O(\Lambda)$ constant from the cosmological corrections.

## lay
Assume the cosmological constant is nonzero, so that the curvature-squared form of the frozen-point action exists. In that action one term grows without bound as a Kasner-type singularity is approached. This result shows that the troublesome term is a total derivative, so its divergence sits entirely on the boundary, and it can be cancelled by adding a matching term on the wall. Doing so leaves the field equations away from the wall unchanged. The cancellation is defined relative to a choice of frame and leaves a finite ambiguity of the size of the cosmological corrections.

## one-liner
Assuming $\Lambda \neq 0$, the divergent curvature-squared value on a Kasner approach is the wall restriction of the Chern-Simons form, $8\,p_1p_2p_3\,\varepsilon^{-2}\,d^3x$, and subtracting it on the wall makes the action finite without changing the interior field equations.
