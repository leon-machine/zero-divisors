---
id: singularity.degeneration-exactly
kind: claim
version: 2
title: The degeneration, exactly
status: proved
region: singularity
subject: singularity
tags: [schwarzschild, degenerate-algebras, null-directions]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:2.6
- kind: check
  ref: check.py::check_rescaled_map_limit_rank_one
- kind: check
  ref: check.py::check_rescaled_metric_limit_form
- kind: check
  ref: check.py::check_folded_direction_is_null_for_limit_form_only
locators:
  paper: T05
  number: Prop 2.6
  label: prop:limit
  line: 1419
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: beta^{-1} hb = beta^{-1} - P over Q(beta) with rank-one limit, the rescaled metric identity, the limit form of signature (0,1,3) and its radical, and e_r null only in the limit. Version 1 -> 2.'
  env: proposition
  context_refs:
  - singularity.cones-fold
  eqrefs: 1
  typing:
    by: ai-typing-pass
    note: 'the reference to the cone-folding proposition only names the direction e_r; the proof does not rely on that result, so it was not added (it also depends on this claim)'
---

## formal
As $r \to 0$, exactly and with every identity holding at finite $\beta$:
\begin{enumerate}
\item (The map.) $\beta^{-1}\hb = \beta^{-1}\,\mathrm{id} - P$, so $\beta^{-1}\hb \to -P$: a rank-one map with image $\R\,\er$ and kernel $\et^{\perp} = \operatorname{span}(\er, e_\vartheta, e_\varphi)$.
\item (The metric.) $\beta^{-2} g(a,b) = -(a\cdot\et)(b\cdot\et) + \beta^{-1}\bigl[(a\cdot\et)(b\cdot\er) + (b\cdot\et)(a\cdot\er)\bigr] + \beta^{-2}(a \cdot b)$, so $\beta^{-2}g \to \hat g$ with
\[
\hat g(a,b) \;=\; -(a\cdot\et)(b\cdot\et) :
\]
a form of rank one and signature $(0,1,3)$, whose radical is $\et^{\perp}$, the kernel of the limit map.
\item (The null direction, located.) The folded direction $\er$ of Proposition \claimref{singularity.cones-fold} lies in the radical of $\hat g$ and is $\hat g$-null, while $g(\er,\er) = -1$ at every finite radius: the nullity of the degenerate direction is a property of the limit form, not of the flat background, and this is the exact content of the phrase ``degeneration through a null kernel direction''. It is the datum Step 2 uses.
\end{enumerate}

## technical
As $r \to 0$ the gauge map and metric have exact rescaled limits, with every identity holding at finite $\beta$. The map satisfies $\beta^{-1}\hb = \beta^{-1}\id - P \to -P$, a rank-one map with image $\R\,\er$ and kernel $\et^{\perp} = \operatorname{span}(\er, e_\vartheta, e_\varphi)$. The metric satisfies $\beta^{-2} g \to \hat g$ with $\hat g(a,b) = -(a\cdot\et)(b\cdot\et)$, a form of rank one and signature $(0,1,3)$ whose radical is $\et^{\perp}$, the kernel of the limit map.

The folded direction $\er$ lies in this radical and is $\hat g$-null, whereas $g(\er,\er) = -1$ at every finite radius. The nullity of the degenerate direction is therefore a property of the limit form, not of the flat background, which is the exact content of degeneration through a null kernel direction.

## lay
Approaching the centre of a black hole the gravitational field grows without bound, but once that overall growth is divided out the field settles to a definite limit. The limit is degenerate: it registers only the time direction and is blind to the other three. The radial direction, along which the light cones fold, becomes one of these blind directions only in the limit, not at any finite distance from the centre.

## one-liner
As $r \to 0$ the rescaled gauge map and metric converge exactly to rank-one limits whose common kernel $\et^{\perp}$ contains the folded direction $\er$, null for the limit form.
