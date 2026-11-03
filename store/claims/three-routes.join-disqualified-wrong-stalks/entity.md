---
id: three-routes.join-disqualified-wrong-stalks
kind: claim
version: 3
title: 'The join is disqualified: wrong stalks'
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
about:
- obj.three-routes.ladder-bundle-even-subbundle
derivations:
- name: main
  uses:
  - three-routes.stalks-are-pointwise-metric-levels@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_three_routes.py
  tags:
  - num:2.5
- kind: check
  ref: check.py::check_join_is_the_whole_ledger
- kind: check
  ref: check.py::check_join_has_elements_odd_at_each_point
locators:
  paper: T05-three-routes
  number: Thm 2.5
  label: thm:join
  line: 160
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: on 2, 3 and 4 points the join contains every generator and spans the whole ledger, and contains elements odd at each point. Version 2 -> 3.'
  typing:
    by: ai-typing-pass
    note: 'Self-contained computation with no premises; only the even-subbundle definition was linked as about.'
  env: theorem
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: [three-routes.stalks-are-pointwise-metric-levels]
    added_dependants: []
    added_about: []
    verdict: connected
    note: 'Part (ii) identifies the pointwise metric levels with the even fibres through the stalks proposition; no later result rests on the theorem, which is read only by the remark that follows it.'
---

## formal
For $U$ with at least two points define the join $J(U) := \bigl\langle \bigcup_{x \in U} \operatorname{Fix}(\operatorname{Ad}\sigma(x)) \bigr\rangle$, the algebra generated inside the $U$-ledger by the pointwise fixed algebras. Then: (i) $J(U)$ is the whole ledger, so the two-ledger discrepancy computed against it vanishes identically; and (ii) $J$ is the section object of no sheaf on $\Sig$ whose stalks are the pointwise metric levels: any presheaf with $J$ as sections contains, at every point $x$, elements odd at $x$, so its stalk data at $x$ properly exceeds $\Aa_x^{+}$.

## technical
For an open $U$ with at least two points, the join $J(U)$ is the algebra generated inside the $U$-ledger by all the pointwise fixed algebras $\operatorname{Fix}(\operatorname{Ad}\sigma(x))$, $x \in U$. Each odd generator at a point $y$ is fixed by the parity at any other point, so $J(U)$ contains every ladder generator and is the whole ledger; the two-ledger discrepancy computed against it therefore vanishes identically.

The join also has the wrong local structure. It contains elements odd at a point $y$, since $\operatorname{Ad}\sigma_y$ negates the odd generator there, whereas every section of a sheaf whose stalks are the pointwise even algebras $\Aa_x^{+}$ is even at every point. So $J$ is the section object of no sheaf whose stalks are the pointwise metric levels.

## lay
There are two natural ways to combine the classical readings at many points of the boundary. This result rules out the more generous one: letting every point's allowed quantities generate an algebra together gives back the entire quantum algebra, so the comparison it was meant to support becomes empty. It also fails to look like the pointwise classical reading near any point, so it cannot be a consistent local notion.

## one-liner
The join of the pointwise fixed algebras is the whole ledger and contains elements odd at each point, so it is the section object of no sheaf whose stalks are the pointwise metric levels.
