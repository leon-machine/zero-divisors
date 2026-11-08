---
id: transport.splitting-along-hyperbolic-plane
kind: claim
version: 3
title: Splitting along a hyperbolic plane
status: proved
region: transport
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
review: typed
derivations:
- name: main
  uses:
  - primer.splitting-along-hyperbolic-plane@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_hyperbolic_pair_and_unique_expansion
- kind: check
  ref: check.py::check_left_multiplication_by_v_injective_on_cl_u
locators:
  paper: T01
  number: Lem 2.4
  label: lem:split
  line: 505
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: for nine forms U'' (degenerate included) and two hyperbolic pairs, {1, v, w0, v w0} x blades(U'') is a basis with an exact unique expansion, and v x is injective on Cl(U'') with half rank on Cl(V''). Version 2 -> 3.'
  env: lemma
  repair:
    note: restatement of the T0 result primer.splitting-along-hyperbolic-plane; derivation and proof text
      supplied by the store
  typing:
    by: ai-typing-pass
    note: 'Edge kept: restatement of the primer lemma, as the store''s repair records.'
subject: zero-divisors
tags: [hyperbolic-plane]
equivalent_to:
- primer.splitting-along-hyperbolic-plane@3
---

## formal
Let $\mathbb{V}' = H_0 \perp U'$ be an orthogonal decomposition with $H_0$ a hyperbolic plane spanned by a hyperbolic pair $(v, w_0)$; the form on $U'$ may be degenerate. Then:
\begin{enumerate}
\item $\{1, v, w_0, v w_0\}$ is a linear basis of $\Cl(H_0)$, and every element of $\Cl(\mathbb{V}')$ admits a \emph{unique} expansion
\[
\sigma \;=\; \alpha + v\beta + w_0\gamma + v w_0\,\delta, \qquad \alpha, \beta, \gamma, \delta \in \Cl(U').
\]
\item Left multiplication by $v$ is injective on $\Cl(U')$.
\end{enumerate}

## technical
Let $\mathbb{V}' = H_0 \perp U'$ with $H_0$ the hyperbolic plane spanned by a hyperbolic pair $(v, w_0)$, the form on $U'$ possibly degenerate. Then $\{1, v, w_0, v w_0\}$ is a linear basis of $\Cl(H_0)$, and every element of $\Cl(\mathbb{V}')$ has a unique expansion $\sigma = \alpha + v\beta + w_0\gamma + v w_0\,\delta$ with $\alpha, \beta, \gamma, \delta \in \Cl(U')$. Moreover, left multiplication by $v$ is injective on $\Cl(U')$.

## lay
When a space contains a light-like direction paired with a partner, the algebra of the whole space splits into four slots built from that pair, each filled by an element of the algebra of the remaining directions. The split is unique, which makes it a reliable bookkeeping device. Multiplying by the light-like direction never sends a nonzero element of the remaining algebra to zero.

## one-liner
Along a hyperbolic plane spanned by $(v, w_0)$, every element of $\Cl(H_0 \perp U')$ expands uniquely as $\alpha + v\beta + w_0\gamma + v w_0\delta$ with coefficients in $\Cl(U')$, and left multiplication by $v$ is injective on $\Cl(U')$.
