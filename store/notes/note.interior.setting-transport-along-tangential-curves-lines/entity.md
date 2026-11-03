---
id: note.interior.setting-transport-along-tangential-curves-lines
kind: note
version: 2
title: Transport along tangential curves, and the $\varphi$-lines
status: setting
subject: interior
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
comments_on:
- interior.transport-level-convergence-along-tangential-curves
- interior.weighted-limit-theorem
- obj.interior.weighted-blow-up-hubble-normalisation-admissible
locators:
  paper: T06
  number: Setting
  section: 'Part three, first half: the approach'
  line: 724
  subsection: Transport along tangential curves, and the $\varphi$-lines
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG sign (Leon 2026-10-23, referee GR1): the model generator H(s) re-signed to -sum_i u^i p_i B_i, the limiting value of the rotation-gauge field in the sign of the definition (DICTIONARY C10); content unchanged. Version 1 -> 2.'
---

## formal
Theorem \claimref{interior.weighted-limit-theorem} proves transport-level convergence along the $t$- and $\theta$-coordinate lines and makes no claim along the $\varphi$-lines, where a divergent boost appears alongside a fixed rotation. This subsection shows that the missing claim concerns coordinate segments, not transport: along every tangential curve of fixed Hubble-normalised length the transport converges to the model's, for every admissible metric, by an elementary bound that needs nothing beyond admissibility; and at Schwarzschild the $\varphi$-lines converge with the explicit rate $\tau^{1/3}$.

Fix on $\mathrm{End}(\R^{6}) \supset \mathfrak{so}(2,4)$ the operator norm induced by the Euclidean norm on $\R^{6}$ in which the adapted tractor frame is orthonormal; it is submultiplicative with $\|1\| = 1$, and each $B_i$ and each rotation $R_{ij}$, whose matrix in that frame has a single pair of entries $\pm 1$ in an off-diagonal $2 \times 2$ block, has $\|B_i\| = \|R_{ij}\| = 1$. A \emph{tangential curve at time $\tau$} is a smooth curve $\gamma$ in the slice $\{\tau\} \times \mathcal{B}$, parametrised by its own Hubble-normalised arclength $s$ (physical arclength divided by $\tau$), with unit tangent $u(s) = \sum_{i} u^{i}(s) e_{i}$, $\sum (u^{i})^{2} = 1$. Its \emph{transport} $T_{\gamma}(\lambda)$ is the solution of $T' = G(s) T$, $T(0) = 1$, on $[0, \lambda]$, with $G(s) = \widehat\Omega_{\tau}(u(s))$ the Hubble-normalised connection of Definition \claimref{obj.interior.weighted-blow-up-hubble-normalisation-admissible} on the unit tangent; its \emph{model transport} $T^{0}_{\gamma}(\lambda)$ solves the same equation with $H(s) = -\sum_{i} u^{i}(s)\, p_{i} B_{i}$, the limiting connection $\widehat\Omega_0$ evaluated on the same unit tangent.

## technical
pending

## lay
pending

## one-liner
pending
