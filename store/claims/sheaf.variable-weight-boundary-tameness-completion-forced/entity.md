---
id: sheaf.variable-weight-boundary-tameness-completion-forced
kind: claim
version: 5
title: Variable-weight boundary tameness, completion, forced weights
status: proved
region: sheaf
subject: walls
tags: [kasner, forcing-and-uniqueness, degenerate-algebras]
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
  - sheaf.determinant-identity-blow-up-expansion@3
  - sheaf.function-linearity-tame-constructions@2
  - sheaf.wall-gram@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_free_module_gram_corank_one
- kind: check
  ref: check.py::check_completion_without_shadow_wall
- kind: check
  ref: check.py::check_weights_forced_pointwise
- kind: check
  ref: check.py::check_boundary_fibre_ideal_and_ladder
locators:
  paper: T04
  number: Thm 9.3
  label: thm:varexp
  line: 1192
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: at three Kasner points with nonconstant units, Gram diag(1, -rho c1, -c2, -c3) of corank one, the (2,4) completion with det h = c2 c3 (1 + rho c1), the forced weights, and the boundary fibre ideal, quotient Cl(1,2) and ladder pair. Version 4 -> 5.'
  env: theorem
  typing:
    by: ai-typing-pass
    added:
    - sheaf.function-linearity-tame-constructions
    note: 'Added function-linearity of the tame constructions, the C-infinity-linearity the closing consequence
      relies on although the source names it without a reference; both existing edges are real premises.
      Levels pass: the lay level no longer widens the scope to a generic singularity (the formal is for
      strict diagonal data), and keeps the condition that the dying axis is named from the geometry.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - sheaf.function-linearity-tame-constructions
---

## formal
For strict diagonal data, let $\shW$ be the $\mathcal{A}$-module with frame $\vartheta_0 = d\tau$, $\vartheta_1 = \sigma^1$, $\vartheta_2 = \tau^{p_2(x)}\sigma^2$, $\vartheta_3 = \tau^{p_3(x)}\sigma^3$ (the letter avoiding the coupling constant $\nu$). Then:
\begin{enumerate}
\item $\shW$ is free of rank four over $\mathcal{A}$, with Gram $\operatorname{diag}(1, -\varrho c_1, -c_2, -c_3)$, $\varrho := \tau^{-2p_1(x)} \in \mathcal{A}$, extending to $E$ with corank exactly one; the radical is the line of the negative-exponent covector $\sigma^1$, and the dying entry is $-\varrho c_1$: exactly first order in the canonical defining element $\varrho$.
\item The one-sided completion applies verbatim: coupling to the dying direction with $\mu\nu < 0$ yields signature $(2,4)$ on a collar, boundary included, with the ladder pair supported exactly on $E$ and no shadow wall ($s = -1/(\varrho c_1) < 0$ throughout, so $F \geq 1$ wherever the bump is supported); the global coupling $\mu\nu = -\tfrac12$ has $\det h = c_2c_3(1 + \varrho c_1)$, nonvanishing everywhere on the collar.
\item The weights are forced pointwise: within diagonal rescalings $\tau^{a_i(x)}$, the corank-one regime \emph{with the negative-exponent axis dying at first order in $\varrho$} forces $(a_0,\dots,a_3) = (0,0,p_2,p_3)$, and the nondegenerate regime forces $(0,p_1,p_2,p_3)$: the local exponents, at each point separately. (As at Schwarzschild, naming the dying axis is read off the geometry, the negative-exponent covector being the radical of the actual degeneration; without naming it other slot assignments exist.) The exceptional Gram is $\operatorname{diag}(1,-c_1,-c_2,-c_3)|_{\tau=0}$, a smooth bundle of nondegenerate $(1,3)$ forms over $E$: the Clifford algebras of the local Kasner forms.
\end{enumerate}
Consequently the degeneration sheaf, the square-zero ideal with quotient $\Cl(1,2)$, the localised ladder pair, and the exceptional algebra all exist with position-dependent exponents, by the $C^\infty$-linearity of their constructions applied fibrewise.

## technical
For strict diagonal data with position-dependent exponents, let $\shW$ be the $\mathcal{A}$-module with frame $d\tau$, $\sigma^1$, $\tau^{p_2(x)}\sigma^2$, $\tau^{p_3(x)}\sigma^3$. It is free of rank four with Gram $\operatorname{diag}(1, -\varrho c_1, -c_2, -c_3)$, where $\varrho = \tau^{-2p_1(x)} \in \mathcal{A}$, extending to the boundary $E$ with corank exactly one, radical the negative-exponent covector $\sigma^1$, and dying entry exactly first order in $\varrho$. The one-sided completion with $\mu\nu < 0$ gives signature $(2,4)$ on a collar, boundary included, with no shadow wall; for $\mu\nu = -\tfrac12$, $\det h = c_2c_3(1 + \varrho c_1)$ never vanishes on the collar.

Within diagonal rescalings $\tau^{a_i(x)}$, the corank-one regime with the negative-exponent axis dying at first order forces $(a_0,\dots,a_3) = (0,0,p_2,p_3)$, and the nondegenerate regime forces $(0,p_1,p_2,p_3)$, at each point separately. The exceptional Gram $\operatorname{diag}(1,-c_1,-c_2,-c_3)$ at $\tau = 0$ is a smooth bundle of nondegenerate $(1,3)$ forms, so the degeneration sheaf, its square-zero ideal with quotient $\Cl(1,2)$, the ladder pair and the exceptional algebra all exist with position-dependent exponents.

## lay
Near a singularity of the strictly diagonal (Kasner-like) kind, space contracts at different rates along fixed perpendicular directions, and the rates can vary from place to place. This result shows that the repair machinery developed for the black hole still works in that setting. Once the direction that degenerates is read off the geometry, the rescaling needed at each point is not a free choice: it is forced, and it equals the local contraction rates.

## one-liner
For strict diagonal data with varying exponents the weighted module is boundary-tame of corank one, admits a $(2,4)$ completion with no shadow wall, and has its weights forced pointwise to the local exponents.
