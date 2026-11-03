---
id: sheaf.matching-fibre
kind: claim
version: 4
title: The matching at the fibre
status: proved
region: sheaf
subject: interior
tags: [kasner]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
about:
- obj.interior.weighted-blow-up-hubble-normalisation-admissible
derivations:
- name: main
  uses:
  - sheaf.weights-are-forced-are-kasner-exponents@5
  - sheaf.weighted-limit@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_bivectors_are_so13
- kind: check
  ref: check.py::check_weight_bivector_is_unit_boost
- kind: check
  ref: check.py::check_ladder_boost_on_ambient_fibre
locators:
  paper: T04
  number: Prop 8.26
  label: prop:fibreweld
  line: 1135
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the bivectors of Cl(1,3) as so(1,3) with the bracket matched, the weight bivector at four Kasner points acting as a unit boost with characteristic polynomial lambda^4 - lambda^2 (control off the circle), and the ladder boost K = k ^ k* = N - 1/2 with K^2 = 1/4. Version 3 -> 4. Fix (Leon 2026-10-23, referee GR1): displayed connection values re-signed to the GTG sign of the definition, D_a = a.nabla + Omega(a) x (Cartan forms omega^i_0 = sigma_i theta^i assemble to -sigma_i B_i; Hubble-normalised Kasner model -sum_i p_i B_i, DICTIONARY C10); content unchanged. The surviving value is -B_w, a unit boost exactly when B_w is; check unchanged (it tests B_w).'
  typing:
    by: ai-typing-pass
    added:
    - sheaf.weighted-limit
    note: 'Added the weighted-limit fact, which the statement cites (extracted as the definition) for
      the holonomy algebra and the surviving matrix it matches; the conservation-of-degeneracy theorem
      in context_refs is cited only to say it is unrelated. Levels pass: conditions already kept.'
  env: proposition
  context_refs:
  - sheaf.conservation-degeneracy-absolute-form
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - sheaf.weighted-limit
---

## formal
Normalise the exceptional Gram to $\eta = \operatorname{diag}(1,-1,-1,-1)$, with $\hat e_0$ the proper-time direction and $\hat e_i$ the Kasner eigendirections. Then: (1) the bivector algebra of the exceptional fibre is $\mathfrak{so}(1,3)$, the holonomy algebra of Fact \claimref{obj.interior.weighted-blow-up-hubble-normalisation-admissible}, and the identification of the two fibres matching proper time, eigendirections, and exponents is canonical up to the isometries preserving the Kasner data; (2) under it, the surviving value $-\sum_i p_i B_i$ of the Hubble-normalised rotation-gauge field (in the sign of the Gauge Theory Gravity definition, $D_a = a \cdot \nabla + \Omega(a) \times$) corresponds to $-B_w$, minus the \emph{weight bivector} $B_w = \sum_i p_i\,\hat e_0 \wedge \hat e_i$, because the weights of the sheaf construction are forced to equal the exponents (Theorem \claimref{sheaf.weights-are-forced-are-kasner-exponents}); (3) $B_w$ is $\eta$-antisymmetric with characteristic polynomial $\lambda^4 - (\sum_i p_i^2)\lambda^2 = \lambda^4 - \lambda^2$: \emph{the second Kasner relation says precisely that the surviving matrix is a unit boost of the exceptional algebra}. The wall itself carries the transverse generator: the ladder boost $K = \tfrac12[k,k^*] = k \wedge k^* = N - \tfrac12$ (no relation to the exterior form $K$ of Theorem \claimref{sheaf.conservation-degeneracy-absolute-form}), with $K^2 = \tfrac14$ on the whole ambient fibre, an $\mathfrak{so}(1,1)$ supported on the wall.

## technical
Normalise the exceptional Gram to $\eta = \operatorname{diag}(1,-1,-1,-1)$, with $\hat e_0$ the proper-time direction and $\hat e_i$ the Kasner eigendirections. The bivector algebra of the exceptional fibre is $\mathfrak{so}(1,3)$, the holonomy algebra of the weighted limit, and the identification of the two fibres matching proper time, eigendirections and exponents is canonical up to the isometries preserving the Kasner data. Under it, the surviving value $-\sum_i p_i B_i$ of the Hubble-normalised rotation-gauge field corresponds to $-B_w$, minus the weight bivector $B_w = \sum_i p_i\,\hat e_0 \wedge \hat e_i$, because the sheaf weights are forced to equal the exponents.

$B_w$ is $\eta$-antisymmetric with characteristic polynomial $\lambda^4 - (\sum_i p_i^2)\lambda^2 = \lambda^4 - \lambda^2$, so the second Kasner relation says exactly that $B_w$ is a unit boost of the exceptional algebra. The wall itself carries the transverse ladder boost $K = k \wedge k^* = N - \tfrac12$, with $K^2 = \tfrac14$ on the whole ambient fibre, an $\mathfrak{so}(1,1)$ supported on the wall.

## lay
This result matches the algebraic and geometric pictures of a black hole's centre at the level of a single point. The Lorentz algebra found in the geometric limit is the same as the algebra living on the special fibre of the completion. Under the match, the limiting stretching becomes a single boost of unit strength, and that unit strength is exactly one of the two classical Kasner conditions.

## one-liner
The exceptional fibre's bivector algebra is $\mathfrak{so}(1,3)$, and under the canonical matching the weighted-limit value becomes $-B_w$, minus the weight bivector $B_w$, which the second Kasner relation makes a unit boost.
