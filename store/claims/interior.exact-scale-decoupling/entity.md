---
id: interior.exact-scale-decoupling
kind: claim
version: 5
title: Exact scale decoupling
status: proved
region: interior
subject: einstein
tags:
- schwarzschild
- curvature-and-field-equations
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
  role: 'consistency pass, the curvature operator written with its stored symbol, script R, in place of R'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - interior.imported-schwarzschild-curvature-spectrum@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:3.3
- kind: check
  ref: check.py::check_shape_operator_algebra
- kind: check
  ref: check.py::check_factorisation_at_every_radius
locators:
  paper: T06
  number: Prop 3.3
  label: prop:shape
  line: 403
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The factorised operator was written R(B), the stored symbol for the background field strength in the literature sign; its values (+2M/r^3 on the radial pair, -M/r^3 on the mixed planes) are those of the store-sign curvature operator, now written with that symbol; the stale paper reference Section sec:setting is replaced by the store sign.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: S = -(B + 3 sigma_r B sigma_r)/2 = 1 - 3 Pi, S^2 + S = 2, eigenspaces 2 and 4, trace 0; calR = -(M/r^3) S from the Schwarzschild gauge fields at eight (M, r) samples in the static and PG gauges, inside the horizon too. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    note: The single use, the imported curvature spectrum, is a genuine premise; the paper notes the classic 2:1
      tidal structure but does not say the operator identity itself is obtained classically, so no standard-route
      was added.
  env: proposition
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: crossover-scan
    note: Linked by specialises to T05 Thm 6.1, which states the same operator identity R = -(M/r^3) S, S = 1 -
      3 Pi, S^2 + S = 2, spectrum (-2,-2,1,1,1,1), and adds the radial plane's invariance under the gauge field,
      the sign convention, and that the doubled eigenvalue sits exactly on {sigma_r, I sigma_r}. Found unlinked
      across subjects (einstein, singularity) by the crossover scan of 21 October; not merged, since T05's statement
      is strictly stronger.
specialises:
- singularity.curvature-gauge-field-exact-shape-decoupling@4
---

## formal
In the conventions of Fact \claimref{interior.imported-schwarzschild-curvature-spectrum}, the Schwarzschild curvature operator is, exactly and at every radius,
\[
\mathcal{R}(B) \;=\; -\,\frac{M}{r^3}\,S(B), \qquad
S \;:=\; 1 - 3\Pi \;=\; -\tfrac12\bigl(B \mapsto B + 3\,\sigma_r B \sigma_r\bigr),
\]
where the shape operator $S$ satisfies the algebraic identity
\[
S^2 + S = 2 ,
\]
has spectrum $(-2, -2, 1, 1, 1, 1)$, and is trace-free. The factorisation is exact: $S$ depends on neither $M$ nor $r$, and the entire approach to the singularity changes only the conformal prefactor $-M/r^3$.

## technical
Let $\Pi$ project the six-dimensional bivector space onto the pair $\operatorname{span}\{\sigma_r, I\sigma_r\}$ formed by the radial boost plane and its dual. Given the imported Schwarzschild spectrum, the curvature operator factorises exactly, at every radius, as $\mathcal{R}(B) = -\frac{M}{r^3}\,S(B)$ with $S = 1 - 3\Pi = -\tfrac12(B \mapsto B + 3\,\sigma_r B\sigma_r)$.

The shape operator obeys $S^2 + S = 2$, has spectrum $(-2,-2,1,1,1,1)$ and is trace-free. It depends on neither $M$ nor $r$, so the whole approach to the singularity changes only the conformal prefactor $-M/r^3$. The singularity paper proves the same identity in its Theorem on the curvature of the gauge field (\claimref{singularity.curvature-gauge-field-exact-shape-decoupling}), adding that the doubled eigenvalue sits exactly on the radial boost plane and its dual.

## lay
Near a Schwarzschild black hole the tidal curvature has a fixed pattern: stretching in one pair of directions and squeezing in the others, in a two-to-one ratio. This result shows the pattern is exactly the same at every radius, all the way in towards the singularity. Only its overall strength, which grows like the inverse cube of the radius, changes.

## one-liner
The Schwarzschild curvature operator is exactly $-(M/r^3)\,S$ with a fixed, trace-free shape operator $S$ satisfying $S^2 + S = 2$, so only the scale changes on the approach to the singularity.
