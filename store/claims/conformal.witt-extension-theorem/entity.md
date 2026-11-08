---
id: conformal.witt-extension-theorem
kind: claim
version: 2
title: The Witt extension theorem
status: imported
region: conformal
subject: completion
tags: [witt-index, classical-theorem]
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
  role: 'maintainer pass, duplicate link at Leon''s decisions'
  version: 2
  source: maintainer pass 2026-11-07 (decisions)
review: typed
imported_from:
- citation: T. Y. Lam, Introduction to Quadratic Forms over Fields, Graduate Studies in Mathematics 67,
    American Mathematical Society (2005).
  key: Lam2005
  locator: Ch.~I, Thm.~4.7
locators:
  paper: T02
  number: Fact 2.2
  label: fact:witt
  line: 149
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Decision item E7 (routine; no retirement): equivalent_to std-algebra.witt-extension@1 added. Witt''s extension theorem as imported in T02 is the standard-algebra entity, kept as the home.'
  env: fact
  typing:
    by: ai-typing-pass
    note: "Imported textbook result; levels describe the classical theorem only."
equivalent_to:
- std-algebra.witt-extension@2
---

## formal
Over a field of characteristic not two, let $(\widetilde W_1, Q_1)$ and $(\widetilde W_2, Q_2)$ be isometric nondegenerate quadratic spaces and let $\sigma : S_1 \to S_2$ be an isometry between subspaces $S_i \subseteq \widetilde W_i$, the $S_i$ arbitrary and possibly degenerate. Then $\sigma$ extends to an isometry $\widetilde W_1 \to \widetilde W_2$. \emph{Provenance:} \cite[Ch.~I, Thm.~4.7]{Lam2005}.

## technical
Over a field of characteristic not two, let $(\widetilde W_1,Q_1)$ and $(\widetilde W_2,Q_2)$ be isometric nondegenerate quadratic spaces and let $\sigma: S_1 \to S_2$ be an isometry between subspaces $S_i \subseteq \widetilde W_i$, which may be degenerate. Then $\sigma$ extends to an isometry $\widetilde W_1 \to \widetilde W_2$.

This is the classical Witt extension theorem of the algebraic theory of quadratic forms. In the series it is what makes minimal completions unique up to an isometry fixing the original space.

## lay
Suppose two spaces carry equivalent nondegenerate notions of length and angle. Then any length-preserving match between a part of one and a part of the other can be extended to a length-preserving match of the whole spaces. This works even when the parts themselves are degenerate. It is a standard theorem about quadratic forms.

## one-liner
Over a field of characteristic not two, an isometry between arbitrary subspaces of two isometric nondegenerate quadratic spaces extends to an isometry of the whole spaces.
