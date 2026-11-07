---
id: one-relation.imported-completion-ladder
kind: claim
version: 6
title: 'Imported: the completion and the ladder'
status: proved
region: one-relation
subject: completion
tags: [hyperbolic-plane, ladder-pairs, car-algebra]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
review: typed
about:
- obj.transport.null-lift-completion
derivations:
- name: main
  uses:
  - tower.answers-iteration-question@5
  - tower.car-limit-even-charge@6
  - transport.minimality@4
  - std-algebra.tensor-rules@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_one_hyperbolic_plane_per_completion
- kind: check
  ref: check.py::check_tower_is_matrix_amplification
- kind: check
  ref: check.py::check_one_fermionic_mode_per_rung
locators:
  paper: T16
  number: Fact 2.1
  label: fact:completion
  line: 505
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.tensor-rules where the proof uses them. Version 5 -> 6.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: one hyperbolic plane per completion, Cl(p+k,q+k) = Cl(p,q) (x) Mat(2^k,R) by twisted generators, and one CAR mode per rung. Version 3 -> 4. Sample inputs moved to module level; no change to what is tested. Version 4 -> 5.'
  env: fact
  context_refs:
  - tower.answers-iteration-question
  - tower.car-limit-even-charge
  - transport.minimality
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'The three uses are exactly the cited minimality, CAR-limit and iteration results; the open
      odd-charge question it mentions is context, not a premise. Levels pass: the lay level now keeps
      the null-lift class within which the minimal completion is minimal.'
---

## formal
Division in a Clifford algebra fails exactly at the non-invertible elements, and among nondegenerate null-lift completions the minimal one adjoins one hyperbolic plane $(1,1)$; iterating gives the tower $\Cl(p+k, q+k) \cong \Mat(2^{k}, \Cl(p,q))$ with one fermionic mode adjoined per rung. For $p - q$ even the completed limit is $\Cl(p,q)_{\C} \otimes \mathrm{CAR}$, the ground algebra complexified and tensored with the CAR algebra; the odd-charge limit is open in the tower paper. \emph{Provenance:} \cite[Thm.~4.13]{ButlerT1}; \cite[Thm.~5.6, Question~5.8, Cor.~6.2]{ButlerT3}.

## technical
Division in a Clifford algebra fails exactly at the non-invertible elements. Among nondegenerate null-lift completions the minimal one adjoins one hyperbolic plane of signature $(1,1)$, and iterating gives the tower $\Cl(p+k,q+k) \cong \Mat(2^k, \Cl(p,q))$, with one fermionic mode adjoined per rung.

For $p-q$ even the completed limit is $\Cl(p,q)_\C \otimes \CAR$, the complexified ground algebra tensored with the CAR algebra; the odd-charge limit is left open. The statement restates earlier series results.

## lay
Each time division fails, the smallest repair of the kind the series considers, a nondegenerate null-lift completion, adds one pair of directions, one of each sign, and repeating this builds an endless ladder of algebras, each a matrix algebra over the one below, with one new fermion-like mode per step. When the starting algebra has an even signature difference, the top of the ladder is the complexified starting algebra combined with the standard algebra of infinitely many fermion modes. The odd case is still open.

## one-liner
The minimal null-lift completion adjoins one hyperbolic plane, iteration gives the tower $\Cl(p+k,q+k) \cong \Mat(2^k,\Cl(p,q))$ with one fermionic mode per rung, and for $p-q$ even the limit is $\Cl(p,q)_\C \otimes \CAR$.
