---
id: interior.transport-level-convergence-along-tangential-curves
kind: claim
version: 4
title: Transport-level convergence along tangential curves, all admissible gravitational fields
status: proved
region: interior
subject: interior
tags: [kasner, limits]
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
about:
- obj.interior.weighted-blow-up-hubble-normalisation-admissible
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:5.11
- kind: check
  ref: check.py::check_variation_of_constants_identity
- kind: check
  ref: check.py::check_model_generator_bounded_by_one
locators:
  paper: T06
  number: Thm 5.11
  label: thm:duhamel
  line: 730
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the variation-of-constants identity by exact power series and the bound ||H|| <= 1 on the Kasner circle. Version 2 -> 3. Sample inputs moved to module level; no change to what is tested. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    note: 'The proof uses only the admissibility definition, recorded in about; no uses edges are needed.'
  env: theorem
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: admissible metric becomes admissible gravitational field (hb, Omega) on the collar of flat spacetime (the definition object now defines admissibility for the field), and the transport is D-transport; title adjusted to match. Bound unchanged; proof not in metric language, untouched.'
---

## formal
Let the gravitational field $(\hb, \Omega)$ on the collar be admissible (Definition \claimref{obj.interior.weighted-blow-up-hubble-normalisation-admissible}), $K \subset \mathcal{B}$ compact, and $\gamma$ a tangential curve at time $\tau$ inside $K$ of Hubble-normalised length $\lambda$, with $T_\gamma$ its $D$-transport and $T^0_\gamma$ that of the Kasner model. Then
\[
\|T_{\gamma}(\lambda) - T^{0}_{\gamma}(\lambda)\| \;\le\; \lambda\, \|E_{\tau}\|_{K}\; \exp\bigl(\lambda\,(1 + \|E_{\tau}\|_{K})\bigr),
\qquad \|E_{\tau}\|_{K} := \sup_{K}\|E_{\tau}\| ,
\]
which tends to zero as $\tau \to 0$, uniformly over all such curves of length at most $\lambda$. No control of the model transport's conjugation of the error is used.

## technical
Let the gravitational field on the collar of flat spacetime be admissible, $K$ a compact subset of the boundary base, and $\gamma$ a tangential curve at time $\tau$ inside $K$ with Hubble-normalised length $\lambda$. The transport $T_\gamma$ by the covariant derivative $D$ and the Kasner model's transport $T^0_\gamma$ satisfy $\|T_\gamma(\lambda) - T^0_\gamma(\lambda)\| \leq \lambda\|E_\tau\|_K \exp(\lambda(1 + \|E_\tau\|_K))$, where $\|E_\tau\|_K$ is the supremum over $K$ of the admissibility error. This tends to zero as $\tau \to 0$, uniformly over all such curves of length at most $\lambda$.

The bound comes from the variation-of-constants identity and Gronwall's inequality, with the model generator bounded by one on unit directions through $\sum_i p_i^2 = 1$; no control of the model transport's conjugation of the error is used.

## lay
Near a singularity of the admissible kind, one can compare how directions are carried along a short path by the real gravitational field with how they would be carried in the idealised Kasner model. This result gives an explicit bound on the difference for every such path, measured in the natural rescaled units. The bound shrinks to zero at the singularity, so the two descriptions agree in the limit.

## one-liner
For every admissible gravitational field, transport along any tangential curve of fixed Hubble-normalised length converges to the Kasner model's transport, with an explicit Gronwall bound in $\|E_\tau\|_K$.
