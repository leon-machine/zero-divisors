---
id: synthesis.admissible-decay-does-not-control-tangential-derivatives
kind: claim
version: 1
title: 'Admissible decay does not control tangential derivatives'
status: proved
region: synthesis
subject: interior
tags: [limits, kasner, no-go]
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
about:
- obj.interior.weighted-blow-up-hubble-normalisation-admissible
derivations:
- name: main
  uses:
  - interior.transport-level-convergence-along-tangential-curves@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_tangential_derivative_not_controlled
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - interior.transport-level-convergence-along-tangential-curves
extraction:
  open_problem: op.generic-weighted-limit
  note: >-
    Bears on the edge-regularity half of the problem. The transport-level convergence theorem uses only the
    decay clauses of admissibility; this shows those clauses, with the Kasner constraint, are compatible with
    a tangential derivative of the transport that diverges (like tau^(-3/2) in the coordinate, tau^(-1/2-p_j) in Hubble-normalised length, for every Kasner exponent p_j) while the transport itself converges. Filed alongside, synthesis.tangential-derivative-transport-bound, which proves the conditional C^1 bound in the Hubble-normalised derivative; this example shows its hypothesis on that derivative is not implied by the decay clauses. So
    a tangential-derivative bound for the admissible class needs either the Einstein clause or an added hypothesis
    on the tangential derivative of E_tau (under which the Gronwall argument extends to first derivatives). The
    family is an abstract error field, not claimed to arise from any metric, Einstein or not; whether the Einstein clause supplies the bound is left
    open. Signature convention: B_2 = e_0 e_2 squares to one in (-,+,+,+) and in the store's (+,-,-,-) alike. Transport-essential in the sense that the object controlled is the transport itself.
---

## formal
Fix a patch of $\mathcal{B}$ with a coordinate $x$ and constants $p_{i} \neq 0$, $\sum_{i} p_{i}^{2} = 1$, and put
\[
E_{\tau} \;=\; a_{\tau}(x)\,B_{2}\otimes\hat\theta^{2}, \qquad a_{\tau}(x) \;=\; \tau^{1/2}\,\varphi(x/\tau^{2}), \qquad \varphi(y) = \frac{y}{1 + y^{2}} .
\]
Then $E_{\tau}$ satisfies every decay clause of Definition \claimref{obj.interior.weighted-blow-up-hubble-normalisation-admissible}: $\sup_{x}\|E_{\tau}\| = \tfrac12\tau^{1/2} \to 0$ and $\int_{0}^{\tau_{0}}\sup_{x}\|E_{\tau}\|\,d\tau/\tau = \tau_{0}^{1/2} < \infty$, uniformly in $x$. Yet the coordinate derivative is $\partial_{x}a_{\tau}(0) = \tau^{-3/2}$, and the derivative along the unit vector of the axis $j$ of $x$, in Hubble-normalised length (the coordinate derivative times $\tau^{1 - p_{j}}$), is $\tau^{-1/2 - p_{j}}$, which diverges for every Kasner exponent, since $p_{j} \geq -\tfrac13$. Along the $\hat\theta^{2}$-curve of Hubble-normalised length $\lambda$ through the point $x$ the transport $T(x) = \exp\bigl(\lambda(p_{2} + a_{\tau}(x))B_{2}\bigr)$ converges to the model transport as Theorem \claimref{interior.transport-level-convergence-along-tangential-curves} says, while its tangential derivative obeys $\|\partial_{x}T(0)\| \geq \lambda\,\tau^{-3/2}$ in the coordinate normalisation and $\geq \lambda\,\tau^{-1/2 - p_{j}}$ in the Hubble-normalised one, both tending to infinity. Hence no bound on first tangential derivatives of $E_{\tau}$ or of the transport, uniform as $\tau \to 0$, follows from the decay clauses and the Kasner constraint: a tangential-derivative bound for the admissible class must use the Einstein clause or an added hypothesis on $\partial_{x}E_{\tau}$.

## technical
The weighted limit's error term is only required to shrink, and to shrink fast enough that its size divided by $\tau$ is integrable. Those conditions say nothing about how fast it may oscillate across the boundary. The example $a_{\tau}(x) = \tau^{1/2}\varphi(x/\tau^{2})$, with $\varphi(y) = y/(1 + y^{2})$ bounded by one half, satisfies both conditions uniformly, but its slope at $x = 0$ is $\tau^{-3/2}$ in the coordinate, and $\tau^{-1/2 - p_{j}}$ along unit vectors in Hubble-normalised length, which blows up whatever the Kasner exponent of that axis. Feeding it into the transport along a fixed boost direction, the transport converges, as the existing theorem guarantees, while its derivative across the boundary diverges in either normalisation. So edge regularity cannot be proved from the decay hypotheses: either the Einstein condition must be used or a hypothesis on derivatives of the error must be added.

## lay
Near the singularity the series compares the true geometry with a simple model and requires the difference to die away. Dying away, though, does not stop the difference from wiggling ever faster from place to place. An explicit example shows this: the difference fades, the model's predictions along each path still come out right, but the rate at which they change from one path to its neighbour grows without limit. So the remaining smoothness question cannot be settled from the fading condition alone; it needs Einstein's equations themselves, or a further assumption.

## one-liner
$E_{\tau} = \tau^{1/2}\varphi(x/\tau^{2})B_{2}\otimes\hat\theta^{2}$, $\varphi(y) = y/(1 + y^{2})$, meets every decay clause of admissibility while the tangential derivative of the transport diverges ($\geq \lambda\tau^{-3/2}$ in the coordinate, $\geq \lambda\tau^{-1/2 - p_{j}}$ in Hubble-normalised length), so a tangential-derivative bound must use the Einstein clause or an added hypothesis on $\partial_{x}E_{\tau}$.
