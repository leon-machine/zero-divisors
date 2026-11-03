---
id: note.mass.setting-grip-composite-frozen-point
kind: note
version: 1
title: The grip of a composite on the frozen point
status: setting
subject: mass
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
comments_on:
- mass.grip-real
- mass.imported-flat-model-twistor-chart-infinity
locators:
  paper: T11
  number: Setting
  section: The exact join
  line: 657
  subsection: The grip of a composite on the frozen point
---

## formal
The classical phase space of $N$ twistors carries the Hermitian form $\Sigma$ of signature $(2,2)$, written $\bar{Z}\cdot W := \Sigma(Z, W)$, and the conformal group acts by $SU(2,2)$. The form is canonical up to a phase and has signature $(2,2)$ \cite[Prop.~4.5(1), (2), (4)]{ButlerT9}; the chart frame fixes the phase, and in it $\Sigma$ is the standard twistor form $\bar{Z}\cdot Z = \omega^{A}\bar\pi_{A} + \bar\omega^{A'}\pi_{A'}$ \cite{PenroseRindler1986}, which pairs $\omega$ with $\bar\pi$ through the frame: for $Z = (\omega, \pi)$ and $W = (\xi, \chi)$,
\begin{equation}
\bar{Z}\cdot W = \hp{\pi}{\xi} + \overline{\hp{\chi}{\omega}}, \qquad \hp{u}{v} := \overline{u^{3}}\,v^{1} + \overline{u^{4}}\,v^{2}\quad (u \in \Sc',\ v \in \Sc),
\end{equation}
the sesquilinear pairing that identifies the frame $e_{3}, e_{4}$ of $\Sc'$ with the frame $e_{1}, e_{2}$ of $\Sc$; we write $\bar{u}_{a}$ for the conjugate of the component of $u \in \Sc'$ so identified with $e_{a}$, so that $\hp{u}{v} = \bar{u}_{a}v^{a}$. The real slice \eqref{eq:realslice} is the one this form determines. The moment map of the action on the phase space is the classical form of the generators of Fact \claimref{mass.imported-flat-model-twistor-chart-infinity}:
\begin{equation}
M_{A}(Z^{1}, \dots, Z^{N}) := i\sum_{i=1}^{N} \bar{Z}^{i}\cdot(A Z^{i}), \qquad A \in \mathfrak{sl}(\T),
\end{equation}
real for $A \in \mathfrak{su}(2,2)$, and $M_{U\wedge V} := M_{A(U\wedge V)}$ for ambient $U, V$. Equivariance is built in: for $\gamma \in SU(2,2)$, $M_{A}(\gamma Z) = M_{\gamma^{-1}A\gamma}(Z)$, and $A(\gamma U \wedge \gamma V) = \gamma\,A(U\wedge V)\,\gamma^{-1}$ because the isomorphism of Fact \claimref{mass.imported-flat-model-twistor-chart-infinity} intertwines the two actions.

## technical
pending

## lay
pending

## one-liner
pending
