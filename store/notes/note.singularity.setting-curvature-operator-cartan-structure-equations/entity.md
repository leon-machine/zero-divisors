---
id: note.singularity.setting-curvature-operator-cartan-structure-equations
kind: note
version: 2
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
- name: Claude Opus 5.5
  role: GA rewrite (static Schwarzschild connection and curvature operator in GTG, Cartan computation as labelled reading)
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
comments_on:
- singularity.solution-where-divergence-lies
- singularity.curvature-gauge-field-exact-shape-decoupling
locators:
  paper: T05
  number: Setting
  section: 'The Schwarzschild curvature and the surface gravity: the metric-picture cross-check'
  line: 2546
  subsection: The curvature operator, by the Cartan structure equations
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Forms to GA: the setting now states the static gauge field (hb^{-1}(e_t) = sqrt(f) gamma_0, hb^{-1}(e_r) = gamma_1/sqrt(f), ...), its rotation-gauge field on the physical frame as the solution of the torsion equation hb^T(grad ^ f^a) = sum_b gamma^b ^ (omega(gamma_b) . gamma^a), and the store-sign curvature operator on the frame planes; the papers Cartan structure-equation computation (coframe, connection forms, curvature two-forms and the sample derivations) is kept as a labelled component reading. Checked exactly with lib/gtg.py in the maintainer scratch from second-order jets of hb at two points with rational sqrt(f) (Schwarzschild M = 1 at r = 8/3, and a non-vacuum f): Omega solved from the torsion condition equals the displayed bivectors, satisfies the GA structure equation, and the store-sign calR on the six frame planes is exactly -f''/2, -f''/2r, (1 - f)/r^2 for general f (so the eigenvalues are these values, not only proportional to them). Title kept (the papers subsection name).'
---

## formal
Take the static gravitational field on flat spacetime with $\hb^{-1}(e_{t}) = \sqrt f\,\gamma_0$, $\hb^{-1}(e_{r}) = \gamma_1/\sqrt f$, $\hb^{-1}(e_{\vartheta}) = r\,\gamma_2$, $\hb^{-1}(e_{\varphi}) = r\sin\vartheta\,\gamma_3$ on the background frame of the labels $(t_s, r, \vartheta, \varphi)$, so that the reciprocal physical frame is $\gamma^a = \hb^{T}(f^a)$ with $f^0 = \sqrt f\,\nabla t_s$, $f^1 = \nabla r/\sqrt f$, $f^2 = r\nabla\vartheta$, $f^3 = r\sin\vartheta\,\nabla\varphi$ (in components, the orthonormal coframe $\theta^{\hat 0} = \sqrt f\,dt_s$, $\theta^{\hat 1} = dr/\sqrt f$, $\theta^{\hat 2} = r\,d\vartheta$, $\theta^{\hat 3} = r\sin\vartheta\,d\varphi$). With $\omega(\gamma_b) := \Omega(\hb(\gamma_b))$, the torsion equation $\hb^{T}(\nabla\wedge f^a) = \sum_b \gamma^b\wedge\bigl(\omega(\gamma_b)\cdot\gamma^a\bigr)$ is solved by
\[
\omega(\gamma_0) = -\tfrac{f'}{2\sqrt f}\,\gamma_0\wedge\gamma_1, \qquad
\omega(\gamma_1) = 0, \qquad
\omega(\gamma_2) = \tfrac{\sqrt f}{r}\,\gamma_1\wedge\gamma_2, \qquad
\omega(\gamma_3) = \tfrac{\sqrt f}{r}\,\gamma_1\wedge\gamma_3 + \tfrac{\cot\vartheta}{r}\,\gamma_2\wedge\gamma_3 ,
\]
each verified by substitution (for instance $\nabla\wedge f^0 = \tfrac{f'}{2\sqrt f}\,\nabla r\wedge\nabla t_s$, whose image under the outermorphism $\hb^{T}$ is $\tfrac{f'}{2\sqrt f}\,\gamma^1\wedge\gamma^0$, matched by $\gamma^0\wedge(\omega(\gamma_0)\cdot\gamma^0) = \tfrac{f'}{2\sqrt f}\,\gamma^0\wedge\gamma_1$). The field strength $R(a\wedge b) = a\cdot\nabla\Omega(b) - b\cdot\nabla\Omega(a) + \Omega(a)\times\Omega(b)$ then gives, in the store's sign $\mathcal{R}(B) = -R(\hb(B))$, an operator diagonal on the frame planes:
\[
\mathcal{R}(\gamma_0\wedge\gamma_1) = -\tfrac{f''}{2}\,\gamma_0\wedge\gamma_1, \qquad
\mathcal{R}(\gamma_0\wedge\gamma_2) = -\tfrac{f'}{2r}\,\gamma_0\wedge\gamma_2, \qquad
\mathcal{R}(\gamma_1\wedge\gamma_2) = -\tfrac{f'}{2r}\,\gamma_1\wedge\gamma_2,
\]
with $\gamma_0\wedge\gamma_3$, $\gamma_1\wedge\gamma_3$ mirroring the $\gamma_2$ entries, and
\[
\mathcal{R}(\gamma_2\wedge\gamma_3) = \tfrac{1 - f}{r^2}\,\gamma_2\wedge\gamma_3 .
\]
(In components, a labelled reading, the paper's metric-picture computation by the Cartan structure equations: the first structure equations $d\theta^{\hat a} = -\,\omega^{\hat a}{}_{\hat b} \wedge \theta^{\hat b}$ are solved by $\omega^{\hat 0}{}_{\hat 1} = \tfrac{f'}{2\sqrt f}\,\theta^{\hat 0}$, $\omega^{\hat 2}{}_{\hat 1} = \tfrac{\sqrt f}{r}\,\theta^{\hat 2}$, $\omega^{\hat 3}{}_{\hat 1} = \tfrac{\sqrt f}{r}\,\theta^{\hat 3}$, $\omega^{\hat 3}{}_{\hat 2} = \tfrac{\cot\vartheta}{r}\,\theta^{\hat 3}$, all other independent components zero, and the second structure equations $R^{\hat a}{}_{\hat b} = d\omega^{\hat a}{}_{\hat b} + \omega^{\hat a}{}_{\hat c}\wedge\omega^{\hat c}{}_{\hat b}$ give the curvature two-forms $R^{\hat 0}{}_{\hat 1} = -\tfrac{f''}{2}\,\theta^{\hat 0}\wedge\theta^{\hat 1}$, $R^{\hat 0}{}_{\hat 2} = -\tfrac{f'}{2r}\,\theta^{\hat 0}\wedge\theta^{\hat 2}$, $R^{\hat 1}{}_{\hat 2} = -\tfrac{f'}{2r}\,\theta^{\hat 1}\wedge\theta^{\hat 2}$, $R^{\hat 2}{}_{\hat 3} = \tfrac{1 - f}{r^2}\,\theta^{\hat 2}\wedge\theta^{\hat 3}$; as samples, $R^{\hat 0}{}_{\hat 1} = d\omega^{\hat 0}{}_{\hat 1} = \bigl(\sqrt f\,(\tfrac{f'}{2\sqrt f})' + \tfrac{f'^2}{4f}\bigr)\theta^{\hat 1}\wedge\theta^{\hat 0} = \tfrac{f''}{2}\,\theta^{\hat 1}\wedge\theta^{\hat 0}$, the $f'^2$ terms cancelling, $R^{\hat 1}{}_{\hat 2} = d(-\sqrt f\,d\vartheta) = -\tfrac{f'}{2r}\theta^{\hat 1}\wedge\theta^{\hat 2}$, and $R^{\hat 2}{}_{\hat 3} = d(-\cos\vartheta\,d\varphi) + \omega^{\hat 2}{}_{\hat 1}\wedge\omega^{\hat 1}{}_{\hat 3} = \tfrac{1 - f}{r^2}\theta^{\hat 2}\wedge\theta^{\hat 3}$.) The curvature operator on the six-dimensional bivector space is therefore diagonal in the coordinate planes, with eigenvalues
\[
-\tfrac{f''}{2} \ \ (\text{radial boost plane } \gamma_0\wedge\gamma_1), \qquad
-\tfrac{f'}{2r} \ \ (\text{the four mixed planes}), \qquad
\tfrac{1-f}{r^2} \ \ (\text{angular plane } \gamma_2\wedge\gamma_3).
\]
For $f = 1 - 2M/r$: $f' = 2M/r^2$, $f'' = -4M/r^3$, so the three values are
\[
\tfrac{2M}{r^3}, \qquad -\tfrac{M}{r^3}, \qquad \tfrac{2M}{r^3} :
\]
the doubled-magnitude eigenvalue $2M/r^3$ is attained exactly on the radial plane and on its dual, the angular plane, at every radius, with the four mixed planes at half the magnitude. The extreme eigenvalue therefore distinguishes the pair $\{\sigma_r, I\sigma_r\}$ invariantly ($I$ the pseudoscalar, as in the body), in agreement with the gauge-sector value of Proposition \claimref{singularity.solution-where-divergence-lies}(1) on the radial plane, and the shape these eigenvalues assemble into is Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling}'s $S = 1 - 3\Pi$, with $\mathcal{R} = -(M/r^{3})S$ in this convention exactly as in the gauge-sector computation (only the ratio $2 : 1$ and the identity of the distinguished plane are used in the chain).
## technical
pending

## lay
pending

## one-liner
pending
