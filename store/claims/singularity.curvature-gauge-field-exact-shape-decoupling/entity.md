---
id: singularity.curvature-gauge-field-exact-shape-decoupling
kind: claim
version: 5
title: 'The curvature of the gauge field: exact shape decoupling'
status: proved
region: singularity
subject: singularity
tags: [schwarzschild, curvature-and-field-equations]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, curvature sign of the statement attributed to the store convention, not to the background field strength'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - singularity.imported-equivalence-einstein-equations@3
  - singularity.solution-where-divergence-lies@4
  - std-algebra.pseudoscalar-commutation@1
  - std-algebra.orthogonal-anticommute@1
  proof: proof-main.tex
- name: standard-route
  uses:
  - pairing.imported-weyl-scalars-petrov-type-schwarzschild@3
  proof: proof-standard-route.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:6.1
- kind: check
  ref: check.py::check_radial_plane_is_hb_invariant
- kind: check
  ref: check.py::check_shape_operator_matches_gauge_curvature
- kind: check
  ref: check.py::check_shape_operator_spectrum
locators:
  paper: T05
  number: Thm 6.1
  label: thm:shape
  line: 1615
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.pseudoscalar-commutation, std-algebra.orthogonal-anticommute where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: hb-invariance of the radial plane, calR = -(M/r^3) S from the PG gauge fields with S = 1 - 3 Pi = -(B + 3 sigma B sigma)/2, S^2 + S = 2, the spectrum and trace. Version 2 -> 3.'
  env: theorem
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    added:
    - pairing.imported-weyl-scalars-petrov-type-schwarzschild
    note: 'removed the repair edge to the transport algorithm, which frames the section as a step of the algorithm but is not a premise of the computation; the paper says the spectrum is classical (citing Chandrasekhar, not in the store), so the standard route uses the store''s imported Petrov type-D entry, which carries the same content from Penrose and Rindler; the operator identity on top of the spectrum is algebra, but whether the standard route should count as recovering the whole theorem is a judgement call.'
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. Citation of the sign corrected, formula unchanged: the statement said its sign convention was that of singularity.solution-where-divergence-lies(1) and of the Cartan appendix, "which agree"; but (1) displays the background field strength R in LDG sign (dictionary C5), whose radial eigenvalue is -2M/r^3, while calR = -(M/r^3)S with calR(sigma_r) = +2M/r^3 sigma_r is the store sign (dictionary C6), that of the Cartan appendix. The statement now names the store sign and says how (1) reads; the proof''s assembly step gets the same sentence. the computation recorded: in lib/GA.py (Cl(1,3)), sigma_r = e_r e_t = -(e_t wedge e_r) with sigma_r^2 = 1, hb(e_t) wedge hb(e_r) = e_t wedge e_r for hb(a) = a - beta (a.e_t) e_r, and with the background field strength R(e_t wedge e_r) = (2M/r^3) sigma_r (the displayed value, commutator term zero) the LDG-sign eigenvalue on that plane is -2M/r^3 and the store sign gives calR(sigma_r) = -R(hb(sigma_r)) = +(2M/r^3) sigma_r, checked at M = 1, r = 2; the orientation sigma_r = e_r e_t is the one docs/gtg-dictionary.md C6 and C10 record for singularity.connection-bivector-computed.'
---

## formal
Let $\sigma_r$ be the unit bivector of the radial boost plane, and let $\Pi$ denote the projection of the six-dimensional bivector space onto $\operatorname{span}\{\sigma_r, I\sigma_r\}$, with $I$ the pseudoscalar. The radial plane is $\hb$-invariant,
\[
\hb(\et) \wedge \hb(\er) \;=\; (\et - \beta\er) \wedge \er \;=\; \et \wedge \er ,
\]
so the coordinate and physical radial planes coincide and $\sigma_r$ needs no chart to define. Then, exactly and at every radius,
\[
\mathcal{R}(B) \;=\; -\,\frac{M}{r^3}\,S(B), \qquad
S \;:=\; 1 - 3\Pi \;=\; -\tfrac12\bigl(B \mapsto B + 3\,\sigma_r B \sigma_r\bigr),
\]
in the store's curvature sign $\mathcal{R}(B) = -R(\hb(B))$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), which is that of the Cartan computation of Appendix \ref{app:schw}: $\mathcal{R}(\sigma_r) = +2M/r^{3}\,\sigma_r$ while $S(\sigma_r) = -2\sigma_r$ (Proposition \claimref{singularity.solution-where-divergence-lies}(1) displays the background field strength $R$ in Lasenby, Doran and Gull's sign, whose eigenvalue on the radial plane, $\sigma_r = \er\et = -\partial_t\wedge\partial_r$, is $-2M/r^{3}$: the same statement) (only the eigenvalue ratio, the trace, and the identity of the distinguished plane pair enter the chain, and each is convention-free). The shape operator satisfies
\[
S^2 + S = 2 ,
\]
has spectrum $(-2, -2, 1, 1, 1, 1)$ with the doubled eigenvalue attained exactly on $\{\sigma_r, I\sigma_r\}$, and is trace-free on $\Lambda^2$, though that verifies an algebraic identity rather than field equations: $\tr(1 - 3\Pi) = 6 - 6 = 0$ holds automatically for any rank-two $\Pi$, and trace-freeness on $\Lambda^2$ is the vanishing of the scalar curvature, not Ricci flatness, which is carried by the solution of Section \ref{sec:locate} and not by this operator identity. The entire approach to the singularity is carried by the single scalar $M/r^3$.

## technical
Let $\Pi$ project the six-dimensional bivector space onto $\operatorname{span}\{\sigma_r, I\sigma_r\}$, where $\sigma_r$ is the unit radial boost bivector; the radial plane is $\hb$-invariant, so $\sigma_r$ is defined without a chart. Then, exactly and at every radius, $\mathcal{R}(B) = -(M/r^3)\,S(B)$ with $S = 1 - 3\Pi$, equivalently $S(B) = -\tfrac12(B + 3\sigma_r B \sigma_r)$. The shape operator satisfies $S^2 + S = 2$, has spectrum $(-2,-2,1,1,1,1)$ with the doubled eigenvalue attained exactly on the plane pair, and is trace-free on $\Lambda^2$.

Trace-freeness holds automatically for any rank-two $\Pi$ and expresses the vanishing of the scalar curvature, not Ricci flatness, which is carried by the solution itself. The entire approach to the singularity is carried by the single scalar $M/r^3$.

## lay
The tidal curvature of a non-rotating black hole splits exactly into a fixed geometric shape times a single number. The shape singles out the radial direction and is the same at every radius; only the strength, mass divided by radius cubed, changes. So the whole approach to the central singularity is governed by that one scalar.

## one-liner
The curvature of the black-hole gauge field is exactly $\mathcal{R} = -(M/r^3)\,S$ with $S = 1 - 3\Pi$ a fixed shape operator of spectrum $(-2,-2,1,1,1,1)$.
