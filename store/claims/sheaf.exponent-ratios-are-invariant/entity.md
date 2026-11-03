---
id: sheaf.exponent-ratios-are-invariant
kind: claim
version: 4
title: Exponent ratios are the invariant
status: proved
region: sheaf
subject: walls
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
- obj.sheaf.variable-order-algebra-strict-diagonal-data
derivations:
- name: main
  uses:
  - sheaf.differential-closure-filtration-conormality@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_ratios_are_the_invariants
- kind: check
  ref: check.py::check_kasner_ratio_monotone_and_separating
- kind: check
  ref: check.py::check_constant_presentation_iff_constant_ratios
- kind: check
  ref: check.py::check_varying_exponents_keep_their_logs
locators:
  paper: T04
  number: Thm 9.10
  label: thm:ratios
  line: 1269
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: exponents rescale by a under tau = zeta sigma^a, Kasner ratios u/(1+u) and u are strictly monotone and separating, constant presentations exist iff ratios are constant, and the reparametrised exponent still produces logs. Version 3 -> 4.'
  env: theorem
  context_refs:
  - sheaf.differential-closure-filtration-conormality
  typing:
    by: ai-typing-pass
    added:
    - sheaf.differential-closure-filtration-conormality
    note: 'Added the differential-closure theorem, since the final clause that the logarithms are unavoidable
      rests on it; the Kasner parametrisation used for the ratio is classical arithmetic with no store
      claim to cite. Levels pass: the lay level and one-liner now keep the assumption that the exponents
      are strictly positive and the restriction to the Kasner constraint variety.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - sheaf.differential-closure-filtration-conormality
---

## formal
A change of boundary defining function within the smooth category, $\tau = \zeta(x,\sigma)\,\sigma$ with $\zeta$ smooth positive (the letter avoiding both the Kasner parameter $u$ and Section \ref{sec:schwarzschild}'s $u = \sqrt r$), carries $\tau^{e(x)}$ to $\zeta^{e}\sigma^{e(x)}$ with $\zeta^{e} = \exp(e\log \zeta)$ a smooth positive unit: the exponent functions are invariants of the smooth collar structure. Allowing quasi-homogeneous reparametrisations $\tau = \zeta(x,\sigma)\,\sigma^{a(x)}$, $a$ smooth positive, the exponents, assumed strictly positive where a reparametrisation is attempted, rescale by $a(x)$ and the \emph{ratios} $e_i/e_j$ are the absolute invariants. Consequently the strict diagonal data of Definition \claimref{obj.sheaf.variable-order-algebra-strict-diagonal-data} admits a presentation with locally constant exponents if and only if all ratios $p_i/p_j$ are locally constant; on the Kasner constraint variety the ratio $-p_1/p_2 = u/(1+u)$ is strictly increasing in the Kasner parameter, so this happens exactly where $u$ is locally constant. For genuinely varying exponents the logarithms of Theorem \claimref{sheaf.differential-closure-filtration-conormality} are unavoidable: the variable-order structure is not a reparametrised constant-order structure.

## technical
A smooth change of boundary defining function, $\tau = \zeta\sigma$ with $\zeta$ smooth and positive, turns $\tau^{e(x)}$ into $\zeta^{e}\sigma^{e(x)}$ with $\zeta^{e}$ a smooth positive unit, so the exponent functions are invariants of the smooth collar structure. Under quasi-homogeneous changes $\tau = \zeta\sigma^{a(x)}$, with $a$ smooth and positive and the exponents strictly positive where this is attempted, the exponents scale by $a(x)$ and the ratios $e_i/e_j$ are the absolute invariants.

Hence strict diagonal data admit a presentation with locally constant exponents exactly when all ratios $p_i/p_j$ are locally constant. On the Kasner constraint variety $-p_1/p_2 = u/(1+u)$ is strictly increasing in the Kasner parameter $u$, so this happens exactly where $u$ is locally constant. For genuinely varying exponents the logarithms of the differential closure cannot be removed by reparametrisation.

## lay
The rates at which directions shrink near a boundary depend on how the distance to the boundary is measured. Changing the measuring function in natural ways can stretch all the rates by a common factor but, provided the rates are positive, cannot change their ratios. So if the ratios genuinely vary from place to place, as they do for Kasner-type data wherever the Kasner parameter varies, no choice of coordinates makes the rates constant, and the logarithms they cause are unavoidable.

## one-liner
Under smooth and quasi-homogeneous changes of defining function, with strictly positive exponents, the exponent ratios are the invariants, so on the Kasner constraint variety strict diagonal data have a constant-exponent presentation exactly where the Kasner parameter is locally constant.
