---
id: synthesis.tangential-derivative-transport-bound
kind: claim
version: 3
title: 'A bound on tangential derivatives of the transport'
status: proved
region: synthesis
subject: interior
tags: [kasner, limits, transport-algorithm]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - interior.transport-level-convergence-along-tangential-curves@4
  - interior.weighted-limit-theorem@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_generators_and_model_bound
- kind: check
  ref: check.py::check_discrete_c1_bound
- kind: check
  ref: check.py::check_bound_terms_needed
- kind: proof
  derivation: main
about:
- obj.interior.weighted-blow-up-hubble-normalisation-admissible
extraction:
  open_problem: op.generic-weighted-limit
  note: >-
    The edge-regularity half of the problem asks for control of tangential derivatives of the
    transport, which T06 names as the only analysis left in the edge problem. The Gronwall bound
    of the tangential convergence theorem extends to first derivatives along any differentiable
    family of tangential curves, with one extra hypothesis: the derivative of the admissibility
    error along the family must tend to zero. For a family that moves the base point in a
    coordinate of the boundary base, which is what regularity of the boundary data needs, this is
    the coordinate derivative of E_tau. Admissibility as defined controls only the size of E_tau;
    the decay clauses do not control this derivative (filed alongside,
    synthesis.admissible-decay-does-not-control-tangential-derivatives, where
    E_tau = tau^{1/2} phi(x/tau) has coordinate derivative tau^{-1/2}). So this is a conditional
    completion: it reduces edge regularity to one decay statement about the coordinate derivative
    of E_tau. Transport-essential in its object (the Hubble-normalised tractor transport),
    standard ODE analysis in its proof. Fix round 2026-10-22-toe: hypothesis restated along the
    family (coordinate normalisation), the Schwarzschild remark dropped, the check strengthened
    with separate constants and tightness controls.
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: admissible metric becomes admissible gravitational field (hb, Omega) on the collar of flat spacetime, and the transport is D-transport of the Hubble-normalised rotation-gauge field; technical and lay wording to match. Bound, hypotheses and conclusion unchanged; check unchanged; proof not in metric language, untouched. Fix (Leon 2026-10-23, referee GR1): displayed connection values re-signed to the GTG sign of the definition, D_a = a.nabla + Omega(a) x (Cartan forms omega^i_0 = sigma_i theta^i assemble to -sigma_i B_i; Hubble-normalised Kasner model -sum_i p_i B_i, DICTIONARY C10); content unchanged. Check: the model generator is now -sum u^i p_i B_i. Check strengthened: per-step Gronwall input ||G_k|| <= 1 + eps asserted and the model bound 1 shown attained at u = |p|; growth factor written once as a module helper; samples moved to module level. Version 2 -> 3.'
---

## formal
Let the gravitational field $(\hb, \Omega)$ on the collar of flat spacetime be admissible (Definition \claimref{obj.interior.weighted-blow-up-hubble-normalisation-admissible}), $K \subset \mathcal{B}$ compact, and $\{\gamma_{y}\}_{|y| < y_{0}}$ a family of tangential curves at time $\tau$ inside $K$, each parametrised by Hubble-normalised arclength on $[0, \lambda]$, with $(y, s) \mapsto \gamma_{y}(s)$ of class $C^{1}$ and unit directions $u_{y}(s)$ differentiable in $y$, $|\partial_{y}u_{y}(s)| \le c_{2}$. Suppose $E_{\tau}$ is $C^{1}$ along $\mathcal{B}$ on $K$, put $\varepsilon := \|E_{\tau}\|_{K}$, and let
\[
\delta \;:=\; \sup_{y,\,s}\bigl\|\partial_{y}\bigl(E_{\tau}(\gamma_{y}(s))[u_{y}(s)]\bigr)\bigr\|
\]
be the derivative of the error along the family. Let $T_{y}$, $T^{0}_{y}$ be the transports along $\gamma_{y}$ of the Hubble-normalised rotation-gauge field (its $D$-transport) and of the Kasner model $-\sum_{i}p_{i}B_{i}\otimes\hat\theta^{i}$ (Theorem \claimref{interior.weighted-limit-theorem}(3)). Then
\[
\bigl\|\partial_{y}T_{y}(\lambda) - \partial_{y}T^{0}_{y}(\lambda)\bigr\| \;\le\; e^{\lambda(1 + \varepsilon)}\bigl(\lambda\,\delta + \varepsilon\,c_{2}\,\lambda^{2}\bigr).
\]
If $\|dE_{\tau}\| \le \varepsilon_{1}$ along unit tangential vectors and $\|\partial_{y}\gamma_{y}\| \le c_{1}$ in Hubble-normalised length, then $\delta \le \varepsilon_{1}c_{1} + \varepsilon c_{2}$. For a coordinate family, in which $y$ moves the base point along a coordinate $x$ of $\mathcal{B}$ with the curves' directions fixed ($c_{2} = 0$), $\delta = \sup_{K}\|\partial_{x}E_{\tau}[u]\|$, the coordinate derivative of the error, and the bound is $\lambda\,\delta\,e^{\lambda(1 + \varepsilon)}$. Consequently, if $\delta(\tau) \to 0$ as $\tau \to 0$, then with Theorem \claimref{interior.transport-level-convergence-along-tangential-curves} $T_{y}(\lambda) \to T^{0}_{y}(\lambda)$ in $C^{1}$ in $y$, uniformly over families with given $\lambda$ and $c_{2}$, and the limiting transport is $C^{1}$ in $y$ with the Kasner model's derivative. The decay clauses of admissibility do not imply $\delta(\tau) \to 0$; the result is conditional on it.

## technical
The tangential convergence theorem compares the transport of the Hubble-normalised connection with the Kasner model's along a single curve at time $\tau$. Edge regularity asks how that comparison varies as the curve moves. Differentiating the two transport equations along a one-parameter family of curves gives a linear equation for the difference of the derivatives, driven by three terms: the error times the model's derivative, the derivative of the error along the family, and the change of the model generator with the curve's direction times the already-controlled difference of the transports. Variation of constants and Gronwall bound it by $e^{\lambda(1+\varepsilon)}(\lambda\delta + \varepsilon c_{2}\lambda^{2})$, where $\varepsilon$ is the size of the admissibility error, $\delta$ the size of its derivative along the family, and $c_{2}$ how fast the curves' directions turn.

For families that move the base point in a coordinate, which is what regularity of the boundary data concerns, $\delta$ is the coordinate derivative of the error. So the derivatives converge whenever that coordinate derivative tends to zero. Admissibility as written does not say this, and its decay clauses cannot: an error that decays while oscillating ever faster has a coordinate derivative that blows up. The remaining edge-regularity question is therefore exactly a decay statement for the coordinate derivative of the error, to be established, or assumed, for the general admissible gravitational field.

## lay
Near the singularity, the framework compares how directions are carried along short paths with how they are carried in a simple model, and an earlier result showed the two agree in the limit. This result asks whether they also agree in how they change when the path is moved sideways. They do, provided the small difference between the true gravitational field and the model changes ever more slowly from place to place as the singularity is approached; if that difference wiggles faster and faster, nothing forces agreement. The question of smoothness at the edge is thereby reduced to one checkable property of that difference.

## one-liner
Along a family of tangential curves, $\|\partial_{y}(T - T^{0})(\lambda)\| \le e^{\lambda(1+\varepsilon)}(\lambda\delta + \varepsilon c_{2}\lambda^{2})$ with $\delta$ the error's derivative along the family, so under the added hypothesis that the coordinate derivative of $E_{\tau}$ tends to zero the transport derivatives converge to the Kasner model's.
