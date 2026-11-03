---
id: neutrino.breaking-relation
kind: claim
version: 3
title: The breaking relation
status: proved
region: neutrino
subject: neutrinos
tags: [seesaw-and-majorana, flavour-and-mixing]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T15, deposited version
review: typed
derivations:
- name: main
  uses:
  - neutrino.invariant-symmetric-matrices@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T15.py
  tags:
  - label:lem:breaking
- kind: check
  ref: check.py::check_exact_identity_and_majorana_only_breaking
- kind: check
  ref: check.py::check_reference_direction_scale
- kind: check
  ref: check.py::check_leading_order_compression_eigenvalues
- kind: check
  ref: check.py::check_instances_diagonalised_exactly
locators:
  paper: T15
  number: Lem 4.6
  label: lem:breaking
  line: 655
extraction:
  env: lemma
  unresolved_refs:
  - rem:branch
  typing:
    by: ai-typing-pass
    note: 'edges unchanged: the one premise is the invariant-matrix lemma, used for the inverse of the
      Majorana matrix. Levels pass: the lay level now keeps the leading-order qualifier on the $\delta^{2}$
      scaling.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the exact identity for three directions and four delta, Majorana-only breaking rank one, lambda_A = 4/9 at e_3 e_3^T, leading order via the compression for generic A, and the exact m_2/m_3 instances. Version 1 -> 2. Check strengthened: compression trace and 2-minor sum pinned by hand; instance ratios pinned to six or seven figures; samples moved to module level. Version 2 -> 3.'
---

## formal
Let $\mD = d(\J + \delta A)$ with $A$ a real $3 \times 3$ matrix (its scale is fixed by the reference direction $e_{3}e_{3}^{\mathsf{T}}$, the $S_{3} \to S_{2}$ direction, for which $\|\Pi A\Pi\| = \tfrac23$ in the operator norm and $\lambda_{A} = \tfrac49$ below; $\delta$ is quoted relative to that direction, as the instances state, and $\delta^{2}\lambda_{A}$ is invariant under a rescaling of $A$), $\delta$ a real breaking parameter, and $M_{R} = \alpha\Pi + M_{3}\J/3$ with $\alpha, M_{3} \neq 0$. Then, exactly,
\[
\mD M_{R}^{-1}\mD^{\mathsf{T}} \;=\; \frac{d^{2}\delta^{2}}{\alpha}\,A\,\Pi\,A^{\mathsf{T}} \;+\; \frac{d^{2}}{3M_{3}}\,q\,q^{\mathsf{T}}, \qquad q = (\J + \delta A)\,u' = 3u' + \delta A u' .
\]
Consequently the second and third light masses are, to leading order in $\delta$, $(d^{2}\delta^{2}/\alpha)$ times the two eigenvalues $\lambda_{A} \ge \lambda'_{A}$ of the compression $\Pi A\Pi A^{\mathsf{T}}\Pi$ of the first term to $u'^{\perp}$ (not of $A\Pi A^{\mathsf{T}}$ itself, whose range is not orthogonal to $u'$), so $m_{1}/m_{2} = \lambda'_{A}/\lambda_{A}$ at this order, and
\[
\frac{m_{2}}{m_{3}} \;=\; \frac{\delta^{2}\lambda_{A}}{9}\,\frac{M_{3}}{\alpha}\,\Bigl(1 + O(\delta) + O\bigl(\delta^{2}M_{3}/\alpha\bigr)\Bigr):
\]
no breaking of the Majorana sector alone lifts $m_{2}$ (since $\J X \J = (\textstyle\sum_{ij}X_{ij})\J$ for every $X$), the Dirac breaking enters squared, and the seesaw enhances it by $M_{3}/\alpha$. The second remainder is $O(m_{2}/m_{3})$, a function of the answer itself, and does not vanish as $\delta \to 0$ at fixed physical ratio; at the sizes of interest the two together are not small (the formula overestimates the exact ratio by more than a half at the instance of Remark \ref{rem:branch}), so the instances are diagonalised exactly rather than read from the formula.

## technical
Take a Dirac matrix $\mD = d(\J + \delta A)$, the all-ones matrix $\J$ broken in a real direction $A$ with parameter $\delta$, and an $S_{3}$-invariant Majorana matrix $M_{R} = \alpha\Pi + M_{3}\J/3$ with $\alpha, M_{3} \neq 0$, where $\Pi$ projects onto the plane orthogonal to $u' = (1,1,1)$. Then exactly $\mD M_{R}^{-1}\mD^{\mathsf{T}} = \frac{d^{2}\delta^{2}}{\alpha}A\Pi A^{\mathsf{T}} + \frac{d^{2}}{3M_{3}}qq^{\mathsf{T}}$ with $q = 3u' + \delta A u'$.

To leading order in $\delta$ the two lighter masses are $d^{2}\delta^{2}/\alpha$ times the eigenvalues $\lambda_{A} \ge \lambda'_{A}$ of the compression $\Pi A\Pi A^{\mathsf{T}}\Pi$, so $m_{1}/m_{2} = \lambda'_{A}/\lambda_{A}$ and $\frac{m_{2}}{m_{3}} = \frac{\delta^{2}\lambda_{A}}{9}\frac{M_{3}}{\alpha}\bigl(1 + O(\delta) + O(\delta^{2}M_{3}/\alpha)\bigr)$. Breaking the Majorana sector alone cannot lift $m_{2}$, since $\J X\J = (\sum_{ij}X_{ij})\J$ for every $X$; the Dirac breaking enters squared and the seesaw enhances it by $M_{3}/\alpha$. The second remainder is of the size of $m_{2}/m_{3}$ itself, so at the sizes of interest the formula is not accurate and instances are diagonalised exactly.

## lay
At first approximation the framework gives only one light neutrino a mass. This result shows how a small distortion of the neutrino's coupling pattern gives mass to a second one: to leading order the effect grows as the square of the distortion and is amplified by the ratio of two heavy mass scales. Distorting only the heavy neutrinos' masses would not do it. At realistic sizes the approximate formula is only a guide, so the paper computes the masses exactly.

## one-liner
A Dirac breaking of size $\delta$ lifts the second light neutrino mass at order $\delta^{2}M_{3}/\alpha$, while a breaking of the Majorana sector alone lifts nothing.
