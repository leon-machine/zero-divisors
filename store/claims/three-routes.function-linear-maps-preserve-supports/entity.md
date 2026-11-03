---
id: three-routes.function-linear-maps-preserve-supports
kind: claim
version: 2
title: Function-linear maps preserve supports
status: proved
region: three-routes
subject: walls
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-three-routes, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_three_routes.py
  tags:
  - num:4.1
- kind: check
  ref: check.py::check_function_linear_maps_are_bundle_maps
- kind: check
  ref: check.py::check_supports_are_preserved
- kind: check
  ref: check.py::check_hopping_is_not_function_linear
locators:
  paper: T05-three-routes
  number: Lem 4.1
  label: lem:support
  line: 232
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: finite core: function-linear maps on finite point modules are exactly bundle maps and preserve supports via Ds = f Ds; hopping maps are not function-linear. Version 1 -> 2.'
  typing:
    by: ai-typing-pass
    note: 'Self-contained lemma with no premises; no edges changed.'
  env: lemma
---

## formal
Let $\mathcal{F}$ be a sheaf of $C^\infty_\Sig$-modules and $D : \mathcal{F}(U) \to \mathcal{F}(U)$ a $C^\infty(U)$-linear map. Then $\supp(Ds) \subseteq \supp(s)$ for every section $s$.

## technical
Let $\mathcal{F}$ be a sheaf of $C^\infty_\Sig$-modules and $D$ a $C^\infty(U)$-linear map on its sections over an open set $U$. Then $\supp(Ds) \subseteq \supp(s)$ for every section $s$.

The point is that a function-linear map commutes with multiplication by functions: if $f$ equals $1$ near $\supp(s)$ then $s = fs$, so $Ds = f\,Ds$ vanishes wherever $f$ does, and such bump functions can be chosen with support as close to $\supp(s)$ as desired.

## lay
An operation that only multiplies by functions, and never compares neighbouring points, cannot spread anything to where it was not already present. If the input is zero on some region, the output is zero there too. Whatever such an operation produces stays inside the region where its input lived.

## one-liner
A function-linear map on sections of a sheaf of smooth-function modules never enlarges the support of a section.
