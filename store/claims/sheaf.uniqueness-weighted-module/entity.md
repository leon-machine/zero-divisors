---
id: sheaf.uniqueness-weighted-module
kind: claim
version: 3
title: Uniqueness of the weighted module
status: proved
region: sheaf
subject: walls
tags: [forcing-and-uniqueness, schwarzschild]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
about:
- obj.sheaf.extensions
- obj.sheaf.weighted-coframe-module
derivations:
- name: main
  uses:
  - sheaf.schwarzschild-degeneration-boundary-tame@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_weighted_gram_is_tame_normal_form
- kind: check
  ref: check.py::check_singular_transitions_violate_tameness
locators:
  paper: T04
  number: Thm 8.18
  label: thm:uniqueW
  line: 1053
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the weighted Gram from the PG cometric with det -r, and for six rain-bounded transitions det G_M = (det A)^2 det G_W with tameness exactly when A(0) is invertible. Version 2 -> 3.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: "Kept the Schwarzschild boundary-tameness edge, which supplies the determinant of the weighted Gram."
---

## formal
$\shW$ is the unique rain-bounded extension satisfying (T2$\partial$) and (T3$\partial$).

## technical
Among the extensions of the Schwarzschild cometric module over the blown-up boundary, $\shW$ is the only one that is rain-bounded and satisfies the boundary versions of corank one and first-order degeneration. Rain-boundedness gives $\mathcal{M} \subseteq \shW$; if $A$ is the transition matrix from an $\mathcal{M}$-frame to the $\shW$-frame, then $\det G_{\mathcal{M}} = (\det A)^2 \det G_{\shW} = -(\det A)^2 r$.

If $A$ failed to be invertible at a boundary point, $\det G_{\mathcal{M}}$ would be $o(r)$ there, and since exactly one eigenvalue dies, the dying eigenvalue would be $o(r)$, contradicting first-order degeneration. So $A$ is invertible along the boundary and $\mathcal{M} = \shW$.

## lay
There are several ways to extend the description of the black hole's geometry up to the singularity. This result shows that only one of them stays finite for a freely falling observer and degenerates in the simplest possible way. That extension is the weighted module used throughout.

## one-liner
The weighted module is the unique rain-bounded extension that degenerates at the boundary with corank one and at first order.
