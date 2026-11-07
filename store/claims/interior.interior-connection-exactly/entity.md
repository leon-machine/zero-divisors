---
id: interior.interior-connection-exactly
kind: claim
version: 8
title: The interior connection, exactly
status: proved
region: interior
subject: interior
tags: [schwarzschild]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
- name: Claude Opus 5.5
  role: GA rewrite (first structure equation as the GTG torsion equation)
  version: 8
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - interior.exact-parallelism-convergence-rate@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_rotation_gauge_field_from_torsion
- kind: check
  ref: check.py::check_frame_parallel_along_free_fall
- kind: check
  ref: check.py::check_sphere_coefficient_scales_as_one_over_r
locators:
  paper: T06
  number: Lem 5.3
  label: lem:conn
  line: 646
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Forms to GA: the proof now solves the torsion equation of the Definition, hb^T(grad ^ f^a) = sum_b e^b ^ (omega(e_b) . e^a), the first structure equation read through the outermorphism hb^T (f^a the background vector fields with hb^T(f^a) = e^a, grad ^ the exterior derivative); the Cartan forms stay as a labelled component reading in the formal level and the proof. Equivalence checked exactly with lib/GA.py and lib/gtg.py in the maintainer scratch: the displayed Omega solves this GA equation at two rational interior points (rank-24 uniqueness by the existing check) and the opposite sign does not; the same identity was checked on the PG field and on the variable-exponent Kasner field. Values unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: interior gauge field on flat spacetime: the proof''s connection forms satisfy the torsion equation (unique, rank 24), D-parallel frame, sphere term cot(theta)/r; boost sign in the Definition''s convention. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 6 -> 7.'
  typing:
    by: ai-typing-pass
    added: [interior.exact-parallelism-convergence-rate]
    note: 'Added the parallel-frame lemma from context_refs because the statement is set in its frame and the proof uses its synchronous scale factors; this is a setting dependency rather than a use of the parallelism itself.'
  env: lemma
  context_refs:
  - interior.exact-parallelism-convergence-rate
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - interior.exact-parallelism-convergence-rate
    note: 'The premise supplies only the parallel frame and the rates sigma_i that the statement is written in; the connection itself is computed directly, so the citation marks the frame.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the Levi-Civita connection of the interior metric is named as the rotation-gauge field Omega of the interior gravitational field (its torsion-free connection, whose reading on the derived metric is the Levi-Civita connection); the sphere term is the connection induced on the round two-spheres. Values unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact. Fix (Leon 2026-10-23, referee GR1): displayed connection values re-signed to the GTG sign of the definition, D_a = a.nabla + Omega(a) x (Cartan forms omega^i_0 = sigma_i theta^i assemble to -sigma_i B_i; Hubble-normalised Kasner model -sum_i p_i B_i, DICTIONARY C10); content unchanged.'
---

## formal
In the parallel frame of Lemma \claimref{interior.exact-parallelism-convergence-rate}, write $B_i := e_0 \wedge e_i$ for the three boost bivectors and $R_{ij} := e_i \wedge e_j$ for the rotations. The rotation-gauge field $\Omega$ of the interior gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}: the torsion-free connection, whose reading on the derived metric is its Levi-Civita connection), evaluated on the unit tangential physical directions (through $A \cdot D = D_{\hb(A)}$, so that $\Omega(e_c)$ stands for $\Omega(\hb(e_c))$), is exactly
\[
\Omega(e_1) = -\sigma_1 B_1, \qquad
\Omega(e_2) = -\sigma_2 B_2, \qquad
\Omega(e_3) = -\sigma_3 B_3 + \frac{\cot\theta}{r}\,R_{23},
\]
and $\Omega(e_0) = 0$, in the sign of the Definition, $D_a M = a \cdot \nabla M + \Omega(a) \times M$ (in components, a labelled reading: the Cartan connection forms $\omega^{i}{}_{0} = \sigma_i\,\theta^i$ of the coframe $\theta^0 = d\tau$, $\theta^i = a_i\,dx^i$ assemble to $-\sigma_i B_i$). The rotation coefficient is the connection induced by $D$ on the round two-spheres of fixed $(\tau, t)$, of radius $r$: in any local orthonormal frame on an $S^2$ coordinate patch its coefficients are $O(1/r)$.

## technical
In the parallel frame of the Schwarzschild interior, write $B_i = e_0 \wedge e_i$ for the boosts and $R_{ij} = e_i \wedge e_j$ for the rotations. The rotation-gauge field $\Omega$ of the gravitational field, the connection of Gauge Theory Gravity on flat spacetime, is on unit tangential directions exactly $\Omega(e_1) = -\sigma_1 B_1$, $\Omega(e_2) = -\sigma_2 B_2$ and $\Omega(e_3) = -\sigma_3 B_3 + (\cot\theta/r)\,R_{23}$, with $\Omega(e_0) = 0$. The only rotation coefficient is the connection induced on the round two-spheres of radius $r$, whose coefficients in any local orthonormal frame on a patch of $S^2$ are $O(1/r)$.

## lay
This result writes down exactly how directions twist into one another as one moves about inside a non-rotating black hole. Along each direction the effect is a pure stretching, except for one extra rotation term that reflects the curvature of the spheres of fixed radius. That rotation term grows like one over the radius.

## one-liner
In the parallel frame of the Schwarzschild interior the rotation-gauge field $\Omega$ is exactly $-\sigma_i B_i$ on each unit tangential direction, plus the round-sphere rotation $(\cot\theta/r)R_{23}$ on $e_3$, with $\Omega(e_0) = 0$.
