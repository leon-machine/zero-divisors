---
id: primer.splitting-along-hyperbolic-plane
kind: claim
version: 3
title: Splitting along a hyperbolic plane
status: proved
region: primer
programme: standard
subject: standard-algebra
tags: [hyperbolic-plane]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T00, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, foundation layer'
  version: 3
  source: run 2026-11-08-foundation-layer
review: typed
founded_on:
- synthesis.continuum-completion-premise@2
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T00.py
  tags:
  - num:9.6
- kind: check
  ref: check.py::check_hyperbolic_pair_and_plane_basis
- kind: check
  ref: check.py::check_unique_split_expansion
- kind: check
  ref: check.py::check_left_mult_by_v_injective
locators:
  paper: T00
  number: Lem 9.6
  label: tk:split
  line: 516
extraction:
  maintainer_pass_2026_11_08_foundation:
    by: ai-maintainer-pass
    note: >-
      Version 2 -> 3. Leon's decision of 8 November 2026: the foundation layer. Founded on synthesis.continuum-completion-premise: the algebra it is stated in rests on the foundation. Foundation postulates are reported as what a result rests on, separately from the premises it holds given (store/conventions.md, "The foundation").
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: unique expansion over {1, v, w0, v w0} x Cl(U'') and injectivity of v on Cl(U''), for nine forms U'' including degenerate ones and two hyperbolic pairs. Version 1 -> 2.'
  env: lemma
  unresolved_refs:
  - ex:hyperbolic
  typing:
    by: ai-typing-pass
    note: 'No edges: the blade count the proof uses is primer section prose citing Chevalley, not a store
      claim.'
---

## formal
Let $\mathbb{V}' = H_0 \perp U'$ be an orthogonal decomposition of a real quadratic space, with $H_0$ a hyperbolic plane spanned by a hyperbolic pair $(v, w_0)$ (a pair of null vectors with $v w_0 + w_0 v = 1$, Example \ref{ex:hyperbolic}); the form on $U'$ may be degenerate. Then:
\begin{enumerate}
\item $\{1, v, w_0, v w_0\}$ is a linear basis of $\Cl(H_0)$, and every element of $\Cl(\mathbb{V}')$ admits a \emph{unique} expansion
\[
\sigma \;=\; \alpha + v\beta + w_0\gamma + v w_0\,\delta, \qquad \alpha, \beta, \gamma, \delta \in \Cl(U').
\]
\item Left multiplication by $v$ is injective on $\Cl(U')$.
\end{enumerate}

## technical
Let $\mathbb{V}' = H_0 \perp U'$, with $H_0$ a hyperbolic plane spanned by null vectors $v, w_0$ satisfying $v w_0 + w_0 v = 1$, and $U'$ carrying a possibly degenerate form. Then $\{1, v, w_0, v w_0\}$ is a basis of $\Cl(H_0)$, and every $\sigma \in \Cl(\mathbb{V}')$ has a unique expansion $\sigma = \alpha + v\beta + w_0\gamma + v w_0\,\delta$ with $\alpha, \beta, \gamma, \delta \in \Cl(U')$; this is the graded tensor decomposition $\Cl(H_0 \perp U') \cong \Cl(H_0)\,\hat{\otimes}\,\Cl(U')$ in coordinates.

By uniqueness, left multiplication by $v$ is injective on $\Cl(U')$.

## lay
Suppose a geometry contains a special plane spanned by two zero-length directions. Then every element of its Clifford algebra can be written in exactly one way as four pieces, each a coefficient from the rest of the geometry multiplied by one of four simple elements of the plane. A consequence is that multiplying by one of the zero-length directions never destroys information carried by the rest of the geometry.

## one-liner
Along a hyperbolic plane spanned by a null pair $(v, w_0)$, every element of $\Cl(H_0 \perp U')$ expands uniquely as $\alpha + v\beta + w_0\gamma + v w_0\delta$ with coefficients in $\Cl(U')$, and left multiplication by $v$ is injective on $\Cl(U')$.
