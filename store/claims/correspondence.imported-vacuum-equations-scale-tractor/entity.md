---
id: correspondence.imported-vacuum-equations-scale-tractor
kind: claim
version: 6
title: 'Imported: the vacuum equations and the scale tractor'
status: proved
region: correspondence
subject: einstein
tags: [tractors, curvature-and-field-equations]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
derivations:
- name: main
  uses:
  - interior.covariant-form-vacuum-equations@5
  - interior.scale-tractor-leaves-cone@8
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_vacuum_iff_null_scale_tractor_parallel
- kind: check
  ref: check.py::check_einstein_scale_tractor_parallel_with_norm
- kind: check
  ref: check.py::check_parallel_section_forces_einstein_lambda_six_rho
locators:
  paper: T09
  number: Fact 4.7
  label: fact:vacuumT6
  line: 562
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: from curvature operators by contraction: Lambda = 0 vacuum iff ninf parallel; on Einstein fields I_g = ninf + (J/4) n0 parallel with Q = Lambda/3; a parallel (1, 0, rho) forces rho constant and Lambda = 6 rho. Version 4 -> 5. The formal level restated: Fix round 2026-10-23: ''the null scale tractor'' reworded, since Q(I_g) = Lambda/3 makes I_g null exactly when Lambda = 0. Version 5 -> 6. The technical level restated: Fix round 2026-10-23: ''the null scale tractor'' reworded, since Q(I_g) = Lambda/3 makes I_g null exactly when Lambda = 0.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the region is the invertible region of a gravitational field on flat spacetime, g its derived metric, the scale tractor the Cl(2,4) vector ninf + rho_g n0 and the connection the tractor gauge field; content unchanged.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  typing:
    by: ai-typing-pass
    note: 'Both restated series results are genuine sources (the Lambda = 0 theorem and the Lambda != 0 theorem); no standard route recorded since the paper gives none at this fact.'
  env: fact
  context_refs:
  - interior.covariant-form-vacuum-equations
  - interior.scale-tractor-leaves-cone
  flags:
  - 'fact restating several series results: derived from them'
---

## formal
Let $g$ be the derived metric of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). On the region where $\hb$ is invertible, the vacuum field equations are exactly equivalent to the covariant constancy, for the tractor connection, which in Gauge Theory Gravity is the $\Cl(2,4)$ rotation-gauge field $D^{T}_{a} = a \cdot \nabla + \Omega_{T}(a)\times$, $\Omega_{T}(a) = \Omega(a) - \nInf \wedge \hb^{-1}(a) + \nO \wedge \Sch(\hb^{-1}(a))$, acting on tractors $\sigma\nInf + \mu + \rho\nO$ (Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}), of the scale tractor $I_g$, null exactly when $\Lambda = 0$; the scale tractor of a scale $g$ is the section $I_g = (1, 0, \rho_g) = \nInf + \rho_g\nO$ in the splitting of that scale, with $\rho_g$ fixed by the scalar curvature of $g$; for an Einstein metric with $\mathrm{Ric} = \Lambda g$ (field strength $\mathcal{R}(a) = \Lambda a$) it is parallel with squared norm $Q(I_g) = \Lambda/3$, and conversely a parallel section of the form $(1,0,\rho)$ forces $\rho$ constant and $g$ Einstein with $\Lambda = 6\rho$. \emph{Provenance:} \cite[Thm.~4.5, Thm.~4.7]{ButlerT6}.

## technical
Where the position-gauge field $\hb$ is invertible, the vacuum field equations are exactly equivalent to $D^{T} I_g = 0$ for the scale tractor of the physical scale (null exactly when $\Lambda = 0$), $D^{T}$ being the tractor connection, which on flat spacetime is the $\Cl(2,4)$ gauge field built from $\Omega$, the frame and the Schouten map. The scale tractor of a scale $g$ is $I_g = (1, 0, \rho_g) = \nInf + \rho_g\nO$ in the splitting of that scale, with $\rho_g$ fixed by the scalar curvature of $g$.

For an Einstein field with $\mathrm{Ric} = \Lambda g$ the scale tractor is parallel with $Q(I_g) = \Lambda/3$; conversely a parallel section of the form $(1, 0, \rho)$ forces $\rho$ constant and $g$ Einstein with $\Lambda = 6\rho$. The entry restates the series' covariant vacuum theorem and its cosmological-constant companion.

## lay
Einstein's vacuum equations can be rewritten as the statement that one vector of the six-dimensional conformal model, attached to the choice of scale, does not change as the gravitational gauge fields carry it across flat spacetime. With a cosmological constant the same holds, and the squared length of that vector is a third of the constant. This entry restates both results from earlier in the series.

## one-liner
On the invertible region of a gravitational field on flat spacetime the vacuum equations are the parallelism of the scale tractor for the tractor gauge field, and a parallel section $(1, 0, \rho)$ is exactly an Einstein scale with $\Lambda = 6\rho$ and squared norm $\Lambda/3$.
