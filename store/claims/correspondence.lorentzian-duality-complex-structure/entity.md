---
id: correspondence.lorentzian-duality-complex-structure
kind: claim
version: 3
title: Lorentzian duality is a complex structure
status: proved
region: correspondence
subject: conformal-spacetime
tags: [chirality, pseudoscalar-and-centre]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T09.py
  tags:
  - label:lem:star
- kind: check
  ref: check.py::check_star_squares_to_minus_one
- kind: check
  ref: check.py::check_star_is_pseudoscalar_multiplication
- kind: check
  ref: check.py::check_eigenspaces_and_conjugation
locators:
  paper: T09
  number: Lem 6.4
  label: lem:star
  line: 799
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Hodge star on Lambda^2 in signatures (1,3) and (3,1): *^2 = -1, * = multiplication by the pseudoscalar, eigenspaces of dimension 3 swapped by conjugation. Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: No edges; a standard linear-algebra fact proved in place, with no imported counterpart in the
      store.
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - "the $\\pm i$ eigenvalues and eigenspaces of the Hodge star on $\\Lambda^2 \\otimes \\C$: a complexified space and complex numbers as eigenvalues, kept"
---

## formal
On $\Lambda^2$ of an oriented $4$-dimensional Lorentzian vector space, the Hodge star satisfies $\ast^2 = -1$; its $\pm i$ eigenspaces $\Lambda^\pm \subset \Lambda^2_\C$ each have dimension three, and complex conjugation (with respect to the real form $\Lambda^2$) interchanges them.

## technical
On the $2$-forms of an oriented $4$-dimensional Lorentzian vector space the Hodge star satisfies $\ast^2 = -1$, so it is a complex structure on the real six-dimensional space $\Lambda^2$. After complexification its $\pm i$ eigenspaces $\Lambda^\pm \subset \Lambda^2_\C$ each have dimension three, and complex conjugation with respect to the real form $\Lambda^2$ interchanges them.

## lay
In four-dimensional spacetime the Hodge star sends each plane element to a complementary one. Doing it twice gives minus the original, just as multiplying by the imaginary unit twice gives minus one. So once complex numbers are allowed, the plane elements split into two three-dimensional halves, self-dual and anti-self-dual, which are complex conjugates of each other.

## one-liner
On $2$-forms of an oriented four-dimensional Lorentzian space the Hodge star squares to $-1$, with three-dimensional, mutually conjugate eigenspaces for the eigenvalues $\pm i$.
