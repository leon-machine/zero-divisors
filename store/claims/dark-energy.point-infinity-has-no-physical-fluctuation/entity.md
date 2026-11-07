---
id: dark-energy.point-infinity-has-no-physical-fluctuation
kind: claim
version: 4
title: 'The point at infinity has no physical fluctuation: the $(I,V)$-sector is pure gauge'
status: proved
region: dark-energy
subject: dark-energy
tags: [frozen-point, mode-counting, quantum-gravity]
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
derivations:
- name: main
  uses:
  - dark-energy.frozen-point-makes-stelle-west-vector@7
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T10.py
  tags:
  - label:prop:goldstone
- kind: check
  ref: check.py::check_constrained_fluctuations_nine
- kind: check
  ref: check.py::check_broken_generators_act_bijectively
- kind: check
  ref: check.py::check_integrand_invariant_under_ambient_group
- kind: check
  ref: check.py::check_fluctuation_is_gauge_on_de_sitter_field
locators:
  paper: T10
  number: Prop 5.4
  label: prop:goldstone
  line: 991
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the 9-dimensional constrained fluctuation space, 9 broken generators acting onto it, invariance of eps(I, V, F, F), and a dV fluctuation absorbed by the soldering frame on the de Sitter field. Version 3 -> 4.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the connection argument of the functional is the tractor gauge field on flat spacetime and the soldering form the physical frame hb^{-1}; counting and claim unchanged.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  typing:
    by: ai-typing-pass
    note: 'Kept the single premise, the action theorem, used in the proof; the Stelle-West lemma is cited
      only for the canonical solution, which the proposition does not use, and the lift assembly is a
      forward pointer. Levels pass: the lay and one-liner now say the result holds within the action''s
      own variational principle, and the lay keeps the assembly-level clause of the MacDowell-Mansouri
      identification.'
  env: proposition
  context_refs:
  - dark-energy.lift-inherits-no-go-steps-itemised
  - dark-energy.stelle-west-vector-frozen-point
  unresolved_refs:
  - rem:weakness
---

## formal
Take the functional in its three-argument form, $S[\nabla, I, V] \sim Q(I)^{-1}\int\epsilon(I, V, F, F)$, with $\nabla$ the tractor connection, on flat spacetime the $\Cl(2,4)$ gauge field $\Omega_{T}$ of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection} (its curvature $F$ the field strength of $\Omega_{T}$), and $I$ and $V$ independent sections subject to the Stelle-West constraints $Q(I) = \Lambda/3$, $\ip{V}{I} = 0$, $Q(V) = -3/\Lambda$; Lemma \claimref{dark-energy.stelle-west-vector-frozen-point} exhibits $V = X - (3/\Lambda)I$ as the canonical solution of the constraints on the Einstein region, but inside the variational principle $V$ is a field, since the canonical tractor $X$ is a fixed section and a transformation acting on $\nabla$ and $I$ alone is not a symmetry of a functional that contains $X$. Then: the constrained fluctuation space of $(I, V)$ has dimension $9$ (twelve components less three independent linearised constraints; it fibres over the five tangential directions of $I$ with four-dimensional affine fibres of $\delta V$, and is not a direct sum); the stabiliser of the pair $(I, V)$ in $SO(2,4)$ is the Lorentz group of $\{I,V\}^\perp$, of dimension six, so the broken generators number $15 - 6 = 9$; and the infinitesimal action $\xi \mapsto (\xi\cdot I, \xi\cdot V)$ of the broken generators onto the constrained fluctuation space is bijective. Unitary gauge $\delta I = \delta V = 0$ therefore exists and is complete: every fluctuation of the pair is a gauge transformation, the eaten Goldstone modes reappearing as the frame freedom of the soldering form (the physical frame $\hb^{-1}(a)$ of the gravitational field, up to rotation gauge), the Stelle-West mechanism read in reverse. In unitary gauge the second variation of the action has legs only on the connection: the graviton carries no $(\delta I, \delta V)$ polarisation. This closes open item (ii) of Remark \ref{rem:weakness} within the action's own variational principle; the four-dimensional lift of the s-wave no-go is the task of Assembly \claimref{dark-energy.lift-inherits-no-go-steps-itemised}, not of this proposition. \emph{Level:} the counting, the bijectivity, and the invariance of the integrand $\epsilon(I,V,F,F)$ under the ambient group acting on all three arguments are proved outright below; that the functional so gauge-fixed is the MacDowell-Mansouri functional is Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}(ii)-(iii), with its assembly-level clause.

## technical
In the three-argument functional $S[\nabla,I,V] \sim Q(I)^{-1}\int\epsilon(I,V,F,F)$, with $\nabla$ the tractor connection, on flat spacetime the $\Cl(2,4)$ gauge field built from gravity's fields, with $I$ and $V$ independent fields subject to $Q(I) = \Lambda/3$, $\langle V,I\rangle = 0$ and $Q(V) = -3/\Lambda$, the constrained fluctuation space of $(I,V)$ has dimension $12 - 3 = 9$. The stabiliser of the pair in $SO(2,4)$ is the Lorentz group of $\{I,V\}^\perp$, of dimension six, so there are $15 - 6 = 9$ broken generators, and $\xi\mapsto(\xi\cdot I, \xi\cdot V)$ maps them bijectively onto the constrained fluctuations.

Hence unitary gauge $\delta I = \delta V = 0$ exists and is complete: every fluctuation of the pair is a gauge transformation, the Goldstone modes reappearing as the frame freedom of the soldering form, and the second variation has legs only on the connection. The counting, the bijectivity and the invariance of the integrand are proved outright; that the gauge-fixed functional is the MacDowell-Mansouri one carries the assembly-level clause of that identification.

## lay
Gravity's action here, written for gauge fields on flat spacetime, contains two fixed-length vectors tied to the point at infinity. One might worry that their wobbles are extra physical fields to which matter could couple. This result counts the possible wobbles and the broken symmetries, finds nine of each, and shows they match one to one, so every wobble can be undone by a symmetry. The graviton therefore carries no extra polarisation from this sector. This holds within the action's own variational principle, with both vectors treated as fields held to their fixed lengths; that the action so fixed is the known MacDowell-Mansouri one rests on the earlier theorem's assembly-level step.

## one-liner
Within the three-argument variational principle, the constrained fluctuations of $(I,V)$ and the broken generators of $SO(2,4)$ both number nine and correspond bijectively, so the $(I,V)$-sector is pure gauge and the graviton has no $(\delta I,\delta V)$ polarisation.
