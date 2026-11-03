---
id: pairing.pairing-class-transverse-derivative-null-direction
kind: claim
version: 4
title: The pairing class is the transverse derivative of the null direction
status: proved
region: pairing
subject: thermality
tags: [pairing-and-bogoliubov, null-directions]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-pairing, the series'' standard disclaimer'
review: typed
about:
- obj.pairing.pairing-class-transport
derivations:
- name: main
  uses:
  - pairing.stabiliser-parabolic-algebra-null-direction@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_omega_reproduces_the_connection
- kind: check
  ref: check.py::check_pairing_class_is_transverse_derivative
- kind: check
  ref: check.py::check_class_scales_with_the_null_direction
- kind: check
  ref: check.py::check_real_directions_parallel_exactly_when_class_vanishes
locators:
  paper: T05-pairing
  number: Prop 4.2
  label: prop:transport
  line: 291
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Omega reproducing nabla, pv(Omega(X)) = <nabla_X l, m> in the static Schwarzschild frame, the rescaling law, and the real-direction equivalence. Version 2 -> 3. check_real_directions_parallel_exactly_when_class_vanishes: added four random metric-compatible connections to the real-direction equivalence (fix round 2026-10-23). Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - pairing.stabiliser-parabolic-algebra-null-direction
    - obj.pairing.pairing-class-transport
    note: 'Added the stabiliser proposition, whose characterisation of the vanishing class (B.l in span{l,
      m}) the real-direction clause uses; this propagates that premise''s unsupported status. Levels pass:
      conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - pairing.stabiliser-parabolic-algebra-null-direction
---

## formal
For every direction $X$,
\[
\pv(\Omega(X)) \;=\; \ip{\nabla_{X}\ell}{m},
\]
and under a rescaling $\ell \mapsto \lambda\ell$ of the null direction by a function the class scales by $\lambda$, so its vanishing locus is a property of the null direction field and not of its normalisation. For a real direction $X$ the vacuum is parallel along $X$ exactly when the null direction is, $\nabla_{X}\ell \propto \ell$.

## technical
Since $\nabla_X \ell = \tfrac12[\Omega(X), \ell] = \Omega(X)\cdot\ell$, the pairing class of the transport along any direction $X$ is the transverse component of the derivative of the null direction, $\pv(\Omega(X)) = \ip{\nabla_X \ell}{m}$. Rescaling $\ell \mapsto \lambda\ell$ by a function multiplies the class by $\lambda$, because the extra term $(X\lambda)\ell$ is orthogonal to $m$; so where the class vanishes is a property of the null direction field, not of its normalisation.

For a real direction $X$, a vanishing class puts $\nabla_X\ell$ in $\operatorname{span}\{\ell, m\}$, and being real it is then a multiple of $\ell$: the vacuum is parallel along $X$ exactly when the null direction is, $\nabla_X\ell \propto \ell$.

## lay
How much moving in a given direction disturbs the fermion vacuum is measured by how much the vacuum's light-like direction tilts sideways along that move. Rescaling that direction changes the size of the effect but not where it vanishes. Along real directions, the vacuum stays put exactly when its light-like direction stays put.

## one-liner
The pairing class of the transport along $X$ equals the transverse derivative of the null direction, $\pv(\Omega(X)) = \ip{\nabla_X\ell}{m}$; it scales with the normalisation of $\ell$, and along a real $X$ it vanishes exactly when $\nabla_X\ell \propto \ell$.
