---
id: note.singularity.setting-metric-gauge-field-static-form
kind: note
version: 1
title: The metric of the gauge field, and its static form
status: setting
subject: singularity
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
comments_on:
- singularity.unipotent-ray
locators:
  paper: T05
  number: Setting
  section: 'The Schwarzschild curvature and the surface gravity: the metric-picture cross-check'
  line: 2525
  subsection: The metric of the gauge field, and its static form
---

## formal
The metric is $g(a,b) = \hb^{-1}(a) \cdot \hb^{-1}(b)$ with $\hb^{-1} = 1 + \beta P$ (Proposition \claimref{singularity.unipotent-ray}). On the $(t,r)$ frame vectors:
\[
g(\et, \et) = (\et + \beta\er)^2 = 1 - \beta^2, \qquad
g(\et, \er) = (\et + \beta\er)\cdot\er = -\beta, \qquad
g(\er, \er) = \er^2 = -1 ,
\]
and the angular directions are untouched. This is the Painlev\'e-Gullstrand line element
\[
ds^2 = \Bigl(1 - \tfrac{2M}{r}\Bigr)\,dt^2 - 2\beta\,dt\,dr - dr^2 - r^2 d\Omega^2 , \qquad \beta^2 = \tfrac{2M}{r} .
\]
Substituting $dt = dt_s + (\beta/f)\,dr$ with $f := 1 - 2M/r = 1 - \beta^2$ eliminates the cross term exactly:
\[
f\,dt^2 - 2\beta\,dt\,dr - dr^2
\;=\; f\,dt_s^2 + 2\beta\,dt_s dr + \tfrac{\beta^2}{f}dr^2 - 2\beta\,dt_s dr - \tfrac{2\beta^2}{f}dr^2 - dr^2
\;=\; f\,dt_s^2 - \tfrac{\beta^2 + f}{f}\,dr^2
\;=\; f\,dt_s^2 - \tfrac{dr^2}{f} ,
\]
since $\beta^2 + f = 1$: the static Schwarzschild form, with the same areal radius $r$. Curvature is a pointwise invariant, so it may be computed in the static chart.

## technical
pending

## lay
pending

## one-liner
pending
