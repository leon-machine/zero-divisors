---
id: sheaf.rain-duality
kind: claim
version: 3
title: Rain duality
status: proved
region: sheaf
subject: walls
tags: [schwarzschild]
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
- obj.sheaf.weighted-coframe-module
derivations:
- name: main
  uses:
  - sheaf.exceptional-algebra-black-hole@4
  - sheaf.schwarzschild-degeneration-boundary-tame@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_dual_coframe_of_rain_frame
- kind: check
  ref: check.py::check_minkowski_gram_at_every_radius
- kind: check
  ref: check.py::check_membership_iff_bounded_rain_components
- kind: check
  ref: check.py::check_exceptional_module_and_transition
locators:
  paper: T04
  number: Prop 8.22
  label: prop:raindual
  line: 1097
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: at two masses, the rain coframe is dual to the rain frame with Minkowski Gram at every radius, membership in W iff bounded rain components (monomial scan), the norm identity and a null counterexample, and the transition rho = sqrt(r) k/sqrt(r) - m dt with determinant -sqrt(r). Version 2 -> 3.'
  env: proposition
  context_refs:
  - sheaf.weights-are-forced-are-kasner-exponents
  unresolved_refs:
  - rem:nullmixing
  typing:
    by: ai-typing-pass
    note: 'Kept both edges; the closing reading of the forced-weights dichotomy is interpretive, so that
      context reference was not added, though it is arguable. Levels pass: conditions already kept.'
---

## formal
At every interior radius, exactly:
\begin{enumerate}
\item the coframe $(\dtPG,\ k/\sqrt r,\ \mu_1,\ \mu_2)$ is the \emph{dual coframe} of the infalling orthonormal frame: the pairing matrix is the identity, the vanishing $(k/\sqrt r)(V) = 0$ being the rain identity of Theorem \claimref{sheaf.schwarzschild-degeneration-boundary-tame}(5);
\item its Gram is exactly Minkowski, $\operatorname{diag}(1,-1,-1,-1)$, at every radius, horizon and collar included: $\dtPG$, the Painlev\'e-Gullstrand time, is the rain's proper-time differential, and the rain observer's covector space never degenerates;
\item a $u$-smooth one-form lies in $\shW$ if and only if its rain-frame components are bounded up to the singularity; the norm identity $|\alpha|_G^2 = \alpha(V)^2 - \sum_i \alpha(e_{\hat\imath})^2$ holds exactly, though boundedness of the norm alone does not suffice for membership (Remark \ref{rem:nullmixing}); the excluded coordinate forms diverge, $dr(V) = -m/\sqrt r$ and $d\theta(e_{\hat\theta}) = 1/r$;
\item the module $\shW_{\mathrm{exc}}$ spanned by the coframe of (1) over $C^\infty(\Mt_u)$ is the exceptional-regime module of Proposition \claimref{sheaf.exceptional-algebra-black-hole}; rain-frame components of a covector are precisely its $\shW_{\mathrm{exc}}$-coefficients; and $\shW \subset \shW_{\mathrm{exc}}$, via $\rho = \sqrt r\,(k/\sqrt r) - m\,\dtPG$, with transition determinant $-\sqrt r$. The weighted module is the $u$-smooth shadow of the rain observer's covector space, and the degeneration-regime/exceptional-regime dichotomy of Theorem \claimref{sheaf.weights-are-forced-are-kasner-exponents} is the dichotomy between the blow-up's smooth structure and the rain frame.
\end{enumerate}

## technical
At every interior radius of the Schwarzschild composite, the coframe $(\dtPG, k/\sqrt r, \mu_1, \mu_2)$ is exactly dual to the infalling (rain) orthonormal frame, and its Gram is the Minkowski form $\operatorname{diag}(1,-1,-1,-1)$ at every radius, horizon and collar included; $\dtPG$, the Painlev\'e-Gullstrand time differential, is the rain's proper-time differential. A $u$-smooth one-form lies in the weighted module $\shW$ exactly when its rain-frame components are bounded up to the singularity; the norm identity $|\alpha|_G^2 = \alpha(V)^2 - \sum_i \alpha(e_{\hat\imath})^2$ holds, but a bounded norm alone does not imply membership.

The module $\shW_{\mathrm{exc}}$ spanned by the rain coframe is the exceptional-regime module, rain-frame components are exactly its coefficients, and $\shW \subset \shW_{\mathrm{exc}}$ via $\rho = \sqrt r\,(k/\sqrt r) - m\,\dtPG$, with transition determinant $-\sqrt r$. So the weighted module is the $u$-smooth shadow of the rain observer's covector space.

## lay
An observer falling freely into a black hole, often called the rain observer, carries measuring directions that never degenerate, even at the horizon. This result shows that the module used to describe the degeneration at the singularity consists exactly of the smooth one-forms whose components, as the rain observer measures them, stay finite. The degenerate description and the non-degenerate one thus correspond to the smooth structure of the blow-up and to the rain frame.

## one-liner
The rain observer's dual coframe has exactly Minkowski Gram at every radius, spans the exceptional-regime module, and characterises the weighted module as the smooth one-forms with bounded rain-frame components.
