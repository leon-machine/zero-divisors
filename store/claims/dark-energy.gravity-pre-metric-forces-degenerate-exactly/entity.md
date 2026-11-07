---
id: dark-energy.gravity-pre-metric-forces-degenerate-exactly
kind: claim
version: 5
title: Gravity is pre-metric; the forces degenerate exactly where the conformal class does
status: proved
region: dark-energy
subject: dark-energy
tags: [refutation, gauge-fields, curvature-and-field-equations, no-go]
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
  role: 'GA rewrite (declared outside_ga)'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'GTG proof: forms as multivector fields, the star as |det hb|^-1 I G(F) with G the cometric map'
  version: 5
  source: maintainer pass 2026-11-07 (consistency, GTG proofs)
- name: Claude Opus 5.5
  role: 'GTG review (referee F1): proof citation corrected'
  version: 5
  source: maintainer pass 2026-11-07 (consistency, GTG review)
review: typed
derivations:
- name: main
  uses:
  - dark-energy.frozen-point-makes-stelle-west-vector@6
  - dark-energy.imported-walls-sphere-theorem@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T10.py
  tags:
  - label:thm:twokinds
- kind: check
  ref: check.py::check_star_free_invariant_is_topological
- kind: check
  ref: check.py::check_hodge_star_depends_on_conformal_class_only
- kind: check
  ref: check.py::check_star_degenerates_at_corank_one_wall
- kind: check
  ref: check.py::check_gtg_star_free_density_is_a_divergence
- kind: check
  ref: check.py::check_gtg_hodge_star_is_the_cometric_duality
- kind: check
  ref: check.py::check_gtg_star_has_no_limit_at_a_corank_one_wall
locators:
  paper: T10
  number: Thm 4.3
  label: thm:twokinds
  line: 823
extraction:
  maintainer_pass_gtg_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Blind referee F1: ACCEPT. Its one remark (the variation''s plus sign is right; the component proof had a minus, harmless since the term vanishes) needs no change. Fixer: the opening sentence attributed the reading of forms as multivector fields to Fact synthesis.imported-gtg-dictionary, which states nothing about forms (clauses (i) to (vi): vectors, derivative, geodesics, curvature, Weyl, Killing); the parenthesis is removed and the reading stands as the proof''s stated convention. Pin dark-energy.frozen-point-makes-stelle-west-vector 5 -> 6 (formal unchanged byte for byte: notation only).'
  maintainer_pass_gtg_proof:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Proof rewritten in Gauge Theory Gravity with forms as multivector fields (d = grad ^, wedge = outer product of background parts, internal Lie algebra as bivectors of an internal Clifford algebra, trace = internal scalar part): Bianchi D ^ F = 0, <F ^ F> = grad ^ CS and the variation a boundary term. The Hodge star on background two-forms derived as the physical duality read back, *_g F = |det hb|^-1 I G(F) with G = hb hb^T the cometric map (outermorphism on bivectors), so scale-invariant (hb -> lam hb) and rotation-gauge invariant, a function of [g] only, squaring to -1 since G(I G(F)) = det(G) I F; at a corank-one wall G -> G_0 of rank 3 and det hb -> 0, so the star has no limit and |det hb| star -> I G_0 has rank 3 of 6. The answer to the earlier declaration (no pseudoscalar duality at the degenerate point): the duality is written for every invertible field near the wall and its failure is read as a limit. Component formula kept as a labelled reading; orig-proof-main.tex kept. New exact checks: check_gtg_star_free_density_is_a_divergence (su(2) as bivectors of Cl(3,0), exact polynomial fields, abelian and nonabelian, Bianchi, <F ^ F> = grad ^ CS, the 2/3 forced), check_gtg_hodge_star_is_the_cometric_duality (the GA star equals the component star on three fields, one with det hb < 0; the inverse-adjoint formula; star^2 = -1; scale and boost invariance; dependence on [g]), check_gtg_star_has_no_limit_at_a_corank_one_wall (divergence like 1/s and the rank-3 limit I G_0). outside_ga withdrawn: the statement''s forms are read as multivector fields and no stand-in remains in the proof.'
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Declared outside_ga (other) and left in its language: The result is about the Hodge star on two-forms as a function of the metric, *alpha_{ab} = (1/2) sqrt|g| epsilon_{abcd} g^{ce} g^{df} alpha_{ef}, and its failure where the metric degenerates; on bivectors of an invertible field it is multiplication by the pseudoscalar, but the degenerate case it treats has no pseudoscalar duality, so the component form is the content.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: tr(F ^ F) = d CS and the Bianchi identity for polynomial gl(2) connections, the Hodge star depending on the conformal class only, and its degeneration at a corank-one wall. Version 2 -> 3. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    added:
    - dark-energy.frozen-point-makes-stelle-west-vector
    note: 'Added the action theorem, which clause (2) cites for gravity''s action being pre-metric; the
      refutation-record citation is context only. Levels pass: the lay level now restricts the wall to
      a tame corank-one wall, speaks of the standard actions of the other forces, and keeps the formal''s
      open question about actions of a different shape.'
  env: theorem
  context_refs:
  - dark-energy.frozen-point-makes-stelle-west-vector
  outside_pilot_cites:
  - ButlerT12
  - ButlerT17
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-energy.frozen-point-makes-stelle-west-vector
---

## formal
(Shared with the Standard-Model paper \cite{ButlerT12}, which uses it from the internal side.)
\begin{enumerate}
\item Neither of the two routes by which the MacDowell-Mansouri mechanism could extend to an internal factor is open. Contraction with the frozen point produces nothing there: $I$ is a singlet for the internal group and an internal field strength carries no tractor index, so no invariant of the form $\epsilon(I, \cdot, F_i, F_i)$ exists. And the star-free quadratic invariants of an internal field strength, $\int\tr(F_i\wedge F_i)$ for each simple factor, are topological: a boundary term with vanishing interior variation and no field equations. The natural conjecture, that the forces are gauged polynomially as gravity is, fails along both routes: the ninth refutation in the series' record \cite[Table~1, row 9]{ButlerT17}. (Whether some polynomial functional of a different shape could serve is not decided here.)
\item What exists instead are the Yang-Mills functionals $S_i = (1/2g_i^2)\int \tr(F_i \wedge {*}F_i)$, and the Hodge star on two-forms in four dimensions depends on exactly one piece of metric data, the conformal class $[g]$, and is independent of the scale. The internal forces are therefore \emph{conformal-level} objects, defined exactly where the conformal class is nondegenerate, while gravity's action alone is \emph{pre-metric}: polynomial in the connection, the frozen point and the Stelle-West vector, defined across the singular locus (Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(1)).
\item Corollary: at a tame corank-one wall the cometric acquires a radical and the metric a pole (Fact \claimref{dark-energy.imported-walls-sphere-theorem}), so the conformal class degenerates and the star on two-forms, built from two inverse metrics and the volume form, is no longer a nondegenerate map there; the internal actions degenerate with the metric, what crosses is gravity together with the topological $\theta$-terms, the part of each force that survives the singularity.
\end{enumerate}

## technical
The MacDowell-Mansouri mechanism does not extend to an internal gauge factor along either route. The frozen point is an internal singlet and an internal field strength carries no tractor index, so no invariant $\epsilon(I,\cdot,F_i,F_i)$ exists; and the star-free quadratic invariants $\int\tr(F_i\wedge F_i)$ are topological, a boundary term with no field equations. Whether a polynomial functional of some other shape could serve is not decided. What exists instead are the Yang-Mills functionals $(1/2g_i^2)\int\tr(F_i\wedge *F_i)$, and the Hodge star on two-forms in four dimensions depends on the conformal class $[g]$ alone.

So the internal forces are conformal-level objects, defined where the conformal class is nondegenerate, while gravity's action is pre-metric: polynomial in the connection, the frozen point and the Stelle-West vector. At a tame corank-one wall the cometric acquires a radical and the metric a pole, the star on two-forms is no longer a nondegenerate map, and the internal actions degenerate; what crosses is gravity together with the topological $\theta$-terms.

## lay
Gravity's action can be written without ever inverting the metric, but the standard actions of the other forces cannot: they need the Hodge star, which depends on the metric's angles though not its overall scale. The two natural ways of writing the other forces in gravity's style either give nothing or give only a term without dynamics; whether some other kind of action could work is left open. So at a mild (tame) singular wall, where the metric loses one direction and degenerates, the ordinary forces break down with it, while gravity and the topological part of each force carry on across.

## one-liner
Gravity's action is pre-metric while the internal forces' Yang-Mills actions need the conformal class, so at a tame corank-one wall the internal actions degenerate and only gravity and the topological $\theta$-terms cross.
