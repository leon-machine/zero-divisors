---
id: transport.minimality
kind: claim
version: 4
title: Minimality
status: proved
region: transport
subject: completion
tags: [transport-algorithm, hyperbolic-plane, forcing-and-uniqueness]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
review: typed
about:
- obj.transport.null-lift-completion
derivations:
- name: main
  uses:
  - std-algebra.witt-decomposition@1
  - std-algebra.sylvester-inertia@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_hyperbolic_plane_completion_in_every_signature
- kind: check
  ref: check.py::check_null_vector_forces_both_signs
- kind: check
  ref: check.py::check_two_dimensional_w_is_hyperbolic_plane
- kind: check
  ref: check.py::check_mixed_signature_second_route
locators:
  paper: T01
  number: Thm 4.13
  label: thm:minimality
  line: 929
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.witt-decomposition, std-algebra.sylvester-inertia where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: hyperbolic-plane completion in 14 signatures, a null vector forces both signs, two-dimensional W is the hyperbolic plane, and the mixed-signature route. Version 2 -> 3.'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'No claim premises (the proof uses classical facts about quadratic spaces from Lam and the definition of a null-lift completion); the paper presents the result as new, so there is no standard route.'
---

## formal
Let $(\mathbb{W}, f)$ be any null-lift completion of $(\mathbb{V}, Q)$. Then $\mathbb{W}$ contains at least one direction of positive square and one of negative square; in particular $\dim \mathbb{W} \geq 2$, and enlargements of signature increment $(+k, 0)$ or $(0, +k)$ are excluded for every $k$. A single hyperbolic plane suffices, and any two-dimensional $\mathbb{W}$ admitted by the definition is a hyperbolic plane; hence the minimal completion is
\[
\Cl(p,q) \;\longrightarrow\; \Cl(p{+}1, q{+}1),
\]
with the adjoined space unique up to isometry, and the signature increment is $(+1,+1)$ in every signature.

## technical
A null-lift completion of $(\mathbb{V}, Q)$ is a nondegenerate quadratic space $\mathbb{W}$ adjoined orthogonally, with a map $f : \mathbb{V} \to \mathbb{W}$, $f(0) \neq 0$, such that $X(x) = f(x) + x$ is null for every $x$. For any such completion, $\mathbb{W}$ contains a direction of positive square and one of negative square, so $\dim \mathbb{W} \geq 2$ and enlargements of increment $(+k, 0)$ or $(0, +k)$ are excluded for every $k$.

A single hyperbolic plane suffices, and any two-dimensional admissible $\mathbb{W}$ is a hyperbolic plane. Hence the minimal completion is $\Cl(p,q) \to \Cl(p{+}1,q{+}1)$, with the adjoined space unique up to isometry and increment $(+1,+1)$ in every signature.

## lay
To make the reciprocal work everywhere, the series represents each point as a light-like direction in a larger space. This result asks how much larger that space has to be. The added part must contain at least one direction of positive square and one of negative square, so adding only space-like or only time-like directions never works, while one such pair is enough and is essentially unique.

## one-liner
Every null-lift completion adjoins directions of both signs, so the minimal completion is the hyperbolic-plane ascent $\Cl(p,q) \to \Cl(p{+}1,q{+}1)$, unique up to isometry, with increment $(+1,+1)$.
