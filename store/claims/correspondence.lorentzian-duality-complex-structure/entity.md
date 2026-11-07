---
id: correspondence.lorentzian-duality-complex-structure
kind: claim
version: 4
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 4
  source: maintainer pass 2026-11-07 (GA units)
- name: Claude Opus 5.5
  role: notation pass, imaginary units resolved by the unit principle
  version: 4
  source: maintainer pass 2026-11-07 (resolve units)
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
  maintainer_pass_resolve_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 kept (already raised in this pass). The i of the +-i eigenspaces is the scalar of the complexification of the real space of 2-forms, which must commute with the Hodge star; by U3 it is the central pseudoscalar I_5 = I_4 e of the odd extension (std-algebra.complexification-is-the-odd-extension, cited as a mention): Lambda^2_C = Lambda^2 + I_5 Lambda^2, eigenvalues +-I_5; the text says that the star itself is multiplication by I_4 on real bivectors, a different element. Correspondence.chirality-split-ordering-insensitivity-asd-sector reads the lemma inside so(2,4)_C with that algebra''s unit I_7. Declaration removed.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (other): the +-i eigenvalues are taken on the complexification of the real space of 2-forms, whose scalar must commute with the Hodge star (on real bivectors, multiplication by I_4 up to sign), so no pseudoscalar can stand for it.'
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
On $\Lambda^2$ of an oriented $4$-dimensional Lorentzian vector space, the Hodge star satisfies $\ast^2 = -1$; its $\pm I_5$ eigenspaces $\Lambda^\pm \subset \Lambda^2_\C$ each have dimension three, and complex conjugation (with respect to the real form $\Lambda^2$, $I_5 \mapsto -I_5$) interchanges them. Here $\Lambda^2_\C = \Lambda^2 \oplus I_5\Lambda^2$, with $I_5 = I_4e$ the central pseudoscalar of the odd extension of the space by a vector $e$ with $Q(e) = +1$, the unit of its complexification (\claimref{std-algebra.complexification-is-the-odd-extension}); on real bivectors $\ast$ is multiplication by the pseudoscalar $I_4$ up to sign, and $I_5$ is a different element.

## technical
On the $2$-forms of an oriented $4$-dimensional Lorentzian vector space the Hodge star satisfies $\ast^2 = -1$, so it is a complex structure on the real six-dimensional space $\Lambda^2$. After complexification by the central pseudoscalar $I_5 = I_4e$ of the odd extension, $\Lambda^2_\C = \Lambda^2 \oplus I_5\Lambda^2$, its $\pm I_5$ eigenspaces $\Lambda^\pm \subset \Lambda^2_\C$ each have dimension three, and complex conjugation with respect to the real form $\Lambda^2$ interchanges them.

## lay
In four-dimensional spacetime the Hodge star sends each plane element to a complementary one. Doing it twice gives minus the original, just as multiplying by the imaginary unit twice gives minus one. So once complex numbers are allowed, the plane elements split into two three-dimensional halves, self-dual and anti-self-dual, which are complex conjugates of each other.

## one-liner
On $2$-forms of an oriented four-dimensional Lorentzian space the Hodge star squares to $-1$, with three-dimensional, mutually conjugate eigenspaces for the eigenvalues $\pm I_5$ of its complexification by the central pseudoscalar $I_5$ of the odd extension.
