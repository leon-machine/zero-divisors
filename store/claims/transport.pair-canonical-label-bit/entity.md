---
id: transport.pair-canonical-label-bit
kind: claim
version: 3
title: The pair is canonical; the label is a bit
status: proved
region: transport
subject: zero-divisors
tags: [idempotents, obstruction-types]
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
- obj.transport.obstruction-types
derivations:
- name: main
  uses:
  - transport.ascent-renders-grade-involution-inner@3
  - transport.classification-idempotent-orbits@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_pair_and_involution_determine_each_other
- kind: check
  ref: check.py::check_type_p_label_inner_iff_balanced
- kind: check
  ref: check.py::check_type_c_label_outer_until_ascent
locators:
  paper: T01
  number: Prop 6.5
  label: prop:pair
  line: 1406
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: u = 2e - 1 is an involution with spectral projections e, 1 - e for conjugated idempotents, e ~ 1 - e by an inner automorphism exactly when balanced, and eps_+- swapped only by the outer grade involution until the ascent. Version 2 -> 3.'
  env: proposition
  unresolved_refs:
  - rem:forgottenbit
  typing:
    by: ai-typing-pass
    note: 'Edges kept: the orbit classification gives the gauge statement and the inner-grade proposition
      is part of the cross-type comparison the statement asserts.'
---

## formal
For an idempotent $e \notin \{0,1\}$, set $u = 2e - 1$, an involution ($u^2 = 1$), with $e = \tfrac12(1+u)$ and $1 - e = \tfrac12(1-u)$ its spectral projections. The unordered pair $\{e, 1-e\}$ and the involution $\pm u$ determine one another canonically; the residual choice (which member to call $e$, equivalently the sign of $u$) is a $\mathbb{Z}_2$ labelling. By Theorem \claimref{transport.classification-idempotent-orbits}(2) this labelling is gauge (implemented by an inner automorphism) precisely for balanced pairs, and is canonically resolved by rank order otherwise. The pattern is now visible across the whole taxonomy: each obstruction type terminates in a residual $\mathbb{Z}_2$: the labelling of $\varepsilon_\pm$ for type C, exchangeable by no inner automorphism and rendered gauge only by the ascent (Proposition \claimref{transport.ascent-renders-grade-involution-inner}); the sign $\gamma$ of the fused ascent for Rule 2, not detected by the algebra (Remark \ref{rem:forgottenbit}); and the labelling of $\{e, 1-e\}$ for type P, gauge already in the base algebra whenever the ranks permit. The three $\mathbb{Z}_2$'s are at strictly decreasing depth: outer, forgotten, inner.

## technical
For an idempotent $e \notin \{0, 1\}$ the element $u = 2e - 1$ is an involution, $u^2 = 1$, with spectral projections $e = \tfrac12(1 + u)$ and $1 - e = \tfrac12(1 - u)$. The unordered pair $\{e, 1 - e\}$ and the involution $\pm u$ determine one another canonically, leaving a $\mathbb{Z}_2$ label: which member is called $e$, equivalently the sign of $u$. By the classification of idempotent orbits this label is gauge, implemented by an inner automorphism, exactly for balanced pairs, and is otherwise resolved by rank order.

Each obstruction type ends in such a $\mathbb{Z}_2$: for type C the labelling of $\varepsilon_\pm$, exchanged by no inner automorphism and made inner only by the ascent; for Rule 2 the sign of the fused ascent, which the algebra does not detect; for type P the labelling of $\{e, 1 - e\}$, inner already in the base whenever the ranks permit. The three sit at strictly decreasing depth: outer, forgotten, inner.

## lay
An element that equals its own square splits the space into two complementary parts, and that pair of parts is fixed without any choice. All that remains is a single yes-or-no choice of which part to call the first. Each of the three kinds of obstruction leaves such a bit, and the three bits are progressively easier to undo by a symmetry.

## one-liner
A nontrivial idempotent and its complement form a canonical pair equivalent to the involution $\pm(2e - 1)$, leaving only a $\mathbb{Z}_2$ label, and each obstruction type ends in such a bit at a different depth.
