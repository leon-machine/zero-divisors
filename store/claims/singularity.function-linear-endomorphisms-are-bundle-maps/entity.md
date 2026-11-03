---
id: singularity.function-linear-endomorphisms-are-bundle-maps
kind: claim
version: 3
title: Function-linear endomorphisms are bundle maps
status: proved
region: singularity
subject: entropy
tags: [classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_function_linear_maps_are_fibrewise
- kind: check
  ref: check.py::check_value_at_x_depends_only_on_s_at_x
- kind: check
  ref: check.py::check_controls_are_not_function_linear
locators:
  paper: T05
  number: Lem C.6
  label: lem:supportT5
  line: 2690
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: over a finite base in a mixed basis, the function-linear endomorphisms of rank 1 and 2 bundles form a space of dimension 3 r^2 of block-diagonal (fibrewise) maps with (Ds)(x) = 0 when s(x) = 0, with difference and derivative controls. Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: No store premises; a self-contained bump-function argument.
---

## formal
Let $\mathcal{F}$ be the sheaf of sections of a vector bundle over $E$ and $D$ a $C^\infty(E)$-linear endomorphism of $\mathcal{F}(E)$. Then $D$ is tensorial: $(Ds)(x)$ depends only on $s(x)$, so $D$ is a bundle map $\{a_x\}$; for a line bundle, multiplication by a function.

## technical
Let $\mathcal{F}$ be the sheaf of sections of a vector bundle over $E$ and $D$ a $C^\infty(E)$-linear endomorphism of $\mathcal{F}(E)$. Then $D$ is tensorial: $(Ds)(x)$ depends only on $s(x)$, so $D$ is a bundle map $\{a_x\}$, and on a line bundle it is multiplication by a function.

The proof uses a local frame and a bump function to show that $(Ds)(x) = 0$ whenever $s(x) = 0$.

## lay
If an operation on fields commutes with multiplication by ordinary functions, it cannot look at neighbouring points: its output at a point depends only on the field's value there. In the simplest case, a field with one component at each point, such an operation is just multiplication by a fixed function.

## one-liner
A $C^\infty(E)$-linear endomorphism of the sections of a vector bundle is a bundle map, and on a line bundle it is multiplication by a function.
