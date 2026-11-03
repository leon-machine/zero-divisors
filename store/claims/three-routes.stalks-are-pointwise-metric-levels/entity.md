---
id: three-routes.stalks-are-pointwise-metric-levels
kind: claim
version: 4
title: The stalks are the pointwise metric levels
status: proved
region: three-routes
subject: walls
tags:
- descent-map
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
  - sheaf.function-linearity-tame-constructions@2
  - singularity.descent-parity-average@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_projection_is_smooth_idempotent_constant_rank
- kind: check
  ref: check.py::check_range_is_even_part_kernel_odd_part
- kind: check
  ref: check.py::check_even_germs_are_the_stalk
locators:
  paper: T05-three-routes
  number: Prop 2.3
  label: prop:stalks
  line: 140
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: for a smooth family of single-mode fibres, (id + alpha_x)/2 is a polynomial idempotent of constant rank 2 with range the even part and kernel the odd part, and it returns even germs. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    removed:
    - singularity.p-reduced-metric-level-reading-many
    added:
    - sheaf.function-linearity-tame-constructions
    - singularity.descent-parity-average
    note: Redirected the linearity premise to the T4 function-linearity proposition that part (ii) of the imported
      fact cites, and added the parity-average theorem for identifying the stalk fibre with the pointwise metric
      level; the descent definition result was left out as already a premise of that theorem.
  env: proposition
  context_refs:
  - singularity.descent-parity-average
  - singularity.descent-what-it-erases
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - sheaf.function-linearity-tame-constructions
    - singularity.descent-parity-average
    note: The existing claimref to singularity.p-reduced-metric-level-reading-many(ii) is the same label-map error
      as in three-routes.class-relative-no-go; the correct premise is cited beside it and the stale pointer is left
      for the maintainer.
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 8
    note: The citation of the machinery's linearity pointed at singularity.p-reduced-metric-level-reading-many,
      which carries only part (i) of the note's Fact 1.3 (the composite proposition); part (ii), the linearity,
      is sheaf.function-linearity-tame-constructions, now the only citation.
---

## formal
For each $x \in \Sig$ the stalk of $\mathfrak{M}$ at $x$ is $C^\infty_x \otimes \Aa_x^{+}$: germs of families valued in the fibre's even part. In particular the stalk's algebra fibre is $\Aa_x^{+}$, the image of the point's own descent, which is the pointwise metric level of \cite[Prop.~5.5, Thm.~5.7]{ButlerT5}.

## technical
The even subbundle $\Aa^{+}$ is locally trivial, its fibrewise projection $\tfrac12(\id + \alpha_x)$ being a smooth idempotent bundle map, so the stalk of $\mathfrak{M}$ at $x \in \Sig$ is $C^\infty_x \otimes \Aa_x^{+}$: germs of families valued in the even part of the fibre.

The algebra fibre of the stalk is therefore $\Aa_x^{+}$, the range of the point's own descent $E(a) = \tfrac12(a + \sigma a \sigma)$, which is the pointwise metric level established earlier in the series.

## lay
Zooming in on a single point of the boundary, the sheaf of classical-level quantities looks exactly like the classical reading of that one point. So the sheaf is built from the right local pieces, and assembling the pointwise readings neither adds nor loses anything locally.

## one-liner
The stalk of the metric-level sheaf at each $x \in \Sig$ is $C^\infty_x \otimes \Aa_x^{+}$, whose algebra fibre is the pointwise metric level.
