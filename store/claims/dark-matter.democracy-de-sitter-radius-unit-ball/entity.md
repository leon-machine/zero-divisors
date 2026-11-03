---
id: dark-matter.democracy-de-sitter-radius-unit-ball
kind: claim
version: 4
title: Democracy at the de Sitter radius is the unit-ball rule
status: proved
region: dark-matter
subject: dark-matter
tags: [counting-rules, dark-matter-ratio, cosmological-constant]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
review: typed
derivations:
- name: main
  assumes:
  - dark-matter.d-democracy-total-mass@1
  - dark-matter.r3-one-cell-per-unshared-direction@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_shares_are_sphere_ratios
- kind: check
  ref: check.py::check_sphere_form_is_ball_form
- kind: check
  ref: check.py::check_total_is_unit_ball_rule
locators:
  paper: T14
  number: Prop 7.20
  label: prop:democracy
  line: 1045
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: shares |S^4|/|S^n| with M and l cancelling, the hat-box identity giving the ball form, and the unit-ball total, as identities in pi. Version 3 -> 4.'
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: VALUES L7
    open_problem: op.small-findings
    note: 'The levels now say that the de Sitter radius enters as the counting unit of R3, not as the extent of a metric fifth direction, which dark-matter.thickness-not-gravitational-quantity shows is excluded by short-range tests of Newton''s law.'
  env: proposition
  context_refs:
  - dark-matter.unit-ball-rule
  unresolved_refs:
  - rem:forms
  typing:
    by: ai-typing-pass
    added:
    - dark-matter.d-democracy-total-mass
    - dark-matter.r3-one-cell-per-unshared-direction
    note: 'Added D (the stated hypothesis) and R3 (the statement takes R3''s thickness with the de Sitter
      radius as its unit, which the paper calls R3''s thickness at one de Sitter radius); the unit-ball
      rule''s total is a comparison reached through the sphere-ball identity, so it is not edged. Levels
      pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-matter.d-democracy-total-mass
    - dark-matter.r3-one-cell-per-unshared-direction
---

## formal
Under D, with the thickness set to $\ell$ (R3 with $\ell$ as the unit), the shares are $\tfrac{|\Sph^{4}|}{|\Sph^{n}|}$, the sphere form of Remark \ref{rem:forms}, and the total is that of Proposition \claimref{dark-matter.unit-ball-rule}.

## technical
Assume every populated tower carries the same total mass $M_{\mathrm{tot}}$ on its de Sitter sphere of radius $\ell$, and take the thickness rule with $\ell$ as its unit. A tower of dimension $n$ then has density $M_{\mathrm{tot}}/(|\Sph^{n}|\,\ell^{n})$ on its sphere; counting one thickness $\ell$ of the direction we cannot see, or sheets $\ell$ apart, turns this into a density per unit of our four-measure, and the share is
$f = |\Sph^{4}|/|\Sph^{n}|$. These are the sphere form of the shares, and their total is the unit-ball rule's. Here $\ell$ is the counting unit of the thickness rule, not the extent of a metric fifth direction: a metric fifth direction of that extent is excluded by short-range tests of Newton's law (Proposition \claimref{dark-matter.thickness-not-gravitational-quantity}).

## lay
Suppose every hidden world holds the same total mass, spread over a sphere whose size is set by the cosmological constant, and the counted slice is one such radius thick. Then the share each world contributes here depends only on ratios of sphere sizes. Those ratios give the same total amount of dark matter as the unit-ball rule, with a cosmic rather than a microscopic unit of length.

## one-liner
Under democracy of the total mass, with the thickness one de Sitter radius, each tower's share is $|\Sph^{4}|/|\Sph^{n}|$ and the total is the unit-ball rule's (the radius as a counting unit; a metric fifth direction of that extent is excluded).
