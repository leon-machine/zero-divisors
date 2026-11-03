---
id: transport.density
kind: claim
version: 3
title: Density
status: proved
region: transport
subject: completion
tags: [conformal-model]
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
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_non_ideal_null_rays_are_lifts
- kind: check
  ref: check.py::check_invertible_points_dense_in_v
- kind: check
  ref: check.py::check_ideal_points_are_limits_of_lifted_invertible_points
- kind: check
  ref: check.py::check_point_at_infinity_is_limit
locators:
  paper: T01
  number: Lem 4.9
  label: lem:density
  line: 855
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: non-ideal null rays are lifts, invertible points accumulate, and the explicit paths to ideal points with exact O(1/s) remainders. Version 1 -> 2. Check strengthened: exact O(1/s) remainder s (rep - ninf) = (2/Q(a)) (a + n0/s) asserted at each sample s; samples moved to module level. Version 2 -> 3.'
  env: lemma
  eqrefs: 1
  typing:
    by: ai-typing-pass
    note: 'No premises; the paper calls the conformal model section containing this lemma standard (Hestenes and coworkers, Dorst-Fontijne-Mann, Doran-Lasenby), but no imported claim for it is in the store, so no standard-route derivation was added.'
---

## formal
The lifted invertible points $\{[X(x)] : x \in \mathbb{V},\ Q(x) \neq 0\}$ are dense in $\mathcal{Q}$.

## technical
In the conformal completion each point $x \in \mathbb{V}$ is lifted to the null ray $[X(x)]$ of $X(x) = \nO + x + \frac12 Q(x)\,\nInf$ on the quadric $\mathcal{Q}$. The lemma states that the lifts of the invertible points, those with $Q(x) \neq 0$, are dense in $\mathcal{Q}$.

So every point of the quadric, including the ideal points that are the lift of no point of $\mathbb{V}$, is a limit of lifted invertible points.

## lay
The repair represents each point of the original space as a light-like ray in a bigger space, and the bigger space also contains extra points at infinity. This result says that the ordinary, invertible points come arbitrarily close to every point of the bigger space, the points at infinity included. Nothing in the enlarged space is cut off from the ordinary points.

## one-liner
The lifted invertible points $[X(x)]$ with $Q(x) \neq 0$ are dense in the quadric $\mathcal{Q}$.
