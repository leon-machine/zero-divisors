---
id: interior.covariant-form-vacuum-equations
kind: claim
version: 5
title: Covariant form of the vacuum equations
status: proved
region: interior
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
  source: authorship disclosure of T06, deposited version
review: typed
derivations:
- name: main
  uses:
  - interior.imported-equivalence-einstein-equations@2
  - interior.imported-tractor-connection@2
  - interior.metric-parallelism-trace-schouten-condition@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:4.5
- kind: check
  ref: check.py::check_derivative_of_the_scale_tractor_is_minus_schouten
- kind: check
  ref: check.py::check_parallel_iff_vacuum
- kind: check
  ref: check.py::check_parallel_null_tractor_without_field_equations
- kind: check
  ref: check.py::check_structure_algebra_so24
locators:
  paper: T06
  number: Thm 4.5
  label: thm:parallel
  line: 510
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: in GTG (jet engine, store-sign curvature from hb and Omega) the Cl(2,4) tractor gauge field gives D^T ninf = -P on Schwarzschild (static and PG), SdS, RN and de Sitter; ninf parallel exactly on the Ricci-flat fields; a parallel null tractor on flat-sliced de Sitter without the field equations; so(2,4) closure. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: g is the derived metric of a gravitational field on flat spacetime and M-circ its invertible region; the tractor connection is named as the flat-space Cl(2,4) gauge field of the tractor theorem, the index display kept as its reading. Proof prefixed with the GTG reading sentence.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: theorem
  eqrefs: 1
  typing:
    by: ai-typing-pass
    note: 'All three uses are genuine premises: the tractor connection formula, part (ii) of the Schouten
      lemma, and the GTG-Einstein equivalence. Levels pass: the lay now restricts the statement to the
      interior region, as the formal does.'
---

## formal
Let $g$ be the derived metric of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) on its invertible region $M^\circ$, and let $I_g := (1, 0, 0) = \nInf$ be the pure-scale section of $\mathcal{T}$ in the scale $g$. For the tractor connection, which in Gauge Theory Gravity is the $\Cl(2,4)$ rotation-gauge field $D^{T}_{a} = a \cdot \nabla + \Omega_{T}(a)\times$, $\Omega_{T}(a) = \Omega(a) - \nInf \wedge \hb^{-1}(a) + \nO \wedge \Sch(\hb^{-1}(a))$, acting on tractors $\sigma\nInf + \mu + \rho\nO$ (Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}), with slots in the splitting of $g$,
\[
\nabla_a I_g = \bigl(0,\; -\Sch_{ab},\; 0\bigr), \qquad\text{that is}\qquad D^{T}_{a}\nInf = -\Sch\bigl(\hb^{-1}(a)\bigr),
\]
so $I_g$ is parallel if and only if $\Sch = 0$, if and only if $g$ is Ricci-flat, if and only if (Fact \claimref{interior.imported-equivalence-einstein-equations}) the GTG vacuum field equations hold. Moreover $Q(I_g) = 0$: the section is null. Hence the vacuum field equations on $M^\circ$ are exactly equivalent to the parallelism of the scale tractor $I_g$ attached to $g$: the ideal point of the fibre quadric that the physical scale distinguishes is covariantly constant. (Existence of \emph{some} parallel null tractor is the strictly weaker, conformally invariant statement that $[g]$ is almost Ricci-flat: it carries an almost-Einstein scale which is Ricci-flat away from that scale's zero set, and the zero set may be non-empty. A non-constant rescaling $e^{2\omega}g$ already keeps the parallel section while losing the field equations.) The statement is covariant under the gauge transformations of $\mathcal{T}$, whose structure algebra is $\mathfrak{so}(2,4)$ acting through the bivectors of $\Cl(2,4)$.

## technical
Let $g$ be the derived metric of a gravitational field on flat spacetime, on its invertible region $\Mo$, and $I_g = (1,0,0) = \nInf$ its pure-scale tractor. The tractor connection, which on flat spacetime is the $\Cl(2,4)$ gauge field $\Omega_{T}$ built from $\Omega$, the frame $\hb^{-1}$ and the Schouten map, gives $\nabla_a I_g = (0,\, -\Sch_{ab},\, 0)$, so $I_g$ is parallel exactly when $\Sch = 0$, which holds exactly when $g$ is Ricci-flat, which is equivalent to the GTG vacuum field equations. The section is null, $Q(I_g) = 0$.

So the vacuum field equations on $\Mo$ are equivalent to parallelism of the scale tractor attached to $g$. The existence of some parallel null tractor is strictly weaker: it says only that $[g]$ is almost Ricci-flat, and a non-constant rescaling $e^{2\omega}g$ keeps a parallel section while losing the field equations. The statement is covariant under the gauge transformations of $\mathcal{T}$, whose structure algebra $\mathfrak{so}(2,4)$ acts through the bivectors of $\Cl(2,4)$.

## lay
In the interior region, Einstein's equations for empty space can be recast as a single condition on the gravitational fields: a particular marker in the six-dimensional conformal extension of spacetime, attached to the physical scale, must stay constant as it is carried from point to point by a gauge field built from gravity. This result proves that the two formulations are exactly equivalent, and that the marker is a null (lightlike) object. It also notes that merely having some constant marker of this kind is a weaker condition that does not by itself give the field equations.

## one-liner
On the invertible region of a gravitational field on flat spacetime, the vacuum field equations hold exactly when the null scale tractor $\nInf$ of the derived metric is parallel for the tractor gauge field $\Omega_{T}$.
