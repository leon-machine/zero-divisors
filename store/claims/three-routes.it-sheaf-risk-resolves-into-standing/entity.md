---
id: three-routes.it-sheaf-risk-resolves-into-standing
kind: claim
version: 7
title: It is a sheaf, and the risk resolves into the standing hypothesis
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
- name: Claude Opus 5.5
  role: consistency pass, proof brought into line with the corrected statement on the even part
  version: 7
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'maintainer pass, duplicate link at Leon''s decisions'
  version: 7
  source: maintainer pass 2026-11-07 (decisions)
review: typed
about:
- obj.three-routes.ladder-bundle-even-subbundle
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  uses:
  - sheaf.function-linearity-tame-constructions@2
  - three-routes.imported-collar-data-coupling@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_three_routes.py
  tags:
  - num:2.2
- kind: check
  ref: check.py::check_fibrewise_even_part_is_subalgebra
- kind: check
  ref: check.py::check_even_families_glue_and_form_an_algebra
- kind: check
  ref: check.py::check_parity_insensitive_to_ladder_rescaling
- kind: check
  ref: check.py::check_untwisted_ladder_exists_iff_w1_zero
- kind: check
  ref: check.py::check_even_part_does_not_see_the_twist
locators:
  paper: T05-three-routes
  number: Prop 2.2
  label: prop:issheaf
  line: 132
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version kept at 7 (already raised in this run). Decision item E6 (routine; no retirement): partial overlap with singularity.sheaf-assembly-sheaf recorded under extraction.overlaps_with (no pinned link: the overlap is partial); this entity carries the 23 October correction.'
  overlaps_with:
  - id: singularity.sheaf-assembly-sheaf
    note: 'Near-duplicate in part (decision E6): with its sibling, this entity restates part of the singularity entity''s sheaf assembly and carries the 23 October correction. Kept both; recorded here since no clause-level link kind exists.'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: "The last sentence of the proof still said that the even part A^+ exists only in the twisted sense, against the statement as corrected on 2026-10-23 (the even part glues on a twisted ladder bundle and does not see the twist); it now says that the sign of the ladder leaves sigma, hence A^+, unchanged and that only the ladder bundle needs the twist. Statement unchanged."
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated (Leon 2026-10-23): the only-if half of the earlier equivalence of the untwisted sheaf with w1(L) = 0 was false, since sigma = k* k - k k* is unchanged under k -> -k and the twisted transition acts as Ad sigma, the identity on the even part. Now: existence of the untwisted ladder bundle, from which M is built, is equivalent to w1(L) = 0, and M itself, built from Ad sigma, glues on a twisted ladder bundle as well (formal, technical, lay, one-liner); the proof carries a first sentence with the corrected statement. Own exact check added: fibrewise even subalgebra, gluing and algebra on a finite cover, rescaling invariance of sigma, the w1 obstruction to a global ladder on the two-chart circle, and gluing of the even part under every transition. Version 4 -> 5. Check strengthened: sigma pinned to diag(-1, 1) under every rescaling; rescalings moved to module level. Version 5 -> 6.'
  typing:
    by: ai-typing-pass
    removed:
    - singularity.p-reduced-metric-level-reading-many
    added:
    - sheaf.function-linearity-tame-constructions
    - three-routes.imported-collar-data-coupling
    note: Redirected the linearity premise from the composite-proposition claim, which covers only part (i) of the
      imported fact, to the T4 function-linearity proposition that part (ii) cites, and added the collar-data fact
      on which the equivalence with w_1 = 0 rests.
  env: proposition
  outside_pilot_cites:
  - ButlerT4
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - sheaf.function-linearity-tame-constructions
    - three-routes.imported-collar-data-coupling
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
$\mathfrak{M}$ is a sheaf of algebras on $\Sig$. Existence of the untwisted ladder bundle, from which $\mathfrak{M}$ is built, is equivalent to $w_1(\shL) = 0$: the fibrewise condition defining $\Aa^{+}$ uses the parity section $\sigma = k^{*}k - kk^{*}$, $\sigma$ is built from the ladder $(k, k^{*})$, and the ladder exists globally exactly when collar data do, which is $w_1(\shL) = 0$. $\mathfrak{M}$ itself, built from $\operatorname{Ad}\sigma$, which is insensitive to the sign of $k$, glues on a twisted ladder bundle as well and does not see the twist.

## technical
Let $\mathfrak{M}$ assign to each open $U \subseteq \Sig$ the sections of the ladder bundle that are even at every point, that is, fixed by the fibrewise parity $\alpha_x = \operatorname{Ad}\sigma(x)$ with $\sigma = k^{*}k - kk^{*}$. Then $\mathfrak{M}$ is a sheaf of algebras: evenness is a fibrewise condition, so locality and gluing are inherited from the sheaf of sections, and restriction is restriction of coefficient functions because the constructions are $C^\infty$-linear.

The untwisted ladder bundle, from which $\mathfrak{M}$ is built, exists exactly when $w_1(\shL) = 0$: the ladder $(k, k^{*})$ exists globally exactly when collar data do. $\mathfrak{M}$ itself does not see the twist: it is built from $\operatorname{Ad}\sigma$, which is insensitive to the sign of $k$, so on a twisted ladder bundle the even parts glue as well.

## lay
Reading the black-hole boundary at the classical level, point by point, gives at each point a small algebra of allowed quantities. This result shows that those pointwise pieces fit together consistently over regions of the boundary, forming what mathematicians call a sheaf. The underlying bundle needs a global orientation of the collapsing direction, which the completion already assumes; the sheaf of allowed quantities fits together even without it.

## one-liner
The metric-level presheaf of pointwise even families is a sheaf of algebras on $\Sig$; the untwisted ladder bundle it is built from exists exactly when $w_1(\shL) = 0$, while the sheaf itself, built from $\operatorname{Ad}\sigma$, does not see the twist.
