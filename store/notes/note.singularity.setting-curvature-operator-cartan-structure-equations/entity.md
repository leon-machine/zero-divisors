---
id: note.singularity.setting-curvature-operator-cartan-structure-equations
kind: note
version: 1
title: The curvature operator, by the Cartan structure equations
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
- singularity.solution-where-divergence-lies
- singularity.curvature-gauge-field-exact-shape-decoupling
locators:
  paper: T05
  number: Setting
  section: 'The Schwarzschild curvature and the surface gravity: the metric-picture cross-check'
  line: 2546
  subsection: The curvature operator, by the Cartan structure equations
---

## formal
Take the orthonormal coframe $\theta^{\hat 0} = \sqrt f\,dt_s$, $\theta^{\hat 1} = dr/\sqrt f$, $\theta^{\hat 2} = r\,d\vartheta$, $\theta^{\hat 3} = r\sin\vartheta\,d\varphi$. The first structure equations $d\theta^{\hat a} = -\,\omega^{\hat a}{}_{\hat b} \wedge \theta^{\hat b}$ are solved by
\[
\omega^{\hat 0}{}_{\hat 1} = \tfrac{f'}{2\sqrt f}\,\theta^{\hat 0}, \qquad
\omega^{\hat 2}{}_{\hat 1} = \tfrac{\sqrt f}{r}\,\theta^{\hat 2}, \qquad
\omega^{\hat 3}{}_{\hat 1} = \tfrac{\sqrt f}{r}\,\theta^{\hat 3}, \qquad
\omega^{\hat 3}{}_{\hat 2} = \tfrac{\cot\vartheta}{r}\,\theta^{\hat 3},
\]
all other independent components zero; each is verified by substitution (for instance $d\theta^{\hat 0} = \tfrac{f'}{2\sqrt f}\,dr \wedge dt_s = \tfrac{f'}{2\sqrt f}\,\theta^{\hat 1}\wedge\theta^{\hat 0}$, matched by $-\,\omega^{\hat 0}{}_{\hat 1}\wedge\theta^{\hat 1}$). The second structure equations $R^{\hat a}{}_{\hat b} = d\omega^{\hat a}{}_{\hat b} + \omega^{\hat a}{}_{\hat c}\wedge\omega^{\hat c}{}_{\hat b}$ then give, writing each curvature two-form on its own plane:
\[
R^{\hat 0}{}_{\hat 1} = -\tfrac{f''}{2}\,\theta^{\hat 0}\wedge\theta^{\hat 1}, \qquad
R^{\hat 0}{}_{\hat 2} = -\tfrac{f'}{2r}\,\theta^{\hat 0}\wedge\theta^{\hat 2}, \qquad
R^{\hat 1}{}_{\hat 2} = -\tfrac{f'}{2r}\,\theta^{\hat 1}\wedge\theta^{\hat 2},
\]
with $R^{\hat 0}{}_{\hat 3}, R^{\hat 1}{}_{\hat 3}$ mirroring the $\hat 2$ entries, and
\[
R^{\hat 2}{}_{\hat 3} = \tfrac{1 - f}{r^2}\,\theta^{\hat 2}\wedge\theta^{\hat 3} .
\]
As a sample of the derivations: $R^{\hat 0}{}_{\hat 1} = d\omega^{\hat 0}{}_{\hat 1} = \bigl(\sqrt f\,(\tfrac{f'}{2\sqrt f})' + \tfrac{f'^2}{4f}\bigr)\theta^{\hat 1}\wedge\theta^{\hat 0} = \tfrac{f''}{2}\,\theta^{\hat 1}\wedge\theta^{\hat 0}$, the $f'^2$ terms cancelling; $R^{\hat 1}{}_{\hat 2} = d(-\sqrt f\,d\vartheta) = -\tfrac{f'}{2\sqrt f}dr\wedge d\vartheta = -\tfrac{f'}{2r}\theta^{\hat 1}\wedge\theta^{\hat 2}$; and $R^{\hat 2}{}_{\hat 3} = d(-\cos\vartheta\,d\varphi) + \omega^{\hat 2}{}_{\hat 1}\wedge\omega^{\hat 1}{}_{\hat 3} = \tfrac{1}{r^2}\theta^{\hat 2}\wedge\theta^{\hat 3} - \tfrac{f}{r^2}\theta^{\hat 2}\wedge\theta^{\hat 3}$. The curvature operator on the six-dimensional bivector space is therefore diagonal in the coordinate planes, with eigenvalues proportional to
\[
-\tfrac{f''}{2} \ \ (\text{radial boost plane } \hat 0\hat 1), \qquad
-\tfrac{f'}{2r} \ \ (\text{the four mixed planes}), \qquad
\tfrac{1-f}{r^2} \ \ (\text{angular plane } \hat 2\hat 3).
\]
For $f = 1 - 2M/r$: $f' = 2M/r^2$, $f'' = -4M/r^3$, so the three values are
\[
\tfrac{2M}{r^3}, \qquad -\tfrac{M}{r^3}, \qquad \tfrac{2M}{r^3} :
\]
the doubled-magnitude eigenvalue $2M/r^3$ is attained exactly on the radial plane $\hat 0\hat 1$ and its Hodge dual $\hat 2\hat 3$, at every radius, with the four mixed planes at half the magnitude. The extreme eigenvalue therefore distinguishes the pair $\{\sigma_r, I\sigma_r\}$ invariantly (the dual written $I\sigma_r$ here as in the body), in agreement with the gauge-sector value of Proposition \claimref{singularity.solution-where-divergence-lies}(1) on the radial plane, and the shape these eigenvalues assemble into is Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling}'s $S = 1 - 3\Pi$, with $\mathcal{R} = -(M/r^{3})S$ in this convention exactly as in the gauge-sector computation (only the ratio $2 : 1$ and the identity of the distinguished plane are used in the chain).

## technical
pending

## lay
pending

## one-liner
pending
