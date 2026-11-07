---
id: conformal.blade-basis-persists-under-degeneracy
kind: claim
version: 5
title: The blade basis persists under degeneracy
status: proved
region: conformal
subject: clifford-structure
tags: [degenerate-algebras, classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T02, deposited version
- name: Claude Opus 5.5
  role: 'consistency pass, blades of a non-orthogonal basis named as ordered products'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: typed
derivations:
- name: main
  uses:
  - conformal.blade-basis-persists-under-degeneracy-external@1
  - sheaf.blade-basis-degenerate-forms-included@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_blades_form_a_basis_for_any_form_and_basis
locators:
  paper: T02
  number: Fact 2.1
  label: fact:blades
  line: 145
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. Notation, as in sheaf.blade-basis-degenerate-forms-included: the ordered products e_I of a possibly non-orthogonal basis are named as such, since obj.std-algebra.blade reserves blade for outer products. Statement unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: blades of skew bases are independent and span Cl(W,B) on Lambda(W) for four forms, degenerate ones included. Version 3 -> 4.'
  env: fact
  context_refs:
  - sheaf.blade-basis-degenerate-forms-included
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: Fact restating the series' blade-basis lemma, both edges kept as its real sources; pure algebra
      with no completion dependence, so no standard-route derivation.
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - conformal.blade-basis-persists-under-degeneracy-external
---

## formal
Let $B$ be any symmetric bilinear form on a real space $W$ of dimension $m$, and let $e_1, \dots, e_m$ be any basis of $W$. Then the $2^m$ blades $e_I = e_{i_1} \cdots e_{i_k}$, $I = \{i_1 < \dots < i_k\}$ (ordered geometric products, outer-product blades only for an orthogonal basis), form a linear basis of $\Cl(W, B)$; in particular $\dim \Cl(W,B) = 2^m$ whether or not $B$ is degenerate. \emph{Provenance:} \cite[Lem.~2.6]{ButlerT4}; classical, \cite{Chevalley1997}.

## technical
Let $B$ be any symmetric bilinear form on a real space $W$ of dimension $m$, degenerate or not, and let $e_1, \dots, e_m$ be any basis of $W$. Then the $2^m$ blades $e_I = e_{i_1} \cdots e_{i_k}$, one for each increasing index set $I$, form a linear basis of $\Cl(W,B)$, so $\dim \Cl(W,B) = 2^m$ in every case.

The fact restates the series' own blade-basis lemma for possibly degenerate forms, which in turn is classical (Chevalley).

## lay
A Clifford algebra is built from a space of directions together with a rule for multiplying them. This fact says that the products of distinct basis directions always form a basis for the whole algebra, so an algebra built on m directions has size two to the power m. That stays true even when the multiplication rule is degenerate, with some directions of zero length against every direction.

## one-liner
For any symmetric bilinear form on an $m$-dimensional real space, degenerate or not, the $2^m$ blades of any basis form a linear basis of $\Cl(W,B)$.
